#!/usr/bin/env node
/**
 * git-freshness — a SessionStart hook that stops a session from silently
 * working against a stale checkout.
 *
 * THE PROBLEM IT SOLVES. When work is pushed from git worktrees, or by other
 * people, or by other agent sessions, the checkout you are sitting in never
 * advances on its own. `git status` still says "clean", because nothing is
 * wrong with your *working tree* — it is the commit under it that is old. So
 * there is no signal at all, and an agent reads month-old files believing they
 * are current. One repo was found thirty-five commits behind this way.
 *
 * WHAT IT DOES. On session start it fetches, and then:
 *   - up to date            -> says nothing, so it is not noise
 *   - behind, safe to move  -> fast-forwards and tells you it did
 *   - behind, work in the way -> refuses to move, names the gap and the files
 *   - ahead / diverged      -> warns about unpushed commits, moves nothing
 *
 * It only ever runs `git fetch` and `git merge --ff-only`. A fast-forward
 * cannot rewrite history and git itself refuses one that would clobber local
 * modifications, so the failure mode is "nothing happened", never lost work.
 *
 * WHY ONLY THE DEFAULT BRANCH. On a feature branch, being behind the default
 * branch is normal and updating would be wrong. This stays quiet there.
 *
 * PORTABLE. Nothing here is specific to any project: no repo name, no branch
 * name, no paths. Copy this file to <project>/.claude/hooks/ and add the
 * SessionStart entry shown at the bottom of this comment to the project's
 * .claude/settings.json.
 *
 *   "hooks": {
 *     "SessionStart": [
 *       {
 *         "hooks": [
 *           {
 *             "type": "command",
 *             "command": "node \"$CLAUDE_PROJECT_DIR/.claude/hooks/git-freshness.mjs\"",
 *             "timeout": 30,
 *             "statusMessage": "Checking the checkout is current"
 *           }
 *         ]
 *       }
 *     ]
 *   }
 *
 * It must never break a session, so every failure path exits 0 quietly.
 */

import { spawnSync } from 'node:child_process'

/* Where the project is. CLAUDE_PROJECT_DIR is set by the harness; fall back to
   cwd so the script is also runnable by hand for testing. */
const CWD = process.env.CLAUDE_PROJECT_DIR || process.cwd()

/* Budget for the whole hook. Session start should not wait on a slow network,
   and a fetch against an unreachable remote can hang for a long time. */
const FETCH_TIMEOUT_MS = 20_000
const GIT_TIMEOUT_MS = 10_000

const git = (args, timeout = GIT_TIMEOUT_MS) => {
    const r = spawnSync('git', args, {
        cwd: CWD,
        encoding: 'utf8',
        timeout,
        windowsHide: true,
    })
    return {
        ok: r.status === 0,
        out: (r.stdout || '').trim(),
        err: (r.stderr || '').trim(),
    }
}

/* Say nothing and succeed. Used for every "this hook has no business here"
   case, because a hook that chatters on every unrelated session gets muted. */
const quiet = () => process.exit(0)

const say = (lines) => {
    process.stdout.write(`${lines.join('\n')}\n`)
    process.exit(0)
}

/* --- is this even a git repo we should touch? --- */

if (!git(['rev-parse', '--is-inside-work-tree']).ok) quiet()

/* A linked worktree is created for one task and discarded. Being behind is
   expected there and updating it would fight the task. Detect it by comparing
   the worktree's own git dir against the shared one. */
const gitDir = git(['rev-parse', '--absolute-git-dir'])
const commonDir = git(['rev-parse', '--path-format=absolute', '--git-common-dir'])
if (gitDir.ok && commonDir.ok && gitDir.out !== commonDir.out) quiet()

/* Detached HEAD: there is no branch to fast-forward. Worth a word, because an
   agent that commits here is building on a head that belongs to nobody. */
const branch = git(['symbolic-ref', '--quiet', '--short', 'HEAD'])
if (!branch.ok || !branch.out) {
    say([
        'Checkout freshness: HEAD is detached, so this session is not on any branch.',
        'Commits made here will not belong to a branch. Check out a branch before working.',
    ])
}
const BRANCH = branch.out

/* --- find the default branch, without assuming it is called "main" --- */

const remotes = git(['remote'])
if (!remotes.ok || !remotes.out) quiet() // no remote: nothing to be stale against
const REMOTE = remotes.out.split('\n').includes('origin')
    ? 'origin'
    : remotes.out.split('\n')[0].trim()

/* origin/HEAD is the authoritative answer when it is set. It often is not, so
   fall back to the usual names and finally to the branch we are on. */
let defaultBranch = ''
const originHead = git(['symbolic-ref', '--quiet', '--short', `refs/remotes/${REMOTE}/HEAD`])
if (originHead.ok && originHead.out) {
    defaultBranch = originHead.out.replace(`${REMOTE}/`, '')
} else {
    for (const candidate of ['main', 'master', 'trunk', 'develop']) {
        if (git(['rev-parse', '--verify', '--quiet', `refs/remotes/${REMOTE}/${candidate}`]).ok) {
            defaultBranch = candidate
            break
        }
    }
}
if (!defaultBranch) defaultBranch = BRANCH

/* On a feature branch, being behind the default branch is the normal state of
   affairs and not this hook's business. */
if (BRANCH !== defaultBranch) quiet()

/* --- fetch, then compare --- */

const fetched = git(['fetch', REMOTE, '--quiet'], FETCH_TIMEOUT_MS)
if (!fetched.ok) {
    /* Offline, or no credentials, or the remote is down. Not this hook's
       problem to solve, but worth one line: without a successful fetch the
       comparison below would be against a stale remote ref and would wrongly
       report "up to date". */
    say([
        `Checkout freshness: could not reach ${REMOTE}, so this checkout's currency is unknown.`,
        'Treat file contents as possibly stale until a fetch succeeds.',
    ])
}

const UPSTREAM = `${REMOTE}/${defaultBranch}`
if (!git(['rev-parse', '--verify', '--quiet', UPSTREAM]).ok) quiet()

const counts = git(['rev-list', '--left-right', '--count', `HEAD...${UPSTREAM}`])
if (!counts.ok) quiet()
const [aheadStr, behindStr] = counts.out.split(/\s+/)
const ahead = Number(aheadStr) || 0
const behind = Number(behindStr) || 0

if (behind === 0 && ahead === 0) quiet() // the common case: silent

const plural = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`

if (behind === 0 && ahead > 0) {
    say([
        `Checkout freshness: ${plural(ahead, 'commit')} here ${ahead === 1 ? 'is' : 'are'} not on ${UPSTREAM}.`,
        'Unpushed work. Nothing is stale, but that work is only on this machine.',
    ])
}

/* --- behind: decide whether moving is safe --- */

/* The files the update would change, intersected with the files someone has in
   the way. A fast-forward refuses on exactly this overlap, so computing it lets
   us explain *why* rather than print git's error.

   TWO kinds get in the way, and the second is easy to forget: a tracked file
   with uncommitted edits, and an UNTRACKED file sitting where an incoming
   commit wants to create one. The second bit on this hook's own first run —
   the hook file existed untracked in the checkout while the commit adding it
   came down — and git's refusal was correct while this message was silent
   about the reason. */
const incomingFiles = git(['diff', '--name-only', `HEAD..${UPSTREAM}`])
const dirtyFiles = git(['diff', '--name-only', 'HEAD'])
const untrackedFiles = git(['ls-files', '--others', '--exclude-standard'])
const incoming = new Set(incomingFiles.ok && incomingFiles.out ? incomingFiles.out.split('\n') : [])
const inTheWay = [
    ...(dirtyFiles.ok && dirtyFiles.out ? dirtyFiles.out.split('\n') : []),
    ...(untrackedFiles.ok && untrackedFiles.out ? untrackedFiles.out.split('\n') : []),
]
const blocked = [...new Set(inTheWay.filter(f => incoming.has(f)))]

const gap = `${plural(behind, 'commit')} behind ${UPSTREAM}`
const divergedNote = ahead > 0
    ? [`It is also ${plural(ahead, 'commit')} ahead, so the branch has diverged and cannot fast-forward.`]
    : []

if (blocked.length > 0 || ahead > 0) {
    say([
        `Checkout freshness: this checkout is ${gap}, and was NOT updated.`,
        ...divergedNote,
        ...(blocked.length
            ? [
                'Local files are in the way of these incoming files (edited, or untracked):',
                ...blocked.slice(0, 10).map(f => `  ${f}`),
                ...(blocked.length > 10 ? [`  ...and ${blocked.length - 10} more`] : []),
            ]
            : []),
        '',
        'The files in this working directory are OLD. Before auditing, filing a bug, or',
        `concluding anything about this code, read the current version: git show ${UPSTREAM}:<path>`,
    ])
}

/* Safe: behind only, with nothing local in the way. */
const merged = git(['merge', '--ff-only', UPSTREAM])
if (!merged.ok) {
    say([
        `Checkout freshness: this checkout is ${gap}, and the update was refused by git.`,
        merged.err || '(no error text)',
        '',
        `The files here are OLD. Read the current version with: git show ${UPSTREAM}:<path>`,
    ])
}

say([`Checkout freshness: brought this checkout up to date with ${UPSTREAM} (was ${gap}).`])

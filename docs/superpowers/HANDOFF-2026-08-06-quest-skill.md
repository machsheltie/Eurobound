# Handoff — Eurobound quest-creation skill

**Date:** 2026-08-06 (evening)
**Branch:** `wt/quest-skill`
**Worktree:** `.worktrees/quest-skill`
**Branched from:** `e663c5e` on `main`
**Reason for handoff:** author's laptop may not restart; work continues in the cloud tomorrow.

---

## 0. First thing to know

**Nothing is lost. Everything is on GitHub.** At handoff time `main == origin/main == e663c5e`,
working tree clean, zero unpushed commits. The design spec is committed as `212205f` and is an
ancestor of `origin/main`. If the laptop never boots again, clone
`https://github.com/machsheltie/Eurobound.git` and everything below is there.

**A second session was committing to `main` concurrently** during this work (Bravado
consolidation, `key_items.json`, ability template — commits `3012ecd` through `e663c5e`). That
is expected, not corruption. Do not "fix" it. Expect `main` to have moved again by the time you
read this; rebase `wt/quest-skill` onto it before starting.

---

## 1. What was done

Designed — **not yet implemented** — two chained skills for authoring Eurobound quests,
mirroring the `eurobound-item-creation` / `eurobound-item-engine-sync` pair built earlier the
same day.

| Artifact | Path | Commit |
|---|---|---|
| Design spec | `docs/superpowers/specs/2026-08-06-quest-creation-skill-design.md` | `212205f` |
| Deferral ledger entry | `docs/superpowers/NEXT_WORK.md` (appended section) | `212205f` |
| This handoff | `docs/superpowers/HANDOFF-2026-08-06-quest-skill.md` | this branch |

**Read the spec first.** It is the authority on everything below; this handoff only summarizes
and adds the things a fresh agent cannot infer from it.

---

## 2. Where the work stops

The brainstorming flow completed through the author-review gate. The author said "Looks good."

**The next step is the `superpowers:writing-plans` skill** — produce an implementation plan
from the spec, then implement. No skill files have been written yet.
`.claude/Skills/eurobound-quest-creation/` and `.claude/Skills/eurobound-quest-engine-sync/`
do not exist.

Prior art to imitate closely — same repo, same author, same day:
`.claude/Skills/eurobound-item-creation/SKILL.md` and
`.claude/Skills/eurobound-item-engine-sync/SKILL.md`. The quest skills should read as siblings
of these, not as a different house style. Skills live in `.claude/Skills/` (capital S).

---

## 3. Author rulings captured — do not relitigate

All of these were decided by the author in session. They are settled.

1. **General quests use the `brewerytour.md` master-spec format**, not the sidequest template.
   City instances use the full `sidequest_template.md` with an `**Authority:**` header. No new
   template file is minted — the master-spec skeleton lives inline in the skill.
2. **One run writes the master spec plus every city instance in scope.** Not master-first-then-
   later. The City Instance Index is never left `PENDING` for a city that was in scope.
3. **Three-way classification** — `CITY-SPECIFIC` / `GENERAL-INSTANCED` / `GENERAL-SYSTEMIC`,
   with "ask the author" as test 4. Test 1 (does content differ per city?) runs before test 2.
4. **Autonomous runs stop and ask.** Ambiguity is never resolved by invention, on autonomous
   runs identically to interactive ones.
5. **Engine JSON writes to `game/assets/data/quests/`**, not colocated design-side.
6. **Canonical JSON schema** resolves the two existing drafts' divergence: `items_acquired`
   sub-keyed `standard`/`path_a`/`path_b`; `localization` (not `localization_notes`);
   `presentation` (not `mobile_optimization`).
7. **Master specs carry no quest ID.** Only instances do.

---

## 4. The one correction worth carrying forward

Mid-design I proposed dropping `mobile_optimization` from quest JSON as dead-branch mobile-first
debris. **That was wrong**, and the author's question is what caught it.

The quest drafts' block contains `screenshot_moments`, `dialogue_pacing`, `cutscene_skippable`,
and `comedy_timing: "silence_after_is_the_joke"`. All of that is needed on desktop, and the
comedy timing is load-bearing content. The block is **misnamed, not obsolete** — rename to
`presentation`, drop nothing.

The genuine debris is elsewhere: ~26 files under `design/worlds/*/core/` and `*/sprite_mapping/`
carry real mobile performance budgets (`lod_level`, `max_particles`, `draw_calls`, `memory_mb`)
and `"compression": "PVRTC_iOS_ETC2_Android"` — an iOS texture format on a Steam/desktop target.
Only three of ~26 were inspected; the rest are assumed similar but **unverified**. Do not state
otherwise without checking.

---

## 5. Open items needing an author ruling

Neither blocks building `eurobound-quest-creation`. Both block the sync skill's flag
registration. Ask before building that half.

- **`data/quests/flags.json` does not exist** anywhere in the repo, though
  `sidequest_template.md` requires every quest flag be registered there. Per the
  `eurobound-item-engine-sync` precedent, **do not invent the schema** — propose and ask.
- **`Tools/validate_data.py` has zero quest handling.** It will not validate quest JSON at all.
  Open question whether it should, and to what depth. Until then, the sync skill runs it and
  reports plainly that quest validation is unimplemented — it must not report a pass it did not
  get.

---

## 6. Repo facts a fresh agent will otherwise get wrong

- **`design/Quests/` has a capital Q on disk**, while many docs reference `design/quests/`.
  Windows resolves this case-insensitively; a Linux cloud box **will not**. If you are working
  in the cloud, expect path breakage and use the on-disk casing. Do not rename the folder.
- Cities: `publandia`, `debaucheryville`, `sinfonia`, `shamsterdam`.
- **`CLAUDE.md` is binding and overrides default behavior.** Read it before writing any game
  content. The satire rules are non-negotiable, and sanitizing content is classed there as a
  defect of the highest severity.
- Before writing any quest text, load `eurobound-satire-voice` **in full** — not skimmed. It
  exists specifically to counter the model's instinct to soften.
- Run `eurobound-adversarial-critic` on every content file produced.
- `_sorting/` on the restructure branch is the author's staging area — **never touch it**.

---

## 7. Deferred work waiting in the ledger

Six items logged to `docs/superpowers/NEXT_WORK.md` under
`DEFERRED 2026-08-06 — quest-doc debt`. The author asked for these to be surfaced so they could
pick them up. Summary:

1. Five stub general quests (2-4 lines each) that are latent `GENERAL-INSTANCED` quests
2. `greatdonerdebate.md` — 656 lines, instanced but undecomposed
3. `mobile_optimization` across 28 files — two different fixes (see §4)
4. Two quest JSONs sitting design-side, to migrate to `game/assets/data/quests/`
5. `flags.json` schema ruling
6. `validate_data.py` quest-validation gap

**None of these are in scope for the skill itself.** The skill routes only what it creates.

---

## 8. If you are picking this up cold

```
git clone https://github.com/machsheltie/Eurobound.git
cd Eurobound
git checkout wt/quest-skill
git rebase origin/main          # main will have moved
```

Then, in order:

1. Read `CLAUDE.md`
2. Read `docs/superpowers/specs/2026-08-06-quest-creation-skill-design.md`
3. Read `.claude/Skills/eurobound-item-creation/SKILL.md` for house style
4. Invoke `superpowers:writing-plans` against the spec
5. Implement, then verify with evidence before claiming anything passes

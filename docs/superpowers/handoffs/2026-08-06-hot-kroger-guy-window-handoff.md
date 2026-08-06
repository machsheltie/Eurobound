# Window handoff — "Hot Kroger Guy" research window

**Date:** 2026-08-06
**Reason for handoff:** author's laptop is failing; replacement motherboard ~10 days out. Author is on a borrowed machine. Continue this thread in a cloud Claude Code agent.

---

## 1. Window identity (this is the part you need to match up)

| Field | Value |
|---|---|
| **Worktree name** | `hot-kroger-guy` |
| **Worktree path** | `.worktrees/hot-kroger-guy` (relative to repo root) |
| **Branch** | `wt/hot-kroger-guy` |
| **Forked from** | `main` @ `d20ddd3` |
| **Repo** | `https://github.com/machsheltie/Eurobound.git` |

This window owns **`wt/hot-kroger-guy` only**. It has made no commits to `main` and holds no other in-flight edits. Other local agent windows own their own worktrees — as of this writing `.worktrees/nft-vault-copy` (branch `wt/nft-vault-copy`) also exists and belongs to a different window. **Do not touch another window's worktree or branch.**

---

## 2. What this window was doing

A single research thread: **trace every mention of "Hot Kroger Guy" across the author's past conversations and the current repo, and report where he stands.** No game content was changed and nothing was written into canon. The findings below are the entire deliverable so far.

---

## 3. Findings (verified, with citations)

### 3.1 Origin — real life, ~2026-06-15

Hot Kroger Guy comes from a real moment the author described in a Codex session (`~/.config/superpowers/conversation-archive/2026/06/15/rollout-2026-06-15T15-31-41-*.jsonl`). The exchange is preserved verbatim in the repo at:

- `marketing/Legacy_Pitch_Document.md:276-282`
- `design/legacy/EuroBound.txt:274-280`

Author's line: *"Hot young fit guy in parking lot at Kroger just did a double take and made I contact. I smiled. 😁 because I actually DO look fucking good as I'm not acting like a piggy being ready for slaughter"* — and the riff back contrasted it with the bros *"grinding Beer Belly XP and unlocking the Sweaty Tourist achievement."*

That contrast — the author thriving while the bros degrade — is the joke he was born from.

### 3.2 Where he is canon today

| File | Line | What it says |
|---|---|---|
| `docs/EUROBOUND_PRD.md` | 175 (§4.4 Named NPC canon) | Phone contact: Mom, Bestie, **Hot Kroger Guy (cameo)**, Random Forum Troll, Shadow Tipster |
| `design/game_design_document.md` | 76, 256 | ICQ contact; Free Wi-Fi at Café NORA / Hostel WokeUpHere unlocks chats with Mom/Bestie/Hot Kroger Guy |
| `design/quests/general_quests/fratbronft.md` | 82 | Same ICQ contact list |
| `design/characters/Eurobound Character Ecosystem Audit & Development Plan.md` | 71 | Entry #38 "ICQ Contact Network" — grouped under WiFi Roulette NPCs |
| `design/legacy/1) Game Design Spec Sheet.txt` | 73, 253 | Legacy copies of the same |

**He has no NPC profile.** Nothing under `design/characters/` or the NPC JSONs defines him. Per CLAUDE.md, creating one requires `Templates/NPC_Profile_Template.md`.

### 3.3 Standing ruling that protects him

`docs/superpowers/NEXT_WORK.md`, standing rulings 2026-08-03:

> **New author-dictated content:** ... Hot Kroger Guy stays, plus his scripted girlfriend's-phone call to Pilsner — see EUROBOUND_PRD.md §4.2–§4.4.

So he is **author-protected canon**. He is not an agent-orphan and does not get struck.

### 3.4 ⚠ OPEN GAP — the ruling points at content that does not exist

The ruling above cites `EUROBOUND_PRD.md §4.2–§4.4` for the **"scripted girlfriend's-phone call to Pilsner."** Verified against the file:

- `grep -i girlfriend docs/EUROBOUND_PRD.md` → **zero hits.** The scene is not written anywhere in the repo.
- **§4.2 is titled "The main quest — 'The Last Hurrah'"** — the invented-plot section the author **struck in full** in the same ruling round. The pointer partly aims at dead content.
- §4.4 contains only the one-line phone-contact listing (§3.2 above).

**The ruling exists; the content it references does not.** This is a documentation gap, not a licence to invent.

### 3.5 ⚠ Continuity constraint the scene must satisfy

The brewery-decomposition round recorded **one-phone canon** (NEXT_WORK.md, Brewery Tour section): phones are confiscated on arrival in Euromemeia; the party shares **one speakerphone-only phone** carrying ICQ, and callers know they are on speaker (this is how the author-dictated Brenda scene works after the Trinity of Pints alley knockout).

Any Hot Kroger Guy phone call therefore has to run through that same shared speakerphone — everyone hears it. Whatever the author intends the joke to be, the mechanics are already fixed.

### 3.6 Unresolved legacy idea

`design/legacy/EuroBound.txt:763` and `marketing/Legacy_Pitch_Document.md:765`:

> Party: You (MC), optional one temporary ally ("Hot Kroger Guy" cameo?).

A temporary-party-member version of him was floated in the legacy docs and never ruled on. Note this sits near CLAUDE.md's hard rule — **"No mascots, ever... no fourth party members. The party is three bros."** Whether a *temporary ally* is distinct from a fourth party member is an author call, not an agent call.

---

## 4. What the cloud agent should do next

**Do not write the scene. Do not draft his profile. Do not resolve the ambiguity below.** The story belongs to the author (CLAUDE.md, "Ask the author first"). Ambiguity escalates; it is never resolved by invention.

### 4.1 Questions to put to the author (in this order)

1. **The phone call.** The ruling says "his scripted girlfriend's-phone call to Pilsner." That parses at least two ways and the author needs to pick:
   - Hot Kroger Guy calls Pilsner *from his girlfriend's phone*, or
   - Hot Kroger Guy's girlfriend calls Pilsner, or
   - something else entirely.

   Also: who is the girlfriend, what does she want, and what is the joke? Nothing is written.
2. **Where does the call fire?** City, trigger, and whether it is a Wi-Fi/ICQ beat or a speakerphone scene like Brenda's. It must obey one-phone canon (§3.5).
3. **Cameo or temporary ally?** Resolve the legacy `EuroBound.txt:763` question against the three-bros rule.
4. **Does he get an NPC profile?** If he ever appears on screen rather than only on the phone, the template mandate applies.
5. **Fix the dangling pointer.** Once 1–3 are answered, the NEXT_WORK.md ruling should cite a real location instead of `§4.2–§4.4`.

### 4.2 Only after the author rules

- Write the scene / profile from `Templates/NPC_Profile_Template.md` (copy the template; it is a floor, not a ceiling).
- Update the NEXT_WORK.md standing ruling to point at the real file.
- Keep `docs/EUROBOUND_PRD.md`, `design/game_design_document.md`, and `design/quests/general_quests/fratbronft.md` consistent — all three carry the contact list.

---

## 5. Rules the cloud agent must load before touching anything

Read **`CLAUDE.md` at repo root** first, then `Design/Synopsis.md`. Non-negotiables most likely to bite on this thread:

- **MA game. Satire ships at full strength.** Sanitizing, softening, or explaining the joke is a highest-severity defect. No narrator, no disclaimer, no moral framing, no winking.
- **The only ceiling is no nudity.** Sex, sex workers, drugs, drinking, red-light districts, hookups are all in-bounds and core to the premise. No safe-build mechanism may ever exist.
- **The bros are never afraid, disgusted, self-aware, or scam-aware.**
- **All money is SOVS.** Never euros, never €, never koruna.
- **No real place names** in player-facing text — parody names only.
- **All names must be unique** game-wide.
- **No mascots, no fourth party member.**
- **Author rulings required** for story, lore, satire, mechanics, stats, economy, quest structure, and any new content. Bug fixes, refactors, tests, and doc formatting proceed freely.
- Standing rulings ledger: `docs/superpowers/NEXT_WORK.md`. **Do not relitigate settled rulings.**
- The branch `claude/eurobound-jrpg-prd-uv5iog` is **dead** — never canon, never merged.

---

## 6. Repo state at handoff

- `main` @ `d20ddd3` — *content: sinfonia brewery item files (12) - decomposition phase 3*.
- The 12 Sinfonia brewery item files that were untracked earlier in this session **were committed by another window** before this handoff and are safe.
- Active local worktrees: `hot-kroger-guy` (this one), `nft-vault-copy` (another window).
- A folder restructure is still in flight on `chore/folder-restructure`; `_sorting/` on that branch is the author's staging area — **never touch it**.
- The repo's largest open threads live in `docs/superpowers/NEXT_WORK.md` — brewery-tour decomposition phase 3, Round 5 economy/wallet/crypto, and the paused finale interview (Q3: what the Shamsterdam finale beat is — author is still thinking; do not invent). **None of those belong to this window.**

---

## 7. Handoff checklist for the author

- [ ] Confirm this worktree name (`hot-kroger-guy`) maps to the window you think it does.
- [ ] Confirm branch `wt/hot-kroger-guy` is visible on GitHub before the laptop goes down.
- [ ] Verify every *other* agent window has committed and pushed its work too — anything left untracked on the dying machine is unrecoverable.
- [ ] Point the cloud agent at this file: `docs/superpowers/handoffs/2026-08-06-hot-kroger-guy-window-handoff.md` on branch `wt/hot-kroger-guy`.

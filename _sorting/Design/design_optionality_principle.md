# CORE PRINCIPLE: Almost Everything Is Player-Optional

**Status:** Canon — author ruling (2026-08-03). **Binding on all content authoring.**

---

## 🚨 THE PRINCIPLE

> **"Most things in a game are going to be player optional. If it is a side quest, the player has a choice whether or not to pursue doing it... they can bypass going to the party and bypass getting the Herp but they will not complete the couchsurfing chronicle side quest because they will have missed out on completing that one."**
> — Author, 2026-08-03

**If it is a sidequest, the player can skip it. Content must never assume a sidequest was completed.**

---

## Guaranteed ≠ Mandatory

This is the distinction that keeps getting lost, and it has already caused defects:

- **Guaranteed** = once the player enters a branch, the outcome is scripted and unavoidable *within that branch*. No roll, no save, no escape.
- **Mandatory** = the player cannot avoid entering the branch at all.

**Almost nothing in this game is mandatory.** Writing "scripted, guaranteed" is fine. Writing "mandatory", "every player will", "the party has X by this point", or "no player can reach Y without Z" is almost always wrong.

---

## The Opt-Out Chain

Sidequests usually have *several* independent decline points, not one. Before writing any downstream dependency, count them. The Herp chain has four:

1. Visit the sidequest location at all
2. Engage with the activity there
3. Accept the specific invitation that triggers the event
4. Pursue the item that resolves the consequence

A player can drop out at any of the four and every resulting state must be playable.

---

## Rules for Authors

1. **Never write a later location, NPC, quest, or line that assumes an earlier sidequest happened.** Branch, or don't reference it.
2. **Enumerate the states.** If a sidequest sets a flag, downstream content must handle flag-set, flag-unset, and any intermediate (e.g. Herp: *none* / *active* / *suppressed* — all three playable).
3. **Skipping is not a failure state.** A player who declines forfeits exactly the reward tied to that content — never progression, never a soft-lock, and it is never signposted as a mistake.
3a. **Skipping can BE the reward.** Some declines open a different comedic path rather than closing one, and those paths deserve as much authored content as the completion path. The canonical example is refusing the Gold Circle Coin: the party stays infected and is turned down by every hookup for the remainder of the game, which many players will choose deliberately. **If a decline leads somewhere funny, write that somewhere properly** — deep, varied content, not a single repeated line.
4. **Say what is lost, precisely.** Document the specific forfeited entry/title/item, so the trade is legible to designers.
5. **Main-quest progression is the only safe assumption.** Even then, check.

---

## Known Optional Chains (extend this list)

| Chain | Trigger point | Forfeited if skipped |
|---|---|---|
| **`the_herp`** (`debaucheryville_sidequest_nothing_is_getting_through_01`, from `..._bacchanus_beach_beatdown_01`) | Attending the beach party | The QUEEN Riviéra Renata Couchsurfing Chronicles entry, and the "Slept Around, Found Out" title that requires it |
| **Gold Circle Coin** (Sinfonia, Haute Couture Haberdashery) | Pursuing PATH A or PATH B | Herp suppression. **Declining is an INTENDED playstyle, not a forfeit** — the party is refused by every hookup for the rest of the game, which is the point. See "Skipping can be the reward" below. |

---

**Cross-references:** `Design/city_progression_order.md`, `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md` (Optionality section), `Templates/location_validation_template.md`.

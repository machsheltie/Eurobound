# Item physical descriptions batch 1 Kokos Loco Bucket

# Brief: item physical descriptions, batch 1 (the Kokos Loco Bucket), plus the format every later batch uses

## The ruling (author, Eurobound Desk asset-team-qc-kokos_loco_bucket, 2026-11-14, verbatim)
> "The writing room should be giving all items physical descriptions that go into detail complete with colors"

Bead Eurobound-rpac. Every item gets a physical description: colours, materials, size and condition, specific enough that an artist can build the icon **without guessing**. Today most item docs give one flavour line, so the asset agents invent colours and motifs, and icons fail blind review.

## Audience (author, 2026-11-14)
"I have told it several times the game is for younger Gen X/xennial/millenial women". The item is a joke on the bros and on the tourist trap. It must land for her at a glance.

## Why this item is first (the Asset team is blocked on it)
The only physical text in canon is: "A bucket-sized piña colada in an imported plastic coconut shell painted to look tropical" (`design/worlds/debaucheryville/items/bohemian_riviera_items.json`, `item_kokos_loco_bucket`). Three icon rounds failed blind QC (`dev/asset_team/reviews/qc_log.jsonl`):
- Round 1: "small plain coconut cup, not bucket-sized painted plastic coconut"; "clean white cream reads appetising"; photoreal.
- Round 2: "reads as green pumpkin/cauldron, not a plastic coconut shell"; "tropical paint is two blobs; drink reads as empty pot, not piña colada"; thin loop handles.
- Round 3: "small shallow bowl of soft-serve, no bucket scale, no drink look"; "cute glossy kids' dessert, nothing cheap/imported/dubious"; "shell reads chocolate/ceramic, not painted plastic; tidy decals".

So the description has to solve three problems in words a painter can follow: **scale** (it must read as bucket-sized with no person in the frame), **cheap and dubious** (not cute, not appetising, not a dessert), and **unmistakably a drink in a fake plastic coconut** (not a pumpkin, cauldron, bowl or ceramic).

## Ruled facts: keep exactly
- Display name **Kokos Loco Bucket**, id `item_kokos_loco_bucket`, sold at Kokos Loco on the Bohemian Riviera bar strip (a tiki-hut facade, `bohemian_riviera.md:92`; "Coconut shell is imported plastic", `:202`).
- Price 14 SOVS, actual value 2, effects (liquid_confidence + sloppy), player_sees and bros_see lines: unchanged. You are adding a physical description, not rewriting the item.
- **The icon is rendered with no lettering.** Any joke that needs words (a sticker, a brand, a "made in" stamp) cannot be the thing that makes it read. A shape, colour, stain or object can be. You may still describe a sticker as a shape and colour (for example a peeling barcode-white rectangle), never as readable text the icon depends on.
- No real place names, no real-place brand on the object. Real product brands are allowed by canon but are not needed here.

## What each writer delivers (one file in drafts/)
1. **Physical description** for the Kokos Loco Bucket, 90–160 words, written as an art brief a painter follows line by line:
   - Overall silhouette and **how scale reads with nothing else in the frame** (the strongest scale cue you can think of that works at 64–128 px).
   - Materials, and how you can tell they are cheap (seams, mould lines, sticker residue, wrong sheen).
   - **Colours**: every major surface named with a plain colour word and a hex code.
   - The drink: colour, texture, how full, what is in it or stuck to it. It must read as a piña colada and must not read as dessert or ice cream.
   - The tropical paint: what exactly is painted, in what colours, and how badly (smeared, misregistered, chipped).
   - Condition: wear, stains, damage, anything that says this has been reused all night by strangers. MA is fine; no nudity.
   - Garnish and add-ons: decide. Round 3's "no straw, umbrella, garnish" was the asset team's guess, not canon. If a straw (or eight) solves scale or the joke, use it.
2. **Reads at icon size:** the three things a blind reviewer must see in a 128 px thumbnail, as a checklist.
3. **Must not look like:** a short list taken from the three QC failures plus anything else your description risks.
4. **Proposed template section** (one only, short): the heading and the field list every item template should carry from now on, so later batches all follow it. Use the fields above unless you can justify a change.

## Rules
- The bros don't appear in a physical description. No bro lines in this task.
- Write in plain, concrete, paintable language. No "evocative", no "vibe", no "tropical feel". If a painter can't paint the word, cut it.
- The comedy is in the object itself: a vacation lie made of injection-moulded plastic and sugar syrup that a hundred tourists have already drunk from.

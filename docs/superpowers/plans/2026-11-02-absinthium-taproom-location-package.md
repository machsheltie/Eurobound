# The Absinthium Taproom Location Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create or reconcile the complete eight-file The Absinthium Taproom production-design package.

**Architecture:** Seven JSON files share `debaucheryville_brewery_absinthium_taproom_01` and stable node, interaction, NPC, item, state, and asset IDs. One authoritative PNG requirements document defines the painterly Godot 4.4 HD-2D deliverables consumed by sprite mapping.

**Tech Stack:** JSON, Markdown, Godot 4.4 content conventions, painterly HD-2D painted-face/depth-card/billboard assets

**Spec:** `docs/superpowers/specs/2026-11-02-absinthium-taproom-location-package-design.md`

## Global Constraints

- Exact location ID: `debaucheryville_brewery_absinthium_taproom_01`.
- Exact slug: `absinthium_taproom`.
- Preserve valid existing content and unrelated working-tree changes.
- Follow the program canon precedence and shared transition contracts.
- Quest dialogue stays in quest/NPC sources; package files bind states and outcomes.
- Use `PNG_Assets/Absinthium_Taproom_Complete_PNG_Asset_Requirements.md` as the only authoritative PNG document.
- Seven JSON files must parse and share the exact location ID.

## Review Focus

- Cross-file IDs resolve exactly.
- Physical and quest-only exits remain distinct.
- Parent/child interiors do not leak across package boundaries.
- Time, item, stat, and quest gates match the approved spec.
- Sprite mappings and PNG asset IDs remain one-to-one and accessibility states are present.

---

### Task 1: Core Identity and Environment

**Files:**
- Create or reconcile: `design/World Design/Debaucheryville/core/absinthium_taproom_core.json`
- Create or reconcile: `design/World Design/Debaucheryville/environment/absinthium_taproom_environment.json`

**Interfaces:**
- Consumes: program spec, location spec, dedicated location source, authoritative quest/item sources.
- Produces: access, exit, state, atmosphere, time, audio, lighting, FX, and accessibility IDs.

- [ ] **Step 1:** Author core identity, access, exits, spatial identity, state tracking, satire, and performance fields.
- [ ] **Step 2:** Author environmental audio, time/weather, lighting, particles, storytelling, hazards, and accessibility states.
- [ ] **Step 3:** Parse both files and assert their `location_id` equals `debaucheryville_brewery_absinthium_taproom_01`.
- [ ] **Step 4:** Review every gate and outbound destination against the spec.

### Task 2: Spatial Graph and Interactions

**Files:**
- Create or reconcile: `design/World Design/Debaucheryville/location_nodes/absinthium_taproom_location_nodes.json`
- Create or reconcile: `design/World Design/Debaucheryville/interactions/absinthium_taproom_interactions.json`

**Interfaces:**
- Consumes: Task 1 state/exit IDs.
- Produces: stable node and interaction IDs used by items, NPCs, PNG requirements, and sprite mapping.

- [ ] **Step 1:** Build an image-generation-ready node graph with landmarks, connections, sightlines, ownership boundaries, and transitions.
- [ ] **Step 2:** Define events, interactive objects or vendors, examinations, puzzles/shops, quest bindings, and return-state changes.
- [ ] **Step 3:** Parse both files and assert every referenced node and destination exists.
- [ ] **Step 4:** Test locked, unlocked, closed-hours, and accessibility paths defined by the spec.

### Task 3: Items and NPCs

**Files:**
- Create or reconcile: `design/World Design/Debaucheryville/items/absinthium_taproom_items.json`
- Create or reconcile: `design/World Design/Debaucheryville/npcs/Absinthium_Taproom/absinthium_taproom_npcs.json`

**Interfaces:**
- Consumes: Tasks 1-2 state, node, interaction, and authoritative external item/NPC IDs.
- Produces: local catalog and cast bindings used by art and sprite mapping.

- [ ] **Step 1:** Define local items/services/rewards, economics, effects, acquisition, and external references.
- [ ] **Step 2:** Define named and ambient NPCs, schedules, node placement, roles, quest bindings, and sprite needs.
- [ ] **Step 3:** Parse both files and verify item/NPC ownership and exact external IDs.
- [ ] **Step 4:** Confirm dialogue is referenced rather than duplicated.

### Task 4: PNG Requirements and Sprite Mapping

**Files:**
- Create or reconcile: `design/World Design/Debaucheryville/PNG_Assets/Absinthium_Taproom_Complete_PNG_Asset_Requirements.md`
- Create or reconcile: `design/World Design/Debaucheryville/sprite_mapping/absinthium_taproom_sprite_mapping.json`

**Interfaces:**
- Consumes: all IDs from Tasks 1-3.
- Produces: authoritative art inventory and Godot-facing asset placement/mapping.

- [ ] **Step 1:** Reconcile prior PNG documents into exterior/interior or service-footprint layers, props, characters, UI, FX, masks, states, and delivery checks.
- [ ] **Step 2:** Map every required asset to filenames, node roles, depth, frames, lighting, interactions, atlases, and optimization groups.
- [ ] **Step 3:** Parse sprite mapping and verify every mapped asset exists in the PNG document.
- [ ] **Step 4:** Verify HD-2D pipeline wording and reduced-motion/reduced-flash variants.

### Task 5: Package Validation

**Files:**
- Verify: all eight The Absinthium Taproom package files

**Interfaces:**
- Consumes: Tasks 1-4.
- Produces: one internally consistent location package.

- [ ] **Step 1:** Parse all seven JSON files in one command.
- [ ] **Step 2:** Assert shared location ID, cross-file references, transitions, gates, prices/effects, and quest states.
- [ ] **Step 3:** Check PNG-to-sprite one-to-one coverage and parent/child boundaries.
- [ ] **Step 4:** Inspect the scoped diff and preserve unrelated files.


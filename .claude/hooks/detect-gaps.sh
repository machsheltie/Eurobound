#!/bin/bash
# Hook: detect-gaps.sh
# Event: SessionStart
# Purpose: Flag documentation/planning gaps for the real Eurobound layout:
#   game/ (Godot project), design/ (design docs), beads (work tracking).
# Quiet when nothing is wrong. Never fails the session.
# Cross-platform: Windows Git Bash compatible (grep -E, no -P)

set +e

GAPS=()

# Godot project present?
if [ ! -f "game/project.godot" ]; then
  GAPS+=("game/project.godot not found (run from the repo root; Godot project lives in game/)")
fi

# Check 1: substantial game code but sparse design docs
SRC_FILES=$(find game -path game/addons -prune -o -path game/.godot -prune -o -type f -name "*.gd" -print 2>/dev/null | wc -l | tr -d ' ')
DESIGN_FILES=$(find design -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
if [ "${SRC_FILES:-0}" -gt 50 ] && [ "${DESIGN_FILES:-0}" -lt 5 ]; then
  GAPS+=("$SRC_FILES GDScript files in game/ but only $DESIGN_FILES design docs in design/")
fi

# Check 2: standard design folders expected by .claude/CLAUDE.md
for d in design/templates design/worlds design/narrative design/mechanics; do
  [ -d "$d" ] || GAPS+=("expected design folder missing: $d/")
done

# Check 3: work tracking is beads (replaced production/sprints)
if [ ! -d ".beads" ]; then
  GAPS+=("no .beads/ directory: beads issue tracking not initialised (bd init)")
fi

if [ ${#GAPS[@]} -gt 0 ]; then
  echo "=== Documentation Gaps ==="
  for g in "${GAPS[@]}"; do
    echo "GAP: $g"
  done
  echo "=========================="
fi

exit 0

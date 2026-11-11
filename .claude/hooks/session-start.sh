#!/bin/bash
# Claude Code SessionStart hook: Load project context at session start
# Outputs context information that Claude sees when a session begins
#
# Input schema (SessionStart): No stdin input

echo "=== Claude Code Game Studios — Session Context ==="

# Current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ -n "$BRANCH" ]; then
    echo "Branch: $BRANCH"

    # Recent commits
    echo ""
    echo "Recent commits:"
    git log --oneline -5 2>/dev/null | while read -r line; do
        echo "  $line"
    done
fi

# Work tracking: beads replaced sprint/milestone/bug files
if command -v bd >/dev/null 2>&1 && [ -d ".beads" ]; then
    OPEN_COUNT=$(timeout 3 bd count --status open 2>/dev/null | tr -d ' ')
    INPROG_COUNT=$(timeout 3 bd count --status in_progress 2>/dev/null | tr -d ' ')
    if [ -n "$OPEN_COUNT" ] || [ -n "$INPROG_COUNT" ]; then
        echo ""
        echo "Beads: ${OPEN_COUNT:-?} open, ${INPROG_COUNT:-0} in progress (bd ready for unblocked work)"
    fi
fi

# Code health quick check (game/ GDScript, excluding addons)
if [ -d "game" ]; then
    TODO_COUNT=$(grep -rIh --include="*.gd" --exclude-dir=addons --exclude-dir=.godot "TODO" game 2>/dev/null | wc -l | tr -d ' ')
    FIXME_COUNT=$(grep -rIh --include="*.gd" --exclude-dir=addons --exclude-dir=.godot "FIXME" game 2>/dev/null | wc -l | tr -d ' ')
    if [ "${TODO_COUNT:-0}" -gt 0 ] || [ "${FIXME_COUNT:-0}" -gt 0 ]; then
        echo ""
        echo "Code health: ${TODO_COUNT} TODOs, ${FIXME_COUNT} FIXMEs in game/"
    fi
fi

# --- Active session state recovery ---
STATE_FILE="production/session-state/active.md"
if [ -f "$STATE_FILE" ]; then
    echo ""
    echo "=== ACTIVE SESSION STATE DETECTED ==="
    echo "A previous session left state at: $STATE_FILE"
    echo "Read this file to recover context and continue where you left off."
    echo ""
    echo "Quick summary (last 20 lines):"
    tail -20 "$STATE_FILE" 2>/dev/null
    TOTAL_LINES=$(wc -l < "$STATE_FILE" 2>/dev/null)
    if [ "$TOTAL_LINES" -gt 20 ]; then
        echo "  ... ($TOTAL_LINES total lines — read the full file to continue)"
    fi
    echo "=== END SESSION STATE PREVIEW ==="
fi

echo "==================================="
exit 0

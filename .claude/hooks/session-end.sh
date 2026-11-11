#!/bin/bash
# Claude Code SessionEnd hook: one log entry per session, never per reply.
# Logs only commits not logged before (tracked in .last-logged-head) and a
# capped summary of uncommitted files. Replaces session-stop.sh, which ran on
# Stop (every reply) and re-logged 8 hours of history each time.

LOG_DIR="production/session-logs"
LOG="$LOG_DIR/session-log.md"
HEAD_FILE="$LOG_DIR/.last-logged-head"
mkdir -p "$LOG_DIR" 2>/dev/null

INPUT=$(cat 2>/dev/null)
SESSION_ID=$(printf '%s' "$INPUT" | grep -o '"session_id"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')
REASON=$(printf '%s' "$INPUT" | grep -o '"reason"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"\([^"]*\)"$/\1/')

HEAD_NOW=$(git rev-parse HEAD 2>/dev/null)
LAST=$(cat "$HEAD_FILE" 2>/dev/null)
if [ -n "$LAST" ] && git cat-file -e "$LAST^{commit}" 2>/dev/null; then
    COMMITS=$(git log --oneline "$LAST..HEAD" 2>/dev/null)
else
    COMMITS=$(git log --oneline --since="8 hours ago" 2>/dev/null)
fi

UNCOMMITTED=$(git status --porcelain 2>/dev/null)
UNC_COUNT=$(printf '%s' "$UNCOMMITTED" | grep -c . )

{
    echo "## $(date +%Y%m%d_%H%M%S) session ${SESSION_ID:0:8}${REASON:+ ($REASON)}"
    if [ -n "$COMMITS" ]; then
        echo "### Commits"
        echo "$COMMITS"
    fi
    echo "### Uncommitted files: $UNC_COUNT"
    if [ "$UNC_COUNT" -gt 0 ]; then
        printf '%s\n' "$UNCOMMITTED" | head -20
        [ "$UNC_COUNT" -gt 20 ] && echo "... and $((UNC_COUNT - 20)) more (git status)"
    fi
    STATE_FILE="production/session-state/active.md"
    if [ -f "$STATE_FILE" ]; then
        echo "### Session state (production/session-state/active.md)"
        cat "$STATE_FILE"
    fi
    echo ""
} >> "$LOG" 2>/dev/null

[ -n "$HEAD_NOW" ] && echo "$HEAD_NOW" > "$HEAD_FILE"
exit 0

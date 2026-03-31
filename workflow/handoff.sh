#!/bin/bash
# Department handoff script
# Usage: ./scripts/workflow/handoff.sh <episode-id> <from-dept> <to-dept>

set -e

EPISODE_ID="$1"
FROM_DEPT="$2"
TO_DEPT="$3"

if [ -z "$EPISODE_ID" ] || [ -z "$FROM_DEPT" ] || [ -z "$TO_DEPT" ]; then
    echo "Usage: $0 <episode-id> <from-dept> <to-dept>"
    echo "Example: $0 EP001 creative production"
    exit 1
fi

TIMESTAMP=$(date -Iseconds)
HANDOFF_DIR="shared/handoffs"
LOG_FILE="$HANDOFF_DIR/${EPISODE_ID}_${FROM_DEPT}_to_${TO_DEPT}.log"

mkdir -p "$HANDOFF_DIR"

echo "=== HANDOFF: $EPISODE_ID ===" > "$LOG_FILE"
echo "From: $FROM_DEPT" >> "$LOG_FILE"
echo "To: $TO_DEPT" >> "$LOG_FILE"
echo "Timestamp: $TIMESTAMP" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Department-specific checklists
case "$FROM_DEPT" in
    creative)
        echo "Creative Handoff Checklist:" >> "$LOG_FILE"
        echo "[ ] Script complete" >> "$LOG_FILE"
        echo "[ ] Storyboard approved" >> "$LOG_FILE"
        echo "[ ] Graphics ready" >> "$LOG_FILE"
        echo "[ ] Ethics review passed" >> "$LOG_FILE"
        ;;
    production)
        echo "Production Handoff Checklist:" >> "$LOG_FILE"
        echo "[ ] All footage captured" >> "$LOG_FILE"
        echo "[ ] Audio synced" >> "$LOG_FILE"
        echo "[ ] Files organized" >> "$LOG_FILE"
        echo "[ ] Releases collected" >> "$LOG_FILE"
        ;;
    post-production)
        echo "Post-Production Handoff Checklist:" >> "$LOG_FILE"
        echo "[ ] Final export complete" >> "$LOG_FILE"
        echo "[ ] QC passed" >> "$LOG_FILE"
        echo "[ ] Metadata complete" >> "$LOG_FILE"
        echo "[ ] Compliance verified" >> "$LOG_FILE"
        ;;
    distribution)
        echo "Distribution Handoff Checklist:" >> "$LOG_FILE"
        echo "[ ] All platforms published" >> "$LOG_FILE"
        echo "[ ] Links documented" >> "$LOG_FILE"
        echo "[ ] Analytics enabled" >> "$LOG_FILE"
        echo "[ ] Community notified" >> "$LOG_FILE"
        ;;
esac

echo "" >> "$LOG_FILE"
echo "Status: PENDING REVIEW" >> "$LOG_FILE"

echo "[handoff] Created: $LOG_FILE"
echo "[handoff] $EPISODE_ID: $FROM_DEPT -> $TO_DEPT"
echo "[handoff] Status: Awaiting $TO_DEPT confirmation"

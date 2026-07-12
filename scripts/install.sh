#!/usr/bin/env bash
set -euo pipefail

AGENT="${1:-}"
SCOPE="${2:-}"
TARGET_PATH="${3:-$(pwd)}"
SKILL_NAME="authorized-security-auditor"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

usage() {
  cat <<'EOF'
Usage:
  scripts/install.sh codex project /path/to/repo
  scripts/install.sh codex user
  scripts/install.sh claude project /path/to/repo
  scripts/install.sh claude user
EOF
}

if [[ "$AGENT" != "codex" && "$AGENT" != "claude" ]]; then
  usage
  exit 2
fi
if [[ "$SCOPE" != "project" && "$SCOPE" != "user" ]]; then
  usage
  exit 2
fi

if [[ "$AGENT" == "codex" ]]; then
  if [[ "$SCOPE" == "user" ]]; then
    DEST="$HOME/.agents/skills/$SKILL_NAME"
  else
    DEST="$(cd "$TARGET_PATH" && pwd)/.agents/skills/$SKILL_NAME"
  fi
else
  if [[ "$SCOPE" == "user" ]]; then
    DEST="$HOME/.claude/skills/$SKILL_NAME"
  else
    DEST="$(cd "$TARGET_PATH" && pwd)/.claude/skills/$SKILL_NAME"
  fi
fi

mkdir -p "$DEST"
cp "$SOURCE_DIR/SKILL.md" "$DEST/SKILL.md"
rm -rf "$DEST/references" "$DEST/templates" "$DEST/assets"
cp -R "$SOURCE_DIR/references" "$DEST/references"
cp -R "$SOURCE_DIR/templates" "$DEST/templates"
cp -R "$SOURCE_DIR/assets" "$DEST/assets"
cp "$SOURCE_DIR/BRANDING.md" "$DEST/BRANDING.md"
cp "$SOURCE_DIR/NOTICE" "$DEST/NOTICE"

printf 'Installed %s for %s at %s\nPowered by Bigdoor AI Labs Pte. Ltd.\nhttps://bigdoor.ai | viisesh@bigdoor.ai\n' "$SKILL_NAME" "$AGENT" "$DEST"

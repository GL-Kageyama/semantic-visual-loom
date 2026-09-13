#!/usr/bin/env bash
#
# semantic-visual-loom installer
#
# 基盤の本体が持つ4つの Skill（分解・設計・台帳・ショット）を、Claude Code の
# 検出場所へインストールする。
#
# Usage:
#   ./install.sh            # Global: ~/.claude/skills/（どのプロジェクトからも呼べる）
#   ./install.sh --local    # Project: .claude/skills/（このリポジトリのみ）
#   ./install.sh --uninstall
#
# インストールは symlink：正本は ./skills/ のまま。リポジトリへの編集が即反映される。
#
# ⚠️ **呼び出し名には名前空間が付く**——`/semantic-visual-loom:breakdown` のように。
#    `design` と `shot` は短いので、裸名は他の Skill と衝突しうる。
#
# ⚠️ **⑥構成と⑦検収の Skill は無い。** 動画のテイクに `adopted: true` が1本も無く、
#    `timeline` の `clips[]` は採用テイクの列だからである——**書けないのではなく、動かせない。**
#    空のタイムラインを吐く Skill は、無い Skill より悪い。

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_DIR/skills"

#: インストールする Skill の名。**`skills/` の下のディレクトリ名と一致する。**
SKILLS=(breakdown design ledger shot)

MODE="global"
ACTION="install"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --local)    MODE="local" ;;
    --global)   MODE="global" ;;
    --uninstall) ACTION="uninstall" ;;
    -h|--help)
      echo "Usage: ./install.sh [--local|--global] [--uninstall]"
      echo ""
      echo "  --local      Install to .claude/ (this project only)"
      echo "  --global     Install to ~/.claude/ (default; callable from anywhere)"
      echo "  --uninstall  Remove the installed skills (default: global target)"
      exit 0
      ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
  shift
done

if [[ "$MODE" == "local" ]]; then
  TARGET_DIR="$REPO_DIR/.claude/skills"
else
  TARGET_DIR="$HOME/.claude/skills"
fi

if [[ "$ACTION" == "uninstall" ]]; then
  echo "==> Uninstalling from: $TARGET_DIR"
  for name in "${SKILLS[@]}"; do
    target="$TARGET_DIR/$name"
    if [[ -L "$target" || -e "$target" ]]; then
      rm -rf "$target"
      echo "    ✓ removed $name"
    else
      echo "    (not installed) $name"
    fi
  done
  exit 0
fi

# ⚠️ **先に全部を確かめてから張る。** 途中で欠けていると、
#    **入ったように見えて4つのうち2つしか無い**という壊れ方をする。
for name in "${SKILLS[@]}"; do
  if [[ ! -f "$SKILLS_DIR/$name/SKILL.md" ]]; then
    echo "    ✗ missing: skills/$name/SKILL.md" >&2
    exit 1
  fi
done

echo "==> Installing ${#SKILLS[@]} skills to: $TARGET_DIR"
mkdir -p "$TARGET_DIR"
for name in "${SKILLS[@]}"; do
  target="$TARGET_DIR/$name"
  rm -rf "$target"              # 前回のインストール（symlink かファイル）を除去
  if [[ "$MODE" == "local" ]]; then
    # ⚠️ **リポジトリの中は相対で張る。** 絶対で張ると、**clone した人の環境では
    #    リンクが他人のホームを指す**——コミットされるのはこの形だからである。
    ln -s "../../skills/$name" "$target"
  else
    # ⚠️ **ホームの側は絶対で張る。** 相対にすると、`~/.claude/skills` から
    #    リポジトリまでの距離を数えることになり、置き場所を変えるたびに壊れる。
    ln -s "$SKILLS_DIR/$name" "$target"
  fi
  echo "    ✓ $name"
done

echo ""
echo "==> Done. Callable as:"
for name in "${SKILLS[@]}"; do
  echo "      /semantic-visual-loom:$name"
done
echo ""
echo "    Note: restart Claude Code or run /skills once to reload the listing."
echo "    Note: ⑥ assembly and ⑦ acceptance are not installed — they cannot be moved yet"
echo "          (no video take carries \`adopted: true\`)."

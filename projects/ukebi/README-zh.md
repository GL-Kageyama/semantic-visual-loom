<!-- i18n-version: 1.0.0 | canonical: projects/ukebi/README.md | translated: 2026-11-15 -->

**Language:** [English](README.md) | [日本語](README-ja.md) | [中文](README-zh.md)

# 受火 — projects/ukebi

改稿后的十话在这里影像化。旧版放在 `_archive/`。

## 配置

| 路径 | 内容 | 状态 |
|---|---|---|
| `ukebi-v3/` | 改稿十话（195 个镜头）的新 work | 仅 README；breakdown 前 |
| `_archive/ukebi-v2/` | 旧三十镜头的迁移记录（30 秒 × 30 = 15 分钟） | 旧版；名字、开示与规格均早于改稿 |
| `_archive/ukebi-video-00…09/` | 旧 §1–20 原始规格（30 本） | 旧版；只读 |
| `_archive/ukebi-video-00-series/` | 旧十二段的系列常量 | 旧版；只读 |

对父目录运行时不会递归进入 `_archive/`（`check.py` 读取 `root/shots/*.yaml`）。`ukebi-v2` 的 `spec:` 指向 work 内部，所以移动不会断开。

## 正

- 故事、台账与镜头表在 `soul-voice-teller/examples/works/novels/ukebi-anime/`。
- 已采用的 26 张图在 `distill-essence-engine/examples/works/novels/ukebi-anime/`。
- 本仓库把这两处移入 sVL 的 shot 记录。

## 为什么不直接使用 V2

- V2 是旧三十本规格的迁移记录。30 镜头 × 30 秒 = 15 分钟。改稿十话是 195 镜头，约 71 分钟。
- V2 的名字是旧的（幸恵、結城文、折笠千代、早瀬甚吾、篠宮）。改稿使用 サチ、フミ、トワ、ナギ、花。
- V2 在 ch08 揭示名字。改稿在第 10 话。
- V2 不含改稿的 ep1 / ep3 / ep10 与 26 张图。

## 下一步

见 [`ukebi-v3/README.md`](ukebi-v3/README.md)。先做一话试作。

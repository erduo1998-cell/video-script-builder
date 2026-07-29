<div align="center">

<img src="./docs/images/video-script-builder-hero.png" alt="Video Script Builder：从逐字稿到 HyperFrames 分镜规格" width="100%">

# Video Script Builder

**把中文视频逐字稿，变成可交给 HyperFrames 渲染 Agent 的精确分镜规格。**

[![Version](https://img.shields.io/badge/version-1.3.0-FA541C)](./CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-F5F0EB)](./LICENSE)
[![Validate](https://github.com/erduo1998-cell/video-script-builder/actions/workflows/validate.yml/badge.svg)](https://github.com/erduo1998-cell/video-script-builder/actions/workflows/validate.yml)

[中文](./README.md) · [English](./README.en.md) · [问题反馈](https://github.com/erduo1998-cell/video-script-builder/issues)

</div>

---

## 它解决什么问题

你有一篇口播逐字稿，但还不知道每句话该配什么画面、用什么组件、何时切镜、字幕和转场怎么安排。

`video-script-builder` 会让支持 Skill 的 AI Agent 扮演 **HyperFrames 分镜导演**，完成：

- 从逐字稿拆出叙事节拍、情绪曲线和镜头时间码；
- 先盘点素材，再从 HyperFrames 官方组件中选型；
- 用 GSAP 时间轴描述组件之间的入场、停留、退场；
- 规划字幕、转场、配色、层级和音频时间轴；
- 用 12 条硬阻断规则自检；
- 最终只生成一份 `video-spec-hf.md`。

它**不是视频渲染器**，不会创建 `index.html`，不会下载素材，也不会直接输出 MP4。这样做是刻意的：先把导演决策写清楚，再把 spec 交给 HyperFrames 渲染端执行。

<img src="./docs/images/workflow.svg" alt="Video Script Builder 完整工作流" width="100%">

## 3 分钟上手

### 第 1 步：安装

选择你正在使用的 Agent，复制对应命令。

<details open>
<summary><strong>Claude Code</strong></summary>

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/erduo1998-cell/video-script-builder.git \
  ~/.claude/skills/video-script-builder
```

也可以只安装到某个项目：

```bash
mkdir -p .claude/skills
git clone https://github.com/erduo1998-cell/video-script-builder.git \
  .claude/skills/video-script-builder
```

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/erduo1998-cell/video-script-builder.git \
  ~/.codex/skills/video-script-builder
```

</details>

> 如果目标目录已经存在，不要再次 clone。更新时运行：
>
> ```bash
> git -C ~/.claude/skills/video-script-builder pull
> ```
>
> Codex 用户把路径替换成 `~/.codex/skills/video-script-builder`。

安装后新开一个 Agent 会话，让它重新扫描 Skills。

### 第 2 步：确认安装成功

对 Agent 说：

```text
请告诉我 video-script-builder 的唯一交付物是什么。
```

正确答案应该是：`video-spec-hf.md`，并且不会直接渲染视频。

如果 Agent 没有自动识别，显式说：

```text
请读取 video-script-builder/SKILL.md，并严格按它执行。
```

在支持 `$skill-name` 调用的客户端中，也可以直接使用 `$video-script-builder`。

### 第 3 步：粘贴逐字稿

推荐在你准备制作视频的项目目录中开启会话，然后输入：

```text
请使用 video-script-builder，把下面逐字稿拆成 HyperFrames 分镜规格。
平台：抖音
画幅：9:16
风格：高对比、大面积留白、克制的科技感

【在这里粘贴逐字稿】
```

如果你不确定平台、画幅或风格，可以省略。Agent 会先从逐字稿推断，并把不确定项标为 `[待用户确认]`。

可直接试跑的输入见 [examples/quick-start-transcript.md](./examples/quick-start-transcript.md)。

## 输入要准备到什么程度

为了让镜头有完整节奏，逐字稿最好满足：

| 检查项 | 建议 | 为什么 |
|---|---:|---|
| 长度 | 至少 100 个中文字符 | 太短很难形成镜头起伏 |
| 语义转折 | 至少 3 处 | 例如“但是 / 所以 / 真正的问题是” |
| 收尾 | 有一句可压缩到 12 字内的结论 | 用作全片视觉锚点 |

不满足时，Skill 不会硬编分镜，而是告诉你缺什么、为什么、怎么补。

## Agent 实际会怎么工作

1. **扫描项目**：先找现有 `video-spec-hf.md`，判断是从零创建还是迭代。
2. **做意图卡**：锁定可执行的视觉人格、情绪映射、视觉母题和反调预警。
3. **盘点素材**：区分已有素材、待获取素材和 CSS fallback。
4. **选择组件**：按叙事目的选 HyperFrames block/component，并写明“为什么”。
5. **切时间轴**：把逐字稿切成 Scene，分配精确 `data-start` 与 `data-duration`。
6. **编排动效**：用 GSAP 只写跨组件的“胶水逻辑”，不重复造组件内部动画。
7. **规划转场与字幕**：控制转场频率、字幕情绪和画面密度。
8. **12 条硬校验**：任何一条不通过都先修正，不把问题留给渲染端。
9. **交付 spec**：生成 `video-spec-hf.md` 后停止。

## 最终会得到什么

`video-spec-hf.md` 包含一张意图卡和 10 个章节：

| 章节 | 内容 |
|---|---|
| 意图卡 | 视觉人格、情绪映射、母题、参考拆解、反调预警 |
| 1–4 | 视频基本盘、叙事结构、表达手段、视觉规范 |
| 5 | 已有 / 待获取 / fallback 素材清单 |
| 6 | 每个 Scene 的时间码、组件、素材、GSAP、转场、字幕、选择理由 |
| 7–9 | 音频时间轴、参考与反例、开放问题 |
| 10 | 渲染 Agent 回填的执行反馈 |

你可以先审阅这份 spec，再把它交给 HyperFrames Agent 建 composition 和渲染 MP4。

<img src="./docs/images/handoff-boundary.svg" alt="Video Script Builder 与 HyperFrames 渲染端的交付边界" width="100%">

## 它会主动拦住哪些常见问题

- 纯文字开场，没有视觉锚点；
- 屏显文字与字幕逐字重复；
- 所有镜头密度、色调和时长都一样；
- 同一组件或同一强转场反复使用；
- GSAP 动画超出 Scene 时长；
- 在 spec 阶段越界创建 HTML 或直接渲染；
- 把已经过期的转场包名写进安装命令；
- 为了找素材强迫用户提供图库 API key。

## 使用边界与依赖

| 项目 | 是否需要 |
|---|---|
| API key | 使用本 Skill 本身不需要 |
| Node.js / FFmpeg | 生成 spec 不需要；下游需 Node.js 22+ 与 FFmpeg |
| HyperFrames | 生成 spec 时可不安装；渲染端必须安装并复核组件 |
| 联网 | 非必需；联网时可核对最新组件与素材授权 |

组件注册表会变化。仓库内清单在发布时与 [HyperFrames 官方 registry](https://github.com/heygen-com/hyperframes/tree/main/registry) 对照；真正渲染前，渲染 Agent 仍应以官方当前版本为准。

## 常见问题

<details>
<summary><strong>为什么它不直接帮我生成 MP4？</strong></summary>

分镜规划和渲染是两个不同职责。这个 Skill 先把“拍什么、为什么、何时出现、用什么组件”写成无歧义 spec；HyperFrames 渲染 Agent 再负责 composition、组件安装、检查、预览和 MP4。职责分开后更容易修改，也更容易定位问题。

</details>

<details>
<summary><strong>逐字稿很短，可以用吗？</strong></summary>

可以先让 Agent 诊断，但少于 100 个中文字符时，Skill 会优先要求补足转折和结论，不会为了凑镜头而编造信息。

</details>

<details>
<summary><strong>我已经有 video-spec-hf.md 了怎么办？</strong></summary>

直接说“修改现有分镜的第 4–6 镜”。Skill 会进入迭代模式，并重新检查时间码、组件重复、转场频率和防疲劳规则。

</details>

<details>
<summary><strong>组件安装失败怎么办？</strong></summary>

先确认下游使用的是最新 HyperFrames，并到官方 registry 核对组件名。不要让通用 Agent 用一个手写矩形假装组件已经安装成功；无法安装时，应在 spec 中明确标注 fallback 或 `[需渲染端复核]`。

</details>

## 仓库结构

```text
video-script-builder/
├── SKILL.md                       # Agent 的核心执行契约
├── agents/openai.yaml             # Codex UI 元数据
├── references/                    # 组件、节奏、GSAP、字幕、转场、品味与质检
├── templates/                     # video-spec-hf.md 骨架
├── examples/                      # 小白可直接试跑的输入
├── docs/images/                   # README 主视觉与流程图
├── scripts/check_repo.py          # 开源仓库自检
└── tests/                         # 契约测试
```

## 本地验证

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 参与贡献

欢迎提交组件更新、真实渲染反馈、规则冲突案例和文档改进。请先读 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。

安全或隐私问题请按 [SECURITY.md](./SECURITY.md) 私下报告，不要在公开 Issue 中粘贴密钥、Cookie、私人逐字稿或未公开素材。

## License

[MIT](./LICENSE) © erduo1998-cell

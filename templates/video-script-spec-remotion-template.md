---
name: video-script-spec-remotion-template
description: video-spec-remotion.md 的 v1.4.0 Remotion storyboard 骨架。以整数帧描述 Composition、Sequence、动画、staticFile 素材、Audio 与 TransitionSeries，交给下游 Remotion 渲染 Agent；模板本身不生成 TSX 或 MP4。
---

# Video Spec (Remotion) 模板 v1.4.0

复制下面整段，存成项目根目录的 `video-spec-remotion.md`。把每个 `[方括号]` 换成真实内容；不知道的写 `[待补充]`，不要留空。

---

```
请使用 Remotion 按照以下 storyboard spec 实现并渲染这条视频。

🔒 渲染框架：Remotion
🔒 时间真源：整数帧；秒数只作校对
🔒 实现基线：Composition + Sequence + useCurrentFrame + interpolate/spring + staticFile + Audio
🔒 转场基线：需要 Scene 转场时使用 TransitionSeries
❌ 禁止：改用 HyperFrames、Manim、MoviePy 或非帧驱动主时间轴
❌ 禁止：用 CSS animation、setTimeout 或播放历史状态驱动画面

本文件是给 Remotion 渲染 Agent 的实现合同。当前分镜 Skill 只产出本 spec，不创建 TSX、Remotion 项目或 MP4。


## 意图卡

> 所有 Scene 的画面、运动、转场与声音选择都必须回扣此卡。

- 视觉人格：[3 个可执行的视觉特征，不写“高级/温暖”等空词]
- 情绪-视觉映射：[逐字稿情绪拐点 → 速度/密度/色彩/运动方式]
- 视觉母题：[一个在 hook、主体、收尾至少出现 3 次的元素及变奏]
- 参考拆解：[具体借鉴点，不只写作品名]
- 反调预警：[本片最容易出现的视觉陷阱]


## 1. 视频基本盘

- 标题：[视频标题]
- 目的：[让谁记住什么、看完做什么]
- 受众：[职业/痛点/观看场景]
- 观众熟悉度：[已懂术语 / 不要预设他懂的内容]
- 平台：[抖音/B站/YouTube/小红书/其他]
- 目标时长：[X 秒，仅用于校对]
- 旁白总字数：[N]
- 核心信息：[≤12 字]
- 信息密度：[hook型/教程型/纪录型]
- 语气基调：[可执行描述 + 明确不要的风格]


## 2. 叙事结构

- 叙事节拍：[每段名称、全局帧区间、叙事职责]
- 情绪曲线：[开头 → 中段 → 收尾的变化]
- 视觉母题轨迹：[hook 首现 → 主体变奏 → 收尾回归]
- 音画关系：[BGM 是叙事性还是氛围性；至少一处音画错位点]
- 最空 Scene：[SNN，密度档位与作用]
- 最满 Scene：[SNN，密度档位与作用]


## 3. 表达手段

- 场景类型组合：[按顺序列 A-roll / B-roll / 产品展示 / 数据可视化 / 桥接]
- 主视觉策略：[实拍素材 / 截图 / CSS-SVG 构图 / 目标项目已有 React 组件]
- 字幕呈现：[常驻/分句/逐词；逐词无时间戳时必须标待转录]
- 关键词强调：[位置、字数、表现方式]
- 组件策略：[优先复用的已有组件；需新实现的 Scene 组件职责]
- 转场策略：[段落间与段内分别使用哪些 presentation；普通 cut 何时使用]
- 节奏基准：[平均每镜帧数、最短/最长镜头]
- 纯文字镜占比上限：≤20%


## 4. 视觉与渲染规范

### 🔒 Composition 合同

```yaml
id: [仅字母、数字、连字符]
width: [1920]
height: [1080]
fps: [30]
durationInFrames: [整数]
durationSecondsForReview: [durationInFrames / fps]
timelineMode: [Sequence | TransitionSeries]
defaultProps:
  [字段名]: [JSON 可序列化默认值]
```

总帧数计算：

- `Sequence` 模式：`durationInFrames = max(Scene.from + Scene.durationInFrames)`
- `TransitionSeries` 模式：`durationInFrames = Σ Scene.sequenceDurationInFrames - Σ Transition.durationInFrames`
- Overlay 不缩短总时长。
- 第一帧为 0；区间统一用左闭右开 `[startFrame, endFrameExclusive)`。

### 🔒 配色

- 背景底：[hex]
- 文字主色：[hex]
- 强调色：[hex]
- 弱化色：[hex]
- 卡片底色：[hex]
- 边框色：[hex]

### 🔒 字体

- display：[字体名 + fallback]
- subtitle：[字体名 + fallback]
- mono：[字体名 + fallback]
- 本地字体目标路径：[public/fonts/xxx.woff2 或 none]

### 🔒 图层

| 层级 | 内容 | z-index 范围 | 约束 |
|---|---|---:|---|
| L0 | 背景/底板 | 0-9 | [规则] |
| L1 | 主素材/主构图 | 10-29 | [规则] |
| L2 | 屏显文字/标注 | 30-49 | [规则] |
| L3 | 字幕 | 50-69 | [安全区] |
| L4 | 转场覆盖/SFX 闪光 | 70-89 | [出现条件] |

### 动效语言

- 常规入场：[如 12 帧 ease-out，位移 40px→0，透明度 0→1]
- 重点入场：[spring 的 duration/damping/stiffness/mass/overshootClamping]
- 常规退场：[帧数、属性、方向]
- 禁止项：[如 glow、过度 bounce、随机粒子]

### 确定性约束

- `useCurrentFrame()` 在 Scene Sequence 内按局部帧从 0 驱动动画。
- `interpolate()` 写明 input/output 与左右 clamp；`spring()` 写明 fps、duration 和物理参数。
- 禁止 CSS animation/transition、timer、wall-clock 时间、无固定种子的随机数。
- 下游先核对目标项目 Remotion 版本、现有组件和许可，再实现 spec。


## 5. 素材清单

> 本地素材统一规划到 Remotion 项目的 `public/`；下游通过 `staticFile()` 访问。此 spec 不执行下载或复制。

| ID | 状态 | 类型 | 来源/许可 | 原始信息 | public 目标路径 | 用途 | fallback |
|---|---|---|---|---|---|---|---|
| A01 | [已有/待获取] | [image/video/audio/font] | [来源] | [尺寸或时长] | `public/[path]` | [Scene] | [退化方案] |

素材硬检查：

- [ ] 所有“已有”路径真实存在
- [ ] 路径无用户机器绝对路径
- [ ] 远程 URL 已确认渲染环境可稳定访问，或已规划本地化
- [ ] 每个待获取素材都有 fallback


## 6. 分镜表

### 6.1 主时间轴台账

#### `Sequence` 模式填写

| Scene | startFrame (= Sequence from) | durationInFrames | endFrameExclusive | 秒数校对 | 旁白范围 |
|---|---:|---:|---:|---:|---|
| S01 | 0 | [N] | [startFrame + duration] | [X.XXs-X.XXs] | [原文起止] |

#### `TransitionSeries` 模式填写

| Scene | sequenceDurationInFrames | transitionOut kind | transitionOut duration | 派生 startFrame（非 prop） | endFrameExclusive |
|---|---:|---|---:|---:|---:|
| S01 | [N] | [transition/overlay/hard-cut] | [N；overlay/hard-cut 对总时长记 0] | 0 | [N] |
| S02 | [N] | [...] | [...] | [S01 startFrame + S01 duration - S01 transition duration] | [startFrame + duration] |

```text
Scene sequence 时长合计 = [N] 帧
Transition overlap 合计 = [N] 帧
Composition.durationInFrames = [N] - [N] = [N] 帧
秒数校对 = [N] / [fps] = [X.XX] 秒
```

### 6.2 Scene 详情

### Scene NN · [标签]

#### A. 时间与口播

- 🔒 帧区间：`startFrame=[N] durationInFrames=[N]`，全局区间 `[startFrame, endFrameExclusive)`
- 🔒 挂载模型：[`Sequence from={startFrame}` / `TransitionSeries.Sequence` 顺序位置；后者没有 `from` prop]
- 📐 秒数参考：[X.XXs-X.XXs]
- 🔒 旁白原文：[逐字稿原文]
- 🔒 口播有效区间：[全局帧 N-N]
- 🔒 屏显文字：[1-4 个关键词，或 null；不得照抄整句字幕]

#### B. React 组件契约

- 🔒 `component`：[PascalCase 名，如 `Scene01Hook`]
- 🔒 `props`：[JSON 可序列化输入；没有则 `{}`]
- 🔒 `assetBindings`：[素材 ID → `staticFile('path')` 或稳定远程 URL + fallback]
- 实现状态：[复用目标项目已有组件 / `[需渲染端实现]`]
- 主视觉职责：[视觉对象、面积、位置、信息载荷]
- 辅视觉职责：[对象、面积、位置，或 none]
- 背景职责：[颜色/素材/可确定求值的程序化图形]
- 字幕职责：[组件/数据/词级时间戳策略]
- 视觉母题对应：[意图卡中的哪次出现或变奏]
- 🎬 选择理由：[≤20 字，不能和前一镜重复]

#### C. 图层与素材

| Layer ID | z-index | 内容 | 素材 ID / public 路径 | staticFile 访问意图 | fallback |
|---|---:|---|---|---|---|
| L1-main | 10 | [内容] | [A01 / none] | [`staticFile('images/xxx.png')` / none] | [方案] |

#### D. 帧驱动动画

> `localFrame` 来自 Scene 所在 Sequence 内的 `useCurrentFrame()`，从 0 开始。只写参数合同，不写完整 TSX。

| 动画 ID | target.property | driver | localFrame / input | output | clamp / physics | 意图 |
|---|---|---|---|---|---|---|
| AN01 | `L1-main.opacity` | interpolate | `[0, 10]` | `[0, 1]` | `both` | [入场] |
| AN02 | `L1-main.translateY` | spring | `frame 0, duration [N]` | `[40px, 0px]` | `damping [N], stiffness [N], mass [N], overshootClamping [true/false]` | [落位] |

#### E. 转场

- 🔒 进入：[hard-cut / 由上一镜 transitionOut 决定]
- 🔒 离开 kind：[transition / overlay / hard-cut]
- presentation：[`fade()` / `slide()` / `wipe()` / `clockWipe()` / `iris()` / `none()` / custom]
- timing：[`linearTiming()` / `springTiming()` / none]
- durationInFrames：[N]
- overlay offset：[整数，仅 overlay；否则 none]
- overlay 边界校验：[duration 是正整数；offset 是有限整数；覆盖区间不早于 frame 0、不越过相邻 sequences 末端]
- 转场理由：[为什么需要；hard-cut 也写具体叙事原因]

#### F. 声音

| Track | public 目标 / src binding | global from | sceneLocalFrame | durationInFrames | trim | volume |
|---|---|---:|---:|---:|---|---|
| VO | [Axx / `staticFile('audio/voice.wav')`] | [N] | [N] | [N] | [before/after] | [0-1] |
| SFX | [名称 / `staticFile('audio/sfx.wav')` / none] | [N] | [N] | [N] | [none] | [0-1] |

#### G. 锁定与可调

- 🔒 不可变：[时间、文字、路径、配色、构图关系]
- 🎨 可调范围：[位置 ±px、动画 ±帧、scale 范围]
- ❌ 禁止：[本镜不应新增什么]
- 期待内容：[观众此刻理解什么]
- 期待效果：[观众此刻感受什么]

> 按以上 A-G 结构复制，直至最后一个 Scene。


## 7. 音频时间轴

> 下游使用 `Audio`（`@remotion/media`）；本地文件通过 `staticFile()` 引用。

| Track | public 目标路径 | src binding | from | durationInFrames | trimBefore | trimAfter | volume / 关键帧 | playbackRate | loop |
|---|---|---|---:|---:|---:|---:|---|---:|---|
| VO | `public/audio/voice.wav` | `staticFile('audio/voice.wav')` | 0 | [N] | 0 | [N] | 1 | 1 | false |
| BGM | `public/audio/bgm.mp3` | `staticFile('audio/bgm.mp3')` | 0 | [N] | 0 | [N] | `frames [0,N...] → [0,0.18...] clamp both` | 1 | [true/false] |
| SFX-01 | `public/audio/[file]` | `staticFile('audio/[file]')` | [N] | [N] | 0 | [N] | [0-1] | 1 | false |

- BGM 与 VO ducking：[全局帧区间 → volume 值]
- 音画错位点：[全局帧 + 设计意图]
- 尾帧处理：[BGM/VO/SFX 均不越过 Composition]


## 8. 参考与反例

- 正向参考：[具体作品/品牌/链接]
- 参考拆解：[构图/配色/运动/节奏中具体借鉴什么]
- 静态参考：[画面或版式参考]
- 反例（视觉）：[不要做成什么样]
- 反例（叙事）：[不要怎么讲]
- 反例（节奏）：[不要什么节奏]
- Remotion 实现反例：[如 CSS animation 代替帧驱动、虚构内置组件]


## 9. 开放问题

- [待用户确认的推断项]
- [缺失素材或许可]
- [需渲染端核对的目标项目组件/Remotion 版本]
- [需渲染端选库并复核许可的 3D/WebGL/图表能力]

### 交付硬门禁

- [ ] 所有帧值为整数；第一帧 0，尾帧为总帧数 - 1
- [ ] Scene 台账与 Composition 总帧数完全一致
- [ ] Transition 时长已从总时长扣除，Overlay 未扣除
- [ ] 每个 transition 小于前后 Scene 各自时长
- [ ] 每个 overlay 的 duration 为正整数、offset 为有限整数，且覆盖区间不越过相邻 sequences
- [ ] 每个 Scene 至少有一个可实现主视觉和明确组件契约
- [ ] 每个动画有 target、局部帧区间、参数，并可由当前帧独立求值
- [ ] 素材全部映射到 public 路径与 staticFile 访问意图
- [ ] 音频轨的 from、duration、trim、volume 齐全且不越界
- [ ] spec 未包含完整 TSX、项目脚手架或 MP4 渲染动作


## 10. 渲染反馈

### Remotion 渲染 Agent 回填

- Composition 实际参数：[id / width / height / fps / durationInFrames]
- 直接可执行的 Scene：[列表]
- 做过调整的 Scene：[改动 + 原因]
- 素材缺失或加载失败：[列表]
- 时间轴核算差异：[none 或说明]
- 理解偏差：[渲染端是否误解了某些指令]
- 最终验证：[Studio 预览 / 类型检查 / 实际渲染；由渲染 Agent 填写]

### 评分

| 维度 | 评分（1-5） | 备注 |
|---|---:|---|
| 组件契约完整性 | | |
| 帧动画可执行性 | | |
| 时间码一致性 | | |
| 无歧义程度 | | |
```

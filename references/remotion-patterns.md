---
name: remotion-patterns
description: Remotion 分镜规格的帧时间、场景装配、动画、素材、音频与转场契约。选择 Remotion 输出时必读；用于写给下游 Remotion 渲染 Agent 的 storyboard spec，不用于生成 TSX 或成片。
---

# Remotion 分镜规格模式

本文件只规定 `video-spec-remotion.md` 应如何描述可实现的 Remotion 视频。当前 Skill 在 spec 交接点停止：不创建 React/TSX，不初始化 Remotion 项目，不启动 Studio，不渲染 MP4。

## 1. 时间模型：帧是唯一真源

Remotion 的渲染结果由当前帧决定。spec 中所有可执行时间都写成整数帧，秒数只作人类校对。

```text
frame = round(seconds × fps)
seconds_display = frame / fps
endFrameExclusive = startFrame + durationInFrames
有效帧区间 = [startFrame, endFrameExclusive)
```

硬规则：

- 全片先锁定一个 `fps`；默认 30，不在 Scene 中改帧率。
- `startFrame`、`durationInFrames`、转场时长、音频裁切点均为非负整数。
- 第一帧是 0；最后一帧是 `durationInFrames - 1`。
- 连续硬切时，后一镜 `startFrame = 前一镜 startFrame + durationInFrames`。
- 不分别四舍五入大量小片段后再相加。先确定整片帧数，再按语义边界分配整数帧，余数在相邻镜吸收。
- 逐字稿时间码如是事实源，先整体换算成帧，再校对 Scene 边界；不得用浮点秒驱动下游动画。

## 2. 官方原语到 storyboard 的映射

| Remotion 原语 | spec 中负责描述什么 | 必须锁定的字段 |
|---|---|---|
| `<Composition>` | 可渲染视频入口 | `id`、`width`、`height`、`fps`、`durationInFrames` |
| `<Sequence>` | 普通 Scene 或局部图层的挂载区间 | `from=startFrame`、`durationInFrames`、`name`、是否预挂载 |
| `useCurrentFrame()` | Scene 内动画的本地帧驱动 | 局部帧区间、0 起点、所属 Sequence |
| `interpolate()` | 线性/分段数值映射 | input frames、output values、左右 clamp、easing 意图 |
| `spring()` | 物理感入场、强调、回弹 | local frame、fps、duration、damping、stiffness、mass、是否禁止 overshoot |
| `staticFile()` | `public/` 下的本地素材 URL | public 相对路径、素材类型、缺失时 fallback |
| `<Audio>` | 旁白、BGM、SFX | src、from、duration、trim、volume、是否 loop |
| `<TransitionSeries>` | 相邻 Scene 的转场或切点覆盖层 | sequence duration、presentation、timing、transition/overlay duration |

`Composition` 是全片注册合同，Scene 不各自注册 Composition。普通 Scene 用 `Sequence from={startFrame}` 定位；使用 `TransitionSeries` 时，主视觉 Scene 用没有 `from` prop 的 `TransitionSeries.Sequence` 顺序串联，`startFrame` 只保留为台账中的派生审计坐标。Scene 内字幕、装饰、局部音效仍可用嵌套 `Sequence`。

## 3. Scene 的局部帧语义

`useCurrentFrame()` 位于 `Sequence` 内时返回相对该 Sequence 起点的局部帧。spec 的动画区间因此默认写局部帧，不写全局帧。

每个动画声明必须包含：

```yaml
driver: interpolate | spring
target: [元素或图层 ID].[属性]
localFrameRange: [起始帧, 结束帧]
from: [数值或 CSS 值]
to: [数值或 CSS 值]
clamp: both | left | right | none
easingIntent: [linear / ease-out / physics / 其他明确意图]
```

### `interpolate()`

- 用于透明度、位移、缩放、旋转、裁切进度、数值与颜色的确定性映射。
- 默认写 `clamp: both`，避免超出输入区间后数值继续增长；确需外推时写原因。
- 多阶段动画把全部关键帧与输出值列在一行，例如 `[0, 8, 42, 50] → [0, 1, 1, 0]`。
- 同一视觉属性只指定一个驱动源，避免下游把 CSS animation 与帧计算叠加。

### `spring()`

- 用于有重量感的入场、卡片落位、轻微回弹，不用于所有淡入淡出。
- 必须传入 Composition 的 `fps`，帧值使用 Scene 局部帧。
- spec 必须给出 `durationInFrames`，使下游能将运动收敛点对齐镜头节拍。
- 禁止回弹时写 `overshootClamping: true`，或给足 damping；不要只写“丝滑”“弹一下”。

## 4. 两种主时间轴

### 模式 A：`Sequence` 硬切/叠层

适用于没有相邻 Scene 转场，或只在切点上叠一个不改变总时长的视觉层。

```text
compositionDuration = max(scene.startFrame + scene.durationInFrames)
```

Scene 可重叠，但重叠必须说明图层关系和音频关系；不得因误算而意外重叠。

### 模式 B：`TransitionSeries` 连续叙事

`TransitionSeries.Transition` 让前后两镜在转场期间同时出现，因此会缩短总时长：

```text
scene[0].startFrame = 0
scene[n+1].startFrame = scene[n].startFrame
                      + scene[n].sequenceDurationInFrames
                      - scene[n].transitionOut.durationInFrames

compositionDuration = sum(all sequenceDurationInFrames)
                    - sum(all Transition durations)
```

硬规则：

- Transition 只能放在相邻两个 `TransitionSeries.Sequence` 之间。
- `transitionOut.durationInFrames` 必须小于相邻两镜各自时长。
- Scene 的 `sequenceDurationInFrames` 包含参与转场重叠的帧。
- 口播和字幕必须按算出的全局 `startFrame` 对齐，不能把 sequence 时长直接累加当全片时长。
- `TransitionSeries.Overlay` 不缩短总时长；它覆盖切点，必须写 `durationInFrames` 与整数 `offset`。
- Overlay 的 `durationInFrames` 必须为正整数，`offset` 必须为有限整数；覆盖区间不得早于 frame 0，也不得越过相邻 sequences 的可用末端。
- 不在同一切点同时指定 Transition 和 Overlay；必须二选一。
- 转场 Scene 保持默认 absolute-fill；不要求 `layout="none"`。
- `springTiming()` 也必须记录其按 Composition fps 解析出的整数 duration，供总帧数核算；不能只写物理参数。

每个切点写清：

```yaml
afterScene: S03
kind: transition | overlay | hard-cut
presentation: fade() | slide() | wipe() | clockWipe() | iris() | custom | none()
timing: linearTiming() | springTiming()
durationInFrames: 15
offset: 0 # 仅 overlay
reason: [为何此处需要它]
```

## 5. Composition 合同

spec 的全局合同至少包含：

```yaml
id: [仅字母、数字、连字符]
width: [整数像素]
height: [整数像素]
fps: [正数]
durationInFrames: [按 Scene 与 transition 台账算出的整数]
timelineMode: Sequence | TransitionSeries
defaultProps: [只列 JSON 可序列化的数据字段；没有则写 none]
```

`defaultProps` 只描述内容和主题参数，不放函数、类或运行时对象。下游可自行选择是否加 schema；storyboard 不替其写实现。

## 6. 素材合同

所有本地静态素材统一规划到下游 Remotion 项目的 `public/`：

| spec 路径写法 | 下游访问意图 |
|---|---|
| `public/images/hero.png` | `staticFile('images/hero.png')` |
| `public/audio/voice.wav` | `staticFile('audio/voice.wav')` |
| `public/fonts/noto-sans-sc.woff2` | `staticFile('fonts/noto-sans-sc.woff2')` |

硬规则：

- 路径区分大小写，不用用户机器绝对路径。
- “已有”素材必须真实存在；否则标 `[待获取]` 并给可执行 fallback。
- 素材清单记录类型、尺寸/时长、许可/来源、用途、目标 public 路径。
- 远程 URL 只有在用户明确提供且渲染环境可稳定访问时才允许；默认落到 `public/`。
- storyboard 只规划素材路径，不复制、下载或转换素材。

## 7. 音频合同

当前官方媒体组件的 `Audio` 来自 `@remotion/media`；本地音频通过 `staticFile()` 引用。每条音轨均写：

```yaml
track: VO | BGM | SFX
publicTarget: public/audio/[file]
srcBinding: staticFile('audio/[file]')
from: [全局起始帧]
durationInFrames: [挂载时长]
trimBefore: [源文件裁掉的起始帧]
trimAfter: [源文件保留到的结束帧]
volume: [0-1，或逐帧关键点]
playbackRate: [默认 1]
loop: [true/false]
```

- 旁白是时间轴事实源时，Scene 边界服从旁白，不通过 `playbackRate` 粗暴挤压。
- BGM 音量包络写成帧关键点，供下游用 `interpolate()` 实现；左右均 clamp。
- SFX 的 `from` 是全局帧；若嵌套在 Scene Sequence，则同时给出 `sceneLocalFrame` 供核对。
- 音频区间不得越过 Composition；循环 BGM 也要用挂载时长封住尾帧。

## 8. 确定性与交接边界

下游实现必须能在任意帧独立求值。storyboard 禁止提出以下实现：

- `setTimeout`、`setInterval`、事件触发后累计状态；
- CSS `animation` / `transition` 充当主时间轴；
- `Date.now()`、无固定种子的随机数、依赖播放历史的动画；
- 用模糊秒数替代整数帧；
- 在 storyboard 中嵌入完整 TSX 组件或渲染命令。

允许的是结构化实现意图：元素层级、组件职责、帧区间、数值范围、素材路径、音频轨、转场 presentation 与 timing。渲染 Agent 据此创建 React 组件并渲染；本 Skill 不越过交接点。

## 9. 交付前计算检查

- [ ] `Composition.durationInFrames` 与时间轴公式一致。
- [ ] 所有 Scene 起止帧为整数且位于 Composition 内。
- [ ] Transition 模式已扣除全部 transition overlap；Overlay 未被扣时长。
- [ ] 每个 Scene 至少有一个可实现主视觉（素材、CSS/SVG 构图或明确的 React 组件职责）。
- [ ] 每个动画都有 target、局部帧区间、起止值和 clamp/physics 参数。
- [ ] 所有本地素材都有 `public/` 目标路径与 `staticFile()` 访问意图。
- [ ] VO、BGM、SFX 的全局帧定位完整，音量不是模糊形容词。
- [ ] spec 未包含完整 TSX、项目脚手架或 MP4 渲染动作。

## 官方真源

实现前按目标项目版本复核以下官方文档：

- [Composition](https://www.remotion.dev/docs/composition) 与 [Sequence](https://www.remotion.dev/docs/sequence)
- [useCurrentFrame](https://www.remotion.dev/docs/use-current-frame)、[interpolate](https://www.remotion.dev/docs/interpolate) 与 [spring](https://www.remotion.dev/docs/spring)
- [staticFile](https://www.remotion.dev/docs/staticfile) 与 [Audio](https://www.remotion.dev/docs/media/audio)
- [TransitionSeries](https://www.remotion.dev/docs/transitions/transitionseries)、[timings](https://www.remotion.dev/docs/transitions/timings) 与 [presentations](https://www.remotion.dev/docs/transitions/presentations)

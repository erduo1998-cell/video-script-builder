---
name: common-pitfalls
description: HyperFrames/Remotion 双后端的常见执行偏差与渲染反馈采集框架。经对应渲染 Agent 实际执行后回填，反向校准 SKILL.md 和模板。
---

# 常见执行偏差

> ⚠️ 本文件是活的——每轮 Agent B 渲染反馈后更新。

## 反馈采集机制

`video-spec-hf.md` 或 `video-spec-remotion.md` 的 §10 由对应渲染 Agent 填写。每次渲染完成后记录：

1. **直接可执行的 Scene**：哪些 Scene 的实现单元、素材绑定和框架专属动画契约无需修改即可落地
2. **需要修改的 Scene**：哪些 Scene 不得不改，具体改了什么
3. **理解偏差**：Agent B 是否误解了某些指令

## 已知偏差模式

### 模式 1: Agent 绕过 HyperFrames 手写 HTML

- **表现**: Agent 产出 video-spec-hf.md 后，又创建了 index.html 和 preview.html，将 spec 中各 Scene 的 HTML/CSS/GSAP 代码块拼接成独立文件，完全绕过 HyperFrames 框架。这样产出的 HTML 缺少 `class="clip"`、`window.__timelines` 注册、`data-composition-id` 等 HF 框架必需结构，无法正确渲染。
- **根因**: 旧版 skill (v1.1) 的 spec 中每个 Scene 都有完整可执行的 HTML/CSS/GSAP 代码块。Agent 看到可执行代码自然想"帮你做出来"，没有明确的 STOP 指令。
- **修复 (v1.2)**:
  1. spec 不再包含完整的 HTML 结构代码块，改为组件引用 + 素材路径 + GSAP 胶水指令，从根本上消除"可以直接拼成 HTML"的错觉
  2. SKILL.md §13 交付收尾硬 gate：禁止创建任何非 spec 文件（index.html / preview.html / compositions/）
  3. 每个 Scene 的 GSAP 代码块只写胶水逻辑（入场/停留/退场时间点和触发顺序），不写完整 tween——完整 tween 由组件自带

### 模式 2: 渲染 Agent 擅自更换 spec 绑定的框架

- **表现**: `video-spec-hf.md` 被改用 Remotion/Manim/MoviePy，或 `video-spec-remotion.md` 被改用 HyperFrames/GSAP。结果是组件契约、时间模型和转场计算失效。
- **根因**: spec 未声明渲染框架绑定，或下游把“支持双后端”误解为“单份 spec 可任意换后端”。
- **修复 (v1.2.1)**:
  1. 两个模板开篇分别声明 HyperFrames 或 Remotion，并明确禁止换框架。
  2. 文件名与时间模型绑定：HF 用秒和 `data-*`；Remotion 用整数帧和 `Sequence`。
  3. SKILL 与质量清单检查一次只交付一种 renderer-bound spec。
  4. 收尾明确交给对应框架渲染 Agent。

### 模式 3: 把双后端做成一份混合 spec

- **表现**: 同一 Scene 同时出现 `data-start`、GSAP、`from`、`durationInFrames` 和 `useCurrentFrame()`，让下游自行挑选。
- **根因**: 为了“复用”而把真正不同的执行契约压在同一层。
- **修复 (v1.4.0)**: 只复用意图、叙事、素材与 10 节语义骨架；模板、时间模型、动画语法和交接文件完全分开。迁移时重新生成目标 spec，不做字符串替换。

### 模式 4: Remotion 仍按秒或运行时时钟驱动

- **表现**: Scene 使用小数秒作为真源，动画依赖 CSS transition、`setTimeout`、`Date.now()` 或未设 seed 的随机数，seek/逐帧渲染不确定。
- **根因**: 把网页实时动画习惯带入离线逐帧渲染。
- **修复 (v1.4.0)**: 锁定 fps，所有 Scene 使用整数 `startFrame` / `durationInFrames`；普通 Sequence 才映射到 `from`，TransitionSeries 使用派生 startFrame 台账。动画只由 `useCurrentFrame()` 驱动，并写明 `interpolate()` clamp 或 `spring()` 参数。

### 模式 5: 忽略 Remotion 转场重叠

- **表现**: 把所有 Scene 帧数直接相加作为总时长，同时又使用 `TransitionSeries.Transition`，导致成片比目标短。
- **根因**: 不知道 transition 会让前后 Scene 同时渲染并缩短时间轴。
- **修复 (v1.4.0)**: 使用 `总帧数 = Σ sceneFrames - Σ transitionFrames`；Overlay 不扣时长；转场时长不得超过任一相邻 Scene。

## 渲染反馈评分维度

Agent B 拿到分镜脚本后，从以下维度评分（1-5）：

| 维度 | 1 分 | 5 分 |
|------|------|------|
| 实现单元完整性 | 多个 Scene 缺组件/props/素材绑定 | HF 组件可复核；Remotion 组件契约可实现 |
| 动画可执行性 | 动画语法或时间边界含糊 | HF 胶水或 Remotion 帧公式均精确 |
| 时间一致性 | Scene、转场、音频对不上 | 目标框架时间轴闭合 |
| 无歧义程度 | Agent B 不得不自己做大量判断 | Agent B 无需任何猜测 |

## 采集流程

```
Agent A 产出一个 renderer-bound spec
        ↓
对应框架 Agent B 实现/渲染，遇到问题记录
        ↓
Agent B 回填 §10 渲染反馈
        ↓
人工/Agent A 审阅反馈 → 更新本文件
        ↓
反馈驱动的改进 → 更新 SKILL.md / 模板
```

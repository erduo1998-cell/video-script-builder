---
name: common-pitfalls
description: 常见执行偏差 + 渲染反馈采集框架。经 Agent B 实际渲染后回填，反向校准 SKILL.md 和模板。v1.2 新增模式 1（Agent 绕过 HF 手写 HTML）。
---

# 常见执行偏差

> ⚠️ 本文件是活的——每轮 Agent B 渲染反馈后更新。

## 反馈采集机制

video-spec-hf.md 的 §10 渲染反馈区由 Agent B 填写。每次渲染完成后，人工/Agent B 从以下维度记录：

1. **直接可执行的 Scene**：哪些 Scene 的组件引用和 GSAP 无需修改直接跑通
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

### 模式 2: Agent B 收到 spec 但跳过 HyperFrames 用其他方式渲染

- **表现**: Agent B 收到 video-spec-hf.md 后，忽略其中的 `npx hyperframes add` 组件安装命令和 shader 转场引用，直接用 Remotion/Manim/MoviePy 等替代框架渲染，或手写独立 HTML+CSS+JS 绕过 HF 管线。结果：组件无法加载、shader 转场丢失、时间轴不同步。
- **根因**: spec 开篇使用泛用指令"请你按照以下 script，帮我生成一条视频"，未声明渲染框架绑定。Agent B 收到后认为自己可以选择任何渲染方式。
- **修复 (v1.2.1)**:
  1. spec 开篇改为"请你使用 HyperFrames 框架，按照以下分镜脚本帮我生成一条视频"，并附加 🔒 渲染框架绑定（管线说明 + 组件安装命令 + 禁止绕过 HF 声明）
  2. SKILL.md 与质量清单新增检查：spec 开篇必须声明 HF 渲染框架绑定
  3. quality-checklist.md 结构校验新增此项
  4. §13 交付收尾话术明确告知"不要将 spec 交给通用 Agent"

## 渲染反馈评分维度

Agent B 拿到分镜脚本后，从以下维度评分（1-5）：

| 维度 | 1 分 | 5 分 |
|------|------|------|
| 组件引用完整性 | 多个 Scene 缺组件名或安装命令 | 每个 Scene 的组件依赖可直接 `npx hyperframes add` |
| GSAP 可执行性 | 胶水逻辑语法错误或时间码对不上 | 所有入场/退场时间点精确，组件间衔接清晰 |
| 时间码一致性 | data-start/duration 与 GSAP position 多处不对齐 | 全部精确对齐 |
| 无歧义程度 | Agent B 不得不自己做大量判断 | Agent B 无需任何猜测 |

## 采集流程

```
Agent A 产出 video-spec-hf.md
        ↓
Agent B (HyperFrames) 渲染，遇到问题记录
        ↓
Agent B 回填 §10 渲染反馈
        ↓
人工/Agent A 审阅反馈 → 更新本文件
        ↓
反馈驱动的改进 → 更新 SKILL.md / 模板
```

---
name: video-script-spec-template
description: video-spec-hf.md 的 v1.4.0 HyperFrames 骨架模板。组件引用 + 素材路径 + GSAP 胶水编排，不含完整 HTML/CSS 代码块。保留 v1.3 的路径与执行契约，含共同 10 节语义骨架。
---

# Video Spec (HyperFrames) 模板 v1.4.0

复制下面整段，存成项目根目录的 `video-spec-hf.md`。每个 `[方括号]` 替换成真实内容。

交付前还必须把安装命令中的 `[component-name]` 替换为逐项真实组件名；最终 spec 不得保留 `<name>`、`<组件名>` 或任何模板占位。

---

```
请你使用 HyperFrames 框架，按照以下分镜脚本帮我生成一条视频。

🔒 渲染框架：HyperFrames
🔒 时间真源：秒；使用 data-start / data-duration
   管线：HTML + CSS + GSAP → Puppeteer 逐帧截图 → FFmpeg 合成 MP4
   组件安装：所有组件通过 `npx hyperframes add <name>` 安装
   交付物：index.html (composition) + 渲染后的 MP4 视频文件
❌ 禁止：绕过 HyperFrames 手写独立 HTML/CSS/JS 文件（无法通过 HF 管线渲染）
❌ 禁止：使用 Remotion、Manim、MoviePy 等其他渲染框架

以下是这条视频的分镜脚本和详细讲解。


## 意图卡

> 本片所有 Scene 的组件选型、转场决策、字幕切换均回扣此卡。§6 每个 Scene 必须能回答"这个选择和意图卡的哪一条对应"。

- 视觉人格: [3 个可执行的形容词]
- 情绪-视觉映射: [逐字稿情绪拐点 → 对应的视觉语言/速度/密度]
- 视觉母题: [一个在全片至少出现 3 次的视觉元素及出现位置]
- 参考拆解: [具体借鉴点，不是参考作品名]
- 反调预警: [本片最容易掉进的视觉陷阱]


## 1. 视频基本盘

- 标题：[视频标题]
- 目的：[这条视频要达成什么——让谁记住什么、看完去做什么]
- 受众：[目标观众——职业、痛点或关注点、在什么场景观看]
- 观众熟悉度：[观众已懂的术语，以及不要预设他懂的术语]
- 平台与时长：[在哪个平台播放、总时长多少]
- 画面规格：[画面比例、帧率]
- 输出：[文件格式、最终画质 high]
- 核心信息：[一句话 takeaway ≤ 12 字]
- 信息密度：[hook型/教程型/纪录型]
- 语气基调：[参考形象 + 明确不要的风格]


## 2. 叙事结构

- 叙事节拍：[每段名称、时间区间、职责]
- 情绪曲线：[开头、中段、收尾分别是什么情绪，要有变化方向]
- 音画关系：[BGM 是叙事性还是氛围性；至少一处音画错位点]
- 同质化反例：[视觉/叙事/节奏 至少各 1 条]


## 3. 表达手段

- 场景类型组合：[按出现顺序列出：A-roll / B-roll / 产品展示 / 数据可视化 / 桥接]
- 字幕呈现：[16 种 HF caption 组件之一，如 caption-pill-karaoke / caption-highlight / caption-weight-shift]
- 关键词强调：[HF 组件方式（caption-kinetic-slam / vfx-text-cursor）或标注"无"]
- 组件策略：[全片核心组件列表，如 vfx-iphone-device ×2, data-chart ×3, grain-overlay 全局]
- 转场风格：[段落间 shader 转场 / 段内 shader 转场，各 1-2 种]
- 节奏基准：[每镜平均时长、旁白总字数]
- 纯文字镜占比上限：≤ 20%


## 4. 视觉与渲染规范

### 🔒 全局参数

- 画幅：[data-width × data-height]
- 帧率：30fps
- 输出画质：high

### 🔒 配色系统

- 背景底：[hex]
- 文字主色：[hex]
- 强调色：[hex]
- 弱化色：[hex]
- 卡片底色：[hex]
- 卡片边框：[hex]

### 🔒 字体栈

- display: [font stack]
- subtitle: [font stack]
- caption: [font stack]
- mono: [font stack]

### 🔒 层级架构

- L0 底板: z-index: 0, data-track-index: 0
- L1 素材层: z-index: 10-20, data-track-index: 1
- L2 文字层: z-index: 30-50, data-track-index: 2
- L3 字幕: z-index: 60, data-track-index: 3

### 🔒 幕组件选择

- 字幕组件: [HF caption 组件名 如 `caption-pill-karaoke` / `caption-highlight` / `caption-weight-shift`]
- 底板 shader: [HF shader 背景 如 `vfx-liquid-background` / `grain-overlay`+`vignette` 组合 / 纯色`#0D0D0D` fallback]
- 转场组件: [段落间: `light-leak` / `cinematic-zoom`，段内: `transitions-dissolve` / `transitions-blur`]
- 装饰组件: [全局 `grain-overlay` / `shimmer-sweep` / `vignette` 或"无"]

### 排版防疲劳 7 规则生效确认

- [ ] 规则 1 (组件轮换)· [ ] 规则 2 (三镜一视)· [ ] 规则 3 (密度交替)
- [ ] 规则 4 (冷暖交替)· [ ] 规则 5 (时长不重复)· [ ] 规则 6 (2D/3D交替)· [ ] 规则 7 (开镜锚点)


## 5. 素材清单

### GitHub CC0 素材
| 素材名 | 仓库名 | 文件路径 | 用途 | 退化方案 |
|--------|--------|---------|------|---------|
| [素材描述] | [GitHub:user/repo] | [相对路径] | [用途] | [纯CSS方案] |

### HF 已捕获素材
| 素材名 | 捕获命令 | 用途 | 退化方案 |
|--------|---------|------|---------|
| [素材描述] | `npx hyperframes capture [url/query]` | [用途] | [纯CSS方案] |

### 本地素材
| 文件路径 | 来源 | 时长/尺寸 | 用途 |
|---------|------|----------|------|

### 待搜索素材
| 源平台 | 关键词（英文） | 用途 | 验收标准 |
|--------|-------------|------|---------|


## 6. 分镜表

### Scene NN · data-start="X.X" data-duration="Y.Y" · [标签]

- 🔒 类型: [A-roll / B-roll / 产品展示 / 数据可视化 / 桥接]
- 🔒 口播文字: [逐字稿原文]
- 🔒 屏显文字: [1-4个关键词，或"无"]

- 🔒 画面构成:
  - 主视觉: [HF组件名 或 素材文件路径] — 占据画面 [X]% 面积
  - 辅视觉: [HF组件名 或 素材文件路径 或 "无"]
  - 背景: [HF shader背景 或 素材视频 或 纯色 #hex]

- 🔒 组件依赖:
  | 组件名 | 安装命令 | 用途 |
  |--------|---------|------|
  | [component-name] | `npx hyperframes add [component-name]` | [描述] |

- 🔒 素材依赖:
  | 文件路径 | 来源 | 退化方案 |
  |---------|------|---------|
  | [assets/xxx.png] | [GitHub:repo-name 或 本地] | [纯CSS卡片 或 纯色占位] |

- 🔒 GSAP 编排: (仅写跨组件的胶水逻辑)
  ```javascript
  // 入场：组件可见性 + 素材淡入
  // 停留：字幕时间点
  // 退场：转场触发
  ```

- 🎬 为什么选这个组件: [≤20 字。不能和前一镜重复。写不出来 = 选错了]

- 🔒 转场进入: [shader转场名 或 CSS fallback]
- 🔒 转场离开: [shader转场名 或 CSS fallback]

- 🎨 可调范围: [duration ±Xs / position ±Xpx / scale ±X]

- 期待内容: [本镜传达的信息]
- 期待效果: [观众反应]

- 🔒 音效: [具体音效 + 时间码，或"无"]
- 🔒 字幕组件: [caption style name]

- 🔒 规则检查:
  - 屏显≠字幕: [✅ 或 ⚠️ 说明]
  - 组件计数: 本镜 [N] 个官方组件
  - 素材计数: 本镜 [N] 个素材
  - 防疲劳-动画轮换: [本镜 anim-XX ← 上一镜 anim-YY ✅/⚠️]
  - 防疲劳-密度交替: [本镜 稀疏/中等/密集 ← 上一镜 XX ✅/⚠️]
  - 防疲劳-冷暖调: [连续 N 镜暖/冷调]
  - 防疲劳-时长差: [本镜 X.Xs ← 上一镜 Y.Ys, 差值 Z.Zs ✅/⚠️]
  - bridge 累计占比: [X.X%]


## 7. 音频时间轴

- BGM: [文件名 + 起止时间]
- 旁白 TTS: [voice_id + speed + 总字数]
- 音效时间码:
  | 时间码 | 音效 | volume | 触发 Scene |
  |--------|------|--------|-----------|


## 8. 参考与反例

- 正向参考: [具体作品/品牌/链接]
- 静态参考: [画面构图/配色参考]
- 反例 (视觉): [不要做成什么样]
- 反例 (叙事): [不要怎么讲]
- 反例 (节奏): [不要什么节奏]


## 9. 开放问题

- [待用户确认的推断项]
- [待补充的缺失信息]


## 品味自检（不看规则看感受）

在交付 spec 前，快速过：

- [ ] 把所有 Scene 的缩略图拼成九宫格，颜色和密度有明显变化吗？（不是每格都差不多）
- [ ] 全片最安静的镜头是 [Scene N]，最吵闹的镜头是 [Scene N]，两者之间有足够距离吗？
- [ ] 关掉所有字幕，画面还能传达情绪吗？
- [ ] 金句到来之前，有没有给观众一个"吸气"的瞬间？[在 Scene N 和 Scene N 之间]
- [ ] 有没有哪个镜头想删掉？（如果有，考虑合并到相邻镜）


## 10. 渲染反馈（Agent B 填写）

### 直接可执行的 Scene
- [Scene NN: 无需修改]
- ...

### 需要修改的 Scene
- Scene NN: [改了什么、为什么]
- ...

### 理解偏差
- [Agent B 是否误解了某些指令]

### 评分

| 维度 | 评分 (1-5) | 备注 |
|------|-----------|------|
| 组件引用完整性 | | |
| GSAP 可执行性 | | |
| 时间码一致性 | | |
| 无歧义程度 | | |
```

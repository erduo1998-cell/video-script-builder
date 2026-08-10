# Video Script Builder 维护规则

- `SKILL.md` 每次只交付一个框架绑定 spec：HyperFrames 用 `video-spec-hf.md`，Remotion 用 `video-spec-remotion.md`；不得扩成渲染 Skill或生成混合双框架 spec。
- 修改组件名、CLI 命令或 HyperFrames 能力前，先核对官方仓库当前真源。
- 修改 Remotion API、包名或时间模型前，先核对 Remotion 官方文档/源码当前真源；分镜以整数帧为时间真源。
- `SKILL.md` 只放执行必需规则并保持在 500 行以内；教程放 README，细节放 `references/`。
- 修改框架路由或质量门控时，同步检查 `SKILL.md`、`references/quality-checklist.md`、两个模板和契约测试。
- 修改组件或转场名时，同步检查 catalog、recipes、GSAP patterns 和模板。
- 不提交私人逐字稿、客户素材、凭证、绝对用户路径或生成的视频文件。
- 提交前运行 `python3 scripts/check_repo.py` 和全部单元测试。

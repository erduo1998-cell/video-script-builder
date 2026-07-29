# Video Script Builder 维护规则

- `SKILL.md` 的唯一交付物始终是 `video-spec-hf.md`；不得扩成渲染 Skill。
- 修改组件名、CLI 命令或 HyperFrames 能力前，先核对官方仓库当前真源。
- `SKILL.md` 只放执行必需规则并保持在 500 行以内；教程放 README，细节放 `references/`。
- 修改质量门控时，同步检查 `SKILL.md`、`references/quality-checklist.md` 和模板。
- 修改组件或转场名时，同步检查 catalog、recipes、GSAP patterns 和模板。
- 不提交私人逐字稿、客户素材、凭证、绝对用户路径或生成的视频文件。
- 提交前运行 `python3 scripts/check_repo.py` 和全部单元测试。

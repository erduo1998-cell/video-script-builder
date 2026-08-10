# Contributing

感谢你改进 Video Script Builder。

## 适合提交的改动

- HyperFrames 官方组件/CLI 或 Remotion 官方 API 变化；
- 真实渲染后发现的 spec 歧义；
- 12 条硬校验之间的冲突案例；
- 更清楚的安装、示例或故障说明；
- 不改变职责边界的视觉导演方法。

## 提交前

1. 不要提交私人逐字稿、未公开素材、客户信息、Cookie、Token 或 API key。
2. HyperFrames 组件/命令与 Remotion API/包名必须回到各自官方仓库或文档核对，不能只凭旧 README 或记忆。
3. `SKILL.md` 只保留 Agent 每次执行真正需要的规则；教程和维护信息放在 README 或贡献文档。
4. 不要让 Skill 越界创建 composition 或渲染视频。
5. 运行：

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Pull Request 说明

请写清楚：

- 你观察到的真实问题；
- 原始事实源或最小复现；
- 为什么要修改 Skill 而不是只改 README；
- 运行了哪些验证；
- 是否改变 `video-spec-hf.md`、`video-spec-remotion.md` 或“一次只交付一个 spec”的输出契约。

from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class PublicRepositoryContractTests(unittest.TestCase):
    def test_repository_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check_repo.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_release_and_exactly_one_deliverable_contract(self) -> None:
        skill = read("SKILL.md")
        frontmatter = skill.split("---\n", 2)[1]
        self.assertIn("# Video Script Builder v1.4.0", skill)
        self.assertLess(len(skill.splitlines()), 500)
        self.assertEqual(
            set(re.findall(r"video-spec-[a-z0-9-]+\.md", frontmatter)),
            {"video-spec-hf.md", "video-spec-remotion.md"},
        )
        self.assertIn("exactly one", frontmatter.lower())
        self.assertIn("一次任务只输出表中一个文件", skill)
        self.assertIn("禁止生成“通用双框架 spec”", skill)

    def test_framework_routing_preserves_hyperframes_default(self) -> None:
        skill = read("SKILL.md")
        self.assertIn("用户明确指定 HyperFrames 或 Remotion", skill)
        self.assertIn("只找到一种现有 spec 时，沿用该 spec 的框架", skill)
        self.assertIn("同时找到两种 spec 或多个候选时", skill)
        self.assertIn("新项目且用户未指定时，为兼容旧行为直接默认 HyperFrames", skill)
        self.assertIn("按真实路径去重", skill)
        self.assertIn("模糊候选必须读取开篇框架声明", skill)
        self.assertIn("迁移模式", skill)
        self.assertIn("不要就地替换框架名", skill)
        self.assertIn("框架继承不等于允许修改已有文件", skill)
        self.assertIn("你是想在这个基础上改，还是新开一份？", skill)
        self.assertIn("在回答前不写文件", skill)
        self.assertIn("不得覆盖现有 spec", skill)
        self.assertIn("不得残留 `<name>`、`<组件名>`", skill)

    def test_templates_share_semantics_but_not_execution_tokens(self) -> None:
        hf = read("templates/video-script-spec-template.md")
        remotion = read("templates/video-script-spec-remotion-template.md")
        expected = [
            ("1", "视频基本盘"),
            ("2", "叙事结构"),
            ("3", "表达手段"),
            ("4", "视觉与渲染规范"),
            ("5", "素材清单"),
            ("6", "分镜表"),
            ("7", "音频时间轴"),
            ("8", "参考与反例"),
            ("9", "开放问题"),
        ]
        for template in [hf, remotion]:
            headings = re.findall(r"(?m)^## (\d+)\. ([^\n]+)$", template)
            self.assertEqual(headings[:9], expected)
            self.assertEqual(len(headings), 10)
            self.assertEqual(headings[-1][0], "10")
            self.assertIn("渲染反馈", headings[-1][1])

        self.assertIn("🔒 渲染框架：HyperFrames", hf)
        self.assertIn("npx hyperframes add", hf)
        self.assertIn("data-start", hf)
        self.assertIn("data-duration", hf)
        self.assertIn("GSAP", hf)
        for token in ["useCurrentFrame", "durationInFrames", "<Composition", "staticFile("]:
            self.assertNotIn(token, hf)

        self.assertIn("🔒 渲染框架：Remotion", remotion)
        for token in [
            "Composition",
            "Sequence",
            "useCurrentFrame",
            "interpolate",
            "spring",
            "staticFile",
            "Audio",
            "TransitionSeries",
            "startFrame",
            "durationInFrames",
        ]:
            self.assertIn(token, remotion)
        for token in ["npx hyperframes add", "data-start", "data-duration", "GSAP"]:
            self.assertNotIn(token, remotion)

    def test_remotion_timeline_contract_is_frame_safe(self) -> None:
        reference = read("references/remotion-patterns.md")
        template = read("templates/video-script-spec-remotion-template.md")
        combined = reference + template
        self.assertIn("<Sequence>", combined)
        self.assertIn("TransitionSeries.Sequence", reference)
        self.assertIn("没有 `from` prop", reference)
        self.assertIn("startFrame` 只保留为台账中的派生审计坐标", reference)
        self.assertIn(
            "compositionDuration = sum(all sequenceDurationInFrames)", reference
        )
        self.assertIn("- sum(all Transition durations)", reference)
        self.assertIn("Overlay 不缩短总时长", combined)
        self.assertIn("Transition 时长已从总时长扣除，Overlay 未扣除", template)
        self.assertIn('不要求 `layout="none"`', reference)
        self.assertIn("没有 `from` prop", reference)
        self.assertNotIn("S01 from +", template)
        self.assertNotIn("[from + duration]", template)
        self.assertIn("duration 是正整数；offset 是有限整数", template)
        self.assertIn("覆盖区间不得早于 frame 0", reference)
        self.assertIn("staticFile('audio/voice.wav')", template)
        self.assertIn("srcBinding: staticFile('audio/[file]')", reference)
        for forbidden in ["setTimeout", "setInterval", "Date.now()"]:
            self.assertIn(forbidden, reference)

    def test_twelve_gates_and_backend_checklist_exist(self) -> None:
        skill = read("SKILL.md")
        match = re.search(r"## 12 条硬阻断\n(?P<section>.*?)(?=\n## )", skill, re.S)
        self.assertIsNotNone(match)
        assert match is not None
        gates = [
            int(value)
            for value in re.findall(r"(?m)^(\d+)\. \*\*", match.group("section"))
        ]
        self.assertEqual(gates, list(range(1, 13)))

        checklist = read("references/quality-checklist.md")
        for heading in range(1, 13):
            self.assertRegex(checklist, rf"(?m)^## {heading}\. ")
        for token in [
            "GSAP",
            "HyperFrames",
            "useCurrentFrame()",
            "interpolate()",
            "spring()",
            "TransitionSeries",
            "一次只检查并交付一种 spec",
        ]:
            self.assertIn(token, checklist)

    def test_release_surfaces_are_dual_backend(self) -> None:
        zh = read("README.md")
        en = read("README.en.md")
        for text in [zh, en]:
            for token in [
                "1.4.0",
                "HyperFrames",
                "Remotion",
                "video-spec-hf.md",
                "video-spec-remotion.md",
            ]:
                self.assertIn(token, text)
        self.assertIn("一次任务只会交付一个", zh)
        self.assertIn("exactly one", en)
        self.assertIn("不是视频渲染器", zh)
        self.assertIn("does **not** render video", en)

        agents = read("agents/openai.yaml")
        self.assertIn("HyperFrames or Remotion", agents)
        rules = read("AGENTS.md")
        self.assertIn("video-spec-hf.md", rules)
        self.assertIn("video-spec-remotion.md", rules)
        self.assertNotIn("唯一交付物始终是 `video-spec-hf.md`", rules)
        pitfalls = read("references/common-pitfalls.md")
        self.assertIn("普通 Sequence 才映射到 `from`", pitfalls)
        self.assertIn("TransitionSeries 使用派生 startFrame 台账", pitfalls)
        self.assertNotIn("所有 Scene 使用整数 `from` / `durationInFrames`", pitfalls)

    def test_audio_example_keeps_chinese_transcription(self) -> None:
        audio = read("references/audio-workflow.md")
        self.assertIn("--model small --language zh", audio)
        self.assertNotIn("--model small.en", audio)
        self.assertIn('@remotion/media', audio)
        self.assertIn("staticFile", audio)


if __name__ == "__main__":
    unittest.main()

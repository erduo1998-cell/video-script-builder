from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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

    def test_template_declares_hyperframes_and_ten_sections(self) -> None:
        template = (
            ROOT / "templates/video-script-spec-template.md"
        ).read_text(encoding="utf-8")
        self.assertIn("🔒 渲染框架：HyperFrames", template)
        for section in range(1, 11):
            self.assertRegex(template, rf"## {section}\.")

    def test_audio_example_keeps_chinese_transcription(self) -> None:
        audio = (ROOT / "references/audio-workflow.md").read_text(encoding="utf-8")
        self.assertIn("--model small --language zh", audio)
        self.assertNotIn("--model small.en", audio)


if __name__ == "__main__":
    unittest.main()

"""Executes the AI CLI subprocess with the assembled prompt."""

import subprocess
import sys
from pathlib import Path


def run_ai(backend: str, prompt: str, project_dir: Path) -> int:
    """Execute the AI CLI with the assembled prompt.

    Creates the project directory if it doesn't exist, then runs the chosen
    AI CLI inside it.

    Args:
        backend: Which CLI to use (claude, gemini, codex).
        prompt: The assembled prompt string.
        project_dir: Path to the project directory to scaffold into.

    Returns:
        The subprocess return code.
    """
    project_dir.mkdir(parents=True, exist_ok=True)

    if backend == "claude":
        cmd = ["claude", "-p", "--dangerously-skip-permissions", prompt]
    elif backend == "gemini":
        cmd = ["gemini", "-p", prompt, "-y"]
    elif backend == "codex":
        cmd = [
            "codex",
            "exec",
            "--dangerously-bypass-approvals-and-sandbox",
            prompt,
        ]
    else:
        print(f"Unknown backend: {backend}", file=sys.stderr)
        return 1

    result = subprocess.run(cmd, cwd=project_dir)
    return result.returncode

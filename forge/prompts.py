"""Interactive question flow for gathering project details."""

import re

import questionary

STACK_CHOICES = [
    questionary.Choice("Next.js + React (frontend or fullstack)", value="nextjs"),
    questionary.Choice("Python API (FastAPI)", value="fastapi"),
    questionary.Choice("Both (Next.js frontend + FastAPI backend)", value="both"),
]


def _validate_project_name(name: str) -> bool | str:
    """Validate that the project name is a valid directory name."""
    if not name.strip():
        return "Project name cannot be empty."
    if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9._-]*$", name):
        return (
            "Must start with a letter/number and contain only"
            " letters, numbers, dots, hyphens, or underscores."
        )
    return True


def collect_answers() -> dict[str, str | bool]:
    """Run the interactive prompt flow and return answers as a dict."""
    name = questionary.text(
        "Project name:",
        validate=_validate_project_name,
    ).ask()
    if name is None:
        raise SystemExit(0)

    stack = questionary.select(
        "What are we building?",
        choices=STACK_CHOICES,
    ).ask()
    if stack is None:
        raise SystemExit(0)

    description = questionary.text("Brief description:").ask()
    if description is None:
        raise SystemExit(0)

    docker = questionary.confirm("Include Docker setup?", default=True).ask()
    if docker is None:
        raise SystemExit(0)

    extra = questionary.text(
        "Any extra instructions? (optional, press Enter to skip):",
        default="",
    ).ask()
    if extra is None:
        raise SystemExit(0)

    return {
        "name": name.strip(),
        "stack": stack,
        "description": description.strip(),
        "docker": docker,
        "extra": extra.strip(),
    }

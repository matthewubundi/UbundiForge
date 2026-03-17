"""Assembles the prompt string that gets piped into the AI CLI."""

STACK_LABELS = {
    "nextjs": "Next.js + React",
    "fastapi": "Python API (FastAPI)",
    "both": "Next.js frontend + FastAPI backend (monorepo)",
}


def build_prompt(
    answers: dict,
    conventions: str,
    claude_md_template: str | None = None,
) -> str:
    """Build the full prompt from user answers, conventions, and optional CLAUDE.md template.

    Args:
        answers: Dict with keys: name, stack, description, docker, extra.
        conventions: Contents of the conventions.md file.
        claude_md_template: Optional CLAUDE.md scaffold template content.

    Returns:
        The assembled prompt string.
    """
    stack_label = STACK_LABELS.get(answers["stack"], answers["stack"])
    docker_str = "Yes" if answers["docker"] else "No"
    extra = answers.get("extra", "").strip() or "None"

    docker_instruction = ""
    if answers["docker"]:
        docker_instruction = "- Include Docker setup (Dockerfile + docker-compose.yml)\n"

    if claude_md_template:
        claude_md_instruction = (
            "- Include a CLAUDE.md at the project root using the template below "
            "as the base structure. Adapt the placeholders to match this project's "
            "actual name, stack, and structure.\n"
        )
    else:
        claude_md_instruction = (
            "- Include a CLAUDE.md at the root that describes this project "
            "for AI coding assistants\n"
        )

    prompt = f"""\
You are scaffolding a new project. Create the full project in the current directory.

PROJECT DETAILS:
- Name: {answers["name"]}
- Stack: {stack_label}
- Description: {answers["description"]}
- Docker: {docker_str}

CONVENTIONS (follow these exactly):
{conventions}

INSTRUCTIONS:
- Create a complete, working project structure with all config files
{claude_md_instruction}\
- Include appropriate .gitignore, .env.example, README.md
{docker_instruction}\
- Initialize with sensible defaults — the user should be able to run the project immediately
- Follow the conventions above strictly for all styling, structure, and coding patterns
- Initialize a git repository and make an initial commit

EXTRA INSTRUCTIONS FROM USER:
{extra}"""

    if claude_md_template:
        prompt += f"""

CLAUDE.MD TEMPLATE (use this as the base for the project's CLAUDE.md):
{claude_md_template}"""

    return prompt

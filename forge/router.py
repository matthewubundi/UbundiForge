"""AI backend routing — picks the best CLI tool for the job."""


def pick_backend(stack: str, override: str | None = None) -> str:
    """Pick the AI CLI backend based on stack selection.

    Args:
        stack: The stack identifier (nextjs, fastapi, both).
        override: Force a specific backend regardless of routing logic.

    Returns:
        The backend name (claude, gemini, or codex).
    """
    if override:
        return override

    routing = {
        "nextjs": "gemini",
        "fastapi": "claude",
        "both": "claude",
    }
    return routing.get(stack, "claude")

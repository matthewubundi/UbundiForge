"""Tests for the AI routing logic."""

from forge.router import pick_backend


def test_nextjs_routes_to_gemini():
    assert pick_backend("nextjs") == "gemini"


def test_fastapi_routes_to_claude():
    assert pick_backend("fastapi") == "claude"


def test_both_routes_to_claude():
    assert pick_backend("both") == "claude"


def test_unknown_stack_defaults_to_claude():
    assert pick_backend("unknown") == "claude"


def test_override_takes_precedence():
    assert pick_backend("nextjs", override="codex") == "codex"
    assert pick_backend("fastapi", override="gemini") == "gemini"


def test_override_none_uses_routing():
    assert pick_backend("nextjs", override=None) == "gemini"

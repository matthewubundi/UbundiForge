"""Forge CLI — entry point."""

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel

from forge import __version__
from forge.config import SUPPORTED_BACKENDS, check_backend_installed
from forge.conventions import load_claude_md_template, load_conventions
from forge.prompt_builder import build_prompt
from forge.prompts import collect_answers
from forge.router import pick_backend
from forge.runner import run_ai

app = typer.Typer(add_completion=False)
console = Console()


@app.callback(invoke_without_command=True)
def main(
    use: Annotated[
        str | None,
        typer.Option("--use", help="Override AI routing (claude, gemini, or codex)."),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Print the assembled prompt without executing."),
    ] = False,
    version: Annotated[
        bool,
        typer.Option("--version", "-v", help="Show version and exit."),
    ] = False,
) -> None:
    """Forge — Ubundi Project Scaffolder. Scaffold projects with AI + your conventions."""
    if version:
        console.print(f"forge {__version__}")
        raise typer.Exit()

    if use and use not in SUPPORTED_BACKENDS:
        backends = ", ".join(SUPPORTED_BACKENDS)
        console.print(f"[red]Unknown backend '{use}'. Choose from: {backends}[/red]")
        raise typer.Exit(1)

    console.print(Panel("[bold]Forge[/bold] -- Ubundi Project Scaffolder", style="cyan"))

    # Collect answers
    answers = collect_answers()

    # Pick backend
    backend = pick_backend(answers["stack"], override=use)
    console.print(f"\n[dim]Using {backend} ({answers['stack']} project detected)[/dim]")

    # Check backend is installed
    if not check_backend_installed(backend):
        console.print(
            f"\n[red bold]{backend}[/red bold] [red]is not installed or not on PATH.[/red]"
            f"\n[dim]Install it and try again, or use --use to pick a different backend.[/dim]"
        )
        raise typer.Exit(1)

    # Load conventions and CLAUDE.md template
    conventions = load_conventions()
    console.print("[dim]Loaded conventions from ~/.forge/conventions.md[/dim]")

    claude_md_template = load_claude_md_template()
    if claude_md_template:
        console.print("[dim]Loaded CLAUDE.md template from ~/.forge/claude-md-template.md[/dim]")

    # Build prompt
    prompt = build_prompt(answers, conventions, claude_md_template)

    if dry_run:
        console.print("\n[bold]Assembled prompt:[/bold]\n")
        console.print(prompt)
        raise typer.Exit()

    # Run
    project_dir = Path.cwd() / answers["name"]
    console.print(f"[dim]Handing off to {backend}...[/dim]\n")
    returncode = run_ai(backend, prompt, project_dir)

    if returncode == 0:
        console.print(f"\n[green bold]Done![/green bold] Project created at [bold]{project_dir}[/bold]")  # noqa: E501
    else:
        console.print(f"\n[red]{backend} exited with code {returncode}.[/red]")
        raise typer.Exit(returncode)

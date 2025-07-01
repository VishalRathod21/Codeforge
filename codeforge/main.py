import json
import typer
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.prompt import Confirm
import importlib.metadata

from codeforge.llm_agent import generate_project_structure
from codeforge.structure_generator import create_project_structure

# Version
__version__ = importlib.metadata.version('codeforge')

app = typer.Typer(
    help="""AI-powered project structure generator
    
    Generate complete project structures with a single command using AI.
    """,
    add_completion=False,
    no_args_is_help=True
)
console = Console()

# Version command
@app.command()
def version():
    """Show the current version of CodeForge"""
    console.print(f"[bold]CodeForge[/] version [cyan]{__version__}[/]")
    console.print("\n[dim]AI-powered project structure generator[/]")

# Add version flag
app.callback(invoke_without_command=True)
def main(version: bool = typer.Option(
    None, 
    "--version", 
    "-v", 
    help="Show version and exit.",
    is_eager=True
)):
    """CodeForge - AI-powered project structure generator"""
    if version:
        version()
        raise typer.Exit()

@app.command()
def create(
    project_description: str = typer.Argument(
        ...,
        help="Description of the project to generate (e.g., 'A Python web app with FastAPI and React')"
    ),
    output_dir: str = typer.Option(
        ".",
        "--output",
        "-o",
        help="Output directory for the project (default: current directory)",
        show_default=True
    ),
    template: Optional[str] = typer.Option(
        None,
        "--template",
        "-t",
        help="Project template to use (see available templates with 'list-templates')",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing files without asking for confirmation"
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Enable debug mode to show detailed error information"
    ),
):
    """
    Generate a complete project structure based on your description.
    
    Examples:
        codeforge create "A Python web app with FastAPI and React"
        codeforge create "A data science project with PyTorch" --output ./my-project
        codeforge create "A CLI tool in Python" --template cli
    """
    try:
        output_path = Path(output_dir).resolve()
        
        if debug:
            console.print("[yellow]Debug mode enabled[/]")
            console.print(f"Output directory: {output_path}")
            console.print(f"Template: {template or 'default'}")
            console.print(f"Force overwrite: {force}")
        
        console.print(f"\n[bold blue]🤖 Generating project structure for:[/] {project_description}")
        
        # Generate project structure using LLM
        try:
            structure = generate_project_structure(project_description, template)
        except Exception as e:
            if debug:
                import traceback
                console.print("\n[red]Debug information:[/]")
                console.print(traceback.format_exc())
            console.print(f"[bold red]❌ Error generating project structure: {str(e)}[/]")
            raise typer.Exit(1)
        
        if not structure:
            console.print("[bold red]❌ Failed to generate project structure: Empty response from API[/]")
            raise typer.Exit(1)
            
        if debug:
            console.print("\n[green]Generated structure:[/]")
            console.print(json.dumps(structure, indent=2))
            
        # Create the project structure
        try:
            created_files = create_project_structure(structure, output_path, force=force)
            
            if not created_files:
                console.print("[yellow]⚠️  No files were created (they might already exist)[/]")
            else:
                console.print(f"\n[bold green]✅ Successfully created {len(created_files)} files:[/]")
                for file in created_files[:10]:  # Show first 10 files to avoid flooding
                    console.print(f"  - {file}")
                if len(created_files) > 10:
                    console.print(f"  ... and {len(created_files) - 10} more")
                
                console.print("\n[bold]🎉 Project generated successfully![/]")
                
        except Exception as e:
            if debug:
                import traceback
                console.print("\n[red]Debug information:[/]")
                console.print(traceback.format_exc())
            console.print(f"[bold red]❌ Error creating project structure: {str(e)}[/]")
            raise typer.Exit(1)
        
    except typer.Exit:
        raise
    except Exception as e:
        console.print(f"[bold red]❌ Unexpected error: {str(e)}[/]")
        if debug:
            import traceback
            console.print("\n[red]Debug information:[/]")
            console.print(traceback.format_exc())
        raise typer.Exit(1)

@app.command()
def list_templates():
    """List all available project templates
    
    Examples:
        codeforge list-templates
    """
    console.print("\n[bold]Available templates:[/]")
    console.print("  - default (No specific template)")
    console.print("  - web (Web application template)")

def main():
    """Main entry point"""
    app()

if __name__ == "__main__":
    main()

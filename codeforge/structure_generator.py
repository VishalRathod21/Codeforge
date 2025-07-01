import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from rich.console import Console

console = Console()

def create_file(file_path: Path, content: str, force: bool = False) -> bool:
    """
    Create a file with the given content
    
    Args:
        file_path: Path to the file to create
        content: File content
        force: Overwrite existing file if True
        
    Returns:
        bool: True if file was created, False otherwise
    """
    try:
        if file_path.exists() and not force:
            console.print(f"[yellow]⚠️  File already exists, skipping: {file_path}[/]")
            return False
            
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True
    except Exception as e:
        console.print(f"[red]❌ Error creating file {file_path}: {str(e)}[/]")
        return False

def create_directory(dir_path: Path, force: bool = False) -> bool:
    """
    Create a directory
    
    Args:
        dir_path: Path to the directory to create
        force: Remove existing directory if True
        
    Returns:
        bool: True if directory was created, False otherwise
    """
    try:
        if dir_path.exists():
            if force:
                shutil.rmtree(dir_path)
            else:
                console.print(f"[yellow]⚠️  Directory already exists, skipping: {dir_path}[/]")
                return False
                
        dir_path.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        console.print(f"[red]❌ Error creating directory {dir_path}: {str(e)}[/]")
        return False

def create_project_structure(structure: Dict[str, Any], base_path: Path, force: bool = False) -> List[str]:
    """
    Create a project structure from a JSON definition
    
    Args:
        structure: Project structure definition
        base_path: Base directory to create the structure in
        force: Overwrite existing files/directories if True
        
    Returns:
        List of created files and directories
    """
    created = []
    project_name = structure.get('project_name', 'my_project')
    project_path = base_path / project_name
    
    # Create project root directory
    if create_directory(project_path, force=force):
        created.append(str(project_path))
    
    # Process each item in the structure
    for item in structure.get('structure', []):
        item_path = project_path / item['name']
        
        if item['type'] == 'directory':
            if create_directory(item_path, force=force):
                created.append(str(item_path))
                
            # Process children recursively
            for child in item.get('children', []):
                child_path = item_path / child['name']
                if child['type'] == 'file':
                    if create_file(child_path, child.get('content', ''), force=force):
                        created.append(str(child_path))
                elif child['type'] == 'directory':
                    if create_directory(child_path, force=force):
                        created.append(str(child_path))
                        
        elif item['type'] == 'file':
            if create_file(item_path, item.get('content', ''), force=force):
                created.append(str(item_path))
    
    return created

def load_template(template_name: str) -> Optional[Dict[str, Any]]:
    """
    Load a project template
    
    Args:
        template_name: Name of the template to load
        
    Returns:
        Template structure or None if not found
    """
    try:
        template_path = Path(__file__).parent / "templates" / f"{template_name}_template.json"
        with open(template_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        console.print(f"[red]❌ Error parsing template {template_name}: {str(e)}[/]")
        return None

if __name__ == "__main__":
    # Test the structure generator
    test_structure = {
        "project_name": "test_project",
        "structure": [
            {
                "type": "file",
                "name": "README.md",
                "content": "# Test Project\n\nThis is a test project."
            },
            {
                "type": "directory",
                "name": "src",
                "children": [
                    {
                        "type": "file",
                        "name": "__init__.py",
                        "content": ""
                    },
                    {
                        "type": "file",
                        "name": "main.py",
                        "content": "def main():\n    print(\"Hello, World!\")\n\nif __name__ == \"__main__\":\n    main()"
                    }
                ]
            }
        ]
    }
    
    print("Testing project structure creation...")
    created = create_project_structure(test_structure, Path("./test_output"), force=True)
    print(f"Created {len(created)} files/directories")
    for item in created:
        print(f"- {item}")

import os
import json
import requests
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
# Supported models: llama3-70b-8192, llama3-8b-8192, mixtral-8x7b-32768
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3-70b-8192")

def load_prompt_template(template_name: str = "base") -> str:
    """Load prompt template from file"""
    try:
        template_path = Path(__file__).parent / "prompts" / f"{template_name}_prompt.txt"
        with open(template_path, "r") as f:
            template = f.read().strip()
        # Verify the template has the correct format
        if "{description}" not in template:
            raise ValueError(f"Template {template_name} is missing required {{description}} placeholder")
        return template
    except FileNotFoundError:
        # Fallback to default prompt if template not found
        return """You are an expert software architect. Your task is to generate a project structure 
based on the user's description. Respond with a JSON object containing a 'structure' 
field with the following format:

{{
    "project_name": "string",
    "structure": [
        {{
            "type": "file" or "directory",
            "name": "string",
            "content": "string"  // Required for files
            // For directories, include a "children" array instead of "content"
        }}
    ]
}}

The project description is: {description}"""

def generate_project_structure(description: str, template: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a project structure using the Groq API
    
    Args:
        description: Project description
        template: Optional template to use
        
    Returns:
        Dict containing the project structure
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    
    # Load the appropriate prompt template
    prompt_template = load_prompt_template(template or "base")
    prompt = prompt_template.format(description=description)
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": """You are a helpful assistant that generates project structures in JSON format. 
            The response must be a valid JSON object with a 'project_name' field and a 'structure' field.
            The 'structure' should be an array of file and directory objects.
            Each file object must have 'type' (file/directory), 'name', and 'content' (for files) or 'children' (for directories)."""},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000,
        "response_format": {"type": "json_object"}
    }
    
    try:
        print(f"Sending request to Groq API with model: {DEFAULT_MODEL}")
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        # Extract the JSON response
        result = response.json()
        print(f"Raw API response: {json.dumps(result, indent=2)}")
        
        if "choices" not in result or not result["choices"]:
            raise ValueError("No choices in API response")
            
        message = result["choices"][0]["message"]
        content = message.get("content", "")
        
        if not content:
            raise ValueError("Empty content in API response")
            
        print(f"Raw content from API: {content}")
        
        # Parse the JSON content
        try:
            parsed = json.loads(content)
            # Validate the structure
            if not isinstance(parsed, dict):
                raise ValueError("Response is not a JSON object")
            if "project_name" not in parsed:
                raise ValueError("Response is missing 'project_name' field")
            if "structure" not in parsed:
                raise ValueError("Response is missing 'structure' field")
            if not isinstance(parsed["structure"], list):
                raise ValueError("'structure' must be an array")
                
            return parsed
            
        except json.JSONDecodeError as e:
            print(f"Failed to parse as JSON: {e}")
            # Try to extract JSON from markdown code block if present
            import re
            json_match = re.search(r'```(?:json)?\s*(\{.*\})\s*```', content, re.DOTALL)
            if json_match:
                print("Found JSON in markdown code block, attempting to parse...")
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError as e2:
                    print(f"Failed to parse JSON from markdown: {e2}")
                    
            print(f"Raw content that failed to parse: {content}")
            raise ValueError(f"Failed to parse LLM response as JSON: {str(e)}")
            
    except requests.exceptions.RequestException as e:
        error_msg = f"API request failed: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_msg += f"\nResponse: {e.response.text}"
        raise Exception(error_msg)
    except Exception as e:
        raise Exception(f"Error generating project structure: {str(e)}")

if __name__ == "__main__":
    # Test the function
    test_description = "A simple Python web application using Flask"
    print("Testing project structure generation...")
    structure = generate_project_structure(test_description)
    print(json.dumps(structure, indent=2))

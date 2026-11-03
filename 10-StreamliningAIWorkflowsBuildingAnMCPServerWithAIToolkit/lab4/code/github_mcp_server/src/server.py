import json
import random
import os
import platform
import subprocess
from pathlib import Path
from mcp.server.mcpserver import MCPServer

# Initialize the MCP server
server = MCPServer("github_mcp_server")

@server.tool()
async def get_weather(location: str) -> str:
    """Get weather for a location.

    Args:
        location: Location to get weather for, e.g., city name, state, or coordinates
    
    """
    if not location:
        return "Location is required."
    
    # mock weather data
    conditions = [ "Sunny", "Rainy", "Cloudy", "Snowy" ]
    weather = {
        "location": location,
        "temperature": f"{random.randint(10, 90)}°F",
        "condition": random.choice(conditions),
    }
    return json.dumps(weather, ensure_ascii=False)

@server.tool()
async def git_clone_repo(repo_url: str, target_folder: str) -> str:
    """Clone a git repository to a specified folder.
    
    Args:
        repo_url: URL of the git repository to clone
        target_folder: Path to the folder where the repository should be cloned
    """
    # Check if target folder exists
    target_path = Path(target_folder).expanduser().absolute()
    if target_path.exists():
        return json.dumps({
            "success": False,
            "error": f"Target folder already exists: {str(target_path)}"
        })
    
    # Check if git is installed
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True, text=True)
    except FileNotFoundError:
        return json.dumps({
            "success": False,
            "error": "Git is not installed. Please install Git first."
        })
    except subprocess.CalledProcessError:
        return json.dumps({
            "success": False,
            "error": "Error checking Git installation."
        })
    
    # Create parent directory if it doesn't exist
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Clone the repository
    try:
        result = subprocess.run(
            ["git", "clone", repo_url, str(target_path)],
            check=True,
            capture_output=True,
            text=True
        )
        return json.dumps({
            "success": True,
            "target_folder": str(target_path)
        })
    except subprocess.CalledProcessError as e:
        return json.dumps({
            "success": False,
            "error": f"Git clone failed: {e.stderr}"
        })

@server.tool()
async def open_in_vscode(folder_path: str, use_insiders: bool = False) -> str:
    """Open a folder in VS Code or VS Code Insiders application.
    
    Args:
        folder_path: Path to the folder to open
        use_insiders: Whether to use VS Code Insiders instead of regular VS Code
    """
    folder_path = Path(folder_path).expanduser().absolute()
    
    if not folder_path.exists():
        return json.dumps({
            "success": False,
            "error": f"Folder does not exist: {str(folder_path)}"
        })
    
    # Determine the command based on OS and whether to use Insiders
    system = platform.system()
    
    try:
        if system == "Darwin":  # macOS
            app_name = "Visual Studio Code - Insiders" if use_insiders else "Visual Studio Code"
            subprocess.run(["open", "-a", app_name, str(folder_path)], check=True)
        elif system == "Windows":
            # On Windows, use the start command to open the application
            vscode_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), 
                                      "Programs",
                                      "Microsoft VS Code Insiders" if use_insiders else "Microsoft VS Code",
                                      "Code.exe")
            
            # Check if VS Code exists at the expected path
            if not os.path.exists(vscode_path):
                # Try alternative installation paths
                program_files = os.environ.get("ProgramFiles", "C:\\Program Files")
                program_files_x86 = os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
                
                alt_paths = [
                    os.path.join(program_files, "Microsoft VS Code" + (" Insiders" if use_insiders else ""), "Code.exe"),
                    os.path.join(program_files_x86, "Microsoft VS Code" + (" Insiders" if use_insiders else ""), "Code.exe")
                ]
                
                for path in alt_paths:
                    if os.path.exists(path):
                        vscode_path = path
                        break
            
            if os.path.exists(vscode_path):
                # Launch the resolved executable directly (no shell) to avoid
                # command injection via shell metacharacters in folder_path.
                subprocess.run([vscode_path, str(folder_path)], check=True)
            else:
                # Fallback to command line approach
                cmd = "code-insiders" if use_insiders else "code"
                subprocess.run([cmd, str(folder_path)], check=True)
                
        elif system == "Linux":
            # On Linux, try to use the desktop application
            app_name = "code-insiders" if use_insiders else "code"
            
            # Try using xdg-open which should use the desktop application
            try:
                subprocess.run(["xdg-open", str(folder_path)], check=True)
            except (FileNotFoundError, subprocess.CalledProcessError):
                # Fallback to direct command
                subprocess.run([app_name, str(folder_path)], check=True)
        else:
            return json.dumps({
                "success": False,
                "error": f"Unsupported operating system: {system}"
            })
        
        return json.dumps({
            "success": True,
            "message": f"Opened {str(folder_path)} in {'VS Code Insiders' if use_insiders else 'VS Code'}"
        })
    except subprocess.CalledProcessError as e:
        return json.dumps({
            "success": False,
            "error": f"Failed to open VS Code: {str(e)}"
        })
    except FileNotFoundError:
        return json.dumps({
            "success": False,
            "error": f"{'VS Code Insiders' if use_insiders else 'VS Code'} is not installed or not in PATH"
        })

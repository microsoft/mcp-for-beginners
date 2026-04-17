from mcp.server.fastmcp import FastMCP

# 1. Create the server — give it a name
mcp = FastMCP("MyFirstServer")


# 2. TOOLS — functions the LLM can call
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to MCP."

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@mcp.tool()
def list_dir(dir: str) -> list[str]:
    """List the files in a directory."""
    import os
    try:
        return os.listdir(dir)
    except Exception:
        return []

# 3. RESOURCES — read-only data the client can fetch
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """A personalized greeting resource."""
    return f"Hello, {name}!"


# 4. PROMPTS — reusable prompt templates
@mcp.prompt()
def explain_topic(topic: str) -> str:
    """Ask the LLM to explain a topic simply."""
    return f"Explain '{topic}' in simple terms, as if I'm a beginner."

if __name__ == "__main__":
    # Runs with stdio transport by default (host spawns this as a subprocess)
    mcp.run()

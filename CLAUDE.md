# CLAUDE.md

This is the **MCP for Beginners** curriculum repository by Microsoft.
It teaches the Model Context Protocol (MCP) through hands-on lessons in Python, TypeScript, JavaScript, C#, Java, and Rust.

## Repository Structure

```
00-Introduction/           Overview of MCP
01-CoreConcepts/           Architecture, transports, primitives (tools/resources/prompts)
02-Security/               Auth and security patterns
03-GettingStarted/         Hands-on lessons (start here)
  01-first-server/         Build your first MCP server
  02-client/               Write an MCP client
  03-llm-client/           Connect an LLM to MCP
  04-vscode/               VS Code integration
  05-stdio-server/         stdio transport
  06-http-streaming/       HTTP/SSE transport
  08-testing/              Testing MCP servers
  13-mcp-inspector/        MCP Inspector tool
  14-sampling/             Sampling (LLM completions via MCP)
  samples/                 Runnable sample code per language
04-PracticalImplementation/ Real-world patterns
05-AdvancedTopics/         Deep dives
11-MCPServerHandsOnLabs/   Lab exercises
```

Each lesson has:
- `README.md` — lesson content and instructions
- `solution/python/` — reference implementation
- `samples/python/` — additional runnable examples

## Working with Python

### Setup (do once)
```bash
cd 03-GettingStarted/01-first-server
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install "mcp>=1.26.0"
```

### Run a server (stdio transport — default)
```bash
python server.py
```

### Test with MCP Inspector
```bash
npx @modelcontextprotocol/inspector python server.py
```

### Key Python library
`mcp` package — uses `FastMCP` for the decorator-based API:
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("MyServer")

@mcp.tool()
def my_tool(x: int) -> int:
    """Description shown to the LLM"""
    return x * 2

@mcp.resource("data://{id}")
def my_resource(id: str) -> str:
    return f"data for {id}"

@mcp.prompt()
def my_prompt(topic: str) -> str:
    return f"Tell me about {topic}"

if __name__ == "__main__":
    mcp.run()
```

## MCP Core Concepts

| Primitive | Purpose | Controlled by |
|-----------|---------|--------------|
| **Tool**  | Function the LLM can call (has side effects) | Model |
| **Resource** | Read-only data the LLM can read (like files/URIs) | Client/User |
| **Prompt** | Reusable prompt templates | Client/User |

## Transports
- **stdio** — default; host spawns server as subprocess, communicates via stdin/stdout
- **HTTP + SSE** — server runs as HTTP service; used for remote/multi-client scenarios

## Progress Tracking

- [x] Environment set up
- [ ] 01-first-server — build first server with tools and resources
- [ ] 02-client — write a client that connects to the server
- [ ] 03-llm-client — wire up an LLM
- [ ] 05-stdio-server — understand stdio transport
- [ ] 06-http-streaming — HTTP transport
- [ ] 08-testing — test your servers

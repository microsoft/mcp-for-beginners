# Setting Up Popular MCP Host Clients

This guide covers how to configure and use MCP servers with popular AI host applications. Each host has its own configuration approach, but once set up, they all communicate with MCP servers using the standardized protocol.

## What is an MCP Host?

An **MCP Host** is an AI application that can connect to MCP servers to extend its capabilities. Think of it as the "front end" that users interact with, while MCP servers provide the "back end" tools and data.

```mermaid
flowchart LR
    User[👤 User] --> Host[🖥️ MCP Host]
    Host --> S1[MCP Server A]
    Host --> S2[MCP Server B]
    Host --> S3[MCP Server C]
    
    subgraph "Popular Hosts"
        H1[Claude Desktop]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Prerequisites

- An MCP server to connect to (see [Module 3.1 - First Server](../01-first-server/README.md))
- The host application installed on your system
- Basic familiarity with JSON configuration files

---

## 1. Claude Desktop

**Claude Desktop** is Anthropic's official desktop application that natively supports MCP.

### Installation

1. Download Claude Desktop from [claude.ai/download](https://claude.ai/download)
2. Install and sign in with your Anthropic account

### Configuration

Claude Desktop uses a JSON configuration file to define MCP servers.

**Configuration file location:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Example configuration:**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### Configuration Options

| Field | Description | Example |
|-------|-------------|---------|
| `command` | The executable to run | `"python"`, `"node"`, `"npx"` |
| `args` | Command line arguments | `["-m", "my_server"]` |
| `env` | Environment variables | `{"API_KEY": "xxx"}` |
| `cwd` | Working directory | `"/path/to/server"` |

### Testing Your Setup

1. Save the configuration file
2. Restart Claude Desktop completely (quit and reopen)
3. Open a new conversation
4. Look for the 🔌 icon indicating connected servers
5. Try asking Claude to use one of your tools

### Troubleshooting Claude Desktop

**Server not appearing:**
- Check the configuration file syntax with a JSON validator
- Ensure the command path is correct
- Check Claude Desktop logs: Help → Show Logs

**Server crashes on startup:**
- Test your server manually in terminal first
- Check environment variables are set correctly
- Ensure all dependencies are installed

---

## 2. VS Code with GitHub Copilot

VS Code supports MCP through GitHub Copilot Chat extensions.

### Prerequisites

1. VS Code 1.99+ installed
2. GitHub Copilot extension installed
3. GitHub Copilot Chat extension installed

### Configuration

VS Code uses `.vscode/mcp.json` in your workspace or user settings.

**Workspace configuration** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

**User settings** (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### Using MCP in VS Code

1. Open the Copilot Chat panel (Ctrl+Shift+I / Cmd+Shift+I)
2. Type `@` to see available MCP tools
3. Use natural language to invoke tools: "Calculate 25 * 48 using the calculator"

### Troubleshooting VS Code

**MCP servers not loading:**
- Check Output panel → "MCP" for error logs
- Reload window: Ctrl+Shift+P → "Developer: Reload Window"
- Verify the server runs standalone first

---

## 3. Cursor

**Cursor** is an AI-first code editor with built-in MCP support.

### Installation

1. Download Cursor from [cursor.sh](https://cursor.sh)
2. Install and sign in

### Configuration

Cursor uses a similar configuration format to Claude Desktop.

**Configuration file location:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Example configuration:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### Using MCP in Cursor

1. Open Cursor's AI chat (Ctrl+L / Cmd+L)
2. MCP tools appear automatically in suggestions
3. Ask the AI to perform tasks using connected servers

---

## 4. Cline (Terminal-Based)

**Cline** is a terminal-based MCP client, ideal for command-line workflows.

### Installation

```bash
npm install -g @anthropic/cline
```

### Configuration

Cline uses environment variables and command-line arguments.

**Using environment variables:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Using command-line arguments:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Configuration file** (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Using Cline

```bash
# Start an interactive session
cline

# Single query with MCP
cline "Calculate the square root of 144 using the calculator"

# List available tools
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** is another AI-powered code editor with MCP support.

### Installation

1. Download Windsurf from [codeium.com/windsurf](https://codeium.com/windsurf)
2. Install and create an account

### Configuration

Windsurf configuration is managed through the settings UI:

1. Open Settings (Ctrl+, / Cmd+,)
2. Search for "MCP"
3. Click "Edit in settings.json"

**Example configuration:**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## Connecting to a Remote Server

Every example above starts a local server with `command` and `args`. A remote server is already running somewhere else, so instead of a command you give the host the server's URL (each host has its own field for it, shown below). For HTTP-based remote connections, MCP has two transports: the older SSE transport (what the VS Code example earlier in this lesson configures with `"type": "sse"` and an `/sse` URL) and the current Streamable HTTP transport (configured with `"type": "http"` in VS Code), which typically uses a single endpoint URL (often `/mcp`). The snippets below use the hosted MCP server from [Keenable](https://keenable.ai) at `https://api.keenable.ai/mcp`, which is free to use without an account or API key; anonymous requests are rate limited per IP.

**VS Code** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "keenable": {
      "type": "http",
      "url": "https://api.keenable.ai/mcp"
    }
  }
}
```

**Cursor** (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "keenable": {
      "url": "https://api.keenable.ai/mcp"
    }
  }
}
```

**Cline** (the VS Code extension; the MCP Servers panel → Configure MCP Servers button opens its `cline_mcp_settings.json`). The CLI flags shown earlier in this lesson start local servers; a remote server is added through this file:

```json
{
  "mcpServers": {
    "keenable": {
      "type": "streamableHttp",
      "url": "https://api.keenable.ai/mcp"
    }
  }
}
```

**Windsurf** (`~/.codeium/windsurf/mcp_config.json`; this is the file that Settings → Cascade → MCP Servers → "View raw config" opens, separate from the editor's `settings.json` shown earlier):

```json
{
  "mcpServers": {
    "keenable": {
      "serverUrl": "https://api.keenable.ai/mcp"
    }
  }
}
```

Claude Desktop does not read an HTTP entry from its configuration file (see the table below), so this example skips it.

After you save the file and reload the host, check its tool list: once the connection succeeds, the server's tools appear there. If nothing shows up, look at the host's MCP output for a connection or rate-limit error before changing the configuration. Then ask a question that needs one of the listed tools and the assistant should call it.

---

## Transport Types Comparison

Different hosts support different transport mechanisms:

| Host | stdio | SSE / Streamable HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Best for local servers started by the host
**SSE / Streamable HTTP**: Best for remote servers or servers shared between multiple clients (Streamable HTTP is the current remote transport; SSE is its predecessor and is still accepted by most hosts)

See [Connecting to a Remote Server](#connecting-to-a-remote-server) above for a Streamable HTTP configuration example for the hosts that support it.

---

## Common Troubleshooting

### Server won't start

1. **Test the server manually first:**
   ```bash
   # For Python
   python -m your_server_module
   
   # For Node.js
   node /path/to/server/index.js
   ```

2. **Check the command path:**
   - Use absolute paths when possible
   - Ensure the executable is in your PATH

3. **Verify dependencies:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server connects but tools don't work

1. **Check server logs** - Most hosts have logging options
2. **Verify tool registration** - Use MCP Inspector to test
3. **Check permissions** - Some tools need file/network access

### Environment variables not passed

- Some hosts sanitize environment variables
- Use the `env` configuration field explicitly
- Avoid sensitive data in config files (use secrets management)

---

## Security Best Practices

1. **Never commit API keys** to configuration files
2. **Use environment variables** for sensitive data
3. **Limit server permissions** to only what's needed
4. **Review server code** before granting access to your system
5. **Use allowlists** for file system and network access

---

## What's Next

- [3.13 - Debugging with MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Create your first MCP server](../01-first-server/README.md)
- [Module 5 - Advanced Topics](../../05-AdvancedTopics/README.md)

---

## Additional Resources

- [Claude Desktop MCP Documentation](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specification - Transports](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/)
- [Official MCP Servers Registry](https://github.com/modelcontextprotocol/servers)
- [Keenable Hosted MCP Server](https://docs.keenable.ai/mcp-server)

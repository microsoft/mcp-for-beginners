# How to Set Up Popular MCP Host Clients

> [!NOTE]
> Host configurations wey dey point to `/sse` na olden days HTTP+SSE example for
> MCP `2025-11-25`. For MCP `2026-07-28`, make you select Streamable HTTP for hosts wey
> dey support am and use the endpoint wey server configure.

Dis guide show how to configure and use MCP servers with popular AI host apps. Each host get im own way to configure, but once you don set am, dem go dey use one style talk to MCP servers.

## Wetin be MCP Host?

**MCP Host** na AI application wey fit connect to MCP servers to make am do more things. Think am like di "front end" wey users dey use, while MCP servers na im dey provide di "back end" tools and data dem.

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

## Wetin you need first

- MCP server wey you fit connect to (see [Module 3.1 - First Server](../01-first-server/README.md))
- Di host app wey you don install for your machine
- Small knowledge about JSON configuration files

---

## 1. Claude Desktop

**Claude Desktop** na Anthropic own official desktop app wey get native support for MCP.

### How to install am

1. Download Claude Desktop from [claude.ai/download](https://claude.ai/download)
2. Install am plus sign in with your Anthropic account

### How to configure am

Claude Desktop dey use JSON configuration file to talk which MCP servers you wan use.

**Where to find di configuration file:**
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

| Field | Wetin e mean | Example |
|-------|-------------|---------|
| `command` | The executable wey you go run | `"python"`, `"node"`, `"npx"` |
| `args` | Command line arguments | `["-m", "my_server"]` |
| `env` | Environment variables | `{"API_KEY": "xxx"}` |
| `cwd` | Working directory | `"/path/to/server"` |

### How to test how you set am

1. Save di configuration file
2. Restart Claude Desktop well well (completely quit and open am again)
3. Open new conversation
4. Watch out for di 🔌 icon wey mean say di servers don connect
5. Try ask Claude make e use one of your tools

### How to fix wahala with Claude Desktop

**If server no show for you:**
- Check configuration file syntax with JSON validator
- Make sure di command path dey correct
- Check Claude Desktop logs: Help → Show Logs

**If server crash when e dey start:**
- Try run your server by hand terminal first
- Make sure environment variables dey set well
- Check all dependencies don install finish

---

## 2. VS Code with GitHub Copilot

VS Code dey support MCP through GitHub Copilot Chat extensions.

### Wetin you need first

1. VS Code 1.99+ wey you don install
2. GitHub Copilot extension wey you don install
3. GitHub Copilot Chat extension wey you don install

### How to configure am

VS Code dey use `.vscode/mcp.json` for your workspace or user settings.

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

### How to use MCP for VS Code

1. Open di Copilot Chat panel (Ctrl+Shift+I / Cmd+Shift+I)
2. Type `@` to see di MCP tools wey dey available
3. Use natural language to call tools: "Calculate 25 * 48 using the calculator"

### How to fix wahala with VS Code

**If MCP servers no dey load:**
- Check Output panel → "MCP" for error logs
- Reload window: Ctrl+Shift+P → "Developer: Reload Window"
- Make sure say the server fit run alone first

---

## 3. Cursor

**Cursor** na AI-first code editor wey get MCP support inside.

### How to install am

1. Download Cursor from [cursor.sh](https://cursor.sh)
2. Install am and sign in

### How to configure am

Cursor use configuration style wey resemble Claude Desktop.

**Where to find di configuration file:**
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

### How to use MCP for Cursor

1. Open Cursor AI chat (Ctrl+L / Cmd+L)
2. MCP tools go show automatically inside suggestions
3. Ask AI make e run tasks with connected servers

---

## 4. Cline (Terminal-Based)

**Cline** na terminal-based MCP client, better for command-line workflows.

### How to install am

```bash
npm install -g @anthropic/cline
```

### How to configure am

Cline dey use environment variables and command-line arguments.

**How to use environment variables:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**How to use command-line arguments:**

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

### How to use Cline

```bash
# Start beta for interactive session
cline

# One query wit MCP
cline "Calculate the square root of 144 using the calculator"

# Show list of tools wey dey available
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** na another AI-powered code editor wey get MCP support.

### How to install am

1. Download Windsurf from [codeium.com/windsurf](https://codeium.com/windsurf)
2. Install am and create account

### How to configure am

Windsurf configuration na through the settings UI:

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

## Transport Types Comparison

Different hosts support different transport methods:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (standard input/output): Best for local servers wey host start
**SSE/HTTP**: Best for remote servers or servers wey multiple clients dey share

---

## Common Wahala and How to Fix Am

### Server no go start

1. **Test server manually first:**
   ```bash
   # For Python
   python -m your_server_module
   
   # For Node.js
   node /path/to/server/index.js
   ```

2. **Check command path:**
   - Use absolute paths if you fit
   - Make sure executable dey your PATH

3. **Check dependencies:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Server connect but tools no dey work

1. **Check server logs** - Most hosts get logging options
2. **Verify tool registration** - Use MCP Inspector to test am
3. **Check permissions** - Some tools need file and network access

### Environment variables no dey pass

- Some hosts dey clean environment variables
- Use the `env` field for configuration clearly
- No put sensitive data for config files (use secrets management)

---

## Security Best Practice

1. **No ever put API keys for configuration files**
2. **Use environment variables** for sensitive data
3. **Limit server permissions** to only wetin e need
4. **Check server code** before you gree make e access your system
5. **Use allowlists** for file system and network access

---

## Wetin You Go Do Next

- [3.13 - Debugging with MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Create your first MCP server](../01-first-server/README.md)
- [Module 5 - Advanced Topics](../../05-AdvancedTopics/README.md)

---

## Other Resources

- [Claude Desktop MCP Documentation](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP Specification - Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Official MCP Servers Registry](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
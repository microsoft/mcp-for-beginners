# Configurando Clientes de Host MCP Populares

> [!NOTE]
> Configurações de host que apontam para `/sse` são exemplos legados de HTTP+SSE para
> MCP `2025-11-25`. Para MCP `2026-07-28`, selecione HTTP Transmissível em hosts que
> o suportem e use o endpoint configurado pelo servidor.

Este guia cobre como configurar e usar servidores MCP com aplicativos populares de host de IA. Cada host tem sua própria abordagem de configuração, mas uma vez configurados, todos se comunicam com os servidores MCP usando o protocolo padronizado.

## O que é um Host MCP?

Um **Host MCP** é um aplicativo de IA que pode se conectar a servidores MCP para expandir suas capacidades. Pense nele como a "interface" que os usuários interagem, enquanto os servidores MCP fornecem as ferramentas e dados do "back end".

```mermaid
flowchart LR
    User[👤 Usuário] --> Host[🖥️ Host MCP]
    Host --> S1[Servidor MCP A]
    Host --> S2[Servidor MCP B]
    Host --> S3[Servidor MCP C]
    
    subgraph "Hosts Populares"
        H1[Desktop Claude]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## Pré-requisitos

- Um servidor MCP para se conectar (veja [Módulo 3.1 - Primeiro Servidor](../01-first-server/README.md))
- O aplicativo host instalado em seu sistema
- Familiaridade básica com arquivos de configuração JSON

---

## 1. Claude Desktop

**Claude Desktop** é o aplicativo oficial de desktop da Anthropic que suporta MCP nativamente.

### Instalação

1. Baixe o Claude Desktop em [claude.ai/download](https://claude.ai/download)
2. Instale e faça login com sua conta Anthropic

### Configuração

Claude Desktop usa um arquivo de configuração JSON para definir servidores MCP.

**Localização do arquivo de configuração:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Exemplo de configuração:**

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

### Opções de Configuração

| Campo | Descrição | Exemplo |
|-------|-------------|---------|
| `command` | O executável a ser rodado | `"python"`, `"node"`, `"npx"` |
| `args` | Argumentos da linha de comando | `["-m", "my_server"]` |
| `env` | Variáveis de ambiente | `{"API_KEY": "xxx"}` |
| `cwd` | Diretório de trabalho | `"/path/to/server"` |

### Testando sua Configuração

1. Salve o arquivo de configuração
2. Reinicie completamente o Claude Desktop (feche e abra novamente)
3. Abra uma nova conversa
4. Procure o ícone 🔌 indicando servidores conectados
5. Tente pedir para Claude usar uma de suas ferramentas

### Resolução de Problemas do Claude Desktop

**Servidor não aparece:**
- Verifique a sintaxe do arquivo de configuração com um validador JSON
- Garanta que o caminho do comando está correto
- Verifique os logs do Claude Desktop: Ajuda → Mostrar Logs

**Servidor fecha na inicialização:**
- Teste seu servidor manualmente no terminal primeiro
- Verifique se as variáveis de ambiente estão configuradas corretamente
- Garanta que todas as dependências estão instaladas

---

## 2. VS Code com GitHub Copilot

VS Code suporta MCP através das extensões GitHub Copilot Chat.

### Pré-requisitos

1. VS Code 1.99+ instalado
2. Extensão GitHub Copilot instalada
3. Extensão GitHub Copilot Chat instalada

### Configuração

VS Code usa `.vscode/mcp.json` nas configurações do espaço de trabalho ou do usuário.

**Configuração do espaço de trabalho** (`.vscode/mcp.json`):

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

**Configuração do usuário** (`settings.json`):

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

### Usando MCP no VS Code

1. Abra o painel Copilot Chat (Ctrl+Shift+I / Cmd+Shift+I)
2. Digite `@` para ver as ferramentas MCP disponíveis
3. Use linguagem natural para chamar ferramentas: "Calcular 25 * 48 usando a calculadora"

### Resolução de Problemas do VS Code

**Servidores MCP não carregam:**
- Verifique o painel de Saída → "MCP" para logs de erro
- Recarregue a janela: Ctrl+Shift+P → "Developer: Reload Window"
- Verifique se o servidor roda isoladamente primeiro

---

## 3. Cursor

**Cursor** é um editor de código com foco em IA com suporte embutido a MCP.

### Instalação

1. Baixe o Cursor em [cursor.sh](https://cursor.sh)
2. Instale e faça login

### Configuração

Cursor usa um formato de configuração similar ao Claude Desktop.

**Localização do arquivo de configuração:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**Exemplo de configuração:**

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

### Usando MCP no Cursor

1. Abra o chat de IA do Cursor (Ctrl+L / Cmd+L)
2. As ferramentas MCP aparecem automaticamente nas sugestões
3. Peça para a IA executar tarefas usando servidores conectados

---

## 4. Cline (Baseado em Terminal)

**Cline** é um cliente MCP baseado em terminal, ideal para fluxos de trabalho via linha de comando.

### Instalação

```bash
npm install -g @anthropic/cline
```

### Configuração

Cline usa variáveis de ambiente e argumentos de linha de comando.

**Usando variáveis de ambiente:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**Usando argumentos de linha de comando:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**Arquivo de configuração** (`~/.clinerc`):

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

### Usando Cline

```bash
# Iniciar uma sessão interativa
cline

# Consulta única com MCP
cline "Calculate the square root of 144 using the calculator"

# Listar ferramentas disponíveis
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** é outro editor de código com suporte a MCP e recurso de IA.

### Instalação

1. Baixe o Windsurf em [codeium.com/windsurf](https://codeium.com/windsurf)
2. Instale e crie uma conta

### Configuração

A configuração do Windsurf é gerenciada através da interface de configurações:

1. Abra Configurações (Ctrl+, / Cmd+,)
2. Procure por "MCP"
3. Clique em "Editar em settings.json"

**Exemplo de configuração:**

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

## Comparação de Tipos de Transporte

Diferentes hosts suportam diferentes mecanismos de transporte:

| Host | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio** (entrada/saída padrão): Melhor para servidores locais iniciados pelo host
**SSE/HTTP**: Melhor para servidores remotos ou servidores compartilhados entre múltiplos clientes

---

## Solução Comum de Problemas

### Servidor não inicia

1. **Teste o servidor manualmente primeiro:**
   ```bash
   # Para Python
   python -m your_server_module
   
   # Para Node.js
   node /path/to/server/index.js
   ```

2. **Verifique o caminho do comando:**
   - Use caminhos absolutos quando possível
   - Garanta que o executável está no PATH

3. **Verifique dependências:**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### Servidor conecta mas ferramentas não funcionam

1. **Verifique os logs do servidor** - A maioria dos hosts tem opções de registro
2. **Verifique o registro das ferramentas** - Use MCP Inspector para testar
3. **Verifique permissões** - Algumas ferramentas precisam de acesso a arquivos/rede

### Variáveis de ambiente não são passadas

- Alguns hosts sanitizam variáveis de ambiente
- Use explicitamente o campo de configuração `env`
- Evite dados sensíveis em arquivos de configuração (use gerenciamento de segredos)

---

## Melhores Práticas de Segurança

1. **Nunca comite chaves de API** em arquivos de configuração
2. **Use variáveis de ambiente** para dados sensíveis
3. **Limite permissões do servidor** apenas ao necessário
4. **Revise o código do servidor** antes de conceder acesso ao seu sistema
5. **Use listas de permissão** para acesso ao sistema de arquivos e rede

---

## O que vem a seguir

- [3.13 - Depuração com MCP Inspector](../13-mcp-inspector/README.md)
- [3.1 - Crie seu primeiro servidor MCP](../01-first-server/README.md)
- [Módulo 5 - Tópicos Avançados](../../05-AdvancedTopics/README.md)

---

## Recursos Adicionais

- [Documentação MCP do Claude Desktop](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [Extensão MCP para VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [Especificação MCP - Transportes](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [Registro Oficial de Servidores MCP](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
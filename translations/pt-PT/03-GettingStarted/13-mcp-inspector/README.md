# Depuração com MCP Inspector

> [!NOTE]
> Comandos usando `--sse` e URLs terminando em `/sse` testam o transporte legado HTTP+SSE.
> Para um novo servidor MCP `2026-07-28`, use uma versão do Inspector que
> suporte Streamable HTTP e selecione esse transporte em vez disso.

O **MCP Inspector** é uma ferramenta essencial de depuração que permite testar e diagnosticar interativamente os seus servidores MCP sem precisar de uma aplicação de host AI completa. Pense nele como o "Postman para MCP" - oferece uma interface visual para enviar pedidos, ver respostas e compreender como o seu servidor se comporta.

## Por que Usar o MCP Inspector?

Ao construir servidores MCP, frequentemente vai encontrar estes desafios:

- **"Será que o meu servidor está sequer a correr?"** - O Inspector mostra o estado da ligação
- **"As minhas ferramentas estão registadas corretamente?"** - O Inspector lista todas as ferramentas disponíveis
- **"Qual é o formato da resposta?"** - O Inspector mostra as respostas JSON completas
- **"Por que é que esta ferramenta não está a funcionar?"** - O Inspector exibe mensagens de erro detalhadas

## Pré-requisitos

- Node.js 18+ instalado
- npm (vem com o Node.js)
- Um servidor MCP para testar (veja [Módulo 3.1 - Primeiro Servidor](../01-first-server/README.md))

## Instalação

### Opção 1: Executar com npx (Recomendado para Testes Rápidos)

```bash
npx @modelcontextprotocol/inspector
```

### Opção 2: Instalar Globalmente

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### Opção 3: Adicionar ao Seu Projeto

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

Adicione ao `package.json`:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## Ligação ao Seu Servidor

### Servidores stdio (Processo Local)

Para servidores que comunicam via entrada/saída padrão:

```bash
# Servidor Python
npx @modelcontextprotocol/inspector python -m your_server_module

# Servidor Node.js
npx @modelcontextprotocol/inspector node ./build/index.js

# Com variáveis de ambiente
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### Servidores SSE/HTTP (Rede)

Para servidores que funcionam como serviços HTTP:

1. Primeiro inicie o seu servidor:
   ```bash
   python server.py  # Servidor a correr em http://localhost:8080
   ```

2. Abra o Inspector e ligue-se:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Visão Geral da Interface do Inspector

Quando o Inspector é iniciado, verá uma interface web (tipicamente em `http://localhost:5173`):

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Testar Ferramentas

### Listar Ferramentas Disponíveis

1. Clique no separador **Ferramentas**
2. O Inspector chama automaticamente `tools/list`
3. Verá todas as ferramentas registadas com:
   - Nome da ferramenta
   - Descrição
   - Esquema de entrada (parâmetros)

### Invocar uma Ferramenta

1. Selecione uma ferramenta da lista
2. Preencha os parâmetros necessários no formulário
3. Clique em **Executar Ferramenta**
4. Veja a resposta no painel de resultados

**Exemplo: Testar uma ferramenta calculadora**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### Depurar Erros da Ferramenta

Quando uma ferramenta falha, o Inspector mostra:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

Códigos de erro comuns:
| Código | Significado |
|------|------------|
| -32700 | Erro de análise (JSON inválido) |
| -32600 | Pedido inválido |
| -32601 | Método não encontrado |
| -32602 | Parâmetros inválidos |
| -32603 | Erro interno |

---

## Testar Recursos

### Listar Recursos

1. Clique no separador **Recursos**
2. O Inspector chama `resources/list`
3. Verá:
   - URIs dos recursos
   - Nomes e descrições
   - Tipos MIME

### Ler um Recurso

1. Selecione um recurso
2. Clique em **Ler Recurso**
3. Veja o conteúdo retornado

**Exemplo de saída:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## Testar Prompts

### Listar Prompts

1. Clique no separador **Prompts**
2. O Inspector chama `prompts/list`
3. Veja os modelos de prompt disponíveis

### Obter um Prompt

1. Selecione um prompt
2. Preencha quaisquer argumentos necessários
3. Clique em **Obter Prompt**
4. Veja as mensagens de prompt renderizadas

---

## Análise do Registo de Mensagens

O registo de mensagens mostra todas as mensagens do protocolo MCP. A transcrição abaixo é de um
servidor legado `2025-11-25` e inclui o handshake `initialize` removido. Um
servidor `2026-07-28` usa metadados de pedido autónomos e `server/discover`
em vez disso.

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### O Que Procurar

- **Pares Pedido/Resposta**: Cada `→` deve ter um correspondente `←`
- **Mensagens de erro**: Procure por `"error"` nas respostas
- **Tempos**: Grandes intervalos podem indicar problemas de desempenho
- **Versão do protocolo**: Assegure que servidor e cliente concordam na versão

---

## Integração com VS Code

Pode executar o Inspector diretamente do VS Code:

### Usando launch.json

Adicione ao `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### Usando Tarefas

Adicione ao `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## Cenários Comuns de Depuração

### Cenário 1: O Servidor Não Consegue Ligar-se

**Sintomas:** O Inspector mostra "Desligado" ou fica preso em "A ligar..."

**Lista de verificação:**
1. ✅ O comando do servidor está correto?
2. ✅ Todas as dependências estão instaladas?
3. ✅ O caminho do servidor é absoluto ou relativo ao diretório atual?
4. ✅ Variáveis de ambiente necessárias estão definidas?

**Passos de depuração:**
```bash
# Testar o servidor manualmente primeiro
python -c "import your_server_module; print('OK')"

# Verificar erros de importação
python -m your_server_module 2>&1 | head -20

# Verificar se o SDK MCP está instalado
pip show mcp
```

### Cenário 2: Ferramentas Não Aparecem

**Sintomas:** O separador de ferramentas mostra uma lista vazia

**Possíveis causas:**
1. Ferramentas não registadas durante a inicialização do servidor
2. Servidor falhou após início
3. O handler `tools/list` está a retornar um array vazio

**Passos de depuração:**
1. Verifique o registo de mensagens para a resposta de `tools/list`
2. Adicione registos ao seu código de registo de ferramentas
3. Verifique se os decoradores `@mcp.tool()` estão presentes (Python)

### Cenário 3: Ferramenta Retorna Erro

**Sintomas:** A chamada da ferramenta retorna uma resposta de erro

**Abordagem de depuração:**
1. Leia atentamente a mensagem de erro
2. Verifique se os tipos dos parâmetros correspondem ao esquema
3. Adicione try/catch com mensagens de erro detalhadas
4. Verifique os registos do servidor para stack traces

**Exemplo de tratamento de erro melhorado:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # Lógica da ferramenta aqui
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### Cenário 4: Conteúdo do Recurso Vazio

**Sintomas:** O recurso retorna, mas o conteúdo está vazio ou nulo

**Lista de verificação:**
1. ✅ O caminho ou URI do ficheiro está correto
2. ✅ O servidor tem permissão para ler o recurso
3. ✅ O conteúdo do recurso está a ser retornado corretamente

---

## Funcionalidades Avançadas do Inspector

### Cabeçalhos Personalizados (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### Registo Verboso

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### Gravação de Sessões

O Inspector pode exportar registos de mensagens para análise posterior:
1. Clique em **Exportar Registo** no painel de mensagens
2. Guarde o ficheiro JSON
3. Partilhe com os membros da equipa para depuração

---

## Boas Práticas

1. **Teste cedo e frequentemente** - Use o Inspector durante o desenvolvimento, não só quando há problemas
2. **Comece simples** - Teste a conectividade básica antes de chamadas complexas a ferramentas
3. **Verifique o esquema** - Muitos erros vêm de incompatibilidades de tipos de parâmetros
4. **Leia as mensagens de erro** - Os erros MCP são geralmente descritivos
5. **Mantenha o Inspector aberto** - Ajuda a captar problemas enquanto desenvolve

---

## Próximos Passos

Concluiu o Módulo 3: Começar! Continue a sua aprendizagem:

- [Módulo 4: Implementação Prática](../../04-PracticalImplementation/README.md)

---

## Recursos Adicionais

- [Repositório MCP Inspector no GitHub](https://github.com/modelcontextprotocol/inspector)
- [Especificação MCP - Mensagens do Protocolo](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Especificação JSON-RPC 2.0](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
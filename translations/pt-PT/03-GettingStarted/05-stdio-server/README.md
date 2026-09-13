# Servidor MCP com transporte stdio

> **⚠️ Atualização Importante**: A partir da Especificação MCP 2025-06-18, o transporte SSE (Server-Sent Events) autónomo foi **descontinuado** e substituído pelo transporte "Streamable HTTP". A especificação atual do MCP define dois mecanismos de transporte principais:
> 1. **stdio** - Entrada/saída standard (recomendado para servidores locais)
> 2. **Streamable HTTP** - Para servidores remotos que podem usar SSE internamente
>
> Esta lição foi atualizada para se concentrar no **transporte stdio**, que é a abordagem recomendada para a maioria das implementações de servidores MCP.

O transporte stdio permite que os servidores MCP comuniquem com clientes através dos fluxos de entrada e saída standard. Este é o mecanismo de transporte mais utilizado e recomendado na especificação atual do MCP, fornecendo uma forma simples e eficiente de construir servidores MCP que podem ser facilmente integrados com várias aplicações clientes.

## Visão Geral

Esta lição aborda como construir e consumir Servidores MCP usando o transporte stdio.

## Objetivos de Aprendizagem

No final desta lição, você será capaz de:

- Construir um Servidor MCP usando o transporte stdio.
- Depurar um Servidor MCP usando o Inspector.
- Consumir um Servidor MCP usando o Visual Studio Code.
- Compreender os mecanismos atuais de transporte MCP e por que o stdio é recomendado.


## Transporte stdio - Como Funciona

O transporte stdio é um dos dois transportes padrão na Especificação MCP
`2026-07-28`. Funciona assim:

- **Comunicação Simples**: O servidor lê mensagens JSON-RPC da entrada standard (`stdin`) e envia mensagens para a saída standard (`stdout`).
- **Baseado em processos**: O cliente inicia o servidor MCP como um subprocesso.
- **Formato das Mensagens**: As mensagens são pedidos JSON-RPC individuais, notificações ou respostas, delimitadas por novas linhas.
- **Registos**: O servidor PODE escrever strings UTF-8 no erro standard (`stderr`) para fins de registo.

### Requisitos Principais:
- As mensagens DEVEM ser delimitadas por novas linhas e NÃO DEVEM conter novas linhas embutidas
- O servidor NÃO PODE escrever nada em `stdout` que não seja uma mensagem MCP válida
- O cliente NÃO PODE escrever nada na `stdin` do servidor que não seja uma mensagem MCP válida

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

No código acima:

- Importamos a classe `Server` e `StdioServerTransport` do MCP SDK
- Criamos uma instância de servidor com configuração básica e capacidades
- Criamos uma instância `StdioServerTransport` e ligamos o servidor a ela, permitindo comunicação via stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Criar instância do servidor
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

No código acima nós:

- Criamos uma instância do servidor usando o MCP SDK
- Definimos ferramentas usando decoradores
- Usamos o gestor de contexto stdio_server para lidar com o transporte

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

A principal diferença do SSE é que os servidores stdio:

- Não requerem configuração de servidor web nem endpoints HTTP
- São iniciados como subprocessos pelo cliente
- Comunicam através dos fluxos stdin/stdout
- São mais simples de implementar e depurar

## Exercício: Criar um Servidor stdio

Para criar o nosso servidor, precisamos ter em mente duas coisas:

- Precisamos de um servidor web para expor endpoints para conexão e mensagens.
## Laboratório: Criar um servidor MCP stdio simples

Neste laboratório, vamos criar um servidor MCP simples usando o transporte stdio recomendado. Este servidor irá expor ferramentas que os clientes podem chamar usando o protocolo padrão Model Context Protocol.

### Pré-requisitos

- Python 3.8 ou superior
- MCP Python SDK: `pip install mcp`
- Compreensão básica de programação assíncrona

Vamos começar criando o nosso primeiro servidor MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configurar o registo de eventos
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar o servidor
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Usar transporte stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Diferenças chave em relação à abordagem SSE descontinuada

**Transporte stdio (Padrão Atual):**
- Modelo simples de subprocesso - o cliente inicia o servidor como processo filho
- Comunicação via stdin/stdout usando mensagens JSON-RPC
- Não requer configuração de servidor HTTP
- Melhor desempenho e segurança
- Depuração e desenvolvimento facilitados

**Transporte SSE (Descontinuado desde MCP 2025-06-18):**
- Requer servidor HTTP com endpoints SSE
- Configuração mais complexa com infraestrutura web
- Considerações adicionais de segurança para endpoints HTTP
- Agora substituído por Streamable HTTP para cenários baseados na web

### Criar um servidor com transporte stdio

Para criar o nosso servidor stdio, precisamos:

1. **Importar as bibliotecas necessárias** - Precisamos dos componentes do servidor MCP e do transporte stdio
2. **Criar uma instância do servidor** - Definir o servidor com as suas capacidades
3. **Definir ferramentas** - Adicionar a funcionalidade que queremos expor
4. **Configurar o transporte** - Configurar a comunicação stdio
5. **Executar o servidor** - Iniciar o servidor e tratar das mensagens

Vamos construir isso passo a passo:

### Passo 1: Criar um servidor stdio básico

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configurar o registo de eventos
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar o servidor
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Passo 2: Adicionar mais ferramentas

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Passo 3: Executar o servidor

Guarde o código como `server.py` e execute-o da linha de comando:

```bash
python server.py
```

O servidor inicia e aguarda a entrada da stdin. Comunica usando mensagens JSON-RPC via transporte stdio.

### Passo 4: Testar com o Inspector

Pode testar o seu servidor usando o MCP Inspector:

1. Instale o Inspector: `npx @modelcontextprotocol/inspector`
2. Execute o Inspector e aponte para o seu servidor
3. Teste as ferramentas que criou

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Depurar o seu servidor stdio

### Usar o MCP Inspector

O MCP Inspector é uma ferramenta valiosa para depurar e testar servidores MCP. Veja como usá-lo com o seu servidor stdio:

1. **Instalar o Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Executar o Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testar o seu servidor**: O Inspector fornece uma interface web onde pode:
   - Ver as capacidades do servidor
   - Testar as ferramentas com diferentes parâmetros
   - Monitorizar mensagens JSON-RPC
   - Depurar problemas de conexão

### Usar VS Code

Também pode depurar o seu servidor MCP diretamente no VS Code:

1. Criar uma configuração de lançamento em `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Definir pontos de interrupção no código do servidor
3. Executar o depurador e testar com o Inspector

### Dicas comuns para depuração

- Use `stderr` para registos - nunca escreva em `stdout` pois é reservado para mensagens MCP
- Garanta que todas as mensagens JSON-RPC estão delimitadas por novas linhas
- Teste primeiro com ferramentas simples antes de adicionar funcionalidades complexas
- Use o Inspector para verificar os formatos das mensagens

## Consumir o seu servidor stdio no VS Code

Depois de construir o seu servidor MCP stdio, pode integrá-lo com o VS Code para o usar com o Claude ou outros clientes compatíveis com MCP.

### Configuração

1. **Crie um ficheiro de configuração MCP** em `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ou `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Reinicie o Claude**: Feche e reabra o Claude para carregar a nova configuração do servidor.

3. **Teste a conexão**: Inicie uma conversa com o Claude e tente usar as ferramentas do seu servidor:
   - "Podes cumprimentar-me usando a ferramenta de saudação?"
   - "Calcula a soma de 15 e 27"
   - "Qual é a informação do servidor?"

### Exemplo de servidor stdio em TypeScript

Aqui está um exemplo completo em TypeScript para referência:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Adicionar ferramentas
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### Exemplo de servidor stdio em .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Resumo

Nesta lição atualizada, aprendeu a:

- Construir servidores MCP usando o atual **transporte stdio** (abordagem recomendada)
- Compreender por que o transporte SSE foi descontinuado em favor do stdio e do Streamable HTTP
- Criar ferramentas que podem ser chamadas pelos clientes MCP
- Depurar o seu servidor usando o MCP Inspector
- Integrar o seu servidor stdio com o VS Code e Claude

O transporte stdio oferece uma forma mais simples, segura e eficiente de construir servidores MCP comparado ao método SSE descontinuado. É o transporte recomendado para a maioria das implementações de servidores MCP desde a especificação de 2025-06-18.


### .NET

1. Vamos criar algumas ferramentas primeiro; para isso criamos um ficheiro *Tools.cs* com o seguinte conteúdo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercício: Testar o seu servidor stdio

Agora que construiu o seu servidor stdio, vamos testá-lo para garantir que funciona corretamente.

### Pré-requisitos

1. Assegure-se que tem o MCP Inspector instalado:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. O código do seu servidor deverá estar guardado (ex.: `server.py`)

### Testar com o Inspector

1. **Inicie o Inspector com o seu servidor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Abra a interface web**: O Inspector abrirá uma janela do navegador mostrando as capacidades do seu servidor.

3. **Teste as ferramentas**:
   - Experimente a ferramenta `get_greeting` com diferentes nomes
   - Teste a ferramenta `calculate_sum` com vários números
   - Chame a ferramenta `get_server_info` para ver a metadata do servidor

4. **Monitorize a comunicação**: O Inspector mostra as mensagens JSON-RPC trocadas entre o cliente e o servidor.

### O que deve ver

Quando o seu servidor arrancar corretamente, deve ver:
- Capacidades do servidor listadas no Inspector
- Ferramentas disponíveis para teste
- Trocas de mensagens JSON-RPC bem-sucedidas
- Respostas das ferramentas mostradas na interface

### Problemas comuns e soluções

**Servidor não arranca:**
- Verifique se todas as dependências estão instaladas: `pip install mcp`
- Verifique a sintaxe e indentação do Python
- Procure mensagens de erro na consola

**Ferramentas não aparecem:**
- Assegure-se que os decoradores `@server.tool()` estão presentes
- Verifique que as funções das ferramentas são definidas antes do `main()`
- Confirme que o servidor está configurado corretamente

**Problemas de conexão:**
- Confirme que o servidor está a usar o transporte stdio corretamente
- Verifique se não há outros processos a interferir
- Confirme a sintaxe do comando do Inspector

## Trabalho de casa

Tente ampliar o seu servidor com mais capacidades. Veja [esta página](https://api.chucknorris.io/) para, por exemplo, adicionar uma ferramenta que chama uma API. Decida como quer que o servidor seja. Divirta-se :)
## Solução

[Solução](./solution/README.md) Aqui está uma possível solução com código funcional.

## Pontos Principais

Os pontos principais deste capítulo são os seguintes:

- O transporte stdio é o mecanismo recomendado para servidores MCP locais.
- O transporte stdio permite comunicação fluida entre servidores MCP e clientes usando fluxos standard de entrada e saída.
- Pode usar tanto o Inspector como o Visual Studio Code para consumir servidores stdio diretamente, facilitando a depuração e integração.

## Exemplos 

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python) 

## Recursos Adicionais

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## O Que Vem a Seguir

## Próximos Passos

Agora que aprendeu a construir servidores MCP com o transporte stdio, pode explorar tópicos mais avançados:

- **Próximo**: [Streaming HTTP com MCP (Streamable HTTP)](../06-http-streaming/README.md) - Aprenda sobre o outro mecanismo de transporte suportado para servidores remotos
- **Avançado**: [Melhores Práticas de Segurança MCP](../../02-Security/README.md) - Implemente segurança nos seus servidores MCP
- **Produção**: [Estratégias de Deployment](../09-deployment/README.md) - Faça deployment dos seus servidores para uso em produção

## Recursos Adicionais

- [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Especificação atual
- [Documentação MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referências do SDK para todas as linguagens
- [Exemplos da Comunidade](../../06-CommunityContributions/README.md) - Mais exemplos de servidores da comunidade

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
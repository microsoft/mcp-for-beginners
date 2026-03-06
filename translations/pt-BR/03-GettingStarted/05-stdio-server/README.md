# Servidor MCP com transporte stdio

> **⚠️ Atualização Importante**: A partir da especificação MCP 2025-06-18, o transporte SSE (Server-Sent Events) independente foi **descontinuado** e substituído pelo transporte "HTTP Streamable". A especificação atual do MCP define dois mecanismos principais de transporte:
> 1. **stdio** - Entrada/saída padrão (recomendado para servidores locais)
> 2. **HTTP Streamable** - Para servidores remotos que podem usar SSE internamente
>
> Esta lição foi atualizada para focar no **transporte stdio**, que é a abordagem recomendada para a maioria das implementações de servidores MCP.

O transporte stdio permite que servidores MCP comuniquem-se com clientes através dos fluxos padrão de entrada e saída. Este é o mecanismo de transporte mais comumente usado e recomendado na especificação atual do MCP, oferecendo uma forma simples e eficiente de construir servidores MCP que podem ser facilmente integrados com várias aplicações cliente.

## Visão geral

Esta lição cobre como construir e consumir servidores MCP usando o transporte stdio.

## Objetivos de aprendizado

Ao final desta lição, você será capaz de:

- Construir um servidor MCP usando o transporte stdio.
- Depurar um servidor MCP usando o Inspector.
- Consumir um servidor MCP usando Visual Studio Code.
- Entender os mecanismos atuais de transporte MCP e por que o stdio é recomendado.

## Transporte stdio - Como funciona

O transporte stdio é um dos dois tipos de transporte suportados na especificação atual do MCP (2025-06-18). Veja como ele funciona:

- **Comunicação simples**: O servidor lê mensagens JSON-RPC da entrada padrão (`stdin`) e envia mensagens para a saída padrão (`stdout`).
- **Baseado em processo**: O cliente inicia o servidor MCP como um subprocesso.
- **Formato das mensagens**: Mensagens são requisições, notificações ou respostas JSON-RPC individuais, delimitadas por quebras de linha.
- **Registro de logs**: O servidor PODE escrever strings UTF-8 no erro padrão (`stderr`) para fins de registro.

### Requisitos principais:
- As mensagens DEVEM ser delimitadas por quebras de linha e NÃO DEVEM conter quebras de linha embutidas
- O servidor NÃO PODE escrever nada em `stdout` que não seja uma mensagem MCP válida
- O cliente NÃO PODE escrever nada no `stdin` do servidor que não seja uma mensagem MCP válida

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
```

No código acima:

- Importamos a classe `Server` e `StdioServerTransport` do MCP SDK
- Criamos uma instância de servidor com configuração básica e capacidades

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

No código anterior, nós:

- Criamos uma instância de servidor usando o MCP SDK
- Definimos ferramentas usando decoradores
- Usamos o gerenciador de contexto stdio_server para lidar com o transporte

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

A principal diferença em relação ao SSE é que servidores stdio:

- Não requerem configuração de servidor web ou endpoints HTTP
- São iniciados como subprocessos pelo cliente
- Se comunicam através dos fluxos stdin/stdout
- São mais simples de implementar e depurar

## Exercício: Criando um servidor stdio

Para criar nosso servidor, precisamos ter em mente duas coisas:

- Precisamos usar um servidor web para expor endpoints para conexão e mensagens.

## Laboratório: Criando um servidor MCP stdio simples

Neste laboratório, vamos criar um servidor MCP simples usando o transporte stdio recomendado. Este servidor irá expor ferramentas que os clientes podem chamar usando o protocolo Model Context padrão.

### Pré-requisitos

- Python 3.8 ou superior
- MCP Python SDK: `pip install mcp`
- Conhecimento básico de programação assíncrona

Vamos começar criando nosso primeiro servidor MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configurar registro
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

## Diferenças principais em relação à abordagem SSE descontinuada

**Transporte Stdio (Padrão Atual):**
- Modelo simples de subprocesso - o cliente inicia o servidor como processo filho
- Comunicação via stdin/stdout usando mensagens JSON-RPC
- Nenhuma configuração de servidor HTTP necessária
- Melhor desempenho e segurança
- Depuração e desenvolvimento mais fáceis

**Transporte SSE (Descontinuado desde MCP 2025-06-18):**
- Requer servidor HTTP com endpoints SSE
- Configuração mais complexa com infraestrutura web
- Considerações adicionais de segurança para endpoints HTTP
- Substituído por HTTP Streamable para cenários baseados na web

### Criando um servidor com transporte stdio

Para criar nosso servidor stdio, precisamos:

1. **Importar as bibliotecas necessárias** - Precisamos dos componentes do servidor MCP e transporte stdio
2. **Criar uma instância do servidor** - Definir o servidor com suas capacidades
3. **Definir ferramentas** - Adicionar funcionalidades que queremos expor
4. **Configurar o transporte** - Configurar comunicação stdio
5. **Rodar o servidor** - Iniciar o servidor e tratar mensagens

Vamos construir passo a passo:

### Passo 1: Crie um servidor stdio básico

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configurar registro de log
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

### Passo 2: Adicione mais ferramentas

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

### Passo 3: Rodando o servidor

Salve o código como `server.py` e execute-o pela linha de comando:

```bash
python server.py
```

O servidor iniciará e aguardará entrada do stdin. Ele se comunica usando mensagens JSON-RPC pelo transporte stdio.

### Passo 4: Teste com o Inspector

Você pode testar seu servidor usando o MCP Inspector:

1. Instale o Inspector: `npx @modelcontextprotocol/inspector`
2. Execute o Inspector e aponte para seu servidor
3. Teste as ferramentas que você criou

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Depurando seu servidor stdio

### Usando o MCP Inspector

O MCP Inspector é uma ferramenta valiosa para depuração e teste de servidores MCP. Veja como usá-lo com seu servidor stdio:

1. **Instale o Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Execute o Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Teste seu servidor**: O Inspector fornece uma interface web onde você pode:
   - Ver capacidades do servidor
   - Testar ferramentas com diferentes parâmetros
   - Monitorar mensagens JSON-RPC
   - Depurar problemas de conexão

### Usando o VS Code

Você também pode depurar seu servidor MCP diretamente no VS Code:

1. Crie uma configuração de execução em `.vscode/launch.json`:
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

2. Defina pontos de interrupção no código do servidor
3. Execute o depurador e teste com o Inspector

### Dicas comuns de depuração

- Use `stderr` para logs - nunca escreva em `stdout` pois é reservado para mensagens MCP
- Garanta que todas as mensagens JSON-RPC estejam delimitadas por nova linha
- Teste com ferramentas simples antes de adicionar funcionalidades complexas
- Use o Inspector para verificar os formatos das mensagens

## Consumindo seu servidor stdio no VS Code

Depois de construir seu servidor MCP stdio, você pode integrá-lo ao VS Code para usá-lo com Claude ou outros clientes compatíveis MCP.

### Configuração

1. **Crie um arquivo de configuração MCP** em `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ou `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Reinicie o Claude**: Feche e abra o Claude para carregar a nova configuração do servidor.

3. **Teste a conexão**: Inicie uma conversa com Claude e tente usar as ferramentas do seu servidor:
   - "Você pode me cumprimentar usando a ferramenta de saudação?"
   - "Calcule a soma de 15 e 27"
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

Nesta lição atualizada, você aprendeu como:

- Construir servidores MCP usando o atual **transporte stdio** (abordagem recomendada)
- Entender por que o transporte SSE foi descontinuado em favor do stdio e HTTP Streamable
- Criar ferramentas que podem ser chamadas por clientes MCP
- Depurar seu servidor usando o MCP Inspector
- Integrar seu servidor stdio ao VS Code e Claude

O transporte stdio oferece uma maneira mais simples, segura e performática de construir servidores MCP em comparação com a abordagem SSE descontinuada. É o transporte recomendado para a maioria das implementações de servidores MCP desde a especificação 2025-06-18.

### .NET

1. Vamos criar algumas ferramentas primeiro, para isso criaremos um arquivo *Tools.cs* com o seguinte conteúdo:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercício: Testando seu servidor stdio

Agora que você construiu seu servidor stdio, vamos testá-lo para garantir que funciona corretamente.

### Pré-requisitos

1. Certifique-se de ter o MCP Inspector instalado:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Seu código do servidor deve estar salvo (exemplo, como `server.py`)

### Testando com o Inspector

1. **Inicie o Inspector com seu servidor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Abra a interface web**: O Inspector abrirá uma janela do navegador mostrando as capacidades do seu servidor.

3. **Teste as ferramentas**:
   - Experimente a ferramenta `get_greeting` com nomes diferentes
   - Teste a ferramenta `calculate_sum` com vários números
   - Chame a ferramenta `get_server_info` para ver metadados do servidor

4. **Monitore a comunicação**: O Inspector mostra as mensagens JSON-RPC trocadas entre cliente e servidor.

### O que você deve ver

Quando seu servidor iniciar corretamente, você deve ver:
- Capacidades do servidor listadas no Inspector
- Ferramentas disponíveis para teste
- Trocas bem-sucedidas de mensagens JSON-RPC
- Respostas das ferramentas exibidas na interface

### Problemas comuns e soluções

**Servidor não inicia:**
- Verifique se todas as dependências estão instaladas: `pip install mcp`
- Confira a sintaxe e indentação do Python
- Procure mensagens de erro no console

**Ferramentas não aparecem:**
- Assegure-se de que os decoradores `@server.tool()` estejam presentes
- Verifique se as funções das ferramentas são definidas antes do `main()`
- Confira se o servidor está configurado corretamente

**Problemas de conexão:**
- Garanta que o servidor esteja usando o transporte stdio corretamente
- Verifique se não há outros processos interferindo
- Confirme o comando usado para o Inspector

## Tarefa

Tente expandir seu servidor com mais capacidades. Veja [esta página](https://api.chucknorris.io/) para, por exemplo, adicionar uma ferramenta que chama uma API. Você decide como o servidor deve ser. Divirta-se :)

## Solução

[Solution](./solution/README.md) Aqui está uma possível solução com código funcionando.

## Principais aprendizados

Os principais aprendizados deste capítulo são:

- O transporte stdio é o mecanismo recomendado para servidores MCP locais.
- O transporte stdio permite comunicação fluida entre servidores e clientes MCP usando os fluxos padrão de entrada e saída.
- Você pode usar tanto o Inspector quanto o Visual Studio Code para consumir servidores stdio diretamente, facilitando a depuração e integração.

## Exemplos

- [Calculadora Java](../samples/java/calculator/README.md)
- [Calculadora .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculadora JavaScript](../samples/javascript/README.md)
- [Calculadora TypeScript](../samples/typescript/README.md)
- [Calculadora Python](../../../../03-GettingStarted/samples/python)

## Recursos adicionais

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## O que vem a seguir

## Próximos passos

Agora que você aprendeu a construir servidores MCP com o transporte stdio, pode explorar tópicos mais avançados:

- **Próximo**: [HTTP Streaming com MCP (Streamable HTTP)](../06-http-streaming/README.md) - Aprenda sobre o outro mecanismo de transporte suportado para servidores remotos
- **Avançado**: [Melhores Práticas de Segurança MCP](../../02-Security/README.md) - Implemente segurança nos seus servidores MCP
- **Produção**: [Estratégias de implantação](../09-deployment/README.md) - Implemente seus servidores para uso em produção

## Recursos adicionais

- [Especificação MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Especificação oficial
- [Documentação do SDK MCP](https://github.com/modelcontextprotocol/sdk) - Referências do SDK para todas as linguagens
- [Exemplos da comunidade](../../06-CommunityContributions/README.md) - Mais exemplos de servidores da comunidade

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por seres humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
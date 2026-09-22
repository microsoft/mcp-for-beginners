# Streaming HTTPS com o Protocolo de Contexto de Modelo (MCP)

Este capítulo fornece um guia abrangente para implementar streaming seguro, escalável e em tempo real com o Protocolo de Contexto de Modelo (MCP) usando HTTPS. Ele cobre a motivação para streaming, os mecanismos de transporte disponíveis, como implementar HTTP streaming no MCP, melhores práticas de segurança, migração de SSE e orientações práticas para construir suas próprias aplicações de streaming MCP.

> [!WARNING]
> Os exemplos de implementação nesta lição são para a **Especificação MCP
> `2025-11-25`** e demonstram o handshake legado `initialize`,
> `Mcp-Session-Id`, evento stream GET e modelo de retomada. O MCP `2026-07-28`
> remove essas funcionalidades. As requisições Streamable HTTP atuais são
> requisições POST autocontidas com os cabeçalhos `MCP-Protocol-Version` e `Mcp-Method`, além de
> `Mcp-Name` quando necessário. Veja
> [O que mudou no MCP: A especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> antes de usar esses exemplos em uma nova implementação.

## Mecanismos de Transporte e Streaming no MCP

Esta seção explora os diferentes mecanismos de transporte disponíveis no MCP e seu papel em possibilitar capacidades de streaming para comunicação em tempo real entre clientes e servidores.

### O que é um Mecanismo de Transporte?

Um mecanismo de transporte define como os dados são trocados entre o cliente e o servidor. O MCP suporta múltiplos tipos de transporte para atender diferentes ambientes e requisitos:

- **stdio**: Entrada/saída padrão, adequado para ferramentas locais e baseadas em CLI. Simples, mas não adequado para web ou nuvem.
- **HTTP+SSE**: Transporte remoto legado, descontinuado no MCP `2025-03-26`
    e substituído pelo Streamable HTTP. Não use para novas implementações.
- **Streamable HTTP**: Transporte de streaming moderno baseado em HTTP, suportando notificações e melhor escalabilidade. Recomendado para a maioria dos cenários em produção e nuvem.

### Tabela Comparativa

Veja a tabela comparativa abaixo para entender as diferenças entre esses mecanismos de transporte:

| Transporte | Status | Notificações | Uso típico |
|---|---|---|---|
| stdio | Atual | Sim | Processos locais |
| HTTP+SSE | Descontinuado | Sim | Implementações remotas legadas |
| Streamable HTTP | Atual | Sim | Servidores remotos e na nuvem |

> **Dica:** Escolher o transporte correto impacta desempenho, escalabilidade e experiência do usuário. **Streamable HTTP** é recomendado para aplicações modernas, escaláveis e prontas para nuvem.

Os transportes padrão são stdio e Streamable HTTP. O HTTP+SSE aparece apenas
em exemplos mais antigos.

## Streaming: Conceitos e Motivação

Entender os conceitos fundamentais e as motivações por trás do streaming é fundamental para implementar sistemas de comunicação em tempo real eficazes.

**Streaming** é uma técnica em programação de rede que permite que os dados sejam enviados e recebidos em pequenos pedaços gerenciáveis ou como uma sequência de eventos, em vez de esperar que toda a resposta esteja pronta. Isso é especialmente útil para:

- Arquivos ou conjuntos de dados grandes.
- Atualizações em tempo real (por exemplo, chat, barras de progresso).
- Computações de longa duração onde se deseja manter o usuário informado.

Aqui está o que você precisa saber sobre streaming em alto nível:

- Os dados são entregues progressivamente, não de uma vez só.
- O cliente pode processar dados à medida que chegam.
- Reduz a latência percebida e melhora a experiência do usuário.

### Por que usar streaming?

As razões para usar streaming são as seguintes:


- Os usuários recebem feedback imediatamente, não apenas no final
- Permite aplicações em tempo real e interfaces responsivas
- Uso mais eficiente dos recursos de rede e computação

### Exemplo Simples: Servidor e Cliente HTTP Streaming

Aqui está um exemplo simples de como streaming pode ser implementado:

#### Python

**Servidor (Python, usando FastAPI e StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Cliente (Python, usando requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Este exemplo demonstra um servidor enviando uma série de mensagens para o cliente conforme elas ficam disponíveis, em vez de esperar que todas as mensagens estejam prontas.

**Como funciona:**

- O servidor gera cada mensagem assim que ela está pronta.
- O cliente recebe e imprime cada pedaço conforme ele chega.

**Requisitos:**

- O servidor deve usar uma resposta de streaming (ex: `StreamingResponse` no FastAPI).
- O cliente deve processar a resposta como um fluxo (`stream=True` em requests).
- O Content-Type geralmente é `text/event-stream` ou `application/octet-stream`.

#### Java

**Servidor (Java, usando Spring Boot e Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Cliente (Java, usando Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Notas sobre a implementação em Java:**

- Usa a pilha reativa do Spring Boot com `Flux` para streaming
- `ServerSentEvent` fornece streaming estruturado de eventos com tipos de evento
- `WebClient` com `bodyToFlux()` permite consumo reativo do streaming
- `delayElements()` simula tempo de processamento entre eventos
- Eventos podem ter tipos (`info`, `result`) para melhor tratamento no cliente

### Comparação: Streaming Clássico vs Streaming MCP

As diferenças entre como o streaming funciona de maneira "clássica" versus como funciona no MCP podem ser representadas assim:

| Recurso                | Streaming HTTP Clássico       | Streaming MCP (Notificações)       |
|------------------------|-------------------------------|-------------------------------------|
| Resposta principal     | Dividida em blocos             | Única, no final                    |
| Atualizações de progresso | Enviadas como blocos de dados | Enviadas como notificações         |
| Requisitos do cliente  | Deve processar o fluxo         | Deve implementar um handler de mensagens |
| Caso de uso            | Arquivos grandes, fluxos de tokens AI | Progresso, logs, feedback em tempo real |

### Diferenças Chave Observadas

Além disso, aqui estão algumas diferenças chaves:

- **Padrão de Comunicação:**
  - Streaming HTTP clássico: Usa codificação simples de transferência em blocos para enviar dados em pedaços
  - Streaming MCP: Usa sistema estruturado de notificações com protocolo JSON-RPC

- **Formato da Mensagem:**
  - HTTP clássico: Pedaços de texto simples com quebras de linha
  - MCP: Objetos estruturados LoggingMessageNotification com metadados

- **Implementação Cliente:**
  - HTTP clássico: Cliente simples que processa respostas de streaming
  - MCP: Cliente mais sofisticado com handler de mensagens para processar diferentes tipos de mensagens

- **Atualizações de Progresso:**
  - HTTP clássico: O progresso faz parte do fluxo da resposta principal
  - MCP: O progresso é enviado via mensagens separadas de notificação enquanto a resposta principal vem no final

### Recomendações

Há algumas coisas que recomendamos ao escolher entre implementar streaming clássico (como um endpoint que mostramos acima usando `/stream`) versus escolher streaming via MCP.

- **Para necessidades simples de streaming:** Streaming HTTP clássico é mais simples de implementar e suficiente para necessidades básicas de streaming.


- **Para aplicações complexas e interativas:** o streaming MCP oferece uma abordagem mais estruturada com metadados mais ricos e separação entre notificações e resultados finais.

- **Para aplicações de IA:** o sistema de notificações do MCP é particularmente útil para tarefas de IA de longa duração, onde você deseja manter os usuários informados sobre o progresso.

## Streaming no MCP

Ok, então você viu algumas recomendações e comparações até agora sobre a diferença entre streaming clássico e streaming no MCP. Vamos nos aprofundar exatamente em como você pode aproveitar o streaming no MCP.

Entender como o streaming funciona dentro da estrutura MCP é essencial para construir aplicações responsivas que fornecem feedback em tempo real para os usuários durante operações de longa duração.

No MCP, streaming não é sobre enviar a resposta principal em partes, mas sobre enviar **notificações** ao cliente enquanto uma ferramenta está processando uma solicitação. Essas notificações podem incluir atualizações de progresso, logs ou outros eventos.

### Como funciona

O resultado principal ainda é enviado como uma única resposta. No entanto, notificações podem ser enviadas como mensagens separadas durante o processamento e assim atualizar o cliente em tempo real. O cliente deve ser capaz de lidar e exibir essas notificações.

### Exercício opcional: conectar-se a um servidor MCP hospedado

Você também pode usar Streamable HTTP sem rodar um servidor local. Este exemplo
conecta ao [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
descobre suas ferramentas e pesquisa a documentação pública do MCP usando o mesmo
SDK Python que o [cliente local](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

O endpoint anônimo da Parallel não requer conta ou chave de API. O acesso gratuito é
limitado por taxa. Executar este script envia as consultas de pesquisa, objetivo e um
identificador de sessão aleatório para a Parallel. O serviço também oferece `web_fetch`,
que envia URLs solicitadas e qualquer contexto fornecido para a Parallel. Use informações públicas
para este exercício; veja seus [termos](https://parallel.ai/customer-terms)
e [política de privacidade](https://parallel.ai/privacy-policy).

Com Python 3.10 ou superior e um ambiente virtual ativado, instale o SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Salve isso como `hosted_search.py` e execute `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Espere que a descoberta inclua `web_search` e `web_fetch`, seguida de uma resposta de busca
contendo URLs de origem e trechos. Os resultados podem variar ou estar vazios.
O script verifica `isError` porque uma ferramenta pode falhar mesmo quando a requisição HTTP
é bem-sucedida. Se o acesso for limitado por taxa, espere antes de tentar novamente. Reutilize o mesmo
`session_id` se você estender o script com chamadas relacionadas de pesquisa ou fetch.

Streamable HTTP permite respostas JSON e SSE; este servidor pode retornar um
resultado JSON completo sem notificações de progresso. O SDK lida com
o transporte. Continue com o exemplo local abaixo para aprender sobre notificações.
Este script opcional faz uma busca explícita e fecha sua conexão ao
terminar. Se você depois expuser essas ferramentas para um agente, o agente pode chamá-las
durante seu trabalho; trate o texto recuperado da web como dados não confiáveis.

## O que é uma Notificação?

Dissemos "Notificação", o que isso significa no contexto do MCP?

Uma notificação é uma mensagem JSON-RPC que não possui um `id` e não
recebe resposta. MCP usa notificações para progresso, cancelamento e
outros eventos unidirecionais.

No MCP `2025-11-25`, um cliente envia `notifications/initialized` após o

aperto de mão de inicialização. O MCP `2026-07-28` não possui aperto de mão de inicialização, então
esta notificação é um comportamento legado.

Uma notificação tem a seguinte aparência como uma mensagem JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

O registro (logging) é um recurso que usa notificações; as notificações em si são um
tipo geral de mensagem JSON-RPC.

> **Obsoleta no MCP `2026-07-28`:** o recurso de Logging continua disponível
> para compatibilidade, mas está elegível para remoção na primeira revisão da especificação
> lançada em ou após 28 de julho de 2027. Novas implementações devem usar
> `stderr` com stdio ou OpenTelemetry para observabilidade estruturada.

Para uma implementação legada `2025-11-25`, o servidor habilita a capacidade de Logging
da seguinte maneira:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependendo do SDK usado, o logging pode estar habilitado por padrão, ou você pode precisar habilitá-lo explicitamente na configuração do seu servidor.

Existem diferentes tipos de notificações:

| Nível     | Descrição                      | Exemplo de Caso de Uso          |
|-----------|-------------------------------|---------------------------------|
| debug     | Informações detalhadas de depuração | Pontos de entrada/saída de funções |
| info      | Mensagens informativas gerais  | Atualizações de progresso de operação |
| notice    | Eventos normais, mas significativos | Alterações de configuração       |
| warning   | Condições de aviso             | Uso de recurso obsoleto          |
| error     | Condições de erro              | Falhas de operação               |
| critical  | Condições críticas             | Falhas de componentes do sistema  |
| alert     | Ação deve ser tomada imediatamente | Corrupção de dados detectada    |
| emergency | Sistema está inutilizável      | Falha completa do sistema        |

## Implementando Notificações no MCP

Para implementar notificações no MCP, você precisa configurar tanto o lado do servidor quanto do cliente para lidar com atualizações em tempo real. Isso permite que sua aplicação forneça feedback imediato aos usuários durante operações de longa duração.

### Lado do Servidor: Enviando Notificações

Vamos começar com o lado servidor. No MCP, você define ferramentas que podem enviar notificações enquanto processam solicitações. O servidor usa o objeto de contexto (geralmente `ctx`) para enviar mensagens ao cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

No exemplo anterior, a ferramenta `process_files` envia três notificações para o cliente enquanto processa cada arquivo. O método `ctx.info()` é usado para enviar mensagens informativas.

Além disso, para habilitar notificações, certifique-se de que seu servidor usa um transporte de streaming (como `streamable-http`) e que seu cliente implemente um manipulador de mensagens para processar notificações. Veja como configurar o servidor para usar o transporte `streamable-http`:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

Neste exemplo .NET, a ferramenta `ProcessFiles` é decorada com o atributo `Tool` e envia três notificações para o cliente enquanto processa cada arquivo. O método `ctx.Info()` é usado para enviar mensagens informativas.

Para habilitar notificações no seu servidor MCP .NET, certifique-se de usar um transporte de streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado do Cliente: Recebendo Notificações

O cliente deve implementar um manipulador de mensagens para processar e exibir notificações conforme elas chegam.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```


No código anterior, a função `message_handler` verifica se a mensagem recebida é uma notificação. Se for, ela imprime a notificação; caso contrário, processa como uma mensagem regular do servidor. Observe também como o `ClientSession` é inicializado com o `message_handler` para tratar notificações recebidas.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```


Neste exemplo .NET, a função `MessageHandler` verifica se a mensagem recebida é uma notificação. Se for, ela imprime a notificação; caso contrário, processa como uma mensagem regular do servidor. A `ClientSession` é inicializada com o manipulador de mensagens via as `ClientSessionOptions`.

Para habilitar notificações, certifique-se de que seu servidor usa um transporte de streaming (como `streamable-http`) e que seu cliente implemente um manipulador de mensagens para processar as notificações.

## Notificações de Progresso e Cenários

Esta seção explica o conceito de notificações de progresso no MCP, por que elas são importantes e como implementá-las usando Streamable HTTP. Você também encontrará um exercício prático para reforçar seu entendimento.

Notificações de progresso são mensagens em tempo real enviadas do servidor para o cliente durante operações demoradas. Em vez de esperar o processo inteiro terminar, o servidor mantém o cliente atualizado sobre o status atual. Isso melhora a transparência, a experiência do usuário e facilita a depuração.

**Exemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Por que Usar Notificações de Progresso?

Notificações de progresso são essenciais por vários motivos:

- **Melhor experiência do usuário:** Os usuários veem atualizações conforme o trabalho avança, não somente no final.
- **Feedback em tempo real:** Os clientes podem mostrar barras de progresso ou logs, fazendo o app parecer responsivo.
- **Depuração e monitoramento facilitados:** Desenvolvedores e usuários podem ver onde um processo está lento ou travado.

### Como Implementar Notificações de Progresso

Veja como implementar notificações de progresso no MCP:

- **No servidor:** Use `ctx.info()` ou `ctx.log()` para enviar notificações à medida que cada item é processado. Isso envia uma mensagem ao cliente antes do resultado principal estar pronto.
- **No cliente:** Implemente um manipulador de mensagens que escute e exiba notificações assim que chegarem. Esse manipulador distingue entre notificações e o resultado final.

**Exemplo de Servidor:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Exemplo de Cliente:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considerações de Segurança

A segurança deve ser uma prioridade máxima ao implementar qualquer servidor, especialmente ao usar transportes baseados em HTTP, como Streamable HTTP no MCP.

Ao implementar servidores MCP com transportes HTTP, a segurança torna-se uma preocupação crucial que exige atenção cuidadosa a múltiplos vetores de ataque e mecanismos de proteção.

### Visão Geral

A segurança é crítica ao expor servidores MCP via HTTP. Streamable HTTP introduz novas superfícies de ataque e requer configurações cuidadosas.

Aqui estão algumas considerações chave de segurança:

- **Validação do Cabeçalho Origin**: Sempre valide o cabeçalho `Origin` para prevenir ataques de DNS rebinding.
- **Vinculação a localhost**: Para desenvolvimento local, vincule os servidores a `localhost` para evitar exposição à internet pública.
- **Autenticação**: Implemente autenticação (ex.: chaves API, OAuth) para ambientes de produção.
- **CORS**: Configure políticas de Cross-Origin Resource Sharing (CORS) para restringir o acesso.
- **HTTPS**: Use HTTPS em produção para criptografar o tráfego.

### Boas Práticas

Além disso, aqui estão algumas boas práticas a seguir ao implementar segurança no seu servidor MCP streaming:

- Nunca confie em requisições recebidas sem validação.
- Registre e monitore todos os acessos e erros.
- Atualize regularmente as dependências para corrigir vulnerabilidades de segurança.

### Desafios

Você enfrentará alguns desafios ao implementar segurança em servidores de streaming MCP:

- Equilibrar segurança com facilidade de desenvolvimento
- Garantir compatibilidade com vários ambientes de clientes


## Atualizando de SSE para Streamable HTTP

Para aplicações que atualmente usam Server-Sent Events (SSE), migrar para Streamable HTTP oferece capacidades aprimoradas e melhor sustentabilidade a longo prazo para suas implementações MCP.

### Por que Atualizar?

Existem duas razões fortes para atualizar de SSE para Streamable HTTP:

- Streamable HTTP oferece melhor escalabilidade, compatibilidade e suporte mais rico a notificações do que SSE.
- É o transporte recomendado para novas aplicações MCP.

### Passos para Migração

Veja como migrar de SSE para Streamable HTTP em suas aplicações MCP:

- **Atualize o código do servidor** para usar `transport="streamable-http"` em `mcp.run()`.
- **Atualize o código do cliente** para usar `streamablehttp_client` em vez do cliente SSE.
- **Implemente um manipulador de mensagens** no cliente para processar notificações.
- **Teste a compatibilidade** com ferramentas e fluxos de trabalho existentes.

### Mantendo Compatibilidade

Recomenda-se manter compatibilidade com clientes SSE existentes durante o processo de migração. Aqui estão algumas estratégias:

- Você pode suportar SSE e Streamable HTTP executando ambos os transportes em endpoints diferentes.
- Migre os clientes gradualmente para o novo transporte.

### Desafios

Garanta que você aborde os seguintes desafios durante a migração:

- Garantir que todos os clientes sejam atualizados
- Lidar com diferenças na entrega de notificações

### Exercício: Construa Seu Próprio App MCP Streaming

**Cenário:**
Construa um servidor e cliente MCP onde o servidor processa uma lista de itens (ex.: arquivos ou documentos) e envia uma notificação para cada item processado. O cliente deve exibir cada notificação assim que chegar.

**Passos:**

1. Implemente uma ferramenta de servidor que processe uma lista e envie notificações para cada item.
2. Implemente um cliente com um manipulador de mensagens para exibir notificações em tempo real.
3. Teste sua implementação executando servidor e cliente, e observe as notificações.

[Solução](./solution/README.md)

## Leituras Complementares & Próximos Passos

Para continuar sua jornada com streaming MCP e expandir seu conhecimento, esta seção fornece recursos adicionais e sugestões de próximos passos para construir aplicações mais avançadas.

### Leituras Complementares

- [Microsoft: Introdução ao Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS no ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Requisições Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### O Que Vem Depois?

- Tente construir ferramentas MCP mais avançadas que usem streaming para análises em tempo real, chat ou edição colaborativa.
- Explore integrar streaming MCP com frameworks frontend (React, Vue, etc.) para atualizações ao vivo da interface.
- Próximo: [Utilizando o AI Toolkit para VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
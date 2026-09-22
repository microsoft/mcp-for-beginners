# Streaming HTTPS com Protocolo de Contexto de Modelo (MCP)

Este capítulo fornece um guia abrangente para implementar streaming seguro, escalável e em tempo real com o Protocolo de Contexto de Modelo (MCP) usando HTTPS. Cobre a motivação para streaming, os mecanismos de transporte disponíveis, como implementar HTTP transmissível em MCP, melhores práticas de segurança, migração do SSE, e orientações práticas para criar as suas próprias aplicações MCP com streaming.

> [!WARNING]
> Os exemplos de implementação nesta lição destinam-se à **Especificação MCP
> `2025-11-25`** e demonstram o handshake legado `initialize`,
> `Mcp-Session-Id`, fluxo de eventos GET, e modelo de retomabilidade. O MCP `2026-07-28`
> remove essas funcionalidades. Os pedidos atuais de HTTP transmissível são pedidos POST autónomos
> com cabeçalhos `MCP-Protocol-Version` e `Mcp-Method`, mais
> `Mcp-Name` quando necessário. Veja
> [O que mudou no MCP: A Especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> antes de usar estes exemplos numa nova implementação.

## Mecanismos de Transporte e Streaming no MCP

Esta seção explora os diferentes mecanismos de transporte disponíveis no MCP e o seu papel na habilitação de capacidades de streaming para comunicação em tempo real entre clientes e servidores.

### O que é um Mecanismo de Transporte?

Um mecanismo de transporte define como os dados são trocados entre o cliente e o servidor. O MCP suporta múltiplos tipos de transporte para acomodar diferentes ambientes e requisitos:

- **stdio**: Entrada/saída padrão, adequado para ferramentas locais e baseadas em CLI. Simples mas não adequado para web ou cloud.
- **HTTP+SSE**: O transporte remoto legado, descontinuado no MCP `2025-03-26`
    e substituído pelo HTTP Transmissível. Não usar para novas implementações.
- **HTTP Transmissível**: Transporte moderno baseado em HTTP para streaming, suportando notificações e melhor escalabilidade. Recomendado para a maioria dos cenários de produção e cloud.

### Tabela de Comparação

Veja a tabela de comparação abaixo para compreender as diferenças entre estes mecanismos de transporte:

| Transporte | Estado | Notificações | Uso típico |
|---|---|---|---|
| stdio | Atual | Sim | Processos locais |
| HTTP+SSE | Descontinuado | Sim | Implementações remotas legadas |
| HTTP Transmissível | Atual | Sim | Servidores remotos e cloud |

> **Dica:** Escolher o transporte certo impacta o desempenho, escalabilidade e experiência do utilizador. **HTTP Transmissível** é recomendado para aplicações modernas, escaláveis e preparadas para cloud.

Os transportes padrão são stdio e HTTP Transmissível. HTTP+SSE aparece apenas em
exemplos mais antigos.

## Streaming: Conceitos e Motivação

Compreender os conceitos fundamentais e as motivações por trás do streaming é essencial para implementar sistemas de comunicação eficazes em tempo real.

**Streaming** é uma técnica em programação de redes que permite enviar e receber dados em pequenos fragmentos geríveis ou como uma sequência de eventos, ao invés de esperar que uma resposta inteira esteja pronta. Isto é especialmente útil para:

- Grandes ficheiros ou conjuntos de dados.
- Atualizações em tempo real (ex., chat, barras de progresso).
- Computações de longa duração onde se quer manter o utilizador informado.

Eis o que precisa de saber sobre streaming a alto nível:

- Dados são entregues progressivamente, não todos de uma vez.
- O cliente pode processar dados à medida que chegam.
- Reduz a latência percebida e melhora a experiência do utilizador.

### Porque usar streaming?

As razões para usar streaming são as seguintes:

- Os utilizadores recebem feedback imediatamente, não só no fim
- Permite aplicações em tempo real e interfaces responsivas
- Uso mais eficiente de recursos de rede e computação

### Exemplo Simples: Servidor & Cliente HTTP Streaming

Aqui está um exemplo simples de como o streaming pode ser implementado:

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

Este exemplo demonstra um servidor a enviar uma série de mensagens para o cliente à medida que ficam disponíveis, ao invés de esperar que todas as mensagens estejam prontas.

**Como funciona:**

- O servidor envia cada mensagem assim que está pronta.
- O cliente recebe e imprime cada fragmento assim que chega.

**Requisitos:**

- O servidor deve usar uma resposta streaming (ex., `StreamingResponse` em FastAPI).
- O cliente deve processar a resposta em streaming (`stream=True` em requests).
- O Content-Type é habitualmente `text/event-stream` ou `application/octet-stream`.

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

**Notas sobre Implementação Java:**

- Usa o stack reativo do Spring Boot com `Flux` para streaming
- `ServerSentEvent` fornece streaming estruturado de eventos com tipos de eventos
- `WebClient` com `bodyToFlux()` permite consumo reativo do streaming
- `delayElements()` simula tempo de processamento entre eventos
- Eventos podem ter tipos (`info`, `result`) para melhor manipulação no cliente

### Comparação: Streaming Clássico vs Streaming MCP

As diferenças entre como o streaming funciona de maneira "clássica" versus como funciona no MCP podem ser representadas assim:

| Característica          | Streaming HTTP Clássico        | Streaming MCP (Notificações)       |
|------------------------|-------------------------------|-------------------------------------|
| Resposta principal     | Fracionada                    | Única, no fim                      |
| Atualizações de progresso | Enviadas como fragmentos de dados | Enviadas como notificações          |
| Requisitos do cliente  | Deve processar stream          | Deve implementar handler de mensagens |
| Caso de uso            | Ficheiros grandes, streams de tokens AI | Progresso, logs, feedback em tempo real |

### Diferenças Chave Observadas

Adicionalmente, aqui estão algumas diferenças chave:

- **Padrão de Comunicação:**
  - Streaming HTTP clássico: Usa transferência chunked simples para enviar dados em fragmentos
  - Streaming MCP: Usa um sistema estruturado de notificações com protocolo JSON-RPC

- **Formato da Mensagem:**
  - HTTP clássico: Fragmentos de texto plano com novas linhas
  - MCP: Objetos estruturados LoggingMessageNotification com metadados

- **Implementação do Cliente:**
  - HTTP clássico: Cliente simples que processa respostas em streaming
  - MCP: Cliente mais sofisticado com handler de mensagens para processar diferentes tipos de mensagens

- **Atualizações de Progresso:**
  - HTTP clássico: O progresso é parte do fluxo de resposta principal
  - MCP: O progresso é enviado via mensagens de notificação separadas enquanto a resposta principal vem no fim

### Recomendações

Existe algumas coisas que recomendamos quando se trata de escolher entre implementar streaming clássico (como o endpoint que mostramos acima usando `/stream`) versus optar pelo streaming via MCP.

- **Para necessidades simples de streaming:** O streaming HTTP clássico é mais simples de implementar e suficiente para necessidades básicas de streaming.


- **Para aplicações interativas complexas:** o streaming MCP fornece uma abordagem mais estruturada com metadados mais ricos e separação entre notificações e resultados finais.

- **Para aplicações de IA:** o sistema de notificações MCP é particularmente útil para tarefas de IA de longa duração onde se deseja manter os utilizadores informados sobre o progresso.

## Streaming em MCP

Ok, então viu algumas recomendações e comparações até agora sobre a diferença entre streaming clássico e streaming em MCP. Vamos entrar em detalhes exatamente sobre como pode tirar partido do streaming em MCP.

Compreender como o streaming funciona no âmbito do framework MCP é essencial para construir aplicações responsivas que forneçam feedback em tempo real aos utilizadores durante operações de longa duração.

Em MCP, streaming não se trata de enviar a resposta principal em fragmentos, mas de enviar **notificações** ao cliente enquanto uma ferramenta está a processar um pedido. Estas notificações podem incluir atualizações de progresso, registos, ou outros eventos.

### Como funciona

O resultado principal ainda é enviado como uma única resposta. No entanto, as notificações podem ser enviadas como mensagens separadas durante o processamento e assim atualizar o cliente em tempo real. O cliente deve ser capaz de tratar e exibir estas notificações.

### Exercício opcional: ligar a um servidor MCP hospedado

Também pode usar Streamable HTTP sem executar um servidor local. Este exemplo
liga-se a [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
descobre as suas ferramentas, e procura documentação pública MCP usando o mesmo
SDK Python que o [cliente local](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

O endpoint anónimo da Parallel não requer conta ou chave API. O acesso gratuito é
sujeito a limitação de taxa. Executar este script envia as consultas de busca, objetivo, e um
identificador de sessão aleatório para a Parallel. O serviço também oferece `web_fetch`,
que envia URLs solicitadas e qualquer contexto fornecido para a Parallel. Utilize informações públicas
para este exercício; consulte os seus [termos](https://parallel.ai/customer-terms)
e [política de privacidade](https://parallel.ai/privacy-policy).

Com Python 3.10 ou superior e um ambiente virtual ativado, instale o SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Guarde isto como `hosted_search.py` e execute `python hosted_search.py`:

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

Espere que a descoberta inclua `web_search` e `web_fetch`, seguida por uma resposta de busca
contendo URLs fonte e excertos. Os resultados podem variar ou estar vazios.
O script verifica `isError` porque uma ferramenta pode falhar mesmo quando o pedido HTTP
é bem-sucedido. Se o acesso estiver limitado por taxa, aguarde antes de tentar novamente. Reutilize o mesmo
`session_id` se ampliar o script com chamadas de busca ou fetch relacionadas.

Streamable HTTP permite tanto respostas JSON como SSE; este servidor pode retornar um
resultado JSON completo sem notificações de progresso. O SDK trata do
transporte. Continue com o exemplo local abaixo para aprender sobre notificações.
Este script opcional faz uma busca explícita e fecha a sua conexão quando
termina. Se mais tarde expuser estas ferramentas a um agente, o agente pode invocá-las
durante o seu trabalho; trate o texto web recuperado como dados não confiáveis.

## O que é uma Notificação?

Dissemos "Notificação", o que significa isso no contexto do MCP?

Uma notificação é uma mensagem JSON-RPC que não tem um `id` e não
recebe resposta. MCP usa notificações para progresso, cancelamento, e
outros eventos unidirecionais.

No MCP `2025-11-25`, um cliente envia `notifications/initialized` após o
handshake de inicialização. MCP `2026-07-28` não tem handshake de inicialização, assim
esta notificação é um comportamento legado.

Uma notificação tem a seguinte aparência como mensagem JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

O registo (logging) é uma funcionalidade que usa notificações; as notificações em si são um
tipo geral de mensagem JSON-RPC.

> **Descontinuado no MCP `2026-07-28`:** a funcionalidade de Logging mantém-se disponível
> para compatibilidade mas é elegível para remoção na primeira revisão da especificação
> lançada em ou após 28 de Julho de 2027. Novas implementações devem usar
> `stderr` com stdio ou OpenTelemetry para observabilidade estruturada.

Para uma implementação legada `2025-11-25`, o servidor ativa a capacidade de Logging
da seguinte forma:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependendo do SDK usado, o logging pode estar ativado por defeito, ou poderá ser necessário ativá-lo explicitamente na configuração do seu servidor.

Existem diferentes tipos de notificações:

| Nível     | Descrição                     | Caso de Uso Exemplo             |
|-----------|-------------------------------|---------------------------------|
| debug     | Informação detalhada de depuração | Pontos de entrada/saída da função |
| info      | Mensagens informativas gerais   | Atualizações de progresso da operação |
| notice    | Eventos normais mas significativos | Alterações de configuração       |
| warning   | Condições de aviso             | Utilização de funcionalidade obsoleta |
| error     | Condições de erro              | Falhas da operação               |
| critical  | Condições críticas             | Falhas de componente do sistema |
| alert     | Ação deve ser tomada imediatamente | Detecção de corrupção de dados  |
| emergency | Sistema está inutilizável      | Falha completa do sistema        |

## Implementando Notificações em MCP

Para implementar notificações em MCP, é necessário configurar ambos os lados, servidor e cliente, para tratar atualizações em tempo real. Isto permite que a sua aplicação forneça feedback imediato aos utilizadores durante operações de longa duração.

### Lado servidor: Enviar Notificações

Comecemos pelo lado servidor. Em MCP, define ferramentas que podem enviar notificações enquanto processam pedidos. O servidor usa o objeto de contexto (normalmente `ctx`) para enviar mensagens ao cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

No exemplo anterior, a ferramenta `process_files` envia três notificações ao cliente conforme processa cada ficheiro. O método `ctx.info()` é usado para enviar mensagens informativas.

Adicionalmente, para ativar notificações, assegure-se de que o seu servidor usa um transporte de streaming (como `streamable-http`) e o seu cliente implementa um manipulador de mensagens para processar notificações. Aqui está como pode configurar o servidor para usar o transporte `streamable-http`:

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

Neste exemplo .NET, a ferramenta `ProcessFiles` está decorada com o atributo `Tool` e envia três notificações ao cliente enquanto processa cada ficheiro. O método `ctx.Info()` é usado para enviar mensagens informativas.

Para ativar notificações no seu servidor MCP .NET, certifique-se de que está a usar um transporte de streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado cliente: Receber Notificações

O cliente deve implementar um manipulador de mensagens para processar e exibir notificações à medida que chegam.

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

No código anterior, a função `message_handler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa-a como uma mensagem normal do servidor. Note também como `ClientSession` é inicializado com `message_handler` para tratar notificações recebidas.

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


Neste exemplo .NET, a função `MessageHandler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa-a como uma mensagem regular do servidor. A `ClientSession` é inicializada com o manipulador de mensagens através do `ClientSessionOptions`.

Para ativar as notificações, assegure-se de que o seu servidor utiliza um transporte em streaming (como `streamable-http`) e que o seu cliente implementa um manipulador de mensagens para processar notificações.

## Notificações de Progresso & Cenários

Esta secção explica o conceito de notificações de progresso em MCP, por que são importantes, e como as implementar usando Streamable HTTP. Também encontrará um exercício prático para reforçar a sua compreensão.

As notificações de progresso são mensagens em tempo real enviadas do servidor para o cliente durante operações de longa duração. Em vez de esperar que todo o processo termine, o servidor mantém o cliente atualizado sobre o estado atual. Isto melhora a transparência, a experiência do utilizador e facilita a depuração.

**Exemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Por Que Usar Notificações de Progresso?

As notificações de progresso são essenciais por várias razões:

- **Melhor experiência do utilizador:** Os utilizadores veem atualizações à medida que o trabalho avança, não apenas no final.
- **Feedback em tempo real:** Os clientes podem mostrar barras de progresso ou registos, tornando a aplicação mais responsiva.
- **Depuração e monitorização mais fáceis:** Desenvolvedores e utilizadores podem ver onde um processo pode estar lento ou bloqueado.

### Como Implementar Notificações de Progresso

Eis como pode implementar notificações de progresso em MCP:

- **No servidor:** Use `ctx.info()` ou `ctx.log()` para enviar notificações à medida que cada item é processado. Isto envia uma mensagem ao cliente antes do resultado principal estar pronto.
- **No cliente:** Implemente um manipulador de mensagens que escute e mostre as notificações assim que chegam. Este manipulador distingue entre notificações e o resultado final.

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

A segurança deve ser uma prioridade máxima ao implementar qualquer servidor, especialmente ao usar transportes baseados em HTTP como o Streamable HTTP em MCP.

Ao implementar servidores MCP com transportes baseados em HTTP, a segurança torna-se uma preocupação primordial que requer atenção cuidadosa a múltiplos vetores de ataque e mecanismos de proteção.

### Visão Geral

A segurança é crítica ao expor servidores MCP via HTTP. O Streamable HTTP introduz novas superfícies de ataque e requer configuração cuidadosa.

Aqui estão algumas considerações-chave de segurança:

- **Validação do Cabeçalho Origin**: Valide sempre o cabeçalho `Origin` para prevenir ataques de DNS rebinding.
- **Vinculação ao Localhost**: Para desenvolvimento local, vincule os servidores a `localhost` para evitar exposição à internet pública.
- **Autenticação**: Implemente autenticação (ex.: chaves API, OAuth) para implementações em produção.
- **CORS**: Configure políticas de Cross-Origin Resource Sharing (CORS) para restringir o acesso.
- **HTTPS**: Use HTTPS em produção para encriptar o tráfego.

### Boas Práticas

Adicionalmente, aqui estão algumas boas práticas a seguir ao implementar segurança no seu servidor de streaming MCP:

- Nunca confie em pedidos recebidos sem validação.
- Registe e monitorize todo o acesso e erros.
- Atualize regularmente as dependências para corrigir vulnerabilidades de segurança.

### Desafios

Vai enfrentar alguns desafios quando implementar segurança em servidores de streaming MCP:

- Equilibrar segurança com facilidade de desenvolvimento
- Garantir compatibilidade com vários ambientes de cliente


## Atualização de SSE para Streamable HTTP

Para aplicações que atualmente usam Server-Sent Events (SSE), migrar para Streamable HTTP oferece capacidades aprimoradas e melhor sustentabilidade a longo prazo para as suas implementações MCP.

### Por Que Atualizar?

Existem duas razões convincentes para atualizar de SSE para Streamable HTTP:

- O Streamable HTTP oferece melhor escalabilidade, compatibilidade e suporte a notificações mais rico do que SSE.
- É o transporte recomendado para novas aplicações MCP.

### Passos para a Migração

Eis como pode migrar de SSE para Streamable HTTP nas suas aplicações MCP:

- **Atualize o código do servidor** para usar `transport="streamable-http"` em `mcp.run()`.
- **Atualize o código do cliente** para usar `streamablehttp_client` em vez do cliente SSE.
- **Implemente um manipulador de mensagens** no cliente para processar notificações.
- **Teste a compatibilidade** com ferramentas e fluxos de trabalho existentes.

### Manutenção da Compatibilidade

Recomenda-se manter a compatibilidade com clientes SSE existentes durante o processo de migração. Aqui estão algumas estratégias:

- Pode suportar tanto SSE como Streamable HTTP executando ambos os transportes em endpoints diferentes.
- Migre gradualmente os clientes para o novo transporte.

### Desafios

Certifique-se de abordar os seguintes desafios durante a migração:

- Garantir que todos os clientes estão atualizados
- Lidar com diferenças na entrega das notificações

### Exercício: Construa a Sua Própria App MCP em Streaming

**Cenário:**
Construa um servidor e cliente MCP onde o servidor processa uma lista de itens (ex.: ficheiros ou documentos) e envia uma notificação para cada item processado. O cliente deve mostrar cada notificação assim que chegar.

**Passos:**

1. Implemente uma ferramenta de servidor que processe uma lista e envie notificações para cada item.
2. Implemente um cliente com um manipulador de mensagens para mostrar notificações em tempo real.
3. Teste a implementação executando tanto o servidor como o cliente, e observe as notificações.

[Solução](./solution/README.md)

## Leituras Adicionais & Próximos Passos

Para continuar a sua jornada com o streaming MCP e expandir o seu conhecimento, esta secção fornece recursos adicionais e passos sugeridos para construir aplicações mais avançadas.

### Leituras Adicionais

- [Microsoft: Introdução ao Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS no ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Requisições em Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Próximos Passos

- Experimente construir ferramentas MCP mais avançadas que usem streaming para análises em tempo real, chat ou edição colaborativa.
- Explore a integração do streaming MCP com frameworks frontend (React, Vue, etc.) para atualizações de UI ao vivo.
- A seguir: [Utilização do AI Toolkit para VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Streaming HTTPS com Model Context Protocol (MCP)

Este capítulo oferece um guia abrangente para implementar streaming seguro, escalável e em tempo real com o Model Context Protocol (MCP) usando HTTPS. Cobre a motivação para streaming, os mecanismos de transporte disponíveis, como implementar HTTP transmissível em MCP, melhores práticas de segurança, migração do SSE e orientações práticas para construir suas próprias aplicações de streaming MCP. 

> **Olhando para frente:** esta lição descreve HTTP transmissível sob a **Especificação MCP 2025-11-25**, onde uma sessão é estabelecida durante `initialize` e fixada com um cabeçalho `Mcp-Session-Id`. O candidato a lançamento `2026-07-28` remove completamente o handshake e o ID de sessão, tornando cada requisição autocontida e roteável para qualquer instância do servidor, sem sessões fixas. Veja [O que está mudando no MCP: o candidato a lançamento 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) para detalhes.

## Mecanismos de Transporte e Streaming no MCP

Esta seção explora os diferentes mecanismos de transporte disponíveis no MCP e seu papel para habilitar capacidades de streaming para comunicação em tempo real entre clientes e servidores.

### O que é um Mecanismo de Transporte?

Um mecanismo de transporte define como os dados são trocados entre o cliente e o servidor. O MCP suporta múltiplos tipos de transporte para atender a diferentes ambientes e requisitos:

- **stdio**: Entrada/saída padrão, adequado para ferramentas locais e baseadas em CLI. Simples, mas não adequado para web ou nuvem.
- **SSE (Server-Sent Events)**: Permite aos servidores enviar atualizações em tempo real para clientes via HTTP. Bom para UIs web, mas limitado em escalabilidade e flexibilidade. A partir da Especificação MCP 2025-06-18, o transporte SSE isolado foi descontinuado e substituído pelo transporte "HTTP transmissível".
- **HTTP transmissível**: Transporte de streaming moderno baseado em HTTP, suportando notificações e melhor escalabilidade. Recomendado para a maioria dos cenários de produção e nuvem.

### Tabela Comparativa

Veja a tabela comparativa abaixo para entender as diferenças entre esses mecanismos de transporte:

| Transporte        | Atualizações em Tempo Real | Streaming | Escalabilidade | Caso de Uso            |
|------------------|----------------------------|-----------|----------------|-----------------------|
| stdio            | Não                        | Não       | Baixa          | Ferramentas CLI locais |
| SSE              | Sim                        | Sim       | Média          | Web, atualizações em tempo real |
| HTTP transmissível| Sim                        | Sim       | Alta           | Nuvem, multi-clientes  |

> **Dica:** Escolher o transporte correto impacta em desempenho, escalabilidade e experiência do usuário. **HTTP transmissível** é recomendado para aplicações modernas, escaláveis e prontos para a nuvem.

Observe os transportes stdio e SSE que foram mostrados nos capítulos anteriores e como o HTTP transmissível é o transporte abordado neste capítulo.

## Streaming: Conceitos e Motivação

Compreender os conceitos fundamentais e motivações por trás do streaming é essencial para implementar sistemas de comunicação em tempo real eficazes.

**Streaming** é uma técnica em programação de redes que permite enviar e receber dados em pequenos pedaços gerenciáveis ou como uma sequência de eventos, em vez de esperar uma resposta inteira estar pronta. Isso é especialmente útil para:

- Arquivos ou conjuntos de dados grandes.
- Atualizações em tempo real (ex.: chat, barras de progresso).
- Computações longas nas quais você deseja manter o usuário informado.

Eis o que você precisa saber sobre streaming em alto nível:

- Os dados são entregues progressivamente, não todos de uma vez.
- O cliente pode processar os dados conforme eles chegam.
- Reduz a latência percebida e melhora a experiência do usuário.

### Por que usar streaming?

Os motivos para usar streaming são os seguintes:

- Usuários recebem feedback imediatamente, não apenas ao final
- Habilita aplicações em tempo real e UIs responsivas
- Uso mais eficiente dos recursos de rede e computação

### Exemplo Simples: Servidor e Cliente de Streaming HTTP

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

Este exemplo demonstra um servidor enviando uma série de mensagens para o cliente conforme elas ficam disponíveis, em vez de esperar todas as mensagens prontas.

**Como funciona:**

- O servidor gera cada mensagem assim que está pronta.
- O cliente recebe e imprime cada pedaço assim que chega.

**Requisitos:**

- O servidor deve usar uma resposta de streaming (ex.: `StreamingResponse` no FastAPI).
- O cliente deve processar a resposta como um stream (`stream=True` em requests).
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

**Notas de implementação Java:**

- Usa a pilha reativa do Spring Boot com `Flux` para streaming
- `ServerSentEvent` fornece streaming estruturado com tipos de eventos
- `WebClient` com `bodyToFlux()` possibilita consumo reativo em streaming
- `delayElements()` simula tempo de processamento entre eventos
- Eventos podem ter tipos (`info`, `result`) para melhor tratamento no cliente

### Comparação: Streaming Clássico vs Streaming MCP

As diferenças entre como o streaming funciona de maneira "clássica" versus como funciona no MCP podem ser representadas assim:

| Recurso                 | Streaming HTTP Clássico         | Streaming MCP (Notificações)       |
|-------------------------|--------------------------------|-----------------------------------|
| Resposta principal      | Fragmentada                    | Única, ao final                   |
| Atualizações de progresso| Enviadas como pedaços de dados | Enviadas como notificações        |
| Requisitos do cliente   | Deve processar stream          | Deve implementar manipulador de mensagens |
| Caso de uso             | Arquivos grandes, streams de tokens AI | Progresso, logs, feedback em tempo real |

### Diferenças principais observadas

Além disso, aqui estão algumas diferenças chave:

- **Padrão de comunicação:**
  - Streaming HTTP clássico: Usa codificação chunked simples para enviar dados em pedaços
  - Streaming MCP: Usa um sistema estruturado de notificações com protocolo JSON-RPC

- **Formato da mensagem:**
  - HTTP clássico: Pedaços de texto simples com quebras de linha
  - MCP: Objetos estruturados LoggingMessageNotification com metadados

- **Implementação do cliente:**
  - HTTP clássico: Cliente simples que processa respostas em streaming
  - MCP: Cliente mais sofisticado com manipulador de mensagens para processar diferentes tipos de mensagens

- **Atualizações de progresso:**
  - HTTP clássico: O progresso é parte do fluxo principal da resposta
  - MCP: O progresso é enviado via mensagens de notificação separadas enquanto o resultado principal vem no final

### Recomendações

Recomendamos algumas coisas na hora de escolher entre implementar streaming clássico (como um endpoint mostrado acima usando `/stream`) versus escolher streaming via MCP.

- **Para necessidades simples de streaming:** Streaming HTTP clássico é mais simples de implementar e suficiente para necessidades básicas.

- **Para aplicações complexas e interativas:** Streaming MCP oferece abordagem mais estruturada com metadados mais ricos e separação entre notificações e resultados finais.

- **Para aplicações AI:** O sistema de notificações do MCP é particularmente útil para tarefas AI longas onde você quer manter o usuário informado do progresso.

## Streaming no MCP

Ok, você viu algumas recomendações e comparações até aqui sobre a diferença entre streaming clássico e streaming no MCP. Vamos ver em detalhe exatamente como você pode tirar proveito do streaming no MCP.

Entender como o streaming funciona dentro do framework MCP é essencial para construir aplicações responsivas que fornecem feedback em tempo real durante operações longas.

No MCP, streaming não é sobre enviar a resposta principal em pedaços, mas sobre enviar **notificações** ao cliente enquanto uma ferramenta processa uma requisição. Essas notificações podem incluir atualizações de progresso, logs ou outros eventos.

### Como funciona

O resultado principal ainda é enviado como uma única resposta. Entretanto, notificações podem ser enviadas como mensagens separadas durante o processamento, atualizando o cliente em tempo real. O cliente deve ser capaz de tratar e exibir essas notificações.

## O que é uma Notificação?

Dissemos "Notificação", o que isso significa no contexto do MCP?

Uma notificação é uma mensagem enviada do servidor ao cliente para informar sobre progresso, status ou outros eventos durante uma operação longa. Notificações melhoram a transparência e a experiência do usuário.

Por exemplo, um cliente deve enviar uma notificação assim que o handshake inicial com o servidor for realizado.

Uma notificação é assim em formato JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notificações pertencem a um tópico no MCP referenciado como ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Aviso de descontinuação:** o candidato a lançamento  `2026-07-28` da especificação MCP marca a primitiva Logging como depreciada em favor do `stderr` para transportes stdio e OpenTelemetry para observabilidade estruturada. Logging continua funcionando em `2025-11-25` e por pelo menos um ano após qualquer descontinuação oficial. Veja [O que está mudando no MCP: o candidato a lançamento 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Para fazer logging funcionar, o servidor precisa habilitá-lo como recurso/capacidade assim:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependendo da SDK usada, logging pode estar habilitado por padrão, ou você pode precisar habilitá-lo explicitamente na configuração do seu servidor.

Existem diferentes tipos de notificações:

| Nível     | Descrição                    | Exemplo de Uso                |
|-----------|------------------------------|------------------------------|
| debug     | Informações detalhadas para debug | Pontos de entrada/saída de funções |
| info      | Mensagens informativas gerais | Atualizações de progresso da operação |
| notice    | Eventos normais mas significativos | Mudanças de configuração       |
| warning   | Condições de aviso             | Uso de recurso depreciado     |
| error     | Condições de erro              | Falhas na operação            |
| critical  | Condições críticas             | Falha de componentes do sistema |
| alert     | Ação deve ser tomada imediatamente | Corrupção de dados detectada |
| emergency | Sistema inutilizável           | Falha total do sistema        |

## Implementando Notificações no MCP

Para implementar notificações no MCP, você precisa configurar tanto o lado do servidor quanto do cliente para lidar com atualizações em tempo real. Isso permite que sua aplicação forneça feedback imediato a usuários durante operações longas.

### Lado do servidor: Enviando Notificações

Vamos começar com o lado do servidor. No MCP, você define ferramentas que podem enviar notificações enquanto processam requisições. O servidor usa o objeto de contexto (geralmente `ctx`) para enviar mensagens ao cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

No exemplo acima, a ferramenta `process_files` envia três notificações para o cliente enquanto processa cada arquivo. O método `ctx.info()` é usado para enviar mensagens informativas.

Além disso, para habilitar notificações, assegure que seu servidor utiliza um transporte de streaming (como `streamable-http`) e seu cliente implementa um manipulador de mensagens para processar notificações. Veja como configurar o servidor para usar o transporte `streamable-http`:

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

Neste exemplo .NET, a ferramenta `ProcessFiles` é decorada com o atributo `Tool` e envia três notificações ao cliente enquanto processa cada arquivo. O método `ctx.Info()` é usado para enviar mensagens informativas.

Para habilitar notificações no seu servidor MCP .NET, assegure que está utilizando um transporte de streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado do cliente: Recebendo Notificações

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

No código acima, a função `message_handler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa como uma mensagem normal do servidor. Note também como `ClientSession` é inicializado com o `message_handler` para tratar notificações recebidas.

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

Neste exemplo .NET, a função `MessageHandler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa como mensagem normal do servidor. O `ClientSession` é inicializado com o manipulador de mensagens via `ClientSessionOptions`.

Para habilitar notificações, assegure que seu servidor usa transporte de streaming (como `streamable-http`) e seu cliente implementa um manipulador para processar notificações.

## Notificações de Progresso & Cenários

Esta seção explica o conceito de notificações de progresso no MCP, por que são importantes e como implementá-las usando HTTP transmissível. Também há uma tarefa prática para reforçar o seu entendimento.

Notificações de progresso são mensagens em tempo real enviadas do servidor para o cliente durante operações longas. Em vez de esperar o processo inteiro terminar, o servidor mantém o cliente atualizado sobre o status atual. Isso melhora a transparência, a experiência do usuário e facilita a depuração.

**Exemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Por que usar notificações de progresso?

Notificações de progresso são essenciais por vários motivos:

- **Melhor experiência do usuário:** Usuários veem atualizações conforme o trabalho progride, não apenas no final.
- **Feedback em tempo real:** Clientes podem exibir barras de progresso ou logs, deixando o app responsivo.
- **Depuração e monitoramento mais fáceis:** Desenvolvedores e usuários podem ver onde um processo está lento ou travado.

### Como implementar notificações de progresso

Veja como implementar notificações de progresso no MCP:

- **No servidor:** Use `ctx.info()` ou `ctx.log()` para enviar notificações conforme cada item é processado. Isso envia uma mensagem ao cliente antes do resultado principal estar pronto.
- **No cliente:** Implemente um manipulador de mensagens que ouça e exiba notificações conforme chegam. Esse manipulador distingue entre notificações e o resultado final.

**Exemplo de servidor:**


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

A segurança deve ser uma prioridade máxima ao implementar qualquer servidor, especialmente ao usar transportes baseados em HTTP como Streamable HTTP no MCP.

Ao implementar servidores MCP com transportes baseados em HTTP, a segurança torna-se uma preocupação primordial que requer atenção cuidadosa a múltiplos vetores de ataque e mecanismos de proteção.

### Visão Geral

A segurança é crítica ao expor servidores MCP via HTTP. Streamable HTTP introduz novas superfícies de ataque e requer configuração cuidadosa.

Aqui estão algumas considerações-chave de segurança:

- **Validação do Cabeçalho Origin**: Sempre valide o cabeçalho `Origin` para prevenir ataques de DNS rebinding.
- **Binding Localhost**: Para desenvolvimento local, vincule os servidores ao `localhost` para evitar expô-los na internet pública.
- **Autenticação**: Implemente autenticação (por exemplo, chaves de API, OAuth) para implantações em produção.
- **CORS**: Configure políticas de Cross-Origin Resource Sharing (CORS) para restringir o acesso.
- **HTTPS**: Use HTTPS em produção para criptografar o tráfego.

### Melhores Práticas

Além disso, aqui estão algumas melhores práticas para seguir ao implementar segurança no seu servidor de streaming MCP:

- Nunca confie em requisições recebidas sem validação.
- Registre e monitore todos os acessos e erros.
- Atualize regularmente as dependências para corrigir vulnerabilidades de segurança.

### Desafios

Você enfrentará alguns desafios ao implementar segurança em servidores de streaming MCP:

- Equilibrar segurança com facilidade de desenvolvimento
- Garantir compatibilidade com vários ambientes de cliente


## Atualizando de SSE para Streamable HTTP

Para aplicações que atualmente usam Server-Sent Events (SSE), migrar para Streamable HTTP oferece capacidades aprimoradas e melhor sustentabilidade a longo prazo para suas implementações MCP.

### Por Que Atualizar?

Existem duas razões convincentes para atualizar de SSE para Streamable HTTP:

- Streamable HTTP oferece melhor escalabilidade, compatibilidade e suporte a notificações mais ricas do que SSE.
- É o transporte recomendado para novas aplicações MCP.

### Passos da Migração

Veja como você pode migrar de SSE para Streamable HTTP nas suas aplicações MCP:

- **Atualize o código do servidor** para usar `transport="streamable-http"` em `mcp.run()`.
- **Atualize o código do cliente** para usar `streamablehttp_client` em vez do cliente SSE.
- **Implemente um manipulador de mensagens** no cliente para processar as notificações.
- **Teste a compatibilidade** com ferramentas e fluxos de trabalho existentes.

### Mantendo a Compatibilidade

Recomenda-se manter a compatibilidade com clientes SSE existentes durante o processo de migração. Aqui estão algumas estratégias:

- Você pode suportar ambos SSE e Streamable HTTP executando ambos os transportes em endpoints diferentes.
- Migre os clientes gradualmente para o novo transporte.

### Desafios

Certifique-se de enfrentar os seguintes desafios durante a migração:

- Garantir que todos os clientes sejam atualizados
- Lidar com diferenças na entrega de notificações

### Exercício: Construa Seu Próprio App MCP de Streaming

**Cenário:**
Construa um servidor e cliente MCP onde o servidor processa uma lista de itens (por exemplo, arquivos ou documentos) e envia uma notificação para cada item processado. O cliente deve exibir cada notificação conforme ela chega.

**Passos:**

1. Implemente uma ferramenta de servidor que processe uma lista e envie notificações para cada item.
2. Implemente um cliente com um manipulador de mensagens para exibir notificações em tempo real.
3. Teste sua implementação executando servidor e cliente, e observe as notificações.

[Solução](./solution/README.md)

## Leituras Adicionais & Próximos Passos

Para continuar sua jornada com streaming MCP e expandir seu conhecimento, esta seção fornece recursos adicionais e próximos passos sugeridos para construir aplicações mais avançadas.

### Leituras Adicionais

- [Microsoft: Introdução ao Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS em ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Requisições com Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Próximos Passos

- Tente construir ferramentas MCP mais avançadas que usem streaming para análises em tempo real, chat ou edição colaborativa.
- Explore integrar o streaming MCP com frameworks frontend (React, Vue, etc.) para atualizações ao vivo na interface do usuário.
- Próximo: [Utilizando o AI Toolkit para VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
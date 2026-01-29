# Transmissão HTTPS com o Protocolo de Contexto de Modelo (MCP)

Este capítulo oferece um guia abrangente para implementar transmissão segura, escalável e em tempo real com o Protocolo de Contexto de Modelo (MCP) usando HTTPS. Ele aborda a motivação para transmissão, os mecanismos de transporte disponíveis, como implementar HTTP transmitível no MCP, melhores práticas de segurança, migração de SSE e orientações práticas para construir suas próprias aplicações MCP de transmissão.

## Mecanismos de Transporte e Transmissão no MCP

Esta seção explora os diferentes mecanismos de transporte disponíveis no MCP e seu papel em habilitar capacidades de transmissão para comunicação em tempo real entre clientes e servidores.

### O que é um Mecanismo de Transporte?

Um mecanismo de transporte define como os dados são trocados entre o cliente e o servidor. O MCP suporta vários tipos de transporte para atender diferentes ambientes e requisitos:

- **stdio**: Entrada/saída padrão, adequado para ferramentas locais e baseadas em CLI. Simples, mas não adequado para web ou nuvem.
- **SSE (Server-Sent Events)**: Permite que servidores enviem atualizações em tempo real para clientes via HTTP. Bom para interfaces web, mas limitado em escalabilidade e flexibilidade.
- **HTTP transmitível**: Transporte moderno baseado em HTTP, suportando notificações e melhor escalabilidade. Recomendado para a maioria dos cenários de produção e nuvem.

### Tabela Comparativa

Veja a tabela comparativa abaixo para entender as diferenças entre esses mecanismos de transporte:

| Transporte         | Atualizações em Tempo Real | Transmissão | Escalabilidade | Caso de Uso                |
|--------------------|----------------------------|-------------|----------------|---------------------------|
| stdio              | Não                        | Não         | Baixa          | Ferramentas CLI locais     |
| SSE                | Sim                        | Sim         | Média          | Web, atualizações em tempo real |
| HTTP transmitível  | Sim                        | Sim         | Alta           | Nuvem, multi-cliente       |

> **Dica:** Escolher o transporte certo impacta o desempenho, escalabilidade e experiência do usuário. **HTTP transmitível** é recomendado para aplicações modernas, escaláveis e prontas para a nuvem.

Observe os transportes stdio e SSE que foram apresentados nos capítulos anteriores e como o HTTP transmitível é o transporte abordado neste capítulo.

## Transmissão: Conceitos e Motivação

Compreender os conceitos fundamentais e as motivações por trás da transmissão é essencial para implementar sistemas eficazes de comunicação em tempo real.

**Transmissão** é uma técnica em programação de rede que permite que os dados sejam enviados e recebidos em pequenos pedaços gerenciáveis ou como uma sequência de eventos, em vez de esperar que uma resposta inteira esteja pronta. Isso é especialmente útil para:

- Arquivos ou conjuntos de dados grandes.
- Atualizações em tempo real (ex.: chat, barras de progresso).
- Computações de longa duração onde você deseja manter o usuário informado.

Aqui está o que você precisa saber sobre transmissão em alto nível:

- Os dados são entregues progressivamente, não de uma vez só.
- O cliente pode processar os dados à medida que chegam.
- Reduz a latência percebida e melhora a experiência do usuário.

### Por que usar transmissão?

As razões para usar transmissão são as seguintes:

- Os usuários recebem feedback imediatamente, não apenas no final.
- Permite aplicações em tempo real e interfaces responsivas.
- Uso mais eficiente de recursos de rede e computação.

### Exemplo Simples: Servidor e Cliente de Transmissão HTTP

Aqui está um exemplo simples de como a transmissão pode ser implementada:

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

Este exemplo demonstra um servidor enviando uma série de mensagens ao cliente à medida que elas ficam disponíveis, em vez de esperar que todas as mensagens estejam prontas.

**Como funciona:**

- O servidor gera cada mensagem à medida que está pronta.
- O cliente recebe e imprime cada pedaço à medida que chega.

**Requisitos:**

- O servidor deve usar uma resposta de transmissão (ex.: `StreamingResponse` no FastAPI).
- O cliente deve processar a resposta como uma transmissão (`stream=True` em requests).
- O tipo de conteúdo geralmente é `text/event-stream` ou `application/octet-stream`.

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

**Notas sobre Implementação em Java:**

- Usa a pilha reativa do Spring Boot com `Flux` para transmissão.
- `ServerSentEvent` fornece transmissão de eventos estruturados com tipos de eventos.
- `WebClient` com `bodyToFlux()` permite consumo reativo de transmissão.
- `delayElements()` simula tempo de processamento entre eventos.
- Os eventos podem ter tipos (`info`, `result`) para melhor manipulação pelo cliente.

### Comparação: Transmissão Clássica vs Transmissão MCP

As diferenças entre como a transmissão funciona de maneira "clássica" e como funciona no MCP podem ser descritas assim:

| Característica          | Transmissão HTTP Clássica       | Transmissão MCP (Notificações)     |
|-------------------------|---------------------------------|------------------------------------|
| Resposta principal      | Fragmentada                    | Única, no final                   |
| Atualizações de progresso | Enviadas como pedaços de dados | Enviadas como notificações         |
| Requisitos do cliente   | Deve processar a transmissão   | Deve implementar manipulador de mensagens |
| Caso de uso             | Arquivos grandes, fluxos de tokens de IA | Progresso, logs, feedback em tempo real |

### Diferenças Principais Observadas

Além disso, aqui estão algumas diferenças principais:

- **Padrão de Comunicação:**
  - Transmissão HTTP clássica: Usa codificação de transferência fragmentada simples para enviar dados em pedaços.
  - Transmissão MCP: Usa um sistema de notificações estruturado com protocolo JSON-RPC.

- **Formato de Mensagem:**
  - HTTP clássico: Pedaços de texto simples com novas linhas.
  - MCP: Objetos LoggingMessageNotification estruturados com metadados.

- **Implementação do Cliente:**
  - HTTP clássico: Cliente simples que processa respostas de transmissão.
  - MCP: Cliente mais sofisticado com um manipulador de mensagens para processar diferentes tipos de mensagens.

- **Atualizações de Progresso:**
  - HTTP clássico: O progresso faz parte do fluxo de resposta principal.
  - MCP: O progresso é enviado via mensagens de notificação separadas enquanto a resposta principal vem no final.

### Recomendações

Há algumas recomendações ao escolher entre implementar transmissão clássica (como um endpoint que mostramos acima usando `/stream`) versus escolher transmissão via MCP.

- **Para necessidades simples de transmissão:** A transmissão HTTP clássica é mais simples de implementar e suficiente para necessidades básicas de transmissão.

- **Para aplicações complexas e interativas:** A transmissão MCP oferece uma abordagem mais estruturada com metadados mais ricos e separação entre notificações e resultados finais.

- **Para aplicações de IA:** O sistema de notificações do MCP é particularmente útil para tarefas de IA de longa duração onde você deseja manter os usuários informados sobre o progresso.

## Transmissão no MCP

Ok, então você já viu algumas recomendações e comparações até agora sobre a diferença entre transmissão clássica e transmissão no MCP. Vamos detalhar exatamente como você pode aproveitar a transmissão no MCP.

Compreender como a transmissão funciona dentro do framework MCP é essencial para construir aplicações responsivas que fornecem feedback em tempo real aos usuários durante operações de longa duração.

No MCP, a transmissão não se trata de enviar a resposta principal em pedaços, mas de enviar **notificações** ao cliente enquanto uma ferramenta está processando uma solicitação. Essas notificações podem incluir atualizações de progresso, logs ou outros eventos.

### Como funciona

O resultado principal ainda é enviado como uma única resposta. No entanto, notificações podem ser enviadas como mensagens separadas durante o processamento, atualizando assim o cliente em tempo real. O cliente deve ser capaz de manipular e exibir essas notificações.

## O que é uma Notificação?

Falamos "Notificação", o que isso significa no contexto do MCP?

Uma notificação é uma mensagem enviada do servidor ao cliente para informar sobre progresso, status ou outros eventos durante uma operação de longa duração. Notificações melhoram a transparência e a experiência do usuário.

Por exemplo, um cliente deve enviar uma notificação assim que o handshake inicial com o servidor for realizado.

Uma notificação se parece com isso como uma mensagem JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

As notificações pertencem a um tópico no MCP referido como ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Para que o logging funcione, o servidor precisa habilitá-lo como recurso/capacidade assim:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Dependendo do SDK usado, o logging pode estar habilitado por padrão ou você pode precisar habilitá-lo explicitamente na configuração do servidor.

Existem diferentes tipos de notificações:

| Nível      | Descrição                     | Caso de Uso Exemplo             |
|------------|-------------------------------|----------------------------------|
| debug      | Informações detalhadas de depuração | Pontos de entrada/saída de função |
| info       | Mensagens informativas gerais | Atualizações de progresso        |
| notice     | Eventos normais mas significativos | Alterações de configuração       |
| warning    | Condições de aviso            | Uso de recurso obsoleto          |
| error      | Condições de erro             | Falhas de operação               |
| critical   | Condições críticas            | Falhas de componentes do sistema |
| alert      | Ação deve ser tomada imediatamente | Corrupção de dados detectada     |
| emergency  | Sistema está inutilizável     | Falha completa do sistema        |

## Implementando Notificações no MCP

Para implementar notificações no MCP, você precisa configurar tanto o lado do servidor quanto o lado do cliente para lidar com atualizações em tempo real. Isso permite que sua aplicação forneça feedback imediato aos usuários durante operações de longa duração.

### Lado do Servidor: Enviando Notificações

Vamos começar com o lado do servidor. No MCP, você define ferramentas que podem enviar notificações enquanto processam solicitações. O servidor usa o objeto de contexto (geralmente `ctx`) para enviar mensagens ao cliente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

No exemplo anterior, a ferramenta `process_files` envia três notificações ao cliente enquanto processa cada arquivo. O método `ctx.info()` é usado para enviar mensagens informativas.

Além disso, para habilitar notificações, certifique-se de que seu servidor usa um transporte de transmissão (como `streamable-http`) e seu cliente implementa um manipulador de mensagens para processar notificações. Aqui está como configurar o servidor para usar o transporte `streamable-http`:

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

Para habilitar notificações no seu servidor MCP .NET, certifique-se de que está usando um transporte de transmissão:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lado do Cliente: Recebendo Notificações

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

No código anterior, a função `message_handler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa como uma mensagem regular do servidor. Também observe como o `ClientSession` é inicializado com o `message_handler` para lidar com notificações recebidas.

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

Neste exemplo .NET, a função `MessageHandler` verifica se a mensagem recebida é uma notificação. Se for, imprime a notificação; caso contrário, processa como uma mensagem regular do servidor. O `ClientSession` é inicializado com o manipulador de mensagens via `ClientSessionOptions`.

Para habilitar notificações, certifique-se de que seu servidor usa um transporte de transmissão (como `streamable-http`) e seu cliente implementa um manipulador de mensagens para processar notificações.

## Notificações de Progresso e Cenários

Esta seção explica o conceito de notificações de progresso no MCP, por que elas são importantes e como implementá-las usando HTTP transmitível. Você também encontrará uma tarefa prática para reforçar sua compreensão.

Notificações de progresso são mensagens em tempo real enviadas do servidor ao cliente durante operações de longa duração. Em vez de esperar que todo o processo termine, o servidor mantém o cliente atualizado sobre o status atual. Isso melhora a transparência, a experiência do usuário e facilita a depuração.

**Exemplo:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Por que Usar Notificações de Progresso?

Notificações de progresso são essenciais por várias razões:

- **Melhor experiência do usuário:** Os usuários veem atualizações à medida que o trabalho avança, não apenas no final.
- **Feedback em tempo real:** Os clientes podem exibir barras de progresso ou logs, tornando o aplicativo mais responsivo.
- **Facilidade de depuração e monitoramento:** Desenvolvedores e usuários podem ver onde um processo pode estar lento ou travado.

### Como Implementar Notificações de Progresso

Aqui está como você pode implementar notificações de progresso no MCP:

- **No servidor:** Use `ctx.info()` ou `ctx.log()` para enviar notificações à medida que cada item é processado. Isso envia uma mensagem ao cliente antes que o resultado principal esteja pronto.
- **No cliente:** Implemente um manipulador de mensagens que escute e exiba notificações à medida que chegam. Este manipulador distingue entre notificações e o resultado final.

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

Ao implementar servidores MCP com transportes baseados em HTTP, a segurança torna-se uma preocupação primordial que exige atenção cuidadosa a múltiplos vetores de ataque e mecanismos de proteção.

### Visão Geral

A segurança é crítica ao expor servidores MCP via HTTP. O HTTP transmitível introduz novas superfícies de ataque e requer configuração cuidadosa.

### Pontos Principais

- **Validação do Cabeçalho Origin**: Sempre valide o cabeçalho `Origin` para evitar ataques de rebinding DNS.
- **Vinculação ao Localhost**: Para desenvolvimento local, vincule servidores ao `localhost` para evitar exposição à internet pública.
- **Autenticação**: Implemente autenticação (ex.: chaves de API, OAuth) para implantações em produção.
- **CORS**: Configure políticas de Cross-Origin Resource Sharing (CORS) para restringir acesso.
- **HTTPS**: Use HTTPS em produção para criptografar o tráfego.

### Melhores Práticas

- Nunca confie em solicitações recebidas sem validação.
- Registre e monitore todos os acessos e erros.
- Atualize regularmente as dependências para corrigir vulnerabilidades de segurança.

### Desafios

- Equilibrar segurança com facilidade de desenvolvimento.
- Garantir compatibilidade com vários ambientes de cliente.

## Atualizando de SSE para HTTP Transmitível

Para aplicações que atualmente usam Server-Sent Events (SSE), migrar para HTTP transmitível oferece capacidades aprimoradas e melhor sustentabilidade a longo prazo para suas implementações MCP.

### Por que Atualizar?
Existem duas razões convincentes para fazer a atualização de SSE para HTTP Streamable:

- O HTTP Streamable oferece melhor escalabilidade, compatibilidade e suporte mais rico para notificações do que o SSE.
- É o transporte recomendado para novas aplicações MCP.

### Passos para Migração

Aqui está como pode migrar de SSE para HTTP Streamable nas suas aplicações MCP:

- **Atualize o código do servidor** para usar `transport="streamable-http"` em `mcp.run()`.
- **Atualize o código do cliente** para usar `streamablehttp_client` em vez do cliente SSE.
- **Implemente um manipulador de mensagens** no cliente para processar notificações.
- **Teste a compatibilidade** com ferramentas e fluxos de trabalho existentes.

### Manter a Compatibilidade

É recomendado manter a compatibilidade com clientes SSE existentes durante o processo de migração. Aqui estão algumas estratégias:

- Pode suportar tanto SSE como HTTP Streamable executando ambos os transportes em diferentes endpoints.
- Migre gradualmente os clientes para o novo transporte.

### Desafios

Certifique-se de abordar os seguintes desafios durante a migração:

- Garantir que todos os clientes sejam atualizados
- Lidar com diferenças na entrega de notificações

## Considerações de Segurança

A segurança deve ser uma prioridade ao implementar qualquer servidor, especialmente ao usar transportes baseados em HTTP como o HTTP Streamable no MCP.

Ao implementar servidores MCP com transportes baseados em HTTP, a segurança torna-se uma preocupação fundamental que exige atenção cuidadosa a múltiplos vetores de ataque e mecanismos de proteção.

### Visão Geral

A segurança é crítica ao expor servidores MCP via HTTP. O HTTP Streamable introduz novas superfícies de ataque e requer configuração cuidadosa.

Aqui estão algumas considerações importantes de segurança:

- **Validação do Header Origin**: Valide sempre o cabeçalho `Origin` para prevenir ataques de DNS rebinding.
- **Ligação ao Localhost**: Para desenvolvimento local, ligue os servidores ao `localhost` para evitar exposição à internet pública.
- **Autenticação**: Implemente autenticação (por exemplo, chaves API, OAuth) para implementações em produção.
- **CORS**: Configure políticas de Cross-Origin Resource Sharing (CORS) para restringir o acesso.
- **HTTPS**: Use HTTPS em produção para encriptar o tráfego.

### Melhores Práticas

Além disso, aqui estão algumas melhores práticas a seguir ao implementar segurança no seu servidor de streaming MCP:

- Nunca confie em pedidos recebidos sem validação.
- Registe e monitorize todos os acessos e erros.
- Atualize regularmente as dependências para corrigir vulnerabilidades de segurança.

### Desafios

Enfrentará alguns desafios ao implementar segurança em servidores de streaming MCP:

- Equilibrar segurança com facilidade de desenvolvimento
- Garantir compatibilidade com vários ambientes de cliente

### Tarefa: Construa a Sua Própria Aplicação MCP de Streaming

**Cenário:**
Construa um servidor e cliente MCP onde o servidor processa uma lista de itens (por exemplo, ficheiros ou documentos) e envia uma notificação para cada item processado. O cliente deve exibir cada notificação à medida que chega.

**Passos:**

1. Implemente uma ferramenta de servidor que processe uma lista e envie notificações para cada item.
2. Implemente um cliente com um manipulador de mensagens para exibir notificações em tempo real.
3. Teste a sua implementação executando tanto o servidor como o cliente e observe as notificações.

[Solution](./solution/README.md)

## Leituras Adicionais e Próximos Passos

Para continuar a sua jornada com streaming MCP e expandir o seu conhecimento, esta secção fornece recursos adicionais e próximos passos sugeridos para construir aplicações mais avançadas.

### Leituras Adicionais

- [Microsoft: Introdução ao HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS no ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Próximos Passos

- Experimente construir ferramentas MCP mais avançadas que utilizem streaming para análises em tempo real, chat ou edição colaborativa.
- Explore a integração do streaming MCP com frameworks frontend (React, Vue, etc.) para atualizações de interface em tempo real.
- Próximo: [Utilizar o AI Toolkit para VSCode](../07-aitk/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
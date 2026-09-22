# MCP Transportes Personalizados - Guia de Implementação Avançada

O Protocolo do Contexto do Modelo (MCP) permite implementações personalizadas de transporte para
ambientes especializados. Este guia avançado explora o Azure Event Grid e
Azure Event Hubs como padrões de arquitetura. Eles não são transportes MCP padrão
e exigem que ambos os pontos finais concordem com o mapeamento personalizado.

> **Âmbito MCP `2026-07-28`:** o protocolo atual não possui sessões a nível de protocolo,
> portanto, os transportes personalizados não devem depender de afinidade de sessão ou
> ordenação por sessão. Os cabeçalhos `Mcp-Method` e condicional `Mcp-Name` são
> requisitos do transporte HTTP Streamable padrão; um transporte não-HTTP
> precisa de um mapeamento equivalente e explicitamente acordado se intermediários tiverem que encaminhar
> sem decodificar o corpo JSON-RPC. Veja
> [O que mudou no MCP: A especificação 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Introdução

Os transportes padrão do MCP são stdio e HTTP Streamable. Alguns ambientes empresariais
utilizam um mapeamento personalizado para integrar com a infraestrutura de mensagens
existente, mas isso pode reduzir a interoperabilidade com hosts MCP e
SDKs que implementam apenas os transportes padrão.

Esta lição aplica os requisitos sem estado da Especificação MCP
`2026-07-28` aos serviços de mensagens Azure e
padrões estabelecidos de integração empresarial.

### **Arquitetura de Transporte MCP**

**Da Especificação MCP `2026-07-28`:**

- **Transportes Padrão**: stdio e HTTP Streamable
- **Transportes Personalizados**: Mapeamentos opcionais, específicos da implementação, acordados por
    ambos os pontos finais
- **Formato da Mensagem**: JSON-RPC 2.0 com extensões específicas MCP
- **Pedidos Autocontidos**: Não há sessão ou handshake do protocolo disponível
    para transportar estado entre pedidos

## Objetivos de Aprendizagem

No final desta lição avançada, será possível:

- **Compreender os Requisitos do Transporte Personalizado**: Implementar o protocolo MCP sobre qualquer camada de transporte mantendo a conformidade
- **Construir Transporte Azure Event Grid**: Criar servidores MCP orientados por eventos utilizando Azure Event Grid para escalabilidade sem servidor
- **Implementar Transporte Azure Event Hubs**: Projetar soluções MCP de alto débito utilizando Azure Event Hubs para streaming em tempo real
- **Aplicar Padrões Empresariais**: Integrar transportes personalizados com infraestrutura e modelos de segurança Azure existentes
- **Gerir Confiabilidade do Transporte**: Implementar durabilidade de mensagens, ordenação e tratamento de erros para cenários empresariais
- **Otimizar Performance**: Projetar soluções de transporte para requisitos de escala, latência e débito

## **Requisitos de Transporte**

### **Requisitos Centrais para MCP `2026-07-28`**

```yaml
Message Protocol:
  format: "JSON-RPC 2.0 with MCP extensions"
    correlation: "Match responses to requests by JSON-RPC id"
    state: "Each request must be self-contained"
  
Transport Layer:
  reliability: "Transport MUST handle connection failures gracefully"
  security: "Transport MUST support secure communication"
    identification: "Carry protocol version, capabilities, and identity per request"
  
Custom Transport:
    compliance: "Map the selected MCP revision without adding session assumptions"
  extensibility: "MAY add transport-specific features"
    interoperability: "Both endpoints MUST agree on the custom mapping"
```

## **Implementação do Transporte Azure Event Grid**

O Azure Event Grid oferece um serviço de roteamento de eventos serverless ideal para arquiteturas MCP orientadas a eventos. Esta implementação demonstra como construir sistemas MCP escaláveis e fracamente acoplados.

### **Visão Geral da Arquitetura**

```mermaid
graph TB
    Client[Cliente MCP] --> EG[Azure Event Grid]
    EG --> Server[Função do Servidor MCP]
    Server --> EG
    EG --> Client
    
    subgraph "Serviços Azure"
        EG
        Server
        KV[Cofre de Chaves]
        Monitor[Application Insights]
    end
```

### **Implementação em C# - Transporte Event Grid**

```csharp
using Azure.Messaging.EventGrid;
using Microsoft.Extensions.Azure;
using System.Text.Json;

public class EventGridMcpTransport : IMcpTransport
{
    private readonly EventGridPublisherClient _publisher;
    private readonly string _topicEndpoint;
    private readonly string _clientId;
    
    public EventGridMcpTransport(string topicEndpoint, string accessKey, string clientId)
    {
        _publisher = new EventGridPublisherClient(
            new Uri(topicEndpoint), 
            new AzureKeyCredential(accessKey));
        _topicEndpoint = topicEndpoint;
        _clientId = clientId;
    }
    
    public async Task SendMessageAsync(McpMessage message)
    {
        var eventGridEvent = new EventGridEvent(
            subject: $"mcp/{_clientId}",
            eventType: "MCP.MessageReceived",
            dataVersion: "1.0",
            data: JsonSerializer.Serialize(message))
        {
            Id = Guid.NewGuid().ToString(),
            EventTime = DateTimeOffset.UtcNow
        };
        
        await _publisher.SendEventAsync(eventGridEvent);
    }
    
    public async Task<McpMessage> ReceiveMessageAsync(CancellationToken cancellationToken)
    {
        // Event Grid is push-based, so implement webhook receiver
        // This would typically be handled by Azure Functions trigger
        throw new NotImplementedException("Use EventGridTrigger in Azure Functions");
    }
}

// Azure Function for receiving Event Grid events
[FunctionName("McpEventGridReceiver")]
public async Task<IActionResult> HandleEventGridMessage(
    [EventGridTrigger] EventGridEvent eventGridEvent,
    ILogger log)
{
    try
    {
        var mcpMessage = JsonSerializer.Deserialize<McpMessage>(
            eventGridEvent.Data.ToString());
        
        // Process MCP message
        var response = await _mcpServer.ProcessMessageAsync(mcpMessage);
        
        // Send response back via Event Grid
        await _transport.SendMessageAsync(response);
        
        return new OkResult();
    }
    catch (Exception ex)
    {
        log.LogError(ex, "Error processing Event Grid MCP message");
        return new BadRequestResult();
    }
}
```

### **Implementação em TypeScript - Transporte Event Grid**

```typescript
import { EventGridPublisherClient, AzureKeyCredential } from "@azure/eventgrid";
import { McpTransport, McpMessage } from "./mcp-types";

export class EventGridMcpTransport implements McpTransport {
    private publisher: EventGridPublisherClient;
    private clientId: string;
    
    constructor(
        private topicEndpoint: string,
        private accessKey: string,
        clientId: string
    ) {
        this.publisher = new EventGridPublisherClient(
            topicEndpoint,
            new AzureKeyCredential(accessKey)
        );
        this.clientId = clientId;
    }
    
    async sendMessage(message: McpMessage): Promise<void> {
        const event = {
            id: crypto.randomUUID(),
            source: `mcp-client-${this.clientId}`,
            type: "MCP.MessageReceived",
            time: new Date(),
            data: message
        };
        
        await this.publisher.sendEvents([event]);
    }
    
    // Receção orientada a eventos via Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // A implementação usaria o gatilho Event Grid das Azure Functions
        // Esta é uma interface conceptual para o receptor do webhook
    }
}

// Implementação Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Processar mensagem MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Enviar resposta via Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Implementação em Python - Transporte Event Grid**

```python
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential
import asyncio
import json
from typing import Callable, Optional
import uuid
from datetime import datetime

class EventGridMcpTransport:
    def __init__(self, topic_endpoint: str, access_key: str, client_id: str):
        self.client = EventGridPublisherClient(
            topic_endpoint, 
            AzureKeyCredential(access_key)
        )
        self.client_id = client_id
        self.message_handler: Optional[Callable] = None
    
    async def send_message(self, message: dict) -> None:
        """Send MCP message via Event Grid"""
        event = EventGridEvent(
            data=message,
            subject=f"mcp/{self.client_id}",
            event_type="MCP.MessageReceived",
            data_version="1.0"
        )
        
        await self.client.send(event)
    
    def on_message(self, handler: Callable[[dict], None]) -> None:
        """Register message handler for incoming events"""
        self.message_handler = handler

# Implementação do Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Analisar mensagem MCP do evento Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Processar mensagem MCP
        response = process_mcp_message(mcp_message)
        
        # Enviar resposta de volta via Event Grid
        # (A implementação criaria um novo cliente Event Grid)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Implementação do Transporte Azure Event Hubs**

O Azure Event Hubs oferece capacidades de streaming em tempo real e alto débito para cenários MCP que exigem baixa latência e elevado volume de mensagens.

### **Visão Geral da Arquitetura**

```mermaid
graph TB
    Client[Cliente MCP] --> EH[Azure Event Hubs]
    EH --> Server[Servidor MCP]
    Server --> EH
    EH --> Client
    
    subgraph "Funcionalidades do Event Hubs"
        Partition[Particionamento]
        Retention[Retenção de Mensagens]
        Scaling[Escalonamento Automático]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```

### **Implementação em C# - Transporte Event Hubs**

```csharp
using Azure.Messaging.EventHubs;
using Azure.Messaging.EventHubs.Producer;
using Azure.Messaging.EventHubs.Consumer;
using System.Text;

public class EventHubsMcpTransport : IMcpTransport, IDisposable
{
    private readonly EventHubProducerClient _producer;
    private readonly EventHubConsumerClient _consumer;
    private readonly string _consumerGroup;
    private readonly CancellationTokenSource _cancellationTokenSource;
    
    public EventHubsMcpTransport(
        string connectionString, 
        string eventHubName,
        string consumerGroup = "$Default")
    {
        _producer = new EventHubProducerClient(connectionString, eventHubName);
        _consumer = new EventHubConsumerClient(
            consumerGroup, 
            connectionString, 
            eventHubName);
        _consumerGroup = consumerGroup;
        _cancellationTokenSource = new CancellationTokenSource();
    }
    
    public async Task SendMessageAsync(McpMessage message)
    {
        var messageBody = JsonSerializer.Serialize(message);
        var eventData = new EventData(Encoding.UTF8.GetBytes(messageBody));
        
        // Add MCP-specific properties
        eventData.Properties.Add("MessageType", message.Method ?? "response");
        eventData.Properties.Add("MessageId", message.Id);
        eventData.Properties.Add("Timestamp", DateTimeOffset.UtcNow);
        
        await _producer.SendAsync(new[] { eventData });
    }
    
    public async Task StartReceivingAsync(
        Func<McpMessage, Task> messageHandler)
    {
        await foreach (PartitionEvent partitionEvent in _consumer.ReadEventsAsync(
            _cancellationTokenSource.Token))
        {
            try
            {
                var messageBody = Encoding.UTF8.GetString(
                    partitionEvent.Data.EventBody.ToArray());
                var mcpMessage = JsonSerializer.Deserialize<McpMessage>(messageBody);
                
                await messageHandler(mcpMessage);
            }
            catch (Exception ex)
            {
                // Handle deserialization or processing errors
                Console.WriteLine($"Error processing message: {ex.Message}");
            }
        }
    }
    
    public void Dispose()
    {
        _cancellationTokenSource?.Cancel();
        _producer?.DisposeAsync().AsTask().Wait();
        _consumer?.DisposeAsync().AsTask().Wait();
        _cancellationTokenSource?.Dispose();
    }
}
```

### **Implementação em TypeScript - Transporte Event Hubs**

```typescript
import { 
    EventHubProducerClient, 
    EventHubConsumerClient, 
    EventData 
} from "@azure/event-hubs";

export class EventHubsMcpTransport implements McpTransport {
    private producer: EventHubProducerClient;
    private consumer: EventHubConsumerClient;
    private isReceiving = false;
    
    constructor(
        private connectionString: string,
        private eventHubName: string,
        private consumerGroup: string = "$Default"
    ) {
        this.producer = new EventHubProducerClient(
            connectionString, 
            eventHubName
        );
        this.consumer = new EventHubConsumerClient(
            consumerGroup,
            connectionString,
            eventHubName
        );
    }
    
    async sendMessage(message: McpMessage): Promise<void> {
        const eventData: EventData = {
            body: JSON.stringify(message),
            properties: {
                messageType: message.method || "response",
                messageId: message.id,
                timestamp: new Date().toISOString()
            }
        };
        
        await this.producer.sendBatch([eventData]);
    }
    
    async startReceiving(
        messageHandler: (message: McpMessage) => Promise<void>
    ): Promise<void> {
        if (this.isReceiving) return;
        
        this.isReceiving = true;
        
        const subscription = this.consumer.subscribe({
            processEvents: async (events, context) => {
                for (const event of events) {
                    try {
                        const messageBody = event.body as string;
                        const mcpMessage: McpMessage = JSON.parse(messageBody);
                        
                        await messageHandler(mcpMessage);
                        
                        // Atualizar ponto de verificação para entrega pelo menos uma vez
                        await context.updateCheckpoint(event);
                    } catch (error) {
                        console.error("Error processing Event Hubs message:", error);
                    }
                }
            },
            processError: async (err, context) => {
                console.error("Event Hubs error:", err);
            }
        });
    }
    
    async close(): Promise<void> {
        this.isReceiving = false;
        await this.producer.close();
        await this.consumer.close();
    }
}
```

### **Implementação em Python - Transporte Event Hubs**

```python
from azure.eventhub import EventHubProducerClient, EventHubConsumerClient
from azure.eventhub import EventData
import json
import asyncio
from typing import Callable, Dict, Any
import logging

class EventHubsMcpTransport:
    def __init__(
        self, 
        connection_string: str, 
        eventhub_name: str,
        consumer_group: str = "$Default"
    ):
        self.producer = EventHubProducerClient.from_connection_string(
            connection_string, 
            eventhub_name=eventhub_name
        )
        self.consumer = EventHubConsumerClient.from_connection_string(
            connection_string,
            consumer_group=consumer_group,
            eventhub_name=eventhub_name
        )
        self.is_receiving = False
    
    async def send_message(self, message: Dict[str, Any]) -> None:
        """Send MCP message via Event Hubs"""
        event_data = EventData(json.dumps(message))
        
        # Adicionar propriedades específicas do MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Usar timestamp real
        }
        
        async with self.producer:
            event_data_batch = await self.producer.create_batch()
            event_data_batch.add(event_data)
            await self.producer.send_batch(event_data_batch)
    
    async def start_receiving(
        self, 
        message_handler: Callable[[Dict[str, Any]], None]
    ) -> None:
        """Start receiving MCP messages from Event Hubs"""
        if self.is_receiving:
            return
        
        self.is_receiving = True
        
        async with self.consumer:
            await self.consumer.receive(
                on_event=self._on_event_received(message_handler),
                starting_position="-1"  # Começar desde o início
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Analisar mensagem MCP do evento do Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Processar mensagem MCP
                await handler(mcp_message)
                
                # Atualizar ponto de verificação para entrega pelo menos uma vez
                await partition_context.update_checkpoint(event)
                
            except Exception as e:
                logging.error(f"Error processing Event Hubs message: {e}")
        
        return handle_event
    
    async def close(self) -> None:
        """Clean up transport resources"""
        self.is_receiving = False
        await self.producer.close()
        await self.consumer.close()
```

## **Padrões Avançados de Transporte**

### **Durabilidade e Confiabilidade da Mensagem**

```csharp
// Implementing message durability with retry logic
public class ReliableTransportWrapper : IMcpTransport
{
    private readonly IMcpTransport _innerTransport;
    private readonly RetryPolicy _retryPolicy;
    
    public async Task SendMessageAsync(McpMessage message)
    {
        await _retryPolicy.ExecuteAsync(async () =>
        {
            try
            {
                await _innerTransport.SendMessageAsync(message);
            }
            catch (TransportException ex) when (ex.IsRetryable)
            {
                // Log and retry
                throw;
            }
        });
    }
}
```

### **Integração de Segurança no Transporte**

```csharp
// Integrating Azure Key Vault for transport security
public class SecureTransportFactory
{
    private readonly SecretClient _keyVaultClient;
    
    public async Task<IMcpTransport> CreateEventGridTransportAsync()
    {
        var accessKey = await _keyVaultClient.GetSecretAsync("EventGridAccessKey");
        var topicEndpoint = await _keyVaultClient.GetSecretAsync("EventGridTopic");
        
        return new EventGridMcpTransport(
            topicEndpoint.Value.Value,
            accessKey.Value.Value,
            Environment.MachineName
        );
    }
}
```

### **Monitorização e Observabilidade do Transporte**

```csharp
// Adding telemetry to custom transports
public class ObservableTransport : IMcpTransport
{
    private readonly IMcpTransport _transport;
    private readonly ILogger _logger;
    private readonly TelemetryClient _telemetryClient;
    
    public async Task SendMessageAsync(McpMessage message)
    {
        using var activity = Activity.StartActivity("MCP.Transport.Send");
        activity?.SetTag("transport.type", "EventGrid");
        activity?.SetTag("message.method", message.Method);
        
        var stopwatch = Stopwatch.StartNew();
        
        try
        {
            await _transport.SendMessageAsync(message);
            
            _telemetryClient.TrackDependency(
                "EventGrid",
                "SendMessage",
                DateTime.UtcNow.Subtract(stopwatch.Elapsed),
                stopwatch.Elapsed,
                true
            );
        }
        catch (Exception ex)
        {
            _telemetryClient.TrackException(ex);
            throw;
        }
    }
}
```

## **Cenários de Integração Empresarial**

### **Cenário 1: Processamento Distribuído MCP**

Utilização do Azure Event Grid para distribuir pedidos MCP por múltiplos nós de processamento:

```yaml
Architecture:
  - MCP Client sends requests to Event Grid topic
  - Multiple Azure Functions subscribe to process different tool types
  - Results aggregated and returned via separate response topic
  
Benefits:
  - Horizontal scaling based on message volume
  - Fault tolerance through redundant processors
  - Cost optimization with serverless compute
```

### **Cenário 2: Streaming MCP em Tempo Real**

Utilização do Azure Event Hubs para interações MCP de alta frequência:

```yaml
Architecture:
  - MCP Client streams continuous requests via Event Hubs
  - Stream Analytics processes and routes messages
  - Multiple consumers handle different aspect of processing
  
Benefits:
  - Low latency for real-time scenarios
  - High throughput for batch processing
  - Built-in partitioning for parallel processing
```

### **Cenário 3: Arquitetura de Transporte Híbrida**

Combinação de vários transportes para diferentes casos de uso:

```csharp
public class HybridMcpTransport : IMcpTransport
{
    private readonly IMcpTransport _realtimeTransport; // Event Hubs
    private readonly IMcpTransport _batchTransport;    // Event Grid
    private readonly IMcpTransport _fallbackTransport; // HTTP Streaming
    
    public async Task SendMessageAsync(McpMessage message)
    {
        // Route based on message characteristics
        var transport = message.Method switch
        {
            "tools/call" when IsRealtime(message) => _realtimeTransport,
            "resources/read" when IsBatch(message) => _batchTransport,
            _ => _fallbackTransport
        };
        
        await transport.SendMessageAsync(message);
    }
}
```

## **Otimização de Performance**

### **Agrupamento de Mensagens para Event Grid**

```csharp
public class BatchingEventGridTransport : IMcpTransport
{
    private readonly List<McpMessage> _messageBuffer = new();
    private readonly Timer _flushTimer;
    private const int MaxBatchSize = 100;
    
    public async Task SendMessageAsync(McpMessage message)
    {
        lock (_messageBuffer)
        {
            _messageBuffer.Add(message);
            
            if (_messageBuffer.Count >= MaxBatchSize)
            {
                _ = Task.Run(FlushMessages);
            }
        }
    }
    
    private async Task FlushMessages()
    {
        List<McpMessage> toSend;
        lock (_messageBuffer)
        {
            toSend = new List<McpMessage>(_messageBuffer);
            _messageBuffer.Clear();
        }
        
        if (toSend.Any())
        {
            var events = toSend.Select(CreateEventGridEvent);
            await _publisher.SendEventsAsync(events);
        }
    }
}
```

### **Estratégia de Particionamento para Event Hubs**

```csharp
public class PartitionedEventHubsTransport : IMcpTransport
{
    public async Task SendMessageAsync(McpMessage message)
    {
        // Partition by client ID for session affinity
        var partitionKey = ExtractClientId(message);
        
        var eventData = new EventData(JsonSerializer.SerializeToUtf8Bytes(message))
        {
            PartitionKey = partitionKey
        };
        
        await _producer.SendAsync(new[] { eventData });
    }
}
```

## **Testar Transportes Personalizados**

### **Testes Unitários com Test Doubles**

```csharp
[Test]
public async Task EventGridTransport_SendMessage_PublishesCorrectEvent()
{
    // Arrange
    var mockPublisher = new Mock<EventGridPublisherClient>();
    var transport = new EventGridMcpTransport(mockPublisher.Object);
    var message = new McpMessage { Method = "tools/list", Id = "test-123" };
    
    // Act
    await transport.SendMessageAsync(message);
    
    // Assert
    mockPublisher.Verify(
        x => x.SendEventAsync(
            It.Is<EventGridEvent>(e => 
                e.EventType == "MCP.MessageReceived" &&
                e.Subject == "mcp/test-client"
            )
        ),
        Times.Once
    );
}
```

### **Testes de Integração com Azure Test Containers**

```csharp
[Test]
public async Task EventHubsTransport_IntegrationTest()
{
    // Using Testcontainers for integration testing
    var eventHubsContainer = new EventHubsContainer()
        .WithEventHub("test-hub");
    
    await eventHubsContainer.StartAsync();
    
    var transport = new EventHubsMcpTransport(
        eventHubsContainer.GetConnectionString(),
        "test-hub"
    );
    
    // Test message round-trip
    var sentMessage = new McpMessage { Method = "test", Id = "123" };
    McpMessage receivedMessage = null;
    
    await transport.StartReceivingAsync(msg => {
        receivedMessage = msg;
        return Task.CompletedTask;
    });
    
    await transport.SendMessageAsync(sentMessage);
    await Task.Delay(1000); // Allow for message processing
    
    Assert.That(receivedMessage?.Id, Is.EqualTo("123"));
}
```

## **Boas Práticas e Diretrizes**

### **Princípios de Design de Transporte**

1. **Idempotência**: Assegurar que o processamento de mensagens é idempotente para lidar com duplicados
2. **Tratamento de Erros**: Implementar tratamento de erros completo e filas de mensagens mortas (dead letter)
3. **Monitorização**: Adicionar telemetria detalhada e verificações de integridade
4. **Segurança**: Usar identidades geridas e acesso pelo princípio do privilégio mínimo
5. **Performance**: Projetar para os seus requisitos específicos de latência e débito

### **Recomendações Específicas Azure**

1. **Utilizar Identidade Gerida**: Evitar strings de conexão em produção
2. **Implementar Circuit Breakers**: Proteger contra falhas nos serviços Azure
3. **Monitorizar Custos**: Acompanhar volume de mensagens e custos de processamento
4. **Planear para Escala**: Projetar estratégias de particionamento e escalabilidade desde cedo
5. **Testar Rigorosamente**: Usar Azure DevTest Labs para testes abrangentes

## **Conclusão**

Transportes MCP personalizados permitem cenários empresariais poderosos utilizando os serviços de mensagens Azure. Ao implementar os transportes Event Grid ou Event Hubs, pode criar soluções MCP escaláveis e fiáveis que se integram perfeitamente com a infraestrutura Azure já existente.

Os exemplos fornecidos demonstram padrões prontos para produção para implementar transportes personalizados mantendo a conformidade com o protocolo MCP e as melhores práticas Azure.

## **Recursos Adicionais**

- [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Documentação Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Documentação Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Evento Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK para .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK para TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK para Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Este guia foca-se em padrões de arquitetura personalizados. Valide o protocolo

> comportamento face à [Especificação MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/),
> e validar a utilização do Azure face aos seus requisitos e limites de serviço.*


## O que vem a seguir
- [6. Contribuições da Comunidade](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
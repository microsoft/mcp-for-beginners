# MCP Custom Transports - Guida Avanzata all'Implementazione

Il Model Context Protocol (MCP) offre flessibilità nei meccanismi di trasporto, consentendo implementazioni personalizzate per ambienti aziendali specializzati. Questa guida avanzata esplora implementazioni di trasporti personalizzati utilizzando Azure Event Grid e Azure Event Hubs come esempi pratici per costruire soluzioni MCP scalabili e native per il cloud.

## Introduzione

Sebbene i trasporti standard di MCP (stdio e streaming HTTP) soddisfino la maggior parte dei casi d'uso, gli ambienti aziendali spesso richiedono meccanismi di trasporto specializzati per migliorare scalabilità, affidabilità e integrazione con l'infrastruttura cloud esistente. I trasporti personalizzati consentono a MCP di sfruttare servizi di messaggistica cloud-native per comunicazioni asincrone, architetture event-driven e elaborazione distribuita.

Questa lezione esplora implementazioni avanzate di trasporti basate sulla più recente specifica MCP (2025-11-25), servizi di messaggistica Azure e pattern consolidati di integrazione aziendale.

### **Architettura del Trasporto MCP**

**Dalla Specifica MCP (2025-11-25):**

- **Trasporti Standard**: stdio (consigliato), streaming HTTP (per scenari remoti)
- **Trasporti Personalizzati**: Qualsiasi trasporto che implementi il protocollo di scambio messaggi MCP
- **Formato Messaggi**: JSON-RPC 2.0 con estensioni specifiche MCP
- **Comunicazione Bidirezionale**: Comunicazione full duplex richiesta per notifiche e risposte

## Obiettivi di Apprendimento

Al termine di questa lezione avanzata, sarai in grado di:

- **Comprendere i Requisiti dei Trasporti Personalizzati**: Implementare il protocollo MCP su qualsiasi livello di trasporto mantenendo la conformità
- **Costruire un Trasporto Azure Event Grid**: Creare server MCP event-driven usando Azure Event Grid per scalabilità serverless
- **Implementare un Trasporto Azure Event Hubs**: Progettare soluzioni MCP ad alto throughput usando Azure Event Hubs per streaming in tempo reale
- **Applicare Pattern Aziendali**: Integrare trasporti personalizzati con infrastruttura e modelli di sicurezza Azure esistenti
- **Gestire l'Affidabilità del Trasporto**: Implementare durabilità dei messaggi, ordinamento e gestione degli errori per scenari aziendali
- **Ottimizzare le Prestazioni**: Progettare soluzioni di trasporto per requisiti di scala, latenza e throughput

## **Requisiti del Trasporto**

### **Requisiti Core dalla Specifica MCP (2025-11-25):**

```yaml
Message Protocol:
  format: "JSON-RPC 2.0 with MCP extensions"
  bidirectional: "Full duplex communication required"
  ordering: "Message ordering must be preserved per session"
  
Transport Layer:
  reliability: "Transport MUST handle connection failures gracefully"
  security: "Transport MUST support secure communication"
  identification: "Each session MUST have unique identifier"
  
Custom Transport:
  compliance: "MUST implement complete MCP message exchange"
  extensibility: "MAY add transport-specific features"
  interoperability: "MUST maintain protocol compatibility"
```

## **Implementazione del Trasporto Azure Event Grid**

Azure Event Grid fornisce un servizio di routing eventi serverless ideale per architetture MCP event-driven. Questa implementazione dimostra come costruire sistemi MCP scalabili e loosely-coupled.

### **Panoramica dell'Architettura**

```mermaid
graph TB
    Client[MCP Client] --> EG[Azure Event Grid]
    EG --> Server[Funzione Server MCP]
    Server --> EG
    EG --> Client
    
    subgraph "Servizi Azure"
        EG
        Server
        KV[Key Vault]
        Monitor[Application Insights]
    end
```
### **Implementazione C# - Trasporto Event Grid**

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

### **Implementazione TypeScript - Trasporto Event Grid**

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
    
    // Ricezione basata su eventi tramite Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // L'implementazione utilizzerebbe il trigger Event Grid di Azure Functions
        // Questa è un'interfaccia concettuale per il ricevitore webhook
    }
}

// Implementazione di Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Elabora il messaggio MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Invia la risposta tramite Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Implementazione Python - Trasporto Event Grid**

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

# Implementazione di Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Analizza il messaggio MCP dall'evento Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Elabora il messaggio MCP
        response = process_mcp_message(mcp_message)
        
        # Invia la risposta tramite Event Grid
        # (L'implementazione creerebbe un nuovo client Event Grid)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Implementazione del Trasporto Azure Event Hubs**

Azure Event Hubs offre capacità di streaming in tempo reale ad alto throughput per scenari MCP che richiedono bassa latenza e alto volume di messaggi.

### **Panoramica dell'Architettura**

```mermaid
graph TB
    Client[MCP Client] --> EH[Azure Event Hubs]
    EH --> Server[MCP Server]
    Server --> EH
    EH --> Client
    
    subgraph "Funzionalità di Event Hubs"
        Partition[Partizionamento]
        Retention[Conservazione dei Messaggi]
        Scaling[Scalabilità Automatica]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **Implementazione C# - Trasporto Event Hubs**

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

### **Implementazione TypeScript - Trasporto Event Hubs**

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
                        
                        // Aggiorna il checkpoint per la consegna almeno una volta
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

### **Implementazione Python - Trasporto Event Hubs**

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
        
        # Aggiungi proprietà specifiche MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Usa il timestamp reale
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
                starting_position="-1"  # Inizia dall'inizio
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Analizza il messaggio MCP dall'evento di Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Elabora il messaggio MCP
                await handler(mcp_message)
                
                # Aggiorna il checkpoint per la consegna almeno una volta
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

## **Pattern Avanzati di Trasporto**

### **Durabilità e Affidabilità dei Messaggi**

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

### **Integrazione della Sicurezza del Trasporto**

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

### **Monitoraggio e Osservabilità del Trasporto**

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

## **Scenari di Integrazione Aziendale**

### **Scenario 1: Elaborazione MCP Distribuita**

Utilizzo di Azure Event Grid per distribuire richieste MCP su più nodi di elaborazione:

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

### **Scenario 2: Streaming MCP in Tempo Reale**

Utilizzo di Azure Event Hubs per interazioni MCP ad alta frequenza:

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

### **Scenario 3: Architettura di Trasporto Ibrida**

Combinazione di più trasporti per diversi casi d'uso:

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

## **Ottimizzazione delle Prestazioni**

### **Batching dei Messaggi per Event Grid**

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

### **Strategia di Partizionamento per Event Hubs**

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

## **Test dei Trasporti Personalizzati**

### **Test Unitari con Test Doubles**

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

### **Test di Integrazione con Azure Test Containers**

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

## **Best Practices e Linee Guida**

### **Principi di Progettazione del Trasporto**

1. **Idempotenza**: Assicurare che l'elaborazione dei messaggi sia idempotente per gestire duplicati
2. **Gestione degli Errori**: Implementare gestione completa degli errori e code di messaggi non recapitati
3. **Monitoraggio**: Aggiungere telemetria dettagliata e controlli di integrità
4. **Sicurezza**: Usare identità gestite e accesso con privilegi minimi
5. **Prestazioni**: Progettare per i requisiti specifici di latenza e throughput

### **Raccomandazioni Specifiche per Azure**

1. **Usare Identità Gestite**: Evitare stringhe di connessione in produzione
2. **Implementare Circuit Breaker**: Proteggersi da interruzioni dei servizi Azure
3. **Monitorare i Costi**: Tenere traccia del volume messaggi e costi di elaborazione
4. **Pianificare la Scalabilità**: Progettare strategie di partizionamento e scaling in anticipo
5. **Testare Approfonditamente**: Usare Azure DevTest Labs per test completi

## **Conclusione**

I trasporti MCP personalizzati abilitano potenti scenari aziendali utilizzando i servizi di messaggistica Azure. Implementando trasporti Event Grid o Event Hubs, puoi costruire soluzioni MCP scalabili e affidabili che si integrano perfettamente con l'infrastruttura Azure esistente.

Gli esempi forniti dimostrano pattern pronti per la produzione per implementare trasporti personalizzati mantenendo la conformità al protocollo MCP e le best practice Azure.

## **Risorse Aggiuntive**

- [Specifiche MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Documentazione Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Documentazione Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK per .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK per TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK per Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Questa guida si concentra su pattern di implementazione pratici per sistemi MCP di produzione. Verifica sempre le implementazioni di trasporto rispetto ai tuoi requisiti specifici e ai limiti dei servizi Azure.*
> **Standard Attuale**: Questa guida riflette i requisiti di trasporto e i pattern avanzati per ambienti aziendali della [Specifiche MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/).


## Cosa c'è dopo
- [6. Contributi della Comunità](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
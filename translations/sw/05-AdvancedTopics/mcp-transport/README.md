# MCP Usafirishaji wa Kipekee - Mwongozo wa Utekelezaji wa Juu

Itifaki ya Muktadha wa Mfano (MCP) inaruhusu utekelezaji wa usafirishaji wa kipekee kwa
mazingira maalum. Mwongozo huu wa juu unachunguza Azure Event Grid na
Azure Event Hubs kama mifano ya usanifu. Sio usafirishaji wa kawaida wa MCP
na zinahitaji pande zote mbili kukubaliana juu ya ramani ya kipekee.

> **Eneo la MCP `2026-07-28`:** itifaki ya sasa haina vikao vya ngazi ya itifaki,
> kwa hivyo usafirishaji wa kipekee hautegemei uhusiano wa kikao au
> upangaji kwa kila kikao. Vichwa `Mcp-Method` na `Mcp-Name` masharti
> ni mahitaji ya usafirishaji wa kawaida wa Streamable HTTP; usafirishaji usio wa HTTP
> unahitaji ramani sawa, iliyokubaliwa wazi ikiwa njia za kati zinapaswa kupeleka
> bila kufungua mwili wa JSON-RPC. Angalia
> [Nini Kimebadilika katika MCP: Maelezo ya 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Utangulizi

Usafirishaji wa kawaida wa MCP ni stdio na Streamable HTTP. Baadhi ya
mazingira ya biashara hutumia ramani za kipekee kuunganishwa na miundombinu ya
ujumbe iliyopo, lakini kufanya hivyo kunaweza kupunguza ufanisi wa ushirikiano na wenyeji wa MCP na
SDKs zinazotekeleza usafirishaji wa kawaida tu.

Somo hili linaweka mahitaji yasiyo ya hali ya MCP Specification
`2026-07-28` kwa huduma za ujumbe za Azure na mifano iliyothibitishwa ya ushirikiano wa biashara.


### **Usanifu wa Usafirishaji wa MCP**

**Kutoka MCP Specification `2026-07-28`:**

- **Usafirishaji wa Kawaida**: stdio na Streamable HTTP
- **Usafirishaji wa Kipekee**: Hiari, ramani maalum za utekelezaji zinazokubaliana na
    pande zote mbili
- **Muundo wa Ujumbe**: JSON-RPC 2.0 na nyongeza za MCP maalum
- **Maombi Yenye Hali Yenyewe**: Hakuna kikao cha itifaki au salamu inapatikana
    kubeba hali kati ya maombi

## Malengo ya Kujifunza

Kufikia mwisho wa somo hili la juu, utaweza:

- **Kuelewa Mahitaji ya Usafirishaji wa Kipekee**: Tekeleza itifaki ya MCP juu ya safu yoyote ya usafirishaji huku ukizingatia kufuata sheria
- **Kujenga Usafirishaji wa Azure Event Grid**: Unda seva za MCP zinazotegemea matukio kwa upanuaji usio na seva
- **Kutekeleza Usafirishaji wa Azure Event Hubs**: Tengeneza suluhisho za MCP zenye mtiririko mkubwa kwa kutumia Azure Event Hubs kwa mtiririko wa wakati halisi
- **Kutumia Mifano ya Biashara**: Unganisha usafirishaji wa kipekee na miundombinu ya Azure iliyopo na mifumo ya usalama
- **Kushughulikia Uaminifu wa Usafirishaji**: Tekeleza uendelevu wa ujumbe, upangaji, na utatuzi wa makosa kwa matukio ya biashara
- **Kuboresha Utendaji**: Tengeneza suluhisho za usafirishaji kwa ukubwa, ucheleweshaji, na mahitaji ya mtiririko

## **Mahitaji ya Usafirishaji**

### **Mahitaji Muhimu kwa MCP `2026-07-28`**

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

## **Utekelezaji wa Usafirishaji wa Azure Event Grid**

Azure Event Grid hutoa huduma ya kusafirisha matukio isiyo na seva bora kwa usanifu wa MCP unaotegemea matukio. Utekelezaji huu unaonyesha jinsi ya kujenga mifumo ya MCP inayoweza upanuzi kwa urahisi, isiyoshikamana sana.

### **Muhtasari wa Usanifu**

```mermaid
graph TB
    Client[Mteja wa MCP] --> EG[Azure Event Grid]
    EG --> Server[Kazi ya Seva ya MCP]
    Server --> EG
    EG --> Client
    
    subgraph "Huduma za Azure"
        EG
        Server
        KV[Hazina ya Funguo]
        Monitor[Uchunguzi wa Programu]
    end
```

### **Utekelezaji wa C# - Usafirishaji wa Event Grid**

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

### **Utekelezaji wa TypeScript - Usafirishaji wa Event Grid**

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
    
    // Kupokea kwa matukio kupitia Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Utekelezaji ungefanya matumizi ya kichocheo cha Azure Functions Event Grid
        // Hii ni kiolesura cha dhana kwa mpokeaji wa webhook
    }
}

// Utekelezaji wa Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Kusindika ujumbe wa MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Tuma jibu kupitia Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Utekelezaji wa Python - Usafirishaji wa Event Grid**

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

# Utekelezaji wa Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Tumia ujumbe wa MCP kutoka kwa tukio la Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Chakata ujumbe wa MCP
        response = process_mcp_message(mcp_message)
        
        # Tuma jibu tena kupitia Event Grid
        # (Utekelezaji ungeunda mteja mpya wa Event Grid)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Utekelezaji wa Usafirishaji wa Azure Event Hubs**

Azure Event Hubs hutoa uwezo mkubwa wa mtiririko wa wakati halisi kwa matukio ya MCP yanayohitaji ucheleweshaji mdogo na wingi mkubwa wa ujumbe.

### **Muhtasari wa Usanifu**

```mermaid
graph TB
    Client[Mteja wa MCP] --> EH[Azure Event Hubs]
    EH --> Server[Seva ya MCP]
    Server --> EH
    EH --> Client
    
    subgraph "Vipengele vya Event Hubs"
        Partition[Kugawanya]
        Retention[Uhifadhi wa Ujumbe]
        Scaling[Uingizaji Pamoja wa Kiotomatiki]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```

### **Utekelezaji wa C# - Usafirishaji wa Event Hubs**

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

### **Utekelezaji wa TypeScript - Usafirishaji wa Event Hubs**

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
                        
                        // Sasisha alama ya ukaguzi kwa utoaji angalau mara moja
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

### **Utekelezaji wa Python - Usafirishaji wa Event Hubs**

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
        
        # Ongeza mali maalum za MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Tumia alama ya wakati halisi
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
                starting_position="-1"  # Anza kutoka mwanzo
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Tafsiri ujumbe wa MCP kutoka tukio la Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Sanifu ujumbe wa MCP
                await handler(mcp_message)
                
                # Sasisha alama ya ukaguzi kwa usafirishaji wa angalau mara moja
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

## **Mifano ya Usafirishaji wa Juu**

### **Uendelevu na Uaminifu wa Ujumbe**

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

### **Uunganishaji wa Usalama wa Usafirishaji**

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

### **Ufuatiliaji na Uchanganuzi wa Usafirishaji**

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

## **Matukio ya Ushirikiano wa Biashara**

### **Matukio 1: Usindikaji wa MCP Uliosambazwa**

Kutumia Azure Event Grid kusambaza maombi ya MCP kwa nodi nyingi za usindikaji:

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

### **Matukio 2: Mtiririko wa MCP wa Wakati Halisi**

Kutumia Azure Event Hubs kwa mwingiliano wa MCP wa mzunguko wa juu:

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

### **Matukio 3: Usanifu Mchanganyiko wa Usafirishaji**

Kuweka pamoja usafirishaji kadhaa kwa matumizi tofauti:

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

## **Uboreshaji wa Utendaji**

### **Kusanya Ujumbe kwa Event Grid**

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

### **Mikakati ya Mgawanyiko kwa Event Hubs**

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

## **Kujaribu Usafirishaji wa Kipekee**

### **Vipimo vya Unit kwa Vitisho vya Jaribio**

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

### **Vipimo vya Ushirikiano na Kontena za Jaribio za Azure**

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

## **Mazingira Bora na Miongozo**

### **Misingi ya Kubuni Usafirishaji**

1. **Idempotency**: Hakikisha usindikaji wa ujumbe hauleta mabadiliko mara nyingi kwa meza moja
2. **Kushughulikia Makosa**: Tekeleza usimamizi wa makosa kamili na foleni za barua zilizokatwa
3. **Ufuatiliaji**: Ongeza telemetry ya kina na ukaguzi wa afya
4. **Usalama**: Tumia vitambulisho vinavyosimamiwa na upatikanaji wa chini zaidi
5. **Utendaji**: Tengeneza kwa mahitaji yako ya ucheleweshaji na mtiririko

### **Mapendekezo Maalum ya Azure**

1. **Tumia Kitambulisho Kinachosimamiwa**: Epuka mistari ya muunganisho katika uzalishaji
2. **Tekeleza Vipinduaji vya Mzunguko (Circuit Breakers)**: Linda dhidi ya matatizo ya huduma za Azure
3. **Fuatilia Gharama**: Angalia kiwango cha ujumbe na gharama za usindikaji
4. **Panga Ukubwa**: Tengeneza mikakati ya kugawanya na kupanua mapema
5. **Jaribu kwa Kina**: Tumia maabara za Azure DevTest kwa vipimo vya kina

## **Hitimisho**

Usafirishaji wa MCP wa kipekee huwasaidia sana mtandao wa biashara kwa kutumia huduma za ujumbe za Azure. Kwa kutekeleza usafirishaji wa Event Grid au Event Hubs, unaweza kujenga suluhisho salama, za kuaminika za MCP zinazoungana vyema na miundombinu ya Azure iliyopo.

Mifano iliyotolewa inaonyesha mifano tayari kwa uzalishaji wa utekelezaji wa usafirishaji wa kipekee huku ukizingatia sheria za itifaki ya MCP na maagizo bora ya Azure.

## **Rasilimali Zaidi**

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure Event Grid Documentation](https://docs.microsoft.com/azure/event-grid/)
- [Azure Event Hubs Documentation](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK for TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Mwongozo huu unazingatia mifano ya usanifu wa kipekee. Thibitisha itifaki

> tabia dhidi ya [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/),
> na thibitisha matumizi ya Azure dhidi ya mahitaji yako na mipaka ya huduma.*


## Nini Kifuatacho
- [6. Michango ya Jamii](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
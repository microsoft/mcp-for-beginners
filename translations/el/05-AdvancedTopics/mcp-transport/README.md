# MCP Προσαρμοσμένα Μεταφορικά Μέσα - Οδηγός Προχωρημένης Υλοποίησης

Το Πρωτόκολλο Πλαισίου Μοντέλου (MCP) επιτρέπει προσαρμοσμένες υλοποιήσεις μεταφοράς για
εξειδικευμένα περιβάλλοντα. Αυτός ο προχωρημένος οδηγός εξερευνά το Azure Event Grid και
το Azure Event Hubs ως πρότυπα αρχιτεκτονικής. Δεν είναι τυπικά μέσα μεταφοράς MCP
και απαιτούν να συμφωνούν και οι δύο άκρες σχετικά με τον προσαρμοσμένο χάρτη.

> **Πεδίο MCP `2026-07-28`:** το τρέχον πρωτόκολλο δεν έχει επίπεδο
> συνεδριών, οπότε τα προσαρμοσμένα μέσα μεταφοράς δεν πρέπει να βασίζονται σε
> αφοσίωση συνεδρίας ή
> σειρά ανά συνεδρία. Οι κεφαλίδες `Mcp-Method` και η προϋποθετική `Mcp-Name` είναι
> απαιτήσεις του τυπικού Streamable HTTP μεταφορικού μέσου· ένα μη HTTP μέσο
> χρειάζεται ισοδύναμο, ρητά συμφωνημένο χάρτη αν ενδιάμεσοι πρέπει να δρομολογούν
> χωρίς να αποκωδικοποιούν το σώμα JSON-RPC. Δείτε




Τα τυπικά μέσα μεταφοράς του MCP είναι τα stdio και Streamable HTTP. Ορισμένα επιχειρησιακά
περιβάλλοντα χρησιμοποιούν προσαρμοσμένο χάρτη για ενσωμάτωση με υπάρχουσα υποδομή
μηνυμάτων, αλλά αυτό μπορεί να μειώσει τη διαλειτουργικότητα με MCP hosts και


Αυτό το μάθημα εφαρμόζει τις απαιτήσεις χωρίς κατάσταση της Προδιαγραφής MCP
`2026-07-28` στις υπηρεσίες μηνυμάτων Azure και σε καθιερωμένα πρότυπα






- **Τυπικά μέσα μεταφοράς**: stdio και Streamable HTTP
- **Προσαρμοσμένα μέσα μεταφοράς**: Προαιρετικά, ειδικά υλοποίησης χαρτογραφήσεις που συμφωνούν
    και οι δύο άκρες
- **Μορφή Μηνύματος**: JSON-RPC 2.0 με επεκτάσεις ειδικές για MCP
- **Αυτεξούσιες Αιτήσεις**: Δεν υπάρχει συνεδρία ή χειραψία πρωτοκόλλου






- **Κατανοείτε τις Απαιτήσεις Προσαρμοσμένων Μεταφορών**: Υλοποιήστε το πρωτόκολλο MCP πάνω από οποιοδήποτε επίπεδο μεταφοράς διατηρώντας συμμόρφωση
- **Κατασκευάσετε Μεταφορά Azure Event Grid**: Δημιουργήστε MCP servers με βάση γεγονότα χρησιμοποιώντας το Azure Event Grid για μη διακοπτόμενη κλιμάκωση
- **Υλοποιήσετε Μεταφορά Azure Event Hubs**: Σχεδιάστε λύσεις MCP με υψηλή απόδοση χρησιμοποιώντας το Azure Event Hubs για πραγματικό χρόνο ροής
- **Εφαρμόσετε Επιχειρησιακά Πρότυπα**: Ενσωματώστε προσαρμοσμένες μεταφορές με υπάρχουσα υποδομή και μοντέλα ασφάλειας Azure
- **Διαχειριστείτε Αξιοπιστία Μεταφοράς**: Υλοποιήστε ανθεκτικότητα μηνυμάτων, σειρά και χειρισμό σφαλμάτων για επιχειρησιακά σενάρια






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







```mermaid
graph TB
    Client[Πελάτης MCP] --> EG[Πλέγμα Συμβάντων Azure]
    EG --> Server[Συνάρτηση Διακομιστή MCP]
    Server --> EG
    EG --> Client
    
    subgraph "Υπηρεσίες Azure"
        EG
        Server
        KV[Αποθήκη Κλειδιών]
        Monitor[Εφαρμογή Insights]
    end
```



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
    
    // Λήψη με ενεργοποίηση από γεγονότα μέσω Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Η υλοποίηση θα χρησιμοποιούσε τον Event Grid trigger των Azure Functions
        // Αυτή είναι μια εννοιολογική διεπαφή για τον δέκτη webhook
    }
}

// Υλοποίηση με Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Επεξεργασία μηνύματος MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Αποστολή απάντησης μέσω Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```



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

# Υλοποίηση Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Ανάλυση μηνύματος MCP από συμβάν Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Επεξεργασία μηνύματος MCP
        response = process_mcp_message(mcp_message)
        
        # Αποστολή απάντησης μέσω Event Grid
        # (Η υλοποίηση θα δημιουργούσε νέο πελάτη Event Grid)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```







```mermaid
graph TB
    Client[Πελάτης MCP] --> EH[Azure Event Hubs]
    EH --> Server[Διακομιστής MCP]
    Server --> EH
    EH --> Client
    
    subgraph "Χαρακτηριστικά Event Hubs"
        Partition[Κατανομή]
        Retention[Διατήρηση Μηνυμάτων]
        Scaling[Αυτόματη Κλιμάκωση]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```



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
                        
                        // Ενημέρωση σημείου ελέγχου για τουλάχιστον μία παράδοση
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
        
        # Προσθήκη ιδιοτήτων ειδικών για MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Χρήση πραγματικού χρονικού σήματος
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
                starting_position="-1"  # Ξεκίνα από την αρχή
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Ανάλυση μηνύματος MCP από γεγονός Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Επεξεργασία μηνύματος MCP
                await handler(mcp_message)
                
                # Ενημέρωση checkpoint για παράδοση τουλάχιστον μία φορά
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





1. **Αιδεοποστέρνωση**: Διασφαλίστε ότι η επεξεργασία μηνυμάτων είναι ασφαλής για διπλότυπα
2. **Χειρισμός Σφαλμάτων**: Υλοποιήστε ολοκληρωμένο χειρισμό σφαλμάτων και ουρές νεκρών μηνυμάτων
3. **Παρακολούθηση**: Προσθέστε λεπτομερή τηλεμετρία και ελέγχους υγείας
4. **Ασφάλεια**: Χρησιμοποιήστε διαχειριζόμενες ταυτότητες και πρόσβαση με το ελάχιστο προνόμιο




1. **Χρησιμοποιήστε Διαχειριζόμενη Ταυτότητα**: Αποφύγετε συμβολοσειρές σύνδεσης σε παραγωγή
2. **Υλοποιήστε Διακόπτες Κυκλώματος**: Προστασία έναντι διακοπών υπηρεσιών Azure
3. **Παρακολουθήστε Κόστη**: Παρακολουθήστε όγκο μηνυμάτων και κόστη επεξεργασίας
4. **Προγραμματίστε για Κλίμακα**: Σχεδιάστε στρατηγικές κατατμήσεων και κλιμάκωσης νωρίς










- [Προδιαγραφή MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Τεκμηρίωση Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Τεκμηρίωση Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK για .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK για TypeScript](https://github.com/Azure/azure-sdk-for-js)




> *Αυτός ο οδηγός εστιάζει σε προσαρμοσμένα πρότυπα αρχιτεκτονικής. Επικυρώστε τη συμπεριφορά του πρωτοκόλλου έναντι της [Προδιαγραφής MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/),
> και επικυρώστε τη χρήση Azure έναντι των απαιτήσεών σας και των ορίων υπηρεσίας.*


## Τι Ακολουθεί
- [6. Συνεισφορές Κοινότητας](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
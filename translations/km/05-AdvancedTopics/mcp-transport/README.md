# MCP ការដឹកជញ្ជូនផ្ទាល់ខ្លួន - មគ្គុទេសក៍អនុវត្តជាក់លាក់

Model Context Protocol (MCP) គឺផ្តល់ភាពយូរអង្វែងក្នុងយ៉ាងង់ដឹកជញ្ជូន ដោយអនុញ្ញាតឱ្យមានការអនុវត្តផ្ទាល់ខ្លួនសម្រាប់បរិយាកាសសហគ្រាសពិសេស។ មគ្គុទេសក៍អនុវត្តជាក់លាក់នេះស្វែងយល់អំពីការអនុវត្តការដឹកជញ្ជូនផ្ទាល់ខ្លួនដោយប្រើ Azure Event Grid និង Azure Event Hubs ជាឧទាហរណ៍ជាក់លាក់សម្រាប់បង្កើតដំណោះស្រាយ MCP អាចពង្រីកបាន និងមានមូលដ្ឋានលើពពក។

## ការណែនាំ

ក្នុងខណៈដែលការដឹកជញ្ជូនស្តង់ដារ MCP (stdio និង HTTP streaming) បម្រើប្រើសម្រាប់ការប្រើប្រាស់ភាគច្រើន បរិយាកាសសហគ្រាសជាច្រើនតម្រូវអោយមានយ៉ាងង់ដឹកជញ្ជូននានាដែលមានការពិសេសក្នុងការកែលម្អភាពអាចពង្រីកបាន, ភាពទុកចិត្ត និងឯកសារភាពជាមួយរចនាសម្ព័ន្ធពពកដែលមានស្រាប់។ ការដឹកជញ្ជូនផ្ទាល់ខ្លួនអាចឲ្យ MCP ប្រើសេវាទំនាក់ទំនងមួយមានមូលដ្ឋានលើពពកសម្រាប់ការទំនាក់ទំនងមិនជាប់គ្នា, វិចិត្រស្ថាបត្យកម្មដែលបង្កើតដោយព្រឹត្តិការណ៍, និងដំណើរការបែងចែក។

មេរៀននេះស្វែងយល់អំពីការអនុវត្តការដឹកជញ្ជូនជាក់លាក់សម្រាប់ MCP dựa trên ឯកសារលំដាប់ថ្មី (2025-11-25), សេវាទំនាក់ទំនង Azure និងគំរោងសហគ្រាសដែលបានបង្កើត។

### **រចនាសម្ព័ន្ធការដឹកជញ្ជូន MCP**

**ចេញពីឯកសារលំដាប់ MCP (2025-11-25):**

- **ការដឹកជញ្ជូនស្តង់ដារ**: stdio (បានណែនាំ), HTTP streaming (សម្រាប់ស្ថានភាពពីចម្ងាយ)
- **ការដឹកជញ្ជូនផ្ទាល់ខ្លួន**: ការដឹកជញ្ជូនណាមួយដែលអនុវត្តពិធីការប្តូរសារម៉ូដែល MCP
- **ទ្រង់ទ្រាយសារ**: JSON-RPC 2.0 ជាមួយនឹងបន្ថែមសម្រាប់ MCP
- **ការទំនាក់ទំនងទ្វេដំណាក់**: តម្រូវឲ្យមានការទំនាក់ទំនងទ្វេដំណាក់ល្អសម្រាប់ការជូនដំណឹង និងការឆ្លើយតប

## គោលបំណងរៀន

នៅចុងបញ្ចប់មេរៀនជាក់លាក់នេះ អ្នកនឹងអាច:

- **យល់ពីតម្រូវការដឹកជញ្ជូនផ្ទាល់ខ្លួន**: អនុវត្តពិធីការជាមួយ MCP លើស្រទាប់ដឹកជញ្ជូនណាមួយ ខណៈបន្តការអនុម័តនឹងតម្រូវការ
- **បង្កើត Azure Event Grid Transport**: បង្កើតម៉ាស៊ីនមេ MCP បង្កើតដោយព្រឹត្តិការណ៍ ដោយប្រើ Azure Event Grid សម្រាប់ការពង្រីកសេរី
- **អនុវត្ត Azure Event Hubs Transport**: រចនាបទដំណោះស្រាយ MCP ប្រើ Azure Event Hubs សម្រាប់អាងហ្សីនពេលវេលាជាក់លាក់
- **អនុវត្តគំរោងសហគ្រាស**: សរសេរត្រាប់តាមការដឹកជញ្ជូនផ្ទាល់ខ្លួនជាមួយរចនាសម្ព័ន្ធ Azure ដែលមានស្រាប់ និងគំរោងសុវត្ថិភាព
- **គ្រប់គ្រងភាពទុកចិត្តនៃការដឹកជញ្ជូន**: អនុវត្តអាចធន់ទ្រាំសារបាន, ការរៀបចំលំដាប់, និងការដោះស្រាយកំហុសសម្រាប់ស្ថានភាពសហគ្រាស
- **បង្ហាប់សមត្ថភាព**: រចនាដំណោះស្រាយដឹកជញ្ជូនសម្រាប់ការពង្រីក, ពេលវេលារាំង និងតម្រូវកម្រិត throughput

## **តម្រូវការផ្នែកដឹកជញ្ជូន**

### **តម្រូវការមូលដ្ឋានពីឯកសារលំដាប់ MCP (2025-11-25):**

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

## **ការអនុវត្តការដឹកជញ្ជូន Azure Event Grid**

Azure Event Grid ផ្តល់សេវាកម្មរុករកព្រឹត្តិការណ៍ឥតម៉ាស៊ីនមេ ដែលល្អបំផុតសម្រាប់រចនាសម្ព័ន្ធ MCP ដែលបង្កើតដោយព្រឹត្តិការណ៍។ ការអនុវត្តនេះបង្ហាញពីរបៀបបង្កើតប្រព័ន្ធ MCP ផ្ទាល់ខ្លួនដែលអាចពង្រីកបាន និងមានការត្រូវគ្នាក្នុងតម្លាភាព។

### **ទិដ្ឋភាពរចនាសម្ព័ន្ធ**

```mermaid
graph TB
    Client[MCP អតិថិជន] --> EG[Azure ហេតុការណ៍បណ្តាញ]
    EG --> Server[MCP ធ្វើមុខងារ​ម៉ាសីនមេ]
    Server --> EG
    EG --> Client
    
    subgraph "សេវាកម្ម Azure"
        EG
        Server
        KV[ទូរទស្សន៍ Key]
        Monitor[ការយល់ដឹងអំពីកម្មវិធី]
    end
```
### **ការអនុវត្ត C# - Azure Event Grid Transport**

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

### **ការអនុវត្ត TypeScript - Azure Event Grid Transport**

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
    
    // ទទួលដោយបណ្តាលមកពីព្រឹត្តិការណ៍តាមរយៈ Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // ការអនុវត្តន៍នឹងប្រើ Azure Functions Event Grid trigger
        // នេះគឺជាមុខងារសង្ខេបសម្រាប់អ្នកទទួល webhook
    }
}

// ការអនុវត្តន៍ Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // ដំណើរការជាមួយសារ MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // ផ្ញើការឆ្លើយតបទៅតាម Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **ការអនុវត្ត Python - Azure Event Grid Transport**

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

# ការអនុវត្ត Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # ដំណើរការសារ MCP ពីព្រឹត្តិការណ៍ Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # ដំណើរការសារ MCP
        response = process_mcp_message(mcp_message)
        
        # ផ្ញើការឆ្លើយតបត្រឡប់តាមរយៈ Event Grid
        # (ការអនុវត្តនឹងបង្កើតអតិថិជន Event Grid ថ្មី)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **ការអនុវត្តការដឹកជញ្ជូន Azure Event Hubs**

Azure Event Hubs ផ្តល់សមត្ថភាពស្ទ្រីមម៉ោងពិតប្រាកដ មានអត្រាច្រាសទិន្នន័យខ្ពស់សម្រាប់ស្ថានភាព MCP ត្រូវការពេលវេលាលឿន និងចំនួនសារខ្ពស់។

### **ទិដ្ឋភាពរចនាសម្ព័ន្ធ**

```mermaid
graph TB
    Client[MCP អតិថិជន] --> EH[Azure Event Hubs]
    EH --> Server[MCP ម៉ាស៊ីនបម្រើ]
    Server --> EH
    EH --> Client
    
    subgraph "លក្ខណៈពិសេស Event Hubs"
        Partition[ការបែងចែក]
        Retention[ការរក្សាអត្ថបទ]
        Scaling[ការកំណត់បរិមាណដោយស្វ័យប្រវត្តិ]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **ការអនុវត្ត C# - Azure Event Hubs Transport**

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

### **ការអនុវត្ត TypeScript - Azure Event Hubs Transport**

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
                        
                        // បន្ទាន់សម័យចំណុចត្រួតពិនិត្យសម្រាប់ការដឹកជញ្ជូនយ៉ាងតិចម្តងတည်း
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

### **ការអនុវត្ត Python - Azure Event Hubs Transport**

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
        
        # បន្ថែមលក្ខណៈពិសេសរបស់ MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # ប្រើពេលវេលាពិតប្រាកដ
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
                starting_position="-1"  # ចាប់ផ្តើមពីដើម
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # ពន្យល់សារបស់ MCP មកពីព្រឹត្តិការណ៍ Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # ដំណើរការសាររបស់ MCP
                await handler(mcp_message)
                
                # កែប្រែចំណុចផ្ទៀងផ្ទាត់សម្រាប់ការដឹកជញ្ជូនយ៉ាងហោចណាស់ម្តងមួយ
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

## **គំរោងដឹកជញ្ជូនជាក់លាក់**

### **ភាពអាចធន់ទ្រាំ និងភាពទុកចិត្តនៅក្នុងសារជាមូលដ្ឋាន**

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

### **ការតភ្ជាប់សុវត្ថិភាពនៃការដឹកជញ្ជូន**

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

### **ការត្រួតពិនិត្យ និងភាពមានរូបភាពនៃការដឹកជញ្ជូន**

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

## **ស្ថានភាពការសម្របសម្រួលសហគ្រាស**

### **ស្ថានភាព ១: ការបែងចែកដំណើរការប្រព័ន្ធ MCP**

ប្រើ Azure Event Grid សម្រាប់ចែកចាយសំណើ MCP ពហុរណបផ្ទាំងចតុកោណ:

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

### **ស្ថានភាព ២: ស្ទ្រីម MCP ពេលវេលាពិតប្រាកដ**

ប្រើ Azure Event Hubs សម្រាប់អន្តរកម្ម MCP ដែលមានអត្រាខ្ពស់:

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

### **ស្ថានភាព ៣: រចនាសម្ព័ន្ធដឹកជញ្ជូនចម្រុះ**

ជាមួយការបញ្ចូលការដឹកជញ្ជូនជាច្រើនសម្រាប់ការប្រើប្រាស់ខុសៗគ្នា:

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

## **ការបង្ហាប់សមត្ថភាព**

### **ការប្រមូលសារសម្រាប់ Event Grid**

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

### **យុទ្ធសាស្រ្តបែងចែកសម្រាប់ Event Hubs**

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

## **ការធ្វើតេស្តការដឹកជញ្ជូនផ្ទាល់ខ្លួន**

### **ធ្វើតេស្តឯកត្តា ជាមួយ Test Doubles**

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

### **ធ្វើតេស្តសម្របសម្រួលជាមួយ Azure Test Containers**

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

## **ការអនុវត្តល្អបំផុត និងមគ្គុទេសក៍**

### **គោលការណ៍រចនាការដឹកជញ្ជូន**

1. **ភាពធន់នឹងចម្លងឡើងវិញ**: ប្រាកដថាការព្យាបាលសារជាក់ទាន់យ៉ាង idempotent ដើម្បីដោះស្រាយចម្លងមួយច្រើន
2. **ការដោះស្រាយកំហុស**: អនុវត្តការដោះស្រាយកំហុសទូលំទូលាយ និងសារលិខិតស្ថិតក្នុង បញ្ជីសារឈប់ប្រើ
3. **ការត្រួតពិនិត្យ**: បន្ថែមទិន្នន័យ telemetry សម្រាប់ការត្រួតពិនិត្យសុខភាព
4. **សុវត្ថិភាព**: ប្រើអត្តសញ្ញាណគ្រប់គ្រង និងការចូលប្រើមានតែតិចបំផុត
5. **សមត្ថភាព**: រចនាសម្រាប់តម្រូវការពេលវេលារាំង និង throughput របស់អ្នក

### **ការណែនាំពិសេស Azure**

1. **ប្រើអត្តសញ្ញាណគ្រប់គ្រង**: រៀបចំឲ្យគ្មានសម្លេងខ្សែការតភ្ជាប់នៅក្នុងផលិតកម្ម
2. **អនុវត្តឧបករណ៍បំបែកសៀគ្វី**: ការពារប្រឆាំងនឹងការប្រឈមមុខខូចខាតសេវា Azure
3. **ត្រួតពិនិត្យការចំណាយ**: តាមដានបរិមាណសារ និងថ្លៃដើមនៃការបរិច្ឆេទ
4. **ផែនការសម្រាប់ការពង្រីក**: រចនាទ្រង់ទ្រាយបែងចែក និងយុទ្ធសាស្រ្តបង្កើនពីដំបូង
5. **ធ្វើតេស្តយ៉ាងពេញលេញ**: ប្រើ Azure DevTest Labs សម្រាប់ការធ្វើតេស្តទូលំទូលាយ

## **សេចក្ដីសង្ខេប**

ការដឹកជញ្ជូនផ្ទាល់ខ្លួន MCP អាចបង្កើតស្ថានភាពសហគ្រាសខ្លាំងមាឌដោយប្រើសេវាទំនាក់ទំនង Azure។ ដោយអនុវត្តការ Azure Event Grid ឬ Event Hubs transports អ្នកអាចបង្កើតដំណោះស្រាយ MCP អាចពង្រីកបាន និងទុកចិត្តសុវត្ថិភាពដែលរួមបញ្ចូលជាមួយរចនាសម្ព័ន្ធ Azure ដែលមានស្រាប់។

ឧទាហរណ៍ដែលបានផ្តល់ជូនបង្ហាញពីគំរោងត្រៀមប្រើផលិតកម្មសម្រាប់អនុវត្តដឹកជញ្ជូនផ្ទាល់ខ្លួន នៅពេលដែលរក្សាការអនុវត្ត protocol MCP និងការណែនាំល្អបំផុតរបស់ Azure។

## **ធនធានបន្ថែម**

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Azure Event Grid Documentation](https://docs.microsoft.com/azure/event-grid/)
- [Azure Event Hubs Documentation](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK for TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

---

> *មគ្គុទេសក៍នេះផ្តោតលើគំរោងអនុវត្តជាក់លាក់សម្រាប់ប្រព័ន្ធ MCP ផលិតកម្ម។ សូមតែងតែកំណត់នឹងធ្វើតេស្តការអនុវត្តន៍ការដឹកជញ្ជូនស្របតាមតម្រូវការពិសេសរបស់អ្នក និងដែនកំណត់សេវា Azure។*
> **លំដាប់ស្តង់ដា​បច្ចុប្បន្នកាល**៖ មគ្គុទេសក៍នេះបង្ហាញតាមតម្រូវការ [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) និងគំរោងដឹកជញ្ជូនជាក់លាក់សម្រាប់បរិយាកាសសហគ្រាស។

## អ្វីដែលត្រូវធ្វើបន្ទាប់
- [6. Community Contributions](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការសំដែងអការណ៍**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមជាភាសាមូលដ្ឋានគួរត្រូវបានចាត់ទុកជាឯកសារដើមដែលមានសក្ដានុពល។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្ដល់ការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកប្រែខុសប្រភេទណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
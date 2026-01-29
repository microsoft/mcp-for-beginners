# MCP कस्टम ट्रान्सपोर्ट्स - प्रगत अंमलबजावणी मार्गदर्शक

मॉडेल कॉन्टेक्स्ट प्रोटोकॉल (MCP) ट्रान्सपोर्ट यंत्रणांमध्ये लवचिकता प्रदान करतो, ज्यामुळे विशेषीकृत एंटरप्राइझ वातावरणांसाठी कस्टम अंमलबजावणी शक्य होते. हा प्रगत मार्गदर्शक Azure Event Grid आणि Azure Event Hubs चा वापर करून कस्टम ट्रान्सपोर्ट अंमलबजावणींचा अभ्यास करतो, जे स्केलेबल, क्लाउड-नेटिव्ह MCP सोल्यूशन्स तयार करण्यासाठी व्यावहारिक उदाहरणे आहेत.

## परिचय

जरी MCP चे मानक ट्रान्सपोर्ट्स (stdio आणि HTTP स्ट्रीमिंग) बहुतेक वापरासाठी उपयुक्त असले तरी, एंटरप्राइझ वातावरणांमध्ये सुधारित स्केलेबिलिटी, विश्वसनीयता आणि विद्यमान क्लाउड इन्फ्रास्ट्रक्चरशी एकत्रीकरणासाठी विशेष ट्रान्सपोर्ट यंत्रणांची गरज असते. कस्टम ट्रान्सपोर्ट्स MCP ला असिंक्रोनस संवाद, इव्हेंट-चालित आर्किटेक्चर्स आणि वितरित प्रक्रिया यासाठी क्लाउड-नेटिव्ह मेसेजिंग सेवा वापरण्याची परवानगी देतात.

हा धडा नवीनतम MCP स्पेसिफिकेशन (2025-11-25), Azure मेसेजिंग सेवा आणि स्थापित एंटरप्राइझ इंटिग्रेशन पॅटर्न्सवर आधारित प्रगत ट्रान्सपोर्ट अंमलबजावणींचा अभ्यास करतो.

### **MCP ट्रान्सपोर्ट आर्किटेक्चर**

**MCP स्पेसिफिकेशन (2025-11-25) नुसार:**

- **मानक ट्रान्सपोर्ट्स**: stdio (शिफारस केलेले), HTTP स्ट्रीमिंग (रिमोट परिस्थितीसाठी)
- **कस्टम ट्रान्सपोर्ट्स**: कोणताही ट्रान्सपोर्ट जो MCP मेसेज एक्सचेंज प्रोटोकॉल अंमलात आणतो
- **मेसेज फॉरमॅट**: JSON-RPC 2.0 MCP-विशिष्ट विस्तारांसह
- **द्विदिश संवाद**: सूचना आणि प्रतिसादांसाठी पूर्ण डुप्लेक्स संवाद आवश्यक

## शिक्षण उद्दिष्टे

या प्रगत धड्याच्या शेवटी, आपण सक्षम असाल:

- **कस्टम ट्रान्सपोर्ट आवश्यकता समजून घेणे**: कोणत्याही ट्रान्सपोर्ट लेयरवर MCP प्रोटोकॉल अंमलात आणणे आणि अनुपालन राखणे
- **Azure Event Grid ट्रान्सपोर्ट तयार करणे**: सर्व्हरलेस स्केलेबिलिटीसाठी Azure Event Grid वापरून इव्हेंट-चालित MCP सर्व्हर तयार करणे
- **Azure Event Hubs ट्रान्सपोर्ट अंमलबजावणी**: रिअल-टाइम स्ट्रीमिंगसाठी Azure Event Hubs वापरून उच्च-थ्रूपुट MCP सोल्यूशन्स डिझाइन करणे
- **एंटरप्राइझ पॅटर्न्स लागू करणे**: विद्यमान Azure इन्फ्रास्ट्रक्चर आणि सुरक्षा मॉडेल्ससह कस्टम ट्रान्सपोर्ट्स एकत्र करणे
- **ट्रान्सपोर्ट विश्वसनीयता हाताळणे**: एंटरप्राइझ परिस्थितीसाठी मेसेज टिकाऊपणा, ऑर्डरिंग आणि त्रुटी हाताळणी अंमलात आणणे
- **कार्यक्षमता ऑप्टिमाइझ करणे**: स्केल, लेटन्सी आणि थ्रूपुट आवश्यकता पूर्ण करणारे ट्रान्सपोर्ट सोल्यूशन्स डिझाइन करणे

## **ट्रान्सपोर्ट आवश्यकता**

### **MCP स्पेसिफिकेशन (2025-11-25) मधील मुख्य आवश्यकता:**

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

## **Azure Event Grid ट्रान्सपोर्ट अंमलबजावणी**

Azure Event Grid ही इव्हेंट-चालित MCP आर्किटेक्चर्ससाठी आदर्श असलेली सर्व्हरलेस इव्हेंट राउटिंग सेवा प्रदान करते. ही अंमलबजावणी स्केलेबल, सैल-संबंधित MCP सिस्टम्स कसे तयार करायचे हे दाखवते.

### **आर्किटेक्चर अवलोकन**

```mermaid
graph TB
    Client[MCP क्लायंट] --> EG[Azure इव्हेंट ग्रिड]
    EG --> Server[MCP सर्व्हर फंक्शन]
    Server --> EG
    EG --> Client
    
    subgraph "Azure सेवा"
        EG
        Server
        KV[की वॉल्ट]
        Monitor[अॅप्लिकेशन इनसाइट्स]
    end
```
### **C# अंमलबजावणी - Event Grid ट्रान्सपोर्ट**

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

### **TypeScript अंमलबजावणी - Event Grid ट्रान्सपोर्ट**

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
    
    // Azure Functions द्वारे इव्हेंट-चालित प्राप्ती
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // अंमलबजावणीसाठी Azure Functions Event Grid ट्रिगर वापरला जाईल
        // हा वेबहूक रिसीव्हरसाठी एक संकल्पनात्मक इंटरफेस आहे
    }
}

// Azure Functions अंमलबजावणी
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // MCP संदेश प्रक्रिया करा
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Event Grid द्वारे प्रतिसाद पाठवा
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Python अंमलबजावणी - Event Grid ट्रान्सपोर्ट**

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

# Azure Functions अंमलबजावणी
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Event Grid इव्हेंटमधून MCP संदेश पार्स करा
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # MCP संदेश प्रक्रिया करा
        response = process_mcp_message(mcp_message)
        
        # Event Grid द्वारे प्रतिसाद परत पाठवा
        # (अंमलबजावणी नवीन Event Grid क्लायंट तयार करेल)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Azure Event Hubs ट्रान्सपोर्ट अंमलबजावणी**

Azure Event Hubs MCP परिस्थितीसाठी उच्च-थ्रूपुट, रिअल-टाइम स्ट्रीमिंग क्षमता प्रदान करते ज्यांना कमी विलंब आणि जास्त मेसेज व्हॉल्यूम आवश्यक आहे.

### **आर्किटेक्चर अवलोकन**

```mermaid
graph TB
    Client[MCP क्लायंट] --> EH[Azure इव्हेंट हब्स]
    EH --> Server[MCP सर्व्हर]
    Server --> EH
    EH --> Client
    
    subgraph "इव्हेंट हब्स वैशिष्ट्ये"
        Partition[विभाजन]
        Retention[संदेश राखीव]
        Scaling[स्वयंचलित स्केलिंग]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **C# अंमलबजावणी - Event Hubs ट्रान्सपोर्ट**

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

### **TypeScript अंमलबजावणी - Event Hubs ट्रान्सपोर्ट**

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
                        
                        // किमान-एकदा वितरणासाठी चेकपॉइंट अद्यतनित करा
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

### **Python अंमलबजावणी - Event Hubs ट्रान्सपोर्ट**

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
        
        # MCP-विशिष्ट गुणधर्म जोडा
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # वास्तविक टाइमस्टॅम्प वापरा
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
                starting_position="-1"  # सुरुवातीपासून सुरू करा
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Event Hubs इव्हेंटमधून MCP संदेश पार्स करा
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # MCP संदेश प्रक्रिया करा
                await handler(mcp_message)
                
                # किमान एकदा वितरणासाठी चेकपॉइंट अपडेट करा
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

## **प्रगत ट्रान्सपोर्ट पॅटर्न्स**

### **मेसेज टिकाऊपणा आणि विश्वसनीयता**

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

### **ट्रान्सपोर्ट सुरक्षा एकत्रीकरण**

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

### **ट्रान्सपोर्ट मॉनिटरिंग आणि निरीक्षण**

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

## **एंटरप्राइझ इंटिग्रेशन परिस्थिती**

### **परिस्थिती 1: वितरित MCP प्रक्रिया**

अनेक प्रक्रिया नोड्समध्ये MCP विनंत्या वितरित करण्यासाठी Azure Event Grid वापरणे:

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

### **परिस्थिती 2: रिअल-टाइम MCP स्ट्रीमिंग**

उच्च-वारंवारतेच्या MCP संवादांसाठी Azure Event Hubs वापरणे:

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

### **परिस्थिती 3: हायब्रिड ट्रान्सपोर्ट आर्किटेक्चर**

वेगवेगळ्या वापरासाठी अनेक ट्रान्सपोर्ट्स एकत्र करणे:

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

## **कार्यक्षमता ऑप्टिमायझेशन**

### **Event Grid साठी मेसेज बॅचिंग**

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

### **Event Hubs साठी पार्टिशनिंग धोरण**

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

## **कस्टम ट्रान्सपोर्ट्सची चाचणी**

### **टेस्ट डबल्ससह युनिट टेस्टिंग**

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

### **Azure टेस्ट कंटेनर्ससह इंटिग्रेशन टेस्टिंग**

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

## **सर्वोत्तम पद्धती आणि मार्गदर्शक तत्त्वे**

### **ट्रान्सपोर्ट डिझाइन तत्त्वे**

1. **आयडेम्पोटन्सी**: डुप्लिकेट हाताळण्यासाठी मेसेज प्रक्रिया आयडेम्पोटंट असावी याची खात्री करा
2. **त्रुटी हाताळणी**: सर्वसमावेशक त्रुटी हाताळणी आणि डेड लेटर क्यूज अंमलात आणा
3. **मॉनिटरिंग**: सविस्तर टेलिमेट्री आणि हेल्थ चेक जोडा
4. **सुरक्षा**: व्यवस्थापित ओळखपत्रे आणि किमान विशेषाधिकार प्रवेश वापरा
5. **कार्यक्षमता**: आपल्या विशिष्ट विलंब आणि थ्रूपुट आवश्यकतांसाठी डिझाइन करा

### **Azure-विशिष्ट शिफारसी**

1. **व्यवस्थापित ओळखपत्र वापरा**: उत्पादनात कनेक्शन स्ट्रिंग्ज टाळा
2. **सर्किट ब्रेकर्स अंमलात आणा**: Azure सेवा अडथळ्यांपासून संरक्षण करा
3. **खर्चे मॉनिटर करा**: मेसेज व्हॉल्यूम आणि प्रक्रिया खर्च ट्रॅक करा
4. **स्केलसाठी योजना करा**: लवकरच पार्टिशनिंग आणि स्केलिंग धोरणे डिझाइन करा
5. **संपूर्णपणे चाचणी करा**: व्यापक चाचणीसाठी Azure DevTest Labs वापरा

## **निष्कर्ष**

कस्टम MCP ट्रान्सपोर्ट्स Azure च्या मेसेजिंग सेवांचा वापर करून सामर्थ्यशाली एंटरप्राइझ परिस्थिती सक्षम करतात. Event Grid किंवा Event Hubs ट्रान्सपोर्ट्स अंमलात आणून, आपण विद्यमान Azure इन्फ्रास्ट्रक्चरशी सुसंगत, स्केलेबल आणि विश्वसनीय MCP सोल्यूशन्स तयार करू शकता.

दिलेली उदाहरणे कस्टम ट्रान्सपोर्ट्स अंमलबजावणीसाठी उत्पादन-तयार पॅटर्न्स दाखवतात, जे MCP प्रोटोकॉल अनुपालन आणि Azure सर्वोत्तम पद्धती राखतात.

## **अतिरिक्त संसाधने**

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Azure Event Grid Documentation](https://docs.microsoft.com/azure/event-grid/)
- [Azure Event Hubs Documentation](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK for TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

---

> *हा मार्गदर्शक उत्पादन MCP सिस्टमसाठी व्यावहारिक अंमलबजावणी पॅटर्नवर लक्ष केंद्रित करतो. नेहमी आपल्या विशिष्ट गरजा आणि Azure सेवा मर्यादांनुसार ट्रान्सपोर्ट अंमलबजावणीची पडताळणी करा.*
> **सध्याचा मानक**: हा मार्गदर्शक [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) ट्रान्सपोर्ट आवश्यकता आणि एंटरप्राइझ वातावरणांसाठी प्रगत ट्रान्सपोर्ट पॅटर्न्स प्रतिबिंबित करतो.


## पुढे काय
- [6. Community Contributions](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
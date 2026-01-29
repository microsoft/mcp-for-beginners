# راهنمای پیشرفته پیاده‌سازی انتقال‌های سفارشی MCP

پروتکل مدل کانتکست (MCP) انعطاف‌پذیری در مکانیزم‌های انتقال فراهم می‌کند و امکان پیاده‌سازی‌های سفارشی برای محیط‌های سازمانی تخصصی را می‌دهد. این راهنمای پیشرفته، پیاده‌سازی‌های انتقال سفارشی را با استفاده از Azure Event Grid و Azure Event Hubs به عنوان مثال‌های عملی برای ساخت راه‌حل‌های مقیاس‌پذیر و بومی ابر MCP بررسی می‌کند.

## مقدمه

در حالی که انتقال‌های استاندارد MCP (stdio و HTTP streaming) بیشتر موارد استفاده را پوشش می‌دهند، محیط‌های سازمانی اغلب به مکانیزم‌های انتقال تخصصی برای بهبود مقیاس‌پذیری، قابلیت اطمینان و یکپارچگی با زیرساخت ابری موجود نیاز دارند. انتقال‌های سفارشی به MCP امکان می‌دهند از خدمات پیام‌رسانی بومی ابر برای ارتباط ناهمزمان، معماری‌های رویدادمحور و پردازش توزیع‌شده بهره‌مند شود.

این درس پیاده‌سازی‌های پیشرفته انتقال را بر اساس آخرین مشخصات MCP (2025-11-25)، خدمات پیام‌رسانی Azure و الگوهای یکپارچگی سازمانی تثبیت‌شده بررسی می‌کند.

### **معماری انتقال MCP**

**از مشخصات MCP (2025-11-25):**

- **انتقال‌های استاندارد**: stdio (توصیه شده)، HTTP streaming (برای سناریوهای راه دور)
- **انتقال‌های سفارشی**: هر انتقالی که پروتکل تبادل پیام MCP را پیاده‌سازی کند
- **فرمت پیام**: JSON-RPC 2.0 با افزونه‌های خاص MCP
- **ارتباط دوطرفه**: ارتباط دوطرفه کامل برای اعلان‌ها و پاسخ‌ها لازم است

## اهداف یادگیری

تا پایان این درس پیشرفته، شما قادر خواهید بود:

- **درک نیازمندی‌های انتقال سفارشی**: پیاده‌سازی پروتکل MCP بر روی هر لایه انتقال در حالی که انطباق حفظ شود
- **ساخت انتقال Azure Event Grid**: ایجاد سرورهای MCP رویدادمحور با استفاده از Azure Event Grid برای مقیاس‌پذیری بدون سرور
- **پیاده‌سازی انتقال Azure Event Hubs**: طراحی راه‌حل‌های MCP با توان بالا با استفاده از Azure Event Hubs برای پخش زنده
- **اعمال الگوهای سازمانی**: یکپارچه‌سازی انتقال‌های سفارشی با زیرساخت و مدل‌های امنیتی Azure موجود
- **مدیریت قابلیت اطمینان انتقال**: پیاده‌سازی دوام پیام، ترتیب‌دهی و مدیریت خطا برای سناریوهای سازمانی
- **بهینه‌سازی عملکرد**: طراحی راه‌حل‌های انتقال برای نیازهای مقیاس، تأخیر و توان عملیاتی

## **نیازمندی‌های انتقال**

### **نیازمندی‌های اصلی از مشخصات MCP (2025-11-25):**

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

## **پیاده‌سازی انتقال Azure Event Grid**

Azure Event Grid یک سرویس مسیریابی رویداد بدون سرور فراهم می‌کند که برای معماری‌های MCP رویدادمحور ایده‌آل است. این پیاده‌سازی نشان می‌دهد چگونه سیستم‌های MCP مقیاس‌پذیر و با اتصال ضعیف بسازیم.

### **نمای کلی معماری**

```mermaid
graph TB
    Client[کلاینت MCP] --> EG[شبکه رویداد آزور]
    EG --> Server[تابع سرور MCP]
    Server --> EG
    EG --> Client
    
    subgraph "خدمات آزور"
        EG
        Server
        KV[گنجینه کلید]
        Monitor[بینش‌های برنامه]
    end
```
### **پیاده‌سازی C# - انتقال Event Grid**

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

### **پیاده‌سازی TypeScript - انتقال Event Grid**

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
    
    // دریافت مبتنی بر رویداد از طریق Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // پیاده‌سازی از تریگر Event Grid در Azure Functions استفاده می‌کند
        // این یک رابط مفهومی برای دریافت‌کننده وب‌هوک است
    }
}

// پیاده‌سازی Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // پردازش پیام MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // ارسال پاسخ از طریق Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **پیاده‌سازی Python - انتقال Event Grid**

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

# پیاده‌سازی Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # تجزیه پیام MCP از رویداد Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # پردازش پیام MCP
        response = process_mcp_message(mcp_message)
        
        # ارسال پاسخ از طریق Event Grid
        # (پیاده‌سازی یک کلاینت جدید Event Grid ایجاد می‌کند)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **پیاده‌سازی انتقال Azure Event Hubs**

Azure Event Hubs قابلیت‌های پخش زنده با توان بالا و تأخیر کم را برای سناریوهای MCP که نیاز به حجم بالای پیام دارند فراهم می‌کند.

### **نمای کلی معماری**

```mermaid
graph TB
    Client[کلاینت MCP] --> EH[آژور ایونت هابز]
    EH --> Server[سرور MCP]
    Server --> EH
    EH --> Client
    
    subgraph "ویژگی‌های ایونت هابز"
        Partition[تقسیم‌بندی]
        Retention[نگهداری پیام]
        Scaling[مقیاس‌بندی خودکار]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **پیاده‌سازی C# - انتقال Event Hubs**

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

### **پیاده‌سازی TypeScript - انتقال Event Hubs**

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
                        
                        // به‌روزرسانی نقطه بازبینی برای تحویل حداقل یک‌بار
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

### **پیاده‌سازی Python - انتقال Event Hubs**

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
        
        # افزودن ویژگی‌های خاص MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # استفاده از زمان واقعی
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
                starting_position="-1"  # شروع از ابتدا
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # تجزیه پیام MCP از رویداد Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # پردازش پیام MCP
                await handler(mcp_message)
                
                # به‌روزرسانی نقطه بررسی برای تحویل حداقل یک بار
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

## **الگوهای پیشرفته انتقال**

### **دوام و قابلیت اطمینان پیام**

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

### **یکپارچگی امنیت انتقال**

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

### **نظارت و قابلیت مشاهده انتقال**

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

## **سناریوهای یکپارچگی سازمانی**

### **سناریو 1: پردازش توزیع‌شده MCP**

استفاده از Azure Event Grid برای توزیع درخواست‌های MCP در چندین گره پردازشی:

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

### **سناریو 2: پخش زنده MCP**

استفاده از Azure Event Hubs برای تعاملات MCP با فرکانس بالا:

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

### **سناریو 3: معماری انتقال ترکیبی**

ترکیب چندین انتقال برای موارد استفاده مختلف:

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

## **بهینه‌سازی عملکرد**

### **بسته‌بندی پیام برای Event Grid**

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

### **استراتژی تقسیم‌بندی برای Event Hubs**

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

## **آزمایش انتقال‌های سفارشی**

### **آزمایش واحد با تست دابل‌ها**

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

### **آزمایش یکپارچه با Azure Test Containers**

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

## **بهترین شیوه‌ها و راهنمایی‌ها**

### **اصول طراحی انتقال**

1. **ایدئومپوتنسی**: اطمینان از پردازش ایدئومپوتنت پیام برای مدیریت تکراری‌ها
2. **مدیریت خطا**: پیاده‌سازی مدیریت جامع خطا و صف‌های نامه‌های مرده
3. **نظارت**: افزودن تله‌متری دقیق و بررسی سلامت
4. **امنیت**: استفاده از هویت‌های مدیریت شده و دسترسی حداقلی
5. **عملکرد**: طراحی بر اساس نیازهای خاص تأخیر و توان عملیاتی

### **توصیه‌های خاص Azure**

1. **استفاده از هویت مدیریت شده**: اجتناب از رشته‌های اتصال در محیط تولید
2. **پیاده‌سازی قطع‌کننده‌های مدار**: محافظت در برابر قطعی سرویس‌های Azure
3. **نظارت بر هزینه‌ها**: پیگیری حجم پیام و هزینه‌های پردازش
4. **برنامه‌ریزی برای مقیاس**: طراحی استراتژی‌های تقسیم‌بندی و مقیاس‌گذاری از ابتدا
5. **آزمایش کامل**: استفاده از Azure DevTest Labs برای آزمایش جامع

## **نتیجه‌گیری**

انتقال‌های سفارشی MCP امکان سناریوهای قدرتمند سازمانی را با استفاده از خدمات پیام‌رسانی Azure فراهم می‌کنند. با پیاده‌سازی انتقال‌های Event Grid یا Event Hubs، می‌توانید راه‌حل‌های MCP مقیاس‌پذیر و قابل اطمینان بسازید که به‌طور یکپارچه با زیرساخت Azure موجود ادغام می‌شوند.

مثال‌های ارائه شده الگوهای آماده تولید برای پیاده‌سازی انتقال‌های سفارشی را در حالی که انطباق با پروتکل MCP و بهترین شیوه‌های Azure حفظ می‌شود، نشان می‌دهند.

## **منابع اضافی**

- [مشخصات MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [مستندات Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [مستندات Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK برای .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK برای TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK برای Python](https://github.com/Azure/azure-sdk-for-python)

---

> *این راهنما بر الگوهای پیاده‌سازی عملی برای سیستم‌های تولیدی MCP تمرکز دارد. همیشه پیاده‌سازی‌های انتقال را با نیازهای خاص خود و محدودیت‌های سرویس Azure اعتبارسنجی کنید.*
> **استاندارد فعلی**: این راهنما نیازمندی‌های انتقال و الگوهای پیشرفته انتقال برای محیط‌های سازمانی را مطابق با [مشخصات MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) منعکس می‌کند.

## مرحله بعد
- [6. مشارکت‌های جامعه](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Custom Transports - Panduan Implementasi Lanjutan

Model Context Protocol (MCP) menyediakan fleksibilitas dalam mekanisme transportasi, memungkinkan implementasi kustom untuk lingkungan perusahaan yang khusus. Panduan lanjutan ini mengeksplorasi implementasi transportasi kustom menggunakan Azure Event Grid dan Azure Event Hubs sebagai contoh praktis untuk membangun solusi MCP yang skalabel dan cloud-native.

## Pendahuluan

Meskipun transportasi standar MCP (stdio dan HTTP streaming) melayani sebagian besar kasus penggunaan, lingkungan perusahaan sering kali memerlukan mekanisme transportasi khusus untuk meningkatkan skalabilitas, keandalan, dan integrasi dengan infrastruktur cloud yang sudah ada. Transportasi kustom memungkinkan MCP memanfaatkan layanan pesan cloud-native untuk komunikasi asinkron, arsitektur berbasis event, dan pemrosesan terdistribusi.

Pelajaran ini mengeksplorasi implementasi transportasi lanjutan berdasarkan spesifikasi MCP terbaru (2025-11-25), layanan pesan Azure, dan pola integrasi perusahaan yang sudah mapan.

### **Arsitektur Transport MCP**

**Dari Spesifikasi MCP (2025-11-25):**

- **Transportasi Standar**: stdio (direkomendasikan), HTTP streaming (untuk skenario jarak jauh)
- **Transportasi Kustom**: Transportasi apa pun yang mengimplementasikan protokol pertukaran pesan MCP
- **Format Pesan**: JSON-RPC 2.0 dengan ekstensi khusus MCP
- **Komunikasi Dua Arah**: Komunikasi full duplex diperlukan untuk notifikasi dan respons

## Tujuan Pembelajaran

Pada akhir pelajaran lanjutan ini, Anda akan dapat:

- **Memahami Persyaratan Transportasi Kustom**: Mengimplementasikan protokol MCP di atas lapisan transportasi apa pun sambil mempertahankan kepatuhan
- **Membangun Transportasi Azure Event Grid**: Membuat server MCP berbasis event menggunakan Azure Event Grid untuk skalabilitas tanpa server
- **Mengimplementasikan Transportasi Azure Event Hubs**: Merancang solusi MCP throughput tinggi menggunakan Azure Event Hubs untuk streaming waktu nyata
- **Menerapkan Pola Perusahaan**: Mengintegrasikan transportasi kustom dengan infrastruktur dan model keamanan Azure yang sudah ada
- **Menangani Keandalan Transportasi**: Mengimplementasikan daya tahan pesan, pengurutan, dan penanganan kesalahan untuk skenario perusahaan
- **Mengoptimalkan Kinerja**: Merancang solusi transportasi untuk kebutuhan skala, latensi, dan throughput

## **Persyaratan Transportasi**

### **Persyaratan Inti dari Spesifikasi MCP (2025-11-25):**

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

## **Implementasi Transportasi Azure Event Grid**

Azure Event Grid menyediakan layanan routing event tanpa server yang ideal untuk arsitektur MCP berbasis event. Implementasi ini menunjukkan cara membangun sistem MCP yang skalabel dan loosely-coupled.

### **Gambaran Arsitektur**

```mermaid
graph TB
    Client[MCP Client] --> EG[Azure Event Grid]
    EG --> Server[Fungsi Server MCP]
    Server --> EG
    EG --> Client
    
    subgraph "Layanan Azure"
        EG
        Server
        KV[Key Vault]
        Monitor[Application Insights]
    end
```
### **Implementasi C# - Transportasi Event Grid**

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

### **Implementasi TypeScript - Transportasi Event Grid**

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
    
    // Penerimaan berbasis peristiwa melalui Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Implementasi akan menggunakan pemicu Event Grid Azure Functions
        // Ini adalah antarmuka konseptual untuk penerima webhook
    }
}

// Implementasi Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Proses pesan MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Kirim respons melalui Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Implementasi Python - Transportasi Event Grid**

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

# Implementasi Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Mengurai pesan MCP dari event Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Memproses pesan MCP
        response = process_mcp_message(mcp_message)
        
        # Mengirim respons kembali melalui Event Grid
        # (Implementasi akan membuat klien Event Grid baru)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Implementasi Transportasi Azure Event Hubs**

Azure Event Hubs menyediakan kemampuan streaming waktu nyata dengan throughput tinggi untuk skenario MCP yang memerlukan latensi rendah dan volume pesan tinggi.

### **Gambaran Arsitektur**

```mermaid
graph TB
    Client[MCP Client] --> EH[Azure Event Hubs]
    EH --> Server[MCP Server]
    Server --> EH
    EH --> Client
    
    subgraph "Fitur Event Hubs"
        Partition[Partisi]
        Retention[Retensi Pesan]
        Scaling[Skala Otomatis]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **Implementasi C# - Transportasi Event Hubs**

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

### **Implementasi TypeScript - Transportasi Event Hubs**

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
                        
                        // Perbarui titik pemeriksaan untuk pengiriman setidaknya sekali
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

### **Implementasi Python - Transportasi Event Hubs**

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
        
        # Tambahkan properti khusus MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Gunakan cap waktu yang sebenarnya
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
                starting_position="-1"  # Mulai dari awal
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Mengurai pesan MCP dari event Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Memproses pesan MCP
                await handler(mcp_message)
                
                # Perbarui checkpoint untuk pengiriman setidaknya sekali
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

## **Pola Transportasi Lanjutan**

### **Daya Tahan dan Keandalan Pesan**

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

### **Integrasi Keamanan Transportasi**

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

### **Pemantauan dan Observabilitas Transportasi**

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

## **Skenario Integrasi Perusahaan**

### **Skenario 1: Pemrosesan MCP Terdistribusi**

Menggunakan Azure Event Grid untuk mendistribusikan permintaan MCP ke beberapa node pemrosesan:

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

### **Skenario 2: Streaming MCP Waktu Nyata**

Menggunakan Azure Event Hubs untuk interaksi MCP frekuensi tinggi:

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

### **Skenario 3: Arsitektur Transportasi Hibrida**

Menggabungkan beberapa transportasi untuk berbagai kasus penggunaan:

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

## **Optimasi Kinerja**

### **Pengelompokan Pesan untuk Event Grid**

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

### **Strategi Partisi untuk Event Hubs**

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

## **Pengujian Transportasi Kustom**

### **Pengujian Unit dengan Test Doubles**

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

### **Pengujian Integrasi dengan Azure Test Containers**

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

## **Praktik Terbaik dan Pedoman**

### **Prinsip Desain Transportasi**

1. **Idempoten**: Pastikan pemrosesan pesan bersifat idempoten untuk menangani duplikat
2. **Penanganan Kesalahan**: Terapkan penanganan kesalahan komprehensif dan antrean dead letter
3. **Pemantauan**: Tambahkan telemetri rinci dan pemeriksaan kesehatan
4. **Keamanan**: Gunakan managed identities dan akses dengan hak minimum
5. **Kinerja**: Rancang sesuai kebutuhan latensi dan throughput spesifik Anda

### **Rekomendasi Khusus Azure**

1. **Gunakan Managed Identity**: Hindari string koneksi di produksi
2. **Implementasikan Circuit Breakers**: Lindungi dari gangguan layanan Azure
3. **Pantau Biaya**: Lacak volume pesan dan biaya pemrosesan
4. **Rencanakan untuk Skala**: Rancang strategi partisi dan penskalaan sejak awal
5. **Uji Secara Menyeluruh**: Gunakan Azure DevTest Labs untuk pengujian komprehensif

## **Kesimpulan**

Transportasi MCP kustom memungkinkan skenario perusahaan yang kuat menggunakan layanan pesan Azure. Dengan mengimplementasikan transportasi Event Grid atau Event Hubs, Anda dapat membangun solusi MCP yang skalabel dan andal yang terintegrasi mulus dengan infrastruktur Azure yang sudah ada.

Contoh yang disediakan menunjukkan pola siap produksi untuk mengimplementasikan transportasi kustom sambil mempertahankan kepatuhan protokol MCP dan praktik terbaik Azure.

## **Sumber Daya Tambahan**

- [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Dokumentasi Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Dokumentasi Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK untuk .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK untuk TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK untuk Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Panduan ini berfokus pada pola implementasi praktis untuk sistem MCP produksi. Selalu validasi implementasi transportasi sesuai dengan kebutuhan spesifik Anda dan batasan layanan Azure.*
> **Standar Saat Ini**: Panduan ini mencerminkan [Spesifikasi MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) persyaratan transportasi dan pola transportasi lanjutan untuk lingkungan perusahaan.


## Selanjutnya
- [6. Kontribusi Komunitas](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
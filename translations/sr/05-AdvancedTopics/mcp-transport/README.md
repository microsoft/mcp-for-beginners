# MCP прилагођени транспорт - Напредни водич за имплементацију

Протокол контекста модела (MCP) дозвољава прилагођене имплементације транспорта за
специјализована окружења. Овај напредни водич истражује Azure Event Grid и
Azure Event Hubs као архитектонске обрасце. Они нису стандардни MCP транспорти
и захтевају да се обе крајње тачке договоре о прилагођеном мапирању.

> **MCP `2026-07-28` обим:** тренутни протокол нема протоколски ниво
> сесија, тако да прилагођени транспорти не смеју зависити од афинитета сесије или
> поретка по појединачној сесији. Заглавља `Mcp-Method` и условна `Mcp-Name` су
> захтеви стандардног Streamable HTTP транспорта; не-HTTP транспорт
> треба еквивалентно, експлицитно усаглашено мапирање ако посредници морају усмеравати
> без декодирања JSON-RPC тела. Погледајте
> [Шта се променило у MCP: Спецификација 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

## Увод

Стандардни MCP транспорти су stdio и Streamable HTTP. Нека предузећа
користе прилагођено мапирање за интеграцију са постојећом инфраструктуром
за размену порука, али то може смањити интероперабилност са MCP домаћинима и
SDK-овима који имплементирају само стандардне транспорте.

Ова лекција примењује бездржавне захтеве спецификације MCP
`2026-07-28` на Azure сервисе за размену порука и успостављене
обрасце интеграције у предузећима.

### **Архитектура MCP транспорта**

**Из спецификације MCP `2026-07-28`:**

- **Стандардни транспорти**: stdio и Streamable HTTP
- **Прилагођени транспорти**: Опционални, имплементационо специфична мапирања договорена од
    обе крајње тачке
- **Формат поруке**: JSON-RPC 2.0 са MCP-специфичним екстензијама
- **Самосталне захтеве**: Нема протоколске сесије или руковања за
    пренос стања између захтева

## Циљеви учења

На крају ове напредне лекције, моћи ћете да:

- **Разумете захтеве прилагођеног транспорта**: Имплементирати MCP протокол преко било ког транспортног слоја уз одржавање усаглашености
- **Изградите Azure Event Grid транспорт**: Креирати MCP сервере засноване на догађајима користећи Azure Event Grid за безсерверску скалабилност
- **Имплементирате Azure Event Hubs транспорт**: Дизајнирати MCP решења великог пропусног опсега користећи Azure Event Hubs за стримовање у реалном времену
- **Примeните пословне обрасце**: Интегрисати прилагођене транспорте са постојећом Azure инфраструктуром и безбедносним моделима
- **Обрадите поузданост транспорта**: Имплементирати издржљивост порука, поређање и руковање грешкама за пословне сценарије
- **Оптимизујте перформансе**: Осмислити транспортна решења за потребе скалабилности, латенције и пропусног опсега

## **Захтеви за транспорт**

### **Језгровни захтеви за MCP `2026-07-28`**

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

## **Имплементација Azure Event Grid транспорта**

Azure Event Grid пружа безсерверску услугу за рутирање догађаја идеалну за MCP архитектуре засноване на догађајима. Ова имплементација демонстрира како изградити скалабилне, лабаво повезане MCP системе.

### **Преглед архитектуре**

```mermaid
graph TB
    Client[MCP Клијент] --> EG[Azure Event Grid]
    EG --> Server[MCP Сервер Функција]
    Server --> EG
    EG --> Client
    
    subgraph "Azure Услуге"
        EG
        Server
        KV[Key Vault]
        Monitor[Application Insights]
    end
```

### **C# имплементација - Event Grid транспорт**

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

### **TypeScript имплементација - Event Grid транспорт**

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
    
    // Пријем заснован на догађајима преко Azure функција
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Имплементација би користила Azure функције Event Grid триггер
        // Ово је концептуални интерфејс за примаоца web-hook-а
    }
}

// Имплементација у Azure функцијама
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Обради MCP поруку
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Пошаљи одговор преко Event Grid-а
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Python имплементација - Event Grid транспорт**

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

# Имплементација Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Парсирај MCP поруку из Event Grid догађаја
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Обради MCP поруку
        response = process_mcp_message(mcp_message)
        
        # Пошаљи одговор назад преко Event Grid-а
        # (Имплементација би направила нови Event Grid клијент)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Имплементација Azure Event Hubs транспорта**

Azure Event Hubs пружа могућности стримовања великог пропусног опсега и у реалном времену за MCP сценарије који захтевају малу латенцију и велики обим порука.

### **Преглед архитектуре**

```mermaid
graph TB
    Client[MCP Клијент] --> EH[Azure Event Hubs]
    EH --> Server[MCP Сервер]
    Server --> EH
    EH --> Client
    
    subgraph "Функције Event Hubs-а"
        Partition[Партиционисање]
        Retention[Чување Порука]
        Scaling[Аутоматско Скалирање]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```

### **C# имплементација - Event Hubs транспорт**

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

### **TypeScript имплементација - Event Hubs транспорт**

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
                        
                        // Ажурирај тачку контроле за испоруку најмање једном
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

### **Python имплементација - Event Hubs транспорт**

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
        
        # Додај MCP-специфична својства
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Употреби стварно време
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
                starting_position="-1"  # Почни од почетка
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Парсирај MCP поруку из догађаја Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Обради MCP поруку
                await handler(mcp_message)
                
                # Ажурирај чекпоинт за доставу најмање једном
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

## **Напредни транспортни обрасци**

### **Издржљивост и поузданост порука**

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

### **Интеграција безбедности транспорта**

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

### **Надгледање и посматрање транспорта**

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

## **Пословни сценарији интеграције**

### **Сценарио 1: Расподељена MCP обрада**

Коришћење Azure Event Grid-а за расподелу MCP захтева преко више обрадних чворова:

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

### **Сценарио 2: Стримовање MCP у реалном времену**

Коришћење Azure Event Hubs-а за MCP интеракције високе фреквенције:

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

### **Сценарио 3: Хибридна архитектура транспорта**

Комбинација више транспорти за различите случајеве употребе:

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

## **Оптимизација перформанси**

### **Пакетирање порука за Event Grid**

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

### **Стратегија партиционисања за Event Hubs**

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

## **Тестирање прилагођених транспорти**

### **Јединично тестирање са тест двојницима**

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

### **Интеграционо тестирање са Azure Test Containers**

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

## **Најбоље праксе и смернице**

### **Принципи дизајна транспорта**

1. **Идeмпотентност**: Осигурати да обрада порука буде идeмпотентна за рад са дупликатима
2. **Руковање грешкама**: Имплементирати комплетно руковање грешкама и редове мртвих порука
3. **Надгледање**: Додати детаљну телеметрију и здравствене провере
4. **Безбедност**: Користити управљане идентитете и приступ са најмањим привилегијама
5. **Перформансе**: Дизајнирати за конкретне захтеве латенције и пропусног опсега

### **Преporуке специфичне за Azure**

1. **Користите управљани идентитет**: Избегавајте конекцијске низове у продукцији
2. **Имплементирајте прекидаче кола**: Заштитите се од прекида у Azure сервисима
3. **Пратите трошкове**: Контролишите обим порука и трошкове обраде
4. **Планирајте скалабилност**: Рано дизајнирајте стратегије партиционисања и скалирања
5. **Темелно тестирајте**: Користите Azure DevTest Labs за свеобухватно тестирање

## **Закључак**

Прилагођени MCP транспорти омогућавају моћне пословне сценарије користећи Azure сервисе за размену порука. Имплементацијом Event Grid или Event Hubs транспорта, можете изградити скалабилна, поуздана MCP решења која се беспрекорно интегришу са постојећом Azure инфраструктуром.

Дати примери показују производне обрасце за имплементацију прилагођених транспорти уз одржавање усаглашености са MCP протоколом и најбољим Azure праксама.

## **Додатни ресурси**

- [MCP спецификација 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Документација Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Документација Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Тригер за Azure Functions Event Grid](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK за .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK за TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK за Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Овај водич се фокусира на прилагођене архитектонске обрасце. Верификујте протокол

> понашање према [MCP спецификацији 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/),
> и валидацију коришћења Azure-а према вашим захтевима и ограничењима услуге.*


## Шта следеће
- [6. Заједнички доприноси](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
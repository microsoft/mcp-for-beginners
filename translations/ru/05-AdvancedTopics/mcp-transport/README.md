# MCP Пользовательские Транспорты - Руководство по Продвинутой Реализации

Протокол Контекста Модели (MCP) предоставляет гибкость в механизмах транспорта, позволяя создавать пользовательские реализации для специализированных корпоративных сред. Это продвинутое руководство рассматривает реализации пользовательских транспортов с использованием Azure Event Grid и Azure Event Hubs в качестве практических примеров для построения масштабируемых, облачно-нативных решений MCP.

## Введение

Хотя стандартные транспорты MCP (stdio и HTTP streaming) подходят для большинства случаев, корпоративные среды часто требуют специализированных транспортных механизмов для улучшения масштабируемости, надежности и интеграции с существующей облачной инфраструктурой. Пользовательские транспорты позволяют MCP использовать облачные сервисы обмена сообщениями для асинхронной коммуникации, событийно-ориентированных архитектур и распределенной обработки.

В этом уроке рассматриваются продвинутые реализации транспортов на основе последней спецификации MCP (2025-11-25), сервисов обмена сообщениями Azure и проверенных корпоративных интеграционных паттернов.

### **Архитектура Транспорта MCP**

**Из спецификации MCP (2025-11-25):**

- **Стандартные транспорты**: stdio (рекомендуется), HTTP streaming (для удаленных сценариев)
- **Пользовательские транспорты**: Любой транспорт, реализующий протокол обмена сообщениями MCP
- **Формат сообщений**: JSON-RPC 2.0 с расширениями MCP
- **Двунаправленная коммуникация**: Требуется полнодуплексная связь для уведомлений и ответов

## Цели Обучения

К концу этого продвинутого урока вы сможете:

- **Понимать требования к пользовательским транспортам**: Реализовывать протокол MCP поверх любого транспортного уровня с соблюдением требований
- **Создавать транспорт Azure Event Grid**: Создавать событийно-ориентированные MCP-серверы с использованием Azure Event Grid для безсерверной масштабируемости
- **Реализовывать транспорт Azure Event Hubs**: Проектировать высокопроизводительные MCP-решения с использованием Azure Event Hubs для потоковой передачи в реальном времени
- **Применять корпоративные паттерны**: Интегрировать пользовательские транспорты с существующей инфраструктурой и моделями безопасности Azure
- **Обеспечивать надежность транспорта**: Реализовывать устойчивость сообщений, упорядочивание и обработку ошибок для корпоративных сценариев
- **Оптимизировать производительность**: Проектировать транспортные решения с учетом масштабируемости, задержек и пропускной способности

## **Требования к Транспорту**

### **Основные требования из спецификации MCP (2025-11-25):**

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

## **Реализация Транспорта Azure Event Grid**

Azure Event Grid предоставляет безсерверный сервис маршрутизации событий, идеально подходящий для событийно-ориентированных архитектур MCP. Эта реализация демонстрирует, как строить масштабируемые, слабо связанные системы MCP.

### **Обзор Архитектуры**

```mermaid
graph TB
    Client[MCP Клиент] --> EG[Azure Event Grid]
    EG --> Server[MCP Серверная Функция]
    Server --> EG
    EG --> Client
    
    subgraph "Сервисы Azure"
        EG
        Server
        KV[Хранилище ключей]
        Monitor[Application Insights]
    end
```
### **Реализация на C# - Транспорт Event Grid**

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

### **Реализация на TypeScript - Транспорт Event Grid**

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
    
    // Прием на основе событий с помощью Azure Functions
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Реализация будет использовать триггер Event Grid в Azure Functions
        // Это концептуальный интерфейс для приемника вебхуков
    }
}

// Реализация Azure Functions
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Обработка сообщения MCP
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Отправка ответа через Event Grid
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Реализация на Python - Транспорт Event Grid**

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

# Реализация Azure Functions
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Разбор сообщения MCP из события Event Grid
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Обработка сообщения MCP
        response = process_mcp_message(mcp_message)
        
        # Отправка ответа обратно через Event Grid
        # (Реализация создаст нового клиента Event Grid)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Реализация Транспорта Azure Event Hubs**

Azure Event Hubs обеспечивает высокопроизводительную потоковую передачу в реальном времени для сценариев MCP, требующих низкой задержки и большого объема сообщений.

### **Обзор Архитектуры**

```mermaid
graph TB
    Client[MCP Клиент] --> EH[Azure Event Hubs]
    EH --> Server[MCP Сервер]
    Server --> EH
    EH --> Client
    
    subgraph "Возможности Event Hubs"
        Partition[Разбиение на разделы]
        Retention[Хранение сообщений]
        Scaling[Автоматическое масштабирование]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **Реализация на C# - Транспорт Event Hubs**

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

### **Реализация на TypeScript - Транспорт Event Hubs**

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
                        
                        // Обновить контрольную точку для доставки как минимум один раз
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

### **Реализация на Python - Транспорт Event Hubs**

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
        
        # Добавить свойства, специфичные для MCP
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Использовать фактическую временную метку
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
                starting_position="-1"  # Начать с начала
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Разобрать сообщение MCP из события Event Hubs
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Обработать сообщение MCP
                await handler(mcp_message)
                
                # Обновить контрольную точку для гарантированной доставки хотя бы один раз
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

## **Продвинутые Паттерны Транспорта**

### **Устойчивость и Надежность Сообщений**

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

### **Интеграция Безопасности Транспорта**

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

### **Мониторинг и Наблюдаемость Транспорта**

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

## **Корпоративные Сценарии Интеграции**

### **Сценарий 1: Распределенная Обработка MCP**

Использование Azure Event Grid для распределения запросов MCP между несколькими узлами обработки:

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

### **Сценарий 2: Потоковая Передача MCP в Реальном Времени**

Использование Azure Event Hubs для высокочастотных взаимодействий MCP:

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

### **Сценарий 3: Гибридная Архитектура Транспорта**

Комбинирование нескольких транспортов для различных случаев использования:

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

## **Оптимизация Производительности**

### **Пакетирование Сообщений для Event Grid**

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

### **Стратегия Партиционирования для Event Hubs**

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

## **Тестирование Пользовательских Транспортов**

### **Модульное Тестирование с Использованием Заглушек**

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

### **Интеграционное Тестирование с Azure Test Containers**

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

## **Лучшие Практики и Рекомендации**

### **Принципы Проектирования Транспорта**

1. **Идемпотентность**: Обеспечьте идемпотентную обработку сообщений для работы с дубликатами
2. **Обработка Ошибок**: Реализуйте комплексную обработку ошибок и очереди мертвых сообщений
3. **Мониторинг**: Добавьте подробную телеметрию и проверки состояния
4. **Безопасность**: Используйте управляемые идентичности и минимально необходимые права доступа
5. **Производительность**: Проектируйте с учетом конкретных требований по задержкам и пропускной способности

### **Рекомендации Специфичные для Azure**

1. **Используйте Управляемую Идентичность**: Избегайте строк подключения в продакшене
2. **Реализуйте Circuit Breakers**: Защищайтесь от сбоев сервисов Azure
3. **Контролируйте Затраты**: Отслеживайте объем сообщений и затраты на обработку
4. **Планируйте Масштабирование**: Раннее проектирование стратегий партиционирования и масштабирования
5. **Тщательно Тестируйте**: Используйте Azure DevTest Labs для комплексного тестирования

## **Заключение**

Пользовательские транспорты MCP открывают мощные корпоративные сценарии с использованием сервисов обмена сообщениями Azure. Реализуя транспорты Event Grid или Event Hubs, вы можете создавать масштабируемые, надежные решения MCP, которые бесшовно интегрируются с существующей инфраструктурой Azure.

Приведенные примеры демонстрируют готовые к производству паттерны реализации пользовательских транспортов с соблюдением протокола MCP и лучших практик Azure.

## **Дополнительные Ресурсы**

- [Спецификация MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Документация Azure Event Grid](https://docs.microsoft.com/azure/event-grid/)
- [Документация Azure Event Hubs](https://docs.microsoft.com/azure/event-hubs/)
- [Триггер Azure Functions для Event Grid](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK для .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK для TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK для Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Это руководство сосредоточено на практических паттернах реализации для производственных систем MCP. Всегда проверяйте реализации транспортов в соответствии с вашими конкретными требованиями и лимитами сервисов Azure.*
> **Текущий Стандарт**: Это руководство отражает требования к транспорту и продвинутые паттерны из [спецификации MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/) для корпоративных сред.


## Что дальше
- [6. Вклад сообщества](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
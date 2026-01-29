# MCP 맞춤형 전송 - 고급 구현 가이드

모델 컨텍스트 프로토콜(MCP)은 맞춤형 구현을 허용하여 특수한 엔터프라이즈 환경에 적합한 전송 메커니즘의 유연성을 제공합니다. 이 고급 가이드는 확장 가능하고 클라우드 네이티브 MCP 솔루션을 구축하기 위한 실용적인 예제로 Azure Event Grid와 Azure Event Hubs를 사용한 맞춤형 전송 구현을 탐구합니다.

## 소개

MCP의 표준 전송(stdio 및 HTTP 스트리밍)은 대부분의 사용 사례에 적합하지만, 엔터프라이즈 환경에서는 확장성, 신뢰성 향상 및 기존 클라우드 인프라와의 통합을 위해 특수한 전송 메커니즘이 종종 필요합니다. 맞춤형 전송은 MCP가 비동기 통신, 이벤트 기반 아키텍처 및 분산 처리를 위해 클라우드 네이티브 메시징 서비스를 활용할 수 있도록 합니다.

이 강의에서는 최신 MCP 사양(2025-11-25), Azure 메시징 서비스 및 확립된 엔터프라이즈 통합 패턴을 기반으로 한 고급 전송 구현을 살펴봅니다.

### **MCP 전송 아키텍처**

**MCP 사양(2025-11-25)에서 발췌:**

- **표준 전송**: stdio(권장), HTTP 스트리밍(원격 시나리오용)
- **맞춤형 전송**: MCP 메시지 교환 프로토콜을 구현하는 모든 전송
- **메시지 형식**: MCP 특정 확장이 포함된 JSON-RPC 2.0
- **양방향 통신**: 알림 및 응답을 위한 전이중 통신 필요

## 학습 목표

이 고급 강의를 마치면 다음을 수행할 수 있습니다:

- **맞춤형 전송 요구사항 이해**: 준수를 유지하면서 모든 전송 계층에서 MCP 프로토콜 구현
- **Azure Event Grid 전송 구축**: 서버리스 확장성을 위한 이벤트 기반 MCP 서버 생성
- **Azure Event Hubs 전송 구현**: 실시간 스트리밍을 위한 고처리량 MCP 솔루션 설계
- **엔터프라이즈 패턴 적용**: 기존 Azure 인프라 및 보안 모델과 맞춤형 전송 통합
- **전송 신뢰성 처리**: 엔터프라이즈 시나리오를 위한 메시지 내구성, 순서 보장 및 오류 처리 구현
- **성능 최적화**: 확장성, 지연 시간 및 처리량 요구사항에 맞는 전송 솔루션 설계

## **전송 요구사항**

### **MCP 사양(2025-11-25)에서 발췌한 핵심 요구사항:**

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

## **Azure Event Grid 전송 구현**

Azure Event Grid는 이벤트 기반 MCP 아키텍처에 이상적인 서버리스 이벤트 라우팅 서비스를 제공합니다. 이 구현은 확장 가능하고 느슨하게 결합된 MCP 시스템을 구축하는 방법을 보여줍니다.

### **아키텍처 개요**

```mermaid
graph TB
    Client[MCP 클라이언트] --> EG[Azure 이벤트 그리드]
    EG --> Server[MCP 서버 함수]
    Server --> EG
    EG --> Client
    
    subgraph "Azure 서비스"
        EG
        Server
        KV[키 볼트]
        Monitor[애플리케이션 인사이트]
    end
```
### **C# 구현 - Event Grid 전송**

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

### **TypeScript 구현 - Event Grid 전송**

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
    
    // Azure Functions를 통한 이벤트 기반 수신
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // 구현은 Azure Functions Event Grid 트리거를 사용합니다
        // 이것은 웹훅 수신기를 위한 개념적 인터페이스입니다
    }
}

// Azure Functions 구현
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // MCP 메시지 처리
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Event Grid를 통해 응답 전송
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Python 구현 - Event Grid 전송**

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

# Azure Functions 구현
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Event Grid 이벤트에서 MCP 메시지 파싱
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # MCP 메시지 처리
        response = process_mcp_message(mcp_message)
        
        # Event Grid를 통해 응답 전송
        # (구현 시 새로운 Event Grid 클라이언트 생성)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Azure Event Hubs 전송 구현**

Azure Event Hubs는 낮은 지연 시간과 높은 메시지 볼륨이 필요한 MCP 시나리오를 위한 고처리량 실시간 스트리밍 기능을 제공합니다.

### **아키텍처 개요**

```mermaid
graph TB
    Client[MCP 클라이언트] --> EH[Azure 이벤트 허브]
    EH --> Server[MCP 서버]
    Server --> EH
    EH --> Client
    
    subgraph "이벤트 허브 기능"
        Partition[파티셔닝]
        Retention[메시지 보존]
        Scaling[자동 확장]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```
### **C# 구현 - Event Hubs 전송**

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

### **TypeScript 구현 - Event Hubs 전송**

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
                        
                        // 적어도 한 번 전달을 위한 체크포인트 업데이트
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

### **Python 구현 - Event Hubs 전송**

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
        
        # MCP 전용 속성 추가
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # 실제 타임스탬프 사용
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
                starting_position="-1"  # 처음부터 시작
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Event Hubs 이벤트에서 MCP 메시지 파싱
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # MCP 메시지 처리
                await handler(mcp_message)
                
                # 최소 한 번 전달을 위한 체크포인트 업데이트
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

## **고급 전송 패턴**

### **메시지 내구성 및 신뢰성**

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

### **전송 보안 통합**

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

### **전송 모니터링 및 관측성**

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

## **엔터프라이즈 통합 시나리오**

### **시나리오 1: 분산 MCP 처리**

Azure Event Grid를 사용하여 여러 처리 노드에 MCP 요청 분산:

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

### **시나리오 2: 실시간 MCP 스트리밍**

Azure Event Hubs를 사용한 고빈도 MCP 상호작용:

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

### **시나리오 3: 하이브리드 전송 아키텍처**

다양한 사용 사례를 위한 여러 전송 결합:

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

## **성능 최적화**

### **Event Grid용 메시지 배치**

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

### **Event Hubs용 파티셔닝 전략**

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

## **맞춤형 전송 테스트**

### **테스트 더블을 사용한 단위 테스트**

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

### **Azure 테스트 컨테이너를 사용한 통합 테스트**

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

## **모범 사례 및 가이드라인**

### **전송 설계 원칙**

1. **멱등성**: 중복 처리를 처리할 수 있도록 메시지 처리를 멱등하게 설계
2. **오류 처리**: 포괄적인 오류 처리 및 데드 레터 큐 구현
3. **모니터링**: 상세한 원격 측정 및 상태 검사 추가
4. **보안**: 관리형 ID 및 최소 권한 액세스 사용
5. **성능**: 특정 지연 시간 및 처리량 요구사항에 맞게 설계

### **Azure 특화 권장사항**

1. **관리형 ID 사용**: 프로덕션에서 연결 문자열 사용 회피
2. **서킷 브레이커 구현**: Azure 서비스 장애에 대비
3. **비용 모니터링**: 메시지 볼륨 및 처리 비용 추적
4. **확장 계획**: 초기부터 파티셔닝 및 확장 전략 설계
5. **철저한 테스트**: Azure DevTest Labs를 활용한 종합 테스트

## **결론**

맞춤형 MCP 전송은 Azure 메시징 서비스를 활용하여 강력한 엔터프라이즈 시나리오를 가능하게 합니다. Event Grid 또는 Event Hubs 전송을 구현함으로써 기존 Azure 인프라와 원활하게 통합되는 확장 가능하고 신뢰할 수 있는 MCP 솔루션을 구축할 수 있습니다.

제공된 예제는 MCP 프로토콜 준수와 Azure 모범 사례를 유지하면서 맞춤형 전송을 구현하기 위한 프로덕션 준비 패턴을 보여줍니다.

## **추가 자료**

- [MCP 사양 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)
- [Azure Event Grid 문서](https://docs.microsoft.com/azure/event-grid/)
- [Azure Event Hubs 문서](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid 트리거](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK for TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

---

> *이 가이드는 프로덕션 MCP 시스템을 위한 실용적인 구현 패턴에 중점을 둡니다. 항상 특정 요구사항과 Azure 서비스 한도에 맞춰 전송 구현을 검증하세요.*
> **현재 표준**: 이 가이드는 [MCP 사양 2025-06-18](https://spec.modelcontextprotocol.io/specification/2025-06-18/)의 전송 요구사항과 엔터프라이즈 환경을 위한 고급 전송 패턴을 반영합니다.


## 다음 단계
- [6. 커뮤니티 기여](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
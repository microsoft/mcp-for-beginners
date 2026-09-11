# MCP Mukautetut Kuljetukset - Edistynyt Toteutusopas

Model Context Protocol (MCP) sallii mukautettujen kuljetusratkaisujen toteuttamisen
erikoistuneissa ympäristöissä. Tämä edistynyt opas tutkii Azure Event Grid:iä ja
Azure Event Hubsia arkkitehtuurilogiikkoina. Ne eivät ole standardeja MCP-kuljetuksia
ja vaativat molempien päätepisteiden sopivan mukautetusta kartoituksesta.

> **MCP `2026-07-28` laajuus:** nykyisellä protokollalla ei ole protokollatason
> istuntoja, joten mukautettujen kuljetusten ei tule riippua istuntoaffiniteetista tai
> istuntokohtaisesta järjestyksestä. `Mcp-Method` ja ehdollinen `Mcp-Name` otsikot ovat
> vaatimuksia standardille Streamable HTTP -kuljetukselle; ei-HTTP-kuljetus
> tarvitsee vastaavan, erikseen sovitun kartoituksen, jos välittäjien täytyy reitittää
> ilman JSON-RPC-kohteen purkamista. Katso
> [Mikä muuttui MCP:ssä: 2026-07-28 määrittely](../../01-CoreConcepts/mcp-2026-07-28.md).

## Johdanto

MCP:n standardikuljetukset ovat stdio ja Streamable HTTP. Jotkut yritysympäristöt
käyttävät mukautettua kartoitusta integroitumaan olemassa olevaan viestintäinfrastruktuuriin,
mutta tämä voi heikentää yhteensopivuutta MCP-isäntien ja
SDK:iden kanssa, jotka toteuttavat vain standardikuljetukset.

Tämä opetus soveltaa MCP-määrittelyn `2026-07-28`
tilattomuusvaatimuksia Azure-viestintäpalveluihin ja vakiintuneisiin yritysintegrointimalleihin.


### **MCP Kuljetusarkkitehtuuri**

**MCP-määrittelystä `2026-07-28`:**

- **Standardikuljetukset**: stdio ja Streamable HTTP
- **Mukautetut kuljetukset**: Vapaaehtoiset, toteutukseen liittyvät kartoitukset, joista molemmat päätepisteet sopivat
    keskenään
- **Viestin muoto**: JSON-RPC 2.0 MCP:lle räätälöidyillä laajennuksilla
- **Itsenäiset pyynnöt**: Protokollan istuntoa tai kättelyä ei ole tilan siirtämiseen pyyntöjen välillä


## Oppimistavoitteet

Tämän edistyneen oppitunnin jälkeen osaat:

- **Ymmärtää mukautettujen kuljetusten vaatimukset**: Toteuttaa MCP-protokolla minkä tahansa kuljetuskerroksen yli pitäen yhteensopivuus
- **Rakentaa Azure Event Grid -kuljetus**: Luo tapahtumapohjaisia MCP-palvelimia Azure Event Gridillä palvelimettomaan skaalautuvuuteen
- **Toteuttaa Azure Event Hubs -kuljetus**: Suunnittele suuritehoisia MCP-ratkaisuja Azure Event Hubsilla reaaliaikaiseen suoratoistoon
- **Soveltaa yrityskäytäntöjä**: Integroi mukautetut kuljetukset olemassa olevaan Azure-infrastruktuuriin ja turvallisuusmalleihin
- **Käsitellä kuljetuksen luotettavuutta**: Toteuta viestien kestävyys, järjestys ja virheiden käsittely yritystapauksissa
- **Optimoida suorituskyky**: Suunnittele kuljetusratkaisuja skaalautuvuuden, viiveen ja läpimenon vaatimuksiin

## **Kuljetusvaatimukset**

### **MCP `2026-07-28` ydinkohdat**

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

## **Azure Event Grid -kuljetuksen toteutus**

Azure Event Grid tarjoaa palvelimettoman tapahtumien reitityspalvelun, joka on ihanteellinen tapahtumalähtöisiin MCP-arkkitehtuureihin. Tämä toteutus osoittaa, kuinka rakentaa skaalautuvia ja löyhästi kytkettyjä MCP-järjestelmiä.

### **Arkkitehtuurin yleiskuvaus**

```mermaid
graph TB
    Client[MCP-asiakas] --> EG[Azure Event Grid]
    EG --> Server[MCP-palvelimen toiminto]
    Server --> EG
    EG --> Client
    
    subgraph "Azure-palvelut"
        EG
        Server
        KV[Key Vault]
        Monitor[Application Insights]
    end
```

### **C#-toteutus - Event Grid -kuljetus**

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

### **TypeScript-toteutus - Event Grid -kuljetus**

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
    
    // Tapahtumapohjainen vastaanotto Azure Functionsin kautta
    onMessage(handler: (message: McpMessage) => Promise<void>): void {
        // Toteutus käyttäisi Azure Functions Event Grid -laukaisinta
        // Tämä on käsitteellinen käyttöliittymä webhook-vastaanottimelle
    }
}

// Azure Functions -toteutus
import { app, InvocationContext, EventGridEvent } from "@azure/functions";

app.eventGrid("mcpEventGridHandler", {
    handler: async (event: EventGridEvent, context: InvocationContext) => {
        try {
            const mcpMessage = event.data as McpMessage;
            
            // Käsittele MCP-viesti
            const response = await mcpServer.processMessage(mcpMessage);
            
            // Lähetä vastaus Event Gridin kautta
            await transport.sendMessage(response);
            
        } catch (error) {
            context.error("Error processing MCP message:", error);
            throw error;
        }
    }
});
```

### **Python-toteutus - Event Grid -kuljetus**

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

# Azure Functions -toteutus
import azure.functions as func
import logging

def main(event: func.EventGridEvent) -> None:
    """Azure Functions Event Grid trigger for MCP messages"""
    try:
        # Jäsennä MCP-viesti Event Grid -tapahtumasta
        mcp_message = json.loads(event.get_body().decode('utf-8'))
        
        # Käsittele MCP-viesti
        response = process_mcp_message(mcp_message)
        
        # Lähetä vastaus takaisin Event Gridin kautta
        # (Toteutus luo uuden Event Grid -asiakkaan)
        
    except Exception as e:
        logging.error(f"Error processing MCP Event Grid message: {e}")
        raise
```

## **Azure Event Hubs -kuljetuksen toteutus**

Azure Event Hubs tarjoaa suuren läpimenon ja reaaliaikaiset suoratoistomahdollisuudet MCP-tilanteisiin, joissa vaaditaan matalaa viivettä ja suurta viestimäärää.

### **Arkkitehtuurin yleiskuvaus**

```mermaid
graph TB
    Client[MCP-asiakas] --> EH[Azure Event Hubs]
    EH --> Server[MCP-palvelin]
    Server --> EH
    EH --> Client
    
    subgraph "Event Hubsin ominaisuudet"
        Partition[Osiointi]
        Retention[Viestien säilytys]
        Scaling[Automaattinen skaalaus]
    end
    
    EH --> Partition
    EH --> Retention
    EH --> Scaling
```


### **C# Toteutus - Event Hubs Kuljetus**

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

### **TypeScript Toteutus - Event Hubs Kuljetus**

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
                        
                        // Päivitä tarkistuspiste vähintään-yhden-kerran toimitukselle
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

### **Python Toteutus - Event Hubs Kuljetus**

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
        
        # Lisää MCP-spesifiset ominaisuudet
        event_data.properties = {
            "messageType": message.get("method", "response"),
            "messageId": message.get("id"),
            "timestamp": "2025-01-14T10:30:00Z"  # Käytä todellista aikaleimaa
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
                starting_position="-1"  # Aloita alusta
            )
    
    def _on_event_received(self, handler: Callable):
        """Internal event handler wrapper"""
        async def handle_event(partition_context, event):
            try:
                # Jäsennä MCP-viesti Event Hubs -tapahtumasta
                message_body = event.body_as_str(encoding='UTF-8')
                mcp_message = json.loads(message_body)
                
                # Käsittele MCP-viesti
                await handler(mcp_message)
                
                # Päivitä tarkistuspiste vähintään kerran toimitusta varten
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

## **Edistyneet Kuljetusmallit**

### **Viestin Kestävyys ja Luotettavuus**

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

### **Kuljetuksen Turvallisuuden Integrointi**

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

### **Kuljetuksen Valvonta ja Havainnointi**

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

## **Yrityksen Integrointiskenaariot**

### **Skenaario 1: Hajautettu MCP-käsittely**

Azure Event Gridin käyttö MCP-pyyntöjen jakamiseen useille käsittelysolmuille:

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

### **Skenaario 2: Reaaliaikainen MCP-suoratoisto**

Azure Event Hubsin käyttö korkeataajuuksiseen MCP-vuorovaikutukseen:

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

### **Skenaario 3: Hybridi Kuljetusarkkitehtuuri**

Useiden kuljetusten yhdistäminen erilaisiin käyttötarkoituksiin:

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

## **Suorituskyvyn Optimointi**

### **Viestien Ryhmittely Event Gridille**

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

### **Osiointistrategia Event Hubsille**

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

## **Mukautettujen Kuljetusten Testaus**

### **Yksikkötestaus Testikaksoisilla**

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

### **Integraatiotestaus Azure Test Containersilla**

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

## **Parhaat Käytännöt ja Ohjeet**

### **Kuljetuksen Suunnittelun Periaatteet**

1. **Idempotenssi**: Varmista viestinkäsittelyn idempotenssi monistusten käsittelyä varten
2. **Virheenkäsittely**: Toteuta kattava virheenkäsittely ja kuolleiden viestien jonot
3. **Valvonta**: Lisää yksityiskohtainen telemetria ja terveystarkastukset
4. **Turvallisuus**: Käytä hallittuja identiteettejä ja vähimmän privilegian periaatetta
5. **Suorituskyky**: Suunnittele spesifisten latenssi- ja läpäisyvaatimustesi mukaisesti

### **Azure-spesifit Suositukset**

1. **Käytä Hallittua Identiteettiä**: Vältä yhteysmerkkijonoja tuotannossa
2. **Toteuta Piirikatkaisijat**: Suojaa Azure-palvelukatkoilta
3. **Seuraa Kustannuksia**: Valvo viestimääriä ja käsittelykustannuksia
4. **Suunnittele Skaalaus**: Suunnittele osiointi- ja skaalausstrategiat varhaisessa vaiheessa
5. **Testaa Huolellisesti**: Käytä Azure DevTest Labsia kattavaan testaukseen

## **Yhteenveto**

Mukautetut MCP-kuljetukset mahdollistavat tehokkaat yritysskenaariot Azure-viestintäpalveluja hyödyntäen. Toteuttamalla Event Grid- tai Event Hubs -kuljetuksia voit rakentaa skaalautuvia, luotettavia MCP-ratkaisuja, jotka integroituvat saumattomasti olemassa olevaan Azure-infrastruktuuriin.

Annetut esimerkit havainnollistavat tuotantovalmiita malleja mukautettujen kuljetusten toteuttamiseen MCP-protokollan vaatimuksia ja Azuren parhaita käytäntöjä noudattaen.

## **Lisäresurssit**

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Azure Event Grid Documentation](https://docs.microsoft.com/azure/event-grid/)
- [Azure Event Hubs Documentation](https://docs.microsoft.com/azure/event-hubs/)
- [Azure Functions Event Grid Trigger](https://docs.microsoft.com/azure/azure-functions/functions-bindings-event-grid)
- [Azure SDK for .NET](https://github.com/Azure/azure-sdk-for-net)
- [Azure SDK for TypeScript](https://github.com/Azure/azure-sdk-for-js)
- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

---

> *Tämä opas keskittyy mukautettuihin arkkitehtuurimalleihin. Vahvista protokolla

> käyttäytyminen [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) mukaisesti,
> ja varmista Azure-käyttö vaatimustesi ja palvelurajojesi mukaisesti.*


## Mitä seuraavaksi
- [6. Yhteisön kontribuutiot](../../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
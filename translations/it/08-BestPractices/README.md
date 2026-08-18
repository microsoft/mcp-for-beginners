# Pratiche Migliori per lo Sviluppo MCP

[![Pratiche Migliori per lo Sviluppo MCP](../../../translated_images/it/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

## Panoramica

Questa lezione si concentra su pratiche avanzate per lo sviluppo, il testing e il deployment di server e funzionalità MCP in ambienti di produzione. Man mano che gli ecosistemi MCP crescono in complessità e importanza, seguire modelli consolidati garantisce affidabilità, manutenibilità e interoperabilità. Questa lezione raccoglie la saggezza pratica derivata da implementazioni MCP reali per guidarti nella creazione di server robusti ed efficienti con risorse, prompt e strumenti efficaci.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Applicare le migliori pratiche del settore nella progettazione di server e funzionalità MCP
- Creare strategie di testing complete per server MCP
- Progettare modelli di workflow efficienti e riutilizzabili per applicazioni MCP complesse
- Implementare una corretta gestione degli errori, registrazione e osservabilità nei server MCP
- Ottimizzare le implementazioni MCP per prestazioni, sicurezza e manutenibilità

## Principi Fondamentali MCP

Prima di entrare nelle pratiche di implementazione specifiche, è importante comprendere i principi fondamentali che guidano uno sviluppo MCP efficace:

1. **Comunicazione Standardizzata**: MCP utilizza JSON-RPC 2.0 come base, fornendo un formato coerente per richieste, risposte e gestione degli errori in tutte le implementazioni.

2. **Design Incentrato sull'Utente**: Dai sempre priorità al consenso, al controllo e alla trasparenza dell'utente nelle tue implementazioni MCP.

3. **Sicurezza Prima di Tutto**: Implementa misure di sicurezza robuste tra cui autenticazione, autorizzazione, validazione e limitazione della frequenza.

4. **Architettura Modulare**: Progetta i tuoi server MCP con un approccio modulare, dove ogni strumento e risorsa ha uno scopo chiaro e focalizzato.

5. **Stato Esplicito**: MCP `2026-07-28` è stateless a livello di protocollo.
   Quando un workflow necessita di uno stato cross-call, usa handle espliciti o
   argomenti ordinari degli strumenti supportati da uno stato applicativo durevole.

## Pratiche Migliori Ufficiali MCP

Le seguenti pratiche migliori sono derivate dalla documentazione ufficiale del Model Context Protocol:

### Pratiche Migliori per la Sicurezza

1. **Consenso e Controllo dell'Utente**: Richiedi sempre il consenso esplicito dell'utente prima di accedere ai dati o eseguire operazioni. Fornisci un controllo chiaro su quali dati vengono condivisi e quali azioni sono autorizzate.

2. **Privacy dei Dati**: Esponi i dati degli utenti solo con consenso esplicito e proteggili con controlli appropriati di accesso. Proteggi contro trasmissioni di dati non autorizzate.

3. **Sicurezza degli Strumenti**: Richiedi il consenso esplicito dell'utente prima di invocare qualsiasi strumento. Assicurati che gli utenti comprendano la funzionalità di ogni strumento e imponga confini di sicurezza robusti.

4. **Controllo dei Permessi degli Strumenti**: Configura quali strumenti un modello può utilizzare per
   ogni richiesta e contesto di autorizzazione, garantendo che siano accessibili solo
   gli strumenti esplicitamente autorizzati.

5. **Autenticazione**: Richiedi un'autenticazione adeguata prima di concedere accesso a strumenti, risorse o operazioni sensibili utilizzando chiavi API, token OAuth o altri metodi di autenticazione sicuri.

6. **Validazione dei Parametri**: Imponi la validazione per tutte le invocazioni degli strumenti per prevenire input malformati o dannosi che raggiungono le implementazioni degli strumenti.

7. **Limitazione della Frequenza**: Implementa la limitazione della frequenza per prevenire abusi e garantire un uso equo delle risorse del server.

### Pratiche Migliori di Implementazione

1. **Negoziazione delle Capacità**: Negozia le versioni di protocollo e
   capacità supportate. In MCP `2026-07-28`, ogni richiesta è autonoma e può
   usare `server/discover`; revisioni precedenti usano il handshake di inizializzazione.

2. **Progettazione degli Strumenti**: Crea strumenti focalizzati che facciano bene una cosa, piuttosto che strumenti monolitici che gestiscono più preoccupazioni.

3. **Gestione degli Errori**: Implementa messaggi di errore e codici standardizzati per aiutare a diagnosticare i problemi, gestire i fallimenti con eleganza e fornire feedback utili.

4. **Osservabilità**: Usa `stderr` per la diagnostica stdio e OpenTelemetry
   per un’osservabilità strutturata. La funzionalità di logging MCP è deprecata nella
   specifica `2026-07-28`.

5. **Tracciamento del Progresso**: Per operazioni di lunga durata, segnala aggiornamenti di progresso per abilitare interfacce utente reattive.

6. **Cancellazione delle Richieste**: Permetti ai client di annullare richieste in corso non più necessarie o troppo lente.

## Riferimenti Aggiuntivi

Per le informazioni più aggiornate sulle pratiche migliori MCP, consulta:

- [Documentazione MCP](https://modelcontextprotocol.io/)
- [Specifiche MCP (2026-07-28)][mcp-2026-spec]
- [Specifiche MCP Precedenti (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Estensione MCP Tasks][mcp-tasks-extension]
- [Repository GitHub](https://github.com/modelcontextprotocol)
- [Pratiche Migliori di Sicurezza](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Rischi di sicurezza e mitigazioni
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formazione pratica sulla sicurezza

### Lezione Companion sulla Affidabilità

I loop di retry generici sono insicuri per strumenti che creano ticket, pagamenti,
messaggi, deployment o altri effetti reali. Una risposta può andare persa
dopo che l’effetto è stato confermato.

Usa la lezione companion sull'affidabilità,
[Retry Sicuri per Strumenti MCP: Un Pattern Sidecar di Affidabilità][reliability-sidecar],
per imparare chiavi di operazione stabili, admission duplicata, checkpointing,
riconciliazione, livelli di evidenza, e iniezione di fallimenti.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Esempi Pratici di Implementazione

### Pratiche Migliori nella Progettazione degli Strumenti

#### 1. Principio di Responsabilità Singola

Ogni strumento MCP dovrebbe avere uno scopo chiaro e focalizzato. Piuttosto che creare strumenti monolitici che tentano di gestire multiple preoccupazioni, sviluppa strumenti specializzati che eccellono in compiti specifici.

```csharp
// A focused tool that does one thing well
public class WeatherForecastTool : ITool
{
    private readonly IWeatherService _weatherService;
    
    public WeatherForecastTool(IWeatherService weatherService)
    {
        _weatherService = weatherService;
    }
    
    public string Name => "weatherForecast";
    public string Description => "Gets weather forecast for a specific location";
    
    public ToolDefinition GetDefinition()
    {
        return new ToolDefinition
        {
            Name = Name,
            Description = Description,
            Parameters = new Dictionary<string, ParameterDefinition>
            {
                ["location"] = new ParameterDefinition
                {
                    Type = ParameterType.String,
                    Description = "City or location name"
                },
                ["days"] = new ParameterDefinition
                {
                    Type = ParameterType.Integer,
                    Description = "Number of forecast days",
                    Default = 3
                }
            },
            Required = new[] { "location" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = parameters.ContainsKey("days") 
            ? Convert.ToInt32(parameters["days"]) 
            : 3;
            
        var forecast = await _weatherService.GetForecastAsync(location, days);
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(JsonSerializer.Serialize(forecast))
            }
        };
    }
}
```

#### 2. Gestione Coerente degli Errori

Implementa una gestione robusta degli errori con messaggi informativi e meccanismi di recupero appropriati.

```python
# Esempio Python con gestione completa degli errori
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Validazione dei parametri
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Validazione della sicurezza
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operazione sul database con timeout
                async with timeout(10):  # Timeout di 10 secondi
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Gli errori di connessione potrebbero essere transitori
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Gli errori di query sono probabilmente errori del client
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Lascia passare gli errori specifici dello strumento
            raise
        except Exception as e:
            # Gestione generale per errori imprevisti
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementazione del rilevamento delle SQL injection
        pass
        
    def _log_error(self, message, error):
        # Implementazione del logging degli errori
        pass
```

#### 3. Validazione dei Parametri

Valida sempre i parametri in modo approfondito per prevenire input malformati o dannosi.

```javascript
// Esempio in JavaScript/TypeScript con validazione dettagliata dei parametri
class FileOperationTool {
  getName() {
    return "fileOperation";
  }
  
  getDescription() {
    return "Performs file operations like read, write, and delete";
  }
  
  getDefinition() {
    return {
      name: this.getName(),
      description: this.getDescription(),
      parameters: {
        operation: {
          type: "string",
          description: "Operation to perform",
          enum: ["read", "write", "delete"]
        },
        path: {
          type: "string",
          description: "File path (must be within allowed directories)"
        },
        content: {
          type: "string",
          description: "Content to write (only for write operation)",
          optional: true
        }
      },
      required: ["operation", "path"]
    };
  }
  
  async execute(parameters) {
    // 1. Verificare la presenza del parametro
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Verificare i tipi dei parametri
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Verificare i valori dei parametri
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Verificare la presenza del contenuto per l'operazione di scrittura
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Validazione della sicurezza del percorso
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementazione basata sui parametri validati
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementazione del controllo di sicurezza del percorso
    // ...
  }
}
```

### Esempi di Implementazione della Sicurezza

#### 1. Autenticazione e Autorizzazione

```java
// Esempio Java con autenticazione e autorizzazione
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Iniezione delle dipendenze
    public SecureDataAccessTool(
            AuthenticationService authService,
            AuthorizationService authzService,
            DataService dataService) {
        this.authService = authService;
        this.authzService = authzService;
        this.dataService = dataService;
    }
    
    @Override
    public String getName() {
        return "secureDataAccess";
    }
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        // 1. Estrarre il contesto di autenticazione
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autenticare l'utente
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Verificare l'autorizzazione per l'operazione specifica
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Procedere con l'operazione autorizzata
        try {
            switch (operation) {
                case "read":
                    Object data = dataService.getData(dataId, user.getId());
                    return ToolResponse.success(data);
                case "update":
                    JsonNode newData = request.getParameters().get("newData");
                    dataService.updateData(dataId, newData, user.getId());
                    return ToolResponse.success("Data updated successfully");
                default:
                    return ToolResponse.error("Unsupported operation: " + operation);
            }
        } catch (Exception e) {
            return ToolResponse.error("Operation failed: " + e.getMessage());
        }
    }
}
```

#### 2. Limitazione della Frequenza

```csharp
// C# rate limiting implementation
public class RateLimitingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly IMemoryCache _cache;
    private readonly ILogger<RateLimitingMiddleware> _logger;
    
    // Configuration options
    private readonly int _maxRequestsPerMinute;
    
    public RateLimitingMiddleware(
        RequestDelegate next,
        IMemoryCache cache,
        ILogger<RateLimitingMiddleware> logger,
        IConfiguration config)
    {
        _next = next;
        _cache = cache;
        _logger = logger;
        _maxRequestsPerMinute = config.GetValue<int>("RateLimit:MaxRequestsPerMinute", 60);
    }
    
    public async Task InvokeAsync(HttpContext context)
    {
        // 1. Get client identifier (API key or user ID)
        string clientId = GetClientIdentifier(context);
        
        // 2. Get rate limiting key for this minute
        string cacheKey = $"rate_limit:{clientId}:{DateTime.UtcNow:yyyyMMddHHmm}";
        
        // 3. Check current request count
        if (!_cache.TryGetValue(cacheKey, out int requestCount))
        {
            requestCount = 0;
        }
        
        // 4. Enforce rate limit
        if (requestCount >= _maxRequestsPerMinute)
        {
            _logger.LogWarning("Rate limit exceeded for client {ClientId}", clientId);
            
            context.Response.StatusCode = StatusCodes.Status429TooManyRequests;
            context.Response.Headers.Add("Retry-After", "60");
            
            await context.Response.WriteAsJsonAsync(new
            {
                error = "Rate limit exceeded",
                message = "Too many requests. Please try again later.",
                retryAfterSeconds = 60
            });
            
            return;
        }
        
        // 5. Increment request count
        _cache.Set(cacheKey, requestCount + 1, TimeSpan.FromMinutes(2));
        
        // 6. Add rate limit headers
        context.Response.Headers.Add("X-RateLimit-Limit", _maxRequestsPerMinute.ToString());
        context.Response.Headers.Add("X-RateLimit-Remaining", (_maxRequestsPerMinute - requestCount - 1).ToString());
        
        // 7. Continue with the request
        await _next(context);
    }
    
    private string GetClientIdentifier(HttpContext context)
    {
        // Implementation to extract API key or user ID
        // ...
    }
}
```

## Pratiche Migliori per il Testing

### 1. Unit Testing di Strumenti MCP

Testa sempre i tuoi strumenti in isolamento, simulando le dipendenze esterne:

```typescript
// Esempio TypeScript di un test unitario per uno strumento
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Crea un servizio meteo fittizio
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Crea lo strumento con la dipendenza fittizia
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Prepara
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Esegui
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Verifica
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Prepara
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Esegui e verifica
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integration Testing

Testa il flusso completo da richieste client a risposte server:

```python
# Esempio di test di integrazione Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Avvia un server di test
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Crea un client
        client = McpClient("http://localhost:5000")
        
        # Testa il rilevamento degli strumenti
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Testa l'esecuzione dello strumento
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verifica la risposta
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Pulisci
        await server.stop()
```

## Ottimizzazione delle Prestazioni

### 1. Strategie di Caching

Implementa caching adeguato per ridurre latenza e utilizzo delle risorse:

```csharp
// C# example with caching
public class CachedWeatherTool : ITool
{
    private readonly IWeatherService _weatherService;
    private readonly IDistributedCache _cache;
    private readonly ILogger<CachedWeatherTool> _logger;
    
    public CachedWeatherTool(
        IWeatherService weatherService,
        IDistributedCache cache,
        ILogger<CachedWeatherTool> logger)
    {
        _weatherService = weatherService;
        _cache = cache;
        _logger = logger;
    }
    
    public string Name => "weatherForecast";
    
    public async Task<ToolResponse> ExecuteAsync(IDictionary<string, object> parameters)
    {
        var location = parameters["location"].ToString();
        var days = Convert.ToInt32(parameters.GetValueOrDefault("days", 3));
        
        // Create cache key
        string cacheKey = $"weather:{location}:{days}";
        
        // Try to get from cache
        string cachedForecast = await _cache.GetStringAsync(cacheKey);
        if (!string.IsNullOrEmpty(cachedForecast))
        {
            _logger.LogInformation("Cache hit for weather forecast: {Location}", location);
            return new ToolResponse
            {
                Content = new List<ContentItem>
                {
                    new TextContent(cachedForecast)
                }
            };
        }
        
        // Cache miss - get from service
        _logger.LogInformation("Cache miss for weather forecast: {Location}", location);
        var forecast = await _weatherService.GetForecastAsync(location, days);
        string forecastJson = JsonSerializer.Serialize(forecast);
        
        // Store in cache (weather forecasts valid for 1 hour)
        await _cache.SetStringAsync(
            cacheKey,
            forecastJson,
            new DistributedCacheEntryOptions
            {
                AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1)
            });
        
        return new ToolResponse
        {
            Content = new List<ContentItem>
            {
                new TextContent(forecastJson)
            }
        };
    }
}
```

#### 2. Injection delle Dipendenze e Testabilità

Progetta strumenti per ricevere le loro dipendenze tramite injection nel costruttore, rendendoli testabili e configurabili:

```java
// Esempio Java con iniezione di dipendenza
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Dipendenze iniettate tramite costruttore
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementazione dello strumento
    // ...
}
```

#### 3. Strumenti Componibili

Progetta strumenti che possono essere composti insieme per creare workflow più complessi:

```python
# Esempio Python che mostra strumenti componibili
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementazione...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Questo strumento può utilizzare i risultati dello strumento dataFetch
    async def execute_async(self, request):
        # Implementazione...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Questo strumento può utilizzare i risultati dello strumento dataAnalysis
    async def execute_async(self, request):
        # Implementazione...
        pass

# Questi strumenti possono essere usati indipendentemente o come parte di un flusso di lavoro
```

### Pratiche Migliori nella Progettazione degli Schemi

Lo schema è il contratto tra il modello e il tuo strumento. Schemi ben progettati portano a una migliore usabilità dello strumento.

#### 1. Descrizioni Chiare dei Parametri

Includi sempre informazioni descrittive per ogni parametro:

```csharp
public object GetSchema()
{
    return new {
        type = "object",
        properties = new {
            query = new { 
                type = "string", 
                description = "Search query text. Use precise keywords for better results." 
            },
            filters = new {
                type = "object",
                description = "Optional filters to narrow down search results",
                properties = new {
                    dateRange = new { 
                        type = "string", 
                        description = "Date range in format YYYY-MM-DD:YYYY-MM-DD" 
                    },
                    category = new { 
                        type = "string", 
                        description = "Category name to filter by" 
                    }
                }
            },
            limit = new { 
                type = "integer", 
                description = "Maximum number of results to return (1-50)",
                default = 10
            }
        },
        required = new[] { "query" }
    };
}
```

#### 2. Vincoli di Validazione

Includi vincoli di validazione per prevenire input non validi:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Proprietà email con validazione del formato
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Proprietà età con vincoli numerici
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Proprietà enumerata
    Map<String, Object> subscription = new HashMap<>();
    subscription.put("type", "string");
    subscription.put("enum", Arrays.asList("free", "basic", "premium"));
    subscription.put("default", "free");
    subscription.put("description", "Subscription tier");
    
    properties.put("email", email);
    properties.put("age", age);
    properties.put("subscription", subscription);
    
    schema.put("properties", properties);
    schema.put("required", Arrays.asList("email"));
    
    return schema;
}
```

#### 3. Strutture di Ritorno Coerenti

Mantieni coerenza nelle strutture di risposta per facilitare l'interpretazione dei risultati da parte dei modelli:

```python
async def execute_async(self, request):
    try:
        # Elabora la richiesta
        results = await self._search_database(request.parameters["query"])
        
        # Restituisci sempre una struttura coerente
        return ToolResponse(
            result={
                "matches": [self._format_item(item) for item in results],
                "totalCount": len(results),
                "queryTime": calculation_time_ms,
                "status": "success"
            }
        )
    except Exception as e:
        return ToolResponse(
            result={
                "matches": [],
                "totalCount": 0,
                "queryTime": 0,
                "status": "error",
                "error": str(e)
            }
        )
    
def _format_item(self, item):
    """Ensures each item has a consistent structure"""
    return {
        "id": item.id,
        "title": item.title,
        "summary": item.summary[:100] + "..." if len(item.summary) > 100 else item.summary,
        "url": item.url,
        "relevance": item.score
    }
```

### Gestione degli Errori

Una gestione robusta degli errori è cruciale per gli strumenti MCP per mantenere l'affidabilità.

#### 1. Gestione Elegante degli Errori

Gestisci gli errori ai livelli appropriati e fornisci messaggi informativi:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    try
    {
        string fileId = request.Parameters.GetProperty("fileId").GetString();
        
        try
        {
            var fileData = await _fileService.GetFileAsync(fileId);
            return new ToolResponse { 
                Result = JsonSerializer.SerializeToElement(fileData) 
            };
        }
        catch (FileNotFoundException)
        {
            throw new ToolExecutionException($"File not found: {fileId}");
        }
        catch (UnauthorizedAccessException)
        {
            throw new ToolExecutionException("You don't have permission to access this file");
        }
        catch (Exception ex) when (ex is IOException || ex is TimeoutException)
        {
            _logger.LogError(ex, "Error accessing file {FileId}", fileId);
            throw new ToolExecutionException("Error accessing file: The service is temporarily unavailable");
        }
    }
    catch (JsonException)
    {
        throw new ToolExecutionException("Invalid file ID format");
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Unexpected error in FileAccessTool");
        throw new ToolExecutionException("An unexpected error occurred");
    }
}
```

#### 2. Risposte di Errore Strutturate

Restituisci informazioni di errore strutturate quando possibile:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementazione
    } catch (Exception ex) {
        Map<String, Object> errorResult = new HashMap<>();
        
        errorResult.put("success", false);
        
        if (ex instanceof ValidationException) {
            ValidationException validationEx = (ValidationException) ex;
            
            errorResult.put("errorType", "validation");
            errorResult.put("errorMessage", validationEx.getMessage());
            errorResult.put("validationErrors", validationEx.getErrors());
            
            return new ToolResponse.Builder()
                .setResult(errorResult)
                .build();
        }
        
        // Rilancia altre eccezioni come ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logica di Retry

Usa la logica di retry generica solo per chiamate in sola lettura o operazioni il cui
contratto a valle è già idempotente. Per operazioni con effetti, un timeout
dopo l’invio della richiesta è ambiguo. Ricongiungi lo stato autorevole e
riutilizza la stessa chiave di operazione stabile prima di eseguire nuovamente. Vedi la
[lezione companion sidecar di affidabilità](./reliability-sidecars/README.md).

Il seguente loop di retry limitato è adatto per una ricerca in sola lettura:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # secondi
    
    while retry_count < max_retries:
        try:
            # Chiamare un'API esterna in sola lettura
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Backoff esponenziale
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Errore non transitorio, non ritentare
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Ottimizzazione delle Prestazioni

#### 1. Caching

Implementa caching per operazioni costose:

```csharp
public class CachedDataTool : IMcpTool
{
    private readonly IDatabase _database;
    private readonly IMemoryCache _cache;
    
    public CachedDataTool(IDatabase database, IMemoryCache cache)
    {
        _database = database;
        _cache = cache;
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var query = request.Parameters.GetProperty("query").GetString();
        
        // Create cache key based on parameters
        var cacheKey = $"data_query_{ComputeHash(query)}";
        
        // Try to get from cache first
        if (_cache.TryGetValue(cacheKey, out var cachedResult))
        {
            return new ToolResponse { Result = cachedResult };
        }
        
        // Cache miss - perform actual query
        var result = await _database.QueryAsync(query);
        
        // Store in cache with expiration
        var cacheOptions = new MemoryCacheEntryOptions()
            .SetAbsoluteExpiration(TimeSpan.FromMinutes(15));
            
        _cache.Set(cacheKey, JsonSerializer.SerializeToElement(result), cacheOptions);
        
        return new ToolResponse { Result = JsonSerializer.SerializeToElement(result) };
    }
    
    private string ComputeHash(string input)
    {
        // Implementation to generate stable hash for cache key
    }
}
```

#### 2. Elaborazione Asincrona

Usa modelli di programmazione asincrona per operazioni I/O-bound:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Per operazioni di lunga durata, restituisci immediatamente un ID di elaborazione
        String processId = UUID.randomUUID().toString();
        
        // Avvia l'elaborazione asincrona
        CompletableFuture.runAsync(() -> {
            try {
                // Esegui l'operazione di lunga durata
                documentService.processDocument(documentId);
                
                // Aggiorna lo stato (di solito verrebbe archiviato in un database)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Restituisci una risposta immediata con l'ID del processo
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Strumento di controllo dello stato companion
    public class ProcessStatusTool implements Tool {
        @Override
        public ToolResponse execute(ToolRequest request) {
            String processId = request.getParameters().get("processId").asText();
            ProcessStatus status = processStatusRepository.getStatus(processId);
            
            return new ToolResponse.Builder().setResult(status).build();
        }
    }
}
```

#### 3. Limitazione delle Risorse

Implementa la limitazione delle risorse per prevenire sovraccarichi:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Consenti 5 richieste al secondo
            bucket_size=10        # Consenti picchi fino a 10 richieste
        )
    
    async def execute_async(self, request):
        # Controlla se possiamo procedere o dobbiamo aspettare
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Se l'attesa è troppo lunga
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Attendi per il tempo di ritardo appropriato
                await asyncio.sleep(delay)
        
        # Consuma un token e procedi con la richiesta
        self.rate_limiter.consume()
        
        # Chiama l'API
        result = await self._call_api(request.parameters)
        return ToolResponse(result=result)

class TokenBucketRateLimiter:
    def __init__(self, tokens_per_second, bucket_size):
        self.tokens_per_second = tokens_per_second
        self.bucket_size = bucket_size
        self.tokens = bucket_size
        self.last_refill = time.time()
        self.lock = asyncio.Lock()
    
    async def get_delay_time(self):
        async with self.lock:
            self._refill()
            if self.tokens >= 1:
                return 0
            
            # Calcola il tempo fino a quando il prossimo token sarà disponibile
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Aggiungi nuovi token basati sul tempo trascorso
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Pratiche Migliori di Sicurezza

#### 1. Validazione degli Input

Valida sempre accuratamente i parametri di input:

```csharp
public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
{
    // Validate parameters exist
    if (!request.Parameters.TryGetProperty("query", out var queryProp))
    {
        throw new ToolExecutionException("Missing required parameter: query");
    }
    
    // Validate correct type
    if (queryProp.ValueKind != JsonValueKind.String)
    {
        throw new ToolExecutionException("Query parameter must be a string");
    }
    
    var query = queryProp.GetString();
    
    // Validate string content
    if (string.IsNullOrWhiteSpace(query))
    {
        throw new ToolExecutionException("Query parameter cannot be empty");
    }
    
    if (query.Length > 500)
    {
        throw new ToolExecutionException("Query parameter exceeds maximum length of 500 characters");
    }
    
    // Check for SQL injection attacks if applicable
    if (ContainsSqlInjection(query))
    {
        throw new ToolExecutionException("Invalid query: contains potentially unsafe SQL");
    }
    
    // Proceed with execution
    // ...
}
```

#### 2. Controlli di Autorizzazione

Implementa controlli appropriati di autorizzazione:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Ottieni il contesto utente dalla richiesta
    UserContext user = request.getContext().getUserContext();
    
    // Verifica se l'utente ha i permessi richiesti
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Per risorse specifiche, verifica l'accesso a quella risorsa
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Procedi con l'esecuzione dello strumento
    // ...
}
```

#### 3. Gestione dei Dati Sensibili

Gestisci con cura i dati sensibili:

```python
class SecureDataTool(Tool):
    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "userId": {"type": "string"},
                "includeSensitiveData": {"type": "boolean", "default": False}
            },
            "required": ["userId"]
        }
    
    async def execute_async(self, request):
        user_id = request.parameters["userId"]
        include_sensitive = request.parameters.get("includeSensitiveData", False)
        
        # Ottieni i dati dell'utente
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtra i campi sensibili a meno che non siano esplicitamente richiesti E autorizzati
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Controlla il livello di autorizzazione nel contesto della richiesta
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Crea una copia per evitare di modificare l'originale
        redacted = user_data.copy()
        
        # Redigi campi sensibili specifici
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Redigi dati sensibili annidati
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Pratiche Migliori per il Testing degli Strumenti MCP

Un testing completo assicura che gli strumenti MCP funzionino correttamente, gestiscano casi limite e si integrino appropriatamente con il resto del sistema.

### Unit Testing

#### 1. Testa Ogni Strumento in Isolamento

Crea test focalizzati per la funzionalità di ogni strumento:

```csharp
[Fact]
public async Task WeatherTool_ValidLocation_ReturnsCorrectForecast()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("Seattle", 3))
        .ReturnsAsync(new WeatherForecast(/* test data */));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "Seattle", 
            days = 3 
        })
    );
    
    // Act
    var response = await tool.ExecuteAsync(request);
    
    // Assert
    Assert.NotNull(response);
    var result = JsonSerializer.Deserialize<WeatherForecast>(response.Result);
    Assert.Equal("Seattle", result.Location);
    Assert.Equal(3, result.DailyForecasts.Count);
}

[Fact]
public async Task WeatherTool_InvalidLocation_ThrowsToolExecutionException()
{
    // Arrange
    var mockWeatherService = new Mock<IWeatherService>();
    mockWeatherService
        .Setup(s => s.GetForecastAsync("InvalidLocation", It.IsAny<int>()))
        .ThrowsAsync(new LocationNotFoundException("Location not found"));
    
    var tool = new WeatherForecastTool(mockWeatherService.Object);
    
    var request = new ToolRequest(
        toolName: "weatherForecast",
        parameters: JsonSerializer.SerializeToElement(new { 
            location = "InvalidLocation", 
            days = 3 
        })
    );
    
    // Act & Assert
    var exception = await Assert.ThrowsAsync<ToolExecutionException>(
        () => tool.ExecuteAsync(request)
    );
    
    Assert.Contains("Location not found", exception.Message);
}
```

#### 2. Test di Validazione degli Schemi

Verifica che gli schemi siano validi e impongano correttamente i vincoli:

```java
@Test
public void testSchemaValidation() {
    // Crea istanza dello strumento
    SearchTool searchTool = new SearchTool();
    
    // Ottieni schema
    Object schema = searchTool.getSchema();
    
    // Converti schema in JSON per la validazione
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Valida che lo schema sia un JSONSchema valido
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Testa parametri validi
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Testa parametro obbligatorio mancante
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Testa tipo di parametro non valido
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Test di Gestione degli Errori

Crea test specifici per condizioni di errore:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Disporre
    tool = ApiTool(timeout=0.1)  # Timeout molto breve
    
    # Simulare una richiesta che scadrà
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Più lungo del timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Azione e verifica
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verificare il messaggio di eccezione
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Disporre
    tool = ApiTool()
    
    # Simulare una risposta con limite di frequenza
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            status=429,
            headers={"Retry-After": "2"},
            body=json.dumps({"error": "Rate limit exceeded"})
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Azione e verifica
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verificare che l'eccezione contenga informazioni sul limite di frequenza
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integration Testing

#### 1. Test della Catena di Strumenti

Testa gli strumenti che lavorano insieme nelle combinazioni previste:

```csharp
[Fact]
public async Task DataProcessingWorkflow_CompletesSuccessfully()
{
    // Arrange
    var dataFetchTool = new DataFetchTool(mockDataService.Object);
    var analysisTools = new DataAnalysisTool(mockAnalysisService.Object);
    var visualizationTool = new DataVisualizationTool(mockVisualizationService.Object);
    
    var toolRegistry = new ToolRegistry();
    toolRegistry.RegisterTool(dataFetchTool);
    toolRegistry.RegisterTool(analysisTools);
    toolRegistry.RegisterTool(visualizationTool);
    
    var workflowExecutor = new WorkflowExecutor(toolRegistry);
    
    // Act
    var result = await workflowExecutor.ExecuteWorkflowAsync(new[] {
        new ToolCall("dataFetch", new { source = "sales2023" }),
        new ToolCall("dataAnalysis", ctx => new { 
            data = ctx.GetResult("dataFetch"),
            analysis = "trend" 
        }),
        new ToolCall("dataVisualize", ctx => new {
            analysisResult = ctx.GetResult("dataAnalysis"),
            type = "line-chart"
        })
    });
    
    // Assert
    Assert.NotNull(result);
    Assert.True(result.Success);
    Assert.NotNull(result.GetResult("dataVisualize"));
    Assert.Contains("chartUrl", result.GetResult("dataVisualize").ToString());
}
```

#### 2. Test del Server MCP

Testa il server MCP con registrazione ed esecuzione completa degli strumenti:

```java
@SpringBootTest
@AutoConfigureMockMvc
public class McpServerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private ObjectMapper objectMapper;
    
    @Test
    public void testToolDiscovery() throws Exception {
        // Testare l'endpoint di scoperta
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Creare la richiesta dello strumento
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Inviare la richiesta e verificare la risposta
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Creare una richiesta strumento non valida
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Parametro mancante "b"
        request.put("parameters", parameters);
        
        // Inviare la richiesta e verificare la risposta di errore
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Test End-to-End

Testa workflow completi dal prompt del modello all’esecuzione dello strumento:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Organizza - Configura il client MCP e il modello mock
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Risposte del modello mock
    mock_model = MockLanguageModel([
        MockResponse(
            "What's the weather in Seattle?",
            tool_calls=[{
                "tool_name": "weatherForecast",
                "parameters": {"location": "Seattle", "days": 3}
            }]
        ),
        MockResponse(
            "Here's the weather forecast for Seattle:\n- Today: 65°F, Partly Cloudy\n- Tomorrow: 68°F, Sunny\n- Day after: 62°F, Rain",
            tool_calls=[]
        )
    ])
    
    # Risposta dello strumento meteo mock
    with aioresponses() as mocked:
        mocked.post(
            "http://localhost:5000/mcp/execute",
            payload={
                "result": {
                    "location": "Seattle",
                    "forecast": [
                        {"date": "2023-06-01", "temperature": 65, "conditions": "Partly Cloudy"},
                        {"date": "2023-06-02", "temperature": 68, "conditions": "Sunny"},
                        {"date": "2023-06-03", "temperature": 62, "conditions": "Rain"}
                    ]
                }
            }
        )
        
        # Agisci
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Asserisci
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Test delle Prestazioni

#### 1. Test di Carico

Verifica quanti richieste simultanee il tuo server MCP può gestire:

```csharp
[Fact]
public async Task McpServer_HandlesHighConcurrency()
{
    // Arrange
    var server = new McpServer(
        name: "TestServer",
        version: "1.0",
        maxConcurrentRequests: 100
    );
    
    server.RegisterTool(new FastExecutingTool());
    await server.StartAsync();
    
    var client = new McpClient("http://localhost:5000");
    
    // Act
    var tasks = new List<Task<McpResponse>>();
    for (int i = 0; i < 1000; i++)
    {
        tasks.Add(client.ExecuteToolAsync("fastTool", new { iteration = i }));
    }
    
    var results = await Task.WhenAll(tasks);
    
    // Assert
    Assert.Equal(1000, results.Length);
    Assert.All(results, r => Assert.NotNull(r));
}
```

#### 2. Test di Stress

Testa il sistema sotto carichi estremi:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Configurare JMeter per il test di stress
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Configurare il piano di test JMeter
    HashTree testPlanTree = new HashTree();
    
    // Creare piano di test, gruppo di thread, sampler, ecc.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Aggiungere sampler HTTP per l'esecuzione dello strumento
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Aggiungere ascoltatori
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Eseguire il test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Validare i risultati
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Tempo medio di risposta < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90° percentile < 500ms
}
```

#### 3. Monitoraggio e Profilazione

Imposta il monitoraggio per analisi delle prestazioni a lungo termine:

```python
# Configurare il monitoraggio per un server MCP
def configure_monitoring(server):
    # Configurare le metriche di Prometheus
    prometheus_metrics = {
        "request_count": Counter("mcp_requests_total", "Total MCP requests"),
        "request_latency": Histogram(
            "mcp_request_duration_seconds", 
            "Request duration in seconds",
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_execution_count": Counter(
            "mcp_tool_executions_total", 
            "Tool execution count",
            labelnames=["tool_name"]
        ),
        "tool_execution_latency": Histogram(
            "mcp_tool_duration_seconds", 
            "Tool execution duration in seconds",
            labelnames=["tool_name"],
            buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
        ),
        "tool_errors": Counter(
            "mcp_tool_errors_total",
            "Tool execution errors",
            labelnames=["tool_name", "error_type"]
        )
    }
    
    # Aggiungere middleware per la temporizzazione e la registrazione delle metriche
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Esporre l'endpoint delle metriche
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Modelli di Progettazione del Workflow MCP

Workflow MCP ben progettati migliorano efficienza, affidabilità e manutenibilità. Ecco i modelli chiave da seguire:

### 1. Modello Catena di Strumenti

Collega più strumenti in una sequenza dove l’output di ogni strumento diventa input per il successivo:

```python
# Implementazione di Python Chain of Tools
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Elenco dei nomi degli strumenti da eseguire in sequenza
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Esegui ogni strumento nella catena, passando il risultato precedente
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Memorizza il risultato e usalo come input per il prossimo strumento
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Esempio di utilizzo
data_processing_chain = ChainWorkflow([
    "dataFetch",
    "dataCleaner",
    "dataAnalyzer",
    "dataVisualizer"
])

result = await data_processing_chain.execute(
    mcp_client,
    {"source": "sales_database", "table": "transactions"}
)
```

### 2. Modello Dispatcher

Usa uno strumento centrale che dispaccia verso strumenti specializzati basandosi sull’input:

```csharp
public class ContentDispatcherTool : IMcpTool
{
    private readonly IMcpClient _mcpClient;
    
    public ContentDispatcherTool(IMcpClient mcpClient)
    {
        _mcpClient = mcpClient;
    }
    
    public string Name => "contentProcessor";
    public string Description => "Processes content of various types";
    
    public object GetSchema()
    {
        return new {
            type = "object",
            properties = new {
                content = new { type = "string" },
                contentType = new { 
                    type = "string",
                    enum = new[] { "text", "html", "markdown", "csv", "code" }
                },
                operation = new { 
                    type = "string",
                    enum = new[] { "summarize", "analyze", "extract", "convert" }
                }
            },
            required = new[] { "content", "contentType", "operation" }
        };
    }
    
    public async Task<ToolResponse> ExecuteAsync(ToolRequest request)
    {
        var content = request.Parameters.GetProperty("content").GetString();
        var contentType = request.Parameters.GetProperty("contentType").GetString();
        var operation = request.Parameters.GetProperty("operation").GetString();
        
        // Determine which specialized tool to use
        string targetTool = DetermineTargetTool(contentType, operation);
        
        // Forward to the specialized tool
        var specializedResponse = await _mcpClient.ExecuteToolAsync(
            targetTool,
            new { content, options = GetOptionsForTool(targetTool, operation) }
        );
        
        return new ToolResponse { Result = specializedResponse.Result };
    }
    
    private string DetermineTargetTool(string contentType, string operation)
    {
        return (contentType, operation) switch
        {
            ("text", "summarize") => "textSummarizer",
            ("text", "analyze") => "textAnalyzer",
            ("html", _) => "htmlProcessor",
            ("markdown", _) => "markdownProcessor",
            ("csv", _) => "csvProcessor",
            ("code", _) => "codeAnalyzer",
            _ => throw new ToolExecutionException($"No tool available for {contentType}/{operation}")
        };
    }
    
    private object GetOptionsForTool(string toolName, string operation)
    {
        // Return appropriate options for each specialized tool
        return toolName switch
        {
            "textSummarizer" => new { length = "medium" },
            "htmlProcessor" => new { cleanUp = true, operation },
            // Options for other tools...
            _ => new { }
        };
    }
}
```

### 3. Modello di Elaborazione Parallela

Esegui più strumenti simultaneamente per efficienza:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Passo 1: Recupera i metadati del dataset (sincrono)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Passo 2: Avvia più analisi in parallelo
        CompletableFuture<ToolResponse> statisticalAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("statisticalAnalysis", Map.of(
                "datasetId", datasetId,
                "type", "comprehensive"
            ))
        );
        
        CompletableFuture<ToolResponse> correlationAnalysis = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("correlationAnalysis", Map.of(
                "datasetId", datasetId,
                "method", "pearson"
            ))
        );
        
        CompletableFuture<ToolResponse> outlierDetection = CompletableFuture.supplyAsync(() ->
            mcpClient.executeTool("outlierDetection", Map.of(
                "datasetId", datasetId,
                "sensitivity", "medium"
            ))
        );
        
        // Attendi che tutti i compiti paralleli siano completati
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Attendi il completamento
        
        // Passo 3: Combina i risultati
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Passo 4: Genera il rapporto riassuntivo
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Restituisci il risultato completo del flusso di lavoro
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Modello di Recupero dagli Errori

Implementa fallback eleganti per i fallimenti degli strumenti:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Prova prima lo strumento principale
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Registra il fallimento
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Passa allo strumento secondario
            try:
                # Potrebbe essere necessario trasformare i parametri per lo strumento di riserva
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Entrambi gli strumenti hanno fallito
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Questa implementazione dipenderebbe dagli strumenti specifici
        # Per questo esempio, restituiremo semplicemente i parametri originali
        return params

# Esempio di utilizzo
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API meteo primaria (a pagamento)
        "basicWeatherService",    # API meteo di riserva (gratuita)
        {"location": location}
    )
```

### 5. Modello di Composizione del Workflow

Costruisci workflow complessi componendo quelli più semplici:

```csharp
public class CompositeWorkflow : IWorkflow
{
    private readonly List<IWorkflow> _workflows;
    
    public CompositeWorkflow(IEnumerable<IWorkflow> workflows)
    {
        _workflows = new List<IWorkflow>(workflows);
    }
    
    public async Task<WorkflowResult> ExecuteAsync(WorkflowContext context)
    {
        var results = new Dictionary<string, object>();
        
        foreach (var workflow in _workflows)
        {
            var workflowResult = await workflow.ExecuteAsync(context);
            
            // Store each workflow's result
            results[workflow.Name] = workflowResult;
            
            // Update context with the result for the next workflow
            context = context.WithResult(workflow.Name, workflowResult);
        }
        
        return new WorkflowResult(results);
    }
    
    public string Name => "CompositeWorkflow";
    public string Description => "Executes multiple workflows in sequence";
}

// Example usage
var documentWorkflow = new CompositeWorkflow(new IWorkflow[] {
    new DocumentFetchWorkflow(),
    new DocumentProcessingWorkflow(),
    new InsightGenerationWorkflow(),
    new ReportGenerationWorkflow()
});

var result = await documentWorkflow.ExecuteAsync(new WorkflowContext {
    Parameters = new { documentId = "12345" }
});
```

# Testing di Server MCP: Pratiche Migliori e Consigli Principali

## Panoramica

Il testing è un aspetto critico dello sviluppo di server MCP affidabili e di alta qualità. Questa guida fornisce pratiche migliori e consigli completi per il testing dei tuoi server MCP durante l'intero ciclo di sviluppo, dai test unitari agli integration test e alla validazione end-to-end.

## Perché il Testing è Importante per i Server MCP

I server MCP fungono da middleware cruciale tra modelli AI e applicazioni client. Un testing accurato garantisce:

- Affidabilità in ambienti di produzione
- Gestione accurata di richieste e risposte
- Corretta implementazione delle specifiche MCP
- Resilienza contro fallimenti e casi limite
- Prestazioni costanti sotto vari carichi

## Unit Testing per Server MCP

### Unit Testing (Base)

I test unitari verificano i singoli componenti del tuo server MCP in isolamento.

#### Cosa Testare

1. **Gestori di Risorse**: Testa logicamente ogni gestore di risorse in modo indipendente
2. **Implementazioni degli Strumenti**: Verifica il comportamento degli strumenti con vari input
3. **Template di Prompt**: Assicurati che i template dei prompt vengano resi correttamente
4. **Validazione dello Schema**: Testa la logica di validazione dei parametri
5. **Gestione degli Errori**: Verifica risposte di errore per input non validi

#### Pratiche Migliori per il Unit Testing

```csharp
// Example unit test for a calculator tool in C#
[Fact]
public async Task CalculatorTool_Add_ReturnsCorrectSum()
{
    // Arrange
    var calculator = new CalculatorTool();
    var parameters = new Dictionary<string, object>
    {
        ["operation"] = "add",
        ["a"] = 5,
        ["b"] = 7
    };
    
    // Act
    var response = await calculator.ExecuteAsync(parameters);
    var result = JsonSerializer.Deserialize<CalculationResult>(response.Content[0].ToString());
    
    // Assert
    Assert.Equal(12, result.Value);
}
```

```python
# Esempio di test unitario per uno strumento calcolatrice in Python
def test_calculator_tool_add():
    # Prepara
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Agisci
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Verifica
    assert result["value"] == 12
```

### Integration Testing (Livello Intermedio)

I test di integrazione verificano le interazioni tra i componenti del tuo server MCP.

#### Cosa Testare

1. **Inizializzazione del Server**: Testa l’avvio del server con varie configurazioni
2. **Registrazione delle Rotte**: Verifica che tutti gli endpoint siano registrati correttamente
3. **Elaborazione delle Richieste**: Testa il ciclo completo richiesta-risposta
4. **Propagazione degli Errori**: Garantire che gli errori siano gestiti correttamente tra i componenti
5. **Autenticazione e Autorizzazione**: Testa i meccanismi di sicurezza

#### Pratiche Migliori per Integration Testing

```csharp
// Example integration test for MCP server in C#
[Fact]
public async Task Server_ProcessToolRequest_ReturnsValidResponse()
{
    // Arrange
    var server = new McpServer();
    server.RegisterTool(new CalculatorTool());
    await server.StartAsync();
    
    var request = new McpRequest
    {
        Tool = "calculator",
        Parameters = new Dictionary<string, object>
        {
            ["operation"] = "multiply",
            ["a"] = 6,
            ["b"] = 7
        }
    };
    
    // Act
    var response = await server.ProcessRequestAsync(request);
    
    // Assert
    Assert.NotNull(response);
    Assert.Equal(McpStatusCodes.Success, response.StatusCode);
    // Additional assertions for response content
    
    // Cleanup
    await server.StopAsync();
}
```

### End-to-End Testing (Livello Superiore)

I test end-to-end verificano il comportamento completo del sistema dal client al server.

#### Cosa Testare

1. **Comunicazione Client-Server**: Testa cicli completi richiesta-risposta
2. **SDK Client Reali**: Testa con implementazioni client reali
3. **Prestazioni sotto Carico**: Verifica il comportamento con molteplici richieste concorrenti
4. **Recupero dagli Errori**: Testa il recupero del sistema da fallimenti

5. **Operazioni a Lungo Termine**: Verificare la gestione dello streaming e delle operazioni prolungate

#### Best Practices per il Testing E2E

```typescript
// Esempio di test E2E con un client in TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Avvia il server nell'ambiente di test
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Esegui
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Verifica
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Strategie di Mocking per il Testing MCP

Il mocking è essenziale per isolare i componenti durante il testing.

### Componenti da Mockare

1. **Modelli AI Esterni**: Mockare le risposte del modello per un testing prevedibile
2. **Servizi Esterni**: Mockare le dipendenze API (database, servizi di terze parti)
3. **Servizi di Autenticazione**: Mockare i provider di identità
4. **Fornitori di Risorse**: Mockare i gestori di risorse costose

### Esempio: Mockare una Risposta di un Modello AI

```csharp
// C# example with Moq
var mockModel = new Mock<ILanguageModel>();
mockModel
    .Setup(m => m.GenerateResponseAsync(
        It.IsAny<string>(),
        It.IsAny<McpRequestContext>()))
    .ReturnsAsync(new ModelResponse { 
        Text = "Mocked model response",
        FinishReason = FinishReason.Completed
    });

var server = new McpServer(modelClient: mockModel.Object);
```

```python
# Esempio Python con unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Configura il mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Usa il mock nel test
    server = McpServer(model_client=mock_model)
    # Continua con il test
```

## Testing delle Prestazioni

Il testing delle prestazioni è cruciale per i server MCP in produzione.

### Cosa Misurare

1. **Latenza**: Tempo di risposta per le richieste
2. **Throughput**: Richieste gestite per secondo
3. **Utilizzo delle Risorse**: CPU, memoria, utilizzo della rete
4. **Gestione della Concorrenza**: Comportamento sotto richieste parallele
5. **Caratteristiche di Scalabilità**: Prestazioni al crescere del carico

### Strumenti per il Testing delle Prestazioni

- **k6**: Strumento open-source per il load testing
- **JMeter**: Testing delle prestazioni completo
- **Locust**: Load testing basato su Python
- **Azure Load Testing**: Testing delle prestazioni basato sul cloud

### Esempio: Test di Carico Base con k6

```javascript
// script k6 per test di carico del server MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 utenti virtuali
  duration: '30s',
};

export default function () {
  const payload = JSON.stringify({
    tool: 'calculator',
    parameters: {
      operation: 'add',
      a: Math.floor(Math.random() * 100),
      b: Math.floor(Math.random() * 100)
    }
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer test-token'
    },
  };

  const res = http.post('http://localhost:5000/api/tools/invoke', payload, params);
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  
  sleep(1);
}
```

## Automazione del Testing per i Server MCP

Automatizzare i tuoi test assicura qualità costante e cicli di feedback più rapidi.

### Integrazione CI/CD

1. **Esegui i Test Unitari sulle Pull Request**: Assicurati che le modifiche al codice non rompano funzionalità esistenti
2. **Test di Integrazione in Staging**: Esegui test di integrazione in ambienti pre-produzione
3. **Baseline delle Prestazioni**: Mantieni benchmark di performance per rilevare regressioni
4. **Scansioni di Sicurezza**: Automatizza il testing della sicurezza come parte della pipeline

### Esempio di Pipeline CI (GitHub Actions)

```yaml
name: MCP Server Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Runtime
      uses: actions/setup-dotnet@v1
      with:
        dotnet-version: '8.0.x'
    
    - name: Restore dependencies
      run: dotnet restore
    
    - name: Build
      run: dotnet build --no-restore
    
    - name: Unit Tests
      run: dotnet test --no-build --filter Category=Unit
    
    - name: Integration Tests
      run: dotnet test --no-build --filter Category=Integration
      
    - name: Performance Tests
      run: dotnet run --project tests/PerformanceTests/PerformanceTests.csproj
```

## Testing per la Conformità alla Specifica MCP

Verifica che il tuo server implementi correttamente la specifica MCP.

### Aree Chiave di Conformità

1. **API Endpoint**: Testare gli endpoint richiesti (/resources, /tools, ecc.)
2. **Formato Richiesta/Risposta**: Validare la conformità agli schemi
3. **Codici di Errore**: Verificare i codici di stato corretti per vari scenari
4. **Tipi di Contenuto**: Testare la gestione di diversi tipi di contenuto
5. **Flusso di Autenticazione**: Verificare i meccanismi di autenticazione conformi alla specifica

### Suite di Test per la Conformità

```csharp
[Fact]
public async Task Server_ResourceEndpoint_ReturnsCorrectSchema()
{
    // Arrange
    var client = new HttpClient();
    client.DefaultRequestHeaders.Add("Authorization", "Bearer test-token");
    
    // Act
    var response = await client.GetAsync("http://localhost:5000/api/resources");
    var content = await response.Content.ReadAsStringAsync();
    var resources = JsonSerializer.Deserialize<ResourceList>(content);
    
    // Assert
    Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    Assert.NotNull(resources);
    Assert.All(resources.Resources, resource => 
    {
        Assert.NotNull(resource.Id);
        Assert.NotNull(resource.Type);
        // Additional schema validation
    });
}
```

## Top 10 Consigli per un Testing Efficace dei Server MCP

1. **Testare le Definizioni degli Strumenti Separatamente**: Verificare le definizioni degli schemi indipendentemente dalla logica dello strumento
2. **Usare Test Parametrizzati**: Testare gli strumenti con una varietà di input, inclusi casi limite
3. **Controllare le Risposte di Errore**: Verificare la corretta gestione degli errori per tutte le condizioni possibili
4. **Testare la Logica di Autorizzazione**: Assicurare un controllo degli accessi adeguato per i diversi ruoli utente
5. **Monitorare la Copertura dei Test**: Mirare a un’elevata copertura del codice dei percorsi critici
6. **Testare le Risposte in Streaming**: Verificare la corretta gestione di contenuti in streaming
7. **Simulare Problemi di Rete**: Testare il comportamento in condizioni di rete scadente
8. **Testare i Limiti delle Risorse**: Verificare il comportamento al raggiungimento di quote o limiti di velocità
9. **Automatizzare i Test di Regressione**: Costruire una suite che venga eseguita ad ogni modifica del codice
10. **Documentare i Casi di Test**: Mantenere una documentazione chiara degli scenari di test

## Errori Comuni nel Testing

- **Eccessiva dipendenza dal testing del percorso felice**: Assicurarsi di testare accuratamente i casi di errore
- **Ignorare il testing delle prestazioni**: Identificare i colli di bottiglia prima che influenzino la produzione
- **Testing in isolamento soltanto**: Combinare test unitari, di integrazione e E2E
- **Copertura API incompleta**: Assicurarsi che tutti gli endpoint e le funzionalità siano testati
- **Ambientazioni di test incoerenti**: Usare container per garantire ambienti di test consistenti

## Conclusione

Una strategia di testing completa è essenziale per sviluppare server MCP affidabili e di alta qualità. Implementando le best practice e i consigli illustrati in questa guida, puoi garantire che le tue implementazioni MCP raggiungano i più alti standard di qualità, affidabilità e prestazioni.


## Punti Chiave

1. **Progettazione degli Strumenti**: Seguire il principio di responsabilità unica, usare dependency injection e progettare per la componibilità
2. **Progettazione degli Schemi**: Creare schemi chiari, ben documentati con appropriati vincoli di validazione
3. **Gestione degli Errori**: Implementare una gestione degli errori elegante, risposte di errore strutturate e logica di retry consapevole degli esiti

4. **Prestazioni**: Usare caching, elaborazione asincrona e throttling delle risorse
5. **Sicurezza**: Applicare una convalida rigorosa degli input, controlli di autorizzazione e gestione dei dati sensibili
6. **Testing**: Creare test unitari, di integrazione e end-to-end completi
7. **Pattern di Workflow**: Applicare pattern consolidati come catene, dispatcher e elaborazione parallela

## Esercizio

Progetta uno strumento MCP e un workflow per un sistema di elaborazione documenti che:

1. Accetti documenti in formati multipli (PDF, DOCX, TXT)
2. Estragga testo e informazioni chiave dai documenti
3. Classifichi i documenti per tipo e contenuto
4. Generi un riassunto di ciascun documento

Implementa gli schemi dello strumento, la gestione degli errori e un pattern di workflow che si adatti meglio a questo scenario. Considera come testeresti questa implementazione.

## Risorse 

1. Unisciti alla community MCP su [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) per rimanere aggiornato sugli ultimi sviluppi 
2. Contribuisci ai [progetti MCP open-source](https://github.com/modelcontextprotocol)
3. Applica i principi MCP nelle iniziative AI della tua organizzazione
4. Esplora implementazioni MCP specializzate per il tuo settore. 
5. Considera di seguire corsi avanzati su argomenti specifici MCP, come integrazione multimodale o integrazione di applicazioni enterprise.
6. Sperimenta costruendo i tuoi strumenti e workflow MCP usando i principi appresi nel [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Cosa Aspettarsi

Successivo: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
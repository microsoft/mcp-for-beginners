# Cele mai bune practici pentru dezvoltarea MCP

[![Cele mai bune practici pentru dezvoltarea MCP](../../../translated_images/ro/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

## Prezentare generală

Această lecție se concentrează pe cele mai bune practici avansate pentru dezvoltarea, testarea și implementarea serverelor și funcțiilor MCP în medii de producție. Pe măsură ce ecosistemele MCP devin tot mai complexe și importante, urmarea unor modele stabilite asigură fiabilitate, întreținere și interoperabilitate. Această lecție consolidează înțelepciunea practică dobândită din implementări MCP din lumea reală pentru a vă ghida în crearea de servere robuste, eficiente, cu resurse, solicitări și instrumente eficiente.

## Obiectivele de învățare

Până la sfârșitul acestei lecții, veți putea să:

- Aplicați cele mai bune practici din industrie în designul serverelor și funcțiilor MCP
- Creați strategii cuprinzătoare de testare pentru serverele MCP
- Proiectați modele de flux de lucru eficiente și reutilizabile pentru aplicații MCP complexe
- Implementați o gestionare corectă a erorilor, jurnalizare și observabilitate în serverele MCP
- Optimizați implementările MCP pentru performanță, securitate și întreținere

## Principiile de bază MCP

Înainte de a intra în practici specifice de implementare, este important să înțelegeți principiile de bază care ghidează dezvoltarea eficientă MCP:

1. **Comunicare standardizată**: MCP folosește JSON-RPC 2.0 ca bază, oferind un format consecvent pentru cereri, răspunsuri și gestionarea erorilor în toate implementările.

2. **Design centrat pe utilizator**: Prioritizați întotdeauna consimțământul, controlul și transparența utilizatorului în implementările MCP.

3. **Securitate pe primul loc**: Implementați măsuri robuste de securitate, inclusiv autentificare, autorizare, validare și limitarea ratei.

4. **Arhitectură modulară**: Proiectați serverele MCP cu o abordare modulară, în care fiecare instrument și resursă are un scop clar și concentrat.

5. **Stare explicită**: MCP `2026-07-28` este fără stare la nivelul protocolului
   . Când un flux de lucru necesită stare între apeluri, folosiți mânere explicite sau
   argumente normale ale instrumentelor susținute de starea durabilă a aplicației.

## Cele mai bune practici oficiale MCP

Următoarele cele mai bune practici sunt derivate din documentația oficială a Model Context Protocol:

### Cele mai bune practici de securitate

1. **Consimțământul și controlul utilizatorului**: Solicitați întotdeauna consimțământ explicit al utilizatorului înainte de a accesa datele sau a efectua operațiuni. Oferiți un control clar asupra datelor partajate și acțiunilor autorizate.

2. **Confidențialitatea datelor**: Expuneți datele utilizatorului doar cu consimțământ explicit și protejați-le cu controale de acces adecvate. Protejați-vă împotriva transmiterii neautorizate a datelor.

3. **Siguranța instrumentelor**: Solicitați consimțământ explicit al utilizatorului înainte de a invoca orice instrument. Asigurați-vă că utilizatorii înțeleg funcționalitatea fiecărui instrument și aplicați limite robuste de securitate.

4. **Controlul permisiunilor instrumentelor**: Configurați ce instrumente poate folosi un model pentru
   fiecare cerere și context de autorizare, asigurând acces doar instrumentelor
   autorizate explicit.

5. **Autentificare**: Solicitați autentificare corespunzătoare înainte de a acorda acces la instrumente, resurse sau operațiuni sensibile folosind chei API, token-uri OAuth sau alte metode sigure de autentificare.

6. **Validarea parametrilor**: Aplicați validarea pentru toate invocările instrumentelor pentru a preveni date de intrare incorecte sau malițioase ce ajung la implementările instrumentelor.

7. **Limitarea ratei**: Implementați limitarea ratei pentru a preveni abuzul și a asigura o utilizare corectă a resurselor serverului.

### Cele mai bune practici de implementare

1. **Negocierea capacităților**: Negociați versiunile de protocol acceptate și
   capacitățile. În MCP `2026-07-28`, fiecare cerere este autonomă și poate
   folosi `server/discover`; reviziile mai vechi folosesc handshake-ul de inițializare.


2. **Proiectarea uneltelor**: Creează unelte specializate care fac bine un singur lucru, mai degrabă decât unelte monolitice care gestionează multiple preocupări.

3. **Gestionarea erorilor**: Implementează mesaje și coduri de eroare standardizate pentru a ajuta la diagnosticarea problemelor, a gestiona eșecurile cu grație și a oferi feedback acționabil.

4. **Observabilitate**: Folosește `stderr` pentru diagnosticul stdio și OpenTelemetry
   pentru observabilitate structurată. Funcția de logare MCP este învechită în
   specificația `2026-07-28`.

5. **Urmărirea progresului**: Pentru operațiuni de durată lungă, raportează actualizări de progres pentru a permite interfețe de utilizator responsivă.

6. **Anularea cererilor**: Permite clienților să anuleze cererile aflate în zbor care nu mai sunt necesare sau care durează prea mult.

## Referințe suplimentare

Pentru cele mai actualizate informații despre cele mai bune practici MCP, consultă:

- [Documentația MCP](https://modelcontextprotocol.io/)
- [Specificația MCP (2026-07-28)][mcp-2026-spec]
- [Specificația anterioară MCP (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Extensia sarcinilor MCP][mcp-tasks-extension]
- [Repository GitHub](https://github.com/modelcontextprotocol)
- [Cele mai bune practici de securitate](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Riscuri de securitate și măsuri de atenuare
- [Atelierul MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Instruire practică în securitate

### Lecția însoțitoare despre fiabilitate

Buclalele generice de reîncercare sunt nesigure pentru unelte care creează bilete, plăți,
mesaje, implementări sau alte efecte în lumea reală. Un răspuns poate fi pierdut
după ce efectul s-a confirmat.

Folosește lecția însoțitoare despre fiabilitate,
[Reîncercări sigure pentru uneltele MCP: un model companion de fiabilitate][reliability-sidecar],
pentru a învăța despre chei de operare stabile, admitere duplicată, checkpointing,
reconciliere, niveluri de dovezi și injectare de eșecuri.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Exemple practice de implementare

### Cele mai bune practici de proiectare a uneltelor

#### 1. Principiul responsabilității unice

Fiecare unealtă MCP ar trebui să aibă un scop clar și concentrat. În loc să creezi unelte monolitice care încearcă să gestioneze mai multe preocupări, dezvoltă unelte specializate care excelează la sarcini specifice.

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

#### 2. Gestionarea consecventă a erorilor

Implementează o gestionare robustă a erorilor cu mesaje informative și mecanisme de recuperare adecvate.

```python
# Exemplu Python cu gestionarea completă a erorilor
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Validarea parametrilor
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Validarea securității
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operațiune pe baza de date cu timeout
                async with timeout(10):  # Timeout de 10 secunde
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Erorile de conexiune pot fi tranzitorii
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Erorile de interogare sunt probabil erori de client
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Permite trecerea erorilor specifice instrumentului
            raise
        except Exception as e:
            # Prindere generală pentru erori neașteptate
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementarea detecției injecției SQL
        pass
        
    def _log_error(self, message, error):
        # Implementarea logării erorilor
        pass
```

#### 3. Validarea parametrilor

Validă întotdeauna parametrii temeinic pentru a preveni intrări eronate sau malițioase.

```javascript
// Exemplu JavaScript/TypeScript cu validare detaliată a parametrilor
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
    // 1. Validarea prezenței parametrului
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Validarea tipurilor parametrilor
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Validarea valorilor parametrilor
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Validarea prezenței conținutului pentru operațiunea de scriere
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Validarea siguranței căii
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementare bazată pe parametri validați
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementarea verificării siguranței căii
    // ...
  }
}
```

### Exemple de implementare în securitate

#### 1. Autentificare și autorizare

```java
// Exemplu Java cu autentificare și autorizare
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Injecția dependențelor
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
        // 1. Extrage contextul de autentificare
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autentifică utilizatorul
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Verifică autorizarea pentru operația specifică
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Continuă cu operația autorizată
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

#### 2. Limitarea ratei

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

## Cele mai bune practici de testare

### 1. Testarea uneltelor MCP la nivel de unitate

Testează întotdeauna uneltele izolat, simulând dependențele externe:

```typescript
// Exemplu TypeScript de test unitar pentru un instrument
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Creează un serviciu de vreme mock
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Creează instrumentul cu dependența mock
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Pregătește
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Acționează
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Afirmă
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Pregătește
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Acționează și afirmă
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Testarea integrării

Testează fluxul complet de la cererile clientului până la răspunsurile serverului:

```python
# Exemplu de test de integrare Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Pornirea unui server de test
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Crearea unui client
        client = McpClient("http://localhost:5000")
        
        # Testarea descoperirii uneltelor
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Testarea execuției uneltelor
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verificarea răspunsului
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Curățare
        await server.stop()
```

## Optimizarea performanței


### 1. Strategii de caching

Implementați caching adecvat pentru a reduce latența și utilizarea resurselor:


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

#### 2. Injecția Dependențelor și Testabilitatea

Proiectați instrumente pentru a primi dependențele prin injecție în constructor, făcându-le testabile și configurabile:

```java
// Exemplu Java cu injecție de dependență
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Dependențe injectate prin constructor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementare a uneltei
    // ...
}
```

#### 3. Instrumente Compozabile

Proiectați instrumente care pot fi compuse împreună pentru a crea fluxuri de lucru mai complexe:

```python
# Exemplu Python care arată instrumente compozabile
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementare...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Acest instrument poate folosi rezultatele din instrumentul dataFetch
    async def execute_async(self, request):
        # Implementare...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Acest instrument poate folosi rezultatele din instrumentul dataAnalysis
    async def execute_async(self, request):
        # Implementare...
        pass

# Aceste instrumente pot fi utilizate independent sau ca parte a unui flux de lucru
```

### Cele Mai Bune Practici pentru Proiectarea Schemelor

Schema este contractul dintre model și instrumentul dumneavoastră. Schemele bine proiectate conduc la o utilizare mai bună a instrumentului.

#### 1. Descrieri Clare ale Parametrilor

Întotdeauna includeți informații descriptive pentru fiecare parametru:

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

#### 2. Constrângeri de Validare

Includeți constrângeri de validare pentru a preveni introducerea de date invalide:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Proprietate de email cu validare de format
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Proprietate de vârstă cu constrângeri numerice
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Proprietate enumerată
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

#### 3. Structuri Consistente ale Răspunsurilor

Mențineți consistența în structurile răspunsurilor pentru a facilita interpretarea rezultatelor de către modele:

```python
async def execute_async(self, request):
    try:
        # Procesează cererea
        results = await self._search_database(request.parameters["query"])
        
        # Întotdeauna returnează o structură consecventă
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

### Gestionarea Erorilor

Gestionarea robustă a erorilor este crucială pentru instrumentele MCP pentru a menține fiabilitatea.

#### 1. Gestionarea Grațioasă a Erorilor

Gestionează erorile la niveluri adecvate și oferă mesaje informative:

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

#### 2. Răspunsuri Structurate la Erori

Furnizează informații structurate despre erori, dacă este posibil:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementare
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
        
        // Aruncă din nou alte excepții ca ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logica de Reîncercare

Folosește logica generică de reîncercare doar pentru apeluri sau operații doar în citire
al căror contract descendent este deja idempotent. Pentru operații efective, un timeout
după trimiterea cererii este ambiguu. Reconcilierea stării autoritare și
reutilizarea aceleiași chei stabile a operației înainte de executarea din nou. Vezi
[lecția companion despre sidecar-ul de fiabilitate](./reliability-sidecars/README.md).

Bucla limitată de reîncercare următoare este potrivită pentru o căutare doar în citire:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # secunde
    
    while retry_count < max_retries:
        try:
            # Apelare către un API extern numai pentru citire
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Reîncercare exponențială
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Eroare non-tranzitorie, nu reîncerca
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Optimizarea Performanței

#### 1. Caching

Implementați caching pentru operații costisitoare:

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

#### 2. Procesare Asincronă

Folosiți modele de programare asincronă pentru operații legate de I/O:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Pentru operațiuni de lungă durată, returnați imediat un ID de procesare
        String processId = UUID.randomUUID().toString();
        
        // Porniți procesarea asincronă
        CompletableFuture.runAsync(() -> {
            try {
                // Efectuați operațiunea de lungă durată
                documentService.processDocument(documentId);
                
                // Actualizați starea (de obicei ar fi stocată într-o bază de date)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Returnați răspuns imediat cu ID-ul procesului
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Unealtă complementară de verificare a stării
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

#### 3. Limitarea Resurselor

Implementați limitarea resurselor pentru a preveni supraîncărcarea:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Permite 5 cereri pe secundă
            bucket_size=10        # Permite rafale de până la 10 cereri
        )
    
    async def execute_async(self, request):
        # Verifică dacă putem continua sau trebuie să așteptăm
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Dacă așteptarea este prea lungă
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Așteaptă timpul de întârziere adecvat
                await asyncio.sleep(delay)
        
        # Consumă un token și continuă cu cererea
        self.rate_limiter.consume()
        
        # Apelează API-ul
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
            
            # Calculează timpul până când următorul token este disponibil
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Adaugă token-uri noi pe baza timpului trecut
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Cele Mai Bune Practici de Securitate

#### 1. Validarea Input-ului

Întotdeauna validați minuțios parametrii de intrare:

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

#### 2. Verificări de Autorizare

Implementați verificările corespunzătoare de autorizare:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Obține contextul utilizatorului din cerere
    UserContext user = request.getContext().getUserContext();
    
    // Verifică dacă utilizatorul are permisiunile necesare
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Pentru resurse specifice, verifică accesul la acea resursă
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Continuă cu executarea uneltei
    // ...
}
```

#### 3. Gestionarea Datelor Sensibile

Manevrați cu grijă datele sensibile:

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
        
        # Obține datele utilizatorului
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtrează câmpurile sensibile decât dacă sunt solicitate explicit ȘI autorizate
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Verifică nivelul de autorizare în contextul cererii
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Creează o copie pentru a evita modificarea originalului
        redacted = user_data.copy()
        
        # Cenzurează câmpurile sensibile specifice
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Cenzurează datele sensibile imbricate
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Cele Mai Bune Practici de Testare pentru Instrumentele MCP

Testarea cuprinzătoare asigură că instrumentele MCP funcționează corect, gestionează cazuri limită și se integrează corect cu restul sistemului.

### Testarea Unităților

#### 1. Testează Fiecare Instrument în Izolare

Creează teste focalizate pe funcționalitatea fiecărui instrument:

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

#### 2. Testarea Validării Schemei

Testează dacă schemele sunt valide și impun corect constrângerile:

```java
@Test
public void testSchemaValidation() {
    // Creați o instanță a instrumentului
    SearchTool searchTool = new SearchTool();
    
    // Obțineți schema
    Object schema = searchTool.getSchema();
    
    // Convertiți schema în JSON pentru validare
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Validați că schema este un JSONSchema valid
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Testați parametrii valizi
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Testați parametru obligatoriu lipsă
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Testați tipul de parametru nevalid
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Teste pentru Gestionarea Erorilor

Creează teste specifice pentru condițiile de eroare:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Aranjează
    tool = ApiTool(timeout=0.1)  # Timeout foarte scurt
    
    # Simulează o cerere care va expira
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Mai lung decât timeout-ul
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Execută și verifică
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verifică mesajul excepției
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Aranjează
    tool = ApiTool()
    
    # Simulează un răspuns cu limită de rată
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
        
        # Execută și verifică
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verifică dacă excepția conține informații despre limita de rată
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Testarea Integrării

#### 1. Testarea Lanțului de Instrumente

Testează instrumentele care lucrează împreună în combinațiile așteptate:

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

#### 2. Testarea Serverului MCP

Testează serverul MCP cu înregistrarea completă și execuția instrumentelor:

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
        // Testați punctul final de descoperire
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Creați o solicitare de instrument
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Trimiteți solicitarea și verificați răspunsul
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Creați o solicitare de instrument nevalidă
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Lipsă parametrul "b"
        request.put("parameters", parameters);
        
        // Trimiteți solicitarea și verificați răspunsul de eroare
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Testarea End-to-End

Testează fluxuri de lucru complete de la solicitarea modelului până la execuția instrumentului:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Aranjează - Configurează clientul MCP și modelul simulare
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Simulează răspunsurile modelului
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
    
    # Simulează răspunsul uneltei meteo
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
        
        # Acționează
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Afirmă
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Testarea Performanței

#### 1. Testarea Încărcării

Testează câte cereri concurente poate gestiona serverul MCP:

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

#### 2. Testarea de Stres

Testează sistemul sub încărcare extremă:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Configurați JMeter pentru testarea de stres
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Configurați planul de testare JMeter
    HashTree testPlanTree = new HashTree();
    
    // Creați planul de testare, grupul de thread-uri, sampler-ele, etc.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Adăugați sampler HTTP pentru execuția instrumentului
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Adăugați ascultători
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Rulați testul
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Validați rezultatele
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Timp mediu de răspuns < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // Percentila 90 < 500ms
}
```

#### 3. Monitorizare și Profilare

Configurează monitorizarea pentru analiza performanței pe termen lung:

```python
# Configurați monitorizarea pentru un server MCP
def configure_monitoring(server):
    # Configurați metrici Prometheus
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
    
    # Adăugați middleware pentru temporizare și înregistrarea metricilor
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Expuneți endpoint-ul pentru metrici
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Modele de Proiectare a Fluxurilor de Lucru MCP

Fluxurile de lucru MCP bine proiectate îmbunătățesc eficiența, fiabilitatea și mentenabilitatea. Iată modele cheie de urmat:

### 1. Modelul Lanțului de Instrumente

Conectează mai multe instrumente într-o succesiune în care ieșirea fiecărui instrument devine intrarea pentru următorul:

```python
# Implementare Python a lanțului de instrumente
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Listă de nume de instrumente pentru a fi executate în secvență
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Execută fiecare instrument din lanț, trecând rezultatul anterior
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Stochează rezultatul și îl folosește ca intrare pentru următorul instrument
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Exemplu de utilizare
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

### 2. Modelul Dispatcher-ului

Folosește un instrument central care direcționează către instrumente specializate în funcție de intrare:

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

### 3. Modelul Procesării Paralele

Execută mai multe instrumente simultan pentru eficiență:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Pasul 1: Preluarea metadatelor setului de date (sincron)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Pasul 2: Lansarea mai multor analize în paralel
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
        
        // Așteaptă finalizarea tuturor sarcinilor paralele
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Așteaptă finalizarea
        
        // Pasul 3: Combinarea rezultatelor
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Pasul 4: Generarea raportului sumar
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Returnează rezultat complet al fluxului de lucru
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Modelul Recuperării în Caz de Eroare

Implementează reveniri grațioase pentru eșecurile instrumentelor:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Încearcă mai întâi unealta principală
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Înregistrează eșecul
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Recurge la unealta secundară
            try:
                # Poate fi nevoie să transformi parametrii pentru unealta de rezervă
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Ambele unelte au eșuat
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Această implementare ar depinde de uneltele specifice
        # Pentru acest exemplu, vom returna pur și simplu parametrii originali
        return params

# Exemplu de utilizare
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API meteo principal (plătit)
        "basicWeatherService",    # API meteo de rezervă (gratuit)
        {"location": location}
    )
```

### 5. Modelul Compoziției Fluxurilor de Lucru

Construiește fluxuri de lucru complexe prin compunerea celor mai simple:

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

# Testarea Serverelor MCP: Cele Mai Bune Practici și Sfaturi de Top

## Prezentare Generală

Testarea este un aspect critic în dezvoltarea serverelor MCP fiabile și de înaltă calitate. Acest ghid oferă cele mai bune practici și sfaturi cuprinzătoare pentru testarea serverelor MCP pe întreg ciclul de viață al dezvoltării, de la teste unitare la teste de integrare și validare end-to-end.

## De ce este Importantă Testarea pentru Serverele MCP

Serverele MCP servesc ca middleware crucial între modelele AI și aplicațiile client. Testarea riguroasă asigură:

- Fiabilitate în mediile de producție
- Gestionarea corectă a cererilor și răspunsurilor
- Implementarea corespunzătoare a specificațiilor MCP
- Reziliență în fața defecțiunilor și a situațiilor-limită
- Performanță constantă sub diferite încărcări

## Testarea Unitară pentru Serverele MCP

### Testarea Unitară (Fundament)

Testele unitare verifică componente individuale ale serverului MCP în izolare.

#### Ce să Testezi

1. **Handleri de Resurse**: Testează logica fiecărui handler de resurse independent
2. **Implementări ale Instrumentelor**: Verifică comportamentul instrumentelor cu intrări diverse
3. **Șabloane de Prompturi**: Asigură că șabloanele de prompt sunt randate corect
4. **Validarea Schemei**: Testează logica de validare a parametrilor
5. **Gestionarea Erorilor**: Verifică răspunsurile la erori pentru intrări invalide

#### Cele Mai Bune Practici pentru Testarea Unitară

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
# Exemplu de test unitar pentru un instrument de calculator în Python
def test_calculator_tool_add():
    # Aranjează
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Acționează
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Asigură
    assert result["value"] == 12
```

### Testarea Integrării (Nivelul Intermediar)

Testele de integrare verifică interacțiunile dintre componentele serverului MCP.

#### Ce să Testezi

1. **Inițializarea Serverului**: Testează pornirea serverului cu diverse configurații
2. **Înregistrarea Rutelor**: Verifică dacă toate endpoint-urile sunt corect înregistrate
3. **Procesarea Cererilor**: Testează ciclul complet cerere-răspuns
4. **Propagarea Erorilor**: Asigură-te că erorile sunt gestionate corect între componente
5. **Autentificare & Autorizare**: Testează mecanismele de securitate

#### Cele Mai Bune Practici pentru Testarea Integrării

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

### Testarea End-to-End (Nivelul Superior)

Testele end-to-end verifică comportamentul complet al sistemului de la client la server.

#### Ce să Testezi

1. **Comunicarea Client-Server**: Testează ciclurile complete cerere-răspuns
2. **SDK-uri Reale pentru Clienți**: Testează cu implementări reale ale clienților
3. **Performanța Sub Încărcare**: Verifică comportamentul cu multiple cereri concurente
4. **Recuperarea după Eroare**: Testează recuperarea sistemului după defecțiuni

5. **Operațiuni de Durată Lungă**: Verificați gestionarea fluxurilor și operațiunilor de durată lungă

#### Cele mai bune practici pentru testarea E2E

```typescript
// Exemplu de test E2E cu un client în TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Pornește serverul în mediul de testare
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Acțiune
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Afirmare
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Strategii de Mocking pentru testarea MCP

Mocking-ul este esențial pentru izolarea componentelor în timpul testării.

### Componente de făcut mock

1. **Modele AI externe**: Mock pentru răspunsurile modelelor pentru testare predictibilă
2. **Servicii externe**: Mock pentru dependențe API (baze de date, servicii terțe)
3. **Servicii de autentificare**: Mock pentru furnizorii de identitate
4. **Furnizori de resurse**: Mock pentru gestiunile resurselor costisitoare

### Exemplu: Mock pentru un răspuns de model AI

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
# Exemplu Python cu unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Configurează mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Folosește mock în test
    server = McpServer(model_client=mock_model)
    # Continuă cu testul
```

## Testarea performanței

Testarea performanței este crucială pentru serverele MCP de producție.

### Ce trebuie măsurat

1. **Latentă**: Timpul de răspuns pentru cereri
2. **Debitul**: Cereri procesate pe secundă
3. **Utilizarea resurselor**: CPU, memorie, utilizare rețea
4. **Gestionarea concurenței**: Comportamentul sub cereri paralele
5. **Caracteristici de scalare**: Performanța pe măsură ce crește încărcarea

### Unelte pentru testarea performanței

- **k6**: Unealtă open-source pentru testare încărcare
- **JMeter**: Testare completă de performanță
- **Locust**: Testare încărcare bazată pe Python
- **Azure Load Testing**: Testare performanță în cloud

### Exemplu: Testare de încărcare simplă cu k6

```javascript
// Script k6 pentru testarea încărcării serverului MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 utilizatori virtuali
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

## Automatizarea testelor pentru serverele MCP

Automatizarea testelor asigură calitate constantă și cicluri de feedback mai rapide.

### Integrare CI/CD

1. **Rulează teste unitare la pull requests**: Asigură-te că modificările codului nu distrug funcționalități existente
2. **Teste de integrare în staging**: Rulează testele de integrare în medii preproducție
3. **Baze de referință de performanță**: Menține reperele de performanță pentru a detecta regresiile
4. **Scanări de securitate**: Automatizează testarea securității ca parte a pipeline-ului

### Exemplu pipeline CI (GitHub Actions)

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

## Testarea conformității cu specificația MCP

Verifică dacă serverul tău implementează corect specificația MCP.

### Domenii-cheie de conformitate

1. **Puncte finale API**: Testează punctele finale cerute (/resources, /tools, etc.)
2. **Format cerere/răspuns**: Validează conformitatea cu schema
3. **Coduri de eroare**: Verifică codurile de stare corecte pentru diferite scenarii
4. **Tipuri de conținut**: Testează gestionarea diferitelor tipuri de conținut
5. **Flux de autentificare**: Verifică mecanismele de autentificare conforme cu specificația

### Suita de testare a conformității

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

## Top 10 sfaturi pentru testarea eficientă a serverului MCP

1. **Testează definițiile instrumentelor separat**: Verifică definițiile schemei independent de logica instrumentului
2. **Folosește teste parametrizate**: Testează instrumentele cu diverse inputuri, inclusiv cazurile limită
3. **Verifică răspunsurile de eroare**: Asigură o gestionare corectă a erorilor pentru toate condițiile posibile
4. **Testează logica de autorizare**: Asigură control corect al accesului pentru diferite roluri de utilizator
5. **Monitorizează acoperirea testelor**: Țintește o acoperire mare a codului din calea critică
6. **Testează răspunsurile în streaming**: Verifică gestionarea corectă a conținutului în flux
7. **Simulează probleme de rețea**: Testează comportamentul în condiții de rețea slabă
8. **Testează limitele de resurse**: Verifică comportamentul la atingererea cotelor sau limitelor de rată
9. **Automatizează testele de regresie**: Construiește o suită ce rulează la fiecare modificare de cod
10. **Documentează cazurile de test**: Menține documentație clară a scenariilor de testare

## Capcane comune la testare

- **Supradependența pe testele pozitive**: Asigură-te că testezi temeinic cazurile de eroare
- **Ignorarea testării performanței**: Identifică blocajele înainte să afecteze producția
- **Testarea doar în izolare**: Combină teste unitare, de integrare și E2E
- **Acoperire incompletă a API-ului**: Asigură testarea tuturor punctelor finale și funcționalităților
- **Medii de testare inconsistente**: Folosește containere pentru medii consistente de testare

## Concluzie

O strategie completă de testare este esențială pentru dezvoltarea unor servere MCP fiabile și de înaltă calitate. Prin implementarea celor mai bune practici și sfaturi detaliate în acest ghid, poți asigura ca implementările MCP să îndeplinească cele mai înalte standarde de calitate, fiabilitate și performanță.


## Puncte cheie de reținut

1. **Proiectarea instrumentelor**: Urmează principiul responsabilității unice, folosește injecția de dependență și proiectează pentru compozabilitate
2. **Proiectarea schemelor**: Creează scheme clare, bine documentate, cu constrângeri adecvate de validare
3. **Gestionarea erorilor**: Implementează gestionare elegantă a erorilor, răspunsuri structurate de eroare și logică de retry conștientă de rezultat

4. **Performanță**: Folosește caching, procesare asincronă și limitarea resurselor
5. **Securitate**: Aplică validarea temeinică a inputurilor, verificări de autorizare și gestionarea datelor sensibile
6. **Testare**: Creează teste cuprinzătoare unitare, de integrare și end-to-end
7. **Modele de workflow**: Aplică modele consacrate precum lanțuri, dispatcheri și procesare paralelă

## Exercițiu

Proiectează un instrument MCP și un workflow pentru un sistem de procesare documente care:

1. Acceptă documente în formate multiple (PDF, DOCX, TXT)
2. Extrage text și informații cheie din documente
3. Clasifică documentele după tip și conținut
4. Generează un rezumat pentru fiecare document

Implementează schemele instrumentului, gestionarea erorilor și un model de workflow care se potrivește cel mai bine acestui scenariu. Gândește-te cum ai testa această implementare.

## Resurse

1. Alătură-te comunității MCP pe [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) pentru a rămâne la curent cu cele mai noi dezvoltări 
2. Contribuie la proiecte open-source [MCP](https://github.com/modelcontextprotocol)
3. Aplică principiile MCP în inițiativele AI din propria organizație
4. Explorează implementări MCP specializate pentru industria ta.
5. Ia în considerare cursuri avansate pe subiecte MCP specifice, cum ar fi integrarea multimodală sau integrarea aplicațiilor enterprise.
6. Experimentează construindu-ți propriile instrumente și workflow-uri MCP folosind principiile învățate prin [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Ce urmează

Următorul: [Studii de caz](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
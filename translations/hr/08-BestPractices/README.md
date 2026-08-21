# Najbolje prakse razvoja MCP-a

[![Najbolje prakse razvoja MCP-a](../../../translated_images/hr/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Kliknite na gornju sliku za pregled video lekcije)_

## Pregled

Ova lekcija fokusira se na napredne najbolje prakse za razvoj, testiranje i implementaciju MCP servera i značajki u produkcijskim okruženjima. Kako ekosistemi MCP-a rastu u složenosti i važnosti, praćenje utvrđenih obrazaca osigurava pouzdanost, održivost i interoperabilnost. Ova lekcija objedinjavanja praktične mudrosti stečene iz stvarnih MCP implementacija za vođenje u kreiranju robusnih, učinkovitih servera s učinkovitim resursima, promptovima i alatima.

## Ciljevi učenja

Do kraja ove lekcije, moći ćete:

- Primijeniti industrijske najbolje prakse u dizajnu MCP servera i značajki
- Kreirati sveobuhvatne strategije testiranja za MCP servere
- Dizajnirati učinkovite, višekratno upotrebljive obrasce tijeka rada za složene MCP aplikacije
- Implementirati pravilno rukovanje greškama, bilježenje i promatranje u MCP serverima
- Optimizirati MCP implementacije za performanse, sigurnost i održivost

## Osnovni principi MCP-a

Prije ulaska u specifične prakse implementacije, važno je razumjeti osnovne principe koji vode učinkoviti razvoj MCP-a:

1. **Standardizirana komunikacija**: MCP koristi JSON-RPC 2.0 kao svoju osnovu, pružajući konzistentan format za zahtjeve, odgovore i rukovanje greškama u svim implementacijama.

2. **Korisnički usmjeren dizajn**: Uvijek dajte prioritet pristanku korisnika, kontroli i transparentnosti u vašim MCP implementacijama.

3. **Sigurnost na prvom mjestu**: Implementirajte snažne sigurnosne mjere uključujući autentikaciju, autorizaciju, validaciju i ograničenje brzine.

4. **Modularna arhitektura**: Dizajnirajte vaše MCP servere modularnim pristupom, gdje svaki alat i resurs ima jasnu, fokusiranu svrhu.

5. **Jasan stanje**: MCP `2026-07-28` je bezstanični na protokolnom
   sloju. Kada tijek rada treba stanje preko poziva, koristite eksplicitne rukohvate ili
   obične argumente alata podržane trajnim stanjem aplikacije.

## Službene najbolje prakse MCP-a

Sljedeće najbolje prakse izvedene su iz službene Model Context Protocol dokumentacije:

### Najbolje prakse sigurnosti

1. **Pristanak i kontrola korisnika**: Uvijek zahtijevajte izričit pristanak korisnika prije pristupa podacima ili obavljanja operacija. Osigurajte jasnu kontrolu nad time koji se podaci dijele i koje su radnje ovlaštene.

2. **Privatnost podataka**: Izlažite korisničke podatke samo uz izričit pristanak i štitite ih odgovarajućim kontrolama pristupa. Zaštitite od neovlaštenog prijenosa podataka.

3. **Sigurnost alata**: Zahtijevajte izričit pristanak korisnika prije pozivanja bilo kojeg alata. Osigurajte da korisnici razumiju funkcionalnost svakog alata i provodite snažne sigurnosne granice.

4. **Kontrola pristupa alatima**: Konfigurirajte koje alate model može koristiti za
   svaki zahtjev i autorizacijski kontekst, osiguravajući pristup samo eksplicitno ovlaštenim
   alatima.

5. **Autentikacija**: Zahtijevajte pravilnu autentikaciju prije dopuštanja pristupa alatima, resursima ili osjetljivim operacijama koristeći API ključeve, OAuth tokene ili druge sigurne metode autentikacije.

6. **Validacija parametara**: Provodite validaciju za sva pozivanja alata kako biste spriječili neispravan ili zlonamjeran unos u implementacije alata.

7. **Ograničenje brzine**: Implementirajte ograničenje brzine kako biste spriječili zloupotrebu i osigurali poštenu upotrebu resursa servera.

### Najbolje prakse implementacije

1. **Pregovaranje sposobnosti**: Pregovarajte podržane verzije protokola i
   sposobnosti. U MCP `2026-07-28` svaki zahtjev je samostalan i može koristiti
   `server/discover`; starije revizije koriste početni rukovanje.

2. **Dizajn alata**: Kreirajte fokusirane alate koji rade jednu stvar dobro, umjesto monolitnih alata koji se bave više pitanja.

3. **Rukovanje greškama**: Implementirajte standardizirane poruke i kodove grešaka za pomoć u dijagnosticiranju problema, elegantno rukovanje pogreškama i pružanje korisnih povratnih informacija.

4. **Promatranje**: Koristite `stderr` za stdio dijagnostiku i OpenTelemetry
   za strukturirano promatranje. MCP značajka bilježenja je zastarjela u
   `2026-07-28` specifikaciji.

5. **Praćenje napretka**: Za dugotrajne operacije, izvješćujte o ažuriranjima napretka za omogućavanje responzivnih korisničkih sučelja.

6. **Otkaži zahtjev**: Dopustite klijentima da otkažu zahtjeve u tijeku koji nisu više potrebni ili traju predugo.

## Dodatne reference

Za najnovije informacije o najboljim praksama MCP-a, pogledajte:

- [MCP dokumentacija](https://modelcontextprotocol.io/)
- [MCP specifikacija (2026-07-28)][mcp-2026-spec]
- [Prethodna MCP specifikacija (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP proširenje zadataka][mcp-tasks-extension]
- [GitHub repozitorij](https://github.com/modelcontextprotocol)
- [Najbolje prakse sigurnosti](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Sigurnosni rizici i mjere ublažavanja
- [MCP Security Summit radionica (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktična sigurnosna obuka

### Lekcija pratitelj pouzdanosti

Generički petlje ponavljanja nisu sigurne za alate koji stvaraju ulaznice, plaćanja,
poruke, implementacije ili druge stvarne efekte. Odgovor može biti izgubljen
nakon što se efekt izvrši.

Koristite lekciju pratitelj pouzdanosti,
[Sigurna ponavljanja za MCP alate: obrazac pouzdanosti sidecara][reliability-sidecar],
za učenje o ključevima stabilne operacije, dupliciranju unosa, snimanju,
usklađivanju, razinama dokaza i injektiranju grešaka.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Primjeri praktične implementacije

### Najbolje prakse dizajniranja alata

#### 1. Princip jedne odgovornosti

Svaki MCP alat treba imati jasnu, fokusiranu svrhu. Umjesto stvaranja monolitnih alata koji pokušavaju rješavati više pitanja, razvijajte specijalizirane alate koji izvrsno obavljaju specifične zadatke.

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

#### 2. Dosljedno rukovanje greškama

Implementirajte robusno rukovanje greškama s informativnim porukama o greškama i odgovarajućim mehanizmima oporavka.

```python
# Python primjer s opsežnim rukovanjem pogreškama
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Provjera valjanosti parametara
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Sigurnosna provjera
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operacija baze podataka s ograničenjem vremena
                async with timeout(10):  # Ograničenje vremena od 10 sekundi
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Greške povezivanja mogu biti prolazne
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Greške upita su vjerojatno greške klijenta
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Dozvoli prolaz specifičnih grešaka alata
            raise
        except Exception as e:
            # Hvatač za neočekivane greške
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementacija otkrivanja SQL injekcija
        pass
        
    def _log_error(self, message, error):
        # Implementacija zapisivanja pogrešaka
        pass
```

#### 3. Validacija parametara

Uvijek temeljito validirajte parametre kako biste spriječili neispravan ili zlonamjeran unos.

```javascript
// Primjer JavaScript/TypeScript s detaljnom provjerom parametara
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
    // 1. Provjeri prisutnost parametra
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Provjeri tipove parametara
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Provjeri vrijednosti parametara
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Provjeri prisutnost sadržaja za operaciju zapisa
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Provjera sigurnosti puta
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementacija na temelju provjerenih parametara
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementacija provjere sigurnosti puta
    // ...
  }
}
```

### Primjeri implementacije sigurnosti

#### 1. Autentikacija i autorizacija

```java
// Java primjer s autentifikacijom i autorizacijom
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Ubrizgavanje ovisnosti
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
        // 1. Izvuci kontekst autentifikacije
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autentificiraj korisnika
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Provjeri autorizaciju za određenu operaciju
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Nastavi s autoriziranom operacijom
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

#### 2. Ograničenje brzine

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

## Najbolje prakse testiranja

### 1. Jedinično testiranje MCP alata

Uvijek testirajte svoje alate izolirano, koristeći simulacije vanjskih ovisnosti:

```typescript
// Primjer TypeScript jediničnog testa za alat
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Kreiraj lažnu uslugu vremenske prognoze
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Kreiraj alat s lažnom ovisnošću
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Priprema
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Izvršenje
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Provjera
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Priprema
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Izvršenje i provjera
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integracijsko testiranje

Testirajte kompletan tijek od klijentskih zahtjeva do odgovora servera:

```python
# Primjer integracijskog testa u Pythonu
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Pokreni testni poslužitelj
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Kreiraj klijenta
        client = McpClient("http://localhost:5000")
        
        # Testiraj otkrivanje alata
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Testiraj izvođenje alata
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Provjeri odgovor
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Očisti resurse
        await server.stop()
```

## Optimizacija performansi

### 1. Strategije keširanja

Implementirajte odgovarajuće keširanje za smanjenje latencije i korištenja resursa:

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

#### 2. Injektiranje ovisnosti i testabilnost

Dizajnirajte alate da primaju svoje ovisnosti putem konstruktor injekcije, čineći ih testabilnima i konfigurabilnima:

```java
// Java primjer s injekcijom ovisnosti
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Ovisnosti ubrizgane kroz konstruktor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementacija alata
    // ...
}
```

#### 3. Kompozabilni alati

Dizajnirajte alate koji se mogu komponirati zajedno za kreiranje složenijih tijekova rada:

```python
# Python primjer koji prikazuje sastavljive alate
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementacija...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Ovaj alat može koristiti rezultate alata dataFetch
    async def execute_async(self, request):
        # Implementacija...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Ovaj alat može koristiti rezultate alata dataAnalysis
    async def execute_async(self, request):
        # Implementacija...
        pass

# Ovi alati mogu se koristiti neovisno ili kao dio radnog tijeka
```

### Najbolje prakse dizajna sheme

Shema je ugovor između modela i vašeg alata. Dobro dizajnirane sheme vode do bolje upotrebljivosti alata.

#### 1. Jasni opisi parametara

Uvijek uključite opisne informacije za svaki parametar:

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

#### 2. Ograničenja validacije

Uključite ograničenja za validaciju kako biste spriječili nevažeće unose:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Svojstvo e-pošte s provjerom formata
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Svojstvo dobi s numeričkim ograničenjima
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Enumerirano svojstvo
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

#### 3. Dosljedne strukture povrataka

Održavajte dosljednost u strukturama odgovora da bi modeli lakše interpretirali rezultate:

```python
async def execute_async(self, request):
    try:
        # Obradi zahtjev
        results = await self._search_database(request.parameters["query"])
        
        # Uvijek vraćaj dosljednu strukturu
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

### Rukovanje greškama

Robusno rukovanje greškama ključno je za MCP alate da održe pouzdanost.

#### 1. Elegatno rukovanje greškama

Rukujte greškama na odgovarajućim razinama i pružajte informativne poruke:

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

#### 2. Strukturirani odgovori o greškama

Vratite strukturirane informacije o greškama kad je moguće:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementacija
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
        
        // Ponovno baci ostale iznimke kao ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logika ponavljanja

Koristite generičku logiku ponavljanja samo za pozive samo za čitanje ili operacije čiji
ugovor downstreama već je idempotentan. Za operacije s efektima, timeout
nakon slanja zahtjeva je dvosmislen. Uskladite autoritativno stanje i
ponovno upotrijebite isti stabilni ključ za operaciju prije ponovnog izvršenja. Pogledajte
[lekciju pratitelj pouzdanosti](./reliability-sidecars/README.md).

Slijedeća ograničena petlja ponavljanja pogodna je za samo čitajući upit:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # sekunde
    
    while retry_count < max_retries:
        try:
            # Pozovi vanjski API samo za čitanje
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Eksponencijalni povratak
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Netransientna pogreška, nemoj ponavljati pokušaj
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Optimizacija performansi

#### 1. Keširanje

Implementirajte keširanje za skupe operacije:

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

#### 2. Asinkrono procesiranje

Koristite obrasce asinkronog programiranja za I/O operacije:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Za dugotrajne operacije, odmah vratite ID obrade
        String processId = UUID.randomUUID().toString();
        
        // Pokreni asinkronu obradu
        CompletableFuture.runAsync(() -> {
            try {
                // Izvrši dugotrajnu operaciju
                documentService.processDocument(documentId);
                
                // Ažuriraj status (obično se pohranjuje u bazu podataka)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Vrati trenutni odgovor s ID-jem procesa
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Alat za provjeru statusa pratitelja
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

#### 3. Ograničenje resursa

Implementirajte ograničenje resursa radi sprječavanja preopterećenja:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Dopušti 5 zahtjeva u sekundi
            bucket_size=10        # Dopušti izboje do 10 zahtjeva
        )
    
    async def execute_async(self, request):
        # Provjeri možemo li nastaviti ili trebamo čekati
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Ako je čekanje predugo
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Pričekaj odgovarajuće vrijeme odgode
                await asyncio.sleep(delay)
        
        # Potroši token i nastavi s zahtjevom
        self.rate_limiter.consume()
        
        # Pozovi API
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
            
            # Izračunaj vrijeme do sljedećeg dostupnog tokena
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Dodaj nove tokene na temelju proteklog vremena
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Najbolje prakse sigurnosti

#### 1. Validacija unosa

Uvijek temeljito validirajte ulazne parametre:

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

#### 2. Provjere autorizacije

Implementirajte pravilne provjere autorizacije:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Dohvati korisnički kontekst iz zahtjeva
    UserContext user = request.getContext().getUserContext();
    
    // Provjeri ima li korisnik potrebne dozvole
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Za određene resurse, provjeri pristup tom resursu
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Nastavi s izvršavanjem alata
    // ...
}
```

#### 3. Rukovanje osjetljivim podacima

Pažljivo rukujte osjetljivim podacima:

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
        
        # Dohvati korisničke podatke
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtriraj osjetljiva polja osim ako nije izričito zatraženo I ovlašteno
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Provjeri razinu autorizacije u kontekstu zahtjeva
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Kreiraj kopiju kako bi se izbjeglo mijenjanje originala
        redacted = user_data.copy()
        
        # Cenzuriraj specifična osjetljiva polja
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Cenzuriraj ugniježđene osjetljive podatke
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Najbolje prakse testiranja MCP alata

Sveobuhvatno testiranje osigurava da MCP alati ispravno funkcioniraju, rješavaju grančne slučajeve i pravilno se integriraju s ostatkom sustava.

### Jedinično testiranje

#### 1. Testirajte svaki alat izolirano

Kreirajte fokusirane testove za funkcionalnost svakog alata:

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

#### 2. Testiranje validacije sheme

Testirajte da su sheme važeće i pravilno provjeravaju ograničenja:

```java
@Test
public void testSchemaValidation() {
    // Kreiraj instancu alata
    SearchTool searchTool = new SearchTool();
    
    // Dohvati shemu
    Object schema = searchTool.getSchema();
    
    // Pretvori shemu u JSON za validaciju
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Validiraj da je shema važeći JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Testiraj važeće parametre
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Testiraj nedostajući obavezni parametar
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Testiraj nevažeći tip parametra
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Testovi rukovanja greškama

Kreirajte specifične testove za uvjete grešaka:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Posloži
    tool = ApiTool(timeout=0.1)  # Vrlo kratki vremenski limit
    
    # Simuliraj zahtjev koji će istek vremena
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Dulje od vremenskog limita
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Izvrši i potvrdi
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Provjeri poruku iznimke
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Posloži
    tool = ApiTool()
    
    # Simuliraj odgovor sa ograničenjem brzine
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
        
        # Izvrši i potvrdi
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Provjeri sadrži li iznimka informacije o ograničenju brzine
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integracijsko testiranje

#### 1. Testiranje lanca alata

Testirajte alate radeći zajedno u očekivanim kombinacijama:

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

#### 2. Testiranje MCP servera

Testirajte MCP server s potpunom registracijom i izvršenjem alata:

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
        // Testiraj odredišnu točku za otkrivanje
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Kreiraj zahtjev za alat
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Pošalji zahtjev i provjeri odgovor
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Kreiraj nevažeći zahtjev za alat
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Nedostaje parametar "b"
        request.put("parameters", parameters);
        
        // Pošalji zahtjev i provjeri odgovor s greškom
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. End-to-end testiranje

Testirajte kompletne tijekove rada od model prompta do izvršenja alata:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Postavi - Postavi MCP klijent i lažni model
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Lažni odgovori modela
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
    
    # Lažni odgovor vremenskog alata
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
        
        # Izvrši
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Potvrdi
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Testiranje performansi

#### 1. Test opterećenja

Testirajte koliko paralelnih zahtjeva vaš MCP server može podnijeti:

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

#### 2. Testiranje opterećenja sustava

Testirajte sustav pod ekstremnim opterećenjem:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Postavite JMeter za stresno testiranje
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigurirajte JMeter plan testa
    HashTree testPlanTree = new HashTree();
    
    // Kreirajte plan testa, thread grupu, uzorkivače, itd.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Dodajte HTTP uzorkivač za izvođenje alata
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Dodajte slušatelje
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Pokrenite test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Provjerite rezultate
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Prosječno vrijeme odziva < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90. percentil < 500ms
}
```

#### 3. Praćenje i profiliranje

Postavite nadzor za dugoročne analize performansi:

```python
# Konfigurirajte nadzor za MCP server
def configure_monitoring(server):
    # Postavite Prometheus metrike
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
    
    # Dodajte middleware za mjerenje vremena i bilježenje metrika
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Izložite endpoint za metrike
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Obrasci dizajna MCP tijekova rada

Dobro dizajnirani MCP tijekovi rada poboljšavaju učinkovitost, pouzdanost i održivost. Evo ključnih obrazaca koje treba slijediti:

### 1. Obrazac lanca alata

Povežite više alata u slijed gdje izlaz jednog alata postaje ulaz za sljedeći:

```python
# Implementacija Python lanca alata
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Popis naziva alata za izvođenje u nizu
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Izvrši svaki alat u lancu, prosljeđujući prethodni rezultat
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Spremi rezultat i koristi ga kao ulaz za sljedeći alat
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Primjer uporabe
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

### 2. Obrazac dispečera

Koristite središnji alat koji šalje pozive specijaliziranim alatima na temelju ulaza:

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

### 3. Obrazac paralelnog procesiranja

Izvršavajte višestruke alate istovremeno za učinkovitost:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Korak 1: Dohvati metapodatke skupa podataka (sinkrono)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Korak 2: Pokreni više analiza paralelno
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
        
        // Pričekaj da se svi paralelni zadaci dovrše
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Pričekaj dovršetak
        
        // Korak 3: Kombiniraj rezultate
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Korak 4: Generiraj sažetak izvještaja
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Vrati potpuni rezultat tijeka rada
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Obrazac oporavka od grešaka

Implementirajte elegantne povrate za neuspjehe alata:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Prvo pokušajte s primarnim alatom
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Zabilježite neuspjeh
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Pređite na sekundarni alat
            try:
                # Možda će trebati transformirati parametre za rezervni alat
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Oba alata nisu uspjela
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ova implementacija ovisila bi o specifičnim alatima
        # Za ovaj primjer, samo ćemo vratiti izvornike parametre
        return params

# Primjer korištenja
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Primarni (plaćeni) vremenski API
        "basicWeatherService",    # Rezervni (besplatni) vremenski API
        {"location": location}
    )
```

### 5. Obrazac kompozicije tijeka rada

Gradite složene tijekove rada komponiranjem jednostavnijih:

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

# Testiranje MCP servera: Najbolje prakse i savjeti

## Pregled

Testiranje je ključan aspekt razvoja pouzdanih, visokokvalitetnih MCP servera. Ovaj vodič pruža sveobuhvatne najbolje prakse i savjete za testiranje vaših MCP servera tijekom cijelog razvojnog ciklusa, od jediničnih testova do integracijskih testova i end-to-end validacije.

## Zašto je testiranje važno za MCP servere

MCP serveri služe kao ključni middleware između AI modela i klijentskih aplikacija. Temeljito testiranje osigurava:

- Pouzdanost u produkcijskim okruženjima
- Točno rukovanje zahtjevima i odgovorima
- Pravilnu implementaciju MCP specifikacija
- Otpornost na kvarove i rubne slučajeve
- Dosljedne performanse pod različitim opterećenjima

## Jedinično testiranje za MCP servere

### Jedinično testiranje (temelj)

Jedinični testovi provjeravaju pojedinačne komponente vašeg MCP servera izolirano.

#### Što testirati

1. **Rukovatelji resursima**: Testirajte logiku svakog rukovatelja resursa neovisno
2. **Implementacije alata**: Provjerite ponašanje alata s različitim unosima
3. **Predlošci za prompt**: Osigurajte da se predlošci pravilno prikazuju
4. **Validacija sheme**: Testirajte logiku validacije parametara
5. **Rukovanje greškama**: Provjerite odgovore na greške za nevažeće unose

#### Najbolje prakse za jedinično testiranje

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
# Primjer jediničnog testa za alat kalkulator u Pythonu
def test_calculator_tool_add():
    # Priprema
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Izvršavanje
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Provjera
    assert result["value"] == 12
```

### Integracijsko testiranje (srednji sloj)

Integracijski testovi provjeravaju interakcije između komponenti vašeg MCP servera.

#### Što testirati

1. **Pokretanje servera**: Testirajte pokretanje servera s različitim konfiguracijama
2. **Registracija ruta**: Provjerite jesu li svi krajnji točke pravilno registrirane
3. **Obrada zahtjeva**: Testirajte puni ciklus zahtjev-odgovor
4. **Propagacija grešaka**: Osigurajte pravilno rukovanje greškama među komponentama
5. **Autentikacija i autorizacija**: Testirajte sigurnosne mehanizme

#### Najbolje prakse za integracijsko testiranje

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

### End-to-End testiranje (gornji sloj)

End-to-end testovi provjeravaju kompletno ponašanje sustava od klijenta do servera.

#### Što testirati

1. **Komunikacija klijent-server**: Testirajte kompletne cikluse zahtjev-odgovor
2. **Pravi klijentski SDK-ovi**: Testirajte s stvarnim implementacijama klijenata
3. **Performanse pod opterećenjem**: Provjerite ponašanje kod višestrukih istodobnih zahtjeva
4. **Oporavak od grešaka**: Testirajte oporavak sustava od kvarova

5. **Dugotrajne operacije**: Provjerite rukovanje streamingom i dugotrajnim operacijama

#### Najbolje prakse za E2E testiranje

```typescript
// Primjer E2E testa s klijentom u TypeScriptu
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Pokreni server u testnom okruženju
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Izvrši
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Provjeri
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Strategije mockiranja za MCP testiranje

Mockiranje je ključno za izoliranje komponenti tijekom testiranja.

### Komponente za mockiranje

1. **Vanjski AI modeli**: Mockirajte odgovore modela za predvidljivo testiranje
2. **Vanjske usluge**: Mockirajte API ovisnosti (baze podataka, usluge trećih strana)
3. **Usluge autentifikacije**: Mockirajte pružatelje identiteta
4. **Pružatelji resursa**: Mockirajte skupe upravitelje resursa

### Primjer: Mockiranje odgovora AI modela

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
# Python primjer sa unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Konfiguriraj mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Koristi mock u testu
    server = McpServer(model_client=mock_model)
    # Nastavi s testom
```

## Testiranje performansi

Testiranje performansi je ključno za produkcijske MCP servere.

### Što mjeriti

1. **Latencija**: Vrijeme odziva na zahtjeve
2. **Propusnost**: Broj obrađenih zahtjeva u sekundi
3. **Korištenje resursa**: CPU, memorija, mreža
4. **Rukovanje istovremenim zahtjevima**: Ponašanje pod paralelnim zahtjevima
5. **Karakteristike skaliranja**: Performanse kako se opterećenje povećava

### Alati za testiranje performansi

- **k6**: Open-source alat za testiranje opterećenja
- **JMeter**: Sveobuhvatno testiranje performansi
- **Locust**: Alat za testiranje opterećenja baziran na Pythonu
- **Azure Load Testing**: Cloud-based testiranje performansi

### Primjer: Osnovni test opterećenja s k6

```javascript
// k6 skripta za testiranje opterećenja MCP servera
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtualnih korisnika
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

## Automatizacija testova za MCP servere

Automatizacija testova osigurava dosljednu kvalitetu i brže povratne informacije.

### Integracija CI/CD

1. **Pokretanje unit testova na pull requestovima**: Osigurajte da promjene koda ne kvare postojeću funkcionalnost
2. **Integracijski testovi u stagingu**: Pokrenite integracijske testove u predprodukcijskim okruženjima
3. **Baze za usporedbu performansi**: Održavajte performanse kao mjere za otkrivanje regresija
4. **Sigurnosni skenovi**: Automatizirajte sigurnosna testiranja kao dio pipelinea

### Primjer CI pipelinea (GitHub Actions)

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

## Testiranje u skladu sa MCP specifikacijom

Provjerite da vaš server ispravno implementira MCP specifikaciju.

### Ključna područja usklađenosti

1. **API krajnje točke**: Testirajte potrebne krajnje točke (/resources, /tools, itd.)
2. **Format zahtjeva/odgovora**: Provjerite usklađenost sa shemom
3. **Kodovi pogrešaka**: Provjerite ispravne statusne kodove za različite scenarije
4. **Vrste sadržaja**: Testirajte rukovanje različitim vrstama sadržaja
5. **Tok autentifikacije**: Provjerite spec-kompatibilne mehanizme autentifikacije

### Paket testova za usklađenost

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

## Top 10 savjeta za učinkovito testiranje MCP servera

1. **Testirajte definicije alata zasebno**: Provjerite definicije shema neovisno o logici alata
2. **Koristite parametarske testove**: Testirajte alate s raznovrsnim unosima, uključujući rubne slučajeve
3. **Provjerite odgovore s greškama**: Osigurajte pravilno rukovanje svim mogućim greškama
4. **Testirajte autorizacijsku logiku**: Osigurajte ispravnu kontrolu pristupa za različite korisničke uloge
5. **Pratite pokrivenost testovima**: Ciljajte visoku pokrivenost kritičnog koda
6. **Testirajte streaming odgovore**: Provjerite pravilno rukovanje streaming sadržajem
7. **Simulirajte mrežne probleme**: Testirajte ponašanje u lošim mrežnim uvjetima
8. **Testirajte limite resursa**: Provjerite ponašanje pri dosezanju kvota ili ograničenja brzine
9. **Automatizirajte regresijske testove**: Izgradite paket koji se pokreće pri svakoj promjeni koda
10. **Dokumentirajte testne slučajeve**: Održavajte jasnu dokumentaciju testnih scenarija

## Uobičajene pogreške u testiranju

- **Preveliko oslanjanje na testiranje "happy path"**: Temeljito testirajte slučajeve pogrešaka
- **Ignoriranje testiranja performansi**: Identificirajte uska grla prije produkcije
- **Testiranje samo u izolaciji**: Kombinirajte unit, integracijske i E2E testove
- **Nepotpuna pokrivenost API-ja**: Osigurajte da su testirane sve krajnje točke i značajke
- **Nedosljedna testna okruženja**: Koristite kontejnere za dosljedna okruženja

## Zaključak

Sveobuhvatna strategija testiranja ključna je za razvoj pouzdanih, visokokvalitetnih MCP servera. Primjenom najboljih praksi i savjeta iz ovog vodiča, možete osigurati da vaše MCP implementacije ispunjavaju najviše standarde kvalitete, pouzdanosti i performansi.


## Ključne spoznaje

1. **Dizajn alata**: Slijedite princip jedne odgovornosti, koristite dependency injection i dizajnirajte za kompozabilnost
2. **Dizajn sheme**: Kreirajte jasne, dobro dokumentirane sheme s odgovarajućim validacijskim ograničenjima
3. **Rukovanje pogreškama**: Uvedite graciozno rukovanje pogreškama, strukturirane odgovore s greškom i logiku ponovnog pokušaja ovisno o ishodu
   
4. **Performanse**: Koristite keširanje, asinkrono procesiranje i ograničavanje resursa
5. **Sigurnost**: Primijenite temeljitu validaciju unosa, provjere autorizacije i rukovanje osjetljivim podacima
6. **Testiranje**: Kreirajte sveobuhvatne unit, integracijske i end-to-end testove
7. **Radni obrasci**: Primijenite ustaljene obrasce poput lanaca, dispatcher-a i paralelnog procesiranja

## Vježba

Dizajnirajte MCP alat i radni tijek za sustav obrade dokumenata koji:

1. Prima dokumente u više formata (PDF, DOCX, TXT)
2. Izvlači tekst i ključne informacije iz dokumenata
3. Klasificira dokumente prema tipu i sadržaju
4. Generira sažetak svakog dokumenta

Implementirajte sheme alata, rukovanje pogreškama i radni obrazac koji najbolje odgovara ovom scenariju. Razmotrite kako biste testirali ovu implementaciju.

## Resursi 

1. Pridružite se MCP zajednici na [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) kako biste bili u tijeku s najnovijim događanjima 
2. Doprinesite open-source [MCP projektima](https://github.com/modelcontextprotocol)
3. Primijenite MCP principe u AI inicijativama vaše organizacije
4. Istražite specijalizirane MCP implementacije za vašu industriju. 
5. Razmislite o naprednim tečajevima na specifične MCP teme, poput multi-modalne integracije ili integracije enterprise aplikacija.
6. Eksperimentirajte s izgradnjom vlastitih MCP alata i radnih tijekova koristeći principe naučene kroz [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Što slijedi

Dalje: [Primjeri slučajeva](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
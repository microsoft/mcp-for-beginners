# MCP Fejlesztési Legjobb Gyakorlatok

[![MCP Fejlesztési Legjobb Gyakorlatok](../../../translated_images/hu/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Kattints a fenti képre a lecke videójának megtekintéséhez)_

## Áttekintés

Ez a lecke a fejlett legjobb gyakorlatokra fókuszál az MCP szerverek és funkciók fejlesztése, tesztelése és éles környezetbe történő telepítése során. Ahogy az MCP ökoszisztémák egyre összetettebbé és fontosabbá válnak, a bevált minták követése biztosítja a megbízhatóságot, karbantarthatóságot és interoperabilitást. Ez a lecke a valós MCP megvalósításokból nyert gyakorlati bölcsességet foglalja össze, hogy segítsen robusztus, hatékony szervereket létrehozni hatékony erőforrásokkal, promptokkal és eszközökkel.

## Tanulási célok

A lecke végére képes leszel:

- Az iparági legjobb gyakorlatok alkalmazása MCP szerver- és funkciótervezésben
- Átfogó tesztelési stratégiák kialakítása MCP szerverekhez
- Hatékony, újrahasznosítható munkafolyamat minták tervezése összetett MCP alkalmazásokhoz
- Megfelelő hibakezelés, naplózás és megfigyelhetőség megvalósítása MCP szerverekben
- MCP megvalósítások optimalizálása teljesítmény, biztonság és karbantarthatóság szempontjából

## MCP Alapelvek

Mielőtt a konkrét megvalósítási gyakorlatokba mélyednénk, fontos megérteni azokat az alapelveket, amelyek az eredményes MCP fejlesztést irányítják:

1. **Szabványosított kommunikáció**: Az MCP JSON-RPC 2.0-t használ alapként, egységes formátumot biztosítva a kérésekhez, válaszokhoz és hibakezeléshez minden megvalósításban.

2. **Felhasználó-központú tervezés**: Mindig helyezd előtérbe a felhasználók beleegyezését, kontrollját és átláthatóságát az MCP megvalósításaidban.

3. **Biztonság mindenekelőtt**: Valósíts meg robusztus biztonsági intézkedéseket, beleértve az autentikációt, jogosultságkezelést, validációt és sebességkorlátozást.

4. **Moduláris architektúra**: Tervezd MCP szervereidet moduláris megközelítéssel, ahol minden eszköznek és erőforrásnak világos, fókuszált célja van.

5. **Kifejezett állapot**: Az MCP `2026-07-28` protokollréteg stateless (állapotmentes).
   Amikor egy munkafolyamatnak kereszt-hívás állapotra van szüksége, használj kifejezett fogantyúkat vagy
   hagyományos eszközargumentumokat tartós alkalmazásállapot támogatásával.

## Hivatalos MCP Legjobb Gyakorlatok

A következő legjobb gyakorlatok a hivatalos Model Context Protocol dokumentációból származnak:

### Biztonsági legjobb gyakorlatok

1. **Felhasználói beleegyezés és kontroll**: Mindig kérj kifejezett felhasználói beleegyezést az adatok eléréséhez vagy műveletek végrehajtásához. Adj világos irányítást arról, milyen adatok kerülnek megosztásra és mely műveletek engedélyezettek.

2. **Adatvédelem**: Csak explicit beleegyezéssel tárj fel felhasználói adatokat, és védd ezeket megfelelő hozzáférésvezérléssel. Védelmezd az illetéktelen adatátvitelt.

3. **Eszközbiztonság**: Kérj kifejezett felhasználói beleegyezést bármely eszköz meghívása előtt. Biztosítsd, hogy a felhasználók értsék az eszköz funkcióját, és érvényesíts erős biztonsági korlátokat.

4. **Eszköz jogkezelés**: Állítsd be, mely eszközöket használhat egy modell
   minden egyes kéréshez és jogosultsági kontextushoz, biztosítva, hogy csak kifejezetten engedélyezett
   eszközök legyenek elérhetők.

5. **Hitelesítés**: Kérj megfelelő hitelesítést eszközök, erőforrások vagy érzékeny műveletek eléréséhez API kulcsok, OAuth tokenek vagy egyéb biztonságos hitelesítési módszerek használatával.

6. **Paraméter érvényesítés**: Kötelező érvényesítés minden eszköz meghívásakor, hogy megakadályozd a helytelen vagy rosszindulatú bemenetek eljutását az eszköz implementációkhoz.

7. **Sebességkorlátozás**: Valósíts meg sebességkorlátozást az erőforrások túlterhelésének megelőzésére és a szerver erőforrások igazságos használatának biztosítására.

### Megvalósítási legjobb gyakorlatok

1. **Képesség egyeztetés**: Egyeztess a támogatott protokollverziókról és
   képességekről. Az MCP `2026-07-28` verzióban minden kérés önálló,
   és használhatja a `server/discover`-t; a régebbi változatok az inicializációs kézfogást használják.


2. **Eszköztervezés**: Hozzon létre olyan fókuszált eszközöket, amelyek egy dolgot jól csinálnak, ahelyett, hogy több feladatot kezelő monolitikus eszközök lennének.

3. **Hibakezelés**: Valósítson meg szabványosított hibajelzéseket és kódokat a problémák diagnosztizálásához, a hibák elegáns kezeléséhez és a cselekvésre ösztönző visszajelzések biztosításához.

4. **Megfigyelhetőség**: Használja a `stderr`-t stdio diagnosztikához és az OpenTelemetry-t
   strukturált megfigyelhetőséghez. Az MCP naplózási funkció a
   `2026-07-28` specifikációban elavult.

5. **Előrehaladási nyomon követés**: Hosszú futású műveleteknél jelentse a folyamat előrehaladását az interaktív felhasználói felületek támogatására.

6. **Kérés megszakítása**: Tegye lehetővé az ügyfelek számára, hogy megszakítsák az éppen futó, már nem szükséges vagy túl sokáig tartó kéréseket.

## További hivatkozások

Az MCP legfrissebb legjobb gyakorlataiért lásd:

- [MCP Dokumentáció](https://modelcontextprotocol.io/)
- [MCP Specifikáció (2026-07-28)][mcp-2026-spec]
- [Előző MCP Specifikáció (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Feladatextenzió][mcp-tasks-extension]
- [GitHub Tároló](https://github.com/modelcontextprotocol)
- [Biztonsági legjobb gyakorlatok](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Biztonsági kockázatok és enyhítések
- [MCP Biztonsági Csúcstalálkozó Műhely (Sherpa)](https://azure-samples.github.io/sherpa/) - Gyakorlati biztonsági képzés

### Megbízhatósági Kísérő Lecke

Általános újrapróbálkozó ciklusok nem biztonságosak jegyek, kifizetések,
üzenetek, telepítések vagy más valós hatások létrehozására szolgáló eszközök esetén. A válasz
elveszhet az effektus végrehajtása után.

Használja a megbízhatósági kísérő leckét,
[Biztonságos újrapróbálkozások MCP eszközök számára: egy Megbízhatósági Sidecar minta][reliability-sidecar],
hogy megismerje a stabil működés kulcsait, a duplikált elfogadást, ellenőrzőpont készítést,
összehangolást, bizonyítékszinteket és a hibainjekciót.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Gyakorlati megvalósítási példák

### Eszköztervezési legjobb gyakorlatok

#### 1. Egy felelősségi elv

Minden MCP eszköznek világos, fókuszált céllal kell rendelkeznie. Ahelyett, hogy monolitikus eszközöket készítenénk, amelyek több területet próbálnak kezelni, fejlesszen ki specializált eszközöket, amelyek egy adott feladatot kiválóan végeznek el.

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

#### 2. Következetes hibakezelés

Valósítson meg robusztus hibakezelést informatív hibajelzésekkel és megfelelő helyreállítási mechanizmusokkal.

```python
# Python példa átfogó hiba kezeléssel
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Paraméter ellenőrzés
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Biztonsági ellenőrzés
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Adatbázis művelet időkorláttal
                async with timeout(10):  # 10 másodperces időkorlát
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # A kapcsolat hibái átmenetiek lehetnek
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # A lekérdezés hibái valószínűleg kliens hibák
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Engedjük át az eszközspecifikus hibákat
            raise
        except Exception as e:
            # Mindent elkapó nem várt hibákra
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL injekció felismerés megvalósítása
        pass
        
    def _log_error(self, message, error):
        # Hibanaplózás megvalósítása
        pass
```

#### 3. Paraméter érvényesítés

Mindig alaposan ellenőrizze a paramétereket a helytelen vagy rosszindulatú bemenetek megelőzése érdekében.

```javascript
// JavaScript/TypeScript példa részletes paraméterellenőrzéssel
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
    // 1. A paraméter jelenlétének ellenőrzése
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. A paraméterek típusainak ellenőrzése
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. A paraméterértékek ellenőrzése
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Tartalom meglétének ellenőrzése írási művelethez
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Útvonal biztonságának ellenőrzése
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Megvalósítás a validált paraméterek alapján
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Az útvonal biztonságának ellenőrzésének megvalósítása
    // ...
  }
}
```

### Biztonsági megvalósítási példák

#### 1. Hitelesítés és jogosultságkezelés

```java
// Java példa hitelesítéssel és jogosultságkezeléssel
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Függőség injektálás
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
        // 1. Hitelesítési kontextus kinyerése
        String authToken = request.getContext().getAuthToken();
        
        // 2. Felhasználó hitelesítése
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Jogosultság ellenőrzése a konkrét művelethez
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Folytatás az engedélyezett művelettel
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

#### 2. Korlátozási ráta

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

## Tesztelési legjobb gyakorlatok

### 1. Egységtesztelés MCP eszközöknél

Mindig tesztelje eszközeit elkülönítve, külső függőségek helyettesítésével:

```typescript
// TypeScript példa egy eszköz egységtesztre
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Hozz létre egy hamis időjárás szolgáltatást
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Hozd létre az eszközt a hamis függőséggel
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Előkészítés
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Végrehajtás
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Ellenőrzés
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Előkészítés
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Végrehajtás és ellenőrzés
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integrációs tesztelés

Tesztelje a teljes folyamatot az ügyfél kéréseitől a szerver válaszaiig:

```python
# Python integrációs teszt példa
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Indíts egy teszt szervert
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Hozz létre egy klienset
        client = McpClient("http://localhost:5000")
        
        # Teszteld az eszköz felderítését
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Teszteld az eszköz végrehajtását
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Ellenőrizd a választ
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Takarítsd el
        await server.stop()
```

## Teljesítményoptimalizálás


### 1. Gyorsítótárazási stratégiák

Alkalmazzon megfelelő gyorsítótárazást a késleltetés és az erőforrás-felhasználás csökkentése érdekében:


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

#### 2. Függőség-injektálás és tesztelhetőség

Tervezze az eszközöket úgy, hogy a függőségeiket konstruktor-injektáláson keresztül kapják meg, így tesztelhetővé és konfigurálhatóvá válnak:

```java
// Java példa függőséginjektálással
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // A függőségek konstruktoron keresztül kerülnek beadásra
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Eszköz megvalósítása
    // ...
}
```

#### 3. Összeállítható eszközök

Tervezzen olyan eszközöket, amelyeket össze lehet kapcsolni komplexebb munkafolyamatok létrehozásához:

```python
# Python példa összetételre alkalmas eszközökre
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Megvalósítás...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Ez az eszköz a dataFetch eszköz eredményeit használhatja
    async def execute_async(self, request):
        # Megvalósítás...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Ez az eszköz a dataAnalysis eszköz eredményeit használhatja
    async def execute_async(self, request):
        # Megvalósítás...
        pass

# Ezek az eszközök önállóan vagy munkafolyamat részeként is használhatók
```

### Sématervezés legjobb gyakorlatai

A séma a szerződés a modell és az eszköze között. A jól megtervezett sémák jobb használhatósághoz vezetnek.

#### 1. Világos paraméterleírások

Mindig mellékeljen leíró információkat minden paraméterhez:

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

#### 2. Érvényesítési korlátozások

Tartalmazzon érvényesítési korlátozásokat érvénytelen bemenetek megelőzésére:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Email tulajdonság formátumellenőrzéssel
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Életkor tulajdonság numerikus megszorításokkal
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Felsorolt tulajdonság
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

#### 3. Következetes válaszstruktúrák

Tartsa fenn a következetességet a válaszstruktúrákban, hogy a modellek könnyebben értelmezhessék az eredményeket:

```python
async def execute_async(self, request):
    try:
        # Kérés feldolgozása
        results = await self._search_database(request.parameters["query"])
        
        # Mindig következetes struktúrát adjon vissza
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

### Hibakezelés

A robusztus hibakezelés elengedhetetlen az MCP eszközök megbízhatóságának fenntartásához.

#### 1. Kíméletes hibakezelés

Kezelje a hibákat a megfelelő szinteken, és biztosítson tájékoztató üzeneteket:

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

#### 2. Strukturált hiba-válaszok

Lehetőség szerint adjon vissza strukturált hibainformációt:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Megvalósítás
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
        
        // Más kivételek újradobása ToolExecutionException-ként
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Újrapróbálkozási logika

Általános újrapróbálkozási logikát csak olvasási hívásokhoz vagy olyan műveletekhez használjon, amelyek
downstream szerződése már idempotens. Effektív műveleteknél az időtúllépés a kérés elküldése után kétértelmű.
Egyeztessen hatókörállapotot, és használja ugyanazt a stabil műveleti kulcsot a végrehajtás megismétlése előtt.
Lásd a
[megbízhatósági sidecar társ leckét](./reliability-sidecars/README.md).

A következő korlátos újrapróbálkozási ciklus megfelelő olvasási lekérdezéshez:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # másodpercek
    
    while retry_count < max_retries:
        try:
            # Hívjon meg egy csak olvasható külső API-t
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Exponenciális visszalépés
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Nem átmeneti hiba, ne próbálkozz újra
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Teljesítményoptimalizálás

#### 1. Gyorsítótárazás

Vezessen be gyorsítótárazást költséges műveletekhez:

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

#### 2. Aszinkron feldolgozás

Használjon aszinkron programozási mintákat I/O-kötött műveletekhez:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Hosszú műveletek esetén azonnal térjen vissza egy feldolgozási azonosítóval
        String processId = UUID.randomUUID().toString();
        
        // Az aszinkron feldolgozás elindítása
        CompletableFuture.runAsync(() -> {
            try {
                // Hosszú művelet végrehajtása
                documentService.processDocument(documentId);
                
                // Állapot frissítése (általában adatbázisban tárolva)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Azonnali válasz visszaadása a folyamat azonosítójával
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Kísérő állapotellenőrző eszköz
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

#### 3. Erőforrás-korlátozás

Vezessen be erőforrás-korlátozást a túlterhelés megelőzésére:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Engedélyezzen 5 kérést másodpercenként
            bucket_size=10        # Engedélyezzen akár 10 kérésig terjedő robbanásokat
        )
    
    async def execute_async(self, request):
        # Ellenőrizze, hogy folytathatjuk-e vagy várni kell
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Ha a várakozás túl hosszú
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Várjon a megfelelő késleltetési időt
                await asyncio.sleep(delay)
        
        # Fogyasszon el egy tokent és folytassa a kérdést
        self.rate_limiter.consume()
        
        # Hívja meg az API-t
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
            
            # Számítsa ki az időt a következő token elérhetőségig
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Adjon hozzá új tokeneket az eltelt idő alapján
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Biztonsági legjobb gyakorlatok

#### 1. Bemeneti érvényesítés

Mindig alaposan ellenőrizze a bemeneti paramétereket:

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

#### 2. Jogosultság-ellenőrzések

Vezessen be megfelelő jogosultság-ellenőrzéseket:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Felhasználói kontextus lekérése a kérésből
    UserContext user = request.getContext().getUserContext();
    
    // Ellenőrizze, hogy a felhasználónak megvannak-e a szükséges engedélyei
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Egyes erőforrások esetén ellenőrizze az adott erőforráshoz való hozzáférést
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Folytassa az eszköz végrehajtását
    // ...
}
```

#### 3. Érzékeny adatok kezelése

Kezelje az érzékeny adatokat gondosan:

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
        
        # Felhasználói adatok lekérése
        user_data = await self.user_service.get_user_data(user_id)
        
        # Érzékeny mezők szűrése, kivéve ha kifejezetten kérték ÉS engedélyezték
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Jogosultsági szint ellenőrzése a kérés kontextusában
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Másolat készítése az eredeti módosításának elkerülése érdekében
        redacted = user_data.copy()
        
        # Konkrét érzékeny mezők eltakarása
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Beágyazott érzékeny adatok eltakarása
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP eszközök tesztelésének legjobb gyakorlatai

Átfogó tesztelés biztosítja, hogy az MCP eszközök helyesen működnek, kezelik a szélsőséges eseteket, és megfelelően integrálódnak a rendszer többi részével.

### Egységtesztelés

#### 1. Minden eszköz tesztelése izoláltan

Készítsen célzott teszteket minden eszköz funkciójára:

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

#### 2. Séma érvényesítési tesztek

Tesztelje, hogy a sémák érvényesek és megfelelően érvényesítik a korlátozásokat:

```java
@Test
public void testSchemaValidation() {
    // Eszköz példány létrehozása
    SearchTool searchTool = new SearchTool();
    
    // Séma lekérése
    Object schema = searchTool.getSchema();
    
    // Séma JSON formátumba konvertálása érvényesítéshez
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // A séma validálása, hogy érvényes JSONSchema-e
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Érvényes paraméterek tesztelése
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Hiányzó kötelező paraméter tesztelése
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Érvénytelen paramétertípus tesztelése
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Hibakezelési tesztek

Készítsen specifikus teszteket hibás feltételekre:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Rendezd el
    tool = ApiTool(timeout=0.1)  # Nagyon rövid időkorlát
    
    # Készíts hamis kérést, ami időtúllépést okoz
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Az időkorlátnál hosszabb
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Végezd el és ellenőrizd
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Ellenőrizd a kivétel üzenetét
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Rendezd el
    tool = ApiTool()
    
    # Készíts hamis, korlátozott sebességű választ
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
        
        # Végezd el és ellenőrizd
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Ellenőrizd, hogy a kivétel tartalmazza a sebességkorlát információt
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integrációs tesztelés

#### 1. Eszközlánc tesztelése

Tesztelje az eszközök együttműködését a várt kombinációkban:

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

#### 2. MCP szerver tesztelése

Tesztelje az MCP szervert teljes eszközregisztrációval és végrehajtással:

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
        // Teszteld a felfedezési végpontot
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Eszköz kérés létrehozása
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Kérés küldése és válasz ellenőrzése
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Érvénytelen eszköz kérés létrehozása
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Hiányzó "b" paraméter
        request.put("parameters", parameters);
        
        // Kérés küldése és hibaválasz ellenőrzése
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Teljes körű tesztelés (end-to-end)

Tesztelje a teljes munkafolyamatokat a modell kimeneti kéréstől az eszköz végrehajtásáig:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Elrendezés - MCP kliens és modell mockolása
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Modell válaszainak mockolása
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
    
    # Időjárás eszköz válaszának mockolása
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
        
        # Művelet végrehajtása
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Ellenőrzés
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Teljesítménytesztelés

#### 1. Terheléses tesztelés

Tesztelje, hány egyidejű kérést képes kezelni az MCP szervere:

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

#### 2. Stressztesztelés

Tesztelje a rendszert extrém terhelés alatt:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // JMeter beállítása terheléses teszteléshez
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter tesztterv konfigurálása
    HashTree testPlanTree = new HashTree();
    
    // Tesztterv, szálcsoport, mintavételezők létrehozása stb.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // HTTP mintavételező hozzáadása az eszköz futtatásához
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Hallgatók hozzáadása
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Teszt futtatása
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Eredmények ellenőrzése
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Átlagos válaszidő < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90. percentilis < 500ms
}
```

#### 3. Monitorozás és profilozás

Állítson be monitorozást hosszú távú teljesítmény elemzéshez:

```python
# MCP szerver monitorozásának konfigurálása
def configure_monitoring(server):
    # Prometheus metrikák beállítása
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
    
    # Middleware hozzáadása az időméréshez és metrikák rögzítéséhez
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Metrikák végpontjának kitétele
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP munkafolyamat-tervezési minták

A jól megtervezett MCP munkafolyamatok növelik a hatékonyságot, megbízhatóságot és karbantarthatóságot. Íme a legfontosabb minták:

### 1. Eszközlánc minta

Kapcsoljon össze több eszközt olyan sorrendben, ahol minden eszköz kimenete a következő bemenete lesz:

```python
# Python Eszközlánc megvalósítása
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Eszköz nevek listája, amelyeket sorban kell végrehajtani
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Minden eszköz végrehajtása a láncban, az előző eredmény átadásával
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Eredmény tárolása és bemenetként használata a következő eszközhöz
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Példa használat
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

### 2. Elosztó minta

Használjon központi eszközt, amely a bemenet alapján specializált eszközökhöz irányít:

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

### 3. Párhuzamos feldolgozás minta

Több eszköz párhuzamos végrehajtása a hatékonyság érdekében:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // 1. lépés: Az adatkészlet metaadatainak lekérése (szinkron)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // 2. lépés: Több elemzés párhuzamos indítása
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
        
        // Várakozás az összes párhuzamos feladat befejeződésére
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Várakozás a befejezésre
        
        // 3. lépés: Eredmények egyesítése
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // 4. lépés: Összefoglaló jelentés létrehozása
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Teljes munkafolyamat eredményének visszaadása
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Hibajavítás minta

Kíméletes visszaállítás hibák esetén:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Először az elsődleges eszközt próbálja ki
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Rögzítse a hibát
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Átváltás másodlagos eszközre
            try:
                # Lehet, hogy át kell alakítani a paramétereket az átváltó eszközhöz
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Mindkét eszköz hibát jelezett
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ez a megvalósítás az adott eszközöktől függne
        # Ebben a példában csak az eredeti paramétereket adjuk vissza
        return params

# Példa használat
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Elsődleges (fizetős) időjárás API
        "basicWeatherService",    # Tartalék (ingyenes) időjárás API
        {"location": location}
    )
```

### 5. Munkafolyamat-összeállítás minta

Építsen komplex munkafolyamatokat egyszerűbbek összeállításával:

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

# MCP szerverek tesztelése: legjobb gyakorlatok és hasznos tippek

## Áttekintés

A tesztelés kritikus eleme a megbízható, magas minőségű MCP szerverek fejlesztésének. Ez az útmutató átfogó legjobb gyakorlatokat és tippeket nyújt az MCP szerverek fejlesztési cikluson átívelő teszteléséhez, az egységtesztektől az integrációs teszteken át a teljes körű validálásig.

## Miért fontos a tesztelés az MCP szerverek esetében

Az MCP szerverek kulcsfontosságú köztes rétegként szolgálnak AI modellek és kliensalkalmazások között. Az alapos tesztelés biztosítja:

- Megbízhatóságot éles környezetben
- Pontos kérés- és válaszkezelést
- Az MCP specifikációk megfelelő megvalósítását
- Ellenálló képességet hibákkal és szélsőséges esetekkel szemben
- Következetes teljesítményt különböző terhelések alatt

## Egységtesztelés MCP szerverekhez

### Egységtesztelés (alap)

Az egységtesztek az MCP szerver egyes alkotóelemeit izoláltan ellenőrzik.

#### Mit teszteljünk

1. **Erőforrás-kezelők**: Tesztelje minden erőforrás-kezelő logikáját külön
2. **Eszköz megvalósítások**: Ellenőrizze az eszközök viselkedését különböző bemenetekkel
3. **Prompt-sablonok**: Biztosítsa, hogy a prompt-sablonok helyesen jelennek meg
4. **Séma érvényesítés**: Tesztelje a paraméterek érvényesítési logikáját
5. **Hibakezelés**: Ellenőrizze a hibaválaszokat érvénytelen bemenetek esetén

#### Legjobb gyakorlatok egységteszteléshez

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
# Példa egységteszt egy számológép eszközhöz Pythonban
def test_calculator_tool_add():
    # Előkészítés
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Művelet végrehajtása
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Ellenőrzés
    assert result["value"] == 12
```

### Integrációs tesztelés (középső réteg)

Az integrációs tesztek az MCP szerver alkotóelemei közötti interakciókat ellenőrzik.

#### Mit teszteljünk

1. **Szerver indítása**: Tesztelje a szerver indítását különböző konfigurációkkal
2. **Útvonal regisztráció**: Ellenőrizze, hogy minden végpont helyesen van regisztrálva
3. **Kérés feldolgozás**: Tesztelje a teljes kérés-válasz ciklust
4. **Hibák továbbítása**: Biztosítsa, hogy a hibák megfelelően kezelődnek a komponensek között
5. **Hitelesítés és jogosultság**: Tesztelje a biztonsági mechanizmusokat

#### Legjobb gyakorlatok integrációs teszteléshez

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

### Teljes körű tesztelés (felső réteg)

A teljes körű tesztek ellenőrzik a rendszer teljes viselkedését kliens és szerver között.

#### Mit teszteljünk

1. **Kliens-szerver kommunikáció**: Tesztelje a teljes kérés-válasz ciklust
2. **Valódi kliens SDK-k**: Teszteljen valódi kliens megvalósításokkal
3. **Teljesítmény terhelés alatt**: Ellenőrizze a viselkedést sok egyidejű kérés esetén
4. **Hibajavítás**: Tesztelje a rendszer helyreállását hibák esetén

5. **Hosszú futású műveletek**: Ellenőrizd a streaming és hosszú műveletek kezelését

#### E2E tesztelés legjobb gyakorlatai

```typescript
// Példa E2E teszt klienssel TypeScript-ben
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Szerver indítása teszt környezetben
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Művelet
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Ellenőrzés
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP teszteléshez való mockolási stratégiák

A mockolás alapvető a komponensek elszigeteléséhez tesztelés közben.

### Mockolandó komponensek

1. **Külső AI modellek**: Mockold a modell válaszokat kiszámítható teszteléshez
2. **Külső szolgáltatások**: Mockold az API függőségeket (adatbázisok, harmadik féltől származó szolgáltatások)
3. **Hitelesítési szolgáltatások**: Mockold az identitásszolgáltatókat
4. **Erőforrás szolgáltatók**: Mockold a költséges erőforrás kezelőket

### Példa: AI modell válaszának mockolása

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
# Python példa unittest.mock használatával
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Mock konfigurálása
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Mock használata a tesztben
    server = McpServer(model_client=mock_model)
    # Folytatás a teszttel
```

## Teljesítmény tesztelés

A teljesítmény tesztelés elengedhetetlen a termelési MCP szerverekhez.

### Mit mérjünk

1. **Válaszidő**: Kérések válaszideje
2. **Átviteli sebesség**: Másodpercenként kezelt kérések száma
3. **Erőforrás kihasználás**: CPU, memória, hálózathasználat
4. **Párhuzamosság kezelése**: Viselkedés párhuzamos kérések esetén
5. **Skálázódási jellemzők**: Teljesítmény a terhelés növekedésével

### Teljesítmény teszthez használható eszközök

- **k6**: Nyílt forráskódú terhelés tesztelő eszköz
- **JMeter**: Átfogó teljesítmény tesztelő eszköz
- **Locust**: Python alapú terhelés tesztelő
- **Azure Load Testing**: Felhő alapú teljesítmény tesztelés

### Példa: Alap terhelés teszt k6-val

```javascript
// k6 szkript az MCP szerver terheléses teszteléséhez
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtuális felhasználó
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

## MCP szerverek tesztelésének automatizálása

A tesztjeid automatizálása biztosítja az állandó minőséget és gyorsabb visszacsatolást.

### CI/CD integráció

1. **Futtass egység teszteket pull requesteken**: Biztosítsd, hogy a kódváltozások ne törjék a meglévő funkciókat
2. **Integrációs tesztek staging környezetben**: Futtass integrációs teszteket előállítás előtti környezetben
3. **Teljesítmény bázisvonalak**: Tarts fenn teljesítmény alapvonalakat a regressziók kiszűrésére
4. **Biztonsági vizsgálatok**: Automatizáld a biztonsági tesztelést a pipeline részeként

### Példa CI pipeline (GitHub Actions)

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

## MCP specifikációnak való megfelelőség tesztelése

Ellenőrizd, hogy a szervered helyesen valósítja meg az MCP specifikációt.

### Kulcsfontosságú megfelelőségi területek

1. **API végpontok**: Teszteld a kötelező végpontokat (/resources, /tools, stb.)
2. **Kérés/Válasz formátum**: Érvényesítsd a séma megfelelőséget
3. **Hibakódok**: Ellenőrizd a helyes státuszkódokat különböző esetekben
4. **Tartalomtípusok**: Teszteld a különféle tartalomtípusok kezelését
5. **Hitelesítési folyamat**: Ellenőrizd a specifikációnak megfelelő hitelesítési mechanizmusokat

### Megfelelőségi teszt csomag

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

## Top 10 tipp az MCP szerver teszteléséhez

1. **Teszteld külön a eszköz definíciókat**: Ellenőrizd a séma definíciókat az eszköz logikától függetlenül
2. **Használj paraméterezett teszteket**: Teszteld az eszközöket változatos bemenetekkel, beleértve a szélsőséges eseteket is
3. **Ellenőrizd a hibaválaszokat**: Biztosítsd a megfelelő hibakezelést minden lehetséges hiba esetén
4. **Teszteld az autorizációs logikát**: Biztosítsd a megfelelő hozzáférés-ellenőrzést különböző felhasználói szerepekhez
5. **Kövesd a teszt lefedettséget**: Tűzz ki célt a kritikus útvonalak magas lefedettségére
6. **Teszteld a streaming válaszokat**: Ellenőrizd a streaming tartalom helyes kezelését
7. **Szimuláld a hálózati problémákat**: Teszteld a viselkedést rossz hálózati körülmények között
8. **Teszteld az erőforrás korlátokat**: Ellenőrizd a működést kvóták vagy sebességkorlátok elérése esetén
9. **Automatizáld a regressziós teszteket**: Építs egy tesztcsomagot, amely minden kódváltozáskor lefut
10. **Dokumentáld a teszt eseteket**: Tarts fenn világos dokumentációt a teszt forgatókönyvekről

## Gyakori tesztelési hibák

- **Túlzott bizalom a pozitív utak tesztelésében**: Győződj meg róla, hogy alaposan teszteled a hibás eseteket is
- **Teljesítmény tesztelés figyelmen kívül hagyása**: Azonosítsd a szűk keresztmetszeteket még a termelés előtt
- **Csak izolált tesztelés**: Kombináld az egység, integrációs és végpont-végpont teszteket
- **Hiányos API lefedettség**: Biztosítsd, hogy minden végpontot és funkciót teszteljenek
- **Inkonzisztens teszt környezetek**: Használj konténereket az egységes teszt környezetekért

## Összefoglalás

Egy átfogó tesztelési stratégia elengedhetetlen a megbízható, magas minőségű MCP szerverek fejlesztéséhez. A jelen útmutatóban ismertetett legjobb gyakorlatok és tippek alkalmazásával biztosíthatod, hogy az MCP implementációid a legmagasabb minőségi, megbízhatósági és teljesítményi szabványoknak megfeleljenek.


## Főbb tanulságok

1. **Eszköz tervezés**: Kövesd az egyetlen felelősség elvét, használj függőség injektálást, és tervezz komponálhatóra
2. **Sémaz tervezés**: Készíts világos, jól dokumentált sémákat megfelelő validációs megszorításokkal
3. **Hibakezelés**: Valósíts meg kifinomult hibakezelést, strukturált hibaválaszokat és eredményorientált újrapróbálkozási logikát
   válaszokat és eredmény-tudatos újrapróbálkozási logikát
4. **Teljesítmény**: Használj gyorsítótárazást, aszinkron feldolgozást és erőforrás korlátozást
5. **Biztonság**: Alkalmazz átfogó bemeneti validációt, jogosultság-ellenőrzéseket és érzékeny adatok kezelését
6. **Tesztelés**: Készíts átfogó egység, integrációs és end-to-end teszteket
7. **Munkafolyamat minták**: Használj bevált mintákat, mint láncolatok, küldők és párhuzamos feldolgozás

## Gyakorlat

Tervezzen meg egy MCP eszközt és munkafolyamatot egy dokumentumfeldolgozó rendszerhez, amely:

1. Több formátumban fogad dokumentumokat (PDF, DOCX, TXT)
2. Kinyeri a szöveget és a kulcsfontosságú információkat a dokumentumokból
3. Osztályozza a dokumentumokat típus és tartalom szerint
4. Összefoglalót generál minden dokumentumról

Valósítsa meg az eszköz sémákat, hibakezelést, és válasszon egy munkafolyamat mintát, amely leginkább illik ehhez a forgatókönyvhöz. Gondolja át, hogyan tesztelné ezt az implementációt.

## Források 

1. Csatlakozzon az MCP közösséghez a [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) oldalon, hogy naprakész legyen a legújabb fejlesztésekről 
2. Vegyen részt nyílt forráskódú [MCP projektekben](https://github.com/modelcontextprotocol)
3. Alkalmazza az MCP elveket a saját szervezete AI kezdeményezéseiben
4. Fedezze fel az iparágának megfelelő speciális MCP implementációkat.
5. Fontolja meg haladó tanfolyamok elvégzését specifikus MCP témákban, mint például multimodális integráció vagy vállalati alkalmazási integráció.
6. Kísérletezzen saját MCP eszközök és munkafolyamatok építésével az itt tanult elvek alapján a [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) segítségével  

## Mi következik

Következő: [Esettanulmányok](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
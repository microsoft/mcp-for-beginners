# MCP arendamise parimad tavad

[![MCP arendamise parimad tavad](../../../translated_images/et/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Selle õppetunni video vaatamiseks kliki üleval olevale pildile)_

## Ülevaade

See õppetund keskendub edasijõudnutele mõeldud parimatele tavadele MCP serverite ja funktsioonide arendamisel, testimisel ja tarnimisel tootmiskeskkondades. Kui MCP ökosüsteemid muutuvad keerukamaks ja olulisemaks, tagab kehtivate mustrite järgimine usaldusväärsuse, hooldatavuse ja ühilduvuse. See õppetund koondab praktilist tarkust, mis on saadud reaalse MCP rakendamise kogemustest, et juhendada sind tugevate, tõhusate serverite loomisel, millel on tõhusad ressursid, käsud ja tööriistad.

## Õpieesmärgid

Selle õppetunni lõpus oskad:

- Rakendada tööstusharu häid tavasid MCP serveri ja funktsiooni disainis
- Luua põhjalikke testimisstrateegiaid MCP serveritele
- Kujundada tõhusaid, korduvkasutatavaid töövoo mustreid keerukatele MCP rakendustele
- Rakendada õiget vigade käsitlemist, logimist ja vaadeldavust MCP serverites
- Optimeerida MCP rakendusi jõudluse, turvalisuse ja hooldatavuse jaoks

## MCP põhiprintsiibid

Enne konkreetsete rakenduspraktikate käsitlemist on oluline mõista põhiprintsiipe, mis juhivad tõhusat MCP arendust:

1. **Standardiseeritud kommunikatsioon**: MCP kasutab oma aluseks JSON-RPC 2.0, tagades ühtlase vormingu päringute, vastuste ja vigade käsitlemise jaoks kõigis rakendustes.

2. **Kasutajakeskne disain**: Sea alati esikohale kasutaja nõusolek, kontroll ja läbipaistvus oma MCP rakendustes.

3. **Turvalisus esikohal**: Rakenda tugevad turvameetmed, sealhulgas autentimine, volitus, valideerimine ja kasutuspiirangud.

4. **Moodulpõhine arhitektuur**: Disaini oma MCP serverid moodulipõhiselt, kus igal tööriistal ja ressursil on selge ja keskendunud eesmärk.

5. **Selge olek**: MCP `2026-07-28` protokolli tasandil on seisunditu.
   Kui töövoos on vaja ristkõne olekut, kasuta ekspressseid identifikaatoreid või
   tavalisi tööriista argumente, mida toetab püsimajääv rakenduse olek.

## Ametlikud MCP parimad tavad

Järgmised parimad tavad pärinevad ametlikust Model Context Protocoli dokumentatsioonist:

### Turvalisuse parimad tavad

1. **Kasutaja nõusolek ja kontroll**: Nõua enne andmetele ligipääsu või toimingute tegemist alati selget kasutaja nõusolekut. Paku selget kontrolli selle üle, milliseid andmeid jagatakse ja milliseid toiminguid lubatakse.

2. **Andmete privaatsus**: Avalda kasutaja andmeid vaid selge nõusoleku alusel ja kaitse neid sobivate juurdepääsukontrollidega. Kaitse volitamata andmeside eest.

3. **Tööriistade turvalisus**: Nõua tööriista kasutamiseks alati selget kasutaja nõusolekut. Veendu, et kasutajad mõistavad iga tööriista funktsionaalsust ja kehtesta tugevad turvapiirid.

4. **Tööriistade õiguste kontroll**: Konfigureeri, milliseid tööriistu mudel võib kasutada
   iga päringu ja autoriseerimiskonteksti puhul, tagades, et ligipääsetavad on ainult selgelt volitatud
   tööriistad.

5. **Autentimine**: Nõua oma tööriistadele, ressurssidele või tundlikele toimingutele ligipääsuks õiget autentimist, kasutades API võtmeid, OAuth tokeneid või muid turvalisi autentimismeetodeid.

6. **Parameetrite valideerimine**: Tagada kõikide tööriista kutsumiste valideerimine, et takistada vigaste või pahatahtlike sisendite jõudmist tööriistade rakendusteni.

7. **Kiirusepiirangud**: Rakenda kiirusepiiranguid, et vältida väärkasutust ja tagada serveri ressursside õiglane jagamine.

### Rakendamise parimad tavad

1. **Võimekuste läbirääkimised**: Läbiräägi toetatud protokolli versioonide ja
   võimekuste üle. MCP `2026-07-28` mahus on iga päring iseseisev ja võib
   kasutada `server/discover`; vanemad versioonid kasutavad initsialiseerimisprotsessi.


2. **Tööriista kujundus**: Loo keskendunud tööriistu, mis teevad hästi ühte asja, mitte monoliitseid tööriistu, mis käsitlevad mitut küsimust.

3. **Vigade käsitlemine**: Rakenda standardiseeritud veateateid ja koode, et aidata probleemide diagnoosimisel, tõrgete sujuval käsitlemisel ja pakkuda tegevusele suunatud tagasisidet.

4. **Jälgitavus**: Kasuta `stderr` stdio diagnostika jaoks ja OpenTelemetry
   struktureeritud jälgitavuse jaoks. MCP logimise funktsioon on
   `2026-07-28` spetsifikatsioonis aegunud.

5. **Edenemise jälgimine**: Pikaajaliste toimingute puhul teata edenemise uuendusi, et võimaldada reageerivaid kasutajaliideseid.

6. **Päringu tühistamine**: Luba klientidel tühistada lennult päringud, mida enam vaja ei ole või mis võtavad liiga kaua aega.

## Täiendavad viited

Kõige ajakohasema teabe saamiseks MCP parimate tavade kohta, vaata:

- [MCP dokumentatsioon](https://modelcontextprotocol.io/)
- [MCP spetsifikatsioon (2026-07-28)][mcp-2026-spec]
- [Eelmine MCP spetsifikatsioon (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP ülesannete laiendus][mcp-tasks-extension]
- [GitHub hoidla](https://github.com/modelcontextprotocol)
- [Turvalisuse parimad tavad](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Turvariskid ja leevendused
- [MCP turvasummit töötoast (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktiline turvakoolitus

### Usaldusväärsuse kaaslase lektioon

Üldised korduslingid pole ohutud tööriistadele, mis loovad pileteid, makseid,
sõnumeid, juurutusi või muid reaalse maailma mõjusid. Vastus võib kaduda
pärast mõju kinnitamist.

Kasuta usaldusväärsuse kaaslase lektiooni,
[MCP tööriistade ohutud kordused: usaldusväärsuse kõrvalkaabli muster][reliability-sidecar],
et õppida stabiilse toimimise võtmeid, kaheksa vastuvõttu, kontrollpunktimist,
kooskõlastamist, tõendusandmeid ja rikete süstimist.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Praktilised rakendusnäited

### Tööriistade kujundamise parimad tavad

#### 1. Ühe vastutuse põhimõte

Igal MCP tööriistal peaks olema selge ja keskendunud eesmärk. Monoliitsete tööriistade loomise asemel, mis püüavad käsitleda mitut küsimust, arenda spetsialiseerunud tööriistu, mis paistavad silma konkreetsete ülesannete täitmisel.

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

#### 2. Ühtlane vigade käsitlemine

Rakenda tugevat vigade käsitlemist informatiivsete veateadete ja asjakohaste taastemehhanismidega.

```python
# Pythoni näide tervikliku veahaldusega
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Parameetrite valideerimine
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Turvakontroll
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Andmebaasi toiming ajapiiranguga
                async with timeout(10):  # 10 sekundi ajapiirang
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Ühenduse vead võivad olla mööduvad
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Päringuvigade põhjuseks on tõenäoliselt kliendipooled vead
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Las tööriista spetsiifilised vead läbi pääseda
            raise
        except Exception as e:
            # Püüdke kõik ootamatud vead kinni
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL-süstimise tuvastamise realiseerimine
        pass
        
    def _log_error(self, message, error):
        # Vealogimise realiseerimine
        pass
```

#### 3. Parameetrite valideerimine

Alati valideeri parameetrid põhjalikult, et vältida valesti vormindatud või pahatahtlikku sisendit.

```javascript
// JavaScript/TypeScript näide detailse parameetrite valideerimisega
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
    // 1. Kontrolli parameetri olemasolu
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Kontrolli parameetri tüüpe
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Kontrolli parameetri väärtusi
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Kontrolli sisu olemasolu kirjutamisoperatsiooni puhul
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Tee ohutuse kontroll
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Rakendamine valideeritud parameetrite põhjal
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Tee ohutuse kontrolli rakendamine
    // ...
  }
}
```

### Turvalisuse rakendusnäited

#### 1. Autentimine ja autoriseerimine

```java
// Java näide autentimise ja autoriseerimisega
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Sõltuvuste süstimine
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
        // 1. Eemalda autentimiskontekst
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autendi kasutaja
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Kontrolli konkreetse toimingu autoriseerimist
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Jätka autoriseeritud toiminguga
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

#### 2. Kiirusepiirang

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

## Testimise parimad tavad

### 1. Ühiktestimine MCP tööriistadele

Testi alati oma tööriistu isoleeritult, tehes väliste sõltuvuste simulatsiooni:

```typescript
// TypeScript näide tööriista üksustestist
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Loo valeilmateenuse teenus
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Loo tööriist vale sõltuvusega
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Ettevalmistus
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Tegutsemine
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Kontrollimine
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Ettevalmistus
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Tegutsemine ja kontrollimine
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integratsioonitestimine

Testi kogu voogu kliendipäringutest serverivastusteni:

```python
# Pythoni integratsioonitesti näide
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Käivita testiserver
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Loo klient
        client = McpClient("http://localhost:5000")
        
        # Testi tööriista avastamist
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Testi tööriista täitmist
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Kontrolli vastust
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Tee koristustööd
        await server.stop()
```

## Jõudluse optimeerimine


### 1. Vahemällu salvestamise strateegiad

Rakendage sobivat vahemällu salvestamist, et vähendada latentsust ja ressursikasutust:


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

#### 2. Sõltuvussüstimine ja testitavus

Kujunda tööriistad nii, et nad võtaksid oma sõltuvused vastu konstruktorisõltuvussüstimise kaudu, muutes need testitavaks ja konfigureeritavaks:

```java
// Java näide sõltuvussüstiga
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Sõltuvused süstitud konstruktoris
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Tööriista rakendus
    // ...
}
```

#### 3. Koostöövõimelised tööriistad

Kujunda tööriistad, mida saab ühendada keerukamate töövoogude loomiseks:

```python
# Pythoni näide koos moodulsete tööriistadega
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Rakendus...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # See tööriist saab kasutada dataFetch tööriista tulemusi
    async def execute_async(self, request):
        # Rakendus...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # See tööriist saab kasutada dataAnalysis tööriista tulemusi
    async def execute_async(self, request):
        # Rakendus...
        pass

# Neid tööriistu saab kasutada iseseisvalt või töövoo osana
```

### Skeemi kujundamise parimad tavad

Skeem on leping mudeli ja su tööriista vahel. Hästi kujundatud skeemid parandavad tööriistade kasutusmugavust.

#### 1. Selged parameetri kirjeldused

Lisa alati kirjeldav teave iga parameetri kohta:

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

#### 2. Valideerimispiirangud

Lisa valideerimispiirangud vigaste sisendite vältimiseks:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // E-posti atribuut koos vormingu valideerimisega
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Vanuse atribuut numbriliste piirangutega
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Enumeratsiooni atribuut
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

#### 3. Järjepidevad tagastusskeemid

Säilita oma vastusestruktuurides järjekindlus, et mudelitel oleks lihtsam tulemusi mõista:

```python
async def execute_async(self, request):
    try:
        # Töötle päringut
        results = await self._search_database(request.parameters["query"])
        
        # Tagasta alati järjekindel struktuur
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

### Veahaldus

Tugev vea käsitlemine on MCP tööriistade usaldusväärsuse tagamiseks kriitiline.

#### 1. Laulev veakäsitlemine

Käsitle vigu sobivatel tasanditel ja paku informatiivseid sõnumeid:

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

#### 2. Struktureeritud veavastused

Tagasta võimalusel struktureeritud veateave:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Rakendus
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
        
        // Heida teised erandid uuesti kui ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Uuesti katsumise loogika

Kasuta üldist uuesti katsumise loogikat ainult lugemiseks mõeldud kõnede või operatsioonide puhul, mille
alluv leping on juba idempotentne. Mõjuga operatsioonide puhul on ajapiirang
päringu saatmise järel ebamäärane. Ühenda ametlik olek ja
taaskasuta sama stabiilne operatsiooni võtit enne uuesti käivitamist. Vaata
[usaldusväärsuse abiaine õppetundi](./reliability-sidecars/README.md).

Järgmine piiratud uuesti katsumise tsükkel sobib lugemiseks mõeldud päringuks:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # sekundid
    
    while retry_count < max_retries:
        try:
            # Kutsu ainult lugemiseks mõeldud välis-API-d
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Eksponentsiaalne tagasilükkamine
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Mitteajutine viga, ära proovi uuesti
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Jõudluse optimeerimine

#### 1. Vahemällu salvestamine

Rakenda vahemälu kulukate operatsioonide jaoks:

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

#### 2. Asünkroonne töötlemine

Kasuta asünkroonseid programmeerimismustreid I/O-tüüpi operatsioonideks:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Pikaajaliste operatsioonide puhul tagastage koheselt töötlemise ID
        String processId = UUID.randomUUID().toString();
        
        // Alustage asünkroonset töötlemist
        CompletableFuture.runAsync(() -> {
            try {
                // Tehke pikaajaline operatsioon
                documentService.processDocument(documentId);
                
                // Uuendage olekut (tavaliselt salvestatakse andmebaasi)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Tagastage kohene vastus koos protsessi ID-ga
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Kaaslase oleku kontrollimise tööriist
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

#### 3. Ressursside piiramine

Rakenda ressursside kitsendamist ülekoormuse vältimiseks:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Luba 5 päringut sekundis
            bucket_size=10        # Luba pursetena kuni 10 päringut
        )
    
    async def execute_async(self, request):
        # Kontrolli, kas saame jätkata või peame ootama
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Kui ooteaeg on liiga pikk
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Oota sobiva viivituse aja
                await asyncio.sleep(delay)
        
        # Kasuta token ja jätka päringuga
        self.rate_limiter.consume()
        
        # Kutsu API
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
            
            # Arvuta aeg järgmise tokeni saadavuseni
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Lisa uusi tokeneid möödunud aja põhjal
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Turvalisuse parimad tavad

#### 1. Sisendi valideerimine

Alati põhjalikult valideeri sisendparameetrid:

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

#### 2. Autoriseerimise kontrollid

Rakenda korrektsed autoriseerimise kontrollid:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Hangi kasutaja kontekst päringust
    UserContext user = request.getContext().getUserContext();
    
    // Kontrolli, kas kasutajal on nõutavad õigused
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Spetsiifiliste ressursside puhul kontrolli ligipääsu sellele ressursile
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Jätka tööriista täitmisega
    // ...
}
```

#### 3. Tundlike andmete käitlemine

Käitle tundlikke andmeid hoolikalt:

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
        
        # Hangi kasutaja andmed
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtreeri tundlikud väljad, välja arvatud juhul, kui need on otseselt nõutud JA lubatud
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Kontrolli autoriseerimistaset päringu kontekstis
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Loo koopia, et vältida originaali muutmist
        redacted = user_data.copy()
        
        # Redigeeri spetsiifilisi tundlikke välju
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Redigeeri pesastatud tundlikke andmeid
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP tööriistade testimise parimad praktikad

Kõikehõlmav testimine tagab, et MCP tööriistad toimivad õigesti, käsitlevad äärejuhtumeid ning integreeruvad korrektselt süsteemi ülejäänud osaga.

### Üksustestimine

#### 1. Testi iga tööriista isoleeritult

Koosta fokuseeritud testid iga tööriista funktsionaalsuse jaoks:

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

#### 2. Skeemi valideerimise testimine

Testi, et skeemid oleksid kehtivad ja nõuetele vastavaks seatud:

```java
@Test
public void testSchemaValidation() {
    // Loo tööriista eksemplar
    SearchTool searchTool = new SearchTool();
    
    // Hangi skeem
    Object schema = searchTool.getSchema();
    
    // Muuda skeem JSON-iks valideerimiseks
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Kontrolli, kas skeem on kehtiv JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Testi kehtivaid parameetreid
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Testi puuduvat nõutud parameetrit
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Testi vigast parameetri tüüpi
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Veakäsitluse testid

Loo konkreetsed testid veaolukordade jaoks:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Korralda
    tool = ApiTool(timeout=0.1)  # Väga lühike ajalõpp
    
    # Tee päringu võltsimine, mis aegub
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Pikem kui ajalõpp
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Tegutse ja kontrolli
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Kontrolli erandi sõnumit
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Korralda
    tool = ApiTool()
    
    # Tee võltsitud kiirusepiiratud vastus
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
        
        # Tegutse ja kontrolli
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Kontrolli, et erand sisaldab kiirusepiirangu teavet
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integratsioonitestimine

#### 1. Tööriistaketti testimine

Testi tööriistade koostööd ootuspärastes kombinatsioonides:

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

#### 2. MCP serveri testimine

Testi MCP serverit täieliku tööriistaregistreerimise ja täitmisega:

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
        // Testi avastamise lõpp-punkti
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Loo tööriista päring
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Saada päring ja kontrolli vastust
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Loo kehtetu tööriista päring
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Puuduv parameeter "b"
        request.put("parameters", parameters);
        
        // Saada päring ja kontrolli veateadet
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Lõpust-lõpuni testimine

Testi täielikke töövooge mudeli päringust tööriista täitmiseni:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Korralda - Sea üles MCP klient ja malli mudel
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Malli mudeli vastused
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
    
    # Malli ilma tööriista vastus
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
        
        # Tegevus
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Kinnita
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Jõudluse testimine

#### 1. Koormustestimine

Testi, mitu samaaegset päringut su MCP server suudab töödelda:

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

#### 2. Stressitestimine

Testi süsteemi äärmusliku koormuse all:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Seadista JMeter koormustestiks
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigureeri JMeteri testi plaan
    HashTree testPlanTree = new HashTree();
    
    // Loo testiplaan, lõime grupp, proovijat jm
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Lisa HTTP proovija tööriista täitmiseks
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Lisa kuulajad
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Käivita test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Kontrolli tulemusi
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Keskmine vastuse aeg < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90 protsentiil < 500ms
}
```

#### 3. Jälgimine ja profilseerimine

Seadista jälgimine pikaajalise jõudlusanalüüsi jaoks:

```python
# Konfigureeri jälgimine MCP serveri jaoks
def configure_monitoring(server):
    # Sea üles Prometheuse mõõdikud
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
    
    # Lisa vahevara ajastuse ja mõõdikute salvestamise jaoks
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Ava mõõdikute lõpp-punkt
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP töövoo kujundusmustrid

Hästi kujundatud MCP töövood parandavad tõhusust, usaldusväärsust ja hooldatavust. Siin on peamised mustrid, mida järgida:

### 1. Tööriistade ahela muster

Ühenda mitu tööriista jadana, kus iga tööriista väljund muutub järgmise sisendiks:

```python
# Pythoni tööriistade ahela teostus
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Tööriistade nimede loend järjestikuseks käivitamiseks
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Käivita iga tööriist ahelas, edastades eelneva tulemuse
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Salvesta tulemus ja kasuta järgmiseks tööriistaks sisendina
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Näidise kasutus
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

### 2. Saatja muster

Kasuta keskselt tööriista, mis suunab sisendi põhjal spetsialiseeritud tööriistadele:

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

### 3. Paralleeltöötluse muster

Käivita mitu tööriista samaaegselt efektiivsuse tagamiseks:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // 1. samm: Andmekogu metaandmete toomine (sünkroonne)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // 2. samm: Käivita mitu analüüsi paralleelselt
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
        
        // Oota, kuni kõik paralleelsed ülesanded on lõpetatud
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Oota lõpetamist
        
        // 3. samm: Tulemuste kombineerimine
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // 4. samm: Loo kokkuvõttev aruanne
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Tagasta täielik töövoo tulemus
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Veast taastumise muster

Rakenda leebed varuplaanid tööriista rikete puhul:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Proovi esmalt põhitööriista
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Logi ebaõnnestumine
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Kasuta varutööriista
            try:
                # Võib-olla tuleb parameetreid varutööriista jaoks teisendada
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Mõlemad tööriistad ebaõnnestusid
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # See implementatsioon sõltub konkreetsetest tööriistadest
        # Selle näite puhul tagastame lihtsalt algsed parameetrid
        return params

# Näidiskasutus
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Põhi (tasuline) ilma API
        "basicWeatherService",    # Varu (tasuta) ilma API
        {"location": location}
    )
```

### 5. Töövoo koostise muster

Ehita keerukaid töövooge lihtsamate koostisosade abil:

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

# MCP serverite testimine: parimad tavad ja peamised näpunäited

## Ülevaade

Testimine on usaldusväärsete, kvaliteetsete MCP serverite juurutamise kriitiline osa. See juhend pakub põhjalikke parimaid tavasid ja näpunäiteid MCP serverite testimiseks kogu arendusprotsessi vältel, alates üksustestidest kuni integratsioonitestide ja lõpp-testideni.

## Miks MCP serverite testimine on oluline

MCP serverid toimivad olulise vahendajana tehisintellekti mudelite ja kliendirakenduste vahel. Põhjalik testimine tagab:

- Usaldusväärsuse tootmiskeskkondades
- Täpse päringute ja vastuste käsitlemise
- MCP spetsifikatsioonide korrektsuse rakendamise
- Kindluse tõrkete ja äärejuhtumite vastu
- Järjepideva jõudluse erinevate koormuste puhul

## Üksustestimine MCP serverite jaoks

### Üksustestimine (alus)

Üksustestid kontrollivad su MCP serveri üksikosade tööd isoleeritult.

#### Mida testida

1. **Ressursside käsitlejad**: testi iga ressursi käsitleja loogikat iseseisvalt
2. **Tööriistade rakendused**: kontrolli tööriistade käitumist erinevate sisendite korral
3. **Päringumallid**: veendu, et päringumallid kuvatakse õigesti
4. **Skeemi valideerimine**: testi parameetrite valideerimiste loogikat
5. **Veakäsitlus**: testi vigaste sisendite korral veavastuseid

#### Parimad tavad üksustestimiseks

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
# Näide ühiku testist kalkulaatori tööriista jaoks Pythoni keeles
def test_calculator_tool_add():
    # Ette valmistamine
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Tegutse
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Kontrolli ehk väida
    assert result["value"] == 12
```

### Integratsioonitestimine (kesktase)

Integratsioonitestid kontrollivad MCP serveri komponentide omavahelist koostööd.

#### Mida testida

1. **Serveri käivitamine**: testi serveri käivitust erinevate konfiguratsioonidega
2. **Marsruutide registreerimine**: veendu, et kõik lõpp-punktid on õigesti registreeritud
3. **Päringu töötlemine**: testi kogu päringu-vastuse tsüklit
4. **Vea levitamine**: veendu, et vead käsitletakse korrektselt komponentide vahel
5. **Autentimine ja autoriseerimine**: testi turvamehhanisme

#### Parimad tavad integratsioonitestimiseks

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

### Lõpust-lõpuni testimine (kõrgtase)

Lõpust-lõpuni testid kontrollivad kogu süsteemi toimimist kliendist serverini.

#### Mida testida

1. **Kliendi ja serveri kommunikatsioon**: testi täis päringu-vastuse tsükleid
2. **Tegelikud kliendi SDK-d**: testi päris kliendirakendustega
3. **Jõudlus koormuse all**: veendu mitme samaaegse päringu korral
4. **Veast taastumine**: testi süsteemi taastumist rikete korral

5. **Pikemaajalised toimingud**: Kontrollige voogesituse ja pikkade toimingute käsitlemist

#### Parimad tavad E2E testimiseks

```typescript
// Näide E2E test kliendiga TypeScriptis
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Käivita server testkeskkonnas
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Tegevus
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Kontroll
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP testimise imiteerimisstrateegiad

Imiteerimine on testimise ajal komponentide isoleerimiseks hädavajalik.

### Komponendid, mida imiteerida

1. **Välised tehisintellekti mudelid**: Imiteerige mudeli vastuseid, et testimine oleks ennustatav
2. **Välised teenused**: Imiteerige API sõltuvusi (andmebaasid, kolmandate osapoolte teenused)
3. **Autentimisteenused**: Imiteerige identiteediteenuse pakkujaid
4. **Ressursside pakkujad**: Imiteerige kallihinnalisi ressursihaldureid

### Näide: AI mudeli vastuse imiteerimine

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
# Pythoni näide kasutades unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Määra mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Kasuta mocki testis
    server = McpServer(model_client=mock_model)
    # Jätka testiga
```

## Jõudlustestimine

Jõudlustestimine on tootmis-MCP serverite jaoks ülioluline.

### Mida mõõta

1. **Latentsus**: Päringutele reageerimise aeg
2. **Läbilaskevõime**: Töödeldud päringute arv sekundis
3. **Ressursside kasutus**: CPU, mälu, võrgu kasutus
4. **Samasajalisuse käsitlemine**: Käitumine paralleelsete päringute korral
5. **Skaleerimise omadused**: Jõudlus koormuse suurenedes

### Jõudlustestimise tööriistad

- **k6**: Avatud lähtekoodiga koormustestimise tööriist
- **JMeter**: Kõikehõlmav jõudlustestimine
- **Locust**: Pythonil põhinev koormustestimine
- **Azure Load Testing**: Pilvepõhine jõudlustestimine

### Näide: Lihtne koormustest k6-ga

```javascript
// k6 skript MCP serveri koormustestimiseks
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtuaalkasutajat
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

## MCP serverite testimise automatiseerimine

Testide automatiseerimine tagab järjepideva kvaliteedi ja kiired tagasisidetsüklid.

### CI/CD integreerimine

1. **Üksustestide käivitamine pull requestidel**: Veenduge, et koodimuudatused ei katkestaks olemasolevat funktsionaalsust
2. **Integratsioonitestid etappkeskkonnas**: Käivitage integratsioonitestid tootmiseelsetes keskkondades
3. **Jõudluslikud baastasemed**: Säilitage jõudluse võrdlusalused regressioonide avastamiseks
4. **Turva skaneeringud**: Automatiseerige turvatestimine osana torujuhtmest

### Näide CI torujuhtmest (GitHub Actions)

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

## MCP spetsifikatsiooni järgimise testimine

Kontrollige, kas teie server rakendab MCP spetsifikatsiooni korrektselt.

### Peamised järgimise valdkonnad

1. **API lõpp-punktid**: Testige nõutud lõpp-punkte (/resources, /tools jne)
2. **Päringu/vastuse formaat**: Kontrollige skeemi järgimist
3. **Vea koodid**: Kontrollige õigeid olekukoodide erinevate stsenaariumide jaoks
4. **Sisu tüübid**: Testige erinevate sisutüüpide käsitlemist
5. **Autentimisteekond**: Kontrollige spetsifikatsioonile vastavaid autentimismehhanisme

### Järgimise testikomplekt

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

## 10 parimat nippi tõhusaks MCP serveri testimiseks

1. **Testige tööriistade määratlusi eraldi**: Kontrollige skeemide määratlusi tööriistaloogikast sõltumatult
2. **Kasutage parameetriseeritud teste**: Testige tööriistu erinevate sisenditega, sealhulgas äärejuhtudel
3. **Kontrollige veavastuseid**: Veenduge, et veakäsitlus oleks kõigi võimalike veatingimuste puhul korralik
4. **Testige autoriseerimisloogikat**: Tagage korrektne juurdepääsu kontroll erinevate kasutajarollide jaoks
5. **Jälgige testide katvust**: Püüdke jõuda kriitilise koodirada kõrge katvuseni
6. **Testige voogesituse vastuseid**: Kontrollige voogedastatud sisu korrektset käsitlemist
7. **Simuleerige võrgu probleeme**: Testige käitumist halbades võrguoludes
8. **Testige ressursipiiranguid**: Kontrollige käitumist kvantiteedi või kiiruse piiride saavutamisel
9. **Automatiseerige tagasikerimise testid**: Looge komplekt, mis käivitatakse iga koodimuudatuse korral
10. **Dokumenteerige testjuhtumid**: Hoidke selget dokumentatsiooni teststsenaariumitest

## Levinumad testimise lõksud

- **Liigne keskendumine lihtsatele juhtumitele**: Veenduge, et veajuhtumid oleksid põhjalikult testitud
- **Jõudlustestimise ignoreerimine**: Tuvastage kitsaskohad enne, kui need tootmises probleeme tekitavad
- **Testimine ainult isolatsioonis**: Kombineerige üksuse-, integratsiooni- ja E2E-teste
- **Ebapiisav API katvus**: Tagage kõigi lõpp-punktide ja funktsioonide testimine
- **Ebatäpsed testikeskkonnad**: Kasutage konteinerid järjepidevate testikeskkondade tagamiseks

## Kokkuvõte

Kõikehõlmav testimisstrateegia on usaldusväärsete, kvaliteetsete MCP serverite arendamisel hädavajalik. Rakendades selles juhendis välja toodud parimaid tavasid ja näpunäiteid, saate tagada, et teie MCP lahendused vastavad kõrgeimatele kvaliteedi, töökindluse ja jõudluse standarditele.


## Peamised järeldused

1. **Tööriista disain**: Järgige ühe vastutuse põhimõtet, kasutage sõltuvuste süstimist ja kavandage koostalitlusvõimalust
2. **Skeemi disain**: Looge selged, hästi dokumenteeritud skeemid koos asjakohaste valideerimiskontraintidega
3. **Veakäsitlus**: Rakendage graatsiline veakäsitlus, struktureeritud veavastused ja tulemust teadlik taaskäivitusloogika

4. **Jõudlus**: Kasutage vahemällu salvestamist, asünkroonset töötlemist ja ressursside piirangut
5. **Turvalisus**: Rakendage põhjalik sisendi valideerimine, autoriseerimis kontrollid ja tundliku info käitlemine
6. **Testimine**: Looge põhjalikud üksuse-, integratsiooni- ja lõpuni-lõpuni testid
7. **Töövoo mustrid**: Rakendage tuntud mustreid nagu ahelad, dispatcherid ja paralleeltöötlus

## Harjutus

Kavandage MCP tööriist ja töövoog dokumenditöötlussüsteemile, mis:

1. Võtab vastu dokumente mitmes vormingus (PDF, DOCX, TXT)
2. Eemaldab tekst ja võtmeinfo dokumentidest
3. Klassifitseerib dokumendid tüübi ja sisu järgi
4. Koostab iga dokumendi kokkuvõtte

Rakendage tööriista skeemid, veakäsitlus ja töövoo muster, mis kõige paremini sobib sellele stsenaariumile. Mõelge, kuidas te seda rakendust testiksite.

## Ressursid 

1. Liituge MCP kogukonnaga [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs), et olla kursis viimaste arengutega 
2. Panustage avatud lähtekoodiga [MCP projektidesse](https://github.com/modelcontextprotocol)
3. Rakendage MCP põhimõtteid oma organisatsiooni tehisintellekti algatustes
4. Uurige tööstusharu eripäraseid MCP rakendusi
5. Kaaluge MDC-teemaliste edasijõudnute kursuste osalemist, näiteks multimodaalse integreerimise või ettevõttesisese rakenduste integreerimise alal.
6. Katsetage oma MCP tööriistade ja töövoogude loomist, kasutades põhimõtteid, mida õppisite [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) juhendis  

## Mis järgmine

Järgmine: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
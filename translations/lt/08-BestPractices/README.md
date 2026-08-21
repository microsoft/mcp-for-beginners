# Geriausios MCP kūrimo praktikos

[![Geriausios MCP kūrimo praktikos](../../../translated_images/lt/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Spustelėkite aukščiau esantį paveikslėlį, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

## Apžvalga

Ši pamoka skirta pažangioms geriausioms praktikoms kurti, testuoti ir diegti MCP serverius bei funkcijas gamybos aplinkose. Kadangi MCP ekosistemos tampa vis sudėtingesnės ir svarbesnės, vadovavimasis nustatytais šablonais užtikrina patikimumą, priežiūrą ir tarpusavio suderinamumą. Ši pamoka apibendrina praktinę patirtį, gautą iš realių MCP įgyvendinimų, kad padėtų jums kurti patikimus, efektyvius serverius su veiksmingais resursais, kvietimais ir įrankiais.

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Taikyti pramonės geriausias praktikas MCP serverių ir funkcijų kūrime
- Kurti išsamią MCP serverių testavimo strategiją
- Projektuoti efektyvius, pakartotinai naudojamus darbo eigų šablonus sudėtingoms MCP programoms
- Įgyvendinti tinkamą klaidų valdymą, registravimą ir stebėjimą MCP serveriuose
- Optimizuoti MCP įgyvendinimus našumui, saugumui ir priežiūrai

## MCP pagrindiniai principai

Prieš gilindamiesi į konkrečias įgyvendinimo praktikas, svarbu suprasti pagrindinius principus, kurie leidžia efektyviai kurti MCP:

1. **Standartizuotas bendravimas**: MCP pagrįstas JSON-RPC 2.0, užtikrinančiu nuoseklią formato struktūrą užklausoms, atsakymams ir klaidų valdymui visuose įgyvendinimuose.

2. **Vartotojui orientuotas dizainas**: Visada pirmiausia dėmesį skirkite vartotojo sutikimui, kontrolei ir skaidrumui MCP įgyvendinimuose.

3. **Saugumas pirmiausia**: Įgyvendinkite tvirtas saugumo priemones, įskaitant autentifikaciją, autorizaciją, patvirtinimą bei užklausų dažnio ribojimą.

4. **Modulinė architektūra**: Projektuokite MCP serverius moduline struktūra, kur kiekvienas įrankis ir resursas turi aiškią, tikslinę paskirtį.

5. **Aiški būsena**: MCP `2026-07-28` protokolo sluoksnyje yra be valstybės
   informacijos. Kai darbo eiga reikalauja tarpinių kvietimų būsenos, naudokite aiškius identifikatorius arba
   įprastus įrankių argumentus, palaikomus patvarios programinės būsenos.

## Oficialios MCP geriausios praktikos

Toliau pateiktos geriausios praktikos yra iš oficialios Model Context Protocol dokumentacijos:

### Saugumo geriausios praktikos

1. **Vartotojo sutikimas ir kontrolė**: Visada reikalaukite aiškaus vartotojo sutikimo prieš prieigą prie duomenų ar atliekant veiksmus. Užtikrinkite aiškią kontrolę, kokie duomenys dalijami ir kokios veiksmai leidžiami.

2. **Duomenų privatumą**: Rodykite vartotojo duomenis tik gavus aiškų sutikimą ir apsaugokite juos tinkamomis prieigos kontrolėmis. Saugokite nuo nesankcionuoto duomenų perdavimo.

3. **Įrankių saugumas**: Reikalaukite aiškaus vartotojo sutikimo prieš paleidžiant bet kurį įrankį. Užtikrinkite, kad vartotojai suprastų kiekvieno įrankio funkcionalumą ir taikykite tvirtas saugumo ribas.

4. **Įrankių leidimų kontrolė**: Konfigūruokite, kuriuos įrankius modelis gali naudoti
   kiekvienai užklausai ir autorizacijos kontekstui, užtikrindami, kad būtų pasiekiami tik aiškiai autorizuoti
   įrankiai.

5. **Autentifikacija**: Reikalaukite tinkamos autentifikacijos prieš leidžiant prieigą prie įrankių, resursų ar jautrių operacijų, naudojant API raktus, OAuth žetonus ar kitas saugias autentifikavimo priemones.

6. **Parametrų patvirtinimas**: Užtikrinkite visų įrankių kvietimų patvirtinimą, kad būtų išvengta klaidingų ar kenksmingų įvesties duomenų pateikimo į įrankių įgyvendinimą.

7. **Užklausų dažnio ribojimas**: Įgyvendinkite užklausų dažnio ribojimą, kad būtų išvengta piktnaudžiavimo ir užtikrintas serverio resursų teisingas naudojimas.

### Įgyvendinimo geriausios praktikos

1. **Galimybių derybos**: Derėkitės dėl palaikomų protokolo versijų ir
   galimybių. MCP `2026-07-28` kiekviena užklausa yra savarankiška ir gali
   naudoti `server/discover`; senesnės versijos naudoja inicializacijos rankos paspaudimą.


2. **Įrankių dizainas**: Kurkite orientuotus įrankius, kurie gerai atlieka vieną užduotį, o ne monolitinius įrankius, apimančius daugelį funkcijų.

3. **Klaidų tvarkymas**: Įgyvendinkite standartizuotas klaidų žinutes ir kodus, kurie padeda diagnozuoti problemas, tinkamai tvarkyti nesėkmes ir suteikti naudingą atsiliepimą.

4. **Stebėjimas**: Naudokite `stderr` stdio diagnostikai ir OpenTelemetry
   struktūrizuotam stebėjimui. MCP žurnalo funkcija yra pasenusi
   pagal `2026-07-28` specifikaciją.

5. **Progreso stebėjimas**: Ilgai trunkančioms operacijoms teikite progreso atnaujinimus, kad būtų užtikrinta reaguojanti vartotojo sąsaja.

6. **Užklausos atšaukimas**: Leiskite klientams atšaukti vykdomas užklausas, kurios nebėra reikalingos arba užtrunka per ilgai.

## Papildomi šaltiniai

Norėdami gauti naujausią informaciją apie MCP geriausias praktikas, žiūrėkite:

- [MCP dokumentacija](https://modelcontextprotocol.io/)
- [MCP specifikacija (2026-07-28)][mcp-2026-spec]
- [Ankstesnė MCP specifikacija (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP užduočių išplėtimas][mcp-tasks-extension]
- [GitHub saugykla](https://github.com/modelcontextprotocol)
- [Saugumo geriausios praktikos](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Saugumo rizikos ir jų mažinimas
- [MCP saugumo viršūnių dirbtuvės (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktinis saugumo mokymas

### Patikimumo lydimosios pamokos

Bendri pakartotinių bandymų ciklai nėra saugūs įrankiams, kurie kuria bilietus, mokėjimus,
žinutes, diegimus ar kitus realaus pasaulio veiksmus. Atsakas gali būti pamestas
po to, kai poveikis jau įvykdytas.

Naudokite patikimumo lydimosios pamoką,
[Saugūs pakartotiniai bandymai MCP įrankiams: patikimumo šoninio automobilio šablonas][reliability-sidecar],
kad sužinotumėte apie stabilumo veikimo klavišus, dubliuotą admisiją, kontrolinius taškus,
sinchronizavimą, įrodymų lygius ir gedimų įpurškimą.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Praktiniai įgyvendinimo pavyzdžiai

### Įrankių dizaino gerosios praktikos

#### 1. Vienos atsakomybės principas

Kiekvienas MCP įrankis turėtų turėti aiškų, konkrečią paskirtį. Vietoje monolitinių įrankių, kurie bando spręsti kelias problemas, kurkite specializuotus įrankius, kurie puikiai atlieka tam tikras užduotis.

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

#### 2. Nuoseklus klaidų tvarkymas

Įgyvendinkite patikimą klaidų tvarkymą su informatyviomis klaidų žinutėmis ir tinkamais atkūrimo mechanizmais.

```python
# Python pavyzdys su išsamia klaidų tvarka
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Parametrų tikrinimas
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Saugumo patikra
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Duomenų bazės operacija su laiko limitu
                async with timeout(10):  # 10 sekundžių laiko limitas
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Ryšio klaidos gali būti laikinos
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Užklausų klaidos greičiausiai yra kliento klaidos
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Leisti specifinėms įrankių klaidoms prasiskverbti
            raise
        except Exception as e:
            # Visų netikėtų klaidų sugavimas
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL injekcijos aptikimo įgyvendinimas
        pass
        
    def _log_error(self, message, error):
        # Klaidos registravimo įgyvendinimas
        pass
```

#### 3. Parametrų tikrinimas

Visada kruopščiai tikrinkite parametrus, kad išvengtumėte klaidingo arba kenksmingo įvesties.

```javascript
// JavaScript/TypeScript pavyzdys su detalizuotu parametrų tikrinimu
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
    // 1. Patikrinti parametro buvimą
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Patikrinti parametro tipus
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Patikrinti parametro reikšmes
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Patikrinti turinio buvimą rašymo operacijai
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Kelio saugumo tikrinimas
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Įgyvendinimas remiantis patikrintais parametrais
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Kelio saugumo tikrinimo įgyvendinimas
    // ...
  }
}
```

### Saugumo įgyvendinimo pavyzdžiai

#### 1. Autentifikavimas ir autorizavimas

```java
// Java pavyzdys su autentifikacija ir autorizacija
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Priklausomybių injekcija
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
        // 1. Ištraukti autentifikacijos kontekstą
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autentifikuoti vartotoją
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Patikrinti autorizaciją konkrečiai operacijai
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Vykdyti įgaliotą operaciją
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

#### 2. Užklausų ribojimas

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

## Testavimo gerosios praktikos

### 1. Vienetinis MCP įrankių testavimas

Visada testuokite savo įrankius izoliuotai, imituodami išorines priklausomybes:

```typescript
// TypeScript pavyzdys įrankio vienetiniam testui
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Sukurti imituotą orų paslaugą
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Sukurti įrankį su imituota priklausomybe
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Paruošti
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Veikti
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Patikrinti
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Paruošti
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Veikti ir patikrinti
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integracinis testavimas

Testuokite visą srautą nuo kliento užklausų iki serverio atsakymų:

```python
# Python integracinio testo pavyzdys
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Paleisti testinį serverį
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Sukurti klientą
        client = McpClient("http://localhost:5000")
        
        # Išbandyti įrankio aptikimą
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Išbandyti įrankio vykdymą
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Patikrinti atsakymą
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Sutvarkyti išteklius
        await server.stop()
```

## Veikimo optimizavimas


### 1. Talpinimo strategijos

Įgyvendinkite tinkamą talpinimą, kad sumažintumėte vėlinimą ir resursų naudojimą:


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

#### 2. Priklausomybių įpurškimas ir testavimas

Kurkite įrankius taip, kad jų priklausomybės būtų perduodamos per konstruktorių, padarant juos testuojamus ir konfigūruojamus:

```java
// Java pavyzdys su priklausomybių injekcija
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Priklausomybės įšvirkščiuotos per konstruktorių
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Įrankio įgyvendinimas
    // ...
}
```

#### 3. Suderinami įrankiai

Kurkite įrankius, kurie gali būti sujungti kartu, kad būtų galima sukurti sudėtingesnius darbo srautus:

```python
# Python pavyzdys, rodantis suderinamus įrankius
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Įgyvendinimas...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Šis įrankis gali naudoti rezultatus iš dataFetch įrankio
    async def execute_async(self, request):
        # Įgyvendinimas...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Šis įrankis gali naudoti rezultatus iš dataAnalysis įrankio
    async def execute_async(self, request):
        # Įgyvendinimas...
        pass

# Šie įrankiai gali būti naudojami nepriklausomai arba kaip darbo eigos dalis
```

### Šemų kūrimo geriausios praktikos

Šema yra sutartis tarp modelio ir jūsų įrankio. Gerai suprojektuotos šemos užtikrina geresnį įrankio naudojimo patogumą.

#### 1. Aiškūs parametrų aprašymai

Visada įtraukite aprašomąją informaciją kiekvienam parametrui:

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

#### 2. Validacijos apribojimai

Įtraukite validacijos apribojimus, kad būtų užkirstas kelias netinkamoms įvestims:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // El. pašto savybė su formato patikrinimu
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Amžiaus savybė su skaitiniais apribojimais
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Išvardinta savybė
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

#### 3. Nuoseklios atsakymų struktūros

Išlaikykite atsakymų struktūrų nuoseklumą, kad modeliams būtų lengviau interpretuoti rezultatus:

```python
async def execute_async(self, request):
    try:
        # Apdoroti užklausą
        results = await self._search_database(request.parameters["query"])
        
        # Visada grąžinti nuoseklią struktūrą
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

### Klaidų tvarkymas

Patikimas klaidų tvarkymas yra labai svarbus MCP įrankiams, kad būtų užtikrintas patikimumas.

#### 1. Malonus klaidų tvarkymas

Tvarkykite klaidas tinkamuose lygiuose ir pateikite informatyvias žinutes:

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

#### 2. Struktūruoti klaidų atsakymai

Kai įmanoma, grąžinkite struktūruotą klaidų informaciją:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Įgyvendinimas
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
        
        // Perkraukite kitas išimtis kaip ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Perbandymo logika

Naudokite bendrą perbandymo logiką tik skaitymo režimo skambučiams ar operacijoms, kurių
sekančioji sutartis jau yra idempotentinė. Efektyvioms operacijoms po užklausos siuntimo
nustatytas laikmatis yra neaiškus. Suderinkite autoritetingą būseną ir
pakartotinai naudokite tą patį stabilų operacijos raktą prieš vėl vykdydami. Žr.
[patikimumo šoninio modulio pamoką](./reliability-sidecars/README.md).

Šis ribotas perbandymo ciklas tinka skaitymo režimo paieškai:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # sekundės
    
    while retry_count < max_retries:
        try:
            # Iškvieskite tik skaitymui skirtą išorinį API
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Eksponentinis atsitraukimas
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Netvarioji klaida, nebandykite dar kartą
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Veikimo optimizavimas

#### 1. Talpyklavimas

Įgyvendinkite talpyklavimą brangioms operacijoms:

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

#### 2. Asinchroninis apdorojimas

Naudokite asinchroninius programavimo modelius I/O ribojamoms operacijoms:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Ilgai trunkančioms operacijoms grąžinkite apdorojimo ID iškart
        String processId = UUID.randomUUID().toString();
        
        // Pradėkite asinchroninį apdorojimą
        CompletableFuture.runAsync(() -> {
            try {
                // Vykdykite ilgai trunkančią operaciją
                documentService.processDocument(documentId);
                
                // Atnaujinkite būseną (dažniausiai saugoma duomenų bazėje)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Grąžinkite momentinį atsakymą su proceso ID
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Pagalbinė būsenos tikrinimo priemonė
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

#### 3. Resursų apribojimas

Įgyvendinkite resursų apribojimus, kad išvengtumėte perkrovos:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Leisti 5 užklausas per sekundę
            bucket_size=10        # Leisti sprogimą iki 10 užklausų
        )
    
    async def execute_async(self, request):
        # Patikrinti, ar galime tęsti, ar reikia palaukti
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Jei laukimas per ilgas
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Palaukti reikiamą delsos laiką
                await asyncio.sleep(delay)
        
        # Panaudoti žetoną ir tęsti užklausą
        self.rate_limiter.consume()
        
        # Iškvieti API
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
            
            # Apskaičiuoti laiką iki kito žetono prieinamumo
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Pridėti naujus žetonus pagal praėjusį laiką
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Saugumo geriausios praktikos

#### 1. Įvesties validacija

Visada kruopščiai tikrinkite įvesties parametrus:

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

#### 2. Autorizacijos patikrinimai

Įgyvendinkite tinkamus autorizacijos patikrinimus:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Gauti vartotojo kontekstą iš užklausos
    UserContext user = request.getContext().getUserContext();
    
    // Patikrinti, ar vartotojas turi reikiamas teises
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Tikrinti prieigą prie konkrečių išteklių
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Tęsti įrankio vykdymą
    // ...
}
```

#### 3. Jautrių duomenų tvarkymas

Kruopščiai tvarkykite jautrius duomenis:

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
        
        # Gauti naudotojo duomenis
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtruoti jautrius laukus, jei nėra aiškiai prašoma IR leidžiama
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Patikrinti autorizacijos lygį užklausoje
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Sukurti kopiją, kad nebūtų modifikuojamas originalas
        redacted = user_data.copy()
        
        # Uždrausti konkrečius jautrius laukus
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Uždrausti įdėtus jautrius duomenis
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP įrankių testavimo geriausios praktikos

Išsamus testavimas užtikrina, kad MCP įrankiai veikia teisingai, tvarko ekstremalias situacijas ir tinkamai integruojasi su sistema.

### Vienetinis testavimas

#### 1. Testuokite kiekvieną įrankį atskirai

Kurkite fokusuotus testus kiekvienos įrankio funkcijos tikrinimui:

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

#### 2. Šemų validacijos testai

Testuokite, ar šemos yra galiojančios ir tinkamai taiko apribojimus:

```java
@Test
public void testSchemaValidation() {
    // Sukurti įrankio egzempliorių
    SearchTool searchTool = new SearchTool();
    
    // Gauti schemą
    Object schema = searchTool.getSchema();
    
    // Konvertuoti schemą į JSON validavimui
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Patikrinti, ar schema yra galiojanti JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Išbandyti galiojančius parametrus
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Išbandyti trūkstamą privalomą parametrą
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Išbandyti neteisingo parametro tipą
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Klaidų tvarkymo testai

Kurkite specifinius testus klaidų sąlygoms:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Sutvarkyti
    tool = ApiTool(timeout=0.1)  # Labai trumpas laukimo laikas
    
    # Sukurkite užklausos imitaciją, kuri baigsis laiko limitu
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Ilgesnis nei laukimo laikas
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Vykdyti ir patvirtinti
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Patikrinkite išimties pranešimą
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Sutvarkyti
    tool = ApiTool()
    
    # Sukurkite riboto greičio atsakymo imitaciją
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
        
        # Vykdyti ir patvirtinti
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Patikrinkite, ar išimtis yra su informacija apie greičio ribojimą
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integracinis testavimas

#### 1. Įrankių grandinės testavimas

Testuokite įrankius dirbančius kartu numatomose kombinacijose:

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

#### 2. MCP serverio testavimas

Testuokite MCP serverį su pilnu įrankių registracijos ir vykdymo procesu:

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
        // Išbandyti atradimo galinį tašką
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Sukurti įrankio užklausą
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Išsiųsti užklausą ir patikrinti atsakymą
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Sukurti neteisingą įrankio užklausą
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Trūksta parametro „b“
        request.put("parameters", parameters);
        
        // Išsiųsti užklausą ir patikrinti klaidos atsakymą
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. E2E testavimas

Testuokite pilnus darbo srautus nuo modelio užklausos iki įrankio vykdymo:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Surinkti - sukonfigūruokite MCP klientą ir imitacijos modelį
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Imitacijos modelio atsakymai
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
    
    # Imituokite orų įrankio atsakymą
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
        
        # Veiksmas
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Patvirtinti
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Veikimo testavimas

#### 1. Apkrovos testavimas

Testuokite, kiek daug lygiagrečių užklausų jūsų MCP serveris gali apdoroti:

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

#### 2. Streso testavimas

Testuokite sistemą ekstremaliomis apkrovomis:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Paruošti JMeter apkrovos testavimui
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigūruoti JMeter testo planą
    HashTree testPlanTree = new HashTree();
    
    // Sukurti testo planą, mazgų grupę, mėgintuvėlius ir kt.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Pridėti HTTP mėgintuvėlį įrankio vykdymui
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Pridėti klausytojus
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Vykdyti testą
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Patvirtinti rezultatus
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Vidutinis atsako laikas < 200 ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90 procentilis < 500 ms
}
```

#### 3. Stebėsena ir profilavimas

Įrenkite stebėseną ilgalaikiam veikimo analizės režimui:

```python
# Konfigūruoti stebėjimą MCP serveriui
def configure_monitoring(server):
    # Nustatyti Prometheus metrikas
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
    
    # Pridėti tarpinį programinį sluoksnį laikui matuoti ir metrikoms įrašyti
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Atidaryti metrikų galinį tašką
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP darbo srautų dizaino šablonai

Gerai suprojektuoti MCP darbo srautai pagerina efektyvumą, patikimumą ir priežiūrą. Štai pagrindiniai šablonai:

### 1. Įrankių grandinės šablonas

Sujunkite kelis įrankius seka, kur kiekvieno įrankio išvestis tampa įvestimi kitam:

```python
# Python įrankių grandinės įgyvendinimas
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Vykdomų įrankių pavadinimų sąrašas
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Vykdykite kiekvieną įrankį grandinėje, perduodami ankstesnį rezultatą
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Išsaugokite rezultatą ir naudokite jį kaip įvestį kitam įrankiui
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Naudojimo pavyzdys
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

### 2. Dispečerio šablonas

Naudokite centrinį įrankį, kuris paskirsto specializuotiems įrankiams pagal įvestį:

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

### 3. Lygiagretus apdorojimo šablonas

Vykdykite kelis įrankius tuo pačiu metu dėl efektyvumo:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // 1 žingsnis: Gauti duomenų rinkinio metaduomenis (sinchroniškai)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // 2 žingsnis: Paleisti kelias analizės užduotis lygiagrečiai
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
        
        // Laukti, kol visos lygiagrečios užduotys bus baigtos
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Laukti užbaigimo
        
        // 3 žingsnis: Apjungti rezultatus
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // 4 žingsnis: Generuoti santraukos ataskaitą
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Grąžinti visos darbo eigos rezultatą
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Klaidos atkūrimo šablonas

Įgyvendinkite malonius atsitraukimus įrankių klaidoms:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Pirmiausia išbandykite pagrindinį įrankį
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Užfiksuokite klaidą
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Grįžkite prie atsarginio įrankio
            try:
                # Gali prireikti transformuoti parametrus atsarginiam įrankiui
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Abu įrankiai nepavyko
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ši įgyvendinimo dalis priklausys nuo konkrečių įrankių
        # Šiame pavyzdyje tiesiog grąžinsime pradines reikšmes
        return params

# Pavyzdinis naudojimas
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Pagrindinis (mokamas) orų API
        "basicWeatherService",    # Atsarginis (nemokamas) orų API
        {"location": location}
    )
```

### 5. Darbo srauto sudarymo šablonas

Kuriate sudėtingus darbo srautus sudedant paprastesnius:

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

# MCP serverių testavimas: geriausios praktikos ir svarbiausios patarimai

## Apžvalga

Testavimas yra labai svarbus patikimų, aukštos kokybės MCP serverių kūrimo aspektas. Šiame vadove pateikiamos išsamios geriausios praktikos ir patarimai jūsų MCP serverių testavimui per visą kūrimo ciklą nuo vienetinių testų iki integracinių ir galutinių patikrinimų.

## Kodėl testavimas yra svarbus MCP serveriams

MCP serveriai yra svarbi tarpinė grandis tarp DI modelių ir kliento programų. Kruopštus testavimas užtikrina:

- Patikimumą gamybos aplinkose
- Teisingą užklausų ir atsakymų apdorojimą
- Tinkamą MCP specifikacijų įgyvendinimą
- Atsparumą gedimams ir kraštutinėms situacijoms
- Nuoseklų veikimą esant įvairioms apkrovoms

## Vienetiniai testai MCP serveriams

### Vienetiniai testai (pagrindas)

Vienetiniai testai tikrina atskiras jūsų MCP serverio dalis izoliacijoje.

#### Ką testuoti

1. **Resursų tvarkytojai**: nepriklausomai testuokite kiekvieno resurso tvarkytojo logiką
2. **Įrankių įgyvendinimas**: patikrinkite įrankių elgesį su įvairiomis įvestimis
3. **Užklausų šablonai**: užtikrinkite, kad šablonai teisingai renderintųsi
4. **Šemų validacija**: testuokite parametrų validacijos logiką
5. **Klaidų tvarkymas**: patikrinkite klaidų atsakymus netinkamoms įvestims

#### Vienetinių testų geriausios praktikos

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
# Pavyzdinis vieneto testas skaičiuotuvo įrankiui Python kalba
def test_calculator_tool_add():
    # Paruoškite
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Veikite
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Patikrinkite
    assert result["value"] == 12
```

### Integraciniai testai (vidurinis sluoksnis)

Integraciniai testai tikrina komponentų bendravimą jūsų MCP serveryje.

#### Ką testuoti

1. **Serverio inicijavimas**: testuokite serverio paleidimą su įvairiomis konfigūracijomis
2. **Maršrutų registracija**: patikrinkite, ar visi galiniai taškai tinkamai užregistruoti
3. **Užklausų apdorojimas**: testuokite visą užklausų ir atsakymų ciklą
4. **Klaidų perdavimas**: užtikrinkite, kad klaidos tinkamai tvarkomos tarp komponentų
5. **Autentifikacija ir autorizacija**: testuokite saugumo mechanizmus

#### Integracinių testų geriausios praktikos

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

### End-to-End testavimas (aukščiausias sluoksnis)

End-to-end testai tikrina viso sistemos elgesį nuo kliento iki serverio.

#### Ką testuoti

1. **Kliento ir serverio komunikacija**: testuokite pilnus užklausų ir atsakymų ciklus
2. **Tikri kliento SDK**: testuokite su tikrais kliento įgyvendinimais
3. **Veikimas esant apkrovai**: patikrinkite elgesį su daugeliu lygiagrečių užklausų
4. **Klaidų atkūrimas**: testuokite sistemos atsistatymą po gedimų

5. **Ilgai trunkančios operacijos**: Patikrinkite srautinio duomenų perdavimo ir ilgų operacijų valdymą

#### Geriausios E2E testavimo praktikos

```typescript
// Pavyzdinis E2E testas su klientu TypeScript kalba
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Paleisti serverį testų aplinkoje
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Veiksmas
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Patvirtinti
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP testavimo imitavimo strategijos

Imitavimas yra būtinas komponentų izoliuotam testavimui.

### Komponentai, kuriuos reikia imituoti

1. **Išoriniai DI modeliai**: Imituokite modelio atsakymus, kad testavimas būtų nuspėjamas
2. **Išorinės paslaugos**: Imituokite API priklausomybes (duomenų bazes, trečiųjų šalių paslaugas)
3. **Autentifikacijos paslaugos**: Imituokite tapatybės teikėjus
4. **Išteklių tiekėjai**: Imituokite brangių išteklių tvarkykles

### Pavyzdys: DI modelio atsakymo imitavimas

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
# Python pavyzdys su unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Konfigūruoti mock objektą
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Naudoti mock testuojant
    server = McpServer(model_client=mock_model)
    # Tęsti su testu
```

## Veiklos testavimas

Veiklos testavimas yra itin svarbus MCP gamybos serveriams.

### Ką matuoti

1. **Vėlavimas**: Užklausų atsakymo laikas
2. **Pralaidumas**: Per sekundę apdorotų užklausų skaičius
3. **Išteklių naudojimas**: CPU, atminties, tinklo naudojimas
4. **Lygiagretumo valdymas**: Elgesys paralelių užklausų metu
5. **Mastelio keitimo charakteristikos**: Veiklos pokyčiai didėjant apkrovai

### Veiklos testavimo įrankiai

- **k6**: Atviro kodo našumo testavimo įrankis
- **JMeter**: Išsamus veiklos testavimas
- **Locust**: Python pagrindu veikiantis apkrovos testavimas
- **Azure Load Testing**: Debesų pagrindu veikiantis našumo testavimas

### Pavyzdys: Bazinis apkrovos testas su k6

```javascript
// k6 scenarijus MCP serverio apkrovos testavimui
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtualių naudotojų
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

## Testų automatizavimas MCP serveriams

Testų automatizavimas užtikrina nuolatinę kokybę ir greitesnį atsiliepimą.

### CI/CD integracija

1. **Vienetinių testų vykdymas prie pull requestų**: Užtikrinkite, kad kodų pakeitimai nesugadintų egzistuojančios funkcionalumo
2. **Integracijos testai testinėje aplinkoje**: Vykdykite integracijos testus prieš gamybą
3. **Veiklos bazės linijos**: Laikykite veiklos rodiklius, kad būtų galima aptikti regresijas
4. **Saugumo skenavimas**: Automatizuokite saugumo testus kaip CI/CD proceso dalį

### Pavyzdys CI proceso (GitHub Actions)

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

## MCP specifikacijos atitikties testavimas

Patikrinkite, ar jūsų serveris tinkamai įgyvendina MCP specifikaciją.

### Pagrindinės atitikties sritys

1. **API galiniai taškai**: Testuokite privalomus galinius taškus (/resources, /tools ir kt.)
2. **Užklausų/atsakymų formatas**: Patvirtinkite schemos atitiktį
3. **Klaidų kodai**: Patikrinkite teisingus statuso kodus įvairioms situacijoms
4. **Turinio tipai**: Testuokite įvairių turinio tipų valdymą
5. **Autentifikacijos srautas**: Patikrinkite spec. atitinkančias autentifikacijos mechanizmus

### Atitikties testų rinkinys

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

## 10 pagrindinių patarimų efektyviam MCP serverių testavimui

1. **Testuokite įrankių apibrėžimus atskirai**: Tikrinkite schemų aprašymus nepriklausomai nuo įrankių logikos
2. **Naudokite parametrinius testus**: Testuokite įrankius su įvairiais įvesties duomenimis, įskaitant kraštutinius atvejus
3. **Tikrinkite klaidų atsakymus**: Patikrinkite teisingą klaidų tvarkymą visomis galimomis klaidų sąlygomis
4. **Testuokite autorizacijos logiką**: Užtikrinkite tinkamą prieigos kontrolę skirtingoms vartotojų rolėms
5. **Stebėkite testų aprėptį**: Siekite aukšto kritinių kodo kelių aprėpties
6. **Testuokite srauto atsakymus**: Patikrinkite teisingą srautinių turinio atsakymų valdymą
7. **Simuliuokite tinklo problemas**: Testuokite elgesį prastų tinklo sąlygų metu
8. **Testuokite išteklių ribas**: Patikrinkite elgesį pasiekiant kvotas ar greičio limitus
9. **Automatizuokite regresijos testus**: Sukurkite rinkinį, kuris veikia su kiekvienu kodo pakeitimu
10. **Dokumentuokite testų scenarijus**: Laikykite aiškią testavimo scenarijų dokumentaciją

## Dažnos testavimo klaidos

- **Per didelis pasikliovimas „akučių“ keliu**: Būtinai kruopščiai testuokite klaidų atvejus
- **Veiklos testavimo ignoravimas**: Identifikuokite našumo kliūtis prieš jas paveikiant gamybą
- **Testavimas tik izoliuotai**: Kombinuokite vienetinius, integracijos ir E2E testus
- **Nepilna API aprėptis**: Užtikrinkite testavimą visų galinių taškų ir savybių
- **Nenuoseklios testų aplinkos**: Naudokite konteinerius, kad užtikrintumėte nuoseklią testų aplinką

## Išvada

Išsami testavimo strategija yra būtina kuriant patikimus, aukštos kokybės MCP serverius. Įgyvendindami geriausias praktikas ir patarimus, pateiktus šiame vadove, užtikrinsite, kad jūsų MCP sprendimai atitiktų aukščiausius kokybės, patikimumo ir veiklos standartus.


## Pagrindinės išvados

1. **Įrankių dizainas**: Laikykitės vienos atsakomybės principo, naudokite priklausomybių injekciją ir projektuokite kompoziciškumui
2. **Schemų dizainas**: Kurkite aiškias, gerai dokumentuotas schemas su tinkamais validacijos apribojimais
3. **Klaidų valdymas**: Įgyvendinkite malonų klaidų tvarkymą, struktūrizuotus klaidų atsakymus ir atsargumo retry logiką
   pagal rezultatus
4. **Veikla**: Naudokite talpyklą, asinchroninį apdorojimą ir išteklių ribojimą
5. **Sauga**: Taikykite kruopščią įvesties patikrą, autorizacijos tikrinimus ir jautrių duomenų valdymą
6. **Testavimas**: Kurkite išsamius vienetinius, integracijos ir galutinio naudojimo testus
7. **Darbo eigų šablonai**: Naudokite įtvirtintus šablonus, tokius kaip grandinės, dispečeriai ir lygiagretus apdorojimas

## Užduotis

Sukurkite MCP įrankį ir darbo eigą dokumentų apdorojimo sistemai, kuri:

1. Priima dokumentus įvairiais formatais (PDF, DOCX, TXT)
2. Ištraukia tekstą ir svarbią informaciją iš dokumentų
3. Klasifikuoja dokumentus pagal tipą ir turinį
4. Generuoja kiekvieno dokumento santrauką

Įgyvendinkite įrankių schemas, klaidų valdymą ir darbo eigų šabloną, kuris geriausiai tinka šiai situacijai. Apsvarstykite, kaip testuotumėte šią implementaciją.

## Ištekliai

1. Prisijunkite prie MCP bendruomenės [Microsoft Foundry Discord bendruomenėje](https://aka.ms/foundrydevs), kad būtumėte informuoti apie naujausias naujienas
2. Prisidėkite prie atviro kodo [MCP projektų](https://github.com/modelcontextprotocol)
3. Taikykite MCP principus savo organizacijos DI iniciatyvose
4. Tyrinėkite specializuotas MCP įgyvendinimo galimybes jūsų pramonės sektoriuje
5. Apsvarstykite galimybę lankyti pažangius kursus apie tam tikras MCP temas, pavyzdžiui, daugiadatai integracijai ar įmonių programų integracijai
6. Eksperimentuokite kurdami savo MCP įrankius ir darbo eigas, pasinaudoję per [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) išmoktomis pamokomis

## Kas toliau

Toliau: [Atvejų studijos](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
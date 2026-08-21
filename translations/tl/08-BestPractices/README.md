# Mga Pinakamahusay na Gawi sa Pag-unlad ng MCP

[![Mga Pinakamahusay na Gawi sa Pag-unlad ng MCP](../../../translated_images/tl/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

## Pangkalahatang-ideya

Ang araling ito ay tumutuon sa mga advanced na pinakamahusay na gawi para sa pagbuo, pagsubok, at pag-deploy ng mga server at tampok ng MCP sa mga production na kapaligiran. Habang lumalalim ang mga MCP ecosystem sa pagiging kumplikado at kahalagahan, ang pagsunod sa mga itinatag na pattern ay nagsisiguro ng pagiging maaasahan, madaling mapanatili, at interoperability. Ang araling ito ay nagpapakilala ng praktikal na karunungan mula sa mga totoong implementasyon ng MCP upang gabayan ka sa paglikha ng matibay, mahusay na mga server na may mga epektibong resource, prompt, at kasangkapan.

## Mga Layunin sa Pagkatuto

Sa katapusan ng araling ito, magagawa mong:

- Ipatupad ang mga pinakamahusay na gawi sa industriya sa disenyo ng MCP server at tampok
- Gumawa ng komprehensibong mga estratehiya sa pagsubok para sa mga MCP server
- Magdisenyo ng mahusay, muling magagamit na mga pattern ng workflow para sa mga kumplikadong aplikasyon ng MCP
- Magpatupad ng tamang paghawak ng error, pag-log, at observability sa mga MCP server
- I-optimize ang mga implementasyon ng MCP para sa pagganap, seguridad, at kakayahang mapanatili

## Mga Pangunahing Prinsipyo ng MCP

Bago sumabak sa mga tiyak na gawi sa implementasyon, mahalagang maunawaan ang mga pangunahing prinsipyo na gumagabay sa epektibong pag-unlad ng MCP:

1. **Standardisadong Komunikasyon**: Gumagamit ang MCP ng JSON-RPC 2.0 bilang pundasyon nito, na nagbibigay ng pare-parehong format para sa mga hiling, tugon, at paghawak ng error sa lahat ng implementasyon.

2. **Disenyong Nakatuon sa Gumagamit**: Laging unahin ang pahintulot ng gumagamit, kontrol, at transparency sa iyong mga implementasyon ng MCP.

3. **Seguridad ang Pangunahing Prayoridad**: Magpatupad ng matibay na mga hakbang sa seguridad kabilang ang authentication, authorization, validation, at rate limiting.

4. **Modular na Arkitektura**: Idisenyo ang iyong mga MCP server gamit ang modular na pamamaraan, kung saan bawat kasangkapan at resource ay may malinaw at pokus na layunin.

5. **Eksplisit na Estado**: Stateless ang MCP `2026-07-28` sa protocol
   layer. Kapag nangangailangan ang isang workflow ng cross-call state, gumamit ng eksplisit na mga handle o
   ordinaryong mga argumento ng kasangkapan na sinusuportahan ng matibay na estado ng aplikasyon.

## Opisyal na Pinakamahusay na Gawi ng MCP

Ang mga sumusunod na pinakamahusay na gawi ay hango mula sa opisyal na dokumentasyon ng Model Context Protocol:

### Pinakamahusay na Gawi sa Seguridad

1. **Pahintulot at Kontrol ng Gumagamit**: Palaging humingi ng malinaw na pahintulot mula sa gumagamit bago ma-access ang data o gumawa ng operasyon. Magbigay ng malinaw na kontrol sa kung anong data ang ibinabahagi at kung aling mga aksyon ang pinapayagan.

2. **Pagkapribado ng Data**: Ipakita lamang ang data ng gumagamit na may malinaw na pahintulot at protektahan ito gamit ang angkop na mga kontrol sa pag-access. Iwasan ang hindi awtorisadong transmission ng data.

3. **Kaligtasan ng Kasangkapan**: Humingi ng malinaw na pahintulot ng gumagamit bago gamitin ang anumang kasangkapan. Siguraduhing nauunawaan ng mga gumagamit ang functionality ng bawat kasangkapan at ipatupad ang matibay na mga hangganan ng seguridad.

4. **Kontrol sa Pahintulot ng Kasangkapan**: I-configure kung aling mga kasangkapan ang maaaring gamitin ng isang modelo para sa
   bawat hiling at konteksto ng awtorisasyon, na nagsisiguro na tanging mga hayagang pinahintulutang
   kasangkapan lamang ang maa-access.

5. **Authentication**: Humingi ng wastong authentication bago payagan ang pag-access sa mga kasangkapan, resources, o sensitibong operasyon gamit ang mga API key, OAuth token, o iba pang ligtas na pamamaraan ng authentication.

6. **Validation ng Parameter**: Ipatupad ang pagsusuri para sa lahat ng paggamit ng kasangkapan upang maiwasan ang mga maling hugis o mapanirang input na makarating sa mga implementasyon ng kasangkapan.

7. **Rate Limiting**: Magpatupad ng rate limiting upang maiwasan ang abuso at matiyak ang patas na paggamit ng mga resource ng server.

### Pinakamahusay na Gawi sa Implementasyon

1. **Negosasyon ng Kakayahan**: Makipagnegosasyon ng mga suportadong bersyon ng protocol at
   kakayahan. Sa MCP `2026-07-28`, ang bawat hiling ay naglalaman ng sarili nitong impormasyon at maaaring
   gumamit ng `server/discover`; ang mga mas lumang bersyon ay gumagamit ng initialization handshake.

2. **Disenyo ng Kasangkapan**: Gumawa ng mga nakatutok na kasangkapan na mahusay sa isang bagay, sa halip na monolitikong mga kasangkapan na humahawak ng maraming alalahanin.

3. **Paghawak ng Error**: Magpatupad ng standardisadong mga mensahe ng error at code upang makatulong sa pag-diagnose ng mga isyu, maghawak nang maayos sa mga pagkabigo, at magbigay ng kapaki-pakinabang na puna.

4. **Observability**: Gumamit ng `stderr` para sa stdio diagnostics at OpenTelemetry
   para sa istrukturang observability. Ang tampok na pag-log ng MCP ay hindi na ginagamit sa
   `2026-07-28` na espesipikasyon.

5. **Pagsubaybay ng Progreso**: Para sa mga operasyon na tumatagal, iulat ang mga update sa progreso upang mapadali ang mga responsibong interface ng gumagamit.

6. **Pagkansela ng Hiling**: Payagan ang mga kliyente na kanselahin ang mga kasalukuyang hiling na hindi na kailangan o masyadong matagal.

## Karagdagang Sanggunian

Para sa pinaka-sariwang impormasyon tungkol sa mga pinakamahusay na gawi ng MCP, sumangguni sa:

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)][mcp-2026-spec]
- [Previous MCP Specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Tasks Extension][mcp-tasks-extension]
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Mga panganib sa seguridad at mga mitigasyon
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on na pagsasanay sa seguridad

### Aralin sa Katambal ng Katatagan

Ang mga generic na retry loop ay hindi ligtas para sa mga kasangkapan na lumilikha ng mga tiket, pagbabayad,
mga mensahe, deployment, o iba pang mga totoong epekto. Ang isang tugon ay maaaring mawala
pagkatapos matupad ang epekto.

Gamitin ang aralin sa katambal ng katatagan,
[Ligtas na mga Retry para sa mga Kasangkapan ng MCP: Isang Pattern ng Reliability Sidecar][reliability-sidecar],
upang matutunan ang mga stable operation key, duplicate admission, checkpointing,
reconciliation, mga antas ng ebidensya, at failure injection.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Mga Praktikal na Halimbawa ng Implementasyon

### Mga Pinakamahusay na Gawi sa Disenyo ng Kasangkapan

#### 1. Prinsipyo ng Solong Responsibilidad

Bawat kasangkapan ng MCP ay dapat may malinaw at pokus na layunin. Sa halip na gumawa ng monolitikong mga kasangkapan na sumusubok hawakan ang maraming alalahanin, bumuo ng mga espesyalisadong kasangkapan na mahusay sa mga partikular na gawain.

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

#### 2. Konsistenteng Paghawak ng Error

Magpatupad ng matibay na paghawak ng error na may informativong mga mensahe ng error at angkop na mga mekanismo sa pagbawi.

```python
# Halimbawa ng Python na may malawak na paghawak ng error
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Pagpapatunay ng parameter
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Pagpapatunay ng seguridad
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operasyon sa database na may timeout
                async with timeout(10):  # 10 segundong timeout
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Ang mga error sa koneksyon ay maaaring pansamantala
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Ang mga error sa query ay malamang na error ng kliyente
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Pabayaan na dumaan ang mga error na partikular sa tool
            raise
        except Exception as e:
            # Pangkalahatang pagkuha para sa hindi inaasahang mga error
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Pagpapatupad ng pagtuklas ng SQL injection
        pass
        
    def _log_error(self, message, error):
        # Pagpapatupad ng pag-log ng error
        pass
```

#### 3. Pagsusuri ng Parameter

Palaging suriin ng mabuti ang mga parameter upang maiwasan ang maling hugis o mapanirang input.

```javascript
// Halimbawa ng JavaScript/TypeScript na may detalyadong pag-validate ng mga parameter
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
    // 1. I-validate ang presensya ng parameter
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. I-validate ang mga uri ng parameter
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. I-validate ang mga halaga ng parameter
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. I-validate ang presensya ng nilalaman para sa operasyon ng pagsusulat
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Pag-validate ng kaligtasan ng path
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementasyon batay sa na-validate na mga parameter
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementasyon ng pag-check sa kaligtasan ng path
    // ...
  }
}
```

### Mga Halimbawa ng Implementasyon sa Seguridad

#### 1. Authentication at Authorization

```java
// Halimbawa ng Java na may pagpapatunay at awtorisasyon
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Injection ng dependency
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
        // 1. Kunin ang konteksto ng pagpapatunay
        String authToken = request.getContext().getAuthToken();
        
        // 2. Patunayan ang user
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Suriin ang awtorisasyon para sa partikular na operasyon
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Magpatuloy sa awtorisadong operasyon
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

#### 2. Rate Limiting

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

## Pinakamahusay na Gawi sa Pagsubok

### 1. Unit Testing ng Mga Kasangkapan ng MCP

Palaging subukan ang iyong mga kasangkapan nang hiwalay, gamit ang pagmomock ng mga eksternal na dependensya:

```typescript
// Halimbawa ng unit test ng tool sa TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Gumawa ng pekeng serbisyong pang-panahon
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Gumawa ng tool gamit ang pekeng dependency
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Ayusin
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Gawin
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Patunayan
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Ayusin
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Gawin at Patunayan
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integration Testing

Subukan ang kumpletong daloy mula sa mga kahilingan ng kliyente hanggang sa mga tugon ng server:

```python
# Halimbawa ng pagsubok sa integrasyon ng Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Simulan ang isang test server
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Gumawa ng isang kliyente
        client = McpClient("http://localhost:5000")
        
        # Subukan ang pagtuklas ng tool
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Subukan ang pagpapatakbo ng tool
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Beripikahin ang tugon
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Linisin pagkatapos
        await server.stop()
```

## Pag-optimize ng Pagganap

### 1. Mga Estratehiya ng Caching

Magpatupad ng angkop na caching upang mabawasan ang latency at paggamit ng resource:

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

#### 2. Dependency Injection at Kakayahang Masubukan

Disenyuhin ang mga kasangkapan na tumanggap ng kanilang mga dependensya sa pamamagitan ng constructor injection, na ginagawang masusubukan at nako-configure ang mga ito:

```java
// Halimbawa ng Java na may dependency injection
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Mga dependency na ini-inject sa pamamagitan ng constructor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementasyon ng tool
    // ...
}
```

#### 3. Mga Kasangkapang Puwedeng Pagsamahin

Disenyuhin ang mga kasangkapan na puwedeng pagsamahin upang lumikha ng mas kumplikadong mga workflow:

```python
# Halimbawa ng Python na nagpapakita ng mga pwedeng pagsamahin na kasangkapan
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementasyon...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Ang tool na ito ay maaaring gumamit ng mga resulta mula sa tool na dataFetch
    async def execute_async(self, request):
        # Implementasyon...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Ang tool na ito ay maaaring gumamit ng mga resulta mula sa tool na dataAnalysis
    async def execute_async(self, request):
        # Implementasyon...
        pass

# Ang mga tool na ito ay maaaring gamitin nang magkakahiwalay o bilang bahagi ng isang workflow
```

### Mga Pinakamahusay na Gawi sa Disenyo ng Schema

Ang schema ay ang kontrata sa pagitan ng modelo at ng iyong kasangkapan. Ang magagandang disenyo ng schema ay nagreresulta sa mas mahusay na pagiging gamit ng kasangkapan.

#### 1. Malinaw na Mga Paglalarawan ng Parameter

Laging isama ang mga mapanlarawang impormasyon para sa bawat parameter:

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

#### 2. Mga Limitasyon sa Validation

Isama ang mga constraint sa validation upang maiwasan ang mga hindi wastong input:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Katangian ng email na may pag-validate sa format
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Katangian ng edad na may mga numerikong limitasyon
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Katangiang may naka-enumerate na halaga
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

#### 3. Konsistenteng Mga Istruktura ng Return

Panatilihin ang konsistensi sa iyong mga istruktura ng tugon upang mapadali para sa mga modelo na bigyang-kahulugan ang mga resulta:

```python
async def execute_async(self, request):
    try:
        # Proseso ng kahilingan
        results = await self._search_database(request.parameters["query"])
        
        # Palaging magbalik ng pare-parehong istruktura
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

### Paghawak ng Error

Mahalaga ang matibay na paghawak ng error para sa mga kasangkapan ng MCP upang mapanatili ang katatagan.

#### 1. Maayos na Paghawak ng Error

Hawakan ang mga error sa naaangkop na mga antas at magbigay ng mga informativong mensahe:

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

#### 2. Istrakturang Tugon sa Error

Magbalik ng istrakturang impormasyon ng error kung maaari:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementasyon
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
        
        // Muling ihagis ang ibang mga eksepsyon bilang ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Loob ng Retry

Gumamit ng generic na retry logic lamang para sa read-only na mga tawag o operasyon kung saan ang
downstream contract ay idempotent na. Para sa mga effectful na operasyon, ang timeout
pagkatapos magpadala ng hiling ay hindi tiyak. Pagsamahin ang authoritative state at
muling gamitin ang parehong stable operation key bago muling magpatupad. Tingnan ang
[aralin sa katambal ng reliability sidecar](./reliability-sidecars/README.md).

Ang sumusunod na bounded retry loop ay angkop para sa isang read-only lookup:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # segundo
    
    while retry_count < max_retries:
        try:
            # Tumawag sa external API na read-only
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Eksponensyal na pagbawi
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Hindi pansamantalang error, huwag ulitin
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Pag-optimize ng Pagganap

#### 1. Caching

Magpatupad ng caching para sa mga mamahaling operasyon:

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

#### 2. Asynchronous na Pagpoproseso

Gumamit ng mga asynchronous na pattern sa programming para sa mga I/O-bound na operasyon:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Para sa mga pangmatagalang operasyon, ibalik agad ang isang processing ID
        String processId = UUID.randomUUID().toString();
        
        // Simulan ang async na proseso
        CompletableFuture.runAsync(() -> {
            try {
                // Isagawa ang pangmatagalang operasyon
                documentService.processDocument(documentId);
                
                // I-update ang status (karaniwan itong iniimbak sa isang database)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Ibalik ang agarang tugon na may prosesong ID
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Kasamang tool para sa pagsuri ng status
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

#### 3. Paghihigpit sa Resource

Magpatupad ng paghihigpit sa resource upang maiwasan ang sobrang paggamit:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Pahintulutan ang 5 kahilingan kada segundo
            bucket_size=10        # Pahintulutan ang biglaang pagtaas hanggang 10 kahilingan
        )
    
    async def execute_async(self, request):
        # Suriin kung maaari tayong magpatuloy o kailangang maghintay
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Kung masyadong mahaba ang paghihintay
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Maghintay para sa angkop na oras ng pagkaantala
                await asyncio.sleep(delay)
        
        # Gumamit ng isang token at magpatuloy sa kahilingan
        self.rate_limiter.consume()
        
        # Tawagan ang API
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
            
            # Kalkulahin ang oras hanggang sa susunod na token ay magagamit
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Magdagdag ng mga bagong token batay sa lumipas na oras
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Pinakamahusay na Gawi sa Seguridad

#### 1. Validation ng Input

Palaging masusi suriin ang mga input parameter:

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

#### 2. Mga Pagsusuri sa Awtorisasyon

Magpatupad ng wastong mga pagsusuri sa awtorisasyon:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Kumuha ng konteksto ng user mula sa kahilingan
    UserContext user = request.getContext().getUserContext();
    
    // Suriin kung ang user ay may kinakailangang mga pahintulot
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Para sa mga partikular na resources, suriin ang access sa resource na iyon
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Ipatuloy ang pagpapatakbo ng tool
    // ...
}
```

#### 3. Paghawak ng Sensitibong Data

Hawakan nang maingat ang sensitibong data:

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
        
        # Kunin ang data ng user
        user_data = await self.user_service.get_user_data(user_id)
        
        # Salain ang mga sensitibong patlang maliban kung hayagang hinihiling AT pinahintulutan
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Suriin ang antas ng awtorisasyon sa konteksto ng kahilingan
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Gumawa ng kopya upang maiwasang baguhin ang orihinal
        redacted = user_data.copy()
        
        # Itago ang tiyak na sensitibong mga patlang
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Itago ang isinusubong sensitibong data
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Pinakamahusay na Gawi sa Pagsubok para sa Mga Kasangkapan ng MCP

Ang komprehensibong pagsubok ay nagsisigurong ang mga kasangkapan ng MCP ay gumagana nang tama, humahawak ng mga edge case, at maayos na nakikisalamuha sa natitirang bahagi ng sistema.

### Unit Testing

#### 1. Subukan Bawat Kasangkapan nang Hiwalay

Gumawa ng mga nakatutok na pagsubok para sa functionality ng bawat kasangkapan:

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

#### 2. Pagsubok ng Validation ng Schema

Subukan na balido ang mga schema at wastong ipinapatupad ang mga constraint:

```java
@Test
public void testSchemaValidation() {
    // Gumawa ng halimbawa ng tool
    SearchTool searchTool = new SearchTool();
    
    // Kunin ang iskema
    Object schema = searchTool.getSchema();
    
    // I-convert ang iskema sa JSON para sa beripikasyon
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Suriin kung ang iskema ay valid na JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Subukan ang mga wastong parameter
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Subukan ang nawawalang kinakailangang parameter
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Subukan ang di-wastong uri ng parameter
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Mga Pagsubok sa Paghawak ng Error

Gumawa ng espesyal na pagsubok para sa mga kalagayan ng error:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Ayusin
    tool = ApiTool(timeout=0.1)  # Napakaikling timeout
    
    # Gawing mock ang isang request na magti-time out
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Higit sa timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Gawin at I-assert
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Suriin ang mensahe ng exception
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Ayusin
    tool = ApiTool()
    
    # Gawing mock ang isang rate-limited na tugon
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
        
        # Gawin at I-assert
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Suriin kung ang exception ay naglalaman ng impormasyon tungkol sa rate limit
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integration Testing

#### 1. Pagsubok ng Chain ng Kasangkapan

Subukan ang mga kasangkapan na nagtutulungan sa inaasahang mga kumbinasyon:

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

#### 2. Pagsubok sa MCP Server

Subukan ang MCP server gamit ang buong pagrerehistro at pagpapatupad ng kasangkapan:

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
        // Subukan ang discovery endpoint
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Gumawa ng kahilingan para sa tool
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Ipadala ang kahilingan at tiyakin ang tugon
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Gumawa ng hindi wastong kahilingan para sa tool
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Nawawalang parametro na "b"
        request.put("parameters", parameters);
        
        // Ipadala ang kahilingan at tiyakin ang tugon ng error
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. End-to-End Testing

Subukan ang kumpletong workflow mula sa prompt ng modelo hanggang sa pagpapatupad ng kasangkapan:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Ayusin - I-set up ang MCP client at mock model
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Mock na mga tugon ng modelo
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
    
    # Mock na tugon ng weather tool
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
        
        # Gawin
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Patunayan
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Pagsubok sa Pagganap

#### 1. Load Testing

Subukan kung ilang magkakasabay na hiling ang kayang hawakan ng iyong MCP server:

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

#### 2. Stress Testing

Subukan ang sistema sa ilalim ng matinding load:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // I-set up ang JMeter para sa stress testing
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // I-configure ang plano ng pagsubok ng JMeter
    HashTree testPlanTree = new HashTree();
    
    // Gumawa ng plano ng pagsubok, thread group, samplers, atbp.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Magdagdag ng HTTP sampler para sa pagpapatakbo ng tool
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Magdagdag ng mga listener
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Patakbuhin ang pagsubok
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Patunayan ang mga resulta
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Average na oras ng tugon < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90th percentile < 500ms
}
```

#### 3. Pagmomonitor at Profiling

Mag-set up ng pagmomonitor para sa pangmatagalang pagsusuri ng pagganap:

```python
# I-configure ang pagmamanman para sa isang MCP server
def configure_monitoring(server):
    # Isaayos ang mga sukatan ng Prometheus
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
    
    # Magdagdag ng middleware para sa pagsukat ng oras at pagtatala ng mga sukatan
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # I-expose ang endpoint ng mga sukatan
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Mga Pattern ng Disenyo ng MCP Workflow

Ang mga maayos na disenyo ng MCP workflow ay nagpapabuti ng kahusayan, pagiging maaasahan, at kakayahang mapanatili. Narito ang mahahalagang pattern na sundin:

### 1. Pattern ng Chain ng Kasangkapan

Ikonekta ang maraming kasangkapan sa isang sunod-sunod na proseso kung saan ang output ng bawat kasangkapan ay nagsisilbing input para sa kasunod:

```python
# Implementasyon ng Python Chain of Tools
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Listahan ng mga pangalan ng tool na isasagawa ng sunud-sunod
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Isagawa ang bawat tool sa chain, ipinapasa ang naunang resulta
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Itago ang resulta at gamitin bilang input para sa susunod na tool
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Halimbawa ng paggamit
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

### 2. Pattern ng Dispatcher

Gumamit ng sentral na kasangkapan na nagdi-dispatch sa mga espesyalisadong kasangkapan batay sa input:

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

### 3. Pattern ng Parallel Processing

Isagawa ang maraming kasangkapan nang sabay-sabay para sa kahusayan:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Hakbang 1: Kunin ang metadata ng dataset (synchronous)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Hakbang 2: Ilunsad ang maramihang pagsusuri nang sabay-sabay
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
        
        // Maghintay hanggang matapos ang lahat ng parallel na gawain
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Maghintay hanggang matapos
        
        // Hakbang 3: Pagsamahin ang mga resulta
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Hakbang 4: Gumawa ng ulat ng buod
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Ibalik ang kumpletong resulta ng workflow
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Pattern ng Pagbawi sa Error

Magpatupad ng maayos na mga fallback para sa mga pagkabigo ng kasangkapan:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Subukan munang gamitin ang pangunahing kasangkapan
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # I-log ang pagkabigo
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Lumipat sa pangalawang kasangkapan
            try:
                # Maaaring kailanganing baguhin ang mga parametro para sa pangalawang kasangkapan
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Nabigo ang parehong mga kasangkapan
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ang implementasyong ito ay depende sa mga espesipikong kasangkapan
        # Sa halimbawa na ito, ibabalik lang natin ang orihinal na mga parametro
        return params

# Halimbawa ng paggamit
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Pangunahing (bayad) na weather API
        "basicWeatherService",    # Pangalawang (libre) na weather API
        {"location": location}
    )
```

### 5. Pattern ng Komposisyon ng Workflow

Bumuo ng mga kumplikadong workflow sa pamamagitan ng pagsasama-sama ng mga mas simpleng workflow:

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

# Pagsubok sa Mga MCP Server: Pinakamahusay na Gawi at Mga Pangunahing Tip

## Pangkalahatang-ideya

Ang pagsubok ay isang kritikal na aspeto ng pagbuo ng mga maaasahan at mataas na kalidad na MCP server. Ang gabay na ito ay nagbibigay ng komprehensibong pinakamahusay na gawi at tip sa pagsubok ng iyong mga MCP server sa buong lifecycle ng pag-unlad, mula sa unit tests hanggang integration tests at end-to-end validation.

## Bakit Mahalaga ang Pagsubok para sa Mga MCP Server

Ang mga MCP server ay nagsisilbing mahalagang middleware sa pagitan ng mga AI model at ng mga aplikasyon ng kliyente. Ang masusing pagsubok ay nagsisiguro ng:

- Katatagan sa mga production na kapaligiran
- Tumpak na paghawak ng mga hiling at tugon
- Wastong implementasyon ng mga espesipikasyon ng MCP
- Kakayahang makabangon mula sa mga error at mga edge case
- Konsistenteng pagganap sa ilalim ng iba't ibang mga load

## Unit Testing para sa Mga MCP Server

### Unit Testing (Pundasyon)

Tine-verify ng mga unit test ang bawat indibidwal na bahagi ng iyong MCP server nang hiwalay.

#### Ano ang Susubukan

1. **Mga Tagahawak ng Resource**: Subukan nang hiwalay ang lohika ng bawat tagahawak ng resource
2. **Mga Implementasyon ng Kasangkapan**: Suriin ang pag-uugali ng kasangkapan gamit ang iba't ibang input
3. **Templates ng Prompt**: Tiyakin na maayos na nairender ang mga template ng prompt
4. **Validation ng Schema**: Subukan ang lohika ng pag-validate ng parameter
5. **Paghawak ng Error**: Tiyakin ang mga tugon sa error para sa mga maling input

#### Mga Pinakamahusay na Gawi para sa Unit Testing

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
# Halimbawang unit test para sa isang calculator tool sa Python
def test_calculator_tool_add():
    # Ayusin
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Gawin
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Patunayan
    assert result["value"] == 12
```

### Integration Testing (Gitnang Layer)

Tine-verify ng integration test ang pakikipag-ugnayan sa pagitan ng mga bahagi ng iyong MCP server.

#### Ano ang Susubukan

1. **Initialization ng Server**: Subukan ang pagsisimula ng server gamit ang iba't ibang configuration
2. **Rehistrasyon ng Ruta**: Tiyakin na ang lahat ng endpoint ay tama na nairehistro
3. **Pagpoproseso ng Hiling**: Subukan ang buong cycle ng request-response
4. **Pagpapalaganap ng Error**: Siguraduhing maayos ang paghawak ng error sa mga bahagi
5. **Authentication at Authorization**: Subukan ang mga mekanismo sa seguridad

#### Mga Pinakamahusay na Gawi para sa Integration Testing

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

### End-to-End Testing (Pinakatuktok na Layer)

Tine-verify ng end-to-end test ang kompletong pag-uugali ng sistema mula kliyente hanggang server.

#### Ano ang Susubukan

1. **Komunikasyon ng Client-Server**: Subukan ang kompletong cycles ng request-response
2. **Tunay na Client SDKs**: Subukan gamit ang totoong mga implementasyon ng kliyente
3. **Pagganap sa Ilalim ng Load**: Tiyakin ang pag-uugali sa maraming sabay-sabay na hiling
4. **Pagbawi mula sa Error**: Subukan ang pagbawi ng sistema mula sa mga pagkabigo

5. **Pang-matagalang Operasyon**: Siguraduhing maayos ang paghawak ng streaming at pang-matagalang operasyon

#### Mga Pinakamahusay na Kasanayan para sa E2E Testing

```typescript
// Halimbawa ng E2E test gamit ang kliyente sa TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Simulan ang server sa test environment
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Gawin
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Patunayan
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Mga Estratehiya sa Mocking para sa MCP Testing

Mahalaga ang mocking para sa pag-isolate ng mga bahagi habang nagte-testing.

### Mga Bahaging Imo-mock

1. **Mga Panlabas na AI Models**: Imock ang mga tugon ng modelo para sa predictable na testing
2. **Mga Panlabas na Serbisyo**: Imock ang mga dependency ng API (databases, third-party services)
3. **Mga Serbisyo sa Authentication**: Imock ang mga identity providers
4. **Mga Provider ng Resource**: Imock ang mahahalagang resource handlers

### Halimbawa: Pagmo-mock ng Tugon mula sa AI Model

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
# Halimbawa ng Python gamit ang unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # I-configure ang mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Gamitin ang mock sa pagsusulit
    server = McpServer(model_client=mock_model)
    # Magpatuloy sa pagsusulit
```

## Performance Testing

Mahalaga ang performance testing para sa mga production MCP server.

### Ano ang Dapat Sukatin

1. **Latency**: Oras ng tugon sa mga kahilingan
2. **Throughput**: Mga kahilingang naiproseso kada segundo
3. **Paggamit ng Resource**: CPU, memorya, paggamit ng network
4. **Paghawak ng Concurrency**: Ugali sa ilalim ng sabayang kahilingan
5. **Katangian ng Pag-scale**: Performance habang tumataas ang load

### Mga Tool para sa Performance Testing

- **k6**: Open-source na load testing tool
- **JMeter**: Komprehensibong performance testing
- **Locust**: Python-based load testing
- **Azure Load Testing**: Cloud-based performance testing

### Halimbawa: Basic Load Test gamit ang k6

```javascript
// k6 script para sa load testing ng MCP server
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtual na mga gumagamit
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

## Test Automation para sa MCP Servers

Tinitiyak ng pag-aautomat ng iyong mga test ang tuloy-tuloy na kalidad at mas mabilis na feedback loops.

### CI/CD Integration

1. **Patakbuhin ang Unit Tests sa Pull Requests**: Siguraduhing hindi nasisira ang umiiral na functionality ng mga pagbabago sa code
2. **Integration Tests sa Staging**: Patakbuhin ang integration tests sa pre-production environment
3. **Mga Baseline ng Performance**: Panatilihin ang performance benchmarks para makita ang mga regression
4. **Security Scans**: I-automate ang security testing bilang bahagi ng pipeline

### Halimbawa ng CI Pipeline (GitHub Actions)

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

## Pagsusuri para sa Pagsunod sa MCP Specification

Siguraduhing tama ang implementasyon ng iyong server sa MCP specification.

### Mga Pangunahing Lugar ng Pagsunod

1. **API Endpoints**: Subukan ang mga kinakailangang endpoints (/resources, /tools, atbp.)
2. **Request/Response Format**: Suriin ang pagsunod sa schema
3. **Error Codes**: Siguraduhing tama ang mga status code para sa iba't ibang sitwasyon
4. **Uri ng Nilalaman**: Subukan ang paghawak ng iba't ibang uri ng nilalaman
5. **Daloy ng Authentication**: Siguraduhing sumusunod ang auth mechanism sa spec

### Compliance Test Suite

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

## Nangungunang 10 Tips para sa Epektibong MCP Server Testing

1. **Subukin nang Hiwa-hiwalay ang Tool Definitions**: Suriin ang schema definitions nang independent sa logic ng tools
2. **Gumamit ng Parameterized Tests**: Subukin ang mga tool gamit ang iba't ibang input, kabilang ang mga edge case
3. **Suriin ang mga Tugon sa Error**: Siguraduhing maayos ang paghawak ng error sa lahat ng posibleng kondisyon ng error
4. **Subukan ang Authorization Logic**: Siguraduhin ang tamang access control para sa iba't ibang role ng user
5. **Subaybayan ang Test Coverage**: Sikaping mataas ang coverage sa mga critical na parte ng code
6. **Subukan ang mga Tugon sa Streaming**: Siguraduhing maayos ang paghawak ng streaming content
7. **Gamitin ang Simulasyon ng Problema sa Network**: Subukin ang ugali sa ilalim ng mahirap na kondisyon ng network
8. **Subukan ang Limitasyon ng Resource**: Siguraduhing maayos ang ugali kapag naabot ang mga quota o rate limits
9. **I-automate ang Regression Tests**: Bumuo ng suite na tatakbo sa bawat pagbabago ng code
10. **Idokumento ang mga Test Case**: Panatilihin ang malinaw na dokumentasyon ng mga test scenario

## Mga Karaniwang Pagkakamali sa Testing

- **Sobrang pagtitiwala sa happy path testing**: Siguraduhing subukan nang mabuti ang mga kaso ng error
- **Pagsasantabi sa performance testing**: Tuklasin ang mga bottleneck bago ito makaapekto sa produksyon
- **Pagsusuri lang nang hiwalay**: Pagsamahin ang unit, integration, at E2E tests
- **Hindi kumpletong API coverage**: Siguraduhing nasusubukan lahat ng endpoints at features
- **Hindi pantay na mga test environment**: Gamitin ang containers para sa consistent na test environment

## Konklusyon

Mahalaga ang komprehensibong estratehiya sa testing para makabuo ng maaasahan, mataas ang kalidad na MCP servers. Sa pagpapatupad ng mga pinakamahusay na kasanayan at mga tip na nakalista sa gabay na ito, masisiguro mong ang iyong mga implementasyon ng MCP ay tumutugon sa pinakamataas na pamantayan ng kalidad, pagiging maaasahan, at performance.


## Mahahalagang Takeaway

1. **Disenyo ng Tool**: Sundin ang prinsipyo ng single responsibility, gumamit ng dependency injection, at magdisenyo para sa composability
2. **Disenyo ng Schema**: Gumawa ng malinaw, mahusay na dokumentadong mga schema na may tamang validation constraints
3. **Paghawak ng Error**: Magpatupad ng maayos na paghawak ng error, istraktura ng error responses, at outcome-aware retry logic

4. **Performance**: Gumamit ng caching, asynchronous processing, at resource throttling
5. **Seguridad**: Magpatupad ng masusing input validation, mga pagsusuri sa authorization, at paghawak ng sensitibong datos
6. **Testing**: Gumawa ng komprehensibong unit, integration, at end-to-end tests
7. **Mga Pattern sa Workflow**: Ilapat ang mga itinatag na pattern tulad ng chains, dispatchers, at parallel processing

## Ehersisyo

Disenyuhin ang isang MCP tool at workflow para sa isang sistema ng pagproseso ng dokumento na:

1. Tumatanggap ng mga dokumento sa iba't ibang format (PDF, DOCX, TXT)
2. Nag-eextract ng teksto at mga mahahalagang impormasyon mula sa mga dokumento
3. Nagsusuri ng mga dokumento ayon sa uri at nilalaman
4. Gumagawa ng buod ng bawat dokumento

Ipatupad ang mga schema ng tool, paghawak ng error, at isang workflow pattern na pinakaangkop sa senaryong ito. Isipin kung paano mo susubukan ang implementasyon na ito.

## Mga Resource 

1. Sumali sa komunidad ng MCP sa [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) para manatiling updated sa mga pinakabagong pag-unlad 
2. Mag-ambag sa open-source na [MCP projects](https://github.com/modelcontextprotocol)
3. Ilapat ang mga prinsipyo ng MCP sa mga inisyatiba ng AI sa iyong sariling organisasyon
4. Tuklasin ang mga espesyalisadong implementasyon ng MCP para sa iyong industriya. 
5. Isaalang-alang ang pagkuha ng mga advanced na kurso sa partikular na paksa ng MCP, tulad ng multi-modal integration o enterprise application integration.
6. Subukan ang paggawa ng sarili mong mga MCP tool at workflow gamit ang mga prinsipyong natutunan sa pamamagitan ng [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Ano ang Susunod

Susunod: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
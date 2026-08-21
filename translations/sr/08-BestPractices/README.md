# Најбоље праксе развоја MCP-а

[![Најбоље праксе развоја MCP-а](../../../translated_images/sr/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Кликните на слику изнад да бисте прегледали видео о овој лекцији)_

## Преглед

Ова лекција се фокусира на напредне најбоље праксе за развој, тестирање и имплементацију MCP сервера и функција у продукцијским окружењима. Како екосистеми MCP-а расту у сложености и значају, придржавање устаљених образаца осигурава поузданост, одрживост и међусобну сарадњу. Ова лекција консолидује практичну мудрост стечену из стварних MCP имплементација како би вам помогла у стварању робусних и ефикасних сервера са функционалним ресурсима, упутствима и алатима.

## Циљеви учења

До краја ове лекције моћи ћете:

- Применити индустријске најбоље праксе у дизајну MCP сервера и функција
- Креирати свеобухватне стратегије тестирања MCP сервера
- Дизајнирати ефикасне, поново употребљиве шаблоне радних токова за сложене MCP апликације
- Имплементирати исправно руковање грешкама, евиденцију и посматрање у MCP серверима
- Оптимизовати MCP имплементације за перформансе, безбедност и одрживост

## Основни принципи MCP-а

Пре него што уђемо у конкретне праксе имплементације, важно је разумети основне принципе који усмеравају ефикасан развој MCP-а:

1. **Стандардизована комуникација**: MCP користи JSON-RPC 2.0 као основ, пружајући доследан формат за захтеве, одговоре и руковање грешкама у свим имплементацијама.

2. **Дизајн усмерен на корисника**: Увек стављајте приоритет на сагласност, контролу и транспарентност корисника у вашим MCP имплементацијама.

3. **Безбедност на првом месту**: Имплементирајте робусне мере безбедности укључујући аутентификацију, ауторизацију, валидацију и ограничење брзине.

4. **Модуларна архитектура**: Дизајнирајте ваше MCP сервере са модуларним приступом, где сваки алат и ресурс имају јасну, фокусирану сврху.

5. **Јасан стате**: MCP `2026-07-28` је без стања на протоколском нивоу.
   Када радни ток захтева стање између позива, користите јасне хендле-ове или
   обичне аргументе алата подржане трајним стањем апликације.

## Званичне најбоље праксе MCP-а

Следеће најбоље праксе потичу из званичне документације Model Context Protocol-а:

### Најбоље праксе безбедности

1. **Сагласност и контрола корисника**: Увек захтевајте изричиту сагласност корисника пре приступа подацима или извођења операција. Обезбедите јасну контролу о томе који подаци се деле и које акције су ауторизоване.

2. **Приватност података**: Излажите корисничке податке само уз изричиту сагласност и заштитите их одговарајућим контролама приступа. Заштитите од неовлашћеног преноса података.

3. **Безбедност алата**: Захтевајте изричиту сагласност корисника пре позива било ког алата. Обезбедите да корисници разумеју функционалност сваког алата и спроводите робусне безбедносне границе.

4. **Контрола дозвола алата**: Конфигуришите које алате модел може користити за
   сваки захтев и контекст ауторизације, осигуравајући да су приступачни само
   изричито ауторизовани алати.

5. **Аутентификација**: Захтевајте исправну аутентификацију пре него што омогућите приступ алатима, ресурсима или осетљивим операцијама користећи API кључеве, OAuth токене или друге безбедне методе аутентификације.

6. **Валидација параметара**: Спроводите валидацију за све позиве алата како бисте спречили да неважећи или злонамерни улаз стигне до имплементације алата.

7. **Ограничење брзине (Rate limiting)**: Имплементирајте ограничење брзине како бисте спречили злоупотребу и обезбедили фер коришћење ресурса сервера.

### Најбоље праксе имплементације

1. **Неговање капацитета**: Неговати подржане верзије протокола и
   капацитете. У MCP `2026-07-28`, сваки захтев је самосталан и може
   користити `server/discover`; старије ревизије користе иницијализациони handshake.

2. **Дизајн алата**: Креирајте фокусиране алате који једну ствар раде добро, уместо монолитних алата који се баве више различитих предмета.

3. **Руковање грешкама**: Имплементирајте стандардизоване поруке о грешкама и кодове како бисте помогли у дијагнози проблема, руковали неподношљивим ситуацијама и пружали корисне повратне информације.

4. **Посматрање (Observability)**: Користите `stderr` за дијагностику stdio и OpenTelemetry
   за структурирану посматраност. MCP функција логовања је застарела у
   спецификацији `2026-07-28`.

5. **Праћење напретка**: За дуготрајне операције, пријављујте ажурирања напретка како бисте омогућили интерfeјсе осетљиве на корисника.

6. **Отказивање захтева**: Омогућите клијентима да откажу захтеве који су у току, а више нису потребни или трају превише дуго.

## Додатне референце

За најновије информације о најбољим праксама MCP-а, обратите се:

- [MCP Документација](https://modelcontextprotocol.io/)
- [MCP Спецификација (2026-07-28)][mcp-2026-spec]
- [Претходна MCP спецификација (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Tasks Extension][mcp-tasks-extension]
- [GitHub Репозиторијум](https://github.com/modelcontextprotocol)
- [Најбоље праксе безбедности](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Топ 10](https://microsoft.github.io/mcp-azure-security-guide/) - Безбедносни ризици и мерe за ублажавање
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Практична безбедносна обука

### Лекција о пратиоцу поузданости

Генерички петље поновног покушаја нису безбедне за алате који креирају тикете, уплате,
поруке, имплементације или друге ефекте у реалном свету. Одговор може бити изгубљен
након што се ефекат изврши.

Користите лекцију о пратиоцу поузданости,
[Безбедни поновни покушаји за MCP алате: образац пратећег програма поузданости][reliability-sidecar],
да бисте научили кључеве стабилне операције, дуплирање пријема, чврсте контролне тачке,
међусобну усаглашеност, нивое доказа и убризгавање грешака.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Практични примери имплементације

### Најбоље праксе дизајна алата

#### 1. Принцип једне одговорности

Сваки MCP алат треба да има јасну и фокусирану сврху. Уместо креирања монолитних алата који покушавају да реше више проблема, развијајте специјализоване алате који одлично обављају одређене задатке.

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

#### 2. Конзистентно руковање грешкама

Имплементирајте робусно руковање грешкама са информативним порукама и одговарајућим механизмима опоравка.

```python
# Пайтон пример са свеобухватном обрадом грешака
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Валидација параметара
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Безбедносна валидација
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Операција базе података са временским ограничењем
                async with timeout(10):  # Временско ограничење од 10 секунди
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Грешке везе могу бити пролазне
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Грешке упита су највероватније грешке клијента
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Дозволити да специфичне грешке алата прођу
            raise
        except Exception as e:
            # Општи хватач за неочекиване грешке
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Имплементација детекције СКЛ инјекције
        pass
        
    def _log_error(self, message, error):
        # Имплементација евидентирања грешака
        pass
```

#### 3. Валидација параметара

Увек темељно валидајте параметре да бисте спречили неисправан или злонамерни унос.

```javascript
// JavaScript/TypeScript пример са детаљном провером параметара
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
    // 1. Проверите присуство параметра
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Проверите типове параметара
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Проверите вредности параметара
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Проверите присуство садржаја за операцију писања
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Провера безбедности путање
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Имплементација заснована на провереним параметрима
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Имплементација провере безбедности путање
    // ...
  }
}
```

### Примери имплементације безбедности

#### 1. Аутентификација и Ауторизација

```java
// Јава пример са аутентикацијом и ауторизацијом
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Инјекција зависности
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
        // 1. Извучите контекст аутентикације
        String authToken = request.getContext().getAuthToken();
        
        // 2. Аутентификујте корисника
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Провера ауторизације за специфичну операцију
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Наставите са овлашћеном операцијом
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

#### 2. Ограничење брзине

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

## Најбоље праксе тестирања

### 1. Јединично тестирање MCP алата

Увек тестирајте ваше алате изоловано, модулирајући спољашње зависности:

```typescript
// Пример јединичног теста алата у TypeScript-у
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Направите макет услуге за временску прогнузу
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Направите алат са макет зависношћу
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Припрема
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Акција
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Потврда
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Припрема
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Акција и потврда
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Интеграционо тестирање

Тестирајте комплетан ток од клијентских захтева до одговора сервера:

```python
# Пример интеграционог теста за Пајтон
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Покрени тест сервер
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Креирај клијента
        client = McpClient("http://localhost:5000")
        
        # Тестирај откривање алата
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Тестирај извршење алата
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Потврди одговор
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Очисти након теста
        await server.stop()
```

## Оптимизација перформанси

### 1. Стратегије кеширања

Имплементирајте одговарајуће кеширање да бисте смањили латенцију и коришћење ресурса:

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

#### 2. Депенденци инжење и тестабилност

Дизајнирајте алате да примају зависности кроз инјекцију у конструктору, чинећи их тестабилним и конфигурисаним:

```java
// Јава пример са убризгавањем зависности
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Зависности убризгане кроз конструктор
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Имплементација алата
    // ...
}
```

#### 3. Композициони алати

Дизајнирајте алате који се могу саставити за прављење сложенијих радних токова:

```python
# Python пример који показује композиционе алате
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Имплементација...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Овај алат може користити резултате из алата dataFetch
    async def execute_async(self, request):
        # Имплементација...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Овај алат може користити резултате из алата dataAnalysis
    async def execute_async(self, request):
        # Имплементација...
        pass

# Ови алати могу се користити независно или као део радаског тока
```

### Најбоље праксе дизајна шеме

Шема је уговор између модела и вашег алата. Добро дизајниране шеме воде ка бољој употребљивости алата.

#### 1. Јасни описи параметара

Увек укључујте описне информације за сваки параметар:

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

#### 2. Ограничења валидације

Укључите ограничења валидације да спречите неважеће уносе:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Емаил својство са валидацијом формата
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Старосно својство са нумеричким ограничењима
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Набројано својство
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

#### 3. Конзистентне структуре повратка

Одржавајте конзистентност у структурама одговора како бисте олакшали моделима интерпретацију резултата:

```python
async def execute_async(self, request):
    try:
        # Обради захтев
        results = await self._search_database(request.parameters["query"])
        
        # Увек врати конзистентну структуру
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

### Руковање грешкама

Робусно руковање грешкама је кључно за MCP алате да би одржали поузданост.

#### 1. Нежно руковање грешкама

Руковати грешкама на одговарајућим нивоима и пружити информативне поруке:

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

#### 2. Структурирани одговори о грешкама

Вратити структуриране информације о грешкама кад год је могуће:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Имплементација
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
        
        // Поново баците друге изузетке као ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Логика поновног покушаја

Користите генеричку логику поновног покушаја само за позиве само за читање или операције чији
долазни уговор је већ идемпотентан. За ефекатне операције рок
након слања захтева је двосмислен. Усагласите ауторитетно стање и
поново употребите исти стабилан кључ операције пре поновног извршења. Погледајте
[лекцију о пратећем програму поузданости](./reliability-sidecars/README.md).

Следећа ограничена петља поновног покушаја одговара за претрагу само за читање:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # секунде
    
    while retry_count < max_retries:
        try:
            # Позовите спољни API за читање
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Експоненцијално одлагање
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Нетранзијентна грешка, не покушавај поново
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Оптимизација перформанси

#### 1. Кеширање

Имплементирајте кеширање за скупе операције:

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

#### 2. Асинхроно процесирање

Користите асинхроне програмске шаблоне за операције везане за улазно-излазне операције:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // За дуготрајне операције, одмах врати ID процеса
        String processId = UUID.randomUUID().toString();
        
        // Покрени асинхроно обраду
        CompletableFuture.runAsync(() -> {
            try {
                // Изврши дуготрајну операцију
                documentService.processDocument(documentId);
                
                // Ажурирај статус (обично би се чувао у бази података)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Врати тренутни одговор са ID процеса
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Алат за проверу статуса (компанион)
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

#### 3. Ограничење ресурса

Имплементирајте ограничење ресурса да бисте спречили преоптерећење:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Дозволи 5 захтева у секунди
            bucket_size=10        # Дозволи нагле порасте до 10 захтева
        )
    
    async def execute_async(self, request):
        # Провери да ли можемо наставити или морамо чекати
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Ако је чекање предуго
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Чекај одговарајуће време кашњења
                await asyncio.sleep(delay)
        
        # Потроши један токен и настави са захтевом
        self.rate_limiter.consume()
        
        # Позови API
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
            
            # Израчунај време до доступности следећег токена
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Додај нове токене у зависности од протеклог времена
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Најбоље праксе безбедности

#### 1. Валидација уноса

Увек темељно проверите параметре уноса:

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

#### 2. Провере ауторизације

Имплементирајте исправне провере ауторизације:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Добити контекст корисника из захтева
    UserContext user = request.getContext().getUserContext();
    
    // Проверити да ли корисник има потребна дозволе
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // За одређене ресурсе, проверити приступ том ресурсу
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Наставити са извршавањем алата
    // ...
}
```

#### 3. Руковање осетљивим подацима

Пажљиво руковати осетљивим подацима:

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
        
        # Преузми корисничке податке
        user_data = await self.user_service.get_user_data(user_id)
        
        # Филтрирај осетљива поља осим ако није изричито затражено И овлашћено
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Провери ниво овлашћења у контексту захтева
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Креирај копију да би се избегла измена оригинала
        redacted = user_data.copy()
        
        # Црвено означи одређена осетљива поља
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Црвено означи уроњене осетљиве податке
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Најбоље праксе тестирања MCP алата

Свеобухватно тестирање осигурава да MCP алати исправно раде, руковају крајњим случајевима и правилно се интегришу са осталим деловима система.

### Јединично тестирање

#### 1. Тестирајте сваки алат изоловано

Креирајте фокусиране тестове функционалности сваког алата:

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

#### 2. Тестирање валидације шеме

Тестирајте да ли су шеме важеће и правилно спроводе ограничења:

```java
@Test
public void testSchemaValidation() {
    // Креирај инстанцу алата
    SearchTool searchTool = new SearchTool();
    
    // Преузми шему
    Object schema = searchTool.getSchema();
    
    // Претвори шему у JSON за валидацију
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Валидација шеме као валидан JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Тестирај валидне параметре
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Тестирај недостатак обавезног параметра
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Тестирај неважећи тип параметра
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Тестови руковања грешкама

Креирајте специфичне тестове за услове грешака:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Поредјати
    tool = ApiTool(timeout=0.1)  # Врло кратко време чекања
    
    # Искључити захтев који ће истећи
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Дуже од времена чекања
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Изврши и потврди
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Потврди поруку искључка
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Поредјати
    tool = ApiTool()
    
    # Искључити одговор са ограничењем броја захтева
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
        
        # Изврши и потврди
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Потврди да искључак садржи информације о ограничењу броја захтева
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Интеграционо тестирање

#### 1. Тестирање ланца алата

Тестирајте заједнички рад алата у очекиваним комбинацијама:

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

#### 2. Тестирање MCP сервера

Тестирајте MCP сервер са пуном регистрацијом алата и извршењем:

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
        // Тестирајте откривајућу тачку
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Креирајте захтев за алат
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Пошаљите захтев и проверите одговор
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Креирајте неважећи захтев за алат
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Недостаје параметар "b"
        request.put("parameters", parameters);
        
        // Пошаљите захтев и проверите одговор са грешком
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Крај-до-крај тестирање

Тестирајте комплетне радне токове од упита модела до извршења алата:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Подесите - Подесите MCP клијента и модел макете
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Одговори модела макете
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
    
    # Одговор алата за временске услове из макете
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
        
        # Делујте
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Потврдите
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Тестирање перформанси

#### 1. Тестирање оптерећења

Тестирајте колико истовремених захтева ваш MCP сервер може да обради:

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

#### 2. Тестирање стреса

Тестирајте систем под екстремним оптерећењем:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Подесите ЈМетер за тестирање оптерећења
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Конфигуришите ЈМетер тест план
    HashTree testPlanTree = new HashTree();
    
    // Креирајте тест план, групу нити, примерке итд.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Додајте HTTP примерке за извршавање алата
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Додајте слушаоце
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Покрените тест
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Потврдите резултате
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Просечно време одговора < 200мс
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90. перцентил < 500мс
}
```

#### 3. Мониторинг и профилисање

Подесите праћење за дугорочну анализу перформанси:

```python
# Конфигуриши надзор за MCP сервер
def configure_monitoring(server):
    # Подеси Prometheus метрике
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
    
    # Додај посреднички програм за мерење времена и снимање метрика
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Објави крајњу тачку за метрике
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Обрасци дизајна радних токова MCP-а

Добро дизајнирани MCP радни токови побољшавају ефикасност, поузданост и одрживост. Ево кључних образаца које треба пратити:

### 1. Образац ланца алата

Повежите више алата у низу где излаз једног алата постаје улаз за следећи:

```python
# Имплементација Пайтон ланца алата
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Листа имена алата за извршавање узастопно
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Изврши сваки алат у ланцу, прослеђујући претходни резултат
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Сачувај резултат и користи га као улаз за следећи алат
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Пример коришћења
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

### 2. Образац диспатчера

Користите централни алат који дистрибуира задатке специјализованим алатима на основу улаза:

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

### 3. Образац паралелне обраде

Извршите више алата истовремено ради ефикасности:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Корак 1: Преузми метаподатке скупa података (синхроно)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Корак 2: Покрени више анализа паралелно
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
        
        // Чекај да се све паралелне задатке заврше
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Чекај на завршетак
        
        // Корак 3: Комбинуј резултате
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Корак 4: Генериши резиме извештај
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Врати комплетан резултат тока рада
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Образац опоравка од грешака

Имплементирајте нежне алтернативе када алати не успеју:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Прво покушајте са примарним алатом
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Забележите неуспех
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Прелазак на секундарни алат
            try:
                # Можда ће бити потребно трансформисати параметре за алат за прелазак
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Оба алата нису успела
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ова имплементација би зависила од специфичних алата
        # За овај пример, вратићемо само оригиналне параметре
        return params

# Пример коришћења
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Примарни (плаћени) временски API
        "basicWeatherService",    # Резервни (бесплатни) временски API
        {"location": location}
    )
```

### 5. Образац композиције радног тока

Креирајте сложене радне токове композицјом једноставнијих:

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

# Тестирање MCP сервера: најбоље праксе и главни савети

## Преглед

Тестирање је критичан аспект развоја поузданих и квалитетних MCP сервера. Овај водич пружа свеобухватне најбоље праксе и савете за тестирање ваших MCP сервера током целог животног циклуса развоја, од јединичних тестова до интеграционих тестова и валидације крај-до-крај.

## Зашто је тестирање важно за MCP сервере

MCP сервери служе као критичан посредник између AI модела и клијентских апликација. Темљно тестирање осигурава:

- Поузданост у продукцијским окружењима
- Тачно руковање захтевима и одговорима
- Правилну имплементацију MCP спецификација
- Отпорност на грешке и крајње случајеве
- Доследне перформансе под разним оптерећењима

## Јединично тестирање за MCP сервере

### Јединично тестирање (основа)

Јединични тестови проверавају појединачне компоненте вашег MCP сервера изоловано.

#### Шта тестирати

1. **Руковаоци ресурса**: Тестирајте логике сваког руковаоца ресурса независно
2. **Имплементације алата**: Верификујте понашање алата са разним улазима
3. **Шаблони упита (Prompt Templates)**: Осигурајте да се шаблони исправно приказују
4. **Валидација шеме**: Тестирајте логику валидације параметара
5. **Руковање грешкама**: Проверите одговоре са грешкама за неважеће уносе

#### Најбоље праксе за јединично тестирање

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
# Пример јединичног теста за алат за калкулатор у Пајтону
def test_calculator_tool_add():
    # Припрема
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Акција
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Потврда
    assert result["value"] == 12
```

### Интеграционо тестирање (средњи слој)

Интеграциони тестови проверавају интеракције између компоненти вашег MCP сервера.

#### Шта тестирати

1. **Иницијализација сервера**: Тестирајте покретање сервера са разним конфигурацијама
2. **Регистрација рута**: Верификујте да су све крајње тачке исправно регистроване
3. **Обрада захтева**: Тестирајте комплетан циклус захтева и одговора
4. **Пропагација грешака**: Обезбедите исправно руковање грешкама кроз компоненте
5. **Аутентификација и ауторизација**: Тестирајте безбедносне механизме

#### Најбоље праксе интеграционог тестирања

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

### Крај-до-крај тестирање (врхунски слој)

Крај-до-крај тестови проверавају комплетно понашање система од клијента до сервера.

#### Шта тестирати

1. **Комуникација клијент-сервер**: Тестирајте комплетне циклусе захтева и одговора
2. **Прави клијентски SDK-ови**: Тестирајте са стварним имплементацијама клијента
3. **Перформансе под оптерећењем**: Верификујте понашање при више истовремених захтева
4. **Опоравак од грешака**: Тестирајте опоравак система од неуспеха

5. **Дуготрајне операције**: Верификујте руковање стримингом и дугим операцијама

#### Најбоље праксе за крајње-текст (E2E) тестирање

```typescript
// Пример E2E теста са клијентом у TypeScript-у
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Покрени сервер у тест окружењу
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Акција
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Потврда
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Стратегије имитације (mock) за MCP тестирање

Имитација је суштинска за изолацију компонената током тестирања.

### Компоненте које треба имитирати

1. **Спољни AI модели**: Имитирајте одговоре модела за предвидљиво тестирање
2. **Спољне услуге**: Имитирајте API зависности (базе података, услуге трећих страна)
3. **Услуге аутентификације**: Имитирајте провајдере идентитета
4. **Провајдери ресурса**: Имитирајте скупе хендлере ресурса

### Пример: Имитирање одговора AI модела

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
# Питхон пример са unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Конфигуришите мок
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Користите мок у тесту
    server = McpServer(model_client=mock_model)
    # Наставите са тестом
```

## Тестирање перформанси

Тестирање перформанси је кључно за продукцијске MCP сервере.

### Шта мерити

1. **Задржаност (латенција)**: Време одговора за захтеве
2. **Пропусност**: Захтеви обрађени у секунди
3. **Коришћење ресурса**: CPU, меморија, коришћење мреже
4. **Руковање конкурентношћу**: Понашање при паралелним захтевима
5. **Карактеристике скалирања**: Перформансе како се оптерећење повећава

### Алати за тестирање перформанси

- **k6**: Отворени алат за тестирање оптерећења
- **JMeter**: Комплексно тестирање перформанси
- **Locust**: Python засновано тестирање оптерећења
- **Azure Load Testing**: Облак засновано тестирање перформанси

### Пример: Основни тест оптерећења са k6

```javascript
// k6 скрипт за оптерећење тестирања MCP сервера
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 виртуелних корисника
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

## Аутоматизација тестирања за MCP сервере

Аутоматизација ваших тестова обезбеђује доследан квалитет и брже повратне информације.

### Интеграција CI/CD

1. **Покретање јединичних тестова на pull захтевима**: Обезбедити да измене кода не кваре постојећу функционалност
2. **Интеграциони тестови у staging окружењу**: Покретањe интеграционих тестова у претпродукцијским окружењима
3. **Перформанса као основа**: Одржавајте перформансне референтне вредности да би открили регресије
4. **Безбедносне скенирања**: Аутоматизујте безбедносно тестирање као део pipeline-а

### Пример CI pipeline-а (GitHub Actions)

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

## Тестирање у складу са MCP спецификацијом

Верификујте да ваш сервер исправно имплементира MCP спецификацију.

### Кључна подручја за услова усклађености

1. **API крајњи поени**: Тестирајте потребне крајње тачке (/resources, /tools и сл.)
2. **Формат захтева/одговора**: Потврдите усклађеност са шемом
3. **Кодови грешака**: Верификујте исправне статус кодове за различите сценарије
4. **Типови садржаја**: Тестирајте руковање различитим типовима садржаја
5. **Аутентификациони ток**: Провера механизама аутентификације у складу са спецификацијом

### Комплет за тестирање усклађености

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

## Топ 10 савета за ефективно тестирање MCP сервера

1. **Тестирајте дефиниције алата посебно**: Верификујте шеме независно од логике алата
2. **Користите параметризоване тестове**: Тестирајте алате са разним улазима, укључујући и рубне случајеве
3. **Проверите одговоре на грешке**: Верификујте правилно руковођење грешкама за све могуће услове
4. **Тестирајте логику ауторизације**: Обезбедите исправну контролу приступа за различите корисничке улоге
5. **Пратите обухват тестова**: Тежите високом обухвату кода критичних путева
6. **Тестирајте стриминг одговоре**: Верификујте исправно руковање стриминг садржајем
7. **Симулирајте мрежне проблеме**: Тестирајте понашање у условима лоше мреже
8. **Тестирајте лимите ресурса**: Верификујте понашање при достигању квота или ограничења брзине
9. **Аутоматизујте регресионе тестове**: Направите сет који се покреће при свакој промени кода
10. **Документујте тест случајеве**: Одржавајте јасну документацију тест сценарија

## Уобичајене замке у тестирању

- **Превелика ослањања на тестирање срећног пута**: Обавезно темељно тестирајте случајеве грешака
- **Игнорисање тестирања перформанси**: Идентификујте грла пре него што утичу на продукцију
- **Тестирање само у изолацији**: Комбинујте јединичне, интеграционе и E2E тестове
- **Непотпун обухват API**: Обезбедите да су сви крајњи поени и функције тестирани
- **Неконсистентна тест окружења**: Користите контејнере за доследна тест окружења

## Закључак

Комплексна стратегија тестирања је неопходна за развој поузданих, квалитетних MCP сервера. Имплементирањем најбољих пракси и савета из овог водича, можете осигурати да ваше MCP имплементације испуне највише стандарде квалитета, поузданости и перформанси.


## Кључни закључци

1. **Дизајн алата**: Пратите принцип једне одговорности, користите dependency injection и дизајнирајте за композицију
2. **Дизајн шеме**: Креирајте јасне, добро документоване шеме са правилним валидирајућим ограничењима
3. **Руковање грешкама**: Имплементирајте благовремено руковођење грешкама, структуиране одговоре на грешке и логику поновног покушаја свесну исхода

4. **Перформансе**: Користите кеширање, асинхрону обраду и контролу ресурса
5. **Безбедност**: Примените темељну валидацију улаза, провере ауторизације и руковање осетљивим подацима
6. **Тестирање**: Креирајте обимне јединичне, интеграционе и крајње-текст тестове
7. **Обрасци радних токова**: Примените успостављене обрасце као што су ланци, dispatcher-и и паралелна обрада

## Вежба

Осмислите MCP алат и радни ток за систем обраде докумената који:

1. Прихвата документе у више формата (PDF, DOCX, TXT)
2. Извлачи текст и кључне информације из докумената
3. Класификује документе по типу и садржају
4. Генерише резиме за сваки документ

Имплементирајте шеме алата, руковање грешкама и образац радног тока који најбоље одговара овом сценарију. Размислите како бисте тестирали ову имплементацију.

## Ресурси 

1. Придружите се MCP заједници на [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) да бисте били у току са најновијим развојем 
2. Доприносите open-source [MCP пројектима](https://github.com/modelcontextprotocol)
3. Примењујте MCP принципе у AI иницијативама ваше организације
4. Истражите специјализоване MCP имплементације за вашу индустрију. 
5. Размотрите похађање напредних курсева о појединим MCP темама, као што су мулти-модална интеграција или интеграција корпоративних апликација.
6. Експериментишите са изградњом сопствених MCP алата и радних токова користећи принципе научене у [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Шта следи

Следеће: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
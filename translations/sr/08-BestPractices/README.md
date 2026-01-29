# MCP Најбоље Праксе Развоја

[![MCP Најбоље Праксе Развоја](../../../translated_images/sr/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(Кликните на слику изнад да бисте погледали видео лекцију)_

## Преглед

Ова лекција се фокусира на напредне најбоље праксе за развој, тестирање и примену MCP сервера и функција у продукционим окружењима. Како MCP екосистеми постају све сложенији и значајнији, праћење утврђених образаца осигурава поузданост, одрживост и интероперабилност. Ова лекција обједињује практична искуства стечена из реалних MCP имплементација како би вас водила у креирању робусних, ефикасних сервера са ефективним ресурсима, упутствима и алатима.

## Циљеви учења

На крају ове лекције, бићете у могућности да:

- Примените најбоље праксе из индустрије у дизајну MCP сервера и функција
- Креирате свеобухватне стратегије тестирања за MCP сервере
- Дизајнирате ефикасне, поново употребљиве обрасце рада за сложене MCP апликације
- Имплементирате правилно руковање грешкама, логовање и посматрање у MCP серверима
- Оптимизујете MCP имплементације за перформансе, безбедност и одрживост

## Основни MCP Принципи

Пре него што се упустимо у специфичне праксе имплементације, важно је разумети основне принципе који воде ефикасан MCP развој:

1. **Стандардизована комуникација**: MCP користи JSON-RPC 2.0 као основу, пружајући конзистентан формат за захтеве, одговоре и руковање грешкама у свим имплементацијама.

2. **Кориснички оријентисан дизајн**: Увек дајте приоритет пристанку корисника, контроли и транспарентности у вашим MCP имплементацијама.

3. **Безбедност на првом месту**: Имплементирајте робусне мере безбедности, укључујући аутентификацију, ауторизацију, валидацију и ограничење брзине.

4. **Модуларна архитектура**: Дизајнирајте MCP сервере са модуларним приступом, где сваки алат и ресурс имају јасну, фокусирану сврху.

5. **Стање везе**: Искористите могућност MCP-а да одржава стање кроз више захтева за кохерентније и свесније интеракције.

## Званичне MCP Најбоље Праксе

Следеће најбоље праксе су изведене из званичне документације Model Context Protocol-а:

### Најбоље Праксе Безбедности

1. **Пристанак и контрола корисника**: Увек захтевајте експлицитан пристанак корисника пре приступања подацима или извршавања операција. Обезбедите јасну контролу над тим који подаци се деле и које акције су овлашћене.

2. **Приватност података**: Излажите корисничке податке само уз експлицитан пристанак и заштитите их одговарајућим контролама приступа. Осигурајте се од неовлашћеног преноса података.

3. **Безбедност алата**: Захтевајте експлицитан пристанак корисника пре позивања било ког алата. Осигурајте да корисници разумеју функционалност сваког алата и примените робусне безбедносне границе.

4. **Контрола дозвола алата**: Конфигуришите који алати су моделу доступни током сесије, осигуравајући да су доступни само експлицитно овлашћени алати.

5. **Аутентификација**: Захтевајте правилну аутентификацију пре него што одобрите приступ алатима, ресурсима или осетљивим операцијама користећи API кључеве, OAuth токене или друге сигурне методе аутентификације.

6. **Валидација параметара**: Примените валидацију за све позиве алата како бисте спречили да неисправан или злонамеран унос дође до имплементације алата.

7. **Ограничење брзине**: Имплементирајте ограничење брзине како бисте спречили злоупотребу и осигурали праведно коришћење серверских ресурса.

### Најбоље Праксе Имплементације

1. **Преговарање о могућностима**: Током успостављања везе, размените информације о подржаним функцијама, верзијама протокола, доступним алатима и ресурсима.

2. **Дизајн алата**: Креирајте фокусиране алате који добро обављају један задатак, уместо монолитних алата који се баве више аспеката.

3. **Руковање грешкама**: Имплементирајте стандардизоване поруке о грешкама и кодове како бисте помогли у дијагностици проблема, руковали неуспесима на елегантан начин и пружили корисне повратне информације.

4. **Логовање**: Конфигуришите структуиране логове за ревизију, отклањање грешака и праћење интеракција протокола.

5. **Праћење напретка**: За дуготрајне операције, пријављујте ажурирања напретка како бисте омогућили одзивна корисничка сучеља.

6. **Отказивање захтева**: Омогућите клијентима да откажу захтеве који су у току, а који више нису потребни или трају предуго.

## Додатне Референце

За најновије информације о MCP најбољим праксама, погледајте:

- [MCP Документација](https://modelcontextprotocol.io/)
- [MCP Спецификација](https://spec.modelcontextprotocol.io/)
- [GitHub Репозиторијум](https://github.com/modelcontextprotocol)
- [Најбоље Праксе Безбедности](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## Практични Примери Имплементације

### Најбоље Праксе Дизајна Алатa

#### 1. Принцип Једне Одговорности

Сваки MCP алат треба да има јасну, фокусирану сврху. Уместо креирања монолитних алата који покушавају да обрађују више аспеката, развијте специјализоване алате који се истичу у специфичним задацима.

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

#### 2. Конзистентно Руковање Грешкама

Имплементирајте робусно руковање грешкама са информативним порукама о грешкама и одговарајућим механизмима за опоравак.

```python
# Python example with comprehensive error handling
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Parameter validation
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Security validation
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Database operation with timeout
                async with timeout(10):  # 10 second timeout
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Connection errors might be transient
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Query errors are likely client errors
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Let tool-specific errors pass through
            raise
        except Exception as e:
            # Catch-all for unexpected errors
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementation of SQL injection detection
        pass
        
    def _log_error(self, message, error):
        # Implementation of error logging
        pass
```

#### 3. Валидација Параметара

Увек темељно валидирајте параметре како бисте спречили неисправан или злонамеран унос.

```javascript
// JavaScript/TypeScript example with detailed parameter validation
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
    // 1. Validate parameter presence
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Validate parameter types
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Validate parameter values
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Validate content presence for write operation
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Path safety validation
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementation based on validated parameters
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementation of path safety check
    // ...
  }
}
```

### Примери Имплементације Безбедности

#### 1. Аутентификација и Ауторизација

```java
// Java example with authentication and authorization
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Dependency injection
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
        // 1. Extract authentication context
        String authToken = request.getContext().getAuthToken();
        
        // 2. Authenticate user
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Check authorization for the specific operation
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Proceed with authorized operation
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

#### 2. Ограничење Брзине

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

## Најбоље Праксе Тестирања

### 1. Јединично Тестирање MCP Алатa

Увек тестирајте своје алате изоловано, симулирајући спољашње зависности:

```typescript
// TypeScript example of a tool unit test
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Create a mock weather service
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Create the tool with the mock dependency
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Arrange
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Act
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Assert
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Arrange
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Act & Assert
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Интеграционо Тестирање

Тестирајте комплетан ток од клијентских захтева до серверских одговора:

```python
# Python integration test example
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Start a test server
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Create a client
        client = McpClient("http://localhost:5000")
        
        # Test tool discovery
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Test tool execution
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verify response
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Clean up
        await server.stop()
```

## Оптимизација Перформанси

### 1. Стратегије Кеширања

Имплементирајте одговарајуће кеширање како бисте смањили кашњење и употребу ресурса:

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

#### 2. Убризгавање Зависности и Тестабилност

Дизајнирајте алате тако да примају своје зависности кроз убризгавање конструктора, чинећи их тестабилним и конфигурабилним:

```java
// Java example with dependency injection
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Dependencies injected through constructor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Tool implementation
    // ...
}
```

#### 3. Компоновани Алат

Дизајнирајте алате који могу бити компоновани заједно како би креирали сложеније токове рада:

```python
# Python example showing composable tools
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementation...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # This tool can use results from the dataFetch tool
    async def execute_async(self, request):
        # Implementation...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # This tool can use results from the dataAnalysis tool
    async def execute_async(self, request):
        # Implementation...
        pass

# These tools can be used independently or as part of a workflow
```

### Најбоље Праксе Дизајна Шема

Шема је уговор између модела и вашег алата. Добро дизајниране шеме воде до боље употребљивости алата.

#### 1. Јасни Опис Параметара

Увек укључите описне информације за сваки параметар:

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

#### 2. Ограничења Валидације

Укључите ограничења валидације како бисте спречили неважеће уносе:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Email property with format validation
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Age property with numeric constraints
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Enumerated property
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

#### 3. Конзистентне Структуре Повратних Одговора

Одржавајте конзистентност у структурама одговора како би моделима било лакше да интерпретирају резултате:

```python
async def execute_async(self, request):
    try:
        # Process request
        results = await self._search_database(request.parameters["query"])
        
        # Always return a consistent structure
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

### Руковање Грешкама

Робусно руковање грешкама је кључно за MCP алате како би одржали поузданост.

#### 1. Елегантно Руковање Грешкама

Руковање грешкама на одговарајућим нивоима и пружање информативних порука:

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

#### 2. Структурисани Одговори на Грешке

Враћајте структурисане информације о грешкама кад год је могуће:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementation
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
        
        // Re-throw other exceptions as ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Логика Поновног Покушаја

Имплементирајте одговарајућу логику поновног покушаја за привремене неуспехе:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # seconds
    
    while retry_count < max_retries:
        try:
            # Call external API
            return await self._call_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Exponential backoff
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Non-transient error, don't retry
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

...
3. **Основне перформанс метрике**: Одржавајте референтне вредности перформанси како бисте открили регресије  
4. **Безбедносно скенирање**: Аутоматизујте тестирање безбедности као део процеса  

### Пример CI Пипелина (GitHub Actions)

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

## Тестирање усклађености са MCP спецификацијом  

Проверите да ли ваш сервер правилно имплементира MCP спецификацију.  

### Кључне области усклађености  

1. **API Ендпоинти**: Тестирајте обавезне ендпоинте (/resources, /tools, итд.)  
2. **Формат захтева/одговора**: Потврдите усклађеност са шемом  
3. **Кодови грешака**: Проверите исправне статус кодове за различите сценарије  
4. **Типови садржаја**: Тестирајте руковање различитим типовима садржаја  
5. **Аутентификациони ток**: Проверите механизме аутентификације у складу са спецификацијом  

### Тестни пакет за усклађеност  

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

## Топ 10 савета за ефикасно тестирање MCP сервера  

1. **Одвојено тестирајте дефиниције алата**: Проверите дефиниције шема независно од логике алата  
2. **Користите параметризоване тестове**: Тестирајте алате са различитим улазима, укључујући граничне случајеве  
3. **Проверите одговоре на грешке**: Потврдите правилно руковање свим могућим условима грешке  
4. **Тестирајте логику ауторизације**: Осигурајте правилну контролу приступа за различите корисничке улоге  
5. **Пратите покривеност тестова**: Тежите високој покривености критичног кода  
6. **Тестирајте стриминг одговоре**: Проверите правилно руковање стриминг садржајем  
7. **Симулирајте проблеме са мрежом**: Тестирајте понашање у условима лоше мрежне конекције  
8. **Тестирајте ограничења ресурса**: Проверите понашање при достизању квота или ограничења брзине  
9. **Аутоматизујте регресионе тестове**: Направите пакет који се покреће при свакој промени кода  
10. **Документујте тест случајеве**: Одржавајте јасну документацију тест сценарија  

## Уобичајене грешке у тестирању  

- **Прекомерно ослањање на тестирање "срећног пута"**: Осигурајте да темељно тестирате случајеве грешке  
- **Игнорисање тестирања перформанси**: Идентификујте уска грла пре него што утичу на продукцију  
- **Тестирање само у изолацији**: Комбинујте јединичне, интеграционе и E2E тестове  
- **Непотпуна покривеност API-ја**: Осигурајте да су сви ендпоинти и функције тестирани  
- **Неконзистентна тестна окружења**: Користите контејнере за осигурање конзистентних тестних окружења  

## Закључак  

Свеобухватна стратегија тестирања је од суштинског значаја за развој поузданих, висококвалитетних MCP сервера. Применом најбољих пракси и савета из овог водича, можете осигурати да ваше MCP имплементације испуњавају највише стандарде квалитета, поузданости и перформанси.  

## Кључни закључци  

1. **Дизајн алата**: Примените принцип једне одговорности, користите убризгавање зависности и дизајнирајте за композабилност  
2. **Дизајн шема**: Направите јасне, добро документоване шеме са одговарајућим ограничењима валидације  
3. **Руковање грешкама**: Имплементирајте елегантно руковање грешкама, структурисане одговоре на грешке и логику поновног покушаја  
4. **Перформансе**: Користите кеширање, асинхрону обраду и ограничење ресурса  
5. **Безбедност**: Примените темељну валидацију уноса, провере ауторизације и руковање осетљивим подацима  
6. **Тестирање**: Направите свеобухватне јединичне, интеграционе и крајње тестове  
7. **Шаблони радних токова**: Примените утврђене шаблоне као што су ланци, диспечери и паралелна обрада  

## Вежба  

Дизајнирајте MCP алат и радни ток за систем за обраду докумената који:  

1. Прихвата документе у више формата (PDF, DOCX, TXT)  
2. Екстрахује текст и кључне информације из докумената  
3. Класификује документе по типу и садржају  
4. Генерише резиме сваког документа  

Имплементирајте шеме алата, руковање грешкама и шаблон радног тока који најбоље одговара овом сценарију. Размислите како бисте тестирали ову имплементацију.  

## Ресурси  

1. Придружите се MCP заједници на [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) како бисте били у току са најновијим дешавањима  
2. Допринесите отвореним [MCP пројектима](https://github.com/modelcontextprotocol)  
3. Примените MCP принципе у иницијативама ваше организације за AI  
4. Истражите специјализоване MCP имплементације за вашу индустрију  
5. Размотрите похађање напредних курсева о специфичним MCP темама, као што су мултимодална интеграција или интеграција у предузећима  
6. Експериментишите са креирањем сопствених MCP алата и радних токова користећи принципе научене кроз [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

Следеће: Најбоље праксе [студије случаја](../09-CaseStudy/README.md)  

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.
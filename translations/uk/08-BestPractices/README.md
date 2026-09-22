# Найкращі практики розробки MCP

[![Найкращі практики розробки MCP](../../../translated_images/uk/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Натисніть на зображення вище, щоб переглянути відеоурок)_

## Огляд

Цей урок зосереджений на розширених найкращих практиках розробки, тестування та розгортання серверів та функцій MCP у виробничих середовищах. Оскільки екосистеми MCP зростають у складності та важливості, слідування встановленим паттернам забезпечує надійність, підтримуваність та взаємодію. Цей урок консолідує практичну мудрість, отриману з реальних впроваджень MCP, щоб допомогти вам створювати надійні, ефективні сервери з ефективними ресурсами, запитами та інструментами.

## Цілі навчання

До кінця цього уроку ви зможете:

- Застосовувати галузеві найкращі практики у проєктуванні серверів та функцій MCP
- Створювати комплексні стратегії тестування серверів MCP
- Проєктувати ефективні, повторно використовувані патерни робочих процесів для складних MCP-додатків
- Реалізовувати належну обробку помилок, логування та спостережуваність у серверах MCP
- Оптимізувати впровадження MCP для продуктивності, безпеки та підтримуваності

## Основні принципи MCP

Перед тим як зануритись у конкретні практики впровадження, важливо зрозуміти основні принципи, які керують ефективною розробкою MCP:

1. **Стандартизована комунікація**: MCP використовує JSON-RPC 2.0 як основу, забезпечуючи послідовний формат для запитів, відповідей та обробки помилок у всіх реалізаціях.

2. **Орієнтація на користувача**: Завжди надавайте пріоритет згоді, контролю і прозорості користувача у ваших реалізаціях MCP.

3. **Безпека на першому місці**: Впроваджуйте надійні заходи безпеки, включаючи аутентифікацію, авторизацію, валідацію та обмеження швидкості.

4. **Модульна архітектура**: Проєктуйте сервери MCP з модульним підходом, де кожен інструмент і ресурс має чітку, сфокусовану мету.

5. **Явний стан**: MCP `2026-07-28` є безстанним на рівні протоколу.
   Коли робочому процесу потрібен стан між викликами, використовуйте явні дескриптори або
   звичайні аргументи інструментів, підкріплені довготривалим станом додатку.

## Офіційні найкращі практики MCP

Наступні найкращі практики походять з офіційної документації Model Context Protocol:

### Найкращі практики безпеки

1. **Згода та контроль користувача**: Завжди вимагайте явну згоду користувача перед доступом до даних або виконанням операцій. Надавайте чіткий контроль над тим, які дані передаються і які дії авторизовані.

2. **Конфіденційність даних**: Поширюйте користувацькі дані лише за явної згоди та захищайте їх відповідними контролями доступу. Захищайте від несанкціонованої передачі даних.

3. **Безпека інструментів**: Вимагайте явної згоди користувача перед викликом будь-якого інструменту. Забезпечуйте розуміння користувачем функціональності кожного інструменту та впроваджуйте надійні межі безпеки.

4. **Контроль дозволів інструментів**: Налаштовуйте, які інструменти модель може використовувати для
   кожного запиту та контексту авторизації, гарантуйте доступ тільки до явно авторизованих
   інструментів.

5. **Аутентифікація**: Вимагайте належну аутентифікацію перед наданням доступу до інструментів, ресурсів або конфіденційних операцій, використовуючи API-ключі, OAuth-токени чи інші безпечні методи аутентифікації.

6. **Валідація параметрів**: Забезпечуйте валідацію всіх викликів інструментів, щоб запобігти надходженню до реалізації інструментів неправильних чи шкідливих вхідних даних.

7. **Обмеження швидкості**: Впроваджуйте обмеження швидкості для запобігання зловживанням та забезпечення справедливого використання ресурсів сервера.

### Найкращі практики впровадження

1. **Переговори можливостей**: Узгоджуйте підтримувані версії протоколу та
   можливості. У MCP `2026-07-28` кожен запит є самодостатнім і може
   використовувати `server/discover`; старіші версії використовують ініціалізаційне рукостискання.

2. **Проєктування інструментів**: Створюйте сфокусовані інструменти, які роблять одну річ добре, а не монолітні інструменти, що охоплюють кілька аспектів.

3. **Обробка помилок**: Впроваджуйте стандартизовані повідомлення про помилки та коди, щоб допомогти діагностувати проблеми, коректно обробляти збої та забезпечувати практичний зворотний зв’язок.

4. **Спостережуваність**: Використовуйте `stderr` для діагностики stdio та OpenTelemetry
   для структурованої спостережуваності. Функція логування MCP застаріла в
   специфікації `2026-07-28`.

5. **Відстеження прогресу**: Для тривалих операцій повідомляйте про оновлення прогресу для забезпечення чутливих інтерфейсів користувача.

6. **Скасування запитів**: Дозволяйте клієнтам скасовувати запити, що виконуються, якщо вони вже не потрібні або займають занадто багато часу.

## Додаткові посилання

Для отримання найактуальнішої інформації щодо найкращих практик MCP звертайтеся до:

- [Документація MCP](https://modelcontextprotocol.io/)
- [Специфікація MCP (2026-07-28)][mcp-2026-spec]
- [Попередня специфікація MCP (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Розширення завдань MCP][mcp-tasks-extension]
- [Репозиторій GitHub](https://github.com/modelcontextprotocol)
- [Найкращі практики безпеки](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Ризики безпеки та заходи захисту
- [Майстер-клас MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Практичне навчання з безпеки

### Урок про надійність-партнер

Загальні цикли повторних спроб небезпечні для інструментів, що створюють тікети, платежі,
повідомлення, розгортання чи інші операції з реальними ефектами. Відповідь може бути втрачена
після того, як ефект вже зафіксований.

Використовуйте урок-партнер з надійності,
[Безпечні повторні спроби для інструментів MCP: патерн Reliability Sidecar][reliability-sidecar],
щоб навчитися стабільним ключам операцій, дублікатам, чекпоінтам,
врегулюванню, рівням доказів і введенню збоїв.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Практичні приклади впровадження

### Найкращі практики проєктування інструментів

#### 1. Принцип єдиної відповідальності

Кожен інструмент MCP повинен мати чітку, сфокусовану мету. Замість створення монолітних інструментів, які намагаються охопити декілька питань, розробляйте спеціалізовані інструменти, які відмінно виконують певні завдання.

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

#### 2. Послідовна обробка помилок

Впроваджуйте надійну обробку помилок з інформативними повідомленнями про помилки та належними механізмами відновлення.

```python
# Приклад на Python з комплексною обробкою помилок
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Перевірка параметрів
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Перевірка безпеки
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Операція з базою даних із тайм-аутом
                async with timeout(10):  # Тайм-аут 10 секунд
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Помилки з’єднання можуть бути тимчасовими
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Помилки запиту, ймовірно, помилки клієнта
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Дозволити проходження помилок, специфічних для інструменту
            raise
        except Exception as e:
            # Захоплення усіх непередбачених помилок
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Реалізація виявлення SQL-ін’єкцій
        pass
        
    def _log_error(self, message, error):
        # Реалізація журналювання помилок
        pass
```

#### 3. Валідація параметрів

Завжди ретельно перевіряйте параметри, щоб уникнути некоректного або шкідливого вводу.

```javascript
// Приклад JavaScript/TypeScript з детальною перевіркою параметрів
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
    // 1. Перевірка наявності параметра
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Перевірка типів параметрів
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Перевірка значень параметрів
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Перевірка наявності вмісту для операції запису
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Перевірка безпеки шляху
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Реалізація на основі перевірених параметрів
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Реалізація перевірки безпеки шляху
    // ...
  }
}
```

### Приклади впровадження безпеки

#### 1. Аутентифікація та авторизація

```java
// Приклад на Java з аутентифікацією та авторизацією
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Впровадження залежностей
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
        // 1. Витягнути контекст аутентифікації
        String authToken = request.getContext().getAuthToken();
        
        // 2. Аутентифікувати користувача
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Перевірити авторизацію для конкретної операції
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Виконати операцію з авторизацією
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

#### 2. Обмеження швидкості

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

## Найкращі практики тестування

### 1. Модульне тестування інструментів MCP

Завжди тестуйте свої інструменти в ізоляції, імітуючи зовнішні залежності:

```typescript
// Приклад юніт-тесту інструмента на TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Створити мок сервіс погоди
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Створити інструмент з підмінною залежністю
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Підготовка
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Дія
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Перевірка
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Підготовка
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Дія та перевірка
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Інтеграційне тестування

Тестуйте повний цикл від запитів клієнта до відповідей сервера:

```python
# Приклад інтеграційного тесту на Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Запустити тестовий сервер
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Створити клієнта
        client = McpClient("http://localhost:5000")
        
        # Перевірити виявлення інструменту
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Перевірити виконання інструменту
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Перевірити відповідь
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Очистити ресурси
        await server.stop()
```

## Оптимізація продуктивності

### 1. Стратегії кешування

Впроваджуйте відповідне кешування, щоб зменшити затримки та використання ресурсів:

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

#### 2. Впровадження залежностей і тестованість

Проєктуйте інструменти так, щоб вони отримували свої залежності через інжекцію конструктору, що робить їх тестованими і налаштовуваними:

```java
// Приклад на Java з впровадженням залежностей
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Залежності впроваджуються через конструктор
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Реалізація інструменту
    // ...
}
```

#### 3. Компонуємi інструменти

Проєктуйте інструменти, які можна комбінувати для створення складніших робочих процесів:

```python
# Приклад на Python, що демонструє комбінацію інструментів
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Реалізація...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Цей інструмент може використовувати результати інструменту dataFetch
    async def execute_async(self, request):
        # Реалізація...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Цей інструмент може використовувати результати інструменту dataAnalysis
    async def execute_async(self, request):
        # Реалізація...
        pass

# Ці інструменти можуть використовуватись окремо або як частина робочого процесу
```

### Найкращі практики проєктування схем

Схема є контрактом між моделлю та вашим інструментом. Добре проєктовані схеми покращують зручність використання інструментів.

#### 1. Чіткий опис параметрів

Завжди додавайте описову інформацію для кожного параметра:

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

#### 2. Обмеження валідації

Включайте обмеження валідації, щоб запобігти неправильному вводу:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Властивість електронної пошти з перевіркою формату
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Властивість віку з числовими обмеженнями
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Перерахована властивість
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

#### 3. Послідовність у структурах повернення

Підтримуйте послідовність у структурах відповідей, щоб моделям було легше інтерпретувати результати:

```python
async def execute_async(self, request):
    try:
        # Обробити запит
        results = await self._search_database(request.parameters["query"])
        
        # Завжди повертати послідовну структуру
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

### Обробка помилок

Надійна обробка помилок є критичною для підтримання надійності інструментів MCP.

#### 1. Коректна обробка помилок

Обробляйте помилки на відповідних рівнях і надавайте інформативні повідомлення:

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

#### 2. Структуровані відповіді про помилки

Повертайте структуровану інформацію про помилки, коли це можливо:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Реалізація
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
        
        // Повторно викинути інші виключення як ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Логіка повторних спроб

Використовуйте загальну логіку повторних спроб лише для операцій, що читають, або операцій, у яких
нижчестоящий контракт уже ідемпотентний. Для операцій з реальним ефектом час очікування
після відправлення запиту є неоднозначним. Узгоджуйте авторитетний стан і
повторно використовуйте той самий стабільний ключ операції перед повторним виконанням. Див. урок
[партнер Reliability Sidecar](./reliability-sidecars/README.md).

Наступний обмежений цикл повторних спроб підходить для операції лише для читання:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # секунди
    
    while retry_count < max_retries:
        try:
            # Викликати зовнішній API лише для читання
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Експоненційне збільшення затримки
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Нетранзитна помилка, не повторювати спробу
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Оптимізація продуктивності

#### 1. Кешування

Впроваджуйте кешування для витратних операцій:

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

#### 2. Асинхронна обробка

Використовуйте асинхронні патерни програмування для операцій, пов’язаних з I/O:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Для довготривалих операцій негайно повертайте ідентифікатор обробки
        String processId = UUID.randomUUID().toString();
        
        // Запустіть асинхронну обробку
        CompletableFuture.runAsync(() -> {
            try {
                // Виконайте довготривалу операцію
                documentService.processDocument(documentId);
                
                // Оновіть статус (зазвичай зберігається в базі даних)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Поверніть миттєву відповідь з ідентифікатором процесу
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Засіб перевірки статусу-компаньйон
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

#### 3. Обмеження ресурсів

Впроваджуйте обмеження використання ресурсів, щоб запобігти перевантаженню:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Дозволити 5 запитів на секунду
            bucket_size=10        # Дозволити сплески до 10 запитів
        )
    
    async def execute_async(self, request):
        # Перевірити, чи можемо продовжувати або потрібно чекати
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Якщо чекання надто довге
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Почекати відповідний час затримки
                await asyncio.sleep(delay)
        
        # Спожити токен і продовжити з запитом
        self.rate_limiter.consume()
        
        # Викликати API
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
            
            # Обчислити час до наявності наступного токена
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Додати нові токени на основі минулого часу
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Найкращі практики безпеки

#### 1. Валідація введення

Завжди ретельно перевіряйте вхідні параметри:

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

#### 2. Перевірки авторизації

Впроваджуйте належні перевірки авторизації:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Отримати контекст користувача з запиту
    UserContext user = request.getContext().getUserContext();
    
    // Перевірити, чи має користувач необхідні дозволи
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Для конкретних ресурсів перевірити доступ до цього ресурсу
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Продовжити виконання інструменту
    // ...
}
```

#### 3. Обробка конфіденційних даних

Обробляйте конфіденційні дані обережно:

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
        
        # Отримати дані користувача
        user_data = await self.user_service.get_user_data(user_id)
        
        # Фільтрувати конфіденційні поля, якщо це не було явно запрошено І авторизовано
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Перевірити рівень авторизації в контексті запиту
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Створити копію, щоб уникнути змін оригіналу
        redacted = user_data.copy()
        
        # Приховати конкретні конфіденційні поля
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Приховати вкладені конфіденційні дані
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Найкращі практики тестування для інструментів MCP

Комплексне тестування гарантує, що інструменти MCP працюють коректно, справляються з крайніми випадками і правильно інтегруються з рештою системи.

### Модульне тестування

#### 1. Тестування кожного інструменту в ізоляції

Створюйте сфокусовані тести для функціональності кожного інструменту:

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

#### 2. Тестування валідації схем

Перевірте, що схеми є валідними і належно застосовують обмеження:

```java
@Test
public void testSchemaValidation() {
    // Створити екземпляр інструменту
    SearchTool searchTool = new SearchTool();
    
    // Отримати схему
    Object schema = searchTool.getSchema();
    
    // Перетворити схему в JSON для валідації
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Перевірити, що схема є валідним JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Перевірити валідні параметри
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Перевірити відсутній обов’язковий параметр
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Перевірити недійсний тип параметра
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Тести обробки помилок

Створюйте спеціфічні тести для умов помилок:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Влаштувати
    tool = ApiTool(timeout=0.1)  # Дуже короткий тайм-аут
    
    # Замокати запит, який завершиться тайм-аутом
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Довше за тайм-аут
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Виконати та перевірити
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Перевірити повідомлення про виключення
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Влаштувати
    tool = ApiTool()
    
    # Замокати відповідь з обмеженням частоти
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
        
        # Виконати та перевірити
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Перевірити, що виключення містить інформацію про обмеження частоти
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Інтеграційне тестування

#### 1. Тестування ланцюжка інструментів

Тестуйте роботу інструментів у передбачених комбінаціях:

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

#### 2. Тестування сервера MCP

Тестуйте сервер MCP з повною реєстрацією та виконанням інструментів:

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
        // Тестувати кінцеву точку відкриття
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Створити запит інструменту
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Надіслати запит і перевірити відповідь
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Створити недійсний запит інструменту
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Відсутній параметр "b"
        request.put("parameters", parameters);
        
        // Надіслати запит і перевірити відповіді з помилкою
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Тестування від початку до кінця

Тестуйте повні робочі процеси від запиту моделі до виконання інструменту:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Налаштувати - Встановити клієнт MCP та замінити модель на макет
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Відповіді макета моделі
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
    
    # Відповідь інструменту погоди макета
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
        
        # Виконати
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Перевірити
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Тестування продуктивності

#### 1. Навантажувальне тестування

Перевірте, скільки одночасних запитів може обробляти ваш сервер MCP:

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

#### 2. Стрес-тестування

Тестуйте систему під екстремальним навантаженням:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Налаштуйте JMeter для стрес-тестування
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Налаштуйте план тестування JMeter
    HashTree testPlanTree = new HashTree();
    
    // Створіть план тестування, групу потоків, вибірки тощо
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Додайте HTTP-вибірку для виконання інструменту
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Додайте прослуховувачі
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Запустіть тест
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Перевірте результати
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Середній час відгуку < 200 мс
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90-й перцентиль < 500 мс
}
```

#### 3. Моніторинг і профілювання

Налаштуйте моніторинг для довгострокового аналізу продуктивності:

```python
# Налаштувати моніторинг для сервера MCP
def configure_monitoring(server):
    # Встановити метрики Prometheus
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
    
    # Додати проміжне програмне забезпечення для вимірювання часу та запису метрик
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Опублікувати кінцеву точку метрик
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Патерни проєктування робочих процесів MCP

Добре проєктовані робочі процеси MCP підвищують ефективність, надійність та підтримуваність. Ось ключові патерни, яких варто дотримуватись:

### 1. Патерн ланцюжка інструментів

З'єднуйте кілька інструментів у послідовності, де вихід одного інструменту стає входом для наступного:

```python
# Реалізація ланцюга інструментів Python
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Список назв інструментів для послідовного виконання
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Виконати кожен інструмент у ланцюжку, передаючи попередній результат
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Зберегти результат і використовувати як вхідні дані для наступного інструменту
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Приклад використання
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

### 2. Патерн диспетчера

Використовуйте центральний інструмент, що направляє запити до спеціалізованих інструментів залежно від вводу:

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

### 3. Патерн паралельної обробки

Виконуйте кілька інструментів одночасно для підвищення ефективності:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Крок 1: Отримати метадані набору даних (синхронно)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Крок 2: Запустити кілька аналізів паралельно
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
        
        // Очікувати завершення всіх паралельних завдань
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Очікувати завершення
        
        // Крок 3: Об’єднати результати
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Крок 4: Згенерувати підсумковий звіт
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Повернути повний результат робочого процесу
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Патерн відновлення після помилок

Впроваджуйте плавні відмови для випадків збою інструментів:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Спробуйте спершу основний інструмент
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Зареєструйте помилку
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Перейдіть до резервного інструменту
            try:
                # Можливо, потрібно трансформувати параметри для резервного інструменту
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Обидва інструменти зазнали невдачі
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Ця реалізація буде залежати від конкретних інструментів
        # Для цього прикладу ми просто повернемо оригінальні параметри
        return params

# Приклад використання
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Основний (платний) погодний API
        "basicWeatherService",    # Резервний (безкоштовний) погодний API
        {"location": location}
    )
```

### 5. Патерн композиції робочих процесів

Створюйте складні робочі процеси, комбінуючи простіші:

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

# Тестування серверів MCP: найкращі практики та поради

## Огляд

Тестування — критично важливий аспект розробки надійних, якісних серверів MCP. Цей посібник надає комплексні найкращі практики та поради щодо тестування серверів MCP протягом усього життєвого циклу розробки — від модульних тестів до інтеграційних і повного end-to-end тестування.

## Чому тестування важливе для серверів MCP

Сервери MCP відіграють ключову роль як проміжне програмне забезпечення між AI-моделями та клієнтськими застосунками. Ретельне тестування забезпечує:

- Надійність у виробничих середовищах
- Коректну обробку запитів і відповідей
- Відповідність специфікаціям MCP
- Стійкість до збоїв та крайніх випадків
- Послідовну продуктивність під різними навантаженнями

## Модульне тестування серверів MCP

### Модульне тестування (основа)

Модульні тести перевіряють окремі компоненти вашого сервера MCP в ізоляції.

#### Що тестувати

1. **Обробники ресурсів**: незалежно перевіряйте логіку кожного обробника ресурсів
2. **Реалізації інструментів**: перевірте поведінку інструментів з різними ввідними даними
3. **Шаблони запитів**: переконайтеся, що шаблони запитів відображаються правильно
4. **Валідація схем**: тестуйте логіку валідації параметрів
5. **Обробка помилок**: перевірте відповіді з помилками для недійсних вводів

#### Найкращі практики модульного тестування

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
# Приклад юніт-тесту для калькулятора на Python
def test_calculator_tool_add():
    # Підготовка
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Виконання
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Перевірка
    assert result["value"] == 12
```

### Інтеграційне тестування (проміжний рівень)

Інтеграційні тести перевіряють взаємодії між компонентами вашого сервера MCP.

#### Що тестувати

1. **Ініціалізація сервера**: тестуйте запуск сервера з різними конфігураціями
2. **Реєстрація маршрутів**: переконайтеся, що всі кінцеві точки зареєстровані коректно
3. **Обробка запитів**: тестуйте повний цикл запит-відповідь
4. **Поширення помилок**: гарантуйте належну обробку помилок між компонентами
5. **Аутентифікація та авторизація**: тестуйте механізми безпеки

#### Найкращі практики інтеграційного тестування

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

### End-to-End тестування (верхній рівень)

End-to-end тести перевіряють повну поведінку системи від клієнта до сервера.

#### Що тестувати

1. **Комунікація клієнт-сервер**: тестуйте повні цикли запит-відповідь
2. **Реальні клієнтські SDK**: тестуйте з реальними клієнтськими реалізаціями
3. **Продуктивність під навантаженням**: перевіряйте поведінку під високим числом одночасних запитів
4. **Відновлення після помилок**: тестуйте відновлення системи після збоїв

5. **Довготривалі операції**: Перевірте обробку потокових та тривалих операцій

#### Кращі практики для E2E тестування

```typescript
// Приклад E2E тесту з клієнтом на TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Запустити сервер у тестовому середовищі
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Виконати дію
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Перевірити результати
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Стратегії мокування для тестування MCP

Мокування є необхідним для ізоляції компонентів під час тестування.

### Компоненти для мокування

1. **Зовнішні AI моделі**: Мокування відповідей моделей для передбачуваного тестування
2. **Зовнішні сервіси**: Мокування API-залежностей (бази даних, сторонні сервіси)
3. **Сервіси автентифікації**: Мокування провайдерів ідентифікації
4. **Постачальники ресурсів**: Мокування дорогих обробників ресурсів

### Приклад: Мокування відповіді AI моделі

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
# Приклад Python з unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Налаштувати заглушку
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Використати заглушку у тесті
    server = McpServer(model_client=mock_model)
    # Продовжити з тестом
```

## Тестування продуктивності

Тестування продуктивності є критично важливим для серверів MCP у продуктивному середовищі.

### Що вимірювати

1. **Затримка**: Час відповіді на запити
2. **Пропускна здатність**: Кількість оброблених запитів за секунду
3. **Використання ресурсів**: Використання CPU, пам’яті, мережі
4. **Обробка конкурентності**: Поведінка під паралельними запитами
5. **Характеристики масштабування**: Продуктивність із зростанням навантаження

### Інструменти для тестування продуктивності

- **k6**: Відкритий інструмент для навантажувального тестування
- **JMeter**: Комплексне тестування продуктивності
- **Locust**: Навантажувальне тестування на Python
- **Azure Load Testing**: Хмарне тестування продуктивності

### Приклад: Базовий тест навантаження за допомогою k6

```javascript
// скрипт k6 для навантажувального тестування сервера MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 віртуальних користувачів
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

## Автоматизація тестування для серверів MCP

Автоматизація тестів забезпечує стабільну якість і швидший цикл зворотного зв’язку.

### Інтеграція CI/CD

1. **Запуск юніт-тестів на pull request'ах**: Забезпечте, що зміни коду не порушують існуючий функціонал
2. **Інтеграційні тести в staging**: Запускайте інтеграційні тести у передпродакшн середовищах
3. **Базові показники продуктивності**: Підтримуйте бенчмарки продуктивності для виявлення регресій
4. **Сканування безпеки**: Автоматизуйте тестування безпеки як частину пайплайна

### Приклад CI пайплайна (GitHub Actions)

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

## Тестування на відповідність MCP Специфікаціям

Переконайтесь, що ваш сервер коректно реалізує специфікації MCP.

### Ключові області відповідності

1. **API кінцеві точки**: Тестуйте необхідні кінцеві точки (/resources, /tools тощо)
2. **Формат запитів/відповідей**: Перевіряйте відповідність схемі
3. **Коди помилок**: Перевіряйте правильність статус кодів для різних сценаріїв
4. **Типи контенту**: Тестуйте обробку різних типів контенту
5. **Потік автентифікації**: Перевіряйте механізми аутентифікації згідно зі специфікацією

### Набір тестів на відповідність

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

## Топ 10 порад для ефективного тестування серверів MCP

1. **Тестуйте визначення інструментів окремо**: Перевіряйте схеми незалежно від логіки інструментів
2. **Використовуйте параметризовані тести**: Тестуйте інструменти з різними вхідними даними, включно з граничними випадками
3. **Перевіряйте відповіді помилок**: Переконайтеся у правильній обробці помилок для усіх потенційних ситуацій
4. **Тестуйте логіку авторизації**: Гарантуйте правильний контроль доступу для різних ролей користувачів
5. **Моніторте покриття тестів**: Стреміться до високого покриття критичних ділянок коду
6. **Тестуйте потокові відповіді**: Перевіряйте коректну обробку стрімінгу
7. **Симулюйте мережеві проблеми**: Тестуйте поведінку за поганих мережевих умов
8. **Тестуйте обмеження ресурсів**: Перевіряйте поведінку при досягненні квот або лімітів швидкості
9. **Автоматизуйте регресійні тести**: Створюйте набір, що запускається при кожній зміні коду
10. **Документуйте тестові випадки**: Підтримуйте чітку документацію тестових сценаріїв

## Типові помилки при тестуванні

- **Надмірне спиральне тестування "щасливого шляху"**: Обов’язково ретельно тестуйте випадки помилок
- **Ігнорування тестування продуктивності**: Виявляйте вузькі місця до запуску в продуктив
- **Тестування виключно в ізоляції**: Комбінуйте юніт, інтеграційні і E2E тести
- **Неповне покриття API**: Переконайтеся, що всі кінцеві точки та функції протестовані
- **Незбалансовані тестові середовища**: Використовуйте контейнери для забезпечення консистентності середовищ

## Висновок

Комплексна стратегія тестування є необхідною для розробки надійних, високоякісних серверів MCP. Застосовуючи кращі практики та поради, викладені в цьому посібнику, ви зможете забезпечити відповідність ваших реалізацій MCP найвищим стандартам якості, надійності та продуктивності.


## Головні висновки

1. **Проєктування інструментів**: Дотримуйтесь принципу єдиної відповідальності, використовуйте dependency injection і проектуйте для композиції
2. **Проєктування схем**: Створюйте чіткі, добре документовані схеми з коректними валідаційними обмеженнями
3. **Обробка помилок**: Реалізуйте плавну обробку помилок, структуровані відповіді на помилки та логіку повторних спроб з урахуванням результатів

4. **Продуктивність**: Використовуйте кешування, асинхронну обробку та дроселювання ресурсів
5. **Безпека**: Надавайте ретельну валідацію входів, перевірку авторизації та безпечну обробку чутливих даних
6. **Тестування**: Створюйте комплексні юніт, інтеграційні та end-to-end тести
7. **Патерни робочих процесів**: Застосовуйте усталені патерни, такі як ланцюги, диспетчери та паралельна обробка

## Вправа

Запроєктуйте інструмент MCP та робочий процес для системи обробки документів, що:

1. Приймає документи у кількох форматах (PDF, DOCX, TXT)
2. Витягує текст та ключову інформацію з документів
3. Класифікує документи за типом та змістом
4. Генерує резюме для кожного документа

Реалізуйте схеми інструмента, обробку помилок та робочий патерн, що найкраще підходить для цього сценарію. Розгляньте, як ви будете тестувати цю реалізацію.

## Ресурси 

1. Приєднуйтесь до спільноти MCP на [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs), щоб бути в курсі останніх подій 
2. Вносьте свій вклад у відкриті [MCP проекти](https://github.com/modelcontextprotocol)
3. Застосовуйте принципи MCP у ініціативах AI вашої організації
4. Вивчайте спеціалізовані реалізації MCP для вашої галузі.
5. Розгляньте можливість проходження курсів підвищеної складності з окремих тем MCP, таких як мульти-модальна інтеграція або інтеграція корпоративних додатків.
6. Експериментуйте із створенням власних інструментів та робочих процесів MCP, використовуючи принципи з [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Що далі

Далі: [Кейс-стаді](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
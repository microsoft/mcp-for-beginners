# Най-добри практики за разработка на MCP

[![Най-добри практики за разработка на MCP](../../../translated_images/bg/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(Кликнете върху изображението по-горе, за да гледате видеото към този урок)_

## Преглед

Този урок се фокусира върху напреднали най-добри практики за разработка, тестване и внедряване на MCP сървъри и функции в производствени среди. С нарастването на сложността и значимостта на MCP екосистемите, следването на утвърдени модели гарантира надеждност, поддръжка и съвместимост. Урокът обединява практически опит, натрупан от реални MCP реализации, за да ви насочи към създаването на стабилни, ефективни сървъри с подходящи ресурси, подсказки и инструменти.

## Цели на обучението

До края на този урок ще можете да:

- Прилагате най-добрите практики в индустрията за проектиране на MCP сървъри и функции
- Създавате цялостни стратегии за тестване на MCP сървъри
- Проектирате ефективни, многократно използваеми модели на работни процеси за сложни MCP приложения
- Реализирате правилно управление на грешки, логване и наблюдаемост в MCP сървъри
- Оптимизирате MCP реализации за производителност, сигурност и поддръжка

## Основни принципи на MCP

Преди да се потопим в конкретни практики за реализация, е важно да разберем основните принципи, които ръководят ефективната разработка на MCP:

1. **Стандартизирана комуникация**: MCP използва JSON-RPC 2.0 като основа, осигурявайки последователен формат за заявки, отговори и управление на грешки във всички реализации.

2. **Дизайн, ориентиран към потребителя**: Винаги поставяйте на първо място съгласието, контрола и прозрачността на потребителя във вашите MCP реализации.

3. **Сигурност на първо място**: Реализирайте надеждни мерки за сигурност, включително удостоверяване, упълномощаване, валидиране и ограничаване на честотата.

4. **Модулна архитектура**: Проектирайте MCP сървъри с модулен подход, където всеки инструмент и ресурс има ясна и фокусирана цел.

5. **Състояние на връзките**: Използвайте способността на MCP да поддържа състояние през множество заявки за по-кохерентни и контекстуално осъзнати взаимодействия.

## Официални най-добри практики за MCP

Следните най-добри практики са извлечени от официалната документация на Model Context Protocol:

### Най-добри практики за сигурност

1. **Съгласие и контрол на потребителя**: Винаги изисквайте изрично съгласие от потребителя преди достъп до данни или извършване на операции. Осигурете ясен контрол върху това какви данни се споделят и какви действия са упълномощени.

2. **Поверителност на данните**: Разкривайте потребителски данни само с изрично съгласие и ги защитавайте с подходящи контроли за достъп. Предпазвайте от неупълномощено предаване на данни.

3. **Безопасност на инструментите**: Изисквайте изрично съгласие от потребителя преди използването на който и да е инструмент. Осигурете разбиране за функционалността на всеки инструмент и наложете надеждни граници за сигурност.

4. **Контрол на разрешенията за инструменти**: Конфигурирайте кои инструменти са разрешени за използване от модел по време на сесия, като гарантирате, че само изрично упълномощени инструменти са достъпни.

5. **Удостоверяване**: Изисквайте правилно удостоверяване преди предоставяне на достъп до инструменти, ресурси или чувствителни операции, използвайки API ключове, OAuth токени или други сигурни методи.

6. **Валидиране на параметри**: Налагайте валидиране за всички извиквания на инструменти, за да предотвратите неправилно форматирани или злонамерени входни данни.

7. **Ограничаване на честотата**: Реализирайте ограничаване на честотата, за да предотвратите злоупотреба и да осигурите справедливо използване на ресурсите на сървъра.

### Най-добри практики за реализация

1. **Преговори за възможности**: По време на настройката на връзката обменяйте информация за поддържаните функции, версии на протокола, налични инструменти и ресурси.

2. **Дизайн на инструменти**: Създавайте фокусирани инструменти, които изпълняват една задача добре, вместо монолитни инструменти, които се занимават с множество аспекти.

3. **Управление на грешки**: Реализирайте стандартизирани съобщения за грешки и кодове, за да помогнете при диагностициране на проблеми, да управлявате неуспехите грациозно и да предоставяте полезна обратна връзка.

4. **Логване**: Конфигурирайте структурирани логове за одит, отстраняване на грешки и наблюдение на взаимодействията с протокола.

5. **Проследяване на напредъка**: За дълготрайни операции предоставяйте актуализации за напредъка, за да позволите отзивчиви потребителски интерфейси.

6. **Отмяна на заявки**: Позволете на клиентите да отменят текущи заявки, които вече не са необходими или отнемат твърде много време.

## Допълнителни референции

За най-актуална информация относно най-добрите практики за MCP, вижте:

- [MCP Документация](https://modelcontextprotocol.io/)
- [MCP Спецификация](https://spec.modelcontextprotocol.io/)
- [GitHub Репозитория](https://github.com/modelcontextprotocol)
- [Най-добри практики за сигурност](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## Примери за практическа реализация

### Най-добри практики за дизайн на инструменти

#### 1. Принцип на единствена отговорност

Всеки MCP инструмент трябва да има ясна и фокусирана цел. Вместо да създавате монолитни инструменти, които се опитват да се справят с множество аспекти, разработвайте специализирани инструменти, които се отличават в конкретни задачи.

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

#### 2. Последователно управление на грешки

Реализирайте надеждно управление на грешки с информативни съобщения за грешки и подходящи механизми за възстановяване.

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

#### 3. Валидиране на параметри

Винаги валидирайте параметрите старателно, за да предотвратите неправилно форматирани или злонамерени входни данни.

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

### Примери за реализация на сигурност

#### 1. Удостоверяване и упълномощаване

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

#### 2. Ограничаване на честотата

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

...
3. **Основни показатели за производителност**: Поддържайте еталони за производителност, за да откривате регресии  
4. **Сканиране за сигурност**: Автоматизирайте тестването за сигурност като част от процеса  

### Пример за CI Pipeline (GitHub Actions)

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

## Тестване за съответствие със спецификацията MCP

Уверете се, че вашият сървър правилно прилага спецификацията MCP.

### Основни области на съответствие

1. **API крайни точки**: Тествайте задължителните крайни точки (/resources, /tools и др.)  
2. **Формат на заявка/отговор**: Проверете съответствието със схемата  
3. **Кодове за грешки**: Уверете се, че се използват правилните статус кодове за различни сценарии  
4. **Типове съдържание**: Тествайте обработката на различни типове съдържание  
5. **Процес на удостоверяване**: Проверете механизмите за удостоверяване, съответстващи на спецификацията  

### Комплект за тестване на съответствие

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

## Топ 10 съвета за ефективно тестване на MCP сървър

1. **Тествайте дефинициите на инструменти отделно**: Проверете дефинициите на схемата независимо от логиката на инструментите  
2. **Използвайте параметризирани тестове**: Тествайте инструментите с разнообразни входни данни, включително гранични случаи  
3. **Проверете отговорите при грешки**: Уверете се, че се обработват правилно всички възможни условия за грешка  
4. **Тествайте логиката за авторизация**: Уверете се, че достъпът е правилно контролиран за различни роли на потребителите  
5. **Следете покритието на тестовете**: Стремете се към високо покритие на критичния код  
6. **Тествайте стрийминг отговори**: Проверете правилната обработка на стрийминг съдържание  
7. **Симулирайте проблеми с мрежата**: Тествайте поведението при лоши мрежови условия  
8. **Тествайте ограниченията на ресурсите**: Проверете поведението при достигане на квоти или лимити на скоростта  
9. **Автоматизирайте регресионните тестове**: Създайте комплект, който се изпълнява при всяка промяна в кода  
10. **Документирайте тестовите случаи**: Поддържайте ясна документация на тестовите сценарии  

## Чести грешки при тестване

- **Прекалено разчитане на тестове за "щастливия път"**: Уверете се, че тествате подробно случаите на грешки  
- **Пренебрегване на тестването за производителност**: Идентифицирайте тесните места, преди да засегнат продукцията  
- **Тестване само в изолация**: Комбинирайте модулни, интеграционни и крайни тестове  
- **Непълно покритие на API**: Уверете се, че всички крайни точки и функции са тествани  
- **Несъответстващи тестови среди**: Използвайте контейнери за осигуряване на последователни тестови среди  

## Заключение

Цялостната стратегия за тестване е от съществено значение за разработването на надеждни и висококачествени MCP сървъри. Чрез прилагане на най-добрите практики и съвети, описани в това ръководство, можете да гарантирате, че вашите MCP реализации отговарят на най-високите стандарти за качество, надеждност и производителност.

## Основни изводи

1. **Дизайн на инструменти**: Следвайте принципа за единична отговорност, използвайте инжектиране на зависимости и проектирайте за съвместимост  
2. **Дизайн на схема**: Създавайте ясни, добре документирани схеми с подходящи ограничения за валидиране  
3. **Обработка на грешки**: Прилагайте елегантна обработка на грешки, структурирани отговори за грешки и логика за повторение  
4. **Производителност**: Използвайте кеширане, асинхронна обработка и ограничаване на ресурсите  
5. **Сигурност**: Прилагайте задълбочена валидиране на входните данни, проверки за авторизация и обработка на чувствителни данни  
6. **Тестване**: Създавайте цялостни модулни, интеграционни и крайни тестове  
7. **Модели на работни процеси**: Прилагайте утвърдени модели като вериги, диспечери и паралелна обработка  

## Упражнение

Проектирайте MCP инструмент и работен процес за система за обработка на документи, която:

1. Приема документи в различни формати (PDF, DOCX, TXT)  
2. Извлича текст и ключова информация от документите  
3. Класифицира документите по тип и съдържание  
4. Генерира резюме на всеки документ  

Прилагайте схемите на инструмента, обработката на грешки и модел на работен процес, който най-добре отговаря на този сценарий. Помислете как бихте тествали тази реализация.

## Ресурси

1. Присъединете се към MCP общността в [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs), за да сте в крак с последните разработки  
2. Допринасяйте за отворени [MCP проекти](https://github.com/modelcontextprotocol)  
3. Прилагайте MCP принципи във вашите собствени AI инициативи в организацията  
4. Изследвайте специализирани MCP реализации за вашата индустрия  
5. Помислете за участие в напреднали курсове по специфични MCP теми, като мултимодална интеграция или интеграция на корпоративни приложения  
6. Експериментирайте със създаването на собствени MCP инструменти и работни процеси, използвайки принципите, научени чрез [Практическата лаборатория](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

Следва: Най-добри практики [случаи от практиката](../09-CaseStudy/README.md)  

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
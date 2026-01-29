# أفضل الممارسات لتطوير MCP

[![أفضل الممارسات لتطوير MCP](../../../translated_images/ar/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(انقر على الصورة أعلاه لمشاهدة فيديو الدرس)_

## نظرة عامة

يركز هذا الدرس على أفضل الممارسات المتقدمة لتطوير واختبار ونشر خوادم MCP والميزات في بيئات الإنتاج. مع زيادة تعقيد وأهمية أنظمة MCP، فإن اتباع الأنماط المعتمدة يضمن الموثوقية وسهولة الصيانة وقابلية التشغيل البيني. يجمع هذا الدرس الحكمة العملية المكتسبة من تطبيقات MCP الواقعية لتوجيهك نحو إنشاء خوادم قوية وفعالة باستخدام الموارد والموجهات والأدوات المناسبة.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- تطبيق أفضل الممارسات الصناعية في تصميم خوادم وميزات MCP
- إنشاء استراتيجيات اختبار شاملة لخوادم MCP
- تصميم أنماط سير عمل فعالة وقابلة لإعادة الاستخدام لتطبيقات MCP المعقدة
- تنفيذ معالجة الأخطاء المناسبة، وتسجيل الأحداث، ومراقبة الأداء في خوادم MCP
- تحسين تطبيقات MCP من حيث الأداء والأمان وسهولة الصيانة

## المبادئ الأساسية لـ MCP

قبل التعمق في ممارسات التنفيذ المحددة، من المهم فهم المبادئ الأساسية التي توجه تطوير MCP الفعال:

1. **الاتصال الموحد**: يعتمد MCP على JSON-RPC 2.0 كأساس له، مما يوفر تنسيقًا موحدًا للطلبات والاستجابات ومعالجة الأخطاء عبر جميع التطبيقات.

2. **تصميم يركز على المستخدم**: يجب دائمًا إعطاء الأولوية لموافقة المستخدم وتحكمه وشفافيته في تطبيقات MCP.

3. **الأمان أولاً**: تنفيذ تدابير أمان قوية تشمل المصادقة، والتفويض، والتحقق، وتحديد المعدل.

4. **الهيكلية المعيارية**: تصميم خوادم MCP بطريقة معيارية، حيث يكون لكل أداة وموارد غرض واضح ومحدد.

5. **الاتصالات ذات الحالة**: الاستفادة من قدرة MCP على الحفاظ على الحالة عبر طلبات متعددة لتحقيق تفاعلات أكثر تماسكًا ووعيًا بالسياق.

## أفضل الممارسات الرسمية لـ MCP

الممارسات التالية مستمدة من وثائق بروتوكول نموذج السياق الرسمي:

### أفضل الممارسات الأمنية

1. **موافقة وتحكم المستخدم**: يجب دائمًا طلب موافقة صريحة من المستخدم قبل الوصول إلى البيانات أو تنفيذ العمليات. توفير تحكم واضح في البيانات التي يتم مشاركتها والإجراءات المصرح بها.

2. **خصوصية البيانات**: لا تكشف عن بيانات المستخدم إلا بموافقة صريحة، واحمها باستخدام ضوابط وصول مناسبة. تأكد من الحماية من نقل البيانات غير المصرح به.

3. **أمان الأدوات**: طلب موافقة صريحة من المستخدم قبل استدعاء أي أداة. تأكد من فهم المستخدمين لوظيفة كل أداة وفرض حدود أمان قوية.

4. **التحكم في أذونات الأدوات**: تكوين الأدوات التي يُسمح للنموذج باستخدامها خلال الجلسة، مما يضمن الوصول فقط إلى الأدوات المصرح بها صراحة.

5. **المصادقة**: طلب مصادقة صحيحة قبل منح الوصول إلى الأدوات أو الموارد أو العمليات الحساسة باستخدام مفاتيح API أو رموز OAuth أو طرق مصادقة آمنة أخرى.

6. **التحقق من المعلمات**: فرض التحقق لجميع استدعاءات الأدوات لمنع وصول المدخلات غير الصحيحة أو الضارة إلى تنفيذ الأدوات.

7. **تحديد المعدل**: تنفيذ تحديد المعدل لمنع الإساءة وضمان الاستخدام العادل لموارد الخادم.

### أفضل الممارسات في التنفيذ

1. **التفاوض على القدرات**: أثناء إعداد الاتصال، تبادل المعلومات حول الميزات المدعومة وإصدارات البروتوكول والأدوات والموارد المتاحة.

2. **تصميم الأدوات**: إنشاء أدوات مركزة تقوم بمهمة واحدة بشكل جيد بدلاً من أدوات ضخمة تتعامل مع اهتمامات متعددة.

3. **معالجة الأخطاء**: تنفيذ رسائل وأكواد أخطاء موحدة للمساعدة في تشخيص المشكلات، ومعالجة الفشل بسلاسة، وتقديم ملاحظات قابلة للتنفيذ.

4. **تسجيل الأحداث**: تكوين سجلات منظمة للتدقيق وتصحيح الأخطاء ومراقبة تفاعلات البروتوكول.

5. **تتبع التقدم**: بالنسبة للعمليات طويلة الأمد، تقديم تحديثات التقدم لتمكين واجهات المستخدم التفاعلية.

6. **إلغاء الطلبات**: السماح للعملاء بإلغاء الطلبات الجارية التي لم تعد مطلوبة أو تستغرق وقتًا طويلاً.

## مراجع إضافية

للحصول على أحدث المعلومات حول أفضل ممارسات MCP، راجع:

- [وثائق MCP](https://modelcontextprotocol.io/)
- [مواصفات MCP](https://spec.modelcontextprotocol.io/)
- [مستودع GitHub](https://github.com/modelcontextprotocol)
- [أفضل الممارسات الأمنية](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## أمثلة عملية على التنفيذ

### أفضل الممارسات في تصميم الأدوات

#### 1. مبدأ المسؤولية الواحدة

يجب أن يكون لكل أداة MCP غرض واضح ومحدد. بدلاً من إنشاء أدوات ضخمة تحاول التعامل مع اهتمامات متعددة، قم بتطوير أدوات متخصصة تتفوق في مهام محددة.

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

#### 2. معالجة الأخطاء بشكل متسق

تنفيذ معالجة أخطاء قوية مع رسائل خطأ مفيدة وآليات استرداد مناسبة.

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

#### 3. التحقق من المعلمات

قم دائمًا بالتحقق من المعلمات بدقة لمنع المدخلات غير الصحيحة أو الضارة.

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

### أمثلة على تنفيذ الأمان

#### 1. المصادقة والتفويض

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

#### 2. تحديد المعدل

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

## أفضل الممارسات لاختبار MCP

### 1. اختبار الوحدات لأدوات MCP

اختبر أدواتك دائمًا بشكل منفصل مع محاكاة التبعيات الخارجية:

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

### 2. اختبار التكامل

اختبر التدفق الكامل من طلبات العميل إلى استجابات الخادم:

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

## تحسين الأداء

### 1. استراتيجيات التخزين المؤقت

تنفيذ التخزين المؤقت المناسب لتقليل التأخير واستخدام الموارد:

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

#### 2. حقن التبعيات وقابلية الاختبار

صمم الأدوات لتلقي تبعياتها من خلال حقن المنشئ، مما يجعلها قابلة للاختبار والتكوين:

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

#### 3. الأدوات القابلة للتكوين

صمم الأدوات بحيث يمكن دمجها معًا لإنشاء سير عمل أكثر تعقيدًا:

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

### أفضل الممارسات لتصميم المخططات

المخطط هو العقد بين النموذج وأداتك. تؤدي المخططات المصممة جيدًا إلى تحسين قابلية استخدام الأدوات.

#### 1. أوصاف واضحة للمعلمات

قم دائمًا بتضمين معلومات وصفية لكل معلمة:

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

#### 2. قيود التحقق

قم بتضمين قيود التحقق لمنع المدخلات غير الصالحة:

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

#### 3. هياكل استجابة متسقة

حافظ على التناسق في هياكل الاستجابة لتسهيل تفسير النتائج من قبل النماذج:

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

### معالجة الأخطاء

تعد معالجة الأخطاء بشكل قوي أمرًا ضروريًا للحفاظ على موثوقية أدوات MCP.

#### 1. معالجة الأخطاء بسلاسة

قم بمعالجة الأخطاء على المستويات المناسبة وقدم رسائل مفيدة:

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

#### 2. استجابات الأخطاء المنظمة

قم بإرجاع معلومات خطأ منظمة عندما يكون ذلك ممكنًا:

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

#### 3. منطق إعادة المحاولة

قم بتنفيذ منطق إعادة المحاولة المناسب للفشل المؤقت:

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

### تحسين الأداء

#### 1. التخزين المؤقت

قم بتنفيذ التخزين المؤقت للعمليات المكلفة:

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

#### 2. المعالجة غير المتزامنة

استخدم أنماط البرمجة غير المتزامنة للعمليات المرتبطة بالإدخال/الإخراج:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // For long-running operations, return a processing ID immediately
        String processId = UUID.randomUUID().toString();
        
        // Start async processing
        CompletableFuture.runAsync(() -> {
            try {
                // Perform long-running operation
                documentService.processDocument(documentId);
                
                // Update status (would typically be stored in a database)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Return immediate response with process ID
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Companion status check tool
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

#### 3. التحكم في الموارد

قم بتنفيذ التحكم في الموارد لمنع التحميل الزائد:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Allow 5 requests per second
            bucket_size=10        # Allow bursts up to 10 requests
        )
    
    async def execute_async(self, request):
        # Check if we can proceed or need to wait
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # If wait is too long
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Wait for the appropriate delay time
                await asyncio.sleep(delay)
        
        # Consume a token and proceed with the request
        self.rate_limiter.consume()
        
        # Call API
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
            
            # Calculate time until next token available
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Add new tokens based on elapsed time
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### أفضل الممارسات الأمنية

#### 1. التحقق من المدخلات

قم دائمًا بالتحقق من معلمات الإدخال بدقة:

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

#### 2. فحوصات التفويض

قم بتنفيذ فحوصات التفويض المناسبة:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Get user context from request
    UserContext user = request.getContext().getUserContext();
    
    // Check if user has required permissions
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // For specific resources, check access to that resource
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Proceed with tool execution
    // ...
}
```

#### 3. التعامل مع البيانات الحساسة

تعامل مع البيانات الحساسة بعناية:

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
        
        # Get user data
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filter sensitive fields unless explicitly requested AND authorized
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Check authorization level in request context
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Create a copy to avoid modifying the original
        redacted = user_data.copy()
        
        # Redact specific sensitive fields
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Redact nested sensitive data
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## أفضل الممارسات لاختبار أدوات MCP

يضمن الاختبار الشامل أن أدوات MCP تعمل بشكل صحيح، وتعالج الحالات الحافة، وتتكامل بشكل صحيح مع بقية النظام.

### اختبار الوحدات

#### 1. اختبار كل أداة بشكل منفصل

قم بإنشاء اختبارات مركزة لوظائف كل أداة:

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

#### 2. اختبار التحقق من المخططات

اختبر أن المخططات صالحة وتفرض القيود بشكل صحيح:

```java
@Test
public void testSchemaValidation() {
    // Create tool instance
    SearchTool searchTool = new SearchTool();
    
    // Get schema
    Object schema = searchTool.getSchema();
    
    // Convert schema to JSON for validation
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Validate schema is valid JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Test valid parameters
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Test missing required parameter
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Test invalid parameter type
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. اختبارات معالجة الأخطاء

قم بإنشاء اختبارات محددة لظروف الخطأ:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Arrange
    tool = ApiTool(timeout=0.1)  # Very short timeout
    
    # Mock a request that will time out
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Longer than timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Act & Assert
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verify exception message
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Arrange
    tool = ApiTool()
    
    # Mock a rate-limited response
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
        
        # Act & Assert
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verify exception contains rate limit information
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### اختبار التكامل

#### 1. اختبار سلسلة الأدوات

اختبر الأدوات التي تعمل معًا في التوليفات المتوقعة:

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

#### 2. اختبار خادم MCP

اختبر خادم MCP مع تسجيل الأدوات وتنفيذها بالكامل:

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
        // Test the discovery endpoint
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Create tool request
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Send request and verify response
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Create invalid tool request
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Missing parameter "b"
        request.put("parameters", parameters);
        
        // Send request and verify error response
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. اختبار شامل

اختبر سير العمل الكامل من طلب النموذج إلى تنفيذ الأداة:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Arrange - Set up MCP client and mock model
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Mock model responses
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
    
    # Mock weather tool response
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
        
        # Act
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Assert
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### اختبار الأداء

#### 1. اختبار التحميل

اختبر عدد الطلبات المتزامنة التي يمكن لخادم MCP التعامل معها:

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

#### 2. اختبار الإجهاد

اختبر النظام تحت حمل شديد:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Set up JMeter for stress testing
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Configure JMeter test plan
    HashTree testPlanTree = new HashTree();
    
    // Create test plan, thread group, samplers, etc.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Add HTTP sampler for tool execution
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Add listeners
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Run test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Validate results
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Average response time < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90th percentile < 500ms
}
```

#### 3. المراقبة والتحليل

قم بإعداد المراقبة لتحليل الأداء طويل الأمد:

```python
# Configure monitoring for an MCP server
def configure_monitoring(server):
    # Set up Prometheus metrics
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
    
    # Add middleware for timing and recording metrics
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Expose metrics endpoint
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## أنماط تصميم سير عمل MCP

تحسن سير العمل المصمم جيدًا من الكفاءة والموثوقية وسهولة الصيانة. فيما يلي الأنماط الرئيسية التي يجب اتباعها:

### 1. نمط سلسلة الأدوات

قم بتوصيل أدوات متعددة في تسلسل حيث يصبح إخراج كل أداة مدخلًا للأداة التالية:

```python
# Python Chain of Tools implementation
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # List of tool names to execute in sequence
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Execute each tool in the chain, passing previous result
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Store result and use as input for next tool
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Example usage
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

### 2. نمط الموزع

استخدم أداة مركزية تقوم بتوزيع المهام على الأدوات المتخصصة بناءً على المدخلات:

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

### 3. نمط المعالجة المتوازية

قم بتنفيذ أدوات متعددة في وقت واحد لتحقيق الكفاءة:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Step 1: Fetch dataset metadata (synchronous)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Step 2: Launch multiple analyses in parallel
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
        
        // Wait for all parallel tasks to complete
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Wait for completion
        
        // Step 3: Combine results
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Step 4: Generate summary report
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Return complete workflow result
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. نمط استرداد الأخطاء

قم بتنفيذ استراتيجيات استرداد سلسة لفشل الأدوات:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Try primary tool first
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Log the failure
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Fall back to secondary tool
            try:
                # Might need to transform parameters for fallback tool
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Both tools failed
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # This implementation would depend on the specific tools
        # For this example, we'll just return the original parameters
        return params

# Example usage
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Primary (paid) weather API
        "basicWeatherService",    # Fallback (free) weather API
        {"location": location}
    )
```

### 5. نمط تكوين سير العمل

قم ببناء سير عمل معقد من خلال تكوين سير عمل أبسط:

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

# اختبار خوادم MCP: أفضل الممارسات وأهم النصائح

## نظرة عامة

يعد الاختبار جانبًا حاسمًا في تطوير خوادم MCP الموثوقة وعالية الجودة. توفر هذه الإرشادات أفضل الممارسات والنصائح الشاملة لاختبار خوادم MCP طوال دورة التطوير، بدءًا من اختبارات الوحدات إلى اختبارات التكامل والتحقق الشامل.

## لماذا يعتبر الاختبار مهمًا لخوادم MCP؟

تعمل خوادم MCP كوسيط حيوي بين نماذج الذكاء الاصطناعي وتطبيقات العميل. يضمن الاختبار الشامل:

- الموثوقية في بيئات الإنتاج
- التعامل الدقيق مع الطلبات والاستجابات
- التنفيذ الصحيح لمواصفات MCP
- المرونة ضد الفشل والحالات الحافة
- الأداء المتسق تحت الأحمال المختلفة

## اختبار الوحدات لخوادم MCP

### اختبار الوحدات (الأساس)

تتحقق اختبارات الوحدات من مكونات خادم MCP الفردية بشكل منفصل.

#### ما الذي يجب اختباره؟

1. **معالجات الموارد**: اختبار منطق كل معالج موارد بشكل مستقل
2. **تنفيذ الأدوات**: التحقق من سلوك الأدوات مع مدخلات مختلفة
3. **قوالب الموجهات**: التأكد من أن قوالب الموجهات تعمل بشكل صحيح
4. **التحقق من المخططات**: اختبار منطق التحقق من المعلمات
5. **معالجة الأخطاء**: التحقق من استجابات الأخطاء للمدخلات غير الصالحة

#### أفضل الممارسات لاختبار الوحدات

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
# Example unit test for a calculator tool in Python
def test_calculator_tool_add():
    # Arrange
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Act
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Assert
    assert result["value"] == 12
```

### اختبار التكامل (الطبقة الوسطى)

تتحقق اختبارات التكامل من التفاعلات بين مكونات خادم MCP.

#### ما الذي يجب اختباره؟

1. **تهيئة الخادم**: اختبار بدء تشغيل الخادم مع تكوينات مختلفة
2. **تسجيل المسارات**: التحقق من تسجيل جميع نقاط النهاية بشكل صحيح
3. **معالجة الطلبات**: اختبار دورة الطلب-الاستجابة الكاملة
4. **نشر الأخطاء**: التأكد من معالجة الأخطاء بشكل صحيح عبر المكونات
5. **المصادقة والتفويض**: اختبار آليات الأمان

#### أفضل الممارسات لاختبار التكامل

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

### الاختبار الشامل (الطبقة العليا)

تتحقق الاختبارات الشاملة من سلوك النظام الكامل من العميل إلى الخادم.

#### ما الذي يجب اختباره؟

1. **اتصال العميل-الخادم**: اختبار دورات الطلب-الاستجابة الكاملة
2. **SDKs العملاء الحقيقية**: الاختبار باستخدام تطبيقات العملاء الفعلية
3. **الأداء تحت الحمل**: التحقق من السلوك مع طلبات متزامنة متعددة
4. **استرداد الأخطاء**: اختبار استرداد النظام من الفشل
5. **العمليات طويلة الأمد**: التحقق من معالجة التدفق والعمليات الطويلة

#### أفضل الممارسات للاختبارات الشاملة

```typescript
// Example E2E test with a client in TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Start server in test environment
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Act
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Assert
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## استراتيجيات المحاكاة لاختبار MCP

تعد المحاكاة ضرورية لعزل المكونات أثناء الاختبار.

### المكونات التي يجب محاكاتها

1. **نماذج الذكاء الاصطناعي الخارجية**: محاكاة استجابات النماذج لاختبارات متوقعة
2. **الخدمات الخارجية**: محاكاة تبعيات API (قواعد البيانات، الخدمات الخارجية)
3. **خدمات المصادقة**: محاكاة مزودي الهوية
4. **موفرو الموارد**: محاكاة معالجات الموارد المكلفة

### مثال: محاكاة استجابة نموذج الذكاء الاصطناعي

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
# Python example with unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Configure mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Use mock in test
    server = McpServer(model_client=mock_model)
    # Continue with test
```

## اختبار الأداء

يعد اختبار الأداء أمرًا بالغ الأهمية لخوادم MCP في بيئات الإنتاج.

### ما الذي يجب قياسه؟

1. **التأخير**: وقت الاستجابة للطلبات
2. **الإنتاجية**: عدد الطلبات التي يتم التعامل معها في الثانية
3. **استخدام الموارد**: استخدام وحدة المعالجة المركزية، والذاكرة، والشبكة
4. **التعامل مع التزامن**: السلوك تحت الطلبات المتوازية
5. **خصائص التوسع**: الأداء مع زيادة الحمل

### أدوات اختبار الأداء

- **k6**: أداة اختبار تحميل مفتوحة المصدر
- **JMeter**: أداة اختبار أداء شاملة
- **Locust**: أداة اختبار تحميل تعتمد على Python
- **Azure Load Testing**: اختبار أداء قائم على السحابة

### مثال: اختبار تحميل أساسي باستخدام k6

```javascript
// k6 script for load testing MCP server
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtual users
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

## أتمتة الاختبارات لخوادم MCP

تضمن أتمتة الاختبارات جودة متسقة وحلقات تغذية راجعة أسرع.

### التكامل مع CI/CD

1. **تشغيل اختبارات الوحدات على طلبات السحب**: التأكد من أن تغييرات الكود لا تكسر الوظائف الحالية
2. **اختبارات التكامل في بيئات التدريج**: تشغيل اختبارات التكامل في بيئات ما قبل الإنتاج
3. **معايير الأداء**: حافظ على معايير الأداء للكشف عن التراجعات  
4. **فحوصات الأمان**: قم بأتمتة اختبارات الأمان كجزء من خط الأنابيب  

### مثال على خط أنابيب CI (GitHub Actions)

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

## اختبار الامتثال لمواصفات MCP  

تحقق من أن الخادم الخاص بك ينفذ مواصفات MCP بشكل صحيح.  

### مجالات الامتثال الرئيسية  

1. **نقاط النهاية API**: اختبر النقاط المطلوبة (/resources, /tools, إلخ)  
2. **تنسيق الطلب/الاستجابة**: تحقق من الامتثال للمخطط  
3. **رموز الأخطاء**: تحقق من رموز الحالة الصحيحة لمختلف السيناريوهات  
4. **أنواع المحتوى**: اختبر التعامل مع أنواع المحتوى المختلفة  
5. **تدفق المصادقة**: تحقق من آليات المصادقة المتوافقة مع المواصفات  

### مجموعة اختبارات الامتثال  

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

## أفضل 10 نصائح لاختبار خوادم MCP بشكل فعال  

1. **اختبر تعريفات الأدوات بشكل منفصل**: تحقق من تعريفات المخطط بشكل مستقل عن منطق الأدوات  
2. **استخدم اختبارات مُعلمة**: اختبر الأدوات بمجموعة متنوعة من المدخلات، بما في ذلك الحالات الحدية  
3. **تحقق من استجابات الأخطاء**: تأكد من التعامل الصحيح مع جميع حالات الخطأ المحتملة  
4. **اختبر منطق التفويض**: تأكد من التحكم المناسب في الوصول لأدوار المستخدم المختلفة  
5. **راقب تغطية الاختبارات**: استهدف تغطية عالية للكود في المسارات الحرجة  
6. **اختبر استجابات البث**: تحقق من التعامل الصحيح مع المحتوى المتدفق  
7. **حاكي مشاكل الشبكة**: اختبر السلوك في ظل ظروف الشبكة السيئة  
8. **اختبر حدود الموارد**: تحقق من السلوك عند الوصول إلى الحصص أو حدود المعدل  
9. **أتمتة اختبارات التراجع**: قم ببناء مجموعة اختبارات تعمل مع كل تغيير في الكود  
10. **وثق حالات الاختبار**: حافظ على توثيق واضح لسيناريوهات الاختبار  

## الأخطاء الشائعة في الاختبار  

- **الاعتماد المفرط على اختبارات المسار السعيد**: تأكد من اختبار حالات الخطأ بشكل شامل  
- **تجاهل اختبارات الأداء**: حدد نقاط الاختناق قبل أن تؤثر على الإنتاج  
- **الاختبار في عزلة فقط**: اجمع بين اختبارات الوحدة، التكامل، واختبارات النهاية إلى النهاية  
- **تغطية API غير مكتملة**: تأكد من اختبار جميع النقاط النهائية والميزات  
- **بيئات اختبار غير متسقة**: استخدم الحاويات لضمان بيئات اختبار متسقة  

## الخاتمة  

استراتيجية اختبار شاملة ضرورية لتطوير خوادم MCP موثوقة وعالية الجودة. من خلال تنفيذ أفضل الممارسات والنصائح الموضحة في هذا الدليل، يمكنك ضمان أن تطبيقات MCP الخاصة بك تلبي أعلى معايير الجودة، الموثوقية، والأداء.  

## النقاط الرئيسية  

1. **تصميم الأدوات**: اتبع مبدأ المسؤولية الواحدة، استخدم حقن التبعيات، وصمم للتكوين  
2. **تصميم المخطط**: أنشئ مخططات واضحة وموثقة جيدًا مع قيود تحقق مناسبة  
3. **التعامل مع الأخطاء**: نفذ معالجة أخطاء سلسة، استجابات أخطاء منظمة، ومنطق إعادة المحاولة  
4. **الأداء**: استخدم التخزين المؤقت، المعالجة غير المتزامنة، وتحديد الموارد  
5. **الأمان**: قم بتطبيق تحقق شامل للمدخلات، فحوصات التفويض، ومعالجة البيانات الحساسة  
6. **الاختبار**: أنشئ اختبارات وحدة، تكامل، ونهاية إلى نهاية شاملة  
7. **أنماط سير العمل**: طبق الأنماط المعروفة مثل السلاسل، الموزعين، والمعالجة المتوازية  

## تمرين  

صمم أداة MCP وسير عمل لنظام معالجة المستندات الذي:  

1. يقبل المستندات بصيغ متعددة (PDF, DOCX, TXT)  
2. يستخرج النص والمعلومات الرئيسية من المستندات  
3. يصنف المستندات حسب النوع والمحتوى  
4. يولد ملخصًا لكل مستند  

قم بتنفيذ مخططات الأدوات، معالجة الأخطاء، ونمط سير العمل الذي يناسب هذا السيناريو. فكر في كيفية اختبار هذا التنفيذ.  

## الموارد  

1. انضم إلى مجتمع MCP على [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) للبقاء على اطلاع على أحدث التطورات  
2. ساهم في مشاريع [MCP مفتوحة المصدر](https://github.com/modelcontextprotocol)  
3. طبق مبادئ MCP في مبادرات الذكاء الاصطناعي الخاصة بمنظمتك  
4. استكشف تطبيقات MCP المتخصصة لصناعتك  
5. فكر في أخذ دورات متقدمة حول موضوعات MCP محددة، مثل التكامل متعدد الوسائط أو تكامل التطبيقات المؤسسية  
6. جرب بناء أدوات وسير عمل MCP الخاصة بك باستخدام المبادئ التي تعلمتها من خلال [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

التالي: أفضل الممارسات [دراسات الحالة](../09-CaseStudy/README.md)  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.
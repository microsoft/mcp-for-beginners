# أفضل ممارسات تطوير MCP

[![أفضل ممارسات تطوير MCP](../../../translated_images/ar/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

## نظرة عامة

يركز هذا الدرس على أفضل الممارسات المتقدمة لتطوير واختبار ونشر خوادم وميزات MCP في بيئات الإنتاج. مع زيادة تعقيد وأهمية نظم MCP، يضمن اتباع الأنماط المعتمدة الموثوقية وقابلية الصيانة وقابلية التشغيل البيني. يجمع هذا الدرس الحكمة العملية المستفادة من تطبيقات MCP الواقعية لتوجيهك نحو إنشاء خوادم قوية وفعالة باستخدام موارد ومحفزات وأدوات فعالة.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- تطبيق أفضل الممارسات الصناعية في تصميم خوادم وميزات MCP
- إنشاء استراتيجيات اختبار شاملة لخوادم MCP
- تصميم أنماط سير عمل فعالة وقابلة لإعادة الاستخدام لتطبيقات MCP المعقدة
- تنفيذ معالجة أخطاء صحيحة، وتسجيل، وإمكانية مراقبة في خوادم MCP
- تحسين تطبيقات MCP من حيث الأداء والأمن وقابلية الصيانة

## المبادئ الأساسية لـ MCP

قبل الخوض في ممارسات التنفيذ المحددة، من المهم فهم المبادئ الأساسية التي توجه تطوير MCP الفعال:

1. **التواصل الموحد**: يستخدم MCP بروتوكول JSON-RPC 2.0 كأساس له، موفرًا تنسيقًا موحدًا للطلبات والاستجابات ومعالجة الأخطاء عبر جميع التطبيقات.

2. **تصميم موجه للمستخدم**: دائمًا أولي أهمية لموافقة المستخدم، والتحكم، والشفافية في تطبيقات MCP الخاصة بك.

3. **الأمن أولاً**: طبق تدابير أمنية قوية تشمل التوثيق، والتفويض، والتحقق، وتحديد المعدل.

4. **هندسة معيارية**: صمم خوادم MCP الخاصة بك بنهج معياري، حيث يكون لكل أداة وموارد هدف واضح ومركز.

5. **الحالة الصريحة**: MCP `2026-07-28` هو بلا حالة على مستوى البروتوكول
   . عندما يحتاج سير العمل إلى حالة عبر المكالمات، استخدم مقابض صريحة أو
   وسائط أداة عادية مدعومة بحالة تطبيق دائمة.

## أفضل الممارسات الرسمية لـ MCP

تستند أفضل الممارسات التالية إلى مستندات بروتوكول نموذج السياق الرسمي:

### أفضل الممارسات الأمنية

1. **موافقة المستخدم والتحكم**: دائمًا اطلب موافقة صريحة من المستخدم قبل الوصول إلى البيانات أو تنفيذ العمليات. قدِّم تحكمًا واضحًا بما يُشارك من بيانات والإجراءات المصرح بها.

2. **خصوصية البيانات**: عرض بيانات المستخدم فقط بموافقته الصريحة واحمها بضوابط وصول مناسبة. حميها ضد نقل البيانات غير المصرح به.

3. **سلامة الأدوات**: اطلب موافقة صريحة من المستخدم قبل استدعاء أي أداة. تأكد من فهم المستخدمين لوظيفة كل أداة وفرض حدود أمنية قوية.

4. **التحكم في صلاحية الأدوات**: قم بتكوين الأدوات التي يمكن للنموذج استخدامها لكل طلب وسياق تفويض، مع التأكد من أن الأدوات المصرح بها صراحة فقط هي المتاحة.
   
   

5. **المصادقة**: طلب المصادقة الصحيحة قبل منح الوصول إلى الأدوات أو الموارد أو العمليات الحساسة باستخدام مفاتيح API، أو رموز OAuth، أو طرق مصادقة آمنة أخرى.

6. **التحقق من المعاملات**: فرض التحقق لجميع استدعاءات الأدوات لمنع إدخال خاطئ أو ضار من الوصول إلى تنفيذ الأدوات.

7. **تحديد المعدل**: تنفيذ تحديد معدل لمنع الإساءة وضمان الاستخدام العادل لموارد الخادم.

### أفضل ممارسات التنفيذ

1. **التفاوض على القدرات**: تفاوض على إصدارات البروتوكول المدعومة
   والقدرات. في MCP `2026-07-28`، كل طلب مستقل وقد
   يستخدم `server/discover`; الإصدارات الأقدم تستخدم مصافحة التهيئة.


2. **تصميم الأدوات**: أنشئ أدوات مركزة تقوم بمهمة واحدة بشكل جيد، بدلاً من الأدوات الضخمة التي تتعامل مع عدة اهتمامات.

3. **معالجة الأخطاء**: نفذ رسائل وأكواد أخطاء موحدة لمساعدة في تشخيص المشكلات، والتعامل مع الإخفاقات بشكل سلس، وتقديم تعليقات قابلة للتنفيذ.

4. **المراقبة**: استخدم `stderr` لتشخيصات stdio و OpenTelemetry
   للمراقبة المهيكلة. ميزة تسجيل MCP مهجورة في
   مواصفة `2026-07-28`.

5. **تتبع التقدم**: بالنسبة للعمليات طويلة الأمد، قم بالإبلاغ عن تحديثات التقدم لتمكين واجهات مستخدم استجابية.

6. **إلغاء الطلبات**: اسمح للعملاء بإلغاء الطلبات الجارية التي لم تعد ضرورية أو تستغرق وقتًا طويلاً.

## مراجع إضافية

لمزيد من المعلومات المحدثة حول أفضل ممارسات MCP، راجع:

- [توثيق MCP](https://modelcontextprotocol.io/)
- [مواصفة MCP (2026-07-28)][mcp-2026-spec]
- [مواصفة MCP السابقة (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [امتداد مهام MCP][mcp-tasks-extension]
- [مستودع GitHub](https://github.com/modelcontextprotocol)
- [أفضل ممارسات الأمان](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP أفضل 10](https://microsoft.github.io/mcp-azure-security-guide/) - مخاطر الأمان وطرق التخفيف
- [ورشة عمل قمة أمان MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - تدريب عملي على الأمان

### درس رفيق الموثوقية

حلقات إعادة المحاولة العامة غير آمنة للأدوات التي تنشئ تذاكر أو مدفوعات،
رسائل، نشرات، أو تأثيرات أخرى في العالم الحقيقي. قد تُفقد الاستجابة
بعد تفعيل التأثير.

استخدم درس رفيق الموثوقية،
[إعادة المحاولة الآمنة لأدوات MCP: نمط الجناح الجانبي للموثوقية][reliability-sidecar],
لتعلم مفاتيح التشغيل المستقرة، وإدخال التكرار، والنقاط المرجعية،
والمصالحة، ومستويات الأدلة، وحقن الإخفاق.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## أمثلة تطبيقية عملية

### أفضل ممارسات تصميم الأدوات

#### 1. مبدأ المسؤولية الواحدة

يجب أن يكون لكل أداة MCP غرض واضح ومركّز. بدلاً من إنشاء أدوات ضخمة تحاول معالجة عدة اهتمامات، طوّر أدوات متخصصة تتفوق في مهام محددة.

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

#### 2. معالجة الأخطاء المتسقة

نفّذ معالجة أخطاء قوية مع رسائل أخطاء إعلامية وآليات تعافي مناسبة.

```python
# مثال بايثون مع معالجة شاملة للأخطاء
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # التحقق من صحة المعاملات
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # التحقق الأمني
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # عملية قاعدة البيانات مع مهلة زمنية
                async with timeout(10):  # مهلة ثانية 10
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # قد تكون أخطاء الاتصال مؤقتة
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # أخطاء الاستعلام على الأرجح أخطاء من العميل
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # السماح بمرور الأخطاء المحددة بالأداة
            raise
        except Exception as e:
            # التقاط جميع الأخطاء غير المتوقعة
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # تنفيذ اكتشاف حقن SQL
        pass
        
    def _log_error(self, message, error):
        # تنفيذ تسجيل الأخطاء
        pass
```

#### 3. التحقق من المعاملات

تحقق دائمًا من المعاملات بشكل شامل لمنع المدخلات المشوهة أو الخبيثة.

```javascript
// مثال على JavaScript/TypeScript مع التحقق المفصل من المعلمات
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
    // 1. التحقق من وجود المعامل
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. التحقق من أنواع المعاملات
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. التحقق من قيم المعاملات
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. التحقق من وجود محتوى لعملية الكتابة
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. التحقق من أمان المسار
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // التنفيذ بناءً على المعلمات التي تم التحقق منها
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // تنفيذ فحص أمان المسار
    // ...
  }
}
```

### أمثلة تنفيذ الأمان

#### 1. التوثيق والتفويض

```java
// مثال على جافا مع المصادقة والتفويض
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // حقن التبعيات
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
        // 1. استخراج سياق المصادقة
        String authToken = request.getContext().getAuthToken();
        
        // 2. مصادقة المستخدم
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. التحقق من التفويض للعملية المحددة
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. المتابعة مع العملية المصرح بها
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

## أفضل ممارسات الاختبار

### 1. اختبار وحدات أدوات MCP

اختبر أدواتك دائمًا في عزلة، معتمداً على تمويه التبعيات الخارجية:

```typescript
// مثال TypeScript لاختبار وحدة أداة
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // إنشاء خدمة طقس وهمية
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // إنشاء الأداة مع الاعتماد الوهمي
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // التهيئة
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // التنفيذ
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // التأكيد
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // التهيئة
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // التنفيذ والتأكيد
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
# مثال اختبار تكامل بايثون
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # بدء خادم الاختبار
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # إنشاء عميل
        client = McpClient("http://localhost:5000")
        
        # اختبار اكتشاف الأداة
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # اختبار تنفيذ الأداة
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # التحقق من الاستجابة
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # التنظيف بعد الاختبار
        await server.stop()
```

## تحسين الأداء


### 1. استراتيجيات التخزين المؤقت

نفذ تخزينًا مؤقتًا مناسبًا لتقليل زمن الاستجابة واستخدام الموارد:


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

صمم الأدوات لتستقبل تبعياتها من خلال حقن المُنشئ، مما يجعلها قابلة للاختبار وقابلة للتكوين:

```java
// مثال جافا مع حقن التبعية
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // التبعيات محقونة من خلال الباني
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // تنفيذ الأداة
    // ...
}
```

#### 3. أدوات قابلة للتكوین

صمم أدوات يمكن تركيبها معًا لإنشاء سير عمل أكثر تعقيدًا:

```python
# مثال بيثون يوضح الأدوات القابلة للتكوين
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # التنفيذ...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # يمكن لهذه الأداة استخدام نتائج أداة جلب البيانات
    async def execute_async(self, request):
        # التنفيذ...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # يمكن لهذه الأداة استخدام نتائج أداة تحليل البيانات
    async def execute_async(self, request):
        # التنفيذ...
        pass

# يمكن استخدام هذه الأدوات بشكل مستقل أو كجزء من سير العمل
```

### أفضل ممارسات تصميم المخطط

المخطط هو العقد بين النموذج وأداتك. تؤدي المخططات المصممة جيدًا إلى تحسين سهولة استخدام الأدوات.

#### 1. أوصاف واضحة للمعلمات

دائمًا قم بتضمين معلومات وصفية لكل معلمة:

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

قم بتضمين قيود تحقق لمنع المدخلات غير الصالحة:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // خاصية البريد الإلكتروني مع التحقق من التنسيق
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // خاصية العمر مع قيود رقمية
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // خاصية معدودة
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

#### 3. هياكل الإرجاع المتسقة

حافظ على الاتساق في هياكل الاستجابة لتسهيل تفسير النتائج على النماذج:

```python
async def execute_async(self, request):
    try:
        # معالجة الطلب
        results = await self._search_database(request.parameters["query"])
        
        # دائمًا أعد هيكلًا متسقًا
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

### التعامل مع الأخطاء

التعامل القوي مع الأخطاء أمر حاسم لأدوات MCP للحفاظ على الموثوقية.

#### 1. التعامل الأنيق مع الأخطاء

تعامل مع الأخطاء على المستويات المناسبة وقدم رسائل إعلامية:

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

#### 2. ردود الأخطاء المنظمة

أعِد معلومات الأخطاء بشكل منظم عندما يكون ذلك ممكنًا:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // التنفيذ
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
        
        // إعادة رمي الاستثناءات الأخرى كـ ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. منطق إعادة المحاولة

استخدم منطق إعادة المحاولة العام فقط للمكالمات أو العمليات التي تكون
عقودها السفلية متسامحة مع التكرار بالفعل. بالنسبة للعمليات المؤثرة، فإن المهلة
بعد إرسال الطلب تكون غامضة. قم بمصالحة الحالة الموثوقة
وأعد استخدام نفس مفتاح العملية المستقر قبل التنفيذ مرة أخرى. راجع
[درس مرافق الجوانب المتعلقة بالموثوقية](./reliability-sidecars/README.md).

حلقة إعادة المحاولة المحدودة التالية مناسبة للبحث فقط للقراءة:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # ثواني
    
    while retry_count < max_retries:
        try:
            # استدعاء واجهة برمجة تطبيقات خارجية للقراءة فقط
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # التراجع الأسّي
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # خطأ دائم، لا تحاول مرة أخرى
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

استخدم أنماط البرمجة غير المتزامنة للعمليات التي تعتمد على الإدخال/الإخراج:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // للعمليات التي تستغرق وقتًا طويلاً، قم بإرجاع معرف المعالجة فورًا
        String processId = UUID.randomUUID().toString();
        
        // ابدأ المعالجة غير المتزامنة
        CompletableFuture.runAsync(() -> {
            try {
                // نفّذ العملية طويلة الأمد
                documentService.processDocument(documentId);
                
                // حدّث الحالة (عادةً ما تُخزن في قاعدة بيانات)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // أرجع استجابة فورية مع معرف العملية
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // أداة فحص الحالة المصاحبة
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

#### 3. تقييد الموارد

قم بتنفيذ تقييد الموارد لمنع التحميل الزائد:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # السماح بـ 5 طلبات في الثانية
            bucket_size=10        # السماح بفجوات تصل إلى 10 طلبات
        )
    
    async def execute_async(self, request):
        # التحقق مما إذا كان بإمكاننا المتابعة أو الحاجة للانتظار
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # إذا كان الانتظار طويلاً جدًا
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # الانتظار للمدة الزمنية المناسبة
                await asyncio.sleep(delay)
        
        # استهلاك رمز والمضي قدمًا في الطلب
        self.rate_limiter.consume()
        
        # استدعاء واجهة برمجة التطبيقات
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
            
            # حساب الوقت حتى يصبح الرمز التالي متوفرًا
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # إضافة رموز جديدة بناءً على الوقت المنقضي
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### أفضل ممارسات الأمان

#### 1. التحقق من صحة المدخلات

دائمًا تحقق من صحة معلمات الإدخال بدقة:

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

قم بتنفيذ فحوصات التفويض السليمة:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // الحصول على سياق المستخدم من الطلب
    UserContext user = request.getContext().getUserContext();
    
    // التحقق مما إذا كان المستخدم لديه الأذونات المطلوبة
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // بالنسبة للموارد المحددة، تحقق من الوصول إلى تلك الموارد
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // المتابعة في تنفيذ الأداة
    // ...
}
```

#### 3. التعامل مع البيانات الحساسة

تعامل مع البيانات الحساسة بحذر:

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
        
        # احصل على بيانات المستخدم
        user_data = await self.user_service.get_user_data(user_id)
        
        # فلتر الحقول الحساسة ما لم يتم طلبها صراحةً وتفويضها
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # تحقق من مستوى التفويض في سياق الطلب
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # أنشئ نسخة لتجنب تعديل الأصل
        redacted = user_data.copy()
        
        # حجب حقول حساسة محددة
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # حجب البيانات الحساسة المتداخلة
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## أفضل ممارسات الاختبار لأدوات MCP

يضمن الاختبار الشامل أن أدوات MCP تعمل بشكل صحيح، تتعامل مع حالات الحافة، وتتفاعل بشكل سليم مع بقية النظام.

### اختبار الوحدة

#### 1. اختبار كل أداة بشكل معزول

أنشئ اختبارات مركزة لكل وظيفة من وظائف الأداة:

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

#### 2. اختبار التحقق من صحة المخطط

اختبر أن المخططات صالحة وتفرض القيود بشكل صحيح:

```java
@Test
public void testSchemaValidation() {
    // إنشاء مثال للأداة
    SearchTool searchTool = new SearchTool();
    
    // الحصول على المخطط
    Object schema = searchTool.getSchema();
    
    // تحويل المخطط إلى JSON للتحقق
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // التحقق من أن المخطط هو JSONSchema صالح
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // اختبار المعلمات الصحيحة
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // اختبار فقدان المعلمة المطلوبة
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // اختبار نوع المعلمة غير الصالح
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. اختبارات التعامل مع الأخطاء

أنشئ اختبارات محددة لحالات الأخطاء:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # رتب
    tool = ApiTool(timeout=0.1)  # مهلة قصيرة جداً
    
    # قم بمحاكاة طلب سينتهي وقت انتظاره
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # أطول من المهلة
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # نفذ وتحقق
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # تحقق من رسالة الاستثناء
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # رتب
    tool = ApiTool()
    
    # قم بمحاكاة استجابة محدودة بمعدل
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
        
        # نفذ وتحقق
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # تحقق من أن الاستثناء يحتوي على معلومات حدود المعدل
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### اختبار التكامل

#### 1. اختبار سلسلة الأدوات

اختبر الأدوات للعمل معًا في التراكيب المتوقعة:

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

اختبر خادم MCP مع تسجيل الأدوات والتنفيذ الكامل:

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
        // اختبار نقطة نهاية الاكتشاف
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // إنشاء طلب الأداة
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // إرسال الطلب والتحقق من الاستجابة
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // إنشاء طلب أداة غير صالح
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // المعامل "b" مفقود
        request.put("parameters", parameters);
        
        // إرسال الطلب والتحقق من استجابة الخطأ
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. اختبار من البداية إلى النهاية

اختبر سير العمل الكامل من موجه النموذج إلى تنفيذ الأداة:


```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # رتب - إعداد عميل MCP ونموذج المحاكاة
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # استجابات نموذج المحاكاة
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
    
    # استجابة أداة الطقس المحاكاة
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
        
        # نفّذ
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # تحقق
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### اختبار الأداء

#### 1. اختبار الحمولة

اختبر عدد الطلبات المتزامنة التي يمكن لخادم MCP الخاص بك التعامل معها:

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

#### 2. اختبار الضغط

اختبر النظام تحت حمل شديد:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // إعداد JMeter لاختبار الضغط
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // تكوين خطة اختبار JMeter
    HashTree testPlanTree = new HashTree();
    
    // إنشاء خطة اختبار، مجموعة الخيوط، المانِعين، إلخ
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // إضافة مانِع HTTP لتنفيذ الأداة
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // إضافة المستمعين
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // تشغيل الاختبار
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // التحقق من النتائج
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // متوسط زمن الاستجابة أقل من 200 مللي ثانية
    assertTrue(summaryReport.getPercentile(90.0) < 500); // النسبة المئوية التسعين أقل من 500 مللي ثانية
}
```

#### 3. المراقبة والتحليل

قم بإعداد المراقبة لتحليل الأداء على المدى الطويل:

```python
# تكوين المراقبة لخادم MCP
def configure_monitoring(server):
    # إعداد مقاييس بروجيثيوس
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
    
    # إضافة وسيط للتوقيت وتسجيل المقاييس
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # كشف نقطة نهاية المقاييس
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## أنماط تصميم تدفقات عمل MCP

تحسن تدفقات عمل MCP المصممة بشكل جيد الكفاءة والموثوقية وقابلية الصيانة. فيما يلي الأنماط الأساسية التي يجب اتباعها:

### 1. نمط سلسلة الأدوات

ربط عدة أدوات في تسلسل حيث يصبح مخرج كل أداة هو المدخل للأداة التالية:

```python
# تنفيذ سلسلة أدوات بايثون
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # قائمة بأسماء الأدوات للتنفيذ بالترتيب
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # تنفيذ كل أداة في السلسلة، مع تمرير النتيجة السابقة
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # تخزين النتيجة واستخدامها كمدخل للأداة التالية
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# مثال للاستخدام
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

استخدم أداة مركزية تقوم بتوزيع العمل إلى أدوات متخصصة بناءً على المدخلات:

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

نفذ عدة أدوات في وقت واحد لتحسين الكفاءة:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // الخطوة 1: جلب بيانات وصف مجموعة البيانات (متزامن)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // الخطوة 2: تشغيل تحليلات متعددة بشكل متوازي
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
        
        // الانتظار حتى تكتمل جميع المهام المتوازية
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // الانتظار حتى الانتهاء
        
        // الخطوة 3: دمج النتائج
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // الخطوة 4: إنشاء تقرير ملخص
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // إرجاع نتيجة سير العمل الكاملة
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. نمط استرجاع الأخطاء

نفذ استرجاعا سلسا في حال فشل الأدوات:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # جرب الأداة الأساسية أولاً
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # سجل الفشل
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # العودة إلى الأداة الثانوية
            try:
                # قد تحتاج إلى تحويل المعلمات لأداة الاستFallbackل
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # كلتا الأداتين فشلتا
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # هذا التنفيذ يعتمد على الأدوات المحددة
        # في هذا المثال، سنُعيد فقط المعلمات الأصلية
        return params

# مثال على الاستخدام
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # واجهة برمجة تطبيقات الطقس الأساسية (مدفوعة)
        "basicWeatherService",    # واجهة برمجة تطبيقات الطقس البديلة (مجاناً)
        {"location": location}
    )
```

### 5. نمط تركيب تدفقات العمل

بناء تدفقات عمل معقدة بتكوين تدفقات أبسط:

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

# اختبار خوادم MCP: أفضل الممارسات والنصائح الهامة

## نظرة عامة

يعد الاختبار جانبًا حاسمًا في تطوير خوادم MCP موثوقة وعالية الجودة. يوفر هذا الدليل أفضل الممارسات الشاملة والنصائح لاختبار خوادم MCP الخاصة بك طوال دورة التطوير، من اختبارات الوحدة إلى اختبارات التكامل والتحقق الشامل.

## لماذا يعتبر الاختبار مهما لخوادم MCP

تعمل خوادم MCP كوسيطات حيوية بين نماذج الذكاء الاصطناعي وتطبيقات العملاء. يضمن الاختبار الشامل:

- الموثوقية في بيئات الإنتاج
- المعالجة الدقيقة للطلبات والاستجابات
- التنفيذ الصحيح لمواصفات MCP
- الصمود ضد الأخطاء والحالات الحدية
- أداء ثابت تحت أحمال مختلفة

## اختبار الوحدة لخوادم MCP

### اختبار الوحدة (الأساس)

تختبر اختبارات الوحدة مكونات وحدة خادم MCP الخاصة بك بشكل مستقل.

#### ما يجب اختباره

1. **معالجات الموارد**: اختبار منطق كل معالج موارد بشكل مستقل
2. **تنفيذ الأدوات**: التحقق من سلوك الأداة مع مدخلات مختلفة
3. **نماذج النصوص التوجيهية**: التأكد من عرض نماذج النصوص بشكل صحيح
4. **التحقق من المخطط**: اختبار منطق التحقق من المعلمات
5. **معالجة الأخطاء**: التحقق من ردود الخطأ للمدخلات غير الصالحة

#### أفضل الممارسات لاختبار الوحدة

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
# اختبار وحدة مثال لأداة الآلة الحاسبة في بايثون
def test_calculator_tool_add():
    # ترتيب
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # تنفيذ
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # تأكيد
    assert result["value"] == 12
```

### اختبار التكامل (الطبقة الوسطى)

تتحقق اختبارات التكامل من التفاعلات بين مكونات خادم MCP الخاص بك.

#### ما يجب اختباره

1. **تهيئة الخادم**: اختبار بدء تشغيل الخادم مع تكوينات مختلفة
2. **تسجيل المسارات**: التحقق من تسجيل جميع نقاط النهاية بشكل صحيح
3. **معالجة الطلبات**: اختبار دورة الطلب والاستجابة كاملة
4. **انتشار الأخطاء**: التأكد من معالجة الأخطاء بشكل صحيح بين المكونات
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

### اختبار شامل من البداية للنهاية (الطبقة العليا)

تتحقق اختبارات البداية للنهاية من سلوك النظام الكامل من العميل إلى الخادم.

#### ما يجب اختباره

1. **التواصل بين العميل والخادم**: اختبار دورات الطلب والاستجابة كاملة
2. **مجموعات تطوير البرامج لعملاء حقيقيين**: اختبار باستخدام تطبيقات عملاء فعلية
3. **الأداء تحت الحمل**: التحقق من السلوك مع طلبات متعددة متزامنة
4. **استرجاع الأخطاء**: اختبار استرداد النظام من حالات الفشل

5. **العمليات طويلة الأمد**: تحقق من معالجة البث والعمليات الطويلة

#### أفضل الممارسات لاختبار نهاية إلى نهاية

```typescript
// مثال لاختبار E2E مع عميل بلغة TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // بدء الخادم في بيئة الاختبار
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // نفذ
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // تحقق من صحة النتائج
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## استراتيجيات المحاكاة لاختبار MCP

المحاكاة ضرورية لعزل المكونات أثناء الاختبار.

### المكونات التي يجب محاكاتها

1. **نماذج الذكاء الاصطناعي الخارجية**: محاكاة استجابات النماذج لاختبارات متوقعة
2. **الخدمات الخارجية**: محاكاة تبعيات واجهات برمجة التطبيقات (قواعد البيانات، خدمات الطرف الثالث)
3. **خدمات المصادقة**: محاكاة مزودي الهوية
4. **مزودو الموارد**: محاكاة معالجات الموارد المكلفة

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
# مثال بايثون باستخدام unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # تكوين الموك
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # استخدام الموك في الاختبار
    server = McpServer(model_client=mock_model)
    # الاستمرار في الاختبار
```

## اختبار الأداء

اختبار الأداء أمر حيوي لخوادم MCP الإنتاجية.

### ما الذي يجب قياسه

1. **الكمون**: زمن استجابة الطلبات
2. **معدل المعالجة**: الطلبات التي يتم التعامل معها في الثانية
3. **استخدام الموارد**: استخدام وحدة المعالجة المركزية، الذاكرة، الشبكة
4. **معالجة التزامن**: السلوك تحت الطلبات المتوازية
5. **خصائص التوسع**: الأداء مع زيادة الحمل

### أدوات اختبار الأداء

- **k6**: أداة اختبار تحميل مفتوحة المصدر
- **JMeter**: اختبار أداء شامل
- **Locust**: اختبار تحميل معتمد على Python
- **Azure Load Testing**: اختبار أداء قائم على السحابة

### مثال: اختبار تحميل أساسي باستخدام k6

```javascript
// برنامج نصي k6 لاختبار تحميل خادم MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 مستخدمين افتراضيين
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

## أتمتة الاختبار لخوادم MCP

أتمتة اختباراتك تضمن جودة متسقة ودورات تغذية راجعة أسرع.

### التكامل مع CI/CD

1. **تشغيل اختبارات الوحدة على طلبات السحب**: تأكد من أن تغييرات الكود لا تكسر الوظائف القائمة
2. **اختبارات التكامل في بيئة الاختبار**: تشغيل اختبارات التكامل في بيئات ما قبل الإنتاج
3. **مقاييس الأداء الأساسية**: الحفاظ على معايير الأداء لاكتشاف الانحدارات
4. **فحوصات الأمان**: أتمتة اختبارات الأمان كجزء من خط الأنابيب

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

## اختبار الالتزام بمواصفة MCP

تحقق من أن خادمك ينفذ مواصفة MCP بشكل صحيح.

### المجالات الرئيسية للامتثال

1. **نقاط نهاية API**: اختبار النقاط المطلوبة (/resources, /tools, إلخ)
2. **تنسيق الطلب/الاستجابة**: التحقق من توافق المخطط
3. **رموز الخطأ**: تحقق من رموز الحالة الصحيحة لمختلف السيناريوهات
4. **أنواع المحتوى**: اختبار التعامل مع أنواع محتوى مختلفة
5. **تدفق المصادقة**: تحقق من آليات المصادقة المتوافقة مع المواصفة

### مجموعة اختبار الامتثال

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

## أفضل 10 نصائح لاختبار خادم MCP بفعالية

1. **اختبر تعريفات الأدوات بشكل منفصل**: تحقق من تعريفات المخطط بشكل مستقل عن منطق الأداة
2. **استخدم اختبارات مع معاملات**: اختبر الأدوات بمجموعة متنوعة من المدخلات، بما في ذلك الحالات الحدية
3. **تحقق من استجابات الأخطاء**: تحقق من التعامل الصحيح مع الأخطاء لكل الحالات الممكنة
4. **اختبر منطق التفويض**: تأكد من التحكم السليم في الوصول لأدوار المستخدم المختلفة
5. **راقب تغطية الاختبار**: استهدف تغطية عالية لكود المسار الحرج
6. **اختبر استجابات البث**: تحقق من المعالجة الصحيحة للمحتوى المتدفق
7. **حاكي مشاكل الشبكة**: اختبر السلوك تحت ظروف شبكة ضعيفة
8. **اختبر حدود الموارد**: تحقق من السلوك عند الوصول إلى الحصص أو حدود المعدل
9. **أتمتة اختبارات الانحدار**: أنشئ مجموعة تشغيل على كل تغيير في الكود
10. **وثق حالات الاختبار**: احتفظ بوثائق واضحة لسيناريوهات الاختبار

## الأخطاء الشائعة في الاختبار

- **الاعتماد المفرط على اختبارات الطريق السلس**: تأكد من اختبار حالات الخطأ بدقة
- **تجاهل اختبار الأداء**: حدد الاختناقات قبل أن تؤثر على الإنتاج
- **الاختبار في عزلة فقط**: اجمع بين اختبارات الوحدة، التكامل، واختبارات نهاية إلى نهاية
- **تغطية غير كاملة لواجهة API**: تأكد من اختبار كل النقاط والميزات
- **بيئات اختبار غير متسقة**: استخدم الحاويات لضمان بيئات اختبار متناسقة

## الخلاصة

استراتيجية اختبار شاملة ضرورية لتطوير خوادم MCP موثوقة وعالية الجودة. من خلال تنفيذ أفضل الممارسات والنصائح الموضحة في هذا الدليل، يمكنك ضمان أن تطبيقات MCP الخاصة بك تلبي أعلى معايير الجودة والموثوقية والأداء.


## النقاط الرئيسية المستفادة

1. **تصميم الأدوات**: اتبع مبدأ المسؤولية الوحيدة، استخدم حقن التبعية، وصمم لتكون قابلة للتركيب
2. **تصميم المخططات**: أنشئ مخططات واضحة وموثقة جيدًا مع قيود تحقق مناسبة
3. **معالجة الأخطاء**: نفذ معالجة أخطاء سلسة، استجابات أخطاء منظمة، ومنطق إعادة المحاولة الواعي للنتائج

4. **الأداء**: استخدم التخزين المؤقت، المعالجة غير المتزامنة، وتخفيض الموارد
5. **الأمان**: طبق تحققًا شاملاً من المدخلات، فحوصات التفويض، والتعامل مع البيانات الحساسة
6. **الاختبار**: أنشئ اختبارات وحدة شاملة، تكامل، ونهاية إلى نهاية
7. **أنماط سير العمل**: طبق أنماط معتمدة مثل السلاسل، المرسلات، والمعالجة المتوازية

## التمرين

صمم أداة MCP وسير عمل لنظام معالجة الوثائق الذي:

1. يقبل المستندات بعدة صيغ (PDF, DOCX, TXT)
2. يستخرج النص والمعلومات الرئيسية من المستندات
3. يصنف الوثائق حسب النوع والمحتوى
4. يولد ملخصًا لكل وثيقة

نفذ مخططات الأداة، معالجة الأخطاء، ونمط سير العمل الذي يناسب هذا السيناريو. ضع في اعتبارك كيفية اختبار هذا التنفيذ.

## الموارد

1. انضم إلى مجتمع MCP على [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) للبقاء على اطلاع على أحدث التطورات
2. ساهم في مشاريع MCP مفتوحة المصدر [MCP projects](https://github.com/modelcontextprotocol)
3. طبق مبادئ MCP في مبادرات الذكاء الاصطناعي بمنظمتك الخاصة
4. استكشف تطبيقات MCP المتخصصة لصناعتك.
5. فكّر في خوض دورات متقدمة حول مواضيع MCP محددة، مثل التكامل متعدد الوسائط أو تكامل تطبيقات المؤسسات.
6. جرب بناء أدوات MCP وسير العمل الخاصة بك باستخدام المبادئ التي تعلمتها من خلال [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

## ما التالي

التالي: [دراسات حالة](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
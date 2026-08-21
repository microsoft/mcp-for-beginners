# MCP ترقی کے بہترین طریقے

[![MCP Development Best Practices](../../../translated_images/ur/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(فصلے کے اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

## جائزہ

یہ سبق MCP سرورز اور فیچرز کو پروڈکشن ماحول میں تیار کرنے، جانچنے اور تعینات کرنے کے لیے جدید بہترین طریقوں پر توجہ مرکوز کرتا ہے۔ جیسے جیسے MCP ایکو سسٹمز کی پیچیدگی اور اہمیت بڑھتی ہے، قائم شدہ طریقہ کار پر عمل کرنا یقین دہانی کرتا ہے کہ بھروسہ مندی، برقرار رکھنے کی آسانی، اور باہمی تعاون ممکن ہو۔ یہ سبق حقیقی دنیا کی MCP عمل درآمد سے حاصل شدہ عملی حکمت عملی کو یکجا کرتا ہے تاکہ آپ کو مضبوط، مؤثر سرورز بنانے کے لیے رہنمائی فراہم کی جا سکے جن میں مؤثر وسائل، پرامپٹس، اور آلات شامل ہوں۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- MCP سرور اور فیچر ڈیزائن میں صنعتی بہترین طریقے اپنانا
- MCP سرورز کے لیے جامع جانچ کی حکمت عملیاں تیار کرنا
- پیچیدہ MCP ایپلیکیشنز کے لیے مؤثر، قابل دوبارہ استعمال ورک فلو پیٹرنز ڈیزائن کرنا
- MCP سرورز میں مناسب ایرر ہینڈلنگ، لاگنگ، اور آبزرویبیلٹی نافذ کرنا
- کارکردگی، سلامتی، اور برقرار رکھنے کے لیے MCP عمل درآمد کو بہتر بنانا

## MCP کے بنیادی اصول

مخصوص عمل درآمد کے طریقوں میں غوطہ لگانے سے پہلے، یہ ضروری ہے کہ ان بنیادی اصولوں کو سمجھا جائے جو مؤثر MCP ترقی کی رہنمائی کرتے ہیں:

1. **معیاری مواصلات**: MCP اپنی بنیاد کے طور پر JSON-RPC 2.0 استعمال کرتا ہے، جو تمام عمل درآمدات میں درخواستوں، جوابات، اور ایرر ہینڈلنگ کے لیے ایک مستقل فارمیٹ فراہم کرتا ہے۔

2. **صارف مرکزیت طراحی**: ہمیشہ اپنے MCP عمل درآمدات میں صارف کی رضا، کنٹرول، اور شفافیت کو ترجیح دیں۔

3. **سلامتی پہلے**: مضبوط سلامتی کے اقدامات نافذ کریں جن میں تصدیق، اجازت، توثیق، اور ریٹ لمیٹنگ شامل ہو۔

4. **ماڈیولر فن تعمیر**: اپنے MCP سرورز کو ماڈیولر انداز میں ڈیزائن کریں، جہاں ہر آلہ اور وسیلہ کا واضح، مرکوز مقصد ہو۔

5. **واضح حالت**: MCP `2026-07-28` پروٹوکول کی سطح پر بے حالت ہے۔
   جب ورک فلو کو کراس کال حالت کی ضرورت ہو، تو واضح ہینڈلز یا
   عام آلے کے دلائل استعمال کریں جنہیں مستقل ایپلیکیشن حالت کی حمایت حاصل ہو۔

## سرکاری MCP بہترین طریقے

مندرجہ ذیل بہترین طریقے سرکاری ماڈل کانٹیکسٹ پروٹوکول دستاویزات سے اخذ کیے گئے ہیں:

### سلامتی کے بہترین طریقے

1. **صارف کی رضا اور کنٹرول**: کسی بھی ڈیٹا تک رسائی یا آپریشن انجام دینے سے پہلے ہمیشہ واضح صارف کی رضا حاصل کریں۔ یہ واضح کنٹرول فراہم کریں کہ کون سا ڈیٹا شیئر کیا جاتا ہے اور کون سے عمل مجاز ہیں۔

2. **ڈیٹا کی رازداری**: صرف واضح رضا کے ساتھ صارف کا ڈیٹا ظاہر کریں اور اسے مناسب رسائی کنٹرولز سے محفوظ رکھیں۔ غیر مجاز ڈیٹا ترسیل کے خلاف حفاظت کریں۔

3. **آلے کی حفاظت**: کسی بھی آلے کو بلانے سے پہلے واضح صارف کی رضا درکار ہے۔ یقینی بنائیں کہ صارفین ہر آلے کی فعالیت کو سمجھیں اور مضبوط سلامتی کی حدود نافذ کریں۔

4. **آلے کی اجازت کنٹرول**: طے کریں کہ ماڈل ہر درخواست اور اجازت سیاق و سباق کے لیے کون سے آلات استعمال کر سکتا ہے، اس بات کو یقینی بنائیں کہ صرف واضح طور پر مجاز آلات تک رسائی حاصل ہو۔



5. **تصدیق**: آلات، وسائل، یا حساس آپریشنز تک رسائی سے پہلے مناسب تصدیق کی ضرورت ہوتی ہے، جیسے API کیز، OAuth ٹوکنز، یا دیگر محفوظ تصدیقی طریقے۔

6. **پیرامیٹر توثیق**: تمام آلے کی کالز کے لیے توثیق نافذ کریں تاکہ خراب یا بدنیتی پر مبنی ان پٹ کے آلات کی عمل درآمد تک پہنچنے سے روکا جا سکے۔

7. **ریٹ لمیٹنگ**: غلط استعمال کو روکنے اور سرور وسائل کے منصفانہ استعمال کو یقینی بنانے کے لیے ریٹ لمیٹنگ نافذ کریں۔

### عمل درآمد کے بہترین طریقے

1. **صلاحیت کی گفت و شنید**: سپورٹڈ پروٹوکول ورژنز اور صلاحیتوں پر بات چیت کریں۔ MCP `2026-07-28` میں، ہر درخواست خود مختار ہوتی ہے اور `server/discover` استعمال کر سکتی ہے؛ پرانے ریویژن initialization handshake استعمال کرتے ہیں۔



2. **آلے کا ڈیزائن**: ایسے مرکوز آلات تیار کریں جو ایک کام بخوبی انجام دیں، بجائے اس کے کہ ایسے بڑے آلات تیار کریں جو متعدد پہلوؤں کو سنبھالیں۔

3. **ایرر ہینڈلنگ**: معیاری ایرر پیغامات اور کوڈز نافذ کریں تاکہ مسائل کی تشخیص میں مدد ملے، ناکامیوں کو ہنر مندی سے سنبھالا جا سکے، اور قابل عمل تاثرات فراہم کیے جا سکیں۔

4. **آبزرویبیلٹی**: stdio تجزیہ کے لیے `stderr` استعمال کریں اور ساخت شدہ آبزرویبیلٹی کے لیے OpenTelemetry استعمال کریں۔ MCP لاگنگ فیچر `2026-07-28` وضاحت میں ختم کر دیا گیا ہے۔



5. **ترقی کا سراغ لگانا**: طویل مدتی آپریشنز کے لیے، پیش رفت کی اپ ڈیٹس رپورٹ کریں تاکہ جوابدہ صارف انٹرفیسز ممکن ہوں۔

6. **درخواست کی منسوخی**: کلائنٹس کو اجازت دیں کہ وہ ایسے ان فلائٹ درخواستوں کو منسوخ کر سکیں جو اب درکار نہیں یا زیادہ وقت لے رہی ہوں۔

## اضافی حوالہ جات

MCP کے بہترین طریقوں پر تازہ ترین معلومات کے لیے، رجوع کریں:

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)][mcp-2026-spec]
- [Previous MCP Specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Tasks Extension][mcp-tasks-extension]
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - سلامتی کے خطرات اور ان کے تدارک
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - عملی سلامتی کی تربیت

### اعتماد پذیری ساتھی سبق

عمومی ری ٹرائی لوپس ایسے آلات کے لیے غیر محفوظ ہیں جو ٹکٹس، ادائیگیاں، پیغامات، تعیناتیاں، یا دیگر حقیقی دنیا کے اثرات پیدا کرتے ہیں۔
ایک جواب اثرات کے کمٹ ہونے کے بعد کھو بھی سکتا ہے۔


اعتماد پذیری ساتھی سبق کا استعمال کریں،
[MCP آلے کے لیے محفوظ ری ٹرائیز: ایک اعتماد پذیری سائڈ کار پیٹرن][reliability-sidecar],
تاکہ آپ مستحکم آپریشن کیز، نقل داخلہ، چیک پوائنٹنگ، مفاہمت، ثبوت کی سطحیں، اور ناکامی کا انجیکشن سیکھ سکیں۔


[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## عملی عمل درآمد کی مثالیں

### آلے کے ڈیزائن کے بہترین طریقے

#### 1. ایک ذمہ داری کا اصول

ہر MCP آلے کا ایک واضح، مرکوز مقصد ہونا چاہیے۔ متعدد پہلوؤں کو سنبھالنے کی کوشش کرنے والے بڑے آلات بنانے کی بجائے، ایسے خصوصی آلات تیار کریں جو مخصوص کاموں میں مہارت رکھتے ہوں۔

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

#### 2. یکساں ایرر ہینڈلنگ

مضبوط ایرر ہینڈلنگ نافذ کریں جس میں معلوماتی ایرر پیغامات اور مناسب بازیابی کے طریقے شامل ہوں۔

```python
# جامع نقص کی سنبھال کے ساتھ پائتھن کی مثال
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # پیرا میٹر کی تصدیق
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # سیکیورٹی کی تصدیق
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # ڈیٹا بیس آپریشن ٹائم آؤٹ کے ساتھ
                async with timeout(10):  # 10 سیکنڈ کا ٹائم آؤٹ
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # کنکشن کی خرابی عارضی ہو سکتی ہیں
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # سوال کی خرابی ممکنہ طور پر کلائنٹ کی خرابی ہے
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # مخصوص ٹول کی خرابیوں کو گزرنے دیں
            raise
        except Exception as e:
            # غیر متوقع خرابیوں کے لیے جامع گرفت
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # ایس کیو ایل انجیکشن کی نشاندہی کا نفاذ
        pass
        
    def _log_error(self, message, error):
        # نقصاندہی کے ریکارڈ کا نفاذ
        pass
```

#### 3. پیرامیٹر کی توثیق

ہمیشہ پیرامیٹرز کی مکمل توثیق کریں تاکہ خراب یا بدنیتی پر مبنی ان پٹ کو روکا جا سکے۔

```javascript
// جاوا اسکرپٹ/ٹائپ اسکرپٹ کی مثال تفصیلی پیرامیٹر کی توثیق کے ساتھ
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
    // 1. پیرامیٹر کی موجودگی کی توثیق کریں
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. پیرامیٹر کی اقسام کی توثیق کریں
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. پیرامیٹر کے اقدار کی توثیق کریں
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. تحریری آپریشن کے لیے مواد کی موجودگی کی توثیق کریں
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. راستے کی سلامتی کی توثیق
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // توثیق شدہ پیرامیٹرز کی بنیاد پر نفاذ
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // راستے کی سلامتی کی جانچ کا نفاذ
    // ...
  }
}
```

### سلامتی کے عمل درآمد کی مثالیں

#### 1. تصدیق اور اجازت

```java
// جاوا کی مثال مصدقہ کاری اور اجازت کے ساتھ
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // انحصار انجیکشن
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
        // 1. تصدیقی سیاق و سباق نکالیں
        String authToken = request.getContext().getAuthToken();
        
        // 2. صارف کی تصدیق کریں
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. مخصوص آپریشن کے لیے اجازت چیک کریں
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. مجاز آپریشن کے ساتھ آگے بڑھیں
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

#### 2. ریٹ لمیٹنگ

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

## جانچ کے بہترین طریقے

### 1. MCP آلات کی یونٹ جانچ

ہمیشہ اپنے آلات کو تنہا ٹیسٹ کریں، بیرونی انحصار کو موک کرکے:

```typescript
// ٹائپ اسکرپٹ کی مثال ایک ٹول یونٹ ٹیسٹ کی
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // ایک جعلی موسم کی خدمت بنائیں
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // ٹول کو جعلی انحصار کے ساتھ بنائیں
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // ترتیب دیں
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // عمل کریں
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // تصدیق کریں
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // ترتیب دیں
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // عمل اور تصدیق کریں
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. انٹیگریشن ٹیسٹنگ

کلائنٹ درخواستوں سے لے کر سرور جوابات تک مکمل عمل کا ٹیسٹ کریں:

```python
# پائتھن انٹیگریشن ٹیسٹ کی مثال
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # ایک ٹیسٹ سرور شروع کریں
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # ایک کلائنٹ بنائیں
        client = McpClient("http://localhost:5000")
        
        # ٹیسٹ ٹول کی دریافت کریں
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # ٹیسٹ ٹول کی اجرا کریں
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # جواب کی تصدیق کریں
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # صفائی کریں
        await server.stop()
```

## کارکردگی کی بہتری

### 1. کیشنگ کی حکمت عملیاں

تاخیر اور وسائل کے استعمال کو کم کرنے کے لیے مناسب کیشنگ نافذ کریں:


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

#### 2. انحصار انجیکشن اور جانچ پذیری

ایسے آلات ڈیزائن کریں جو اپنے انحصارات کنسٹرکٹر انجیکشن کے ذریعہ وصول کریں، اس طرح انہیں جانچنے اور ترتیب دینے کے قابل بنایا جا سکے:

```java
// جاوا کی مثال ساتھ انحصار انجکشن
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // کنسٹرکٹر کے ذریعے انجکت شدہ انحصار
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // ٹول کا نفاذ
    // ...
}
```

#### 3. تشکیل پذیر آلات

ایسے آلات ڈیزائن کریں جو ایک ساتھ جوڑے جا سکیں تاکہ مزید پیچیدہ ورک فلو بنائے جا سکیں:

```python
# پائتھن کی مثال جو قابل ملاپ اوزار دکھا رہی ہے
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # نفاذ...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # یہ آلہ dataFetch آلے کے نتائج استعمال کر سکتا ہے
    async def execute_async(self, request):
        # نفاذ...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # یہ آلہ dataAnalysis آلے کے نتائج استعمال کر سکتا ہے
    async def execute_async(self, request):
        # نفاذ...
        pass

# یہ اوزار خود مختار طور پر یا ورک فلو کے حصہ کے طور پر استعمال کیے جا سکتے ہیں
```

### اسکیمہ ڈیزائن کی بہترین مشقیں

اسکیمہ ماڈل اور آپ کے آلے کے درمیان معاہدہ ہے۔ اچھی طرح ڈیزائن کیے گئے اسکیمے بہتر آلے کی قابلِ استعمالیت کا باعث بنتے ہیں۔

#### 1. واضح پیرامیٹر کی تفصیلات

ہر پیرامیٹر کے لئے وضاحتی معلومات ہمیشہ شامل کریں:

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

#### 2. توثیقی پابندیاں

غلط ان پٹ کو روکنے کے لیے توثیقی پابندیاں شامل کریں:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // ای میل پراپرٹی فارمیٹ کی تصدیق کے ساتھ
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // عمر پراپرٹی عددی پابندیوں کے ساتھ
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // گنتی کی گئی پراپرٹی
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

#### 3. مستقل واپسی کے ڈھانچے

نتائج کی تشریح کو آسان بنانے کے لیے آپ کے جواب کے ڈھانچے میں مستقل مزاجی برقرار رکھیں:

```python
async def execute_async(self, request):
    try:
        # درخواست کو پروسیس کریں
        results = await self._search_database(request.parameters["query"])
        
        # ہمیشہ ایک مستقل ساخت واپس کریں
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

### ایرر ہینڈلنگ

معتبر ایرر ہینڈلنگ MCP آلات کی پائداری کو برقرار رکھنے کے لیے اہم ہے۔

#### 1. نرم مزاج ایرر ہینڈلنگ

مناسب سطحوں پر ایرر کو سنبھالیں اور معلوماتی پیغامات فراہم کریں:

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

#### 2. منظم ایرر جوابات

جب ممکن ہو تو منظم ایرر معلومات واپس کریں:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // عمل درآمد
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
        
        // دیگر استثنائیں ToolExecutionException کے طور پر دوبارہ پھینکیں
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. ریٹری لاجک

عمومی ریٹری لاجک صرف پڑھنے-صرف کالز یا ایسی کارروائیوں کے لیے استعمال کریں جن کے
نیچے کے معاہدے پہلے ہی مطلق ہوں۔ مؤثر کارروائیوں کے لیے، درخواست بھیجنے کے بعد
ٹائم آؤٹ مبہم ہوتا ہے۔ مقتدر اسٹیٹ کو درست کریں اور
دوبارہ چلانے سے پہلے ایک ہی مستحکم آپریشن کلید کو دوبارہ استعمال کریں۔ دیکھیں
[reliability sidecar companion lesson](./reliability-sidecars/README.md).

درج ذیل محدود ریٹری لوپ پڑھنے-صرف تلاش کے لیے مناسب ہے:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # سیکنڈ
    
    while retry_count < max_retries:
        try:
            # ایک ریڈ اونلی بیرونی API کال کریں
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # نمایاں بیک آف
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # غیر عارضی خرابی، دوبارہ کوشش نہ کریں
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### کارکردگی کی اصلاح

#### 1. کیشنگ

مہنگی کارروائیوں کے لیے کیشنگ کو نافذ کریں:

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

#### 2. غیر ہم آہنگی پراسیسنگ

آئی/او-باؤنڈ کارروائیوں کے لیے غیر ہم آہنگی پروگرامنگ نمونوں کا استعمال کریں:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // طویل مدتی آپریشنز کے لیے فوری طور پر پراسیسنگ ID لوٹائیں
        String processId = UUID.randomUUID().toString();
        
        // اسینک پروسیسنگ شروع کریں
        CompletableFuture.runAsync(() -> {
            try {
                // طویل مدتی آپریشن انجام دیں
                documentService.processDocument(documentId);
                
                // اسٹیٹس اپڈیٹ کریں (عام طور پر ڈیٹا بیس میں محفوظ کی جاتی ہے)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // عمل کی ID کے ساتھ فوری جواب دیں
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // ساتھی اسٹیٹس چیک ٹول
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

#### 3. وسائل کی تھروٹلنگ

اوورلوڈ روکنے کے لیے وسائل کی تھروٹلنگ نافذ کریں:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # ہر سیکنڈ 5 درخواستیں اجازت دیں
            bucket_size=10        # ایک دم میں 10 درخواستیں تک کی اجازت دیں
        )
    
    async def execute_async(self, request):
        # چیک کریں کہ کیا ہم آگے بڑھ سکتے ہیں یا انتظار کرنا ہوگا
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # اگر انتظار بہت زیادہ ہو جائے
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # مناسب تأخیر کے وقت کے لئے انتظار کریں
                await asyncio.sleep(delay)
        
        # ایک ٹوکن استعمال کریں اور درخواست کے ساتھ آگے بڑھیں
        self.rate_limiter.consume()
        
        # API کو کال کریں
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
            
            # اگلے دستیاب ٹوکن تک کا وقت حساب کریں
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # گذرے ہوئے وقت کی بنیاد پر نئے ٹوکن شامل کریں
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### سیکیورٹی کی بہترین مشقیں

#### 1. ان پٹ کی توثیق

ان پٹ پیرامیٹرز کی مکمل جانچ کریں:

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

#### 2. اجازت کی جانچ

مناسب اجازت کی جانچ نافذ کریں:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // درخواست سے صارف کا سیاق و سباق حاصل کریں
    UserContext user = request.getContext().getUserContext();
    
    // چیک کریں کہ آیا صارف کے پاس مطلوبہ اجازتیں ہیں
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // مخصوص وسائل کے لیے، اس وسیلہ تک رسائی کی جانچ کریں
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // آلے کے نفاذ کے ساتھ آگے بڑھیں
    // ...
}
```

#### 3. حساس ڈیٹا کی ہینڈلنگ

حساس ڈیٹا کو احتیاط سے سنبھالیں:

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
        
        # صارف کا ڈیٹا حاصل کریں
        user_data = await self.user_service.get_user_data(user_id)
        
        # حساس فیلڈز کو فلٹر کریں جب تک کہ کھلے عام درخواست نہ کی گئی ہو اور اجازت نہ دی گئی ہو
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # درخواست کے سیاق و سباق میں اجازت کی سطح چیک کریں
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # اصل کو تبدیل کرنے سے بچنے کے لیے ایک نقل بنائیں
        redacted = user_data.copy()
        
        # مخصوص حساس فیلڈز کو مسخ کریں
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # نیسٹڈ حساس ڈیٹا کو مسخ کریں
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP آلات کے لیے جانچ کی بہترین مشقیں

مکمل جانچ اس بات کو یقینی بناتی ہے کہ MCP آلات درست طریقے سے کام کریں، ایج کیسز کو سنبھالیں، اور نظام کے باقی حصے کے ساتھ مناسب انضمام کریں۔

### یونٹ ٹیسٹنگ

#### 1. ہر آلے کی علیحدہ جانچ کریں

ہر آلے کی فعالیت کے لیے مخصوص ٹیسٹ بنائیں:

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

#### 2. اسکیمہ توثیق کی جانچ

جانچ کریں کہ اسکیمے درست ہیں اور پابندیاں مناسب طریقے سے لاگو کر رہے ہیں:

```java
@Test
public void testSchemaValidation() {
    // ٹول کی مثال بنائیں
    SearchTool searchTool = new SearchTool();
    
    // خاکہ حاصل کریں
    Object schema = searchTool.getSchema();
    
    // تصدیق کے لئے خاکہ کو JSON میں تبدیل کریں
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // تصدیق کریں کہ خاکہ درست JSONSchema ہے
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // درست پیرا میٹرز کا آزمائش کریں
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // مطلوبہ پیرا میٹر کے بغیر آزمائش کریں
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // غلط پیرا میٹر قسم کا آزمائش کریں
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. ایرر ہینڈلنگ ٹیسٹس

مخصوص ایرر حالات کے لیے ٹیسٹ بنائیں:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # ترتیب دیں
    tool = ApiTool(timeout=0.1)  # بہت کم وقت ختم ہونا
    
    # ایک درخواست کی نقاب کشائی کریں جو وقت ختم ہو جائے گی
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # وقت ختم ہونے سے زیادہ طویل
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # عمل کریں اور یقین دہانی کریں
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # استثناء کے پیغام کی تصدیق کریں
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # ترتیب دیں
    tool = ApiTool()
    
    # ایک حد شدہ ردعمل کی نقاب کشائی کریں
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
        
        # عمل کریں اور یقین دہانی کریں
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # استثناء میں حد رفتار کی معلومات شامل ہونے کی تصدیق کریں
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### انضمامی جانچ

#### 1. ٹول چین ٹیسٹنگ

متوقع امتزاج میں مل کر کام کرنے والے آلات کی جانچ کریں:

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

#### 2. MCP سرور کی جانچ

مکمل ٹول رجسٹریشن اور عمل درآمد کے ساتھ MCP سرور کی جانچ کریں:

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
        // دریافت کے اینڈ پوائنٹ کا ٹیسٹ کریں
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // ٹول کی درخواست بنائیں
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // درخواست بھیجیں اور جواب کی تصدیق کریں
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // غلط ٹول کی درخواست بنائیں
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // پیرامیٹر "b" غائب ہے
        request.put("parameters", parameters);
        
        // درخواست بھیجیں اور غلطی کے جواب کی تصدیق کریں
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. مکمل ورک فلو کی جانچ

ماڈل پرامپٹ سے لے کر ٹول کے عمل درآمد تک مکمل ورک فلو کی جانچ کریں:


```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # ترتیب دیں - MCP کلائنٹ اور ماک ماڈل ترتیب دیں
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # ماک ماڈل جوابات
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
    
    # ماک موسم کا آلہ جواب
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
        
        # عمل کریں
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # یقین دہانی کریں
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### کارکردگی کی جانچ

#### 1. لوڈ ٹیسٹنگ

جانچیں کہ آپ کا MCP سرور کتنے متوازی درخواستیں سنبھال سکتا ہے:

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

#### 2. اسٹریس ٹیسٹنگ

نظام کو انتہائی بوجھ کے تحت جانچیں:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // جے میٹر کو اسٹریس ٹیسٹنگ کے لیے سیٹ اپ کریں
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // جے میٹر ٹیسٹ پلان کو ترتیب دیں
    HashTree testPlanTree = new HashTree();
    
    // ٹیسٹ پلان، تھریڈ گروپ، سیمپلرز وغیرہ بنائیں
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // ٹول کے نفاذ کے لیے HTTP سیمپلر شامل کریں
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // لسنرز شامل کریں
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // ٹیسٹ چلائیں
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // نتائج کی توثیق کریں
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // اوسط ردعمل کا وقت < 200 ملی سیکنڈ
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90 ویں فیصدی < 500 ملی سیکنڈ
}
```

#### 3. مانیٹرنگ اور پروفائلنگ

طویل مدتی کارکردگی کے تجزیے کے لیے مانیٹرنگ قائم کریں:

```python
# ایم سی پی سرور کے لیے مانیٹرنگ کو ترتیب دیں
def configure_monitoring(server):
    # پرومیٹھیئس میٹرکس کو سیٹ اپ کریں
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
    
    # میٹرکس کی وقت بندی اور ریکارڈنگ کے لیے مڈل ویئر شامل کریں
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # میٹرکس اینڈ پوائنٹ کو ظاہر کریں
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP ورک فلو ڈیزائن پیٹرنز

اچھی طرح سے ڈیزائن کیے گئے MCP ورک فلو افادیت، بھروسے مندی، اور دیکھ بھال کی صلاحیت کو بہتر بناتے ہیں۔ یہاں کلیدی پیٹرنز درج ہیں جن پر عمل کرنا چاہیے:

### 1. چین آف ٹولز پیٹرن

متعدد ٹولز کو ایک سلسلہ وار طور پر مربوط کریں جہاں ہر ٹول کی آؤٹ پٹ اگلے کے ان پٹ بن جائے:

```python
# پائتھن چین آف ٹولز کی تنفیذ
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # تسلسل میں چلانے کے لیے ٹولز کے ناموں کی فہرست
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # چین میں ہر ٹول کو چلائیں، پچھلا نتیجہ پاس کریں
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # نتیجہ محفوظ کریں اور اگلے ٹول کے لیے ان پٹ کے طور پر استعمال کریں
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# استعمال کی مثال
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

### 2. ڈسپیچر پیٹرن

ایک مرکزی ٹول استعمال کریں جو ان پٹ کی بنیاد پر مخصوص ٹولز کو تقسیم کرے:

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

### 3. متوازی پروسیسنگ پیٹرن

افادیت کے لیے متعدد ٹولز کو بیک وقت چلائیں:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // مرحلہ 1: ڈیٹا سیٹ میٹا ڈیٹا حاصل کریں (ہم وقت ساز)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // مرحلہ 2: متعدد تجزیے متوازی طور پر شروع کریں
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
        
        // تمام متوازی کاموں کے مکمل ہونے کا انتظار کریں
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // تکمیل کے انتظار میں رہیں
        
        // مرحلہ 3: نتائج کو یکجا کریں
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // مرحلہ 4: خلاصہ رپورٹ تیار کریں
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // مکمل ورک فلو کے نتائج واپس کریں
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. ایرر ریکوری پیٹرن

ٹول ناکامیوں کے لیے نرم تبدیلیاں نافذ کریں:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # پہلے بنیادی آلے کو آزمائیں
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # ناکامی کو لاگ کریں
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # ثانوی آلے کی طرف رجوع کریں
            try:
                # شايد فالبیک آلے کے لئے پیرامیٹرز کی تبدیلی کی ضرورت ہو
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # دونوں آلے ناکام ہوگئے
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # یہ عمل درآمد مخصوص آلے پر منحصر ہوگا
        # اس مثال کے لئے، ہم صرف اصل پیرامیٹرز واپس کریں گے
        return params

# مثال کا استعمال
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # بنیادی (ادائیگی والا) موسم کا API
        "basicWeatherService",    # فالبیک (مفت) موسم کا API
        {"location": location}
    )
```

### 5. ورک فلو کمپوزیشن پیٹرن

آسان ورک فلو کو کمپوز کرکے پیچیدہ ورک فلو تعمیر کریں:

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

# MCP سرورز کی جانچ: بہترین طریقے اور اعلیٰ تجاویز

## جائزہ

جانچ معتبر، اعلیٰ معیار کے MCP سرورز کی ترقی کا ایک اہم پہلو ہے۔ یہ رہنما آپ کے MCP سرورز کی پورے ترقیاتی عمل کے دوران یونٹ ٹیسٹس سے لے کر انٹیگریشن ٹیسٹس اور اختتامی سے اختتامی تصدیق تک جامع بہترین طریقے اور تجاویز فراہم کرتی ہے۔

## MCP سرورز کے لیے جانچ کیوں ضروری ہے

MCP سرورز AI ماڈلز اور کلائنٹ ایپلیکیشنز کے درمیان ایک اہم مڈل ویئر کے طور پر کام کرتے ہیں۔ جامع جانچ یقینی بناتی ہے کہ:

- پروڈکشن ماحول میں بھروسے مندی
- درخواستوں اور جوابات کی درست ہینڈلنگ
- MCP مواصفات کا مناسب نفاذ
- ناکامیوں اور حدی معاملات کے خلاف مضبوطی
- مختلف بوجھ کے تحت یکساں کارکردگی

## MCP سرورز کے لیے یونٹ ٹیسٹنگ

### یونٹ ٹیسٹنگ (بنیاد)

یونٹ ٹیسٹ آپ کے MCP سرور کے ہر ایک جزو کی علیحدہ جانچ کرتے ہیں۔

#### کیا جانچنا ہے

1. **وسائل کے ہینڈلرز**: ہر وسائل کی ہینڈلر کی منطق کو آزادانہ طور پر جانچیں
2. **ٹول کی تنفیذ**: مختلف ان پٹس کے ساتھ ٹول کے رویے کی تصدیق کریں
3. **پرومپٹ ٹیمپلیٹس**: یقین کریں کہ پرومپٹ ٹیمپلیٹس درست طریقے سے رینڈر ہوتے ہیں
4. **اسکیمہ کی توثیق**: پیرامیٹر کی توثیق کی منطق کو جانچیں
5. **ایرر ہینڈلنگ**: نا جائز ان پٹس کے لیے ایرر جوابات کی تصدیق کریں

#### یونٹ ٹیسٹنگ کے لیے بہترین طریقے

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
# پائیتھن میں کیلکولیٹر ٹول کے لیے مثال یونٹ ٹیسٹ
def test_calculator_tool_add():
    # بندوبست کریں
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # عمل کریں
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # یقین دہانی کریں
    assert result["value"] == 12
```

### انٹیگریشن ٹیسٹنگ (درمیانی تہہ)

انٹیگریشن ٹیسٹس آپ کے MCP سرور کے اجزاء کے مابین تعاملات کی جانچ کرتے ہیں۔

#### کیا جانچنا ہے

1. **سرور کی شروعات**: مختلف کنفیگریشنز کے ساتھ سرور کے آغاز کی جانچ کریں
2. **روٹ رجسٹریشن**: تمام اینڈپوائنٹس کی درست رجسٹریشن کی تصدیق کریں
3. **درخواست کا عمل**: درخواست-جواب کے مکمل چکر کی جانچ کریں
4. **ایرر کی منتقلی**: یقینی بنائیں کہ غلطیاں مناسب طریقے سے تمام اجزاء میں سنبھالی جاتی ہیں
5. **توثیق اور اجازت**: سیکورٹی میکانزم کی جانچ کریں

#### انٹیگریشن ٹیسٹنگ کے لیے بہترین طریقے

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

### اختتامی سے اختتامی جانچ (اوپری تہہ)

اختتامی سے اختتامی ٹیسٹس مکمل نظام کے رویے کی جانچ کرتے ہیں، کلائنٹ سے سرور تک۔

#### کیا جانچنا ہے

1. **کلائنٹ-سرور مواصلات**: مکمل درخواست-جواب کے چکروں کی جانچ کریں
2. **حقیقی کلائنٹ SDKs**: اصل کلائنٹ تنفیذات کے ساتھ جانچ کریں
3. **لوڈ کے تحت کارکردگی**: متعدد متوازی درخواستوں کے ساتھ رویے کی تصدیق کریں
4. **ایرر کی بحالی**: ناکامیوں سے نظام کی بحالی کی جانچ کریں

5. **طویل مدتی آپریشنز**: اسٹریمینگ اور طویل آپریشنز کی ہینڈلنگ کی تصدیق کریں

#### ای2ای ٹیسٹنگ کے لیے بہترین طریقے

```typescript
// ٹائپ اسکرپٹ میں کلائنٹ کے ساتھ مثال E2E ٹیسٹ
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // ٹیسٹ ماحول میں سرور شروع کریں
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // عمل کریں
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // تصدیق کریں
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP ٹیسٹنگ کے لیے نقلی حکمت عملیاں

ٹیسٹنگ کے دوران اجزاء کو الگ تھلگ کرنے کے لیے نقلی کرنا ضروری ہے۔

### نقلی کرنے کے لیے اجزاء

1. **بیرونی AI ماڈلز**: قابل پیش گوئی ٹیسٹنگ کے لیے ماڈل کے جوابات کی نقلی کریں
2. **بیرونی خدمات**: API انحصارات کی نقلی (ڈیٹا بیس، تیسرے فریق کی خدمات)
3. **تصدیقی خدمات**: شناخت فراہم کرنے والوں کی نقلی کریں
4. **وسیلہ فراہم کرنے والے**: مہنگے وسائل کے ہینڈلرز کی نقلی کریں

### مثال: AI ماڈل کے جواب کی نقلی

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
# پائتھن کی مثال unittest.mock کے ساتھ
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # موک کو ترتیب دیں
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # ٹیسٹ میں موک کا استعمال کریں
    server = McpServer(model_client=mock_model)
    # ٹیسٹ جاری رکھیں
```

## کارکردگی کی جانچ

پیداوار MCP سرورز کے لیے کارکردگی کی جانچ بہت اہم ہے۔

### کیا ماپنا ہے

1. **لاکافتہ**: درخواستوں کے جوابی وقت
2. **تھروپٹ**: فی سیکنڈ ہینڈل کی گئی درخواستیں
3. **وسائل کا استعمال**: CPU، میموری، نیٹ ورک کا استعمال
4. **ہم وقتی ہینڈلنگ**: متوازی درخواستوں کے تحت رویہ
5. **اسکیلنگ کی خصوصیات**: بوجھ بڑھنے پر کارکردگی

### کارکردگی کی جانچ کے لیے اوزار

- **k6**: اوپن سورس لوڈ ٹیسٹنگ ٹول
- **JMeter**: جامع کارکردگی کی جانچ
- **Locust**: پائتھون پر مبنی لوڈ ٹیسٹنگ
- **Azure Load Testing**: کلاؤڈ پر مبنی کارکردگی کی جانچ

### مثال: k6 کے ساتھ بنیادی لوڈ ٹیسٹ

```javascript
// MCP سرور کے لوڈ ٹیسٹنگ کے لیے k6 اسکرپٹ
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // ۱۰ ورچوئل صارفین
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

## MCP سرورز کے لیے ٹیسٹ آٹومیشن

آپ کے ٹیسٹ کو خودکار بنانے سے مستقل معیار اور تیز تر فیڈبیک لوپ یقینی بنتے ہیں۔

### CI/CD انضمام

1. **پُل درخواستوں پر یونٹ ٹیسٹ چلائیں**: یقینی بنائیں کہ کوڈ تبدیلیاں موجودہ فعالیت کو خراب نہ کریں
2. **اسٹیجنگ میں انضمامی ٹیسٹ**: پیشگی پیداوار ماحول میں انضمامی ٹیسٹ چلائیں
3. **کارکردگی کی بنچ مارکس**: پس ماندگی کو پکڑنے کے لیے کارکردگی کے معیار کو برقرار رکھیں
4. **سیکیورٹی اسکینز**: پائپ لائن کے حصے کے طور پر سیکیورٹی ٹیسٹنگ کو خودکار کریں

### مثال CI پائپ لائن (GitHub Actions)

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

## MCP وضاحت کے مطابق جانچ

تصدیق کریں کہ آپ کا سرور MCP وضاحت کو صحیح طریقے سے نافذ کرتا ہے۔

### کلیدی تعمیل کے علاقے

1. **API اینڈ پوائنٹس**: ضروری اینڈ پوائنٹس کی جانچ کریں (/resources, /tools, وغیرہ)
2. **درخواست/جواب کا فارمیٹ**: اسکیمہ کی تعمیل کی توثیق کریں
3. **ایرر کوڈز**: مختلف حالات کے لیے درست اسٹیٹس کوڈز کی تصدیق کریں
4. **مواد کی اقسام**: مختلف مواد کی اقسام کی ہینڈلنگ کی جانچ کریں
5. **تصدیق کے عمل**: وضاحت کے مطابق توثیقی طریقہ کار کی تصدیق کریں

### تعمیل کا ٹیسٹ سوئٹ

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

## MCP سرور کی موثر جانچ کے لیے ٹاپ 10 ٹپس

1. **ٹول کی تعریفوں کو الگ سے ٹیسٹ کریں**: ٹول کی منطق سے اسکیمہ کی تعریفوں کی الگ سے تصدیق کریں
2. **پیرامیٹرائزڈ ٹیسٹ استعمال کریں**: مختلف ان پٹس بشمول ایج کیسز کے ساتھ ٹولز کی جانچ کریں
3. **ایرر جوابات کی جانچ کریں**: تمام ممکنہ ایرر شرائط کے لیے مناسب ہینڈلنگ کی تصدیق کریں
4. **اجازت کے منطقی ٹیسٹ کریں**: مختلف صارف کرداروں کے لیے مناسب رسائی کنٹرول کو یقینی بنائیں
5. **ٹیسٹ کوریج مانیٹر کریں**: اہم راستہ کوڈ کی اعلیٰ کوریج کا ہدف رکھیں
6. **اسٹریمینگ جوابات کی جانچ کریں**: اسٹریمینگ مواد کی مناسب ہینڈلنگ کی تصدیق کریں
7. **نیٹ ورک مسائل کی تقلید کریں**: خراب نیٹ ورک حالات کے تحت رویے کی جانچ کریں
8. **وسیلہ کی حدود کی جانچ کریں**: کوٹہ یا ریٹ لمٹس تک پہنچنے پر رویے کی تصدیق کریں
9. **ریگریشن ٹیسٹ کو خودکار کریں**: ہر کوڈ تبدیلی پر چلنے والا سوئٹ بنائیں
10. **ٹیسٹ کیسز کی دستاویزات بنائیں**: ٹیسٹ منظرناموں کی واضح دستاویزات رکھیں

## عام ٹیسٹنگ کی غلطیاں

- **صرف خوشگوار راستے کی جانچ پر زیادہ انحصار**: یقینی بنائیں کہ ایرر کیسز کو مکمل طور پر ٹیسٹ کیا جائے
- **کارکردگی کی جانچ کو نظر انداز کرنا**: پیداوار کو متاثر کرنے والے رکاوٹوں کی شناخت کریں
- **صرف الگ تھلگ ٹیسٹنگ**: یونٹ، انضمامی، اور ای2ای ٹیسٹ کو یکجا کریں
- **ادھوری API کوریج**: یقینی بنائیں کہ تمام اینڈ پوائنٹس اور خصوصیات کی جانچ کی گئی ہو
- **ٹیسٹ ماحول کا غیر مستقل ہونا**: مستقل ماحول کے لیے کنٹینرز استعمال کریں

## نتیجہ

ایک جامع ٹیسٹنگ حکمت عملی قابل اعتماد، اعلی معیار کے MCP سرورز کی ترقی کے لیے ضروری ہے۔ اس گائیڈ میں دی گئی بہترین طریقوں اور نکات کو نافذ کر کے آپ یقینی بنا سکتے ہیں کہ آپ کی MCP امپلیمنٹیشنز اعلی ترین معیار، اعتماد اور کارکردگی کے معیار پر پورا اترتی ہیں۔


## اہم نکات

1. **ٹول ڈیزائن**: سنگل ذمہ داری اصول کی پیروی کریں، انحصاری انجیکشن استعمال کریں، اور مرکب سازی کے لیے ڈیزائن کریں
2. **اسکیمہ ڈیزائن**: واضح، اچھی دستاویزی اسکیمہ بنائیں جس میں مناسب تصدیقی قیود ہوں
3. **ایرر ہینڈلنگ**: نرم ہینڈلنگ، منظم ایرر جوابات، اور نتیجہ سے آگاہ ریٹری منطق نافذ کریں
   جوابات اور نتیجہ آگاہ ریٹری منطق
4. **کارکردگی**: کیشنگ، غیر ہم وقت پروسیسنگ، اور وسائل کی تھروٹلنگ استعمال کریں
5. **سیکیورٹی**: مکمل ان پٹ ویلیڈیشن، اجازت جانچ، اور حساس ڈیٹا کی ہینڈلنگ اپنائیں
6. **ٹیسٹنگ**: جامع یونٹ، انضمامی، اور اختتامی ٹیسٹ بنائیں
7. **ورک فلو پیٹرنز**: قائم شدہ پیٹرنز جیسے چینز، ڈسپیچرز، اور متوازی پروسیسنگ اپنائیں

## مشق

ایک MCP ٹول اور ورک فلو ڈیزائن کریں جو ایک دستاویزی پراسیسنگ سسٹم کے لیے ہو جو:

1. دستاویزات کو متعدد فارمیٹس میں قبول کرے (PDF, DOCX, TXT)
2. دستاویزات سے متن اور کلیدی معلومات نکالے
3. دستاویزات کو قسم اور مواد کے لحاظ سے درجہ بندی کرے
4. ہر دستاویز کا خلاصہ تیار کرے

اس منظرنامے کے لیے موزوں بہترین ٹول اسکیمہ، ایرر ہینڈلنگ، اور ورک فلو پیٹرن نافذ کریں۔ غور کریں کہ آپ اس نفاذ کی جانچ کیسے کریں گے۔

## وسائل

1. MCP کمیونٹی جوائن کریں [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) پر تاکہ تازہ ترین ترقیات سے باخبر رہیں
2. اوپن سورس [MCP پروجیکٹس](https://github.com/modelcontextprotocol) میں تعاون کریں
3. اپنے ادارے کی AI پہل کاریوں میں MCP اصول نافذ کریں
4. اپنی صنعت کے لیے مخصوص MCP نفاذ کو دریافت کریں۔
5. مخصوص MCP موضوعات جیسے کہ کثیرالمسیری انضمام یا انٹرپرائز ایپلیکیشن انضمام پر اعلیٰ کورسز لینے پر غور کریں۔
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) کے ذریعہ سیکھی گئی اصولوں کا استعمال کرتے ہوئے اپنے MCP ٹولز اور ورک فلو بنانے کا تجربہ کریں

## اگلا کیا ہے

اگلا: [کیس اسٹڈیز](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
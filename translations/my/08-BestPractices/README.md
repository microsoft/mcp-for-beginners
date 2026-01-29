# MCP ဖွံ့ဖြိုးရေးအကောင်းဆုံးအလေ့အကျင့်များ

[![MCP ဖွံ့ဖြိုးရေးအကောင်းဆုံးအလေ့အကျင့်များ](../../../translated_images/my/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရန် အထက်ပါပုံကို နှိပ်ပါ)_

## အကျဉ်းချုပ်

ဤသင်ခန်းစာသည် MCP server များနှင့် production ပတ်ဝန်းကျင်များတွင် feature များ ဖွံ့ဖြိုးခြင်း၊ စမ်းသပ်ခြင်းနှင့် တင်သွင်းခြင်းဆိုင်ရာ အဆင့်မြင့်အကောင်းဆုံးအလေ့အကျင့်များကို အဓိကထားပါသည်။ MCP ecosystem များသည် ရှုပ်ထွေးမှုနှင့် အရေးပါမှုများ တိုးလာသည့်အခါတွင် စံသတ်မှတ်ထားသော ပုံစံများကို လိုက်နာခြင်းသည် ယုံကြည်စိတ်ချရမှု၊ ထိန်းသိမ်းနိုင်မှုနှင့် အပြန်အလှန်လုပ်ဆောင်နိုင်မှုကို အာမခံပေးပါသည်။ ဤသင်ခန်းစာသည် အမှန်တကယ် MCP implementation များမှ ရရှိသော အတွေ့အကြုံများကို စုစည်းထားပြီး သင်၏ server များကို သုံးစွဲသူများအတွက် ထိရောက်သော resource များ၊ prompt များနှင့် tool များဖြင့် ခိုင်ခံ့ပြီး ထိရောက်သော server များ ဖန်တီးနိုင်ရန် လမ်းညွှန်ပေးပါသည်။

## သင်ခန်းစာ၏ ရည်မှန်းချက်များ

ဤသင်ခန်းစာ၏ နောက်ဆုံးတွင် သင်သည် အောက်ပါအရာများကို လုပ်ဆောင်နိုင်မည်ဖြစ်သည်-

- MCP server နှင့် feature design တွင် စက်မှုလုပ်ငန်း၏ အကောင်းဆုံးအလေ့အကျင့်များကို အသုံးချနိုင်ခြင်း
- MCP server များအတွက် စုံလင်သော စမ်းသပ်မှုမဟာဗျူဟာများ ဖန်တီးနိုင်ခြင်း
- ရှုပ်ထွေးသော MCP application များအတွက် ထိရောက်ပြီး ပြန်အသုံးပြုနိုင်သော workflow ပုံစံများ ဖန်တီးနိုင်ခြင်း
- MCP server များတွင် မှားယွင်းမှုကို ကိုင်တွယ်ခြင်း၊ log ထုတ်ခြင်းနှင့် observability ကို သင့်တော်စွာ အကောင်အထည်ဖော်နိုင်ခြင်း
- MCP implementation များကို စွမ်းဆောင်ရည်၊ လုံခြုံရေးနှင့် ထိန်းသိမ်းနိုင်မှုအတွက် အကောင်းဆုံး optimize လုပ်နိုင်ခြင်း

## MCP အခြေခံအချက်များ

အကောင်အထည်ဖော်မှုဆိုင်ရာ အထူးအလေ့အကျင့်များကို စတင်မလုပ်မီ MCP ဖွံ့ဖြိုးမှုကို ထိရောက်စွာ လမ်းညွှန်ပေးသော အခြေခံအချက်များကို နားလည်ထားရန် အရေးကြီးပါသည်-

1. **စံပြဆက်သွယ်မှု**: MCP သည် JSON-RPC 2.0 ကို အခြေခံထားပြီး request များ၊ response များနှင့် error ကိုင်တွယ်မှုများအတွက် အဆင်ပြေသော format ကို ပေးစွမ်းပါသည်။

2. **အသုံးပြုသူအခြေခံဒီဇိုင်း**: MCP implementation များတွင် အသုံးပြုသူ၏ သဘောတူညီမှု၊ ထိန်းချုပ်မှုနှင့် ပွင့်လင်းမြင်သာမှုကို အမြဲဦးစားပေးပါ။

3. **လုံခြုံရေးဦးစားပေးမှု**: authentication, authorization, validation နှင့် rate limiting အပါအဝင် ခိုင်ခံ့သော လုံခြုံရေးအတိုင်းအတာများကို အကောင်အထည်ဖော်ပါ။

4. **Modular Architecture**: MCP server များကို tool နှင့် resource တစ်ခုစီ၏ ရည်ရွယ်ချက်ကို ရှင်းလင်းစွာ သတ်မှတ်ထားသော modular approach ဖြင့် ဒီဇိုင်းဆွဲပါ။

5. **Stateful Connections**: MCP သည် request များစွာအတွင်း state ကို ထိန်းသိမ်းနိုင်စွမ်းရှိသောကြောင့် ပိုမိုချောမွေ့ပြီး အကြောင်းအရာနှင့် သက်ဆိုင်သော အပြန်အလှန်လုပ်ဆောင်မှုများကို အကောင်းဆုံး အသုံးချပါ။

## MCP အတည်ပြုထားသော အကောင်းဆုံးအလေ့အကျင့်များ

အောက်ပါအကောင်းဆုံးအလေ့အကျင့်များကို Model Context Protocol documentation မှ ရယူထားပါသည်-

### လုံခြုံရေးဆိုင်ရာ အကောင်းဆုံးအလေ့အကျင့်များ

1. **အသုံးပြုသူ၏ သဘောတူညီမှုနှင့် ထိန်းချုပ်မှု**: ဒေတာကို access လုပ်ခြင်း သို့မဟုတ် လုပ်ဆောင်မှုများကို ပြုလုပ်မီ အမြဲတမ်း အသုံးပြုသူ၏ သဘောတူညီမှုကို လိုအပ်ပါသည်။ မျှဝေသည့် ဒေတာနှင့် ခွင့်ပြုထားသော လုပ်ဆောင်မှုများကို ရှင်းလင်းစွာ ထိန်းချုပ်နိုင်စွမ်းပေးပါ။

2. **ဒေတာကိုယ်ရေးကိုယ်တာ**: အသုံးပြုသူ၏ သဘောတူညီမှုမရှိဘဲ ဒေတာကို မဖော်ထုတ်ပါနှင့်။ သင့်တော်သော access control များဖြင့် ဒေတာကို ကာကွယ်ပါ။

3. **Tool လုံခြုံမှု**: Tool တစ်ခုကို invoke လုပ်မီ အသုံးပြုသူ၏ သဘောတူညီမှုကို အမြဲတမ်း လိုအပ်ပါသည်။ Tool တစ်ခုစီ၏ လုပ်ဆောင်နိုင်မှုကို အသုံးပြုသူများ နားလည်စေရန်နှင့် ခိုင်ခံ့သော လုံခြုံရေးအကန့်အသတ်များကို အကောင်အထည်ဖော်ပါ။

4. **Tool ခွင့်ပြုချက်ထိန်းချုပ်မှု**: session တစ်ခုအတွင်း model သုံးစွဲနိုင်သော tool များကို configure လုပ်ပါ။ ခွင့်ပြုထားသော tool များသာ အသုံးပြုနိုင်စေရန် အာမခံပါ။

5. **Authentication**: API key, OAuth token သို့မဟုတ် အခြား secure authentication နည်းလမ်းများကို အသုံးပြု၍ tool, resource သို့မဟုတ် sensitive operation များကို access လုပ်မီ သင့်တော်သော authentication ကို လိုအပ်ပါသည်။

6. **Parameter Validation**: Tool invocation များအတွက် validation ကို အကောင်အထည်ဖော်ပါ။ Malformed သို့မဟုတ် မကောင်းသော input များ tool implementation များသို့ ရောက်မလာစေရန် ကာကွယ်ပါ။

7. **Rate Limiting**: Abuse ကို ကာကွယ်ရန်နှင့် server resource များကို တရားမျှတစွာ အသုံးပြုနိုင်စေရန် rate limiting ကို အကောင်အထည်ဖော်ပါ။

### အကောင်အထည်ဖော်မှုဆိုင်ရာ အကောင်းဆုံးအလေ့အကျင့်များ

1. **Capability Negotiation**: Connection setup အတွင်း support လုပ်ထားသော feature များ၊ protocol version များ၊ ရရှိနိုင်သော tool များနှင့် resource များအကြောင်း အချက်အလက်များကို လဲလှယ်ပါ။

2. **Tool Design**: အဓိကရည်ရွယ်ချက်တစ်ခုကိုသာ အကောင်းဆုံးလုပ်ဆောင်နိုင်သော tool များ ဖန်တီးပါ။ အများကြီးကို handle လုပ်ရန် ကြိုးစားသော monolithic tool များကို ရှောင်ပါ။

3. **Error Handling**: ပြဿနာများကို ရှာဖွေခြင်း၊ မှားယွင်းမှုများကို ချောမွေ့စွာ ကိုင်တွယ်ခြင်းနှင့် အကျိုးရှိသော feedback ပေးနိုင်ရန် standardized error message များနှင့် code များကို အကောင်အထည်ဖော်ပါ။

4. **Logging**: Protocol interaction များကို auditing, debugging နှင့် monitoring လုပ်နိုင်ရန် structured log များကို configure လုပ်ပါ။

5. **Progress Tracking**: အချိန်ကြာရှည်သော operation များအတွက် progress update များကို report လုပ်ပါ။ responsive user interface များကို enable လုပ်နိုင်ပါသည်။

6. **Request Cancellation**: မလိုအပ်တော့သော request များ သို့မဟုတ် အချိန်ကြာလွန်းသော request များကို client များ cancel လုပ်နိုင်စေရန် ခွင့်ပြုပါ။

## ထပ်မံရရှိနိုင်သော ရင်းမြစ်များ

MCP အကောင်းဆုံးအလေ့အကျင့်များအကြောင်း အနောက်ဆုံးရသတင်းအချက်အလက်များအတွက် အောက်ပါကို ရှုပါ-

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## အကောင်အထည်ဖော်မှုဆိုင်ရာ လက်တွေ့နမူနာများ

### Tool Design အကောင်းဆုံးအလေ့အကျင့်များ

#### 1. Single Responsibility Principle

MCP tool တစ်ခုစီသည် ရှင်းလင်းပြီး အဓိကရည်ရွယ်ချက်တစ်ခုသာ ရှိရမည်။ အများကြီးကို handle လုပ်ရန် ကြိုးစားသော monolithic tool များကို ဖန်တီးခြင်းမဟုတ်ဘဲ အထူးပြုလုပ်ဆောင်နိုင်သော tool များကို ဖွံ့ဖြိုးပါ။

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

#### 2. Consistent Error Handling

အကျိုးရှိသော error message များနှင့် သင့်တော်သော recovery mechanism များဖြင့် error handling ကို ခိုင်ခံ့စွာ အကောင်အထည်ဖော်ပါ။

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

#### 3. Parameter Validation

Malformed သို့မဟုတ် malicious input များကို ကာကွယ်ရန် parameter များကို အမြဲတမ်း validate လုပ်ပါ။

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

### လုံခြုံရေးဆိုင်ရာ အကောင်အထည်ဖော်မှုနမူနာများ

#### 1. Authentication နှင့် Authorization

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

## MCP Tool များအတွက် စမ်းသပ်မှုဆိုင်ရာ အကောင်းဆုံးအလေ့အကျင့်များ

### Unit Testing MCP Tools

Tool များကို isolation အတွင်း စမ်းသပ်ပါ။ အပြင်ပေါ်မှ အခွင့်အာနိသင်များကို mock လုပ်ပါ-

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

### Integration Testing

Client request များမှ server response များအထိ အပြည့်အစုံ flow ကို စမ်းသပ်ပါ-

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

## စွမ်းဆောင်ရည်မြှင့်တင်ခြင်း

### Caching Strategies

Latency နှင့် resource အသုံးပြုမှုကို လျှော့ချရန် သင့်တော်သော caching ကို အကောင်အထည်ဖော်ပါ-

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

#### Dependency Injection နှင့် Testability

Constructor injection ဖြင့် dependency များကို tool များသို့ ပေးသွင်းပါ။ Test လုပ်နိုင်ပြီး configure လုပ်နိုင်သော tool များကို ဒီဇိုင်းဆွဲပါ-

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

#### Composable Tools

ပိုမိုရှုပ်ထွေးသော workflow များ ဖန်တီးရန် tool များကို ပေါင်းစပ်နိုင်သော ပုံစံဖြင့် ဒီဇိုင်းဆွဲပါ-

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

### Schema Design အကောင်းဆုံးအလေ့အကျင့်များ

Schema သည် model နှင့် tool အကြား contract ဖြစ်သည်။ Schema များကို ကောင်းစွာ ဒီဇိုင်းဆွဲခြင်းသည် tool usability ကို တိုးတက်စေပါသည်။

#### 1. Parameter များကို ရှင်းလင်းစွာ ဖော်ပြခြင်း

Parameter တစ်ခုစီအတွက် ဖော်ပြချက်များကို အမြဲထည့်ပါ-

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

#### 2. Validation Constraints

Invalid input များကို ကာကွယ်ရန် validation constraints များကို ထည့်ပါ-

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

#### 3. Consistent Return Structures

Response structure များကို တိကျမှုရှိစေရန် ထိန်းသိမ်းပါ-

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

### Error Handling

MCP tool များ၏ ယုံကြည်စိတ်ချရမှုကို ထိန်းသိမ်းရန် error handling သည် အရေးကြီးပါသည်။

#### 1. Graceful Error Handling

Error များကို သင့်တော်သောအဆင့်တွင် ကိုင်တွယ်ပြီး အကျိုးရှိသော message များကို ပေးပါ-

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

#### 2. Structured Error Responses

Structured error information ကို အခွင့်အာနိသင်ရှိသလောက် ပြန်ပေးပါ-

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

#### 3. Retry Logic

Transient failure များအတွက် သင့်တော်သော retry logic ကို အကောင်အထည်ဖော်ပါ-

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

### စွမ်းဆောင်ရည်မြှင့်တင်ခြင်း

#### 1. Caching

စျေးကြီးသော operation များအတွက် caching ကို အကောင်အထည်ဖော်ပါ-

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

#### 2. Asynchronous Processing

I/O-bound operation များအတွက် asynchronous programming pattern များကို အသုံးပြုပါ-

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

#### 3. Resource Throttling

Overload ဖြစ်ခြင်းကို ကာကွယ်ရန် resource throttling ကို အကောင်အထည်ဖော်ပါ-

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

### လုံခြုံရေးဆိုင်ရာ အကောင်းဆုံးအလေ့အကျင့်များ

#### 1. Input Validation

Input parameter များကို အမြဲတမ်း validate လုပ်ပါ-

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

#### 2. Authorization Checks

သင့်တော်သော authorization check များကို အကောင်အထည်ဖော်ပါ-

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

#### 3. Sensitive Data Handling

Sensitive data ကို သတိထားစွာ ကိုင်တွယ်ပါ-

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

## MCP Tool များအတွက် စမ်းသပ်မှုဆိုင်ရာ အကောင်းဆုံးအလေ့အကျင့်များ

စုံလင်သော စမ်းသပ်မှုသည် MCP tool များသည် မှန်ကန်စွာ လုပ်ဆောင်နိုင်မှု၊ edge case များ handle လုပ်နိုင်မှုနှင့် စနစ်၏ အခြားအစိတ်အပိုင်းများနှင့် ပေါင်းစည်းနိုင်မှုကို အာမခံပေးပါသည်။

### Unit Testing

#### 1. Tool တစ်ခုစီကို Isolation အတွင်း စမ်းသပ်ပါ

Tool တစ်ခုစီ၏ လုပ်ဆောင်နိုင်မှုအတွက် အထူးပြု စမ်းသပ်မှုများ ဖန်တီးပါ-

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

#### 2. Schema Validation Testing

Schema များသည် သက်တမ်းရှိပြီး constraint များကို သေချာစွာ enforce လုပ်နိုင်မှုကို စမ်းသပ်ပါ-

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

#### 3. Error Handling Tests

Error condition များအတွက် အထူးပြု စမ်းသပ်မှုများ ဖန်တီးပါ-

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

### Integration Testing

#### 1. Tool Chain Testing

Tool များကို မျှော်မှန်းထားသော ပေါင်းစပ်မှုများတွင် အတူတကွ လုပ်ဆောင်နိုင်မှုကို စမ်းသပ်ပါ-

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

#### 2. MCP Server Testing

Tool registration နှင့် execution အပြည့်အစုံဖြင့် MCP server ကို စမ်းသပ်ပါ-

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

#### 3. End-to-End Testing

Model prompt မှ tool execution အထိ workflow အပြည့်အစုံကို စမ်းသပ်ပါ-

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

### စွမ်းဆောင်ရည် စမ်းသပ်မှု

#### 1. Load Testing

MCP server သည် ဘယ်လောက်အထိ concurrent request များကို handle လုပ်နိုင်သည်ကို စမ်းသပ်ပါ-

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

Extreme load အောက်တွင် စနစ်၏ အပြုအမူကို စမ်းသပ်ပါ-

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

#### 3. Monitoring နှင့် Profiling

ရေရှည် စွမ်းဆောင်ရည် analysis အတွက် monitoring ကို စနစ်တကျ ပြုလုပ်ပါ-

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

## MCP Workflow Design Pattern များ

MCP workflow များကို ကောင်းစွာ ဒီဇိုင်းဆွဲခြင်းသည် ထိရောက်မှု၊ ယုံကြည်စိတ်ချရမှုနှင့် ထိန်းသိမ်းနိုင်မှုကို တိုးတက်စေပါသည်။ လိုက်နာရန် အရေးကြီးသော pattern များမှာ-

### 1. Chain of Tools Pattern

Tool များကို အစဉ်လိုက်ချိတ်ဆက်ပြီး tool တစ်ခု၏ output ကို နောက်တစ်ခု၏ input အဖြစ် အသုံးပြုပါ-

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

### 2. Dispatcher Pattern

Input အပေါ်မူတည်၍ specialized tool များသို့ dispatch လုပ်သော central tool ကို အသုံးပြုပါ-

@@CODE_BLOCK_32
3. **စွမ်းဆောင်ရည်အခြေခံများ**: စွမ်းဆောင်ရည်အခြေခံများကို ထိန်းသိမ်းထားပြီး ပြန်လည်ကျဆင်းမှုများကို ဖမ်းဆီးပါ။
4. **လုံခြုံရေးစစ်ဆေးမှုများ**: Pipeline အတွင်းတွင် လုံခြုံရေးစစ်ဆေးမှုများကို အလိုအလျောက်လုပ်ဆောင်ပါ။

### CI Pipeline (GitHub Actions) အတွက် နမူနာ

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

## MCP Specification နှင့်အညီ စစ်ဆေးခြင်း

သင့် server သည် MCP specification ကို မှန်ကန်စွာ အကောင်အထည်ဖော်ထားသည်ကို အတည်ပြုပါ။

### အဓိကလိုက်နာရမည့်အပိုင်းများ

1. **API Endpoints**: လိုအပ်သော endpoints (/resources, /tools, စသည်) ကို စစ်ဆေးပါ။
2. **Request/Response Format**: Schema ကို မှန်ကန်စွာ လိုက်နာမှုကို အတည်ပြုပါ။
3. **Error Codes**: အခြေအနေအမျိုးမျိုးအတွက် မှန်ကန်သော status codes ကို စစ်ဆေးပါ။
4. **Content Types**: အမျိုးမျိုးသော content types ကို ကိုင်တွယ်နိုင်မှုကို စစ်ဆေးပါ။
5. **Authentication Flow**: Specification နှင့်အညီ authentication mechanism များကို စစ်ဆေးပါ။

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

## MCP Server စစ်ဆေးမှုအတွက် ထိရောက်သော အကြံဉာဏ် ၁၀ ခု

1. **Tool Definitions ကို သီးခြားစစ်ဆေးပါ**: Schema definitions ကို tool logic မှ သီးခြားစစ်ဆေးပါ။
2. **Parameterized Tests ကို အသုံးပြုပါ**: Edge cases အပါအဝင် input များစွာဖြင့် tools များကို စစ်ဆေးပါ။
3. **Error Responses ကို စစ်ဆေးပါ**: Error conditions အားလုံးအတွက် မှန်ကန်သော error handling ကို အတည်ပြုပါ။
4. **Authorization Logic ကို စစ်ဆေးပါ**: အသုံးပြုသူအခန်းကဏ္ဍများအတွက် မှန်ကန်သော access control ကို အတည်ပြုပါ။
5. **Test Coverage ကို စောင့်ကြည့်ပါ**: အရေးကြီးသော code path များအတွက် coverage မြင့်မားစေရန် ရှိပါစေ။
6. **Streaming Responses ကို စစ်ဆေးပါ**: Streaming content ကို မှန်ကန်စွာ ကိုင်တွယ်နိုင်မှုကို စစ်ဆေးပါ။
7. **Network ပြဿနာများကို simulation လုပ်ပါ**: အဆင်မပြေသော network အခြေအနေများအောက်တွင် server ၏ အပြုအမူကို စစ်ဆေးပါ။
8. **Resource Limits ကို စစ်ဆေးပါ**: Quotas သို့မဟုတ် rate limits များကို ရောက်ရှိသောအခါ server ၏ အပြုအမူကို စစ်ဆေးပါ။
9. **Regression Tests ကို အလိုအလျောက်လုပ်ဆောင်ပါ**: Code ပြောင်းလဲမှုတိုင်းအတွက် စစ်ဆေးမှုများကို အလိုအလျောက်လုပ်ဆောင်ပါ။
10. **Test Cases များကို Documentation ပြုလုပ်ပါ**: စစ်ဆေးမှုအခြေအနေများကို ရှင်းလင်းသော documentation ဖြင့် ထိန်းသိမ်းပါ။

## Testing တွင် ဖြစ်နိုင်သော အမှားများ

- **Happy path testing ကို အလွန်အကျွံ မှီခိုခြင်း**: Error cases များကို အပြည့်အဝ စစ်ဆေးပါ။
- **စွမ်းဆောင်ရည် စစ်ဆေးမှုကို မလွှမ်းမိုးခြင်း**: Production ကို ထိခိုက်မီ bottlenecks များကို ရှာဖွေပါ။
- **Isolation တွင်သာ စစ်ဆေးခြင်း**: Unit, integration, နှင့် E2E tests များကို ပေါင်းစပ်ပါ။
- **API coverage မလုံလောက်ခြင်း**: Endpoints နှင့် features အားလုံးကို စစ်ဆေးပါ။
- **Test environments မတူညီခြင်း**: Containers ကို အသုံးပြု၍ test environments တူညီမှုကို အတည်ပြုပါ။

## နိဂုံး

MCP servers များကို ယုံကြည်ရသော၊ အရည်အသွေးမြင့်သော အဆင့်သို့ ရောက်ရှိစေရန် Comprehensive testing strategy တစ်ခုလိုအပ်သည်။ ဤလမ်းညွှန်စာအုပ်တွင် ဖော်ပြထားသော အကောင်းဆုံးအလေ့အကျင့်များနှင့် အကြံဉာဏ်များကို အကောင်အထည်ဖော်ခြင်းအားဖြင့် MCP implementations များကို အရည်အသွေး၊ ယုံကြည်မှုနှင့် စွမ်းဆောင်ရည်အမြင့်ဆုံး စံချိန်များနှင့် ကိုက်ညီစေရန် အာမခံနိုင်ပါသည်။

## အဓိကအချက်များ

1. **Tool Design**: Single responsibility principle ကို လိုက်နာပါ၊ dependency injection ကို အသုံးပြုပါ၊ composability အတွက် ဒီဇိုင်းဆွဲပါ။
2. **Schema Design**: ရှင်းလင်းပြီး documentation ပြုလုပ်ထားသော schemas များကို validation constraints များနှင့်အတူ ဖန်တီးပါ။
3. **Error Handling**: Error handling ကို သက်သာလွယ်ကူစွာ ပြုလုပ်ပါ၊ structured error responses နှင့် retry logic ကို အကောင်အထည်ဖော်ပါ။
4. **Performance**: Caching, asynchronous processing, နှင့် resource throttling ကို အသုံးပြုပါ။
5. **Security**: Input validation, authorization checks, နှင့် sensitive data handling ကို ကျယ်ကျယ်ပြန့်ပြန့် လုပ်ဆောင်ပါ။
6. **Testing**: Comprehensive unit, integration, နှင့် end-to-end tests များကို ဖန်တီးပါ။
7. **Workflow Patterns**: Chains, dispatchers, နှင့် parallel processing ကဲ့သို့သော patterns များကို အသုံးပြုပါ။

## လေ့ကျင့်ခန်း

Document processing system အတွက် MCP tool နှင့် workflow တစ်ခုကို ဒီဇိုင်းဆွဲပါ-

1. PDF, DOCX, TXT ကဲ့သို့သော format များစွာကို လက်ခံပါ။
2. Documents များမှ text နှင့် အရေးကြီးသော အချက်အလက်များကို ထုတ်ယူပါ။
3. Documents များကို အမျိုးအစားနှင့် content အလိုက် ခွဲခြားပါ။
4. Document တစ်ခုစီ၏ အကျဉ်းချုပ်ကို ဖန်တီးပါ။

ဤ scenario အတွက် tool schemas, error handling, နှင့် အကောင်းဆုံးသင့်လျော်သော workflow pattern ကို အကောင်အထည်ဖော်ပါ။ ဤ implementation ကို စစ်ဆေးရန် သင်ဘယ်လိုလုပ်ဆောင်မည်ကို စဉ်းစားပါ။

## Resources 

1. MCP community ကို [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) တွင် ပူးပေါင်းပါ။
2. [MCP projects](https://github.com/modelcontextprotocol) တွင် open-source အတွက် အထောက်အကူပြုပါ။
3. MCP principles များကို သင့်အဖွဲ့အစည်း၏ AI initiatives တွင် အသုံးချပါ။
4. သင့်လုပ်ငန်းအတွက် အထူးပြု MCP implementations များကို ရှာဖွေပါ။
5. Multi-modal integration သို့မဟုတ် enterprise application integration ကဲ့သို့သော MCP topics အတွက် အဆင့်မြင့်သင်တန်းများကို စဉ်းစားပါ။
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) မှတစ်ဆင့် သင်လေ့လာထားသော principles များကို အသုံးပြု၍ MCP tools နှင့် workflows ကို ကိုယ်တိုင် ဖန်တီးပါ။

Next: Best Practices [case studies](../09-CaseStudy/README.md)

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူလဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။ 
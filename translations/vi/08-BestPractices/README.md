# Thực hành tốt nhất phát triển MCP

[![Thực hành tốt nhất phát triển MCP](../../../translated_images/vi/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(Nhấp vào hình ảnh trên để xem video của bài học này)_

## Tổng quan

Bài học này tập trung vào các thực hành tốt nhất nâng cao để phát triển, kiểm thử và triển khai các máy chủ và tính năng MCP trong môi trường sản xuất. Khi hệ sinh thái MCP ngày càng phức tạp và quan trọng, việc tuân theo các mẫu đã được thiết lập sẽ đảm bảo độ tin cậy, khả năng bảo trì và khả năng tương tác. Bài học này tổng hợp những kinh nghiệm thực tế từ các triển khai MCP thực tế để hướng dẫn bạn tạo ra các máy chủ mạnh mẽ, hiệu quả với các tài nguyên, lời nhắc và công cụ hiệu quả.

## Mục tiêu học tập

Sau khi hoàn thành bài học này, bạn sẽ có thể:

- Áp dụng các thực hành tốt nhất trong ngành vào thiết kế máy chủ và tính năng MCP
- Tạo chiến lược kiểm thử toàn diện cho các máy chủ MCP
- Thiết kế các mẫu quy trình làm việc hiệu quả, có thể tái sử dụng cho các ứng dụng MCP phức tạp
- Triển khai xử lý lỗi, ghi nhật ký và khả năng quan sát đúng cách trong các máy chủ MCP
- Tối ưu hóa các triển khai MCP về hiệu suất, bảo mật và khả năng bảo trì

## Nguyên tắc cốt lõi của MCP

Trước khi đi sâu vào các thực hành triển khai cụ thể, điều quan trọng là phải hiểu các nguyên tắc cốt lõi hướng dẫn phát triển MCP hiệu quả:

1. **Giao tiếp tiêu chuẩn hóa**: MCP sử dụng JSON-RPC 2.0 làm nền tảng, cung cấp định dạng nhất quán cho các yêu cầu, phản hồi và xử lý lỗi trên tất cả các triển khai.

2. **Thiết kế lấy người dùng làm trung tâm**: Luôn ưu tiên sự đồng ý, kiểm soát và minh bạch của người dùng trong các triển khai MCP của bạn.

3. **Bảo mật là trên hết**: Triển khai các biện pháp bảo mật mạnh mẽ bao gồm xác thực, ủy quyền, xác thực và giới hạn tốc độ.

4. **Kiến trúc mô-đun**: Thiết kế các máy chủ MCP của bạn theo cách tiếp cận mô-đun, trong đó mỗi công cụ và tài nguyên có một mục đích rõ ràng, tập trung.

5. **Kết nối có trạng thái**: Tận dụng khả năng của MCP để duy trì trạng thái qua nhiều yêu cầu để có các tương tác mạch lạc và nhận thức ngữ cảnh hơn.

## Thực hành tốt nhất chính thức của MCP

Các thực hành tốt nhất sau đây được lấy từ tài liệu chính thức của Giao thức Ngữ cảnh Mô hình:

### Thực hành tốt nhất về bảo mật

1. **Sự đồng ý và kiểm soát của người dùng**: Luôn yêu cầu sự đồng ý rõ ràng của người dùng trước khi truy cập dữ liệu hoặc thực hiện các thao tác. Cung cấp quyền kiểm soát rõ ràng về dữ liệu nào được chia sẻ và hành động nào được ủy quyền.

2. **Quyền riêng tư dữ liệu**: Chỉ tiết lộ dữ liệu người dùng khi có sự đồng ý rõ ràng và bảo vệ nó bằng các kiểm soát truy cập phù hợp. Bảo vệ chống lại việc truyền dữ liệu trái phép.

3. **An toàn công cụ**: Yêu cầu sự đồng ý rõ ràng của người dùng trước khi gọi bất kỳ công cụ nào. Đảm bảo người dùng hiểu chức năng của từng công cụ và thực thi các ranh giới bảo mật mạnh mẽ.

4. **Kiểm soát quyền công cụ**: Cấu hình các công cụ mà một mô hình được phép sử dụng trong một phiên, đảm bảo chỉ các công cụ được ủy quyền rõ ràng mới có thể truy cập.

5. **Xác thực**: Yêu cầu xác thực phù hợp trước khi cấp quyền truy cập vào các công cụ, tài nguyên hoặc thao tác nhạy cảm bằng cách sử dụng khóa API, mã thông báo OAuth hoặc các phương pháp xác thực an toàn khác.

6. **Xác thực tham số**: Thực thi xác thực cho tất cả các lần gọi công cụ để ngăn chặn đầu vào không hợp lệ hoặc độc hại đến các triển khai công cụ.

7. **Giới hạn tốc độ**: Triển khai giới hạn tốc độ để ngăn chặn lạm dụng và đảm bảo sử dụng công bằng tài nguyên máy chủ.

### Thực hành tốt nhất về triển khai

1. **Đàm phán khả năng**: Trong quá trình thiết lập kết nối, trao đổi thông tin về các tính năng được hỗ trợ, phiên bản giao thức, công cụ và tài nguyên có sẵn.

2. **Thiết kế công cụ**: Tạo các công cụ tập trung làm tốt một việc, thay vì các công cụ nguyên khối xử lý nhiều mối quan tâm.

3. **Xử lý lỗi**: Triển khai các thông báo lỗi và mã lỗi tiêu chuẩn để giúp chẩn đoán sự cố, xử lý lỗi một cách duyên dáng và cung cấp phản hồi có thể hành động.

4. **Ghi nhật ký**: Cấu hình nhật ký có cấu trúc để kiểm tra, gỡ lỗi và giám sát các tương tác giao thức.

5. **Theo dõi tiến độ**: Đối với các thao tác chạy lâu, báo cáo cập nhật tiến độ để cho phép giao diện người dùng phản hồi.

6. **Hủy yêu cầu**: Cho phép khách hàng hủy các yêu cầu đang thực hiện không còn cần thiết hoặc mất quá nhiều thời gian.

## Tài liệu tham khảo bổ sung

Để biết thông tin cập nhật nhất về các thực hành tốt nhất của MCP, hãy tham khảo:

- [Tài liệu MCP](https://modelcontextprotocol.io/)
- [Đặc tả MCP](https://spec.modelcontextprotocol.io/)
- [Kho GitHub](https://github.com/modelcontextprotocol)
- [Thực hành tốt nhất về bảo mật](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## Ví dụ triển khai thực tế

### Thực hành tốt nhất về thiết kế công cụ

#### 1. Nguyên tắc trách nhiệm đơn lẻ

Mỗi công cụ MCP nên có một mục đích rõ ràng, tập trung. Thay vì tạo các công cụ nguyên khối cố gắng xử lý nhiều mối quan tâm, hãy phát triển các công cụ chuyên biệt xuất sắc trong các nhiệm vụ cụ thể.

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

#### 2. Xử lý lỗi nhất quán

Triển khai xử lý lỗi mạnh mẽ với các thông báo lỗi thông tin và cơ chế khôi phục phù hợp.

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

#### 3. Xác thực tham số

Luôn xác thực tham số kỹ lưỡng để ngăn chặn đầu vào không hợp lệ hoặc độc hại.

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

### Ví dụ triển khai bảo mật

#### 1. Xác thực và ủy quyền

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

#### 2. Giới hạn tốc độ

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

## Thực hành tốt nhất về kiểm thử

### 1. Kiểm thử đơn vị công cụ MCP

Luôn kiểm thử các công cụ của bạn một cách độc lập, mô phỏng các phụ thuộc bên ngoài:

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

### 2. Kiểm thử tích hợp

Kiểm thử toàn bộ luồng từ yêu cầu của khách hàng đến phản hồi của máy chủ:

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

## Tối ưu hóa hiệu suất

### 1. Chiến lược bộ nhớ đệm

Triển khai bộ nhớ đệm phù hợp để giảm độ trễ và sử dụng tài nguyên:

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

#### 2. Tiêm phụ thuộc và khả năng kiểm thử

Thiết kế các công cụ để nhận các phụ thuộc của chúng thông qua tiêm constructor, giúp chúng có thể kiểm thử và cấu hình:

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

#### 3. Công cụ có thể kết hợp

Thiết kế các công cụ có thể được kết hợp với nhau để tạo ra các quy trình làm việc phức tạp hơn:

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

### Thực hành tốt nhất về thiết kế lược đồ

Lược đồ là hợp đồng giữa mô hình và công cụ của bạn. Lược đồ được thiết kế tốt dẫn đến khả năng sử dụng công cụ tốt hơn.

#### 1. Mô tả tham số rõ ràng

Luôn bao gồm thông tin mô tả cho từng tham số:

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

#### 2. Ràng buộc xác thực

Bao gồm các ràng buộc xác thực để ngăn chặn đầu vào không hợp lệ:

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

#### 3. Cấu trúc trả về nhất quán

Duy trì tính nhất quán trong các cấu trúc phản hồi của bạn để giúp các mô hình dễ dàng diễn giải kết quả:

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

### Xử lý lỗi

Xử lý lỗi mạnh mẽ là rất quan trọng để các công cụ MCP duy trì độ tin cậy.

#### 1. Xử lý lỗi duyên dáng

Xử lý lỗi ở các cấp độ phù hợp và cung cấp các thông báo thông tin:

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

#### 2. Phản hồi lỗi có cấu trúc

Trả về thông tin lỗi có cấu trúc khi có thể:

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

#### 3. Logic thử lại

Triển khai logic thử lại phù hợp cho các lỗi tạm thời:

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

### Tối ưu hóa hiệu suất

#### 1. Bộ nhớ đệm

Triển khai bộ nhớ đệm cho các thao tác tốn kém:

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

#### 2. Xử lý bất đồng bộ

Sử dụng các mẫu lập trình bất đồng bộ cho các thao tác ràng buộc I/O:

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

#### 3. Điều tiết tài nguyên

Triển khai điều tiết tài nguyên để ngăn chặn quá tải:

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

### Thực hành tốt nhất về bảo mật

#### 1. Xác thực đầu vào

Luôn xác thực kỹ lưỡng các tham số đầu vào:

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

#### 2. Kiểm tra ủy quyền

Triển khai kiểm tra ủy quyền phù hợp:

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

#### 3. Xử lý dữ liệu nhạy cảm

Xử lý dữ liệu nhạy cảm một cách cẩn thận:

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

## Thực hành tốt nhất về kiểm thử công cụ MCP

Kiểm thử toàn diện đảm bảo rằng các công cụ MCP hoạt động chính xác, xử lý các trường hợp biên và tích hợp đúng cách với phần còn lại của hệ thống.

### Kiểm thử đơn vị

#### 1. Kiểm thử từng công cụ riêng lẻ

Tạo các bài kiểm thử tập trung cho chức năng của từng công cụ:

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

#### 2. Kiểm thử xác thực lược đồ

Kiểm thử rằng các lược đồ hợp lệ và thực thi đúng các ràng buộc:

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

#### 3. Kiểm thử xử lý lỗi

Tạo các bài kiểm thử cụ thể cho các điều kiện lỗi:

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

### Kiểm thử tích hợp

#### 1. Kiểm thử chuỗi công cụ

Kiểm thử các công cụ hoạt động cùng nhau trong các tổ hợp dự kiến:

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

#### 2. Kiểm thử máy chủ MCP

Kiểm thử máy chủ MCP với đầy đủ đăng ký và thực thi công cụ:

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

#### 3. Kiểm thử đầu cuối

Kiểm thử toàn bộ quy trình làm việc từ lời nhắc của mô hình đến thực thi công cụ:

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

### Kiểm thử hiệu suất

#### 1. Kiểm thử tải

Kiểm thử số lượng yêu cầu đồng thời mà máy chủ MCP của bạn có thể xử lý:

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

#### 2. Kiểm thử căng thẳng

Kiểm thử hệ thống dưới tải trọng cực lớn:

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

#### 3. Giám sát và phân tích hiệu suất

Thiết lập giám sát để phân tích hiệu suất dài hạn:

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

## Mẫu thiết kế quy trình làm việc MCP

Các quy trình làm việc MCP được thiết kế tốt cải thiện hiệu quả, độ tin cậy và khả năng bảo trì. Dưới đây là các mẫu chính cần tuân theo:

### 1. Mẫu chuỗi công cụ

Kết nối nhiều công cụ trong một chuỗi, trong đó đầu ra của mỗi công cụ trở thành đầu vào cho công cụ tiếp theo:

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

### 2. Mẫu bộ phân phối

Sử dụng một công cụ trung tâm để phân phối đến các công cụ chuyên biệt dựa trên đầu vào:

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

### 3. Mẫu xử lý song song

Thực thi nhiều công cụ đồng thời để tăng hiệu quả:

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

### 4. Mẫu khôi phục lỗi

Triển khai các phương án dự phòng duyên dáng cho các lỗi công cụ:

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

### 5. Mẫu thành phần quy trình làm việc

Xây dựng các quy trình làm việc phức tạp bằng cách kết hợp các quy trình đơn giản hơn:

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

# Kiểm thử máy chủ MCP: Thực hành tốt nhất và mẹo hàng đầu

## Tổng quan

Kiểm thử là một khía cạnh quan trọng trong việc phát triển các máy chủ MCP đáng tin cậy, chất lượng cao. Hướng dẫn này cung cấp các thực hành tốt nhất và mẹo toàn diện để kiểm thử các máy chủ MCP của bạn trong suốt vòng đời phát triển, từ kiểm thử đơn vị đến kiểm thử tích hợp và xác thực đầu cuối.

## Tại sao kiểm thử quan trọng đối với máy chủ MCP

Máy chủ MCP đóng vai trò là phần trung gian quan trọng giữa các mô hình AI và ứng dụng khách. Kiểm thử kỹ lưỡng đảm bảo:

- Độ tin cậy trong môi trường sản xuất
- Xử lý chính xác các yêu cầu và phản hồi
- Triển khai đúng các đặc tả MCP
- Khả năng chống chịu trước các lỗi và trường hợp biên
- Hiệu suất nhất quán dưới các tải khác nhau

## Kiểm thử đơn vị cho máy chủ MCP

### Kiểm thử đơn vị (Nền tảng)

Kiểm thử đơn vị xác minh các thành phần riêng lẻ của máy chủ MCP của bạn một cách độc lập.

#### Những gì cần kiểm thử

1. **Trình xử lý tài nguyên**: Kiểm thử logic của từng trình xử lý tài nguyên một cách độc lập
2. **Triển khai công cụ**: Xác minh hành vi của công cụ với các đầu vào khác nhau
3. **Mẫu lời nhắc**: Đảm bảo các mẫu lời nhắc hiển thị chính xác
4. **Xác thực lược đồ**: Kiểm thử logic xác thực tham số
5. **Xử lý lỗi**: Xác minh phản hồi lỗi cho các đầu vào không hợp lệ

#### Thực hành tốt nhất cho kiểm thử đơn vị

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

### Kiểm thử tích hợp (Lớp giữa)

Kiểm thử tích hợp xác minh các tương tác giữa các thành phần của máy chủ MCP.

#### Những gì cần kiểm thử

1. **Khởi tạo máy chủ**: Kiểm thử khởi động máy chủ với các cấu hình khác nhau
2. **Đăng ký tuyến**: Xác minh tất cả các điểm cuối được đăng ký chính xác
3. **Xử lý yêu cầu**: Kiểm thử toàn bộ chu trình yêu cầu-phản hồi
4. **Lan truyền lỗi**: Đảm bảo lỗi được xử lý đúng cách trên các thành phần
5. **Xác thực & Ủy quyền**: Kiểm thử các cơ chế bảo mật

#### Thực hành tốt nhất cho kiểm thử tích hợp

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

### Kiểm thử đầu cuối (Lớp trên cùng)

Kiểm thử đầu cuối xác minh hành vi của toàn bộ hệ thống từ khách hàng đến máy chủ.

#### Những gì cần kiểm thử

1. **Giao tiếp khách hàng-máy chủ**: Kiểm thử toàn bộ chu trình yêu cầu-phản hồi
2. **SDK khách hàng thực tế**: Kiểm thử với các triển khai khách hàng thực tế
3. **Hiệu suất dưới tải**: Xác minh hành vi với nhiều yêu cầu đồng thời
4. **Khôi phục lỗi**: Kiểm thử hệ thống khôi phục từ các lỗi
5. **Thao tác dài hạn**: Xác minh xử lý luồng và các thao tác dài

#### Thực hành tốt nhất cho kiểm thử đầu cuối

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

## Chiến lược mô phỏng cho kiểm thử MCP

Mô phỏng là điều cần thiết để cô lập các thành phần trong quá trình kiểm thử.

### Các thành phần cần mô phỏng

1. **Mô hình AI bên ngoài**: Mô phỏng phản hồi của mô hình để kiểm thử có thể dự đoán
2. **Dịch vụ bên ngoài**: Mô phỏng các phụ thuộc API (cơ sở dữ liệu, dịch vụ bên thứ ba)
3. **Dịch vụ xác thực**: Mô phỏng các nhà cung cấp danh tính
4. **Nhà cung cấp tài nguyên**: Mô phỏng các trình xử lý tài nguyên tốn kém

### Ví dụ: Mô phỏng phản hồi của mô hình AI

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

## Kiểm thử hiệu suất

Kiểm thử hiệu suất là rất quan trọng đối với các máy chủ MCP trong sản xuất.

### Những gì cần đo lường

1. **Độ trễ**: Thời gian phản hồi cho các yêu cầu
2. **Thông lượng**: Số lượng yêu cầu được xử lý mỗi giây
3. **Sử dụng tài nguyên**: CPU, bộ nhớ, sử dụng mạng
4. **Xử lý đồng thời**: Hành vi dưới các yêu cầu song song
5. **Đặc điểm mở rộng**: Hiệu suất khi tải tăng

### Công cụ kiểm thử hiệu suất

- **k6**: Công cụ kiểm thử tải mã nguồn mở
- **JMeter**: Công cụ kiểm thử hiệu suất toàn diện
- **Locust**: Công cụ kiểm thử tải dựa trên Python
- **Azure Load Testing**: Kiểm thử hiệu suất dựa trên đám
3. **Các tiêu chuẩn hiệu suất**: Duy trì các tiêu chuẩn hiệu suất để phát hiện các lỗi thoái hóa  
4. **Quét bảo mật**: Tự động hóa kiểm tra bảo mật như một phần của pipeline  

### Ví dụ về CI Pipeline (GitHub Actions)

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

## Kiểm tra tuân thủ theo đặc tả MCP

Xác minh rằng máy chủ của bạn triển khai đúng đặc tả MCP.

### Các khu vực tuân thủ chính

1. **API Endpoints**: Kiểm tra các endpoint bắt buộc (/resources, /tools, v.v.)  
2. **Định dạng Request/Response**: Xác thực tuân thủ schema  
3. **Mã lỗi**: Xác minh mã trạng thái chính xác cho các tình huống khác nhau  
4. **Loại nội dung**: Kiểm tra xử lý các loại nội dung khác nhau  
5. **Luồng xác thực**: Xác minh cơ chế xác thực tuân thủ đặc tả  

### Bộ kiểm tra tuân thủ

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

## 10 mẹo hàng đầu để kiểm tra máy chủ MCP hiệu quả

1. **Kiểm tra định nghĩa công cụ riêng biệt**: Xác minh định nghĩa schema độc lập với logic công cụ  
2. **Sử dụng kiểm tra tham số hóa**: Kiểm tra công cụ với nhiều đầu vào khác nhau, bao gồm các trường hợp biên  
3. **Kiểm tra phản hồi lỗi**: Xác minh xử lý lỗi đúng cách cho tất cả các điều kiện lỗi có thể xảy ra  
4. **Kiểm tra logic ủy quyền**: Đảm bảo kiểm soát truy cập đúng cho các vai trò người dùng khác nhau  
5. **Theo dõi phạm vi kiểm tra**: Nhắm đến phạm vi cao cho mã quan trọng  
6. **Kiểm tra phản hồi streaming**: Xác minh xử lý đúng nội dung streaming  
7. **Mô phỏng sự cố mạng**: Kiểm tra hành vi trong điều kiện mạng kém  
8. **Kiểm tra giới hạn tài nguyên**: Xác minh hành vi khi đạt đến hạn mức hoặc giới hạn tốc độ  
9. **Tự động hóa kiểm tra thoái hóa**: Xây dựng bộ kiểm tra chạy trên mọi thay đổi mã  
10. **Tài liệu hóa các trường hợp kiểm tra**: Duy trì tài liệu rõ ràng về các kịch bản kiểm tra  

## Những lỗi phổ biến khi kiểm tra

- **Quá phụ thuộc vào kiểm tra happy path**: Đảm bảo kiểm tra kỹ các trường hợp lỗi  
- **Bỏ qua kiểm tra hiệu suất**: Xác định các nút thắt cổ chai trước khi chúng ảnh hưởng đến sản xuất  
- **Chỉ kiểm tra trong môi trường cô lập**: Kết hợp kiểm tra đơn vị, tích hợp và E2E  
- **Phạm vi API không đầy đủ**: Đảm bảo tất cả các endpoint và tính năng được kiểm tra  
- **Môi trường kiểm tra không nhất quán**: Sử dụng container để đảm bảo môi trường kiểm tra nhất quán  

## Kết luận

Chiến lược kiểm tra toàn diện là điều cần thiết để phát triển các máy chủ MCP đáng tin cậy và chất lượng cao. Bằng cách áp dụng các phương pháp và mẹo tốt nhất được nêu trong hướng dẫn này, bạn có thể đảm bảo rằng các triển khai MCP của mình đáp ứng các tiêu chuẩn cao nhất về chất lượng, độ tin cậy và hiệu suất.

## Những điểm chính cần ghi nhớ

1. **Thiết kế công cụ**: Tuân theo nguyên tắc trách nhiệm đơn lẻ, sử dụng dependency injection và thiết kế để dễ dàng kết hợp  
2. **Thiết kế schema**: Tạo các schema rõ ràng, được tài liệu hóa tốt với các ràng buộc xác thực phù hợp  
3. **Xử lý lỗi**: Triển khai xử lý lỗi linh hoạt, phản hồi lỗi có cấu trúc và logic thử lại  
4. **Hiệu suất**: Sử dụng caching, xử lý bất đồng bộ và giới hạn tài nguyên  
5. **Bảo mật**: Áp dụng xác thực đầu vào kỹ lưỡng, kiểm tra ủy quyền và xử lý dữ liệu nhạy cảm  
6. **Kiểm tra**: Tạo các kiểm tra đơn vị, tích hợp và end-to-end toàn diện  
7. **Mẫu quy trình làm việc**: Áp dụng các mẫu đã được thiết lập như chuỗi, bộ điều phối và xử lý song song  

## Bài tập

Thiết kế một công cụ MCP và quy trình làm việc cho hệ thống xử lý tài liệu bao gồm:  

1. Chấp nhận tài liệu ở nhiều định dạng (PDF, DOCX, TXT)  
2. Trích xuất văn bản và thông tin chính từ tài liệu  
3. Phân loại tài liệu theo loại và nội dung  
4. Tạo bản tóm tắt cho mỗi tài liệu  

Triển khai các schema công cụ, xử lý lỗi và một mẫu quy trình làm việc phù hợp nhất với kịch bản này. Cân nhắc cách bạn sẽ kiểm tra triển khai này.

## Tài nguyên

1. Tham gia cộng đồng MCP trên [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) để cập nhật những phát triển mới nhất  
2. Đóng góp cho các [dự án MCP mã nguồn mở](https://github.com/modelcontextprotocol)  
3. Áp dụng các nguyên tắc MCP trong các sáng kiến AI của tổ chức bạn  
4. Khám phá các triển khai MCP chuyên biệt cho ngành của bạn  
5. Cân nhắc tham gia các khóa học nâng cao về các chủ đề MCP cụ thể, như tích hợp đa phương thức hoặc tích hợp ứng dụng doanh nghiệp  
6. Thử nghiệm xây dựng các công cụ và quy trình làm việc MCP của riêng bạn bằng cách áp dụng các nguyên tắc đã học thông qua [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

Tiếp theo: Các phương pháp hay nhất [case studies](../09-CaseStudy/README.md)  

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
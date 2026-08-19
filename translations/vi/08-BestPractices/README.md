# Thực hành tốt nhất trong phát triển MCP

[![Thực hành tốt nhất trong phát triển MCP](../../../translated_images/vi/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Bấm vào hình trên để xem video bài học này)_

## Tổng quan

Bài học này tập trung vào các thực hành tốt nâng cao để phát triển, kiểm thử và triển khai các máy chủ MCP và tính năng trong môi trường sản xuất. Khi hệ sinh thái MCP ngày càng phức tạp và quan trọng, việc tuân theo các mẫu đã được thiết lập đảm bảo độ tin cậy, khả năng bảo trì và khả năng tương tác. Bài học này tổng hợp kinh nghiệm thực tiễn thu được từ các triển khai MCP thực tế để hướng dẫn bạn tạo ra các máy chủ mạnh mẽ, hiệu quả với tài nguyên, lời nhắc và công cụ hiệu quả.

## Mục tiêu học tập

Kết thúc bài học này, bạn sẽ có khả năng:

- Áp dụng các thực hành tốt của ngành trong thiết kế máy chủ và tính năng MCP
- Tạo chiến lược kiểm thử toàn diện cho các máy chủ MCP
- Thiết kế các mẫu quy trình làm việc hiệu quả, tái sử dụng được cho các ứng dụng MCP phức tạp
- Triển khai xử lý lỗi, ghi nhật ký và quan sát đúng cách trong các máy chủ MCP
- Tối ưu hóa các triển khai MCP về hiệu suất, bảo mật và khả năng bảo trì

## Nguyên tắc cốt lõi của MCP

Trước khi đi sâu vào các thực hành triển khai cụ thể, điều quan trọng là hiểu các nguyên tắc cốt lõi hướng dẫn phát triển MCP hiệu quả:

1. **Giao tiếp tiêu chuẩn hóa**: MCP sử dụng JSON-RPC 2.0 làm nền tảng, cung cấp định dạng nhất quán cho các yêu cầu, phản hồi và xử lý lỗi trên tất cả các triển khai.

2. **Thiết kế lấy người dùng làm trung tâm**: Luôn ưu tiên sự đồng ý, kiểm soát và minh bạch của người dùng trong các triển khai MCP của bạn.

3. **Bảo mật ưu tiên hàng đầu**: Triển khai các biện pháp bảo mật mạnh mẽ bao gồm xác thực, phân quyền, xác thực dữ liệu và giới hạn tốc độ.

4. **Kiến trúc mô-đun**: Thiết kế các máy chủ MCP của bạn theo cách mô-đun, trong đó mỗi công cụ và tài nguyên có mục đích rõ ràng và tập trung.

5. **Trạng thái rõ ràng**: MCP `2026-07-28` không giữ trạng thái ở cấp giao thức
   . Khi một quy trình làm việc cần trạng thái qua các lần gọi, sử dụng các handle rõ ràng hoặc
   các đối số công cụ thông thường được hỗ trợ bởi trạng thái ứng dụng bền bỉ.

## Thực hành tốt nhất chính thức của MCP

Các thực hành tốt nhất sau đây được rút ra từ tài liệu chính thức của Model Context Protocol:

### Thực hành tốt nhất về bảo mật

1. **Sự đồng ý và kiểm soát của người dùng**: Luôn yêu cầu sự đồng ý rõ ràng của người dùng trước khi truy cập dữ liệu hoặc thực hiện các thao tác. Cung cấp kiểm soát rõ ràng về dữ liệu được chia sẻ và các hành động được cho phép.

2. **Bảo mật dữ liệu**: Chỉ tiết lộ dữ liệu người dùng với sự đồng ý rõ ràng và bảo vệ nó bằng các kiểm soát truy cập phù hợp. Ngăn ngừa truyền dữ liệu trái phép.

3. **An toàn công cụ**: Yêu cầu sự đồng ý rõ ràng của người dùng trước khi gọi bất kỳ công cụ nào. Đảm bảo người dùng hiểu chức năng của mỗi công cụ và áp dụng các ranh giới bảo mật mạnh mẽ.

4. **Kiểm soát quyền công cụ**: Cấu hình công cụ mà mô hình có thể sử dụng cho
   mỗi yêu cầu và ngữ cảnh ủy quyền, đảm bảo chỉ các công cụ được phép rõ ràng
   mới được truy cập.

5. **Xác thực**: Yêu cầu xác thực đúng cách trước khi cấp quyền truy cập vào công cụ, tài nguyên hoặc các thao tác nhạy cảm sử dụng các khóa API, token OAuth hoặc các phương thức xác thực bảo mật khác.

6. **Xác thực tham số**: Thực thi xác thực cho tất cả các gọi công cụ để ngăn chặn dữ liệu đầu vào bị lỗi hoặc độc hại đến các triển khai công cụ.

7. **Giới hạn tốc độ**: Triển khai giới hạn tốc độ để ngăn chặn việc lạm dụng và đảm bảo việc sử dụng công bằng các tài nguyên máy chủ.

### Thực hành tốt nhất trong triển khai

1. **Đàm phán năng lực**: Đàm phán các phiên bản giao thức được hỗ trợ và
   năng lực. Trong MCP `2026-07-28`, mỗi yêu cầu là tự chứa và có thể
   sử dụng `server/discover`; các phiên bản cũ hơn dùng handshake khởi tạo.

2. **Thiết kế công cụ**: Tạo các công cụ tập trung vào một nhiệm vụ duy nhất thay vì các công cụ đơn khổng lồ xử lý nhiều mối quan tâm.

3. **Xử lý lỗi**: Triển khai các thông điệp lỗi chuẩn hóa và mã lỗi giúp chẩn đoán sự cố, xử lý thất bại một cách nhẹ nhàng, và cung cấp phản hồi có thể hành động.

4. **Quan sát**: Sử dụng `stderr` để chẩn đoán stdio và OpenTelemetry
   cho quan sát có cấu trúc. Tính năng ghi nhật ký MCP đã bị loại bỏ trong
   đặc tả `2026-07-28`.

5. **Theo dõi tiến trình**: Đối với các thao tác chạy lâu, báo cáo các cập nhật tiến độ để cho phép giao diện người dùng đáp ứng.

6. **Hủy yêu cầu**: Cho phép client hủy các yêu cầu đang thực hiện mà không còn cần thiết hoặc mất quá nhiều thời gian.

## Tài liệu tham khảo bổ sung

Để có thông tin cập nhật nhất về các thực hành tốt MCP, tham khảo:

- [Tài liệu MCP](https://modelcontextprotocol.io/)
- [Đặc tả MCP (2026-07-28)][mcp-2026-spec]
- [Đặc tả MCP trước đây (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Phần mở rộng nhiệm vụ MCP][mcp-tasks-extension]
- [Kho GitHub](https://github.com/modelcontextprotocol)
- [Thực hành tốt về bảo mật](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Rủi ro bảo mật và các phương án giảm thiểu
- [Hội thảo MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Đào tạo bảo mật thực hành

### Bài học kèm theo về Độ tin cậy

Các vòng lặp thử lại tổng quát không an toàn cho các công cụ tạo vé, thanh toán,
thông điệp, triển khai hoặc các hiệu ứng thực tế khác. Một phản hồi có thể bị mất
sau khi hiệu ứng đã cam kết.

Sử dụng bài học kèm về độ tin cậy,
[Thử lại an toàn cho công cụ MCP: Mẫu sidecar độ tin cậy][reliability-sidecar],
để học các khóa hoạt động ổn định, nhận dạng trùng lặp, điểm kiểm tra,
hòa giải, mức độ bằng chứng và tiêm lỗi.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Ví dụ triển khai thực tiễn

### Thực hành tốt trong thiết kế công cụ

#### 1. Nguyên tắc Trách nhiệm Đơn lẻ

Mỗi công cụ MCP nên có một mục đích rõ ràng, tập trung. Thay vì tạo các công cụ đơn khổng lồ cố gắng xử lý nhiều mối quan tâm, hãy phát triển các công cụ chuyên biệt xuất sắc trong các nhiệm vụ cụ thể.

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

Triển khai xử lý lỗi mạnh mẽ với các thông điệp lỗi đầy đủ thông tin và cơ chế phục hồi phù hợp.

```python
# Ví dụ Python với xử lý lỗi toàn diện
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Kiểm tra tham số
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Xác thực bảo mật
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Thao tác cơ sở dữ liệu với giới hạn thời gian
                async with timeout(10):  # Giới hạn thời gian 10 giây
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Lỗi kết nối có thể là tạm thời
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Lỗi truy vấn có thể là lỗi phía khách hàng
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Cho phép lỗi đặc thù của công cụ đi qua
            raise
        except Exception as e:
            # Bắt tất cả lỗi không mong đợi
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Triển khai phát hiện SQL injection
        pass
        
    def _log_error(self, message, error):
        # Triển khai ghi nhật ký lỗi
        pass
```

#### 3. Xác thực tham số

Luôn xác thực kỹ lưỡng các tham số để ngăn ngừa đầu vào bị lỗi hoặc độc hại.

```javascript
// Ví dụ JavaScript/TypeScript với xác thực tham số chi tiết
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
    // 1. Xác thực sự hiện diện của tham số
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Xác thực kiểu dữ liệu của tham số
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Xác thực giá trị của tham số
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Xác thực sự hiện diện nội dung cho thao tác ghi
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Xác thực an toàn đường dẫn
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Triển khai dựa trên các tham số đã được xác thực
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Triển khai kiểm tra an toàn đường dẫn
    // ...
  }
}
```

### Ví dụ triển khai bảo mật

#### 1. Xác thực và Phân quyền

```java
// Ví dụ Java với xác thực và phân quyền
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Tiêm phụ thuộc
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
        // 1. Trích xuất ngữ cảnh xác thực
        String authToken = request.getContext().getAuthToken();
        
        // 2. Xác thực người dùng
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Kiểm tra phân quyền cho thao tác cụ thể
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Tiến hành thao tác đã được phép
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

## Thực hành tốt nhất trong kiểm thử

### 1. Kiểm thử đơn vị công cụ MCP

Luôn kiểm thử các công cụ của bạn một cách cô lập, giả lập các phụ thuộc bên ngoài:

```typescript
// Ví dụ về unit test công cụ trong TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Tạo dịch vụ thời tiết giả lập
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Tạo công cụ với phụ thuộc giả lập
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Chuẩn bị
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Thực hiện
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Kiểm tra
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Chuẩn bị
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Thực hiện & Kiểm tra
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Kiểm thử tích hợp

Kiểm thử quy trình hoàn chỉnh từ yêu cầu client đến phản hồi máy chủ:

```python
# Ví dụ kiểm thử tích hợp Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Khởi động máy chủ thử nghiệm
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Tạo một client
        client = McpClient("http://localhost:5000")
        
        # Kiểm thử phát hiện công cụ
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Kiểm thử thực thi công cụ
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Xác minh phản hồi
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Dọn dẹp
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

Thiết kế công cụ nhận các phụ thuộc thông qua tiêm trong hàm khởi tạo, làm chúng có thể kiểm thử và cấu hình được:

```java
// Ví dụ Java với tiêm phụ thuộc
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Phụ thuộc được tiêm thông qua constructor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Triển khai công cụ
    // ...
}
```

#### 3. Công cụ có thể ghép nối

Thiết kế các công cụ có thể kết hợp với nhau tạo thành các quy trình làm việc phức tạp hơn:

```python
# Ví dụ Python minh họa các công cụ có thể kết hợp
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Triển khai...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Công cụ này có thể sử dụng kết quả từ công cụ dataFetch
    async def execute_async(self, request):
        # Triển khai...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Công cụ này có thể sử dụng kết quả từ công cụ dataAnalysis
    async def execute_async(self, request):
        # Triển khai...
        pass

# Các công cụ này có thể được sử dụng độc lập hoặc như một phần của quy trình làm việc
```

### Thực hành tốt trong thiết kế schema

Schema là hợp đồng giữa mô hình và công cụ của bạn. Schema được thiết kế tốt giúp công cụ dễ sử dụng hơn.

#### 1. Mô tả tham số rõ ràng

Luôn bao gồm thông tin mô tả cho mỗi tham số:

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

Bao gồm ràng buộc xác thực để ngăn đầu vào không hợp lệ:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Thuộc tính email với xác thực định dạng
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Thuộc tính tuổi với các ràng buộc số
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Thuộc tính liệt kê
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

#### 3. Cấu trúc phản hồi nhất quán

Duy trì tính nhất quán trong cấu trúc phản hồi giúp mô hình dễ dàng diễn giải kết quả hơn:

```python
async def execute_async(self, request):
    try:
        # Xử lý yêu cầu
        results = await self._search_database(request.parameters["query"])
        
        # Luôn trả về một cấu trúc nhất quán
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

Xử lý lỗi mạnh mẽ rất quan trọng để các công cụ MCP duy trì độ tin cậy.

#### 1. Xử lý lỗi nhẹ nhàng

Xử lý lỗi ở các cấp phù hợp và cung cấp các thông điệp đầy đủ thông tin:

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
        // Triển khai
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
        
        // Ném lại các ngoại lệ khác dưới dạng ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logic thử lại

Chỉ sử dụng logic thử lại tổng quát cho các cuộc gọi chỉ đọc hoặc các thao tác có
hợp đồng xuống dòng đã đảm bảo idempotent. Đối với các thao tác có hiệu ứng, thời gian chờ
sau khi gửi yêu cầu là không rõ ràng. Hòa giải trạng thái có thẩm quyền và
tái sử dụng cùng một khóa hoạt động ổn định trước khi thực hiện lại. Xem bài học
[bài học kèm sidecar độ tin cậy](./reliability-sidecars/README.md).

Vòng lặp thử lại có giới hạn sau phù hợp cho tra cứu chỉ đọc:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # giây
    
    while retry_count < max_retries:
        try:
            # Gọi API bên ngoài chỉ đọc
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Phản hồi lùi theo cấp số nhân
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Lỗi không tạm thời, không thử lại
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Tối ưu hóa hiệu suất

#### 1. Bộ nhớ đệm

Triển khai bộ nhớ đệm cho các thao tác tốn tài nguyên:

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

Sử dụng mẫu lập trình bất đồng bộ cho các thao tác I/O:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Đối với các thao tác chạy lâu, trả về ID xử lý ngay lập tức
        String processId = UUID.randomUUID().toString();
        
        // Bắt đầu xử lý bất đồng bộ
        CompletableFuture.runAsync(() -> {
            try {
                // Thực hiện thao tác chạy lâu
                documentService.processDocument(documentId);
                
                // Cập nhật trạng thái (thông thường sẽ được lưu trong cơ sở dữ liệu)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Trả về phản hồi ngay lập tức với ID tiến trình
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Công cụ kiểm tra trạng thái đi kèm
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

#### 3. Giới hạn tài nguyên

Triển khai giới hạn tài nguyên để ngăn chặn quá tải:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Cho phép 5 yêu cầu mỗi giây
            bucket_size=10        # Cho phép bùng phát lên đến 10 yêu cầu
        )
    
    async def execute_async(self, request):
        # Kiểm tra xem chúng ta có thể tiến hành hay cần phải đợi
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Nếu thời gian chờ quá lâu
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Đợi trong thời gian trễ phù hợp
                await asyncio.sleep(delay)
        
        # Tiêu thụ một token và tiếp tục với yêu cầu
        self.rate_limiter.consume()
        
        # Gọi API
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
            
            # Tính toán thời gian cho đến khi token tiếp theo có sẵn
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Thêm token mới dựa trên thời gian đã trôi qua
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Thực hành tốt về bảo mật

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

#### 2. Kiểm tra phân quyền

Triển khai kiểm tra phân quyền đúng cách:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Lấy ngữ cảnh người dùng từ yêu cầu
    UserContext user = request.getContext().getUserContext();
    
    // Kiểm tra nếu người dùng có quyền cần thiết
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Đối với tài nguyên cụ thể, kiểm tra quyền truy cập vào tài nguyên đó
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Tiếp tục với việc thực thi công cụ
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
        
        # Lấy dữ liệu người dùng
        user_data = await self.user_service.get_user_data(user_id)
        
        # Lọc các trường nhạy cảm trừ khi được yêu cầu rõ ràng VÀ được phép
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Kiểm tra cấp độ ủy quyền trong ngữ cảnh yêu cầu
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Tạo bản sao để tránh sửa đổi bản gốc
        redacted = user_data.copy()
        
        # Che khuất các trường nhạy cảm cụ thể
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Che khuất dữ liệu nhạy cảm lồng nhau
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Thực hành tốt trong kiểm thử công cụ MCP

Kiểm thử toàn diện đảm bảo các công cụ MCP hoạt động đúng, xử lý các trường hợp biên và tích hợp đúng cách với hệ thống còn lại.

### Kiểm thử đơn vị

#### 1. Kiểm thử từng công cụ một cách cô lập

Tạo các kiểm thử tập trung vào chức năng của từng công cụ:

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

#### 2. Kiểm thử xác thực schema

Kiểm thử các schema hợp lệ và thực thi ràng buộc đúng cách:

```java
@Test
public void testSchemaValidation() {
    // Tạo thể hiện công cụ
    SearchTool searchTool = new SearchTool();
    
    // Lấy sơ đồ
    Object schema = searchTool.getSchema();
    
    // Chuyển đổi sơ đồ sang JSON để xác thực
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Xác thực sơ đồ là JSONSchema hợp lệ
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Kiểm tra các tham số hợp lệ
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Kiểm tra tham số bắt buộc bị thiếu
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Kiểm tra loại tham số không hợp lệ
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Kiểm thử xử lý lỗi

Tạo các kiểm thử cụ thể cho điều kiện lỗi:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Sắp xếp
    tool = ApiTool(timeout=0.1)  # Timeout rất ngắn
    
    # Giả lập một yêu cầu sẽ bị timeout
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Dài hơn thời gian timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Thực thi & Xác nhận
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Xác minh thông báo ngoại lệ
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Sắp xếp
    tool = ApiTool()
    
    # Giả lập một phản hồi bị giới hạn tần suất
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
        
        # Thực thi & Xác nhận
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Xác minh ngoại lệ chứa thông tin giới hạn tần suất
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Kiểm thử tích hợp

#### 1. Kiểm thử chuỗi công cụ

Kiểm thử các công cụ hoạt động cùng nhau như dự kiến:

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

Kiểm thử máy chủ MCP với đăng ký và thực thi đầy đủ công cụ:

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
        // Kiểm tra điểm cuối khám phá
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Tạo yêu cầu công cụ
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Gửi yêu cầu và xác minh phản hồi
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Tạo yêu cầu công cụ không hợp lệ
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Thiếu tham số "b"
        request.put("parameters", parameters);
        
        // Gửi yêu cầu và xác minh phản hồi lỗi
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Kiểm thử đầu-cuối

Kiểm thử quy trình hoàn chỉnh từ lời nhắc mô hình đến thực thi công cụ:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Sắp xếp - Thiết lập client MCP và mô hình giả lập
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Giả lập phản hồi của mô hình
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
    
    # Giả lập phản hồi công cụ thời tiết
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
        
        # Thực hiện
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Xác nhận
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Kiểm thử hiệu suất

#### 1. Kiểm thử tải

Kiểm thử máy chủ MCP có thể xử lý bao nhiêu yêu cầu đồng thời:

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

#### 2. Kiểm thử chịu tải

Kiểm thử hệ thống dưới tải cực đoan:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Thiết lập JMeter để kiểm thử áp lực
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Cấu hình kế hoạch kiểm thử JMeter
    HashTree testPlanTree = new HashTree();
    
    // Tạo kế hoạch kiểm thử, nhóm luồng, bộ lấy mẫu, v.v.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Thêm bộ lấy mẫu HTTP để thực thi công cụ
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Thêm bộ lắng nghe
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Chạy kiểm thử
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Xác nhận kết quả
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Thời gian phản hồi trung bình < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // Phần trăm thứ 90 < 500ms
}
```

#### 3. Giám sát và phân tích

Thiết lập giám sát để phân tích hiệu suất lâu dài:

```python
# Cấu hình giám sát cho máy chủ MCP
def configure_monitoring(server):
    # Thiết lập các chỉ số Prometheus
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
    
    # Thêm middleware để đo thời gian và ghi lại các chỉ số
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Mở endpoint cho các chỉ số
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Các mẫu thiết kế quy trình MCP

Các quy trình MCP được thiết kế tốt cải thiện hiệu quả, độ tin cậy và khả năng bảo trì. Dưới đây là các mẫu chính cần theo:

### 1. Mẫu chuỗi công cụ

Kết nối nhiều công cụ theo chuỗi, đầu ra của công cụ này trở thành đầu vào cho công cụ kế tiếp:

```python
# Triển khai Chuỗi Công cụ Python
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Danh sách tên công cụ để thực thi theo thứ tự
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Thực thi từng công cụ trong chuỗi, truyền kết quả trước đó
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Lưu kết quả và sử dụng làm đầu vào cho công cụ tiếp theo
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Ví dụ sử dụng
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

### 2. Mẫu bộ điều phối

Sử dụng một công cụ trung tâm phân phối tới các công cụ chuyên biệt dựa trên đầu vào:

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

Thực thi đồng thời nhiều công cụ để tăng hiệu quả:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Bước 1: Lấy metadata bộ dữ liệu (đồng bộ)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Bước 2: Khởi chạy nhiều phân tích song song
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
        
        // Chờ tất cả các tác vụ song song hoàn thành
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Chờ hoàn tất
        
        // Bước 3: Kết hợp kết quả
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Bước 4: Tạo báo cáo tóm tắt
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Trả về kết quả toàn bộ quy trình công việc
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Mẫu phục hồi lỗi

Triển khai các giải pháp dự phòng nhẹ nhàng cho các lỗi công cụ:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Thử công cụ chính trước
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Ghi lại lỗi
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Chuyển sang công cụ phụ
            try:
                # Có thể cần chuyển đổi tham số cho công cụ dự phòng
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Cả hai công cụ đều thất bại
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Việc triển khai này sẽ phụ thuộc vào các công cụ cụ thể
        # Trong ví dụ này, chúng ta sẽ chỉ trả về các tham số ban đầu
        return params

# Ví dụ sử dụng
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API thời tiết chính (có phí)
        "basicWeatherService",    # API thời tiết dự phòng (miễn phí)
        {"location": location}
    )
```

### 5. Mẫu phối hợp quy trình làm việc

Xây dựng các quy trình phức tạp bằng cách phối hợp các quy trình đơn giản hơn:

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

Kiểm thử là một khía cạnh quan trọng trong việc phát triển các máy chủ MCP đáng tin cậy, chất lượng cao. Hướng dẫn này cung cấp các thực hành tốt nhất toàn diện và mẹo để kiểm thử các máy chủ MCP của bạn trong suốt vòng đời phát triển, từ kiểm thử đơn vị đến kiểm thử tích hợp và xác nhận đầu-cuối.

## Tại sao kiểm thử quan trọng đối với các máy chủ MCP

Máy chủ MCP đóng vai trò quan trọng là tầng trung gian giữa các mô hình AI và ứng dụng client. Kiểm thử kỹ lưỡng đảm bảo:

- Độ tin cậy trong môi trường sản xuất
- Xử lý chính xác các yêu cầu và phản hồi
- Triển khai đúng các đặc tả MCP
- Khả năng chịu lỗi và các trường hợp biên
- Hiệu suất ổn định dưới các mức tải khác nhau

## Kiểm thử đơn vị cho máy chủ MCP

### Kiểm thử đơn vị (Nền tảng)

Kiểm thử đơn vị xác minh các thành phần riêng lẻ của máy chủ MCP của bạn một cách cô lập.

#### Những gì cần kiểm thử

1. **Bộ xử lý tài nguyên**: Kiểm thử logic của từng bộ xử lý tài nguyên một cách độc lập
2. **Triển khai công cụ**: Xác minh hành vi công cụ với các đầu vào khác nhau
3. **Mẫu lời nhắc**: Đảm bảo các mẫu lời nhắc hiển thị đúng
4. **Xác thực schema**: Kiểm thử logic xác thực tham số
5. **Xử lý lỗi**: Kiểm thử phản hồi lỗi đối với các đầu vào không hợp lệ

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
# Ví dụ về bài kiểm tra đơn vị cho công cụ máy tính trong Python
def test_calculator_tool_add():
    # Sắp xếp
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Thực hiện
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Khẳng định
    assert result["value"] == 12
```

### Kiểm thử tích hợp (Tầng giữa)

Kiểm thử tích hợp xác minh sự tương tác giữa các thành phần của máy chủ MCP của bạn.

#### Những gì cần kiểm thử

1. **Khởi tạo máy chủ**: Kiểm thử khởi động máy chủ với các cấu hình khác nhau
2. **Đăng ký tuyến đường**: Xác minh tất cả các điểm cuối được đăng ký chính xác
3. **Xử lý yêu cầu**: Kiểm thử chu trình yêu cầu-phản hồi đầy đủ
4. **Truyền lỗi**: Đảm bảo lỗi được xử lý đúng cách qua các thành phần
5. **Xác thực & Phân quyền**: Kiểm thử các cơ chế bảo mật

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

### Kiểm thử đầu-cuối (Tầng trên cùng)

Kiểm thử đầu-cuối xác minh hành vi toàn bộ hệ thống từ client đến máy chủ.

#### Những gì cần kiểm thử

1. **Giao tiếp client-máy chủ**: Kiểm thử chu trình yêu cầu-phản hồi hoàn chỉnh
2. **SDK client thực tế**: Kiểm thử với các triển khai client thật sự
3. **Hiệu suất dưới tải**: Xác minh hành vi với nhiều yêu cầu đồng thời
4. **Phục hồi lỗi**: Kiểm thử phục hồi hệ thống từ các sự cố

5. **Các hoạt động chạy dài**: Xác minh việc xử lý các hoạt động truyền và hoạt động dài hạn

#### Các Thực Tiễn Tốt Nhất cho Kiểm Thử E2E

```typescript
// Ví dụ kiểm thử E2E với một client bằng TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Khởi động server trong môi trường kiểm thử
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Thực hiện hành động
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Kiểm tra kết quả
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Chiến Lược Giả Lập cho Kiểm Thử MCP

Giả lập rất cần thiết để cô lập các thành phần trong quá trình kiểm thử.

### Các Thành Phần Cần Giả Lập

1. **Mô hình AI bên ngoài**: Giả lập phản hồi mô hình để kiểm thử có thể dự đoán được
2. **Dịch vụ bên ngoài**: Giả lập các phụ thuộc API (cơ sở dữ liệu, dịch vụ bên thứ ba)
3. **Dịch vụ xác thực**: Giả lập nhà cung cấp nhận dạng
4. **Nhà cung cấp tài nguyên**: Giả lập các trình xử lý tài nguyên tốn kém

### Ví dụ: Giả Lập Phản Hồi Mô Hình AI

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
# Ví dụ Python với unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Cấu hình mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Sử dụng mock trong bài kiểm tra
    server = McpServer(model_client=mock_model)
    # Tiếp tục với bài kiểm tra
```

## Kiểm Thử Hiệu Suất

Kiểm thử hiệu suất rất quan trọng cho các máy chủ MCP trong môi trường sản xuất.

### Những Điều Cần Đo Lường

1. **Độ trễ**: Thời gian phản hồi cho các yêu cầu
2. **Thông lượng**: Số lượng yêu cầu xử lý được mỗi giây
3. **Sử dụng tài nguyên**: CPU, bộ nhớ, sử dụng mạng
4. **Xử lý đồng thời**: Hành vi dưới các yêu cầu song song
5. **Đặc điểm mở rộng**: Hiệu suất khi tải tăng lên

### Công Cụ Kiểm Thử Hiệu Suất

- **k6**: Công cụ kiểm tra tải mã nguồn mở
- **JMeter**: Kiểm thử hiệu suất toàn diện
- **Locust**: Kiểm thử tải dựa trên Python
- **Azure Load Testing**: Kiểm thử hiệu suất dựa trên đám mây

### Ví dụ: Kiểm Tra Tải Cơ Bản với k6

```javascript
// k6 script để kiểm thử tải máy chủ MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 người dùng ảo
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

## Tự Động Hóa Kiểm Thử cho Máy Chủ MCP

Tự động hóa kiểm thử giúp đảm bảo chất lượng đồng nhất và vòng phản hồi nhanh hơn.

### Tích Hợp CI/CD

1. **Chạy Kiểm Thử Đơn Vị trên Pull Requests**: Đảm bảo các thay đổi mã không phá vỡ chức năng hiện có
2. **Kiểm Thử Tích Hợp trên môi trường Staging**: Chạy kiểm thử tích hợp ở môi trường tiền sản xuất
3. **Cơ Sở Hiệu Suất**: Duy trì các chuẩn mực hiệu suất để phát hiện suy giảm
4. **Quét An Ninh**: Tự động hóa kiểm thử an ninh như một phần của pipeline

### Ví dụ Pipeline CI (GitHub Actions)

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

## Kiểm Thử Tuân Thủ Đặc Tả MCP

Xác minh máy chủ của bạn thực thi đúng đặc tả MCP.

### Các Lĩnh Vực Tuân Thủ Chính

1. **Các Endpoint API**: Kiểm thử các endpoint bắt buộc (/resources, /tools, v.v.)
2. **Định dạng Yêu cầu/Phản hồi**: Xác nhận tuân thủ schema
3. **Mã lỗi**: Xác minh mã trạng thái đúng cho các kịch bản khác nhau
4. **Loại Nội dung**: Kiểm thử xử lý các loại nội dung khác nhau
5. **Quy trình Xác thực**: Xác minh các cơ chế xác thực phù hợp theo đặc tả

### Bộ Kiểm Thử Tuân Thủ

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

## 10 Mẹo Hàng Đầu cho Kiểm Thử Máy Chủ MCP Hiệu Quả

1. **Kiểm thử Định nghĩa Công cụ Riêng biệt**: Xác minh các định nghĩa schema độc lập với logic công cụ
2. **Sử dụng Kiểm thử Tham số hóa**: Thử các công cụ với nhiều đầu vào đa dạng, bao gồm các trường hợp biên
3. **Kiểm tra Phản hồi Lỗi**: Xác minh xử lý lỗi đúng đắn cho mọi điều kiện lỗi có thể xảy ra
4. **Kiểm thử Logic Ủy quyền**: Đảm bảo kiểm soát truy cập phù hợp cho các vai trò người dùng khác nhau
5. **Theo dõi Phủ sóng Kiểm thử**: Hướng tới phủ sóng cao của mã đường dẫn quan trọng
6. **Kiểm thử Phản hồi Luồng**: Xác minh xử lý đúng nội dung luồng
7. **Mô phỏng Sự cố Mạng**: Kiểm thử hành vi trong điều kiện mạng kém
8. **Kiểm thử Giới hạn Tài nguyên**: Xác minh hành vi khi đạt hạn mức hoặc giới hạn tốc độ
9. **Tự động hóa Kiểm thử Hồi quy**: Xây dựng bộ kiểm thử chạy mỗi khi có thay đổi mã
10. **Tài liệu Hóa Các Tình Huống Kiểm Thử**: Duy trì tài liệu rõ ràng về các kịch bản kiểm thử

## Những Cạm Bẫy Thường Gặp trong Kiểm Thử

- **Phụ thuộc quá mức vào kiểm thử đường dẫn thuận lợi**: Đảm bảo kiểm thử kỹ các trường hợp lỗi
- **Bỏ qua kiểm thử hiệu suất**: Phát hiện nút thắt trước khi ảnh hưởng đến sản xuất
- **Chỉ kiểm thử cô lập**: Kết hợp kiểm thử đơn vị, tích hợp và E2E
- **Phủ sóng API không đầy đủ**: Đảm bảo mọi endpoint và tính năng đều được kiểm thử
- **Môi trường kiểm thử không nhất quán**: Sử dụng container để đảm bảo môi trường kiểm thử nhất quán

## Kết Luận

Chiến lược kiểm thử toàn diện là cần thiết để phát triển các máy chủ MCP đáng tin cậy, chất lượng cao. Bằng cách triển khai các thực tiễn tốt nhất và mẹo trong hướng dẫn này, bạn có thể đảm bảo các triển khai MCP đạt chuẩn mực cao nhất về chất lượng, độ tin cậy và hiệu suất.


## Những Điểm Chính Rút Ra

1. **Thiết Kế Công Cụ**: Tuân theo nguyên tắc trách nhiệm đơn, sử dụng tiêm phụ thuộc, và thiết kế cho tính tổng hợp
2. **Thiết Kế Schema**: Tạo các schema rõ ràng, có tài liệu đầy đủ với các ràng buộc xác thực phù hợp
3. **Xử Lý Lỗi**: Thực hiện xử lý lỗi nhẹ nhàng, phản hồi lỗi có cấu trúc và logic thử lại có nhận thức kết quả

4. **Hiệu Suất**: Sử dụng bộ đệm, xử lý bất đồng bộ và hạn chế tài nguyên
5. **Bảo Mật**: Áp dụng xác thực đầu vào kỹ lưỡng, kiểm tra ủy quyền, và xử lý dữ liệu nhạy cảm
6. **Kiểm Thử**: Tạo các kiểm thử đơn vị, tích hợp và đầu-cuối toàn diện
7. **Mẫu Quy Trình Làm Việc**: Áp dụng các mẫu đã được thiết lập như chuỗi, bộ điều phối và xử lý song song

## Bài Tập

Thiết kế một công cụ MCP và quy trình làm việc cho hệ thống xử lý tài liệu mà:

1. Chấp nhận tài liệu ở nhiều định dạng (PDF, DOCX, TXT)
2. Trích xuất văn bản và thông tin chính từ tài liệu
3. Phân loại tài liệu theo loại và nội dung
4. Tạo tóm tắt cho mỗi tài liệu

Thực hiện các schema công cụ, xử lý lỗi và mẫu quy trình làm việc phù hợp nhất cho kịch bản này. Cân nhắc cách bạn sẽ kiểm thử triển khai này.

## Tài Nguyên

1. Tham gia cộng đồng MCP trên [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) để cập nhật các phát triển mới nhất
2. Góp phần vào các dự án [MCP mã nguồn mở](https://github.com/modelcontextprotocol)
3. Áp dụng các nguyên tắc MCP trong các sáng kiến AI của tổ chức bạn
4. Khám phá các triển khai MCP chuyên ngành cho ngành của bạn.
5. Cân nhắc tham gia các khóa học nâng cao về các chủ đề MCP cụ thể, như tích hợp đa mô-đun hoặc tích hợp ứng dụng doanh nghiệp.
6. Thử nghiệm xây dựng công cụ và quy trình làm việc MCP riêng của bạn sử dụng các nguyên tắc học được trong [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

## Tiếp theo

Tiếp theo: [Nghiên Cứu Tình Huống](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
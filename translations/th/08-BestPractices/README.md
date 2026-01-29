# แนวทางปฏิบัติที่ดีที่สุดในการพัฒนา MCP

[![แนวทางปฏิบัติที่ดีที่สุดในการพัฒนา MCP](../../../translated_images/th/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

## ภาพรวม

บทเรียนนี้มุ่งเน้นไปที่แนวทางปฏิบัติขั้นสูงสำหรับการพัฒนา ทดสอบ และปรับใช้เซิร์ฟเวอร์ MCP และฟีเจอร์ในสภาพแวดล้อมการผลิต เมื่อระบบนิเวศ MCP มีความซับซ้อนและมีความสำคัญมากขึ้น การปฏิบัติตามรูปแบบที่กำหนดไว้จะช่วยให้มั่นใจในความน่าเชื่อถือ การบำรุงรักษา และการทำงานร่วมกัน บทเรียนนี้รวบรวมความรู้เชิงปฏิบัติที่ได้จากการใช้งาน MCP ในโลกจริงเพื่อแนะนำคุณในการสร้างเซิร์ฟเวอร์ที่แข็งแกร่งและมีประสิทธิภาพ พร้อมด้วยทรัพยากร คำแนะนำ และเครื่องมือที่มีประสิทธิภาพ

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- ใช้แนวทางปฏิบัติที่ดีที่สุดในอุตสาหกรรมในการออกแบบเซิร์ฟเวอร์และฟีเจอร์ MCP
- สร้างกลยุทธ์การทดสอบที่ครอบคลุมสำหรับเซิร์ฟเวอร์ MCP
- ออกแบบรูปแบบการทำงานที่มีประสิทธิภาพและนำกลับมาใช้ใหม่ได้สำหรับแอปพลิเคชัน MCP ที่ซับซ้อน
- ใช้การจัดการข้อผิดพลาด การบันทึก และการสังเกตการณ์ที่เหมาะสมในเซิร์ฟเวอร์ MCP
- ปรับปรุงการใช้งาน MCP ให้เหมาะสมสำหรับประสิทธิภาพ ความปลอดภัย และการบำรุงรักษา

## หลักการสำคัญของ MCP

ก่อนที่จะลงลึกในแนวทางปฏิบัติการใช้งานเฉพาะ สิ่งสำคัญคือต้องเข้าใจหลักการสำคัญที่เป็นแนวทางในการพัฒนา MCP อย่างมีประสิทธิภาพ:

1. **การสื่อสารที่เป็นมาตรฐาน**: MCP ใช้ JSON-RPC 2.0 เป็นพื้นฐาน โดยให้รูปแบบที่สอดคล้องกันสำหรับคำขอ การตอบกลับ และการจัดการข้อผิดพลาดในทุกการใช้งาน

2. **การออกแบบที่เน้นผู้ใช้**: ให้ความสำคัญกับการยินยอม การควบคุม และความโปร่งใสของผู้ใช้ในทุกการใช้งาน MCP

3. **ความปลอดภัยเป็นอันดับแรก**: ใช้มาตรการรักษาความปลอดภัยที่แข็งแกร่ง รวมถึงการตรวจสอบสิทธิ์ การอนุญาต การตรวจสอบความถูกต้อง และการจำกัดอัตรา

4. **สถาปัตยกรรมแบบโมดูลาร์**: ออกแบบเซิร์ฟเวอร์ MCP ของคุณด้วยแนวทางแบบโมดูลาร์ โดยที่แต่ละเครื่องมือและทรัพยากรมีวัตถุประสงค์ที่ชัดเจนและมุ่งเน้น

5. **การเชื่อมต่อแบบมีสถานะ**: ใช้ความสามารถของ MCP ในการรักษาสถานะระหว่างคำขอหลายรายการเพื่อการโต้ตอบที่สอดคล้องและคำนึงถึงบริบทมากขึ้น

## แนวทางปฏิบัติที่ดีที่สุดของ MCP อย่างเป็นทางการ

แนวทางปฏิบัติที่ดีที่สุดต่อไปนี้ได้มาจากเอกสาร Model Context Protocol อย่างเป็นทางการ:

### แนวทางปฏิบัติด้านความปลอดภัย

1. **การยินยอมและการควบคุมของผู้ใช้**: ต้องการการยินยอมจากผู้ใช้อย่างชัดเจนก่อนเข้าถึงข้อมูลหรือดำเนินการ ให้การควบคุมที่ชัดเจนเกี่ยวกับข้อมูลที่แชร์และการดำเนินการที่ได้รับอนุญาต

2. **ความเป็นส่วนตัวของข้อมูล**: เปิดเผยข้อมูลผู้ใช้เฉพาะเมื่อได้รับการยินยอมอย่างชัดเจนและปกป้องข้อมูลด้วยการควบคุมการเข้าถึงที่เหมาะสม ป้องกันการส่งข้อมูลโดยไม่ได้รับอนุญาต

3. **ความปลอดภัยของเครื่องมือ**: ต้องการการยินยอมจากผู้ใช้อย่างชัดเจนก่อนเรียกใช้เครื่องมือใด ๆ ตรวจสอบให้แน่ใจว่าผู้ใช้เข้าใจฟังก์ชันการทำงานของแต่ละเครื่องมือและบังคับใช้ขอบเขตความปลอดภัยที่แข็งแกร่ง

4. **การควบคุมสิทธิ์ของเครื่องมือ**: กำหนดค่าเครื่องมือที่โมเดลสามารถใช้ได้ในระหว่างเซสชัน เพื่อให้แน่ใจว่าเครื่องมือที่ได้รับอนุญาตอย่างชัดเจนเท่านั้นที่สามารถเข้าถึงได้

5. **การตรวจสอบสิทธิ์**: ต้องการการตรวจสอบสิทธิ์ที่เหมาะสมก่อนให้สิทธิ์เข้าถึงเครื่องมือ ทรัพยากร หรือการดำเนินการที่ละเอียดอ่อน โดยใช้ API keys, OAuth tokens หรือวิธีการตรวจสอบสิทธิ์ที่ปลอดภัยอื่น ๆ

6. **การตรวจสอบพารามิเตอร์**: บังคับใช้การตรวจสอบสำหรับการเรียกใช้เครื่องมือทั้งหมดเพื่อป้องกันข้อมูลที่ไม่ถูกต้องหรือเป็นอันตรายจากการเข้าถึงการใช้งานเครื่องมือ

7. **การจำกัดอัตรา**: ใช้การจำกัดอัตราเพื่อป้องกันการใช้งานในทางที่ผิดและรับรองการใช้งานทรัพยากรเซิร์ฟเวอร์อย่างเป็นธรรม

### แนวทางปฏิบัติในการใช้งาน

1. **การเจรจาความสามารถ**: ในระหว่างการตั้งค่าการเชื่อมต่อ ให้แลกเปลี่ยนข้อมูลเกี่ยวกับฟีเจอร์ที่รองรับ เวอร์ชันโปรโตคอล เครื่องมือที่มี และทรัพยากร

2. **การออกแบบเครื่องมือ**: สร้างเครื่องมือที่มุ่งเน้นซึ่งทำสิ่งหนึ่งได้ดี แทนที่จะสร้างเครื่องมือขนาดใหญ่ที่จัดการหลายข้อกังวล

3. **การจัดการข้อผิดพลาด**: ใช้ข้อความและรหัสข้อผิดพลาดที่เป็นมาตรฐานเพื่อช่วยวินิจฉัยปัญหา จัดการความล้มเหลวอย่างสง่างาม และให้ข้อเสนอแนะที่นำไปปฏิบัติได้

4. **การบันทึก**: กำหนดค่าการบันทึกแบบมีโครงสร้างสำหรับการตรวจสอบ การแก้ไขข้อบกพร่อง และการตรวจสอบการโต้ตอบของโปรโตคอล

5. **การติดตามความคืบหน้า**: สำหรับการดำเนินการที่ใช้เวลานาน ให้รายงานการอัปเดตความคืบหน้าเพื่อเปิดใช้งานอินเทอร์เฟซผู้ใช้ที่ตอบสนอง

6. **การยกเลิกคำขอ**: อนุญาตให้ลูกค้ายกเลิกคำขอที่กำลังดำเนินการซึ่งไม่จำเป็นอีกต่อไปหรือใช้เวลานานเกินไป

## แหล่งข้อมูลเพิ่มเติม

สำหรับข้อมูลล่าสุดเกี่ยวกับแนวทางปฏิบัติที่ดีที่สุดของ MCP โปรดดูที่:

- [เอกสาร MCP](https://modelcontextprotocol.io/)
- [สเปค MCP](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [แนวทางปฏิบัติด้านความปลอดภัย](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## ตัวอย่างการใช้งานจริง

### แนวทางปฏิบัติในการออกแบบเครื่องมือ

#### 1. หลักการความรับผิดชอบเดียว

เครื่องมือ MCP แต่ละตัวควรมีวัตถุประสงค์ที่ชัดเจนและมุ่งเน้น แทนที่จะสร้างเครื่องมือขนาดใหญ่ที่พยายามจัดการหลายข้อกังวล ให้พัฒนาเครื่องมือเฉพาะที่ยอดเยี่ยมในงานเฉพาะ

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

#### 2. การจัดการข้อผิดพลาดที่สอดคล้องกัน

ใช้การจัดการข้อผิดพลาดที่แข็งแกร่งพร้อมข้อความข้อผิดพลาดที่ให้ข้อมูลและกลไกการกู้คืนที่เหมาะสม

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

#### 3. การตรวจสอบพารามิเตอร์

ตรวจสอบพารามิเตอร์อย่างละเอียดเสมอเพื่อป้องกันข้อมูลที่ไม่ถูกต้องหรือเป็นอันตราย

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

### ตัวอย่างการใช้งานด้านความปลอดภัย

#### 1. การตรวจสอบสิทธิ์และการอนุญาต

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

#### 2. การจำกัดอัตรา

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

## แนวทางปฏิบัติในการทดสอบ

### 1. การทดสอบหน่วยของเครื่องมือ MCP

ทดสอบเครื่องมือของคุณในสภาพแวดล้อมที่แยกออกจากกัน โดยจำลองการพึ่งพาภายนอก:

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

### 2. การทดสอบการรวมระบบ

ทดสอบกระบวนการทั้งหมดตั้งแต่คำขอของลูกค้าไปจนถึงการตอบกลับของเซิร์ฟเวอร์:

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

## การปรับปรุงประสิทธิภาพ

### 1. กลยุทธ์การแคช

ใช้การแคชที่เหมาะสมเพื่อลดเวลาแฝงและการใช้งานทรัพยากร:

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

#### 2. การฉีดการพึ่งพาและการทดสอบได้

ออกแบบเครื่องมือเพื่อรับการพึ่งพาผ่านการฉีดตัวสร้าง ทำให้สามารถทดสอบและกำหนดค่าได้:

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

#### 3. เครื่องมือที่ประกอบได้

ออกแบบเครื่องมือที่สามารถประกอบเข้าด้วยกันเพื่อสร้างเวิร์กโฟลว์ที่ซับซ้อนมากขึ้น:

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

### แนวทางปฏิบัติในการออกแบบสคีมา

สคีมาคือสัญญาระหว่างโมเดลและเครื่องมือของคุณ สคีมาที่ออกแบบมาอย่างดีช่วยให้การใช้งานเครื่องมือดีขึ้น

#### 1. คำอธิบายพารามิเตอร์ที่ชัดเจน

รวมข้อมูลคำอธิบายสำหรับแต่ละพารามิเตอร์เสมอ:

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

#### 2. ข้อจำกัดการตรวจสอบ

รวมข้อจำกัดการตรวจสอบเพื่อป้องกันข้อมูลที่ไม่ถูกต้อง:

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

#### 3. โครงสร้างการตอบกลับที่สอดคล้องกัน

รักษาความสอดคล้องในโครงสร้างการตอบกลับของคุณเพื่อให้ง่ายต่อการตีความผลลัพธ์โดยโมเดล:

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

### การจัดการข้อผิดพลาด

การจัดการข้อผิดพลาดที่แข็งแกร่งเป็นสิ่งสำคัญสำหรับเครื่องมือ MCP เพื่อรักษาความน่าเชื่อถือ

#### 1. การจัดการข้อผิดพลาดอย่างสง่างาม

จัดการข้อผิดพลาดในระดับที่เหมาะสมและให้ข้อความที่ให้ข้อมูล:

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

#### 2. การตอบกลับข้อผิดพลาดแบบมีโครงสร้าง

ส่งคืนข้อมูลข้อผิดพลาดแบบมีโครงสร้างเมื่อเป็นไปได้:

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

#### 3. ตรรกะการลองใหม่

ใช้ตรรกะการลองใหม่ที่เหมาะสมสำหรับความล้มเหลวชั่วคราว:

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

### การปรับปรุงประสิทธิภาพ

#### 1. การแคช

ใช้การแคชสำหรับการดำเนินการที่มีค่าใช้จ่ายสูง:

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

#### 2. การประมวลผลแบบอะซิงโครนัส

ใช้รูปแบบการเขียนโปรแกรมแบบอะซิงโครนัสสำหรับการดำเนินการที่มี I/O-bound:

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

#### 3. การควบคุมทรัพยากร

ใช้การควบคุมทรัพยากรเพื่อป้องกันการโอเวอร์โหลด:

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

### แนวทางปฏิบัติด้านความปลอดภัย

#### 1. การตรวจสอบข้อมูลนำเข้า

ตรวจสอบพารามิเตอร์นำเข้าอย่างละเอียดเสมอ:

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

#### 2. การตรวจสอบสิทธิ์

ใช้การตรวจสอบสิทธิ์ที่เหมาะสม:

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

#### 3. การจัดการข้อมูลที่ละเอียดอ่อน

จัดการข้อมูลที่ละเอียดอ่อนอย่างระมัดระวัง:

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

## แนวทางปฏิบัติในการทดสอบเครื่องมือ MCP

การทดสอบที่ครอบคลุมช่วยให้มั่นใจว่าเครื่องมือ MCP ทำงานได้อย่างถูกต้อง จัดการกรณีขอบ และรวมเข้ากับระบบอื่นได้อย่างเหมาะสม

### การทดสอบหน่วย

#### 1. ทดสอบเครื่องมือแต่ละตัวในสภาพแวดล้อมที่แยกออกจากกัน

สร้างการทดสอบที่มุ่งเน้นสำหรับฟังก์ชันการทำงานของเครื่องมือแต่ละตัว:

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

#### 2. การทดสอบการตรวจสอบสคีมา

ทดสอบว่าสคีมาถูกต้องและบังคับใช้ข้อจำกัดอย่างเหมาะสม:

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

#### 3. การทดสอบการจัดการข้อผิดพลาด

สร้างการทดสอบเฉพาะสำหรับเงื่อนไขข้อผิดพลาด:

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

### การทดสอบการรวมระบบ

#### 1. การทดสอบการทำงานร่วมกันของเครื่องมือ

ทดสอบเครื่องมือที่ทำงานร่วมกันในชุดค่าผสมที่คาดหวัง:

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

#### 2. การทดสอบเซิร์ฟเวอร์ MCP

ทดสอบเซิร์ฟเวอร์ MCP พร้อมการลงทะเบียนเครื่องมือและการดำเนินการเต็มรูปแบบ:

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

#### 3. การทดสอบแบบ End-to-End

ทดสอบเวิร์กโฟลว์ที่สมบูรณ์ตั้งแต่คำแนะนำของโมเดลไปจนถึงการดำเนินการเครื่องมือ:

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

### การทดสอบประสิทธิภาพ

#### 1. การทดสอบโหลด

ทดสอบจำนวนคำขอพร้อมกันที่เซิร์ฟเวอร์ MCP ของคุณสามารถจัดการได้:

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

#### 2. การทดสอบความเครียด

ทดสอบระบบภายใต้โหลดที่รุนแรง:

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

#### 3. การตรวจสอบและการวิเคราะห์ประสิทธิภาพ

ตั้งค่าการตรวจสอบสำหรับการวิเคราะห์ประสิทธิภาพระยะยาว:

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

## รูปแบบการออกแบบเวิร์กโฟลว์ MCP

เวิร์กโฟลว์ MCP ที่ออกแบบมาอย่างดีช่วยเพิ่มประสิทธิภาพ ความน่าเชื่อถือ และการบำรุงรักษา นี่คือรูปแบบสำคัญที่ควรปฏิบัติตาม:

### 1. รูปแบบการเชื่อมโยงเครื่องมือ

เชื่อมต่อเครื่องมือหลายตัวในลำดับที่ผลลัพธ์ของแต่ละเครื่องมือกลายเป็นข้อมูลนำเข้าสำหรับเครื่องมือถัดไป:

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

### 2. รูปแบบ Dispatcher

ใช้เครื่องมือกลางที่ส่งต่อไปยังเครื่องมือเฉพาะตามข้อมูลนำเข้า:

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

### 3. รูปแบบการประมวลผลแบบขนาน

ดำเนินการเครื่องมือหลายตัวพร้อมกันเพื่อประสิทธิภาพ:

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

### 4. รูปแบบการกู้คืนข้อผิดพลาด

ใช้การกู้คืนที่สง่างามสำหรับความล้มเหลวของเครื่องมือ:

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

### 5. รูปแบบการประกอบเวิร์กโฟลว์

สร้างเวิร์กโฟลว์ที่ซับซ้อนโดยการประกอบเวิร์กโฟลว์ที่ง่ายกว่า:

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

# การทดสอบเซิร์ฟเวอร์ MCP: แนวทางปฏิบัติที่ดีที่สุดและเคล็ดลับสำคัญ

## ภาพรวม

การทดสอบเป็นส่วนสำคัญของการพัฒนาเซิร์ฟเวอร์ MCP ที่เชื่อถือได้และมีคุณภาพสูง คู่มือนี้ให้แนวทางปฏิบัติที่ดีที่สุดและเคล็ดลับสำหรับการทดสอบเซิร์ฟเวอร์ MCP ของคุณตลอดวงจรการพัฒนา ตั้งแต่การทดสอบหน่วยไปจนถึงการทดสอบการรวมระบบและการตรวจสอบแบบ End-to-End

## ทำไมการทดสอบจึงสำคัญสำหรับเซิร์ฟเวอร์ MCP

เซิร์ฟเวอร์ MCP ทำหน้าที่เป็นตัวกลางที่สำคัญระหว่างโมเดล AI และแอปพลิเคชันของลูกค้า การทดสอบอย่างละเอียดช่วยให้มั่นใจว่า:

- ความน่าเชื่อถือในสภาพแวดล้อมการผลิต
- การจัดการคำขอและการตอบกลับอย่างถูกต้อง
- การใช้งานข้อกำหนด MCP อย่างเหมาะสม
- ความยืดหยุ่นต่อความล้มเหลวและกรณีขอบ
- ประสิทธิภาพที่สม่ำเสมอภายใต้โหลดต่าง ๆ

## การทดสอบหน่วยสำหรับเซิร์ฟเวอร์ MCP

### การทดสอบหน่วย (พื้นฐาน)

การทดสอบหน่วยตรวจสอบส่วนประกอบแต่ละส่วนของเซิร์ฟเวอร์ MCP ของคุณในสภาพแวดล้อมที่แยกออกจากกัน

#### สิ่งที่ควรทดสอบ

1. **ตัวจัดการทรัพ
3. **เกณฑ์มาตรฐานด้านประสิทธิภาพ**: รักษาเกณฑ์มาตรฐานด้านประสิทธิภาพเพื่อป้องกันการถดถอย  
4. **การสแกนความปลอดภัย**: ทำการทดสอบความปลอดภัยโดยอัตโนมัติในกระบวนการพัฒนา  

### ตัวอย่าง CI Pipeline (GitHub Actions)

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

## การทดสอบความสอดคล้องกับข้อกำหนด MCP

ตรวจสอบว่าเซิร์ฟเวอร์ของคุณดำเนินการตามข้อกำหนด MCP อย่างถูกต้อง  

### พื้นที่สำคัญของความสอดคล้อง

1. **API Endpoints**: ทดสอบ endpoints ที่จำเป็น (/resources, /tools, ฯลฯ)  
2. **รูปแบบคำขอ/คำตอบ**: ตรวจสอบความสอดคล้องของ schema  
3. **รหัสข้อผิดพลาด**: ตรวจสอบรหัสสถานะที่ถูกต้องสำหรับสถานการณ์ต่างๆ  
4. **ประเภทเนื้อหา**: ทดสอบการจัดการประเภทเนื้อหาที่แตกต่างกัน  
5. **กระบวนการยืนยันตัวตน**: ตรวจสอบกลไกการยืนยันตัวตนที่สอดคล้องกับข้อกำหนด  

### ชุดทดสอบความสอดคล้อง

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

## 10 เคล็ดลับสำหรับการทดสอบเซิร์ฟเวอร์ MCP อย่างมีประสิทธิภาพ

1. **ทดสอบการกำหนดเครื่องมือแยกกัน**: ตรวจสอบ schema definitions โดยไม่พึ่งพา logic ของเครื่องมือ  
2. **ใช้การทดสอบแบบพารามิเตอร์**: ทดสอบเครื่องมือด้วยข้อมูลหลากหลาย รวมถึงกรณีขอบเขต  
3. **ตรวจสอบการตอบสนองข้อผิดพลาด**: ตรวจสอบการจัดการข้อผิดพลาดที่เหมาะสมสำหรับทุกเงื่อนไขข้อผิดพลาด  
4. **ทดสอบตรรกะการอนุญาต**: ตรวจสอบการควบคุมการเข้าถึงสำหรับบทบาทผู้ใช้ที่แตกต่างกัน  
5. **ติดตามความครอบคลุมของการทดสอบ**: ตั้งเป้าหมายให้ครอบคลุมโค้ดในเส้นทางสำคัญ  
6. **ทดสอบการตอบสนองแบบสตรีมมิ่ง**: ตรวจสอบการจัดการเนื้อหาแบบสตรีมมิ่งอย่างเหมาะสม  
7. **จำลองปัญหาเครือข่าย**: ทดสอบพฤติกรรมในสภาพเครือข่ายที่ไม่ดี  
8. **ทดสอบข้อจำกัดของทรัพยากร**: ตรวจสอบพฤติกรรมเมื่อถึงขีดจำกัดหรืออัตราการใช้งาน  
9. **ทำการทดสอบการถดถอยโดยอัตโนมัติ**: สร้างชุดทดสอบที่ทำงานทุกครั้งที่มีการเปลี่ยนแปลงโค้ด  
10. **จัดทำเอกสารกรณีทดสอบ**: รักษาเอกสารที่ชัดเจนของสถานการณ์การทดสอบ  

## ข้อผิดพลาดทั่วไปในการทดสอบ

- **พึ่งพาการทดสอบเส้นทางที่ราบรื่นมากเกินไป**: อย่าลืมทดสอบกรณีข้อผิดพลาดอย่างละเอียด  
- **ละเลยการทดสอบประสิทธิภาพ**: ระบุคอขวดก่อนที่จะส่งผลกระทบต่อการใช้งานจริง  
- **ทดสอบเฉพาะในสภาพแวดล้อมแยก**: รวมการทดสอบหน่วย, การทดสอบการรวม, และการทดสอบแบบ E2E  
- **การครอบคลุม API ไม่ครบถ้วน**: ตรวจสอบให้แน่ใจว่า endpoints และฟีเจอร์ทั้งหมดได้รับการทดสอบ  
- **สภาพแวดล้อมการทดสอบที่ไม่สม่ำเสมอ**: ใช้คอนเทนเนอร์เพื่อให้แน่ใจว่าสภาพแวดล้อมการทดสอบสม่ำเสมอ  

## สรุป

กลยุทธ์การทดสอบที่ครอบคลุมเป็นสิ่งสำคัญสำหรับการพัฒนาเซิร์ฟเวอร์ MCP ที่เชื่อถือได้และมีคุณภาพสูง ด้วยการนำแนวทางปฏิบัติที่ดีที่สุดและเคล็ดลับที่ระบุไว้ในคู่มือนี้ไปใช้ คุณสามารถมั่นใจได้ว่า MCP ของคุณจะมีคุณภาพ ความน่าเชื่อถือ และประสิทธิภาพในระดับสูงสุด  

## ประเด็นสำคัญ

1. **การออกแบบเครื่องมือ**: ปฏิบัติตามหลักการความรับผิดชอบเดียว ใช้ dependency injection และออกแบบให้สามารถประกอบกันได้  
2. **การออกแบบ Schema**: สร้าง schema ที่ชัดเจน มีเอกสารประกอบ และมีข้อจำกัดการตรวจสอบที่เหมาะสม  
3. **การจัดการข้อผิดพลาด**: ใช้การจัดการข้อผิดพลาดที่ราบรื่น การตอบสนองข้อผิดพลาดที่มีโครงสร้าง และตรรกะการลองใหม่  
4. **ประสิทธิภาพ**: ใช้ caching, การประมวลผลแบบอะซิงโครนัส และการควบคุมทรัพยากร  
5. **ความปลอดภัย**: ใช้การตรวจสอบข้อมูลนำเข้า การตรวจสอบสิทธิ์ และการจัดการข้อมูลที่ละเอียดอ่อนอย่างละเอียด  
6. **การทดสอบ**: สร้างการทดสอบหน่วย การทดสอบการรวม และการทดสอบแบบ end-to-end ที่ครอบคลุม  
7. **รูปแบบการทำงาน**: ใช้รูปแบบที่เป็นที่ยอมรับ เช่น chains, dispatchers, และการประมวลผลแบบขนาน  

## แบบฝึกหัด

ออกแบบเครื่องมือ MCP และ workflow สำหรับระบบประมวลผลเอกสารที่:  

1. รับเอกสารในหลายรูปแบบ (PDF, DOCX, TXT)  
2. ดึงข้อความและข้อมูลสำคัญจากเอกสาร  
3. จัดประเภทเอกสารตามประเภทและเนื้อหา  
4. สร้างสรุปของแต่ละเอกสาร  

ดำเนินการ schema ของเครื่องมือ การจัดการข้อผิดพลาด และรูปแบบ workflow ที่เหมาะสมกับสถานการณ์นี้ พิจารณาว่าคุณจะทดสอบการดำเนินการนี้อย่างไร  

## แหล่งข้อมูล

1. เข้าร่วมชุมชน MCP บน [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) เพื่อรับข่าวสารล่าสุด  
2. มีส่วนร่วมใน [โครงการ MCP แบบโอเพนซอร์ส](https://github.com/modelcontextprotocol)  
3. นำหลักการ MCP ไปใช้ในโครงการ AI ขององค์กรของคุณ  
4. สำรวจการใช้งาน MCP เฉพาะทางสำหรับอุตสาหกรรมของคุณ  
5. พิจารณาเรียนหลักสูตรขั้นสูงในหัวข้อ MCP เฉพาะ เช่น การรวมหลายรูปแบบหรือการรวมแอปพลิเคชันระดับองค์กร  
6. ทดลองสร้างเครื่องมือและ workflow MCP ของคุณเองโดยใช้หลักการที่ได้เรียนรู้ผ่าน [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

ถัดไป: แนวทางปฏิบัติที่ดีที่สุด [กรณีศึกษา](../09-CaseStudy/README.md)  

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้
# แนวทางปฏิบัติที่ดีที่สุดในการพัฒนา MCP

[![แนวทางปฏิบัติที่ดีที่สุดในการพัฒนา MCP](../../../translated_images/th/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

## ภาพรวม

บทเรียนนี้เน้นที่แนวทางปฏิบัติขั้นสูงสำหรับการพัฒนา ทดสอบ และปรับใช้เซิร์ฟเวอร์และฟีเจอร์ MCP ในสภาพแวดล้อมจริง เมื่อระบบนิเวศของ MCP ซับซ้อนและมีความสำคัญมากขึ้น การปฏิบัติตามแบบแผนที่กำหนดไว้ช่วยให้มั่นใจในความน่าเชื่อถือ การบำรุงรักษา และการทำงานร่วมกัน บทเรียนนี้รวบรวมปัญญาที่ได้จากการใช้งานจริงของ MCP เพื่อแนะนำคุณในการสร้างเซิร์ฟเวอร์ที่มั่นคง มีประสิทธิภาพ พร้อมทรัพยากร คำสั่ง และเครื่องมือที่มีประสิทธิผล

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- นำแนวทางปฏิบัติที่ดีที่สุดในอุตสาหกรรมมาใช้ในการออกแบบเซิร์ฟเวอร์และฟีเจอร์ MCP
- สร้างกลยุทธ์การทดสอบที่ครอบคลุมสำหรับเซิร์ฟเวอร์ MCP
- ออกแบบรูปแบบเวิร์กโฟลว์ที่มีประสิทธิภาพและใช้ใหม่ได้สำหรับแอปพลิเคชัน MCP ที่ซับซ้อน
- นำการจัดการข้อผิดพลาด การบันทึก และการสังเกตการณ์ไปใช้ในเซิร์ฟเวอร์ MCP อย่างเหมาะสม
- ปรับปรุงการใช้งาน MCP ให้เหมาะสมกับประสิทธิภาพ ความปลอดภัย และการบำรุงรักษา

## หลักการสำคัญของ MCP

ก่อนที่จะเจาะลึกลงไปในแนวทางปฏิบัติในการใช้งานเฉพาะด้าน สิ่งสำคัญคือการเข้าใจหลักการพื้นฐานที่ชี้นำการพัฒนา MCP อย่างมีประสิทธิภาพ:

1. **การสื่อสารมาตรฐาน**: MCP ใช้ JSON-RPC 2.0 เป็นพื้นฐาน ให้รูปแบบที่สอดคล้องสำหรับคำขอ การตอบสนอง และการจัดการข้อผิดพลาดในทุกการใช้งาน

2. **การออกแบบที่เน้นผู้ใช้เป็นศูนย์กลาง**: ให้ความสำคัญกับการยินยอม การควบคุม และความโปร่งใสของผู้ใช้ในทุกการใช้งาน MCP

3. **ความปลอดภัยเป็นอันดับแรก**: นำนโยบายความปลอดภัยที่แข็งแกร่งมาใช้ รวมถึงการยืนยันตัวตน การอนุญาต การตรวจสอบ และการจำกัดอัตรา

4. **สถาปัตยกรรมแบบโมดูลาร์**: ออกแบบเซิร์ฟเวอร์ MCP ของคุณด้วยแนวทางแบบโมดูลาร์ โดยที่แต่ละเครื่องมือและทรัพยากรมีวัตถุประสงค์ที่ชัดเจนและมุ่งเน้น

5. **สถานะที่ชัดเจน**: MCP `2026-07-28` ไม่มีสถานะที่ระดับโปรโตคอล
   เมื่อเวิร์กโฟลว์ต้องการสถานะข้ามการเรียก ใช้การจัดการที่ชัดเจนหรือ
   อาร์กิวเมนต์เครื่องมือปกติที่สำรองโดยสถานะแอปพลิเคชันที่ทนทาน

## แนวทางปฏิบัติที่ดีที่สุดจากทางการของ MCP

แนวทางปฏิบัติที่ดีที่สุดต่อไปนี้มาจากเอกสารอย่างเป็นทางการของ Model Context Protocol:

### แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย

1. **การยินยอมและการควบคุมของผู้ใช้**: ต้องการการยินยอมที่ชัดเจนจากผู้ใช้ก่อนเข้าถึงข้อมูลหรือดำเนินการใด ๆ ให้การควบคุมที่ชัดเจนเกี่ยวกับข้อมูลที่จะเปิดเผยและการอนุญาตการกระทำต่าง ๆ

2. **ความเป็นส่วนตัวของข้อมูล**: เปิดเผยข้อมูลผู้ใช้เฉพาะเมื่อได้รับความยินยอมอย่างชัดเจนและปกป้องด้วยการควบคุมการเข้าถึงที่เหมาะสม ป้องกันการส่งข้อมูลที่ไม่ได้รับอนุญาต

3. **ความปลอดภัยของเครื่องมือ**: ต้องการการยินยอมที่ชัดเจนจากผู้ใช้ก่อนเรียกใช้เครื่องมือใด ๆ ให้ผู้ใช้เข้าใจฟังก์ชันของแต่ละเครื่องมือและบังคับใช้ขอบเขตความปลอดภัยที่แข็งแกร่ง

4. **การควบคุมสิทธิ์เครื่องมือ**: กำหนดว่าเครื่องมือใดที่โมเดลอาจใช้สำหรับ
   ในแต่ละคำขอและบริบทการอนุญาต โดยมั่นใจว่าเครื่องมือที่เข้าถึงได้
   มีเพียงที่ได้รับอนุญาตอย่างชัดเจนเท่านั้น

5. **การยืนยันตัวตน**: ต้องการการยืนยันตัวตนที่เหมาะสมก่อนให้สิทธิ์การเข้าถึงเครื่องมือ ทรัพยากร หรือการดำเนินการที่มีความละเอียดอ่อนผ่านการใช้คีย์ API โทเค็น OAuth หรือตัววิธีการยืนยันตัวตนที่ปลอดภัยอื่น ๆ

6. **การตรวจสอบพารามิเตอร์**: บังคับให้มีการตรวจสอบสำหรับการเรียกใช้เครื่องมือทั้งหมดเพื่อป้องกันอินพุตที่ผิดรูปแบบหรือเป็นอันตรายจากการเข้าถึงการใช้งานของเครื่องมือ

7. **การจำกัดอัตรา**: นำการจำกัดอัตรามาใช้เพื่อป้องกันการใช้งานเกินสมควรและเพื่อให้การใช้งานทรัพยากรเซิร์ฟเวอร์เป็นธรรม

### แนวทางปฏิบัติที่ดีที่สุดด้านการใช้งาน

1. **การเจรจาขีดความสามารถ**: เจรจาเวอร์ชันโปรโตคอลที่รองรับและ
   ขีดความสามารถ ใน MCP `2026-07-28` แต่ละคำขอจะเป็นอิสระในตัวเองและอาจ
   ใช้ `server/discover`; เวอร์ชันเก่าจะใช้การจับมือในขั้นตอนเริ่มต้น


2. **การออกแบบเครื่องมือ**: สร้างเครื่องมือที่มุ่งเน้นทำงานอย่างใดอย่างหนึ่งได้ดี แทนที่จะเป็นเครื่องมือขนาดใหญ่ที่จัดการหลายเรื่องพร้อมกัน

3. **การจัดการข้อผิดพลาด**: นำข้อความและรหัสข้อผิดพลาดมาตรฐานมาใช้เพื่อช่วยวินิจฉัยปัญหา จัดการความล้มเหลวอย่างมีประสิทธิภาพ และให้ข้อเสนอแนะที่ดำเนินการได้

4. **ความสามารถในการตรวจสอบ**: ใช้ `stderr` สำหรับการวินิจฉัย stdio และ OpenTelemetry
   สำหรับการตรวจสอบที่มีโครงสร้าง ฟีเจอร์การบันทึก MCP ถูกเลิกใช้ใน
   สเปค `2026-07-28`

5. **การติดตามความคืบหน้า**: สำหรับกระบวนการที่ใช้เวลานาน ให้รายงานความคืบหน้าเพื่อเปิดใช้งานส่วนติดต่อผู้ใช้ที่ตอบสนองได้

6. **การยกเลิกคำขอ**: อนุญาตให้ลูกค้ายกเลิกคำขอที่อยู่ระหว่างดำเนินการซึ่งไม่จำเป็นหรือใช้เวลานานเกินไป

## เอกสารอ้างอิงเพิ่มเติม

สำหรับข้อมูลล่าสุดเกี่ยวกับแนวทางปฏิบัติที่ดีที่สุดของ MCP โปรดดูที่:

- [เอกสาร MCP](https://modelcontextprotocol.io/)
- [สเปค MCP (2026-07-28)][mcp-2026-spec]
- [สเปค MCP ก่อนหน้า (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [ส่วนขยายงาน MCP][mcp-tasks-extension]
- [ที่เก็บ GitHub](https://github.com/modelcontextprotocol)
- [แนวทางการปฏิบัติด้านความปลอดภัยที่ดีที่สุด](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - ความเสี่ยงด้านความปลอดภัยและแนวทางป้องกัน
- [เวิร์กช็อป MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - การฝึกอบรมด้านความปลอดภัยแบบลงมือทำ

### บทเรียนประกอบความน่าเชื่อถือ

วนลูปลองใหม่ทั่วไปไม่ปลอดภัยสำหรับเครื่องมือที่สร้างตั๋ว การชำระเงิน,
ข้อความ การปรับใช้ หรือผลลัพธ์ในโลกจริงอื่นๆ การตอบสนองอาจสูญหาย
หลังจากผลกระทบถูกยืนยันแล้ว

ใช้บทเรียนประกอบความน่าเชื่อถือ,
[การลองใหม่อย่างปลอดภัยสำหรับเครื่องมือ MCP: รูปแบบ Reliability Sidecar][reliability-sidecar],
เพื่อเรียนรู้คีย์การทำงานที่เสถียร การรับซ้ำ การสร้างจุดตรวจ,
การปรับให้ตรงกัน ระดับหลักฐาน และการฉีดข้อผิดพลาด

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## ตัวอย่างการใช้งานจริง

### แนวทางปฏิบัติที่ดีที่สุดด้านการออกแบบเครื่องมือ

#### 1. หลักการความรับผิดชอบเดียว

แต่ละเครื่องมือ MCP ควรมีวัตถุประสงค์ที่ชัดเจนและมีจุดมุ่งหมายที่เฉพาะเจาะจง แทนที่จะสร้างเครื่องมือขนาดใหญ่ที่พยายามจัดการหลายเรื่อง ให้พัฒนาเครื่องมือเฉพาะทางที่โดดเด่นในงานที่เฉพาะเจาะจง

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

#### 2. การจัดการข้อผิดพลาดที่สม่ำเสมอ

นำการจัดการข้อผิดพลาดที่เข้มแข็งพร้อมข้อความข้อผิดพลาดที่ให้ข้อมูลและกลไกการกู้คืนที่เหมาะสมมาใช้

```python
# ตัวอย่าง Python พร้อมการจัดการข้อผิดพลาดอย่างครบถ้วน
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # การตรวจสอบพารามิเตอร์
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # การตรวจสอบความปลอดภัย
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # การดำเนินการฐานข้อมูลพร้อมการหมดเวลา
                async with timeout(10):  # หมดเวลา 10 วินาที
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # ข้อผิดพลาดการเชื่อมต่ออาจเป็นชั่วคราว
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # ข้อผิดพลาดของคำสั่งอาจเป็นข้อผิดพลาดของไคลเอนต์
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # ให้ข้อผิดพลาดเฉพาะเครื่องมือผ่านไป
            raise
        except Exception as e:
            # จับข้อผิดพลาดที่ไม่คาดคิดทั้งหมด
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # การใช้งานตรวจจับ SQL injection
        pass
        
    def _log_error(self, message, error):
        # การใช้งานบันทึกข้อผิดพลาด
        pass
```

#### 3. การตรวจสอบพารามิเตอร์

ตรวจสอบพารามิเตอร์อย่างละเอียดเสมอเพื่อป้องกันอินพุตที่ผิดรูปแบบหรือเป็นอันตราย

```javascript
// ตัวอย่าง JavaScript/TypeScript พร้อมการตรวจสอบพารามิเตอร์อย่างละเอียด
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
    // 1. ตรวจสอบการมีอยู่ของพารามิเตอร์
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. ตรวจสอบประเภทของพารามิเตอร์
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. ตรวจสอบค่าของพารามิเตอร์
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. ตรวจสอบการมีเนื้อหาสำหรับการเขียน
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. ตรวจสอบความปลอดภัยของเส้นทาง
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // การดำเนินการตามพารามิเตอร์ที่ได้รับการตรวจสอบแล้ว
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // การดำเนินการตรวจสอบความปลอดภัยของเส้นทาง
    // ...
  }
}
```

### ตัวอย่างการใช้งานด้านความปลอดภัย

#### 1. การพิสูจน์ตัวตนและการอนุญาต

```java
// ตัวอย่าง Java พร้อมการพิสูจน์ตัวตนและการอนุญาต
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // การฉีดขึ้นตอน
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
        // 1. ดึงบริบทการพิสูจน์ตัวตนออกมา
        String authToken = request.getContext().getAuthToken();
        
        // 2. ตรวจสอบตัวตนผู้ใช้
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. ตรวจสอบการอนุญาตสำหรับการดำเนินการเฉพาะ
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. ดำเนินการต่อกับการดำเนินการที่ได้รับอนุญาต
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

## แนวทางปฏิบัติที่ดีที่สุดในการทดสอบ

### 1. การทดสอบหน่วยของเครื่องมือ MCP

ทดสอบเครื่องมือของคุณแยกจากกันเสมอ โดยใช้การ mock กับการขึ้นต่อภายนอก:

```typescript
// ตัวอย่างการทดสอบหน่วยเครื่องมือใน TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // สร้างบริการพยากรณ์อากาศจำลอง
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // สร้างเครื่องมือพร้อมกับการพึ่งพาการจำลอง
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // จัดเตรียม
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // ดำเนินการ
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // ยืนยัน
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // จัดเตรียม
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // ดำเนินการและยืนยัน
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. การทดสอบการบูรณาการ

ทดสอบกระบวนการทั้งหมดตั้งแต่คำขอของลูกค้าจนถึงการตอบสนองของเซิร์ฟเวอร์:

```python
# ตัวอย่างการทดสอบการรวม Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # เริ่มเซิร์ฟเวอร์ทดสอบ
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # สร้างไคลเอนต์
        client = McpClient("http://localhost:5000")
        
        # ทดสอบการค้นหาเครื่องมือ
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # ทดสอบการรันเครื่องมือ
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # ตรวจสอบการตอบกลับ
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # ทำความสะอาด
        await server.stop()
```

## การปรับปรุงประสิทธิภาพ


### 1. กลยุทธ์การแคช

ใช้การแคชที่เหมาะสมเพื่อลดความหน่วงและการใช้ทรัพยากร:


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

#### 2. การฉีดพึ่งพิงและการทดสอบได้

ออกแบบเครื่องมือให้รับการพึ่งพิงผ่านการฉีดผ่านตัวสร้าง (constructor injection) เพื่อให้สามารถทดสอบและกำหนดค่าได้:

```java
// ตัวอย่าง Java พร้อมการฉีดพึ่งพา
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // พึ่งพาถูกฉีดผ่านตัวสร้าง
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // การใช้งานเครื่องมือ
    // ...
}
```

#### 3. เครื่องมือที่ประกอบกันได้

ออกแบบเครื่องมือที่สามารถประกอบเข้าด้วยกันเพื่อสร้างเวิร์กโฟลว์ที่ซับซ้อนมากขึ้น:

```python
# ตัวอย่าง Python ที่แสดงเครื่องมือที่สามารถประกอบกันได้
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # การทำงาน...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # เครื่องมือนี้สามารถใช้ผลลัพธ์จากเครื่องมือดึงข้อมูล
    async def execute_async(self, request):
        # การทำงาน...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # เครื่องมือนี้สามารถใช้ผลลัพธ์จากเครื่องมือวิเคราะห์ข้อมูล
    async def execute_async(self, request):
        # การทำงาน...
        pass

# เครื่องมือเหล่านี้สามารถใช้งานได้อย่างอิสระหรือเป็นส่วนหนึ่งของกระบวนการทำงาน
```

### แนวทางปฏิบัติที่ดีที่สุดในการออกแบบสคีมา

สคีมาเป็นสัญญาระหว่างโมเดลและเครื่องมือของคุณ สคีมาที่ออกแบบได้ดีช่วยเพิ่มความสามารถในการใช้งานเครื่องมือได้ดียิ่งขึ้น

#### 1. คำอธิบายพารามิเตอร์ที่ชัดเจน

ให้ข้อมูลคำอธิบายสำหรับแต่ละพารามิเตอร์เสมอ:

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

#### 2. ข้อจำกัดการตรวจสอบความถูกต้อง

รวมข้อจำกัดการตรวจสอบความถูกต้องเพื่อป้องกันข้อมูลนำเข้าไม่ถูกต้อง:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // คุณสมบัติอีเมลพร้อมการตรวจสอบรูปแบบ
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // คุณสมบัติอายุพร้อมข้อจำกัดเชิงตัวเลข
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // คุณสมบัติแบบระบุค่าได้
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

#### 3. โครงสร้างการตอบกลับที่สม่ำเสมอ

รักษาความสม่ำเสมอในโครงสร้างการตอบกลับเพื่อให้ง่ายต่อการตีความผลลัพธ์ของโมเดล:

```python
async def execute_async(self, request):
    try:
        # ประมวลผลคำขอ
        results = await self._search_database(request.parameters["query"])
        
        # ส่งคืนโครงสร้างที่สม่ำเสมอเสมอ
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

การจัดการข้อผิดพลาดที่เข้มแข็งเป็นสิ่งสำคัญสำหรับเครื่องมือ MCP เพื่อรักษาความน่าเชื่อถือ

#### 1. การจัดการข้อผิดพลาดอย่างสุภาพ

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

#### 2. การตอบกลับข้อผิดพลาดที่มีโครงสร้าง

ส่งข้อมูลข้อผิดพลาดที่มีโครงสร้างเมื่อต้องการ:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // การดำเนินการ
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
        
        // โยนข้อผิดพลาดอื่นๆ ใหม่ในรูปแบบ ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. โลจิกการลองใหม่ (Retry Logic)

ใช้โลจิกการลองใหม่ทั่วไปเฉพาะสำหรับการเรียกอ่านอย่างเดียวหรือการดำเนินการที่
สัญญาลงล่างเป็นไปตามลักษณะ idempotent อยู่แล้ว สำหรับการดำเนินการที่มีผลลัพธ์
เวลาหมดอายุหลังส่งคำขออาจก่อให้เกิดความไม่แน่นอน ประสานสถานะที่เป็นทางการ
และใช้คีย์การดำเนินการที่เสถียรก่อนทำการอีกครั้ง ดูบทเรียน
[reliability sidecar companion lesson](./reliability-sidecars/README.md).

วงล้อการลองใหม่ที่จำกัดต่อไปนี้เหมาะสำหรับการค้นหาอ่านอย่างเดียว:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # วินาที
    
    while retry_count < max_retries:
        try:
            # เรียกใช้ API ภายนอกแบบอ่านอย่างเดียว
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # การหน่วงเวลายกกำลังสอง
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # ข้อผิดพลาดที่ไม่ใช่ชั่วคราว อย่าลองใหม่
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### การเพิ่มประสิทธิภาพ

#### 1. การเก็บแคช

ใช้การเก็บแคชสำหรับการดำเนินการที่มีค่าใช้จ่ายสูง:

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

ใช้รูปแบบการเขียนโปรแกรมแบบอะซิงโครนัสสำหรับการดำเนินการที่ผูกกับ I/O:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // สำหรับการดำเนินการที่ใช้เวลานาน ให้ส่งคืน ID การประมวลผลทันที
        String processId = UUID.randomUUID().toString();
        
        // เริ่มต้นการประมวลผลแบบอะซิงค์
        CompletableFuture.runAsync(() -> {
            try {
                // ดำเนินการตามกระบวนการที่ใช้เวลานาน
                documentService.processDocument(documentId);
                
                // อัปเดตสถานะ (โดยปกติจะเก็บในฐานข้อมูล)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // ส่งคืนการตอบกลับทันทีพร้อมกับ ID กระบวนการ
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // เครื่องมือตรวจสอบสถานะคู่กัน
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

#### 3. การลดความหน่วงของทรัพยากร

ใช้การลดความหน่วงของทรัพยากรเพื่อป้องกันการโหลดเกิน:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # อนุญาต 5 คำขอ ต่อวินาที
            bucket_size=10        # อนุญาตให้ระเบิดสูงสุด 10 คำขอ
        )
    
    async def execute_async(self, request):
        # ตรวจสอบว่าเราสามารถดำเนินการต่อหรือจำเป็นต้องรอ
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # หากการรอนานเกินไป
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # รอเวลาหน่วงที่เหมาะสม
                await asyncio.sleep(delay)
        
        # ใช้โทเค็นหนึ่งอันและดำเนินการคำขอ
        self.rate_limiter.consume()
        
        # เรียก API
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
            
            # คำนวณเวลาจนกว่าโทเค็นถัดไปจะพร้อมใช้งาน
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # เพิ่มโทเค็นใหม่ตามเวลาที่ผ่านไป
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย

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

ดำเนินการตรวจสอบสิทธิ์อย่างถูกต้อง:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // รับบริบทผู้ใช้จากคำขอ
    UserContext user = request.getContext().getUserContext();
    
    // ตรวจสอบว่าผู้ใช้มีสิทธิ์ที่จำเป็นหรือไม่
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // สำหรับทรัพยากรเฉพาะ ให้ตรวจสอบการเข้าถึงทรัพยกรนั้น
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // ดำเนินการต่อด้วยการรันเครื่องมือ
    // ...
}
```

#### 3. การดูแลข้อมูลที่ละเอียดอ่อน

ดูแลข้อมูลที่ละเอียดอ่อนอย่างระมัดระวัง:

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
        
        # รับข้อมูลผู้ใช้
        user_data = await self.user_service.get_user_data(user_id)
        
        # กรองฟิลด์ที่ละเอียดอ่อนเว้นแต่จะมีการร้องขอและได้รับอนุญาตอย่างชัดเจน
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # ตรวจสอบระดับการอนุญาตในบริบทคำขอ
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # สร้างสำเนาเพื่อหลีกเลี่ยงการแก้ไขต้นฉบับ
        redacted = user_data.copy()
        
        # ลบข้อมูลที่ละเอียดอ่อนเฉพาะ
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # ลบข้อมูลที่ละเอียดอ่อนซ้อนอยู่
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## แนวทางปฏิบัติที่ดีที่สุดสำหรับการทดสอบเครื่องมือ MCP

การทดสอบอย่างครอบคลุมช่วยให้มั่นใจว่าเครื่องมือ MCP ทำงานถูกต้อง จัดการกรณีขอบเขต และบูรณาการกับระบบได้อย่างเหมาะสม

### การทดสอบแบบหน่วย (Unit Testing)

#### 1. ทดสอบเครื่องมือแต่ละตัวแยกกัน

สร้างการทดสอบที่เน้นด้านการทำงานของแต่ละเครื่องมือ:

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

#### 2. การทดสอบการตรวจสอบความถูกต้องของสคีมา

ทดสอบว่าสคีมาถูกต้องและบังคับใช้ข้อจำกัดอย่างเหมาะสม:

```java
@Test
public void testSchemaValidation() {
    // สร้างอินสแตนซ์ของเครื่องมือ
    SearchTool searchTool = new SearchTool();
    
    // ดึงสคีมา
    Object schema = searchTool.getSchema();
    
    // แปลงสคีมาเป็น JSON สำหรับการตรวจสอบ
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // ตรวจสอบว่าสคีมาเป็น JSONSchema ที่ถูกต้อง
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // ทดสอบพารามิเตอร์ที่ถูกต้อง
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // ทดสอบพารามิเตอร์ที่จำเป็นหายไป
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // ทดสอบพารามิเตอร์ที่มีชนิดข้อมูลไม่ถูกต้อง
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. การทดสอบการจัดการข้อผิดพลาด

สร้างการทดสอบเฉพาะสำหรับสถานการณ์ข้อผิดพลาด:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # จัดเรียง
    tool = ApiTool(timeout=0.1)  # หมดเวลาสั้นมาก
    
    # จำลองคำขอที่จะหมดเวลา
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # นานกว่าหมดเวลา
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # ดำเนินการ & ตรวจสอบ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # ตรวจสอบข้อความข้อยกเว้น
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # จัดเรียง
    tool = ApiTool()
    
    # จำลองการตอบสนองที่ถูกจำกัดอัตรา
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
        
        # ดำเนินการ & ตรวจสอบ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # ตรวจสอบข้อยกเว้นว่ามีข้อมูลจำกัดอัตราอยู่ด้วย
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### การทดสอบแบบบูรณาการ (Integration Testing)

#### 1. การทดสอบห่วงโซ่เครื่องมือ

ทดสอบเครื่องมือที่ทำงานร่วมกันในรูปแบบที่คาดหวัง:

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

ทดสอบเซิร์ฟเวอร์ MCP ด้วยการลงทะเบียนและการดำเนินการเครื่องมือครบถ้วน:

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
        // ทดสอบจุดสิ้นสุดการค้นพบ
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // สร้างคำขอเครื่องมือ
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // ส่งคำขอและตรวจสอบการตอบกลับ
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // สร้างคำขอเครื่องมือที่ไม่ถูกต้อง
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // ขาดพารามิเตอร์ "b"
        request.put("parameters", parameters);
        
        // ส่งคำขอและตรวจสอบการตอบกลับข้อผิดพลาด
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. การทดสอบปลายทางถึงปลายทาง (End-to-End Testing)

ทดสอบเวิร์กโฟลว์ทั้งหมดตั้งแต่คำสั่งโมเดลจนถึงการดำเนินการเครื่องมือ:


```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # จัดเตรียม - ตั้งค่าลูกค้า MCP และโมเดลจำลอง
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # จำลองการตอบสนองของโมเดล
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
    
    # จำลองการตอบสนองของเครื่องมือพยากรณ์อากาศ
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
        
        # ดำเนินการ
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # ตรวจสอบผล
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### การทดสอบประสิทธิภาพ

#### 1. การทดสอบภาระงาน

ทดสอบจำนวนคำขอที่พร้อมกันที่เซิร์ฟเวอร์ MCP ของคุณสามารถรองรับได้:

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

ทดสอบระบบภายใต้ภาระงานที่สูงสุด:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // ตั้งค่า JMeter สำหรับการทดสอบความเครียด
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // กำหนดแผนการทดสอบ JMeter
    HashTree testPlanTree = new HashTree();
    
    // สร้างแผนการทดสอบ กลุ่มเธรด ตัวสุ่มตัวอย่าง ฯลฯ
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // เพิ่มตัวสุ่มตัวอย่าง HTTP สำหรับการรันเครื่องมือ
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // เพิ่มผู้ฟัง
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // รันการทดสอบ
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // ตรวจสอบผลลัพธ์
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // ระยะเวลาตอบสนองโดยเฉลี่ย < 200 มิลลิวินาที
    assertTrue(summaryReport.getPercentile(90.0) < 500); // ค่าสถิติเชิงเปอร์เซ็นไทล์ที่ 90 < 500 มิลลิวินาที
}
```

#### 3. การตรวจสอบและการวิเคราะห์ประสิทธิภาพ

ตั้งค่าการตรวจสอบเพื่อการวิเคราะห์ประสิทธิภาพระยะยาว:

```python
# กำหนดค่าการตรวจสอบสำหรับเซิร์ฟเวอร์ MCP
def configure_monitoring(server):
    # ตั้งค่าเมตริก Prometheus
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
    
    # เพิ่มมิดเดิลแวร์สำหรับการจับเวลาและบันทึกเมตริก
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # เปิดเผยจุดสิ้นสุดเมตริก
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## รูปแบบการออกแบบเวิร์กโฟลว์ MCP

เวิร์กโฟลว์ MCP ที่ได้รับการออกแบบอย่างดีช่วยเพิ่มประสิทธิภาพ ความน่าเชื่อถือ และความสามารถในการบำรุงรักษา ต่อไปนี้คือรูปแบบสำคัญที่ควรปฏิบัติ:

### 1. รูปแบบลำดับเครื่องมือ

เชื่อมต่อเครื่องมือหลายตัวในลำดับที่เอาต์พุตของเครื่องมือแต่ละตัวกลายเป็นอินพุตของเครื่องมือต่อไป:

```python
# การใช้งาน Python Chain of Tools
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # รายชื่อเครื่องมือที่จะทำงานตามลำดับ
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # ดำเนินการแต่ละเครื่องมือในสายโซ่ โดยส่งผลลัพธ์ก่อนหน้าไป
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # เก็บผลลัพธ์และใช้เป็นอินพุตสำหรับเครื่องมือถัดไป
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# ตัวอย่างการใช้งาน
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

### 2. รูปแบบตัวแจกจ่าย

ใช้เครื่องมือศูนย์กลางที่แจกจ่ายไปยังเครื่องมือเฉพาะตามอินพุต:

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

### 3. รูปแบบการประมวลผลพร้อมกัน

ดำเนินการเครื่องมือหลายตัวพร้อมกันเพื่อประสิทธิภาพ:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // ขั้นตอนที่ 1: ดึงข้อมูลเมตาของชุดข้อมูล (แบบซิงโครนัส)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // ขั้นตอนที่ 2: เปิดการวิเคราะห์หลายแบบพร้อมกัน
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
        
        // รอจนกว่างานแบบขนานทั้งหมดจะเสร็จสิ้น
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // รอจนเสร็จสิ้น
        
        // ขั้นตอนที่ 3: รวมผลลัพธ์
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // ขั้นตอนที่ 4: สร้างรายงานสรุป
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // ส่งคืนผลลัพธ์ของเวิร์กโฟลว์ทั้งหมด
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. รูปแบบการกู้คืนข้อผิดพลาด

นำทางเลือกสำรองมาใช้เมื่อเครื่องมือล้มเหลวอย่างนุ่มนวล:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # ลองใช้เครื่องมือหลักก่อน
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # บันทึกล้มเหลว
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # กลับไปใช้เครื่องมือรอง
            try:
                # อาจต้องแปลงพารามิเตอร์สำหรับเครื่องมือรอง
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # เครื่องมือทั้งสองล้มเหลว
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # การใช้งานนี้ขึ้นอยู่กับเครื่องมือเฉพาะ
        # สำหรับตัวอย่างนี้ เราจะส่งคืนพารามิเตอร์เดิม
        return params

# ตัวอย่างการใช้งาน
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API สภาพอากาศหลัก (แบบจ่ายเงิน)
        "basicWeatherService",    # API สภาพอากาศรอง (ฟรี)
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

# การทดสอบเซิร์ฟเวอร์ MCP: แนวทางปฏิบัติที่ดีที่สุดและคำแนะนำชั้นยอด

## ภาพรวม

การทดสอบเป็นส่วนสำคัญของการพัฒนาเซิร์ฟเวอร์ MCP ที่เชื่อถือได้และคุณภาพสูง คู่มือนี้นำเสนอแนวทางปฏิบัติที่ดีที่สุดและคำแนะนำครอบคลุมสำหรับการทดสอบเซิร์ฟเวอร์ MCP ของคุณตลอดวงจรการพัฒนา ตั้งแต่การทดสอบหน่วยไปจนถึงการทดสอบแบบบูรณาการและการตรวจสอบครบวงจร

## ทำไมการทดสอบจึงสำคัญสำหรับเซิร์ฟเวอร์ MCP

เซิร์ฟเวอร์ MCP ทำหน้าที่เป็นชั้นกลางสำคัญระหว่างโมเดล AI และแอปพลิเคชันของลูกค้า การทดสอบอย่างละเอียดช่วยให้มั่นใจว่า:

- ความน่าเชื่อถือในสภาพแวดล้อมการผลิต
- การจัดการคำขอและการตอบสนองที่ถูกต้องแม่นยำ
- การนำสเปก MCP ไปใช้อย่างถูกต้อง
- ความสามารถในการฟื้นตัวจากความล้มเหลวและกรณีขอบ
- ประสิทธิภาพที่สม่ำเสมอภายใต้ภาระงานหลากหลาย

## การทดสอบหน่วยสำหรับเซิร์ฟเวอร์ MCP

### การทดสอบหน่วย (พื้นฐาน)

การทดสอบหน่วยตรวจสอบส่วนประกอบเดี่ยวของเซิร์ฟเวอร์ MCP ของคุณอย่างแยกกัน

#### สิ่งที่ต้องทดสอบ

1. **ตัวจัดการทรัพยากร**: ทดสอบตรรกะของตัวจัดการทรัพยากรแต่ละตัวอย่างอิสระ
2. **การใช้งานเครื่องมือ**: ตรวจสอบพฤติกรรมเครื่องมือด้วยอินพุตหลากหลาย
3. **แม่แบบพร้อมท์**: ตรวจสอบว่าแม่แบบพร้อมท์เรนเดอร์ถูกต้อง
4. **การตรวจสอบสคีมา**: ทดสอบตรรกะการตรวจสอบพารามิเตอร์
5. **การจัดการข้อผิดพลาด**: ตรวจสอบการตอบสนองข้อผิดพลาดสำหรับอินพุตที่ไม่ถูกต้อง

#### แนวทางปฏิบัติที่ดีที่สุดสำหรับการทดสอบหน่วย

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
# ตัวอย่างการทดสอบหน่วยสำหรับเครื่องคิดเลขใน Python
def test_calculator_tool_add():
    # จัดเตรียม
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # ดำเนินการ
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # ตรวจสอบผลลัพธ์
    assert result["value"] == 12
```

### การทดสอบแบบบูรณาการ (ชั้นกลาง)

การทดสอบแบบบูรณาการตรวจสอบปฏิสัมพันธ์ระหว่างส่วนประกอบของเซิร์ฟเวอร์ MCP ของคุณ

#### สิ่งที่ต้องทดสอบ

1. **การเริ่มต้นเซิร์ฟเวอร์**: ทดสอบการเริ่มต้นเซิร์ฟเวอร์พร้อมการกำหนดค่าหลากหลาย
2. **การลงทะเบียนเส้นทาง**: ตรวจสอบว่าจุดสิ้นสุดทั้งหมดลงทะเบียนถูกต้อง
3. **การประมวลผลคำขอ**: ทดสอบรอบคำขอ-ตอบสนองเต็มรูปแบบ
4. **การแพร่กระจายข้อผิดพลาด**: ให้แน่ใจว่าข้อผิดพลาดถูกจัดการอย่างถูกต้องในส่วนประกอบต่างๆ
5. **การยืนยันตัวตนและการอนุญาต**: ทดสอบกลไกความปลอดภัย

#### แนวทางปฏิบัติที่ดีที่สุดสำหรับการทดสอบแบบบูรณาการ

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

### การทดสอบครบวงจร (ชั้นบน)

การทดสอบครบวงจรตรวจสอบพฤติกรรมระบบโดยรวมจากลูกค้าไปยังเซิร์ฟเวอร์

#### สิ่งที่ต้องทดสอบ

1. **การสื่อสารลูกค้า-เซิร์ฟเวอร์**: ทดสอบรอบคำขอ-ตอบสนองครบถ้วน
2. **SDK ลูกค้าจริง**: ทดสอบกับการใช้งานลูกค้าจริง
3. **ประสิทธิภาพภายใต้ภาระงาน**: ตรวจสอบพฤติกรรมกับคำขอพร้อมกันหลายรายการ
4. **การกู้คืนข้อผิดพลาด**: ทดสอบการกู้ระบบจากความล้มเหลว

5. **การทำงานระยะยาว**: ตรวจสอบการจัดการการสตรีมและการทำงานระยะยาว

#### แนวทางปฏิบัติที่ดีที่สุดสำหรับการทดสอบ E2E

```typescript
// ตัวอย่างการทดสอบ E2E กับไคลเอนต์ใน TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // เริ่มเซิร์ฟเวอร์ในสภาพแวดล้อมการทดสอบ
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // ปฏิบัติ
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // ตรวจสอบผล
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## กลยุทธ์การจำลองสำหรับการทดสอบ MCP

การจำลองเป็นสิ่งจำเป็นสำหรับการแยกส่วนประกอบในระหว่างการทดสอบ

### ส่วนประกอบที่ต้องจำลอง

1. **โมเดล AI ภายนอก**: จำลองการตอบสนองของโมเดลเพื่อการทดสอบที่คาดเดาได้
2. **บริการภายนอก**: จำลองการพึ่งพา API (ฐานข้อมูล บริการบุคคลที่สาม)
3. **บริการตรวจสอบสิทธิ์**: จำลองผู้ให้บริการตัวตน
4. **ผู้ให้บริการทรัพยากร**: จำลองผู้จัดการทรัพยากรที่มีราคาแพง

### ตัวอย่าง: การจำลองการตอบสนองของโมเดล AI

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
# ตัวอย่าง Python กับ unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # กำหนดค่า mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # ใช้ mock ในการทดสอบ
    server = McpServer(model_client=mock_model)
    # ดำเนินการทดสอบต่อ
```

## การทดสอบประสิทธิภาพ

การทดสอบประสิทธิภาพเป็นสิ่งสำคัญสำหรับเซิร์ฟเวอร์ MCP ในการผลิต

### สิ่งที่ต้องวัด

1. **ค่าหน่วงเวลา**: เวลาตอบสนองสำหรับคำขอ
2. **อัตราการประมวลผล**: จำนวนคำขอที่จัดการได้ต่อวินาที
3. **การใช้ทรัพยากร**: การใช้ CPU, หน่วยความจำ, เครือข่าย
4. **การจัดการความพร้อมกัน**: พฤติกรรมภายใต้คำขอแบบขนาน
5. **ลักษณะการปรับขนาด**: ประสิทธิภาพเมื่อโหลดเพิ่มขึ้น

### เครื่องมือสำหรับการทดสอบประสิทธิภาพ

- **k6**: เครื่องมือทดสอบโหลดแบบโอเพนซอร์ส
- **JMeter**: การทดสอบประสิทธิภาพแบบครอบคลุม
- **Locust**: เครื่องมือทดสอบโหลดที่ใช้ Python
- **Azure Load Testing**: การทดสอบประสิทธิภาพบนคลาวด์

### ตัวอย่าง: การทดสอบโหลดพื้นฐานด้วย k6

```javascript
// สคริปต์ k6 สำหรับทดสอบความทนทานของเซิร์ฟเวอร์ MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // ผู้ใช้เสมือน 10 คน
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

## การทดสอบอัตโนมัติสำหรับเซิร์ฟเวอร์ MCP

การทำให้อัตโนมัติในการทดสอบช่วยให้มั่นใจในคุณภาพสม่ำเสมอและวงจรตอบกลับที่รวดเร็วขึ้น

### การรวม CI/CD

1. **รันการทดสอบหน่วยเมื่อมี Pull Requests**: ตรวจสอบให้แน่ใจว่าการเปลี่ยนแปลงโค้ดไม่ทำให้ฟังก์ชันเดิมเสีย
2. **ทดสอบการรวมในสเตจจิ้ง**: รันทดสอบการรวมในสภาพแวดล้อมก่อนผลิต
3. **เก็บบรรทัดฐานประสิทธิภาพ**: รักษามาตรฐานประสิทธิภาพเพื่อตรวจจับการถดถอย
4. **สแกนความปลอดภัย**: ทำการทดสอบความปลอดภัยโดยอัตโนมัติเป็นส่วนหนึ่งของกระบวนการ

### ตัวอย่างท่อ CI (GitHub Actions)

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

## การทดสอบเพื่อให้เป็นไปตามข้อกำหนด MCP

ตรวจสอบให้แน่ใจว่าเซิร์ฟเวอร์ของคุณปฏิบัติตามข้อกำหนด MCP อย่างถูกต้อง

### พื้นที่สำคัญของการปฏิบัติตาม

1. **API Endpoints**: ทดสอบจุดสิ้นสุดที่จำเป็น (/resources, /tools, เป็นต้น)
2. **รูปแบบคำขอ/คำตอบ**: ตรวจสอบความถูกต้องของสคีมา
3. **รหัสข้อผิดพลาด**: ตรวจสอบว่าใช้รหัสสถานะที่ถูกต้องสำหรับสถานการณ์ต่าง ๆ
4. **ประเภทเนื้อหา**: ทดสอบการจัดการประเภทเนื้อหาต่าง ๆ
5. **กระบวนการตรวจสอบสิทธิ์**: ตรวจสอบให้แน่ใจว่าเป็นไปตามข้อกำหนดการยืนยันตัวตน

### ชุดทดสอบการปฏิบัติตาม

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

## 10 เคล็ดลับยอดนิยมสำหรับการทดสอบเซิร์ฟเวอร์ MCP อย่างมีประสิทธิภาพ

1. **แยกทดสอบการกำหนดเครื่องมือ**: ตรวจสอบการกำหนดสคีมาแยกจากตรรกะของเครื่องมือ
2. **ใช้การทดสอบที่มีพารามิเตอร์**: ทดสอบเครื่องมือด้วยอินพุตหลากหลายรวมถึงกรณีพิเศษ
3. **ตรวจสอบการตอบสนองข้อผิดพลาด**: ตรวจสอบการจัดการข้อผิดพลาดที่เหมาะสมสำหรับทุกเงื่อนไข
4. **ทดสอบตรรกะการอนุญาต**: ให้แน่ใจว่าการควบคุมการเข้าถึงถูกต้องสำหรับบทบาทผู้ใช้ต่าง ๆ
5. **ติดตามความครอบคลุมการทดสอบ**: ตั้งเป้าความครอบคลุมสูงของโค้ดเส้นทางสำคัญ
6. **ทดสอบการตอบสนองแบบสตรีมมิ่ง**: ตรวจสอบการจัดการเนื้อหาที่สตรีมได้อย่างถูกต้อง
7. **จำลองปัญหาเครือข่าย**: ทดสอบพฤติกรรมในสภาพแวดล้อมเครือข่ายที่ไม่ดี
8. **ทดสอบขีดจำกัดทรัพยากร**: ตรวจสอบพฤติกรรมเมื่อถึงโควตาหรือขีดจำกัดอัตรา
9. **ทำให้อัตโนมัติการทดสอบถดถอย**: สร้างชุดทดสอบที่ทำงานทุกครั้งที่เปลี่ยนแปลงโค้ด
10. **บันทึกกรณีทดสอบอย่างละเอียด**: รักษาการบันทึกที่ชัดเจนของสถานการณ์ทดสอบ

## ความผิดพลาดทั่วไปในการทดสอบ

- **พึ่งพาการทดสอบเส้นทางที่สำเร็จมากเกินไป**: ตรวจสอบให้แน่ใจว่าทดสอบกรณีข้อผิดพลาดอย่างละเอียด
- **ละเลยการทดสอบประสิทธิภาพ**: ค้นหาคอขวดก่อนที่มีผลต่อการผลิต
- **ทดสอบแบบแยกส่วนเพียงอย่างเดียว**: รวมการทดสอบหน่วย การทดสอบการรวม และ E2E
- **ความครอบคลุม API ไม่ครบถ้วน**: ตรวจสอบให้แน่ใจว่าจุดสิ้นสุดและฟีเจอร์ทั้งหมดถูกทดสอบ
- **สภาพแวดล้อมทดสอบไม่สม่ำเสมอ**: ใช้คอนเทนเนอร์เพื่อให้ได้สภาพแวดล้อมทดสอบที่เหมือนกัน

## สรุป

ยุทธศาสตร์การทดสอบที่ครอบคลุมเป็นสิ่งสำคัญสำหรับการพัฒนาเซิร์ฟเวอร์ MCP ที่เชื่อถือได้และมีคุณภาพสูง โดยการปรับใช้แนวทางปฏิบัติที่ดีที่สุดและเคล็ดลับในคู่มือนี้ คุณจะมั่นใจว่า MCP ที่พัฒนาขึ้นตรงตามมาตรฐานสูงสุดด้านคุณภาพ ความน่าเชื่อถือ และประสิทธิภาพ


## ประเด็นสำคัญ

1. **การออกแบบเครื่องมือ**: ปฏิบัติตามหลักการความรับผิดชอบเดียว ใช้การฉีดพึ่งพิง และออกแบบเพื่อความสามารถในการประกอบ
2. **การออกแบบสคีมา**: สร้างสคีมาที่ชัดเจน มีเอกสารดี และข้อจำกัดที่ถูกต้องในการตรวจสอบ
3. **การจัดการข้อผิดพลาด**: ปฏิบัติการจัดการข้อผิดพลาดอย่างราบรื่น ตอบสนองข้อผิดพลาดแบบมีโครงสร้าง และตรรกะการลองใหม่โดยคำนึงถึงผลลัพธ์

4. **ประสิทธิภาพ**: ใช้แคช การประมวลผลแบบอะซิงโครนัส และการจำกัดทรัพยากร
5. **ความปลอดภัย**: ใช้การตรวจสอบข้อมูลเข้าอย่างละเอียด ตรวจสอบการอนุญาต และการจัดการข้อมูลที่ละเอียดอ่อน
6. **การทดสอบ**: สร้างการทดสอบหน่วย การทดสอบการรวม และการทดสอบแบบครบวงจร
7. **รูปแบบกระบวนการทำงาน**: ใช้รูปแบบที่ยอมรับ เช่น โซ่, ผู้กระจาย, และการประมวลผลแบบขนาน

## แบบฝึกหัด

ออกแบบเครื่องมือและกระบวนการ MCP สำหรับระบบประมวลผลเอกสารที่:

1. รับเอกสารในหลายรูปแบบ (PDF, DOCX, TXT)
2. สกัดข้อความและข้อมูลสำคัญจากเอกสาร
3. จัดประเภทเอกสารตามประเภทและเนื้อหา
4. สร้างสรุปของแต่ละเอกสาร

นำไปปฏิบัติการสคีมาของเครื่องมือ การจัดการข้อผิดพลาด และรูปแบบกระบวนการทำงานที่เหมาะสมกับสถานการณ์พิจารณาว่าคุณจะทดสอบการนำไปใช้นี้อย่างไร

## แหล่งข้อมูล

1. เข้าร่วมชุมชน MCP บน [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) เพื่อรับข่าวสารล่าสุดเกี่ยวกับการพัฒนา
2. ร่วมมีส่วนร่วมในโครงการโอเพนซอร์ส [MCP projects](https://github.com/modelcontextprotocol)
3. นำหลักการ MCP ไปปรับใช้ในโครงการ AI ขององค์กรของคุณเอง
4. สำรวจการนำ MCP ไปใช้เฉพาะอุตสาหกรรมของคุณ
5. พิจารณาเรียนหลักสูตรขั้นสูงเกี่ยวกับหัวข้อเฉพาะของ MCP เช่น การบูรณาการมัลติ-โหมด หรือการบูรณาการแอปพลิเคชันองค์กร
6. ทดลองสร้างเครื่องมือและกระบวนการ MCP ของคุณเองโดยใช้หลักการที่เรียนรู้ผ่าน [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

## ต่อไป

ต่อไป: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
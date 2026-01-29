# MCP மேம்பாட்டு சிறந்த நடைமுறைகள்

[![MCP மேம்பாட்டு சிறந்த நடைமுறைகள்](../../../translated_images/ta/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(மேலே உள்ள படத்தை கிளிக் செய்து இந்த பாடத்தின் வீடியோவைப் பாருங்கள்)_

## கண்ணோட்டம்

இந்த பாடம் MCP சர்வர்கள் மற்றும் அம்சங்களை உற்பத்தி சூழல்களில் உருவாக்க, சோதனை செய்ய மற்றும் வெளியிடுவதற்கான மேம்பட்ட சிறந்த நடைமுறைகளை மையமாகக் கொண்டுள்ளது. MCP சூழல்கள் சிக்கலான மற்றும் முக்கியமானதாக வளரும்போது, நிறுவப்பட்ட முறைமைகளை பின்பற்றுவது நம்பகத்தன்மை, பராமரிப்பு மற்றும் பரஸ்பர செயல்பாட்டை உறுதிப்படுத்துகிறது. இந்த பாடம் உண்மையான MCP செயல்பாடுகளில் இருந்து பெறப்பட்ட நடைமுறை அறிவை ஒருங்கிணைத்து, வலுவான, திறமையான MCP சர்வர்களை உருவாக்க வழிகாட்டுகிறது.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- MCP சர்வர் மற்றும் அம்ச வடிவமைப்பில் தொழில்துறை சிறந்த நடைமுறைகளைப் பயன்படுத்த முடியும்
- MCP சர்வர்களுக்கான விரிவான சோதனை உத்திகளை உருவாக்க முடியும்
- சிக்கலான MCP பயன்பாடுகளுக்கான திறமையான, மீண்டும் பயன்படுத்தக்கூடிய வேலைப்பாடுகளை வடிவமைக்க முடியும்
- MCP சர்வர்களில் சரியான பிழை கையாளுதல், பதிவு மற்றும் கண்காணிப்பை செயல்படுத்த முடியும்
- செயல்திறன், பாதுகாப்பு மற்றும் பராமரிப்புக்கான MCP செயல்பாடுகளை மேம்படுத்த முடியும்

## MCP முக்கியக் கொள்கைகள்

குறிப்பிட்ட செயல்பாட்டு நடைமுறைகளில் இறங்குவதற்கு முன், MCP மேம்பாட்டைச் செயல்படுத்த வழிகாட்டும் முக்கியக் கொள்கைகளைப் புரிந்துகொள்வது முக்கியம்:

1. **மிகைப்படுத்தப்பட்ட தொடர்பு**: MCP JSON-RPC 2.0 ஐ அடிப்படையாகக் கொண்டது, அனைத்து செயல்பாடுகளிலும் கோரிக்கைகள், பதில்கள் மற்றும் பிழை கையாளுதலுக்கான ஒரே வடிவத்தை வழங்குகிறது.

2. **பயனர் மையமான வடிவமைப்பு**: MCP செயல்பாடுகளில் எப்போதும் பயனர் ஒப்புதல், கட்டுப்பாடு மற்றும் வெளிப்படைத்தன்மையை முன்னுரிமை அளிக்கவும்.

3. **பாதுகாப்பு முதலில்**: அங்கீகாரம், அனுமதி, சரிபார்ப்பு மற்றும் விகித வரையறை ஆகியவற்றை உள்ளடக்கிய வலுவான பாதுகாப்பு நடவடிக்கைகளை செயல்படுத்தவும்.

4. **தொகுதி கட்டமைப்பு**: ஒவ்வொரு கருவி மற்றும் வளமும் தெளிவான, மையமான நோக்கத்துடன் இருக்கும் வகையில் MCP சர்வர்களை தொகுதி அணுகுமுறையுடன் வடிவமைக்கவும்.

5. **நிலைமையான இணைப்புகள்**: பல கோரிக்கைகளுக்கு இடையில் நிலையை பராமரிக்க MCP இன் திறனை பயன்படுத்தி, மேலும் தெளிவான மற்றும் சூழலுக்கு பொருந்தக்கூடிய தொடர்புகளை உருவாக்கவும்.

## MCP அதிகாரப்பூர்வ சிறந்த நடைமுறைகள்

அதிகாரப்பூர்வ Model Context Protocol ஆவணங்களில் இருந்து பெறப்பட்ட சிறந்த நடைமுறைகள் பின்வருமாறு:

### பாதுகாப்பு சிறந்த நடைமுறைகள்

1. **பயனர் ஒப்புதல் மற்றும் கட்டுப்பாடு**: தரவுகளை அணுகுவதற்கு அல்லது செயல்பாடுகளைச் செய்யும் முன் எப்போதும் வெளிப்படையான பயனர் ஒப்புதலை தேவைப்படுத்தவும். எந்த தரவுகள் பகிரப்படுகின்றன மற்றும் எந்த நடவடிக்கைகள் அங்கீகரிக்கப்படுகின்றன என்பதை தெளிவாகக் கூறவும்.

2. **தரவு தனியுரிமை**: வெளிப்படையான ஒப்புதலுடன் மட்டுமே பயனர் தரவுகளை வெளிப்படுத்தவும் மற்றும் அதனை சரியான அணுகல் கட்டுப்பாடுகளுடன் பாதுகாக்கவும். அனுமதியில்லாத தரவுப் பரிமாற்றத்திலிருந்து பாதுகாக்கவும்.

3. **கருவி பாதுகாப்பு**: எந்த கருவியையும் இயக்குவதற்கு முன் வெளிப்படையான பயனர் ஒப்புதலை தேவைப்படுத்தவும். ஒவ்வொரு கருவியின் செயல்பாட்டை பயனர்கள் புரிந்துகொள்ளவும் மற்றும் வலுவான பாதுகாப்பு எல்லைகளை அமல்படுத்தவும்.

4. **கருவி அனுமதி கட்டுப்பாடு**: ஒரு அமர்வின் போது ஒரு மாதிரி எந்த கருவிகளைப் பயன்படுத்த அனுமதிக்கப்படுகிறது என்பதை உள்ளமைக்கவும், வெளிப்படையாக அங்கீகரிக்கப்பட்ட கருவிகள் மட்டுமே அணுகக்கூடியவை என்பதை உறுதிப்படுத்தவும்.

5. **அங்கீகாரம்**: API கீக்கள், OAuth டோக்கன்கள் அல்லது பிற பாதுகாப்பான அங்கீகார முறைகளைப் பயன்படுத்தி கருவிகள், வளங்கள் அல்லது நுணுக்கமான செயல்பாடுகளுக்கு அணுகலை வழங்குவதற்கு முன் சரியான அங்கீகாரத்தை தேவைப்படுத்தவும்.

6. **அளவுரு சரிபார்ப்பு**: கருவி செயல்பாடுகளுக்கு தவறான அல்லது தீவிர உள்ளீடுகளைத் தடுக்க அனைத்து அழைப்புகளுக்கும் சரிபார்ப்பை அமல்படுத்தவும்.

7. **விகித வரையறை**: MCP சர்வர் வளங்களை நியாயமான முறையில் பயன்படுத்தவும் மற்றும் தவறாக பயன்படுத்துவதைத் தடுக்க விகித வரையறையை செயல்படுத்தவும்.

### செயல்பாட்டு சிறந்த நடைமுறைகள்

1. **திறன் பேச்சுவார்த்தை**: இணைப்பு அமைப்பின் போது, ஆதரிக்கப்படும் அம்சங்கள், நெறிமுறை பதிப்புகள், கிடைக்கக்கூடிய கருவிகள் மற்றும் வளங்கள் பற்றிய தகவல்களை பரிமாறவும்.

2. **கருவி வடிவமைப்பு**: பல கவலைகளை கையாளும் மொத்த கருவிகளை உருவாக்குவதற்குப் பதிலாக, ஒரு விஷயத்தை நன்றாகச் செய்யும் மையமான கருவிகளை உருவாக்கவும்.

3. **பிழை கையாளுதல்**: சிக்கல்களைத் தீர்க்க உதவும், தோல்விகளை நன்றாக கையாளவும் மற்றும் செயல்படக்கூடிய கருத்துகளை வழங்கவும், தரநிலையான பிழை செய்திகளையும் குறியீடுகளையும் செயல்படுத்தவும்.

4. **பதிவு**: நெறிமுறை தொடர்புகளை கண்காணிக்க, பிழை தீர்க்க மற்றும் கண்காணிக்க அமைக்கப்பட்ட பதிவுகளை உள்ளமைக்கவும்.

5. **முன்னேற்ற கண்காணிப்பு**: நீண்ட செயல்பாடுகளுக்கு, பதிலளிக்கக்கூடிய பயனர் இடைமுகங்களை இயக்க முன்னேற்றப் புதுப்பிப்புகளைப் புகாரளிக்கவும்.

6. **கோரிக்கை ரத்து**: தேவையில்லாத அல்லது அதிக நேரம் எடுத்துக்கொள்ளும் கோரிக்கைகளை ரத்து செய்ய வாடிக்கையாளர்களுக்கு அனுமதி அளிக்கவும்.

## கூடுதல் குறிப்புகள்

MCP சிறந்த நடைமுறைகள் பற்றிய சமீபத்திய தகவல்களுக்கு, பின்வரும் இணைப்புகளைப் பார்க்கவும்:

- [MCP ஆவணங்கள்](https://modelcontextprotocol.io/)
- [MCP விவரக்குறிப்பு](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [பாதுகாப்பு சிறந்த நடைமுறைகள்](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## நடைமுறை செயல்பாட்டு உதாரணங்கள்

### கருவி வடிவமைப்பு சிறந்த நடைமுறைகள்

#### 1. ஒற்றை பொறுப்பு கொள்கை

ஒவ்வொரு MCP கருவியும் தெளிவான, மையமான நோக்கத்துடன் இருக்க வேண்டும். பல கவலைகளை கையாள முயற்சிக்கும் மொத்த கருவிகளை உருவாக்குவதற்குப் பதிலாக, குறிப்பிட்ட பணிகளில் சிறப்பாக செயல்படும் சிறப்பு கருவிகளை உருவாக்கவும்.

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

#### 2. நிலையான பிழை கையாளுதல்

தகவலளிக்கும் பிழை செய்திகளுடன் வலுவான பிழை கையாளுதலை செயல்படுத்தவும் மற்றும் பொருத்தமான மீட்பு முறைகளை உள்ளமைக்கவும்.

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

#### 3. அளவுரு சரிபார்ப்பு

தவறான அல்லது தீவிர உள்ளீடுகளைத் தடுக்க, அளவுருக்களை எப்போதும் முழுமையாகச் சரிபார்க்கவும்.

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

### பாதுகாப்பு செயல்பாட்டு உதாரணங்கள்

#### 1. அங்கீகாரம் மற்றும் அனுமதி

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

#### 2. விகித வரையறை

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

## சோதனை சிறந்த நடைமுறைகள்

### 1. MCP கருவிகளுக்கான யூனிட் சோதனை

வெளிப்புற சார்புகளை மொக்கிங் செய்து, உங்கள் கருவிகளை தனித்துவமாகச் சோதிக்கவும்:

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

### 2. ஒருங்கிணைப்பு சோதனை

வாடிக்கையாளர் கோரிக்கைகளிலிருந்து சர்வர் பதில்கள் வரை முழு ஓட்டத்தைச் சோதிக்கவும்:

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

## செயல்திறன் மேம்பாடு

### 1. கேஷிங் உத்திகள்

தாமதம் மற்றும் வள பயன்பாட்டை குறைக்க பொருத்தமான கேஷிங்கை செயல்படுத்தவும்:

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

#### 2. சார்பு ஊடுருவல் மற்றும் சோதனை திறன்

கருவிகள் தங்கள் சார்புகளை கட்டமைப்பாளர் ஊடுருவலின் மூலம் பெறும் வகையில் வடிவமைக்கவும், அவற்றை சோதிக்கக்கூடிய மற்றும் உள்ளமைக்கக்கூடியதாக மாற்றவும்:

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

#### 3. இணைக்கக்கூடிய கருவிகள்

மேலும் சிக்கலான வேலைப்பாடுகளை உருவாக்க பல கருவிகளை இணைக்கக்கூடியதாக வடிவமைக்கவும்:

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

### ஸ்கீமா வடிவமைப்பு சிறந்த நடைமுறைகள்

ஸ்கீமா என்பது மாதிரி மற்றும் உங்கள் கருவிக்கிடையேயான ஒப்பந்தமாகும். நன்றாக வடிவமைக்கப்பட்ட ஸ்கீமாக்கள் கருவி பயன்பாட்டை மேம்படுத்துகின்றன.

#### 1. தெளிவான அளவுரு விளக்கங்கள்

ஒவ்வொரு அளவுருவிற்கும் விளக்கமான தகவல்களை எப்போதும் சேர்க்கவும்:

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

#### 2. சரிபார்ப்பு கட்டுப்பாடுகள்

தவறான உள்ளீடுகளைத் தடுக்க சரிபார்ப்பு கட்டுப்பாடுகளைச் சேர்க்கவும்:

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

#### 3. நிலையான பதில் அமைப்புகள்

மாதிரிகள் முடிவுகளை விளக்க எளிதாக இருக்க பதில் அமைப்புகளில் நிலைத்தன்மையை பராமரிக்கவும்:

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

### பிழை கையாளுதல்

MCP கருவிகளின் நம்பகத்தன்மையை பராமரிக்க வலுவான பிழை கையாளுதல் முக்கியம்.

#### 1. நன்றாக பிழை கையாளுதல்

பிழைகளை பொருத்தமான நிலைகளில் கையாளவும் மற்றும் தகவலளிக்கும் செய்திகளை வழங்கவும்:

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

#### 2. அமைக்கப்பட்ட பிழை பதில்கள்

சாத்தியமான போது அமைக்கப்பட்ட பிழை தகவலைத் திருப்பவும்:

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

#### 3. மீண்டும் முயற்சி செய்யும் முறை

தற்காலிக தோல்விகளுக்கு பொருத்தமான மீண்டும் முயற்சி செய்யும் முறையை செயல்படுத்தவும்:

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

### செயல்திறன் மேம்பாடு

#### 1. கேஷிங்

செலவான செயல்பாடுகளுக்கு கேஷிங்கை செயல்படுத்தவும்:

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

#### 2. அசிங்க செயல்பாடு

I/O சார்ந்த செயல்பாடுகளுக்கு அசிங்க நிரலாக்க முறைகளைப் பயன்படுத்தவும்:

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

#### 3. வளக் கட்டுப்பாடு

அதிக சுமையைத் தடுக்க வளக் கட்டுப்பாட்டை செயல்படுத்தவும்:

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

### பாதுகாப்பு சிறந்த நடைமுறைகள்

#### 1. உள்ளீடு சரிபார்ப்பு

அளவுரு உள்ளீடுகளை எப்போதும் முழுமையாகச் சரிபார்க்கவும்:

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

#### 2. அனுமதி சரிபார்ப்பு

சரியான அனுமதி சரிபார்ப்புகளை செயல்படுத்தவும்:

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

#### 3. நுணுக்கமான தரவுகளை கையாளுதல்

நுணுக்கமான தரவுகளை கவனமாக கையாளவும்:

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

## MCP கருவிகளுக்கான சோதனை சிறந்த நடைமுறைகள்

விரிவான சோதனை MCP கருவிகள் சரியாக செயல்படுவதை, விளிம்பு வழக்குகளை கையாளுவதை மற்றும் மொத்த அமைப்புடன் சரியாக ஒருங்கிணைக்கப்படுவதை உறுதிப்படுத்துகிறது.

### யூனிட் சோதனை

#### 1. ஒவ்வொரு கருவியையும் தனித்துவமாகச் சோதிக்கவும்

ஒவ்வொரு கருவியின் செயல்பாட்டிற்கான மைய சோதனைகளை உருவாக்கவும்:

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

#### 2. ஸ்கீமா சரிபார்ப்பு சோதனை

ஸ்கீமாக்கள் செல்லுபடியாகும் மற்றும் சரிபார்ப்பு கட்டுப்பாடுகளை சரியாக அமல்படுத்துவதைச் சோதிக்கவும்:

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

#### 3. பிழை கையாளுதல் சோதனைகள்

பிழை நிலைகளுக்கான குறிப்பிட்ட சோதனைகளை உருவாக்கவும்:

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

### ஒருங்கிணைப்பு சோதனை

#### 1. கருவி சங்கிலி சோதனை

எதிர்பார்க்கப்பட்ட இணைப்புகளில் வேலை செய்யும் கருவிகளைச் சோதிக்கவும்:

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

#### 2. MCP சர்வர் சோதனை

முழு கருவி பதிவு மற்றும் செயல்பாட்டுடன் MCP சர்வரைச் சோதிக்கவும்:

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

#### 3. முடிவு முதல் இறுதி வரை சோதனை

மாதிரி உந்துதல் முதல் கருவி செயல்பாடு வரை முழு வேலைப்பாடுகளைச் சோதிக்கவும்:

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

### செயல்திறன் சோதனை

#### 1. சுமை சோதனை

உங்கள் MCP சர்வர் எவ்வளவு ஒரே நேரத்தில் கோரிக்கைகளை கையாள முடியும் என்பதைச் சோதிக்கவும்:

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

#### 2. அழுத்த சோதனை

அதிக சுமையின் கீழ் அமைப்பைச் சோதிக்கவும்:

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

#### 3. கண்காணிப்பு மற்றும் சுயவிவர அமைப்பு

நீண்டகால செயல்திறன் பகுப்பாய்வுக்கான கண்காணிப்பை அமைக்கவும்:

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

## MCP வேலைப்பாடு வடிவமைப்பு முறைமைகள்

நன்றாக வடிவமைக்கப்பட்ட MCP வேலைப்பாடுகள் திறன், நம்பகத்தன்மை மற்றும் பராமரிப்பை மேம்படுத்துகின்றன. பின்வரும் முக்கிய முறைமைகளைப் பின்பற்றவும்:

### 1. கருவி சங்கிலி முறை

ஒவ்வொரு கருவியின் வெளியீடு அடுத்த கருவியின் உள்ளீடாக மாறும் வரிசையில் பல கருவிகளை இணைக்கவும்:

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

### 2. அனுப்புநர் முறை

உள்ளீட்டின் அடிப்படையில் சிறப்பு கருவிகளுக்கு அனுப்பும் மைய கருவியைப் பயன்படுத்தவும்:

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

### 3. இணை செயலாக்க முறை

திறமையை மேம்படுத்த பல கருவிகளை ஒரே நேரத்தில் செயல்படுத்தவும்:

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

### 4. பிழை மீட்பு முறை

கருவி தோல்விகளுக்கு நன்றாக மாற்றங்களை செயல்படுத்தவும்:

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

### 5. வேலைப்பாடு அமைப்பு முறை

எளிய வேலைப்பாடுகளை இணைத்து சிக்கலான வேலைப்பாடுகளை உருவாக்கவும்:

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

# MCP சர்வர்களை சோதனை செய்வது: சிறந்த நடைமுறைகள் மற்றும் முக்கிய குறிப்புகள்

## கண்ணோட்டம்

சோதனை என்பது MCP சர்வர்களை நம்பகமான, உயர் தரமானதாக உருவாக்குவதற்கான முக்கிய அம்சமாகும். இந்த வழிகாட்டி உங்கள் MCP சர்வர்களை மேம்பாட்டு வாழ்க்கைச் சுழற்சியின் முழு நீளத்திலும், யூனிட் சோதனைகளிலிருந்து ஒருங்கிணைப்பு சோதனைகள் மற்றும் முடிவு முதல் இறுதி வரை சரிபார்ப்பு வரை சோதனை செய்ய சிறந்த நடைமுறைகள் மற்றும் குறிப்புகளை வழங்குகிறது.

## MCP சர்வர்களுக்கான சோதனை ஏன் முக்கியம்

MCP சர்வர்கள் AI மாதிரிகள் மற்றும் வாடிக்கையாளர் பயன்பாடுகளுக்கு இடையேயான முக்கிய இடைமுகமாக செயல்படுகின்றன. முழுமையான சோதனை உறுதிப்படுத்துகிறது:

- உற்பத்தி சூழல்களில் நம்பகத்தன்மை
- கோரிக்கைகள் மற்றும் பதில்களை சரியாக கையாளுதல்
- MCP விவரக்குறிப்புகளின் சரியான செயல்பாடு
- தோல்விகள் மற்றும் விளிம்பு வழக்குகளுக்கு எதிரான பொறுமை
- பல்வேறு சுமைகளின் கீழ் நிலையான செயல்திறன்

## MCP சர்வர்களுக்கான யூனிட் சோதனை

### யூனிட் சோதனை (அடித்தளம்)

யூனிட் சோதனைகள் உங்கள் MCP சர்வரின் தனித்துவமான கூறுகளை தனித்துவமாகச் சரிபார்க்கின்றன.

#### என்ன சோதிக்க வேண்டும்

1. **வளக் கையாளர்கள்**: ஒவ்வொரு வளக் கையாளரின் தர்க்கத்தை தனித்துவமாகச் சோதிக்கவும்
2. **கருவி செயல்பாடுகள்**: பல உள்ளீடுகளுடன் கருவி நடத்தை சரிபார்க்கவும்
3. **உந்துதல் வார்ப்புருக்கள்**: உந்துதல் வார்ப்புருக்கள் சரியாக உருவாக்கப்படுவதை உறுதிப்படுத்தவும்
4. **ஸ்கீமா சரிபார்ப்பு**: அளவுரு சரிபார்ப்பு தர்க்கத்தைச் சோதிக்க
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

## MCP விவரக்குறிப்பு உடன் இணக்கமானதா என்பதை சோதனை செய்வது

உங்கள் சர்வர் MCP விவரக்குறிப்பை சரியாக செயல்படுத்துகிறதா என்பதை உறுதிப்படுத்தவும்.

### முக்கிய இணக்கமான பகுதிகள்

1. **API முடுக்கங்கள்**: தேவையான முடுக்கங்களை (/resources, /tools, etc.) சோதனை செய்யவும்
2. **கோரிக்கை/பதில் வடிவம்**: Schema இணக்கத்தைக் கண்டறியவும்
3. **பிழை குறியீடுகள்**: பல சூழல்களுக்கு சரியான நிலை குறியீடுகளை உறுதிப்படுத்தவும்
4. **உள்ளடக்க வகைகள்**: பல உள்ளடக்க வகைகளை கையாள்வதை சோதனை செய்யவும்
5. **அங்கீகார ஓட்டம்**: விவரக்குறிப்புடன் இணக்கமான அங்கீகார முறைகளை உறுதிப்படுத்தவும்

### இணக்கமான சோதனை தொகுப்பு

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

## MCP சர்வர் சோதனைக்கு 10 சிறந்த குறிப்புகள்

1. **கருவி வரையறைகளை தனியாக சோதனை செய்யவும்**: Schema வரையறைகளை கருவி தார்மீகத்திலிருந்து தனியாக உறுதிப்படுத்தவும்
2. **அளவுரு சோதனைகளைப் பயன்படுத்தவும்**: பல உள்ளீடுகளுடன், குறிப்பாக விளிம்பு வழக்குகளுடன் கருவிகளை சோதனை செய்யவும்
3. **பிழை பதில்களைச் சோதிக்கவும்**: அனைத்து சாத்தியமான பிழை நிலைகளுக்கு சரியான பிழை கையாளுதலை உறுதிப்படுத்தவும்
4. **அங்கீகார தார்மீகத்தைச் சோதிக்கவும்**: பல பயனர் பங்குகளுக்கு சரியான அணுகல் கட்டுப்பாட்டை உறுதிப்படுத்தவும்
5. **சோதனை கவரேஜை கண்காணிக்கவும்**: முக்கிய பாதை குறியீட்டின் அதிக கவரேஜை நோக்கமாகக் கொள்ளவும்
6. **ஸ்ட்ரீமிங் பதில்களைச் சோதிக்கவும்**: ஸ்ட்ரீமிங் உள்ளடக்கத்தை சரியாக கையாள்வதை உறுதிப்படுத்தவும்
7. **நெட்வொர்க் பிரச்சினைகளை ஒத்திகை செய்யவும்**: மோசமான நெட்வொர்க் நிலைகளின் கீழ் நடத்தை சோதனை செய்யவும்
8. **வள வரம்புகளைச் சோதிக்கவும்**: கோட்டாக்கள் அல்லது வீத வரம்புகளை அடையும் போது நடத்தை உறுதிப்படுத்தவும்
9. **மீள்நிலை சோதனைகளை தானியக்கமாக்கவும்**: ஒவ்வொரு குறியீட்டு மாற்றத்திலும் இயங்கும் தொகுப்பை உருவாக்கவும்
10. **சோதனை வழக்குகளை ஆவணப்படுத்தவும்**: சோதனை சூழல்களின் தெளிவான ஆவணங்களை பராமரிக்கவும்

## பொதுவான சோதனை தவறுகள்

- **சந்தோஷமான பாதை சோதனையில் அதிக நம்பிக்கை**: பிழை வழக்குகளை முழுமையாக சோதனை செய்யவும்
- **செயல்திறன் சோதனையை புறக்கணித்தல்**: உற்பத்திக்கு பாதிப்பை ஏற்படுத்தும் முன் bottlenecks ஐ கண்டறியவும்
- **தனிமையில் மட்டும் சோதனை செய்யுதல்**: Unit, Integration, மற்றும் E2E சோதனைகளை இணைக்கவும்
- **முழுமையான API கவரேஜ் இல்லாமல்**: அனைத்து முடுக்கங்கள் மற்றும் அம்சங்கள் சோதனை செய்யப்படுவதை உறுதிப்படுத்தவும்
- **மாறுபட்ட சோதனை சூழல்கள்**: Containers ஐப் பயன்படுத்தி சோதனை சூழல்களின் நிலைத்தன்மையை உறுதிப்படுத்தவும்

## முடிவு

ஒரு விரிவான சோதனை உத்தி MCP சர்வர்களை நம்பகமான, உயர் தரமானதாக உருவாக்குவதற்கு அவசியமானது. இந்த வழிகாட்டியில் குறிப்பிடப்பட்ட சிறந்த நடைமுறைகள் மற்றும் குறிப்புகளை செயல்படுத்துவதன் மூலம், உங்கள் MCP செயல்பாடுகள் தரம், நம்பகத்தன்மை மற்றும் செயல்திறனின் மிக உயர்ந்த தரங்களை பூர்த்தி செய்யும் என்பதை உறுதிப்படுத்தலாம்.

## முக்கிய எடுத்துக்காட்டுகள்

1. **கருவி வடிவமைப்பு**: Single Responsibility Principle ஐ பின்பற்றவும், Dependency Injection ஐப் பயன்படுத்தவும், மற்றும் Composability க்காக வடிவமைக்கவும்
2. **Schema வடிவமைப்பு**: தெளிவான, நன்கு ஆவணப்படுத்தப்பட்ட schemas ஐ உருவாக்கவும், சரியான validation கட்டுப்பாடுகளுடன்
3. **பிழை கையாளுதல்**: மெல்லிய பிழை கையாளுதல், அமைந்த பிழை பதில்கள், மற்றும் மீண்டும் முயற்சி செய்யும் தார்மீகத்தை செயல்படுத்தவும்
4. **செயல்திறன்**: Caching, Asynchronous Processing, மற்றும் Resource Throttling ஐப் பயன்படுத்தவும்
5. **பாதுகாப்பு**: முழுமையான உள்ளீட்டு சரிபார்ப்பு, அங்கீகார சோதனைகள், மற்றும் நுண்ணறிவு தரவுகளை கையாளுதல்
6. **சோதனை**: விரிவான Unit, Integration, மற்றும் End-to-End சோதனைகளை உருவாக்கவும்
7. **Workflow Patterns**: Chains, Dispatchers, மற்றும் Parallel Processing போன்ற நிலைநிறுத்தப்பட்ட முறைமைகளைப் பயன்படுத்தவும்

## பயிற்சி

ஒரு MCP கருவி மற்றும் workflow ஐ ஒரு ஆவண செயலாக்க அமைப்பிற்காக வடிவமைக்கவும்:

1. பல வடிவங்களில் (PDF, DOCX, TXT) ஆவணங்களை ஏற்கிறது
2. ஆவணங்களில் இருந்து உரை மற்றும் முக்கிய தகவல்களை எடுக்கிறது
3. ஆவணங்களை வகை மற்றும் உள்ளடக்கத்தின் அடிப்படையில் வகைப்படுத்துகிறது
4. ஒவ்வொரு ஆவணத்திற்கும் சுருக்கத்தை உருவாக்குகிறது

இந்த சூழலுக்கு மிகவும் பொருத்தமான கருவி schemas, பிழை கையாளுதல், மற்றும் workflow முறைமையை செயல்படுத்தவும். இந்த செயல்பாட்டை நீங்கள் எப்படி சோதனை செய்வீர்கள் என்பதை பரிசீலிக்கவும்.

## வளங்கள்

1. [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) இல் MCP சமூகத்தில் சேர்ந்து சமீபத்திய முன்னேற்றங்களைப் பெறுங்கள்
2. [MCP projects](https://github.com/modelcontextprotocol) இல் திறந்த மூலமாக பங்களிக்கவும்
3. உங்கள் நிறுவனத்தின் AI முயற்சிகளில் MCP கொள்கைகளைப் பயன்படுத்தவும்
4. உங்கள் தொழில்துறைக்கு சிறப்பு MCP செயல்பாடுகளை ஆராயவும்
5. பல்துறை ஒருங்கிணைப்பு அல்லது நிறுவன பயன்பாட்டு ஒருங்கிணைப்பு போன்ற MCP குறிப்புகளில் மேம்பட்ட பாடங்களை எடுத்துக்கொள்ள பரிசீலிக்கவும்
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) மூலம் கற்றுக்கொண்ட கொள்கைகளைப் பயன்படுத்தி உங்கள் சொந்த MCP கருவிகள் மற்றும் workflows ஐ உருவாக்க முயற்சிக்கவும்

Next: Best Practices [case studies](../09-CaseStudy/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
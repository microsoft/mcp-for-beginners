# MCP विकास सर्वोत्तम पद्धती

[![MCP विकास सर्वोत्तम पद्धती](../../../translated_images/mr/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(वरील प्रतिमेवर क्लिक करून या धड्याचा व्हिडिओ पहा)_

## आढावा

हा धडा उत्पादन वातावरणात MCP सर्व्हर आणि वैशिष्ट्ये विकसित करणे, चाचणी करणे आणि तैनात करण्यासाठी प्रगत सर्वोत्तम पद्धतींवर केंद्रित आहे. MCP परिसंस्था जसे अधिक गुंतागुंतीच्या आणि महत्त्वाच्या होत जातात, तसे प्रस्थापित नमुन्यांचे पालन करणे विश्वसनीयता, देखभालक्षमता आणि परस्परसंवाद सुनिश्चित करते. हा धडा MCP अंमलबजावणीच्या वास्तव-जगातील अनुभवांमधून मिळालेल्या व्यावहारिक ज्ञानाचे संकलन करतो, जेणेकरून तुम्ही मजबूत, कार्यक्षम सर्व्हर तयार करू शकाल.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकाल:

- MCP सर्व्हर आणि वैशिष्ट्य डिझाइनमध्ये उद्योगातील सर्वोत्तम पद्धती लागू करा
- MCP सर्व्हरसाठी सर्वसमावेशक चाचणी धोरणे तयार करा
- जटिल MCP अनुप्रयोगांसाठी कार्यक्षम, पुनर्वापरयोग्य कार्यप्रवाह नमुने डिझाइन करा
- MCP सर्व्हरमध्ये योग्य त्रुटी हाताळणी, लॉगिंग आणि निरीक्षण अंमलात आणा
- कार्यक्षमता, सुरक्षा आणि देखभालक्षमतेसाठी MCP अंमलबजावणी ऑप्टिमाइझ करा

## MCP मुख्य तत्त्वे

विशिष्ट अंमलबजावणी पद्धतींमध्ये जाण्यापूर्वी, प्रभावी MCP विकास मार्गदर्शन करणारी मुख्य तत्त्वे समजून घेणे महत्त्वाचे आहे:

1. **प्रमाणित संवाद**: MCP JSON-RPC 2.0 चा पाया म्हणून वापरतो, सर्व अंमलबजावणींमध्ये विनंत्या, प्रतिसाद आणि त्रुटी हाताळणीसाठी सुसंगत स्वरूप प्रदान करतो.

2. **वापरकर्ता-केंद्रित डिझाइन**: नेहमीच MCP अंमलबजावणीमध्ये वापरकर्त्याची संमती, नियंत्रण आणि पारदर्शकतेला प्राधान्य द्या.

3. **सुरक्षा प्रथम**: प्रमाणीकरण, अधिकृतता, सत्यापन आणि दर मर्यादेसह मजबूत सुरक्षा उपाय अंमलात आणा.

4. **मॉड्यूलर आर्किटेक्चर**: MCP सर्व्हर मॉड्यूलर दृष्टिकोनाने डिझाइन करा, जिथे प्रत्येक साधन आणि संसाधनाचे स्पष्ट, केंद्रित उद्दिष्ट असते.

5. **स्थितीपूर्ण कनेक्शन**: अधिक सुसंगत आणि संदर्भ-जागरूक संवादांसाठी अनेक विनंत्यांमध्ये स्थिती राखण्याची MCP ची क्षमता वापरा.

## अधिकृत MCP सर्वोत्तम पद्धती

खालील सर्वोत्तम पद्धती अधिकृत मॉडेल संदर्भ प्रोटोकॉल दस्तऐवजांमधून घेतल्या आहेत:

### सुरक्षा सर्वोत्तम पद्धती

1. **वापरकर्ता संमती आणि नियंत्रण**: डेटा प्रवेश करण्यापूर्वी किंवा ऑपरेशन्स करण्यापूर्वी नेहमी स्पष्ट वापरकर्ता संमती आवश्यक आहे. कोणता डेटा सामायिक केला जातो आणि कोणती क्रिया अधिकृत आहे यावर स्पष्ट नियंत्रण प्रदान करा.

2. **डेटा गोपनीयता**: केवळ स्पष्ट संमतीने वापरकर्ता डेटा उघड करा आणि त्याचे योग्य प्रवेश नियंत्रणांसह संरक्षण करा. अनधिकृत डेटा प्रसारण टाळा.

3. **साधन सुरक्षा**: कोणतेही साधन सक्रिय करण्यापूर्वी स्पष्ट वापरकर्ता संमती आवश्यक आहे. प्रत्येक साधनाची कार्यक्षमता वापरकर्त्यांना समजेल याची खात्री करा आणि मजबूत सुरक्षा सीमा लागू करा.

4. **साधन परवानगी नियंत्रण**: सत्रादरम्यान कोणती साधने मॉडेल वापरू शकतात ते कॉन्फिगर करा, जेणेकरून केवळ स्पष्टपणे अधिकृत साधनेच प्रवेशयोग्य असतील.

5. **प्रमाणीकरण**: API की, OAuth टोकन किंवा इतर सुरक्षित प्रमाणीकरण पद्धती वापरून साधने, संसाधने किंवा संवेदनशील ऑपरेशन्समध्ये प्रवेश देण्यापूर्वी योग्य प्रमाणीकरण आवश्यक आहे.

6. **पॅरामीटर सत्यापन**: चुकीच्या किंवा दुर्भावनायुक्त इनपुटला साधन अंमलबजावणीपर्यंत पोहोचण्यापासून रोखण्यासाठी सर्व साधन सक्रियतेसाठी सत्यापन लागू करा.

7. **दर मर्यादित करणे**: गैरवापर टाळण्यासाठी आणि सर्व्हर संसाधनांचा न्याय्य वापर सुनिश्चित करण्यासाठी दर मर्यादित करणे अंमलात आणा.

### अंमलबजावणी सर्वोत्तम पद्धती

1. **क्षमता वाटाघाटी**: कनेक्शन सेटअप दरम्यान, समर्थित वैशिष्ट्ये, प्रोटोकॉल आवृत्त्या, उपलब्ध साधने आणि संसाधने याबद्दल माहिती देवाणघेवाण करा.

2. **साधन डिझाइन**: एकाच वेळी अनेक जबाबदाऱ्या हाताळणाऱ्या साधनांऐवजी, एकाच कार्यात उत्कृष्ट काम करणारी केंद्रित साधने तयार करा.

3. **त्रुटी हाताळणी**: समस्या निदान करण्यासाठी, अपयशांचा सौम्यपणे सामना करण्यासाठी आणि कृतीयोग्य अभिप्राय प्रदान करण्यासाठी प्रमाणित त्रुटी संदेश आणि कोड अंमलात आणा.

4. **लॉगिंग**: प्रोटोकॉल संवादांचे ऑडिटिंग, डीबगिंग आणि निरीक्षण करण्यासाठी संरचित लॉग्स कॉन्फिगर करा.

5. **प्रगती ट्रॅकिंग**: दीर्घकालीन ऑपरेशन्ससाठी, प्रतिसादक्षम वापरकर्ता इंटरफेस सक्षम करण्यासाठी प्रगती अद्यतने नोंदवा.

6. **विनंती रद्द करणे**: क्लायंटला गरज नसलेल्या किंवा खूप वेळ घेणाऱ्या विनंत्या रद्द करण्याची परवानगी द्या.

## अतिरिक्त संदर्भ

MCP सर्वोत्तम पद्धतींबद्दल सर्वात अद्ययावत माहितीसाठी, खालील गोष्टी पहा:

- [MCP दस्तऐवज](https://modelcontextprotocol.io/)
- [MCP तपशील](https://spec.modelcontextprotocol.io/)
- [GitHub रिपॉझिटरी](https://github.com/modelcontextprotocol)
- [सुरक्षा सर्वोत्तम पद्धती](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## व्यावहारिक अंमलबजावणी उदाहरणे

### साधन डिझाइन सर्वोत्तम पद्धती

#### 1. सिंगल रिस्पॉन्सिबिलिटी प्रिन्सिपल

प्रत्येक MCP साधनाचे स्पष्ट, केंद्रित उद्दिष्ट असावे. अनेक जबाबदाऱ्या हाताळण्याचा प्रयत्न करणारी साधने तयार करण्याऐवजी, विशिष्ट कार्यांमध्ये उत्कृष्ट काम करणारी तज्ज्ञ साधने विकसित करा.

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

#### 2. सुसंगत त्रुटी हाताळणी

माहितीपूर्ण त्रुटी संदेश आणि योग्य पुनर्प्राप्ती यंत्रणांसह मजबूत त्रुटी हाताळणी अंमलात आणा.

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

#### 3. पॅरामीटर सत्यापन

चुकीच्या किंवा दुर्भावनायुक्त इनपुटला टाळण्यासाठी नेहमीच पॅरामीटरची काटेकोरपणे पडताळणी करा.

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

### सुरक्षा अंमलबजावणी उदाहरणे

#### 1. प्रमाणीकरण आणि अधिकृतता

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

#### 2. दर मर्यादित करणे

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

## चाचणी सर्वोत्तम पद्धती

### 1. MCP साधनांची युनिट चाचणी

नेहमीच साधनांची स्वतंत्र चाचणी करा, बाह्य अवलंबित्वांचे मॉकिंग करा:

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

### 2. एकत्रीकरण चाचणी

क्लायंट विनंत्यांपासून सर्व्हर प्रतिसादांपर्यंत संपूर्ण प्रवाहाची चाचणी करा:

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

## कार्यक्षमता ऑप्टिमायझेशन

### 1. कॅशिंग धोरणे

प्रतीक्षा वेळ कमी करण्यासाठी आणि संसाधनांचा वापर कमी करण्यासाठी योग्य कॅशिंग अंमलात आणा:

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

#### 2. अवलंबित्व इंजेक्शन आणि चाचणीक्षमता

साधनांना त्यांच्या अवलंबित्वांचे कन्स्ट्रक्टर इंजेक्शनद्वारे प्राप्त होण्यासाठी डिझाइन करा, ज्यामुळे ती चाचणीयोग्य आणि कॉन्फिगर करण्यायोग्य बनतील:

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

#### 3. संयोज्य साधने

अधिक जटिल कार्यप्रवाह तयार करण्यासाठी एकत्रितपणे कार्य करणारी साधने डिझाइन करा:

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

### स्कीमा डिझाइन सर्वोत्तम पद्धती

स्कीमा हे मॉडेल आणि तुमच्या साधनादरम्यानचे करार आहे. चांगल्या प्रकारे डिझाइन केलेल्या स्कीमांमुळे साधनांचा वापर सुलभ होतो.

#### 1. स्पष्ट पॅरामीटर वर्णने

प्रत्येक पॅरामीटरसाठी वर्णनात्मक माहिती नेहमीच समाविष्ट करा:

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

#### 2. सत्यापन मर्यादा

अवैध इनपुट टाळण्यासाठी सत्यापन मर्यादा समाविष्ट करा:

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

#### 3. सुसंगत परतावा संरचना

तुमच्या प्रतिसाद संरचनांमध्ये सुसंगतता राखा, ज्यामुळे मॉडेल्सना परिणाम समजणे सोपे होईल:

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

### त्रुटी हाताळणी

MCP साधनांच्या विश्वसनीयतेसाठी मजबूत त्रुटी हाताळणी महत्त्वाची आहे.

#### 1. सौम्य त्रुटी हाताळणी

योग्य स्तरांवर त्रुटी हाताळा आणि माहितीपूर्ण संदेश प्रदान करा:

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

#### 2. संरचित त्रुटी प्रतिसाद

शक्य असल्यास संरचित त्रुटी माहिती परत करा:

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

#### 3. पुनःप्रयत्न युक्तिवाद

तात्पुरत्या अपयशांसाठी योग्य पुनःप्रयत्न युक्तिवाद अंमलात आणा:

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

### कार्यक्षमता ऑप्टिमायझेशन

#### 1. कॅशिंग

महागड्या ऑपरेशन्ससाठी कॅशिंग अंमलात आणा:

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

#### 2. असिंक्रोनस प्रक्रिया

I/O-बाउंड ऑपरेशन्ससाठी असिंक्रोनस प्रोग्रामिंग नमुने वापरा:

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

#### 3. संसाधन थ्रॉटलिंग

ओव्हरलोड टाळण्यासाठी संसाधन थ्रॉटलिंग अंमलात आणा:

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

### सुरक्षा सर्वोत्तम पद्धती

#### 1. इनपुट सत्यापन

नेहमीच इनपुट पॅरामीटरची काटेकोरपणे पडताळणी करा:

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

#### 2. अधिकृतता तपासणी

योग्य अधिकृतता तपासणी अंमलात आणा:

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

#### 3. संवेदनशील डेटा हाताळणी

संवेदनशील डेटाचे काळजीपूर्वक हाताळणी करा:

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

## MCP साधनांसाठी चाचणी सर्वोत्तम पद्धती

संपूर्ण चाचणी MCP साधने योग्यरित्या कार्य करतात, काठाच्या प्रकरणांचा सामना करतात आणि सिस्टमच्या उर्वरित भागाशी योग्यरित्या समाकलित होतात याची खात्री करते.

### युनिट चाचणी

#### 1. प्रत्येक साधन स्वतंत्रपणे चाचणी करा

प्रत्येक साधनाच्या कार्यक्षमतेसाठी केंद्रित चाचण्या तयार करा:

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

#### 2. स्कीमा सत्यापन चाचणी

स्कीमा वैध आहेत आणि योग्यरित्या मर्यादा लागू करतात याची चाचणी करा:

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

#### 3. त्रुटी हाताळणी चाचण्या

त्रुटी परिस्थितीसाठी विशिष्ट चाचण्या तयार करा:

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

### एकत्रीकरण चाचणी

#### 1. साधन साखळी चाचणी

अपेक्षित संयोजनांमध्ये एकत्र काम करणाऱ्या साधनांची चाचणी करा:

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

#### 2. MCP सर्व्हर चाचणी

पूर्ण साधन नोंदणी आणि अंमलबजावणीसह MCP सर्व्हरची चाचणी करा:

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

#### 3. एंड-टू-एंड चाचणी

मॉडेल प्रॉम्प्टपासून साधन अंमलबजावणीपर्यंत संपूर्ण कार्यप्रवाहांची चाचणी करा:

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

### कार्यक्षमता चाचणी

#### 1. लोड चाचणी

तुमचा MCP सर्व्हर किती समांतर विनंत्या हाताळू शकतो याची चाचणी करा:

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

#### 2. ताण चाचणी

अत्यंत लोडखाली सिस्टमची चाचणी करा:

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

#### 3. निरीक्षण आणि प्रोफाइलिंग

दीर्घकालीन कार्यक्षमता विश्लेषणासाठी निरीक्षण सेट करा:

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

## MCP कार्यप्रवाह डिझाइन नमुने

चांगल्या प्रकारे डिझाइन केलेले MCP कार्यप्रवाह कार्यक्षमता, विश्वसनीयता आणि देखभालक्षमता सुधारतात. खालील महत्त्वाचे नमुने अनुसरण करा:

### 1. साधन साखळी नमुना

प्रत्येक साधनाचे आउटपुट पुढील साधनासाठी इनपुट म्हणून वापरून अनेक साधने जोडणे:

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

### 2. डिस्पॅचर नमुना

इनपुटच्या आधारे विशेष साधनांकडे पाठवणारे केंद्रीय साधन वापरा:

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

### 3. समांतर प्रक्रिया नमुना

कार्यक्षमतेसाठी अनेक साधने एकाच वेळी चालवा:

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

### 4. त्रुटी पुनर्प्राप्ती नमुना

साधन अपयशांसाठी सौम्य फॉलबॅक अंमलात आणा:

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

### 5. कार्यप्रवाह रचना नमुना

सोप्या कार्यप्रवाहांचे संयोजन करून जटिल कार्यप्रवाह तयार करा:

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

# MCP सर्व्हर चाचणी: सर्वोत्तम पद्धती आणि शीर्ष टिपा

## आढावा

चाचणी हा MCP सर्व्हर विकसित करण्याचा एक महत्त्वाचा भाग आहे. युनिट चाचण्यांपासून एकत्रीकरण चाचण्यांपर्यंत आणि एंड-टू-एंड पडताळणीपर्यंत, विकास जीवनचक्रात MCP सर्व्हरची चाचणी घेण्यासाठी या मार्गदर्शकामध्ये सर्वसमावेशक सर्वोत्तम पद्धती आणि टिपा दिल्या आहेत.

## MCP सर्व्हरसाठी चाचणी का महत्त्वाची आहे

MCP सर्व्हर हे AI मॉडेल्स आणि क्लायंट अनुप्रयोगांमधील महत्त्वाचे मध्यस्थ म्हणून काम करतात. सखोल चाचणी सुनिश्चित करते:

- उत्पादन वातावरणातील विश्वसनीयता
- विनंत्या आणि प्रतिसादांचे अचूक हाताळणी
- MCP तपशीलांचे योग्य अंमलबजावणी
- अपयश आणि काठाच्या प्रकरणांपासून लवचिकता
- विविध लोड्सखाली सुसंगत कार्यक्षमता

## MCP सर्व्हरसाठी युनिट चाचणी

### युनिट चाचणी (पायाभूत)

युनिट चाचण्या MCP सर्व्हरच्या वैयक्तिक घटकांची स्वतंत्रपणे पडताळणी करतात.

#### काय चाचणी करावी

1. **संसाधन हँडलर्स**: प्रत्येक संसाधन हँडलरचे लॉजिक स्वतंत्रपणे चाचणी करा
2. **साधन अंमलबजावणी**: विविध इनपुटसह साधनांचे वर्तन पडताळा
3. **प्रॉम्प्ट टेम्पलेट्स**: प्रॉम्प्ट टेम्पलेट्स योग्यरित्या रेंडर होतात याची खात्री करा
4. **स्कीमा सत्यापन**: पॅरामीटर सत्यापन लॉजिक चाचणी करा
5. **त्रुटी हाताळणी**: अवैध इनपुटसाठी त्रुटी प्रतिसाद पडताळा

#### युनिट चाचणीसाठी सर्वोत्तम पद्धती

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

### एकत्रीकरण चाचणी (मध्य स्तर)

एकत्रीकरण चाचण्या MCP सर्व्हरच्या घटकांमधील परस्परसंवाद पडताळतात.

#### काय चाचणी करावी

1. **सर्व्हर प्रारंभ**: विविध कॉन्फिगरेशनसह सर्व्हर स्टार्टअप चाचणी करा
2. **मार्ग नोंदणी**: सर्व एंडपॉइंट्स योग्यरित्या नोंदणीकृत आहेत याची पडताळणी करा
3. **विनंती प्रक्रिया**: संपूर्ण विनंती-प्रतिसाद चक्र चाचणी करा
4. **त्रुटी प्रसार**: घटकांमध्ये त्रुटी योग्यरित
3. **कामगिरीची मूलभूत पातळी**: कामगिरीची मानके राखा जेणेकरून मागे जाण्याचे प्रकार ओळखता येतील  
4. **सुरक्षा स्कॅन**: पाइपलाइनचा भाग म्हणून सुरक्षा चाचणी स्वयंचलित करा  

### उदाहरण CI पाइपलाइन (GitHub Actions)

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

## MCP स्पेसिफिकेशनशी अनुपालनासाठी चाचणी  

तुमचा सर्व्हर MCP स्पेसिफिकेशन योग्य प्रकारे अंमलात आणतो का ते सत्यापित करा.  

### मुख्य अनुपालन क्षेत्रे  

1. **API एंडपॉइंट्स**: आवश्यक एंडपॉइंट्सची चाचणी करा (/resources, /tools, इत्यादी)  
2. **रिक्वेस्ट/रेस्पॉन्स फॉर्मॅट**: स्कीमा अनुपालन सत्यापित करा  
3. **एरर कोड्स**: विविध परिस्थितींसाठी योग्य स्टेटस कोड्स सत्यापित करा  
4. **कंटेंट टाइप्स**: विविध कंटेंट टाइप्स हाताळण्याची चाचणी करा  
5. **ऑथेंटिकेशन फ्लो**: स्पेसिफिकेशन-अनुपालन ऑथ मेकॅनिझम सत्यापित करा  

### अनुपालन चाचणी संच  

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

## प्रभावी MCP सर्व्हर चाचणीसाठी टॉप 10 टिप्स  

1. **टूल डिफिनिशन्स स्वतंत्रपणे चाचणी करा**: स्कीमा डिफिनिशन्स टूल लॉजिकपासून स्वतंत्रपणे सत्यापित करा  
2. **पॅरामीटराइज्ड चाचण्या वापरा**: विविध इनपुट्ससह टूल्सची चाचणी करा, ज्यामध्ये एज केससुद्धा समाविष्ट आहेत  
3. **एरर रिस्पॉन्सेस तपासा**: सर्व संभाव्य एरर परिस्थितींसाठी योग्य एरर हाताळणी सत्यापित करा  
4. **ऑथरायझेशन लॉजिक चाचणी करा**: विविध युजर रोल्ससाठी योग्य ऍक्सेस कंट्रोल सुनिश्चित करा  
5. **चाचणी कव्हरेज मॉनिटर करा**: महत्त्वाच्या कोड पथासाठी उच्च कव्हरेज साध्य करा  
6. **स्ट्रीमिंग रिस्पॉन्सेस चाचणी करा**: स्ट्रीमिंग कंटेंट योग्य प्रकारे हाताळण्याची सत्यापित करा  
7. **नेटवर्क समस्यांचे अनुकरण करा**: खराब नेटवर्क परिस्थितीत वर्तनाची चाचणी करा  
8. **रिसोर्स लिमिट्स चाचणी करा**: कोटा किंवा रेट लिमिट्स गाठल्यावर वर्तन सत्यापित करा  
9. **रिग्रेशन चाचण्या स्वयंचलित करा**: प्रत्येक कोड बदलावर चालणारा संच तयार करा  
10. **चाचणी प्रकरणे दस्तऐवजीकरण करा**: चाचणी परिस्थितींचे स्पष्ट दस्तऐवजीकरण राखा  

## सामान्य चाचणी त्रुटी  

- **हॅपी पाथ चाचणीवर जास्त अवलंबित्व**: एरर परिस्थितींची सखोल चाचणी सुनिश्चित करा  
- **कामगिरी चाचणी दुर्लक्षित करणे**: उत्पादनावर परिणाम होण्यापूर्वी अडथळे ओळखा  
- **फक्त वेगळ्या चाचण्या करणे**: युनिट, इंटिग्रेशन, आणि E2E चाचण्या एकत्र करा  
- **अपूर्ण API कव्हरेज**: सर्व एंडपॉइंट्स आणि वैशिष्ट्ये चाचणी सुनिश्चित करा  
- **असंगत चाचणी वातावरणे**: कंटेनर्स वापरून सुसंगत चाचणी वातावरणे सुनिश्चित करा  

## निष्कर्ष  

विश्वसनीय, उच्च-गुणवत्तेचे MCP सर्व्हर विकसित करण्यासाठी व्यापक चाचणी धोरण आवश्यक आहे. या मार्गदर्शकात दिलेल्या सर्वोत्तम पद्धती आणि टिप्स अंमलात आणून, तुम्ही तुमच्या MCP अंमलबजावणीस गुणवत्ता, विश्वसनीयता, आणि कामगिरीच्या उच्चतम मानकांपर्यंत पोहोचवू शकता.  

## मुख्य मुद्दे  

1. **टूल डिझाइन**: सिंगल रिस्पॉन्सिबिलिटी प्रिन्सिपलचे पालन करा, डिपेंडन्सी इंजेक्शन वापरा, आणि कंपोजेबिलिटीसाठी डिझाइन करा  
2. **स्कीमा डिझाइन**: स्पष्ट, चांगल्या प्रकारे दस्तऐवजीकृत स्कीमा तयार करा ज्यामध्ये योग्य व्हॅलिडेशन मर्यादा आहेत  
3. **एरर हाताळणी**: ग्रेसफुल एरर हाताळणी, संरचित एरर रिस्पॉन्सेस, आणि रिट्राय लॉजिक अंमलात आणा  
4. **कामगिरी**: कॅशिंग, असिंक्रोनस प्रोसेसिंग, आणि रिसोर्स थ्रॉटलिंग वापरा  
5. **सुरक्षा**: सखोल इनपुट व्हॅलिडेशन, ऑथरायझेशन तपासणी, आणि संवेदनशील डेटा हाताळणी लागू करा  
6. **चाचणी**: व्यापक युनिट, इंटिग्रेशन, आणि एंड-टू-एंड चाचण्या तयार करा  
7. **वर्कफ्लो पॅटर्न्स**: चेन, डिस्पॅचर्स, आणि पॅरलल प्रोसेसिंगसारख्या स्थापित पॅटर्न्स लागू करा  

## व्यायाम  

डॉक्युमेंट प्रोसेसिंग सिस्टीमसाठी MCP टूल आणि वर्कफ्लो डिझाइन करा जे:  

1. अनेक फॉरमॅट्समध्ये (PDF, DOCX, TXT) डॉक्युमेंट्स स्वीकारते  
2. डॉक्युमेंट्समधून टेक्स्ट आणि महत्त्वाची माहिती काढते  
3. डॉक्युमेंट्स प्रकार आणि सामग्रीनुसार वर्गीकृत करते  
4. प्रत्येक डॉक्युमेंटचा सारांश तयार करते  

या परिस्थितीसाठी टूल स्कीमा, एरर हाताळणी, आणि वर्कफ्लो पॅटर्न अंमलात आणा. तुम्ही या अंमलबजावणीची चाचणी कशी कराल याचा विचार करा.  

## संसाधने  

1. [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) वर MCP समुदायामध्ये सामील व्हा आणि नवीनतम घडामोडींबद्दल अद्ययावत रहा  
2. ओपन-सोर्स [MCP प्रोजेक्ट्स](https://github.com/modelcontextprotocol) मध्ये योगदान द्या  
3. तुमच्या स्वतःच्या संस्थेच्या AI उपक्रमांमध्ये MCP तत्त्वे लागू करा  
4. तुमच्या उद्योगासाठी विशेष MCP अंमलबजावणी एक्सप्लोर करा  
5. मल्टी-मोडल इंटिग्रेशन किंवा एंटरप्राइज ऍप्लिकेशन इंटिग्रेशनसारख्या विशिष्ट MCP विषयांवर प्रगत अभ्यासक्रम घेण्याचा विचार करा  
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) मधून शिकलेल्या तत्त्वांचा वापर करून स्वतःचे MCP टूल्स आणि वर्कफ्लो तयार करण्याचा प्रयोग करा  

Next: Best Practices [case studies](../09-CaseStudy/README.md)  

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.
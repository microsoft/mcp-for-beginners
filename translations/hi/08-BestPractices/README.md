# MCP विकास के सर्वोत्तम अभ्यास

[![MCP विकास के सर्वोत्तम अभ्यास](../../../translated_images/hi/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(इस पाठ का वीडियो देखने के लिए ऊपर दी गई छवि पर क्लिक करें)_

## परिचय

यह पाठ MCP सर्वर और फीचर्स को प्रोडक्शन वातावरण में विकसित, परीक्षण और तैनात करने के उन्नत सर्वोत्तम अभ्यासों पर केंद्रित है। जैसे-जैसे MCP इकोसिस्टम जटिल और महत्वपूर्ण होते जाते हैं, स्थापित पैटर्न का पालन करना विश्वसनीयता, रखरखाव और इंटरऑपरेबिलिटी सुनिश्चित करता है। यह पाठ वास्तविक दुनिया के MCP कार्यान्वयन से प्राप्त व्यावहारिक ज्ञान को समेकित करता है ताकि आप मजबूत, कुशल सर्वर बनाने के लिए मार्गदर्शन कर सकें, जिनमें प्रभावी संसाधन, प्रॉम्प्ट और उपकरण हों।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- MCP सर्वर और फीचर डिज़ाइन में उद्योग के सर्वोत्तम अभ्यास लागू करना
- MCP सर्वरों के लिए व्यापक परीक्षण रणनीतियाँ बनाना
- जटिल MCP अनुप्रयोगों के लिए कुशल, पुन: उपयोग योग्य वर्कफ़्लो पैटर्न डिज़ाइन करना
- MCP सर्वरों में उचित त्रुटि प्रबंधन, लॉगिंग और अवलोकन को लागू करना
- प्रदर्शन, सुरक्षा और रखरखाव के लिए MCP कार्यान्वयन को अनुकूलित करना

## MCP के मुख्य सिद्धांत

विशिष्ट कार्यान्वयन अभ्यासों में गहराई से जाने से पहले, उन मुख्य सिद्धांतों को समझना महत्वपूर्ण है जो प्रभावी MCP विकास का मार्गदर्शन करते हैं:

1. **मानकीकृत संचार**: MCP JSON-RPC 2.0 का उपयोग करता है, जो सभी कार्यान्वयनों में अनुरोधों, प्रतिक्रियाओं और त्रुटि प्रबंधन के लिए एक सुसंगत प्रारूप प्रदान करता है।

2. **उपयोगकर्ता-केंद्रित डिज़ाइन**: हमेशा अपने MCP कार्यान्वयनों में उपयोगकर्ता की सहमति, नियंत्रण और पारदर्शिता को प्राथमिकता दें।

3. **सुरक्षा पहले**: मजबूत सुरक्षा उपाय लागू करें, जिनमें प्रमाणीकरण, प्राधिकरण, सत्यापन और दर सीमित करना शामिल है।

4. **मॉड्यूलर आर्किटेक्चर**: अपने MCP सर्वरों को मॉड्यूलर दृष्टिकोण के साथ डिज़ाइन करें, जहाँ प्रत्येक उपकरण और संसाधन का एक स्पष्ट, केंद्रित उद्देश्य हो।

5. **स्टेटफुल कनेक्शन**: कई अनुरोधों में स्थिति बनाए रखने की MCP की क्षमता का लाभ उठाएं ताकि अधिक सुसंगत और संदर्भ-सचेत इंटरैक्शन हो सकें।

## आधिकारिक MCP सर्वोत्तम अभ्यास

निम्नलिखित सर्वोत्तम अभ्यास आधिकारिक मॉडल संदर्भ प्रोटोकॉल दस्तावेज़ से लिए गए हैं:

### सुरक्षा सर्वोत्तम अभ्यास

1. **उपयोगकर्ता की सहमति और नियंत्रण**: डेटा तक पहुँचने या संचालन करने से पहले हमेशा स्पष्ट उपयोगकर्ता सहमति की आवश्यकता होती है। यह सुनिश्चित करें कि उपयोगकर्ता को स्पष्ट नियंत्रण हो कि कौन सा डेटा साझा किया गया है और कौन से कार्य अधिकृत हैं।

2. **डेटा गोपनीयता**: केवल उपयोगकर्ता की स्पष्ट सहमति के साथ डेटा को उजागर करें और इसे उचित एक्सेस नियंत्रण के साथ सुरक्षित रखें। अनधिकृत डेटा ट्रांसमिशन से बचाव करें।

3. **उपकरण सुरक्षा**: किसी भी उपकरण को सक्रिय करने से पहले स्पष्ट उपयोगकर्ता सहमति की आवश्यकता होती है। यह सुनिश्चित करें कि उपयोगकर्ता प्रत्येक उपकरण की कार्यक्षमता को समझें और मजबूत सुरक्षा सीमाएँ लागू करें।

4. **उपकरण अनुमति नियंत्रण**: यह कॉन्फ़िगर करें कि सत्र के दौरान मॉडल को कौन से उपकरण उपयोग करने की अनुमति है, यह सुनिश्चित करते हुए कि केवल स्पष्ट रूप से अधिकृत उपकरण ही सुलभ हैं।

5. **प्रमाणीकरण**: उपकरणों, संसाधनों या संवेदनशील संचालन तक पहुँच प्रदान करने से पहले उचित प्रमाणीकरण की आवश्यकता होती है, जैसे API कुंजी, OAuth टोकन, या अन्य सुरक्षित प्रमाणीकरण विधियाँ।

6. **पैरामीटर सत्यापन**: सभी उपकरण सक्रियणों के लिए सत्यापन लागू करें ताकि खराब स्वरूपित या दुर्भावनापूर्ण इनपुट को उपकरण कार्यान्वयन तक पहुँचने से रोका जा सके।

7. **दर सीमित करना**: दुरुपयोग को रोकने और सर्वर संसाधनों के उचित उपयोग को सुनिश्चित करने के लिए दर सीमित करना लागू करें।

### कार्यान्वयन सर्वोत्तम अभ्यास

1. **क्षमता वार्ता**: कनेक्शन सेटअप के दौरान, समर्थित सुविधाओं, प्रोटोकॉल संस्करणों, उपलब्ध उपकरणों और संसाधनों के बारे में जानकारी का आदान-प्रदान करें।

2. **उपकरण डिज़ाइन**: ऐसे केंद्रित उपकरण बनाएँ जो एक काम को अच्छी तरह से करें, बजाय इसके कि ऐसे उपकरण बनाएँ जो कई चिंताओं को संभालें।

3. **त्रुटि प्रबंधन**: समस्याओं का निदान करने, विफलताओं को सहजता से संभालने और कार्रवाई योग्य प्रतिक्रिया प्रदान करने में मदद के लिए मानकीकृत त्रुटि संदेश और कोड लागू करें।

4. **लॉगिंग**: प्रोटोकॉल इंटरैक्शन का ऑडिटिंग, डिबगिंग और मॉनिटरिंग के लिए संरचित लॉग्स कॉन्फ़िगर करें।

5. **प्रगति ट्रैकिंग**: लंबे समय तक चलने वाले संचालन के लिए, उत्तरदायी उपयोगकर्ता इंटरफेस सक्षम करने के लिए प्रगति अपडेट की रिपोर्ट करें।

6. **अनुरोध रद्द करना**: ग्राहकों को उन अनुरोधों को रद्द करने की अनुमति दें जो अब आवश्यक नहीं हैं या बहुत अधिक समय ले रहे हैं।

## अतिरिक्त संदर्भ

MCP सर्वोत्तम अभ्यासों पर सबसे अद्यतन जानकारी के लिए, निम्नलिखित देखें:

- [MCP दस्तावेज़ीकरण](https://modelcontextprotocol.io/)
- [MCP विनिर्देश](https://spec.modelcontextprotocol.io/)
- [GitHub रिपॉजिटरी](https://github.com/modelcontextprotocol)
- [सुरक्षा सर्वोत्तम अभ्यास](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## व्यावहारिक कार्यान्वयन उदाहरण

### उपकरण डिज़ाइन सर्वोत्तम अभ्यास

#### 1. सिंगल रिस्पॉन्सिबिलिटी प्रिंसिपल

प्रत्येक MCP उपकरण का एक स्पष्ट, केंद्रित उद्देश्य होना चाहिए। ऐसे उपकरण बनाने के बजाय जो कई चिंताओं को संभालने का प्रयास करते हैं, विशिष्ट कार्यों में उत्कृष्टता प्राप्त करने वाले विशेषज्ञ उपकरण विकसित करें।

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

#### 2. सुसंगत त्रुटि प्रबंधन

जानकारीपूर्ण त्रुटि संदेशों और उपयुक्त पुनर्प्राप्ति तंत्र के साथ मजबूत त्रुटि प्रबंधन लागू करें।

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

#### 3. पैरामीटर सत्यापन

हमेशा पैरामीटर को अच्छी तरह से सत्यापित करें ताकि खराब स्वरूपित या दुर्भावनापूर्ण इनपुट को रोका जा सके।

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

### सुरक्षा कार्यान्वयन उदाहरण

#### 1. प्रमाणीकरण और प्राधिकरण

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

#### 2. दर सीमित करना

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

## परीक्षण सर्वोत्तम अभ्यास

### 1. MCP उपकरणों का यूनिट परीक्षण

हमेशा अपने उपकरणों का अलगाव में परीक्षण करें, बाहरी निर्भरताओं को मॉक करें:

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

### 2. एकीकरण परीक्षण

क्लाइंट अनुरोधों से लेकर सर्वर प्रतिक्रियाओं तक की पूरी प्रक्रिया का परीक्षण करें:

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

## प्रदर्शन अनुकूलन

### 1. कैशिंग रणनीतियाँ

प्रतीक्षा समय और संसाधन उपयोग को कम करने के लिए उपयुक्त कैशिंग लागू करें:

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

#### 2. निर्भरता इंजेक्शन और परीक्षण योग्यता

उपकरणों को उनके निर्भरता को कंस्ट्रक्टर इंजेक्शन के माध्यम से प्राप्त करने के लिए डिज़ाइन करें, जिससे वे परीक्षण योग्य और कॉन्फ़िगर करने योग्य बनें:

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

#### 3. संयोज्य उपकरण

ऐसे उपकरण डिज़ाइन करें जिन्हें अधिक जटिल वर्कफ़्लो बनाने के लिए एक साथ जोड़ा जा सके:

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

### स्कीमा डिज़ाइन सर्वोत्तम अभ्यास

स्कीमा मॉडल और आपके उपकरण के बीच अनुबंध है। अच्छी तरह से डिज़ाइन किए गए स्कीमा बेहतर उपकरण उपयोगिता की ओर ले जाते हैं।

#### 1. स्पष्ट पैरामीटर विवरण

प्रत्येक पैरामीटर के लिए वर्णनात्मक जानकारी हमेशा शामिल करें:

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

#### 2. सत्यापन बाधाएँ

अमान्य इनपुट को रोकने के लिए सत्यापन बाधाएँ शामिल करें:

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

#### 3. सुसंगत रिटर्न संरचनाएँ

अपने प्रतिक्रिया संरचनाओं में सुसंगतता बनाए रखें ताकि मॉडल के लिए परिणामों की व्याख्या करना आसान हो:

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

### त्रुटि प्रबंधन

MCP उपकरणों की विश्वसनीयता बनाए रखने के लिए मजबूत त्रुटि प्रबंधन महत्वपूर्ण है।

#### 1. सहज त्रुटि प्रबंधन

उपयुक्त स्तरों पर त्रुटियों को संभालें और जानकारीपूर्ण संदेश प्रदान करें:

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

#### 2. संरचित त्रुटि प्रतिक्रियाएँ

जहाँ संभव हो, संरचित त्रुटि जानकारी लौटाएँ:

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

#### 3. पुनः प्रयास तर्क

क्षणिक विफलताओं के लिए उपयुक्त पुनः प्रयास तर्क लागू करें:

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

### प्रदर्शन अनुकूलन

#### 1. कैशिंग

महंगे संचालन के लिए कैशिंग लागू करें:

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

#### 2. असिंक्रोनस प्रोसेसिंग

I/O-बाउंड संचालन के लिए असिंक्रोनस प्रोग्रामिंग पैटर्न का उपयोग करें:

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

ओवरलोड को रोकने के लिए संसाधन थ्रॉटलिंग लागू करें:

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

### सुरक्षा सर्वोत्तम अभ्यास

#### 1. इनपुट सत्यापन

हमेशा इनपुट पैरामीटर को अच्छी तरह से सत्यापित करें:

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

#### 2. प्राधिकरण जांच

उचित प्राधिकरण जांच लागू करें:

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

#### 3. संवेदनशील डेटा प्रबंधन

संवेदनशील डेटा को सावधानीपूर्वक संभालें:

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

## MCP उपकरणों के लिए परीक्षण सर्वोत्तम अभ्यास

व्यापक परीक्षण यह सुनिश्चित करता है कि MCP उपकरण सही ढंग से कार्य करें, किनारे के मामलों को संभालें, और सिस्टम के बाकी हिस्सों के साथ सही ढंग से एकीकृत हों।

### यूनिट परीक्षण

#### 1. प्रत्येक उपकरण का अलगाव में परीक्षण करें

प्रत्येक उपकरण की कार्यक्षमता के लिए केंद्रित परीक्षण बनाएँ:

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

#### 2. स्कीमा सत्यापन परीक्षण

परीक्षण करें कि स्कीमा मान्य हैं और ठीक से बाधाओं को लागू करते हैं:

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

#### 3. त्रुटि प्रबंधन परीक्षण

त्रुटि स्थितियों के लिए विशिष्ट परीक्षण बनाएँ:

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

### एकीकरण परीक्षण

#### 1. उपकरण श्रृंखला परीक्षण

उपकरणों को अपेक्षित संयोजनों में एक साथ काम करते हुए परीक्षण करें:

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

#### 2. MCP सर्वर परीक्षण

पूर्ण उपकरण पंजीकरण और निष्पादन के साथ MCP सर्वर का परीक्षण करें:

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

#### 3. एंड-टू-एंड परीक्षण

मॉडल प्रॉम्प्ट से उपकरण निष्पादन तक पूर्ण वर्कफ़्लो का परीक्षण करें:

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

### प्रदर्शन परीक्षण

#### 1. लोड परीक्षण

परीक्षण करें कि आपका MCP सर्वर कितने समवर्ती अनुरोधों को संभाल सकता है:

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

#### 2. तनाव परीक्षण

अत्यधिक लोड के तहत सिस्टम का परीक्षण करें:

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

#### 3. निगरानी और प्रोफाइलिंग

दीर्घकालिक प्रदर्शन विश्लेषण के लिए निगरानी सेट करें:

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

## MCP वर्कफ़्लो डिज़ाइन पैटर्न

अच्छी तरह से डिज़ाइन किए गए MCP वर्कफ़्लो दक्षता, विश्वसनीयता और रखरखाव में सुधार करते हैं। पालन करने के लिए प्रमुख पैटर्न यहाँ दिए गए हैं:

### 1. उपकरण श्रृंखला पैटर्न

कई उपकरणों को एक अनुक्रम में जोड़ें, जहाँ प्रत्येक उपकरण का आउटपुट अगले के लिए इनपुट बनता है:

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

### 2. डिस्पैचर पैटर्न

एक केंद्रीय उपकरण का उपयोग करें जो इनपुट के आधार पर विशेषज्ञ उपकरणों को भेजता है:

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

### 3. समानांतर प्रोसेसिंग पैटर्न

दक्षता के लिए कई उपकरणों को एक साथ निष्पादित करें:

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

### 4. त्रुटि पुनर्प्राप्ति पैटर्न

उपकरण विफलताओं के लिए सहज फॉलबैक लागू करें:

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

### 5. वर्कफ़्लो संरचना पैटर्न

सरल वर्कफ़्लो को जोड़कर जटिल वर्कफ़्लो बनाएं:

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

# MCP सर्वरों का परीक्षण: सर्वोत्तम अभ्यास और शीर्ष सुझाव

## परिचय

परीक्षण विश्वसनीय, उच्च-गुणवत्ता वाले MCP सर्वरों को विकसित करने का एक महत्वपूर्ण पहलू है। यह मार्गदर्शिका आपके MCP सर्वरों का विकास चक्र के दौरान, यूनिट परीक्षणों से लेकर एकीकरण परीक्षणों और एंड-टू-एंड सत्यापन तक, परीक्षण करने के लिए व्यापक सर्वोत्तम अभ्यास और सुझाव प्रदान करती है।

## MCP सर्वरों के लिए परीक्षण क्यों महत्वपूर्ण है

MCP सर्वर AI मॉडल और क्लाइंट अनुप्रयोगों के बीच महत्वपूर्ण मिडलवेयर के रूप में कार्य करते हैं। व्यापक परीक्षण सुनिश्चित करता है:

- प्रोडक्शन वातावरण में विश्वसनीयता
- अनुरोधों और प्रतिक्रियाओं का सटीक प्रबंधन
- MCP विनिर्देशों का उचित कार्यान्वयन
- विफलताओं और किनारे के मामलों के खिलाफ लचीलापन
- विभिन्न लोड के तहत सुसंगत प्रदर्शन

## MCP सर्वरों के लिए यूनिट परीक्षण

### यूनिट परीक्षण (आधार)

यूनिट परीक्षण आपके MCP सर्वर के व्यक्तिगत घटकों को अलगाव में सत्यापित करते हैं।

#### क्या परीक्षण करें

1. **संसाधन हैंडलर**: प्रत्येक संसाधन हैंडलर की तर्क को स्वतंत्र रूप से परीक्षण करें
2. **उपकरण कार्यान्वयन**: विभिन्न इनपुट के साथ उपकरण व्यवहार सत्यापित करें
3. **प्रॉम्प्ट टेम्पलेट्स**: सुनिश्चित करें कि प्रॉम्प्ट टेम्पलेट्स सही ढंग से प्रस्तुत होते हैं
4. **स्कीमा सत्यापन**: पैरामीटर सत्यापन तर्क का परीक्षण करें
5. **त्रुटि प्रबंधन**: अमान्य इनपुट के लिए त्रुटि प्रतिक्रियाओं को सत्यापित करें

#### यूनिट परीक्षण के लिए सर्वोत्तम अभ्यास

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

### एकीकरण परीक्षण (मध्य परत)

एकीकरण परीक्षण आपके MCP सर्वर के घटकों के बीच इंटरैक्शन को सत्यापित करते हैं।

#### क्या परीक्षण करें

1. **सर्वर प्रारंभिककरण**: विभिन्न कॉन्फ़िगरेशन के साथ सर्वर स्टार्टअप का परीक्षण करें
2. **रूट पंजीकरण**: सत्यापित करें कि सभी एंडपॉइंट सही ढंग से पंजीकृत हैं
3. **अनुरोध प्रसंस्करण**: पूर्ण अनुरोध-प्रतिक्रिया चक्र का परीक्षण करें
4. **त्रुटि प्रचार**: सुनिश्चित करें कि त्रुटियों को घटकों के बीच सही ढंग से संभाला गया है
5. **प्रमाणीकरण और प्राधिकरण**: सुरक्षा तंत्र का परीक्षण करें

#### एकीकरण परीक्षण के लिए सर्वोत्तम अभ्यास

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

### एंड-टू-एंड परीक्षण (शीर्ष परत)

एंड-टू-एंड परीक्षण क्लाइंट से सर्वर तक पूरे सिस्टम व्यवहार को सत्यापित करते हैं।

#### क्या परीक्षण करें

1. **क्लाइंट-सर्वर संचार**: पूर्ण अनुरोध-प्रतिक्रिया चक्र का परीक्षण करें
2. **वास्तविक क्लाइंट SDKs**: वास्तविक क्लाइंट कार्यान्वयन के साथ परीक्षण करें
3. **लोड के तहत प्रदर्शन**: कई समवर्ती अनुरोधों के साथ व्यवहार सत्यापित करें
4. **त्रुटि पुनर्प्राप्ति**: विफलताओं से सिस्टम पुनर्प्राप्ति का परीक्षण करें
5. **लंबे समय तक चलने वाले संचालन**: स्ट्रीमिंग और लंबे संचालन को संभालने का सत्यापन करें

#### E2E परीक्षण के लिए सर्वोत्तम अभ्यास

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

## MCP परीक्षण के लिए मॉकिंग रणनीतियाँ

मॉकिंग परीक्षण के दौरान घटकों को अलग करने के लिए आवश्यक है।

### मॉक करने के लिए घटक

1. **बाहरी AI मॉडल**: पूर्वानुमानित परीक्षण के लिए मॉडल प्रतिक्रियाओं को मॉक करें
2. **बाहरी सेवाएँ**: API निर्भरताओं (डेटाबेस, तृतीय-पक्ष सेवाएँ) को मॉक करें
3. **प्रमाणीकरण सेवाएँ**: पहचान प्रदाताओं को मॉक करें
4. **संसाधन प्रदाता**: महंगे संसाधन हैंडलर को मॉक करें

### उदाहरण: AI मॉडल प्रतिक्रिया को मॉक करना

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

## प्रदर्शन परीक्षण

प्रोडक्शन MCP सर्वरों के लिए प्रदर्शन परीक्षण महत्वपूर्ण है।

### क्या मापें

1. **प्रतीक्षा समय**: अनुरोधों के लिए प्रतिक्रिया समय
2. **थ्रूपुट**: प्रति सेकंड संभाले गए अनुर
3. **प्रदर्शन मानक**: प्रदर्शन बेंचमार्क बनाए रखें ताकि रिग्रेशन को पकड़ा जा सके  
4. **सुरक्षा स्कैन**: पाइपलाइन का हिस्सा बनाकर सुरक्षा परीक्षण को स्वचालित करें  

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

## MCP स्पेसिफिकेशन के अनुपालन के लिए परीक्षण  

सुनिश्चित करें कि आपका सर्वर MCP स्पेसिफिकेशन को सही तरीके से लागू करता है।  

### प्रमुख अनुपालन क्षेत्र  

1. **API एंडपॉइंट्स**: आवश्यक एंडपॉइंट्स (/resources, /tools, आदि) का परीक्षण करें  
2. **रिक्वेस्ट/रिस्पॉन्स फॉर्मेट**: स्कीमा अनुपालन को सत्यापित करें  
3. **एरर कोड्स**: विभिन्न परिदृश्यों के लिए सही स्टेटस कोड्स की पुष्टि करें  
4. **कंटेंट टाइप्स**: विभिन्न कंटेंट टाइप्स को संभालने का परीक्षण करें  
5. **ऑथेंटिकेशन फ्लो**: स्पेसिफिकेशन-अनुपालन ऑथ मेकैनिज़्म की पुष्टि करें  

### अनुपालन परीक्षण सूट  

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

## प्रभावी MCP सर्वर परीक्षण के लिए शीर्ष 10 सुझाव  

1. **टूल डिफिनिशन का अलग से परीक्षण करें**: टूल लॉजिक से अलग स्कीमा डिफिनिशन को सत्यापित करें  
2. **पैरामीटराइज्ड टेस्ट का उपयोग करें**: टूल्स को विभिन्न इनपुट्स, विशेष रूप से किनारे के मामलों के साथ परीक्षण करें  
3. **एरर रिस्पॉन्स की जांच करें**: सभी संभावित एरर कंडीशन्स के लिए सही एरर हैंडलिंग की पुष्टि करें  
4. **ऑथराइजेशन लॉजिक का परीक्षण करें**: विभिन्न उपयोगकर्ता भूमिकाओं के लिए सही एक्सेस कंट्रोल सुनिश्चित करें  
5. **टेस्ट कवरेज की निगरानी करें**: महत्वपूर्ण कोड पथ का उच्च कवरेज प्राप्त करने का लक्ष्य रखें  
6. **स्ट्रीमिंग रिस्पॉन्स का परीक्षण करें**: स्ट्रीमिंग कंटेंट को सही तरीके से संभालने की पुष्टि करें  
7. **नेटवर्क समस्याओं का अनुकरण करें**: खराब नेटवर्क स्थितियों में व्यवहार का परीक्षण करें  
8. **संसाधन सीमाओं का परीक्षण करें**: कोटा या दर सीमाओं तक पहुंचने पर व्यवहार की पुष्टि करें  
9. **रिग्रेशन टेस्ट को स्वचालित करें**: एक ऐसा सूट बनाएं जो हर कोड परिवर्तन पर चले  
10. **टेस्ट केस का दस्तावेजीकरण करें**: परीक्षण परिदृश्यों का स्पष्ट दस्तावेज बनाए रखें  

## सामान्य परीक्षण गलतियां  

- **सिर्फ हैप्पी पाथ परीक्षण पर निर्भरता**: एरर मामलों का गहराई से परीक्षण करना सुनिश्चित करें  
- **प्रदर्शन परीक्षण की अनदेखी**: उत्पादन को प्रभावित करने से पहले बॉटलनेक्स की पहचान करें  
- **केवल अलगाव में परीक्षण करना**: यूनिट, इंटीग्रेशन, और एंड-टू-एंड परीक्षणों को मिलाएं  
- **अधूरी API कवरेज**: सुनिश्चित करें कि सभी एंडपॉइंट्स और फीचर्स का परीक्षण किया गया है  
- **असंगत परीक्षण वातावरण**: कंटेनरों का उपयोग करें ताकि परीक्षण वातावरण सुसंगत हो  

## निष्कर्ष  

एक व्यापक परीक्षण रणनीति विश्वसनीय, उच्च-गुणवत्ता वाले MCP सर्वर विकसित करने के लिए आवश्यक है। इस गाइड में उल्लिखित सर्वोत्तम प्रथाओं और सुझावों को लागू करके, आप सुनिश्चित कर सकते हैं कि आपके MCP कार्यान्वयन गुणवत्ता, विश्वसनीयता और प्रदर्शन के उच्चतम मानकों को पूरा करते हैं।  

## मुख्य बातें  

1. **टूल डिज़ाइन**: सिंगल रिस्पॉन्सिबिलिटी प्रिंसिपल का पालन करें, डिपेंडेंसी इंजेक्शन का उपयोग करें, और कंपोज़ेबिलिटी के लिए डिज़ाइन करें  
2. **स्कीमा डिज़ाइन**: स्पष्ट, अच्छी तरह से प्रलेखित स्कीमा बनाएं जिनमें उचित सत्यापन बाधाएं हों  
3. **एरर हैंडलिंग**: ग्रेसफुल एरर हैंडलिंग, संरचित एरर रिस्पॉन्स, और रिट्राई लॉजिक लागू करें  
4. **प्रदर्शन**: कैशिंग, असिंक्रोनस प्रोसेसिंग, और संसाधन थ्रॉटलिंग का उपयोग करें  
5. **सुरक्षा**: इनपुट सत्यापन, ऑथराइजेशन चेक्स, और संवेदनशील डेटा हैंडलिंग को लागू करें  
6. **परीक्षण**: व्यापक यूनिट, इंटीग्रेशन, और एंड-टू-एंड परीक्षण बनाएं  
7. **वर्कफ़्लो पैटर्न**: चेन, डिस्पैचर्स, और पैरेलल प्रोसेसिंग जैसे स्थापित पैटर्न लागू करें  

## अभ्यास  

एक दस्तावेज़ प्रसंस्करण प्रणाली के लिए MCP टूल और वर्कफ़्लो डिज़ाइन करें जो:  

1. कई प्रारूपों (PDF, DOCX, TXT) में दस्तावेज़ स्वीकार करता है  
2. दस्तावेज़ों से टेक्स्ट और प्रमुख जानकारी निकालता है  
3. दस्तावेज़ों को प्रकार और सामग्री के अनुसार वर्गीकृत करता है  
4. प्रत्येक दस्तावेज़ का सारांश उत्पन्न करता है  

इस परिदृश्य के लिए टूल स्कीमा, एरर हैंडलिंग, और एक वर्कफ़्लो पैटर्न लागू करें। विचार करें कि आप इस कार्यान्वयन का परीक्षण कैसे करेंगे।  

## संसाधन  

1. नवीनतम विकास पर अपडेट रहने के लिए [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) में MCP समुदाय से जुड़ें  
2. ओपन-सोर्स [MCP प्रोजेक्ट्स](https://github.com/modelcontextprotocol) में योगदान करें  
3. अपनी खुद की संगठनात्मक AI पहलों में MCP सिद्धांतों को लागू करें  
4. अपने उद्योग के लिए विशेष MCP कार्यान्वयन का अन्वेषण करें  
5. विशिष्ट MCP विषयों, जैसे मल्टी-मोडल इंटीग्रेशन या एंटरप्राइज एप्लिकेशन इंटीग्रेशन पर उन्नत पाठ्यक्रम लेने पर विचार करें  
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) के माध्यम से सीखे गए सिद्धांतों का उपयोग करके अपने खुद के MCP टूल और वर्कफ़्लो बनाने के साथ प्रयोग करें  

अगला: सर्वोत्तम प्रथाओं [केस स्टडी](../09-CaseStudy/README.md)  

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
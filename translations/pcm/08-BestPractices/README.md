<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62150e27d4b7b5797ee41146d176e6b",
  "translation_date": "2025-11-18T20:04:49+00:00",
  "source_file": "08-BestPractices/README.md",
  "language_code": "pcm"
}
-->
# MCP Development Best Practices

[![MCP Development Best Practices](../../../translated_images/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.pcm.png)](https://youtu.be/W56H9W7x-ao)

_(Click di image wey dey up to watch di video for dis lesson)_

## Overview

Dis lesson dey talk about di advanced best practices wey go help you develop, test, and deploy MCP servers and di features for production environments. As MCP ecosystems dey grow dey complex and important, e good make you follow di correct way so dat e go dey reliable, easy to maintain, and go fit work well with other systems. Dis lesson go show you di practical things wey people don learn from real MCP implementations so you fit create strong, efficient servers wey get correct resources, prompts, and tools.

## Learning Objectives

By di end of dis lesson, you go sabi:

- Use di industry best practices for MCP server and feature design
- Create better testing plans for MCP servers
- Design workflows wey dey efficient and fit reuse for complex MCP applications
- Handle errors well, log events, and make MCP servers dey easy to monitor
- Make MCP implementations dey fast, secure, and easy to maintain

## MCP Core Principles

Before we go enter di specific ways to implement MCP, e good make you understand di main principles wey dey guide MCP development:

1. **Standardized Communication**: MCP dey use JSON-RPC 2.0 as di base, e dey provide one consistent format for requests, responses, and error handling for all implementations.

2. **User-Centric Design**: Always make sure say user dey in control, dey give consent, and understand wetin dey happen for your MCP implementations.

3. **Security First**: Put strong security measures like authentication, authorization, validation, and rate limiting.

4. **Modular Architecture**: Design your MCP servers in a way wey each tool and resource get one clear purpose.

5. **Stateful Connections**: Use MCP ability to keep state across multiple requests so interactions go dey more coherent and dey make sense.

## Official MCP Best Practices

Di following best practices na from di official Model Context Protocol documentation:

### Security Best Practices

1. **User Consent and Control**: Always make sure say user gree before you access data or do any operation. Give dem clear control over di data wey dem dey share and di actions wey dem authorize.

2. **Data Privacy**: No expose user data unless dem gree, and protect am with correct access controls. Make sure say unauthorized data no dey transmit.

3. **Tool Safety**: Make sure user gree before you use any tool. Explain di tool functionality well and put strong security boundaries.

4. **Tool Permission Control**: Set di tools wey model fit use for session, make sure say only di tools wey dem authorize dey accessible.

5. **Authentication**: Make sure say authentication dey before you allow access to tools, resources, or sensitive operations. Use API keys, OAuth tokens, or other secure methods.

6. **Parameter Validation**: Check all tool inputs well to stop bad or harmful input from reaching di tool.

7. **Rate Limiting**: Use rate limiting to stop abuse and make sure server resources dey share well.

### Implementation Best Practices

1. **Capability Negotiation**: When connection dey setup, exchange information about di features wey dey available, protocol versions, tools, and resources.

2. **Tool Design**: Create tools wey dey focus on one thing and dey do am well, no create tools wey dey try handle many things at once.

3. **Error Handling**: Use standardized error messages and codes to help diagnose problems, handle failures well, and give feedback wey people fit use.

4. **Logging**: Set up structured logs for auditing, debugging, and monitoring protocol interactions.

5. **Progress Tracking**: For operations wey dey take time, dey report progress updates so user interfaces go dey responsive.

6. **Request Cancellation**: Allow clients to cancel requests wey dem no need again or wey dey take too much time.

## Additional References

For di latest information on MCP best practices, check:

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## Practical Implementation Examples

### Tool Design Best Practices

#### 1. Single Responsibility Principle

Each MCP tool suppose get one clear purpose. No create tools wey dey try do many things at once, instead make tools wey dey specialize for one task.

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

Make sure say error handling dey strong, dey give clear error messages, and dey provide ways to recover.

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

Always check di parameters well to stop bad or harmful input.

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

### Security Implementation Examples

#### 1. Authentication and Authorization

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

## Testing Best Practices

### 1. Unit Testing MCP Tools

Always test your tools one by one, mock di external dependencies:

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

### 2. Integration Testing

Test di full flow from client requests to server responses:

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

## Performance Optimization

### 1. Caching Strategies

Use caching well to reduce latency and resource usage:

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

#### 2. Dependency Injection and Testability

Design tools wey go receive their dependencies through constructor injection, so dem go dey testable and configurable:

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

#### 3. Composable Tools

Design tools wey fit work together to create more complex workflows:

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

### Schema Design Best Practices

Di schema na di contract between di model and your tool. If you design di schema well, e go make di tool easy to use.

#### 1. Clear Parameter Descriptions

Always put clear description for each parameter:

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

Add validation constraints to stop invalid inputs:

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

Make sure say your response structures dey consistent so models go fit understand di results well:

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

Strong error handling dey important for MCP tools to dey reliable.

#### 1. Graceful Error Handling

Handle errors well and give clear messages:

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

Return error information wey dey structured if e dey possible:

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

Add retry logic for failures wey fit happen sometimes:

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

### Performance Optimization

#### 1. Caching

Use caching for operations wey dey expensive:

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

Use asynchronous programming for operations wey dey depend on I/O:

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

Use resource throttling to stop overload:

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

### Security Best Practices

#### 1. Input Validation

Always check input parameters well:

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

Make sure say authorization checks dey:

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

Handle sensitive data with care:

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

## Testing Best Practices for MCP Tools

Testing well go make sure say MCP tools dey work correctly, dey handle edge cases, and dey fit work well with di rest of di system.

### Unit Testing

#### 1. Test Each Tool in Isolation

Create tests wey dey focus on each tool functionality:

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

Test say schemas dey valid and dey enforce constraints well:

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

Create tests wey dey focus on error conditions:

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

Test tools wey dey work together in di way wey you expect:

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

Test di MCP server with full tool registration and execution:

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

Test di complete workflows from model prompt to tool execution:

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

### Performance Testing

#### 1. Load Testing

Test how many requests your MCP server fit handle at di same time:

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

Test di system when e dey under heavy load:

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

#### 3. Monitoring and Profiling

Set up monitoring to check performance over time:

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

## MCP Workflow Design Patterns

Good MCP workflows go make things dey efficient, reliable, and easy to maintain. Here be di key patterns wey you fit follow:

### 1. Chain of Tools Pattern

Connect tools one after di other, where di output of one tool go be di input for di next:

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

Use one central tool wey go send work to di correct specialized tools based on di input:

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

### 3. Parallel Processing Pattern

Run multiple tools at di same time to save time:

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

### 4. Error Recovery Pattern

Add ways to recover well if tool fail:

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

### 5. Workflow Composition Pattern

Create complex workflows by joining simpler ones together:

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

# Testing MCP Servers: Best Practices and Top Tips

## Overview

Testing na one important part of developing MCP servers wey dey reliable and high-quality. Dis guide go show you di best practices and tips for testing your MCP servers from di beginning to di end, including unit tests, integration tests, and end-to-end validation.

## Why Testing Matters for MCP Servers

MCP servers dey act as di middleman between AI models and client applications. Testing well go make sure say:

- E dey reliable for production environments
- E dey handle requests and responses correctly
- E dey follow MCP specifications well
- E fit handle failures and edge cases
- E dey perform well under different loads

## Unit Testing for MCP Servers

### Unit Testing (Foundation)

Unit tests dey check di individual parts of your MCP server one by one.

#### Wetin to Test

1. **Resource Handlers**: Test di logic for each resource handler separately
2. **Tool Implementations**: Check how tools dey behave with different inputs
3. **Prompt Templates**: Make sure say prompt templates dey render well
4. **Schema Validation**: Test di logic wey dey validate parameters
5. **Error Handling**: Check di error responses for bad inputs

#### Best Practices for Unit Testing

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

### Integration Testing (Middle Layer)

Integration tests dey check how di parts of your MCP server dey work together.

#### Wetin to Test

1. **Server Initialization**: Test di server startup with different settings
2. **Route Registration**: Make sure say all endpoints dey register well
3. **Request Processing**: Test di full request-response cycle
4. **Error Propagation**: Make sure say errors dey handle well across di parts
5. **Authentication & Authorization**: Test di security features

#### Best Practices for Integration Testing

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

### End-to-End Testing (Top Layer)

End-to-end tests dey check di whole system from client to server.

#### Wetin to Test

1. **Client-Server Communication**: Test di full request-response cycle
2. **Real Client SDKs**: Test with di actual client implementations
3. **Performance Under Load**: Check how e dey behave with many requests at di same time
4. **Error Recovery**: Test how e dey recover from failures
5. **Long-Running Operations**: Check how e dey handle streaming and operations wey dey take time

#### Best Practices for E2E Testing

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

## Mocking Strategies for MCP Testing

Mocking dey important to separate di parts during testing.

### Wetin to Mock

1. **External AI Models**: Mock di model responses for predictable testing
2. **External Services**: Mock API dependencies like databases or third-party services
3. **Authentication Services**: Mock identity providers
4. **Resource Providers**: Mock resource handlers wey dey expensive

### Example: Mocking an AI Model Response

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

## Performance Testing

Performance testing dey important for MCP servers wey dey production.

### Wetin to Measure

1. **Latency**: Di time wey e dey take to respond to requests
2. **Throughput**: Di number of requests wey e dey handle per second
3. **Resource Utilization**: Di CPU, memory, and network usage
4. **Concurrency Handling**: How e dey behave when many requests dey come at di same time
5. **Scaling Characteristics**: How e dey perform as di load dey increase

### Tools for Performance Testing

- **k6**: Open-source tool for load testing
- **JMeter**: Tool for performance testing
- **Locust**: Python-based tool for load testing
- **Azure Load Testing**: Cloud-based tool for performance testing

### Example: Basic Load Test with k6

```javascript
// k6 script for load testing MCP server
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtual users
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

## Test Automation for MCP Servers

Automating your tests go make sure say quality dey consistent and feedback dey fast.

### CI/CD Integration

1. **Run Unit Tests on Pull Requests**: Make sure say code changes no go spoil di existing functionality
2. **Integration Tests in Staging**: Run integration tests for pre-production environments
3. **Performance Baselines**: Keep performance benchmarks to catch regressions
4. **Security Scans**: Automate security testing as part of di pipeline

### Example CI Pipeline (GitHub Actions)
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

## How to Test Say MCP Specification Dey Work Well

Make sure say your server dey follow MCP specification correct.

### Important Compliance Areas

1. **API Endpoints**: Test di endpoints wey dem need (/resources, /tools, etc.)
2. **Request/Response Format**: Check say schema dey follow di rules
3. **Error Codes**: Make sure say di status codes dey correct for different situations
4. **Content Types**: Test how e dey handle different content types
5. **Authentication Flow**: Confirm say di auth mechanism dey follow di spec

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

## Top 10 Tips to Test MCP Server Well Well

1. **Test Tool Definitions One by One**: Check schema definitions separate from di tool logic
2. **Use Parameterized Tests**: Test di tools with different inputs, even di ones wey dey hard
3. **Check Error Responses**: Make sure say e dey handle errors well for all di possible error conditions
4. **Test Authorization Logic**: Confirm say e dey control access well for different user roles
5. **Monitor Test Coverage**: Try make di critical path code get high coverage
6. **Test Streaming Responses**: Make sure say e dey handle streaming content well
7. **Simulate Network Wahala**: Test how e go behave if network no dey good
8. **Test Resource Limits**: Check how e go behave if e reach quota or rate limits
9. **Automate Regression Tests**: Create tests wey go run anytime code change
10. **Document Test Cases**: Keep clear documentation for di test scenarios

## Common Testing Mistakes

- **Too much happy path testing**: Make sure say you test di error cases well
- **Forget performance testing**: Find di bottlenecks before dem go affect production
- **Testing alone**: Combine unit, integration, and E2E tests
- **Incomplete API coverage**: Test all di endpoints and features
- **Inconsistent test environments**: Use containers to make sure test environments dey consistent

## Conclusion

If you wan build MCP servers wey dey reliable and high-quality, you need better testing strategy. Follow di best practices and tips wey dey this guide to make sure say your MCP implementations dey meet di highest standards for quality, reliability, and performance.

## Key Points to Remember

1. **Tool Design**: Follow single responsibility principle, use dependency injection, and design am make e fit work with other tools
2. **Schema Design**: Create schemas wey clear, well-documented, and get proper validation constraints
3. **Error Handling**: Make sure say e dey handle errors well, get structured error responses, and retry logic
4. **Performance**: Use caching, asynchronous processing, and resource throttling
5. **Security**: Do thorough input validation, authorization checks, and handle sensitive data well
6. **Testing**: Create unit, integration, and end-to-end tests wey complete
7. **Workflow Patterns**: Use patterns like chains, dispatchers, and parallel processing

## Exercise

Design MCP tool and workflow for document processing system wey go:

1. Accept documents for different formats (PDF, DOCX, TXT)
2. Extract text and key information from di documents
3. Classify di documents by type and content
4. Generate summary for each document

Create di tool schemas, error handling, and workflow pattern wey go fit this scenario. Think about how you go test di implementation.

## Resources 

1. Join di MCP community for [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) to dey follow di latest updates 
2. Contribute to open-source [MCP projects](https://github.com/modelcontextprotocol)
3. Use MCP principles for your organization AI work
4. Check di MCP implementations wey dey special for your industry. 
5. Try take advanced courses for MCP topics like multi-modal integration or enterprise application integration.
6. Try build your own MCP tools and workflows with di principles wey you learn for [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

Next: Best Practices [case studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
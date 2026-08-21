# MCP Development Best Practices

[![MCP Development Best Practices](../../../translated_images/pcm/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Click di pikshua wey dey above to watch dis lesson video)_

## Overview

Dis lesson dey focus on advanced best practices for developing, testing, and deploying MCP servers and features inside production environments. As MCP ecosystems dey grow complex and important, to follow correct patterns dey make sure sey e reliable, e fit maintain, and e fit connect well well. Dis lesson dey put together correct knowledge wey come from real-world MCP implementations to help you create strong, efficient servers with good resources, prompts, and tools.

## Learning Objectives

By the time you finish dis lesson, you go fit:

- Use industry best practices for MCP server and feature design
- Create complete testing strategies for MCP servers
- Design efficient, reusable workflow patterns for complex MCP applications
- Implement correct error handling, logging, and observability for MCP servers
- Optimize MCP implementations for performance, security, and maintainability

## MCP Core Principles

Before you start to sabi specific implementation practices, e important to understand the core principles wey guide better MCP development:

1. **Standardized Communication**: MCP dey use JSON-RPC 2.0 as im base, wey dey give steady format for requests, responses, and error handling for all implementations.

2. **User-Centric Design**: Always put user consent, control, and transparency first for your MCP implementations.

3. **Security First**: Put strong security measures like authentication, authorization, validation, and rate limiting.

4. **Modular Architecture**: Design your MCP servers with modular way, so each tool and resource get clear and focused purpose.

5. **Explicit State**: MCP `2026-07-28` no get state for protocol
   layer. When workflow need cross-call state, use clear handles or
   normal tool arguments backed by steady application state.

## Official MCP Best Practices

The following best practices come from official Model Context Protocol documentation:

### Security Best Practices

1. **User Consent and Control**: Always make sure user give clear consent before you access data or perform operations. Give clear control over wetin data dem share and which actions dem allow.

2. **Data Privacy**: Only expose user data with clear consent and protect am with correct access controls. Safeguard against unauthorized data transmission.

3. **Tool Safety**: Make sure user give clear consent before you use any tool. Make dem understand each tool work and keep strong security boundaries.

4. **Tool Permission Control**: Fix which tools model fit use for
   each request and authorization context, make sure only tools wey dem allow
   fit access.

5. **Authentication**: Make sure correct authentication dey before access tools, resources, or sensitive operations, use API keys, OAuth tokens, or other secure authentication methods.

6. **Parameter Validation**: Make sure validation dey for all tool invocations to prevent bad or harmful input from enter tool implementations.

7. **Rate Limiting**: Use rate limiting to stop misuse and make sure fair usage of server resources.

### Implementation Best Practices

1. **Capability Negotiation**: Talk to and agree the protocol versions and
   capabilities wey MCP `2026-07-28` get. Each request dey complete by itself and fit
   use `server/discover`; old versions dey use initialization handshake.

2. **Tool Design**: Create focused tools wey dey do one thing well, not big tools wey handle many things.

3. **Error Handling**: Put standard error messages and codes to help you find wahala, handle failure well, and give correct feedback.

4. **Observability**: Use `stderr` for stdio diagnostics and OpenTelemetry
   for structured observability. MCP logging feature no dey use again for
   `2026-07-28` specification.

5. **Progress Tracking**: For long operations, make you report progress updates to help user interfaces respond well.

6. **Request Cancellation**: Make allow clients cancel requests wey dem no need again or wey dey take too long.

## Additional References

For most current info on MCP best practices, use:

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)][mcp-2026-spec]
- [Previous MCP Specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Tasks Extension][mcp-tasks-extension]
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Security risks and mitigations
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on security training

### Reliability Companion Lesson

Normal retry loops no safe for tools wey dey create tickets, payments,
messages, deployments, or other real effects. Response fit lost
after the effect don happen.

Use the reliability companion lesson,
[Safe Retries for MCP Tools: A Reliability Sidecar Pattern][reliability-sidecar],
to sabi stable operation keys, duplicate admission, checkpointing,
reconciliation, evidence levels, and failure injection.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Practical Implementation Examples

### Tool Design Best Practices

#### 1. Single Responsibility Principle

Every MCP tool suppose get clear and focused purpose. Instead make big tools wey try do many things, develop special tools wey sabi one particular task well.

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

Put strong error handling with clear error messages and correct recovery ways.

```python
# Python example wey get beta error handling
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Parameter check
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Security check
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Database work wit timeout
                async with timeout(10):  # 10 second timeout
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Connection wahala fit be small one
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Query wahala na likely client wahala
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Make tool-specific errors pass through
            raise
        except Exception as e:
            # Catch-all for surprise wahala
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # How to detect SQL injection
        pass
        
    def _log_error(self, message, error):
        # How to log error dem
        pass
```

#### 3. Parameter Validation

Always check parameters well to stop bad or malicious input.

```javascript
// JavaScript/TypeScript example wit detailed parameter validation
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
    // 1. Check say parameter dey
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Check parameter type dem
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Check parameter value dem
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Check say content dey for write operation
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Check say path safe
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementation based on di parameters wey don pass validation
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // How to check if path safe
    // ...
  }
}
```

### Security Implementation Examples

#### 1. Authentication and Authorization

```java
// Java example wit authentication an authorization
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
        // 1. Comot authentication context
        String authToken = request.getContext().getAuthToken();
        
        // 2. Authenticate user
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Check authorization for di correct operation
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Continue wit authorized operation
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

Always test your tools separate, use mocking for outside dependencies:

```typescript
// TypeScript example of a tool unit test
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Make one fake weather service
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Make the tool with the fake dependency
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

Test the entire flow from client requests to server responses:

```python
# Python integration test example
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Start test server
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Create client
        client = McpClient("http://localhost:5000")
        
        # Test if tool fit show
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Test if tool fit run
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Check say response correct
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Comot everytin wey no need
        await server.stop()
```

## Performance Optimization

### 1. Caching Strategies

Use correct caching to reduce delay and save resource usage:


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

#### 2. Dependency Injection na Testability

Design tools wey go receive dia dependencies through constructor injection, make dem dey testable and configurable:

```java
// Java example wit dependency injection
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Dependencies we dem put inside through constructor
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

Design tools wey fit compose together to create more complex workflows:

```python
# Python example wey dey show how tools fit join body
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # How to take do am...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Dis tool fit use result wey dataFetch tool bring
    async def execute_async(self, request):
        # How to take do am...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Dis tool fit use result wey dataAnalysis tool bring
    async def execute_async(self, request):
        # How to take do am...
        pass

# Dem fit use dis tools onnay-one or join body as workflow part
```

### Schema Design Best Practices

The schema na the contract between the model and your tool. Well-designed schemas dey lead to better tool usability.

#### 1. Clear Parameter Descriptions

Always include descriptive information for every parameter:

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

Include validation constraints to stop wrong inputs:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Email property wey dey check say e correct format
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Age property wey get number-limit
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Property wey get set list of values
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

Make sure say your response structures dey consistent to make am easy for models to understand results:

```python
async def execute_async(self, request):
    try:
        # Dey process request
        results = await self._search_database(request.parameters["query"])
        
        # Always return structure wey no go change
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

Strong error handling dey important for MCP tools to maintain reliability.

#### 1. Graceful Error Handling

Handle errors at correct levels and give informative messages:

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

Return structured error information when e possible:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implemencheshon
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
        
        // Chook back oda exception dem as ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Retry Logic

Use normal retry logic only for read-only calls or operations wey
downstream contract don already be idempotent. For effectful operations, timeout
after sending the request fit confuse. Make sure say you reconcile authoritative state and
use the same stable operation key before you run am again. See the
[reliability sidecar companion lesson](./reliability-sidecars/README.md).

The bounded retry loop wey follow good for read-only lookup be dis:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # seconds
    
    while retry_count < max_retries:
        try:
            # Call one read-only external API
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Exponential backoff
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Non-transient error, no try again
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Performance Optimization

#### 1. Caching

Implement caching for expensive operations:

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

Use asynchronous programming patterns for I/O-bound operations:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // For long-running operations, return a processing ID immediately
        String processId = UUID.randomUUID().toString();
        
        // Begin async processing
        CompletableFuture.runAsync(() -> {
            try {
                // Do long-running operation
                documentService.processDocument(documentId);
                
                // Update status (e go usually dey stored for database)
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

Implement resource throttling to avoid overload:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Make e possible to accept 5 request per second
            bucket_size=10        # Make e possible to carry burst reach 10 request
        )
    
    async def execute_async(self, request):
        # Check if we fit continue or if we gats wait
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # If di wait too long
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Wait for correct delay time
                await asyncio.sleep(delay)
        
        # Use one token come continue wit di request
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
            
            # Calculate time reach next token go dey available
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Add new tokens based on how time don pass
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Security Best Practices

#### 1. Input Validation

Always validate input parameters properly:

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

Implement correct authorization checks:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Comot user context from request
    UserContext user = request.getContext().getUserContext();
    
    // Check if user get di permissions wey e need
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // For specific resources, check if user fit access dat resource
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Continue with tool execution
    // ...
}
```

#### 3. Sensitive Data Handling

Handle sensitive data carefully:

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
        
        # Collect user data
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filter sensitive fields if dem no specifically ask or no get permission
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Check permission level inside request context
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Make copy so e no go change di original one
        redacted = user_data.copy()
        
        # Hide specific sensitive fields
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Hide sensitive data wey de inside other data
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Testing Best Practices for MCP Tools

Complete testing dey ensure say MCP tools dey work well, fit handle edge cases, and integrate properly with the rest of the system.

### Unit Testing

#### 1. Test Each Tool for Inside Only

Create focused tests for every tool functionality:

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

Test say schemas valid and dey enforce constraints well:

```java
@Test
public void testSchemaValidation() {
    // Make tool instance
    SearchTool searchTool = new SearchTool();
    
    // Get schema
    Object schema = searchTool.getSchema();
    
    // Change schema to JSON for validation
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Check sey schema dey valid JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Try correct parameters
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Try weh require parameter no dey
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Try wrong parameter type
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Error Handling Tests

Create specific tests for error conditions:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Arrange
    tool = ApiTool(timeout=0.1)  # Very short timeout
    
    # Mock wan request wey go time out
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
    
    # Mock wan rate-limited response
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
        
        # Verify exception get rate limit info
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integration Testing

#### 1. Tool Chain Testing

Test tools wey dey work together in expected combinations:

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

Test the MCP server with full tool registration and execution:

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
        // Test di discovery endpoint
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
        
        // Send request and check di response
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Make invalid tool request
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Parameter "b" no dey
        request.put("parameters", parameters);
        
        // Send request and check for error response
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. End-to-End Testing

Test complete workflows from model prompt reach tool execution:

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

Test how many concurrent requests your MCP server fit handle:

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

Test the system under heavy load:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Arrange JMeter for stress testing
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Setup JMeter test plan
    HashTree testPlanTree = new HashTree();
    
    // Make test plan, thread group, samplers, etc.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Add HTTP sampler for tool run
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
    
    // Run the test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Check if results correct
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Average response time no pass 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90th percentile no pass 500ms
}
```

#### 3. Monitoring and Profiling

Set up monitoring for long-term performance analysis:

```python
# Set up monitoring for MCP server
def configure_monitoring(server):
    # Arrange Prometheus metrics
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
    
    # Add middleware wey go time and record metrics
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Make metrics endpoint dey available
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP Workflow Design Patterns

Well-designed MCP workflows improve efficiency, reliability, and maintainability. Here be main patterns to follow:

### 1. Chain of Tools Pattern

Join plenty tools together for sequence where each tool output dey become input for the next one:

```python
# Python Chain of Tools implementation
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # List of tool names we go run one by one
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Run each tool for the chain, carry the last result go next
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Keep result and use am as input for the next tool
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Example of how to use am
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

Use central tool wey dey dispatch to specialized tools based on input:

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

Run many tools at the same time for efficiency:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Step 1: Carry dataset metadata come (synchronous)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Step 2: Run plenti analyses for parallel
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
        
        // Wait make all di parallel work finish
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Wait till e complete
        
        // Step 3: Join all di results togeder
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Step 4: Make summary report
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Return di complete work result
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Error Recovery Pattern

Implement smooth fallback for tool failures:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Try di main tool first
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Write down di failure
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Use di secondary tool
            try:
                # Fit need transform parameters for fallback tool
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Both tools no work
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Dis implementation go depend on di specific tools
        # For dis example, we go just return di original parameters
        return params

# Example use
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Primary (paid) weather API
        "basicWeatherService",    # Fallback (free) weather API
        {"location": location}
    )
```

### 5. Workflow Composition Pattern

Build complex workflows by joining simpler ones together:

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

Testing na important part of developing reliable, high-quality MCP servers. This guide dey provide complete best practices and tips for testing your MCP servers all through development lifecycle, from unit tests down to integration tests and end-to-end validation.

## Why Testing Matter for MCP Servers

MCP servers na critical middleware between AI models and client apps. Thorough testing dey ensure:

- Reliability for production environments
- Correct handling of requests and responses
- Proper implementation of MCP specifications
- Strength to face failures and edge cases
- Steady performance under different loads

## Unit Testing for MCP Servers

### Unit Testing (Foundation)

Unit tests go check individual parts of your MCP server separately.

#### Wetin to Test

1. **Resource Handlers**: Test each resource handler logic alone
2. **Tool Implementations**: Check tool behavior with different inputs
3. **Prompt Templates**: Make sure prompt templates display correct
4. **Schema Validation**: Test parameter validation logic
5. **Error Handling**: Confirm error responses for wrong inputs

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
# Example unit test for calculator tool for Python
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
    
    # Make sure say e correct
    assert result["value"] == 12
```

### Integration Testing (Middle Layer)

Integration tests go check how components of your MCP server dey interact.

#### Wetin to Test

1. **Server Initialization**: Test server startup with different configurations
2. **Route Registration**: Check if all endpoints dey registered well
3. **Request Processing**: Test the full request-response cycle
4. **Error Propagation**: Make sure errors dey handled well through components
5. **Authentication & Authorization**: Test security mechanisms

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

End-to-end tests dey check the full system behavior from client to server.

#### Wetin to Test

1. **Client-Server Communication**: Test full request-response cycles
2. **Real Client SDKs**: Test with real client implementations
3. **Performance Under Load**: Check behavior with many concurrent requests
4. **Error Recovery**: Test system recovery from failures

5. **Operations Wey Dey Run Long Time**: Check how una dey handle streaming and long operations dem

#### Best Way to Do E2E Testing

```typescript
// Example E2E test wit client for TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Start server for test environment
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Do am
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Check am
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Mocking Strategies for MCP Testing

Mocking na important tin to separate components during testing.

### Components Wey Need Make You Mock

1. **External AI Models**: Mock model responses make testing dey predictable
2. **External Services**: Mock API dependencies (databases, third-party services)
3. **Authentication Services**: Mock identity providers
4. **Resource Providers**: Mock expensive resource handlers

### Example: Mocking AI Model Response

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
# Python example wit unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Arrange mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Use mock for test
    server = McpServer(model_client=mock_model)
    # Continue wit test
```

## Performance Testing

Performance testing na beta thing for production MCP servers.

### Wetin You Go Measure

1. **Latency**: How fast responses dey come
2. **Throughput**: How many requests dem fit handle per second
3. **Resource Utilization**: CPU, memory, network usage
4. **Concurrency Handling**: How e be when requests dey come for parallel
5. **Scaling Characteristics**: How e go perform as load too much

### Tools Wey Fit Use for Performance Testing

- **k6**: Open-source load testing tool
- **JMeter**: Beta beta performance testing tool
- **Locust**: Python-based load testing tool
- **Azure Load Testing**: Cloud-based performance testing

### Example: Basic Load Test with k6

```javascript
// k6 skript for load test MCP server
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

Automating your tests dey ensure consistent quality and faster feedback.

### CI/CD Integration

1. **Run Unit Tests on Pull Requests**: Make sure code change no spoil wetin dey work
2. **Integration Tests in Staging**: Run integration tests for pre-production
3. **Performance Baselines**: Keep performance benchmarks make you fit catch regressions
4. **Security Scans**: Automate security testing as part of pipeline

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

## Testing for Compliance with MCP Specification

Check make sure your server dey implement MCP specification well.

### Key Compliance Areas

1. **API Endpoints**: Test all necessary endpoints (/resources, /tools, etc.)
2. **Request/Response Format**: Check schema compliance
3. **Error Codes**: Verify correct status codes for different scenarios
4. **Content Types**: Test how different content types dey handled
5. **Authentication Flow**: Verify spec-compliant auth mechanisms

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

## Top 10 Tips for Effective MCP Server Testing

1. **Test Tool Definitions Separately**: Verify schema definitions separate from tool logic
2. **Use Parameterized Tests**: Test tools with plenty inputs, including edge cases
3. **Check Error Responses**: Verify correct error handling for all error cases
4. **Test Authorization Logic**: Confirm proper access control for different user roles
5. **Monitor Test Coverage**: Try get plenty coverage for critical path code
6. **Test Streaming Responses**: Verify proper handling of streaming content
7. **Simulate Network Issues**: Test wetin happen under bad network condition
8. **Test Resource Limits**: Check how e go be when reach quotas or rate limits
9. **Automate Regression Tests**: Build suite wey go run every code change
10. **Document Test Cases**: Keep clear documentation of test scenarios

## Common Testing Pitfalls

- **Over-reliance on happy path testing**: Make sure say you dey test error cases well well
- **Ignoring performance testing**: Find bottlenecks before dem spoil production
- **Testing in isolation only**: Make you combine unit, integration, and E2E tests
- **Incomplete API coverage**: Make sure all endpoints and features dey tested
- **Inconsistent test environments**: Use containers to get consistent test environments

## Conclusion

Good testing strategy na beta way to get reliable, high-quality MCP servers. If you follow best practices and tips for this guide, you fit make sure your MCP implementations meet top standards for quality, reliability, and performance.


## Key Takeaways

1. **Tool Design**: Follow single responsibility principle, use dependency injection, and design for composability
2. **Schema Design**: Create clear, well-documented schemas with proper validation constraints
3. **Error Handling**: Implement smooth error handling, structured error
   responses, and outcome-aware retry logic
4. **Performance**: Use caching, asynchronous processing, and resource throttling
5. **Security**: Apply thorough input validation, authorization checks, and sensitive data handling
6. **Testing**: Create thorough unit, integration, and end-to-end tests
7. **Workflow Patterns**: Use well-known patterns like chains, dispatchers, and parallel processing

## Exercise

Design MCP tool and workflow for document processing system wey:

1. Accept documents for different formats (PDF, DOCX, TXT)
2. Extract text and important info from the documents
3. Classify documents by type and content
4. Generate summary of each document

Implement the tool schemas, error handling, and workflow pattern wey best for this case. Think how you go test am.

## Resources 

1. Join MCP community for [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) to dey updated on latest developments 
2. Contribute to open-source [MCP projects](https://github.com/modelcontextprotocol)
3. Use MCP principles for your own organization AI initiatives
4. Explore special MCP implementations for your industry. 
5. Think about taking advanced courses on specific MCP topics, like multi-modal integration or enterprise application integration.
6. Try build your own MCP tools and workflows with principles wey you learn from the [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Wetin Next

Next: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
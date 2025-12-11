<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62150e27d4b7b5797ee41146d176e6b",
  "translation_date": "2025-12-11T10:44:19+00:00",
  "source_file": "08-BestPractices/README.md",
  "language_code": "te"
}
-->
# MCP అభివృద్ధి ఉత్తమ పద్ధతులు

[![MCP అభివృద్ధి ఉత్తమ పద్ధతులు](../../../translated_images/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.te.png)](https://youtu.be/W56H9W7x-ao)

_(ఈ పాఠం వీడియోను చూడడానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

## అవలోకనం

ఈ పాఠం ఉత్పత్తి వాతావరణాలలో MCP సర్వర్లు మరియు ఫీచర్లను అభివృద్ధి, పరీక్ష మరియు అమలు చేయడంలో ఆధునిక ఉత్తమ పద్ధతులపై దృష్టి సారిస్తుంది. MCP పర్యావరణాలు సంక్లిష్టత మరియు ప్రాముఖ్యత పెరుగుతున్నందున, స్థాపించబడిన నమూనాలను అనుసరించడం విశ్వసనీయత, నిర్వహణ సామర్థ్యం మరియు పరస్పర కార్యాచరణను నిర్ధారిస్తుంది. ఈ పాఠం వాస్తవ ప్రపంచ MCP అమలుల నుండి పొందిన ప్రాక్టికల్ జ్ఞానాన్ని సమీకరించి, సమర్థవంతమైన వనరులు, ప్రాంప్ట్‌లు మరియు సాధనాలతో బలమైన, సమర్థవంతమైన సర్వర్లను సృష్టించడంలో మీకు మార్గనిర్దేశం చేస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసే సమయానికి, మీరు చేయగలుగుతారు:

- MCP సర్వర్ మరియు ఫీచర్ డిజైన్‌లో పరిశ్రమ ఉత్తమ పద్ధతులను వర్తింపజేయండి
- MCP సర్వర్ల కోసం సమగ్ర పరీక్షా వ్యూహాలను సృష్టించండి
- సంక్లిష్ట MCP అనువర్తనాల కోసం సమర్థవంతమైన, పునర్వినియోగపరచదగిన వర్క్‌ఫ్లో నమూనాలను డిజైన్ చేయండి
- MCP సర్వర్లలో సరైన లోప నిర్వహణ, లాగింగ్ మరియు పరిశీలనను అమలు చేయండి
- పనితీరు, భద్రత మరియు నిర్వహణ సామర్థ్యానికి MCP అమలులను ఆప్టిమైజ్ చేయండి

## MCP ప్రాథమిక సూత్రాలు

నిర్దిష్ట అమలు పద్ధతులలోకి దిగేముందు, సమర్థవంతమైన MCP అభివృద్ధిని మార్గనిర్దేశం చేసే ప్రాథమిక సూత్రాలను అర్థం చేసుకోవడం ముఖ్యం:

1. **ప్రామాణికీకృత కమ్యూనికేషన్**: MCP దాని ఆధారంగా JSON-RPC 2.0 ను ఉపయోగిస్తుంది, ఇది అన్ని అమలులలో అభ్యర్థనలు, ప్రతిస్పందనలు మరియు లోప నిర్వహణకు సुसंगత ఫార్మాట్‌ను అందిస్తుంది.

2. **వినియోగదారుడు-కేంద్రీకృత డిజైన్**: మీ MCP అమలులలో ఎప్పుడూ వినియోగదారుడి అనుమతి, నియంత్రణ మరియు పారదర్శకతను ప్రాధాన్యం ఇవ్వండి.

3. **భద్రత మొదట**: ధృడమైన భద్రతా చర్యలను అమలు చేయండి, అందులో గుర్తింపు, అనుమతి, ధృవీకరణ మరియు రేటు పరిమితి ఉన్నాయి.

4. **మాడ్యులర్ ఆర్కిటెక్చర్**: ప్రతి సాధనం మరియు వనరు స్పష్టమైన, కేంద్రీకృత ఉద్దేశ్యంతో ఉండేలా మీ MCP సర్వర్లను మాడ్యులర్ దృష్టితో డిజైన్ చేయండి.

5. **స్థితిస్థాపక కనెక్షన్లు**: అనేక అభ్యర్థనల మధ్య స్థితిని నిర్వహించే MCP సామర్థ్యాన్ని ఉపయోగించి మరింత సుస్పష్టమైన మరియు సందర్భానుగుణమైన పరస్పర చర్యలను సాధించండి.

## అధికారిక MCP ఉత్తమ పద్ధతులు

క్రింది ఉత్తమ పద్ధతులు అధికారిక మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ డాక్యుమెంటేషన్ నుండి తీసుకోబడ్డాయి:

### భద్రత ఉత్తమ పద్ధతులు

1. **వినియోగదారుడు అనుమతి మరియు నియంత్రణ**: డేటా యాక్సెస్ చేయడానికి లేదా ఆపరేషన్లు నిర్వహించడానికి ఎప్పుడూ స్పష్టమైన వినియోగదారుడు అనుమతిని కోరండి. ఏ డేటా పంచబడుతుంది మరియు ఏ చర్యలు అనుమతించబడ్డాయో స్పష్టమైన నియంత్రణను అందించండి.

2. **డేటా గోప్యత**: స్పష్టమైన అనుమతితో మాత్రమే వినియోగదారుడి డేటాను ప్రదర్శించండి మరియు సరైన యాక్సెస్ నియంత్రణలతో రక్షించండి. అనధికార డేటా ప్రసారం నుండి రక్షించండి.

3. **సాధన భద్రత**: ఏ సాధనను పిలవడానికి ముందు స్పష్టమైన వినియోగదారుడు అనుమతిని కోరండి. ప్రతి సాధన యొక్క కార్యాచరణను వినియోగదారులు అర్థం చేసుకోవాలని నిర్ధారించండి మరియు ధృడమైన భద్రతా సరిహద్దులను అమలు చేయండి.

4. **సాధన అనుమతి నియంత్రణ**: సెషన్ సమయంలో మోడల్ ఉపయోగించగల సాధనలను కాన్ఫిగర్ చేయండి, స్పష్టంగా అనుమతించబడిన సాధనలకే యాక్సెస్ ఉండేలా చూసుకోండి.

5. **గుర్తింపు**: సాధనాలు, వనరులు లేదా సున్నితమైన ఆపరేషన్లకు యాక్సెస్ ఇవ్వడానికి సరైన గుర్తింపును కోరండి, API కీలు, OAuth టోకెన్లు లేదా ఇతర భద్రతా పద్ధతులను ఉపయోగించి.

6. **పారామీటర్ ధృవీకరణ**: అన్ని సాధన పిలుపులకు ధృవీకరణను అమలు చేయండి, దుర్వినియోగ లేదా దుష్టమైన ఇన్‌పుట్ సాధన అమలులకు చేరకుండా నిరోధించండి.

7. **రేటు పరిమితి**: దుర్వినియోగాన్ని నివారించడానికి మరియు సర్వర్ వనరుల న్యాయమైన వినియోగాన్ని నిర్ధారించడానికి రేటు పరిమితిని అమలు చేయండి.

### అమలు ఉత్తమ పద్ధతులు

1. **సామర్థ్య చర్చ**: కనెక్షన్ సెటప్ సమయంలో, మద్దతు పొందిన ఫీచర్లు, ప్రోటోకాల్ సంస్కరణలు, అందుబాటులో ఉన్న సాధనాలు మరియు వనరుల గురించి సమాచారం మార్పిడి చేయండి.

2. **సాధన డిజైన్**: బహుళ సమస్యలను నిర్వహించే మోనోలిథిక్ సాధనల కంటే ఒక పని బాగా చేసే కేంద్రీకృత సాధనలను సృష్టించండి.

3. **లోప నిర్వహణ**: సమస్యలను గుర్తించడానికి, వైఫల్యాలను సున్నితంగా నిర్వహించడానికి మరియు చర్య తీసుకునే ఫీడ్‌బ్యాక్ అందించడానికి ప్రామాణికీకృత లోప సందేశాలు మరియు కోడ్‌లను అమలు చేయండి.

4. **లాగింగ్**: ఆడిటింగ్, డీబగ్గింగ్ మరియు ప్రోటోకాల్ పరస్పర చర్యలను పర్యవేక్షించడానికి నిర్మిత లాగ్‌లను కాన్ఫిగర్ చేయండి.

5. **ప్రగతి ట్రాకింగ్**: దీర్ఘకాలిక ఆపరేషన్ల కోసం, స్పందనాత్మక వినియోగదారుఇంటర్‌ఫేస్‌లను సాధించడానికి ప్రగతి నవీకరణలను నివేదించండి.

6. **అభ్యర్థన రద్దు**: ఇక అవసరం లేని లేదా ఎక్కువ సమయం తీసుకుంటున్న ఫ్లైట్‌లో ఉన్న అభ్యర్థనలను క్లయింట్లు రద్దు చేయగలగాలి.

## అదనపు సూచనలు

MCP ఉత్తమ పద్ధతులపై తాజా సమాచారం కోసం, చూడండి:

- [MCP డాక్యుమెంటేషన్](https://modelcontextprotocol.io/)
- [MCP స్పెసిఫికేషన్](https://spec.modelcontextprotocol.io/)
- [GitHub రిపాజిటరీ](https://github.com/modelcontextprotocol)
- [భద్రత ఉత్తమ పద్ధతులు](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## ప్రాక్టికల్ అమలు ఉదాహరణలు

### సాధన డిజైన్ ఉత్తమ పద్ధతులు

#### 1. ఏకైక బాధ్యత సూత్రం

ప్రతి MCP సాధనకు స్పష్టమైన, కేంద్రీకృత ఉద్దేశ్యం ఉండాలి. బహుళ సమస్యలను నిర్వహించడానికి ప్రయత్నించే మోనోలిథిక్ సాధనలను సృష్టించడానికి బదులు, నిర్దిష్ట పనులలో నైపుణ్యం కలిగిన ప్రత్యేక సాధనలను అభివృద్ధి చేయండి.

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

#### 2. సुसంగత లోప నిర్వహణ

సమాచారాత్మక లోప సందేశాలు మరియు సరైన పునరుద్ధరణ యంత్రాంగాలతో ధృడమైన లోప నిర్వహణను అమలు చేయండి.

```python
# సమగ్ర లోపం నిర్వహణతో పython ఉదాహరణ
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # పారామితి ధృవీకరణ
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # భద్రత ధృవీకరణ
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # టైమౌట్‌తో డేటాబేస్ ఆపరేషన్
                async with timeout(10):  # 10 సెకన్ల టైమౌట్
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # కనెక్షన్ లోపాలు తాత్కాలికంగా ఉండవచ్చు
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # క్వెరీ లోపాలు సాధారణంగా క్లయింట్ లోపాలు
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # టూల్-స్పెసిఫిక్ లోపాలు దాటించండి
            raise
        except Exception as e:
            # అనుకోని లోపాల కోసం క్యాచ్-ఆల్
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL ఇంజెక్షన్ గుర్తింపు అమలు
        pass
        
    def _log_error(self, message, error):
        # లోపం లాగింగ్ అమలు
        pass
```

#### 3. పారామీటర్ ధృవీకరణ

తప్పు లేదా దుష్టమైన ఇన్‌పుట్‌ను నివారించడానికి ఎప్పుడూ పారామీటర్లను పూర్తిగా ధృవీకరించండి.

```javascript
// JavaScript/TypeScript ఉదాహరణతో వివరమైన పారామితి ధృవీకరణ
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
    // 1. పారామితి ఉనికిని ధృవీకరించండి
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. పారామితి రకాలును ధృవీకరించండి
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. పారామితి విలువలను ధృవీకరించండి
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. రాయడం ఆపరేషన్ కోసం కంటెంట్ ఉనికిని ధృవీకరించండి
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. మార్గం భద్రత ధృవీకరణ
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // ధృవీకరించిన పారామితుల ఆధారంగా అమలు
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // మార్గం భద్రత తనిఖీ అమలు
    // ...
  }
}
```

### భద్రత అమలు ఉదాహరణలు

#### 1. గుర్తింపు మరియు అనుమతి

```java
// ధృవీకరణ మరియు అనుమతితో జావా ఉదాహరణ
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // డిపెండెన్సీ ఇంజెక్షన్
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
        // 1. ధృవీకరణ సందర్భాన్ని తీసుకోండి
        String authToken = request.getContext().getAuthToken();
        
        // 2. వినియోగదారుని ధృవీకరించండి
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. నిర్దిష్ట ఆపరేషన్ కోసం అనుమతిని తనిఖీ చేయండి
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. అనుమతిప్రాప్త ఆపరేషన్‌తో కొనసాగండి
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

#### 2. రేటు పరిమితి

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

## పరీక్షా ఉత్తమ పద్ధతులు

### 1. యూనిట్ టెస్టింగ్ MCP సాధనాలు

మీ సాధనలను ఎప్పుడూ వేరుగా పరీక్షించండి, బాహ్య ఆధారాలను మాక్ చేయండి:

```typescript
// టైప్‌స్క్రిప్ట్ టూల్ యూనిట్ టెస్ట్ ఉదాహరణ
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // మాక్ వాతావరణ సేవను సృష్టించండి
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // మాక్ డిపెండెన్సీతో టూల్‌ను సృష్టించండి
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // ఏర్పాట్లు
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // చర్య
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // నిర్ధారణ
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // ఏర్పాట్లు
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // చర్య & నిర్ధారణ
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. ఇంటిగ్రేషన్ టెస్టింగ్

క్లయింట్ అభ్యర్థనల నుండి సర్వర్ ప్రతిస్పందనల వరకు పూర్తి ప్రవాహాన్ని పరీక్షించండి:

```python
# పైథాన్ ఇంటిగ్రేషన్ టెస్ట్ ఉదాహరణ
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # టెస్ట్ సర్వర్ ప్రారంభించండి
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # క్లయింట్ సృష్టించండి
        client = McpClient("http://localhost:5000")
        
        # టూల్ కనుగొనడం పరీక్షించండి
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # టూల్ అమలు పరీక్షించండి
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # ప్రతిస్పందనను ధృవీకరించండి
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # శుభ్రపరచండి
        await server.stop()
```

## పనితీరు ఆప్టిమైజేషన్

### 1. క్యాచింగ్ వ్యూహాలు

విలంబం మరియు వనరు వినియోగాన్ని తగ్గించడానికి సరైన క్యాచింగ్‌ను అమలు చేయండి:

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

#### 2. డిపెండెన్సీ ఇంజెక్షన్ మరియు పరీక్షా సామర్థ్యం

కన్స్ట్రక్టర్ ఇంజెక్షన్ ద్వారా వారి ఆధారాలను అందుకునేలా సాధనలను డిజైన్ చేయండి, తద్వారా అవి పరీక్షించదగినవి మరియు కాన్ఫిగర్ చేయదగినవి అవుతాయి:

```java
// డిపెండెన్సీ ఇంజెక్షన్‌తో జావా ఉదాహరణ
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // కన్‌స్ట్రక్టర్ ద్వారా ఇంజెక్ట్ చేయబడిన డిపెండెన్సీలు
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // టూల్ అమలు
    // ...
}
```

#### 3. కంపోజబుల్ సాధనాలు

సంక్లిష్ట వర్క్‌ఫ్లోలను సృష్టించడానికి కలిసి పనిచేసే సాధనలను డిజైన్ చేయండి:

```python
# కంపోజబుల్ టూల్స్ చూపించే పైథాన్ ఉదాహరణ
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # అమలు...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # ఈ టూల్ dataFetch టూల్ నుండి ఫలితాలను ఉపయోగించవచ్చు
    async def execute_async(self, request):
        # అమలు...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # ఈ టూల్ dataAnalysis టూల్ నుండి ఫలితాలను ఉపయోగించవచ్చు
    async def execute_async(self, request):
        # అమలు...
        pass

# ఈ టూల్స్ స్వతంత్రంగా లేదా వర్క్‌ఫ్లో భాగంగా ఉపయోగించవచ్చు
```

### స్కీమా డిజైన్ ఉత్తమ పద్ధతులు

స్కీమా మోడల్ మరియు మీ సాధన మధ్య ఒప్పందం. బాగా డిజైన్ చేసిన స్కీమాలు మెరుగైన సాధన వినియోగాన్ని కలిగిస్తాయి.

#### 1. స్పష్టమైన పారామీటర్ వివరణలు

ప్రతి పారామీటర్ కోసం వివరణాత్మక సమాచారాన్ని ఎప్పుడూ చేర్చండి:

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

#### 2. ధృవీకరణ పరిమితులు

చెల్లని ఇన్‌పుట్‌లను నివారించడానికి ధృవీకరణ పరిమితులను చేర్చండి:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // ఫార్మాట్ ధృవీకరణతో ఇమెయిల్ ప్రాపర్టీ
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // సంఖ్యా పరిమితులతో వయస్సు ప్రాపర్టీ
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // ఎన్యూమరేటెడ్ ప్రాపర్టీ
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

#### 3. సుసంగత రిటర్న్ నిర్మాణాలు

ఫలితాలను మోడల్స్ సులభంగా అర్థం చేసుకునేలా మీ ప్రతిస్పందన నిర్మాణాలలో సుసంగతతను నిలుపుకోండి:

```python
async def execute_async(self, request):
    try:
        # అభ్యర్థనను ప్రాసెస్ చేయండి
        results = await self._search_database(request.parameters["query"])
        
        # ఎప్పుడూ ఒక సुसంగతమైన నిర్మాణాన్ని తిరిగి ఇవ్వండి
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

### లోప నిర్వహణ

ధృడమైన లోప నిర్వహణ MCP సాధనాల విశ్వసనీయతను నిలుపుకోవడానికి కీలకం.

#### 1. సున్నితమైన లోప నిర్వహణ

సరైన స్థాయిల్లో లోపాలను నిర్వహించి సమాచారాత్మక సందేశాలను అందించండి:

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

#### 2. నిర్మిత లోప ప్రతిస్పందనలు

సాధ్యమైనప్పుడు నిర్మిత లోప సమాచారాన్ని తిరిగి ఇవ్వండి:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // అమలు
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
        
        // ఇతర తప్పిదాలను ToolExecutionException గా మళ్లీ విసిరి వేయండి
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. మళ్లీ ప్రయత్నించే లాజిక్

తాత్కాలిక వైఫల్యాలకు సరైన మళ్లీ ప్రయత్నించే లాజిక్‌ను అమలు చేయండి:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # సెకన్లు
    
    while retry_count < max_retries:
        try:
            # బాహ్య API ని పిలవండి
            return await self._call_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # ఘాతాంక వెనుకడుగు
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # తాత్కాలిక కాని లోపం, మళ్లీ ప్రయత్నించవద్దు
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### పనితీరు ఆప్టిమైజేషన్

#### 1. క్యాచింగ్

ఖర్చుతో కూడుకున్న ఆపరేషన్ల కోసం క్యాచింగ్‌ను అమలు చేయండి:

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

#### 2. అసింక్రోనస్ ప్రాసెసింగ్

I/O-బౌండ్ ఆపరేషన్ల కోసం అసింక్రోనస్ ప్రోగ్రామింగ్ నమూనాలను ఉపయోగించండి:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // దీర్ఘకాలిక ఆపరేషన్ల కోసం, ప్రాసెసింగ్ ID ను వెంటనే తిరిగి ఇవ్వండి
        String processId = UUID.randomUUID().toString();
        
        // అసింక్ ప్రాసెసింగ్ ప్రారంభించండి
        CompletableFuture.runAsync(() -> {
            try {
                // దీర్ఘకాలిక ఆపరేషన్ నిర్వహించండి
                documentService.processDocument(documentId);
                
                // స్థితిని నవీకరించండి (సాధారణంగా డేటాబేస్‌లో నిల్వ చేయబడుతుంది)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // ప్రాసెస్ ID తో తక్షణ స్పందనను తిరిగి ఇవ్వండి
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // సహచర స్థితి తనిఖీ సాధనం
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

#### 3. వనరు త్రాట్లింగ్

ఓవర్‌లోడ్ నివారించడానికి వనరు త్రాట్లింగ్‌ను అమలు చేయండి:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # సెకనుకు 5 అభ్యర్థనలను అనుమతించండి
            bucket_size=10        # 10 అభ్యర్థనల వరకు బర్స్‌లను అనుమతించండి
        )
    
    async def execute_async(self, request):
        # మేము కొనసాగవచ్చా లేదా వేచి ఉండాల్సిన అవసరముందో తనిఖీ చేయండి
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # వేచి ఉండటం చాలా ఎక్కువ అయితే
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # సరైన ఆలస్యం సమయానికి వేచి ఉండండి
                await asyncio.sleep(delay)
        
        # ఒక టోకెన్‌ను వినియోగించి అభ్యర్థనతో కొనసాగండి
        self.rate_limiter.consume()
        
        # APIని పిలవండి
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
            
            # తదుపరి టోకెన్ అందుబాటులో ఉండే వరకు సమయాన్ని లెక్కించండి
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # గడిచిన సమయాన్ని ఆధారంగా కొత్త టోకెన్లను జోడించండి
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### భద్రత ఉత్తమ పద్ధతులు

#### 1. ఇన్‌పుట్ ధృవీకరణ

ఎప్పుడూ ఇన్‌పుట్ పారామీటర్లను పూర్తిగా ధృవీకరించండి:

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

#### 2. అనుమతి తనిఖీలు

సరైన అనుమతి తనిఖీలను అమలు చేయండి:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // అభ్యర్థన నుండి వినియోగదారు సందర్భాన్ని పొందండి
    UserContext user = request.getContext().getUserContext();
    
    // వినియోగదారుకు అవసరమైన అనుమతులు ఉన్నాయా అని తనిఖీ చేయండి
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // నిర్దిష్ట వనరుల కోసం, ఆ వనరుకు ప్రాప్తి ఉందా అని తనిఖీ చేయండి
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // టూల్ అమలు కొనసాగించండి
    // ...
}
```

#### 3. సున్నితమైన డేటా నిర్వహణ

సున్నితమైన డేటాను జాగ్రత్తగా నిర్వహించండి:

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
        
        # వినియోగదారు డేటాను పొందండి
        user_data = await self.user_service.get_user_data(user_id)
        
        # స్పష్టంగా అభ్యర్థించబడిన మరియు అనుమతించబడినప్పుడే సున్నితమైన ఫీల్డులను ఫిల్టర్ చేయండి
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # అభ్యర్థన సందర్భంలో అనుమతి స్థాయిని తనిఖీ చేయండి
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # అసలు డేటాను మార్చకుండా కాపీని సృష్టించండి
        redacted = user_data.copy()
        
        # నిర్దిష్ట సున్నితమైన ఫీల్డులను రిడాక్ట్ చేయండి
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # లోపల ఉన్న సున్నితమైన డేటాను రిడాక్ట్ చేయండి
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP సాధనాల కోసం పరీక్షా ఉత్తమ పద్ధతులు

సమగ్ర పరీక్ష MCP సాధనాలు సరిగ్గా పనిచేస్తున్నాయో, ఎడ్జ్ కేసులను నిర్వహిస్తున్నాయో, మరియు వ్యవస్థతో సరిగ్గా సమగ్రపరచబడ్డాయో నిర్ధారిస్తుంది.

### యూనిట్ టెస్టింగ్

#### 1. ప్రతి సాధనను వేరుగా పరీక్షించండి

ప్రతి సాధన యొక్క కార్యాచరణ కోసం కేంద్రీకృత పరీక్షలను సృష్టించండి:

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

#### 2. స్కీమా ధృవీకరణ పరీక్ష

స్కీమాలు చెల్లుబాటు అయ్యేలా మరియు పరిమితులను సరైన రీతిలో అమలు చేస్తున్నాయో పరీక్షించండి:

```java
@Test
public void testSchemaValidation() {
    // టూల్ ఇన్స్టాన్స్ సృష్టించండి
    SearchTool searchTool = new SearchTool();
    
    // స్కీమాను పొందండి
    Object schema = searchTool.getSchema();
    
    // ధృవీకరణ కోసం స్కీమాను JSON గా మార్చండి
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // స్కీమా సరైన JSONSchema కాదని ధృవీకరించండి
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // సరైన పారామితులను పరీక్షించండి
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // అవసరమైన పారామితి లేకపోవడం పరీక్షించండి
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // తప్పు పారామితి రకం పరీక్షించండి
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. లోప నిర్వహణ పరీక్షలు

లోప పరిస్థితుల కోసం ప్రత్యేక పరీక్షలను సృష్టించండి:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # ఏర్పాటు చేయండి
    tool = ApiTool(timeout=0.1)  # చాలా చిన్న టైమ్‌అవుట్
    
    # టైమ్‌అవుట్ అయ్యే అభ్యర్థనను మాక్ చేయండి
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # టైమ్‌అవుట్ కంటే ఎక్కువ
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # చర్య & నిర్ధారణ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # తప్పిద సందేశాన్ని ధృవీకరించండి
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # ఏర్పాటు చేయండి
    tool = ApiTool()
    
    # రేట్-లిమిటెడ్ స్పందనను మాక్ చేయండి
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
        
        # చర్య & నిర్ధారణ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # తప్పిదంలో రేట్ లిమిట్ సమాచారం ఉందని ధృవీకరించండి
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### ఇంటిగ్రేషన్ టెస్టింగ్

#### 1. సాధన చైన్ పరీక్ష

అంచనా వేయబడిన కలయికలలో కలిసి పనిచేసే సాధనలను పరీక్షించండి:

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

#### 2. MCP సర్వర్ పరీక్ష

పూర్తి సాధన నమోదు మరియు అమలుతో MCP సర్వర్‌ను పరీక్షించండి:

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
        // డిస్కవరీ ఎండ్‌పాయింట్‌ను పరీక్షించండి
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // టూల్ అభ్యర్థన సృష్టించండి
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // అభ్యర్థన పంపండి మరియు ప్రతిస్పందనను ధృవీకరించండి
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // చెల్లని టూల్ అభ్యర్థన సృష్టించండి
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // "b" పరామితి లేదు
        request.put("parameters", parameters);
        
        // అభ్యర్థన పంపండి మరియు లోపం ప్రతిస్పందనను ధృవీకరించండి
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. ఎండ్-టు-ఎండ్ పరీక్ష

మోడల్ ప్రాంప్ట్ నుండి సాధన అమలుకు పూర్తి వర్క్‌ఫ్లోలను పరీక్షించండి:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # అమర్చండి - MCP క్లయింట్ మరియు మాక్ మోడల్ సెట్ చేయండి
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # మాక్ మోడల్ ప్రతిస్పందనలు
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
    
    # మాక్ వాతావరణ సాధనం ప్రతిస్పందన
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
        
        # చర్య తీసుకోండి
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # నిర్ధారించండి
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### పనితీరు పరీక్ష

#### 1. లోడ్ పరీక్ష

మీ MCP సర్వర్ ఎంత concurrent అభ్యర్థనలను నిర్వహించగలదో పరీక్షించండి:

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

#### 2. స్ట్రెస్ పరీక్ష

అత్యధిక లోడ్ కింద వ్యవస్థను పరీక్షించండి:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // స్ట్రెస్ టెస్టింగ్ కోసం JMeter సెటప్ చేయండి
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter టెస్ట్ ప్లాన్ కాన్ఫిగర్ చేయండి
    HashTree testPlanTree = new HashTree();
    
    // టెస్ట్ ప్లాన్, థ్రెడ్ గ్రూప్, సాంప్లర్లు మొదలైనవి సృష్టించండి
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // టూల్ ఎగ్జిక్యూషన్ కోసం HTTP సాంప్లర్ జోడించండి
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // లిసనర్లు జోడించండి
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // టెస్ట్ నడపండి
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // ఫలితాలను ధృవీకరించండి
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // సగటు స్పందన సమయం < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90వ శాతం < 500ms
}
```

#### 3. పర్యవేక్షణ మరియు ప్రొఫైలింగ్

దీర్ఘకాలిక పనితీరు విశ్లేషణ కోసం పర్యవేక్షణను ఏర్పాటు చేయండి:

```python
# MCP సర్వర్ కోసం మానిటరింగ్‌ను కాన్ఫిగర్ చేయండి
def configure_monitoring(server):
    # Prometheus మెట్రిక్స్‌ను సెటప్ చేయండి
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
    
    # టైమింగ్ మరియు రికార్డింగ్ మెట్రిక్స్ కోసం మిడిల్వేర్‌ను జోడించండి
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # మెట్రిక్స్ ఎండ్పాయింట్‌ను ఎక్స్‌పోజ్ చేయండి
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP వర్క్‌ఫ్లో డిజైన్ నమూనాలు

బాగా డిజైన్ చేసిన MCP వర్క్‌ఫ్లోలు సమర్థవంతత, విశ్వసనీయత మరియు నిర్వహణ సామర్థ్యాన్ని మెరుగుపరుస్తాయి. అనుసరించవలసిన ముఖ్యమైన నమూనాలు:

### 1. సాధనల గొలుసు నమూనా

ప్రతి సాధన అవుట్‌పుట్ తదుపరి సాధన ఇన్‌పుట్‌గా మారేలా అనేక సాధనలను వరుసగా కనెక్ట్ చేయండి:

```python
# పైథాన్ చైన్ ఆఫ్ టూల్స్ అమలు
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # వరుసగా అమలు చేయడానికి టూల్ పేర్ల జాబితా
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # చైన్‌లో ప్రతి టూల్‌ను అమలు చేయండి, మునుపటి ఫలితాన్ని పంపండి
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # ఫలితాన్ని నిల్వ చేసి తదుపరి టూల్‌కు ఇన్‌పుట్‌గా ఉపయోగించండి
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# ఉదాహరణ ఉపయోగం
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

### 2. డిస్పాచర్ నమూనా

ఇన్‌పుట్ ఆధారంగా ప్రత్యేక సాధనలకు పంపిణీ చేసే కేంద్ర సాధనను ఉపయోగించండి:

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

### 3. సమాంతర ప్రాసెసింగ్ నమూనా

సమర్థవంతత కోసం అనేక సాధనలను ఒకేసారి అమలు చేయండి:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // దశ 1: డేటాసెట్ మెటాడేటాను పొందండి (సింక్రోనస్)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // దశ 2: అనేక విశ్లేషణలను సమాంతరంగా ప్రారంభించండి
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
        
        // అన్ని సమాంతర పనులు పూర్తయ్యేవరకు వేచి ఉండండి
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // పూర్తి కావడానికి వేచి ఉండండి
        
        // దశ 3: ఫలితాలను కలపండి
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // దశ 4: సారాంశ నివేదికను రూపొందించండి
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // పూర్తి వర్క్‌ఫ్లో ఫలితాన్ని తిరిగి ఇవ్వండి
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. లోప పునరుద్ధరణ నమూనా

సాధన వైఫల్యాలకు సున్నితమైన ఫాల్బ్యాక్‌లను అమలు చేయండి:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # మొదటి సాధనాన్ని ప్రయత్నించండి
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # విఫలమవడాన్ని లాగ్ చేయండి
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # ద్వితీయ సాధనానికి తిరిగి వెళ్ళండి
            try:
                # తిరిగి వెళ్ళే సాధనానికి పారామితులను మార్చాల్సి ఉండవచ్చు
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # రెండు సాధనాలు విఫలమయ్యాయి
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # ఈ అమలు నిర్దిష్ట సాధనాలపై ఆధారపడి ఉంటుంది
        # ఈ ఉదాహరణకు, మేము అసలు పారామితులను మాత్రమే తిరిగి ఇస్తాము
        return params

# ఉదాహరణ ఉపయోగం
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # ప్రాథమిక (చెల్లింపు) వాతావరణ API
        "basicWeatherService",    # తిరిగి వెళ్ళే (ఉచిత) వాతావరణ API
        {"location": location}
    )
```

### 5. వర్క్‌ఫ్లో కంపోజిషన్ నమూనా

సరళమైన వాటిని కలిపి సంక్లిష్ట వర్క్‌ఫ్లోలను నిర్మించండి:

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

# MCP సర్వర్ల పరీక్ష: ఉత్తమ పద్ధతులు మరియు ముఖ్య సూచనలు

## అవలోకనం

పరీక్ష MCP సర్వర్లను విశ్వసనీయమైన, ఉన్నత-నాణ్యత గల సర్వర్లుగా అభివృద్ధి చేయడంలో కీలకమైన అంశం. ఈ మార్గదర్శకం యూనిట్ టెస్టుల నుండి ఇంటిగ్రేషన్ టెస్టులు మరియు ఎండ్-టు-ఎండ్ ధృవీకరణ వరకు మీ MCP సర్వర్లను అభివృద్ధి జీవన చక్రం అంతటా పరీక్షించడానికి సమగ్ర ఉత్తమ పద్ధతులు మరియు సూచనలను అందిస్తుంది.

## MCP సర్వర్ల కోసం పరీక్ష ఎందుకు ముఖ్యం

MCP సర్వర్లు AI మోడల్స్ మరియు క్లయింట్ అనువర్తనాల మధ్య కీలక మిడిల్వేర్‌గా పనిచేస్తాయి. సమగ్ర పరీక్ష నిర్ధారిస్తుంది:

- ఉత్పత్తి వాతావరణాలలో విశ్వసనీయత
- అభ్యర్థనలు మరియు ప్రతిస్పందనలను ఖచ్చితంగా నిర్వహించడం
- MCP స్పెసిఫికేషన్ల సరైన అమలు
- వైఫల్యాలు మరియు ఎడ్జ్ కేసులపై ప్రతిఘటన
- వివిధ లోడ్ల కింద సుసంగత పనితీరు

## MCP సర్వర్ల కోసం యూన
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

## MCP స్పెసిఫికేషన్‌తో అనుగుణత కోసం పరీక్షించడం

మీ సర్వర్ సరిగ్గా MCP స్పెసిఫికేషన్‌ను అమలు చేస్తున్నదని నిర్ధారించుకోండి.

### ముఖ్య అనుగుణత ప్రాంతాలు

1. **API ఎండ్‌పాయింట్లు**: అవసరమైన ఎండ్‌పాయింట్లను పరీక్షించండి (/resources, /tools, మొదలైనవి)
2. **అభ్యర్థన/ప్రతిస్పందన ఫార్మాట్**: స్కీమా అనుగుణతను ధృవీకరించండి
3. **లోపం కోడ్లు**: వివిధ పరిస్థితుల కోసం సరైన స్థితి కోడ్లను నిర్ధారించండి
4. **కంటెంట్ రకాల**: వేర్వేరు కంటెంట్ రకాల నిర్వహణను పరీక్షించండి
5. **ప్రామాణీకరణ ప్రవాహం**: స్పెక్స్ అనుగుణమైన ఆథ్ మెకానిజంలను నిర్ధారించండి

### అనుగుణత పరీక్ష సూట్

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

## సమర్థవంతమైన MCP సర్వర్ పరీక్ష కోసం టాప్ 10 సూచనలు

1. **టూల్ నిర్వచనాలను వేరుగా పరీక్షించండి**: టూల్ లాజిక్ నుండి స్వతంత్రంగా స్కీమా నిర్వచనాలను నిర్ధారించండి
2. **పారామెటరైజ్డ్ పరీక్షలను ఉపయోగించండి**: వివిధ ఇన్‌పుట్‌లతో, ఎడ్జ్ కేస్‌లతో టూల్స్‌ను పరీక్షించండి
3. **లోపం ప్రతిస్పందనలను తనిఖీ చేయండి**: అన్ని సాధ్యమైన లోప పరిస్థితుల కోసం సరైన లోప నిర్వహణను నిర్ధారించండి
4. **అధికార లాజిక్‌ను పరీక్షించండి**: వేర్వేరు యూజర్ పాత్రల కోసం సరైన యాక్సెస్ నియంత్రణను నిర్ధారించండి
5. **పరీక్ష కవరేజ్‌ను పర్యవేక్షించండి**: కీలక మార్గ కోడ్ యొక్క అధిక కవరేజ్ లక్ష్యంగా పెట్టుకోండి
6. **స్ట్రీమింగ్ ప్రతిస్పందనలను పరీక్షించండి**: స్ట్రీమింగ్ కంటెంట్ సరైన నిర్వహణను నిర్ధారించండి
7. **నెట్‌వర్క్ సమస్యలను అనుకరించండి**: తక్కువ నెట్‌వర్క్ పరిస్థితులలో ప్రవర్తనను పరీక్షించండి
8. **వనరు పరిమితులను పరీక్షించండి**: క్వోటాలు లేదా రేట్ పరిమితులు చేరినప్పుడు ప్రవర్తనను నిర్ధారించండి
9. **రిగాression పరీక్షలను ఆటోమేట్ చేయండి**: ప్రతి కోడ్ మార్పుపై నడిచే సూట్‌ను నిర్మించండి
10. **పరీక్ష కేసులను డాక్యుమెంట్ చేయండి**: పరీక్ష పరిస్థితుల స్పష్టమైన డాక్యుమెంటేషన్‌ను నిర్వహించండి

## సాధారణ పరీక్ష లోపాలు

- **సంతోషకరమైన మార్గ పరీక్షపై అధిక ఆధారపడటం**: లోప కేసులను పూర్తిగా పరీక్షించండి
- **పనితీరు పరీక్షను నిర్లక్ష్యం చేయడం**: ఉత్పత్తిపై ప్రభావం చూపే ముందు బాటిల్‌నెక్స్‌ను గుర్తించండి
- **వేరుగా మాత్రమే పరీక్షించడం**: యూనిట్, ఇంటిగ్రేషన్, మరియు E2E పరీక్షలను కలపండి
- **అపూర్ణ API కవరేజ్**: అన్ని ఎండ్‌పాయింట్లు మరియు ఫీచర్లను పరీక్షించండి
- **అసమంజసమైన పరీక్ష వాతావరణాలు**: సుస్పష్టమైన పరీక్ష వాతావరణాల కోసం కంటైనర్లను ఉపయోగించండి

## ముగింపు

నమ్మకమైన, ఉన్నత-నాణ్యత MCP సర్వర్లను అభివృద్ధి చేయడానికి సమగ్ర పరీక్ష వ్యూహం అవసరం. ఈ గైడ్‌లో వివరించిన ఉత్తమ పద్ధతులు మరియు సూచనలను అమలు చేయడం ద్వారా, మీ MCP అమలు నాణ్యత, నమ్మకదారితనం, మరియు పనితీరు యొక్క అత్యున్నత ప్రమాణాలను చేరుకుంటాయని మీరు నిర్ధారించుకోవచ్చు.


## ముఖ్యమైన పాఠాలు

1. **టూల్ డిజైన్**: సింగిల్ రెస్పాన్సిబిలిటీ సూత్రాన్ని అనుసరించండి, డిపెండెన్సీ ఇంజెక్షన్ ఉపయోగించండి, మరియు కంపోజబిలిటీ కోసం డిజైన్ చేయండి
2. **స్కీమా డిజైన్**: స్పష్టమైన, బాగా డాక్యుమెంటెడ్ స్కీమాలను సరైన ధృవీకరణ పరిమితులతో సృష్టించండి
3. **లోప నిర్వహణ**: సున్నితమైన లోప నిర్వహణ, నిర్మిత లోప ప్రతిస్పందనలు, మరియు రీట్రై లాజిక్‌ను అమలు చేయండి
4. **పనితీరు**: క్యాషింగ్, అసింక్రోనస్ ప్రాసెసింగ్, మరియు వనరు త్రోట్లింగ్ ఉపయోగించండి
5. **భద్రత**: సమగ్ర ఇన్‌పుట్ ధృవీకరణ, అధికార తనిఖీలు, మరియు సున్నితమైన డేటా నిర్వహణను వర్తించండి
6. **పరీక్ష**: సమగ్ర యూనిట్, ఇంటిగ్రేషన్, మరియు ఎండ్-టు-ఎండ్ పరీక్షలను సృష్టించండి
7. **వర్క్‌ఫ్లో నమూనాలు**: చైన్లు, డిస్పాచర్స్, మరియు సమాంతర ప్రాసెసింగ్ వంటి స్థాపిత నమూనాలను వర్తించండి

## వ్యాయామం

కింది లక్షణాలు కలిగిన డాక్యుమెంట్ ప్రాసెసింగ్ సిస్టమ్ కోసం MCP టూల్ మరియు వర్క్‌ఫ్లో డిజైన్ చేయండి:

1. బహుళ ఫార్మాట్లలో డాక్యుమెంట్లను స్వీకరించండి (PDF, DOCX, TXT)
2. డాక్యుమెంట్ల నుండి టెక్స్ట్ మరియు ముఖ్య సమాచారం తీసుకోండి
3. డాక్యుమెంట్లను రకం మరియు కంటెంట్ ఆధారంగా వర్గీకరించండి
4. ప్రతి డాక్యుమెంట్ యొక్క సారాంశాన్ని రూపొందించండి

ఈ సన్నివేశానికి ఉత్తమంగా సరిపోయే టూల్ స్కీమాలు, లోప నిర్వహణ, మరియు వర్క్‌ఫ్లో నమూనాను అమలు చేయండి. మీరు ఈ అమలును ఎలా పరీక్షిస్తారో పరిగణించండి.

## వనరులు

1. తాజా అభివృద్ధులపై అప్డేట్ కావడానికి [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs) లో MCP కమ్యూనిటీకి చేరండి
2. ఓపెన్-సోర్స్ [MCP ప్రాజెక్టులకు](https://github.com/modelcontextprotocol) సహకరించండి
3. మీ స్వంత సంస్థ యొక్క AI కార్యక్రమాలలో MCP సూత్రాలను వర్తించండి
4. మీ పరిశ్రమ కోసం ప్రత్యేక MCP అమలులను అన్వేషించండి
5. బహుముఖ మోడల్ ఇంటిగ్రేషన్ లేదా ఎంటర్ప్రైజ్ అప్లికేషన్ ఇంటిగ్రేషన్ వంటి ప్రత్యేక MCP అంశాలపై అధునాతన కోర్సులు తీసుకోవడం పరిగణించండి
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) ద్వారా నేర్చుకున్న సూత్రాలను ఉపయోగించి మీ స్వంత MCP టూల్స్ మరియు వర్క్‌ఫ్లోలను ప్రయోగించండి

తర్వాత: ఉత్తమ పద్ధతులు [కేస్ స్టడీస్](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
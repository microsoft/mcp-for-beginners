# MCP అభివృద్ధి ఉత్తమ అలవాట్లు

[![MCP అభివృద్ధి ఉత్తమ అలవాట్లు](../../../translated_images/te/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(ఈ పాఠంలోని వీడియోను వీక్షించడానికి పై చిత్రం క్లిక్ చేయండి)_

## అవలోకనం

ఈ పాఠం ఉత్పత్తి వాతావరణాల్లో MCP సర్వర్లను మరియు ఫీచర్లను అభివృద్ధి చేయడం, పరీక్షించడం మరియు రూపాయి చేసే ఉన్నత ఉత్తమ ఆచారాలపై దృష్టి సారిస్తుంది. MCP పరిసరాలు క్లిష్టత మరియు ప్రాధాన్యత పెరిగిన కొద్దీ, ప్రస్థాపిత నమూనాలను అనుసరించడం నమ్మకదాయకత, నిర్వహణ సౌలభ్యం మరియు అంతరసంబంధితతను నిర్ధారిస్తుంది. ఈ పాఠం ఆచరణాత్మక జ్ఞానాన్ని సమీకరించి, మీరు బలమైన, సమర్థవంతమైన సర్వర్‌లు, సమర్థవంతమైన వనరులు, ప్రాంప్ట్‌లు మరియు టూల్‌లతో సృష్టించే మార్గదర్శకత్వం అందిస్తుంది.

## అభ్యాస లక్ష్యాలు

ఈ పాఠం ముగియునప్పుడు మీరు చేయగలుగుతారు:

- MCP సర్వర్ మరియు ఫీచర్ డిజైన్‌లో పరిశ్రమ ఉత్తమ అలవాట్లను వర్తింపజేయండి
- MCP సర్వర్ల కొరకు సమగ్ర పరీక్షా వ్యూహాలను రూపొందించండి
- క్లిష్ట MCP అనువర్తనాల కొరకు సమర్థవంతమైన, పునర్వినియోగపరచగల వర్క్‌ఫ్లో నమూనాలను రూపకల్పన చేయండి
- MCP సర్వర్లలో సరైన లోపం నిర్వహణ, లాగింగ్ మరియు గమనించదగినతను అమలు చేయండి
- పనితీరు, భద్రత మరియు నిర్వహణ సౌలభ్యం కోసం MCP అమలులను ఆప్టిమైజ్ చేయండి

## MCP ప్రాథమిక సూత్రాలు

నిర్దిష్ట అమలు అలవాట్లలోకి వెళ్లేముందు, సమర్థవంతమైన MCP అభివృద్ధిని నడిపే ప్రాథమిక సూత్రాలను అర్థం చేసుకోవడం ముఖ్యం:

1. **ప్రామాణీకృత కమ్యూనికేషన్**: MCP దాని అంతస్తుగా JSON-RPC 2.0 ను ఉపయోగిస్తుంది, అన్ని అమలులలో అభ్యర్థన‌లు, స్పందన‌లు మరియు లోపాల నిర్వహణకు సుసాందర్భ రూపాన్ని అందిస్తుంది.

2. **ఉపయోగకర్త కేంద్రీకృత డిజైన్**: మీ MCP అమలుల్లో ఎప్పుడూ వినియోగదారు అనుమతి, నియంత్రణ మరియు పారదర్శకతను ప్రాధాన్యత ఇవ్వండి.

3. **భద్రత మొదటి ప్రాధాన్యం**: సరైన భద్రతా చర్యలు అమలు చేయండి, అందులో ప్రామాణీకరణ, అధికారప్రదానం, ధృవీకరణ మరియు రేటు పరిమితి ఉన్నాయి.

4. **మాడ్యులర్ నిర్మాణం**: ప్రతి టూల్ మరియు వనరు స్పష్టమైన, లక్ష్యస్పష్టమైన ఉద్దేశ్యంతో MCP సర్వర్‌లను మాడ్యులర్ విధానంలో రూపొందించండి.

5. **స్పష్ట స్థితి**: MCP `2026-07-28` ప్రోటకాల్ అంతస్తులో స్థితి రహితం.
   ఒక వర్క్‌ఫ్లో క్రాస్-కాల్ స్థితిని అవసరం చేసుకుంటే, స్పష్టమైన హ్యాండిల్స్ లేదా
   సాధారణ టూల్ ఆర్గుమెంట్లను ఉపయోగించండి, ఇవి దీర్ఘకాలిక అనువర్తన స్థితితో మద్దతు పొందుతాయి.

## అధికార MCP ఉత్తమ అలవాట్లు

క్రింద పేర్కొన్న ఉత్తమ అలవాట్లు అధికార మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ డాక్యుమెంటేషన్ నుండి తీసుకున్నవి:

### భద్రత ఉత్తమ అలవాట్లు

1. **వినియోగదారు అనుమతి మరియు నియంత్రణ**: డేటా యాక్సెస్ లేదా ఆపరేషన్‌లు నిర్వహించే ముందు ఎప్పుడూ స్పష్టమైన వినియోగదారు అనుమతిని కోరండి. ఏ డేటా పంచుకోవాలో మరియు ఏ చర్యలు అధికృతమవుతున్నాయో స్పష్టమైన నియంత్రణను అందించండి.

2. **డేటా గోప్యత**: వినియోగదారుని స్పష్టమైన అనుమతితో మాత్రమే డేటా ప్రదర్శన చేయండి మరియు అనుకూల యాక్సెస్ నియంత్రణలతో దానికి రక్షణ ఇవ్వండి. అనధికార డేటా ప్రసారం నుండి రక్షించండి.

3. **టూల్ సురక్షత**: ఏ టూల్‌ను పిలవడానికి ముందే వినియోగదారు స్పష్టమైన అనుమతిని కోరండి. ప్రతి టూల్ యొక్క పనితీరు వినియోగదారులు అర్థం చేసుకోవాలి మరియు ఘనమైన భద్రతా సరిహద్దులను అమలు చేయండి.

4. **టూల్ అనుమతి నియంత్రణ**: ప్రతి అభ్యర్థన మరియు అధికార సందర్భం కోసం మోడలుకి ఉపయోగించదగిన టూల్స్‌ను ఆకృతీకరించండి, కేవలం స్పష్టంగా అధిరోహిత టూల్స్ మాత్రమే యాక్సెస్ ఉండే విధంగా చేస్తూ.
   
   

5. **ప్రామాణీకరణ**: టూల్స్, వనరులు లేదా సున్నితమైన ఆపరేషన్లకు యాక్సెస్ ఇవ్వడానికి సరైన ప్రామాణీకరణను కోరండి, API కీస్, OAuth టోకెన్‌లు లేదా ఇతర సురక్షిత ప్రామాణీకరణ విధానాలు ఉపయోగించండి.

6. **పారామీటర్ ధృవీకరణ**: సమస్త టూల్ పిలుపులకూ ధృవీకరణను అమలు చేసి, అశుద్ధము లేదా మాలిషియస్ ఇన్‌పుట్ టూల్ అమలులవద్దికి చేరకుండా నిరోధించండి.

7. **రేటు పరిమితి**: వనరు పాడుచేసే దుర్వినియోగాన్ని నివారించడానికి, సర్వర్ వనరుల న్యాయమైన వాడకాన్ని నిర్ధారించడానికి రేటు పరిమితిని అమలు చేయండి.

### అమలు ఉత్తమ అలవాట్లు

1. **సామర్థ్య చర్చ**: మద్దతు లభించే ప్రోటకాల్ సంస్కరణలు మరియు సామర్థ్యాలను చర్చించండి. MCP `2026-07-28` లో ప్రతి అభ్యర్థన స్వీయ కంటైనర్ మరియు `server/discover` ఉపయోగించవచ్చు; పాత సంస్కరణలు ప్రారంభ హెండ్‌షేక్ ఉపయోగిస్తాయి.
   
   

2. **టూల్ డిజైన్**: బహు అంశాలను నిర్వహించే మోనోలిథిక్ టూల్స్ కన్నా ఒక పని బాగా చేసే స్పష్టమైన టూల్స్ రూపొందించండి.

3. **లోపం నిర్వహణ**: సమస్యలను గుర్తించేందుకు, విఫలాలను మృదువుగా నిర్వహించేందుకు, ఆచరణీయమైన ప్రతిస్పందనల కోసం ప్రామాణీకృత లోప సందేశాలు మరియు కోడ్స్ అమలు చేయండి.

4. **గమనించదగినత**: stdio రోగనిర్ధారణల కోసం `stderr` మరియు నిర్మిత గమనించదగినత కోసం OpenTelemetry ఉపయోగించండి. MCP లాగింగ్ ఫీచర్ `2026-07-28` స్పెసిఫికేషన్‌లో పాతదయ్యింది.
   
   

5. **ప్రమోత్త చర్యలపై గమనింపు**: దీర్ఘకాలిక ఆపరేషన్ల కోసం, ప్రగతి నవీకరణలను నివేదించి స్పందనాత్మక వినియోగదారు ఇంటర్ఫేసులను సక్రియం చేయండి.

6. **అభ్యర్థన రద్దు**: అవసరం లేకపోతే లేదా తక్కువ సమయం తీసుకుంటున్న ఇన్-ఫ్లైట్ అభ్యర్థనలను క్లయింట్లు రద్దు చేసుకోగలగాలి.

## అదనపు సూచనలు

MCP ఉత్తమ అలవాట్లపై తాజా సమాచారం కోసం, చూడండి:

- [MCP డాక్యుమెంటేషన్](https://modelcontextprotocol.io/)
- [MCP స్పెసిఫికేషన్ (2026-07-28)][mcp-2026-spec]
- [మునుపటి MCP స్పెసిఫికేషన్ (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP టాస్క్స్ విస్తరణ][mcp-tasks-extension]
- [గిట్‌హబ్ రిపాజిటరీ](https://github.com/modelcontextprotocol)
- [భద్రత ఉత్తమ అలవాట్లు](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP టాప్ 10](https://microsoft.github.io/mcp-azure-security-guide/) - భద్రతా ప్రమాదాలు మరియు ఉపశమనం
- [MCP భద్రతా సమ్మిట్ వర్క్షాప్ (షెర్పా)](https://azure-samples.github.io/sherpa/) - చేతిలో భద్రతా శిక్షణ

### విశ్వసనీయత సహచర పాఠం

సాధారణ రీట్రై లూప్‌లు టికెట్లు, చెల్లింపులు, సందేశాలు, డిప్లాయ్‌మెంట్లు లేదా ఇతర వాస్తవ ప్రభావాల సృష్టించే టూల్స్ కోసం సురక్షితం కావు. ఒక స్పందన ప్రభావం ఎక్కించిన తర్వాత కోల్పోయే అవకాశం ఉంటుంది.
   
   

విశ్వసనీయత సహచర పాఠం ఉపయోగించండి,
[MCP టూల్స్ కొరకు సురక్షిత రీట్రైలు: ఒక విశ్వసనీయత సైడ్‌కార్ నమూనా][reliability-sidecar],
స్థిరమైన ఆపరేషన్ కీలు, డూప్లికేట్ ఆడ్మిషన్, చెక్కుపాయింటింగ్, పునర్సమీపనం, సాక్ష్య స్తాయిలు మరియు విఫలం ఇంజెక్షన్ నేర్చుకోండి.


[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## ఆచరణాత్మక అమలు ఉదాహరణలు

### టూల్ డిజైన్ ఉత్తమ అలవాట్లు

#### 1. ఒక విధేయత సిద్ధాంతం

ప్రతి MCP టూల్ స్పష్టమైన, లక్ష్యస్పష్టమైన ఉద్దేశ్యం కలిగి ఉండాలి. బహు అంశాలను నిర్వహించటాన్ని ప్రయత్నించే మోనోలిథిక్ టూల్స్ సృష్టించే బదులు, నిర్ధిష్ట పనులలో మిహురించిన ప్రత్యేక టూల్స్ అభివృద్ధి చేయండి.

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

#### 2. సుస్థిర లోప నిర్వహణ

సమాచార లోప సందేశాలు మరియు సరైన పునరుద్ధరణ పద్ధతులతో ఘనమైన లోప నిర్వహణను అమలు చేయండి.

```python
# విస్తృతమైన లోప నిర్ధారణతో పైథాన్ ఉదాహరణ
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # పారామీటర్ ధ్రువీకరణ
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # భద్రతా ధ్రువీకరణ
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
                # క్వరీ లోపాలు సాధారణంగా క్లయింట్ లోపాలు అవుతాయి
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # టూల్-స్పెసిఫిక్ లోపాలను గమ్యస్థానంలో దాటించుము
            raise
        except Exception as e:
            # అనుకోని లోపాల కోసం సాధారణ క్యాచ్
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL ఇంజెక్షన్ గుర్తింపులో అమలు
        pass
        
    def _log_error(self, message, error):
        # లోపాలు నమోదు మీద అమలు
        pass
```

#### 3. పారామీటర్ ధృవీకరణ

ఎల్లప్పుడూ పార్థకత రహిత లేదా దురాశయపూరిత ఇన్‌పుట్‌ను నివారించేందుకు పారామీటర్లను పూర్తిగా ధృవీకరించండి.

```javascript
// విస్తృతమైన పారామితి ధృవీకరణతో JavaScript/TypeScript ఉదాహరణ
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
    
    // 2. పారామితి రకాలను ధృవీకరించండి
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
    
    // ధృవీకరించిన పారామితీల ఆధారంగా అమలు
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // మార్గ భద్రత తనిఖీ అమలు
    // ...
  }
}
```

### భద్రత అమలు ఉదాహరణలు

#### 1. ప్రామాణీకరణ మరియు అధికారప్రదానం

```java
// అథెంటికేషన్ మరియు అథరైజేషన్ తో జావా ఉదాహరణ
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
        // 1. అథెంటికేషన్ సందర్భం బయట తీయండి
        String authToken = request.getContext().getAuthToken();
        
        // 2. వినియోగదారుని అథెంటికేట్ చేయండి
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. నిర్దిష్ట ఆపరేషన్ కోసం అథరైజేషన్ తనిఖీ చేయండి
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. అథరైజ్డ్ ఆపరేషన్ తో కొనసాగించండి
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

## పరీక్షల ఉత్తమ అలవాట్లు

### 1. MCP టూల్స్ యూనిట్ టెస్టింగ్

ఎల్లప్పుడూ మీ టూల్స్‌ను ఒకటికొకటి పరీక్షించండి, బాహ్య ఆధారాలను మాక్ చేయండి:

```typescript
// టైప్‌స్క్రిప్ట్ సాధనం యూనిట్ టెస్ట్ యొక్క ఉదాహరణ
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // ఒక మాక్ వాతావరణ సేవను సృష్టించండి
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // మాక్ డిపెండెన్సీతో సాధనాన్ని సృష్టించండి
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
    
    // నిర్ధారించండి
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

### 2. సమగ్ర పరీక్ష

క్లయింట్ అభ్యర్థన‌ల నుండి సర్వర్ స్పంద‌న‌ల వరకూ మొత్తం ప్రవాహాన్ని పరీక్షించండి:

```python
# పython సమ్మిళిత పరీక్ష ఉదాహరణ
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # పరీక్ష సర్వర్ ప్రారంభించండి
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
        
        # స్పందనను నిర్ధారించండి
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # శుభ్రపరచండి
        await server.stop()
```

## ప్రదర్శన ఆప్టిమైజేషన్

### 1. క్యాషింగ్ వ్యూహాలు

ఆలస్యాన్ని తగ్గించడానికి మరియు వనరు వినియోగాన్ని తగ్గించడానికి తగిన విధంగా క్యాషింగ్ అమలు చేయండి:


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

#### 2. డిపెండెన్సీ ఇంజెక్షన్ మరియు టెస్ట్‌బిలిటీ

టూల్స్‌ను వారి డిపెండెన్సీలను కన్‌స్ట్రక్టర్ ఇంజెక్షన్ ద్వారా తీసుకునే విధంగా డిజైన్ చేయండి, తద్వారా అవి టెస్ట్ చేయదగినవి మరియు కాన్ఫిగర్ చేయదగినవి అవుతాయి:

```java
// డిపెండెన్సీ ఇంజెక్షన్ తో జావా ఉదాహరణ
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // డిపెండెన్సీలు కన్‌స్ట్రక్టర్ ద్వారా ఇంజెక్ట్ చేయబడతాయి
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

#### 3. కంపోజబుల్ టూల్స్

మరింత క్లిష్టమైన వర్క్‌ఫ్లోలను సృష్టించడానికి కలిసి కంపోజ్ చేయగలిగే టూల్స్‌ను డిజైన్ చేయండి:

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

### స్కీమా డిజైన్ ఉత్తమ ఆచారాలు

స్కీమా అనేది మోడల్ మరియు మీ టూల్ మధ్య ఒప్పందం. బాగా డిజైన్ చేసిన స్కీమాలు మెరుగైన టూల్ వాడుకను కలిగిస్తాయి.

#### 1. స్పష్టమైన పారామీటర్ వివరణలు

ప్రతి పారామీటర్‌కు వివరణాత్మక సమాచారాన్ని ఎప్పుడూ చేర్చండి:

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

#### 2. సబబు నిరోధనలు

తప్పైన ఇన్పుట్‌లను నివారించడానికి సరైన నిరోధనలు చేర్చండి:

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
    
    // ఎరుగుచేసిన ప్రాపర్టీ
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

#### 3. సమానమైన రిటర్న్ నిర్మాణాలు

ఫలితాలను మోడల్స్ సులభంగా అర్థం చేసుకునేలా మీ ప్రతిస్పందన నిర్మాణాలలో సాకార్యతను పాటించండి:

```python
async def execute_async(self, request):
    try:
        # అభ్యర్థన ప్రాసెస్ చేయండి
        results = await self._search_database(request.parameters["query"])
        
        # ఎప్పుడూ ఒక సంతులితమైన నిర్మాణాన్ని ఇించిన్చండి
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

### పొరపాటు నిర్వహణ

MCP టూల్స్ నమ్మకాస్పదంగా ఉండటానికి బలమైన పొరపాటు నిర్వహణ అవసరం.

#### 1. సౌమ్యమైన పొరపాటు నిర్వహణ

సరైన స్థాయిల్లో పొరపాట్లు నిర్వహించి సమాచారపూర్వక సందేశాలు ఇవ్వండి:

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

#### 2. నిర్మించబడిన పొరపాటు ప్రతిస్పందనలు

సాధ్యమైనప్పుడు నిర్మిత పొరపాటు సమాచారాన్ని తిరిగి ఇవ్వండి:

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
        
        // ఇతర తప్పిదాలను ToolExecutionExceptionగా తిరిగి త్రో చేయండి
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. రీట్రై తర్కం

పఠన- మాత్రమే కాల్స్ లేదా డౌన్‌స్ట్రీమ్ ఒప్పందం ఇప్పటికే ఐడెమ్పొటెంట్ అయిన ఆపరేషన్ల కోసం మాత్రమే సాధారణ రీట్రై తర్కాన్ని ఉపయోగించండి. ప్రభావవంతమైన ఆపరేషన్ల కోసం, అభ్యర్థన పంపిన తర్వాత టైమ్‌ఔట్ గమనార్హం కాదు. అధికారిక స్థితిని క్యాలిబ్రేట్ చేసి, మళ్ళీ అమలు చేసేముందు అదే స్థిరమైన ఆపరేషన్ కీలను పునఃపయోగించండి. 



[నమ్మకవంతమైన సైడ్కార్ తోడు పాఠం](./reliability-sidecars/README.md) చూడండి.

క్రింది పరిమిత రీట్రై లూప్ పఠన- కొరకు అనుకూలం:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # సెకన్లు
    
    while retry_count < max_retries:
        try:
            # చదవగలిగే బాహ్య API ను పిలవండి
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # ఘాతాంక చెల్లింపు తగ్గింపు
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # తాత్కాలికమైనది కాని లోపం, మళ్లీ ప్రయత్నించకండి
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### పనితీరు మెరుగుదల

#### 1. కాచింగ్

ఖర్చుతో కూడుకున్న ఆపరేషన్ల కోసం కాచింగ్ అమలు చేయండి:

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

#### 2. అసింక్రనస్ ప్రాసెసింగ్

I/O- బౌండ్ ఆపరేషన్ల కోసం అసింక్రనస్ ప్రోగ్రామింగ్ నమూనాలు ఉపయోగించండి:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // పరుగులో ఉండే ఆపరేషన్ల కోసం, ప్రాసెసింగ్ ID ని తక్షణమే తిరిగి ఇవ్వండి
        String processId = UUID.randomUUID().toString();
        
        // అసింక్రోనస్ ప్రాసెసింగ్ ప్రారంభించండి
        CompletableFuture.runAsync(() -> {
            try {
                // వరకు కొనసాగించే ఆపరేషన్‌ను జరపండి
                documentService.processDocument(documentId);
                
                // స్థితి నవీకరించండి (సాధారణంగా డేటాబేస్‌లో నిల్వ చేయబడుతుంది)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // ప్రాసెస్ IDతో తక్షణ స్పందనను తిరిగి ఇవ్వండి
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

#### 3. వనరు నియంత్రణ

ఓవర్‌లోడ్ నివారించడానికి వనరు నియంత్రణను అమలు చేయండి:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # సెకనుకి 5 అభ్యర్థనలను అనుమతించండి
            bucket_size=10        # 10 అభ్యర్థనల వరకు గట్టి విరామాలను అనుమతించండి
        )
    
    async def execute_async(self, request):
        # సాగదీయగలమా లేదా వేచి ఉండవలసిందేనా తనిఖీ చేయండి
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # వేచి ఉండడం చాలా ఎక్కువైతే
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # సరైన ఆలస్య సమయానికి వేచి ఉండండి
                await asyncio.sleep(delay)
        
        # ఒక టోకెన్‌ను వినియోగించి అభ్యర్థనతో కొనసాగండి
        self.rate_limiter.consume()
        
        # API‌ను కాల్ చేయండి
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
            
            # తదుపరి టోకెన్ లభించేదాకా సమయాన్ని గణించండి
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

### భద్రత ఉత్తమ ఆచారాలు

#### 1. ఇన్పుట్ తనిఖీలు

ఎప్పుడూ ఇన్పుట్ పారామీటర్లను పూర్తిగా పరిశీలించండి:

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

#### 2. అధికారం తనిఖీలు

సరైన అధికారం తనిఖీలను అమలు చేయండి:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // అభ్యర్థన నుండి వినియోగదారు సందర్భాన్ని పొందండి
    UserContext user = request.getContext().getUserContext();
    
    // వినియోగదారుడికి కావలసిన అనుమతులు ఉన్నాయో లేదో తనిఖీ చేయండి
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // నిర్దిష్ట వనరుల కోసం, ఆ వనరుకు ప్రాప్తి ఉందో చూసుకోండి
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // సాధన అమలు కొనసాగించండి
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
        
        # వినియోగదారుని డేటాను పొందండి
        user_data = await self.user_service.get_user_data(user_id)
        
        # స్పష్టంగా అభ్యర్థించబడినప్పుడల్లా మరియు అనుమతి లభించినప్పుడు మాత్రమే సున్నితమైన ఫీల్డ్స్‌ను వడపోత చేయండి
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # అభ్యర్థన సందర్భంలో అనుమతికి స్థాయిని తనిఖీ చేయండి
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # అసలు డేటాను మార్చకుండానే ఒక ప్రతిని సృష్టించండి
        redacted = user_data.copy()
        
        # ప్రత్యేకమైన సున్నితమైన ఫీల్డ్స్‌ను తొలగించండి
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # జటిలమైన సున్నితమైన డేటాను తొలగించండి
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP టూల్స్ కోసం పరీక్షల ఉత్తమ ఆచారాలు

సమగ్ర పరీక్షలు MCP టూల్స్ సరిగ్గా పనిచేస్తున్నాయో, అడ్డంకుల కేసులతో నిపుణులుగా వ్యవహరిస్తున్నాయో, మరియు వ్యవస్థలో మిగతావారితో సరిైన సమ్మిళనం కలిగి ఉందో నిర్ధారిస్తాయి.

### యూనిట్ టెస్టింగ్

#### 1. ప్రతి టూల్‌ను వేరుగా పరీక్షించండి

ప్రతి టూల్ యొక్క ఫంక్షనాలిటీకి దృష్టి పెట్టిన పరిక్షలును రూపొందించండి:

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

#### 2. స్కీమా నిర్ధారణ పరీక్ష

స్కీమాలు సరైనవి మరియు నిరోధనలను సరిగ్గా అమలు చేస్తున్నాయో పరీక్షించండి:

```java
@Test
public void testSchemaValidation() {
    // టూల్ ఉదాహరణని సృష్టించండి
    SearchTool searchTool = new SearchTool();
    
    // స్కీమాను పొందండి
    Object schema = searchTool.getSchema();
    
    // ధృవీకరణ కోసం స్కీమాను JSONకి మార్చండి
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // స్కీమా సరైన JSONSchema인지 ధృవీకరించండి
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // చెల్లుబాటు అయ్యే పారామితులను పరీక్షించండి
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // తప్పిపోయిన అవసరమైన పారామితిని పరీక్షించండి
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // తప్పు పారామితి రకం ని పరీక్షించండి
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. పొరపాటు నిర్వహణ పరీక్షలు

పొరపాటు పరిస్థితుల కోసం ప్రత్యేక పరీక్షలు చేయండి:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # ఏర్పాటుచేయండి
    tool = ApiTool(timeout=0.1)  # చాలా қыска టైమౌట్
    
    # టైమౌట్ అయ్యే అభ్యర్థనను మాక్ చేయండి
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # టైమౌట్ కంటే ఎక్కువ
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # చర్య & నిర్థారణ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # తప్పిద సందేశాన్ని గమనించండి
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # ఏర్పాటుచేయండి
    tool = ApiTool()
    
    # రేటు పరిమితి ఉన్న స్పందనను మాక్ చేయండి
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
        
        # చర్య & నిర్థారణ
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # తప్పుడు సందేశంలో రేటు పరిమితి సమాచారం ఉందని ధృవీకరించండి
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### సమ్మిళిత పరీక్ష

#### 1. టూల్ చైన్ పరీక్ష

ఆశించిన కాంబినేషన్లలో కలిసి పనిచేస్తున్న టూల్స్‌ను పరీక్షించండి:

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

పూర్తి టూల్ నమోదు మరియు అమలుతో MCP సర్వర్‌ను పరీక్షించండి:

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
        // చూసే ఎండ్‌పాయింట్‌ని పరీక్షించండి
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
        
        // అభ్యర్థన పంపించి ప్రతిస్పందనని నిర్ధారించండి
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // సరైన కాని టూల్ అభ్యర్థన సృష్టించండి
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // "b" పరామితి లేదు
        request.put("parameters", parameters);
        
        // అభ్యర్థన పంపించి లోపపు ప్రతిస్పందన‌ని నిర్ధారించండి
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. ఎండ్- టూ-ఎండ్ పరీక్ష

మోడల్ ప్రాంప్ట్ నుండి టూల్ అమల వరకు పూర్తి వర్క్‌ఫ్లోలను పరీక్షించండి:


```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # ఏర్పాటు చేయండి - MCP క్లయింట్ మరియు మాక్ మోడల్ సెట్ చేయండి
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # మాక్ మోడల్ స్పందనలు
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
    
    # మాక్ వాతావరణ సాధనం స్పందన
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

మీ MCP సర్వర్ ఎంత concurrency అభ్యర్థనలను నిర్వహించగలదో పరీక్షించండి:

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

తీవ్రమైన లోడ్ క్రింద సిస్టమ్‌ని పరీక్షించండి:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // స్ట్రెస్ టెస్ట్ కోసం JMeter సెటప్ చేయండి
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter టెస్ట్ ప్లాన్ కాన్ఫిగర్ చేయండి
    HashTree testPlanTree = new HashTree();
    
    // టెస్ట్ ప్లాన్, థ్రెడ్ గ్రూప్, శాంప్లర్లు మొదలైన వాటి సృష్టించండి
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // టూల్ ఎగ్జిక్యూషన్ కోసం HTTP శాంప్లర్ జోడించండి
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // లిసనర్లను జోడించండి
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

#### 3. మానిటరింగ్ మరియు ప్రొఫైలింగ్

దీర్ఘకాలిక పనితీరు విశ్లేషణ కోసం మానిటరింగ్ సెట్ చేయండి:

```python
# MCP సర్వర్ కోసం మానిటరింగ్ కాన్ఫిగర్ చేయండి
def configure_monitoring(server):
    # Prometheus మెట్రిక్స్ సెటప్ చేయండి
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
    
    # టైమింగ్ మరియు మెట్రిక్స్ రికార్డింగ్ కోసం మిడిల్‌వేర్ జోడించండి
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # మెట్రిక్స్ ఎండ్పాయింట్‌ను ఎక్స్‌పోజ్ చేయండి
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP వర్క్‌ఫ్లో డిజైన్ ప్యాటర్న్లు

బాగా రూపకల్పన చేసిన MCP వర్క్‌ఫ్లోలు సమర్ధత, నమ్మకదారితనం మరియు నిర్వహణ సౌలభ్యాన్ని మెరుగుపరుస్తాయి. అనుసరించాల్సిన ప్రధాన ప్యాటర్న్లు ఇక్కడ ఉన్నాయి:

### 1. టూల్స్ చైన్ ప్యాటర్న్

ఒకదాని తర్వాత ఒకటి అనుసంధానించే పద్దతిలో అనేక టూల్స్ కలపండి, ఇక్కడ ప్రతి టూల్ యొక్క అవుట్పుట్ తదుపరి టూల్ యొక్క ఇన్పుట్‌గా ఉంటుంది:

```python
# పైన్లను టూల్స్ ప్రయోగం అమలు
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # వరుసగా అమలు చేయవలసిన టూల్ పేర్ల జాబితా
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # ప్రతి టూల్ ను చైన్ లో అమలు చేయండి, ముందు ఫలితాన్ని పంపండి
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # ఫలితాన్ని నిల్వ చేసి తదుపరి టూల్ కు ఇన్‌పుట్ గా ఉపయోగించండి
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

### 2. డిస్పాచర్ ప్యాటర్న్

ఇన్పుట్ ఆధారంగా ప్రత్యేక టూల్స్ కు పంపిణీ చేసే కేంద్ర టూల్ ను ఉపయోగించండి:

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

### 3. సమాంతర ప్రాసెసింగ్ ప్యాటర్న్

సమర్ధత కోసం ఒకేసారి అనేక టూల్స్‌ను నడిపించండి:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // దశ 1: డేటాసెట్ మెటాడేటాను పొందండి (సింక్రనస్)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // దశ 2: బహుళ విశ్లేషణలను సమాంతరంగా ప్రారంభించండి
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
        
        // అన్ని సమాంతర పనులు పూర్తవ్వాలని కాపాడండి
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // పూర్తయేవరకు వేటపడండి
        
        // దశ 3: ఫలితాలను సంయోజించండి
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // దశ 4: సారాంశ నివేదికను తయారు చేయండి
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

### 4. లోపాలు పునరుద్ధరణ ప్యాటర్న్

టూల్ వైఫల్యాల కోసం సౌమ్యమైనFallbacks ని అమలు చేయండి:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # ముందుగా ప్రాథమిక పరిచయ పరికరాన్ని ప్రయత్నించండి
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # వైఫల్యాన్ని లాగ్ చేయండి
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # రెండవ పరికరాన్ని ఉపయోగించండి
            try:
                # fallback పరికరం కోసం పారామితులు మార్పిడి అవసరం కావచ్చు
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # రెండు పరికరాలు కూడా విఫలమయ్యాయి
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # ఈ అమలు నిర్దిష్ట పరికరాలపై ఆధారపడి ఉంటుంది
        # ఈ ఉదాహరణ కోసం, మేము అసలు పారామితులను ఇవ్వబోతున్నాం
        return params

# ఉదాహరణ వాడకం
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # ప్రాథమిక (చెల్లింపు) వాతావరణ API
        "basicWeatherService",    # fallback (ఉచితం) వాతావరణ API
        {"location": location}
    )
```

### 5. వర్క్‌ఫ్లో కంపోజిషన్ ప్యాటర్న్

సాధారణ వర్క్‌ఫ్లోలను కలిపి సంక్లిష్ట వర్క్‌ఫ్లోలను నిర్మించండి:

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

# MCP సర్వర్ల పరీక్ష: ఉత్తమ ప్రవర్తనలు మరియు టాప్ చిట్కాలు

## అవలోకనం

నమ్మదగిన, అధిక గుణాత్మక MCP సర్వర్లను అభివృద్ధి చేయడంలో పరీక్ష ఒక కీలకాంశం. ఈ గైడ్ యూనిట్ టెస్టులు నుండి ఇంటిగ్రేషన్ టెస్టులు మరియు ఎండ్-టు-ఎండ్ పరీక్షల వరకు MCP సర్వర్ల యొక్క అభివృద్ధి చక్రంలో అన్ని దశల్లో comprehensive ఉత్తమ పద్ధతులు మరియు చిట్కాలను అందిస్తుంది.

## MCP సర్వర్లకు పరీక్ష ముఖ్యమైనదే ఎందుకు

MCP సర్వర్లు AI మోడల్స్ మరియు క్లయింట్ అనువర్తనాల మధ్య ముఖ్యమైన మిడ్‌లేయర్ గా పనిచేస్తాయి. సంపూర్ణమైన పరీక్ష:

- ఉత్పత్తి వాతావరణాలలో నమ్మకదారితనం
- అభ్యర్థనలు మరియు ప్రతిస్పందనలను ఖచ్చితంగా నిర్వహణ
- MCP స్పెసిఫికేషన్ల సరైన అమలును
- వైఫల్యాల మరియు హద్దుల కేసులకు వ్యతిరేక నిరోధకత
- వివిధ లోడ్ల క్రింద స్థిరమైన పనితీరు

## MCP సర్వర్ల కోసం యూనిట్ పరీక్ష

### యూనిట్ పరీక్ష (బేస్)

యూనిట్ పరీక్షలు మీ MCP సర్వర్ యొక్క వ్యక్తిగత భాగాలను వేరుగా నిర్ధారిస్తాయి.

#### ఏమి పరీక్షించాలి

1. **రిసోర్స్ హ్యాండ్లర్స్**: ప్రతి రిసోర్స్ హ్యాండ్లర్ లాజిక్ ని స్వతంత్రంగా పరీక్షించండి
2. **టూల్ అమలులు**: వివిధ ఇన్పుట్‌లతో టూల్ ప్రవర్తనను నిర్ధారించండి
3. **ప్రాంప్ట్ టెంప్లేట్లు**: ప్రాంప్ట్ టెంప్లేట్లు సరిగ్గా ప్రదర్శిస్తున్నాయా తెలియజేయండి
4. **స్కీమా ధ్రువీకరణ**: పారామీటర్ ధ్రువీకరణ లాజిక్ ని పరీక్షించండి
5. **లోపాలను నిర్వహణ**: చెల్లని ఇన్పుట్స్ కి లోపపు ప్రతిస్పందనలను నిర్ధారించండి

#### యూనిట్ పరీక్షకు ఉత్తమ పద్ధతులు

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
# పైథాన్‌లో కేలిక్యులేటర్ టూల్ కోసం ఉదాహరణ యూనిట్ టెస్ట్
def test_calculator_tool_add():
    # ఏర్పాటు చేయండి
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # చర్య తీసుకోండి
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # నిర్ధారించండి
    assert result["value"] == 12
```

### ఇంటిగ్రేషన్ పరీక్ష (మధ్యస్థర)

ఇంటిగ్రేషన్ పరీక్షలు MCP సర్వర్ భాగాల మధ్య పరస్పర చర్యలను నిర్ధారిస్తాయి.

#### ఏమి పరీక్షించాలి

1. **సర్వర్ ఆరంభత**: వివిధ కాన్ఫిగరేషన్లతో సర్వర్ స్టార్టప్‌ను పరీక్షించండి
2. **రూట్ రిజిస్ట్రేషన్**: అన్ని ఎండ్పాయింట్లు సరిగా నమోదు అయివున్నాయా చూడండి
3. **అభ్యర్థన ప్రాసెస్**: పూర్తి అభ్యర్థన-ప్రతిస్పందన చక్రాన్ని పరీక్షించండి
4. **లోప వ్యాప్తి**: భాగాల మధ్య లోపాలు సరైన విధంగా నిర్వహించబడుతున్నాయా ధృవీకరించండి
5. **అథెంటికేషన్ & ఆమోదం**: భద్రతా యంత్రాంగాలను పరీక్షించండి

#### ఇంటిగ్రేషన్ పరీక్షకు ఉత్తమ పద్ధతులు

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

### ఎండ్-టు-ఎండ్ పరీక్ష (శ్రేష్ఠ స్థరం)

ఎండ్-టు-ఎండ్ పరీక్షలు క్లయింట్ నుండి సర్వర్ వరకు పూర్తి సిస్టమ్ ప్రవర్తనను నిర్ధారిస్తాయి.

#### ఏమి పరీక్షించాలి

1. **క్లయింట్-సర్వర్ కమ్యూనికేషన్**: పూర్తి అభ్యర్థన-ప్రతిస్పందన చక్రాలను పరీక్షించండి
2. **వాస్తవ క్లయింట్ SDKలు**: నిజమైన క్లయింట్ అమలులతో పరీక్షించండి
3. **లోడ్ క్రింద పనితీరు**: ఒకేసారి అనేక concurrency అభ్యర్థనలతో ప్రవర్తనను నిర్ధారించండి
4. **లోప పునరుద్ధరణ**: వైఫల్యాల నుండి సిస్టమ్ పునరుద్ధరణను పరీక్షించండి

5. **దీర్ఘకాలం నడిచే ఆపరేషన్లు**: స్ట్రీమింగ్ మరియు దీర్ఘకాల ఆపరేషన్ల నిర్వహణను ధృవీకరించండి

#### E2E టెస్టింగ్ కోసం ఉత్తమ ఆచారాలు

```typescript
// TypeScriptలో క్లయింట్‌తో ఉదాహరణ E2E పరీక్ష
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // టెస్ట్ వాతావరణంలో సర్వర్ ప్రారంభించండి
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // చర్య
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // నిర్ధారణ చేయండి
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP టెస్టింగ్ కోసం మాక్ చేయడం వ్యూహాలు

పరీక్షల సమయంలో భాగాలను విభజించడానికి మాక్ చేయడం అనివార్యం.

### మాక్ చేయాల్సిన భాగాలు

1. **బాహ్య AI మోడల్స్**: పూర్వనిర్ధారిత పరీక్షల కోసం మోడల్ ప్రతిస్పందనలను మాక్ చేయండి
2. **బాహ్య సర్వీసులు**: API ఆధారిత (డేటాబేసులు, మూడవ పార్టీ సర్వీసులు) మాక్ చేయండి
3. **ప్రామాణీకరణ సర్వీసులు**: గుర్తింపు ప్రదాతలను మాక్ చేయండి
4. **వనరులు ప్రదాతలు**: ఖరీదైన వనరుల నిర్వహణలను మాక్ చేయండి

### ఉదాహరణ: AI మోడల్ ప్రతిస్పందన మాక్ చేయడం

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
# unittest.mock తో పైథాన్ ఉదాహరణ
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # మాక్‌ను కాన్ఫిగర్ చేయండి
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # టెస్ట్‌లో మాక్‌ని ఉపయోగించండి
    server = McpServer(model_client=mock_model)
    # టెస్ట్‌తో కొనసాగండి
```

## పనితీరు పరీక్ష

ఉత్పత్తి MCP సర్వర్ల కోసం పనితీరు పరీక్ష చాలా ముఖ్యമാണ്.

### ఏది కొలవాలి

1. **విలంబం**: అభ్యర్థనలకు స్పందించే సమయం
2. **థ్రూపుట్**: సెకనుకి నిర్వహించిన అభ్యర్థనలు
3. **వనరు వినియోగం**: CPU, మెమరీ, నెట్‌వర్క్ వినియోగం
4. **సమాంతర నిర్వహణ**: సమాంతర అభ్యర్థనల క్రింద ప్రవర్తనలు
5. **స్కేలింగ్ లక్షణాలు**: లోడ్ పెరిగేకొద్దీ పనితీరు

### పనితీరు పరీక్షకు ఉపయోగించే టూల్స్

- **k6**: ఓపెన్-సోర్స్ లోడ్ పరీక్ష టూల్
- **JMeter**: సమగ్ర పనితీరు పరీక్షా పరికరం
- **Locust**: పైథాన్ ఆధారిత లోడ్ పరీక్ష
- **Azure Load Testing**: క్లౌడ్ ఆధారిత పనితీరు పరీక్ష

### ఉదాహరణ: k6 తో ప్రాథమిక లోడ్ పరీక్ష

```javascript
// MCP సర్వర్ లోడ్ పరీక్ష కోసం k6 స్క్రిప్ట్
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 వర్చువల్ యూజర్లు
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

## MCP సర్వర్ల కోసం పరీక్ష ఆటోమేషన్

మీ పరీక్షలను ఆటోమేట్ చేయడం స్థిరమైన నాణ్యత మరియు వేగవంతమైన ఫీడ్బ్యాక్ లూక్స్‌ను నిర్ధారిస్తుంది.

### CI/CD సమన్వయం

1. **పుల్ రిక్వెస్ట్స్‌పై యూనిట్ టెస్ట్‌లు నడపండి**: కోడ్ మార్పులు ప్రస్తుతం ఉన్న ఫంక్షనాలిటీని బ్రేక్ చేయకూడదు అని నిర్ధారించండి
2. **స్టేజింగ్‌లో ఇంటిగ్రేషన్ టెస్ట్‌లు**: ప్రీ-ప్రొడక్షన్ పరిసరాలలో ఇంటిగ్రేషన్ పరీక్షలు నిర్వహించండి
3. **పనితీరు బ్యాస్లైన్స్**: రిగ్రెషన్లను గుర్తించడానికి పనితీరు ప్రమాణాలను నిర్వహించండి
4. **సెక్యూరిటీ స్కాన్లు**: పైప్లైన్‌లో భాగంగా సెక్యూరిటీ పరీక్షలను ఆటోమేట్ చేయండి

### ఉదాహరణ CI పైప్లైన్ (GitHub యాక్షన్స్)

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

## MCP స్పెసిఫికేషన్‌తో అనుగుణమైన పరీక్ష

మీ సర్వర్ MCP స్పెసిఫికేషన్‌ను సరిగ్గా అమలు చేస్తున్నదా అని నిర్ధారించండి.

### ముఖ్య అనుగుణత ప్రాంతాలు

1. **API ఎండ్‌పాయింట్లు**: అవసరమైన ఎండ్‌పాయింట్లను పరీక్షించండి (/resources, /tools, మొదలైనవి)
2. **అభ్యర్థన/స్పందన ఫార్మాట్**: స్కీమా అనుగుణతను ధృవీకరించండి
3. **పొరపాటు కోడ్స్**: వివిధ సందర్భాలకు సరైన స్థితి కోడ్లను నిర్ధారించండి
4. **కంటెంట్ రకం**: వేరే వేరే కంటెంట్ రకాల నిర్వహణను పరీక్షించండి
5. **ప్రామాణీకరణ ఫ్లో**: స్పెక్స్‌కు అనుగుణమైన ఆథ్ మెకానిజమ్లను ధృవీకరించండి

### అనుగుణత పరీక్షా సూట్

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

## సమర్థవంతమైన MCP సర్వర్ టెస్టింగ్ కోసం టాప్ 10 సూచనలు

1. **పరికరం నిర్వచనాలను విడిగా పరీక్షించండి**: పరికరం లాజిక్ నుండి స్వతంత్రంగా స్కీమా నిర్వచనాలను ధృవీకరించండి
2. **పారామెటరైజ్డ్ టెస్ట్‌లు ఉపయోగించండి**: విభిన్న ఇన్‌పుట్లతో పరికరాలను పరీక్షించండి, సరిహద్దుల కేసులు సహా
3. **పొరపాటు స్పందనలను తనిఖీ చేయండి**: అన్ని సాధ్యమైన పొరపాటు పరిస్థితుల కోసం సరైన దోష నిర్వహణను ధృవీకరించండి
4. **అధికారం లాజిక్‌ను పరీక్షించండి**: వేరే వేరే యూజర్ పాత్రల కోసం సరైన యాక్సెస్ నియంత్రణను నిర్ధారించండి
5. **పరీక్ష కవచాన్ని మానిటర్ చేయండి**: ముఖ్య మార్గ కోడ్‌ను ఎక్కువ కవర్ చేయాలని లక్ష్యం పెట్టుకోండి
6. **స్ట్రీమింగ్ స్పందనలను పరీక్షించండి**: స్ట్రీమింగ్ కంటెంట్ సరైన నిర్వహణను ధృవీకరించండి
7. **నెట్‌వర్క్ సమస్యలను సిమ్యులేట్ చేయండి**: తక్కువ నెట్‌వర్క్ పరిస్థితుల క్రింద ప్రవర్తనను పరీక్షించండి
8. **వనరు పరిమితులను పరీక్షించండి**:ాట క్వాటాలు లేదా రేటు పరిమితులు చేరుకున్నప్పుడు ప్రవర్తనను ధృవీకరించండి
9. **రిస్గ్రెషన్ టెస్ట్‌లను ఆటోమేట్ చేయండి**: ప్రతి కోడ్ మార్పుపై నడిచే సూట్‌ను నిర్మించండి
10. **పరీక్ష కేసులను డాక్యుమెంట్ చేయండి**: పరీక్ష సందర్భాల యొక్క స్పష్టమైన డాక్యుమెంటేషన్‌ని నిర్వహించండి

## సాధారణ పరీక్షలో తప్పులు

- **సంతోష మార్గ పరీక్షలపై అధిక ఆధారపడి ఉండటం**: పొరపాటు కేసులను పూర్తిగా పరీక్షించండి
- **పనితీరు పరీక్షలను నిర్లక్ష్యం చేయటం**: ఉత్పత్తిపై ప్రభావం చూపించే ముందే బాట్లెనెక్స్ గుర్తించండి
- **విభజనలో మాత్రమే పరీక్షించడం**: యూనిట్, ఇంటిగ్రేషన్, మరియు E2E పరీక్షలను కలపండి
- **పూర్తిగా API కవచం లేకపోవడం**: అన్ని ఎండ్‌పాయింట్లు మరియు లక్షణాలు పరీక్షించబడినట్లు నిర్ధారించండి
- **అసంగత పరీక్షా పరిసరాలు**: స్థిరమైన పరీక్షా పరిసరాలను నిర్ధారించడానికి కంటైనర్లను ఉపయోగించండి

## నిరూపణ

విశ్లేషణాత్మక పరీక్షా వ్యూహం నమ్మకమైన, ఉన్నత నాణ్యత MCP సర్వర్ల అభివృద్ధికి అవసరం. ఈ మార్గదర్శకంలో వివరించిన ఉత్తమ ఆచారాలు మరియు సూచనలను అమలు చేస్తే, మీ MCP అమలు అత్యున్నత నాణ్యత, నమ్మక్యత మరియు పనితీరు ప్రమాణాలను చేరుకుంటాయని నిర్ధారించవచ్చు.


## ముఖ్యమైన తీసుకోవాల్సిన పాఠాలు

1. **పరికరం రూపకల్పన**: ఒక్క బాధ్యత సూత్రాన్ని అనుసరించండి, డిపెండెన్సీ ఇంజెక్షన్ ఉపయోగించండి, మరియు కంపోజబిలిటీ కోసం డిజైన్ చేయండి
2. **స్కీమా రూపకల్పన**: స్పష్టమైన, బాగా డాక్యుమెంట్ చేసిన స్కీమాలను సరైన ప్రమాణాల్తో సృష్టించండి
3. **పొరపాటు నిర్వహణ**: సున్నితమైన పొరపాటు నిర్వహణ, నిర్మిత పొరపాటు ప్రతిస్పందనలు, మరియు ఫలితాన్ని గుర్తించే మళ్లీ ప్రయత్నించే లాజిక్ అమలు చేయండి
   
4. **పనితీరు**: కాషింగ్, అసింక్రోనస్ ప్రాసెసింగ్ మరియు వనరు నియంత్రణను ఉపయోగించండి
5. **సెక్యూరిటీ**: గాఢ ఇన్‌పుట్ పరిశీలన, అధీకారం తనఖీలు, మరియు సున్నితమైన డేటా నిర్వహణను వర్తించండి
6. **పరీక్ష**: సమగ్ర యూనిట్, ఇంటిగ్రేషన్, మరియు ఎండ్-టు-ఎండ్ పరీక్షలను సృష్టించండి
7. **వర్క్‌ఫ్లో నమూనాలు**: చైన్స్, డిస్పాచర్లు, మరియు సమాంతర ప్రాసెసింగ్ వంటి స్థాపిత నమూనాలను వర్తించండి

## వ్యాయామం

డాక్యుమెంట్ ప్రాసెసింగ్ సిస్టమ్ కోసం MCP పరికరం మరియు వర్క్‌ఫ్లో రూపకల్పన చేయండి:

1. బహుళ ఫార్మాట్లలో డాక్యుమెంట్లను స్వీకరిస్తుంది (PDF, DOCX, TXT)
2. డాక్యుమెంట్ల నుండి టెక్స్ట్ మరియు ముఖ్య సమాచారాన్ని ఎగ Zhu
3. డాక్యుమెంట్లను రకం మరియు అంశం ఆధారంగా వర్గీకరిస్తుంది
4. ప్రతి డాక్యుమెంట్ యొక్క సమరీను సృష్టిస్తుంది

పరికర స్కీమాలు, పొరపాటు నిర్వహణ, మరియు ఈ పరిస్థితికి ఉత్తమమైన వర్క్‌ఫ్లో నమూనాను అమలు చేయండి. మీరు ఈ అమలు ఎలా పరీక్షిస్తారో పరిగణించండి.

## వనరులు 

1. నేటి అభివృద్ధులను అప్‌డేట్‌గా ఉండటానికి [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) లో MCP కమ్యూనిటీకి చేరండి 
2. ఓపెన్-సోర్స్ [MCP ప్రాజెక్టులలో](https://github.com/modelcontextprotocol) సహకారం చేయండి
3. మీ స్వంత సంస్థలో AI ప్రోగ్రామ్లలో MCP సిద్దాంతాలను వర్తించండి
4. మీ పరిశ్రమకు ప్రత్యేకత కలిగిన MCP అమలులను అన్వేషించండి. 
5. మల్టీ-మోడల్ సమన్వయం లేదా ఎంటర్ప్రైజ్ అప్లికేషన్ సమన్వయం వంటి MCP అంశాలపై అధునాతన కోర్సులు తీసుకోవడాన్ని పరిగణించండి.
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) ద్వారా నేర్చుకున్న సిద్దాంతాలతో మీ స్వంత MCP పరికరాలు మరియు వర్క్‌ఫ్లోలు నిర్మించడంలో ప్రయోగం చేయండి  

## తరువాత ఏమిటి

తరువాత: [కేస్ స్టడీస్](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
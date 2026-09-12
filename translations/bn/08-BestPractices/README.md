# MCP উন্নয়নের সেরা অনুশীলনসমূহ

[![MCP Development Best Practices](../../../translated_images/bn/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

## ওভারভিউ

এই পাঠটি MCP সার্ভার এবং বৈশিষ্ট্যগুলি উৎপাদন পরিবেশে উন্নয়ন, পরীক্ষণ এবং মোতায়েনের উন্নত সেরা অনুশীলনগুলোর উপর গুরুত্বারোপ করে। MCP ইকোসিস্টেমগুলি যেমন জটিলতা এবং গুরুত্ব বাড়ছে, প্রতিষ্ঠিত নকশাগুলো অনুসরণ করা নির্ভরযোগ্যতা, রক্ষণাবেক্ষণযোগ্যতা এবং আন্তঃপরিচালনক্ষমতা নিশ্চিত করে। এই পাঠ বাস্তব MCP বাস্তবায়ন থেকে প্রাপ্ত কার্যকরী জ্ঞান সংহত করে, যা আপনাকে কার্যকর সংস্থান, প্রম্পট এবং সরঞ্জাম সহ শক্তিশালী, দক্ষ সার্ভার তৈরি করতে গাইড করে।

## শেখার উদ্দেশ্য

এই পাঠ শেষ হওয়ার পরে, আপনি সক্ষম হবেন:

- MCP সার্ভার এবং ফিচার ডিজাইনে ইন্ডাস্ট্রি সেরা অনুশীলন প্রয়োগ করা
- MCP সার্ভারের জন্য ব্যাপক পরীক্ষণ কৌশল তৈরি করা
- জটিল MCP অ্যাপ্লিকেশনগুলোর জন্য দক্ষ, পুনর্ব্যবহারযোগ্য ওয়ার্কফ্লো প্যাটার্ন ডিজাইন করা
- MCP সার্ভারে সঠিক ত্রুটি হ্যান্ডলিং, লগিং, এবং পর্যবেক্ষণক্ষমতা প্রয়োগ করা
- পারফরম্যান্স, সিকিউরিটি এবং রক্ষণাবেক্ষণযোগ্যতার জন্য MCP বাস্তবায়নগুলি অপ্টিমাইজ করা

## MCP মূল নীতি

নির্দিষ্ট বাস্তবায়ন অনুশীলনে ডুব দেওয়ার আগে, কার্যকর MCP উন্নয়ন নির্দেশ করে এমন মূল নীতিগুলো বুঝা গুরুত্বপূর্ণ:

১. **স্ট্যান্ডার্ডাইজড কমিউনিকেশন**: MCP এর ভিত্তি হিসেবে JSON-RPC 2.0 ব্যবহৃত হয়, যা সমস্ত বাস্তবায়নে অনুরোধ, প্রতিক্রিয়া, এবং ত্রুটি হ্যান্ডলিংয়ের জন্য একটি সঙ্গতিপূর্ণ ফরম্যাট প্রদান করে।

২. **ইউজার-কেন্দ্রিক ডিজাইন**: সর্বদা ব্যবহারকারীর সম্মতি, নিয়ন্ত্রণ এবং স্বচ্ছতাকে MCP বাস্তবায়নে অগ্রাধিকার দিন।

৩. **নিরাপত্তা প্রথমে**: প্রমাণীকরণ, অনুমোদন, যাচাইকরণ, এবং রেট সীমাবদ্ধকরণসহ শক্তিশালী নিরাপত্তা ব্যবস্থা প্রয়োগ করুন।

৪. **মডুলার আর্কিটেকচার**: আপনার MCP সার্ভারগুলো মডুলার পদ্ধতিতে ডিজাইন করুন, যেখানে প্রতিটি টুল এবং সংস্থানের একটি স্পষ্ট, কেন্দ্রীভূত উদ্দেশ্য থাকে।

৫. **স্পষ্ট স্টেট**: MCP `2026-07-28` প্রোটোকল স্তরে স্টেটলেস। যখন একটি ওয়ার্কফ্লোতে ক্রস-কলে স্টেট প্রয়োজন হয়, তখন স্পষ্ট হ্যান্ডেল বা টেকসই অ্যাপ্লিকেশন স্টেট দ্বারা সমর্থিত সাধারণ টুল আর্গুমেন্ট ব্যবহার করুন।
   
   

## অফিসিয়াল MCP সেরা অনুশীলনসমূহ

নিম্নলিখিত সেরা অনুশীলনসমূহ অফিসিয়াল মডেল কনটেক্সট প্রোটোকল ডকুমেন্টেশন থেকে নেওয়া হয়েছে:

### নিরাপত্তা সেরা অনুশীলনসমূহ

১. **ব্যবহারকারীর সম্মতি এবং নিয়ন্ত্রণ**: ডেটা অ্যাক্সেস বা অপারেশন করার আগে সর্বদা স্পষ্ট ব্যবহারকারী সম্মতি চাইুন। কোন ডেটা শেয়ার করা হবে এবং কোন ক্রিয়াসমূহ অনুমোদিত তা স্পষ্ট নিয়ন্ত্রণ প্রদান করুন।

২. **ডেটা গোপনীয়তা**: শুধুমাত্র স্পষ্ট সম্মতি নিয়ে ব্যবহারকারী ডেটা প্রকাশ করুন এবং যথাযথ এক্সেস নিয়ন্ত্রণ দিয়ে তা রক্ষা করুন। অনুমোদন ছাড়া ডেটা স্থানান্তর প্রতিরোধ করুন।

৩. **টুল সুরক্ষা**: কোনও টুল আহ্বান করার আগে স্পষ্ট ব্যবহারকারী সম্মতি চাইুন। ব্যবহারকারীরা প্রতিটি টুলের কার্যকারিতা বোঝে তা নিশ্চিত করুন এবং শক্তিশালী নিরাপত্তা সীমান্ত বজায় রাখুন।

৪. **টুল অনুমতি নিয়ন্ত্রণ**: প্রতিটি অনুরোধ এবং অনুমোদন প্রসঙ্গের জন্য কোন টুল ব্যবহার করা যেতে পারে তা কনফিগার করুন, নিশ্চিত করুন শুধুমাত্র স্পষ্টভাবে অনুমোদিত টুলই অ্যাক্সেসযোগ্য।
   
   

৫. **প্রমাণীকরণ**: টুল, সংস্থান, অথবা সংবেদনশীল অপারেশনে প্রোপার প্রমাণীকরণ প্রয়োজন, যা API কী, OAuth টোকেন বা অন্যান্য নিরাপদ প্রমাণীকরণ পদ্ধতি ব্যবহার করে।

৬. **প্যারামিটার যাচাই**: সমস্ত টুল আহ্বানের জন্য যাচাই প্রয়োগ করুন যাতে খারাপ বা ক্ষতিকর ইনপুট টুল বাস্তবায়নে পৌঁছাতে না পারে।

৭. **রেট সীমাবদ্ধকরণ**: সার্ভার সংস্থান ব্যবহারে অপব্যবহার প্রতিরোধ এবং ন্যায্য ব্যবহার নিশ্চিত করতে রেট সীমাবদ্ধকরণ প্রয়োগ করুন।

### বাস্তবায়ন সেরা অনুশীলনসমূহ

১. **ক্ষমতা দর-কষাকষি**: সমর্থিত প্রোটোকল সংস্করণ এবং সক্ষমতাগুলোর জন্য দর-কষাকষি করুন। MCP `2026-07-28` তে, প্রতিটি অনুরোধ স্ব-সঙ্গত এবং `server/discover` ব্যবহার করতে পারে; পুরাতন সংস্করণগুলি ইনিশিয়ালাইজেশন হ্যান্ডশেক ব্যবহার করে।
   
   

২. **টুল ডিজাইন**: একক কাজ ভালোভাবে করা কেন্দ্রীভূত টুল তৈরি করুন, পরিবর্তে বহু বিষয় সামলানো মনোলিথিক টুল না।

৩. **ত্রুটি হ্যান্ডলিং**: মানকৃত ত্রুটি বার্তা এবং কোড ব্যবহার করুন যা সমস্যা নির্ণয়ে সাহায্য করে, ব্যর্থতাকে সুশৃঙ্খলভাবে হ্যান্ডল করে এবং কার্যকর প্রতিক্রিয়া প্রদান করে।

৪. **পর্যবেক্ষণক্ষমতা**: stdio ডায়াগনস্টিকের জন্য `stderr` ব্যবহার করুন এবং স্ট্রাকচার্ড পর্যবেক্ষণক্ষমতার জন্য OpenTelemetry ব্যবহার করুন। MCP লগিং ফিচার `2026-07-28` স্পেসিফিকেশনে ডিপ্রিকেটেড।
   
   

৫. **প্রগতি ট্র্যাকিং**: দীর্ঘ সময় চালিত অপারেশনের জন্য, প্রতিক্রিয়াশীল ইউজার ইন্টারফেস সক্ষম করতে প্রগতি আপডেট রিপোর্ট করুন।

৬. **অনুরোধ বাতিলকরণ**: ক্লায়েন্টদের এমন অনুরোধ বাতিল করার অনুমতি দিন যা আর প্রয়োজন নেই বা অনেক সময় নিচ্ছে।

## অতিরিক্ত রেফারেন্স

MCP সেরা অনুশীলন সম্পর্কে সর্বশেষ তথ্যের জন্য দেখুন:

- [MCP ডকুমেন্টেশন](https://modelcontextprotocol.io/)
- [MCP স্পেসিফিকেশন (2026-07-28)][mcp-2026-spec]
- [পূর্ববর্তী MCP স্পেসিফিকেশন (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP টাস্কস এক্সটেনশন][mcp-tasks-extension]
- [GitHub রিপোজিটরি](https://github.com/modelcontextprotocol)
- [নিরাপত্তা সেরা অনুশীলন](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP টপ ১০](https://microsoft.github.io/mcp-azure-security-guide/) - নিরাপত্তা ঝুঁকি এবং প্রতিকার
- [MCP সিকিউরিটি সামিট ওয়ার্কশপ (শেরপা)](https://azure-samples.github.io/sherpa/) - হাতে কলমে নিরাপত্তা প্রশিক্ষণ

### নির্ভরযোগ্যতা সহায়ক পাঠ

জেনেরিক রিট্রাই লুপ সেই সব টুলের জন্য বিপজ্জনক যা টিকিট, পেমেন্ট, মেসেজ, ডিপ্লয়মেন্ট অথবা অন্য বাস্তবসম্মত প্রভাব তৈরি করে। প্রভাব.Commit করার পর প্রতিক্রিয়া হারাতে পারে।
   
   

নির্ভরযোগ্যতা সহায়ক পাঠ ব্যবহার করুন,
[MCP টুলের জন্য নিরাপদ রিট্রাই: একটি নির্ভরযোগ্যতা সাইডকার প্যাটার্ন][reliability-sidecar],
স্থিতিশীল অপারেশন কী, ডুপ্লিকেট এডমিশন, চেকপয়েন্টিং, পুনর্মিলন, প্রমাণ স্তর এবং ব্যর্থতা ইনজেকশন শিখতে।
   

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## প্রায়োগিক বাস্তবায়ন উদাহরণসমূহ

### টুল ডিজাইন সেরা অনুশীলনসমূহ

#### ১. একক দায়িত্ব নীতি

প্রতিটি MCP টুলের একটি সুস্পষ্ট, কেন্দ্রীভূত উদ্দেশ্য থাকা উচিত। বহুবিধ সমস্যার সমাধান করার জন্য মনোলিথিক টুল তৈরি করার পরিবর্তে নির্দিষ্ট কাজগুলোতে পারদর্শী বিশেষায়িত টুল উন্নয়ন করুন।

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

#### ২. সঙ্গতিপূর্ণ ত্রুটি হ্যান্ডলিং

তথ্যবহুল ত্রুটি বার্তা এবং উপযুক্ত পুনরুদ্ধার প্রক্রিয়া সহ শক্তিশালী ত্রুটি হ্যান্ডলিং বাস্তবায়ন করুন।

```python
# পূর্ণাঙ্গ ত্রুটি হ্যান্ডলিং সহ পাইথন উদাহরণ
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # পরামিতি যাচাই
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # নিরাপত্তা যাচাই
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # টাইমআউট সহ ডাটাবেস অপারেশন
                async with timeout(10):  # ১০ সেকেন্ড টাইমআউট
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # সংযোগ ত্রুটি অস্থায়ী হতে পারে
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # কুয়েরি ত্রুটি সম্ভবত ক্লায়েন্ট ত্রুটি
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # টুল-নির্দিষ্ট ত্রুটিগুলো পার হতে দিন
            raise
        except Exception as e:
            # অপ্রত্যাশিত ত্রুটির জন্য ধরা-পড়া
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQL ইনজেকশন সনাক্তকরণের বাস্তবায়ন
        pass
        
    def _log_error(self, message, error):
        # ত্রুটি লগিং বাস্তবায়ন
        pass
```

#### ৩. প্যারামিটার যাচাই

সর্বদা প্যারামিটারগুলি সম্পূর্ণরূপে যাচাই করুন যাতে খারাপ বা ক্ষতিকর ইনপুট প্রতিরোধ করা যায়।

```javascript
// JavaScript/TypeScript উদাহরণ বিস্তারিত পরামিতি যাচাই সহ
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
    // 1. পরামিতি উপস্থিতি যাচাই করুন
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. পরামিতি প্রকার যাচাই করুন
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. পরামিতি মান যাচাই করুন
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. লেখার অপারেশনের জন্য কন্টেন্ট উপস্থিতি যাচাই করুন
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. পাথ নিরাপত্তা যাচাই
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // যাচাই করা পরামিতির উপর ভিত্তিক বাস্তবায়ন
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // পাথ নিরাপত্তা যাচাইয়ের বাস্তবায়ন
    // ...
  }
}
```

### নিরাপত্তা বাস্তবায়ন উদাহরণসমূহ

#### ১. প্রমাণীকরণ এবং অনুমোদন

```java
// প্রমাণীকরণ এবং অনুমোদনের সাথে জাভা উদাহরণ
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // ডিপেন্ডেন্সি ইনজেকশন
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
        // 1. প্রমাণীকরণ প্রসঙ্গ বের করুন
        String authToken = request.getContext().getAuthToken();
        
        // 2. ব্যবহারকারী প্রমাণীকরণ করুন
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. নির্দিষ্ট অপারেশনের জন্য অনুমোদন পরীক্ষা করুন
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. অনুমোদিত অপারেশন সঙ্গে এগিয়ে যান
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

#### ২. রেট সীমাবদ্ধকরণ

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

## পরীক্ষণ সেরা অনুশীলনসমূহ

### ১. MCP টুলের ইউনিট টেস্টিং

সর্বদা আপনার টুলগুলো আলাদাভাবে পরীক্ষা করুন, বাহ্যিক নির্ভরশীলতাগুলো মকিং করে:

```typescript
// TypeScript এর টুল ইউনিট টেস্টের উদাহরণ
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // একটি মক ওয়েদার সার্ভিস তৈরি করুন
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // মক ডিপেন্ডেন্সি সহ টুল তৈরি করুন
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // সাজানো
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // কার্যকর করা
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // নিশ্চিত করা
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // সাজানো
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // কার্যকর করা ও নিশ্চিত করা
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### ২. ইন্টিগ্রেশন পরীক্ষণ

ক্লায়েন্ট অনুরোধ থেকে সার্ভার প্রতিক্রিয়া পর্যন্ত পূর্ণ প্রবাহ পরীক্ষা করুন:

```python
# পাইথন ইন্টিগ্রেশন টেস্ট উদাহরণ
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # একটি টেস্ট সার্ভার শুরু করুন
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # একটি ক্লায়েন্ট তৈরি করুন
        client = McpClient("http://localhost:5000")
        
        # টুল ডিসকভারি পরীক্ষা করুন
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # টুল কার্যকরীতা পরীক্ষা করুন
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # প্রতিক্রিয়া যাচাই করুন
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # পরিষ্কার করুন
        await server.stop()
```

## পারফরম্যান্স অপ্টিমাইজেশন

### ১. ক্যাশিং কৌশলসমূহ

বিলম্ব এবং সংস্থান ব্যবহারে হ্রাস করার জন্য উপযুক্ত ক্যাশিং প্রয়োগ করুন:


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

#### ২. ডিপেন্ডেন্সি ইনজেকশন এবং টেস্টেবিলিটি

টুলগুলোকে তাদের ডিপেন্ডেন্সি কনস্ট্রাক্টর ইনজেকশনের মাধ্যমে গ্রহণ করার জন্য ডিজাইন করুন, যাতে সেগুলো টেস্টযোগ্য এবং কনফিগারযোগ্য হয়:

```java
// ডিপেন্ডেন্সি ইনজেকশনের সাথে জাভা উদাহরণ
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // নির্মাতার মাধ্যমে ডিপেন্ডেন্সি ইনজেক্ট করা হয়েছে
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // টুল ইমপ্লিমেন্টেশন
    // ...
}
```

#### ৩. কম্পোজেবল টুলস

এমন টুল ডিজাইন করুন যা একসাথে কম্পোজ করে আরও জটিল ওয়ার্কফ্লো তৈরি করতে পারে:

```python
# পাইথন উদাহরণ যা কম্পোজেবল টুলস দেখায়
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # বাস্তবায়ন...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # এই টুলটি dataFetch টুলের ফলাফল ব্যবহার করতে পারে
    async def execute_async(self, request):
        # বাস্তবায়ন...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # এই টুলটি dataAnalysis টুলের ফলাফল ব্যবহার করতে পারে
    async def execute_async(self, request):
        # বাস্তবায়ন...
        pass

# এই টুলগুলো স্বাধীনভাবে বা একটি ওয়ার্কফ্লোর অংশ হিসেবে ব্যবহৃত হতে পারে
```

### স্কিমা ডিজাইন সেরা অনুশীলন

স্কিমা হলো মডেল এবং আপনার টুলের মধ্যে চুক্তি। ভাল ডিজাইন করা স্কিমাগুলো টুলের ব্যবহারযোগ্যতা বাড়ায়।

#### ১. স্পষ্ট প্যারামিটার বর্ণনা

প্রতিটি প্যারামিটারের জন্য সর্বদা বর্ণনামূলক তথ্য অন্তর্ভুক্ত করুন:

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

#### ২. যাচাই সীমাবদ্ধতা

অবৈধ ইনপুট এড়াতে যাচাই সীমাবদ্ধতা অন্তর্ভুক্ত করুন:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // ফরম্যাট যাচাইসহ ইমেইল প্রোপার্টি
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // সংখ্যাসূচক সীমাবদ্ধতা সহ বয়স প্রোপার্টি
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // এনামারেটেড প্রোপার্টি
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

#### ৩. সঙ্গতিপূর্ণ রিটার্ন স্ট্রাকচার

আপনার রেসপন্স স্ট্রাকচারে সঙ্গতি বজায় রাখুন যাতে মডেলগুলো সহজে ফলাফল ব্যাখ্যা করতে পারে:

```python
async def execute_async(self, request):
    try:
        # অনুরোধ প্রক্রিয়াকরণ করুন
        results = await self._search_database(request.parameters["query"])
        
        # সর্বদা একটি সঙ্গতিশীল কাঠামো ফেরত দিন
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

### এরর হ্যান্ডলিং

MCP টুলের নির্ভরযোগ্যতা বজায় রাখার জন্য শক্তিশালী এরর হ্যান্ডলিং অপরিহার্য।

#### ১. সদয় এরর হ্যান্ডলিং

যথাযথ স্তরে ত্রুটিগুলো পরিচালনা করুন এবং তথ্যবহুল বার্তা প্রদান করুন:

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

#### ২. গঠনগত এরর রেসপন্স

সম্ভব হলে গঠনগত এরর তথ্য ফেরত দিন:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // বাস্তবায়ন
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
        
        // অন্য ব্যতিক্রমগুলো ToolExecutionException হিসাবে পুনরায় ছুড়ে দিন
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### ৩. রিট্রাই লজিক

সাধারণ রিড-ওনলি কল অথবা এমন অপারেশনের জন্য রিট্রাই লজিক ব্যবহার করুন যেটার
ডাউনস্ট্রিম চুক্তি ইতিমধ্যেই আইডেম্পোটেন্ট। কার্যকর অপারেশনের জন্য, রিকোয়েস্ট পাঠানোর পর
টাইমআউট বিভ্রান্তিকর। কর্তৃত্বপূর্ণ স্টেট পুনর্মিলন করুন এবং
একই স্থিতিশীল অপারেশন কী পুনর্ব্যবহার করুন পুনরায় কার্যকর করার আগে। দেখুন
[রিলায়েবিলিটি সাইডকার কম্প্যানিয়ন লেসন](./reliability-sidecars/README.md)।

পড়ার-ওনলি লুকআপের জন্য নিম্নলিখিত সীমাবদ্ধ রিট্রাই লুপ উপযুক্ত:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # সেকেন্ড
    
    while retry_count < max_retries:
        try:
            # একটি শুধুমাত্র-পঠন বহিঃস্থ API কল করুন
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # সূচকীয় ব্যাকঅফ
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # অস্থায়ী নয় এমন ত্রুটি, পুনরায় চেষ্টা করবেন না
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### পারফরম্যান্স অপটিমাইজেশন

#### ১. ক্যাশিং

ব্যয়বহুল অপারেশনের জন্য ক্যাশিং প্রয়োগ করুন:

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

#### ২. অ্যাসিঙ্ক্রোনাস প্রসেসিং

আই/ও-সম্পর্কিত অপারেশনের জন্য অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং প্যাটার্ন ব্যবহার করুন:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // দীর্ঘমেয়াদী অপারেশনের জন্য, অবিলম্বে একটি প্রসেসিং আইডি ফিরিয়ে দিন
        String processId = UUID.randomUUID().toString();
        
        // অ্যাসিঙ্ক্রোনাস প্রসেসিং শুরু করুন
        CompletableFuture.runAsync(() -> {
            try {
                // দীর্ঘমেয়াদী অপারেশন সম্পাদন করুন
                documentService.processDocument(documentId);
                
                // স্ট্যাটাস আপডেট করুন (সাধারণত একটি ডাটাবেসে সংরক্ষণ করা হয়)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // প্রসেস আইডি সহ অবিলম্বে প্রতিক্রিয়া ফেরত দিন
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // কম্প্যানিয়ন স্ট্যাটাস চেক টুল
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

#### ৩. রিসোর্স থ্রটলিং

অতিরিক্ত লোড এড়াতে রিসোর্স থ্রটলিং প্রয়োগ করুন:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # প্রতি সেকেন্ডে ৫টি অনুরোধ অনুমতি দিন
            bucket_size=10        # ১০টি অনুরোধ পর্যন্ত একটি বিস্ফোরণ অনুমতি দিন
        )
    
    async def execute_async(self, request):
        # আমরা এগিয়ে যেতে পারব কিনা বা অপেক্ষা করতে হবে কিনা তা পরীক্ষা করুন
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # যদি অপেক্ষা অনেক দীর্ঘ হয়
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # সঠিক বিলম্ব সময়ের জন্য অপেক্ষা করুন
                await asyncio.sleep(delay)
        
        # একটি টোকেন খরচ করুন এবং অনুরোধের সাথে এগিয়ে যান
        self.rate_limiter.consume()
        
        # এপিআই কল করুন
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
            
            # পরবর্তী টোকেন পাওয়া পর্যন্ত সময় গণনা করুন
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # শেষ হওয়া সময়ের ভিত্তিতে নতুন টোকেন যোগ করুন
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### সিকিউরিটি সেরা অনুশীলন

#### ১. ইনপুট যাচাই

সর্বদা ইনপুট প্যারামিটারগুলো যথাযথভাবে যাচাই করুন:

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

#### ২. অনুমোদন যাচাইকরণ

যথাযথ অনুমোদন যাচাইকরণ প্রয়োগ করুন:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // অনুরোধ থেকে ব্যবহারকারীর প্রসঙ্গ নিন
    UserContext user = request.getContext().getUserContext();
    
    // ব্যবহারকারীর প্রয়োজনীয় অনুমতি আছে কিনা পরীক্ষা করুন
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // নির্দিষ্ট সম্পদের জন্য, সেই সম্পদে অ্যাক্সেস পরীক্ষা করুন
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // টুল কার্যকর করার সাথে এগিয়ে যান
    // ...
}
```

#### ৩. সংবেদনশীল ডেটা পরিচালনা

সংবেদনশীল ডেটা যত্নসহকারে পরিচালনা করুন:

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
        
        # ব্যবহারকারীর ডেটা পান
        user_data = await self.user_service.get_user_data(user_id)
        
        # স্পষ্টভাবে অনুরোধ এবং অনুমোদিত না হলে সংবেদনশীল ক্ষেত্রগুলি ফিল্টার করুন
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # অনুরোধ প্রসঙ্গে অনুমোদন স্তর পরীক্ষা করুন
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # মূলটি পরিবর্তন এড়াতে একটি কপি তৈরি করুন
        redacted = user_data.copy()
        
        # নির্দিষ্ট সংবেদনশীল ক্ষেত্রগুলি লুকান
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # গহ্বরিত সংবেদনশীল ডেটা লুকান
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCP টুলের জন্য টেস্টিং সেরা অনুশীলন

ব্যাপক টেস্টিং নিশ্চিত করে MCP টুলগুলি সঠিকভাবে কাজ করে, এজ কেস হ্যান্ডেল করে এবং সিস্টেমের সাথে সঠিকভাবে ইন্টিগ্রেট হয়।

### ইউনিট টেস্টিং

#### ১. প্রত্যেক টুল আলাদাভাবে টেস্ট করুন

প্রত্যেক টুলের কার্যকারিতার জন্য কেন্দ্রীভূত টেস্ট তৈরি করুন:

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

#### ২. স্কিমা যাচাই টেস্টিং

যাচাই করুন স্কিমাগুলো বৈধ এবং সঠিকভাবে সীমাবদ্ধতা প্রয়োগ করে:

```java
@Test
public void testSchemaValidation() {
    // টুল ইনস্ট্যান্স তৈরি করুন
    SearchTool searchTool = new SearchTool();
    
    // স্কিমা নিন
    Object schema = searchTool.getSchema();
    
    // যাচাইয়ের জন্য স্কিমা JSON এ রূপান্তর করুন
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // যাচাই করুন স্কিমা বৈধ JSONSchema কিনা
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // বৈধ প্যারামিটার পরীক্ষা করুন
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // অনুপস্থিত প্রয়োজনীয় প্যারামিটার পরীক্ষা করুন
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // অবৈধ প্যারামিটার টাইপ পরীক্ষা করুন
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### ৩. এরর হ্যান্ডলিং টেস্ট

ত্রুটির শর্তগুলির জন্য নির্দিষ্ট টেস্ট তৈরি করুন:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # সাজান
    tool = ApiTool(timeout=0.1)  # খুব সংক্ষিপ্ত টাইমআউট
    
    # একটি অনুরোধ মক করুন যা টাইমআউট হবে
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # টাইমআউটের চেয়ে দীর্ঘ
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # কার্যকর করুন & নিশ্চিত করুন
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # ত্রুটির বার্তা যাচাই করুন
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # সাজান
    tool = ApiTool()
    
    # একটি রেট-সীমিত প্রতিক্রিয়া মক করুন
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
        
        # কার্যকর করুন & নিশ্চিত করুন
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # নিশ্চিত করুন যে ত্রুটিতে রেট সীমার তথ্য রয়েছে
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### ইন্টিগ্রেশন টেস্টিং

#### ১. টুল চেইন টেস্টিং

প্রত্যাশিত সংমিশ্রণে একসঙ্গে কাজ করা টুলগুলো টেস্ট করুন:

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

#### ২. MCP সার্ভার টেস্টিং

পূর্ণ টুল রেজিস্ট্রেশন এবং Execution সহ MCP সার্ভার টেস্ট করুন:

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
        // ডিসকভারি এন্ডপয়েন্ট পরীক্ষা করুন
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // টুল অনুরোধ তৈরি করুন
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // অনুরোধ পাঠান এবং প্রতিক্রিয়া যাচাই করুন
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // অবৈধ টুল অনুরোধ তৈরি করুন
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // "b" প্যারামিটার অনুপস্থিত
        request.put("parameters", parameters);
        
        // অনুরোধ পাঠান এবং ত্রুটি প্রতিক্রিয়া যাচাই করুন
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### ৩. End-to-End টেস্টিং

মডেল প্রম্পট থেকে টুল Execution পর্যন্ত সম্পূর্ণ ওয়ার্কফ্লো টেস্ট করুন:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # আয়োজন - MCP ক্লায়েন্ট এবং মক মডেল সেট আপ করুন
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # মক মডেল প্রতিক্রিয়া
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
    
    # মক আবহাওয়া টুল প্রতিক্রিয়া
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
        
        # কার্যকর করুন
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # নিশ্চয়তা প্রদান করুন
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### পারফরম্যান্স টেস্টিং

#### ১. লোড টেস্টিং

পরীক্ষা করুন আপনার MCP সার্ভার কত সংখ্যক সমসাময়িক অনুরোধ পরিচালনা করতে পারে:

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

#### ২. স্ট্রেস টেস্টিং

চরম লোডের অধীনে সিস্টেম টেস্ট করুন:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // চাপ পরীক্ষার জন্য JMeter সেট আপ করুন
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeter টেস্ট প্ল্যান কনফিগার করুন
    HashTree testPlanTree = new HashTree();
    
    // টেস্ট প্ল্যান, থ্রেড গ্রুপ, স্যাম্পলার ইত্যাদি তৈরি করুন
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // টুল এক্সিকিউশনের জন্য HTTP স্যাম্পলার যোগ করুন
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // লিসেনার যোগ করুন
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // পরীক্ষা চালান
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // ফলাফল যাচাই করুন
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // গড় প্রতিক্রিয়া সময় < ২০০মি.সেকেন্ড
    assertTrue(summaryReport.getPercentile(90.0) < 500); // ৯০তম শতকীয় < ৫০০মি.সেকেন্ড
}
```

#### ৩. পর্যবেক্ষণ এবং প্রোফাইলিং

দীর্ঘমেয়াদী পারফরম্যান্স বিশ্লেষণ জন্য পর্যবেক্ষণ পরিচালনা করুন:

```python
# একটি MCP সার্ভারের জন্য মনিটরিং কনফিগার করুন
def configure_monitoring(server):
    # Prometheus মেট্রিক্স সেট আপ করুন
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
    
    # টাইমিং এবং মেট্রিক্স রেকর্ড করার জন্য মিডলওয়্যার যুক্ত করুন
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # মেট্রিক্স এন্ডপয়েন্ট প্রকাশ করুন
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP ওয়ার্কফ্লো ডিজাইন প্যাটার্ন

ভাল ডিজাইন করা MCP ওয়ার্কফ্লো দক্ষতা, নির্ভরযোগ্যতা এবং রক্ষণযোগ্যতা উন্নত করে। অনুসরণের জন্য এখানে প্রধান প্যাটার্নসমূহ:

### ১. টুল চেইন প্যাটার্ন

একটির আউটপুট পরেরটির ইনপুট হয় এমনভাবে একাধিক টুল যুক্ত করুন:

```python
# পাইথন চেইন অফ টুলস বাস্তবায়ন
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # ধারাবাহিকভাবে চালানোর জন্য টুলের নামের তালিকা
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # চেইনের প্রতিটি টুল চালান, পূর্বের ফলাফল পাস করে
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # ফলাফল সংরক্ষণ করুন এবং পরবর্তী টুলের ইনপুট হিসাবে ব্যবহার করুন
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# উদাহরণ ব্যবহার
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

### ২. ডিসপ্যাচার প্যাটার্ন

ইনপুটের উপর ভিত্তি করে বিশেষায়িত টুলগুলোতে ডিসপ্যাচ করার জন্য কেন্দ্রীয় টুল ব্যবহার করুন:

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

### ৩. প্যারালাল প্রসেসিং প্যাটার্ন

দক্ষতার জন্য একাধিক টুল একই সময়ে কার্যকর করুন:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // ধাপ ১: ডেটাসেট মেটাডেটা সংগ্রহ করা (সমলয়িক)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // ধাপ ২: একাধিক বিশ্লেষণ সমান্তরালে চালু করা
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
        
        // সমস্ত সমান্তরাল কাজ শেষ হওয়ার জন্য অপেক্ষা করুন
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // সমাপ্তির জন্য অপেক্ষা করুন
        
        // ধাপ ৩: ফলাফল সমন্বিত করুন
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // ধাপ ৪: সামারি রিপোর্ট তৈরি করুন
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // সম্পূর্ণ কর্মপ্রবাহের ফলাফল ফেরত দিন
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### ৪. এরর রিকভারি প্যাটার্ন

টুল ব্যর্থতার জন্য সদয় ফallbackগুলি প্রয়োগ করুন:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # প্রথমে প্রাথমিক টুলটি চেষ্টা করুন
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # ব্যর্থতা লোগ করুন
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # মাধ্যমিক টুলে ফিরে যান
            try:
                # ফallback টুলের জন্য প্যারামিটারগুলি রূপান্তর করতে হতে পারে
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # উভয় টুল ব্যর্থ হয়েছে
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # এই বাস্তবায়ন নির্দিষ্ট টুলগুলোর উপর নির্ভর করবে
        # এই উদাহরণের জন্য, আমরা শুধু মূল প্যারামিটারগুলি ফিরিয়ে দেব
        return params

# উদাহরণস্বরূপ ব্যবহার
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # প্রাথমিক (পেইড) আবহাওয়া API
        "basicWeatherService",    # ফallback (ফ্রি) আবহাওয়া API
        {"location": location}
    )
```

### ৫. ওয়ার্কফ্লো কম্পোজিশন প্যাটার্ন

সহজ ওয়ার্কফ্লো একসাথে নিয়ে জটিল ওয়ার্কফ্লো তৈরি করুন:

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

# MCP সার্ভার টেস্টিং: সেরা অনুশীলন এবং শীর্ষ টিপস

## ওভারভিউ

নির্ভরযোগ্য, উচ্চ-গুণমান MCP সার্ভার বিকাশের জন্য টেস্টিং একটি গুরুত্বপূর্ণ দিক। এই গাইডটি একক টেস্ট থেকে ইন্টিগ্রেশন টেস্ট এবং এন্ড-টু-এন্ড ভ্যালিডেশন পর্যন্ত আপনার MCP সার্ভার টেস্টিংয়ের জন্য ব্যাপক সেরা অনুশীলন এবং টিপস প্রদান করে।

## MCP সার্ভারের জন্য টেস্টিং কেন গুরুত্বপূর্ণ

MCP সার্ভারগুলি AI মডেল এবং ক্লায়েন্ট অ্যাপ্লিকেশনের মধ্যে গুরুত্বপূর্ণ মিডলওয়্যার হিসেবে কাজ করে। ব্যাপক টেস্টিং নিশ্চিত করে:

- প্রোডাকশন পরিবেশে নির্ভরযোগ্যতা
- অনুরোধ এবং প্রতিক্রিয়াগুলোর সঠিক হ্যান্ডলিং
- MCP স্পেসিফিকেশন সঠিক বাস্তবায়ন
- ব্যর্থতা এবং এজ কেসের বিরুদ্ধে প্রতিরোধ ক্ষমতা
- বিভিন্ন লোডে ধারাবাহিক পারফরম্যান্স

## MCP সার্ভারের জন্য ইউনিট টেস্টিং

### ইউনিট টেস্টিং (মূল স্তর)

ইউনিট টেস্টগুলি আপনার MCP সার্ভারের পৃথক উপাদানগুলো আলাদাভাবে যাচাই করে।

#### কি টেস্ট করবেন

১. **রিসোর্স হ্যান্ডলার**: প্রতিটি রিসোর্স হ্যান্ডলারের লজিক আলাদাভাবে টেস্ট করুন
২. **টুল ইমপ্লিমেন্টেশন**: বিভিন্ন ইনপুট নিয়ে টুলের আচরণ যাচাই করুন
৩. **প্রম্পট টেমপ্লেট**: নিশ্চিত করুন প্রম্পট টেমপ্লেট সঠিকভাবে রেন্ডার হয়
৪. **স্কিমা যাচাই**: প্যারামিটার যাচাই লজিক টেস্ট করুন
৫. **এরর হ্যান্ডলিং**: অবৈধ ইনপুটের জন্য এরর রেসপন্স যাচাই করুন

#### ইউনিট টেস্টিংয়ের সেরা অনুশীলন

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
# পাইথনে একটি ক্যালকুলেটর টুলের উদাহরণ ইউনিট টেস্ট
def test_calculator_tool_add():
    # ব্যবস্থা করুন
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # কর্ম করুন
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # নিশ্চিত করুন
    assert result["value"] == 12
```

### ইন্টিগ্রেশন টেস্টিং (মধ্য স্তর)

ইন্টিগ্রেশন টেস্টগুলি আপনার MCP সার্ভারের উপাদানগুলোর মধ্যে ইন্টারঅ্যাকশন যাচাই করে।

#### কি টেস্ট করবেন

১. **সার্ভার ইনিশিয়ালাইজেশন**: বিভিন্ন কনফিগারেশন নিয়ে সার্ভার স্টার্টআপ টেস্ট করুন
২. **রুট রেজিস্ট্রেশন**: নিশ্চিত করুন সব এন্ডপয়েন্ট সঠিকভাবে রেজিস্টার হয়েছে
৩. **রিকুয়েস্ট প্রসেসিং**: সম্পূর্ণ রিকুয়েস্ট-রেসপন্স সাইকেল টেস্ট করুন
৪. **এরর প্রসার**: নিশ্চিত করুন ত্রুটিগুলো উপাদানগুলোর মধ্যে সঠিকভাবে হ্যান্ডল করা হয়
৫. **অথেনটিকেশন ও অথরাইজেশন**: সিকিউরিটি মেকানিজম টেস্ট করুন

#### ইন্টিগ্রেশন টেস্টিংয়ের সেরা অনুশীলন

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

### এন্ড-টু-এন্ড টেস্টিং (উচ্চ স্তর)

এন্ড-টু-এন্ড টেস্ট পুরো সিস্টেমের আচরণ ক্লায়েন্ট থেকে সার্ভার পর্যন্ত যাচাই করে।

#### কি টেস্ট করবেন

১. **ক্লায়েন্ট-সার্ভার যোগাযোগ**: সম্পূর্ণ রিকুয়েস্ট-রেসপন্স সাইকেল টেস্ট করুন
২. **বাস্তব ক্লায়েন্ট SDK**: আসল ক্লায়েন্ট ইমপ্লিমেন্টেশন নিয়ে টেস্ট করুন
৩. **লোডের অধীনে পারফরম্যান্স**: একাধিক সমসাময়িক রিকুয়েস্ট নিয়ে আচরণ যাচাই করুন
৪. **ত্রুটি পুনরুদ্ধার**: ব্যর্থতা থেকে সিস্টেম পুনরুদ্ধার টেস্ট করুন

5. **দীর্ঘমেয়াদী অপারেশনস**: স্ট্রিমিং এবং দীর্ঘ অপারেশনগুলি সঠিকভাবে পরিচালিত হচ্ছে কিনা যাচাইকরণ করুন

#### ই2ই পরীক্ষার জন্য সেরা অনুশীলন

```typescript
// টাইপস্ক্রিপ্টে ক্লায়েন্ট সহ উদাহরণ E2E টেস্ট
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // টেস্ট পরিবেশে সার্ভার শুরু করুন
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // কার্যকর করুন
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // নিশ্চিত করুন
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCP পরীক্ষার জন্য মকিং কৌশল

পরীক্ষার সময় উপাদানগুলি আলাদা করার জন্য মকিং অপরিহার্য।

### মক করার উপাদানসমূহ

1. **বাহ্যিক এআই মডেলসমূহ**: পূর্বানুমানযোগ্য পরীক্ষার জন্য মডেল রেসপন্স মক করুন
2. **বাহ্যিক পরিষেবাসমূহ**: API নির্ভরশীলতাগুলি মক করুন (ডাটাবেস, তৃতীয় পক্ষের পরিষেবা)
3. **প্রমাণীকরণ পরিষেবাসমূহ**: পরিচয় প্রদানকারীদের মক করুন
4. **সম্পদ প্রদানকারীরা**: ব্যয়বহুল সম্পদ হ্যান্ডলার মক করুন

### উদাহরণ: একটি এআই মডেল রেসপন্স মক করা

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
# পাইথন উদাহরণ unittest.mock সহ
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # মক কনফিগার করুন
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # টেস্টে মক ব্যবহার করুন
    server = McpServer(model_client=mock_model)
    # টেস্ট চালিয়ে যান
```

## কর্মদক্ষতা পরীক্ষা

উৎপাদন MCP সার্ভারের জন্য কর্মদক্ষতা পরীক্ষা অত্যন্ত জরুরি।

### কী মাপবেন

1. **প্রতিবিম্বণকাল**: অনুরোধের জন্য রেসপন্স সময়
2. **থ্রুপুট**: প্রতি সেকেন্ডে প্রক্রিয়াকৃত অনুরোধের সংখ্যা
3. **সম্পদ ব্যবহারের পরিসর**: CPU, মেমরি, নেটওয়ার্ক ব্যবহার
4. **সহচরিতার হ্যান্ডলিং**: সমান্তরাল অনুরোধের সময় আচরণ
5. **স্কেলিং বৈশিষ্ট্যাবলী**: লোড বৃদ্ধি পাওয়ার সাথে কর্মক্ষমতা

### কর্মদক্ষতা পরীক্ষার জন্য সরঞ্জামসমূহ

- **k6**: ওপেন-সোর্স লোড পরীক্ষার সরঞ্জাম
- **JMeter**: ব্যাপক কর্মদক্ষতা পরীক্ষা
- **Locust**: পাইথন ভিত্তিক লোড পরীক্ষা
- **Azure Load Testing**: ক্লাউড-বেসড কর্মদক্ষতা পরীক্ষা

### উদাহরণ: k6 দিয়ে মৌলিক লোড টেস্ট

```javascript
// MCP সার্ভারের লোড টেস্টিংয়ের জন্য k6 স্ক্রিপ্ট
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 ভার্চুয়াল ব্যবহারকারী
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

## MCP সার্ভারের জন্য টেস্ট অটোমেশন

আপনার পরীক্ষাগুলো স্বয়ংক্রিয়করণ নিশ্চিত করে ধারাবাহিক মান এবং দ্রুত প্রতিক্রিয়া।

### সিআই/সিডি একত্রিকরণ

1. **পুল রিকোয়েস্টে ইউনিট টেস্ট চালানো**: কোড পরিবর্তন ফাংশনভঙ্গ করে কিনা নিশ্চিত করা
2. **স্টেজিং-এ ইন্টিগ্রেশন টেস্ট**: প্রি-প্রোডাকশন পরিবেশে ইন্টিগ্রেশন টেস্ট চালানো
3. **পারফরম্যান্স বেজলাইন**: কর্মক্ষমতা বেঞ্চমার্ক বজায় রাখা যাতে রিগ্রেশন ধরা যায়
4. **নিরাপত্তা স্ক্যান**: পাইলাইনের অংশ হিসাবে নিরাপত্তা পরীক্ষা অটোমেশন

### উদাহরণ সিআই পাইপলাইন (GitHub Actions)

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

## MCP স্পেসিফিকেশন সামঞ্জস্য পরীক্ষণ

যাচাই করুন আপনার সার্ভার MCP স্পেসিফিকেশন সঠিকভাবে বাস্তবায়িত করছে কিনা।

### মূল সামঞ্জস্য ক্ষেত্রসমূহ

1. **API এন্ডপয়েন্টগুলি**: প্রয়োজনীয় এন্ডপয়েন্ট পরীক্ষা করুন (/resources, /tools ইত্যাদি)
2. **অনুরোধ/প্রতিক্রিয়া ফর্ম্যাট**: স্কিমা সামঞ্জস্য যাচাই করুন
3. **ত্রুটি কোডসমূহ**: বিভিন্ন পরিস্থিতিতে সঠিক স্ট্যাটাস কোড যাচাই করুন
4. **কন্টেন্ট টাইপসমূহ**: ভিন্ন ভিন্ন কন্টেন্ট টাইপের হ্যান্ডলিং পরীক্ষা করুন
5. **প্রমাণীকরণ প্রবাহ**: স্পেক-অনুবর্তী প্রমাণীকরণ প্রক্রিয়া যাচাই করুন

### সামঞ্জস্য পরীক্ষা স্যুট

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

## MCP সার্ভার পরীক্ষার জন্য সেরা ১০ টিপস

1. **টুল সংজ্ঞাগুলো আলাদাভাবে পরীক্ষা করুন**: টুল লজিক থেকে স্কিমা সংজ্ঞাগুলো স্বাধীনভাবে যাচাই করুন
2. **প্যারামিটারভিত্তিক টেস্ট ব্যবহার করুন**: বিভিন্ন ইনপুট ও যান্ত্রিক কেস নিয়ে টুল টেস্ট করুন
3. **ত্রুটি প্রতিক্রিয়াগুলো পরীক্ষা করুন**: সমস্ত সম্ভাব্য ত্রুটি শর্তের জন্য সঠিক হ্যান্ডলিং যাচাই করুন
4. **প্রমাণীকরণ লজিক পরীক্ষা করুন**: বিভিন্ন ব্যবহারকারী ভূমিকার জন্য যথাযথ নিয়ন্ত্রণ নিশ্চিত করুন
5. **টেস্ট কভারেজ পর্যবেক্ষণ করুন**: গুরুত্বপূর্ণ পথ কোডের উচ্চ কভারেজ লক্ষ্যমাত্রা করুন
6. **স্ট্রিমিং রেসপন্স পরীক্ষা করুন**: স্ট্রিমিং কন্টেন্ট সঠিকভাবে পরিচালনা হচ্ছে কিনা যাচাই করুন
7. **নেটওয়ার্ক সমস্যা সিমুলেট করুন**: খারাপ নেটওয়ার্ক অবস্থায় আচরণ পরীক্ষা করুন
8. **সম্পদ সীমা পরীক্ষা করুন**: কোটা বা রেট লিমিট পৌঁছালে আচরণ যাচাই করুন
9. **রিগ্রেশন টেস্ট অটোমেট করুন**: এমন একটি স্যুট তৈরি করুন যা প্রতিটি কোড পরিবর্তনে চলে
10. **টেস্ট কেস ডকুমেন্ট করুন**: টেস্ট দৃশ্যপটের স্পষ্ট ডকুমেন্টেশন রক্ষণাবেক্ষণ করুন

## সাধারণ পরীক্ষার ভুল

- **শুধুমাত্র সফল পথ পরীক্ষা উপর অতিরিক্ত নির্ভরতা**: ত্রুটি কেসগুলো সম্পূর্ণরূপে পরীক্ষা করুন
- **কর্মদক্ষতা পরীক্ষা উপেক্ষা**: উৎপাদনের আগেই সংকট চিহ্নিত করুন
- **একমাত্র বিচ্ছিন্নভাবে পরীক্ষা করা**: ইউনিট, ইন্টিগ্রেশন, এবং ই2ই টেস্টের সমন্বয় করুন
- **অসম্পূর্ণ API কভারেজ**: সব এন্ডপয়েন্ট ও ফিচার পরীক্ষা নিশ্চিত করুন
- **অসামঞ্জস্যপূর্ণ পরীক্ষার পরিবেশ**: ধারাবাহিক পরীক্ষা পরিবেশ নিশ্চিত করতে কন্টেইনার ব্যবহার করুন

## উপসংহার

একটি ব্যাপক পরীক্ষার কৌশল নির্ভরযোগ্য, উচ্চ-মানের MCP সার্ভার উন্নয়নের জন্য অপরিহার্য। এই গাইডের সেরা অনুশীলন এবং টিপসগুলি প্রয়োগ করে, আপনি নিশ্চিত করতে পারবেন যে আপনার MCP বাস্তবায়নগুলি সর্বোচ্চ মান, নির্ভরযোগ্যতা এবং কর্মদক্ষতা অর্জন করছে।


## মূল বিষয়গুলি

1. **টুল ডিজাইন**: একক দায়িত্ব নীতিমালা অনুসরণ করুন, ডিপেন্ডেন্সি ইনজেকশন ব্যবহার করুন, এবং সংযোজ্যতার জন্য ডিজাইন করুন
2. **স্কিমা ডিজাইন**: পরিষ্কার, ভাল ডকুমেন্টেড স্কিমা তৈরি করুন যথাযথ বৈধতা বিধিনিষেধ সহ
3. **ত্রুটি হ্যান্ডলিং**: শালীন ত্রুটি হ্যান্ডলিং, গঠিত ত্রুটি প্রতিক্রিয়া, এবং আউটকাম-সচেতন পুনরায়চেষ্টা লজিক বাস্তবায়ন করুন
4. **কর্মক্ষমতা**: ক্যাশিং, অ্যাসিঙ্ক্রোনাস প্রক্রিয়াকরণ, এবং সম্পদ থ্রটলিং ব্যবহার করুন
5. **নিরাপত্তা**: বিস্তারিত ইনপুট বৈধতা, অনুমোদন পরীক্ষা, এবং সংবেদনশীল তথ্য পরিচালনা প্রয়োগ করুন
6. **পরীক্ষা**: ব্যাপক ইউনিট, ইন্টিগ্রেশন, এবং এন্ড-টু-এন্ড পরীক্ষা তৈরি করুন
7. **ওয়ার্কফ্লো প্যাটার্নস**: চেইন, ডিসপ্যাচার, এবং প্যারালাল প্রসেসিংয়ের মতো প্রতিষ্ঠিত প্যাটার্ন প্রয়োগ করুন






2. ডকুমেন্ট থেকে টেক্সট এবং মূল তথ্য বের করে
3. ডকুমেন্ট শ্রেণীবদ্ধ করে টাইপ এবং বিষয়বস্তু অনুযায়ী
4. প্রতিটি ডকুমেন্টের একটি সংক্ষিপ্তসার তৈরি করে




## সম্পদসমূহ 

1. সর্বশেষ উন্নয়ন সম্পর্কে আপডেট থাকার জন্য MCP কমিউনিটিতে যোগ দিন [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs)
2. ওপেন-সোর্স [MCP প্রকল্পে অবদান রাখুন](https://github.com/modelcontextprotocol)
3. আপনার নিজের সংস্থার AI উদ্যোগে MCP নীতিমালা প্রয়োগ করুন
4. আপনার শিল্পের জন্য বিশেষায়িত MCP বাস্তবায়নগুলো এক্সপ্লোর করুন।
5. বিশেষ MCP বিষয়ের উপর উন্নত কোর্স নেওয়ার কথা বিবেচনা করুন, যেমন মাল্টি-মোডাল ইন্টিগ্রেশন বা এন্টারপ্রাইজ অ্যাপ্লিকেশন ইন্টিগ্রেশন।
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) এর মাধ্যমে শেখা নীতিমালা ব্যবহার করে নিজের MCP টুল এবং ওয়ার্কফ্লো তৈরি করে পরীক্ষা-নিরীক্ষা করুন

## পরবর্তী কি

পরবর্তী: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
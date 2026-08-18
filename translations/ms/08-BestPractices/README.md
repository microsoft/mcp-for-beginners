# Amalan Terbaik Pembangunan MCP

[![Amalan Terbaik Pembangunan MCP](../../../translated_images/ms/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Klik imej di atas untuk melihat video pelajaran ini)_

## Gambaran Keseluruhan

Pelajaran ini menumpukan pada amalan terbaik lanjutan untuk membangun, menguji, dan menyebarkan pelayan dan ciri MCP di persekitaran pengeluaran. Apabila ekosistem MCP menjadi lebih kompleks dan penting, mengikuti corak yang telah ditetapkan memastikan kebolehpercayaan, kebolehselenggaraan, dan keserasian. Pelajaran ini mengumpulkan kebijaksanaan praktikal yang diperoleh daripada pelaksanaan MCP dunia nyata untuk membimbing anda dalam mencipta pelayan yang mantap dan cekap dengan sumber, arahan, dan alat yang berkesan.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Mengaplikasikan amalan terbaik industri dalam reka bentuk pelayan dan ciri MCP
- Mewujudkan strategi ujian menyeluruh untuk pelayan MCP
- Merekabentuk corak aliran kerja yang cekap dan boleh diguna semula untuk aplikasi MCP yang kompleks
- Melaksanakan pengendalian ralat, pencatatan, dan observabiliti yang betul dalam pelayan MCP
- Mengoptimumkan pelaksanaan MCP untuk prestasi, keselamatan, dan kebolehselenggaraan

## Prinsip Teras MCP

Sebelum menyelami amalan pelaksanaan tertentu, adalah penting untuk memahami prinsip teras yang membimbing pembangunan MCP yang berkesan:

1. **Komunikasi Standard**: MCP menggunakan JSON-RPC 2.0 sebagai asasnya, menyediakan format konsisten untuk permintaan, tindak balas, dan pengendalian ralat di semua pelaksanaan.

2. **Reka Bentuk Berorientasikan Pengguna**: Sentiasa mengutamakan persetujuan, kawalan, dan ketelusan pengguna dalam pelaksanaan MCP anda.

3. **Keselamatan Diutamakan**: Melaksanakan langkah keselamatan yang mantap termasuk pengesahan, kebenaran, pengesahan parameter, dan had kadar.

4. **Seni Bina Modular**: Reka pelayan MCP anda dengan pendekatan modular, di mana setiap alat dan sumber mempunyai tujuan yang jelas dan fokus.

5. **Keadaan Eksplisit**: MCP `2026-07-28` adalah tanpa keadaan di lapisan protokol.
   Apabila aliran kerja memerlukan keadaan silang-panggilan, gunakan pemegang eksplisit atau
   argumen alat biasa yang disokong oleh keadaan aplikasi yang tahan lama.

## Amalan Terbaik Rasmi MCP

Amalan terbaik berikut diambil daripada dokumentasi Model Context Protocol rasmi:

### Amalan Terbaik Keselamatan

1. **Persetujuan dan Kawalan Pengguna**: Sentiasa memerlukan persetujuan pengguna yang jelas sebelum mengakses data atau melaksanakan operasi. Berikan kawalan yang jelas terhadap data yang dikongsi dan tindakan yang dibenarkan.

2. **Privasi Data**: Hanya dedahkan data pengguna dengan persetujuan yang jelas dan lindungi dengan kawalan akses yang sesuai. Lindungi daripada penghantaran data tanpa kebenaran.

3. **Keselamatan Alat**: Memerlukan persetujuan pengguna yang jelas sebelum memanggil mana-mana alat. Pastikan pengguna memahami fungsi setiap alat dan menguatkuasakan sempadan keselamatan yang kukuh.

4. **Kawalan Kebenaran Alat**: Konfigurasikan alat mana yang model boleh gunakan untuk
   setiap permintaan dan konteks kebenaran, memastikan hanya
   alat yang diberi kebenaran secara eksplisit dapat diakses.

5. **Pengesahan**: Memerlukan pengesahan yang betul sebelum memberikan akses kepada alat, sumber, atau operasi sensitif menggunakan kunci API, token OAuth, atau kaedah pengesahan selamat lain.

6. **Pengesahan Parameter**: Menguatkuasakan pengesahan untuk semua pemanggilan alat untuk mengelakkan input yang rosak atau berniat jahat daripada mencapai pelaksanaan alat.

7. **Had Kadar**: Melaksanakan had kadar untuk mengelakkan penyalahgunaan dan memastikan penggunaan sumber pelayan yang adil.

### Amalan Terbaik Pelaksanaan

1. **Rundingan Keupayaan**: Rundingkan versi protokol dan
   keupayaan yang disokong. Dalam MCP `2026-07-28`, setiap permintaan adalah bergantung sendiri dan boleh
   menggunakan `server/discover`; semakan lama menggunakan jabat tangan inisialisasi.

2. **Reka Bentuk Alat**: Cipta alat fokus yang melakukan satu perkara dengan baik, bukannya alat monolitik yang mengendalikan pelbagai perkara.

3. **Pengendalian Ralat**: Laksanakan mesej dan kod ralat standard untuk membantu mendiagnosis isu, mengendalikan kegagalan dengan lancar, dan memberikan maklum balas yang boleh diambil tindakan.

4. **Observabiliti**: Gunakan `stderr` untuk diagnostik stdio dan OpenTelemetry
   untuk observabiliti berstruktur. Ciri pencatatan MCP sudah dihentikan dalam
   spesifikasi `2026-07-28`.

5. **Penjejakan Kemajuan**: Untuk operasi yang berjalan lama, laporkan kemas kini kemajuan untuk membolehkan antara muka pengguna yang responsif.

6. **Pembatalan Permintaan**: Benarkan klien membatalkan permintaan yang sedang berjalan yang tidak lagi diperlukan atau mengambil masa terlalu lama.

## Rujukan Tambahan

Untuk maklumat paling terkini mengenai amalan terbaik MCP, rujuk:

- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP (2026-07-28)][mcp-2026-spec]
- [Spesifikasi MCP Sebelumnya (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Sambungan Tugasan MCP][mcp-tasks-extension]
- [Repositori GitHub](https://github.com/modelcontextprotocol)
- [Amalan Terbaik Keselamatan](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Risiko keselamatan dan mitigasi
- [Bengkel Sidang Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) - Latihan keselamatan praktikal

### Pelajaran Pendamping Ketekalan

Gelung cuba semula umum tidak selamat untuk alat yang membuat tiket, pembayaran,
mesej, penyebaran, atau kesan dunia nyata lain. Tindak balas boleh hilang
selepas kesan dilaksanakan.

Gunakan pelajaran pendamping ketekalan,
[Cubaan Selamat untuk Alat MCP: Corak Kereta Sampingan Ketekalan][reliability-sidecar],
untuk mempelajari kunci operasi stabil, kemasukan berganda, penanda aras,
penyesuaian, tahap bukti, dan suntikan kegagalan.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Contoh Pelaksanaan Praktikal

### Amalan Terbaik Reka Bentuk Alat

#### 1. Prinsip Tanggungjawab Tunggal

Setiap alat MCP harus mempunyai tujuan yang jelas dan fokus. Daripada mencipta alat monolitik yang cuba mengendalikan pelbagai perkara, bangunkan alat khusus yang cemerlang dalam tugas tertentu.

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

#### 2. Pengendalian Ralat Konsisten

Laksanakan pengendalian ralat yang mantap dengan mesej ralat yang informatif dan mekanisme pemulihan yang sesuai.

```python
# Contoh Python dengan pengendalian ralat yang menyeluruh
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Pengesahan parameter
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Pengesahan keselamatan
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operasi pangkalan data dengan had masa
                async with timeout(10):  # Had masa 10 saat
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Ralat sambungan mungkin bersifat sementara
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Ralat pertanyaan mungkin ralat klien
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Biarkan ralat khusus alat melalui
            raise
        except Exception as e:
            # Tangkap semua untuk ralat yang tidak dijangka
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Pelaksanaan pengesanan suntikan SQL
        pass
        
    def _log_error(self, message, error):
        # Pelaksanaan perekodan ralat
        pass
```

#### 3. Pengesahan Parameter

Sentiasa sahkan parameter dengan teliti untuk mengelakkan input yang rosak atau berniat jahat.

```javascript
// Contoh JavaScript/TypeScript dengan pengesahan parameter terperinci
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
    // 1. Sahkan kehadiran parameter
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Sahkan jenis parameter
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Sahkan nilai parameter
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Sahkan kehadiran kandungan untuk operasi tulis
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Pengesahan keselamatan laluan
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Pelaksanaan berdasarkan parameter yang disahkan
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Pelaksanaan pemeriksaan keselamatan laluan
    // ...
  }
}
```

### Contoh Pelaksanaan Keselamatan

#### 1. Pengesahan dan Kebenaran

```java
// Contoh Java dengan pengesahan dan kebenaran
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Suntikan kebergantungan
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
        // 1. Ekstrak konteks pengesahan
        String authToken = request.getContext().getAuthToken();
        
        // 2. Sahkan pengguna
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Semak kebenaran untuk operasi tertentu
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Teruskan dengan operasi yang dibenarkan
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

#### 2. Had Kadar

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

## Amalan Terbaik Ujian

### 1. Ujian Unit Alat MCP

Sentiasa uji alat anda secara terpencil, menipu pergantungan luaran:

```typescript
// Contoh ujian unit alat dalam TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Buat perkhidmatan cuaca tiruan
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Buat alat dengan pergantungan tiruan
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Atur
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Bertindak
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Sahkan
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Atur
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Bertindak & Sahkan
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Ujian Integrasi

Uji aliran lengkap dari permintaan klien ke tindak balas pelayan:

```python
# Contoh ujian integrasi Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Mulakan pelayan ujian
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Cipta klien
        client = McpClient("http://localhost:5000")
        
        # Uji penemuan alat
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Uji pelaksanaan alat
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Sahkan respons
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Bersihkan
        await server.stop()
```

## Pengoptimuman Prestasi

### 1. Strategi Caching

Laksanakan caching yang sesuai untuk mengurangkan kelewatan dan penggunaan sumber:


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

#### 2. Suntikan Kebergantungan dan Kebolehujian

Reka alat untuk menerima kebergantungan mereka melalui suntikan konstruktor, menjadikannya boleh diuji dan boleh dikonfigurasi:

```java
// Contoh Java dengan suntikan pergantungan
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Pergantungan disuntik melalui konstruktor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Pelaksanaan alat
    // ...
}
```

#### 3. Alat Komposabel

Reka alat yang boleh digabungkan bersama untuk mencipta aliran kerja yang lebih kompleks:

```python
# Contoh Python yang menunjukkan alat yang boleh disusun
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Pelaksanaan...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Alat ini boleh menggunakan keputusan dari alat dataFetch
    async def execute_async(self, request):
        # Pelaksanaan...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Alat ini boleh menggunakan keputusan dari alat dataAnalysis
    async def execute_async(self, request):
        # Pelaksanaan...
        pass

# Alat-alat ini boleh digunakan secara bebas atau sebagai sebahagian daripada aliran kerja
```

### Amalan Terbaik Reka Bentuk Skema

Skema adalah kontrak antara model dan alat anda. Skema yang direka dengan baik membawa kepada kebolehgunaan alat yang lebih baik.

#### 1. Penerangan Parameter yang Jelas

Sentiasa sertakan maklumat deskriptif untuk setiap parameter:

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

#### 2. Kekangan Pengesahan

Sertakan kekangan pengesahan untuk mengelakkan input yang tidak sah:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Harta e-mel dengan pengesahan format
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Harta umur dengan kekangan angka
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Harta disenaraikan
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

#### 3. Struktur Pulangan Konsisten

Kekalkan konsistensi dalam struktur respons anda untuk memudahkan model mentafsirkan keputusan:

```python
async def execute_async(self, request):
    try:
        # Proses permintaan
        results = await self._search_database(request.parameters["query"])
        
        # Sentiasa kembalikan struktur yang konsisten
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

### Pengendalian Ralat

Pengendalian ralat yang mantap adalah penting bagi alat MCP untuk mengekalkan kebolehpercayaan.

#### 1. Pengendalian Ralat dengan Anggun

Tangani ralat pada tahap yang sesuai dan sediakan mesej yang bermaklumat:

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

#### 2. Respons Ralat Berstruktur

Pulangkan maklumat ralat berstruktur apabila boleh:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Pelaksanaan
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
        
        // Lempar semula pengecualian lain sebagai ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logik Cuba Semula

Gunakan logik cuba semula generik hanya untuk panggilan baca sahaja atau operasi yang
kontrak hiliran sudah idempotent. Untuk operasi berkesan, tamat masa
selepas menghantar permintaan adalah samar. Selesaikan keadaan autoritatif dan
gunakan semula kunci operasi stabil yang sama sebelum melaksanakan lagi. Lihat
[pelajaran rakan sekerja sisi kebolehpercayaan](./reliability-sidecars/README.md).

Gelung cuba semula terhad berikut sesuai untuk carian baca sahaja:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # saat
    
    while retry_count < max_retries:
        try:
            # Panggil API luaran hanya baca
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Jeda eksponen
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Ralat bukan sementara, jangan cuba semula
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Pengoptimuman Prestasi

#### 1. Caching

Laksanakan caching untuk operasi yang mahal:

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

#### 2. Pemprosesan Tak Seiring

Gunakan corak pengaturcaraan tak seiring untuk operasi terikat I/O:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Untuk operasi yang berjalan lama, kembalikan ID pemprosesan dengan segera
        String processId = UUID.randomUUID().toString();
        
        // Mula pemprosesan asinkron
        CompletableFuture.runAsync(() -> {
            try {
                // Laksanakan operasi yang berjalan lama
                documentService.processDocument(documentId);
                
                // Kemas kini status (biasanya akan disimpan dalam pangkalan data)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Pulangkan respons segera dengan ID proses
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Alat semakan status pendamping
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

#### 3. Pengawalan Sumber

Laksanakan pengawalan sumber untuk mengelakkan beban berlebihan:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Benarkan 5 permintaan setiap saat
            bucket_size=10        # Benarkan letupan sehingga 10 permintaan
        )
    
    async def execute_async(self, request):
        # Semak jika kita boleh teruskan atau perlu tunggu
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Jika menunggu terlalu lama
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Tunggu masa kelewatan yang sesuai
                await asyncio.sleep(delay)
        
        # Gunakan satu token dan teruskan dengan permintaan
        self.rate_limiter.consume()
        
        # Panggil API
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
            
            # Kira masa sehingga token seterusnya tersedia
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Tambah token baru berdasarkan masa yang telah berlalu
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Amalan Terbaik Keselamatan

#### 1. Pengesahan Input

Sentiasa sahkan parameter input dengan teliti:

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

#### 2. Semakan Kebenaran

Laksanakan semakan kebenaran yang betul:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Dapatkan konteks pengguna dari permintaan
    UserContext user = request.getContext().getUserContext();
    
    // Periksa jika pengguna mempunyai kebenaran yang diperlukan
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Untuk sumber tertentu, periksa akses kepada sumber tersebut
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Teruskan dengan pelaksanaan alat
    // ...
}
```

#### 3. Pengendalian Data Sensitif

Kendalikan data sensitif dengan cermat:

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
        
        # Dapatkan data pengguna
        user_data = await self.user_service.get_user_data(user_id)
        
        # Tapis medan sensitif kecuali diminta secara jelas DAN diberi kuasa
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Semak tahap kebenaran dalam konteks permintaan
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Buat salinan untuk mengelakkan mengubah asal
        redacted = user_data.copy()
        
        # Tapis medan sensitif tertentu
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Tapis data sensitif bersarang
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Amalan Terbaik Ujian untuk Alat MCP

Ujian menyeluruh memastikan alat MCP berfungsi dengan betul, mengendalikan kes tepi, dan berintegrasi dengan sempurna dengan sistem lain.

### Ujian Unit

#### 1. Uji Setiap Alat Secara Terasing

Cipta ujian fokus untuk fungsi setiap alat:

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

#### 2. Ujian Pengesahan Skema

Uji bahawa skema adalah sah dan menguatkuasakan kekangan dengan betul:

```java
@Test
public void testSchemaValidation() {
    // Cipta contoh alat
    SearchTool searchTool = new SearchTool();
    
    // Dapatkan skema
    Object schema = searchTool.getSchema();
    
    // Tukar skema kepada JSON untuk pengesahan
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Sahkan skema adalah JSONSchema yang sah
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Uji parameter yang sah
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Uji parameter wajib yang hilang
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Uji jenis parameter yang tidak sah
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Ujian Pengendalian Ralat

Cipta ujian khusus untuk kondisi ralat:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Susun
    tool = ApiTool(timeout=0.1)  # Tempoh tamat masa yang sangat singkat
    
    # Meniru permintaan yang akan tamat masa
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Lebih lama daripada tamat masa
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Bertindak & Menegaskan
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Sahkan mesej pengecualian
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Susun
    tool = ApiTool()
    
    # Meniru tindak balas terhad kadar
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
        
        # Bertindak & Menegaskan
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Sahkan pengecualian mengandungi maklumat had kadar
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Ujian Integrasi

#### 1. Ujian Rangkaian Alat

Uji alat yang bekerja bersama dalam gabungan yang dijangka:

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

#### 2. Ujian Server MCP

Uji server MCP dengan pendaftaran dan pelaksanaan alat yang lengkap:

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
        // Uji titik akhir penemuan
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Buat permintaan alat
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Hantar permintaan dan sahkan respons
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Buat permintaan alat yang tidak sah
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Parameter "b" hilang
        request.put("parameters", parameters);
        
        // Hantar permintaan dan sahkan respons ralat
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Ujian Menyeluruh

Uji aliran kerja lengkap dari arahan model ke pelaksanaan alat:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Susun - Tetapkan pelanggan MCP dan model tiruan
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Respons model tiruan
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
    
    # Respons alat cuaca tiruan
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
        
        # Bertindak
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Nyatakan
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Ujian Prestasi

#### 1. Ujian Beban

Uji berapa banyak permintaan serentak yang boleh server MCP anda kendalikan:

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

#### 2. Ujian Tekanan

Uji sistem di bawah beban ekstrem:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Sediakan JMeter untuk ujian tekanan
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigurasikan pelan ujian JMeter
    HashTree testPlanTree = new HashTree();
    
    // Cipta pelan ujian, kumpulan benang, sampler, dan lain-lain
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Tambah sampler HTTP untuk pelaksanaan alat
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Tambah pendengar
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Jalankan ujian
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Sahkan keputusan
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Purata masa tindak balas < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // Peratusan ke-90 < 500ms
}
```

#### 3. Pemantauan dan Profiling

Sediakan pemantauan untuk analisis prestasi jangka panjang:

```python
# Konfigurasikan pemantauan untuk pelayan MCP
def configure_monitoring(server):
    # Tetapkan metrik Prometheus
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
    
    # Tambah perantara untuk pengukuran masa dan merekod metrik
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Dedahkan titik akhir metrik
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Corak Reka Bentuk Aliran Kerja MCP

Aliran kerja MCP yang direka dengan baik meningkatkan kecekapan, kebolehpercayaan, dan kebolehselenggaraan. Berikut adalah corak utama yang perlu diikuti:

### 1. Corak Rantaian Alat

Sambungkan pelbagai alat dalam urutan dimana output setiap alat menjadi input untuk yang berikutnya:

```python
# Pelaksanaan Rantaian Alat Python
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Senarai nama alat untuk dilaksanakan secara berurutan
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Laksanakan setiap alat dalam rantaian, menghantar hasil sebelumnya
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Simpan hasil dan gunakan sebagai input untuk alat seterusnya
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Contoh penggunaan
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

### 2. Corak Pengedar

Gunakan alat pusat yang mengedar kepada alat khusus berdasarkan input:

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

### 3. Corak Pemprosesan Selari

Laksanakan pelbagai alat secara serentak untuk kecekapan:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Langkah 1: Dapatkan metadata dataset (selari)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Langkah 2: Lancarkan pelbagai analisis secara serentak
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
        
        // Tunggu semua tugasan serentak selesai
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Tunggu penyiapan
        
        // Langkah 3: Gabungkan keputusan
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Langkah 4: Hasilkan laporan ringkasan
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Pulangkan hasil keseluruhan aliran kerja
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Corak Pemulihan Ralat

Laksanakan fallback anggun untuk kegagalan alat:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Cuba alat utama terlebih dahulu
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Logkan kegagalan
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Beralih kepada alat sekunder
            try:
                # Mungkin perlu menukar parameter untuk alat gantian
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Kedua-dua alat gagal
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Pelaksanaan ini bergantung kepada alat tertentu
        # Untuk contoh ini, kita hanya akan mengembalikan parameter asal
        return params

# Contoh penggunaan
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API cuaca utama (berbayar)
        "basicWeatherService",    # API cuaca gantian (percuma)
        {"location": location}
    )
```

### 5. Corak Penyusunan Aliran Kerja

Bina aliran kerja kompleks dengan menyusun aliran kerja yang lebih mudah:

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

# Menguji Server MCP: Amalan Terbaik dan Petua Teratas

## Gambaran Keseluruhan

Ujian adalah aspek penting dalam membangunkan server MCP yang boleh dipercayai dan berkualiti tinggi. Panduan ini menyediakan amalan terbaik dan petua komprehensif untuk menguji server MCP anda sepanjang kitaran pembangunan, daripada ujian unit kepada ujian integrasi dan pengesahan menyeluruh.

## Kenapa Ujian Penting untuk Server MCP

Server MCP berfungsi sebagai middleware penting antara model AI dan aplikasi klien. Ujian menyeluruh memastikan:

- Kebolehpercayaan dalam persekitaran produksi
- Pengendalian permintaan dan respons yang tepat
- Pelaksanaan spesifikasi MCP yang betul
- Ketahanan terhadap kegagalan dan kes tepi
- Prestasi konsisten di bawah pelbagai beban

## Ujian Unit untuk Server MCP

### Ujian Unit (Asas)

Ujian unit mengesahkan komponen individu server MCP anda secara terasing.

#### Apa yang Perlu Diuji

1. **Pengendali Sumber**: Uji logik setiap pengendali sumber secara bebas
2. **Pelaksanaan Alat**: Sahkan tingkah laku alat dengan pelbagai input
3. **Templat Arahan**: Pastikan templat arahan dipaparkan dengan betul
4. **Pengesahan Skema**: Uji logik pengesahan parameter
5. **Pengendalian Ralat**: Sahkan respons ralat untuk input tidak sah

#### Amalan Terbaik untuk Ujian Unit

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
# Contoh ujian unit untuk alat kalkulator dalam Python
def test_calculator_tool_add():
    # Susun
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Bertindak
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Sahkan
    assert result["value"] == 12
```

### Ujian Integrasi (Lapisan Tengah)

Ujian integrasi mengesahkan interaksi antara komponen server MCP anda.

#### Apa yang Perlu Diuji

1. **Inisialisasi Server**: Uji permulaan server dengan pelbagai konfigurasi
2. **Pendaftaran Laluan**: Sahkan semua titik akhir didaftarkan dengan betul
3. **Pemprosesan Permintaan**: Uji kitaran penuh permintaan-respons
4. **Propagasi Ralat**: Pastikan ralat diurus dengan betul merentasi komponen
5. **Pengesahan & Kebenaran**: Uji mekanisme keselamatan

#### Amalan Terbaik untuk Ujian Integrasi

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

### Ujian Menyeluruh (Lapisan Atas)

Ujian menyeluruh mengesahkan tingkah laku sistem lengkap dari klien ke server.

#### Apa yang Perlu Diuji

1. **Komunikasi Klien-Server**: Uji kitaran lengkap permintaan-respons
2. **SDK Klien Sebenar**: Uji dengan pelaksanaan klien sebenar
3. **Prestasi Di Bawah Beban**: Sahkan tingkah laku dengan pelbagai permintaan serentak
4. **Pemulihan Ralat**: Uji pemulihan sistem dari kegagalan

5. **Operasi Berjalan Lama**: Sahkan pengendalian penstriman dan operasi panjang

#### Amalan Terbaik untuk Ujian E2E

```typescript
// Contoh ujian E2E dengan klien dalam TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Mulakan pelayan dalam persekitaran ujian
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Bertindak
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Tegaskan
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Strategi Pemalsuan untuk Ujian MCP

Pemalsuan adalah penting untuk mengasingkan komponen semasa ujian.

### Komponen untuk Dipalsukan

1. **Model AI Luaran**: Palsukan respons model untuk ujian yang boleh diramal
2. **Perkhidmatan Luaran**: Palsukan pergantungan API (pangkalan data, perkhidmatan pihak ketiga)
3. **Perkhidmatan Pengesahan**: Palsukan penyedia identiti
4. **Penyedia Sumber**: Palsukan pengendali sumber mahal

### Contoh: Memalsukan Respons Model AI

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
# Contoh Python dengan unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Konfigurasikan mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Gunakan mock dalam ujian
    server = McpServer(model_client=mock_model)
    # Teruskan dengan ujian
```

## Ujian Prestasi

Ujian prestasi adalah penting untuk pelayan MCP produksi.

### Apa yang Perlu Diukur

1. **Kelewatan**: Masa tindak balas bagi permintaan
2. **Aliran Melalui**: Permintaan yang dikendalikan setiap saat
3. **Penggunaan Sumber**: Penggunaan CPU, memori, rangkaian
4. **Pengendalian Serentak**: Tingkah laku di bawah permintaan selari
5. **Ciri Skala**: Prestasi apabila beban bertambah

### Alat untuk Ujian Prestasi

- **k6**: Alat ujian beban sumber terbuka
- **JMeter**: Ujian prestasi menyeluruh
- **Locust**: Ujian beban berasaskan Python
- **Azure Load Testing**: Ujian prestasi berasaskan awan

### Contoh: Ujian Beban Asas dengan k6

```javascript
// skrip k6 untuk ujian beban pelayan MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 pengguna maya
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

## Automasi Ujian untuk Pelayan MCP

Mengautomasikan ujian anda memastikan kualiti konsisten dan gelung maklum balas yang lebih pantas.

### Integrasi CI/CD

1. **Jalankan Ujian Unit pada Permintaan Tarik**: Pastikan perubahan kod tidak memecah fungsi sedia ada
2. **Ujian Integrasi dalam Peringkat Prapengeluaran**: Jalankan ujian integrasi dalam persekitaran pra-produksi
3. **Penanda Aras Prestasi**: Kekalkan penanda aras prestasi untuk mengesan regresi
4. **Imbasan Keselamatan**: Automatikkan ujian keselamatan sebagai sebahagian saluran

### Contoh Saluran CI (GitHub Actions)

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

## Ujian untuk Pematuhan dengan Spesifikasi MCP

Sahkan pelayan anda melaksanakan spesifikasi MCP dengan betul.

### Kawasan Pematuhan Utama

1. **Titik Akhir API**: Uji titik akhir yang diperlukan (/resources, /tools, dll.)
2. **Format Permintaan/Respons**: Sahkan pematuhan skema
3. **Kod Ralat**: Pastikan kod status betul untuk pelbagai senario
4. **Jenis Kandungan**: Uji pengendalian pelbagai jenis kandungan
5. **Aliran Pengesahan**: Sahkan mekanisme pengesahan yang mematuhi spesifikasi

### Set Ujian Pematuhan

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

## 10 Tips Teratas untuk Ujian Pelayan MCP Berkesan

1. **Uji Definisi Alat Secara Berasingan**: Sahkan definisi skema secara bebas daripada logik alat
2. **Gunakan Ujian Berparameter**: Uji alat dengan pelbagai input, termasuk kes tepi
3. **Periksa Respons Ralat**: Pastikan pengendalian ralat yang betul untuk semua keadaan ralat yang mungkin
4. **Uji Logik Pemberian Kebenaran**: Pastikan kawalan akses yang betul untuk peranan pengguna berbeza
5. **Pantau Liputan Ujian**: Sasarkan liputan tinggi bagi kod laluan kritikal
6. **Uji Respons Penstriman**: Sahkan pengendalian kandungan penstriman yang betul
7. **Simulasikan Isu Rangkaian**: Uji tingkah laku di bawah keadaan rangkaian yang lemah
8. **Uji Had Sumber**: Sahkan tingkah laku apabila mencapai kuota atau had kadar
9. **Automatikkan Ujian Regresi**: Bangunkan set ujian yang berjalan pada setiap perubahan kod
10. **Dokumentasikan Kes Ujian**: Kekalkan dokumentasi yang jelas mengenai senario ujian

## Perangkap Ujian Biasa

- **Terlalu bergantung pada ujian laluan bahagia**: Pastikan juga menguji kes ralat dengan teliti
- **Mengabaikan ujian prestasi**: Kenal pasti halangan sebelum menjejaskan produksi
- **Ujian dalam pengasingan sahaja**: Gabungkan ujian unit, integrasi, dan E2E
- **Liputan API tidak lengkap**: Pastikan semua titik akhir dan ciri diuji
- **Persekitaran ujian tidak konsisten**: Gunakan kontena untuk memastikan persekitaran ujian konsisten

## Kesimpulan

Strategi ujian yang komprehensif adalah penting untuk membangunkan pelayan MCP yang boleh dipercayai dan berkualiti tinggi. Dengan melaksanakan amalan terbaik dan petua yang dinyatakan dalam panduan ini, anda boleh memastikan pelaksanaan MCP anda memenuhi piawaian tertinggi kualiti, kebolehpercayaan, dan prestasi.


## Perkara Utama

1. **Reka Bentuk Alat**: Ikuti prinsip tanggungjawab tunggal, gunakan suntikan pergantungan, dan reka bentuk untuk kebolehkomposan
2. **Reka Bentuk Skema**: Cipta skema yang jelas dan didokumenkan dengan baik serta had pengesahan yang sesuai
3. **Pengendalian Ralat**: Laksanakan pengendalian ralat yang anggun, respons ralat berstruktur,
   dan logik cuba semula berasaskan hasil
4. **Prestasi**: Gunakan caching, pemprosesan tak segerak, dan pengekangan sumber
5. **Keselamatan**: Terapkan pengesahan input yang teliti, pemeriksaan kebenaran, dan pengendalian data sensitif
6. **Ujian**: Cipta ujian unit, integrasi, dan hujung-ke-hujung yang komprehensif
7. **Corak Aliran Kerja**: Terapkan corak yang telah ditetapkan seperti rantaian, penghantar, dan pemprosesan selari

## Latihan

Reka alat dan aliran kerja MCP untuk sistem pemprosesan dokumen yang:

1. Menerima dokumen dalam pelbagai format (PDF, DOCX, TXT)
2. Mengekstrak teks dan maklumat utama dari dokumen
3. Mengklasifikasikan dokumen mengikut jenis dan kandungan
4. Menjana ringkasan setiap dokumen

Laksanakan skema alat, pengendalian ralat, dan corak aliran kerja yang paling sesuai untuk senario ini. Pertimbangkan bagaimana anda akan menguji pelaksanaan ini.

## Sumber 

1. Sertai komuniti MCP di [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) untuk kekal dikemas kini tentang perkembangan terkini 
2. Menyumbang kepada projek sumber terbuka [MCP](https://github.com/modelcontextprotocol)
3. Terapkan prinsip MCP dalam inisiatif AI organisasi anda sendiri
4. Terokai pelaksanaan MCP khusus untuk industri anda. 
5. Pertimbangkan mengambil kursus lanjutan tentang topik MCP tertentu, seperti integrasi multi-modal atau integrasi aplikasi perusahaan.
6. Cuba bina alat dan aliran kerja MCP anda sendiri menggunakan prinsip yang dipelajari melalui [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Apa Seterusnya

Seterusnya: [Kajian Kes](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Praktik Terbaik Pengembangan MCP

[![Praktik Terbaik Pengembangan MCP](../../../translated_images/id/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Klik gambar di atas untuk menonton video pelajaran ini)_

## Ikhtisar

Pelajaran ini berfokus pada praktik terbaik lanjutan untuk mengembangkan, menguji, dan menerapkan server dan fitur MCP dalam lingkungan produksi. Seiring ekosistem MCP yang semakin kompleks dan penting, mengikuti pola yang telah ditetapkan memastikan keandalan, kemudahan pemeliharaan, dan interoperabilitas. Pelajaran ini mengkonsolidasikan kebijaksanaan praktis yang diperoleh dari implementasi MCP dunia nyata untuk membimbing Anda dalam menciptakan server yang kuat, efisien dengan sumber daya, prompt, dan alat yang efektif.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menerapkan praktik terbaik industri dalam desain server dan fitur MCP
- Membuat strategi pengujian komprehensif untuk server MCP
- Merancang pola alur kerja efisien dan dapat digunakan ulang untuk aplikasi MCP yang kompleks
- Menerapkan penanganan kesalahan, pencatatan, dan observabilitas yang tepat pada server MCP
- Mengoptimalkan implementasi MCP untuk kinerja, keamanan, dan kemudahan pemeliharaan

## Prinsip Inti MCP

Sebelum menyelami praktik implementasi spesifik, penting untuk memahami prinsip inti yang memandu pengembangan MCP yang efektif:

1. **Komunikasi Standar**: MCP menggunakan JSON-RPC 2.0 sebagai dasarnya, menyediakan format konsisten untuk permintaan, respons, dan penanganan kesalahan di semua implementasi.

2. **Desain Berorientasi Pengguna**: Selalu utamakan persetujuan, kontrol, dan transparansi pengguna dalam implementasi MCP Anda.

3. **Keamanan Utama**: Terapkan langkah keamanan kuat termasuk autentikasi, otorisasi, validasi, dan pembatasan laju.

4. **Arsitektur Modular**: Rancang server MCP Anda dengan pendekatan modular, dimana setiap alat dan sumber daya memiliki tujuan yang jelas dan fokus.

5. **Status Eksplisit**: MCP `2026-07-28` adalah tanpa status pada lapisan protokol.
   Ketika alur kerja membutuhkan status lintas-panggilan, gunakan pegangan eksplisit atau
   argumen alat biasa yang didukung oleh status aplikasi yang tahan lama.

## Praktik Terbaik Resmi MCP

Praktik terbaik berikut diambil dari dokumentasi resmi Model Context Protocol:

### Praktik Terbaik Keamanan

1. **Persetujuan dan Kontrol Pengguna**: Selalu minta persetujuan eksplisit pengguna sebelum mengakses data atau melakukan operasi. Berikan kontrol yang jelas atas data apa yang dibagikan dan tindakan mana yang diizinkan.

2. **Privasi Data**: Hanya ungkapkan data pengguna dengan persetujuan eksplisit dan lindungi dengan kontrol akses yang sesuai. Lindungi dari transmisi data tanpa izin.

3. **Keamanan Alat**: Minta persetujuan eksplisit pengguna sebelum memanggil alat apa pun. Pastikan pengguna memahami fungsi tiap alat dan terapkan batasan keamanan yang kuat.

4. **Kontrol Izin Alat**: Konfigurasikan alat mana yang boleh digunakan model untuk
   setiap permintaan dan konteks otorisasi, memastikan hanya alat yang secara eksplisit diizinkan
   yang dapat diakses.

5. **Autentikasi**: Minta autentikasi yang tepat sebelum memberikan akses ke alat, sumber daya, atau operasi sensitif menggunakan kunci API, token OAuth, atau metode autentikasi aman lainnya.

6. **Validasi Parameter**: Tegakkan validasi untuk semua pemanggilan alat agar mencegah input yang salah format atau berbahaya mencapai implementasi alat.

7. **Pembatasan Laju**: Terapkan pembatasan laju untuk mencegah penyalahgunaan dan memastikan penggunaan sumber daya server yang adil.

### Praktik Terbaik Implementasi

1. **Negosiasi Kapabilitas**: Negosiasikan versi protokol dan
   kapabilitas yang didukung. Dalam MCP `2026-07-28`, setiap permintaan mandiri dan dapat
   menggunakan `server/discover`; revisi lama menggunakan sambutan inisialisasi.

2. **Desain Alat**: Buat alat yang fokus pada satu fungsi dengan baik, daripada alat monolitik yang menangani banyak masalah.

3. **Penanganan Kesalahan**: Terapkan pesan dan kode kesalahan standar untuk membantu mendiagnosis masalah, menangani kegagalan dengan anggun, dan memberikan umpan balik yang dapat ditindaklanjuti.

4. **Observabilitas**: Gunakan `stderr` untuk diagnostik stdio dan OpenTelemetry
   untuk observabilitas terstruktur. Fitur pencatatan MCP dinyatakan usang dalam
   spesifikasi `2026-07-28`.

5. **Pelacakan Progres**: Untuk operasi yang berjalan lama, laporkan pembaruan progres guna mendukung antarmuka pengguna yang responsif.

6. **Pembatalan Permintaan**: Izinkan klien membatalkan permintaan yang sedang berjalan jika sudah tidak dibutuhkan atau memakan waktu terlalu lama.

## Referensi Tambahan

Untuk informasi terbaru tentang praktik terbaik MCP, lihat:

- [Dokumentasi MCP](https://modelcontextprotocol.io/)
- [Spesifikasi MCP (2026-07-28)][mcp-2026-spec]
- [Spesifikasi MCP Sebelumnya (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Ekstensi Tugas MCP][mcp-tasks-extension]
- [Repositori GitHub](https://github.com/modelcontextprotocol)
- [Praktik Terbaik Keamanan](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Risiko keamanan dan mitigasinya
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Pelatihan keamanan praktis

### Pelajaran Pendamping Keandalan

Loop retry generik tidak aman untuk alat yang membuat tiket, pembayaran,
pesan, penyebaran, atau efek dunia nyata lainnya. Sebuah respons dapat hilang
setelah efeknya selesai.

Gunakan pelajaran pendamping keandalan,
[Retry Aman untuk Alat MCP: Pola Reliability Sidecar][reliability-sidecar],
untuk mempelajari kunci operasi stabil, penerimaan ganda, checkpointing,
rekonsiliasi, tingkat bukti, dan injeksi kegagalan.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Contoh Implementasi Praktis

### Praktik Terbaik Desain Alat

#### 1. Prinsip Tanggung Jawab Tunggal

Setiap alat MCP harus memiliki tujuan yang jelas dan fokus. Daripada membuat alat monolitik yang mencoba menangani banyak masalah, kembangkan alat khusus yang unggul dalam tugas tertentu.

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

#### 2. Penanganan Kesalahan Konsisten

Terapkan penanganan kesalahan yang kuat dengan pesan kesalahan informatif dan mekanisme pemulihan yang sesuai.

```python
# Contoh Python dengan penanganan kesalahan yang komprehensif
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Validasi parameter
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Validasi keamanan
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operasi database dengan batas waktu
                async with timeout(10):  # Batas waktu 10 detik
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Kesalahan koneksi mungkin bersifat sementara
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Kesalahan kueri kemungkinan adalah kesalahan klien
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Biarkan kesalahan spesifik alat melewati
            raise
        except Exception as e:
            # Penangkap semua untuk kesalahan yang tidak terduga
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementasi deteksi injeksi SQL
        pass
        
    def _log_error(self, message, error):
        # Implementasi pencatatan kesalahan
        pass
```

#### 3. Validasi Parameter

Selalu validasi parameter secara menyeluruh untuk mencegah input yang salah bentuk atau berbahaya.

```javascript
// Contoh JavaScript/TypeScript dengan validasi parameter yang detail
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
    // 1. Validasi keberadaan parameter
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Validasi tipe parameter
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Validasi nilai parameter
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Validasi keberadaan konten untuk operasi penulisan
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Validasi keamanan jalur
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementasi berdasarkan parameter yang sudah divalidasi
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementasi pemeriksaan keamanan jalur
    // ...
  }
}
```

### Contoh Implementasi Keamanan

#### 1. Autentikasi dan Otorisasi

```java
// Contoh Java dengan autentikasi dan otorisasi
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Penyuntikan dependensi
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
        // 1. Ekstrak konteks autentikasi
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autentikasi pengguna
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Periksa otorisasi untuk operasi tertentu
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Lanjutkan dengan operasi yang diotorisasi
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

#### 2. Pembatasan Laju

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

## Praktik Terbaik Pengujian

### 1. Pengujian Unit Alat MCP

Selalu uji alat Anda secara terpisah dengan memodifikasi ketergantungan eksternal:

```typescript
// Contoh unit test alat menggunakan TypeScript
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Buat layanan cuaca palsu
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Buat alat dengan ketergantungan palsu
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
    
    // Pastikan
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Atur
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Bertindak & Pastikan
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Pengujian Integrasi

Uji alur lengkap dari permintaan klien hingga respons server:

```python
# Contoh pengujian integrasi Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Mulai server pengujian
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Buat klien
        client = McpClient("http://localhost:5000")
        
        # Uji penemuan alat
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Uji eksekusi alat
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verifikasi respons
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Bersihkan
        await server.stop()
```

## Optimasi Kinerja

### 1. Strategi Caching

Terapkan caching yang tepat untuk mengurangi latensi dan penggunaan sumber daya:

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

#### 2. Dependency Injection dan Kemudahan Pengujian

Rancang alat agar menerima ketergantungan melalui konstruktor, membuatnya mudah diuji dan dikonfigurasi:

```java
// Contoh Java dengan penyuntikan ketergantungan
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Ketergantungan disuntikkan melalui konstruktor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementasi alat
    // ...
}
```

#### 3. Alat yang Bisa Disusun

Rancang alat yang dapat disusun bersama untuk membuat alur kerja yang lebih kompleks:

```python
# Contoh Python yang menunjukkan alat yang dapat digabungkan
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementasi...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Alat ini dapat menggunakan hasil dari alat dataFetch
    async def execute_async(self, request):
        # Implementasi...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Alat ini dapat menggunakan hasil dari alat dataAnalysis
    async def execute_async(self, request):
        # Implementasi...
        pass

# Alat ini dapat digunakan secara mandiri atau sebagai bagian dari alur kerja
```

### Praktik Terbaik Desain Skema

Skema adalah kontrak antara model dan alat Anda. Skema yang dirancang dengan baik menghasilkan kemudahan penggunaan alat yang lebih baik.

#### 1. Deskripsi Parameter yang Jelas

Selalu sertakan informasi deskriptif untuk setiap parameter:

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

#### 2. Batasan Validasi

Sertakan batasan validasi untuk mencegah input tidak valid:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Properti email dengan validasi format
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Properti umur dengan batasan numerik
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Properti yang menggunakan enumerasi
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

#### 3. Struktur Return yang Konsisten

Pertahankan konsistensi dalam struktur respons Anda agar model lebih mudah memahami hasil:

```python
async def execute_async(self, request):
    try:
        # Proses permintaan
        results = await self._search_database(request.parameters["query"])
        
        # Selalu kembalikan struktur yang konsisten
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

### Penanganan Kesalahan

Penanganan kesalahan yang kuat sangat penting untuk menjaga keandalan alat MCP.

#### 1. Penanganan Kesalahan dengan Anggun

Tangani kesalahan pada tingkat yang sesuai dan berikan pesan informatif:

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

#### 2. Respons Kesalahan Terstruktur

Kembalikan informasi kesalahan terstruktur bila memungkinkan:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementasi
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
        
        // Lempar ulang pengecualian lain sebagai ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Logika Retry

Gunakan logika retry generik hanya untuk panggilan baca-saja atau operasi yang
kontrak hilirnya sudah idempoten. Untuk operasi berpengaruh, timeout
setelah mengirim permintaan ambigu. Rekonsiliasikan status yang otoritatif dan
gunakan kembali kunci operasi stabil yang sama sebelum menjalankan lagi. Lihat
[pelajaran pendamping reliability sidecar](./reliability-sidecars/README.md).

Loop retry terbatas berikut cocok untuk pencarian baca-saja:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # detik
    
    while retry_count < max_retries:
        try:
            # Memanggil API eksternal yang hanya baca
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Penundaan eksponensial
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Kesalahan non-transien, jangan coba ulang
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Optimasi Kinerja

#### 1. Caching

Terapkan caching untuk operasi mahal:

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

#### 2. Pemrosesan Asinkron

Gunakan pola pemrograman asinkron untuk operasi I/O-bound:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Untuk operasi yang berjalan lama, kembalikan ID pemrosesan segera
        String processId = UUID.randomUUID().toString();
        
        // Mulai pemrosesan async
        CompletableFuture.runAsync(() -> {
            try {
                // Lakukan operasi yang berjalan lama
                documentService.processDocument(documentId);
                
                // Perbarui status (biasanya disimpan dalam basis data)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Kembalikan respons segera dengan ID proses
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Alat pemeriksaan status pendamping
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

#### 3. Pembatasan Sumber Daya

Terapkan pembatasan sumber daya untuk mencegah kelebihan beban:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Izinkan 5 permintaan per detik
            bucket_size=10        # Izinkan lonjakan hingga 10 permintaan
        )
    
    async def execute_async(self, request):
        # Periksa apakah kita bisa melanjutkan atau perlu menunggu
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Jika menunggu terlalu lama
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Tunggu selama waktu tunda yang sesuai
                await asyncio.sleep(delay)
        
        # Gunakan satu token dan lanjutkan dengan permintaan
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
            
            # Hitung waktu hingga token berikutnya tersedia
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Tambahkan token baru berdasarkan waktu yang telah berlalu
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Praktik Terbaik Keamanan

#### 1. Validasi Input

Selalu validasi parameter input secara menyeluruh:

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

#### 2. Pemeriksaan Otorisasi

Terapkan pemeriksaan otorisasi yang tepat:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Dapatkan konteks pengguna dari permintaan
    UserContext user = request.getContext().getUserContext();
    
    // Periksa apakah pengguna memiliki izin yang diperlukan
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Untuk sumber daya tertentu, periksa akses ke sumber daya tersebut
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Lanjutkan dengan eksekusi alat
    // ...
}
```

#### 3. Penanganan Data Sensitif

Tangani data sensitif dengan hati-hati:

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
        
        # Saring bidang sensitif kecuali diminta secara eksplisit DAN berwenang
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Periksa tingkat otorisasi dalam konteks permintaan
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Buat salinan untuk menghindari mengubah yang asli
        redacted = user_data.copy()
        
        # Menyekat bidang sensitif tertentu
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Menyekat data sensitif yang bersarang
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Praktik Terbaik Pengujian untuk Alat MCP

Pengujian komprehensif memastikan alat MCP berfungsi dengan benar, menangani kasus tepi, dan terintegrasi dengan baik ke sistem.

### Pengujian Unit

#### 1. Uji Setiap Alat Secara Terpisah

Buat tes fokus untuk fungsi setiap alat:

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

#### 2. Pengujian Validasi Skema

Uji bahwa skema valid dan menegakkan batasan dengan benar:

```java
@Test
public void testSchemaValidation() {
    // Buat instance alat
    SearchTool searchTool = new SearchTool();
    
    // Dapatkan skema
    Object schema = searchTool.getSchema();
    
    // Konversi skema ke JSON untuk validasi
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Validasi skema adalah JSONSchema yang valid
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Uji parameter yang valid
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Uji parameter yang dibutuhkan hilang
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Uji tipe parameter yang tidak valid
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Tes Penanganan Kesalahan

Buat tes spesifik untuk kondisi kesalahan:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Atur
    tool = ApiTool(timeout=0.1)  # Timeout sangat singkat
    
    # Palsukan permintaan yang akan timeout
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Lebih lama dari timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Lakukan & Periksa
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verifikasi pesan pengecualian
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Atur
    tool = ApiTool()
    
    # Palsukan respons dengan pembatasan laju
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
        
        # Lakukan & Periksa
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verifikasi pengecualian mengandung informasi batas laju
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Pengujian Integrasi

#### 1. Pengujian Rangkaian Alat

Uji alat bekerja bersama dalam kombinasi yang diharapkan:

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

#### 2. Pengujian Server MCP

Uji server MCP dengan pendaftaran dan eksekusi alat lengkap:

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
        
        // Kirim permintaan dan verifikasi respons
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Buat permintaan alat yang tidak valid
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Parameter "b" hilang
        request.put("parameters", parameters);
        
        // Kirim permintaan dan verifikasi respons kesalahan
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Pengujian End-to-End

Uji alur kerja lengkap dari prompt model hingga eksekusi alat:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Atur - Siapkan klien MCP dan model tiruan
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Tirukan respons model
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
    
    # Tirukan respons alat cuaca
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
        
        # Lakukan
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Pastikan
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Pengujian Kinerja

#### 1. Pengujian Beban

Uji berapa banyak permintaan bersamaan yang dapat ditangani server MCP Anda:

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

#### 2. Pengujian Stres

Uji sistem di bawah beban ekstrem:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Siapkan JMeter untuk pengujian stres
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigurasikan rencana pengujian JMeter
    HashTree testPlanTree = new HashTree();
    
    // Buat rencana pengujian, grup thread, sampler, dll.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Tambahkan sampler HTTP untuk eksekusi alat
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Tambahkan pendengar
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Jalankan pengujian
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Validasi hasil
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Waktu respons rata-rata < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // Persentil ke-90 < 500ms
}
```

#### 3. Monitoring dan Profiling

Siapkan monitoring untuk analisis kinerja jangka panjang:

```python
# Konfigurasikan pemantauan untuk server MCP
def configure_monitoring(server):
    # Atur metrik Prometheus
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
    
    # Tambahkan middleware untuk pengukuran waktu dan pencatatan metrik
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Buka endpoint metrik
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Pola Desain Alur Kerja MCP

Alur kerja MCP yang dirancang dengan baik meningkatkan efisiensi, keandalan, dan kemudahan pemeliharaan. Berikut pola utama yang harus diikuti:

### 1. Pola Rangkaian Alat

Hubungkan beberapa alat berurutan dimana keluaran tiap alat menjadi masukan alat berikutnya:

```python
# Implementasi Rangkaian Alat Python
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Daftar nama alat untuk dijalankan secara berurutan
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Jalankan setiap alat dalam rantai, meneruskan hasil sebelumnya
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Simpan hasil dan gunakan sebagai input untuk alat berikutnya
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

### 2. Pola Dispatcher

Gunakan alat sentral yang mengarahkan ke alat khusus berdasarkan masukan:

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

### 3. Pola Pemrosesan Paralel

Jalankan beberapa alat secara bersamaan untuk efisiensi:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Langkah 1: Ambil metadata dataset (sinkron)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Langkah 2: Jalankan beberapa analisis secara paralel
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
        
        // Tunggu semua tugas paralel selesai
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Tunggu hingga selesai
        
        // Langkah 3: Gabungkan hasil
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Langkah 4: Buat laporan ringkasan
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Kembalikan hasil alur kerja lengkap
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Pola Pemulihan Kesalahan

Terapkan fallback anggun untuk kegagalan alat:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Coba alat utama terlebih dahulu
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Catat kegagalan
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Beralih ke alat sekunder
            try:
                # Mungkin perlu mengubah parameter untuk alat cadangan
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Kedua alat gagal
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Implementasi ini akan bergantung pada alat spesifik
        # Untuk contoh ini, kita hanya akan mengembalikan parameter asli
        return params

# Contoh penggunaan
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API cuaca utama (berbayar)
        "basicWeatherService",    # API cuaca cadangan (gratis)
        {"location": location}
    )
```

### 5. Pola Komposisi Alur Kerja

Bangun alur kerja kompleks dengan menyusun alur kerja sederhana:

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

# Pengujian Server MCP: Praktik Terbaik dan Tips Teratas

## Ikhtisar

Pengujian adalah aspek penting dalam mengembangkan server MCP yang andal dan berkualitas tinggi. Panduan ini menyediakan praktik terbaik dan tips komprehensif untuk menguji server MCP Anda sepanjang siklus pengembangan, dari pengujian unit, pengujian integrasi, hingga validasi end-to-end.

## Mengapa Pengujian Penting untuk Server MCP

Server MCP berfungsi sebagai middleware penting antara model AI dan aplikasi klien. Pengujian menyeluruh memastikan:

- Keandalan dalam lingkungan produksi
- Penanganan permintaan dan respons yang akurat
- Implementasi spesifikasi MCP yang tepat
- Ketahanan terhadap kegagalan dan kasus tepi
- Performa konsisten di berbagai beban

## Pengujian Unit untuk Server MCP

### Pengujian Unit (Fondasi)

Pengujian unit memverifikasi komponen individual server MCP Anda secara terpisah.

#### Apa yang Diuji

1. **Penangkap Sumber Daya**: Uji logika setiap penangkap sumber daya secara independen
2. **Implementasi Alat**: Verifikasi perilaku alat dengan berbagai masukan
3. **Template Prompt**: Pastikan template prompt dirender dengan benar
4. **Validasi Skema**: Uji logika validasi parameter
5. **Penanganan Kesalahan**: Verifikasi respons kesalahan untuk masukan tidak valid

#### Praktik Terbaik untuk Pengujian Unit

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
# Contoh unit test untuk alat kalkulator dalam Python
def test_calculator_tool_add():
    # Menyusun
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Bertindak
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Memastikan
    assert result["value"] == 12
```

### Pengujian Integrasi (Lapisan Tengah)

Pengujian integrasi memverifikasi interaksi antar komponen server MCP Anda.

#### Apa yang Diuji

1. **Inisialisasi Server**: Uji startup server dengan konfigurasi berbeda
2. **Pendaftaran Route**: Verifikasi semua endpoint terdaftar dengan benar
3. **Pemrosesan Permintaan**: Uji siklus permintaan-respons penuh
4. **Propagasi Kesalahan**: Pastikan kesalahan tertangani dengan baik antar komponen
5. **Autentikasi & Otorisasi**: Uji mekanisme keamanan

#### Praktik Terbaik untuk Pengujian Integrasi

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

### Pengujian End-to-End (Lapisan Teratas)

Pengujian end-to-end memverifikasi perilaku sistem lengkap dari klien ke server.

#### Apa yang Diuji

1. **Komunikasi Klien-Server**: Uji siklus permintaan-respons lengkap
2. **SDK Klien Asli**: Uji dengan implementasi klien sebenarnya
3. **Performa di Bawah Beban**: Verifikasi perilaku dengan banyak permintaan simultan
4. **Pemulihan dari Kesalahan**: Uji pemulihan sistem dari kegagalan

5. **Operasi Berjalan Lama**: Verifikasi penanganan streaming dan operasi panjang

#### Praktik Terbaik untuk Pengujian E2E

```typescript
// Contoh tes E2E dengan klien dalam TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Mulai server di lingkungan pengujian
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Lakukan aksi
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Pastikan hasil
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Strategi Mocking untuk Pengujian MCP

Mocking sangat penting untuk mengisolasi komponen selama pengujian.

### Komponen yang Harus Dimock

1. **Model AI Eksternal**: Mock respons model untuk pengujian yang dapat diprediksi
2. **Layanan Eksternal**: Mock dependensi API (basis data, layanan pihak ketiga)
3. **Layanan Autentikasi**: Mock penyedia identitas
4. **Penyedia Sumber Daya**: Mock pengelola sumber daya mahal

### Contoh: Mock Respons Model AI

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
    
    # Gunakan mock dalam pengujian
    server = McpServer(model_client=mock_model)
    # Lanjutkan dengan pengujian
```

## Pengujian Performa

Pengujian performa sangat krusial untuk server MCP produksi.

### Apa yang Diukur

1. **Latensi**: Waktu respons untuk permintaan
2. **Throughput**: Permintaan yang ditangani per detik
3. **Pemanfaatan Sumber Daya**: Penggunaan CPU, memori, jaringan
4. **Penanganan Konkuren**: Perilaku di bawah permintaan paralel
5. **Karakteristik Skalabilitas**: Performa saat beban meningkat

### Alat untuk Pengujian Performa

- **k6**: Alat pengujian beban sumber terbuka
- **JMeter**: Pengujian performa komprehensif
- **Locust**: Pengujian beban berbasis Python
- **Azure Load Testing**: Pengujian performa berbasis cloud

### Contoh: Uji Beban Dasar dengan k6

```javascript
// skrip k6 untuk pengujian beban server MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 pengguna virtual
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

## Automasi Pengujian untuk Server MCP

Mengotomasi pengujian memastikan kualitas yang konsisten dan siklus umpan balik yang lebih cepat.

### Integrasi CI/CD

1. **Jalankan Unit Test pada Pull Request**: Pastikan perubahan kode tidak merusak fungsi yang ada
2. **Tes Integrasi di Staging**: Jalankan tes integrasi di lingkungan pra-produksi
3. **Baseline Performa**: Pertahankan tolok ukur performa untuk menangkap regresi
4. **Pemeriksaan Keamanan**: Otomatiskan pengujian keamanan sebagai bagian dari pipeline

### Contoh Pipeline CI (GitHub Actions)

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

## Pengujian Kepatuhan terhadap Spesifikasi MCP

Verifikasi server Anda mengimplementasikan spesifikasi MCP dengan benar.

### Area Kepatuhan Utama

1. **Endpoint API**: Uji endpoint yang diperlukan (/resources, /tools, dll.)
2. **Format Permintaan/Respons**: Validasi kepatuhan skema
3. **Kode Kesalahan**: Verifikasi kode status yang benar untuk berbagai skenario
4. **Jenis Konten**: Uji penanganan jenis konten berbeda
5. **Alur Autentikasi**: Verifikasi mekanisme otentikasi sesuai spesifikasi

### Suite Pengujian Kepatuhan

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

## 10 Tips Teratas untuk Pengujian Server MCP yang Efektif

1. **Uji Definisi Alat Secara Terpisah**: Verifikasi definisi skema secara mandiri dari logika alat
2. **Gunakan Tes Parameterized**: Uji alat dengan berbagai input, termasuk kasus tepi
3. **Periksa Respons Kesalahan**: Verifikasi penanganan kesalahan yang tepat untuk semua kondisi kesalahan
4. **Uji Logika Otorisasi**: Pastikan kontrol akses yang tepat untuk berbagai peran pengguna
5. **Pantau Cakupan Tes**: Upayakan cakupan tinggi pada kode jalur kritis
6. **Uji Respons Streaming**: Verifikasi penanganan konten streaming yang tepat
7. **Simulasikan Masalah Jaringan**: Uji perilaku di bawah kondisi jaringan yang buruk
8. **Uji Batas Sumber Daya**: Verifikasi perilaku saat mencapai kuota atau batas laju
9. **Otomatiskan Tes Regresi**: Bangun suite yang berjalan di setiap perubahan kode
10. **Dokumentasikan Kasus Tes**: Pertahankan dokumentasi yang jelas dari skenario pengujian

## Kesalahan Umum dalam Pengujian

- **Terlalu mengandalkan pengujian jalur bahagia**: Pastikan menguji kasus kesalahan secara menyeluruh
- **Mengabaikan pengujian performa**: Identifikasi hambatan sebelum mempengaruhi produksi
- **Hanya menguji secara terisolasi**: Gabungkan unit, integrasi, dan tes E2E
- **Cakupan API tidak lengkap**: Pastikan semua endpoint dan fitur diuji
- **Lingkungan uji yang tidak konsisten**: Gunakan kontainer untuk memastikan lingkungan uji yang konsisten

## Kesimpulan

Strategi pengujian yang komprehensif sangat penting untuk mengembangkan server MCP yang andal dan berkualitas tinggi. Dengan menerapkan praktik terbaik dan tips yang dijabarkan dalam panduan ini, Anda dapat memastikan implementasi MCP Anda memenuhi standar tertinggi kualitas, keandalan, dan performa.


## Pokok-pokok Penting

1. **Desain Alat**: Ikuti prinsip tanggung jawab tunggal, gunakan dependency injection, dan desain untuk komposabilitas
2. **Desain Skema**: Buat skema yang jelas dan terdokumentasi dengan batasan validasi yang tepat
3. **Penanganan Kesalahan**: Terapkan penanganan kesalahan yang anggun, respons kesalahan terstruktur,
   dan logika retry yang sadar hasil
4. **Performa**: Gunakan caching, pemrosesan asinkron, dan pembatasan sumber daya
5. **Keamanan**: Terapkan validasi input menyeluruh, pemeriksaan otorisasi, dan penanganan data sensitif
6. **Pengujian**: Buat tes unit, integrasi, dan end-to-end yang komprehensif
7. **Pola Alur Kerja**: Terapkan pola yang sudah mapan seperti rantai, dispatcher, dan pemrosesan paralel

## Latihan

Rancang alat MCP dan alur kerja untuk sistem pemrosesan dokumen yang:

1. Menerima dokumen dalam berbagai format (PDF, DOCX, TXT)
2. Mengekstrak teks dan informasi kunci dari dokumen
3. Mengklasifikasikan dokumen berdasarkan jenis dan isi
4. Membuat ringkasan dari setiap dokumen

Implementasikan skema alat, penanganan kesalahan, dan pola alur kerja yang paling sesuai dengan skenario ini. Pertimbangkan bagaimana Anda akan menguji implementasi ini.

## Sumber Daya 

1. Bergabunglah dengan komunitas MCP di [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) untuk tetap mendapatkan informasi terbaru
2. Berkontribusi pada proyek sumber terbuka [MCP](https://github.com/modelcontextprotocol)
3. Terapkan prinsip MCP dalam inisiatif AI organisasi Anda sendiri
4. Jelajahi implementasi MCP khusus untuk industri Anda.
5. Pertimbangkan mengambil kursus lanjutan tentang topik MCP spesifik, seperti integrasi multi-modal atau integrasi aplikasi enterprise.
6. Bereksperimen dengan membangun alat dan alur kerja MCP Anda sendiri menggunakan prinsip yang dipelajari melalui [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

## Selanjutnya

Selanjutnya: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
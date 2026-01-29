# Nejlepší postupy pro vývoj MCP

[![Nejlepší postupy pro vývoj MCP](../../../translated_images/cs/09.d0f6d86c9d72134ccf5a8d8c8650a0557e519936661fc894cad72d73522227cb.png)](https://youtu.be/W56H9W7x-ao)

_(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

## Přehled

Tato lekce se zaměřuje na pokročilé nejlepší postupy pro vývoj, testování a nasazení MCP serverů a funkcí v produkčním prostředí. Jak ekosystémy MCP rostou na složitosti a významu, dodržování zavedených vzorců zajišťuje spolehlivost, udržovatelnost a interoperabilitu. Tato lekce shrnuje praktické zkušenosti získané z reálných implementací MCP, aby vás vedla při vytváření robustních a efektivních serverů s účinnými zdroji, výzvami a nástroji.

## Cíle učení

Na konci této lekce budete schopni:

- Aplikovat nejlepší postupy v oboru při návrhu MCP serverů a funkcí
- Vytvořit komplexní strategie testování MCP serverů
- Navrhnout efektivní a znovupoužitelné pracovní vzory pro složité aplikace MCP
- Implementovat správné zpracování chyb, logování a sledování v MCP serverech
- Optimalizovat implementace MCP pro výkon, bezpečnost a udržovatelnost

## Základní principy MCP

Než se ponoříme do konkrétních implementačních postupů, je důležité pochopit základní principy, které vedou efektivní vývoj MCP:

1. **Standardizovaná komunikace**: MCP využívá JSON-RPC 2.0 jako svůj základ, což poskytuje konzistentní formát pro požadavky, odpovědi a zpracování chyb napříč všemi implementacemi.

2. **Uživatelsky orientovaný design**: Vždy upřednostňujte souhlas, kontrolu a transparentnost uživatele ve vašich implementacích MCP.

3. **Bezpečnost na prvním místě**: Implementujte robustní bezpečnostní opatření včetně autentizace, autorizace, validace a omezení rychlosti.

4. **Modulární architektura**: Navrhujte MCP servery s modulárním přístupem, kde každý nástroj a zdroj má jasný a zaměřený účel.

5. **Stavové připojení**: Využijte schopnost MCP udržovat stav napříč více požadavky pro koherentnější a kontextově uvědomělé interakce.

## Oficiální nejlepší postupy MCP

Následující nejlepší postupy jsou odvozeny z oficiální dokumentace Model Context Protocol:

### Nejlepší postupy pro bezpečnost

1. **Souhlas a kontrola uživatele**: Vždy vyžadujte explicitní souhlas uživatele před přístupem k datům nebo prováděním operací. Poskytněte jasnou kontrolu nad tím, jaká data jsou sdílena a jaké akce jsou autorizovány.

2. **Ochrana soukromí dat**: Zveřejňujte uživatelská data pouze s explicitním souhlasem a chraňte je vhodnými přístupovými kontrolami. Zabraňte neoprávněnému přenosu dat.

3. **Bezpečnost nástrojů**: Vyžadujte explicitní souhlas uživatele před spuštěním jakéhokoliv nástroje. Zajistěte, aby uživatelé rozuměli funkcionalitě každého nástroje, a prosazujte robustní bezpečnostní hranice.

4. **Kontrola oprávnění nástrojů**: Nakonfigurujte, které nástroje může model během relace používat, a zajistěte, že jsou přístupné pouze explicitně autorizované nástroje.

5. **Autentizace**: Vyžadujte správnou autentizaci před udělením přístupu k nástrojům, zdrojům nebo citlivým operacím pomocí API klíčů, OAuth tokenů nebo jiných bezpečných metod autentizace.

6. **Validace parametrů**: Prosazujte validaci pro všechny spuštěné nástroje, abyste zabránili chybným nebo škodlivým vstupům.

7. **Omezení rychlosti**: Implementujte omezení rychlosti, abyste zabránili zneužití a zajistili spravedlivé využití serverových zdrojů.

### Nejlepší postupy pro implementaci

1. **Vyjednávání schopností**: Během nastavení připojení si vyměňte informace o podporovaných funkcích, verzích protokolu, dostupných nástrojích a zdrojích.

2. **Návrh nástrojů**: Vytvářejte zaměřené nástroje, které dělají jednu věc dobře, místo monolitických nástrojů, které řeší více problémů najednou.

3. **Zpracování chyb**: Implementujte standardizované chybové zprávy a kódy, které pomohou diagnostikovat problémy, elegantně zvládat selhání a poskytovat akční zpětnou vazbu.

4. **Logování**: Nakonfigurujte strukturované logy pro auditování, ladění a monitorování interakcí protokolu.

5. **Sledování pokroku**: U dlouhotrvajících operací hlaste aktualizace pokroku, aby bylo možné vytvořit responzivní uživatelská rozhraní.

6. **Zrušení požadavků**: Umožněte klientům zrušit probíhající požadavky, které již nejsou potřeba nebo trvají příliš dlouho.

## Další odkazy

Pro nejaktuálnější informace o nejlepších postupech MCP se podívejte na:

- [Dokumentace MCP](https://modelcontextprotocol.io/)
- [Specifikace MCP](https://spec.modelcontextprotocol.io/)
- [GitHub repozitář](https://github.com/modelcontextprotocol)
- [Nejlepší postupy pro bezpečnost](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)

## Praktické příklady implementace

### Nejlepší postupy pro návrh nástrojů

#### 1. Princip jediné odpovědnosti

Každý nástroj MCP by měl mít jasný a zaměřený účel. Místo vytváření monolitických nástrojů, které se snaží řešit více problémů, vyvíjejte specializované nástroje, které vynikají v konkrétních úkolech.

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

#### 2. Konzistentní zpracování chyb

Implementujte robustní zpracování chyb s informativními chybovými zprávami a vhodnými mechanismy obnovy.

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

#### 3. Validace parametrů

Vždy důkladně validujte parametry, abyste zabránili chybným nebo škodlivým vstupům.

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

### Příklady implementace bezpečnosti

#### 1. Autentizace a autorizace

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

#### 2. Omezení rychlosti

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

...
3. **Výkonnostní základny**: Udržujte výkonnostní benchmarky, abyste odhalili regresi
4. **Bezpečnostní skeny**: Automatizujte bezpečnostní testování jako součást pipeline

### Příklad CI pipeline (GitHub Actions)

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

## Testování souladu se specifikací MCP

Ověřte, že váš server správně implementuje specifikaci MCP.

### Klíčové oblasti souladu

1. **API koncové body**: Testujte požadované koncové body (/resources, /tools, atd.)
2. **Formát požadavků/odpovědí**: Ověřte soulad se schématem
3. **Chybové kódy**: Ověřte správné status kódy pro různé scénáře
4. **Typy obsahu**: Testujte zpracování různých typů obsahu
5. **Autentizační proces**: Ověřte mechanismy autentizace v souladu se specifikací

### Testovací sada pro soulad

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

## Top 10 tipů pro efektivní testování MCP serveru

1. **Testujte definice nástrojů samostatně**: Ověřte schémata nezávisle na logice nástrojů
2. **Používejte parametrizované testy**: Testujte nástroje s různými vstupy, včetně hraničních případů
3. **Kontrolujte chybové odpovědi**: Ověřte správné zpracování všech možných chybových stavů
4. **Testujte logiku autorizace**: Zajistěte správnou kontrolu přístupu pro různé uživatelské role
5. **Sledujte pokrytí testů**: Usilujte o vysoké pokrytí kritického kódu
6. **Testujte streamované odpovědi**: Ověřte správné zpracování streamovaného obsahu
7. **Simulujte problémy sítě**: Testujte chování při špatných síťových podmínkách
8. **Testujte limity zdrojů**: Ověřte chování při dosažení kvót nebo limitů rychlosti
9. **Automatizujte regresní testy**: Vytvořte sadu, která se spouští při každé změně kódu
10. **Dokumentujte testovací případy**: Udržujte jasnou dokumentaci testovacích scénářů

## Běžné chyby při testování

- **Přílišná závislost na testování "šťastné cesty"**: Ujistěte se, že důkladně testujete chybové případy
- **Ignorování výkonnostního testování**: Identifikujte úzká místa dříve, než ovlivní produkci
- **Testování pouze v izolaci**: Kombinujte jednotkové, integrační a E2E testy
- **Neúplné pokrytí API**: Zajistěte testování všech koncových bodů a funkcí
- **Nekonzistentní testovací prostředí**: Používejte kontejnery pro zajištění konzistentního prostředí

## Závěr

Komplexní testovací strategie je klíčová pro vývoj spolehlivých a kvalitních MCP serverů. Implementací osvědčených postupů a tipů uvedených v tomto průvodci můžete zajistit, že vaše implementace MCP splňují nejvyšší standardy kvality, spolehlivosti a výkonu.

## Klíčové poznatky

1. **Návrh nástrojů**: Dodržujte princip jedné odpovědnosti, používejte injekci závislostí a navrhujte pro kompozici
2. **Návrh schémat**: Vytvářejte jasná, dobře dokumentovaná schémata s vhodnými validačními omezeními
3. **Zpracování chyb**: Implementujte elegantní zpracování chyb, strukturované chybové odpovědi a logiku opakování
4. **Výkon**: Používejte caching, asynchronní zpracování a omezení zdrojů
5. **Bezpečnost**: Aplikujte důkladnou validaci vstupů, kontroly autorizace a zpracování citlivých dat
6. **Testování**: Vytvářejte komplexní jednotkové, integrační a end-to-end testy
7. **Vzory pracovních postupů**: Aplikujte osvědčené vzory jako řetězce, dispečery a paralelní zpracování

## Cvičení

Navrhněte MCP nástroj a pracovní postup pro systém zpracování dokumentů, který:

1. Přijímá dokumenty v různých formátech (PDF, DOCX, TXT)
2. Extrahuje text a klíčové informace z dokumentů
3. Klasifikuje dokumenty podle typu a obsahu
4. Generuje shrnutí každého dokumentu

Implementujte schémata nástrojů, zpracování chyb a pracovní postup, který nejlépe vyhovuje tomuto scénáři. Zvažte, jak byste testovali tuto implementaci.

## Zdroje

1. Připojte se ke komunitě MCP na [Azure AI Foundry Discord Community](https://aka.ms/foundrydevs), abyste byli informováni o nejnovějším vývoji
2. Přispívejte do open-source [MCP projektů](https://github.com/modelcontextprotocol)
3. Aplikujte principy MCP ve vlastních AI iniciativách vaší organizace
4. Prozkoumejte specializované implementace MCP pro váš průmysl
5. Zvažte absolvování pokročilých kurzů na specifická témata MCP, jako je multimodální integrace nebo integrace podnikových aplikací
6. Experimentujte s vytvářením vlastních MCP nástrojů a pracovních postupů pomocí principů naučených prostřednictvím [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)

Další: Osvědčené postupy [případové studie](../09-CaseStudy/README.md)

**Upozornění**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
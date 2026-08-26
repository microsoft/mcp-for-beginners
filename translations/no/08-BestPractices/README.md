# MCP Utviklings Beste Praksiser

[![MCP Utviklings Beste Praksiser](../../../translated_images/no/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

## Oversikt

Denne leksjonen fokuserer på avanserte beste praksiser for utvikling, testing og distribusjon av MCP-servere og funksjoner i produksjonsmiljøer. Etter hvert som MCP-økosystemer blir mer komplekse og viktige, sikrer det å følge etablerte mønstre pålitelighet, vedlikeholdbarhet og interoperabilitet. Denne leksjonen samler praktisk visdom fra virkelige MCP-implementasjoner for å veilede deg i å lage robuste, effektive servere med effektive ressurser, prompts og verktøy.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Anvende bransjens beste praksiser i design av MCP-servere og funksjoner
- Lage omfattende teststrategier for MCP-servere
- Designe effektive, gjenbrukbare arbeidsflytmønstre for komplekse MCP-applikasjoner
- Implementere korrekt feilhåndtering, logging og observabilitet i MCP-servere
- Optimalisere MCP-implementasjoner for ytelse, sikkerhet og vedlikeholdbarhet

## MCP Kjerneprinsipper

Før vi dykker ned i spesifikke implementeringspraksiser, er det viktig å forstå kjerneprinsippene som leder effektiv MCP-utvikling:

1. **Standardisert Kommunikasjon**: MCP bruker JSON-RPC 2.0 som grunnlag, og gir et konsekvent format for forespørsler, svar og feilhåndtering på tvers av alle implementasjoner.

2. **Brukersentrert Design**: Prioriter alltid brukerens samtykke, kontroll og åpenhet i dine MCP-implementasjoner.

3. **Sikkerhet Først**: Implementer robuste sikkerhetstiltak inkludert autentisering, autorisasjon, validering og begrensning av forespørselsfrekvens.

4. **Modulær Arkitektur**: Design dine MCP-servere med en modulær tilnærming, hvor hvert verktøy og ressurs har et klart, fokusert formål.

5. **Eksplisitt Tilstand**: MCP `2026-07-28` er tilstandsløs på protokollnivå.
   Når en arbeidsflyt trenger tilstand på tvers av kall, bruk eksplisitte håndtak eller
   vanlige verktøysargumenter støttet av varig applikasjonstilstand.

## Offisielle MCP Beste Praksiser

Følgende beste praksiser er avledet fra den offisielle Model Context Protocol dokumentasjonen:

### Sikkerhets Beste Praksiser

1. **Brukersamtykke og Kontroll**: Krev alltid eksplisitt brukersamtykke før du får tilgang til data eller utfører operasjoner. Gi klar kontroll over hvilke data som deles og hvilke handlinger som er autorisert.

2. **Datapersonvern**: Eksponer kun brukerdata med eksplisitt samtykke og beskytt det med passende tilgangskontroller. Beskytt mot uautorisert datatransmisjon.

3. **Verktøysikkerhet**: Krev eksplisitt brukersamtykke før du påkaller noe verktøy. Sørg for at brukerne forstår hvert verktøys funksjonalitet og håndhev robuste sikkerhetsgrenser.

4. **Verktøystillatelseskontroll**: Konfigurer hvilke verktøy en modell kan bruke for
   hver forespørsel og autorisasjonskontekst, slik at bare eksplisitt autoriserte
   verktøy er tilgjengelige.

5. **Autentisering**: Krev korrekt autentisering før du gir tilgang til verktøy, ressurser eller sensitive operasjoner ved bruk av API-nøkler, OAuth-tokens eller andre sikre autentiseringsmetoder.

6. **Parameter Validering**: Håndhev validering for alle verktøypårop for å forhindre feilformet eller ondsinnet input fra å nå verktøyimplementeringene.

7. **Begrensning av forespørselsfrekvens**: Implementer begrensning av forespørselsfrekvens for å forhindre misbruk og sikre rettferdig bruk av serverressurser.

### Implementerings Beste Praksiser

1. **Funksjonsforhandling**: Forhandle støttede protokollversjoner og
   funksjoner. I MCP `2026-07-28` er hver forespørsel selvstendig og kan
   bruke `server/discover`; eldre revisjoner bruker initialiseringshåndtrykket.

2. **Verktøydesign**: Lag fokuserte verktøy som gjør én ting godt, istedenfor monolittiske verktøy som håndterer flere bekymringer.

3. **Feilhåndtering**: Implementer standardiserte feilmeldinger og -koder for å hjelpe med å diagnostisere problemer, håndtere feil på en elegant måte og gi handlingsrettet tilbakemelding.

4. **Observabilitet**: Bruk `stderr` for stdio-diagnostikk og OpenTelemetry
   for strukturert observabilitet. MCP logging-funksjonen er avskrevet i
   `2026-07-28` spesifikasjonen.

5. **Fremdriftssporing**: For langvarige operasjoner, rapporter fremdriftsoppdateringer for å muliggjøre responsive brukergrensesnitt.

6. **Kansellering av Forespørsler**: Tillat klienter å kansellere pågående forespørsler som ikke lengre er nødvendige eller tar for lang tid.

## Ytterligere Referanser

For den mest oppdaterte informasjonen om MCP beste praksiser, se:

- [MCP Dokumentasjon](https://modelcontextprotocol.io/)
- [MCP Spesifikasjon (2026-07-28)][mcp-2026-spec]
- [Forrige MCP Spesifikasjon (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Oppgaveutvidelse][mcp-tasks-extension]
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [Sikkerhets Beste Praksiser](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Topp 10](https://microsoft.github.io/mcp-azure-security-guide/) - Sikkerhetsrisikoer og mitigering
- [MCP Sikkerhetstoppmøte Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktisk sikkerhetstrening

### Pålitelighets Følgeleksjon

Generiske retry-løkker er usikre for verktøy som lager billetter, betalinger,
meldinger, distribusjoner eller andre virkelige effekter. Et svar kan gå tapt
etter at effekten har blitt utført.

Bruk pålitelighets-følgeleksjonen,
[Sikre Retry for MCP Verktøy: Et Pålitelighets Sidecar-mønster][reliability-sidecar],
for å lære stabile operasjonsnøkler, duplikatopptak, checkpointing,
forsoning, bevisnivåer og feilinjeksjon.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Praktiske Implementeringseksempler

### Verktøydesign Beste Praksiser

#### 1. Enkelt Ansvar Prinsipp

Hvert MCP-verktøy bør ha et klart og fokusert formål. I stedet for å lage monolittiske verktøy som prøver å håndtere flere bekymringer, utvikle spesialiserte verktøy som utmerker seg på spesifikke oppgaver.

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

#### 2. Konsistent Feilhåndtering

Implementer robust feilhåndtering med informative feilmeldinger og passende gjenopprettingsmekanismer.

```python
# Python-eksempel med omfattende feilhåndtering
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Parametervalidering
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Sikkerhetsvalidering
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Databaseoperasjon med tidsavbrudd
                async with timeout(10):  # 10 sekunders tidsavbrudd
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Tilkoblingsfeil kan være midlertidige
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Spørringsfeil er sannsynligvis klientfeil
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # La verktøyspesifikke feil gå gjennom
            raise
        except Exception as e:
            # Fangst for uventede feil
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementering av påvisning av SQL-injeksjon
        pass
        
    def _log_error(self, message, error):
        # Implementering av feillogging
        pass
```

#### 3. Parameter Validering

Alltid valider parametere grundig for å forhindre feilformet eller ondsinnet input.

```javascript
// JavaScript/TypeScript-eksempel med detaljert parametervalidering
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
    // 1. Valider tilstedeværelse av parameter
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Valider parametertyper
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Valider parameterverdier
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Valider innholdstilstedeværelse for skriveoperasjon
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Valideringssikkerhet for sti
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementering basert på validerte parametere
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementering av sikkerhetssjekk for sti
    // ...
  }
}
```

### Sikkerhetsimplementeringseksempler

#### 1. Autentisering og Autorisasjon

```java
// Java-eksempel med autentisering og autorisasjon
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Avhengighetsinjeksjon
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
        // 1. Hent ut autentiseringskontekst
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autentiser bruker
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Sjekk autorisasjon for den spesifikke operasjonen
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Fortsett med autorisert operasjon
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

#### 2. Begrensning av Forespørselsfrekvens

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

## Beste Praksiser for Testing

### 1. Enhetstesting av MCP-Verktøy

Test alltid dine verktøy i isolasjon, ved å mocke eksterne avhengigheter:

```typescript
// TypeScript-eksempel på en enhetstest for verktøy
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Opprett en falsk vær-tjeneste
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Opprett verktøyet med den falske avhengigheten
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Arranger
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Utfør
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Bekreft
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Arranger
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Utfør og bekreft
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Integrasjonstesting

Test hele flyten fra klientforespørsler til serversvar:

```python
# Python integrasjonstest eksempel
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Start en testserver
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Opprett en klient
        client = McpClient("http://localhost:5000")
        
        # Test verktøyoppdagelse
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Test verktøykjøring
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verifiser respons
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Rydd opp
        await server.stop()
```

## Ytelsesoptimalisering

### 1. Cache-strategier

Implementer passende caching for å redusere forsinkelse og ressursbruk:

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

#### 2. Avhengighetsinjeksjon og Testbarhet

Design verktøy til å motta sine avhengigheter gjennom konstruktørinjeksjon, slik at de blir testbare og konfigurerbare:

```java
// Java-eksempel med avhengighetsinjeksjon
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Avhengigheter injisert gjennom konstruktør
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Verktøyimplementasjon
    // ...
}
```

#### 3. Komponerbare Verktøy

Design verktøy som kan komponeres sammen for å lage mer komplekse arbeidsflyter:

```python
# Python-eksempel som viser sammenstillbare verktøy
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementering...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Dette verktøyet kan bruke resultater fra dataFetch-verktøyet
    async def execute_async(self, request):
        # Implementering...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Dette verktøyet kan bruke resultater fra dataAnalysis-verktøyet
    async def execute_async(self, request):
        # Implementering...
        pass

# Disse verktøyene kan brukes uavhengig eller som en del av en arbeidsflyt
```

### Skjema Design Beste Praksiser

Skjemaet er kontrakten mellom modellen og ditt verktøy. Godt designede skjemaer fører til bedre verktøybrukervennlighet.

#### 1. Klare Parameterbeskrivelser

Inkluder alltid beskrivende informasjon for hver parameter:

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

#### 2. Valideringsbegrensninger

Inkluder valideringsbegrensninger for å forhindre ugyldige input:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // E-postegenskap med formatvalidering
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Alderseiendom med numeriske begrensninger
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Enumerert eiendom
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

#### 3. Konsistente Returstrukturer

Oppretthold konsistens i dine responsstrukturer for å gjøre det enklere for modeller å tolke resultater:

```python
async def execute_async(self, request):
    try:
        # Behandle forespørsel
        results = await self._search_database(request.parameters["query"])
        
        # Returner alltid en konsistent struktur
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

### Feilhåndtering

Robust feilhåndtering er avgjørende for MCP-verktøy for å opprettholde pålitelighet.

#### 1. Elegant Feilhåndtering

Håndter feil på passende nivåer og gi informative meldinger:

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

#### 2. Strukturerte Feilresponser

Returner strukturert feilinformasjon når mulig:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementering
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
        
        // Kast andre unntak på nytt som ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Retry-Logikk

Bruk generisk retry-logikk kun for lesebaserte kall eller operasjoner hvis
nedstrøms kontrakt allerede er idempotent. For effektfulle operasjoner er en timeout
etter å ha sendt forespørselen tvetydig. Forson autoritativ tilstand og
gjenbruk samme stabile operasjonsnøkkel før du utfører igjen. Se
[pålitelighets sidecar følgeleksjon](./reliability-sidecars/README.md).

Følgende begrensede retry-løkke er egnet for et leseoppslag:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # sekunder
    
    while retry_count < max_retries:
        try:
            # Kall en ekstern API med lese-only tilgang
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Eksponensiell tilbakeoff
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Ikke-overgangsfeil, ikke prøv på nytt
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Ytelsesoptimalisering

#### 1. Caching

Implementer caching for kostbare operasjoner:

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

#### 2. Asynkron Behandling

Bruk asynkrone programmeringsmønstre for I/O-bundne operasjoner:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // For langvarige operasjoner, returner en behandlings-ID umiddelbart
        String processId = UUID.randomUUID().toString();
        
        // Start asynkron behandling
        CompletableFuture.runAsync(() -> {
            try {
                // Utfør langvarig operasjon
                documentService.processDocument(documentId);
                
                // Oppdater status (ville vanligvis bli lagret i en database)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Returner umiddelbart svar med behandlings-ID
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Tilhørende verktøy for statuskontroll
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

#### 3. Ressursbegrensning

Implementer ressursbegrensning for å forhindre overbelastning:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Tillat 5 forespørsler per sekund
            bucket_size=10        # Tillat opptil 10 forespørsler i raske sekvenser
        )
    
    async def execute_async(self, request):
        # Sjekk om vi kan fortsette eller må vente
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Hvis ventetiden er for lang
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Vent i passende tidsperiode
                await asyncio.sleep(delay)
        
        # Forbruk en token og fortsett med forespørselen
        self.rate_limiter.consume()
        
        # Kall API
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
            
            # Beregn tid til neste token er tilgjengelig
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Legg til nye tokens basert på forløpt tid
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Sikkerhets Beste Praksiser

#### 1. Inndata Validering

Alltid valider inngangsparametere grundig:

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

#### 2. Autorisasjonskontroller

Implementer korrekte autorisasjonskontroller:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Få brukerens kontekst fra forespørselen
    UserContext user = request.getContext().getUserContext();
    
    // Sjekk om brukeren har nødvendige tillatelser
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // For spesifikke ressurser, sjekk tilgang til den ressursen
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Fortsett med verktøykjøring
    // ...
}
```

#### 3. Håndtering av Sensitive Data

Håndter sensitive data med forsiktighet:

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
        
        # Hent brukerdata
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtrer sensitive felt med mindre det eksplisitt er forespurt OG autorisert
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Sjekk autorisasjonsnivå i forespørselskontekst
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Lag en kopi for å unngå å endre originalen
        redacted = user_data.copy()
        
        # Sensurer spesifikke sensitive felt
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Sensurer innhyllede sensitive data
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Test Beste Praksiser for MCP Verktøy

Omfattende testing sikrer at MCP-verktøy fungerer korrekt, håndterer spesialtilfeller og integreres riktig med resten av systemet.

### Enhetstesting

#### 1. Test Hvert Verktøy i Isolasjon

Lag fokuserte tester for hver verktøys funksjonalitet:

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

#### 2. Skjemavalideringstesting

Test at skjemaer er gyldige og håndhever begrensninger korrekt:

```java
@Test
public void testSchemaValidation() {
    // Opprett verktøyinstans
    SearchTool searchTool = new SearchTool();
    
    // Hent skjema
    Object schema = searchTool.getSchema();
    
    // Konverter skjema til JSON for validering
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Valider at skjemaet er gyldig JSONSchema
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Test gyldige parametere
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Test manglende påkrevd parameter
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Test ugyldig parametertype
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Feilhåndteringstester

Lag spesifikke tester for feiltilstander:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Ordne
    tool = ApiTool(timeout=0.1)  # Veldig kort tidsavbrudd
    
    # Simuler en forespørsel som vil gå ut på tid
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Lengre enn tidsavbrudd
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Utfør og påstå
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Bekreft unntaksmelding
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Ordne
    tool = ApiTool()
    
    # Simuler et svar med begrenset hastighet
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
        
        # Utfør og påstå
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Bekreft at unntaket inneholder informasjon om hastighetsbegrensning
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Integrasjonstesting

#### 1. Verktøykjedetesting

Test verktøy som fungerer sammen i forventede kombinasjoner:

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

Test MCP-serveren med full verktøyregistrering og kjøring:

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
        // Test oppdagelsesendepunktet
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Opprett verktøyforespørsel
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Send forespørsel og bekreft svar
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Opprett ugyldig verktøyforespørsel
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Manglende parameter "b"
        request.put("parameters", parameters);
        
        // Send forespørsel og bekreft feilsvar
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. End-to-End Testing

Test komplette arbeidsflyter fra modellprompt til verktøykjøring:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Ordne - Sett opp MCP-klient og mock-modell
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Mock modellresponser
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
    
    # Mock værverktøyrespons
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
        
        # Utfør
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Påstå
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Ytelsestesting

#### 1. Belastningstesting

Test hvor mange samtidige forespørsler din MCP-server kan håndtere:

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

#### 2. Stresstesting

Test systemet under ekstrem belastning:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Sett opp JMeter for stresstesting
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Konfigurer JMeter testplan
    HashTree testPlanTree = new HashTree();
    
    // Lag testplan, trådgruppe, samplere, osv.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Legg til HTTP-sampler for verktøykjøring
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Legg til lyttere
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Kjør test
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Valider resultater
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Gjennomsnittlig responstid < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90. persentil < 500ms
}
```

#### 3. Overvåking og Profilering

Sett opp overvåking for langsiktig ytelsesanalyse:

```python
# Konfigurer overvåking for en MCP-server
def configure_monitoring(server):
    # Sett opp Prometheus-målinger
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
    
    # Legg til mellomvare for timing og opptak av målinger
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Eksponer målepunktsendepunktet
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCP Arbeidsflytdesignmønstre

Godt designede MCP-arbeidsflyter forbedrer effektivitet, pålitelighet og vedlikeholdbarhet. Her er viktige mønstre å følge:

### 1. Kjede av Verktøy-mønsteret

Koble flere verktøy i en sekvens der hver verktøys output blir input for neste:

```python
# Implementasjon av Python Chain of Tools
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Liste over verktøynavn som skal utføres i rekkefølge
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Utfør hvert verktøy i kjeden, og send forrige resultat videre
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Lagre resultat og bruk som input for neste verktøy
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Eksempel på bruk
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

### 2. Dispatcher-mønsteret

Bruk et sentralt verktøy som sender videre til spesialiserte verktøy basert på input:

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

### 3. Parallell Behandlingsmønster

Utfør flere verktøy samtidig for effektivitet:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Trinn 1: Hent datasettmetadata (synkront)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Trinn 2: Start flere analyser parallelt
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
        
        // Vent på at alle parallelle oppgaver fullføres
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Vent på fullføring
        
        // Trinn 3: Kombiner resultater
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Trinn 4: Generer sammendragsrapport
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Returner komplett arbeidsflytresultat
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Feilgjenopprettingsmønster

Implementer elegante fallback-løsninger ved verktøyfeil:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Prøv primærverktøyet først
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Logg feilen
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Gå over til sekundærverktøyet
            try:
                # Kan hende må parametere transformeres for tilbakefallsverktøyet
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Begge verktøyene feilet
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Denne implementeringen vil avhenge av de spesifikke verktøyene
        # For dette eksempelet returnerer vi bare de opprinnelige parameterne
        return params

# Eksempel på bruk
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # Primær (betalt) vær-API
        "basicWeatherService",    # Tilbakefall (gratis) vær-API
        {"location": location}
    )
```

### 5. Arbeidsflytsammensetningsmønster

Bygg komplekse arbeidsflyter ved å komponere enklere:

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

# Testing av MCP-servere: Beste praksiser og topp tips

## Oversikt

Testing er en kritisk del av utviklingen av pålitelige, høy-kvalitets MCP-servere. Denne guiden gir omfattende beste praksiser og tips for testing av MCP-servere gjennom hele utviklingslivssyklusen, fra enhetstester til integrasjonstester og ende-til-ende-validering.

## Hvorfor Testing Er Viktig for MCP-servere

MCP-servere fungerer som kritisk middleware mellom AI-modeller og klientapplikasjoner. Grundig testing sikrer:

- Pålitelighet i produksjonsmiljøer
- Korrekt håndtering av forespørsler og svar
- Korrekt implementering av MCP-spesifikasjoner
- Robusthet mot feil og spesialtilfeller
- Konsistent ytelse under ulike belastninger

## Enhetstesting for MCP-servere

### Enhetstesting (Grunnlag)

Enhetstester verifiserer individuelle komponenter i din MCP-server isolert.

#### Hva skal testes

1. **Ressurshåndterere**: Test hver ressurshåndterers logikk uavhengig
2. **Verktøyimplementasjoner**: Verifiser verktøyets atferd med ulike inndata
3. **Promptmaler**: Sørg for at promptmalene rendres korrekt
4. **Skjema Validering**: Test parameter valideringslogikk
5. **Feilhåndtering**: Verifiser feilrespons for ugyldige inndata

#### Beste praksiser for enhetstesting

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
# Eksempel på enhetstest for et kalkulatorverktøy i Python
def test_calculator_tool_add():
    # Forbered
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Utfør
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Bekreft
    assert result["value"] == 12
```

### Integrasjonstesting (Mellomnivå)

Integrasjonstester verifiserer samspill mellom komponenter i din MCP-server.

#### Hva skal testes

1. **Serverinitialisering**: Test serveroppstart med ulike konfigurasjoner
2. **Rute-registrering**: Verifiser at alle endepunkter er riktig registrert
3. **Forespørselsbehandling**: Test hele forespørsel-svar syklusen
4. **Feil-propagasjon**: Sørg for at feil håndteres korrekt på tvers av komponenter
5. **Autentisering & Autorisasjon**: Test sikkerhetsmekanismer

#### Beste praksiser for integrasjonstesting

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

### Ende-til-ende Testing (Topplag)

Ende-til-ende tester verifiserer fullstendig systematferd fra klient til server.

#### Hva skal testes

1. **Klient-server kommunikasjon**: Test komplette forespørsel-svar sykluser
2. **Reelle klient SDKer**: Test med faktiske klientimplementasjoner
3. **Ytelse under belastning**: Verifiser oppførsel med flere samtidige forespørsler
4. **Feilgjenoppretting**: Test systemets gjenoppretting fra feil

5. **Langvarige operasjoner**: Verifiser håndtering av streaming og langvarige operasjoner

#### Beste praksis for ende-til-ende-testing

```typescript
// Eksempel på E2E-test med en klient i TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Start server i testmiljø
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Utfør
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Bekreft
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Mocking-strategier for MCP-testing

Mocking er essensielt for å isolere komponenter under testing.

### Komponenter å mocke

1. **Eksterne AI-modeller**: Mock modellresponser for forutsigbar testing
2. **Eksterne tjenester**: Mock API-avhengigheter (databaser, tredjepartstjenester)
3. **Autentiseringstjenester**: Mock identitetsleverandører
4. **Ressursleverandører**: Mock dyre ressursbehandlere

### Eksempel: Mocking av en AI-modellrespons

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
# Python-eksempel med unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Konfigurer mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Bruk mock i testen
    server = McpServer(model_client=mock_model)
    # Fortsett med testen
```

## Ytelsestesting

Ytelsestesting er avgjørende for produksjons-MCP-servere.

### Hva som skal måles

1. **Ventetid**: Responstid for forespørsler
2. **Gjennomstrømning**: Forespørsler håndtert per sekund
3. **Ressursbruk**: CPU, minne, nettverksbruk
4. **Parallell håndtering**: Oppførsel under samtidige forespørsler
5. **Skaleringskarakteristikker**: Ytelse ved økende belastning

### Verktøy for ytelsestesting

- **k6**: Open source verktøy for belastningstesting
- **JMeter**: Omfattende ytelsestesting
- **Locust**: Python-basert belastningstesting
- **Azure Load Testing**: Skybasert ytelsestesting

### Eksempel: Grunnleggende belastningstest med k6

```javascript
// k6-skript for belastningstesting av MCP-server
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 virtuelle brukere
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

## Testautomatisering for MCP-servere

Automatisering av testene dine sikrer konsekvent kvalitet og raskere tilbakemeldingssløyfer.

### CI/CD-integrasjon

1. **Kjør enhetstester ved pull-forespørsler**: Sørg for at kodeendringer ikke bryter eksisterende funksjonalitet
2. **Integrasjonstester i staging**: Kjør integrasjonstester i pre-produksjonsmiljøer
3. **Ytelsesbaseliner**: Oppretthold ytelsesmål for å fange regresjoner
4. **Sikkerhetsskanninger**: Automatiser sikkerhetstesting som en del av pipeline

### Eksempel på CI-pipeline (GitHub Actions)

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

## Testing for samsvar med MCP-spesifikasjonen

Verifiser at serveren din korrekt implementerer MCP-spesifikasjonen.

### Viktige samsvarsområder

1. **API-endepunkter**: Test nødvendige endepunkter (/resources, /tools, osv.)
2. **Forespørsel-/responsskjema**: Valider skjemaoverholdelse
3. **Feilkoder**: Verifiser riktige statuskoder for ulike scenarioer
4. **Innholdstyper**: Test håndtering av forskjellige innholdstyper
5. **Autentiseringsflyt**: Verifiser spesifikasjonskompatible autentiseringsmekanismer

### Samsvarstestsett

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

## Topp 10 tips for effektiv MCP-servertesting

1. **Test verktøydefinisjoner separat**: Verifiser skjema-definisjoner uavhengig av verktøylogikk
2. **Bruk parameteriserte tester**: Test verktøy med ulike input, inkludert kanttilfeller
3. **Sjekk feilsvar**: Verifiser korrekt feilhåndtering for alle mulige feilsituasjoner
4. **Test autorisasjonslogikk**: Sørg for korrekt tilgangskontroll for forskjellige brukerroller
5. **Overvåk testdekning**: Sikt mot høy dekning av kritisk kodevei
6. **Test streaming-responser**: Verifiser korrekt håndtering av streaming-innhold
7. **Simuler nettverksproblemer**: Test oppførsel under dårlige nettverksforhold
8. **Test ressursgrenser**: Verifiser oppførsel ved kvoter eller hastighetsbegrensninger
9. **Automatiser regresjonstester**: Bygg et testsett som kjører på hver kodeendring
10. **Dokumenter testtilfeller**: Oppretthold tydelig dokumentasjon av testscenarier

## Vanlige fallgruver i testing

- **Overavhengighet på "happy path"-testing**: Sørg for å teste feilsituasjoner grundig
- **Ignorering av ytelsestesting**: Identifiser flaskehalser før de påvirker produksjon
- **Testing kun i isolasjon**: Kombiner enhetstester, integrasjonstester og end-to-end-tester
- **Manglende API-dekning**: Sikre at alle endepunkter og funksjoner er testet
- **Ulike testmiljøer**: Bruk containere for å sikre konsistente testmiljøer

## Konklusjon

En omfattende teststrategi er avgjørende for å utvikle pålitelige, høy-kvalitets MCP-servere. Ved å implementere beste praksis og tips skissert i denne guiden, kan du sikre at dine MCP-implementasjoner møter de høyeste standardene for kvalitet, pålitelighet og ytelse.


## Viktige punkter

1. **Verktøydesign**: Følg prinsippet om enkeltansvar, bruk dependency injection og design for komponérbarhet
2. **Skjemadesign**: Lag klare, godt dokumenterte skjemaer med riktige valideringsbegrensninger
3. **Feilhåndtering**: Implementer grasiøs feilhåndtering, strukturerte feilresponser og utfallsbevisst retry-logikk
4. **Ytelse**: Bruk caching, asynkron behandling og ressursbegrensning
5. **Sikkerhet**: Anvend grundig validering av input, autorisasjonskontroller og håndtering av sensitiv data
6. **Testing**: Lag omfattende enhetstester, integrasjonstester og ende-til-ende-tester
7. **Workflow-mønstre**: Bruk etablerte mønstre som kjeder, dispachere og parallell behandling

## Øvelse

Design et MCP-verktøy og en arbeidsflyt for et dokumentbehandlingssystem som:

1. Godtar dokumenter i flere formater (PDF, DOCX, TXT)
2. Ekstraherer tekst og nøkkelinformasjon fra dokumentene
3. Klassifiserer dokumenter etter type og innhold
4. Genererer et sammendrag av hvert dokument

Implementer verktøyskjemaene, feilhåndteringen og et arbeidsflytmønster som passer best for dette scenarioet. Vurder hvordan du vil teste denne implementeringen.

## Ressurser 

1. Bli med i MCP-fellesskapet på [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) for å holde deg oppdatert på siste utvikling 
2. Bidra til open source [MCP-prosjekter](https://github.com/modelcontextprotocol)
3. Anvend MCP-prinsipper i dine egne organisasjons AI-initiativer
4. Utforsk spesialiserte MCP-implementasjoner for din bransje. 
5. Vurder å ta avanserte kurs i spesifikke MCP-temaer, som multimodal integrasjon eller enterprise applikasjonsintegrasjon.
6. Eksperimenter med å bygge dine egne MCP-verktøy og workflows ved bruk av prinsippene lært gjennom [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## Hva nå

Neste: [Case Studies](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Melhores Práticas de Desenvolvimento MCP

[![Melhores Práticas de Desenvolvimento MCP](../../../translated_images/pt-PT/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(Clique na imagem acima para ver o vídeo desta lição)_

## Visão Geral

Esta lição concentra-se em melhores práticas avançadas para desenvolver, testar e implementar servidores e funcionalidades MCP em ambientes de produção. À medida que os ecossistemas MCP crescem em complexidade e importância, seguir padrões estabelecidos garante fiabilidade, manutenção e interoperabilidade. Esta lição consolida a sabedoria prática adquirida por implementações reais de MCP para lhe guiar na criação de servidores robustos, eficientes, com recursos, prompts e ferramentas eficazes.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:

- Aplicar as melhores práticas da indústria no design de servidores e funcionalidades MCP
- Criar estratégias abrangentes de teste para servidores MCP
- Desenhar padrões de fluxo de trabalho eficientes e reutilizáveis para aplicações MCP complexas
- Implementar um tratamento adequado de erros, registos e observabilidade em servidores MCP
- Otimizar implementações MCP para desempenho, segurança e manutenção

## Princípios Centrais do MCP

Antes de mergulhar em práticas específicas de implementação, é importante compreender os princípios centrais que orientam o desenvolvimento eficaz de MCP:

1. **Comunicação Padronizada**: O MCP usa JSON-RPC 2.0 como base, fornecendo um formato consistente para pedidos, respostas e tratamento de erros em todas as implementações.

2. **Design Centrado no Utilizador**: Priorize sempre o consentimento, controlo e transparência do utilizador nas suas implementações MCP.

3. **Segurança em Primeiro Lugar**: Implemente medidas robustas de segurança, incluindo autenticação, autorização, validação e limitação de taxa.

4. **Arquitetura Modular**: Conceba os seus servidores MCP com uma abordagem modular, onde cada ferramenta e recurso tem um propósito claro e focado.

5. **Estado Explícito**: O MCP `2026-07-28` é sem estado ao nível do protocolo.
   Quando um fluxo de trabalho necessita de estado entre chamadas, use identificadores explícitos ou
   argumentos de ferramentas comuns suportados por um estado de aplicação duradouro.

## Melhores Práticas Oficiais do MCP

As seguintes melhores práticas são derivadas da documentação oficial do Protocolo de Contexto do Modelo:

### Melhores Práticas de Segurança

1. **Consentimento e Controlo do Utilizador**: Exija sempre consentimento explícito do utilizador antes de aceder a dados ou executar operações. Forneça controlo claro sobre quais dados são partilhados e quais ações são autorizadas.

2. **Privacidade dos Dados**: Exponha dados do utilizador apenas com consentimento explícito e proteja-os com controlos de acesso adequados. Previna transmissões de dados não autorizadas.

3. **Segurança das Ferramentas**: Exija consentimento explícito do utilizador antes de invocar qualquer ferramenta. Assegure que os utilizadores compreendem a funcionalidade de cada ferramenta e imponha limites de segurança rigorosos.

4. **Controlo de Permissões das Ferramentas**: Configure quais ferramentas um modelo pode usar para
   cada pedido e contexto de autorização, assegurando que apenas ferramentas explicitamente autorizadas
   estejam acessíveis.

5. **Autenticação**: Exija autenticação apropriada antes de conceder acesso a ferramentas, recursos ou operações sensíveis usando chaves API, tokens OAuth ou outros métodos seguros de autenticação.

6. **Validação de Parâmetros**: Imponha validação para todas as invocações de ferramentas para evitar que entradas malformadas ou maliciosas cheguem às implementações das ferramentas.

7. **Limitação de Taxa**: Implemente limitação de taxa para prevenir abusos e garantir uso justo dos recursos do servidor.

### Melhores Práticas de Implementação

1. **Negociação de Capacidades**: Negocie versões do protocolo suportadas e
   capacidades. No MCP `2026-07-28`, cada pedido é autónomo e pode
   usar `server/discover`; revisões anteriores usam o handshake de inicialização.

2. **Design de Ferramentas**: Crie ferramentas focadas que façam uma coisa bem, em vez de ferramentas monolíticas que lidam com múltiplas preocupações.

3. **Tratamento de Erros**: Implemente mensagens e códigos de erro padronizados para ajudar a diagnosticar problemas, gerir falhas com elegância e fornecer feedback acionável.

4. **Observabilidade**: Use `stderr` para diagnósticos stdio e OpenTelemetry
   para observabilidade estruturada. A funcionalidade de registo MCP está obsoleta na
   especificação `2026-07-28`.

5. **Acompanhamento de Progresso**: Para operações de longa duração, reporte atualizações de progresso para permitir interfaces de utilizador responsivas.

6. **Cancelamento de Pedidos**: Permita que clientes cancelem pedidos em curso que já não são necessários ou que estejam a demorar demasiado.

## Referências Adicionais

Para a informação mais atualizada sobre melhores práticas MCP, consulte:

- [Documentação MCP](https://modelcontextprotocol.io/)
- [Especificação MCP (2026-07-28)][mcp-2026-spec]
- [Especificação MCP Anterior (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25)
- [Extensão de Tarefas MCP][mcp-tasks-extension]
- [Repositório GitHub](https://github.com/modelcontextprotocol)
- [Melhores Práticas de Segurança](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/) - Riscos e medidas de mitigação de segurança
- [Workshop MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Formação prática em segurança

### Lição Complementar de Fiabilidade

Loops genéricos de repetição são inseguros para ferramentas que criam bilhetes, pagamentos,
mensagens, implementações ou outros efeitos reais. Uma resposta pode ser perdida
após o efeito ser comprometido.

Utilize a lição complementar de fiabilidade,
[Retentativas Seguras para Ferramentas MCP: Um Padrão de Sidecar para Fiabilidade][reliability-sidecar],
para aprender sobre chaves de operação estáveis, admissão duplicada, checkpoints,
reconciliação, níveis de evidência e injeção de falhas.

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## Exemplos Práticos de Implementação

### Melhores Práticas de Design de Ferramentas

#### 1. Princípio da Responsabilidade Única

Cada ferramenta MCP deve ter um propósito claro e focado. Em vez de criar ferramentas monolíticas que tentam lidar com múltiplas preocupações, desenvolva ferramentas especializadas que se destaquem em tarefas específicas.

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

#### 2. Tratamento Consistente de Erros

Implemente tratamento robusto de erros com mensagens informativas e mecanismos adequados de recuperação.

```python
# Exemplo Python com tratamento de erros abrangente
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # Validação de parâmetros
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # Validação de segurança
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # Operação de base de dados com tempo limite
                async with timeout(10):  # Tempo limite de 10 segundos
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # Erros de ligação podem ser temporários
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # Erros de consulta são provavelmente erros do cliente
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # Deixar passar erros específicos da ferramenta
            raise
        except Exception as e:
            # Captura geral para erros inesperados
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # Implementação da deteção de injeção SQL
        pass
        
    def _log_error(self, message, error):
        # Implementação do registo de erros
        pass
```

#### 3. Validação de Parâmetros

Valide sempre os parâmetros minuciosamente para evitar entradas malformadas ou maliciosas.

```javascript
// Exemplo em JavaScript/TypeScript com validação detalhada de parâmetros
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
    // 1. Validar a presença do parâmetro
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. Validar os tipos dos parâmetros
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. Validar os valores dos parâmetros
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. Validar a presença de conteúdo para operação de escrita
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. Validação de segurança do caminho
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // Implementação baseada nos parâmetros validados
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // Implementação da verificação de segurança do caminho
    // ...
  }
}
```

### Exemplos de Implementação de Segurança

#### 1. Autenticação e Autorização

```java
// Exemplo em Java com autenticação e autorização
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // Injeção de dependências
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
        // 1. Extrair o contexto de autenticação
        String authToken = request.getContext().getAuthToken();
        
        // 2. Autenticar utilizador
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. Verificar autorização para a operação específica
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. Proceder com a operação autorizada
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

#### 2. Limitação de Taxa

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

## Melhores Práticas de Teste

### 1. Teste Unitário de Ferramentas MCP

Teste sempre as suas ferramentas isoladamente, simulando dependências externas:

```typescript
// Exemplo em TypeScript de um teste unitário de uma ferramenta
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // Criar um serviço de meteorologia simulado
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // Criar a ferramenta com a dependência simulada
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // Preparar
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // Executar
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // Verificar
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // Preparar
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // Executar e Verificar
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. Teste de Integração

Teste o fluxo completo desde pedidos do cliente até respostas do servidor:

```python
# Exemplo de teste de integração em Python
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # Iniciar um servidor de teste
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # Criar um cliente
        client = McpClient("http://localhost:5000")
        
        # Testar a descoberta de ferramentas
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # Testar a execução de ferramentas
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # Verificar a resposta
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # Limpar
        await server.stop()
```

## Otimização de Desempenho

### 1. Estratégias de Cache

Implemente cache apropriado para reduzir latência e uso de recursos:


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

#### 2. Injeção de Dependências e Testabilidade

Projete ferramentas para receberem as suas dependências através da injeção no construtor, tornando-as testáveis e configuráveis:

```java
// Exemplo Java com injeção de dependências
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // Dependências injetadas através do construtor
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // Implementação da ferramenta
    // ...
}
```

#### 3. Ferramentas Componíveis

Projete ferramentas que possam ser compostas em conjunto para criar fluxos de trabalho mais complexos:

```python
# Exemplo em Python a mostrar ferramentas compostas
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # Implementação...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # Esta ferramenta pode usar resultados da ferramenta dataFetch
    async def execute_async(self, request):
        # Implementação...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # Esta ferramenta pode usar resultados da ferramenta dataAnalysis
    async def execute_async(self, request):
        # Implementação...
        pass

# Estas ferramentas podem ser usadas de forma independente ou como parte de um fluxo de trabalho
```

### Melhores Práticas de Design de Esquema

O esquema é o contrato entre o modelo e a sua ferramenta. Esquemas bem projetados levam a melhor usabilidade da ferramenta.

#### 1. Descrições Claras dos Parâmetros

Inclua sempre informações descritivas para cada parâmetro:

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

#### 2. Restrições de Validação

Inclua restrições de validação para evitar entradas inválidas:

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // Propriedade de email com validação de formato
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // Propriedade de idade com restrições numéricas
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // Propriedade enumerada
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

#### 3. Estruturas de Retorno Consistentes

Mantenha consistência nas estruturas de resposta para facilitar a interpretação dos resultados pelos modelos:

```python
async def execute_async(self, request):
    try:
        # Processar pedido
        results = await self._search_database(request.parameters["query"])
        
        # Sempre retornar uma estrutura consistente
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

### Tratamento de Erros

Um tratamento robusto de erros é crucial para que as ferramentas MCP mantenham a fiabilidade.

#### 1. Tratamento Elegante de Erros

Trate erros nos níveis apropriados e forneça mensagens informativas:

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

#### 2. Respostas Estruturadas de Erro

Retorne informações de erro estruturadas sempre que possível:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // Implementação
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
        
        // Relançar outras exceções como ToolExecutionException
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. Lógica de Retry

Utilize lógica genérica de retry apenas para chamadas de leitura ou operações cujo
contrato downstream já seja idempotente. Para operações com efeito, um timeout
após enviar o pedido é ambíguo. Reconciliar o estado autoritativo e
reutilizar a mesma chave de operação estável antes de executar novamente. Veja a
[lição companheira de confiabilidade sidecar](./reliability-sidecars/README.md).

O seguinte ciclo limitado de retry é adequado para uma procura de leitura:

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # segundos
    
    while retry_count < max_retries:
        try:
            # Chamar uma API externa somente de leitura
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # Retração exponencial
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # Erro não transitório, não tentar novamente
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### Otimização de Performance

#### 1. Caching

Implemente caching para operações dispendiosas:

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

#### 2. Processamento Assíncrono

Utilize padrões de programação assíncrona para operações com E/S:

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // Para operações de longa duração, retorne imediatamente um ID de processamento
        String processId = UUID.randomUUID().toString();
        
        // Iniciar processamento assíncrono
        CompletableFuture.runAsync(() -> {
            try {
                // Executar operação de longa duração
                documentService.processDocument(documentId);
                
                // Atualizar estado (normalmente seria armazenado numa base de dados)
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // Retornar resposta imediata com ID de processo
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // Ferramenta acompanhante para verificação de estado
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

#### 3. Controlo de Recursos

Implemente limitação de recursos para evitar sobrecarga:

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # Permitir 5 pedidos por segundo
            bucket_size=10        # Permitir picos até 10 pedidos
        )
    
    async def execute_async(self, request):
        # Verificar se podemos avançar ou precisamos esperar
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # Se a espera for demasiado longa
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # Esperar o tempo de atraso apropriado
                await asyncio.sleep(delay)
        
        # Consumir um token e prosseguir com o pedido
        self.rate_limiter.consume()
        
        # Chamara à API
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
            
            # Calcular o tempo até ao próximo token disponível
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # Adicionar novos tokens com base no tempo decorrido
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### Melhores Práticas de Segurança

#### 1. Validação de Entrada

Valide sempre exaustivamente os parâmetros de entrada:

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

#### 2. Verificações de Autorização

Implemente verificações apropriadas de autorização:

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // Obter o contexto do utilizador a partir da requisição
    UserContext user = request.getContext().getUserContext();
    
    // Verificar se o utilizador tem as permissões necessárias
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // Para recursos específicos, verificar o acesso a esse recurso
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // Prosseguir com a execução da ferramenta
    // ...
}
```

#### 3. Tratamento de Dados Sensíveis

Trate dados sensíveis com cuidado:

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
        
        # Obter dados do utilizador
        user_data = await self.user_service.get_user_data(user_id)
        
        # Filtrar campos sensíveis a menos que solicitados E autorizados explicitamente
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # Verificar o nível de autorização no contexto do pedido
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # Criar uma cópia para evitar modificar o original
        redacted = user_data.copy()
        
        # Ocultar campos sensíveis específicos
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # Ocultar dados sensíveis aninhados
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## Melhores Práticas de Teste para Ferramentas MCP

Testes abrangentes garantem que as ferramentas MCP funcionem corretamente, tratem casos de exceção e integrem-se adequadamente com o restante sistema.

### Teste Unitário

#### 1. Teste Cada Ferramenta Isoladamente

Crie testes focados na funcionalidade de cada ferramenta:

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

#### 2. Teste de Validação de Esquemas

Teste se os esquemas são válidos e aplicam corretamente as restrições:

```java
@Test
public void testSchemaValidation() {
    // Criar instância da ferramenta
    SearchTool searchTool = new SearchTool();
    
    // Obter esquema
    Object schema = searchTool.getSchema();
    
    // Converter esquema para JSON para validação
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // Validar se o esquema é um JSONSchema válido
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // Testar parâmetros válidos
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // Testar parâmetro obrigatório em falta
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // Testar tipo de parâmetro inválido
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. Testes de Tratamento de Erros

Crie testes específicos para condições de erro:

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # Organizar
    tool = ApiTool(timeout=0.1)  # Timeout muito curto
    
    # Simular uma requisição que irá expirar
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # Maior que o timeout
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # Agir e Confirmar
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verificar mensagem de exceção
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # Organizar
    tool = ApiTool()
    
    # Simular uma resposta limitada por taxa
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
        
        # Agir e Confirmar
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # Verificar se a exceção contém informação sobre o limite de taxa
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### Teste de Integração

#### 1. Teste de Cadeia de Ferramentas

Teste ferramentas a funcionar em conjunto nas combinações esperadas:

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

#### 2. Teste do Servidor MCP

Teste o servidor MCP com registo completo e execução de ferramentas:

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
        // Testar o endpoint de descoberta
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // Criar pedido de ferramenta
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // Enviar pedido e verificar resposta
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // Criar pedido de ferramenta inválido
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // Faltando o parâmetro "b"
        request.put("parameters", parameters);
        
        // Enviar pedido e verificar resposta de erro
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. Teste de Ponta a Ponta

Teste fluxos completos desde o prompt do modelo até à execução da ferramenta:

```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # Organizar - Configurar cliente MCP e modelo simulado
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # Respostas do modelo simulado
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
    
    # Resposta da ferramenta meteorológica simulada
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
        
        # Agir
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # Afirmar
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### Teste de Performance

#### 1. Teste de Carga

Teste quantos pedidos concorrentes o seu servidor MCP pode suportar:

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

#### 2. Teste de Stress

Teste o sistema sob carga extrema:

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // Configurar o JMeter para testes de esforço
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // Configurar o plano de teste do JMeter
    HashTree testPlanTree = new HashTree();
    
    // Criar plano de teste, grupo de threads, samples, etc.
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // Adicionar sampler HTTP para execução da ferramenta
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // Adicionar listeners
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // Executar teste
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // Validar resultados
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // Tempo médio de resposta < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // Percentil 90 < 500ms
}
```

#### 3. Monitorização e Perfilagem

Configure monitorização para análise de performance a longo prazo:

```python
# Configurar monitorização para um servidor MCP
def configure_monitoring(server):
    # Configurar métricas Prometheus
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
    
    # Adicionar middleware para temporização e gravação de métricas
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # Expor endpoint de métricas
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## Padrões de Design de Workflows MCP

Workflows MCP bem desenhados melhoram a eficiência, fiabilidade e manutenção. Aqui estão os principais padrões a seguir:

### 1. Padrão Cadeia de Ferramentas

Ligue várias ferramentas em sequência onde a saída de cada ferramenta se torna a entrada para a seguinte:

```python
# Implementação da Cadeia de Ferramentas em Python
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # Lista de nomes de ferramentas para executar em sequência
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # Executar cada ferramenta na cadeia, passando o resultado anterior
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # Armazenar o resultado e usar como entrada para a próxima ferramenta
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# Exemplo de utilização
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

### 2. Padrão Despachante

Utilize uma ferramenta central que despache para ferramentas especializadas com base na entrada:

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

### 3. Padrão de Processamento Paralelo

Execute múltiplas ferramentas simultaneamente para eficiência:

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // Passo 1: Obter metadados do conjunto de dados (síncrono)
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // Passo 2: Lançar múltiplas análises em paralelo
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
        
        // Esperar que todas as tarefas paralelas terminem
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // Esperar pela conclusão
        
        // Passo 3: Combinar resultados
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // Passo 4: Gerar relatório resumo
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // Retornar resultado completo do fluxo de trabalho
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. Padrão de Recuperação de Erros

Implemente fallback elegante para falhas de ferramentas:

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # Tente primeiro a ferramenta principal
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # Registe a falha
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # Recurso à ferramenta secundária
            try:
                # Pode ser necessário transformar os parâmetros para a ferramenta de recurso
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # Ambas as ferramentas falharam
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # Esta implementação dependeria das ferramentas específicas
        # Para este exemplo, vamos apenas devolver os parâmetros originais
        return params

# Exemplo de utilização
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # API meteorológica principal (paga)
        "basicWeatherService",    # API meteorológica de recurso (gratuita)
        {"location": location}
    )
```

### 5. Padrão de Composição de Workflow

Construa workflows complexos compondo workflows mais simples:

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

# Testar Servidores MCP: Melhores Práticas e Principais Dicas

## Visão Geral

Testar é um aspeto crítico no desenvolvimento de servidores MCP fiáveis e de alta qualidade. Este guia fornece práticas recomendadas abrangentes e dicas para testar os seus servidores MCP ao longo do ciclo de desenvolvimento, desde testes unitários a testes de integração e validação ponta a ponta.

## Por Que Testar É Importante para Servidores MCP

Os servidores MCP funcionam como middleware crucial entre modelos de IA e aplicações cliente. Testar cuidadosamente garante:

- Fiabilidade em ambientes de produção
- Tratamento correto de pedidos e respostas
- Implementação adequada das especificações MCP
- Resiliência contra falhas e casos limite
- Performance consistente sob várias cargas

## Teste Unitário para Servidores MCP

### Teste Unitário (Fundamental)

Testes unitários verificam componentes individuais do seu servidor MCP isoladamente.

#### O que Testar

1. **Manipuladores de Recursos**: Teste a lógica de cada manipulador de recursos independentemente
2. **Implementações de Ferramentas**: Verifique o comportamento das ferramentas com várias entradas
3. **Modelos de Prompt**: Assegure que os modelos de prompt geram corretamente
4. **Validação de Esquema**: Teste a lógica de validação dos parâmetros
5. **Tratamento de Erros**: Verifique as respostas de erro para entradas inválidas

#### Melhores Práticas para Teste Unitário

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
# Exemplo de teste unitário para uma ferramenta de calculadora em Python
def test_calculator_tool_add():
    # Organizar
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # Agir
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # Afirmar
    assert result["value"] == 12
```

### Teste de Integração (Camada Intermediária)

Testes de integração verificam interações entre componentes do seu servidor MCP.

#### O que Testar

1. **Inicialização do Servidor**: Teste o arranque do servidor com várias configurações
2. **Registo de Rotas**: Verifique se todos os endpoints estão corretamente registados
3. **Processamento de Pedidos**: Teste o ciclo completo pedido-resposta
4. **Propagação de Erros**: Assegure que os erros são tratados corretamente entre componentes
5. **Autenticação & Autorização**: Teste os mecanismos de segurança

#### Melhores Práticas para Teste de Integração

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

### Teste Ponta a Ponta (Camada Superior)

Testes ponta a ponta verificam o comportamento completo do sistema do cliente ao servidor.

#### O que Testar

1. **Comunicação Cliente-Servidor**: Teste ciclos completos de pedido-resposta
2. **SDKs Reais de Cliente**: Teste com implementações reais de cliente
3. **Performance Sob Carga**: Verifique o comportamento com múltiplos pedidos concorrentes
4. **Recuperação de Erros**: Teste a recuperação do sistema de falhas

5. **Operações de Longa Duração**: Verificar o tratamento de operações de streaming e longas

#### Melhores Práticas para Testes E2E

```typescript
// Exemplo de teste E2E com um cliente em TypeScript
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // Iniciar servidor em ambiente de teste
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // Executar
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // Verificar
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## Estratégias de Mocking para Testes MCP

O mocking é essencial para isolar componentes durante os testes.

### Componentes a Mockar

1. **Modelos Externos de IA**: Mockar respostas do modelo para testes previsíveis
2. **Serviços Externos**: Mockar dependências de API (bases de dados, serviços de terceiros)
3. **Serviços de Autenticação**: Mockar fornecedores de identidade
4. **Fornecedores de Recursos**: Mockar controladores de recursos dispendiosos

### Exemplo: Mockar uma Resposta de Modelo de IA

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
# Exemplo em Python com unittest.mock
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # Configurar mock
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # Usar mock no teste
    server = McpServer(model_client=mock_model)
    # Continuar com o teste
```

## Testes de Performance

Os testes de performance são cruciais para servidores MCP em produção.

### O Que Medir

1. **Latência**: Tempo de resposta para solicitações
2. **Taxa de Transferência**: Solicitações processadas por segundo
3. **Utilização de Recursos**: Uso de CPU, memória, rede
4. **Gestão de Concorrência**: Comportamento sob solicitações paralelas
5. **Características de Escalabilidade**: Performance à medida que a carga aumenta

### Ferramentas para Testes de Performance

- **k6**: Ferramenta open-source de testes de carga
- **JMeter**: Testes de performance abrangentes
- **Locust**: Testes de carga baseados em Python
- **Azure Load Testing**: Testes de performance baseados na cloud

### Exemplo: Teste de Carga Básico com k6

```javascript
// Script k6 para teste de carga do servidor MCP
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10 utilizadores virtuais
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

## Automação de Testes para Servidores MCP

Automatizar os seus testes garante qualidade consistente e ciclos de feedback mais rápidos.

### Integração CI/CD

1. **Executar Testes Unitários em Pull Requests**: Garantir que alterações no código não quebrem funcionalidades existentes
2. **Testes de Integração em Staging**: Executar testes de integração em ambientes pré-produção
3. **Referências de Performance**: Manter benchmarks de performance para detectar regressões
4. **Scans de Segurança**: Automatizar testes de segurança como parte do pipeline

### Exemplo de Pipeline CI (GitHub Actions)

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

## Testar Conformidade com a Especificação MCP

Verifique se o seu servidor implementa corretamente a especificação MCP.

### Áreas Chave de Conformidade

1. **Endpoints da API**: Testar endpoints obrigatórios (/resources, /tools, etc.)
2. **Formato Request/Response**: Validar conformidade com o esquema
3. **Códigos de Erro**: Verificar códigos de estado corretos para vários cenários
4. **Tipos de Conteúdo**: Testar o tratamento de diferentes tipos de conteúdo
5. **Fluxo de Autenticação**: Verificar mecanismos de autenticação conforme a especificação

### Suíte de Testes de Conformidade

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

## Top 10 Dicas para Testar Servidores MCP Eficazmente

1. **Testar Definições de Ferramentas Separadamente**: Verificar definições do esquema independentemente da lógica da ferramenta
2. **Usar Testes Parametrizados**: Testar ferramentas com várias entradas, incluindo casos limite
3. **Verificar Respostas de Erro**: Garantir tratamento correto de erros para todas as condições possíveis
4. **Testar Lógica de Autorização**: Assegurar controlo de acesso adequado para diferentes perfis de utilizador
5. **Monitorizar Cobertura de Testes**: Almejar alta cobertura do código de caminho crítico
6. **Testar Respostas de Streaming**: Verificar tratamento apropriado de conteúdos por streaming
7. **Simular Problemas de Rede**: Testar comportamento sob condições de rede precárias
8. **Testar Limites de Recursos**: Verificar comportamento ao atingir quotas ou limites de taxa
9. **Automatizar Testes de Regressão**: Construir uma suíte que seja executada em cada alteração de código
10. **Documentar Casos de Teste**: Manter documentação clara dos cenários de teste

## Armadilhas Comuns nos Testes

- **Dependência excessiva em testes de caminho feliz**: Assegure-se de testar casos de erro exaustivamente
- **Ignorar testes de performance**: Identifique gargalos antes que afetem a produção
- **Testar apenas em isolamento**: Combine testes unitários, de integração e E2E
- **Cobertura incompleta da API**: Garanta que todos os endpoints e funcionalidades sejam testados
- **Ambientes de teste inconsistentes**: Use contêineres para garantir ambientes de teste consistentes

## Conclusão

Uma estratégia abrangente de testes é essencial para desenvolver servidores MCP confiáveis e de alta qualidade. Ao implementar as melhores práticas e dicas descritas neste guia, pode assegurar que as suas implementações MCP cumpram os mais altos padrões de qualidade, fiabilidade e performance.


## Principais Conclusões

1. **Design da Ferramenta**: Siga o princípio da responsabilidade única, use injeção de dependências e desenhe para composibilidade
2. **Design do Esquema**: Crie esquemas claros, bem documentados com restrições de validação apropriadas
3. **Tratamento de Erros**: Implemente tratamento de erros elegante, respostas estruturadas de erro e lógica de reteste consciente do resultado

4. **Performance**: Use caching, processamento assíncrono e limitação de recursos
5. **Segurança**: Aplique validação rigorosa de entradas, verificações de autorização e gestão de dados sensíveis
6. **Testes**: Crie testes unitários, de integração e end-to-end abrangentes
7. **Padrões de Workflow**: Aplique padrões estabelecidos como cadeias, distribuidores e processamento paralelo

## Exercício

Desenhe uma ferramenta MCP e um workflow para um sistema de processamento de documentos que:

1. Aceite documentos em múltiplos formatos (PDF, DOCX, TXT)
2. Extraia texto e informações chave dos documentos
3. Classifique documentos por tipo e conteúdo
4. Gere um resumo de cada documento

Implemente os esquemas da ferramenta, tratamento de erros e um padrão de workflow que melhor se adeque a este cenário. Considere como testaria esta implementação.

## Recursos 

1. Junte-se à comunidade MCP no [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) para ficar atualizado sobre as últimas novidades 
2. Contribua para projetos open-source [MCP](https://github.com/modelcontextprotocol)
3. Aplique princípios MCP nas iniciativas de IA da sua própria organização
4. Explore implementações MCP especializadas para a sua indústria. 
5. Considere fazer cursos avançados sobre tópicos específicos MCP, como integração multimodal ou integração de aplicações empresariais.
6. Experimente construir as suas próprias ferramentas e workflows MCP usando os princípios aprendidos no [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)  

## O Que Vem a Seguir

Seguinte: [Estudos de Caso](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
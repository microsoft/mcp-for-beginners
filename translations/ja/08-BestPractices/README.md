# MCP開発のベストプラクティス

[![MCP開発のベストプラクティス](../../../translated_images/ja/09.d0f6d86c9d72134c.webp)](https://youtu.be/W56H9W7x-ao)

_(上の画像をクリックしてこのレッスンのビデオを表示)_

## 概要

このレッスンでは、MCPサーバーおよび機能の本番環境での開発、テスト、デプロイに関する高度なベストプラクティスに焦点を当てます。MCPエコシステムが複雑さと重要性を増す中で、確立されたパターンに従うことで信頼性、保守性、相互運用性を確保します。このレッスンは、実際のMCP導入から得られた実践的な知見をまとめ、効果的なリソース、プロンプト、ツールを用いた堅牢で効率的なサーバー作成の指針を提供します。

## 学習目標

このレッスンを終える頃には、以下ができるようになります：

- MCPサーバーおよび機能設計における業界のベストプラクティスを適用する
- MCPサーバーの包括的なテスト戦略を作成する
- 複雑なMCPアプリケーションのための効率的で再利用可能なワークフローパターンを設計する
- MCPサーバーでの適切なエラー処理、ログ記録、および可観測性を実装する
- パフォーマンス、セキュリティ、保守性のためにMCP実装を最適化する

## MCPの基本原則

具体的な実装手法に入る前に、効果的なMCP開発を導く基本原則を理解することが重要です：

1. <strong>標準化された通信</strong>：MCPはJSON-RPC 2.0を基盤に使用し、すべての実装にわたってリクエスト、レスポンス、およびエラー処理の一貫した形式を提供します。

2. <strong>ユーザー中心設計</strong>：常にユーザーの同意、制御、および透明性を優先してください。

3. <strong>セキュリティファースト</strong>：認証、権限付与、検証、レート制限を含む堅牢なセキュリティ対策を実装します。

4. <strong>モジュール設計</strong>：各ツールやリソースに明確で焦点を絞った目的を持たせ、モジュラーアプローチでMCPサーバーを設計してください。

5. <strong>明示的な状態管理</strong>：MCP `2026-07-28` はプロトコルレイヤーでステートレスです。
   ワークフローが跨るコール間の状態を必要とする場合は、明示的なハンドル
   や永続的なアプリケーション状態に裏付けられた通常のツール引数を使用してください。

## 公式MCPベストプラクティス

以下のベストプラクティスは、公式のModel Context Protocolドキュメントを基にしています：

### セキュリティのベストプラクティス

1. <strong>ユーザーの同意と制御</strong>：データアクセスや操作を行う前に常に明示的なユーザー同意を求めてください。共有されるデータと認可される操作について明確な制御を提供します。

2. <strong>データプライバシー</strong>：明示的な同意がある場合のみユーザーデータを公開し、適切なアクセス制御で保護します。無許可のデータ送信を防止してください。

3. <strong>ツールの安全性</strong>：ツールを呼び出す前に明確なユーザー同意を必要とします。各ツールの機能をユーザーに理解させ、堅牢なセキュリティ境界を適用してください。

4. <strong>ツールの権限制御</strong>：モデルごとに各リクエストおよび認可コンテキストで使用可能なツールを設定し、明示的に許可されたツールのみへのアクセスを保証します。



5. <strong>認証</strong>：APIキー、OAuthトークン、その他の安全な認証方法を使用して、ツール、リソース、および機密操作へのアクセス前に適切な認証を要求します。

6. <strong>パラメータ検証</strong>：すべてのツール呼び出しの検証を強制し、不正な形式や悪意のある入力がツール実装に届かないようにします。

7. <strong>レート制限</strong>：乱用を防ぎ、サーバーリソースの公平な使用を保証するためにレート制限を実装します。

### 実装のベストプラクティス

1. <strong>機能交渉</strong>：サポートされるプロトコルバージョンと機能を交渉します。MCP `2026-07-28` では各リクエストは自己完結型で `server/discover` を使用することができ、旧バージョンは初期化のハンドシェイクを使用します。




2. <strong>ツール設計</strong>: 複数の機能を扱うモノリシックなツールではなく、一つのことをうまく行う集中型のツールを作成します。

3. <strong>エラー処理</strong>: 問題の診断、障害の優雅な処理、実行可能なフィードバックの提供を助けるために、標準化されたエラーメッセージとコードを実装します。

4. <strong>可観測性</strong>: stdio診断には `stderr` を、構造化された可観測性にはOpenTelemetryを使用します。MCPのログ機能は
   `2026-07-28` 仕様で非推奨となりました。


5. <strong>進捗追跡</strong>: 長時間実行される操作では、進捗の更新を報告し、応答性の高いユーザーインターフェイスを可能にします。

6. <strong>リクエストのキャンセル</strong>: 必要なくなったり時間がかかりすぎる進行中のリクエストをクライアントがキャンセルできるようにします。

## 追加の参考資料

MCPのベストプラクティスに関する最新情報は以下を参照してください：

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)][mcp-2026-spec]
- [前回のMCP仕様（2025-11-25）](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Tasks Extension][mcp-tasks-extension]
- [GitHubリポジトリ](https://github.com/modelcontextprotocol)
- [セキュリティベストプラクティス](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- [OWASP MCPトップ10](https://microsoft.github.io/mcp-azure-security-guide/) - セキュリティリスクと緩和策
- [MCPセキュリティサミットワークショップ (Sherpa)](https://azure-samples.github.io/sherpa/) - ハンズオンのセキュリティトレーニング

### 信頼性補助レッスン

汎用的なリトライループは、チケット、支払い、
メッセージ、デプロイなどの実際の効果を伴うツールには安全ではありません。効果が確定した後に応答が失われる可能性があります。


信頼性補助レッスン
[MCPツールの安全なリトライ：信頼性サイドカー・パターン][reliability-sidecar]
を利用して、安定動作の鍵、重複許可、チェックポイント、
照合、証拠レベル、障害注入について学んでください。

[mcp-2026-spec]: https://modelcontextprotocol.io/specification/2026-07-28
[mcp-tasks-extension]: https://modelcontextprotocol.io/extensions/tasks/overview
[reliability-sidecar]: ./reliability-sidecars/README.md

## 実践的な実装例

### ツール設計のベストプラクティス

#### 1. 単一責任原則

各MCPツールは明確で集中した目的を持つべきです。複数の関心事を扱おうとするモノリシックなツールを作るのではなく、特定のタスクに優れた専門的なツールを開発してください。

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

#### 2. 一貫したエラー処理

情報豊富なエラーメッセージと適切な回復機構を備えた堅牢なエラー処理を実装します。

```python
# エラー処理を網羅したPythonの例
class DataQueryTool:
    def get_name(self):
        return "dataQuery"
        
    def get_description(self):
        return "Queries data from specified database tables"
    
    async def execute(self, parameters):
        try:
            # パラメータの検証
            if "query" not in parameters:
                raise ToolParameterError("Missing required parameter: query")
                
            query = parameters["query"]
            
            # セキュリティ検証
            if self._contains_unsafe_sql(query):
                raise ToolSecurityError("Query contains potentially unsafe SQL")
            
            try:
                # タイムアウト付きデータベース操作
                async with timeout(10):  # 10秒のタイムアウト
                    result = await self._database.execute_query(query)
                    
                return ToolResponse(
                    content=[TextContent(json.dumps(result))]
                )
            except asyncio.TimeoutError:
                raise ToolExecutionError("Database query timed out after 10 seconds")
            except DatabaseConnectionError as e:
                # 接続エラーは一時的なものかもしれません
                self._log_error("Database connection error", e)
                raise ToolExecutionError(f"Database connection error: {str(e)}")
            except DatabaseQueryError as e:
                # クエリエラーはクライアント側のエラーである可能性が高いです
                self._log_error("Database query error", e)
                raise ToolExecutionError(f"Invalid query: {str(e)}")
                
        except ToolError:
            # ツール固有のエラーは通過させる
            raise
        except Exception as e:
            # 予期しないエラーのキャッチオール
            self._log_error("Unexpected error in DataQueryTool", e)
            raise ToolExecutionError(f"An unexpected error occurred: {str(e)}")
    
    def _contains_unsafe_sql(self, query):
        # SQLインジェクション検出の実装
        pass
        
    def _log_error(self, message, error):
        # エラーロギングの実装
        pass
```

#### 3. パラメータ検証

不正な形式または悪意のある入力を防ぐために、常にパラメータを徹底的に検証してください。

```javascript
// JavaScript/TypeScriptの詳細なパラメータ検証の例
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
    // 1. パラメータの存在を検証する
    if (!parameters.operation) {
      throw new ToolError("Missing required parameter: operation");
    }
    
    if (!parameters.path) {
      throw new ToolError("Missing required parameter: path");
    }
    
    // 2. パラメータの型を検証する
    if (typeof parameters.operation !== "string") {
      throw new ToolError("Parameter 'operation' must be a string");
    }
    
    if (typeof parameters.path !== "string") {
      throw new ToolError("Parameter 'path' must be a string");
    }
    
    // 3. パラメータの値を検証する
    const validOperations = ["read", "write", "delete"];
    if (!validOperations.includes(parameters.operation)) {
      throw new ToolError(`Invalid operation. Must be one of: ${validOperations.join(", ")}`);
    }
    
    // 4. 書き込み操作のための内容の存在を検証する
    if (parameters.operation === "write" && !parameters.content) {
      throw new ToolError("Content parameter is required for write operation");
    }
    
    // 5. パスの安全性を検証する
    if (!this.isPathWithinAllowedDirectories(parameters.path)) {
      throw new ToolError("Access denied: path is outside of allowed directories");
    }
    
    // 検証されたパラメータに基づく実装
    // ...
  }
  
  isPathWithinAllowedDirectories(path) {
    // パスの安全性チェックの実装
    // ...
  }
}
```

### セキュリティ実装例

#### 1. 認証と認可

```java
// 認証と認可を含むJavaの例
public class SecureDataAccessTool implements Tool {
    private final AuthenticationService authService;
    private final AuthorizationService authzService;
    private final DataService dataService;
    
    // 依存性注入
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
        // 1. 認証コンテキストを抽出する
        String authToken = request.getContext().getAuthToken();
        
        // 2. ユーザーを認証する
        UserIdentity user;
        try {
            user = authService.validateToken(authToken);
        } catch (AuthenticationException e) {
            return ToolResponse.error("Authentication failed: " + e.getMessage());
        }
        
        // 3. 特定の操作に対する認可を確認する
        String dataId = request.getParameters().get("dataId").getAsString();
        String operation = request.getParameters().get("operation").getAsString();
        
        boolean isAuthorized = authzService.isAuthorized(user, "data:" + dataId, operation);
        if (!isAuthorized) {
            return ToolResponse.error("Access denied: Insufficient permissions for this operation");
        }
        
        // 4. 認可された操作を続行する
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

#### 2. レート制限

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

## テストのベストプラクティス

### 1. MCPツールの単体テスト

外部依存をモックしつつ、ツールを単独で必ずテストしてください：

```typescript
// ツールのユニットテストのTypeScript例
describe('WeatherForecastTool', () => {
  let tool: WeatherForecastTool;
  let mockWeatherService: jest.Mocked<IWeatherService>;
  
  beforeEach(() => {
    // モックの天気サービスを作成する
    mockWeatherService = {
      getForecasts: jest.fn()
    } as any;
    
    // モック依存関係でツールを作成する
    tool = new WeatherForecastTool(mockWeatherService);
  });
  
  it('should return weather forecast for a location', async () => {
    // 準備
    const mockForecast = {
      location: 'Seattle',
      forecasts: [
        { date: '2025-07-16', temperature: 72, conditions: 'Sunny' },
        { date: '2025-07-17', temperature: 68, conditions: 'Partly Cloudy' },
        { date: '2025-07-18', temperature: 65, conditions: 'Rain' }
      ]
    };
    
    mockWeatherService.getForecasts.mockResolvedValue(mockForecast);
    
    // 実行
    const response = await tool.execute({
      location: 'Seattle',
      days: 3
    });
    
    // 検証
    expect(mockWeatherService.getForecasts).toHaveBeenCalledWith('Seattle', 3);
    expect(response.content[0].text).toContain('Seattle');
    expect(response.content[0].text).toContain('Sunny');
  });
  
  it('should handle errors from the weather service', async () => {
    // 準備
    mockWeatherService.getForecasts.mockRejectedValue(new Error('Service unavailable'));
    
    // 実行と検証
    await expect(tool.execute({
      location: 'Seattle',
      days: 3
    })).rejects.toThrow('Weather service error: Service unavailable');
  });
});
```

### 2. 統合テスト

クライアントのリクエストからサーバーのレスポンスまでの完全なフローをテストします：

```python
# Python 統合テストの例
@pytest.mark.asyncio
async def test_mcp_server_integration():
    # テストサーバーを起動する
    server = McpServer()
    server.register_tool(WeatherForecastTool(MockWeatherService()))
    await server.start(port=5000)
    
    try:
        # クライアントを作成する
        client = McpClient("http://localhost:5000")
        
        # ツールの検出をテストする
        tools = await client.discover_tools()
        assert "weatherForecast" in [t.name for t in tools]
        
        # ツールの実行をテストする
        response = await client.execute_tool("weatherForecast", {
            "location": "Seattle",
            "days": 3
        })
        
        # レスポンスを検証する
        assert response.status_code == 200
        assert "Seattle" in response.content[0].text
        assert len(json.loads(response.content[0].text)["forecasts"]) == 3
        
    finally:
        # クリーンアップする
        await server.stop()
```

## パフォーマンス最適化


### 1. キャッシング戦略

レイテンシーとリソース使用量を削減するために、適切なキャッシングを実装します:


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

#### 2. 依存性注入とテスト容易性

ツールを設計する際は、依存関係をコンストラクター注入によって受け取るようにし、テスト可能かつ設定可能にします：

```java
// 依存性注入を使用したJavaの例
public class CurrencyConversionTool implements Tool {
    private final ExchangeRateService exchangeService;
    private final CacheService cacheService;
    private final Logger logger;
    
    // 依存関係はコンストラクタを通じて注入される
    public CurrencyConversionTool(
            ExchangeRateService exchangeService,
            CacheService cacheService,
            Logger logger) {
        this.exchangeService = exchangeService;
        this.cacheService = cacheService;
        this.logger = logger;
    }
    
    // ツールの実装
    // ...
}
```

#### 3. 組み合わせ可能なツール

より複雑なワークフローを作成できるよう、組み合わせ可能なツールを設計します：

```python
# Pythonの例、合成可能なツールを示す
class DataFetchTool(Tool):
    def get_name(self):
        return "dataFetch"
    
    # 実装...

class DataAnalysisTool(Tool):
    def get_name(self):
        return "dataAnalysis"
    
    # このツールはdataFetchツールの結果を使用できます
    async def execute_async(self, request):
        # 実装...
        pass

class DataVisualizationTool(Tool):
    def get_name(self):
        return "dataVisualize"
    
    # このツールはdataAnalysisツールの結果を使用できます
    async def execute_async(self, request):
        # 実装...
        pass

# これらのツールは単独で、またはワークフローの一部として使用できます
```

### スキーマ設計のベストプラクティス

スキーマはモデルとツール間の契約です。適切に設計されたスキーマはツールの使いやすさを向上させます。

#### 1. 明確なパラメーター説明

各パラメーターに説明情報を必ず含めます：

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

#### 2. バリデーション制約

無効な入力を防ぐためにバリデーション制約を含めます：

```java
Map<String, Object> getSchema() {
    Map<String, Object> schema = new HashMap<>();
    schema.put("type", "object");
    
    Map<String, Object> properties = new HashMap<>();
    
    // フォーマット検証付きのメールプロパティ
    Map<String, Object> email = new HashMap<>();
    email.put("type", "string");
    email.put("format", "email");
    email.put("description", "User email address");
    
    // 数値制約付きの年齢プロパティ
    Map<String, Object> age = new HashMap<>();
    age.put("type", "integer");
    age.put("minimum", 13);
    age.put("maximum", 120);
    age.put("description", "User age in years");
    
    // 列挙型プロパティ
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

#### 3. 一貫した返却構造

モデルが結果を解釈しやすくするため、レスポンス構造の一貫性を維持します：

```python
async def execute_async(self, request):
    try:
        # リクエストを処理する
        results = await self._search_database(request.parameters["query"])
        
        # 常に一貫した構造を返す
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

### エラーハンドリング

MCPツールの信頼性を保つためには堅牢なエラーハンドリングが不可欠です。

#### 1. 優雅なエラーハンドリング

適切なレベルでエラーを処理し、有益なメッセージを提供します：

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

#### 2. 構造化されたエラー応答

可能な場合は構造化されたエラー情報を返します：

```java
@Override
public ToolResponse execute(ToolRequest request) {
    try {
        // 実装
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
        
        // 他の例外を ToolExecutionException として再スローする
        throw new ToolExecutionException("Tool execution failed: " + ex.getMessage(), ex);
    }
}
```

#### 3. 再試行ロジック

一般的な再試行ロジックは、読み取り専用呼び出しや下流契約がすでに冪等である操作にのみ使います。副作用のある操作では、リクエスト送信後のタイムアウトは曖昧です。権威ある状態を調整し、同じ安定した操作キーを再利用してから再実行してください。[reliability sidecar companion lesson](./reliability-sidecars/README.md)を参照してください。





以下の有限の再試行ループは読み取り専用のルックアップに適しています：

```python
async def execute_async(self, request):
    max_retries = 3
    retry_count = 0
    base_delay = 1  # 秒
    
    while retry_count < max_retries:
        try:
            # 読み取り専用の外部APIを呼び出す
            return await self._call_read_only_api(request.parameters)
        except TransientError as e:
            retry_count += 1
            if retry_count >= max_retries:
                raise ToolExecutionException(f"Operation failed after {max_retries} attempts: {str(e)}")
                
            # 指数バックオフ
            delay = base_delay * (2 ** (retry_count - 1))
            logging.warning(f"Transient error, retrying in {delay}s: {str(e)}")
            await asyncio.sleep(delay)
        except Exception as e:
            # 一時的でないエラー、リトライしない
            raise ToolExecutionException(f"Operation failed: {str(e)}")
```

### パフォーマンス最適化

#### 1. キャッシュ

高価な操作にはキャッシュを実装します：

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

#### 2. 非同期処理

I/O バウンドの操作には非同期プログラミングパターンを使用します：

```java
public class AsyncDocumentProcessingTool implements Tool {
    private final DocumentService documentService;
    private final ExecutorService executorService;
    
    @Override
    public ToolResponse execute(ToolRequest request) {
        String documentId = request.getParameters().get("documentId").asText();
        
        // 長時間実行される操作の場合、すぐに処理IDを返します
        String processId = UUID.randomUUID().toString();
        
        // 非同期処理を開始します
        CompletableFuture.runAsync(() -> {
            try {
                // 長時間実行される操作を行います
                documentService.processDocument(documentId);
                
                // ステータスを更新します（通常はデータベースに保存されます）
                processStatusRepository.updateStatus(processId, "completed");
            } catch (Exception ex) {
                processStatusRepository.updateStatus(processId, "failed", ex.getMessage());
            }
        }, executorService);
        
        // 処理ID付きの即時応答を返します
        Map<String, Object> result = new HashMap<>();
        result.put("processId", processId);
        result.put("status", "processing");
        result.put("estimatedCompletionTime", ZonedDateTime.now().plusMinutes(5));
        
        return new ToolResponse.Builder().setResult(result).build();
    }
    
    // 連携するステータスチェックツール
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

#### 3. リソース制限

過負荷を防ぐためリソース制限を実装します：

```python
class ThrottledApiTool(Tool):
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(
            tokens_per_second=5,  # 1秒あたり5リクエストを許可する
            bucket_size=10        # バーストは最大10リクエストまで許可する
        )
    
    async def execute_async(self, request):
        # 続行できるか、待つ必要があるかを確認する
        delay = self.rate_limiter.get_delay_time()
        
        if delay > 0:
            if delay > 2.0:  # 待機時間が長すぎる場合
                raise ToolExecutionException(
                    f"Rate limit exceeded. Please try again in {delay:.1f} seconds."
                )
            else:
                # 適切な遅延時間だけ待機する
                await asyncio.sleep(delay)
        
        # トークンを消費してリクエストを続行する
        self.rate_limiter.consume()
        
        # APIを呼び出す
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
            
            # 次のトークンが利用可能になるまでの時間を計算する
            return (1 - self.tokens) / self.tokens_per_second
    
    async def consume(self):
        async with self.lock:
            self._refill()
            self.tokens -= 1
    
    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        
        # 経過時間に基づいて新しいトークンを追加する
        new_tokens = elapsed * self.tokens_per_second
        self.tokens = min(self.bucket_size, self.tokens + new_tokens)
        self.last_refill = now
```

### セキュリティのベストプラクティス

#### 1. 入力バリデーション

入力パラメーターは常に徹底的に検証してください：

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

#### 2. 認可チェック

適切な認可チェックを実装します：

```java
@Override
public ToolResponse execute(ToolRequest request) {
    // リクエストからユーザーコンテキストを取得する
    UserContext user = request.getContext().getUserContext();
    
    // ユーザーが必要な権限を持っているか確認する
    if (!authorizationService.hasPermission(user, "documents:read")) {
        throw new ToolExecutionException("User does not have permission to access documents");
    }
    
    // 特定のリソースについては、そのリソースへのアクセスを確認する
    String documentId = request.getParameters().get("documentId").asText();
    if (!documentService.canUserAccess(user.getId(), documentId)) {
        throw new ToolExecutionException("Access denied to the requested document");
    }
    
    // ツールの実行を続行する
    // ...
}
```

#### 3. 機密データの取り扱い

機密データは慎重に扱います：

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
        
        # ユーザーデータを取得する
        user_data = await self.user_service.get_user_data(user_id)
        
        # 明示的に要求されかつ許可されていない限り、機密フィールドをフィルタリングする
        if not include_sensitive or not self._is_authorized_for_sensitive_data(request):
            user_data = self._redact_sensitive_fields(user_data)
        
        return ToolResponse(result=user_data)
    
    def _is_authorized_for_sensitive_data(self, request):
        # リクエストコンテキストで認可レベルを確認する
        auth_level = request.context.get("authorizationLevel")
        return auth_level == "admin"
    
    def _redact_sensitive_fields(self, user_data):
        # 元のデータを変更しないようコピーを作成する
        redacted = user_data.copy()
        
        # 特定の機密フィールドを伏せ字にする
        sensitive_fields = ["ssn", "creditCardNumber", "password"]
        for field in sensitive_fields:
            if field in redacted:
                redacted[field] = "REDACTED"
        
        # ネストされた機密データを伏せ字にする
        if "financialInfo" in redacted:
            redacted["financialInfo"] = {"available": True, "accessRestricted": True}
        
        return redacted
```

## MCPツールのテストベストプラクティス

包括的なテストは、MCPツールが正しく機能し、エッジケースを処理し、システムの他の部分と適切に統合されることを保証します。

### ユニットテスト

#### 1. 各ツールを個別にテスト

各ツールの機能に焦点を当てたテストを作成します：

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

#### 2. スキーマ検証テスト

スキーマが有効で制約を正しく強制しているかをテストします：

```java
@Test
public void testSchemaValidation() {
    // ツールインスタンスを作成する
    SearchTool searchTool = new SearchTool();
    
    // スキーマを取得する
    Object schema = searchTool.getSchema();
    
    // バリデーションのためにスキーマをJSONに変換する
    String schemaJson = objectMapper.writeValueAsString(schema);
    
    // スキーマが有効なJSONSchemaであることを検証する
    JsonSchemaFactory factory = JsonSchemaFactory.byDefault();
    JsonSchema jsonSchema = factory.getJsonSchema(schemaJson);
    
    // 有効なパラメータをテストする
    JsonNode validParams = objectMapper.createObjectNode()
        .put("query", "test query")
        .put("limit", 5);
        
    ProcessingReport validReport = jsonSchema.validate(validParams);
    assertTrue(validReport.isSuccess());
    
    // 必須パラメータが欠落している場合をテストする
    JsonNode missingRequired = objectMapper.createObjectNode()
        .put("limit", 5);
        
    ProcessingReport missingReport = jsonSchema.validate(missingRequired);
    assertFalse(missingReport.isSuccess());
    
    // 無効なパラメータ型をテストする
    JsonNode invalidType = objectMapper.createObjectNode()
        .put("query", "test")
        .put("limit", "not-a-number");
        
    ProcessingReport invalidReport = jsonSchema.validate(invalidType);
    assertFalse(invalidReport.isSuccess());
}
```

#### 3. エラーハンドリングテスト

エラー条件に特化したテストを作成します：

```python
@pytest.mark.asyncio
async def test_api_tool_handles_timeout():
    # 整える
    tool = ApiTool(timeout=0.1)  # 非常に短いタイムアウト
    
    # タイムアウトするリクエストをモックする
    with aioresponses() as mocked:
        mocked.get(
            "https://api.example.com/data",
            callback=lambda *args, **kwargs: asyncio.sleep(0.5)  # タイムアウトより長い
        )
        
        request = ToolRequest(
            tool_name="apiTool",
            parameters={"url": "https://api.example.com/data"}
        )
        
        # 実行＆アサート
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # 例外メッセージを検証する
        assert "timed out" in str(exc_info.value).lower()

@pytest.mark.asyncio
async def test_api_tool_handles_rate_limiting():
    # 整える
    tool = ApiTool()
    
    # レート制限されたレスポンスをモックする
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
        
        # 実行＆アサート
        with pytest.raises(ToolExecutionException) as exc_info:
            await tool.execute_async(request)
        
        # 例外にレート制限情報が含まれていることを検証する
        error_msg = str(exc_info.value).lower()
        assert "rate limit" in error_msg
        assert "try again" in error_msg
```

### 統合テスト

#### 1. ツールチェーンテスト

期待される組み合わせでツールが連携して動作するかをテストします：

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

#### 2. MCPサーバーテスト

フルツール登録と実行を含むMCPサーバーをテストします：

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
        // ディスカバリーエンドポイントをテストする
        mockMvc.perform(get("/mcp/tools"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.tools").isArray())
            .andExpect(jsonPath("$.tools[*].name").value(hasItems(
                "weatherForecast", "calculator", "documentSearch"
            )));
    }
    
    @Test
    public void testToolExecution() throws Exception {
        // ツールリクエストを作成する
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "add");
        parameters.put("a", 5);
        parameters.put("b", 7);
        request.put("parameters", parameters);
        
        // リクエストを送信してレスポンスを検証する
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.result.value").value(12));
    }
    
    @Test
    public void testToolValidation() throws Exception {
        // 無効なツールリクエストを作成する
        Map<String, Object> request = new HashMap<>();
        request.put("toolName", "calculator");
        
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("operation", "divide");
        parameters.put("a", 10);
        // パラメータ "b" が欠落しています
        request.put("parameters", parameters);
        
        // リクエストを送信してエラーレスポンスを検証する
        mockMvc.perform(post("/mcp/execute")
            .contentType(MediaType.APPLICATION_JSON)
            .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.error").exists());
    }
}
```

#### 3. エンドツーエンドテスト

モデルプロンプトからツール実行までの完全なワークフローをテストします：


```python
@pytest.mark.asyncio
async def test_model_interaction_with_tool():
    # 設定 - MCPクライアントとモックモデルをセットアップする
    mcp_client = McpClient(server_url="http://localhost:5000")
    
    # モックモデルの応答
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
    
    # 天気ツールのモック応答
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
        
        # 実行
        response = await mcp_client.send_prompt(
            "What's the weather in Seattle?",
            model=mock_model,
            allowed_tools=["weatherForecast"]
        )
        
        # 検証する
        assert "Seattle" in response.generated_text
        assert "65" in response.generated_text
        assert "Sunny" in response.generated_text
        assert "Rain" in response.generated_text
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0].tool_name == "weatherForecast"
```

### パフォーマンステスト

#### 1. 負荷テスト

MCPサーバーが同時に処理可能なリクエスト数をテストします：

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

#### 2. ストレステスト

システムを極限の負荷状態でテストします：

```java
@Test
public void testServerUnderStress() {
    int maxUsers = 1000;
    int rampUpTimeSeconds = 60;
    int testDurationSeconds = 300;
    
    // ストレステストのためにJMeterを設定する
    StandardJMeterEngine jmeter = new StandardJMeterEngine();
    
    // JMeterのテストプランを構成する
    HashTree testPlanTree = new HashTree();
    
    // テストプラン、スレッドグループ、サンプラーなどを作成する
    TestPlan testPlan = new TestPlan("MCP Server Stress Test");
    testPlanTree.add(testPlan);
    
    ThreadGroup threadGroup = new ThreadGroup();
    threadGroup.setNumThreads(maxUsers);
    threadGroup.setRampUp(rampUpTimeSeconds);
    threadGroup.setScheduler(true);
    threadGroup.setDuration(testDurationSeconds);
    
    testPlanTree.add(threadGroup);
    
    // ツール実行用のHTTPサンプラーを追加する
    HTTPSampler toolExecutionSampler = new HTTPSampler();
    toolExecutionSampler.setDomain("localhost");
    toolExecutionSampler.setPort(5000);
    toolExecutionSampler.setPath("/mcp/execute");
    toolExecutionSampler.setMethod("POST");
    toolExecutionSampler.addArgument("toolName", "calculator");
    toolExecutionSampler.addArgument("parameters", "{\"operation\":\"add\",\"a\":5,\"b\":7}");
    
    threadGroup.add(toolExecutionSampler);
    
    // リスナーを追加する
    SummaryReport summaryReport = new SummaryReport();
    threadGroup.add(summaryReport);
    
    // テストを実行する
    jmeter.configure(testPlanTree);
    jmeter.run();
    
    // 結果を検証する
    assertEquals(0, summaryReport.getErrorCount());
    assertTrue(summaryReport.getAverage() < 200); // 平均応答時間 < 200ms
    assertTrue(summaryReport.getPercentile(90.0) < 500); // 90パーセンタイル < 500ms
}
```

#### 3. 監視とプロファイリング

長期的なパフォーマンス分析のための監視を設定します：

```python
# MCPサーバーの監視を構成する
def configure_monitoring(server):
    # Prometheusメトリクスを設定する
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
    
    # タイミングとメトリクス記録のためのミドルウェアを追加する
    server.add_middleware(PrometheusMiddleware(prometheus_metrics))
    
    # メトリクスエンドポイントを公開する
    @server.router.get("/metrics")
    async def metrics():
        return generate_latest()
    
    return server
```

## MCPワークフローデザインパターン

良く設計されたMCPワークフローは効率性、信頼性、保守性を向上させます。以下の重要なパターンを参考にしてください：

### 1. ツールの連鎖パターン

複数のツールを順番に接続し、各ツールの出力が次のツールの入力になるようにします：

```python
# Python チェインオブツールの実装
class ChainWorkflow:
    def __init__(self, tools_chain):
        self.tools_chain = tools_chain  # 順番に実行するツール名のリスト
    
    async def execute(self, mcp_client, initial_input):
        current_result = initial_input
        all_results = {"input": initial_input}
        
        for tool_name in self.tools_chain:
            # チェーンの各ツールを実行し、前の結果を渡す
            response = await mcp_client.execute_tool(tool_name, current_result)
            
            # 結果を保存し、次のツールの入力として使用する
            all_results[tool_name] = response.result
            current_result = response.result
        
        return {
            "final_result": current_result,
            "all_results": all_results
        }

# 使用例
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

### 2. ディスパッチャーパターン

入力に基づいて専門的なツールに振り分ける中央ツールを使用します：

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

### 3. 並列処理パターン

効率化のために複数のツールを同時に実行します：

```java
public class ParallelDataProcessingWorkflow {
    private final McpClient mcpClient;
    
    public ParallelDataProcessingWorkflow(McpClient mcpClient) {
        this.mcpClient = mcpClient;
    }
    
    public WorkflowResult execute(String datasetId) {
        // ステップ1: データセットのメタデータを取得する（同期）
        ToolResponse metadataResponse = mcpClient.executeTool("datasetMetadata", 
            Map.of("datasetId", datasetId));
        
        // ステップ2: 複数の解析を並行して開始する
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
        
        // すべての並行タスクが完了するまで待つ
        CompletableFuture<Void> allAnalyses = CompletableFuture.allOf(
            statisticalAnalysis, correlationAnalysis, outlierDetection
        );
        
        allAnalyses.join();  // 完了を待つ
        
        // ステップ3: 結果を統合する
        Map<String, Object> combinedResults = new HashMap<>();
        combinedResults.put("metadata", metadataResponse.getResult());
        combinedResults.put("statistics", statisticalAnalysis.join().getResult());
        combinedResults.put("correlations", correlationAnalysis.join().getResult());
        combinedResults.put("outliers", outlierDetection.join().getResult());
        
        // ステップ4: サマリーレポートを生成する
        ToolResponse summaryResponse = mcpClient.executeTool("reportGenerator", 
            Map.of("analysisResults", combinedResults));
        
        // 完成したワークフローの結果を返す
        WorkflowResult result = new WorkflowResult();
        result.setDatasetId(datasetId);
        result.setAnalysisResults(combinedResults);
        result.setSummaryReport(summaryResponse.getResult());
        
        return result;
    }
}
```

### 4. エラー回復パターン

ツールの失敗時に優雅に代替処理を実装します：

```python
class ResilientWorkflow:
    def __init__(self, mcp_client):
        self.client = mcp_client
    
    async def execute_with_fallback(self, primary_tool, fallback_tool, parameters):
        try:
            # まずは主要なツールを試す
            response = await self.client.execute_tool(primary_tool, parameters)
            return {
                "result": response.result,
                "source": "primary",
                "tool": primary_tool
            }
        except ToolExecutionException as e:
            # 失敗を記録する
            logging.warning(f"Primary tool '{primary_tool}' failed: {str(e)}")
            
            # 補助的なツールにフォールバックする
            try:
                # フォールバックツール用にパラメータを変換する必要があるかもしれない
                fallback_params = self._adapt_parameters(parameters, primary_tool, fallback_tool)
                
                response = await self.client.execute_tool(fallback_tool, fallback_params)
                return {
                    "result": response.result,
                    "source": "fallback",
                    "tool": fallback_tool,
                    "primaryError": str(e)
                }
            except ToolExecutionException as fallback_error:
                # 両方のツールが失敗した
                logging.error(f"Both primary and fallback tools failed. Fallback error: {str(fallback_error)}")
                raise WorkflowExecutionException(
                    f"Workflow failed: primary error: {str(e)}; fallback error: {str(fallback_error)}"
                )
    
    def _adapt_parameters(self, params, from_tool, to_tool):
        """Adapt parameters between different tools if needed"""
        # この実装は特定のツールに依存する
        # この例では、元のパラメータをそのまま返すだけにする
        return params

# 使用例
async def get_weather(workflow, location):
    return await workflow.execute_with_fallback(
        "premiumWeatherService",  # 主要（有料）天気API
        "basicWeatherService",    # フォールバック（無料）天気API
        {"location": location}
    )
```

### 5. ワークフロー構成パターン

より単純なものを組み合わせて複雑なワークフローを構築します：

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

# MCPサーバーのテスト：ベストプラクティスとトップヒント

## 概要

テストは信頼性が高く高品質なMCPサーバーを開発するための重要な側面です。このガイドは、単体テストから統合テスト、エンドツーエンド検証まで、開発ライフサイクルを通じてMCPサーバーをテストするための包括的なベストプラクティスとヒントを提供します。

## MCPサーバーにおけるテストの重要性

MCPサーバーはAIモデルとクライアントアプリケーションの間の重要なミドルウェアとして機能します。徹底したテストは以下を保証します：

- 本番環境での信頼性
- リクエストとレスポンスの正確な処理
- MCP仕様の正しい実装
- 障害やエッジケースに対する耐久性
- 様々な負荷下での一貫したパフォーマンス

## MCPサーバーの単体テスト

### 単体テスト（基礎）

単体テストはMCPサーバーの個々のコンポーネントを単独で検証します。

#### テストすべきもの

1. <strong>リソースハンドラー</strong>：各リソースハンドラーのロジックを独立してテストする
2. <strong>ツール実装</strong>：様々な入力に対するツールの挙動を検証する
3. <strong>プロンプトテンプレート</strong>：プロンプトテンプレートが正しくレンダリングされることを確認する
4. <strong>スキーマ検証</strong>：パラメーター検証のロジックをテストする
5. <strong>エラー処理</strong>：無効な入力に対するエラー応答を検証する

#### 単体テストのベストプラクティス

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
# Pythonでの計算機ツールの例の単体テスト
def test_calculator_tool_add():
    # 準備
    calculator = CalculatorTool()
    parameters = {
        "operation": "add",
        "a": 5,
        "b": 7
    }
    
    # 実行
    response = calculator.execute(parameters)
    result = json.loads(response.content[0].text)
    
    # 検証
    assert result["value"] == 12
```

### 統合テスト（ミドルレイヤー）

統合テストはMCPサーバーのコンポーネント間の相互作用を検証します。

#### テストすべきもの

1. <strong>サーバー初期化</strong>：様々な構成でのサーバー起動をテストする
2. <strong>ルート登録</strong>：すべてのエンドポイントが正しく登録されていることを検証する
3. <strong>リクエスト処理</strong>：完全なリクエスト-レスポンスサイクルをテストする
4. <strong>エラー伝播</strong>：コンポーネント間でエラーが適切に処理されていることを確認する
5. <strong>認証と認可</strong>：セキュリティ機構をテストする

#### 統合テストのベストプラクティス

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

### エンドツーエンドテスト（トップレイヤー）

エンドツーエンドテストはクライアントからサーバーまでのシステム全体の動作を検証します。

#### テストすべきもの

1. **クライアント-サーバー通信**：完全なリクエスト-レスポンスサイクルをテストする
2. **実際のクライアントSDK**：実際のクライアント実装を用いてテストする
3. <strong>負荷下でのパフォーマンス</strong>：複数の同時リクエストによる挙動を検証する
4. <strong>エラー回復</strong>：障害からのシステム回復をテストする

5. <strong>長時間実行される操作</strong>: ストリーミングおよび長時間実行される操作の処理を検証する

#### エンドツーエンドテストのベストプラクティス

```typescript
// TypeScriptでのクライアントを使ったE2Eテストの例
describe('MCP Server E2E Tests', () => {
  let client: McpClient;
  
  beforeAll(async () => {
    // テスト環境でサーバーを起動する
    await startTestServer();
    client = new McpClient('http://localhost:5000');
  });
  
  afterAll(async () => {
    await stopTestServer();
  });
  
  test('Client can invoke calculator tool and get correct result', async () => {
    // 実行
    const response = await client.invokeToolAsync('calculator', {
      operation: 'divide',
      a: 20,
      b: 4
    });
    
    // 検証
    expect(response.statusCode).toBe(200);
    expect(response.content[0].text).toContain('5');
  });
});
```

## MCPテストのためのモッキング戦略

テスト中にコンポーネントを分離するためにモッキングは不可欠です。

### モックすべきコンポーネント

1. **外部AIモデル**: 予測可能なテストのためにモデルの応答をモックする
2. <strong>外部サービス</strong>: API依存関係（データベース、サードパーティサービス）をモックする
3. <strong>認証サービス</strong>: アイデンティティプロバイダーをモックする
4. <strong>リソースプロバイダー</strong>: 高コストなリソースハンドラーをモックする

### 例: AIモデル応答のモッキング

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
# unittest.mock を使ったPythonの例
@patch('mcp_server.models.OpenAIModel')
def test_with_mock_model(mock_model):
    # モックを設定する
    mock_model.return_value.generate_response.return_value = {
        "text": "Mocked model response",
        "finish_reason": "completed"
    }
    
    # テストでモックを使う
    server = McpServer(model_client=mock_model)
    # テストを続行する
```

## パフォーマンステスト

パフォーマンステストは本番MCPサーバーにとって非常に重要です。

### 測定項目

1. <strong>レイテンシ</strong>: リクエストへの応答時間
2. <strong>スループット</strong>: 1秒あたりに処理されるリクエスト数
3. <strong>リソース利用率</strong>: CPU、メモリ、ネットワークの使用状況
4. <strong>同時処理対応</strong>: 並列リクエスト下での動作
5. <strong>スケーリング特性</strong>: 負荷増加時のパフォーマンス

### パフォーマンステスト用ツール

- **k6**: オープンソースの負荷テストツール
- **JMeter**: 包括的なパフォーマンステスト
- **Locust**: Pythonベースの負荷テスト
- **Azure Load Testing**: クラウドベースのパフォーマンステスト

### 例: k6による基本的な負荷テスト

```javascript
// MCPサーバーの負荷テスト用k6スクリプト
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,  // 10仮想ユーザー
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

## MCPサーバーのテスト自動化

テストの自動化は一貫した品質と迅速なフィードバックループを保証します。

### CI/CD統合

1. <strong>プルリクエストでユニットテストを実行</strong>: 既存機能が壊れていないか確認
2. <strong>ステージング環境で統合テストを実行</strong>: プリプロダクション環境で統合テストを実施
3. <strong>パフォーマンスベースラインの維持</strong>: パフォーマンス回帰を検知
4. <strong>セキュリティスキャン</strong>: パイプラインの一環として自動化

### CIパイプラインの例（GitHub Actions）

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

## MCP仕様準拠のテスト

サーバーがMCP仕様を正しく実装しているか検証します。

### 重要な準拠ポイント

1. **APIエンドポイント**: 必須エンドポイントのテスト（/resources、/toolsなど）
2. **リクエスト/レスポンスフォーマット**: スキーマ準拠の検証
3. <strong>エラーコード</strong>: 様々なケースで正しいステータスコードを検証
4. <strong>コンテンツタイプ</strong>: 異なるコンテンツタイプの取り扱いをテスト
5. <strong>認証フロー</strong>: 仕様準拠の認証メカニズムを検証

### 準拠テストスイート

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

## 効果的なMCPサーバーテストのトップ10のヒント

1. <strong>ツール定義を個別にテスト</strong>: ツールロジックからスキーマ定義を独立して検証
2. <strong>パラメータ化テストを使用</strong>: 多様な入力、境界値を含むツールのテスト
3. <strong>エラー応答をチェック</strong>: あらゆるエラー状態の適切な処理を確認
4. <strong>認可ロジックをテスト</strong>: ユーザーロールごとのアクセス制御を保証
5. <strong>テストカバレッジを監視</strong>: 重要経路コードの高いカバレッジを目指す
6. <strong>ストリーミング応答をテスト</strong>: ストリーミングコンテンツの正しい処理を検証
7. <strong>ネットワーク障害をシミュレート</strong>: 悪条件下での動作をテスト
8. <strong>リソース制限をテスト</strong>: クォータやレート制限に達した場合の動作を検証
9. <strong>回帰テストを自動化</strong>: すべてのコード変更で実行されるテストスイート作成
10. <strong>テストケースを文書化</strong>: テストシナリオの明確な文書管理

## よくあるテストの落とし穴

- <strong>ハッピーパステストへの過度な依存</strong>: エラーケースも十分にテストする
- <strong>パフォーマンステストの無視</strong>: 本番前にボトルネックを特定
- <strong>単独の隔離テストのみ実施</strong>: ユニット、統合、E2Eテストを組み合わせる
- **APIカバレッジの不完全さ**: すべてのエンドポイントと機能をテスト対象にする
- <strong>一貫性のないテスト環境</strong>: コンテナを利用して安定環境を確保

## 結論

信頼性が高く高品質なMCPサーバーを開発するためには包括的なテスト戦略が不可欠です。本ガイドで示されたベストプラクティスとヒントを実装することで、MCP実装が最高水準の品質、信頼性、パフォーマンスを満たしていることを保証できます。


## 重要なポイント

1. <strong>ツール設計</strong>: 単一責任原則を守り、依存性注入を用い、再利用可能な設計を行う
2. <strong>スキーマ設計</strong>: 明確で十分に文書化されたスキーマを作成し、適切な検証制約を設ける
3. <strong>エラー処理</strong>: 優雅なエラー処理、構造化されたエラー応答、結果に応じたリトライロジックを実装
   する
4. <strong>パフォーマンス</strong>: キャッシュ、非同期処理、リソース制限を用いる
5. <strong>セキュリティ</strong>: 厳密な入力検証、認可チェック、機微なデータ処理を適用する
6. <strong>テスト</strong>: 包括的なユニットテスト、統合テスト、エンドツーエンドテストを作成
7. <strong>ワークフローパターン</strong>: チェーン、ディスパッチャ、並列処理など既存のパターンを適用する

## 演習

文書処理システム向けのMCPツールとワークフローを設計してください。要件は以下の通りです：

1. 複数のフォーマット（PDF、DOCX、TXT）で文書を受け入れる
2. 文書からテキストと重要情報を抽出する
3. 文書をタイプと内容で分類する
4. 各文書の要約を生成する

このシナリオに最適なツールスキーマ、エラー処理、ワークフローパターンを実装し、どのようにテストするかも考えてみてください。

## リソース 

1. [Microsoft Foundry Discord Community](https://aka.ms/foundrydevs) のMCPコミュニティに参加し、最新情報を入手する
2. オープンソースの[MCPプロジェクト](https://github.com/modelcontextprotocol)に貢献する
3. 自社のAIイニシアティブにMCPの原則を適用する
4. 自分の業界に特化したMCP実装を探求する
5. マルチモーダル統合やエンタープライズアプリケーション統合など、特定のMCPトピックの高度なコース受講を検討する
6. [Hands on Lab](../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) を通じて学んだ原則を使い、自分でMCPツールとワークフローを構築する実験をする

## 次のステップ

次へ: [ケーススタディ](../09-CaseStudy/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
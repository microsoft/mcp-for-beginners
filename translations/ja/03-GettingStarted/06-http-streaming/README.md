# HTTPSストリーミングとModel Context Protocol (MCP)

この章では、HTTPSを使用してModel Context Protocol (MCP)を活用した安全でスケーラブルなリアルタイムストリーミングの実装方法について詳しく説明します。ストリーミングの動機、利用可能なトランスポートメカニズム、MCPでのストリーム可能なHTTPの実装方法、セキュリティのベストプラクティス、SSEからの移行、そして独自のストリーミングMCPアプリケーションを構築するための実践的なガイダンスを取り上げます。

## MCPにおけるトランスポートメカニズムとストリーミング

このセクションでは、MCPで利用可能なさまざまなトランスポートメカニズムと、それらがクライアントとサーバー間のリアルタイム通信を可能にするストリーミング機能に果たす役割について説明します。

### トランスポートメカニズムとは？

トランスポートメカニズムは、クライアントとサーバー間でデータがどのように交換されるかを定義します。MCPは、さまざまな環境や要件に対応するために複数のトランスポートタイプをサポートしています：

- **stdio**: 標準入力/出力。ローカルやCLIベースのツールに適しているが、Webやクラウドには不向き。
- **SSE (Server-Sent Events)**: サーバーがHTTPを介してクライアントにリアルタイム更新をプッシュする仕組み。Web UIに適しているが、スケーラビリティや柔軟性に制限がある。
- **Streamable HTTP**: モダンなHTTPベースのストリーミングトランスポートで、通知をサポートし、スケーラビリティが向上。ほとんどの本番環境やクラウドシナリオに推奨される。

### 比較表

以下の比較表を見て、これらのトランスポートメカニズムの違いを理解してください：

| トランスポート       | リアルタイム更新 | ストリーミング | スケーラビリティ | ユースケース               |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | いいえ           | いいえ     | 低い         | ローカルCLIツール         |
| SSE               | はい             | はい       | 中程度       | Web、リアルタイム更新     |
| Streamable HTTP   | はい             | はい       | 高い         | クラウド、マルチクライアント |

> **Tip:** 適切なトランスポートの選択は、パフォーマンス、スケーラビリティ、ユーザー体験に影響を与えます。**Streamable HTTP**は、モダンでスケーラブル、クラウド対応のアプリケーションに推奨されます。

前の章で説明したstdioとSSEのトランスポートに注意してください。この章では、Streamable HTTPに焦点を当てています。

## ストリーミング：概念と動機

ストリーミングの基本的な概念と動機を理解することは、効果的なリアルタイム通信システムを実装するために重要です。

**ストリーミング**とは、ネットワークプログラミングにおいて、データを一度にすべて受信するのではなく、小さなチャンクやイベントのシーケンスとして送受信する技術です。これは特に以下の場合に有用です：

- 大規模なファイルやデータセット
- リアルタイム更新（例：チャット、進行状況バー）
- 長時間実行される計算で、ユーザーに進行状況を知らせたい場合

ストリーミングについて高レベルで知っておくべきこと：

- データは一度にではなく、段階的に配信される。
- クライアントはデータが到着するたびに処理できる。
- 知覚される遅延を減らし、ユーザー体験を向上させる。

### なぜストリーミングを使用するのか？

ストリーミングを使用する理由は以下の通りです：

- ユーザーは終了時だけでなく、即座にフィードバックを得られる。
- リアルタイムアプリケーションや応答性の高いUIを実現。
- ネットワークや計算リソースをより効率的に利用。

### 簡単な例：HTTPストリーミングサーバーとクライアント

以下は、ストリーミングを実装する簡単な例です：

#### Python

**サーバー (Python, FastAPIとStreamingResponseを使用):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**クライアント (Python, requestsを使用):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

この例では、サーバーがすべてのメッセージが準備されるのを待つのではなく、利用可能になるたびにクライアントに一連のメッセージを送信する方法を示しています。

**仕組み：**

- サーバーはメッセージが準備されるたびにそれを生成する。
- クライアントは到着するたびに各チャンクを受信して表示する。

**要件：**

- サーバーはストリーミングレスポンスを使用する必要がある（例：FastAPIの`StreamingResponse`）。
- クライアントはレスポンスをストリームとして処理する必要がある（requestsの`stream=True`）。
- Content-Typeは通常`text/event-stream`または`application/octet-stream`。

#### Java

**サーバー (Java, Spring BootとServer-Sent Eventsを使用):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**クライアント (Java, Spring WebFlux WebClientを使用):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Java実装の注意点：**

- Spring Bootのリアクティブスタックを使用し、`Flux`でストリーミングを実現。
- `ServerSentEvent`はイベントタイプを持つ構造化イベントストリーミングを提供。
- `WebClient`の`bodyToFlux()`でリアクティブなストリーミング消費を可能に。
- `delayElements()`でイベント間の処理時間をシミュレート。
- イベントにはタイプ（`info`、`result`など）があり、クライアントでの処理が容易。

### 比較：従来のストリーミングとMCPストリーミング

従来の方法でのストリーミングとMCPでのストリーミングの違いは以下の通りです：

| 特徴                  | 従来のHTTPストリーミング         | MCPストリーミング（通知）         |
|------------------------|-------------------------------|-------------------------------------|
| メインレスポンス        | チャンク形式                   | 最後に一括送信                     |
| 進行状況の更新         | データチャンクとして送信         | 通知として送信                     |
| クライアント要件        | ストリームを処理する必要あり     | メッセージハンドラーを実装する必要あり |
| ユースケース            | 大規模ファイル、AIトークンストリーム | 進行状況、ログ、リアルタイムフィードバック |

### 観察された主な違い

さらに、以下のような主な違いがあります：

- **通信パターン：**
  - 従来のHTTPストリーミング：データをチャンク形式で送信。
  - MCPストリーミング：JSON-RPCプロトコルを使用した構造化通知システム。

- **メッセージ形式：**
  - 従来のHTTP：改行付きのプレーンテキストチャンク。
  - MCP：メタデータを含む構造化された`LoggingMessageNotification`オブジェクト。

- **クライアント実装：**
  - 従来のHTTP：ストリーミングレスポンスを処理するシンプルなクライアント。
  - MCP：さまざまなタイプのメッセージを処理するメッセージハンドラーを備えた高度なクライアント。

- **進行状況の更新：**
  - 従来のHTTP：進行状況はメインレスポンスストリームの一部。
  - MCP：進行状況は別の通知メッセージとして送信され、メインレスポンスは最後に送信。

### 推奨事項

従来のストリーミング（例：`/stream`エンドポイントを使用）を実装するか、MCPを介したストリーミングを選択するかについて、以下を推奨します：

- **シンプルなストリーミングニーズの場合：** 従来のHTTPストリーミングは実装が簡単で、基本的なストリーミングニーズに十分です。

- **複雑でインタラクティブなアプリケーションの場合：** MCPストリーミングは、リッチなメタデータと通知と最終結果の分離を提供する、より構造化されたアプローチを提供します。

- **AIアプリケーションの場合：** MCPの通知システムは、進行状況をユーザーに通知したい長時間実行されるAIタスクに特に有用です。

## MCPにおけるストリーミング

これまでに、従来のストリーミングとMCPストリーミングの違いや推奨事項を見てきました。ここでは、MCPでのストリーミングをどのように活用できるかを詳しく説明します。

MCPフレームワーク内でのストリーミングの仕組みを理解することは、長時間実行される操作中にリアルタイムフィードバックをユーザーに提供するレスポンシブなアプリケーションを構築するために不可欠です。

MCPにおけるストリーミングは、メインレスポンスをチャンクで送信することではなく、ツールがリクエストを処理している間にクライアントに**通知**を送信することです。これらの通知には、進行状況の更新、ログ、その他のイベントが含まれます。

### 仕組み

メインの結果は依然として単一のレスポンスとして送信されます。ただし、通知は処理中に個別のメッセージとして送信され、リアルタイムでクライアントを更新します。クライアントはこれらの通知を処理して表示できる必要があります。

## 通知とは？

「通知」とは、MCPのコンテキストで、長時間実行される操作中に進行状況、ステータス、またはその他のイベントをクライアントに通知するためにサーバーから送信されるメッセージを指します。通知は透明性とユーザー体験を向上させます。

例えば、クライアントはサーバーとの初期ハンドシェイクが完了した後に通知を送信する必要があります。

通知は以下のようなJSONメッセージとして表されます：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知は、MCPで「[Logging](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)」と呼ばれるトピックに属します。

ログを機能/機能として有効にするには、サーバーで以下のように設定する必要があります：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 使用するSDKによっては、ログがデフォルトで有効になっている場合や、サーバー構成で明示的に有効にする必要がある場合があります。

通知にはさまざまなタイプがあります：

| レベル       | 説明                          | 使用例                          |
|-------------|-------------------------------|---------------------------------|
| debug       | 詳細なデバッグ情報             | 関数の開始/終了ポイント         |
| info        | 一般的な情報メッセージ         | 操作の進行状況の更新            |
| notice      | 通常だが重要なイベント         | 設定変更                        |
| warning     | 警告条件                       | 非推奨機能の使用                |
| error       | エラー条件                     | 操作の失敗                     |
| critical    | 重大な条件                     | システムコンポーネントの障害    |
| alert       | 即時の対応が必要な条件         | データ破損の検出                |
| emergency   | システムが使用不能             | システム全体の障害              |

## MCPでの通知の実装

通知を実装するには、サーバーとクライアントの両方でリアルタイム更新を処理できるように設定する必要があります。これにより、アプリケーションは長時間実行される操作中にユーザーに即時フィードバックを提供できます。

### サーバー側：通知の送信

まずはサーバー側から始めましょう。MCPでは、リクエストを処理しながら通知を送信できるツールを定義します。サーバーはコンテキストオブジェクト（通常は`ctx`）を使用してクライアントにメッセージを送信します。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

上記の例では、`process_files`ツールが各ファイルを処理する際にクライアントに3つの通知を送信します。`ctx.info()`メソッドを使用して情報メッセージを送信しています。

さらに、通知を有効にするには、サーバーがストリーミングトランスポート（例：`streamable-http`）を使用し、クライアントが通知を処理するメッセージハンドラーを実装していることを確認してください。以下は、サーバーを`streamable-http`トランスポートで設定する方法です：

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

この.NETの例では、`ProcessFiles`ツールが`Tool`属性で装飾されており、各ファイルを処理する際にクライアントに3つの通知を送信します。`ctx.Info()`メソッドを使用して情報メッセージを送信しています。

.NET MCPサーバーで通知を有効にするには、ストリーミングトランスポートを使用していることを確認してください：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### クライアント側：通知の受信

クライアントは、通知が到着した際にそれを処理して表示するメッセージハンドラーを実装する必要があります。

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

上記のコードでは、`message_handler`関数が受信メッセージが通知であるかどうかを確認します。通知であれば、それを出力し、そうでなければ通常のサーバーメッセージとして処理します。また、`ClientSession`が通知を処理するために`message_handler`で初期化されている点に注目してください。

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

この.NETの例では、`MessageHandler`関数が受信メッセージが通知であるかどうかを確認します。通知であれば、それを出力し、そうでなければ通常のサーバーメッセージとして処理します。`ClientSession`は`ClientSessionOptions`を介してメッセージハンドラーで初期化されています。

通知を有効にするには、サーバーがストリーミングトランスポート（例：`streamable-http`）を使用し、クライアントが通知を処理するメッセージハンドラーを実装していることを確認してください。

## 進行状況通知とシナリオ

このセクションでは、MCPにおける進行状況通知の概念、その重要性、およびStreamable HTTPを使用した実装方法について説明します。また、理解を深めるための実践的な課題も紹介します。

進行状況通知は、長時間実行される操作中にサーバーからクライアントに送信されるリアルタイムメッセージです。プロセス全体が完了するのを待つ代わりに、サーバーは現在のステータスをクライアントに更新し続けます。これにより、透明性が向上し、ユーザー体験が向上し、デバッグが容易になります。

**例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### なぜ進行状況通知を使用するのか？

進行状況通知が重要な理由は以下の通りです：

- **より良いユーザー体験：** 作業が進行するにつれて更新が表示され、終了時だけではない。
- **リアルタイムフィードバック：** クライアントは進行状況バーやログを表示でき、アプリが応答性を持つように感じられる。
- **デバッグと監視が容易：** プロセスが遅いまたは停止している箇
SSEからStreamable HTTPにアップグレードするには、次の2つの説得力のある理由があります：

- Streamable HTTPは、SSEよりも優れたスケーラビリティ、互換性、そしてより豊富な通知サポートを提供します。
- 新しいMCPアプリケーションに推奨されるトランスポートです。

### 移行手順

MCPアプリケーションでSSEからStreamable HTTPに移行する方法は以下の通りです：

- **サーバーコードを更新**して、`mcp.run()`で`transport="streamable-http"`を使用します。
- **クライアントコードを更新**して、SSEクライアントの代わりに`streamablehttp_client`を使用します。
- **メッセージハンドラーを実装**して、クライアントで通知を処理します。
- **既存のツールやワークフローとの互換性をテスト**します。

### 互換性の維持

移行プロセス中は、既存のSSEクライアントとの互換性を維持することをお勧めします。以下の戦略を検討してください：

- 異なるエンドポイントでSSEとStreamable HTTPの両方をサポートすることができます。
- クライアントを新しいトランスポートに徐々に移行します。

### 課題

移行中に以下の課題に対処する必要があります：

- すべてのクライアントが更新されていることを確認する
- 通知配信の違いを処理する

## セキュリティに関する考慮事項

特にStreamable HTTPのようなHTTPベースのトランスポートを使用する場合、サーバーを実装する際にはセキュリティを最優先に考える必要があります。

HTTPベースのトランスポートを使用したMCPサーバーの実装では、複数の攻撃ベクトルと保護メカニズムに注意を払う必要があります。

### 概要

MCPサーバーをHTTP経由で公開する場合、セキュリティは非常に重要です。Streamable HTTPは新しい攻撃面を導入するため、慎重な設定が必要です。

以下は主なセキュリティに関する考慮事項です：

- **Originヘッダーの検証**：DNSリバインディング攻撃を防ぐために、常に`Origin`ヘッダーを検証してください。
- **ローカルホストバインディング**：ローカル開発では、サーバーを`localhost`にバインドして、インターネット上に公開されないようにします。
- **認証**：本番環境では、APIキーやOAuthなどの認証を実装してください。
- **CORS**：クロスオリジンリソース共有（CORS）ポリシーを設定してアクセスを制限します。
- **HTTPS**：本番環境ではHTTPSを使用してトラフィックを暗号化します。

### ベストプラクティス

さらに、MCPストリーミングサーバーのセキュリティを実装する際に従うべきベストプラクティスを以下に示します：

- 検証なしで受信リクエストを信用しないでください。
- すべてのアクセスとエラーをログに記録し、監視してください。
- セキュリティ脆弱性を修正するために依存関係を定期的に更新してください。

### 課題

MCPストリーミングサーバーのセキュリティを実装する際には、以下の課題に直面する可能性があります：

- 開発の容易さとセキュリティのバランスを取る
- さまざまなクライアント環境との互換性を確保する

### 課題：独自のストリーミングMCPアプリを構築する

**シナリオ：**  
サーバーがアイテム（例：ファイルやドキュメント）のリストを処理し、処理された各アイテムについて通知を送信するMCPサーバーとクライアントを構築してください。クライアントは、通知が到着するたびにそれを表示する必要があります。

**手順：**

1. リストを処理し、各アイテムについて通知を送信するサーバーツールを実装します。
2. 通知をリアルタイムで表示するメッセージハンドラーを備えたクライアントを実装します。
3. サーバーとクライアントを実行してテストし、通知を観察します。

[解答](./solution/README.md)

## さらなる学習と次のステップ

MCPストリーミングに関する知識を深め、より高度なアプリケーションを構築するための次のステップを以下に示します。

### さらなる学習

- [Microsoft: HTTPストリーミングの概要](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET CoreにおけるCORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: ストリーミングリクエスト](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 次のステップ

- ストリーミングを使用してリアルタイム分析、チャット、または共同編集を行う、より高度なMCPツールを構築してみてください。
- MCPストリーミングをフロントエンドフレームワーク（React、Vueなど）と統合して、ライブUI更新を実現してください。
- 次へ：[VSCode用AIツールキットの活用](../07-aitk/README.md)

**免責事項**:  
この文書はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤訳について、当社は一切の責任を負いません。

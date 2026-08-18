# モデルコンテキストプロトコル（MCP）によるHTTPSストリーミング

本章では、HTTPSを使用したモデルコンテキストプロトコル（MCP）による安全でスケーラブル、かつリアルタイムのストリーミング実装について包括的に解説します。ストリーミングの動機、利用可能なトランスポート機構、MCPにおけるストリーム可能なHTTPの実装方法、セキュリティのベストプラクティス、SSEからの移行、そして独自のストリーミングMCPアプリケーション構築の実践的なガイダンスを扱います。

> **今後の展望:** 本レッスンでは、<strong>MCP Specification 2025-11-25</strong>に基づくストリーム可能なHTTPを説明します。この仕様では`initialize`でセッションが確立され、`Mcp-Session-Id`ヘッダーでピン留めされます。`2026-07-28`リリース候補版ではハンドシェイクとセッションIDが完全に廃止され、すべてのリクエストが自己完結型となり、スティッキーセッションなしで任意のサーバーインスタンスにルーティング可能になります。詳細は[What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)を参照してください。

## MCPにおけるトランスポート機構とストリーミング

このセクションでは、MCPで利用可能なさまざまなトランスポート機構と、それらがクライアントとサーバー間のリアルタイム通信におけるストリーミング機能を実現する役割を探ります。

### トランスポート機構とは？

トランスポート機構はクライアントとサーバー間でデータがどのように交換されるかを定義します。MCPは異なる環境や要件に適した複数のトランスポートタイプをサポートしています：

- **stdio**: 標準入出力。ローカルやCLIベースのツールに適しています。シンプルですが、ウェブやクラウドには不向きです。
- **SSE (Server-Sent Events)**: サーバーがHTTP経由でクライアントにリアルタイム更新をプッシュできます。ウェブUI向きですが、スケーラビリティと柔軟性に限界があります。MCP Specification 2025-06-18以降、独立したSSEトランスポートは非推奨となり、"Streamable HTTP"トランスポートに置き換えられました。
- **Streamable HTTP**: 現代的なHTTPベースのストリーミングトランスポートで、通知機能や優れたスケーラビリティをサポートします。ほとんどの本番およびクラウドシナリオで推奨されます。

### 比較表

以下の比較表をご覧いただき、これらのトランスポート機構の違いを理解してください：

| トランスポート     | リアルタイム更新   | ストリーミング | スケーラビリティ | 利用ケース                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | いいえ           | いいえ    | 低          | ローカルCLIツール       |
| SSE               | はい             | はい      | 中          | ウェブ、リアルタイム更新|
| Streamable HTTP   | はい             | はい      | 高          | クラウド、マルチクライアント|

> **ヒント:** 適切なトランスポート選択はパフォーマンス、スケーラビリティ、ユーザー体験に影響します。<strong>Streamable HTTP</strong>は最新のスケーラブルでクラウド対応アプリに推奨されます。

前章で紹介したstdioとSSEと、そして本章で説明するストリーム可能なHTTPがどのように異なるかに注目してください。

## ストリーミング：概念と動機

ストリーミングの基本的な概念と動機を理解することは、効果的なリアルタイム通信システムを構築する上で重要です。

<strong>ストリーミング</strong>は、ネットワークプログラミングにおける手法で、応答全体の準備が整うのを待つのではなく、データを小さく管理可能なチャンクやイベントシーケンスとして送受信します。特に以下に有用です：

- 大きなファイルやデータセット。
- リアルタイム更新（例：チャット、進捗バー）。
- ユーザーに情報を提供し続けたい長時間実行される計算。

ストリーミングの主なポイントは以下の通りです：

- データは一気にではなく段階的に配信される。
- クライアントは到着次第データを処理できる。
- 表面上の遅延が減り、ユーザー体験が向上する。

### なぜストリーミングを使うのか？

ストリーミングを使う理由は以下の通りです：

- ユーザーは終了時だけでなく即時にフィードバックを得られる。
- リアルタイムアプリケーションや応答性の高いUIを実現できる。
- ネットワークと計算リソースの効率的な活用。

### 簡単な例：HTTPストリーミングサーバー＆クライアント

ストリーミングの実装例を示します：

#### Python

**サーバー（Python、FastAPIとStreamingResponse使用）：**

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

**クライアント（Python、requests使用）：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

この例では、すべてのメッセージが準備されるのを待つのではなく、サーバーが利用可能なメッセージを順次クライアントに送信します。

**動作の概要：**

- サーバーはメッセージが準備されるごとに逐次yieldする。
- クライアントは到着するチャンクを受け取って出力する。

**必要条件：**

- サーバーはストリーミング応答（例：FastAPIの`StreamingResponse`）を使用する必要がある。
- クライアントはストリームとして応答を処理する必要がある（requestsの`stream=True`）。
- Content-Typeは通常`text/event-stream`または`application/octet-stream`。

#### Java

**サーバー（Java、Spring BootとServer-Sent Events使用）：**

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

**クライアント（Java、Spring WebFlux WebClient使用）：**

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

**Java実装のポイント：**

- Spring Bootのリアクティブスタックと`Flux`でストリーミングを実現
- `ServerSentEvent`でイベントタイプ付きの構造化されたストリーミング提供
- `WebClient`の`bodyToFlux()`でリアクティブにストリームを受信
- `delayElements()`がイベント間の処理時間をシミュレーション
- イベントは`info`、`result`などタイプを持ち、クライアントでの処理が向上

### 比較：従来のストリーミング vs MCPストリーミング

クラシックなストリーミングとMCPストリーミングがどのように異なるかは以下の通りです：

| 特徴                  | クラシックHTTPストリーミング    | MCPストリーミング（通知）        |
|------------------------|-------------------------------|-------------------------------------|
| 主応答                 | チャンク単位                   | 1回、最後に                        |
| 進捗更新               | データチャンクとして送信       | 通知として送信                     |
| クライアント要件       | ストリーム処理が必須          | メッセージハンドラーの実装が必須  |
| 使用例                 | 大きなファイル、AIトークンストリーム | 進捗、ログ、リアルタイムフィードバック |

### 見られる主な違い

さらに、主な違いとして以下があります：

- **通信パターン：**
  - クラシックHTTPストリーミング：シンプルなチャンク転送エンコーディングでチャンクを送信
  - MCPストリーミング：JSON-RPCプロトコルによる構造化通知システムを使用

- **メッセージ形式：**
  - クラシックHTTP：改行区切りのプレーンテキストチャンク
  - MCP：メタデータ付きの構造化されたLoggingMessageNotificationオブジェクト

- **クライアント実装：**
  - クラシックHTTP：ストリーミングレスポンスを処理するシンプルなクライアント
  - MCP：さまざまなメッセージタイプを処理するメッセージハンドラーを備えた洗練されたクライアント

- **進捗更新：**
  - クラシックHTTP：進捗は主応答ストリームの一部
  - MCP：進捗は通知メッセージとして送信され、主応答は最後に届く

### 推奨事項

クラシックストリーミング（前述の`/stream`エンドポイント利用）とMCPによるストリーミングのどちらを実装するか選ぶ際に推奨される点を以下に示します。

- **シンプルなストリーミングニーズ向け:** クラシックHTTPストリーミングは実装が簡単で基本的なストリーミングには十分です。

- **複雑でインタラクティブなアプリ向け:** MCPストリーミングは通知と最終結果の分離、豊富なメタデータを備えた構造化されたアプローチを提供します。

- **AI対応アプリケーション向け:** MCPの通知システムは、長時間実行されるAIタスクの進捗をユーザーに情報提供するのに特に有用です。

## MCPにおけるストリーミング

これまでにクラシックストリーミングとMCPストリーミングの比較や推奨事項を見てきました。ここからは、MCPでストリーミングをどのように活用できるかを詳細に解説します。

MCPフレームワーク内でのストリーミングの仕組みを理解することは、長時間の処理中にユーザーにリアルタイムのフィードバックを提供する応答性の高いアプリケーション構築に不可欠です。

MCPでは、主な応答をチャンクで送信するのではなく、<strong>通知</strong>を利用して、ツールがリクエストを処理している間にクライアントに進捗やログ、その他のイベントを送信します。

### 仕組み

主な結果は単一の応答として送信されますが、処理中に通知を別メッセージとして送ることでクライアントをリアルタイム更新します。クライアントはこれらの通知を受け取り表示できる必要があります。

## 通知とは？

「通知」といいますが、MCPの文脈での意味は何でしょうか？

通知は、サーバーがクライアントに長時間処理の進捗、状態、その他のイベントを知らせるために送るメッセージです。通知は透明性とユーザー体験を向上させます。

例えば、クライアントは初期のサーバーハンドシェイクが完了したら通知を送ることになっています。

通知は以下のようなJSONメッセージです：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知はMCPのトピック["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)に属します。

> **廃止予告:** `2026-07-28` MCP仕様リリース候補版では、Loggingプリミティブが非推奨となり、stdioトランスポート向けに`stderr`、構造化観測性向けにOpenTelemetryが推奨されます。Loggingは`2025-11-25`仕様および正式に非推奨になってから少なくとも1年間は引き続き動作します。詳細は[What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)を参照してください。

ロギングを有効にするには、サーバーで以下のように機能/機能セットとして有効化する必要があります：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 使用するSDKによっては、ロギングがデフォルトで有効になっている場合や、サーバー設定で明示的に有効化が必要な場合があります。

通知には以下の種類があります：

| レベル          | 説明                          | 利用例                         |
|-----------------|-------------------------------|--------------------------------|
| debug           | 詳細なデバッグ情報            | 関数の入り口/出口            |
| info            | 一般的な情報メッセージ        | 操作の進捗更新               |
| notice          | 通常だが重要なイベント        | 設定変更                     |
| warning         | 警告条件                      | 廃止予定機能の使用           |
| error           | エラー条件                    | 操作の失敗                   |
| critical        | 重大な条件                    | システムコンポーネントの障害  |
| alert           | 直ちに対応が必要               | データ破損検出               |
| emergency       | システム使用不可              | 完全なシステム障害           |

## MCPでの通知の実装

MCPで通知を実装するには、リアルタイム更新を扱うサーバー側とクライアント側の両方を設定する必要があります。これにより、長時間処理中にユーザーへ即時フィードバックを提供できます。

### サーバー側：通知の送信

まずサーバー側から見ましょう。MCPでは、リクエスト処理中に通知を送信できるツールを定義します。サーバーは通常、コンテキストオブジェクト（通常は`ctx`）を使用してクライアントにメッセージを送信します。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

先の例では、`process_files`ツールが各ファイル処理中に3回通知をクライアントに送信します。`ctx.info()`メソッドは情報メッセージ送信に使われます。

さらに通知を有効にするには、サーバーがストリーミングトランスポート（`streamable-http`など）を使用し、クライアントが通知を処理するメッセージハンドラーを実装していることを確認してください。サーバーを`streamable-http`トランスポートで使用する設定例は以下の通りです：

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

この.NET例では、`ProcessFiles`ツールがファイル処理中に3回通知をクライアントに送信します。`ctx.Info()`メソッドは情報メッセージ送信に使われます。

.NET MCPサーバーで通知を有効にするには、ストリーミングトランスポートを使用していることを確認してください：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### クライアント側：通知の受信

クライアントは、通知を受信して処理および表示するメッセージハンドラーを実装する必要があります。

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

前述のコードでは、`message_handler`関数が受信メッセージが通知かどうかを判別します。通知ならプリントし、そうでなければ通常のサーバーメッセージとして処理します。また、`ClientSession`は通知処理のために`message_handler`を用いて初期化されています。

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

この.NET例では、`MessageHandler`関数が受信メッセージが通知かどうかを判別し、通知ならプリント、そうでなければ通常メッセージとして処理します。`ClientSession`は`ClientSessionOptions`経由でメッセージハンドラーを割り当てて初期化されます。

通知を有効にするには、サーバーがストリーミングトランスポート（`streamable-http`など）を使用し、クライアントが通知を処理するメッセージハンドラーを実装していることを確認してください。

## 進捗通知とシナリオ

このセクションでは、MCPにおける進捗通知の概念、それが重要な理由、Streamable HTTPを用いた実装方法を説明します。理解を深めるための実践課題もあります。

進捗通知は、長時間処理中にサーバーからクライアントに送信されるリアルタイムメッセージです。完了を待つ代わりに、サーバーは現在の状況を継続的にクライアントに通知し、透明性とユーザー体験を向上し、デバッグを容易にします。

**例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### なぜ進捗通知を使うのか？

進捗通知が重要な理由は以下の通りです：

- **より良いユーザー体験:** ユーザーは作業進行中に更新を確認できる（完了時だけでなく）。
- **リアルタイムフィードバック:** クライアントは進捗バーやログを表示し、アプリの応答性を向上できる。
- **デバッグと監視が容易:** 開発者やユーザーが処理遅延や停止箇所を特定しやすくなる。

### 進捗通知の実装方法

MCPで進捗通知を実装する方法は以下の通りです：

- **サーバー側:** 各アイテム処理時に`ctx.info()`や`ctx.log()`で通知を送信。これにより主結果が準備される前にクライアントにメッセージが届く。
- **クライアント側:** 到着した通知を受信して表示するメッセージハンドラーを実装。通知と最終結果を区別する。

**サーバー例：**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**クライアント例:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## セキュリティ上の考慮事項

サーバーを実装する際には、特にMCPのStreamable HTTPなどのHTTPベースのトランスポートを使用する場合、セキュリティを最優先に考慮する必要があります。

HTTPベースのトランスポートでMCPサーバーを実装する際には、複数の攻撃ベクトルや防御機構に注意を払うことが極めて重要です。

### 概要

MCPサーバーをHTTPで公開する際はセキュリティが非常に重要です。Streamable HTTPは新たな攻撃対象をもたらし、慎重な設定が求められます。

主なセキュリティ上の考慮点は以下の通りです:

- **Originヘッダーの検証**: DNSリバインディング攻撃を防ぐため、常に`Origin`ヘッダーを検証してください。
- <strong>ローカルホストバインディング</strong>: ローカル開発の場合、サーバーは`localhost`にバインドして公開インターネットに晒さないようにします。
- <strong>認証</strong>: 本番環境ではAPIキーやOAuthなどの認証を実装してください。
- **CORS**: クロスオリジンリソース共有（CORS）ポリシーを設定し、アクセスを制限します。
- **HTTPS**: 本番ではHTTPSを使用して通信を暗号化してください。

### ベストプラクティス

MCPのストリーミングサーバーでセキュリティを実装する際に従うべきベストプラクティスは以下の通りです:

- 入ってくるリクエストを検証なしで信用しないこと。
- すべてのアクセスとエラーをログに記録・監視すること。
- セキュリティ脆弱性を修正するために依存関係を定期的に更新すること。

### 課題

MCPストリーミングサーバーのセキュリティ実装で直面する課題は次の通りです:

- セキュリティと開発のしやすさのバランスを取ること
- 多様なクライアント環境との互換性を確保すること


## SSEからStreamable HTTPへのアップグレード

既にServer-Sent Events（SSE）を使っているアプリケーションでは、Streamable HTTPへ移行することでMCP実装の能力向上と持続可能性の向上が期待できます。

### なぜアップグレードするのか？

SSEからStreamable HTTPにアップグレードすべき理由は二つあります:

- Streamable HTTPはSSEよりもスケーラビリティ、互換性、および豊富な通知サポートを提供します。
- 新しいMCPアプリケーションには推奨されるトランスポートです。

### 移行手順

MCPアプリケーションでSSEからStreamable HTTPに移行する方法は次のとおりです:

- <strong>サーバーコードを更新</strong>し、`mcp.run()`で`transport="streamable-http"`を使用します。
- <strong>クライアントコードを更新</strong>し、SSEクライアントの代わりに`streamablehttp_client`を使用します。
- <strong>クライアントでメッセージハンドラーを実装</strong>し、通知を処理します。
- <strong>既存のツールやワークフローとの互換性をテスト</strong>します。

### 互換性の維持

移行期間中は既存のSSEクライアントとの互換性を維持することが推奨されます。以下の方法があります:

- SSEとStreamable HTTPの両方を異なるエンドポイントで稼働させ両方をサポートする。
- クライアントを徐々に新トランスポートに移行する。

### 課題

移行の際には次の課題に取り組むことが重要です:

- すべてのクライアントが更新されることを確保する
- 通知配信の違いを処理する

### 課題: 自分でストリーミングMCPアプリを作ろう

**シナリオ:**
MCPサーバーとクライアントを構築し、サーバーがアイテム（ファイルやドキュメントなど）のリストを処理し、処理した各アイテム毎に通知を送信します。クライアントは到着した通知を逐次表示します。

**手順:**

1. リストを処理し、各アイテムについて通知を送るサーバーツールを実装します。
2. 通知をリアルタイムで表示するメッセージハンドラーを持つクライアントを実装します。
3. サーバーとクライアントを実行して実装をテストし、通知を確認します。

[Solution](./solution/README.md)

## さらに学ぶ & 次にやること

MCPストリーミングの旅を続け、知識を拡げるために、このセクションでは追加リソースとより高度なアプリケーション構築のための次のステップを提供します。

### さらに学ぶ

- [Microsoft: HTTPストリーミング入門](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET CoreのCORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: ストリーミングリクエスト](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 次にやること

- リアルタイム分析、チャット、共同編集などにストリーミングを使ったより高度なMCPツールを作成してみましょう。
- MCPストリーミングをフロントエンドフレームワーク（React、Vueなど）と統合し、ライブUI更新を試みましょう。
- 次へ: [VSCode用AIツールキットの活用](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
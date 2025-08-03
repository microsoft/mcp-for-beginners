<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "40b1bbffdb8ce6812bf6e701cad876b6",
  "translation_date": "2025-07-17T17:57:41+00:00",
  "source_file": "03-GettingStarted/06-http-streaming/README.md",
  "language_code": "ja"
}
-->
# HTTPS ストリーミングと Model Context Protocol (MCP)

この章では、HTTPS を使った Model Context Protocol (MCP) による安全でスケーラブル、かつリアルタイムなストリーミングの実装方法を詳しく解説します。ストリーミングの動機、利用可能なトランスポート機構、MCP におけるストリーム可能な HTTP の実装方法、セキュリティのベストプラクティス、SSE からの移行、そして実際にストリーミング MCP アプリケーションを構築するための実践的なガイダンスを含みます。

## MCP におけるトランスポート機構とストリーミング

このセクションでは、MCP で利用可能なさまざまなトランスポート機構と、それらがクライアントとサーバー間のリアルタイム通信におけるストリーミング機能をどのように実現しているかを説明します。

### トランスポート機構とは？

トランスポート機構とは、クライアントとサーバー間でデータがどのようにやり取りされるかを定義するものです。MCP は異なる環境や要件に対応するために複数のトランスポートタイプをサポートしています：

- **stdio**: 標準入出力。ローカルや CLI ベースのツールに適しています。シンプルですが、ウェブやクラウドには向きません。
- **SSE (Server-Sent Events)**: サーバーが HTTP 経由でクライアントにリアルタイム更新をプッシュできます。ウェブ UI に適していますが、スケーラビリティや柔軟性に制限があります。
- **Streamable HTTP**: 通知機能や高いスケーラビリティをサポートする最新の HTTP ベースのストリーミングトランスポート。ほとんどの本番環境やクラウドシナリオで推奨されます。

### 比較表

以下の比較表で、これらのトランスポート機構の違いを確認してください：

| トランスポート       | リアルタイム更新 | ストリーミング | スケーラビリティ | 利用ケース               |
|---------------------|------------------|---------------|-----------------|-------------------------|
| stdio               | いいえ           | いいえ        | 低              | ローカル CLI ツール      |
| SSE                 | はい             | はい          | 中              | ウェブ、リアルタイム更新 |
| Streamable HTTP     | はい             | はい          | 高              | クラウド、マルチクライアント |

> **Tip:** 適切なトランスポートの選択はパフォーマンス、スケーラビリティ、ユーザー体験に影響します。**Streamable HTTP** はモダンでスケーラブル、クラウド対応のアプリケーションに推奨されます。

前章で紹介した stdio と SSE に加え、この章では Streamable HTTP が扱われるトランスポートです。

## ストリーミング：概念と動機

ストリーミングの基本的な概念と動機を理解することは、効果的なリアルタイム通信システムを実装する上で重要です。

**ストリーミング** とは、ネットワークプログラミングにおいて、データを一度に全て受け取るのではなく、小さなチャンクやイベントの連続として送受信する技術です。特に以下のような場合に有効です：

- 大きなファイルやデータセット
- リアルタイム更新（例：チャット、進捗バー）
- 長時間かかる計算処理でユーザーに状況を知らせたい場合

ストリーミングのポイントは以下の通りです：

- データは段階的に配信され、一度に全て送られない
- クライアントは到着したデータを随時処理できる
- 待ち時間の感覚を減らし、ユーザー体験を向上させる

### なぜストリーミングを使うのか？

ストリーミングを使う理由は以下の通りです：

- ユーザーは処理完了を待たずに即座にフィードバックを得られる
- リアルタイムアプリケーションや応答性の高い UI を実現できる
- ネットワークや計算資源の効率的な利用が可能になる

### 簡単な例：HTTP ストリーミングサーバーとクライアント

ストリーミングの実装例を示します。

## Python

**サーバー (Python, FastAPI と StreamingResponse を使用):**

### Python

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


**クライアント (Python, requests を使用):**

### Python

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```


この例では、サーバーがすべてのメッセージが揃うのを待つのではなく、準備ができたメッセージを順次クライアントに送信しています。

**動作の仕組み:**
- サーバーはメッセージが準備でき次第それを yield する
- クライアントは到着したチャンクを受け取り、順次表示する

**要件:**
- サーバーはストリーミングレスポンスを使う（例：FastAPI の `StreamingResponse`）
- クライアントはレスポンスをストリームとして処理する（requests の `stream=True`）
- Content-Type は通常 `text/event-stream` または `application/octet-stream`

## Java

**サーバー (Java, Spring Boot と Server-Sent Events を使用):**

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

**クライアント (Java, Spring WebFlux WebClient を使用):**

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

**Java 実装のポイント:**
- Spring Boot のリアクティブスタックで `Flux` を使ったストリーミング
- `ServerSentEvent` によるイベントタイプ付きの構造化ストリーミング
- `WebClient` の `bodyToFlux()` でリアクティブストリーミングを受信
- `delayElements()` でイベント間の処理時間をシミュレート
- イベントに `info` や `result` といったタイプを付与し、クライアントでの処理を容易に

### 比較：従来のストリーミング vs MCP ストリーミング

従来のストリーミングと MCP におけるストリーミングの違いは以下のようにまとめられます：

| 特徴                   | 従来の HTTP ストリーミング       | MCP ストリーミング（通知）          |
|------------------------|---------------------------------|-------------------------------------|
| メインレスポンス       | チャンク単位で送信               | 最後に一括で送信                    |
| 進捗更新               | データチャンクとして送信         | 通知メッセージとして送信            |
| クライアント要件       | ストリームを処理できること       | メッセージハンドラーの実装が必要    |
| 利用ケース             | 大きなファイル、AI トークンストリーム | 進捗、ログ、リアルタイムフィードバック |

### 主な違い

さらに、以下のような違いがあります：

- **通信パターン:**
   - 従来の HTTP ストリーミング：単純なチャンク転送エンコーディングを使用
   - MCP ストリーミング：JSON-RPC プロトコルを使った構造化通知システム

- **メッセージ形式:**
   - 従来の HTTP：改行区切りのプレーンテキストチャンク
   - MCP：メタデータ付きの構造化された LoggingMessageNotification オブジェクト

- **クライアント実装:**
   - 従来の HTTP：ストリーミングレスポンスを処理するシンプルなクライアント
   - MCP：異なる種類のメッセージを処理するメッセージハンドラーを備えた高度なクライアント

- **進捗更新:**
   - 従来の HTTP：進捗はメインレスポンスの一部として送信
   - MCP：進捗は別の通知メッセージとして送信され、メインレスポンスは最後に届く

### 推奨事項

従来のストリーミング（上記の `/stream` エンドポイントのような）と MCP ストリーミングのどちらを選ぶかについて、以下の点を推奨します。

- **シンプルなストリーミングが必要な場合:** 従来の HTTP ストリーミングは実装が簡単で基本的なニーズに十分対応可能です。

- **複雑でインタラクティブなアプリケーションの場合:** MCP ストリーミングは、より豊富なメタデータと通知と最終結果の分離を提供し、構造化されたアプローチを実現します。

- **AI アプリケーションの場合:** MCP の通知システムは、長時間かかる AI タスクの進捗をユーザーに知らせるのに特に有効です。

## MCP におけるストリーミング

ここまでで、従来のストリーミングと MCP ストリーミングの違いと推奨事項を見てきました。ここからは、MCP でストリーミングをどのように活用できるかを詳しく説明します。

MCP フレームワーク内でのストリーミングの仕組みを理解することは、長時間かかる処理中にユーザーにリアルタイムのフィードバックを提供する応答性の高いアプリケーションを構築する上で不可欠です。

MCP では、メインレスポンスをチャンクで送るのではなく、ツールがリクエストを処理している間にクライアントへ **通知** を送る形でストリーミングを実現します。これらの通知には進捗更新やログ、その他のイベントが含まれます。

### 動作の仕組み

メインの結果は依然として単一のレスポンスとして送信されますが、処理中に通知が別メッセージとして送られ、クライアントをリアルタイムに更新します。クライアントはこれらの通知を受け取り、表示できる必要があります。

## 通知とは何か？

「通知」とは MCP の文脈で何を意味するのでしょうか？

通知とは、長時間かかる処理の進捗や状態、その他のイベントをサーバーからクライアントに知らせるメッセージです。通知は透明性を高め、ユーザー体験を向上させます。

例えば、クライアントはサーバーとの初期ハンドシェイクが完了した時点で通知を送ることが想定されています。

通知は JSON メッセージとして以下のような形式を取ります：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知は MCP のトピックの一つである ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) に属します。

ログ機能を有効にするには、サーバー側で以下のように機能/能力として設定する必要があります：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 使用する SDK によっては、ログ機能がデフォルトで有効になっている場合もありますが、サーバー設定で明示的に有効化が必要な場合もあります。

通知には以下のような種類があります：

| レベル       | 説明                           | 例となる利用ケース               |
|--------------|--------------------------------|---------------------------------|
| debug        | 詳細なデバッグ情報             | 関数の開始・終了ポイント         |
| info         | 一般的な情報メッセージ         | 処理の進捗更新                   |
| notice       | 通常だが重要なイベント         | 設定変更                         |
| warning      | 警告状態                       | 非推奨機能の使用                 |
| error        | エラー状態                     | 処理の失敗                       |
| critical     | 重大な状態                     | システムコンポーネントの障害     |
| alert        | 直ちに対応が必要な状態         | データ破損の検出                 |
| emergency    | システムが使用不能な状態       | システム全体の障害               |

## MCP における通知の実装

MCP で通知を実装するには、サーバー側とクライアント側の両方でリアルタイム更新を扱う仕組みを整える必要があります。これにより、長時間かかる処理中にユーザーに即時フィードバックを提供できます。

### サーバー側：通知の送信

まずサーバー側から。MCP では、リクエスト処理中に通知を送信できるツールを定義します。サーバーは通常 `ctx` と呼ばれるコンテキストオブジェクトを使ってクライアントにメッセージを送ります。

### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

上記の例では、`process_files` ツールがファイルを処理するたびに 3 回の通知をクライアントに送信しています。`ctx.info()` メソッドは情報メッセージを送るために使われています。

さらに、通知を有効にするには、サーバーがストリーミングトランスポート（例：`streamable-http`）を使い、クライアントが通知を処理するメッセージハンドラーを実装している必要があります。サーバーで `streamable-http` トランスポートを設定する例は以下の通りです：

```python
mcp.run(transport="streamable-http")
```

### .NET

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

この .NET の例では、`ProcessFiles` ツールが `Tool` 属性で装飾され、ファイル処理ごとに 3 回の通知をクライアントに送信しています。`ctx.Info()` メソッドは情報メッセージ送信に使われています。

.NET MCP サーバーで通知を有効にするには、ストリーミングトランスポートを使用していることを確認してください：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### クライアント側：通知の受信

クライアントは通知を受け取り、表示するためのメッセージハンドラーを実装する必要があります。

### Python

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

上記コードでは、`message_handler` 関数が受信メッセージが通知かどうかを判定し、通知なら表示し、そうでなければ通常のサーバーメッセージとして処理しています。また、`ClientSession` は通知を処理するために `message_handler` を初期化時に渡しています。

### .NET

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

この .NET の例でも、`MessageHandler` 関数が通知かどうかを判定し、通知なら表示、そうでなければ通常のメッセージとして処理しています。`ClientSession` は `ClientSessionOptions` を通じてメッセージハンドラーを設定しています。

通知を有効にするには、サーバーがストリーミングトランスポート（例：`streamable-http`）を使い、クライアントが通知を処理するメッセージハンドラーを実装していることが必要です。

## 進捗通知とシナリオ

このセクションでは、MCP における進捗通知の概念、その重要性、Streamable HTTP を使った実装方法を説明します。理解を深めるための実践課題も含まれています。

進捗通知とは、長時間かかる処理中にサーバーからクライアントへリアルタイムで送られるメッセージです。処理完了を待つのではなく、現在の状況を逐次クライアントに伝えることで、透明性やユーザー体験を向上させ、デバッグも容易にします。

**例:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### なぜ進捗通知を使うのか？

進捗通知が重要な理由は以下の通りです：

- **ユーザー体験の向上:** 処理が進むにつれて更新が見えるため、ユーザーは待ち時間を感じにくい
- **リアルタイムフィードバック:** クライアントは進捗バーやログを表示でき、アプリが応答的に感じられる
- **デバッグや監視の容易化:** 開発者やユーザーが処理のどこで遅延や問題が起きているかを把握しやすい

### 進捗通知の実装方法

進捗通知は以下のように実装します：

- **サーバー側:** 各処理項目の完了時に `ctx.info()` や `ctx.log()` を使って通知を送信。これによりメイン結果が準備される前にクライ
### なぜアップグレードするのか？

SSEからStreamable HTTPにアップグレードする理由は主に2つあります：

- Streamable HTTPはSSEよりもスケーラビリティ、互換性、そしてより豊富な通知サポートを提供します。
- 新しいMCPアプリケーションには推奨されるトランスポート方式です。

### 移行手順

MCPアプリケーションでSSEからStreamable HTTPに移行する方法は以下の通りです：

- **サーバーコードを更新**し、`mcp.run()`で`transport="streamable-http"`を使用します。
- **クライアントコードを更新**し、SSEクライアントの代わりに`streamablehttp_client`を使用します。
- **クライアントにメッセージハンドラーを実装**して通知を処理します。
- **既存のツールやワークフローとの互換性をテスト**します。

### 互換性の維持

移行中は既存のSSEクライアントとの互換性を保つことが推奨されます。以下のような方法があります：

- 異なるエンドポイントでSSEとStreamable HTTPの両方をサポートすることが可能です。
- クライアントを段階的に新しいトランスポートに移行させます。

### 課題

移行時に以下の課題に対応する必要があります：

- すべてのクライアントが更新されていることを確認する
- 通知配信の違いを適切に処理する

## セキュリティ上の考慮事項

MCPでHTTPベースのトランスポート（Streamable HTTPなど）を使用する際は、セキュリティが最優先事項です。

HTTPベースのトランスポートを用いたMCPサーバーの実装では、多様な攻撃ベクトルや防御策に細心の注意を払う必要があります。

### 概要

MCPサーバーをHTTP経由で公開する場合、セキュリティは非常に重要です。Streamable HTTPは新たな攻撃対象を生み出すため、慎重な設定が求められます。

主なセキュリティ上のポイントは以下の通りです：

- **Originヘッダーの検証**：DNSリバインディング攻撃を防ぐために必ず`Origin`ヘッダーを検証してください。
- **ローカルホストバインディング**：ローカル開発時はサーバーを`localhost`にバインドし、公開インターネットへの露出を避けましょう。
- **認証**：本番環境ではAPIキーやOAuthなどの認証を実装してください。
- **CORS**：アクセス制限のためにクロスオリジンリソース共有（CORS）ポリシーを設定しましょう。
- **HTTPS**：本番環境では通信を暗号化するためにHTTPSを使用してください。

### ベストプラクティス

MCPストリーミングサーバーのセキュリティ実装におけるベストプラクティスは以下の通りです：

- 入ってくるリクエストを検証せずに信用しないこと。
- すべてのアクセスとエラーをログに記録し、監視すること。
- セキュリティ脆弱性を修正するために依存関係を定期的に更新すること。

### 課題

MCPストリーミングサーバーのセキュリティ実装で直面する課題は以下の通りです：

- セキュリティと開発のしやすさのバランスを取ること
- 多様なクライアント環境との互換性を確保すること

### 課題：自分でストリーミングMCPアプリを作ろう

**シナリオ：**  
サーバーがアイテムのリスト（ファイルやドキュメントなど）を処理し、処理した各アイテムについて通知を送信するMCPサーバーとクライアントを作成します。クライアントは通知を受け取るたびに表示します。

**手順：**

1. リストを処理し、各アイテムの通知を送信するサーバーツールを実装する。
2. 通知をリアルタイムで表示するメッセージハンドラーを持つクライアントを実装する。
3. サーバーとクライアントの両方を実行して、通知が届く様子を確認する。

[解答](./solution/README.md)

## さらなる学習と次のステップ

MCPストリーミングの理解を深め、より高度なアプリケーション構築に進むための追加リソースと次のステップを紹介します。

### さらなる学習

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 次のステップ

- リアルタイム分析、チャット、共同編集などのためにストリーミングを活用したより高度なMCPツールの構築に挑戦してみましょう。
- MCPストリーミングをフロントエンドフレームワーク（React、Vueなど）と統合し、ライブUI更新を実現してみましょう。
- 次へ：[Utilising AI Toolkit for VSCode](../07-aitk/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。

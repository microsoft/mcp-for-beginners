# MCP Java Client - 電卓デモ

このプロジェクトは、MCP（Model Context Protocol）サーバーに接続してやり取りするJavaクライアントの作成方法を示しています。ここでは、Chapter 01の電卓サーバーに接続し、さまざまな数学的操作を実行します。

## 前提条件

このクライアントを実行する前に、以下を準備してください：

1. Chapter 01の**電卓サーバーを起動**する：
   - 電卓サーバーのディレクトリに移動：`03-GettingStarted/01-first-server/solution/java/`
   - 電卓サーバーをビルドして実行：
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - サーバーは`http://localhost:8080`で動作しているはずです

2. システムに**Java 21以上**がインストールされていること
3. **Maven**（Maven Wrapper経由で含まれています）

## SDKClientとは？

`SDKClient`は、以下を示すJavaアプリケーションです：
- Server-Sent Events（SSE）トランスポートを使ってMCPサーバーに接続する方法
- サーバーから利用可能なツールを一覧表示する方法
- 電卓のさまざまな関数をリモートで呼び出す方法
- レスポンスを処理し、結果を表示する方法

## 動作の仕組み

クライアントはSpring AI MCPフレームワークを使って：

1. **接続の確立**：WebFlux SSEクライアントトランスポートを作成し、電卓サーバーに接続
2. **クライアントの初期化**：MCPクライアントをセットアップし、接続を確立
3. **ツールの検出**：利用可能な電卓操作をすべて一覧表示
4. **操作の実行**：サンプルデータを使ってさまざまな数学関数を呼び出し
5. **結果の表示**：各計算の結果を表示

## プロジェクト構成

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## 主要な依存関係

プロジェクトでは以下の主要な依存関係を使用しています：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

この依存関係は以下を提供します：
- `McpClient` - メインのクライアントインターフェース
- `WebFluxSseClientTransport` - Webベース通信のためのSSEトランスポート
- MCPプロトコルのスキーマおよびリクエスト/レスポンス型

## プロジェクトのビルド

Maven Wrapperを使ってプロジェクトをビルドします：

```cmd
.\mvnw clean install
```

## クライアントの実行

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**注意**：これらのコマンドを実行する前に、電卓サーバーが`http://localhost:8080`で起動していることを確認してください。

## クライアントの動作内容

クライアントを実行すると、以下の処理を行います：

1. `http://localhost:8080`の電卓サーバーに**接続**
2. **ツール一覧表示** - 利用可能な電卓操作をすべて表示
3. **計算の実行**：
   - 加算: 5 + 3 = 8
   - 減算: 10 - 4 = 6
   - 乗算: 6 × 7 = 42
   - 除算: 20 ÷ 4 = 5
   - 累乗: 2^8 = 256
   - 平方根: √16 = 4
   - 絶対値: |-5.5| = 5.5
   - ヘルプ: 利用可能な操作を表示

## 期待される出力

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**注意**：最後にMavenのスレッド残留に関する警告が表示されることがありますが、これはリアクティブアプリケーションでは正常な動作であり、エラーではありません。

## コードの理解

### 1. トランスポートの設定
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
これは電卓サーバーに接続するSSE（Server-Sent Events）トランスポートを作成します。

### 2. クライアントの作成
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
同期的なMCPクライアントを作成し、接続を初期化します。

### 3. ツールの呼び出し
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
パラメータa=5.0、b=3.0で「add」ツールを呼び出します。

## トラブルシューティング

### サーバーが起動していない場合
接続エラーが発生したら、Chapter 01の電卓サーバーが起動しているか確認してください：
```
Error: Connection refused
```
**解決策**：まず電卓サーバーを起動してください。

### ポートがすでに使用中の場合
ポート8080が使用中の場合：
```
Error: Address already in use
```
**解決策**：ポート8080を使用している他のアプリケーションを停止するか、サーバーのポートを変更してください。

### ビルドエラーが発生した場合
ビルドエラーが発生した場合：
```cmd
.\mvnw clean install -DskipTests
```

## さらに学ぶ

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
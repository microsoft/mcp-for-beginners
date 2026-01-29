# Calculator HTTP Streaming デモ

このプロジェクトは、Spring Boot WebFlux を使った Server-Sent Events (SSE) による HTTP ストリーミングを示しています。2つのアプリケーションで構成されています：

- **Calculator Server**：計算を行い、SSE を使って結果をストリーミングするリアクティブなウェブサービス
- **Calculator Client**：ストリーミングエンドポイントを利用するクライアントアプリケーション

## 前提条件

- Java 17 以上
- Maven 3.6 以上

## プロジェクト構成

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## 動作の仕組み

1. **Calculator Server** は `/calculate` エンドポイントを公開し、以下を行います：
   - クエリパラメータを受け取る：`a`（数値）、`b`（数値）、`op`（演算）
   - 対応する演算：`add`、`sub`、`mul`、`div`
   - 計算の進捗と結果を Server-Sent Events で返す

2. **Calculator Client** はサーバーに接続し：
   - `7 * 5` の計算リクエストを送る
   - ストリーミングレスポンスを受け取る
   - 各イベントをコンソールに表示する

## アプリケーションの実行方法

### オプション1：Maven を使う（推奨）

#### 1. Calculator Server を起動する

ターミナルを開き、サーバーディレクトリに移動します：

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

サーバーは `http://localhost:8080` で起動します

以下のような出力が表示されます：
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client を実行する

**新しいターミナル**を開き、クライアントディレクトリに移動します：

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

クライアントはサーバーに接続し、計算を実行してストリーミング結果を表示します。

### オプション2：Java を直接使う

#### 1. サーバーをコンパイルして実行する：

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. クライアントをコンパイルして実行する：

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## サーバーの手動テスト

ブラウザや curl を使ってサーバーをテストすることもできます：

### ブラウザを使う場合：
`http://localhost:8080/calculate?a=10&b=5&op=add` にアクセスしてください

### curl を使う場合：
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## 期待される出力

クライアントを実行すると、以下のようなストリーミング出力が表示されます：

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## 対応している演算

- `add` - 加算 (a + b)
- `sub` - 減算 (a - b)
- `mul` - 乗算 (a * b)
- `div` - 除算 (a / b、b = 0 の場合は NaN を返す)

## API リファレンス

### GET /calculate

**パラメータ:**
- `a`（必須）：最初の数値（double）
- `b`（必須）：2番目の数値（double）
- `op`（必須）：演算（`add`、`sub`、`mul`、`div`）

**レスポンス:**
- Content-Type: `text/event-stream`
- 計算の進捗と結果を Server-Sent Events で返す

**リクエスト例:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**レスポンス例:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## トラブルシューティング

### よくある問題

1. **ポート8080がすでに使用中**
   - ポート8080を使っている他のアプリケーションを停止してください
   - または `calculator-server/src/main/resources/application.yml` でサーバーポートを変更してください

2. **接続拒否される**
   - クライアントを起動する前にサーバーが起動していることを確認してください
   - サーバーがポート8080で正常に起動しているか確認してください

3. **パラメータ名の問題**
   - このプロジェクトは Maven のコンパイラ設定で `-parameters` フラグを使用しています
   - パラメータバインディングの問題が発生した場合は、この設定でビルドされているか確認してください

### アプリケーションの停止方法

- 各アプリケーションが動作しているターミナルで `Ctrl+C` を押してください
- バックグラウンドで実行している場合は `mvn spring-boot:stop` を使って停止できます

## 技術スタック

- **Spring Boot 3.3.1** - アプリケーションフレームワーク
- **Spring WebFlux** - リアクティブウェブフレームワーク
- **Project Reactor** - リアクティブストリームライブラリ
- **Netty** - ノンブロッキングI/Oサーバー
- **Maven** - ビルドツール
- **Java 17+** - プログラミング言語

## 次のステップ

コードを変更してみましょう：
- さらに多くの数学的演算を追加する
- 無効な演算に対するエラーハンドリングを含める
- リクエスト/レスポンスのログを追加する
- 認証を実装する
- ユニットテストを追加する

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
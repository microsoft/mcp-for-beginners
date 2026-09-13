# 電卓LLMクライアント

> [!NOTE]
> このソリューションはコースのレガシーHTTP+SSE電卓サービスに接続し、
> MCP `2025-11-25` SDK APIを対象としています。`2026-07-28`のStreamable HTTPの
> 例ではありません。

LangChain4jを使用して、MiniMaxのOpenAI互換APIを介してMCP（モデルコンテキストプロトコル）電卓サービスに接続する方法を示すJavaアプリケーションです。

## 前提条件

- Java 21以上
- Maven 3.6+（または同梱のMavenラッパーを使用）
- MiniMax APIキー
- `http://localhost:8080`で動作しているMCP電卓サービス

## APIキーの取得

このアプリケーションはMiniMaxのOpenAI互換APIを使用します。キーとエンドポイントを取得するには以下の手順に従ってください：

### 1. エンドポイントを選択
1. グローバルエンドポイントには `https://api.minimax.io/v1` を使用
2. 中国向けエンドポイントには `https://api.minimaxi.com/v1` を使用

### 2. APIキーを作成
1. MiniMaxアカウントからMiniMax APIキーを作成
2. キーは安全な場所に保管

### 3. 環境変数を設定

#### Windows（コマンドプロンプト）で：
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows（PowerShell）で：
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linuxで：
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## セットアップとインストール

1. <strong>プロジェクトディレクトリをクローンまたは移動</strong>

2. <strong>依存関係をインストール</strong>：
   ```cmd
   mvnw clean install
   ```
   またはMavenがグローバルにインストールされている場合：
   ```cmd
   mvn clean install
   ```

3. <strong>環境変数を設定</strong>（上記「APIキーの取得」セクション参照）

4. **MCP電卓サービスを起動**：
   1章のMCP電卓サービスが `http://localhost:8080/sse` で起動していることを確認してください。これはクライアントを起動する前に実行されている必要があります。

## アプリケーションの実行

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## アプリケーションの動作内容

このアプリケーションは電卓サービスへの三つの主な操作を示します：

1. <strong>加算</strong>：24.5と17.3の合計を計算
2. <strong>平方根</strong>：144の平方根を計算
3. <strong>ヘルプ</strong>：使用可能な電卓関数を表示

## 予想される出力

正常に実行されると、以下のような出力が表示されます：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## トラブルシューティング

### よくある問題

1. **「OPENAI_API_KEY環境変数が設定されていません」**
   - `OPENAI_API_KEY`環境変数を設定していることを確認してください
   - 変数設定後に端末やコマンドプロンプトを再起動してください

2. **「localhost:8080への接続が拒否されました」**
   - MCP電卓サービスがポート8080で起動していることを確認
   - 他のサービスがポート8080を使用していないか確認

3. **「認証に失敗しました」**
   - APIキーが有効か確認
   - `OPENAI_BASE_URL`が使用したいエンドポイントと一致しているか確認

4. **Mavenのビルドエラー**
   - Java 21以上を使用しているか確認：`java -version`
   - ビルドをクリーンしてみてください：`mvnw clean`

### デバッグ

デバッグログを有効にするには、実行時に以下のJVM引数を追加してください：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

アプリケーションの設定内容：
- デフォルトでMiniMax-M3を使用。`MINIMAX_MODEL_ID`で`MiniMax-M3`または`MiniMax-M2.7`を選択可能
- `OPENAI_BASE_URL`が設定されている場合はそのURLに接続。設定されていない場合は、`MINIMAX_REGION=cn_zh`なら`https://api.minimaxi.com/v1`、それ以外はデフォルトで`https://api.minimax.io/v1`を使用
- MCPサービスのURLは `http://localhost:8080/sse`
- リクエストのタイムアウトは60秒

## 依存関係

このプロジェクトで使用されている主な依存関係：
- **LangChain4j**：AI統合とツール管理のため
- **LangChain4j MCP**：モデルコンテキストプロトコル対応のため
- **LangChain4j OpenAI公式**：MiniMaxのOpenAI互換API統合のため
- **Spring Boot**：アプリケーションフレームワークと依存性注入のため

## ライセンス

このプロジェクトはApache License 2.0の下でライセンスされています。詳細は[LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)ファイルを参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
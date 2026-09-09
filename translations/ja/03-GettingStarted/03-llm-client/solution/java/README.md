# 電卓LLMクライアント

LangChain4jを使用して、MiniMaxのOpenAI互換APIを介してMCP（モデルコンテキストプロトコル）電卓サービスに接続する方法を示すJavaアプリケーションです。

## 前提条件

- Java 21以上
- Maven 3.6+（または同梱のMavenラッパーを使用）
- MiniMax APIキー
- `http://localhost:8080`で実行中のMCP電卓サービス

## APIキーの取得

本アプリケーションはMiniMaxのOpenAI互換APIを使用します。キーとエンドポイントを取得する手順は以下の通りです：

### 1. エンドポイントの選択
1. グローバルエンドポイントの場合は`https://api.minimax.io/v1`を使用
2. 中国エンドポイントの場合は`https://api.minimaxi.com/v1`を使用

### 2. APIキーの作成
1. MiniMaxアカウントからMiniMax APIキーを作成
2. キーは安全な場所に保管

### 3. 環境変数の設定

#### Windows（コマンドプロンプト）での設定：
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows（PowerShell）での設定：
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linuxでの設定：
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## セットアップとインストール

1. <strong>プロジェクトディレクトリをクローンまたは移動</strong>

2. <strong>依存関係のインストール</strong>：
   ```cmd
   mvnw clean install
   ```
   または Maven がグローバルにインストールされている場合：
   ```cmd
   mvn clean install
   ```

3. <strong>環境変数の設定</strong>（上記「APIキーの取得」セクション参照）

4. **MCP電卓サービスの起動**：
   chapter 1のMCP電卓サービスが`http://localhost:8080/sse`で実行されていることを確認してください。クライアントを起動する前にサービスが稼働中である必要があります。

## アプリケーションの実行

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## アプリケーションの機能

本アプリケーションは電卓サービスとの3つの主なやり取りを示します：

1. <strong>加算</strong>：24.5と17.3の合計を計算
2. <strong>平方根</strong>：144の平方根を計算
3. <strong>ヘルプ</strong>：利用可能な電卓関数を表示

## 予想される出力

正常に実行された場合、以下のような出力が表示されます：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## トラブルシューティング

### よくある問題

1. **"OPENAI_API_KEY環境変数が設定されていません"**
   - `OPENAI_API_KEY`環境変数を設定したか確認
   - 変数設定後に端末/コマンドプロンプトを再起動

2. **"localhost:8080への接続が拒否されました"**
   - MCP電卓サービスがポート8080で実行中か確認
   - 他に8080番ポートを使用しているサービスがないか確認

3. **"認証に失敗しました"**
   - APIキーが有効か確認
   - `OPENAI_BASE_URL`が使用する予定のエンドポイントに合っているか確認

4. **Mavenビルドエラー**
   - Java 21以上を使用しているか確認：`java -version`
   - ビルドをクリーンしてみる：`mvnw clean`

### デバッグ

デバッグログを有効にするには、実行時に以下のJVM引数を追加してください：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

本アプリケーションの設定：
- デフォルトでMiniMax-M3を使用。`MINIMAX_MODEL_ID`で`MiniMax-M3`または`MiniMax-M2.7`を選択可能
- `OPENAI_BASE_URL`が設定されている場合はそこに接続。未設定の場合`MINIMAX_REGION=cn_zh`時は`https://api.minimaxi.com/v1`、それ以外は`https://api.minimax.io/v1`を使用
- MCPサービスには`http://localhost:8080/sse`で接続
- リクエストのタイムアウトは60秒

## 依存関係

本プロジェクトで使用される主な依存関係：
- **LangChain4j**：AI統合とツール管理用
- **LangChain4j MCP**：モデルコンテキストプロトコルサポート用
- **LangChain4j OpenAI公式**：MiniMax OpenAI互換API統合用
- **Spring Boot**：アプリケーションフレームワークおよび依存性注入用

## ライセンス

本プロジェクトはApache License 2.0の下でライセンスされています。詳細は [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ファイルをご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
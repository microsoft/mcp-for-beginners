# Calculator LLM Client

LangChain4jを使って、GitHub Modelsと連携したMCP（Model Context Protocol）電卓サービスに接続するJavaアプリケーションのデモです。

## 前提条件

- Java 21以上
- Maven 3.6以上（または同梱のMavenラッパーを使用）
- GitHub ModelsにアクセスできるGitHubアカウント
- `http://localhost:8080`で動作しているMCP電卓サービス

## GitHubトークンの取得

このアプリケーションはGitHub Modelsを使用するため、GitHubのパーソナルアクセストークンが必要です。以下の手順でトークンを取得してください。

### 1. GitHub Modelsにアクセス
1. [GitHub Models](https://github.com/marketplace/models)にアクセス
2. GitHubアカウントでサインイン
3. まだアクセス権がない場合は、GitHub Modelsへのアクセスをリクエスト

### 2. パーソナルアクセストークンの作成
1. [GitHub設定 → 開発者設定 → パーソナルアクセストークン → トークン（クラシック）](https://github.com/settings/tokens)に移動
2. 「新しいトークンを生成」→「新しいトークンを生成（クラシック）」をクリック
3. トークンにわかりやすい名前を付ける（例：「MCP Calculator Client」）
4. 必要に応じて有効期限を設定
5. 以下のスコープを選択：
   - `repo`（プライベートリポジトリにアクセスする場合）
   - `user:email`
6. 「トークンを生成」をクリック
7. **重要**：トークンはこの時点でしか表示されないので、必ずコピーしてください！

### 3. 環境変数の設定

#### Windows（コマンドプロンプト）:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows（PowerShell）:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## セットアップとインストール

1. **プロジェクトディレクトリをクローンまたは移動**

2. **依存関係のインストール**:
   ```cmd
   mvnw clean install
   ```
   または、Mavenがグローバルにインストールされている場合：
   ```cmd
   mvn clean install
   ```

3. **環境変数の設定**（上記「GitHubトークンの取得」セクション参照）

4. **MCP電卓サービスの起動**:
   1章のMCP電卓サービスが`http://localhost:8080/sse`で動作していることを確認してください。クライアントを起動する前にサービスが稼働している必要があります。

## アプリケーションの実行

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## アプリケーションの動作内容

このアプリケーションは電卓サービスとの3つの主なやり取りを示します：

1. **加算**：24.5と17.3の合計を計算
2. **平方根**：144の平方根を計算
3. **ヘルプ**：利用可能な電卓関数を表示

## 期待される出力

正常に実行されると、以下のような出力が表示されます：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## トラブルシューティング

### よくある問題

1. **「GITHUB_TOKEN環境変数が設定されていません」**
   - `GITHUB_TOKEN`環境変数が設定されているか確認
   - 変数設定後にターミナルやコマンドプロンプトを再起動

2. **「localhost:8080への接続が拒否されました」**
   - MCP電卓サービスがポート8080で動作しているか確認
   - 他のサービスがポート8080を使用していないか確認

3. **「認証に失敗しました」**
   - GitHubトークンが有効で正しい権限を持っているか確認
   - GitHub Modelsへのアクセス権があるか確認

4. **Mavenビルドエラー**
   - Java 21以上を使用しているか確認：`java -version`
   - ビルドのクリーンを試す：`mvnw clean`

### デバッグ

デバッグログを有効にするには、実行時に以下のJVM引数を追加してください：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

アプリケーションの設定内容：
- GitHub Modelsの`gpt-4.1-nano`モデルを使用
- MCPサービスに`http://localhost:8080/sse`で接続
- リクエストのタイムアウトは60秒
- デバッグ用にリクエスト/レスポンスのログを有効化

## 依存関係

本プロジェクトで使用している主な依存関係：
- **LangChain4j**：AI統合とツール管理用
- **LangChain4j MCP**：Model Context Protocol対応
- **LangChain4j GitHub Models**：GitHub Models連携用
- **Spring Boot**：アプリケーションフレームワークと依存性注入用

## ライセンス

本プロジェクトはApache License 2.0の下でライセンスされています。詳細は[LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)ファイルをご覧ください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
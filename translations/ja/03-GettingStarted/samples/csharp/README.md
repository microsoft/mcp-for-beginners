# Basic Calculator MCP Service

このサービスは、Model Context Protocol（MCP）を通じて基本的な計算機能を提供します。MCPの実装を学ぶ初心者向けのシンプルな例として設計されています。

詳細は[C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)をご覧ください。

## Features

この計算機サービスは以下の機能を提供します：

1. **基本的な算術演算**：
   - 2つの数の加算
   - 1つの数から別の数を減算
   - 2つの数の乗算
   - 1つの数を別の数で除算（ゼロ除算チェック付き）

## Using `stdio` Type
  
## Configuration

1. **MCPサーバーの設定**：
   - VS Codeでワークスペースを開きます。
   - ワークスペースフォルダー内に `.vscode/mcp.json` ファイルを作成し、MCPサーバーを設定します。設定例：

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - GitHubリポジトリのルートを入力するよう求められます。これはコマンド `git rev-parse --show-toplevel` で取得可能です。

## Using the Service

このサービスはMCPプロトコルを通じて以下のAPIエンドポイントを公開しています：

- `add(a, b)`: 2つの数を加算
- `subtract(a, b)`: 2番目の数を1番目の数から減算
- `multiply(a, b)`: 2つの数を乗算
- `divide(a, b)`: 1番目の数を2番目の数で除算（ゼロチェック付き）
- isPrime(n): 数が素数かどうかを判定

## Test with Github Copilot Chat in VS Code

1. MCPプロトコルを使ってサービスにリクエストを送ってみましょう。例えば、以下のように尋ねることができます：
   - 「5と3を足して」
   - 「4から10を引いて」
   - 「6と7を掛けて」
   - 「8を2で割って」
   - 「37854は素数ですか？」
   - 「4242の前後の3つの素数は何ですか？」
2. ツールを使っていることを明示するために、プロンプトに #MyCalculator を追加してください。例えば：
   - 「5と3を足して #MyCalculator」
   - 「4から10を引いて #MyCalculator」

## Containerized Version

.NET SDKがインストールされ、すべての依存関係が整っている場合は前述の方法が便利です。しかし、ソリューションを共有したり別の環境で実行したい場合は、コンテナ版を利用できます。

1. Dockerを起動し、動作していることを確認します。
1. ターミナルで `03-GettingStarted\samples\csharp\src` フォルダーに移動します。
1. 計算機サービスのDockerイメージをビルドするには、以下のコマンドを実行します（`<YOUR-DOCKER-USERNAME>`はDocker Hubのユーザー名に置き換えてください）：
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. イメージのビルドが完了したら、Docker Hubにアップロードします。以下のコマンドを実行してください：
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Use the Dockerized Version

1. `.vscode/mcp.json` ファイル内のサーバー設定を以下の内容に置き換えます：
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   設定を見ると、コマンドは `docker`、引数は `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc` となっています。`--rm` フラグはコンテナ停止後に削除することを保証し、`-i` フラグはコンテナの標準入力と対話できるようにします。最後の引数は先ほどビルドしてDocker Hubにプッシュしたイメージ名です。

## Test the Dockerized Version

`"mcp-calc": {` の上にある小さなスタートボタンをクリックしてMCPサーバーを起動し、前と同様に計算機サービスに計算を依頼してみましょう。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
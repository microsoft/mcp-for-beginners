# MCPサーバーのデプロイ

MCPサーバーをデプロイすることで、ローカル環境を超えて他のユーザーがそのツールやリソースにアクセスできるようになります。スケーラビリティ、信頼性、管理のしやすさなどの要件に応じて、いくつかのデプロイ戦略があります。以下では、ローカル環境、コンテナ、クラウドへのMCPサーバーのデプロイ方法について説明します。

## 概要

このレッスンでは、MCPサーバーアプリのデプロイ方法を扱います。

## 学習目標

このレッスンを終えるまでに、以下ができるようになります：

- さまざまなデプロイ方法を評価する。
- アプリをデプロイする。

## ローカル開発とデプロイ

サーバーがユーザーのマシン上で動作することを想定している場合は、以下の手順に従ってください：

1. **サーバーをダウンロードする**。サーバーを自分で作成していない場合は、まずマシンにダウンロードします。  
1. **サーバープロセスを起動する**：MCPサーバーアプリケーションを実行します。

SSEの場合（stdioタイプのサーバーでは不要です）

1. **ネットワーク設定**：サーバーが期待されるポートでアクセス可能であることを確認します。  
1. **クライアントを接続する**：`http://localhost:3000` のようなローカル接続URLを使用します。

## クラウドデプロイ

MCPサーバーはさまざまなクラウドプラットフォームにデプロイ可能です：

- **サーバーレス関数**：軽量なMCPサーバーをサーバーレス関数としてデプロイ  
- **コンテナサービス**：Azure Container Apps、AWS ECS、Google Cloud Runなどのサービスを利用  
- **Kubernetes**：高可用性のためにKubernetesクラスターでMCPサーバーをデプロイ・管理

### 例：Azure Container Apps

Azure Container AppsはMCPサーバーのデプロイをサポートしています。まだ開発途中ですが、現在はSSEサーバーをサポートしています。

手順は以下の通りです：

1. リポジトリをクローンします：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. ローカルで動作確認をします：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. ローカルで試すには、*.vscode*ディレクトリに*mcp.json*ファイルを作成し、以下の内容を追加します：

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  SSEサーバーが起動したら、JSONファイルの再生アイコンをクリックしてください。GitHub Copilotがサーバー上のツールを認識し、ツールアイコンが表示されるはずです。

1. デプロイするには、以下のコマンドを実行します：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

以上で、ローカルでのデプロイやAzureへのデプロイが完了します。

## 追加リソース

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 記事](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP リポジトリ](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## 次に進む

- 次へ：[実践的な実装](../../04-PracticalImplementation/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
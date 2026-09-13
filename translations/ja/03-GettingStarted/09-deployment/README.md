# MCPサーバーのデプロイ

> [!NOTE]
> `/sse` エンドポイントを使用する設定例はレガシーなHTTP+SSEトランスポートを対象としています。MCP `2026-07-28` リモートサーバーは通常 `/mcp` のようなサーバー定義のエンドポイントでStreamable HTTPを使用します。
> 
> 

MCPサーバーをデプロイすることで、ローカル環境を超えて他のユーザーがそのツールとリソースへアクセスできるようになります。スケーラビリティ、信頼性、管理の容易さなどの要件に応じて検討すべき複数のデプロイ戦略があります。以下に、ローカル、コンテナ、およびクラウドへのMCPサーバーのデプロイガイダンスを示します。

## 概要

このレッスンでは、MCPサーバーアプリのデプロイ方法を説明します。

## 学習目標

このレッスンの終了時には、以下ができるようになります。

- さまざまなデプロイ方法の評価。
- アプリをデプロイする。

## ローカル開発とデプロイ

サーバーがユーザーのマシン上で動作することを想定している場合、以下のステップを実行してください。

1. <strong>サーバーをダウンロードする</strong>。サーバーを自身で作成していない場合、まずマシンにダウンロードします。
1. <strong>サーバープロセスを開始する</strong>：MCPサーバーアプリケーションを実行します。

SSEの場合（stdioタイプサーバーには不要）

1. <strong>ネットワークを設定する</strong>：サーバーが期待されるポートでアクセス可能であることを確認します。
1. <strong>クライアントを接続する</strong>：`http://localhost:3000` のようなローカル接続URLを使用します。

## クラウドデプロイ

MCPサーバーはさまざまなクラウドプラットフォームにデプロイ可能です：

- <strong>サーバーレス関数</strong>：軽量なMCPサーバーをサーバーレス関数としてデプロイ
- <strong>コンテナサービス</strong>：Azure Container Apps、AWS ECS、Google Cloud Runなどのサービスを利用
- **Kubernetes**：高可用性のためにKubernetesクラスターでMCPサーバーをデプロイおよび管理

### 例：Azure Container Apps

Azure Container AppsはMCPサーバーのデプロイをサポートしています。まだ開発途上であり、現在はSSEサーバーに対応しています。

方法は以下の通りです：

1. リポジトリをクローンします：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. ローカルで実行してテストします：

  ```sh
  uv venv
  uv sync

  # Linux/macOS
  export API_KEYS=<AN_API_KEY>
  # Windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. ローカルで試すには、<em>.vscode</em>ディレクトリに<em>mcp.json</em>ファイルを作成し、以下の内容を追加します：

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

  SSEサーバーが起動したら、JSONファイルの再生アイコンをクリックできます。GitHub Copilotがサーバー上のツールを認識し、ツールアイコンが表示されるはずです。

1. デプロイするには、以下のコマンドを実行します：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

これで、ローカルおよびAzureへのデプロイ方法がわかりました。

## 追加リソース

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps 記事](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP リポジトリ](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 次のステップ

- 次へ: [高度なサーバートピック](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
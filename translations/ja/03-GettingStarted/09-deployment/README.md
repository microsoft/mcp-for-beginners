# MCPサーバーのデプロイ

MCPサーバーをデプロイすることで、他のユーザーがローカル環境を超えてそのツールやリソースにアクセスできるようになります。スケーラビリティ、信頼性、管理のしやすさに応じて、検討すべきいくつかのデプロイ戦略があります。以下に、ローカル、コンテナ、およびクラウドへのMCPサーバーのデプロイ方法についてのガイダンスを示します。

## 概要

このレッスンでは、MCPサーバーアプリのデプロイ方法について説明します。

## 学習目標

このレッスンの終了時には、以下のことができるようになります：

- さまざまなデプロイ手法を評価する。
- アプリをデプロイする。

## ローカル開発とデプロイ

サーバーがユーザーのマシン上で実行されることを想定している場合、以下の手順に従うことができます：

1. **サーバーをダウンロード**。自分でサーバーを書いていない場合は、まずマシンにダウンロードします。 
1. **サーバープロセスを起動**：MCPサーバーアプリケーションを実行します。

SSEの場合（stdioタイプサーバーには不要です）

1. **ネットワーク設定**：サーバーが期待されるポートでアクセス可能であることを確認します。
1. **クライアントを接続**：`http://localhost:3000` のようなローカル接続URLを使用します。

## クラウドデプロイ

MCPサーバーはさまざまなクラウドプラットフォームにデプロイできます：

- **サーバーレス関数**：軽量のMCPサーバーをサーバーレス関数としてデプロイ
- **コンテナサービス**：Azure Container Apps、AWS ECS、Google Cloud Runなどのサービスを利用
- **Kubernetes**：高可用性のためにKubernetesクラスター上でMCPサーバーをデプロイ・管理

### 例：Azure Container Apps

Azure Container AppsはMCPサーバーのデプロイをサポートしています。まだ開発途中ですが、現在はSSEサーバーをサポートしています。

手順は次のとおりです：

1. リポジトリをクローンします：

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. ローカルで動作をテストします：

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # ウィンドウズ
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. ローカルで試すには、*.vscode* ディレクトリに *mcp.json* ファイルを作成し、以下の内容を追加します：

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

  SSEサーバーが起動すると、JSONファイルの再生アイコンをクリックできます。GitHub Copilotでサーバー上のツールが認識され、ツールアイコンが表示されるはずです。

1. デプロイするには、次のコマンドを実行します：

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

これで、ローカルにデプロイし、これらの手順でAzureにデプロイできます。

## 追加リソース

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps記事](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCPリポジトリ](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## 次に進むこと

- 次へ：[高度なサーバートピック](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語によるオリジナル文書を正式な情報源としてください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

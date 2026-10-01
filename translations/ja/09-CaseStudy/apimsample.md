# ケーススタディ: API ManagementでREST APIをMCPサーバーとして公開する

Azure API Managementは、APIエンドポイントの上にゲートウェイを提供するサービスです。仕組みとしては、Azure API ManagementがAPIの前にプロキシのように立ち、受信したリクエストに対して何をするかを決定します。

これを使うことで、以下のような多くの機能を追加できます：

- <strong>セキュリティ</strong>：APIキー、JWT、マネージドIDまで幅広く利用可能です。
- <strong>レート制限</strong>：一定時間あたりの呼び出し回数を制限できる優れた機能です。これにより、すべてのユーザーが優れた体験を得られ、またサービスが過負荷になるのを防ぎます。
- <strong>スケーリングとロードバランシング</strong>：複数のエンドポイントを設定して負荷を分散し、どのように「ロードバランス」するかも決められます。
- **意味キャッシュ、トークン制限やトークン監視などのAI機能**：これらは応答性を向上させ、トークンの消費管理にも役立つ優れた機能です。[詳細はこちら](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## なぜMCPとAzure API Managementを使うのか？

Model Context Protocolは、エージェント型AIアプリやツール・データを一貫した形で公開するための規格として急速に普及しています。Azure API ManagementはAPIを「管理」する際の自然な選択肢です。MCPサーバーはしばしば他のAPIとも統合して、例えばツールへリクエストを解決します。したがって、Azure API ManagementとMCPを組み合わせるのは理にかなっています。

## 概要

本ユースケースでは、APIエンドポイントをMCPサーバーとして公開する方法を学びます。これにより、これらのエンドポイントをエージェント型アプリの一部に簡単に組み込みながら、Azure API Managementの機能を活用できます。

## 主要な機能

- 公開したいエンドポイントのメソッドをツールとして選択できます。
- 追加で得られる機能は、APIのポリシーセクションで設定した内容によりますが、ここではレート制限の追加方法を示します。

## 前提ステップ: APIをインポートする

もしすでにAzure API ManagementにAPIがあるならこのステップはスキップ可能です。ない場合は、こちらのリンクをご覧ください、[Azure API ManagementへのAPIのインポート](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## APIをMCPサーバーとして公開する

APIエンドポイントを公開するには、以下の手順に従います：

1. Azureポータルにアクセスし、次のアドレスへ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
API Managementインスタンスに移動します。

1. 左メニューで、APIs > MCP Servers > + 新しいMCPサーバーの作成 を選択します。

1. APIの欄で、MCPサーバーとして公開するREST APIを選択します。

1. 1つ以上のAPI操作をツールとして公開するために選択します。すべての操作または特定の操作のみを選択可能です。

    ![公開するメソッドを選択](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. <strong>作成</strong>を選択します。

1. メニューの<strong>APIs</strong>と<strong>MCP Servers</strong>に移動すると次のように表示されます：

    ![メインペインのMCPサーバー](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCPサーバーが作成され、API操作がツールとして公開されました。MCP ServersペインにMCPサーバーがリストされます。URL列には、テストやクライアントアプリから呼び出し可能なMCPサーバーのエンドポイントが表示されています。

## オプション: ポリシーの構成

Azure API Managementにはポリシーという核心概念があり、レート制限や意味的キャッシュのようにエンドポイントに適用する様々なルールを設定できます。これらのポリシーはXMLで作成されます。

MCPサーバーのレート制限ポリシーを設定する例は以下の通りです：

1. ポータルでAPIsの下の<strong>MCP Servers</strong>を選びます。

1. 作成したMCPサーバーを選択します。

1. 左メニューのMCPの下で<strong>Policies</strong>を選択します。

1. ポリシーエディターで、MCPサーバーのツールに適用したいポリシーを追加・編集します。ポリシーはXMLフォーマットで定義されており、例えばクライアントIPアドレスごとに30秒あたり5回の呼び出し制限を設定する場合のXMLは次の通りです：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ポリシーエディターの画像はこちらです：

    ![ポリシーエディター](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 試してみる

MCPサーバーが意図通りに動作しているか確認しましょう。

> [!NOTE]
> Azure API Managementは現在このサーバーをStreamable HTTPの`/mcp`エンドポイントで公開しています。旧来のHTTP+SSEの`/sse`トランスポートは非推奨で、レガシークライアントでのみ使用してください。
>
>

ここではVisual Studio CodeとGitHub Copilotのエージェントモードを使います。MCPサーバーを<em>mcp.json</em>に追加します。これにより、Visual Studio Codeはエージェント機能を持つクライアントとして動作し、エンドユーザーはプロンプトを入力してサーバーと対話できます。

Visual Studio CodeでMCPサーバーを追加する方法を見てみましょう：

1. コマンドパレットからMCP: <strong>Add Serverコマンド</strong>を使用します。

1. サーバータイプを選択するよう求められたら、<strong>HTTP (HTTP または Server Sent Events)</strong>を選択します。

1. API ManagementにあるMCPサーバー用のStreamable HTTP URLを入力します。
    例：
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`

1. 任意のサーバーIDを入力します。これは重要な値ではありませんが、このサーバーインスタンスを識別するのに役立ちます。

1. 設定をワークスペース設定かユーザー設定のどちらに保存するか選択します。

    - <strong>ワークスペース設定</strong> - 設定は現在のワークスペース内でのみ利用可能な.vscode/mcp.jsonファイルに保存されます。

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - <strong>ユーザー設定</strong> - 設定はグローバルな<em>settings.json</em>ファイルに追加され、全ワークスペースで利用可能です。構成は概ね以下のようになります：

    ![ユーザー設定](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. またAzure API Managementへの適切な認証を確実に行うため、<strong>Ocp-Apim-Subscription-Key</strong>というヘッダーを設定に追加する必要があります。

    - これを設定に追加する方法はこちらです：

    ![認証用ヘッダーの追加](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)。この操作によりAPIキーの入力を求めるプロンプトが表示されます。このAPIキーはAzureポータル内のAzure API Managementインスタンスで確認できます。

   - <em>mcp.json</em>に直接追加する場合は次のように記述します：

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### エージェントモードの利用

設定または<em>.vscode/mcp.json</em>で準備が整いました。さっそく試してみましょう。

ここにサーバーから公開されたツールの一覧が表示されるツールアイコンがあるはずです：

![サーバーからのツール](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ツールアイコンをクリックすると、次のようなツール一覧が表示されます：

    ![ツール](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. チャット欄にプロンプトを入力してツールを呼び出します。例えば注文情報を取得するツールを選んだ場合、エージェントに注文について尋ねられます。以下は例のプロンプトです：

    ```text
    get information from order 2
    ```

    ツールアイコンが表示され、ツールの呼び出しを進めるか確認されます。続行すると以下のような出力が表示されます：

    ![プロンプトの結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上記の表示は設定したツールによりますが、要はテキスト形式で応答が得られるということです**


## 参考資料

詳しくはこちらをご覧ください：

- [Azure API ManagementとMCPのチュートリアル](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Pythonサンプル: Azure API ManagementでリモートMCPサーバーをセキュア化（実験的）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCPクライアント認可ラボ](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code用Azure API Management拡張機能でAPIをインポート・管理](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API CenterでリモートMCPサーバーを登録・検出](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Managementを用いた多くのAI機能を示す優れたリポジトリ
- [AI Gateway ワークショップ](https://azure-samples.github.io/AI-Gateway/) Azure Portalを使ったワークショップが含まれており、AI機能の評価を始めるには最適です。

## 次にやること

- 前に戻る: [ケーススタディの概要](./README.md)
- 次へ: [Azure AI トラベルエージェント](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

# ケーススタディ: API ManagementでREST APIをMCPサーバーとして公開する

Azure API Managementは、APIエンドポイントの上にゲートウェイを提供するサービスです。仕組みとしては、Azure API ManagementがAPIの前にプロキシとして機能し、受信リクエストに対して何を行うかを決定します。

これを使用することで、以下のような多くの機能を追加できます：

- **セキュリティ**: APIキー、JWT、マネージドIDなど、さまざまなセキュリティオプションを利用可能。
- **レート制限**: 一定時間内に通過できるリクエスト数を制限する機能。これにより、すべてのユーザーが快適に利用でき、サービスがリクエストで圧倒されるのを防ぎます。
- **スケーリングと負荷分散**: 複数のエンドポイントを設定して負荷を分散させることができ、負荷分散の方法も選択可能。
- **AI機能**: セマンティックキャッシング、トークン制限、トークンモニタリングなど。これらの機能は応答性を向上させ、トークン使用量を管理するのに役立ちます。[詳細はこちら](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## MCP + Azure API Managementの理由

Model Context Protocol (MCP)は、エージェント型AIアプリケーションやツール・データを一貫した方法で公開するための標準として急速に普及しています。APIを「管理」する必要がある場合、Azure API Managementは自然な選択肢です。MCPサーバーは、ツールへのリクエストを解決するために他のAPIと統合することがよくあります。そのため、Azure API ManagementとMCPを組み合わせることには多くの利点があります。

## 概要

このユースケースでは、APIエンドポイントをMCPサーバーとして公開する方法を学びます。これにより、これらのエンドポイントをエージェント型アプリケーションの一部として簡単に組み込むことができ、同時にAzure API Managementの機能を活用できます。

## 主な機能

- 公開したいエンドポイントメソッドを選択可能。
- 追加機能は、APIのポリシーセクションで設定した内容に依存します。ここでは、レート制限を追加する方法を紹介します。

## 事前ステップ: APIのインポート

すでにAzure API ManagementにAPIがある場合、このステップはスキップできます。ない場合は、[Azure API ManagementへのAPIのインポート](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)を参照してください。

## APIをMCPサーバーとして公開する

APIエンドポイントを公開するには、以下の手順に従います：

1. Azureポータルにアクセスし、次のアドレスに移動します: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   API Managementインスタンスに移動します。

1. 左側のメニューで、**APIs > MCP Servers > + Create new MCP Server**を選択します。

1. **API**で、MCPサーバーとして公開するREST APIを選択します。

1. ツールとして公開する1つ以上のAPI操作を選択します。すべての操作を選択することも、特定の操作だけを選択することも可能です。

    ![公開するメソッドを選択](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create**を選択します。

1. メニューオプションの**APIs**と**MCP Servers**に移動すると、次のように表示されます：

    ![メインペインにMCPサーバーを表示](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCPサーバーが作成され、API操作がツールとして公開されます。MCPサーバーはMCP Serversペインにリストされ、URL列にはテストやクライアントアプリケーション内で呼び出すためのMCPサーバーのエンドポイントが表示されます。

## オプション: ポリシーの設定

Azure API Managementには、エンドポイントに対してさまざまなルールを設定するためのポリシーというコアコンセプトがあります。たとえば、レート制限やセマンティックキャッシングなどです。これらのポリシーはXMLで記述されます。

以下は、MCPサーバーにレート制限を設定する方法です：

1. ポータルで、**APIs**の下にある**MCP Servers**を選択します。

1. 作成したMCPサーバーを選択します。

1. 左側のメニューで、**MCP > Policies**を選択します。

1. ポリシーエディターで、MCPサーバーのツールに適用するポリシーを追加または編集します。ポリシーはXML形式で定義されます。たとえば、クライアントIPアドレスごとに30秒間に5回の呼び出しを制限するポリシーを追加できます。以下はそのXML例です：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ポリシーエディターの画像はこちら：

    ![ポリシーエディター](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 試してみる

MCPサーバーが意図したとおりに動作しているか確認しましょう。

これには、Visual Studio CodeとGitHub Copilotのエージェントモードを使用します。MCPサーバーを*mcp.json*ファイルに追加します。これにより、Visual Studio Codeがエージェント機能を持つクライアントとして動作し、エンドユーザーがプロンプトを入力してサーバーと対話できるようになります。

以下は、Visual Studio CodeでMCPサーバーを追加する方法です：

1. コマンドパレットから**MCP: Add Server**コマンドを使用します。

1. プロンプトが表示されたら、サーバータイプを選択します：**HTTP (HTTP or Server Sent Events)**。

1. API Management内のMCPサーバーのURLを入力します。例：  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSEエンドポイントの場合)  
   または  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCPエンドポイントの場合)。  
   トランスポートの違いは`/sse`または`/mcp`です。

1. 任意のサーバーIDを入力します。この値は重要ではありませんが、このサーバーインスタンスが何であるかを覚えるのに役立ちます。

1. 設定をワークスペース設定またはユーザー設定に保存するか選択します。

  - **ワークスペース設定** - サーバー設定は現在のワークスペースでのみ利用可能な.vscode/mcp.jsonファイルに保存されます。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    または、トランスポートとしてストリーミングHTTPを選択した場合は少し異なります：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ユーザー設定** - サーバー設定はグローバル*settings.json*ファイルに追加され、すべてのワークスペースで利用可能です。設定は次のようになります：

    ![ユーザー設定](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. また、Azure API Managementに対して適切に認証されるようにヘッダーを追加する必要があります。**Ocp-Apim-Subscription-Key**というヘッダーを使用します。

    - 設定に追加する方法はこちら：

    ![認証用ヘッダーの追加](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)。これにより、APIキー値を入力するプロンプトが表示されます。この値はAzureポータルのAzure API Managementインスタンスで確認できます。

   - *mcp.json*に追加する場合は、次のように記述します：

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

### エージェントモードを使用する

これで、設定または*.vscode/mcp.json*のいずれかでセットアップが完了しました。試してみましょう。

ツールアイコンが次のように表示され、サーバーから公開されたツールがリストされます：

![サーバーからのツール](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ツールアイコンをクリックすると、次のようにツールのリストが表示されます：

    ![ツール](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. チャットにプロンプトを入力してツールを呼び出します。たとえば、注文に関する情報を取得するツールを選択した場合、エージェントに注文について尋ねることができます。以下はプロンプトの例です：

    ```text
    get information from order 2
    ```

    これで、ツールを呼び出すよう促すアイコンが表示されます。ツールの実行を続行するよう選択すると、次のような出力が表示されます：

    ![プロンプトの結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上記の内容は設定したツールによって異なりますが、基本的な考え方は上記のようにテキスト応答を得ることです。**

## 参考資料

以下でさらに学ぶことができます：

- [Azure API ManagementとMCPのチュートリアル](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Pythonサンプル: Azure API Managementを使用してリモートMCPサーバーをセキュアにする（実験的）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCPクライアント認証ラボ](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code用Azure API Management拡張機能を使用してAPIをインポートおよび管理する](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API CenterでリモートMCPサーバーを登録および検出する](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Managementを使用した多くのAI機能を示す優れたリポジトリ
- [AI Gatewayワークショップ](https://azure-samples.github.io/AI-Gateway/) Azureポータルを使用したワークショップを含み、AI機能を評価するための優れた出発点です。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤訳について、当社は一切の責任を負いません。
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ea28e5e566edd5969337fd0b191ba3f",
  "translation_date": "2025-07-16T21:38:54+00:00",
  "source_file": "03-GettingStarted/04-vscode/README.md",
  "language_code": "ja"
}
-->
# GitHub Copilot Agentモードでサーバーを利用する

Visual Studio CodeとGitHub Copilotはクライアントとして動作し、MCPサーバーを利用することができます。なぜそれをしたいのか疑問に思うかもしれませんね。つまり、MCPサーバーが持つ機能をIDE内から直接使えるようになるということです。例えばGitHubのMCPサーバーを追加すれば、特定のコマンドをターミナルで打つ代わりにプロンプトでGitHubを操作できるようになります。あるいは、自然言語で操作できる開発者体験を向上させる何かを想像してみてください。これで利点が見えてきましたよね？

## 概要

このレッスンでは、Visual Studio CodeとGitHub CopilotのAgentモードを使ってMCPサーバーのクライアントとして利用する方法を説明します。

## 学習目標

このレッスンを終える頃には、以下ができるようになります：

- Visual Studio Codeを通じてMCPサーバーを利用する。
- GitHub Copilotを使ってツールなどの機能を実行する。
- Visual Studio Codeを設定してMCPサーバーを検出・管理する。

## 使い方

MCPサーバーは以下の2つの方法で操作できます：

- ユーザーインターフェース：この章の後半で詳しく説明します。
- ターミナル：`code`実行ファイルを使ってターミナルから操作可能です。

  ユーザープロファイルにMCPサーバーを追加するには、--add-mcpコマンドラインオプションを使い、JSON形式のサーバー設定（{\"name\":\"server-name\",\"command\":...}）を指定します。

  ```
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

### スクリーンショット

![Visual Studio CodeでのMCPサーバー設定ガイド](../../../../translated_images/chat-mode-agent.729a22473f822216dd1e723aaee1f7d4a2ede571ee0948037a2d9357a63b9d0b.ja.png)  
![エージェントセッションごとのツール選択](../../../../translated_images/agent-mode-select-tools.522c7ba5df0848f8f0d1e439c2e96159431bc620cb39ccf3f5dc611412fd0006.ja.png)  
![MCP開発中のエラーを簡単にデバッグ](../../../../translated_images/mcp-list-servers.fce89eefe3f30032bed8952e110ab9d82fadf043fcfa071f7d40cf93fb1ea9e9.ja.png)

次のセクションでビジュアルインターフェースの使い方について詳しく説明します。

## アプローチ

大まかな流れは以下の通りです：

- MCPサーバーを見つけるための設定ファイルを用意する。
- サーバーを起動または接続し、利用可能な機能を取得する。
- GitHub Copilot Chatインターフェースを通じてその機能を使う。

流れがわかったところで、Visual Studio Codeを使ってMCPサーバーを利用する演習に挑戦しましょう。

## 演習：サーバーを利用する

この演習では、Visual Studio Codeを設定してMCPサーバーを見つけ、GitHub Copilot Chatインターフェースから利用できるようにします。

### -0- 事前準備：MCPサーバーの検出を有効にする

MCPサーバーの検出を有効にする必要があるかもしれません。

1. Visual Studio Codeで `ファイル -> 設定 -> 設定` に移動します。

1. 「MCP」で検索し、settings.jsonファイル内の `chat.mcp.discovery.enabled` を有効にします。

### -1- 設定ファイルを作成する

まず、プロジェクトのルートに設定ファイルを作成します。`.vscode`というフォルダを作り、その中にMCP.jsonというファイルを置きます。内容は以下のようになります：

```text
.vscode
|-- mcp.json
```

次に、サーバーのエントリを追加する方法を見てみましょう。

### -2- サーバーを設定する

*mcp.json*に以下の内容を追加します：

```json
{
    "inputs": [],
    "servers": {
       "hello-mcp": {
           "command": "node",
           "args": [
               "build/index.js"
           ]
       }
    }
}
```

上記はNode.jsで書かれたサーバーを起動する簡単な例です。その他のランタイムの場合は、`command`と`args`で適切な起動コマンドを指定してください。

### -3- サーバーを起動する

エントリを追加したら、サーバーを起動しましょう：

1. *mcp.json*内のエントリを見つけ、「再生」アイコンがあることを確認します：

  ![Visual Studio Codeでサーバーを起動](../../../../translated_images/vscode-start-server.8e3c986612e3555de47e5b1e37b2f3020457eeb6a206568570fd74a17e3796ad.ja.png)  

1. 「再生」アイコンをクリックすると、GitHub Copilot Chatのツールアイコンに利用可能なツールの数が増えます。ツールアイコンをクリックすると登録されたツールの一覧が表示されます。GitHub Copilotにツールをコンテキストとして使わせたい場合はチェックを入れたり外したりできます：

  ![Visual Studio Codeでツールを選択](../../../../translated_images/vscode-tool.0b3bbea2fb7d8c26ddf573cad15ef654e55302a323267d8ee6bd742fe7df7fed.ja.png)

1. ツールを実行するには、ツールの説明に合致するプロンプトを入力します。例えば「add 22 to 1」のようなプロンプトです：

  ![GitHub Copilotからツールを実行](../../../../translated_images/vscode-agent.d5a0e0b897331060518fe3f13907677ef52b879db98c64d68a38338608f3751e.ja.png)

  「23」と返答が返ってくるはずです。

## 課題

*mcp.json*にサーバーのエントリを追加し、サーバーの起動・停止ができることを確認してください。また、GitHub Copilot Chatインターフェースを通じてサーバー上のツールと通信できることも確認しましょう。

## 解答

[解答](./solution/README.md)

## 重要なポイント

この章のポイントは以下の通りです：

- Visual Studio Codeは複数のMCPサーバーとそのツールを利用できる優れたクライアントです。
- GitHub Copilot Chatインターフェースがサーバーとのやり取りの窓口となります。
- APIキーなどのユーザー入力をプロンプトで受け取り、*mcp.json*のサーバー設定に渡すことができます。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## 追加リソース

- [Visual Studio docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## 次に進む

- 次へ: [SSEサーバーの作成](../05-sse-server/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。

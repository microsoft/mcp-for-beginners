<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "858362ce0118de3fec0f9114bf396101",
  "translation_date": "2025-07-29T00:16:40+00:00",
  "source_file": "03-GettingStarted/README.md",
  "language_code": "ja"
}
-->
## はじめに  

[![最初のMCPサーバーを構築する](../../../translated_images/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.ja.png)](https://youtu.be/sNDZO9N4m9Y)

_(上の画像をクリックすると、このレッスンのビデオを視聴できます)_

このセクションは以下の複数のレッスンで構成されています：

- **1 最初のサーバー**: この最初のレッスンでは、最初のサーバーを作成し、インスペクターツールを使って確認する方法を学びます。これはサーバーをテストおよびデバッグするための貴重な方法です。[レッスンはこちら](01-first-server/README.md)

- **2 クライアント**: このレッスンでは、サーバーに接続できるクライアントを作成する方法を学びます。[レッスンはこちら](02-client/README.md)

- **3 LLMを使用したクライアント**: クライアントにLLMを追加することで、サーバーと「交渉」して何をすべきかを決定する、より優れた方法を学びます。[レッスンはこちら](03-llm-client/README.md)

- **4 Visual Studio CodeでGitHub Copilotエージェントモードを使用したサーバーの利用**: このレッスンでは、Visual Studio Code内でMCPサーバーを実行する方法を学びます。[レッスンはこちら](04-vscode/README.md)

- **5 SSE（サーバー送信イベント）からの利用**: SSEはサーバーからクライアントへのストリーミングの標準であり、HTTPを介してリアルタイムの更新をクライアントにプッシュすることを可能にします。[レッスンはこちら](05-sse-server/README.md)

- **6 MCPを使用したHTTPストリーミング（ストリーム可能なHTTP）**: 最新のHTTPストリーミング、進行状況通知、およびストリーム可能なHTTPを使用してスケーラブルなリアルタイムMCPサーバーとクライアントを実装する方法を学びます。[レッスンはこちら](06-http-streaming/README.md)

- **7 VSCode用AIツールキットの活用**: MCPクライアントとサーバーを利用およびテストする方法を学びます。[レッスンはこちら](07-aitk/README.md)

- **8 テスト**: このレッスンでは、サーバーとクライアントをさまざまな方法でテストする方法に特に焦点を当てます。[レッスンはこちら](08-testing/README.md)

- **9 デプロイ**: この章では、MCPソリューションをデプロイするさまざまな方法について学びます。[レッスンはこちら](09-deployment/README.md)

Model Context Protocol (MCP) は、アプリケーションがLLMにコンテキストを提供する方法を標準化するオープンプロトコルです。MCPをAIアプリケーションのUSB-Cポートのようなものと考えてください。さまざまなデータソースやツールにAIモデルを接続するための標準化された方法を提供します。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- C#、Java、Python、TypeScript、JavaScriptでMCPの開発環境をセットアップする
- カスタム機能（リソース、プロンプト、ツール）を備えた基本的なMCPサーバーを構築およびデプロイする
- MCPサーバーに接続するホストアプリケーションを作成する
- MCPの実装をテストおよびデバッグする
- 一般的なセットアップの課題とその解決策を理解する
- MCPの実装を人気のあるLLMサービスに接続する

## MCP環境のセットアップ

MCPを使い始める前に、開発環境を準備し、基本的なワークフローを理解することが重要です。このセクションでは、MCPをスムーズに始めるための初期設定手順を案内します。

### 前提条件

MCP開発に取り組む前に、以下を準備してください：

- **開発環境**: 選択した言語（C#、Java、Python、TypeScript、JavaScript）用の環境
- **IDE/エディタ**: Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm、またはその他のモダンなコードエディタ
- **パッケージマネージャー**: NuGet、Maven/Gradle、pip、npm/yarn
- **APIキー**: ホストアプリケーションで使用する予定のAIサービス用

### 公式SDK

次の章では、Python、TypeScript、Java、.NETを使用して構築されたソリューションを紹介します。以下は公式にサポートされているすべてのSDKです。

MCPは複数の言語向けに公式SDKを提供しています：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoftと共同で管理
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AIと共同で管理
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式TypeScript実装
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式Python実装
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 公式Kotlin実装
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AIと共同で管理
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 公式Rust実装

## 重要なポイント

- MCPの開発環境のセットアップは、言語固有のSDKを使用することで簡単に行えます
- MCPサーバーの構築には、明確なスキーマを持つツールの作成と登録が含まれます
- MCPクライアントは、拡張機能を活用するためにサーバーやモデルに接続します
- 信頼性の高いMCP実装には、テストとデバッグが不可欠です
- デプロイメントの選択肢は、ローカル開発からクラウドベースのソリューションまで多岐にわたります

## 練習

このセクションのすべての章で紹介される演習を補完するサンプルセットを用意しています。さらに、各章には独自の演習と課題も含まれています。

- [Java 計算機](./samples/java/calculator/README.md)
- [.Net 計算機](../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](./samples/javascript/README.md)
- [TypeScript 計算機](./samples/typescript/README.md)
- [Python 計算機](../../../03-GettingStarted/samples/python)

## 追加リソース

- [AzureでModel Context Protocolを使用してエージェントを構築する](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Appsを使用したリモートMCP（Node.js/TypeScript/JavaScript）](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCPエージェント](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 次に進む

次: [最初のMCPサーバーを作成する](01-first-server/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。

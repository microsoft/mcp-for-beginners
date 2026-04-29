## はじめに

[![Build Your First MCP Server](../../../translated_images/ja/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(上の画像をクリックすると、このレッスンのビデオを視聴できます)_

このセクションはいくつかのレッスンで構成されています：

- **1 最初のサーバー**、最初のレッスンでは、最初のサーバーを作成し、インスペクターツールで検査する方法を学びます。これはサーバーのテストとデバッグに役立ちます。[レッスンへ](01-first-server/README.md)

- **2 クライアント**、このレッスンでは、サーバーに接続できるクライアントの書き方を学びます。[レッスンへ](02-client/README.md)

- **3 LLMを追加したクライアント**、さらに良いクライアントの作成方法として、LLMを追加し、サーバーと「交渉」しながら動作させる方法を学びます。[レッスンへ](03-llm-client/README.md)

- **4 Visual Studio CodeでGitHub Copilotエージェントモードを使用する**。ここでは、Visual Studio Code内からMCPサーバーを実行する方法を見ていきます。[レッスンへ](04-vscode/README.md)

- **5 stdioトランスポートサーバー**、stdioトランスポートは、ローカルのMCPサーバーとクライアント間通信の標準として推奨されており、組み込みのプロセス分離を伴う安全なサブプロセス通信を提供します。[レッスンへ](05-stdio-server/README.md)

- **6 MCP（Streamable HTTP）を使用したHTTPストリーミング**。最新のHTTPストリーミングトランスポート（[MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http)で推奨されるリモートMCPサーバー向けアプローチ）、進捗通知、Streamable HTTPを使ったスケーラブルでリアルタイムなMCPサーバーとクライアントの実装について学びます。[レッスンへ](06-http-streaming/README.md)

- **7 VS Code 用 AI ツールキットの活用**、MCPクライアントとサーバーの利用とテストに役立つツールの活用方法を学びます。[レッスンへ](07-aitk/README.md)

- **8 テスト**。ここでは特にサーバーとクライアントを様々な方法でテストする方法に焦点をあてます。[レッスンへ](08-testing/README.md)

- **9 デプロイメント**。この章では、MCPソリューションの異なるデプロイ方法を見ていきます。[レッスンへ](09-deployment/README.md)

- **10 高度なサーバー利用法**。高度なサーバー利用法について説明します。[レッスンへ](./10-advanced/README.md)

- **11 認証**。Basic AuthからJWTやRBACを使ったシンプルな認証の追加方法を扱います。ここから始めて、第5章の高度なトピックや第2章の推奨事項による追加のセキュリティ強化も検討することを推奨します。[レッスンへ](./11-simple-auth/README.md)

- **12 MCPホスト**。Claude Desktop、Cursor、Cline、Windsurfなどの人気MCPホストクライアントの構成と利用方法、トランスポート種類やトラブルシューティングを学びます。[レッスンへ](./12-mcp-hosts/README.md)

- **13 MCP Inspector**。MCP Inspectorツールを用いてMCPサーバーを対話的にデバッグおよびテストする方法を学びます。ツール、リソース、プロトコルメッセージのトラブルシューティングも習得します。[レッスンへ](./13-mcp-inspector/README.md)

- **14 サンプリング**。MCPクライアントと連携するMCPサーバーの作成、特にLLM関連タスクでの協調作業を行います。[レッスンへ](./14-sampling/README.md)

- **15 MCPアプリ**。UI命令で応答も行うMCPサーバーを構築します。[レッスンへ](./15-mcp-apps/README.md)

Model Context Protocol (MCP)は、アプリケーションがLLMにコンテキストを提供する方法を標準化するオープンプロトコルです。MCPはUSB-Cポートのようなもので、AIモデルを様々なデータソースやツールに標準化された方法で接続します。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- C#, Java, Python, TypeScript, JavaScriptでMCPの開発環境をセットアップする
- カスタム機能（リソース、プロンプト、ツール）を備えた基本的なMCPサーバーの構築とデプロイ
- MCPサーバーに接続するホストアプリケーションの作成
- MCP実装のテストとデバッグ
- 一般的なセットアップの課題とその解決策を理解する
- MCP実装を人気のあるLLMサービスに接続する

## MCP環境のセットアップ

MCPを扱う前に、開発環境の準備と基本的なワークフローを理解することが重要です。このセクションでは、スムーズにMCPを始めるための初期設定手順を案内します。

### 前提条件

MCP開発に入る前に、以下を用意してください：

- **開発環境**：C#, Java, Python, TypeScript, JavaScriptから選択した言語の環境
- **IDE/エディター**：Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm、または任意のモダンコードエディター
- **パッケージマネージャー**：NuGet、Maven/Gradle、pip、npm/yarn
- **APIキー**：ホストアプリケーションで使用する予定のAIサービスのAPIキー

### 公式SDK

今後の章ではPython、TypeScript、Java、.NETを使ったソリューションが示されます。以下は公式にサポートされているSDKです。

MCPは複数の言語用に公式SDKを提供しています（[MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)に準拠）：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoftとの連携でメンテナンス
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AIと連携してメンテナンス
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式TypeScript実装
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式Python実装（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 公式Kotlin実装
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AIと連携してメンテナンス
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 公式Rust実装
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 公式Go実装

## 主なポイント

- MCPの開発環境は言語別SDKで簡単にセットアップ可能
- MCPサーバー構築にはスキーマ定義されたツールを作成・登録することが重要
- MCPクライアントはサーバーやモデルに接続し拡張機能を活用できる
- テストとデバッグは信頼性あるMCP実装に不可欠
- デプロイ方法はローカル開発からクラウドまで多様

## 練習

このセクションのすべての章で出てくる演習を補完するサンプルセットがあります。各章には独自の演習と課題も含まれています。

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## 追加リソース

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 次に進む

最初のレッスンから始めましょう： [最初のMCPサーバーを作成する](01-first-server/README.md)

このモジュールを完了したら次に進みます： [モジュール4：実践的な実装](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正本として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用に起因する誤解や誤訳について、一切の責任を負いかねますのでご了承ください。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

## はじめに  

[![Build Your First MCP Server](../../../translated_images/ja/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(このレッスンのビデオを見るには上の画像をクリックしてください)_

このセクションは複数のレッスンで構成されています：

- **1 あなたの最初のサーバー**、この最初のレッスンでは、初めてのサーバーの作成方法とインスペクター・ツールを使ってサーバーを検査する方法を学びます。これはサーバーのテストやデバッグに役立ちます。[レッスンへ](01-first-server/README.md)

- **2 クライアント**、このレッスンでは、サーバーに接続できるクライアントの書き方を学びます。[レッスンへ](02-client/README.md)

- **3 LLMを使ったクライアント**、クライアントを書くより良い方法として、クライアントにLLMを追加し、サーバーと「交渉」できるようにする方法を学びます。[レッスンへ](03-llm-client/README.md)

- **4 Visual Studio CodeでのGitHub Copilot Agentモードを使ったサーバーの利用**。ここではVisual Studio Code内でMCPサーバーを実行する様子を見ます。[レッスンへ](04-vscode/README.md)

- **5 stdioトランスポートサーバー** stdioトランスポートはローカルMCPサーバーとクライアント間の通信に推奨される標準で、プロセス分離を備えた安全なサブプロセスベースの通信を提供します。[レッスンへ](05-stdio-server/README.md)

- **6 MCPを使ったHTTPストリーミング（Streamable HTTP）**。最新のHTTPストリーミングトランスポート（[MCP仕様 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http)でリモートMCPサーバーに推奨されるアプローチ）、進捗通知、Streamable HTTPを使った拡張可能でリアルタイムなMCPサーバーとクライアントの実装方法を学びます。[レッスンへ](06-http-streaming/README.md)

- **7 VSCode用AIツールキットの活用** MCPクライアントとサーバーの消費とテスト方法を学びます。[レッスンへ](07-aitk/README.md)

- **8 テスト**。ここでは特にサーバーとクライアントをさまざまな方法でテストする方法に焦点を当てます。[レッスンへ](08-testing/README.md)

- **9 デプロイ**。この章ではMCPソリューションのさまざまなデプロイ方法を見ていきます。[レッスンへ](09-deployment/README.md)

- **10 高度なサーバー利用**。この章では高度なサーバーの使い方を扱います。[レッスンへ](./10-advanced/README.md)

- **11 認証**。この章ではBasic AuthからJWT、RBACまでの簡単な認証追加方法を解説します。まずここから始めて、次に第5章の高度なトピックを見て、第2章の推奨に従い追加のセキュリティ強化を行うことを推奨します。[レッスンへ](./11-simple-auth/README.md)

- **12 MCPホスト**。Claude Desktop、Cursor、Cline、Windsurfなどの人気MCPホストクライアントの設定と利用方法を学びます。トランスポートタイプやトラブルシューティングも扱います。[レッスンへ](./12-mcp-hosts/README.md)

- **13 MCPインスペクター**。MCPインスペクターツールを使って、MCPサーバーのインタラクティブなデバッグとテストを学びます。ツール、リソース、プロトコルメッセージのトラブルシューティングを習得します。[レッスンへ](./13-mcp-inspector/README.md)

- **14 サンプリング**。LLM関連タスクでMCPクライアントと協働するMCPサーバーを作成します（`2026-07-28`リリース候補では非推奨；`2025-11-25`までは有効）。[レッスンへ](./14-sampling/README.md)

- **15 MCPアプリ**。UI指示も返すMCPサーバーを構築します。[レッスンへ](./15-mcp-apps/README.md)

モデルコンテキストプロトコル（MCP）は、アプリケーションがLLMにコンテキストを提供する方法を標準化したオープンプロトコルです。MCPはAIアプリケーションのUSB-Cポートのようなもので、異なるデータソースやツールへAIモデルを標準化された方法で接続できます。

## 学習目標

このレッスンの終わりまでに、あなたは以下ができるようになります:

- MCPのC#、Java、Python、TypeScript、JavaScriptの開発環境をセットアップする
- カスタム機能（リソース、プロンプト、ツール）を備えた基本的なMCPサーバーを構築・デプロイする
- MCPサーバーに接続するホストアプリケーションを作成する
- MCP実装をテスト・デバッグする
- よくあるセットアップの課題とその解決策を理解する
- あなたのMCP実装を人気のLLMサービスに接続する

## MCP環境のセットアップ

MCPの作業を始める前に、開発環境を準備し基本的なワークフローを理解することが重要です。このセクションでは、MCPをスムーズに始めるための初期セットアップ手順を案内します。

### 前提条件

MCP開発に入る前に、以下を確認してください:

- <strong>開発環境</strong>: 選んだ言語（C#, Java, Python, TypeScript, JavaScript）用の環境
- **IDE/エディタ**: Visual Studio、Visual Studio Code、IntelliJ、Eclipse、PyCharm、または任意のモダンコードエディタ
- <strong>パッケージマネージャー</strong>: NuGet、Maven/Gradle、pip、またはnpm/yarn
- **APIキー**: ホストアプリケーションで使う予定の任意のAIサービス用


### 公式SDK

今後の章ではPython、TypeScript、Java、.NETを使ったソリューションを紹介します。以下は公式にサポートされているSDK一覧です。

MCPは複数言語向けに公式SDKを提供しています（[MCP仕様 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)に準拠）：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoftと共同でメンテナンス
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AIと共同でメンテナンス
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式のTypeScript実装
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式のPython実装（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 公式のKotlin実装
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AIと共同でメンテナンス
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 公式のRust実装
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 公式のGo実装

## 重要なポイントまとめ

- MCP開発環境は言語別SDKで簡単にセットアップ可能
- MCPサーバー構築は明確なスキーマを持つツールの作成と登録を含む
- MCPクライアントはサーバーやモデルに接続し拡張機能を活用する
- テストとデバッグは信頼できるMCP実装には不可欠
- デプロイはローカル開発からクラウドベースまで選択肢がある

## 実践

このセクションのすべての章で行う演習を補完するサンプルセットがあります。さらに各章には独自の演習と課題もあります。

- [Java 計算機](./samples/java/calculator/README.md)
- [.NET 計算機](../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](./samples/javascript/README.md)
- [TypeScript 計算機](./samples/typescript/README.md)
- [Python 計算機](../../../03-GettingStarted/samples/python)

## 追加リソース

- [Azureでモデルコンテキストプロトコルを使ったエージェント構築](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container AppsでのリモートMCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 次に進むべきこと

最初のレッスンから始めましょう：[はじめてのMCPサーバーを作成する](01-first-server/README.md)

このモジュールを完了したら、次に以下を続けてください：[モジュール4：実践的な実装](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

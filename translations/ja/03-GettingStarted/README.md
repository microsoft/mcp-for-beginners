## はじめに  

[![Build Your First MCP Server](../../../translated_images/ja/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(上の画像をクリックすると、このレッスンのビデオが見られます)_

このセクションは複数のレッスンで構成されています：

- **1 あなたの最初のサーバー**、この最初のレッスンでは、最初のサーバーの作成方法と、サーバーのテストやデバッグに便利なインスペクターツールでの検査方法を学びます、[レッスンへ](01-first-server/README.md)

- **2 クライアント**、このレッスンでは、サーバーに接続できるクライアントの作成方法を学びます、[レッスンへ](02-client/README.md)

- **3 LLM付きクライアント**、より良いクライアントの書き方として、サーバーと「交渉」できるようにLLMを追加する方法を学びます、[レッスンへ](03-llm-client/README.md)

- **4 Visual Studio CodeでサーバーのGitHub Copilotエージェントモードを利用する方法**。ここではVisual Studio Code内でMCPサーバーを実行する方法を見ていきます、[レッスンへ](04-vscode/README.md)

- **5 stdioトランスポートサーバー** stdioトランスポートはローカルMCPサーバークライアント間通信の推奨標準であり、プロセスの分離を備えた安全なサブプロセスベースの通信を提供します [レッスンへ](05-stdio-server/README.md)

- **6 MCPを使用したHTTPストリーミング（ストリーミング可能なHTTP）**。標準の
	リモートトランスポートについて[MCP仕様2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)を学びます、
	加えてレッスン内で保持されているレガシーのセッションベース実装についても説明します。
	[レッスンへ](06-http-streaming/README.md)

- **7 VSCode用AIツールキットの利用** MCPクライアントとサーバーの利用及びテスト方法、[レッスンへ](07-aitk/README.md)

- **8 テスト**。ここでは特にサーバーとクライアントを様々な方法でテストする方法に焦点を当てます、[レッスンへ](08-testing/README.md)

- **9 デプロイメント**。この章ではMCPソリューションの異なるデプロイ方法を見ていきます、[レッスンへ](09-deployment/README.md)

- **10 高度なサーバー活用**。この章は高度なサーバーの使い方をカバーします、[レッスンへ](./10-advanced/README.md)

- **11 認証**。この章ではBasic AuthからJWT、RBACを使ったシンプルな認証の追加方法を扱います。最初にここから始めて、第5章の高度なトピックや第2章の推奨に従った追加のセキュリティ強化を行うことを推奨します、[レッスンへ](./11-simple-auth/README.md)

- **12 MCPホスト**。Claude Desktop、Cursor、Cline、Windsurfなど人気のあるMCPホストクライアントの設定と利用、トランスポートの種類とトラブルシューティングを学びます、[レッスンへ](./12-mcp-hosts/README.md)

- **13 MCPインスペクター**。MCPインスペクターを使ってMCPサーバーをインタラクティブにデバッグ・テストします。ツール、リソース、プロトコルメッセージのトラブルシューティングを学びます、[レッスンへ](./13-mcp-inspector/README.md)


- **14 サンプリング**。`2025-11-25` のレガシーな Sampling プリミティブと、直接 LLM プロバイダー統合への新しい設計の移行方法を学びます。Sampling は MCP `2026-07-28` で非推奨となります。[レッスンへ](./14-sampling/README.md)
	どう新しい設計をダイレクト LLM プロバイダー統合に移行するかを学びます。Sampling は
	MCP `2026-07-28` で非推奨となります。[レッスンへ](./14-sampling/README.md)

- **15 MCP アプリ**。UI 指示にも応答する MCP サーバーを構築します。[レッスンへ](./15-mcp-apps/README.md)

Model Context Protocol (MCP) はアプリケーションが LLM にコンテキストを提供する方法を標準化したオープンプロトコルです。MCP を AI アプリケーションの USB-C ポートのように考えてください。異なるデータソースやツールに AI モデルを標準化された方法で接続する手段を提供します。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- C#, Java, Python, TypeScript, JavaScript での MCP 開発環境のセットアップ
- カスタム機能（リソース、プロンプト、ツール）を持つ基本的な MCP サーバーの構築とデプロイ
- MCP サーバーに接続するホストアプリケーションの作成
- MCP 実装のテストとデバッグ
- 一般的なセットアップの課題とその解決策の理解
- 人気のある LLM サービスへの MCP 実装の接続

## MCP 環境のセットアップ

MCP を使い始める前に、開発環境を準備し基本的なワークフローを理解することが重要です。このセクションでは、スムーズに MCP を開始するための初期設定手順を案内します。

### 前提条件

MCP 開発に取り組む前に、以下を準備してください：

- <strong>開発環境</strong>：選択する言語（C#, Java, Python, TypeScript または JavaScript）用
- **IDE/エディター**：Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm または最新のコードエディター
- <strong>パッケージマネージャー</strong>：NuGet, Maven/Gradle, pip または npm/yarn
- **API キー**：ホストアプリケーションで使用する予定の AI サービス用


### 公式 SDK

今後の章では Python, TypeScript,
Java, .NET を使ったソリューションを紹介します。以下が公式 SDK です。

MCP `2026-07-28` 用の SDK 対応は言語ごとに順次展開されています。
実例を実行する前に、そのパッケージのバージョンと SDK のリリースノートで
対応プロトコルの改訂を確認してください。詳細は
[公式 SDK リスト](https://modelcontextprotocol.io/docs/sdk)をご覧ください：
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft と共同メンテナンス
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI と共同メンテナンス
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 公式 TypeScript 実装
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 公式 Python 実装（FastMCP）
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 公式 Kotlin 実装
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI と共同メンテナンス
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 公式 Rust 実装
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - 公式 Go 実装

## 重要ポイントまとめ

- MCP 開発環境のセットアップは言語別 SDK で簡単に行える
- MCP サーバー構築は明確なスキーマを持つツールの作成と登録を含む

- MCPクライアントはサーバーやモデルに接続して拡張機能を活用します
- テストとデバッグは信頼性の高いMCP実装には不可欠です
- 展開オプションはローカル開発からクラウドベースのソリューションまで多岐にわたります

## 実践


このセクションのすべての章で見られる演習を補完するサンプルのセットがあります。さらに、各章にはそれぞれ独自の演習と課題もあります。

- [Java Calculator](./samples/java/calculator/README.md)
- [.NET Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## 追加のリソース

- [Azure 上の Model Context Protocol を使用したエージェントの構築](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps でのリモート MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP エージェント](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 次に進む

最初のレッスンから始めましょう: [Creating your first MCP Server](01-first-server/README.md)

このモジュールを完了したら、次へ進みましょう: [Module 4: Practical Implementation](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
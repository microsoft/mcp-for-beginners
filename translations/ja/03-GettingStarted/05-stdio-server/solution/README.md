# MCP stdio サーバーソリューション

> **⚠️ 重要**: これらのソリューションは、MCP仕様2025-06-18で推奨されている**stdioトランスポート**を使用するよう更新されています。従来のSSE（Server-Sent Events）トランスポートは廃止されました。

以下は、各ランタイムでstdioトランスポートを使用してMCPサーバーを構築するための完全なソリューションです：

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - 完全なstdioサーバー実装
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - asyncioを使用したPython stdioサーバー
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - 依存性注入を使用した.NET stdioサーバー

各ソリューションでは以下を示しています：
- stdioトランスポートのセットアップ
- サーバーツールの定義
- 適切なJSON-RPCメッセージ処理
- ClaudeのようなMCPクライアントとの統合

すべてのソリューションは最新のMCP仕様に準拠しており、最適なパフォーマンスとセキュリティを実現するために推奨されるstdioトランスポートを使用しています。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。
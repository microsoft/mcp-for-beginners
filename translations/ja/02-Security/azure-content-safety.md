# Azure Content Safetyによる高度なMCPセキュリティ

> **OWASP MCPリスク対応**: [MCP06 - 意図の流れの改ざん](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)

Azure Content Safetyは、MCPの実装セキュリティを強化するための強力なツールをいくつか提供します。実践的な実装体験については、[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) キャンプ3: I/Oセキュリティを参照してください。

## プロンプトシールド

MicrosoftのAIプロンプトシールドは、直接的および間接的なプロンプトインジェクション攻撃からの堅牢な保護を次の方法で提供します:

1. <strong>高度な検出</strong>: コンテンツに埋め込まれた悪意のある指示を機械学習で識別します。
2. <strong>スポットライト</strong>: AIシステムが有効な指示と外部入力を区別しやすくするために入力テキストを変換します。
3. <strong>区切り文字およびデータマーク</strong>: 信頼できるデータと信頼できないデータの境界をマークします。
4. **Content Safety統合**: Azure AI Content Safetyと連携して脱獄試行や有害コンテンツを検出します。
5. <strong>継続的な更新</strong>: Microsoftは新たな脅威に対する保護メカニズムを定期的に更新しています。

## MCPでのAzure Content Safetyの実装

このアプローチは多層防御を提供します:
- 処理前の入力スキャン
- 返却前の出力検証
- 既知の有害パターンに対するブロックリストの使用
- Azureの継続的に更新されるContent Safetyモデルの活用

## Azure Content Safetyリソース

MCPサーバーでAzure Content Safetyを実装する方法について詳しくは、以下の公式リソースをご覧ください:

1. [Azure AI Content Safety ドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safetyの公式ドキュメント。
2. [Prompt Shield ドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - プロンプトインジェクション攻撃を防ぐ方法について学べます。
3. [コンテンツ安全性 API リファレンス](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safetyの実装に関する詳細なAPIリファレンス。
4. [クイックスタート: C# を使用した Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C#を使った迅速な実装ガイド。
5. [コンテンツの安全性に関するクライアントライブラリ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - 各種プログラミング言語向けのクライアントライブラリ。
6. [ジェイルブレイクの試みの検出](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 脱獄試行の検出と防止に関する具体的なガイダンス。
7. [コンテンツの安全性を確保するためのベストプラクティス](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Content Safetyを効果的に実装するためのベストプラクティス。

より詳細な実装については、[Azure Content Safety 実装ガイド](./azure-content-safety-implementation.md)をご覧ください。

## 次のステップ

- 読む: [Azure Content Safety の実装](./azure-content-safety-implementation.md)
- 戻る: [セキュリティ モジュールの概要](./README.md)
- 次へ: [モジュール3: はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

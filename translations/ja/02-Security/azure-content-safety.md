# Azure Content Safetyを使った高度なMCPセキュリティ

> **対応するOWASP MCPリスク**: [MCP06 - コンテキストペイロードによるプロンプトインジェクション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)

Azure Content Safetyは、MCP実装のセキュリティを強化する強力なツールをいくつか提供しています。実践的な実装経験については、[MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/)キャンプ3：I/Oセキュリティを参照してください。

## プロンプトシールド

MicrosoftのAIプロンプトシールドは、直接的および間接的なプロンプトインジェクション攻撃に対して以下の方法で強力な保護を提供します：

1. **高度な検出**：機械学習を活用して、コンテンツに埋め込まれた悪意のある指示を特定します。
2. **スポットライト付与**：入力テキストを変換し、AIシステムが有効な指示と外部入力を区別しやすくします。
3. **区切り記号とデータマーキング**：信頼されたデータと信頼されていないデータの境界を明示します。
4. **Content Safetyとの統合**：Azure AI Content Safetyと連携して、脱獄試行や有害なコンテンツを検出します。
5. **継続的な更新**：Microsoftは新たな脅威に対抗するため、保護機構を定期的に更新しています。

## MCPでのAzure Content Safetyの実装

このアプローチは多層的な保護を提供します：
- 処理前の入力のスキャン
- 結果返却前の出力の検証
- 既知の有害パターンに対するブロックリストの使用
- Azureの継続的に更新されるContent Safetyモデルの活用

## Azure Content Safetyのリソース

MCPサーバーでAzure Content Safetyを実装する方法の詳細については、以下の公式リソースをご参照ください：

1. [Azure AI Content Safety ドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safetyの公式ドキュメント。
2. [プロンプトシールドドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - プロンプトインジェクション攻撃の防止方法について。
3. [Content Safety APIリファレンス](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety実装のための詳細なAPIリファレンス。
4. [クイックスタート：C#でのAzure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C#を使ったクイック実装ガイド。
5. [Content Safety クライアントライブラリ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - 各種プログラミング言語向けのクライアントライブラリ。
6. [脱獄試行の検出](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 脱獄試行の検出と防止に関する特定の指針。
7. [Content Safetyのベストプラクティス](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - 効果的なContent Safety実装のためのベストプラクティス。

より詳細な実装については、[Azure Content Safety実装ガイド](./azure-content-safety-implementation.md)をご覧ください。

## 次のステップ

- 読む： [Azure Content Safety実装](./azure-content-safety-implementation.md)
- 戻る： [セキュリティモジュール概要](./README.md)
- 続ける： [モジュール3：はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文の言語で記載された原文書が正式な情報源として優先されます。重要な情報については専門の人間による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

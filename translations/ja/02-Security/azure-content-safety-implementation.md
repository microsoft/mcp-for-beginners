# MCPでのAzure Content Safetyの実装

> **OWASP MCPリスク対応**: [MCP06 - コンテキストペイロードによるプロンプトインジェクション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)

プロンプトインジェクション、ツールポイズニング、その他AI固有の脆弱性に対してMCPのセキュリティを強化するために、Azure Content Safetyの統合を強く推奨します。この実装ガイドは、[MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/)キャンプ3：I/Oセキュリティに沿ったものです。

## MCPサーバーとの統合

Azure Content SafetyをMCPサーバーに統合するには、リクエスト処理パイプラインにコンテンツセーフティフィルターをミドルウェアとして追加します。

1. サーバー起動時にフィルターを初期化する
2. 処理前にすべての受信ツールリクエストを検証する
3. クライアントに返す前にすべての応答をチェックする
4. セーフティ違反を記録しアラートを発する
5. コンテンツセーフティチェック失敗時の適切なエラーハンドリングを実装する

これにより以下に対して強力な防御を提供します：
- プロンプトインジェクション攻撃
- ツールポイズニングの試み
- 悪意ある入力によるデータ持ち出し
- 有害なコンテンツの生成

## Azure Content Safety統合のベストプラクティス

1. **カスタムブロックリスト**: MCPインジェクションパターン専用のカスタムブロックリストを作成する
2. **重大度調整**: 特定のユースケースとリスク許容度に基づき重大度閾値を調整する
3. **包括的カバレッジ**: すべての入力および出力にコンテンツセーフティチェックを適用する
4. **パフォーマンス最適化**: 繰り返しのコンテンツセーフティチェックにキャッシュの実装を検討する
5. **フォールバック機構**: コンテンツセーフティサービスが利用できない場合の明確なフォールバック動作を定義する
6. **ユーザーフィードバック**: コンテンツがセーフティ上の理由でブロックされた場合、ユーザーへ明確なフィードバックを提供する
7. **継続的改善**: 新たな脅威に応じてブロックリストやパターンを定期的に更新する

## 追加リソース

### OWASP MCPセキュリティガイダンス
- [OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/) - Azure実装を含む包括的なOWASP MCP Top 10
- [MCP06 - プロンプトインジェクション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/) - 詳細なプロンプトインジェクション緩和パターン
- [MCPセキュリティサミットワークショップ](https://azure-samples.github.io/sherpa/) - ハンズオンキャンプ3：I/Oセキュリティでコンテンツセーフティを網羅

### Azureドキュメント
- [Azure Content Safetyの概要](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Prompt Shieldsのドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure AI Content Safetyクイックスタート](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text)

## 次のステップ

- 戻る：[セキュリティモジュール概要](./README.md)
- 続ける：[モジュール3: はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（原言語の文書）が正式な情報源としてご参照ください。重要な情報に関しては、専門の人間翻訳者による翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤読についても、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

# MCPでのAzure Content Safetyの実装

> **対応するOWASP MCPリスク**: [MCP06 - インテントフローのサブバージョン](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)

MCPのセキュリティをプロンプトインジェクション、ツールのポイズニング、その他AI固有の脆弱性から強化するために、Azure Content Safetyの統合が強く推奨されます。本実装ガイドは、[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) のCamp 3: I/O Securityに準拠しています。

## MCPサーバーとの統合

Azure Content SafetyをMCPサーバーに統合するには、リクエスト処理パイプラインのミドルウェアとしてコンテンツセーフティフィルターを追加します：

1. サーバー起動時にフィルターを初期化する
2. 処理前にすべての着信ツールリクエストを検証する
3. クライアントに返却する前にすべての応答をチェックする
4. セーフティ違反をログ記録およびアラートする
5. コンテンツセーフティチェックが失敗した場合の適切なエラーハンドリングを実装する

これにより以下に対する堅牢な防御が提供されます：
- プロンプトインジェクション攻撃
- ツールのポイズニング試行
- 悪意のある入力によるデータの持ち出し
- 有害コンテンツの生成

## Azure Content Safety統合のベストプラクティス

1. <strong>カスタムブロックリスト</strong>：MCPインジェクションパターン専用のカスタムブロックリストを作成する
2. <strong>重大度調整</strong>：特定のユースケースやリスク許容度に基づいて重大度閾値を調整する
3. <strong>包括的カバレッジ</strong>：すべての入力と出力にコンテンツセーフティチェックを適用する
4. <strong>パフォーマンス最適化</strong>：繰り返しのコンテンツセーフティチェックに対してキャッシュの実装を検討する
5. <strong>フォールバック機構</strong>：コンテンツセーフティサービスが利用不可の場合の明確なフォールバック動作を定義する
6. <strong>ユーザーフィードバック</strong>：コンテンツがセーフティ懸念でブロックされた際に明確なフィードバックをユーザーに提供する
7. <strong>継続的改善</strong>：新興の脅威に基づいてブロックリストやパターンを定期的に更新する

## 追加リソース

### OWASP MCPセキュリティガイダンス
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Azure実装を含む包括的なOWASP MCPトップ10
- [MCP06 - プロンプトインジェクション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/) - 詳細なプロンプトインジェクション緩和パターン
- [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) - 実践的なCamp 3: I/O Securityではコンテンツセーフティをカバー

### Azureドキュメンテーション
- [Azure Content Safety概要](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Prompt Shieldsドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure AI Content Safetyクイックスタート](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text)

## 次のステップ

- 戻る：[セキュリティモジュール概要](./README.md)
- 続ける：[モジュール3: はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

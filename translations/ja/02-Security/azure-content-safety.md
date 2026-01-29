# Azure Content Safetyによる高度なMCPセキュリティ

Azure Content Safetyは、MCPの実装におけるセキュリティを強化するための強力なツールをいくつか提供しています。

## Prompt Shields

MicrosoftのAI Prompt Shieldsは、直接的および間接的なプロンプトインジェクション攻撃から強力に保護します。具体的には以下の方法で対応しています：

1. **高度な検出**：機械学習を用いて、コンテンツに埋め込まれた悪意のある指示を識別します。
2. **スポットライト機能**：入力テキストを変換し、AIシステムが有効な指示と外部からの入力を区別しやすくします。
3. **区切り文字とデータマーキング**：信頼できるデータと信頼できないデータの境界を明示します。
4. **Content Safetyとの統合**：Azure AI Content Safetyと連携し、脱獄試行や有害なコンテンツを検出します。
5. **継続的なアップデート**：Microsoftは新たな脅威に対応するため、保護機能を定期的に更新しています。

## MCPでのAzure Content Safetyの実装

この方法は多層的な保護を提供します：
- 処理前の入力スキャン
- 返却前の出力検証
- 既知の有害パターンに対するブロックリストの利用
- Azureの継続的に更新されるContent Safetyモデルの活用

## Azure Content Safetyのリソース

MCPサーバーでAzure Content Safetyを実装する方法については、以下の公式リソースをご参照ください：

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safetyの公式ドキュメント。
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - プロンプトインジェクション攻撃の防止方法。
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safetyの詳細なAPIリファレンス。
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C#を使った迅速な実装ガイド。
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - 各種プログラミング言語向けのクライアントライブラリ。
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 脱獄試行の検出と防止に関する具体的なガイダンス。
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - 効果的なContent Safety実装のベストプラクティス。

より詳細な実装については、[Azure Content Safety Implementation guide](./azure-content-safety-implementation.md)をご覧ください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
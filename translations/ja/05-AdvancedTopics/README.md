# MCPの高度なトピック

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/ja/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(上の画像をクリックすると、このレッスンのビデオが表示されます)_

本章では、モデルコンテキストプロトコル（MCP）実装の高度なトピックを一連で扱います。マルチモーダル統合、スケーラビリティ、セキュリティのベストプラクティス、エンタープライズ統合などを含みます。これらのトピックは、現代のAIシステムの要求に応えられる堅牢で製品投入可能なMCPアプリケーション構築に重要です。

## 概要

このレッスンでは、モデルコンテキストプロトコル実装における高度な概念を探求します。特にマルチモーダル統合、スケーラビリティ、セキュリティのベストプラクティス、エンタープライズ統合に焦点を当てています。これらは、エンタープライズ環境での複雑な要件に対応できる製品品質のMCPアプリケーション構築に不可欠です。

> **現在の仕様に関する注意:** MCP `2026-07-28`はレッスン5.4と5.6で扱うRootsおよびSamplingプリミティブを廃止します。また、プロトコル機能（5.16）で参照される実験的なTasks機能を専用のTasks拡張に移行しました。それらのレッスンはレガシー`2025-11-25`実装のために保持されており、移行ガイダンスを含みます。詳細は[What's Changed in MCP: The 2026-07-28 Specification](../01-CoreConcepts/mcp-2026-07-28.md)を参照してください。






## 学習目標

このレッスンの終わりまでに、以下が可能になります：

- MCPフレームワーク内でのマルチモーダル機能の実装
- 高負荷シナリオに対応するスケーラブルなMCPアーキテクチャの設計
- MCPのセキュリティ原則に沿ったベストプラクティスの適用
- MCPをエンタープライズAIシステムやフレームワークと統合
- 製品環境でのパフォーマンスと信頼性の最適化

## レッスンとサンプルプロジェクト

| Link | タイトル | 説明 |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Azureとの統合 | Azure上でMCPサーバーを統合する方法を学ぶ |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCPマルチモーダルサンプル | 音声、画像、マルチモーダル応答のサンプル |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2デモ | OAuth2を用いたMCPの最小限Spring Bootアプリ。認可とリソースサーバーの両方として機能し、セキュアなトークン発行、保護されたエンドポイント、Azure Container Appsへのデプロイ、API Management統合を示します。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | ルートコンテキスト | レガシーな`2025-11-25`ルートプリミティブと現在の移行オプション（`2026-07-28`で非推奨）を学ぶ |
| [5.5 Routing](./mcp-routing/README.md) | ルーティング | さまざまな種類のルーティングについて学ぶ |
| [5.6 Sampling](./mcp-sampling/README.md) | サンプリング | レガシーな`2025-11-25`サンプリングプリミティブと現在の移行オプション（`2026-07-28`で非推奨）を学ぶ |
| [5.7 Scaling](./mcp-scaling/README.md) | スケーリング | スケーリングについて学ぶ |
| [5.8 Security](./mcp-security/README.md) | セキュリティ | MCPサーバーを保護する |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web検索MCP | SerpAPIと統合したPython MCPサーバーとクライアント。リアルタイムのウェブ、ニュース、製品検索、Q&Aを提供。マルチツールオーケストレーション、外部API統合、堅牢なエラーハンドリングを示す。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | ストリーミング | 今日のデータ駆動型世界では、ビジネスやアプリケーションが迅速な意思決定のためリアルタイムで情報にアクセスすることが不可欠となっている。|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web検索 | MCPがAIモデル、検索エンジン、アプリケーション間で標準化されたコンテキスト管理を提供し、リアルタイムウェブ検索をどのように変革するか。| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID認証 | Microsoft Entra IDはクラウドベースの強力なアイデンティティ・アクセス管理ソリューションを提供し、認可されたユーザーとアプリケーションのみがMCPサーバーとやり取りできるようにします。|
| [5.13 Microsoft Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Microsoft Foundry統合 | MCPサーバーをMicrosoft Foundryエージェントと統合し、標準化された外部データソース接続による強力なツールオーケストレーションとエンタープライズAI機能を実現する方法を学ぶ。|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | コンテキストエンジニアリング | MCPサーバー向けの将来的なコンテキストエンジニアリング技術の機会。コンテキスト最適化、動的コンテキスト管理、効果的なプロンプトエンジニアリング戦略をMCPフレームワーク内で扱う。|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | カスタムトランスポート | 専用のMCP通信シナリオのためのカスタムトランスポート機構の実装方法を学ぶ。|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | プロトコル機能 | 進捗通知、要求キャンセル、リソーステンプレート、エラーハンドリングパターンなどの高度なプロトコル機能を習得する。|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 反対多エージェント | 対立する立場の2つのエージェントが単一のMCPツールセットを共有して、幻覚を見破り、エッジケースを浮かび上がらせ、構造化された議論を通じてより良く校正された出力を生成する。|

> **歴史的な`2025-11-25`注:** その改訂では実験的なTasksが導入され、いくつかのプロトコル機能が拡張されました。`2026-07-28`ではTasksは公式の拡張に移動し、Rootsは非推奨となりました。`2025-11-25`の機能ステータスを現在の指針として使用しないでください。詳細は[2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)を参照してください。





## 追加参考資料

最新の高度なMCPトピック情報については、以下を参照してください：
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - セキュリティリスクと緩和策
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - ハンズオンセキュリティトレーニング

## 主要ポイント

- マルチモーダルのMCP実装はテキスト処理を超えたAI機能を拡張する
- スケーラビリティはエンタープライズ展開に不可欠であり、水平方向および垂直方向のスケーリングで対応可能
- 包括的なセキュリティ対策でデータを保護し、適切なアクセス制御を確保
- Azure OpenAIやMicrosoft AI Foundryなどのプラットフォームとのエンタープライズ統合によりMCPの機能が強化される
- 高度なMCP実装には最適化されたアーキテクチャと慎重なリソース管理が有益

## 演習

特定のユースケースに対するエンタープライズ級のMCP実装を設計してください：

1. ユースケースのマルチモーダル要件を特定する
2. 機微なデータを保護するためのセキュリティコントロールを概説する
3. 変動する負荷に対応可能なスケーラブルなアーキテクチャを設計する
4. エンタープライズAIシステムとの統合ポイントを計画する
5. 潜在的なパフォーマンスボトルネックと緩和策を文書化する

## 追加リソース

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## 次に進むには

このモジュールのレッスンを[5.1 MCP 統合](./mcp-integration/README.md)から開始してください

このモジュールを完了したら、次は[モジュール6: コミュニティと貢献](../06-CommunityContributions/README.md)へ進みましょう

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

# MCPの高度なトピック

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/ja/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(上の画像をクリックするとこのレッスンのビデオを視聴できます)_

この章では、Model Context Protocol（MCP）実装における一連の高度なトピックを扱います。マルチモーダル統合、スケーラビリティ、セキュリティのベストプラクティス、エンタープライズ統合などが含まれます。これらのトピックは、現代のAIシステムの要求に応える堅牢でプロダクション対応のMCPアプリケーションを構築するために重要です。

## 概要

このレッスンでは、Model Context Protocolの実装における高度な概念を探ります。マルチモーダル統合、スケーラビリティ、セキュリティのベストプラクティス、エンタープライズ統合に焦点を当てています。これらのトピックは、エンタープライズ環境で複雑な要件を処理できるプロダクショングレードのMCPアプリケーション構築に不可欠です。

## 学習目標

このレッスンの終了時には、以下を実行できるようになります：

- MCPフレームワーク内でマルチモーダル機能を実装する
- 高負荷シナリオ向けにスケーラブルなMCPアーキテクチャを設計する
- MCPのセキュリティ原則に準拠したベストプラクティスを適用する
- MCPをエンタープライズAIシステムやフレームワークと統合する
- プロダクション環境におけるパフォーマンスと信頼性を最適化する

## レッスンとサンプルプロジェクト

| Link | タイトル | 説明 |
|------|----------|-------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Azureとの統合 | Azure上でMCPサーバーを統合する方法を学ぶ |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCPマルチモーダルサンプル | 音声、画像、マルチモーダルレスポンスのサンプル |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2デモ | AuthorizationとResource Server両方を示すMCPのOAuth2を用いた最小限のSpring Bootアプリ。安全なトークン発行、保護されたエンドポイント、Azure Container Appsへのデプロイ、API Managementの統合を実演。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | ルートコンテキスト | ルートコンテキストの詳細と実装方法を学ぶ |
| [5.5 Routing](./mcp-routing/README.md) | ルーティング | さまざまなタイプのルーティングを学ぶ |
| [5.6 Sampling](./mcp-sampling/README.md) | サンプリング | サンプリングの扱い方を学ぶ |
| [5.7 Scaling](./mcp-scaling/README.md) | スケーリング | スケーリングについて学ぶ |
| [5.8 Security](./mcp-security/README.md) | セキュリティ | MCPサーバーのセキュリティを強化する |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web検索MCP | SerpAPIと統合したPython MCPサーバーとクライアントで、リアルタイムのウェブ・ニュース・製品検索およびQ&Aを実現。マルチツールのオーケストレーション、外部API連携、堅牢なエラーハンドリングを示す。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | ストリーミング | 今日のデータ駆動型社会では、ビジネスやアプリケーションが即時に情報アクセスを必要とするため、リアルタイムデータストリーミングが不可欠となっている。 |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | ウェブ検索 | MCPはAIモデル、検索エンジン、アプリケーション間でのコンテキスト管理を標準化する方法を提供し、リアルタイムのウェブ検索を変革する。 |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID認証 | Microsoft Entra IDはクラウドベースの堅牢なIDとアクセス管理ソリューションを提供し、許可されたユーザーとアプリケーションだけがMCPサーバーとやり取りできるよう支援。 |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry統合 | MCPサーバーをAzure AI Foundryエージェントと統合し、標準化された外部データソース接続による強力なツールオーケストレーションとエンタープライズAI機能を実現する方法を学ぶ。 |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | コンテキストエンジニアリング | MCPサーバーにおける将来のコンテキストエンジニアリング技術の機会、コンテキストの最適化、動的管理、効果的なプロンプトエンジニアリング戦略を含む。 |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | カスタムトランスポート | 特定のMCP通信シナリオ向けにカスタムトランスポート機構を実装する方法を学ぶ。 |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | プロトコル機能 | 進捗通知、リクエストキャンセル、リソーステンプレート、エラーハンドリングパターンなどの高度なプロトコル機能を習得。 |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 対立マルチエージェント | 対立する立場を持つ二つのエージェントが単一のMCPツールセットを共有して、幻覚検出、エッジケース顕在化、構造化討論によるより良い評価出力を実現。 |

> **MCP仕様 2025-11-25 新機能**: 仕様に実験的サポートとして、<strong>タスク</strong>（進捗追跡可能な長時間実行オペレーション）、<strong>ツール注釈</strong>（安全性のためのツール動作メタデータ）、**URLモードエリシテーション**（クライアントへ特定URLコンテンツのリクエスト）、および強化された<strong>ルーツ</strong>（作業スペースコンテキスト管理）が含まれるようになりました。詳細は[MCP仕様の変更ログ](https://spec.modelcontextprotocol.io/)を参照してください。

## 追加参考資料

高度なMCPトピックの最新情報については以下を参照してください：
- [MCPドキュメント](https://modelcontextprotocol.io/)
- [MCP仕様（2025-11-25）](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHubリポジトリ](https://github.com/modelcontextprotocol)
- [OWASP MCPトップ10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - セキュリティリスクと対策
- [MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/) - 実践的なセキュリティトレーニング

## 重要ポイント

- マルチモーダルMCP実装はテキスト処理を越えたAIの能力を拡張する
- スケーラビリティはエンタープライズ展開に不可欠であり、水平方向および垂直方向のスケーリングで対応可能
- 包括的なセキュリティ対策によりデータ保護と適切なアクセス制御を実現
- Azure OpenAIやMicrosoft AI Foundryなどのプラットフォームとのエンタープライズ統合でMCPの能力が向上
- 高度なMCP実装は最適化されたアーキテクチャと資源管理の慎重な設計により恩恵を受ける

## 演習

特定のユースケース向けにエンタープライズグレードのMCP実装を設計してください：

1. ユースケースのマルチモーダル要件を特定する
2. 機微なデータを保護するためのセキュリティ制御を概説する
3. 変動する負荷に対応可能なスケーラブルなアーキテクチャを設計する
4. エンタープライズAIシステムとの統合ポイントを計画する
5. 潜在的なパフォーマンスのボトルネックと緩和策を文書化する

## 追加リソース

- [Azure OpenAI ドキュメント](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry ドキュメント](https://learn.microsoft.com/en-us/ai-services/)

---

## 次に進むには

このモジュールのレッスンを[5.1 MCP Integration](./mcp-integration/README.md)から始めてください。

このモジュール完了後は、[モジュール 6: コミュニティ貢献](../06-CommunityContributions/README.md)に進んでください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文のネイティブ言語での文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤訳について、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP セキュリティベストプラクティス - 2026年9月更新

本包括的ガイドは、Model Context Protocol（MCP）システムの実装に関する必須のセキュリティベストプラクティスを
**MCP Specification 2026-07-28** および現行の業界標準に基づいて概説しています。これらの
プラクティスは、従来のセキュリティ問題とMCP展開に特有のAI関連脅威の両方に対応しています。



## 重要なセキュリティ要件

### 必須のセキュリティコントロール（MUST要件）

1. <strong>トークン検証</strong>：MCPサーバーは、MCPサーバー自体に明示的に発行されたトークン以外は<strong>受け入れてはならない</strong>
2. <strong>認可検証</strong>：認可を実装するMCPサーバーはすべての受信リクエストを検証し、認証にセッションを使用してはならない
3. <strong>ユーザー同意</strong>：静的なサードパーティクライアントIDを使用するMCPプロキシサーバーは、認可フローを転送する前に各MCPクライアントの明示的な同意を得なければならない
4. <strong>状態ハンドルのセキュリティ</strong>：MCPサーバーは、アプリケーション状態ハンドルの所持を認証とみなしてはならず、
	使用されるすべてのリクエストを認可しなければならない


## コアセキュリティプラクティス

### 1. 入力検証とサニタイズ
- <strong>包括的な入力検証</strong>：すべての入力を検証およびサニタイズし、インジェクション攻撃、混乱代理問題、プロンプトインジェクションの脆弱性を防止する
- <strong>パラメータスキーマの適用</strong>：すべてのツールパラメータおよびAPI入力に対して厳格なJSONスキーマ検証を実装する
- <strong>コンテンツフィルタリング</strong>：Microsoft Prompt Shields と Azure Content Safety を使用して、プロンプトおよびレスポンスにおける悪意のあるコンテンツをフィルタリングする
- <strong>出力のサニタイズ</strong>：ユーザーや下流システムに提示する前にすべてのモデル出力を検証およびサニタイズする

### 2. 認証と認可の徹底  
- **外部IDプロバイダー**：カスタム認証の実装ではなく、確立されたIDプロバイダー（Microsoft Entra ID、OAuth 2.1プロバイダー）に認証を委任する
- <strong>クライアント登録</strong>：クライアントIDメタデータドキュメントまたは事前登録を推奨し、互換性のためにのみ非推奨の動的クライアント登録を使用する
- <strong>細粒度の権限</strong>：最小権限の原則に従い、ツール固有の詳細な権限を実装する
- <strong>トークンライフサイクル管理</strong>：安全なローテーションと適切なオーディエンス検証を持つ短命のアクセストークンを使用する
- <strong>多要素認証</strong>：すべての管理アクセスおよび機密操作に対してMFAを必須にする

### 3. セキュアな通信プロトコル
- <strong>トランスポート層セキュリティ</strong>：リモートHTTP MCP通信には適切な証明書検証付きHTTPSを使用する
	ローカルのstdioサーバーにはプロセス分離と環境認証情報を使用する

- <strong>エンドツーエンド暗号化</strong>：転送中および保存中の非常に機密性の高いデータに対して追加の暗号化層を実装する
- <strong>証明書管理</strong>：自動更新プロセスを伴う適切な証明書ライフサイクル管理を維持する
- <strong>プロトコルバージョンの適用</strong>：MCP `2026-07-28` を使用し、すべてのリクエストに必須の
	バージョンメタデータを含め、サポートされていないバージョンは拒否する

### 4. 高度なレートリミットとリソース保護
- <strong>多層レートリミット</strong>：ユーザー、認証情報、操作、ツール、リソースごとにレートリミットを実装し、乱用を防止する

- <strong>適応型レートリミット</strong>：使用パターンおよび脅威指標に適応する機械学習ベースのレートリミットを使用する
- <strong>リソースクオータ管理</strong>：計算リソース、メモリ使用量、実行時間に適切な制限を設定する
- **DDoS保護**：包括的なDDoS保護およびトラフィック分析システムを導入する

### 5. 包括的なログ記録と監視
- <strong>構造化された監査ログ</strong>：すべてのMCP操作、ツール実行、安全イベントに対して詳細で検索可能なログを実装する
- <strong>リアルタイムのセキュリティ監視</strong>：AI駆動の異常検出を備えたSIEMシステムをMCPワークロードに展開する
- <strong>プライバシー準拠のログ記録</strong>：データプライバシー要件および規制を尊重しつつセキュリティイベントをログに記録する
- <strong>インシデント対応の統合</strong>：ログ記録システムを自動化されたインシデント対応ワークフローに接続する

### 6. 強化された安全なストレージプラクティス
- <strong>ハードウェアセキュリティモジュール</strong>：重要な暗号操作のためにHSM対応のキー保管（Azure Key Vault、AWS CloudHSM）を使用する
- <strong>暗号鍵管理</strong>：鍵の適切なローテーション、分離、およびアクセス制御を実装する
- <strong>シークレット管理</strong>：すべてのAPIキー、トークン、および認証情報を専用のシークレット管理システムに保管する
- <strong>データ分類</strong>：機密度レベルに基づいてデータを分類し、適切な保護措置を適用する

### 7. 高度なトークン管理
- <strong>トークンパススルー防止</strong>：セキュリティコントロールを回避するトークンパススルーパターンを明示的に禁止する
- <strong>オーディエンス検証</strong>：トークンのオーディエンスクレームが意図したMCPサーバーのIDと一致することを常に検証する
- <strong>クレームベースの認可</strong>：トークンクレームおよびユーザー属性に基づく細粒度の認可を実装する
- <strong>トークンバインディング</strong>：トークンが意図したMCPリソースをターゲットとしていることを検証し、
	アプリケーション状態ハンドルを認証プリンシパルにサーバー側でバインドする

### 8. セキュアなアプリケーション状態

- <strong>暗号化された状態ハンドル</strong>：リクエストを跨ぐ状態のために不透明で非決定的なハンドルを生成する

- <strong>ユーザー固有のバインディング</strong>：各ハンドルを認証されたプリンシパルにサーバー側でバインドし、クライアントから提供されたユーザーIDを信用しない

- <strong>ライフサイクル管理</strong>：ハンドルの有効期限切れおよび取り消しを行い、コール元が古い状態から回復する方法を定義する

- <strong>リクエスト毎の認可</strong>：ハンドルが提示されるたびに認可を再確認する。ハンドルは名前であり、認証情報ではない


### 9. AI特有のセキュリティコントロール
- <strong>プロンプトインジェクション防御</strong>：スポットライト、デリミター、データマーキング技術を備えたMicrosoft Prompt Shieldsを展開する
- <strong>ツール汚染防止</strong>：ツールのメタデータを検証し、動的な変更を監視し、ツールの整合性を検証する
- <strong>モデル出力検証</strong>：モデル出力をスキャンし、潜在的なデータ漏洩、有害なコンテンツ、またはセキュリティポリシー違反を検出する
- <strong>コンテキストウィンドウ保護</strong>：コンテキストウィンドウの汚染や操作攻撃を防止するためのコントロールを実装する

### 10. ツール実行のセキュリティ
- <strong>実行サンドボックス化</strong>：リソース制限付きのコンテナ化された分離環境でツール実行を行う
- <strong>権限分離</strong>：最小限の必要権限でツールを実行し、サービスアカウントを分離する
- <strong>ネットワーク分離</strong>：ツール実行環境にネットワークセグメンテーションを実装する
- <strong>実行監視</strong>：異常な動作、リソース使用状況、セキュリティ違反に対してツール実行を監視する

### 11. 継続的なセキュリティ検証
- <strong>自動化されたセキュリティテスト</strong>：GitHub Advanced Securityなどのツールを用いてCI/CDパイプラインにセキュリティテストを統合する
- <strong>脆弱性管理</strong>：AIモデルや外部サービスを含むすべての依存関係を定期的にスキャンする
- <strong>侵入テスト</strong>：特にMCP実装を対象に定期的なセキュリティ評価を実施する
- <strong>セキュリティコードレビュー</strong>：すべてのMCP関連のコード変更に対して必須のセキュリティレビューを実装する

### 12. AIのサプライチェーンセキュリティ
- <strong>コンポーネント検証</strong>：すべてのAIコンポーネント（モデル、埋め込み、API）の出所、整合性、およびセキュリティを検証する
- <strong>依存関係管理</strong>：すべてのソフトウェアおよびAI依存関係の最新インベントリを維持し、脆弱性追跡を行う
- <strong>信頼されたリポジトリ</strong>：すべてのAIモデル、ライブラリ、およびツールに対して検証済みの信頼できるソースを使用する
- <strong>サプライチェーンの監視</strong>：AIサービスプロバイダーおよびモデルリポジトリの妥協に対して継続的に監視する

## 高度なセキュリティパターン

### MCPのゼロトラストアーキテクチャ
- **決して信用せず、常に検証する**：すべてのMCP参加者に対して継続的な検証を実施する
- <strong>マイクロセグメンテーション</strong>：詳細なネットワークおよびIDコントロールでMCPコンポーネントを分離する
- <strong>条件付きアクセス</strong>：状況や行動に適応するリスクベースのアクセスコントロールを実装する
- <strong>継続的なリスク評価</strong>：現在の脅威指標に基づいてセキュリティ姿勢を動的に評価する

### プライバシー保護AIの実装
- <strong>データ最小化</strong>：各MCP操作に必要最小限のデータのみを公開する
- <strong>差分プライバシー</strong>：機密データ処理にプライバシー保護技術を実装する
- <strong>準同型暗号</strong>：暗号化されたデータ上での安全な計算のために高度な暗号技術を使用する
- <strong>フェデレーテッドラーニング</strong>：データの局所性およびプライバシーを保護する分散学習アプローチを実装する

### AIシステムのインシデント対応
- **AI特有のインシデント手順**：AIおよびMCP固有の脅威に対応したインシデント対応手順を策定する
- <strong>自動化対応</strong>：一般的なAIセキュリティインシデントに対する自動封じ込めと修復を実装する  
- <strong>フォレンジック能力</strong>：AIシステムの妥協やデータ漏洩に対するフォレンジック準備を維持する
- <strong>回復手順</strong>：AIモデル汚染、プロンプトインジェクション攻撃、サービス妥協からの回復手順を確立する

## 実装リソースと標準

### 🏔️ ハンズオンセキュリティトレーニング
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - AzureにおけるMCPサーバーのセキュリティ強化のための包括的ハンズオンワークショップ
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - 参照アーキテクチャおよびOWASP MCPトップ10実装ガイダンス

### 公式MCPドキュメント
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 現行のMCPプロトコル仕様
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 公式セキュリティガイダンス
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP認可パターン
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - トランスポート要件

### Microsoft セキュリティソリューション
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 高度なプロンプトインジェクション保護
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 包括的なAIコンテンツフィルタリング
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - エンタープライズIDおよびアクセス管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全なシークレットおよび認証情報管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - サプライチェーンおよびコードセキュリティスキャン

### セキュリティ標準およびフレームワーク
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 現行OAuthセキュリティガイダンス
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webアプリケーションセキュリティリスク
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI特有のセキュリティリスク
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 包括的なAIリスク管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 情報セキュリティマネジメントシステム

### 実装ガイドおよびチュートリアル
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - エンタープライズ認証パターン
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - IDプロバイダー統合
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - トークン管理ベストプラクティス
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高度な暗号パターン

### 高度なセキュリティリソース
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 安全な開発プラクティス
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI特有のセキュリティテスト
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI脅威モデリング方法論
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - プライバシー保護AI技術

### コンプライアンスおよびガバナンス
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AIシステムにおけるプライバシー準拠
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 責任あるAI実装
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AIサービスプロバイダー向けセキュリティコントロール
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 医療AI準拠要件

### DevSecOpsおよび自動化
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全なAI開発パイプライン
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 継続的なセキュリティ検証
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全なインフラストラクチャ展開
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AIワークロードのコンテナ化セキュリティ

### 監視およびインシデント対応  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 包括的な監視ソリューション
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI特有のインシデント対応手順
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - セキュリティ情報およびイベント管理

- [AI向けの脅威インテリジェンス](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI脅威インテリジェンスソース

## 🔄 継続的改善

### 進化する基準に常に対応する
- **MCP仕様の更新**: 公式MCP仕様変更およびセキュリティアドバイザリを監視する
- <strong>脅威インテリジェンス</strong>: AIセキュリティ脅威フィードや脆弱性データベースに登録する  
- <strong>コミュニティ参加</strong>: MCPセキュリティコミュニティの議論やワーキンググループに参加する
- <strong>定期評価</strong>: 四半期ごとにセキュリティ態勢を評価し、それに応じた実践を更新する

### MCPセキュリティへの貢献
- <strong>セキュリティ研究</strong>: MCPセキュリティ研究や脆弱性開示プログラムに貢献する
- <strong>ベストプラクティスの共有</strong>: セキュリティ実装と学びをコミュニティと共有する
- <strong>標準開発</strong>: MCP仕様開発やセキュリティ標準の作成に参加する
- <strong>ツール開発</strong>: MCPエコシステム向けのセキュリティツールやライブラリを開発し、共有する

---

*本書は2026年9月9日時点のMCPセキュリティベストプラクティスを反映しており、  
MCP仕様 `2026-07-28` に基づいています。プロトコルと脅威の状況に応じて  
セキュリティ実践は定期的に見直す必要があります。*

## 今後の展開

- 読む: [MCPセキュリティベストプラクティス](./mcp-security-best-practices.md)
- 戻る: [セキュリティモジュール概要](./README.md)
- 続ける: [モジュール3：はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
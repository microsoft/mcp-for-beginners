# MCP セキュリティベストプラクティス 2025

この包括的なガイドは、最新の **MCP Specification 2025-11-25** および現在の業界標準に基づいて、Model Context Protocol (MCP) システムの実装に必要なセキュリティベストプラクティスを概説しています。これらのプラクティスは、従来のセキュリティ上の懸念事項と、MCP展開に特有のAI固有の脅威の両方に対応しています。

## 重要なセキュリティ要件

### 必須のセキュリティコントロール（MUST要件）

1. **トークン検証**: MCPサーバーは、明示的にMCPサーバー自身のために発行されていないトークンを**受け入れてはなりません**
2. **認可検証**: 認可を実装するMCPサーバーは、すべての受信リクエストを検証し、認証にセッションを使用してはなりません  
3. **ユーザー同意**: 静的クライアントIDを使用するMCPプロキシサーバーは、動的に登録された各クライアントに対して明示的なユーザー同意を取得する必要があります
4. **安全なセッションID**: MCPサーバーは、暗号学的に安全で非決定論的なセッションIDを安全な乱数生成器で生成して使用しなければなりません

## コアセキュリティプラクティス

### 1. 入力検証とサニタイズ
- **包括的な入力検証**: すべての入力を検証およびサニタイズし、インジェクション攻撃、混乱代理問題、プロンプトインジェクションの脆弱性を防止する
- **パラメータスキーマの強制**: すべてのツールパラメータおよびAPI入力に対して厳格なJSONスキーマ検証を実装する
- **コンテンツフィルタリング**: Microsoft Prompt ShieldsおよびAzure Content Safetyを使用して、プロンプトや応答内の悪意のあるコンテンツをフィルタリングする
- **出力のサニタイズ**: ユーザーや下流システムに提示する前に、すべてのモデル出力を検証およびサニタイズする

### 2. 認証と認可の優秀性  
- **外部IDプロバイダー**: カスタム認証を実装するのではなく、確立されたIDプロバイダー（Microsoft Entra ID、OAuth 2.1プロバイダー）に認証を委任する
- **細粒度の権限**: 最小権限の原則に従い、ツール固有の細かい権限を実装する
- **トークンライフサイクル管理**: 短命なアクセストークンを使用し、安全なローテーションと適切なオーディエンス検証を行う
- **多要素認証**: すべての管理アクセスおよび機密操作にMFAを要求する

### 3. 安全な通信プロトコル
- **トランスポート層セキュリティ**: すべてのMCP通信にHTTPS/TLS 1.3を使用し、適切な証明書検証を行う
- **エンドツーエンド暗号化**: 転送中および保存時の高度に機密性の高いデータに対して追加の暗号化レイヤーを実装する
- **証明書管理**: 自動更新プロセスを備えた適切な証明書ライフサイクル管理を維持する
- **プロトコルバージョンの強制**: 現行のMCPプロトコルバージョン（2025-11-25）を使用し、適切なバージョンネゴシエーションを行う

### 4. 高度なレート制限とリソース保護
- **多層レート制限**: ユーザー、セッション、ツール、リソースレベルでレート制限を実装し、悪用を防止する
- **適応型レート制限**: 使用パターンや脅威指標に適応する機械学習ベースのレート制限を使用する
- **リソースクォータ管理**: 計算リソース、メモリ使用量、実行時間に適切な制限を設定する
- **DDoS保護**: 包括的なDDoS保護およびトラフィック分析システムを展開する

### 5. 包括的なログ記録と監視
- **構造化された監査ログ**: すべてのMCP操作、ツール実行、セキュリティイベントに対して詳細で検索可能なログを実装する
- **リアルタイムセキュリティ監視**: AI搭載の異常検知を備えたSIEMシステムをMCPワークロードに展開する
- **プライバシー準拠のログ記録**: データプライバシー要件および規制を尊重しつつセキュリティイベントをログに記録する
- **インシデント対応統合**: ロギングシステムを自動化されたインシデント対応ワークフローに接続する

### 6. 強化された安全なストレージプラクティス
- **ハードウェアセキュリティモジュール**: 重要な暗号操作にAzure Key Vault、AWS CloudHSMなどのHSM対応キー保管を使用する
- **暗号鍵管理**: 適切な鍵ローテーション、分離、アクセス制御を暗号鍵に対して実装する
- **シークレット管理**: すべてのAPIキー、トークン、資格情報を専用のシークレット管理システムに保存する
- **データ分類**: 敏感度レベルに基づいてデータを分類し、適切な保護措置を適用する

### 7. 高度なトークン管理
- **トークンパススルー防止**: セキュリティコントロールを回避するトークンパススルーパターンを明示的に禁止する
- **オーディエンス検証**: トークンのオーディエンスクレームが意図されたMCPサーバーのIDと一致することを常に検証する
- **クレームベース認可**: トークンクレームおよびユーザー属性に基づく細粒度の認可を実装する
- **トークンバインディング**: 適切な場合、トークンを特定のセッション、ユーザー、デバイスにバインドする

### 8. 安全なセッション管理
- **暗号学的セッションID**: 予測不可能なシーケンスではなく、暗号学的に安全な乱数生成器を使用してセッションIDを生成する
- **ユーザー固有のバインディング**: `<user_id>:<session_id>` のような安全な形式でセッションIDをユーザー固有情報にバインドする
- **セッションライフサイクル制御**: 適切なセッションの有効期限、ローテーション、無効化メカニズムを実装する
- **セッションセキュリティヘッダー**: セッション保護のために適切なHTTPセキュリティヘッダーを使用する

### 9. AI固有のセキュリティコントロール
- **プロンプトインジェクション防御**: Microsoft Prompt Shieldsをスポットライト、デリミター、データマーキング技術と共に展開する
- **ツールポイズニング防止**: ツールメタデータを検証し、動的変更を監視し、ツールの整合性を検証する
- **モデル出力検証**: モデル出力をスキャンし、潜在的なデータ漏洩、有害コンテンツ、セキュリティポリシー違反を検出する
- **コンテキストウィンドウ保護**: コンテキストウィンドウのポイズニングおよび操作攻撃を防止するコントロールを実装する

### 10. ツール実行のセキュリティ
- **実行サンドボックス**: ツール実行をコンテナ化された分離環境でリソース制限付きで実行する
- **権限分離**: 最小限の必要権限でツールを実行し、サービスアカウントを分離する
- **ネットワーク分離**: ツール実行環境にネットワークセグメンテーションを実装する
- **実行監視**: ツール実行の異常動作、リソース使用、セキュリティ違反を監視する

### 11. 継続的なセキュリティ検証
- **自動化されたセキュリティテスト**: GitHub Advanced Securityなどのツールを用いてCI/CDパイプラインにセキュリティテストを統合する
- **脆弱性管理**: AIモデルや外部サービスを含むすべての依存関係を定期的にスキャンする
- **ペネトレーションテスト**: MCP実装を対象とした定期的なセキュリティ評価を実施する
- **セキュリティコードレビュー**: すべてのMCP関連コード変更に対して必須のセキュリティレビューを実施する

### 12. AIのサプライチェーンセキュリティ
- **コンポーネント検証**: すべてのAIコンポーネント（モデル、埋め込み、API）の出所、整合性、セキュリティを検証する
- **依存関係管理**: 脆弱性追跡を含むすべてのソフトウェアおよびAI依存関係の最新インベントリを維持する
- **信頼できるリポジトリ**: すべてのAIモデル、ライブラリ、ツールに対して検証済みの信頼できるソースを使用する
- **サプライチェーン監視**: AIサービスプロバイダーおよびモデルリポジトリの妥協を継続的に監視する

## 高度なセキュリティパターン

### MCPのゼロトラストアーキテクチャ
- **決して信頼せず、常に検証する**: すべてのMCP参加者に対して継続的な検証を実装する
- **マイクロセグメンテーション**: 細粒度のネットワークおよびIDコントロールでMCPコンポーネントを分離する
- **条件付きアクセス**: コンテキストや行動に適応するリスクベースのアクセスコントロールを実装する
- **継続的リスク評価**: 現在の脅威指標に基づいてセキュリティ姿勢を動的に評価する

### プライバシー保護AIの実装
- **データ最小化**: 各MCP操作に必要な最小限のデータのみを公開する
- **差分プライバシー**: 機密データ処理のためのプライバシー保護技術を実装する
- **準同型暗号**: 暗号化データ上の安全な計算のための高度な暗号技術を使用する
- **フェデレーテッドラーニング**: データの局所性とプライバシーを保護する分散学習アプローチを実装する

### AIシステムのインシデント対応
- **AI固有のインシデント手順**: AIおよびMCP固有の脅威に対応したインシデント対応手順を策定する
- **自動化対応**: 一般的なAIセキュリティインシデントに対する自動封じ込めおよび修復を実装する  
- **フォレンジック能力**: AIシステムの侵害およびデータ漏洩に備えたフォレンジック準備を維持する
- **復旧手順**: AIモデルのポイズニング、プロンプトインジェクション攻撃、サービス侵害からの復旧手順を確立する

## 実装リソースと標準

### 公式MCPドキュメント
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - 現行のMCPプロトコル仕様
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - 公式セキュリティガイダンス
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - 認証および認可パターン
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - トランスポート層セキュリティ要件

### Microsoftセキュリティソリューション
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 高度なプロンプトインジェクション防御
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 包括的なAIコンテンツフィルタリング
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - エンタープライズIDおよびアクセス管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全なシークレットおよび資格情報管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - サプライチェーンおよびコードセキュリティスキャン

### セキュリティ標準とフレームワーク
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 現行のOAuthセキュリティガイダンス
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Webアプリケーションのセキュリティリスク
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI固有のセキュリティリスク
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 包括的なAIリスク管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 情報セキュリティマネジメントシステム

### 実装ガイドとチュートリアル
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - エンタープライズ認証パターン
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - IDプロバイダー統合
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - トークン管理ベストプラクティス
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高度な暗号化パターン

### 高度なセキュリティリソース
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 安全な開発プラクティス
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI固有のセキュリティテスト
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI脅威モデリング手法
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - プライバシー保護AI技術

### コンプライアンスとガバナンス
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AIシステムにおけるプライバシー準拠
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 責任あるAI実装
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AIサービスプロバイダー向けセキュリティコントロール
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 医療AIのコンプライアンス要件

### DevSecOpsと自動化
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全なAI開発パイプライン
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 継続的なセキュリティ検証
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全なインフラ展開
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AIワークロードのコンテナ化セキュリティ

### 監視とインシデント対応  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 包括的な監視ソリューション
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI固有のインシデント手順
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - セキュリティ情報およびイベント管理
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI脅威インテリジェンスソース

## 🔄 継続的改善

### 進化する標準に追従する
- **MCP仕様の更新**: 公式MCP仕様の変更およびセキュリティ勧告を監視する
- **脅威インテリジェンス**: AIセキュリティ脅威フィードおよび脆弱性データベースを購読する  
- **コミュニティ参加**: MCPセキュリティコミュニティの議論および作業グループに参加する
- **定期評価**: 四半期ごとにセキュリティ姿勢評価を実施し、プラクティスを更新する

### MCPセキュリティへの貢献
- **セキュリティ研究**: MCPセキュリティ研究および脆弱性開示プログラムに貢献する
- **ベストプラクティス共有**: セキュリティ実装および学びをコミュニティと共有する
- **標準開発**: MCP仕様の開発およびセキュリティ標準の作成に参加する  
- **ツール開発**: MCPエコシステム向けのセキュリティツールおよびライブラリを開発し共有する  

---

*この文書は、2025年12月18日時点のMCP仕様2025-11-25に基づくMCPセキュリティのベストプラクティスを反映しています。セキュリティの実践は、プロトコルおよび脅威の状況の変化に応じて定期的に見直し、更新する必要があります。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
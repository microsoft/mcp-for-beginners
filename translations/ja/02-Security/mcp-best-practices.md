# MCP セキュリティベストプラクティス 2025

この包括的なガイドは、最新の **MCP Specification 2025-11-25** と現在の業界標準に基づいて、モデルコンテキストプロトコル（MCP）システムを実装するための重要なセキュリティベストプラクティスを概説しています。これらのプラクティスは、従来のセキュリティ上の懸念事項と、MCP 展開に特有の AI 関連の脅威の両方に対応しています。

## 重要なセキュリティ要件

### 必須のセキュリティコントロール（MUST 要件）

1. **トークン検証**: MCP サーバーは、MCP サーバー自身のために明示的に発行されたトークン以外は一切受け付けてはなりません
2. **認可の検証**: 認可を実装する MCP サーバーは、すべての受信リクエストを検証し、認証にセッションを使用してはなりません  
3. **ユーザー同意**: 静的クライアント ID を使用する MCP プロキシサーバーは、動的に登録された各クライアントに対して明示的なユーザー同意を得る必要があります
4. **安全なセッションID**: MCP サーバーは、暗号的に安全で非決定論的なセッションIDを、安全な乱数生成器を用いて生成しなければなりません

## コアセキュリティプラクティス

### 1. 入力検証とサニタイズ
- **包括的な入力検証**: すべての入力を検証およびサニタイズし、インジェクション攻撃、混乱したデピュティ問題、およびプロンプトインジェクションの脆弱性を防止
- **パラメータスキーマの強制**: すべてのツールパラメータおよび API 入力に対して厳格な JSON スキーマ検証を実装
- **コンテンツフィルタリング**: Microsoft Prompt Shields および Azure Content Safety を使用し、プロンプトおよびレスポンス内の悪意あるコンテンツをフィルタリング
- **出力のサニタイズ**: モデルのすべての出力を、ユーザーまたは下流システムに提示する前に検証およびサニタイズ

### 2. 認証と認可の徹底
- **外部アイデンティティプロバイダー**: 独自認証の実装ではなく、確立されたアイデンティティプロバイダー（Microsoft Entra ID、OAuth 2.1 プロバイダー）に認証を委任
- **細粒度の権限設定**: 最小特権の原則に従った、ツールごとの細かい権限管理を実装
- **トークンライフサイクル管理**: 短命なアクセストークンを使用し、安全なローテーションと適切なオーディエンス検証を行う
- **多要素認証**: すべての管理者アクセスおよび重要な操作に対して MFA を必須化

### 3. 安全な通信プロトコル
- **トランスポート層セキュリティ**: すべての MCP 通信に HTTPS/TLS 1.3 を使用し、適切な証明書検証を実施
- **エンドツーエンド暗号化**: 送信中および保存時の高度に機密性の高いデータに対して追加の暗号化レイヤーを実装
- **証明書管理**: 自動更新プロセスを備えた適切な証明書ライフサイクル管理を維持
- **プロトコルバージョンの強制**: 現行 MCP プロトコルバージョン（2025-11-25）を使用し、適切なバージョン交渉を行う

### 4. 高度なレートリミティングとリソース保護
- **多層レートリミティング**: ユーザー、セッション、ツール、リソースレベルでレートリミティングを実装し、悪用を防止
- **適応型レートリミティング**: 利用パターンや脅威指標に適応する機械学習ベースのレートリミティングを使用
- **リソースクォータ管理**: 計算リソース、メモリ使用量、実行時間の適切な制限を設定
- **DDoS 対策**: 包括的な DDoS 保護およびトラフィック解析システムを展開

### 5. 包括的なログ記録と監視
- **構造化監査ログ**: すべての MCP 操作、ツール実行、およびセキュリティイベントに対して詳細かつ検索可能なログを実装
- **リアルタイムセキュリティ監視**: MCP ワークロード向けに AI 搭載の異常検知を備えた SIEM システムを展開
- **プライバシー準拠のログ記録**: データプライバシー要件・規制を遵守しつつセキュリティイベントを記録
- **インシデントレスポンスとの連携**: ロギングシステムを自動インシデントレスポンスワークフローに接続

### 6. 強化された安全なストレージプラクティス
- **ハードウェアセキュリティモジュール**: 重要な暗号オペレーションには HSM 対応のキー保管（Azure Key Vault、AWS CloudHSM）を使用
- **暗号鍵管理**: 適切な鍵ローテーション、分離およびアクセス制御を暗号鍵に適用
- **シークレット管理**: すべての API キー、トークン、および認証情報は専用のシークレット管理システムに保管
- **データ分類**: 機密性レベルに基づきデータを分類し、適切な保護措置を適用

### 7. 高度なトークン管理
- **トークンパススルー防止**: セキュリティコントロールを回避するトークンパススルーパターンを明示的に禁止
- **オーディエンス検証**: トークンのオーディエンスクレームが対象の MCP サーバーIDと一致することを常に検証
- **クレームベース認可**: トークンのクレームおよびユーザー属性に基づく細粒度認可を実装
- **トークンバインディング**: 適切な場合にはトークンを特定のセッション、ユーザー、またはデバイスにバインド

### 8. 安全なセッション管理
- **暗号化されたセッションID**: 予測不可能な暗号的安全な乱数生成器を用いてセッションIDを生成
- **ユーザー固有のバインディング**: `<user_id>:<session_id>` のような安全なフォーマットでセッションIDをユーザー固有情報に紐づけ
- **セッションライフサイクル制御**: 適切なセッション期限切れ、ローテーション、無効化メカニズムを実装
- **セッションセキュリティヘッダー**: セッション保護のために適切な HTTP セキュリティヘッダーを使用

### 9. AI 専用のセキュリティコントロール
- **プロンプトインジェクション防御**: Microsoft Prompt Shields をスポットライト、デリミター、データマーキング技術とともに展開
- **ツールポイズニング防止**: ツールメタデータの検証、動的変化の監視、ツールの整合性検証を実施
- **モデル出力検証**: モデルの出力をスキャンし、データリーク、有害コンテンツ、またはセキュリティポリシー違反の可能性を確認
- **コンテキストウィンドウ保護**: コンテキストウィンドウのポイズニングや改ざん攻撃を防止するコントロールを実装

### 10. ツール実行のセキュリティ
- **実行サンドボックス化**: ツール実行をリソース制限付きのコンテナ化された隔離環境で実行
- **権限分離**: 最小限の権限でツールを実行し、サービスアカウントを分離
- **ネットワーク分離**: ツール実行環境のネットワークセグメンテーションを実施
- **実行監視**: ツール実行の異常行動、リソース利用、およびセキュリティ違反を監視

### 11. 継続的なセキュリティ検証
- **自動化されたセキュリティテスト**: GitHub Advanced Security などのツールを用いて CI/CD パイプラインにセキュリティテストを統合
- **脆弱性管理**: AI モデルや外部サービスを含むすべての依存関係を定期的にスキャン
- **ペネトレーションテスト**: MCP 実装を対象とした定期的なセキュリティ評価を実施
- **セキュリティコードレビュー**: MCP 関連のコード変更に対して必須のセキュリティレビューを実施

### 12. AI に対するサプライチェーンセキュリティ
- **コンポーネント検証**: すべての AI コンポーネント（モデル、埋め込み、API）の由来、整合性、およびセキュリティを検証
- **依存関係管理**: 脆弱性追跡を含むすべてのソフトウェアおよび AI 依存関係の最新インベントリを維持
- **信頼できるリポジトリ**: すべての AI モデル、ライブラリ、およびツールに検証済みの信頼されたソースを使用
- **サプライチェーン監視**: AI サービスプロバイダーおよびモデルリポジトリにおける侵害を継続的に監視

## 高度なセキュリティパターン

### MCP のゼロトラストアーキテクチャ
- **決して信用せず、常に検証する**: すべての MCP 参加者に対し継続的な検証を実装
- **マイクロセグメンテーション**: 詳細なネットワークおよびアイデンティティコントロールで MCP コンポーネントを分離
- **条件付きアクセス**: コンテキストおよび行動に応じて適応するリスクベースアクセスコントロールを実装
- **継続的リスク評価**: 現在の脅威指標に基づきセキュリティ姿勢を動的に評価

### プライバシー保護 AI 実装
- **データ最小化**: 各 MCP 操作に必要最低限のデータのみを公開
- **差分プライバシー**: 機密データ処理にプライバシー保護技術を実装
- **ホモモルフィック暗号**: 暗号化データ上での安全な計算のための高度な暗号技術を使用
- **フェデレーテッドラーニング**: データの局所性とプライバシーを保護する分散学習アプローチを実装

### AI システムのインシデント対応
- **AI 専用インシデント手順**: AI および MCP 固有の脅威に対応したインシデントレスポンス手順を策定
- **自動化対応**: 一般的な AI セキュリティインシデントに対する自動封じ込めおよび修復を実装  
- **フォレンジック能力**: AI システムの侵害やデータ漏えいに備えたフォレンジック準備態勢を維持
- **回復手順**: AI モデルのポイズニング、プロンプトインジェクション攻撃、サービス侵害からの回復手順を確立

## 実装リソースと標準

### 🏔️ ハンズオントレーニング
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Azure 上での MCP サーバーのセキュリティに関する包括的なハンズオンワークショップ
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - 参照アーキテクチャおよび OWASP MCP Top 10 実装ガイダンス

### 公式 MCP ドキュメント
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - 現行 MCP プロトコル仕様
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - 公式セキュリティガイダンス
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - 認証および認可パターン
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - トランスポート層セキュリティ要件

### Microsoft セキュリティソリューション
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 高度なプロンプトインジェクション防御
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 総合的な AI コンテンツフィルタリング
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - エンタープライズアイデンティティおよびアクセス管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全なシークレットおよび認証情報管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - サプライチェーンおよびコードセキュリティスキャン

### セキュリティ標準とフレームワーク
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 現行の OAuth セキュリティガイダンス
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web アプリケーションセキュリティリスク
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 特有のセキュリティリスク
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 包括的な AI リスク管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 情報セキュリティマネジメントシステム

### 実装ガイドおよびチュートリアル
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - エンタープライズ認証パターン
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - アイデンティティプロバイダー統合
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - トークン管理ベストプラクティス
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高度な暗号化パターン

### 高度なセキュリティリソース
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - セキュア開発プラクティス
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI 特有のセキュリティテスト
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 脅威モデリング手法
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - プライバシー保護 AI 技術

### コンプライアンスとガバナンス
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI システムにおけるプライバシーコンプライアンス
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 責任ある AI 実装
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI サービスプロバイダー向けセキュリティコントロール
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 医療 AI コンプライアンス要件

### DevSecOps と自動化
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - セキュアな AI 開発パイプライン
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 継続的なセキュリティ検証
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全なインフラ展開
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI ワークロードのコンテナ化セキュリティ

### 監視とインシデントレスポンス  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 包括的な監視ソリューション
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 専用のインシデント対応手順
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - セキュリティ情報イベント管理
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 脅威インテリジェンスソース

## 🔄 継続的改善

### 進化する標準に合わせて常に最新を維持
- **MCP 仕様の更新**: 公式 MCP 仕様の変更およびセキュリティ勧告を監視
- **脅威インテリジェンス**: AI セキュリティの脅威フィードや脆弱性データベースを購読  

- **コミュニティの関与**: MCPセキュリティコミュニティのディスカッションやワーキンググループに参加する
- **定期的な評価**: 四半期ごとにセキュリティ体制評価を実施し、それに応じて実践を更新する

### MCPセキュリティへの貢献
- **セキュリティ調査**: MCPのセキュリティ調査や脆弱性開示プログラムに貢献する
- **ベストプラクティスの共有**: コミュニティとセキュリティ実装や学んだ教訓を共有する
- **標準の開発**: MCP仕様開発およびセキュリティ標準作成に参加する
- **ツール開発**: MCPエコシステム向けのセキュリティツールやライブラリを開発・共有する

---

*このドキュメントは、MCP仕様2025-11-25に基づく2025年12月18日現在のMCPセキュリティベストプラクティスを反映しています。セキュリティの実践は、プロトコルや脅威の状況の変化に合わせて定期的に見直しおよび更新する必要があります。*

## 次に読むべき内容

- 読む: [MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)
- 戻る: [Security Module Overview](./README.md)
- 続ける: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報については、原文の言語で記載されたオリジナルの文書を信頼してください。重要な情報に関しては、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

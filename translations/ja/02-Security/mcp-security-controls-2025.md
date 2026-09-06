# MCPセキュリティコントロール - 2026年2月更新

> <strong>現行標準</strong>: 本書は[MCP仕様 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)のセキュリティ要件および公式の[MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)を反映しています。

Model Context Protocol (MCP) は、従来のソフトウェアセキュリティとAI固有の脅威の両方に対応した強化されたセキュリティコントロールにより大きく成熟しました。本書はOWASP MCP Top 10フレームワークに準拠した安全なMCP実装のための包括的なセキュリティコントロールを提供します。

## 🏔️ 実践的セキュリティトレーニング

実践的なセキュリティ実装経験を得るために、<strong>[MCPセキュリティサミットワークショップ (Sherpa)](https://azure-samples.github.io/sherpa/)</strong>を推奨します。これは「脆弱 → 脆弱性の悪用 → 修正 → 検証」という手法でAzure上のMCPサーバーを保護する包括的なガイド付き遠征です。

本書のすべてのセキュリティコントロールは、OWASP MCP Top 10リスクに対する参照アーキテクチャとAzure固有の実装ガイダンスを提供する<strong>[OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/)</strong>と整合しています。

## <strong>必須セキュリティ要件</strong>

### **MCP仕様からの重要な禁止事項:**

> <strong>禁じられている</strong>: MCPサーバーは明示的にMCPサーバー用に発行されていないトークンを受け入れてはならない  
>
> <strong>禁止</strong>: MCPサーバーは認証にセッションを使用してはならない  
>
> <strong>必須</strong>: 認可を実装するMCPサーバーは全ての受信リクエストを検証しなければならない  
>
> <strong>必須</strong>: 静的クライアントIDを使うMCPプロキシサーバーは、動的に登録されたクライアントごとにユーザーの同意を得なければならない  

---

## 1. <strong>認証および認可コントロール</strong>

### <strong>外部アイデンティティプロバイダー統合</strong>

**現行MCP標準 (2025-11-25)** は、MCPサーバーが認証を外部アイデンティティプロバイダーに委任することを許可し、これは大幅なセキュリティ改善を示しています：

**対応するOWASP MCPリスク**: [MCP07 - 不十分な認証と認可](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**セキュリティ上のメリット:**
1. <strong>カスタム認証リスクの排除</strong>: カスタム認証実装による脆弱性を削減
2. <strong>エンタープライズグレードのセキュリティ</strong>: Microsoft Entra IDのような高度なセキュリティ機能を持つプロバイダーの活用
3. <strong>集中管理のアイデンティティ</strong>: ユーザーのライフサイクル管理、アクセス制御、コンプライアンス監査の簡素化
4. <strong>多要素認証</strong>: エンタープライズアイデンティティプロバイダーからMFA機能を継承
5. **条件付きアクセス ポリシー**: リスクベースのアクセス制御や適応型認証の利用

**実装要件:**
- <strong>トークンのオーディエンス検証</strong>: すべてのトークンが明示的にMCPサーバー向けに発行されていることを検証
- <strong>発行者検証</strong>: トークン発行者が期待するアイデンティティプロバイダーと一致するかを確認
- <strong>署名検証</strong>: トークン整合性の暗号学的検証
- <strong>有効期限の遵守</strong>: トークンの有効期間制限を厳密に遵守
- <strong>スコープ検証</strong>: トークンに要求された操作に適切な権限が含まれていることを保証

### <strong>認可ロジックのセキュリティ</strong>

**重要コントロール:**
- <strong>包括的な認可監査</strong>: すべての認可判断ポイントの定期的なセキュリティレビュー
- <strong>フェールセーフデフォルト</strong>: 認可ロジックで明確な判断がつかない場合はアクセスを拒否
- <strong>権限境界の明確化</strong>: 異なる特権レベルやリソースアクセスの明確な分離
- <strong>監査ログ記録</strong>: 認可判断のすべてを完全にログ記録し、セキュリティ監視に利用
- <strong>定期的なアクセスレビュー</strong>: ユーザー権限や特権割り当ての周期的検証

## 2. <strong>トークンセキュリティとパススルー防止コントロール</strong>

**対応するOWASP MCPリスク**: [MCP01 - トークンの誤管理と秘密情報の露出](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### <strong>トークンパススルー防止</strong>

MCP認可仕様では、重大なセキュリティリスクのために<strong>トークンのパススルーは明確に禁止</strong>されています：

**対処されるセキュリティリスク:**
- <strong>制御回避</strong>: レート制限、リクエスト検証、トラフィック監視といった重要なセキュリティコントロールを回避
- <strong>監査責任の欠如</strong>: クライアント特定が困難となり、監査や事故調査が破綻
- <strong>プロキシ経由の情報持ち出し</strong>: 攻撃者がサーバーを不正データアクセスのプロキシとして利用可能
- <strong>信頼境界の違反</strong>: 下流サービスのトークン出所に関する信頼が破綻
- <strong>横移動攻撃</strong>: 複数サービス間でトークンが悪用され、攻撃範囲が拡大

**実装コントロール:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### <strong>安全なトークン管理パターン</strong>

**ベストプラクティス:**
- <strong>短期有効トークン</strong>: トークンの露出期間を最小化し頻繁にローテーション
- <strong>ジャストインタイム発行</strong>: 特定操作に必要な時のみトークンを発行
- <strong>安全な保管</strong>: ハードウェアセキュリティモジュール(HSM)や安全なキーコンテナの利用
- <strong>トークンバインディング</strong>: 可能な限りトークンを特定クライアント、セッション、操作に紐付け
- <strong>監視およびアラート</strong>: トークンの誤用や不正アクセスパターンをリアルタイムで検知

## 3. <strong>セッションセキュリティコントロール</strong>

### <strong>セッションハイジャック防止</strong>

**対処される攻撃ベクトル:**
- <strong>セッションハイジャックのプロンプトインジェクション</strong>: 共有セッション状態への悪意あるイベント注入
- <strong>セッションなりすまし</strong>: 不正に取得したセッションIDで認証回避
- <strong>再開可能なストリーム攻撃</strong>: サーバー送信イベントの再開機能を悪用し悪意ある内容を注入

**必須のセッションコントロール:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**通信の安全性:**
- **HTTPS強制**: すべてのセッション通信はTLS 1.3経由で行う
- **安全なCookie属性**: HttpOnly、Secure、SameSite=Strict設定
- <strong>証明書ピンニング</strong>: MITM攻撃防止のため重要接続に対して実施

### <strong>ステートフルとステートレスの考慮</strong>

**ステートフル実装の場合:**
- 共有セッション状態は注入攻撃に対しさらなる保護が必要
- キュー方式のセッション管理は整合性検証が必須
- 複数サーバー間で安全なセッション状態同期を要する

**ステートレス実装の場合:**
- JWTなどのトークンベースセッション管理
- セッション状態の暗号的整合性検証
- 攻撃面は狭くなるが堅牢なトークン検証が必須

## 4. **AI固有のセキュリティコントロール**

**対応するOWASP MCPリスク**:
- [MCP06 - 意図フローのサブバーション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - ツールポイズニング](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - コマンドインジェクションおよび実行](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### <strong>プロンプトインジェクション防御</strong>

**Microsoft Prompt Shields統合:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**実装コントロール:**
- <strong>入力のサニタイズ</strong>: すべてのユーザー入力に対する包括的な検証とフィルタリング
- <strong>コンテンツ境界の定義</strong>: システム指示とユーザーコンテンツの明確な分離
- <strong>指示の階層化</strong>: 矛盾する指示の優先順位ルールの適用
- <strong>出力の監視</strong>: 潜在的に有害または改ざんされた出力の検出

### <strong>ツールポイズニング防止</strong>

**ツールセキュリティフレームワーク:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**動的ツール管理:**
- <strong>承認ワークフロー</strong>: ツールの変更に対する明示的なユーザー同意
- <strong>ロールバック機能</strong>: 前のツールバージョンへの復帰可能性
- <strong>変更監査</strong>: ツール定義変更の完全な履歴管理
- <strong>リスク評価</strong>: ツールのセキュリティ状況の自動評価

## 5. <strong>混乱代理人攻撃防止</strong>

### **OAuthプロキシセキュリティ**

**攻撃防止コントロール:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**実装要件:**
- <strong>ユーザー同意の検証</strong>: 動的クライアント登録の同意画面を省略しない
- **リダイレクトURI検証**: リダイレクト先の厳格なホワイトリスト検証
- <strong>認可コード保護</strong>: 短命で単一使用の認可コード
- **クライアントID検証**: クライアント資格情報とメタデータの強固な検証

## 6. <strong>ツール実行セキュリティ</strong>

### <strong>サンドボックス化と分離</strong>

**コンテナベースの分離:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**プロセスの分離:**
- <strong>独立したプロセスコンテキスト</strong>: 各ツール実行を分離されたプロセス空間で実施
- <strong>プロセス間通信</strong>: 検証付き安全なIPCメカニズム
- <strong>プロセス監視</strong>: 実行時の振る舞い分析と異常検知
- <strong>リソース制限</strong>: CPU、メモリ、I/O操作に対する厳密な上限設定

### <strong>最小権限の実装</strong>

**権限管理:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. <strong>サプライチェーンセキュリティコントロール</strong>

**対応するOWASP MCPリスク**: [MCP04 - ソフトウェアサプライチェーン攻撃と依存関係の改ざん](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### <strong>依存関係の検証</strong>

**包括的なコンポーネントセキュリティ:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### <strong>継続的監視</strong>

**サプライチェーンの脅威検出:**
- <strong>依存関係の健全性監視</strong>: すべての依存関係のセキュリティ問題を継続的に評価
- <strong>脅威インテリジェンス統合</strong>: 新興サプライチェーン脅威に関するリアルタイム更新
- <strong>振る舞い分析</strong>: 外部コンポーネントの異常行動検出
- <strong>自動対応</strong>: 侵害されたコンポーネントの即時隔離

## 8. <strong>監視と検出コントロール</strong>

**対応するOWASP MCPリスク**: [MCP08 - 監査およびテレメトリ不足](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **セキュリティ情報およびイベント管理 (SIEM)**

**包括的なログ戦略:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### <strong>リアルタイム脅威検出</strong>

**行動分析:**
- **ユーザー行動分析 (UBA)**: 異常なユーザーアクセスパターンの検出
- **エンティティ行動分析 (EBA)**: MCPサーバーやツールの動作監視
- <strong>機械学習による異常検知</strong>: AIを用いたセキュリティ脅威の特定
- <strong>脅威インテリジェンス相関</strong>: 既知の攻撃パターンとの照合

## 9. <strong>インシデント対応と復旧</strong>

### <strong>自動応答機能</strong>

**即時応答アクション:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### <strong>フォレンジック能力</strong>

**調査支援:**
- <strong>監査証跡の保全</strong>: 暗号的整合性を備えた改変不可能なログ
- <strong>証拠収集</strong>: 関連するセキュリティ証拠の自動収集
- <strong>タイムライン再構築</strong>: セキュリティインシデントに至るイベントの詳細な時系列構築
- <strong>影響評価</strong>: 侵害範囲とデータ漏洩の評価

## <strong>重要なセキュリティアーキテクチャ原則</strong>

### **多層防御 (Defense in Depth)**
- <strong>多数のセキュリティ層</strong>: セキュリティアーキテクチャに単一障害点がないこと
- <strong>冗長なコントロール</strong>: 重要機能に重複するセキュリティ対策を配置
- <strong>フェールセーフ機構</strong>: エラーや攻撃時に安全なデフォルト状態を保証

### <strong>ゼロトラストの実装</strong>
- **決して信用せず、常に検証**: すべてのエンティティとリクエストの継続的検証
- <strong>最小権限の原則</strong>: すべてのコンポーネントに対して必要最小限のアクセス権のみ付与
- <strong>マイクロセグメンテーション</strong>: 細分化されたネットワークとアクセス制御

### <strong>継続的なセキュリティ進化</strong>
- <strong>脅威環境の適応</strong>: 新たな脅威に対応するための定期的な更新
- <strong>コントロール効果の評価</strong>: コントロールの継続的な評価と改善
- <strong>仕様準拠</strong>: 進化するMCPセキュリティ基準との整合

---

## <strong>実装リソース</strong>

### **公式MCPドキュメント**
- [MCP仕様 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP認可仕様](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **OWASP MCPセキュリティリソース**
- [OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/) - Azure実装を含むOWASP MCP Top 10の包括的ガイド
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - 公式OWASP MCPセキュリティリスク
- [MCPセキュリティサミットワークショップ (Sherpa)](https://azure-samples.github.io/sherpa/) - Azure上のMCP向け実践的セキュリティトレーニング

### **Microsoftセキュリティソリューション**
- [Microsoft プロンプト シールド](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### <strong>セキュリティ標準</strong>
- [OAuth 2.0 セキュリティベストプラクティス (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP 大型言語モデル向けTop 10](https://genai.owasp.org/)
- [NISTサイバーセキュリティフレームワーク](https://www.nist.gov/cyberframework)

---

> <strong>重要</strong>: これらのセキュリティコントロールは最新のMCP仕様 (2025-11-25) を反映しています。基準は急速に進化しているため、常に最新の[公式ドキュメント](https://spec.modelcontextprotocol.io/)で確認してください。

## 次に進む

- 戻る: [セキュリティモジュール概要](./README.md)
- 続ける: [モジュール3: はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

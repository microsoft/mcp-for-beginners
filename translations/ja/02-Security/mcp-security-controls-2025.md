# MCP セキュリティコントロール - 2025年12月アップデート

> **現在の標準**: 本ドキュメントは [MCP仕様 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) のセキュリティ要件および公式の [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) を反映しています。

Model Context Protocol (MCP) は、従来のソフトウェアセキュリティとAI特有の脅威の両方に対応した強化されたセキュリティコントロールにより大きく成熟しました。本ドキュメントは2025年12月時点での安全なMCP実装のための包括的なセキュリティコントロールを提供します。

## **必須のセキュリティ要件**

### **MCP仕様からの重要な禁止事項:**

> **禁止**: MCPサーバーはMCPサーバー向けに明示的に発行されていないトークンを受け入れてはなりません  
>
> **禁止**: MCPサーバーは認証にセッションを使用してはなりません  
>
> **必須**: 認可を実装するMCPサーバーはすべての受信リクエストを検証しなければなりません  
>
> **必須**: 静的クライアントIDを使用するMCPプロキシサーバーは、動的に登録されたクライアントごとにユーザーの同意を取得しなければなりません

---

## 1. **認証および認可コントロール**

### **外部アイデンティティプロバイダー統合**

**現在のMCP標準 (2025-06-18)** では、MCPサーバーが認証を外部アイデンティティプロバイダーに委任することを許可しており、これは大きなセキュリティ向上を意味します。

### **外部アイデンティティプロバイダー統合**

**現在のMCP標準 (2025-11-25)** では、MCPサーバーが認証を外部アイデンティティプロバイダーに委任することを許可しており、これは大きなセキュリティ向上を意味します。

**セキュリティ上の利点:**
1. **カスタム認証リスクの排除**: カスタム認証実装を避けることで脆弱性の表面を減少
2. **エンタープライズグレードのセキュリティ**: Microsoft Entra IDなどの確立されたアイデンティティプロバイダーの高度なセキュリティ機能を活用
3. **集中管理されたアイデンティティ管理**: ユーザーライフサイクル管理、アクセス制御、コンプライアンス監査の簡素化
4. **多要素認証**: エンタープライズアイデンティティプロバイダーからMFA機能を継承
5. **条件付きアクセス ポリシー**: リスクベースのアクセス制御および適応認証の恩恵

**実装要件:**
- **トークンのオーディエンス検証**: すべてのトークンがMCPサーバー向けに明示的に発行されていることを検証
- **発行者検証**: トークンの発行者が期待されるアイデンティティプロバイダーと一致することを確認
- **署名検証**: トークンの整合性を暗号的に検証
- **有効期限の厳格な適用**: トークンの有効期間制限を厳密に適用
- **スコープ検証**: トークンが要求された操作に適切な権限を含んでいることを確認

### **認可ロジックのセキュリティ**

**重要なコントロール:**
- **包括的な認可監査**: すべての認可決定ポイントの定期的なセキュリティレビュー
- **フェイルセーフのデフォルト**: 認可ロジックが明確な決定を下せない場合はアクセスを拒否
- **権限境界**: 異なる特権レベルおよびリソースアクセスの明確な分離
- **監査ログ**: すべての認可決定の完全なログ記録によるセキュリティ監視
- **定期的なアクセスレビュー**: ユーザー権限および特権割り当ての定期的な検証

## 2. **トークンセキュリティおよびアンチパススルーコントロール**

### **トークンパススルー防止**

MCP認可仕様では、重大なセキュリティリスクのために**トークンパススルーは明確に禁止**されています。

**対処されるセキュリティリスク:**
- **制御回避**: レート制限、リクエスト検証、トラフィック監視などの重要なセキュリティコントロールを回避
- **責任の所在の崩壊**: クライアント識別が不可能となり、監査証跡やインシデント調査が破壊される
- **プロキシベースの情報流出**: 悪意のある者がサーバーを不正データアクセスのプロキシとして利用可能に
- **信頼境界の侵害**: 下流サービスのトークン起源に関する信頼前提を破壊
- **横移動**: 複数サービス間でのトークンの悪用により攻撃範囲が拡大

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

### **安全なトークン管理パターン**

**ベストプラクティス:**
- **短命トークン**: 頻繁なトークンローテーションで露出時間を最小化
- **ジャストインタイム発行**: 特定の操作に必要な時のみトークンを発行
- **安全な保管**: ハードウェアセキュリティモジュール（HSM）や安全なキー保管庫を使用
- **トークンバインディング**: 可能な限りトークンを特定のクライアント、セッション、操作に紐付け
- **監視とアラート**: トークンの不正使用や不正アクセスパターンのリアルタイム検出

## 3. **セッションセキュリティコントロール**

### **セッションハイジャック防止**

**対処される攻撃ベクトル:**
- **セッションハイジャックプロンプトインジェクション**: 共有セッション状態への悪意あるイベント注入
- **セッションなりすまし**: 盗まれたセッションIDの不正使用による認証回避
- **再開可能なストリーム攻撃**: サーバー送信イベントの再開機能を悪用した悪意あるコンテンツ注入

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

**通信のセキュリティ:**
- **HTTPSの強制**: すべてのセッション通信はTLS 1.3上で行う
- **安全なクッキー属性**: HttpOnly、Secure、SameSite=Strict
- **証明書ピンニング**: MITM攻撃防止のため重要接続に適用

### **ステートフル vs ステートレスの考慮**

**ステートフル実装の場合:**
- 共有セッション状態はインジェクション攻撃に対する追加保護が必要
- キュー方式のセッション管理は整合性検証が必要
- 複数サーバーインスタンスは安全なセッション状態同期が必要

**ステートレス実装の場合:**
- JWTなどのトークンベースのセッション管理
- セッション状態の暗号的整合性検証
- 攻撃面は減少するが堅牢なトークン検証が必要

## 4. **AI特有のセキュリティコントロール**

### **プロンプトインジェクション防御**

**Microsoft Prompt Shields 統合:**
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
- **入力のサニタイズ**: すべてのユーザー入力の包括的な検証とフィルタリング
- **コンテンツ境界の定義**: システム指示とユーザーコンテンツの明確な分離
- **指示の階層構造**: 矛盾する指示に対する適切な優先順位ルール
- **出力の監視**: 潜在的に有害または操作された出力の検出

### **ツールポイズニング防止**

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
- **承認ワークフロー**: ツール変更に対する明示的なユーザー同意
- **ロールバック機能**: 以前のツールバージョンへの復元能力
- **変更監査**: ツール定義変更の完全な履歴管理
- **リスク評価**: ツールのセキュリティ状態の自動評価

## 5. **混乱代理攻撃防止**

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
- **ユーザー同意の検証**: 動的クライアント登録の同意画面を決してスキップしない
- **リダイレクトURI検証**: 厳格なホワイトリストベースのリダイレクト先検証
- **認可コード保護**: 短命で一回限りの使用を強制
- **クライアント識別検証**: クライアント資格情報およびメタデータの堅牢な検証

## 6. **ツール実行セキュリティ**

### **サンドボックス化と分離**

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

**プロセス分離:**
- **個別プロセスコンテキスト**: 各ツール実行は分離されたプロセス空間で実行
- **プロセス間通信**: 検証付きの安全なIPCメカニズム
- **プロセス監視**: 実行時の挙動分析と異常検出
- **リソース制限**: CPU、メモリ、I/O操作に対する厳格な制限

### **最小権限の実装**

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

## 7. **サプライチェーンセキュリティコントロール**

### **依存関係の検証**

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

### **継続的監視**

**サプライチェーン脅威検出:**
- **依存関係の健全性監視**: すべての依存関係のセキュリティ問題を継続的に評価
- **脅威インテリジェンス統合**: 新たなサプライチェーン脅威に関するリアルタイム更新
- **行動分析**: 外部コンポーネントの異常行動検出
- **自動対応**: 侵害されたコンポーネントの即時封じ込め

## 8. **監視および検出コントロール**

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

### **リアルタイム脅威検出**

**行動分析:**
- **ユーザー行動分析 (UBA)**: 異常なユーザーアクセスパターンの検出
- **エンティティ行動分析 (EBA)**: MCPサーバーおよびツールの挙動監視
- **機械学習異常検出**: AIによるセキュリティ脅威の特定
- **脅威インテリジェンス相関**: 既知の攻撃パターンとの照合

## 9. **インシデント対応および復旧**

### **自動応答機能**

**即時対応アクション:**
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

### **フォレンジック機能**

**調査支援:**
- **監査証跡の保全**: 暗号的整合性を持つ不変のログ記録
- **証拠収集**: 関連するセキュリティアーティファクトの自動収集
- **タイムライン再構築**: セキュリティインシデントに至る詳細なイベント順序
- **影響評価**: 侵害範囲およびデータ漏洩の評価

## **主要なセキュリティアーキテクチャ原則**

### **多層防御 (Defense in Depth)**
- **複数のセキュリティ層**: セキュリティアーキテクチャに単一障害点なし
- **冗長なコントロール**: 重要機能に重複したセキュリティ対策
- **フェイルセーフ機構**: システムがエラーや攻撃に遭遇した際の安全なデフォルト

### **ゼロトラスト実装**
- **決して信頼せず、常に検証**: すべてのエンティティとリクエストを継続的に検証
- **最小権限の原則**: すべてのコンポーネントに最小限のアクセス権を付与
- **マイクロセグメンテーション**: 詳細なネットワークおよびアクセス制御

### **継続的なセキュリティ進化**
- **脅威環境への適応**: 新たな脅威に対応するための定期的な更新
- **セキュリティコントロールの有効性**: コントロールの継続的な評価と改善
- **仕様準拠**: 進化するMCPセキュリティ標準との整合性

---

## **実装リソース**

### **公式MCPドキュメント**
- [MCP仕様 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP認可仕様](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoftセキュリティソリューション**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **セキュリティ標準**
- [OAuth 2.0 セキュリティベストプラクティス (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP 大規模言語モデル向けトップ10](https://genai.owasp.org/)
- [NIST サイバーセキュリティフレームワーク](https://www.nist.gov/cyberframework)

---

> **重要**: これらのセキュリティコントロールは現在のMCP仕様 (2025-06-18) を反映しています。標準は急速に進化しているため、常に最新の [公式ドキュメント](https://spec.modelcontextprotocol.io/) を確認してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
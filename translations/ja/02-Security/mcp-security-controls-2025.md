# MCP セキュリティコントロール - 2026年2月アップデート

> **現行標準**: 本ドキュメントは [MCP仕様書 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) のセキュリティ要求事項および公式の [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) を反映しています。

Model Context Protocol (MCP) は伝統的なソフトウェアセキュリティだけでなく、AI固有の脅威にも対応する強化されたセキュリティコントロールにより大きく成熟しました。本ドキュメントは OWASP MCP トップ10フレームワークに沿った安全なMCP実装のための包括的なセキュリティコントロールを提供します。

## 🏔️ 実践的セキュリティトレーニング

実践的なハンズオンによるセキュリティ実装経験のために、**[MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/)** を推奨します。これは「脆弱 → 攻撃 → 修正 → 検証」という方法論でAzure上のMCPサーバーのセキュリティを包括的に案内するガイド付き遠征です。

本ドキュメントのすべてのセキュリティコントロールは、OWASP MCP トップ10リスクに対する参照アーキテクチャやAzure固有の実装ガイダンスを提供する**[OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/)** と整合しています。

## **必須セキュリティ要件**

### **MCP仕様からの重大な禁止事項：**

> **禁止**: MCPサーバーは、明示的にMCPサーバー向けに発行されていないトークンを受け入れてはならない  
>
> **禁止**: MCPサーバーは認証にセッションを使用してはならない  
>
> **必須**: 認可を実装するMCPサーバーは、すべての受信リクエストを検証しなければならない  
>
> **必須**: 静的クライアントIDを使用するMCPプロキシサーバーは動的に登録されたクライアントに対してユーザー同意を取得しなければならない  

---

## 1. **認証・認可コントロール**

### **外部IDプロバイダー統合**

**現行MCP標準 (2025-11-25)** ではMCPサーバーが認証を外部IDプロバイダーに委任可能であり、これは大きなセキュリティ改善です：

**対応するOWASP MCPリスク**: [MCP07 - 不十分な認証と認可](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**セキュリティ上の利点:**
1. **カスタム認証リスクの排除**: 独自実装の認証による脆弱性を削減
2. **エンタープライズグレードのセキュリティ**: Microsoft Entra IDなど確立されたIDプロバイダーの高度なセキュリティ機能を活用
3. **中央管理されたアイデンティティ管理**: ユーザーのライフサイクル管理、アクセス制御、監査を簡素化
4. **多要素認証**: 企業IDプロバイダーからのMFA機能を継承
5. **条件付きアクセスポリシー**: リスクベースのアクセス制御や適応認証の恩恵を享受

**実装要件:**
- **トークンのオーディエンス検証**: すべてのトークンがMCPサーバー向けに発行されていることを確認する
- **発行者検証**: トークン発行者が期待されるIDプロバイダーと一致することを検証
- **署名検証**: トークンの暗号的整合性を検証
- **有効期限の厳守**: トークンの寿命制限を厳格に適用
- **スコープ検証**: トークンにリクエストされた操作に適切な権限が含まれていることを確認

### **認可ロジックのセキュリティ**

**重要なコントロール:**
- **包括的な認可監査**: すべての認可判断点に関する定期的なセキュリティレビュー
- **フェイルセーフのデフォルト設定**: 認可ロジックで明確な判断ができない場合はアクセス拒否
- **権限境界の明確化**: 異なる特権レベルとリソースアクセスの明確な分離
- **監査ログ**: すべての認可判断を完全にログに記録しセキュリティ監視に活用
- **定期的なアクセスレビュー**: ユーザー権限と特権設定の定期検証

## 2. **トークンセキュリティとアンチパススルーコントロール**

**対応するOWASP MCPリスク**: [MCP01 - トークン管理不良と秘密情報漏えい](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **トークンパススルーの防止**

トークンパススルーはMCP認可仕様で明確に禁止されており、重大なセキュリティリスクがあります：

**対応するセキュリティリスク:**
- **コントロールの回避**: レート制限、リクエスト検証、トラフィック監視などの重要なセキュリティコントロールをバイパス
- **アカウンタビリティ破綻**: クライアント識別不能となり監査証跡やインシデント調査が困難に
- **プロキシを使ったデータ流出**: 不正なデータアクセスのためにサーバーをプロキシとして利用される可能性
- **信頼境界の違反**: トークン出所に関する下流サービスの信頼想定を破壊
- **ラテラルムーブメント**: 複数サービス間でトークンが悪用されより広範な攻撃拡大を促進

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
- **短寿命トークン**: トークンの露出時間を最小化するために頻繁なローテーションを行う
- **ジャストインタイム発行**: 具体的な操作に必要な時のみトークンを発行
- **安全な保管**: ハードウェアセキュリティモジュール(HSM)や安全なキーコンテナを使用
- **トークンバインディング**: 可能な場合は特定クライアント、セッション、操作にトークンを紐付ける
- **監視・警告**: トークンの不正使用や未承認アクセスパターンをリアルタイム検知

## 3. **セッションセキュリティコントロール**

### **セッションハイジャック防止**

**対応攻撃ベクトル:**
- **セッションハイジャックによるプロンプトインジェクション**: 共有セッション状態への悪意あるイベント注入
- **セッションなりすまし**: 盗用されたセッションIDの不正使用による認証回避
- **再開可能なストリーム攻撃**: サーバー送信イベント再開機能を悪用した悪意のあるコンテンツ注入

**必須セッションコントロール:**
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

**通信セキュリティ:**
- **HTTPS適用**: すべてのセッション通信はTLS 1.3で
- **セキュアクッキー属性**: HttpOnly、Secure、SameSite=Strict
- **証明書ピニング**: 中間者攻撃防止のため重要接続で適用

### **ステートフル vs ステートレスの考慮**

**ステートフル実装の場合:**
- 共有セッション状態は注入攻撃に対する追加保護が必要
- キュー方式のセッション管理は状態の整合性を検証
- 複数サーバーインスタンス間のセッション状態同期を安全に実施

**ステートレス実装の場合:**
- JWTや類似のトークンベースセッション管理
- セッション状態整合性の暗号的検証
- 攻撃対象を減らすが堅牢なトークン検証が必須

## 4. **AI固有のセキュリティコントロール**

**対応するOWASP MCPリスク**:
- [MCP06 - コンテキストペイロードによるプロンプトインジェクション](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - ツールポイズニング](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - コマンドインジェクションおよび実行](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

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
- **入力サニタイズ**: すべてのユーザー入力に対して包括的な検証とフィルタリング
- **コンテンツ境界の定義**: システム命令とユーザーコンテンツの明確な分離
- **指示の階層構造**: 矛盾する命令の優先順位規則の適用
- **出力監視**: 潜在的に有害または操作された出力の検知

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
- **承認ワークフロー**: ツール改変に対する明確なユーザー同意取得
- **ロールバック機能**: 以前のツールバージョンへの復帰能力
- **変更監査**: ツール定義変更履歴の完全記録
- **リスク評価**: ツールのセキュリティ姿勢の自動評価

## 5. **Confused Deputy攻撃防止**

### **OAuthプロキシセキュリティ**

**防止コントロール:**
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
- **ユーザー同意の検証**: 動的クライアント登録で同意画面を省略しない
- **リダイレクトURI検証**: ホワイトリストによる厳格なリダイレクト先検証
- **認可コード保護**: 短命で一回限り利用を強制
- **クライアント識別検証**: クライアント認証情報やメタデータの堅牢な検証

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
- **個別プロセスコンテキスト**: 各ツール実行は分離されたプロセス空間内で行う
- **プロセス間通信**: バリデーション付きの安全なIPC機構
- **プロセス監視**: 実行時の振る舞い解析と異常検知
- **リソース制限**: CPU、メモリ、I/O操作に対するハードリミット設定

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

**対応するOWASP MCPリスク**: [MCP04 - サプライチェーン攻撃](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **依存関係の検証**

**包括的コンポーネントセキュリティ:**
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
- **依存関係ヘルスモニタリング**: すべての依存関係のセキュリティ問題を継続的に評価
- **脅威インテリジェンス連携**: 新興サプライチェーン脅威に関するリアルタイム更新
- **挙動分析**: 外部コンポーネントの異常挙動検出
- **自動対応**: 侵害されたコンポーネントの即時封じ込め

## 8. **監視・検知コントロール**

**対応するOWASP MCPリスク**: [MCP08 - 監査およびテレメトリ不足](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **セキュリティ情報・イベント管理 (SIEM)**

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

### **リアルタイム脅威検知**

**行動分析:**
- **ユーザー行動分析 (UBA)**: 異常なユーザーアクセスパターンの検出
- **エンティティ行動分析 (EBA)**: MCPサーバーおよびツールの振る舞い監視
- **機械学習異常検知**: AIによるセキュリティ脅威の識別
- **脅威インテリジェンス相関**: 確認された攻撃パターンと活動を照合

## 9. **インシデント対応・復旧**

### **自動対応能力**

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

### **フォレンジック能力**

**調査支援:**
- **監査証跡の保全**: 暗号的整合性を備えた不変ログ
- **証拠収集**: 関連するセキュリティアーティファクトの自動収集
- **時間軸再構築**: セキュリティインシデントに至る詳細なイベントシーケンス
- **影響評価**: 侵害範囲およびデータ露見の評価

## **主要なセキュリティアーキテクチャ原則**

### **多層防御 (Defense in Depth)**
- **複数のセキュリティレイヤー**: セキュリティ構造に単一障害点なし
- **冗長コントロール**: 重要機能に対する重複セキュリティ対策
- **フェイルセーフメカニズム**: システム障害や攻撃時に安全なデフォルトを適用

### **ゼロトラスト実装**
- **信用しない、常に検証する**: すべてのエンティティとリクエストを継続的に検証
- **最小権限の原則**: すべてのコンポーネントに対する最小限のアクセス権
- **マイクロセグメンテーション**: 詳細なネットワークおよびアクセス制御

### **継続的なセキュリティ進化**
- **脅威環境の適応**: 新たに出現する脅威に対応するため定期的な更新
- **セキュリティコントロールの効果測定**: 継続的な評価と改善
- **仕様への準拠**: 進化するMCPセキュリティ標準との整合

---

## **実装リソース**

### **公式MCPドキュメント**
- [MCP仕様書 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP認可仕様](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **OWASP MCPセキュリティリソース**
- [OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/) - Azure実装を含むOWASP MCPトップ10の包括的ガイド
- [OWASP MCPトップ10](https://owasp.org/www-project-mcp-top-10/) - 公式OWASP MCPセキュリティリスク
- [MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/) - Azure上MCPの実践的セキュリティトレーニング

### **Microsoftセキュリティソリューション**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **セキュリティ標準**
- [OAuth 2.0 セキュリティベストプラクティス (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP 大規模言語モデルトップ10](https://genai.owasp.org/)
- [NIST サイバーセキュリティフレームワーク](https://www.nist.gov/cyberframework)

---

> **重要**: これらのセキュリティコントロールは現行のMCP仕様書 (2025-11-25) に基づいています。標準は急速に進化しているため、常に最新の[公式ドキュメント](https://spec.modelcontextprotocol.io/)と照合してください。

## 次のステップ

- 戻る： [セキュリティモジュール概要](./README.md)
- 続けて: [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語版を正式な情報源としてご参照ください。重要な情報については、専門の翻訳者による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳に関して、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

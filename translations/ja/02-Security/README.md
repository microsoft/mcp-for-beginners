# MCP セキュリティ: AI システムの包括的な保護

[![MCP Security Best Practices](../../../translated_images/ja/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_（上の画像をクリックするとこのレッスンのビデオが表示されます）_

セキュリティはAIシステム設計の基本であり、これが私たちが第二のセクションとして優先している理由です。これはMicrosoftの[Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/)の<strong>Secure by Design</strong>原則と一致しています。

Model Context Protocol (MCP) は、AI駆動アプリケーションに強力な新機能をもたらす一方で、従来のソフトウェアリスクを超えた独自のセキュリティ課題も導入します。MCPシステムは、従来のセキュリティ問題（セキュアコーディング、最小権限、サプライチェーンセキュリティ）に加え、プロンプトインジェクション、ツール汚染、セッションハイジャック、混乱代理攻撃、トークンパススルー脆弱性、動的機能変更など、AI特有の新たな脅威にも直面しています。

このレッスンでは、MCP実装における最重要のセキュリティリスクを探り、認証、認可、過剰な権限、間接的なプロンプトインジェクション、セッションセキュリティ、混乱代理問題、トークン管理、サプライチェーンの脆弱性をカバーします。これらのリスクを軽減するための実践的なコントロールやベストプラクティスを学び、MicrosoftのPrompt Shields、Azure Content Safety、GitHub Advanced Securityなどのソリューションを活用してMCP展開を強化する方法を理解します。

## 学習目標

このレッスンの終了時には、次のことができるようになります:

- **MCP固有の脅威の特定**: プロンプトインジェクション、ツール汚染、過剰な権限、セッションハイジャック、混乱代理問題、トークンパススルー脆弱性、サプライチェーンリスクなど、MCPシステム特有のセキュリティリスクを認識する
- <strong>セキュリティコントロールの適用</strong>: 強固な認証、最小権限アクセス、安全なトークン管理、セッションセキュリティ、サプライチェーン検証など、効果的な対策を実装する
- **Microsoftのセキュリティソリューションの活用**: MicrosoftのPrompt Shields、Azure Content Safety、GitHub Advanced Securityを理解し、MCPワークロード保護に展開する
- <strong>ツールセキュリティの検証</strong>: ツールのメタデータ検証、動的変更の監視、間接的なプロンプトインジェクション攻撃への防御の重要性を認識する
- <strong>ベストプラクティスの統合</strong>: セキュアコーディングやサーバーハードニング、ゼロトラストなどの基礎的なセキュリティとMCP固有のコントロールを組み合わせて包括的な保護を実現する

# MCP セキュリティアーキテクチャとコントロール

近代的なMCP実装では、従来のソフトウェアセキュリティとAI特有の脅威の両方に対応する多層的なセキュリティアプローチが必要です。急速に進化するMCP仕様はセキュリティコントロールの成熟を進めており、エンタープライズのセキュリティアーキテクチャや確立されたベストプラクティスとの統合を促進しています。

[Microsoft Digital Defense Report](https://aka.ms/mddr) の調査によれば、<strong>報告された侵害の98%は堅牢なセキュリティ衛生管理によって防止可能</strong>です。最も効果的な保護戦略は、基礎的なセキュリティプラクティスとMCP固有のコントロールを組み合わせたものであり、証明されたベースラインのセキュリティ対策が全体的なセキュリティリスクの減少に最も強い影響を与えます。

## 現行のセキュリティ状況

> **注意:** 本章では、確立されたMCPセキュリティコントロールと
> 現行の<strong>MCP仕様 2026-07-28</strong>の認可ガイダンスを組み合わせています。常に
> 最新の[MCP仕様](https://modelcontextprotocol.io/specification/2026-07-28/)、
> [MCP GitHubリポジトリ](https://github.com/modelcontextprotocol)、
> [セキュリティベストプラクティス文書](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> を参照して、セキュリティに敏感なコードを実装してください。

> **認可の更新:** MCP `2026-07-28` ではクライアントが認可応答で
> `iss` パラメーターの検証（RFC 9207）を行い、登録済み資格情報を発行元の認可サーバーに
> バインドすることが求められています。Dynamic Client Registrationは非推奨となり、
> 新しい実装ではClient ID メタデータドキュメントを使用すべきです。
> 詳細は[What's Changed in MCP: The 2026-07-28 Specification](../01-CoreConcepts/mcp-2026-07-28.md)
> を参照し、認可の変更点を確認してください。

## 🏔️ MCPセキュリティサミットワークショップ（Sherpa）

<strong>実践的なセキュリティトレーニング</strong>として、Microsoft Azure上のMCPサーバーを安全にするための包括的なガイド付き遠征である<strong>MCPセキュリティサミットワークショップ（Sherpa）</strong>を強くお勧めします。

### ワークショップ概要

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) は、検証済みの「脆弱 → 攻撃 → 修正 → 検証」メソッドを通じて実践的で実行可能なセキュリティトレーニングを提供します。次のことが体験できます：

- **壊して学ぶ:** 意図的に脆弱なサーバーを攻撃して脆弱性を直接経験する
- **Azureネイティブセキュリティを利用:** Azure Entra ID、Key Vault、API Management、AI Content Safetyを活用
- **多層防御を実践:** 拠点ごとに包括的なセキュリティ層を構築して進む
- **OWASP基準に準拠:** すべての手法が[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)に対応
- **本番コードを入手:** 動作検証済みの実装を持ち帰る

### 遠征ルート

| キャンプ | 焦点 | 対応するOWASPリスク |
|------|-------|---------------------|
| <strong>ベースキャンプ</strong> | MCP基礎 & 認証の脆弱性 | MCP01, MCP07 |
| **キャンプ1: アイデンティティ** | OAuth 2.1、Azureマネージドアイデンティティ、Key Vault | MCP01, MCP02, MCP07 |
| **キャンプ2: ゲートウェイ** | API Management、プライベートエンドポイント、ガバナンス | MCP02, MCP06, MCP07, MCP09 |
| **キャンプ3: I/Oセキュリティ** | プロンプトインジェクション、PII保護、コンテンツセーフティ | MCP03, MCP05, MCP06, MCP10 |
| **キャンプ4: 監視** | ログアナリティクス、ダッシュボード、脅威検出 | MCP04, MCP08 |
| <strong>サミット</strong> | レッドチーム / ブルーチーム統合テスト | 全リスク |

**始める:** [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP トップ10 セキュリティリスク

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)には、MCP実装における最も重要な10のセキュリティリスクが詳細に記載されています:

| リスク | 説明 | Azureによる緩和策 |
|------|-------|------------------|
| **MCP01** | トークンの誤管理と秘密の漏洩 | Azure Key Vault、マネージドアイデンティティ |
| **MCP02** | スコープクリープによる権限昇格 | RBAC、条件付きアクセス |
| **MCP03** | ツール汚染 | ツールの検証、整合性確認 |
| **MCP04** | ソフトウェアサプライチェーン攻撃および依存関係改ざん | GitHub Advanced Security、依存関係スキャン |
| **MCP05** | コマンドインジェクションと実行 | 入力検証、サンドボックス |
| **MCP06** | 意図フローの攪乱 | Azure AI Content Safety、Prompt Shields |

| **MCP07** | 不十分な認証および認可 | Azure Entra ID、PKCE対応OAuth 2.1 |
| **MCP08** | 監査およびテレメトリの欠如 | Azure Monitor、Application Insights |
| **MCP09** | シャドウMCPサーバー | APIセンターガバナンス、ネットワーク分離 |
| **MCP10** | コンテキスト注入および過剰共有 | データ分類、最小限の公開 |

### MCP認証の進化

MCP仕様は認証および認可のアプローチにおいて大きく進化しています：

- <strong>元のアプローチ</strong>：初期仕様では開発者がカスタム認証サーバーを実装し、MCPサーバーはOAuth 2.0認可サーバーとしてユーザー認証を直接管理していました
- **現在の標準（`2026-07-28`）**：MCPサーバーは認証を
  Microsoft Entra IDなど外部のIDプロバイダーに委任できます。クライアントも
  現行の発行者検証および資格情報バインディング要件を適用しなければなりません。
- <strong>トランスポート層のセキュリティ</strong>：ローカル（STDIO）およびリモート（ストリーム可能なHTTP）接続の両方に適切な認証パターンを備えた安全なトランスポートメカニズムのサポート強化

## 認証および認可のセキュリティ

### 現在のセキュリティ課題

現代のMCP実装は複数の認証および認可に関する課題に直面しています：

### リスクおよび脅威ベクトル

- <strong>誤設定された認可ロジック</strong>：MCPサーバーの脆弱な認可実装により機密データが露出し、アクセス制御が誤って適用される可能性があります
- **OAuthトークンの乗っ取り**：ローカルMCPサーバートークンの窃盗により攻撃者はサーバーを偽装して下流サービスにアクセス可能になります
- <strong>トークンパススルーの脆弱性</strong>：不適切なトークン処理でセキュリティ制御の回避や責任追跡の欠落を招きます
- <strong>過剰な権限</strong>：権限の過剰なMCPサーバーは最小権限原則に反し攻撃対象範囲を広げます

#### トークンパススルー：重大なアンチパターン

<strong>トークンパススルーは現在のMCP認可仕様で厳禁</strong>とされており、重大なセキュリティ上の影響があります：

##### セキュリティ制御の迂回
- MCPサーバーおよび下流APIは（レートリミット、リクエスト検証、トラフィック監視など）重要なセキュリティ制御をトークン検証に依存しています
- クライアントからAPIへの直接トークン使用はこれらの保護を回避し、セキュリティアーキテクチャを破壊します

##### 責任追跡および監査上の課題  
- MCPサーバーは上流発行トークンを用いるクライアントの区別がつかず、監査トレイルが破壊されます
- 下流リソースサーバーログは誤解を招くリクエスト起点を示し、実際のMCPサーバー中継を反映しません
- インシデント調査やコンプライアンス監査が著しく困難になります

##### データ外部流出リスク
- 検証されていないトークン請求情報により、盗まれたトークンで悪意のある攻撃者がMCPサーバーを代理にデータ外部流出を行えます
- 信頼境界の破壊により、意図されたセキュリティ制御を回避する不正なアクセスパターンが許されます

##### 複数サービスにわたる攻撃ベクトル
- 複数サービスで受け入れられる乗っ取られたトークンが隣接するシステム間の水平移動を可能にします
- トークンの出所検証不能により、サービス間の信頼仮定が侵害される可能性があります

### セキュリティ制御および緩和策

**重要なセキュリティ要件:**

> <strong>必須</strong>：MCPサーバーは<strong>明示的にMCPサーバー用に発行されていないトークンを受け入れてはなりません</strong>

#### 認証および認可の制御

- <strong>厳格な認可レビュー</strong>：MCPサーバーの認可ロジックを包括的に監査し、意図しないユーザーやクライアントに機密リソースがアクセスされないことを保証します
  - <strong>実装ガイド</strong>：[Azure API Management as Authentication Gateway for MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **ID統合**：[Using Microsoft Entra ID for MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- <strong>安全なトークン管理</strong>：[Microsoftのトークン検証およびライフサイクルベストプラクティス](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)を実装
  - トークンのaudience請求情報がMCPサーバーIDに一致することを検証
  - 適切なトークンのローテーションおよび有効期限ポリシーを実施
  - トークンのリプレイ攻撃や不正使用を防止

- <strong>保護されたトークンストレージ</strong>：保存時および転送時に暗号化した安全なトークン保管
  - <strong>ベストプラクティス</strong>：[Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### アクセス制御の実装

- <strong>最小権限の原則</strong>：MCPサーバーに対し、必要な機能のための最小限の権限のみ付与
  - 権限の過剰付与を防ぐため定期的なレビュおよび更新
  - **Microsoftドキュメント**：[Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **ロールベースアクセス制御（RBAC）**：細かい役割割り当てを実施
  - 特定リソースやアクションにロールを厳密にスコープ
  - 攻撃対象範囲を拡大する広範または不要な権限を回避

- <strong>継続的な権限監視</strong>：アクセス監査および監視を継続的に実施
  - 異常な権限使用パターンを監視
  - 過剰または未使用権限の速やかな是正措置

## AI特有のセキュリティ脅威

### プロンプトインジェクションおよびツール操作攻撃

現代のMCP実装は、従来のセキュリティ対策では充分に対処できない高度なAI特有の攻撃ベクトルに直面しています：

#### **間接的プロンプトインジェクション（クロスドメインプロンプトインジェクション）**

<strong>間接的プロンプトインジェクション</strong>は、MCP対応AIシステムにおける最も重大な脆弱性の一つです。攻撃者は悪意のある指示を外部コンテンツ（文書、ウェブページ、メール、データソース）に埋め込み、AIがこれを正当なコマンドとして処理します。

**攻撃シナリオ：**
- <strong>文書ベースのインジェクション</strong>：処理される文書に隠された悪意の指示が意図しないAI動作を引き起こす
- <strong>ウェブコンテンツ悪用</strong>：スクレイピング時にAIの振る舞いを操作する埋め込みプロンプトを含む改ざんされたウェブページ
- <strong>メールベース攻撃</strong>：AIアシスタントが情報漏洩や不正動作を行う悪意のあるメール内プロンプト
- <strong>データソース汚染</strong>：汚染された内容をAIに提供する改ざんされたデータベースやAPI

<strong>実際の影響</strong>：これらの攻撃はデータ流出、プライバシー侵害、有害コンテンツ生成、ユーザー対話操作を引き起こす可能性があります。詳細な分析は[Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)を参照してください。

![Prompt Injection Attack Diagram](../../../translated_images/ja/prompt-injection.ed9fbfde297ca877.webp)

#### <strong>ツールポイズニング攻撃</strong>

<strong>ツールポイズニング</strong>はMCPツールのメタデータを標的とし、LLMがツールの説明やパラメーターをどのように解釈して実行判断をするかを悪用します。

**攻撃手法：**
- <strong>メタデータ操作</strong>：攻撃者がツールの説明、パラメーター定義、使用例に悪意のある指示を注入
- <strong>不可視指示</strong>：ユーザーに見えないがAIモデルに処理されるツールメタデータ内プロンプト
- **動的ツール変更（「ラグプル」）**：ユーザーが承認したツールを後から悪意ある動作に変更
- <strong>パラメーターインジェクション</strong>：モデルの振る舞いに影響を与えるツールパラメーター定義への悪意の埋め込み


<strong>ホスト型サーバーのリスク</strong>: リモートMCPサーバーは、ツール定義がユーザーの初回承認後に更新される可能性があるため、以前は安全だったツールが悪意のあるものになるシナリオを生み出し、リスクが高まります。詳細な分析については、[Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) を参照してください。

![Tool Injection Attack Diagram](../../../translated_images/ja/tool-injection.3b0b4a6b24de6bef.webp)

#### **追加のAI攻撃ベクトル**

- **クロスドメインプロンプトインジェクション (XPIA)**: 複数のドメインのコンテンツを活用してセキュリティ制御を回避する高度な攻撃
- <strong>動的能力変更</strong>: 初期のセキュリティ評価を回避するためのリアルタイムでのツール能力変更
- <strong>コンテキストウィンドウ汚染</strong>: 大きなコンテキストウィンドウを操作して悪意のある指示を隠す攻撃
- <strong>モデル混乱攻撃</strong>: モデルの制限を悪用して予測不能または安全でない動作を引き起こす


### AIセキュリティリスクの影響

**大きな影響を及ぼす結果:**
- <strong>データ流出</strong>: 企業や個人の機密データへの不正アクセスおよび窃取
- <strong>プライバシー侵害</strong>: 個人識別情報（PII）や機密的なビジネスデータの露出  
- <strong>システム操作</strong>: 重要システムやワークフローへの意図しない変更
- <strong>認証情報の窃取</strong>: 認証トークンやサービス資格情報の侵害
- <strong>横展開</strong>: 侵害されたAIシステムを足がかりにネットワーク全体への攻撃を拡大

### Microsoft AIセキュリティソリューション

#### **AIプロンプトシールド: インジェクション攻撃に対する高度な防御**

Microsoftの **AIプロンプトシールド** は、複数のセキュリティレイヤーを通じて直接的・間接的なプロンプトインジェクション攻撃から包括的な防御を提供します：

##### **コア保護メカニズム:**

1. <strong>高度な検出とフィルタリング</strong>
   - 悪意のある指示を検出する機械学習アルゴリズムと自然言語処理技術
   - ドキュメント、ウェブページ、メール、データソースのリアルタイム解析による埋め込み脅威の検出
   - 合法的なプロンプトパターンと悪意のあるものの文脈的理解

2. <strong>スポットライト技術</strong>  
   - 信頼されたシステム指示と潜在的に侵害された外部入力を識別
   - 悪意のあるコンテンツを分離しつつモデルの関連性を高めるテキスト変換手法
   - AIシステムが適正な指示階層を維持し、挿入された命令を無視するのを支援

3. <strong>区切り文字とデータマークシステム</strong>
   - 信頼されたシステムメッセージと外部テキスト入力間の明示的な境界定義
   - 信頼・非信頼データソース間の境界を強調表示する特殊マーカー
   - 明確な分離により指示の混乱や不正なコマンド実行を防止

4. <strong>継続的な脅威インテリジェンス</strong>
   - Microsoftは新興の攻撃パターンを継続的に監視し、防御を更新
   - 新たなインジェクション技術や攻撃ベクトルの積極的な脅威ハンティング
   - 進化する脅威に対抗するための定期的なセキュリティモデルの更新

5. **Azure Content Safety連携**
   - Azure AI Content Safetyスイートの一部
   - ジェイルブレイク試行、有害コンテンツ、セキュリティポリシー違反の追加検出
   - AIアプリケーションコンポーネント全体での統合セキュリティ制御

<strong>実装リソース</strong>: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/ja/prompt-shield.ff5b95be76e9c78c.webp)


## 高度なMCPセキュリティ脅威

### セッションハイジャック脆弱性

<strong>セッションハイジャック</strong>は、状態を保持するMCP実装において、正当なセッション識別子を不正に取得し悪用することでクライアントになりすまし、不正な行為を行う重大な攻撃経路を指します。

#### <strong>攻撃シナリオとリスク</strong>

- <strong>セッションハイジャックプロンプトインジェクション</strong>: 盗まれたセッションIDを持つ攻撃者が、セッション状態を共有するサーバーに悪意のあるイベントを注入し、有害な行動や機密データへのアクセスを引き起こす可能性
- <strong>直接なりすまし</strong>: 盗まれたセッションIDにより認証を回避する直接的なMCPサーバー呼び出しが可能となり、攻撃者が正当なユーザーとして扱われる
- <strong>侵害された再開可能ストリーム</strong>: 攻撃者がリクエストを早期終了させ、正当なクライアントが悪意のあるコンテンツで再開する可能性

#### <strong>セッション管理のためのセキュリティ制御</strong>

**重要な要件:**
- <strong>認可検証</strong>: 認可を実装するMCPサーバーはすべての受信リクエストを検証し、セッションによる認証に依存してはならない
- <strong>安全なセッション生成</strong>: 暗号的に安全で非決定論的なセッションIDを、安全な乱数生成器で生成すること
- <strong>ユーザー固有のバインディング</strong>: `<user_id>:<session_id>` などの形式でセッションIDをユーザー固有情報に紐付け、クロスユーザーセッションの悪用を防止
- <strong>セッションライフサイクル管理</strong>: 適切な期限切れ、ローテーション、無効化を実施し、脆弱性の窓を限定
- <strong>通信の安全性</strong>: セッションIDの盗聴を防ぐためすべての通信にHTTPSを必須化

### 混乱代理問題

<strong>混乱代理問題</strong>は、MCPサーバーがクライアントとサードパーティサービスの間の認証プロキシとして機能する際に生じ、静的なクライアントIDの悪用による認可バイパスの機会を生み出します。

#### <strong>攻撃の仕組みとリスク</strong>

- <strong>クッキーによる同意バイパス</strong>: 先行するユーザー認証が同意クッキーを作成し、攻撃者が悪意のある認可要求と細工されたリダイレクトURIを使ってこれを悪用
- <strong>認可コードの窃取</strong>: 既存の同意クッキーによって認可サーバーが同意画面をスキップし、コードを攻撃者管理のエンドポイントにリダイレクト
- **不正なAPIアクセス**: 窃取された認可コードにより明示的承認なしにトークン交換やユーザーなりすましが可能

#### <strong>軽減戦略</strong>

**必須制御事項:**
- <strong>明示的同意要求</strong>: 静的クライアントIDを使用するMCPプロキシサーバーは、動的に登録された各クライアントについてユーザーの同意を取得すべき
- **OAuth 2.1のセキュリティ実装**: すべての認可要求にPKCE（Proof Key for Code Exchange）を含む現在のOAuthセキュリティベストプラクティスを遵守
- <strong>厳格なクライアント検証</strong>: リダイレクトURIとクライアント識別子の厳密な検証を実装し悪用を防止

### トークンパススルー脆弱性  

<strong>トークンパススルー</strong>は、MCPサーバーがクライアントトークンを適切に検証せずに受け入れ、下流のAPIに転送することで、MCP認可仕様に違反する明確なアンチパターンを示します。

#### <strong>セキュリティ上の影響</strong>

- <strong>制御回避</strong>: クライアントからAPIへの直接トークン利用は重要なレート制限、検証、監視を迂回
- <strong>監査トレイルの破損</strong>: 上流発行トークンはクライアント特定を不可能にし、インシデント調査機能を破壊
- <strong>プロキシによるデータ流出</strong>: 検証されていないトークンはサーバーを不正データアクセスのプロキシとして悪用可能に
- <strong>信頼境界の違反</strong>: 下流サービスの信頼前提がトークン起源不明により破られる可能性
- <strong>マルチサービス攻撃拡大</strong>: 複数サービスで有効な侵害トークンにより横展開が可能

#### <strong>必須セキュリティ制御</strong>

**譲れない要件:**
- <strong>トークン検証</strong>: MCPサーバーは明示的にMCPサーバー用に発行されていないトークンを受け入れてはならない
- <strong>オーディエンス検証</strong>: トークンのオーディエンスクレームがMCPサーバーのIDと一致するか常に検証する
- <strong>適切なトークンライフサイクル</strong>: 短寿命アクセストークンを実装し安全なローテーションを行う


## AIシステムのサプライチェーンセキュリティ

サプライチェーンセキュリティは従来のソフトウェア依存関係を超えてAIエコシステム全体に及んでいます。最新のMCP実装はすべてのAI関連コンポーネントを厳格に検証・監視する必要があり、それぞれがシステムの整合性を脅かす可能性のある脆弱性をもたらします。

### 拡張されたAIサプライチェーン構成要素

**従来のソフトウェア依存関係:**
- オープンソースのライブラリおよびフレームワーク
- コンテナイメージおよびベースシステム  
- 開発ツールおよびビルドパイプライン
- インフラストラクチャのコンポーネントとサービス

**AI固有のサプライチェーン要素:**
- <strong>ファウンデーションモデル</strong>: 各種プロバイダーからの事前学習済みモデルで出所検証が必要
- <strong>埋め込みサービス</strong>: 外部のベクトル化および意味検索サービス
- <strong>コンテキストプロバイダー</strong>: データソース、ナレッジベース、ドキュメントリポジトリ  
- **サードパーティAPI**: 外部AIサービス、MLパイプライン、データ処理エンドポイント
- <strong>モデルアーティファクト</strong>: 重み、構成、ファインチューニング済みモデルバリアント
- <strong>トレーニングデータソース</strong>: モデルのトレーニングおよびファインチューニングに使用されるデータセット

### 包括的なサプライチェーンセキュリティ戦略

#### <strong>コンポーネントの検証と信頼</strong>
- <strong>出所の検証</strong>: すべてのAIコンポーネントの起源、ライセンス、整合性を統合前に確認
- <strong>セキュリティ評価</strong>: モデル、データソース、AIサービスの脆弱性スキャンとセキュリティレビューを実施
- <strong>評判分析</strong>: AIサービスプロバイダーのセキュリティ実績と慣行を評価
- <strong>コンプライアンス検証</strong>: すべてのコンポーネントが組織のセキュリティおよび規制要件を満たしていることを確認

#### <strong>安全なデプロイメントパイプライン</strong>  
- **自動CI/CDセキュリティ**: 自動化されたデプロイメントパイプライン全体でのセキュリティスキャンを統合
- <strong>アーティファクトの整合性</strong>: すべての展開済みアーティファクト（コード、モデル、構成）に対する暗号検証の実装
- <strong>段階的デプロイ</strong>: 各段階でセキュリティ検証を行う漸進的デプロイ戦略の利用
- <strong>信頼されたアーティファクトリポジトリ</strong>: 検証済みで安全なアーティファクトレジストリ・リポジトリからのみ展開

#### <strong>継続的な監視と対応</strong>
- <strong>依存性スキャン</strong>: すべてのソフトウェアおよびAIコンポーネントの依存関係に対する継続的な脆弱性監視
- <strong>モデル監視</strong>: モデルの動作、性能の変動、セキュリティ異常の継続的評価
- <strong>サービス稼働状態追跡</strong>: 外部AIサービスの可用性、セキュリティインシデント、およびポリシー変更の監視
- <strong>脅威インテリジェンス統合</strong>: AIおよびMLのセキュリティリスクに特化した脅威フィードの取り込み

#### <strong>アクセス制御と最小権限</strong>
- <strong>コンポーネントレベルの権限</strong>: ビジネス上必要な範囲に基づいてモデル、データ、サービスへのアクセス制限
- <strong>サービスアカウント管理</strong>: 最小限の権限を持つ専用サービスアカウントの実装
- <strong>ネットワーク分割</strong>: AIコンポーネントの隔離とサービス間ネットワークアクセスの制限
- **APIゲートウェイ制御**: 外部AIサービスへのアクセス制御と監視を行う集中APIゲートウェイの利用

#### <strong>インシデント対応と復旧</strong>
- <strong>迅速対応手順</strong>: 侵害されたAIコンポーネントの修正または交換の確立されたプロセス
- <strong>認証情報ローテーション</strong>: シークレット、APIキー、サービス資格情報の自動ローテーションシステム
- <strong>ロールバック機能</strong>: AIコンポーネントの既知の正常バージョンに迅速に復帰する能力
- <strong>サプライチェーン侵害復旧</strong>: 上流AIサービス侵害への対応に特化した手順

### Microsoftのセキュリティツールと連携

<strong>GitHub Advanced Security</strong>は、包括的なサプライチェーン保護を提供し、以下を含みます：
- <strong>シークレットスキャン</strong>: リポジトリ内の資格情報、APIキー、トークンの自動検出
- <strong>依存性スキャン</strong>: オープンソース依存関係およびライブラリの脆弱性評価
- **CodeQL分析**: セキュリティ脆弱性とコーディング問題の静的コード解析
- <strong>サプライチェーンインサイト</strong>: 依存関係の健全性とセキュリティ状態の可視化

**Azure DevOps & Azure Repos連携:**
- Microsoftの開発プラットフォーム全体でのシームレスなセキュリティスキャン統合
- AIワークロード向けAzure Pipelinesの自動セキュリティチェック
- 安全なAIコンポーネント展開のポリシー強制

**Microsoft社内の運用:**
Microsoftはすべての製品において広範なサプライチェーンセキュリティ実践を実施しています。実証済みのアプローチについては、[The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/) をご覧ください。


## 基盤セキュリティのベストプラクティス

MCPの実装は組織の既存のセキュリティ態勢を継承し、それを基に構築されます。基盤となるセキュリティ実践を強化することは、AIシステムおよびMCP展開の全体的なセキュリティを大幅に向上させます。

### コアセキュリティ基礎

#### <strong>安全な開発実践</strong>
- **OWASP準拠**: [OWASP Top 10](https://owasp.org/www-project-top-ten/) のウェブアプリケーション脆弱性から保護
- **AI特有の保護**: [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) に対する制御の実装
- <strong>安全なシークレット管理</strong>: トークン、APIキー、機密設定データのための専用ボールトの使用
- <strong>エンドツーエンド暗号化</strong>: すべてのアプリケーションコンポーネントおよびデータフローに安全な通信を実装
- <strong>入力検証</strong>: すべてのユーザー入力、APIパラメータ、データソースの厳格な検証

#### <strong>インフラストラクチャの強化</strong>
- <strong>多要素認証</strong>: すべての管理者およびサービスアカウントでMFAを必須
- <strong>パッチ管理</strong>: オペレーティングシステム、フレームワーク、依存関係の自動かつ適時なパッチ適用  
- **IDプロバイダー連携**: 企業のIDプロバイダー（Microsoft Entra ID、Active Directory）による集中ID管理
- <strong>ネットワーク分割</strong>: 横展開の可能性を限定するMCPコンポーネントの論理的隔離
- <strong>最小権限の原則</strong>: すべてのシステムコンポーネントおよびアカウントに必要最小限の権限

#### <strong>セキュリティ監視と検知</strong>
- <strong>包括的なログ記録</strong>: MCPクライアント・サーバー間のインタラクションを含むAIアプリケーション活動の詳細なログ記録
- **SIEM統合**: 異常検知のための集中セキュリティ情報およびイベント管理
- <strong>行動分析</strong>: システムおよびユーザー動作の異常パターンを検出するAI駆動の監視
- <strong>脅威インテリジェンス</strong>: 外部脅威フィードおよび侵害指標（IOC）の統合
- <strong>インシデント対応</strong>: セキュリティインシデントの検出、対応、回復のための明確な手順

#### <strong>ゼロトラストアーキテクチャ</strong>
- <strong>信頼せず常に検証</strong>: ユーザー、デバイス、ネットワーク接続の継続的な検証
- <strong>マイクロセグメンテーション</strong>: 個々のワークロードおよびサービスを隔離する詳細なネットワーク制御
- <strong>アイデンティティ中心のセキュリティ</strong>: ネットワーク位置よりも検証済みアイデンティティに基づくセキュリティポリシー
- <strong>継続的リスク評価</strong>: 現状のコンテキストおよび行動に基づく動的なセキュリティ態勢評価
- <strong>条件付きアクセス</strong>: リスク要因、位置、デバイス信頼に応じて適応するアクセス制御

### エンタープライズ統合パターン

#### **Microsoftセキュリティエコシステム連携**
- **Microsoft Defender for Cloud**: 包括的なクラウドセキュリティ態勢管理
- **Azure Sentinel**: AIワークロード保護のためのクラウドネイティブSIEMおよびSOAR機能
- **Microsoft Entra ID**: 条件付きアクセスポリシーを備えた企業IDおよびアクセス管理
- **Azure Key Vault**: ハードウェアセキュリティモジュール（HSM）を利用した集中シークレット管理
- **Microsoft Purview**: AIデータソースおよびワークフローのデータガバナンスとコンプライアンス

#### <strong>コンプライアンスおよびガバナンス</strong>
- <strong>規制準拠の整合</strong>: MCP実装が業界固有のコンプライアンス要件（GDPR、HIPAA、SOC 2）を満たすことを保証

- <strong>データ分類</strong>: AIシステムが処理する機密データの適切な分類と取り扱い
- <strong>監査ログ</strong>: 規制遵守および鑑識調査のための包括的なログ記録
- <strong>プライバシーコントロール</strong>: AIシステムアーキテクチャにおけるプライバシーバイデザイン原則の実装
- <strong>変更管理</strong>: AIシステムの修正に対するセキュリティレビューの正式なプロセス

これらの基礎的な実践は、MCP固有のセキュリティコントロールの効果を高め、AI駆動アプリケーションに包括的な保護を提供する堅牢なセキュリティ基盤を構築します。

## 重要なセキュリティのポイント

- <strong>多層防御アプローチ</strong>: 基礎的なセキュリティ実践（安全なコーディング、最小権限、サプライチェーン検証、継続的監視）とAI固有のコントロールを組み合わせて包括的な保護を実現

- **AI特有の脅威環境**: MCPシステムは、プロンプトインジェクション、ツールポイズニング、セッションハイジャック、混乱した代理人問題、トークンパススルーの脆弱性、過剰な権限など、専門的な緩和策が必要な独自のリスクに直面

- <strong>認証と認可の優秀性</strong>: 外部IDプロバイダー（Microsoft Entra ID）を用いた強力な認証を実装し、適切なトークン検証を強制し、MCPサーバー向けに明示的に発行されていないトークンを決して受け入れない

- **AI攻撃の防止**: Microsoft Prompt Shields と Azure Content Safety を展開し、間接的なプロンプトインジェクションやツールポイズニング攻撃を防御しつつ、ツールのメタデータを検証し動的変化を監視

- <strong>セッションと通信のセキュリティ</strong>: ユーザー識別に紐づく暗号的に安全で非決定的なセッションIDを使用し、適切なセッションライフサイクル管理を実施し、認証にセッションを決して使用しない

- **OAuthセキュリティのベストプラクティス**: 動的登録クライアントに対する明示的なユーザー同意、PKCEを用いた適切なOAuth 2.1実装、厳格なリダイレクトURI検証により混乱した代理人攻撃を防止  

- <strong>トークンセキュリティの原則</strong>: トークンパススルーのアンチパターンを避け、トークンのオーディエンスクレームを検証し、短命トークンの安全なローテーションを実装し、明確な信頼境界を維持

- <strong>包括的なサプライチェーンセキュリティ</strong>: モデル、埋め込み、コンテキストプロバイダー、外部APIなどAIエコシステムの全コンポーネントを従来のソフトウェア依存関係と同じ厳格なセキュリティで扱う

- <strong>継続的な進化</strong>: 急速に進化するMCP仕様に最新の状態を保ち、セキュリティコミュニティの標準に貢献し、プロトコルの成熟に合わせて適応的なセキュリティ態勢を維持

- **Microsoftセキュリティ統合**: Microsoftの包括的なセキュリティエコシステム（Prompt Shields、Azure Content Safety、GitHub Advanced Security、Entra ID）を活用してMCP展開の保護を強化

## 包括的リソース

### **公式MCPセキュリティドキュメント**
- [MCP仕様（最新：2026-07-28）](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCPセキュリティベストプラクティス](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP認可仕様](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHubリポジトリ](https://github.com/modelcontextprotocol)

### **OWASP MCPセキュリティリソース**
- [OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/) - Azure実装ガイダンス付きの包括的なOWASP MCP Top 10
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - 公式OWASP MCPセキュリティリスク
- [MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/) - AzureにおけるMCPの実践的なセキュリティトレーニング

### <strong>セキュリティ標準とベストプラクティス</strong>
- [OAuth 2.0 セキュリティベストプラクティス (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Webアプリケーションセキュリティ](https://owasp.org/www-project-top-ten/)
- [大規模言語モデル向けOWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft デジタルディフェンスレポート](https://aka.ms/mddr)

### **AIセキュリティ研究＆分析**
- [MCPにおけるプロンプトインジェクション（Simon Willison）](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [ツールポイズニング攻撃（Invariant Labs）](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCPセキュリティ研究ブリーフィング（Wiz Security）](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoftセキュリティソリューション**
- [Microsoft Prompt Shieldsドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safetyサービス](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra IDセキュリティ](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azureトークン管理ベストプラクティス](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **実装ガイド＆チュートリアル**
- [Azure API ManagementをMCP認証ゲートウェイとして使用](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra IDを用いたMCPサーバー認証](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [安全なトークンストレージと暗号化（動画）](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps＆サプライチェーンセキュリティ**
- [Azure DevOpsセキュリティ](https://azure.microsoft.com/products/devops)
- [Azure Reposセキュリティ](https://azure.microsoft.com/products/devops/repos/)
- [Microsoftサプライチェーンセキュリティの歩み](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## <strong>追加のセキュリティドキュメント</strong>

包括的なセキュリティガイダンスについては、このセクションの専門ドキュメントを参照してください:

- **[CIMDおよびDCR認可サンプル](./samples/cimd-dcr-auth/README.md)** - 推奨クライアントIDメタデータドキュメントと廃止予定の動的クライアント登録フォールバックを比較する実行可能なTypeScript MCP `2026-07-28`リソースサーバー
- **[MCPセキュリティベストプラクティス](./mcp-security-best-practices.md)** - MCP実装のための完全なセキュリティベストプラクティス
- **[Azure Content Safety実装](./azure-content-safety-implementation.md)** - Azure Content Safety統合の実践的な実装例  
- **[MCPセキュリティコントロール](./mcp-security-controls.md)** - MCP展開の最新セキュリティコントロールと技術
- **[MCPベストプラクティスクイックリファレンス](./mcp-best-practices.md)** - 重要なMCPセキュリティ実践のクイックリファレンスガイド
- **[BlueHat 2026: AIの未来を守る: 多層防御パターンによるMCPの保護](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Microsoft Security Response Center (MSRC)による多層防御パターン

### <strong>実践的なセキュリティトレーニング</strong>

- **[MCPセキュリティサミットワークショップ（Sherpa）](https://azure-samples.github.io/sherpa/)** - Base CampからSummitまで段階的に進むAzure上のMCPサーバーセキュリティの包括的な実践ワークショップ
- **[OWASP MCP Azureセキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/)** - すべてのOWASP MCP Top 10リスクに関するリファレンスアーキテクチャと実装ガイダンス

---

## 次のステップ

次へ: [第3章: はじめに](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
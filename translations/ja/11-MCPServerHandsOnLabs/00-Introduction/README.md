# MCPデータベース統合の紹介

> [!NOTE]
> この学習パスの図やコードでHTTP/SSEまたは初期化オプションを使用している場合、
> サンプルのMCP `2025-11-25`の依存関係を反映しています。新規実装には、
> `2026-07-28`のステートレスリクエストとストリーミングHTTPを使用してください。

## 🎯 本ラボの内容

この入門ラボでは、データベース統合を用いたModel Context Protocol（MCP）サーバーの構築を包括的に説明します。https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-RetailのZava Retail分析ユースケースを通じて、ビジネスケース、技術アーキテクチャ、実際の応用を理解します。

## 概要

**Model Context Protocol (MCP)** は、AIアシスタントが外部データソースにリアルタイムで安全にアクセスし、やり取りできるようにします。データベース統合と組み合わせることで、強力なデータ駆動型AIアプリケーションの可能性を広げます。

この学習パスでは、PostgreSQLを介してAIアシスタントを小売販売データに接続し、行レベルセキュリティ、セマンティック検索、マルチテナントデータアクセスなどのエンタープライズパターンを実装した、運用準備の整ったMCPサーバーの構築を学びます。

## 学習目標

このラボ終了時には以下ができるようになります：

- <strong>モデルコンテキストプロトコルの定義</strong> とデータベース統合の中核的メリットの理解
- **MCPサーバーアーキテクチャの主要コンポーネントの特定**（データベース含む）
- **Zava Retailユースケースとビジネス要件の理解**
- <strong>安全かつ拡張性のあるデータベースアクセスのエンタープライズパターンの認識</strong>
- <strong>学習パスで使用されるツールと技術のリストアップ</strong>

## 🧭 課題：AIと現実世界のデータの融合

### 従来のAIの制約

現代のAIアシスタントは非常に強力ですが、実際のビジネスデータを扱う際には大きな制限があります：

| <strong>課題</strong> | <strong>説明</strong> | <strong>ビジネスインパクト</strong> |
|---------------|-----------------|-------------------|
| <strong>静的知識</strong> | 固定されたデータセットで学習したAIモデルは現在のビジネスデータにアクセスできない | 時代遅れの洞察、機会損失 |
| <strong>データサイロ</strong> | データベース、API、システムに閉じ込められた情報はAIのアクセス不能 | 不完全な分析、断片的な作業フロー |
| <strong>セキュリティ制約</strong> | 直接のデータベースアクセスはセキュリティとコンプライアンスリスクを生む | 展開の制限、手動によるデータ準備 |
| <strong>複雑なクエリ</strong> | ビジネスユーザーはデータ洞察の抽出に技術的知識を必要とする | 採用率低下、非効率なプロセス |

### MCPによる解決策

Model Context Protocolは以下を提供して、これらの課題に対処します：

- <strong>リアルタイムデータアクセス</strong>：AIアシスタントがライブデータベースとAPIを照会
- <strong>安全な統合</strong>：認証と権限による制御されたアクセス
- <strong>自然言語インターフェース</strong>：ビジネスユーザーが平易な英語で質問可能
- <strong>標準化プロトコル</strong>：異なるAIプラットフォームやツール間で動作

## 🏪 Zava Retail紹介：学習用ケーススタディ https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

この学習パスを通じて、複数店舗を持つ架空のDIY小売チェーン「Zava Retail」のためのMCPサーバーを構築します。このリアリティのあるシナリオはエンタープライズグレードのMCP実装を示しています。

### ビジネスコンテキスト

<strong>Zava Retail</strong>は以下を運営しています：
- ワシントン州内（シアトル、ベルビュー、タコマ、スポケーン、エバレット、レドモンド、カークランド）に<strong>8つの実店舗</strong>
- eコマース販売向けに<strong>1つのオンラインストア</strong>
- 工具、ハードウェア、園芸用品、建築資材など多様な製品カタログ
- 店舗マネージャー、地域マネージャー、役員による多層管理体制

### ビジネス要件

店舗マネージャーと役員はAI搭載アナリティクスを必要としています：

1. 店舗ごとや期間ごとの<strong>販売パフォーマンス分析</strong>
2. <strong>在庫レベルの追跡</strong>と補充ニーズの特定
3. <strong>顧客行動</strong>や購買パターンの把握
4. セマンティック検索による<strong>製品洞察の発見</strong>
5. 自然言語クエリによる<strong>レポート生成</strong>
6. 役割ベースアクセス制御による<strong>データセキュリティの維持</strong>

### 技術要件

MCPサーバーは以下を提供しなければなりません：

- 店舗マネージャーが自店舗のデータのみ参照できる<strong>マルチテナントデータアクセス</strong>
- 複雑なSQL操作をサポートする<strong>柔軟なクエリ性能</strong>
- 製品発見と推奨のための<strong>セマンティック検索</strong>
- 現在のビジネス状態を反映する<strong>リアルタイムデータ</strong>
- 行レベルセキュリティによる<strong>安全な認証</strong>
- 複数同時ユーザーを支える<strong>拡張可能なアーキテクチャ</strong>

## 🏗️ MCPサーバーアーキテクチャ概要

当社のMCPサーバーは、データベース統合に最適化された層状アーキテクチャで構築されています：

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### キーコンポーネント

#### **1. MCPサーバーレイヤー**
- **FastMCPフレームワーク**：モダンなPythonベースのMCPサーバー実装
- <strong>ツール登録</strong>：型安全な宣言的ツール定義
- <strong>リクエストコンテキスト</strong>：ユーザー認証とセッション管理
- <strong>エラーハンドリング</strong>：堅牢なエラー管理とログ記録

#### **2. データベース統合レイヤー**
- <strong>接続プーリング</strong>：効率的なasyncpg接続管理
- <strong>スキーマプロバイダ</strong>：動的なテーブルスキーマ検出
- <strong>クエリエグゼキュータ</strong>：RLSコンテキストによる安全なSQL実行
- <strong>トランザクション管理</strong>：ACID準拠とロールバック処理

#### **3. セキュリティレイヤー**
- <strong>行レベルセキュリティ</strong>：PostgreSQL RLSによるマルチテナントデータ分離
- <strong>ユーザーアイデンティティ</strong>：店舗マネージャーの認証と認可
- <strong>アクセス制御</strong>：詳細な権限設定と監査ログ
- <strong>入力検証</strong>：SQLインジェクション防止とクエリ検証

#### **4. AI強化レイヤー**
- <strong>セマンティック検索</strong>：製品発見のためのベクトル埋め込み
- **Azure OpenAI統合**：テキスト埋め込み生成
- <strong>類似度アルゴリズム</strong>：pgvectorによるコサイン類似度検索
- <strong>検索最適化</strong>：インデックスとパフォーマンス調整

## 🔧 技術スタック

### コア技術

| <strong>コンポーネント</strong> | <strong>技術</strong> | <strong>目的</strong> |
|---------------|----------------|-------------|
| **MCPフレームワーク** | FastMCP (Python) | モダンなMCPサーバー実装 |
| <strong>データベース</strong> | PostgreSQL 17 + pgvector | 関係データとベクトル検索 |
| **AIサービス** | Azure OpenAI | テキスト埋め込みと言語モデル |
| <strong>コンテナ化</strong> | Docker + Docker Compose | 開発環境 |
| <strong>クラウドプラットフォーム</strong> | Microsoft Azure | 本番展開 |
| **IDE統合** | VS Code | AIチャットと開発ワークフロー |

### 開発ツール

| <strong>ツール</strong> | <strong>目的</strong> |
|----------|-------------|
| **asyncpg** | 高性能PostgreSQLドライバー |
| **Pydantic** | データ検証と直列化 |
| **Azure SDK** | クラウドサービス統合 |
| **pytest** | テストフレームワーク |
| **Docker** | コンテナ化とデプロイメント |

### 本番スタック

| <strong>サービス</strong> | **Azureリソース** | <strong>目的</strong> |
|-------------|-------------------|-------------|
| <strong>データベース</strong> | Azure Database for PostgreSQL | マネージドデータベースサービス |
| <strong>コンテナ</strong> | Azure Container Apps | サーバーレスコンテナホスティング |
| **AIサービス** | Microsoft Foundry | OpenAIモデルとエンドポイント |
| <strong>監視</strong> | Application Insights | 可観測性と診断 |
| <strong>セキュリティ</strong> | Azure Key Vault | シークレットと構成管理 |

## 🎬 実際の利用シナリオ

様々なユーザーがMCPサーバーとどのようにやり取りするかを見てみましょう：

### シナリオ1：店舗マネージャーのパフォーマンスレビュー

<strong>ユーザー</strong>：サラ、シアトル店舗マネージャー  
<strong>目標</strong>：前四半期の売上パフォーマンス分析

<strong>自然言語クエリ</strong>：
> "私の店舗の2024年第4四半期の売上トップ10の商品を見せて"

<strong>処理内容</strong>：
1. VS Code AIチャットがクエリをMCPサーバーに送信
2. MCPサーバーがサラの店舗コンテキスト（シアトル）を識別
3. RLSポリシーでシアトル店舗のデータのみフィルタリング
4. SQLクエリ生成と実行
5. 結果がフォーマットされAIチャットに返送
6. AIが分析と洞察を提供

### シナリオ2：セマンティック検索による製品発見

<strong>ユーザー</strong>：マイク、在庫管理マネージャー  
<strong>目標</strong>：顧客の要望に近い製品を見つける

<strong>自然言語クエリ</strong>：
> "『屋外用防水電気コネクタ』に似た製品は何がありますか？"

<strong>処理内容</strong>：
1. セマンティック検索ツールによるクエリ処理
2. Azure OpenAIが埋め込みベクターを生成
3. pgvectorが類似度検索を実行
4. 関連製品を関連度順にランキング
5. 結果に製品詳細と在庫状況を含む
6. AIが代替案とバンドル提案を提示

### シナリオ3：複数店舗間の分析

<strong>ユーザー</strong>：ジェニファー、地域マネージャー  
<strong>目標</strong>：すべての店舗のパフォーマンス比較

<strong>自然言語クエリ</strong>：
> "過去6か月間のすべての店舗のカテゴリ別売上を比較してください"

<strong>処理内容</strong>：
1. 地域マネージャーのRLSコンテキストを設定
2. 複雑なマルチストアクエリを生成
3. 店舗ロケーションをまたぐデータ集約
4. トレンドや比較結果を含めて返却
5. AIが洞察と推奨を特定

## 🔒 セキュリティとマルチテナンシーの詳細

実装はエンタープライズグレードのセキュリティを優先しています：

### 行レベルセキュリティ（RLS）

PostgreSQLのRLSがデータの分離を保証します：

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### ユーザーアイデンティティ管理

各MCP接続には以下が含まれます：
- **店舗マネージャーID**：RLSコンテキストのユニーク識別子
- <strong>役割割当</strong>：権限とアクセスレベル
- <strong>セッション管理</strong>：安全な認証トークン
- <strong>監査ログ</strong>：完全なアクセス履歴

### データ保護

複数のセキュリティ層：
- <strong>接続暗号化</strong>：すべてのデータベース接続にTLSを使用
- **SQLインジェクション防止**：パラメータ化クエリのみ
- <strong>入力検証</strong>：リクエストの包括的検証
- <strong>エラーハンドリング</strong>：エラーメッセージに機密情報なし

## 🎯 重要なポイント

この入門を終えた後、以下を理解しているはずです：

✅ **MCPの価値提案**：AIアシスタントと現実データを橋渡しする方法  
✅ <strong>ビジネスコンテキスト</strong>：Zava Retailの要件と課題  
✅ <strong>アーキテクチャ概要</strong>：主要コンポーネントとその相互作用  
✅ <strong>技術スタック</strong>：使用するツールとフレームワーク  
✅ <strong>セキュリティモデル</strong>：マルチテナントデータアクセスと保護  
✅ <strong>利用パターン</strong>：実際のクエリシナリオとワークフロー  

## 🚀 次のステップ

より深く学習する準備はできましたか？続けてください：

**[ラボ01：コアアーキテクチャコンセプト](../01-Architecture/README.md)**

MCPサーバーのアーキテクチャパターン、データベース設計原理、および小売分析ソリューションを支える詳細な技術実装について学びます。

## 📚 追加リソース

### MCPドキュメント
- [MCP仕様書](https://modelcontextprotocol.io/docs/) - 公式プロトコルドキュメント
- [MCP入門](https://aka.ms/mcp-for-beginners) - 包括的なMCP学習ガイド
- [FastMCPドキュメント](https://github.com/modelcontextprotocol/python-sdk) - Python SDKドキュメント

### データベース統合
- [PostgreSQLドキュメント](https://www.postgresql.org/docs/) - 完全なPostgreSQLリファレンス
- [pgvectorガイド](https://github.com/pgvector/pgvector) - ベクトル拡張ドキュメント
- [行レベルセキュリティ](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLSガイド

### Azureサービス
- [Azure OpenAIドキュメント](https://docs.microsoft.com/azure/cognitive-services/openai/) - AIサービス統合
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - マネージドデータベースサービス
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - サーバーレスコンテナ

---

<strong>免責事項</strong>：これは架空の小売データを用いた学習用演習です。本番環境で類似のソリューションを実装する際は、必ず組織のデータガバナンスとセキュリティポリシーに従ってください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
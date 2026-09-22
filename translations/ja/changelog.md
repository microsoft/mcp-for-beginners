# 変更履歴: 初心者向けMCPカリキュラム

この文書は、Model Context Protocol（MCP）初心者向けカリキュラムに行われた重要な変更をすべて記録するものです。変更は逆時系列（最新の変更が最初）で記録されています。

## 2026年9月9日

### MCP 2026-07-28 最終仕様調整

英語カリキュラムをリリース候補版および `2025-11-25`
ベースラインガイダンスから、最終MCP `2026-07-28`仕様へ更新しました。

- <strong>更新</strong>: 現行バージョンの参照、仕様リンク、ステートレスな
  リクエストガイダンス、`server/discover`、Streamable HTTPヘッダー、
  およびTasks拡張のライフサイクルを38の英語ドキュメントファイルで更新。
- <strong>修正</strong>: Elicitationは現在`elicitation/create`を使い、Samplingは
  `sampling/createMessage`を使い、`InputRequiredResult.resultType`は
  `"input_required"`を使うよう修正。
- <strong>置換</strong>: 不正確だったRoot Contextの会話状態レッスンを、
  情報ファイルシステムのヒント、現在の複数往復フロー、
  セキュリティ境界、移行オプションをカバーするプロトコル精度の高いRootsレッスンに置換。
- <strong>明確化</strong>: Roots、Sampling、Logging、Dynamic Client Registrationは
  `2026-07-28`で非推奨となり、推奨される代替手段や最早削除予定日を明示。
- <strong>ラベル付け</strong>: MCP `2025-11-25`、HTTP+SSE、初期化ハンドシェイク、
  またはプロトコルセッションに依存するサンプルは、
  現行実装ではなくレガシー互換性例として保持。
- <strong>セキュリティガイダンス</strong>: スタンドアロンのセキュリティガイドを
  リクエスト単位の認可と明示的なアプリケーション状態ハンドルを用い、
  削除されたプロトコルセッションIDの代わりに更新。Client ID Metadata Documentsが
  推奨登録経路となり、DCRは互換性向けのみに。
- <strong>補足資料</strong>: 学習ガイド、コントリビューターチェックリスト、
  Publoraケーススタディ、APIMケーススタディを更新。
  APIMウォークスルーは廃止された`/sse`ではなく
  現行のStreamable HTTP `/mcp`エンドポイントを推奨。
- **正規URL**: 英語のソースMarkdown中の廃止済みおよびドラフト仕様URLを
  バージョン付き`2026-07-28`リンクに置換、ただしサンプルが
  古いツールに固定されている場合はレガシーバージョンへの明示的リンクは残す。
- <strong>安定ファイル名</strong>: 最終仕様ガイドと2つのセキュリティガイドのリリース候補版および
  年付け接尾辞を除去し、全ての英語ハイパーリンクを安定パスに更新。
- <strong>新しい認可サンプル</strong>: テスト済みの
  [TypeScript MCP `2026-07-28`リソースサーバー](./02-Security/samples/cimd-dcr-auth/README.md)
  を追加。推奨のClient ID Metadata Documentsと廃止予定のDynamic
  Client Registrationフォールバックを比較。サンプルにはRFC 9728ディスカバリ、
  JWKS検証、ツールごとのスコープ、12のテスト、Auth0セットアップのウォークスルーが含まれる。
- <strong>翻訳範囲</strong>: 英語のソースファイルのみ編集し、生成された翻訳や翻訳済み画像は
  自動翻訳のため変更なし。






最終`2026-07-28`仕様に整合。


  2つのMermaid図、リトライ意思決定フローを用いて安定したオペレーションキー、
  原子重複受付、調整、証拠、およびTasks拡張の境界を説明。
- <strong>新</strong>: 標準ライブラリのPythonとSQLiteによる障害注入演習では
  別々のオペレーションストアとチケットストアを用い、
  外部効果のコミット後に応答を失うことを実証。6つの確定的テストで
  単純な重複、保護された再起動復旧、ペイロード競合、キャッシュ結果、
  アクティブクレーム、および同時重複受付をカバー。
- <strong>更新</strong>: モジュール08はコンパニオンレッスンへのリンクを追加し、
  最終`2026-07-28`ステートレスリクエストモデルを識別し、
  OpenTelemetryオブザーバビリティと非推奨のMCPロギング機能を区別し、
  一般的なリトライ例は読み取り専用操作に制限。
- <strong>オプション</strong>: レッスンは可搬概念を1つのタグ付きコミュニティ実装にマップし、
  ホストされたサービスやネットワークコールを演習の一部にはしない。

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md








  新しい`Mcp-Method`/`Mcp-Name`ルーティングヘッダー、`ttlMs`/`cacheScope`キャッシュメタデータ、

  6つの認可強化SEP、Roots/Sampling/Loggingの廃止、ツールスキーマの完全なるJSON Schema 2020-12移行をカバーする全レッスン。
- <strong>更新</strong>: 前向きな注意喚起として新レッスンへのリンクを追加:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): プロトコルバージョンの注記、Sampling/Roots/Logging/Tasksセクション、「次に何が起きるか」
  - [02-Security/README.md](./02-Security/README.md): 認可強化の注意喚起
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): ステートレストランスポートの注意喚起
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling廃止の注意喚起
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging廃止とTasks拡張の注意喚起

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): ステートレス/セッションルーティングの強調表示
  - [README.md](./README.md): 仕様セクションの「今後の展望」メモとカリキュラムモジュール表の新しい`1.1`エントリ
  - [study_guide.md](./study_guide.md): コアコンセプト概要の先を見据えた箇条書きと日付入り追補メモ
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): ステートレスリクエストモデルの前にある`mcp-session-id`トランスポートのマップの強調
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): ルートコンテキスト/サンプリングの非推奨化とタスク拡張に関するモジュール概要の強調表示
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): 認可強化に関する強調表示

## 2026年6月24日

### 新しいレッスン: CopilotアプリでのMCP使用方法

- [ツーリングセクション](./12-tooling/README.md) ツーリングセクションを追加しました。
- [CopilotアプリのMCP](./12-tooling/01-copilot-app/README.md)

## 2026年6月16日

### MCP仕様の整合およびサンプル検証

カリキュラムを現在の<strong>MCP Specification 2025-11-25</strong>および最新の公式SDKに対して検証し、残存していた古い仕様参照を修正、コアサンプルが正しくビルド・実行できることを確認しました。

#### 仕様バージョンの修正（2025-06-18 / 2025-03-26 → 2025-11-25）

古い仕様リビジョンが<em>現在の/最新の</em>基準であると記載していた英語部分を更新し、リンクを公式の`modelcontextprotocol.io`仕様パスに再指向しました：
- **05-AdvancedTopics/mcp-security/README.md**: 「Current Standard」バナー、イントロダクション、コアセキュリティ原則ヘッダー、必須要件ヘッダー、Microsoft Entra IDセクション、参考資料リンク、締めのセキュリティ注意喚起（8つの参照）を2025-11-25に更新
- **05-AdvancedTopics/mcp-transport/README.md**: 追加リソースの仕様リンクと「Current Standard」バナーを2025-11-25に更新
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: 古い`2025-03-26`のセキュリティ・トラストリンクを最新の2025-11-25のセキュリティベストプラクティスページに置き換え
- **03-GettingStarted/14-sampling/README.md**: 公式サンプリングドキュメントリンクを2025-11-25に更新
- **03-GettingStarted/05-stdio-server/README.md**: 現在形の「現行MCP仕様」参照および追加リソースの仕様リンクを2025-11-25に更新（正確性のため歴史的なSSE非推奨メモはそのまま）

#### 現行SDKに対するサンプル検証

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install`は`@modelcontextprotocol/sdk@1.29.0`を解決；`tsc --noEmit`は型エラー無く通過 — 既存の`McpServer`/`StdioServerTransport` APIは有効
- **Python (03-GettingStarted/01-first-server/solution/python)**: `.venv`環境で`mcp[cli]`(1.27.2)を使って検証；`py_compile`は成功、`FastMCP.list_tools()`は`add`と`subtract`ツールを正しく返しました
- すべてのサンプルの`@modelcontextprotocol/sdk`バージョン範囲（`>=1.26.0` / `^1.26.0` / `^1.27.0`）が破壊的なAPI変更なく現行の`1.29.0`に問題なく解決されることを確認済み

#### 依存関係ピンの整合（バージョンギャップの解消）

老朽化していたSDKのピンを最新のMCPリリースに合わせて全サンプルを更新、リポジトリ全体の規約に沿わせました：
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk`を`^1.8.0`から`>=1.26.0`に上げ、古くなっていた「MCP 2025-06-18用に更新済み」のパッケージ説明を「MCP Specification 2025-11-25に整合」に変更
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** と **lab4/code/github_mcp_server/pyproject.toml**: 正確ピン`mcp==1.23.0`を`mcp>=1.26.0`に上げ、両方の`uv.lock`ファイルを再生成（`uv lock`）し、ロックファイルが現行の`mcp 1.27.2`を解決し、マニフェストと同期状態を維持するようにしました

#### カリキュラムギャップ分析 — 最新仕様の機能カバー範囲

カリキュラムはすでにMCP 2025-11-25に導入/拡充されたすべてのプリミティブをカバーしているため、コンテンツにギャップはありません：
- **Sampling**: レッスン 03-GettingStarted/14-sampling および 05-AdvancedTopics/mcp-sampling
- **Elicitation (URLモード含む)**: 01-CoreConceptsおよび05-AdvancedTopics/mcp-protocol-featuresに記述
- **Roots**: 00-Introduction、01-CoreConcepts、および05-AdvancedTopics/mcp-root-contextsに記述
- **Tasks（実験的、長時間処理）**: 01-CoreConceptsおよび05-AdvancedTopics/mcp-protocol-featuresに記述
- <strong>ツール注釈</strong> (`readOnlyHint` / `destructiveHint`): 01-CoreConceptsおよび05-AdvancedTopics/mcp-protocol-featuresに記述

### セキュリティ強化と依存関係の脆弱性修正

すべての依存関係のマニフェストとサンプルソースコードに対する完全なセキュリティ検査を実施し、報告されたnpmアドバイザリと1件のコードレベルの問題を修正しました。修正後、`npm audit`はすべての検査ディレクトリで<strong>脆弱性なし</strong>を報告しています。

#### npm依存関係の脆弱性（間接依存） — 修正済み

コミットされた15の`package-lock.json`ファイルをすべて監査。脆弱性はMCP Inspectorの開発ツール、OpenAIクライアント、MCP SDKが引き込む間接依存に限定されていました。すべてサンプルに影響を与えず修正済みです。

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** と **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector`（`0.16.6` / `0.14.1` → `0.22.0`）を更新しました。これによりバンドルされていた `ajv`、`brace-expansion`、`diff`、`path-to-regexp`、`ws` のアドバイザリが解消されました。`concurrently` が持っていた残りのクリティカルなアドバイザリを排除するために、パッチ済みの `shell-quote@1.8.4` を強制する npm の `overrides` エントリを追加し、両方のロックファイルを再生成しました（現在脆弱性なし）
- **03-GettingStarted/samples/typescript**: `npm audit fix` によりトランジティブな `qs`（中程度）がパッチ済みリリースに更新されました
- **03-GettingStarted/samples/javascript**: `npm audit fix` によりトランジティブな `hono`（中程度）がパッチ済みリリースに更新されました
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` によりトランジティブな `form-data`（高リスク）がパッチ済みリリースに更新されました
- **03-GettingStarted/11-simple-auth/solution/typescript**: プロジェクトの再現性と監査可能性のため、欠落していた `package-lock.json` を生成しました（脆弱性なし）

#### コードレベルのセキュリティ修正（OWASP A03: インジェクション）

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` ツールから `shell=True` を削除しました。以前の `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` は `cmd.exe` によるフォルダパス内のシェルメタ文字の解釈を許しており（コマンドインジェクションの原因）、現在は解決された `Code.exe` をフォルダを引数として直接起動するように変更しました。シェルを介さず、機能的には同等で安全です

#### Python 依存関係監査

- すべての Python requirements セットを `pip-audit` で監査しました。`05-AdvancedTopics` と `03-GettingStarted/samples/python` は <strong>既知の脆弱性なし</strong> と報告されました（それらの `mcp` / `httpx` / `pydantic` / `python-dotenv` の範囲が現在のパッチ済みリリースに解決されています）
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` はトランジティブ依存の **`werkzeug` 3.1.1** に対して、3つの `safe_join` Windows デバイス名 DoS アドバイザリ — `CVE-2025-66221`、`CVE-2026-21860`、`CVE-2026-27199`（いずれも3.1.6で修正済み）を検出しました。パッチ済みリリースが解決されるように明示的なセキュリティピン `werkzeug>=3.1.6` を追加し、`chainlit` / `mcp` / `semantic-kernel` スタックで制約が正常に解決されることを検証しました

### 製品名のリブランディング

Microsoft の製品リブランディングを反映するためにすべてのカリキュラムコンテンツを更新しました：

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord コミュニティリンクを更新
- **AGENTS.md**: Discord サーバー参照を更新
- **README.md**: 技術エコシステム参照を更新
- **study_guide.md**: ケーススタディ参照を更新
- **05-AdvancedTopics/README.md**: モジュール5.13のタイトルと説明を更新
- **05-AdvancedTopics/mcp-integration/README.md**: セクションヘッダーと説明を更新
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: モジュール全タイトルと内容を更新
- **05-AdvancedTopics/mcp-security-entra/README.md**: クロスリファレンスリンクを更新
- **07-LessonsfromEarlyAdoption/README.md**: ケーススタディ参照を更新
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: セクション9ヘッダー、バッジ、機能を更新
- **08-BestPractices/README.md**: Discord コミュニティリンクを更新
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discord チャンネル参照を更新
- **09-CaseStudy/docs-mcp/solution/python/README.md**: モデルデプロイメント参照を更新
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI サービス表を更新
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: リソース参照を更新

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: メインカリキュラム参照を更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: モジュールタイトル、概要、およびすべてのモジュールヘッダーを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: タイトル、学習目標、セットアップ手順、リソースを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: タイトル、学習目標、MCP ホストテーブル、およびクロスリファレンスを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: タイトル、バッジ、前提条件、リソースを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: エージェントビルダーの参照とフィードバックリンクを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: 前提条件と拡張機能参照を更新

---

## 2026年4月11日

### 新しいレッスン、ドキュメント修正、および依存関係の更新

#### 新しいカリキュラムコンテンツの追加

**モジュール 05 - 高度なトピック**
- **レッスン 5.17: MCPを用いた対立型マルチエージェント推論** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): マルチエージェントシステム向け対立議論パターンを包括的に解説する新しいガイド
  - Mermaid アーキテクチャ図：二人のエージェント → 共有の MCP サーバー → 討論記録 → ジャッジ → 判定
  - 共有 MCP ツールサーバー（`web_search` + `run_python`）は Python と TypeScript で実装
  - 対立するシステムプロンプト（賛成 / 反対 / ジャッジ）と明示的なツール使用要件
  - Python、TypeScript、および C# で書かれた討論オーケストレーターがラウンドと議論を管理
  - オーケストレーター向け MCP `ClientSession` のワイヤリングによりリアルなツール呼び出しを実現
  - 利用ケース表（幻覚検出、脅威モデリング、API設計レビュー、事実検証、技術選定）
  - セキュリティ考慮事項：サンドボックス実行、ツール呼び出し検証、レート制限、監査ログ
  - 3つの実践的シナリオを含む構造化演習（コードレビュー、アーキテクチャ決定、コンテンツモデレーション）

#### ドキュメント修正

**モジュール 03 - はじめに**
- **05-stdio-server/README.md**: 不完全だった TypeScript stdio サーバーの例を修正 — 不足していたトランスポートのインスタンス化（`new StdioServerTransport()`）と、Python および .NET の同セクション例に合わせた `server.connect(transport)` 呼び出しを追加
- **14-sampling/README.md**: タイポ修正 — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### カリキュラム更新

**メイン README.md**
- カリキュラム表にエントリー 5.17（MCPを用いた対立型マルチエージェント推論）を追加し、新しいレッスンへの直接リンクを設定

**05-AdvancedTopics/README.md**
- レッスン表にレッスン 5.17 の行を追加

**study_guide.md**
- 高度なトピックのマインドマップと文章説明に対立型マルチエージェント推論トピックを追加

#### コードとセキュリティの修正

**モジュール 05 - 対立型エージェント (`mcp-adversarial-agents`)**
- **セキュリティ修正 — コマンドインジェクション**: TypeScript `run_python` ツールで `execSync` のシェルインターポレーションを `execFile` + `promisify` に置き換え、コマンドインジェクションの可能性を排除（LLM制御のコードはシェルを介さずリテラルな argv 要素として渡される）
- **MCPツールループのワイヤリング**: Python の討論オーケストレーターをアップデートし、`AsyncAnthropic` クライアントを使用（ブロッキングな同期 `Anthropic` を置換）、ライブな `ClientSession` を各エージェントターンに直接渡し、各ターンで `session.list_tools()` でツール定義を取得、モデルが最終テキストレスポンスを出すまでループで `session.call_tool()` で `tool_use` ブロックをディスパッチ

#### 依存関係の更新

- 複数パッケージ（03-GettingStarted、04-PracticalImplementation、10-StreamliningAIWorkflows）で `hono` を 4.12.12 に更新
- TypeScript パッケージで `@hono/node-server` を 1.19.11 から 1.19.13 に更新
- Python パッケージ（10-StreamliningAIWorkflows ラボ3と4）で `cryptography` を 46.0.5 から 46.0.7 に更新
- 10-StreamliningAIWorkflows インスペクターで `lodash` を 4.17.23 から 4.18.1 に更新

#### 翻訳

- 48以上の言語で最新のソース変更に合わせて翻訳を同期（i18n アップデート）

---

## 2026年2月5日

### リポジトリ全体の検証とナビゲーション改善

#### 新しいカリキュラムコンテンツ追加

**モジュール 03 - はじめに**
- **12-mcp-hosts/README.md**: MCP ホスト設定のための新しい包括的ガイド
  - Claude Desktop、VS Code、Cursor、Cline、Windsurf の設定例
  - 主なホスト用の JSON 設定テンプレート
  - トランスポートタイプ比較表（stdio、SSE/HTTP、WebSocket）
  - 一般的な接続問題のトラブルシューティング
  - ホスト設定のセキュリティベストプラクティス

- **13-mcp-inspector/README.md**: MCP インスペクター用の新しいデバッグガイド
  - インストール方法（npx、npm グローバル、ソースから）
  - stdio および HTTP/SSE 経由でのサーバー接続
  - テストツール、リソース、およびプロンプトワークフロー
  - VS Code と MCP インスペクターの統合
  - よくあるデバッグシナリオと解決策

**モジュール 04 - 実践的実装**
- **pagination/README.md**: 新しいページネーション実装ガイド
  - Python、TypeScript、Java におけるカーサー型ページネーションパターン
  - クライアント側のページネーション処理
  - カーサーデザイン戦略（不透明 vs 構造化）
  - パフォーマンス最適化の推奨事項

**モジュール 05 - 高度なトピック**
- **mcp-protocol-features/README.md**: 新しいプロトコル機能の詳細解説
  - 進捗通知の実装
  - リクエストキャンセルパターン
  - URI パターンによるリソーステンプレート
  - サーバーのライフサイクル管理
  - ロギングレベルの制御
  - JSON-RPC コードによるエラーハンドリングパターン

#### ナビゲーション修正（24以上のファイル更新）

**主要モジュール README**
 先頭レッスンへのリンクと次モジュールへのリンクの両方を追加

**02-Security サブファイル**
- すべての5つの補助セキュリティ文書に「What's Next」ナビゲーションを追加

**09-CaseStudy ファイル**
- すべてのケーススタディファイルに連続的なナビゲーションを追加

**10-StreamliningAI ラボ**
モジュール10の概要とモジュール11に「What's Next」セクションを追加

#### コードおよびコンテンツ修正

**SDKおよび依存関係の更新**
空の openai バージョンを `^4.95.0` に修正
SDK を `^1.8.0` から `>=1.26.0` に更新
mcp バージョンピンを `>=1.26.0` に更新

<strong>コード修正</strong>
無効なモデル `gpt-4o-mini` を `gpt-4.1-mini` に修正

<strong>コンテンツ修正</strong>
壊れたリンク `READMEmd` → `README.md` を修正、カリキュラムヘッダー `Module 1-3` → `Module 0-3` を修正、大文字小文字区別のあるパスを修正
壊れたケーススタディ5の重複コンテンツを削除

<strong>初心者向けガイダンスの改善</strong>
正しい導入、学習目標、および前提条件を初心者向けに追加

#### カリキュラム更新

**メイン README.md**
- カリキュラム表に 3.12（MCP ホスト）、3.13（MCP インスペクター）、4.1（ページネーション）、5.16（プロトコル機能）を追加

**モジュール README**
レッスン12と13をレッスンリストに追加
ページネーションリンク付きの実践ガイドセクションを追加
レッスン5.15（カスタムトランスポート）と5.16（プロトコル機能）を追加

**study_guide.md**
- MCP ホスト設定、MCP インスペクター、ページネーション戦略、プロトコル機能の詳細を含むすべての新トピックでマインドマップを更新

## 2026年1月28日

### MCP 仕様 2025-11-25 コンプライアンスレビュー

#### コアコンセプト強化（01-CoreConcepts/）
- **新しいクライアントプリミティブ - Roots**: サーバーがファイルシステムの境界とアクセス権限を理解できるようにする Roots クライアントプリミティブに関する包括的ドキュメントを追加
- <strong>ツール注釈</strong>: より良いツール実行判断のためのツールの振る舞い注釈（`readOnlyHint`、`destructiveHint`）に関するドキュメントを追加
- <strong>サンプリング中のツール呼び出し</strong>: サンプリングドキュメントに、サンプリングリクエスト中のモデル駆動ツール呼び出し用パラメータ `tools` と `toolChoice` を追加
- **URL モード誘発**: サーバー主導の外部ウェブ操作のための URL ベース誘発に関するドキュメントを追加
- **タスク（実験的）**: 耐久実行ラッパーおよび遅延結果取得用の実験的タスク機能に関する新しいセクションを追加

- <strong>アイコンサポート</strong>: ツール、リソース、リソーステンプレート、およびプロンプトが追加のメタデータとしてアイコンを含められるようになったことを記載

#### ドキュメントの更新
- **README.md**: MCP仕様 2025-11-25 バージョンの参照および日付ベースのバージョニング説明を追加
- **study_guide.md**: コアコンセプトセクションにタスクとツール注釈を含めるようにカリキュラムマップを更新；ドキュメントのタイムスタンプを更新

#### 仕様準拠の検証
- <strong>プロトコルバージョン</strong>: すべてのドキュメントが現在のMCP仕様 2025-11-25を参照していることを確認
- <strong>アーキテクチャの整合性</strong>: 2層アーキテクチャ（データレイヤー＋トランスポートレイヤー）のドキュメントの正確さを確認
- <strong>プリミティブのドキュメント</strong>: サーバープリミティブ（リソース、プロンプト、ツール）およびクライアントプリミティブ（サンプリング、誘導、ロギング、ルーツ）を検証
- <strong>トランスポートメカニズム</strong>: STDIOおよびストリーミングHTTPトランスポートのドキュメントの正確さを検証
- <strong>セキュリティガイダンス</strong>: 現行のMCPセキュリティベストプラクティスドキュメントとの整合性を確認

#### キーMCP 2025-11-25 機能の文書化
- **OpenID Connect Discovery**: OIDCを介した認証サーバーのディスカバリ
- **OAuthクライアントIDメタデータドキュメント**: 推奨されるクライアント登録メカニズム
- **JSON Schema 2020-12**: MCPスキーマ定義のデフォルト方言
- **SDKティアリングシステム**: SDK機能サポートおよびメンテナンスに関する正式な要件
- <strong>ガバナンス構造</strong>: MCPガバナンスでの作業グループおよび関心グループの正式化

### セキュリティドキュメントの大幅な更新 (02-Security/)

#### MCPセキュリティサミットワークショップ（Sherpa）統合
- <strong>新しいハンズオン研修リソース</strong>: [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) との包括的な統合をすべてのセキュリティドキュメントに追加
- <strong>遠征ルートのカバレッジ</strong>: ベースキャンプからサミットまでの完全なキャンプ間進行を文書化
- **OWASPとの整合性**: すべてのセキュリティガイダンスがOWASP MCP Azure Security Guideのリスクにマッピングされるように更新

#### OWASP MCP Top 10統合
- <strong>新セクション</strong>: Azureの軽減策付きOWASP MCP Top 10セキュリティリスク表をメインのSecurity READMEに追加
- <strong>リスクベースドドキュメント</strong>: 各セキュリティドメインのOWASP MCPリスク参照を含めてmcp-security-controls-2025.mdを更新
- <strong>リファレンスアーキテクチャ</strong>: OWASP MCP Azure Security Guideのリファレンスアーキテクチャおよび実装パターンへのリンクを追加

#### 更新されたセキュリティファイル
- **README.md**: Sherpaワークショップの概要、遠征ルート表、OWASP MCP Top 10リスク概要、およびハンズオン研修セクションを追加
- **mcp-security-controls-2025.md**: ヘッダーを2026年2月に更新、OWASPリスク参照（MCP01-MCP08）を追加、仕様バージョンの不一致を修正
- **mcp-security-best-practices-2025.md**: SherpaおよびOWASPリソースセクションを追加し、タイムスタンプを更新
- **mcp-best-practices.md**: SherpaおよびOWASPリンク付きのハンズオン研修セクションを追加
- **azure-content-safety-implementation.md**: OWASP MCP06参照、Sherpaキャンプ3整合、および追加リソースセクションを追加

#### 新規リソースリンク追加
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- OWASP MCP各リスクページ（MCP01-MCP10）

### カリキュラム全面でのMCP仕様 2025-11-25 対応

#### モジュール03 - 入門
- **SDKドキュメンテーション**: Go SDKを公式SDKリストに追加；すべてのSDK参照をMCP仕様 2025-11-25に合わせて更新
- <strong>トランスポートの明確化</strong>: STDIOおよびHTTPストリーミングトランスポートの説明に明示的な仕様参照を追加

#### モジュール04 - 実践的実装
- **SDK更新**: Go SDK追加；SDKリストを仕様バージョン参照付きで更新
- <strong>認可仕様</strong>: MCP認可仕様リンクを現行の2025-11-25バージョンに更新

#### モジュール05 - 高度なトピック
- <strong>新機能</strong>: MCP仕様 2025-11-25 の新機能（タスク、ツール注釈、URLモードの誘導、ルーツ）についての注記を追加
- <strong>セキュリティリソース</strong>: OWASP MCP Top 10およびSherpaワークショップリンクを追加の参考資料として追加

#### モジュール06 - コミュニティ貢献
- **SDKリスト**: SwiftおよびRust SDKを追加；仕様リンクを2025-11-25に更新
- <strong>仕様参照</strong>: MCP仕様リンクを直接仕様URLに更新

#### モジュール07 - 早期採用からの教訓
- <strong>リソース更新</strong>: MCP仕様 2025-11-25 へのリンクとOWASP MCP Top 10を追加リソースに追加

#### モジュール08 - ベストプラクティス
- <strong>仕様バージョン</strong>: MCP仕様参照を2025-11-25に更新
- <strong>セキュリティリソース</strong>: OWASP MCP Top 10とSherpaワークショップを追加リファレンスに追加

#### モジュール10 - AIワークフローの効率化
- <strong>バッジ更新</strong>: MCPバージョンバッジをSDKバージョン（1.9.3）から仕様バージョン（2025-11-25）に変更
- <strong>リソースリンク</strong>: MCP仕様リンクを更新；OWASP MCP Top 10を追加

#### モジュール11 - MCPサーバーハンズオンラボ
- <strong>仕様参照</strong>: MCP仕様リンクを2025-11-25バージョンに更新
- <strong>セキュリティリソース</strong>: 正式なリソースにOWASP MCP Top 10を追加

## 2025年12月18日

### セキュリティドキュメント更新 - MCP仕様 2025-11-25

#### MCPセキュリティベストプラクティス (02-Security/mcp-best-practices.md) - 仕様バージョンの更新
- <strong>プロトコルバージョン更新</strong>: 最新MCP仕様 2025-11-25（2025年11月25日リリース）を参照するように更新
  - すべての仕様バージョン参照を2025-06-18から2025-11-25に更新
  - 文書の日付参照を2025年8月18日から2025年12月18日に更新
  - すべての仕様URLが現在のドキュメントを指していることを確認
- <strong>コンテンツ検証</strong>: 最新標準に対するセキュリティベストプラクティスの包括的な検証
  - **Microsoftセキュリティソリューション**: Prompt Shields（旧「Jailbreakリスク検出」）、Azure Content Safety、Microsoft Entra ID、Azure Key Vaultの現在の用語とリンクを検証
  - **OAuth 2.1セキュリティ**: 最新のOAuthセキュリティベストプラクティスとの整合性を確認
  - **OWASP標準**: LLM向けOWASP Top 10の参照が最新であることを検証
  - **Azureサービス**: すべてのMicrosoft Azureドキュメントリンクとベストプラクティスを確認
- <strong>標準準拠</strong>: 参照されたすべてのセキュリティ標準が最新であることを確認
  - NIST AIリスク管理フレームワーク
  - ISO 27001:2022
  - OAuth 2.1セキュリティベストプラクティス
  - Azure セキュリティおよびコンプライアンスフレームワーク
- <strong>実装リソース</strong>: すべての実装ガイドリンクとリソースを検証
  - Azure API Management認証パターン
  - Microsoft Entra ID統合ガイド
  - Azure Key Vaultのシークレット管理
  - DevSecOpsパイプラインおよび監視ソリューション

### ドキュメント品質保証
- <strong>仕様準拠</strong>: すべての必須MCPセキュリティ要件（MUST/MUST NOT）が最新仕様に対応していることを確認
- <strong>リソースの最新性</strong>: Microsoftドキュメント、セキュリティ標準、および実装ガイドへのすべての外部リンクを検証
- <strong>ベストプラクティスのカバレッジ</strong>: 認証、認可、AI固有の脅威、サプライチェーンセキュリティ、企業パターンの包括的なカバレッジを確認

## 2025年10月6日

### 入門セクションの拡張 – 高度なサーバー使用法＆シンプル認証

#### 高度なサーバー使用法 (03-GettingStarted/10-advanced)
- <strong>新章追加</strong>: 通常サーバーと低レベルサーバーアーキテクチャの両方をカバーする高度なMCPサーバー使用法の包括的ガイドを導入
  - <strong>通常サーバーと低レベルサーバーの比較</strong>: 両アプローチの詳細な比較とPythonおよびTypeScriptのコード例
  - <strong>ハンドラベースデザイン</strong>: 拡張性と柔軟性のあるサーバー実装のためのハンドラベースのツール/リソース/プロンプト管理の説明
  - <strong>実践的パターン</strong>: 高度な機能とアーキテクチャのために低レベルサーバーパターンが役立つ実際のシナリオ

#### シンプル認証 (03-GettingStarted/11-simple-auth)
- <strong>新章追加</strong>: MCPサーバーにおけるシンプル認証の実装手順ガイド
  - <strong>認証概念</strong>: 認証と認可、および認証情報の取り扱いの明確な説明
  - <strong>基本認証の実装</strong>: Python（Starlette）およびTypeScript（Express）によるミドルウェアベースの認証パターンとコード例
  - <strong>高度なセキュリティへの進展</strong>: シンプル認証からOAuth 2.1およびRBACへの移行ガイド、および高度なセキュリティモジュールへの参照

これらの追加は、基礎概念と高度な本番パターンを橋渡しし、より堅牢で安全かつ柔軟なMCPサーバー実装の構築に実践的なハンズオンガイダンスを提供します。

## 2025年9月29日

### MCPサーバーデータベース統合ラボ - 包括的ハンズオン学習パス

#### 11-MCPServerHandsOnLabs - 新しい完全なデータベース統合カリキュラム
- **完全な13ラボ学習パス**: PostgreSQLデータベース統合による本番レディなMCPサーバー構築の包括的ハンズオンカリキュラムを追加
  - <strong>実際の実装</strong>: エンタープライズ級パターンを示すZava Retail分析のユースケース
  - <strong>構造化された学習進行</strong>:
    - **ラボ 00-03: 基礎** - 入門、コアアーキテクチャ、セキュリティ＆マルチテナンシー、環境セットアップ
    - **ラボ 04-06: MCPサーバー構築** - データベース設計＆スキーマ、MCPサーバー実装、ツール開発
    - **ラボ 07-09: 高度な機能** - セマンティック検索統合、テスト＆デバッグ、VS Code統合
    - **ラボ 10-12: 本番運用＆ベストプラクティス** - デプロイ戦略、モニタリング＆可観測性、ベストプラクティス＆最適化
  - <strong>エンタープライズ技術</strong>: FastMCPフレームワーク、pgvector付きPostgreSQL、Azure OpenAI埋め込み、Azure Container Apps、Application Insights
  - <strong>高度機能</strong>: 行レベルセキュリティ（RLS）、セマンティック検索、マルチテナントデータアクセス、ベクトル埋め込み、リアルタイムモニタリング

#### 用語標準化 - モジュールからラボへの名称変更
- <strong>包括的なドキュメント更新</strong>: 11-MCPServerHandsOnLabsの全READMEファイルを体系的に更新し、「モジュール」ではなく「ラボ」用語を使用
  - <strong>セクションヘッダー</strong>: 13ラボすべてで「このモジュールがカバーする内容」を「このラボがカバーする内容」に更新
  - <strong>コンテンツ説明</strong>: ドキュメント全体で「このモジュールは提供する…」を「このラボは提供する…」に変更
  - <strong>学習目標</strong>: 「このモジュールの終了時に…」を「このラボの終了時に…」に更新
  - <strong>ナビゲーションリンク</strong>: すべての「モジュールXX:」の参照をクロスリファレンスおよびナビゲーションで「ラボXX:」に変換
  - <strong>完了追跡</strong>: 「このモジュールを完了後…」を「このラボを完了後…」に更新
  - <strong>技術的参照保持</strong>: 設定ファイル内のPythonモジュール参照（例: `"module": "mcp_server.main"`）は維持

#### スタディガイド強化 (study_guide.md)
- <strong>ビジュアルカリキュラムマップ</strong>: 包括的なラボ構成の可視化を伴う新しい「11. データベース統合ラボ」セクションを追加
- <strong>リポジトリ構造</strong>: 10から11の主要セクションに更新し、11-MCPServerHandsOnLabsの詳細説明を追加
- <strong>学習パスの案内</strong>: セクション00-11をカバーするナビゲーション指示を強化
- <strong>技術カバレッジ</strong>: FastMCP、PostgreSQL、Azureサービス統合の詳細を追加
- <strong>学習成果</strong>: 本番対応のサーバー開発、データベース統合パターン、およびエンタープライズセキュリティを強調

#### メインREADME構造の強化
- <strong>ラボベース用語</strong>: 11-MCPServerHandsOnLabsのメインREADME.mdを一貫して「ラボ」構造を使用するように更新
- <strong>学習パスの組織化</strong>: 基礎概念から高度な実装、そして本番展開までの明確な進行
- <strong>実践的焦点</strong>: エンタープライズ級パターンと技術を伴う実践的ハンズオン学習を強調

### ドキュメントの品質と一貫性の改善
- <strong>ハンズオン学習の強調</strong>: ドキュメント全体に実践的でラボベースのアプローチを強化
- <strong>エンタープライズパターンの焦点</strong>: 本番対応実装とエンタープライズセキュリティ考慮事項を強調
- <strong>技術統合</strong>: 最新のAzureサービスとAI統合パターンを包括的にカバー
- <strong>学習進行</strong>: 基礎概念から本番展開までの明確で構造化されたパス

## 2025年9月26日

### ケーススタディ強化 - GitHub MCP Registry統合

#### ケーススタディ (09-CaseStudy/) - エコシステム開発の焦点
- **README.md**: GitHub MCP Registryケーススタディによる大幅な拡張
  - **GitHub MCP Registryケーススタディ**: 2025年9月のGitHub MCP Registryローンチを詳細に分析した新しいケーススタディ
    - <strong>問題の分析</strong>: 断片化されたMCPサーバーの検出とデプロイメント課題を詳細に検討
    - <strong>解決策のアーキテクチャ</strong>: GitHubの集中型レジストリアプローチとワンクリックVS Codeインストール
    - <strong>ビジネスインパクト</strong>: 開発者のオンボーディングと生産性の測定可能な向上
    - <strong>戦略的価値</strong>: モジュラーエージェント展開とツール間相互運用性に注力
    - <strong>エコシステム開発</strong>: エージェント統合の基盤となるプラットフォームとしての位置付け
  - <strong>強化されたケーススタディ構造</strong>: 7つのケーススタディすべてを一貫したフォーマットと包括的な説明で更新
    - Azure AIトラベルエージェント: マルチエージェントオーケストレーションの強調
    - Azure DevOps統合: ワークフロー自動化の焦点
    - リアルタイムドキュメント取得: Pythonコンソールクライアントの実装
    - インタラクティブ学習プラン生成器: Chainlit会話型Webアプリ

    - エディター内ドキュメント：VS CodeとGitHub Copilotの統合
    - Azure API管理：エンタープライズAPI統合パターン
    - GitHub MCPレジストリ：エコシステム開発およびコミュニティプラットフォーム
  - <strong>総合的な結論</strong>：複数のMCP実装次元を跨ぐ7つのケーススタディを強調した結論セクションの書き換え
    - エンタープライズ統合、マルチエージェントオーケストレーション、開発者生産性
    - エコシステム開発、教育応用のカテゴリ分類
    - アーキテクチャパターン、実装戦略、およびベストプラクティスへの洞察強化
    - MCPを成熟した本番環境対応プロトコルとして強調

#### スタディガイドの更新 (study_guide.md)
- <strong>ビジュアルカリキュラムマップ</strong>：ケーススタディのセクションにGitHub MCPレジストリを含むマインドマップを更新
- <strong>ケーススタディの説明</strong>：一般的な説明から7つの包括的ケーススタディの詳細な内訳に強化
- <strong>リポジトリ構造</strong>：特定の実装詳細を含む包括的ケーススタディのカバレッジを反映するためセクション10を更新
- <strong>変更履歴の統合</strong>：2025年9月26日のエントリを追加し、GitHub MCPレジストリの追加とケーススタディの強化を記録
- <strong>日付更新</strong>：最新リビジョン（2025年9月26日）を反映するためフッターのタイムスタンプを更新

### ドキュメント品質の改善
- <strong>一貫性の向上</strong>：7つのすべての例でケーススタディのフォーマットと構成を標準化
- <strong>包括的カバレッジ</strong>：ケーススタディはエンタープライズ、生産性、エコシステム開発のシナリオにまたがる
- <strong>戦略的ポジショニング</strong>：エージェントシステム展開の基盤プラットフォームとしてのMCPの強調
- <strong>リソース統合</strong>：追加リソースを更新しGitHub MCPレジストリへのリンクを含む

## 2025年9月15日

### 高度なトピック拡張 - カスタムトランスポート & コンテキストエンジニアリング

#### MCPカスタムトランスポート (05-AdvancedTopics/mcp-transport/) - 新しい高度実装ガイド
- **README.md**：カスタムMCPトランスポート機構の完全な実装ガイド
  - **Azure Event Gridトランスポート**：包括的なサーバーレスイベント駆動トランスポート実装
    - C#, TypeScript, Pythonの例とAzure Functions統合
    - 拡張可能なMCPソリューションのイベント駆動型アーキテクチャパターン
    - Webhook受信およびプッシュベースのメッセージ処理
  - **Azure Event Hubsトランスポート**：高スループットストリーミングトランスポート実装
    - 低遅延シナリオ向けのリアルタイムストリーミング機能
    - パーティショニング戦略とチェックポイント管理
    - メッセージバッチ処理とパフォーマンス最適化
  - <strong>エンタープライズ統合パターン</strong>：本番環境対応のアーキテクチャ例
    - 複数のAzure Functionsに分散したMCP処理
    - 複数トランスポートタイプを組み合わせたハイブリッドアーキテクチャ
    - メッセージ耐久性、信頼性、およびエラーハンドリング戦略
  - <strong>セキュリティと監視</strong>：Azure Key Vault統合および可観測性パターン
    - マネージドID認証と最小権限アクセス
    - Application Insightsのテレメトリとパフォーマンス監視
    - サーキットブレーカーとフォールトトレランスパターン
  - <strong>テストフレームワーク</strong>：カスタムトランスポート向けの包括的テスト戦略
    - テストダブルおよびモッキングフレームワークによるユニットテスト
    - Azure Test Containersによる統合テスト
    - パフォーマンスおよび負荷テストの考慮事項

#### コンテキストエンジニアリング (05-AdvancedTopics/mcp-contextengineering/) - 新興AI分野
- **README.md**：新興分野としてのコンテキストエンジニアリングの包括的探究
  - <strong>コア原則</strong>：完全なコンテキスト共有、行動決定の認識、コンテキストウィンドウ管理
  - **MCPプロトコル整合**：MCP設計がコンテキストエンジニアリングの課題に対応する方法
    - コンテキストウィンドウの制限と漸進的読み込み戦略
    - 関連性判定と動的コンテキスト取得
    - マルチモーダルコンテキスト処理とセキュリティ考慮
  - <strong>実装アプローチ</strong>：シングルスレッド対マルチエージェントアーキテクチャ
    - コンテキストチャンク化および優先順位付け技法
    - 漸進的コンテキスト読み込みと圧縮戦略
    - 階層的コンテキストアプローチと取得最適化
  - <strong>評価フレームワーク</strong>：コンテキスト有効性評価の新興メトリクス
    - 入力効率、パフォーマンス、品質、およびユーザー体験の考慮
    - コンテキスト最適化の実験的アプローチ
    - 失敗分析と改善方法論

#### カリキュラムナビゲーションの更新 (README.md)
- <strong>強化されたモジュール構成</strong>：新しい高度トピックを含めるためカリキュラムテーブルを更新
  - コンテキストエンジニアリング（5.14）とカスタムトランスポート（5.15）を追加
  - すべてのモジュールにおける一貫した書式とナビゲーションリンク
  - 現在のコンテンツ範囲を反映する説明の更新

### ディレクトリ構造の改善
- <strong>命名の標準化</strong>：「mcp transport」を他の高度トピックフォルダとの一貫性のために「mcp-transport」に改名
- <strong>コンテンツ構成</strong>：すべての05-AdvancedTopicsフォルダは現在一貫した命名パターン（mcp-[トピック]）に従う

### ドキュメント品質の向上
- **MCP仕様整合**：すべての新規コンテンツは現在のMCP仕様2025-06-18を参照
- <strong>多言語例</strong>：C#, TypeScript, Pythonでの包括的なコード例
- <strong>エンタープライズフォーカス</strong>：本番対応パターンとAzureクラウド統合を全体にわたって
- <strong>ビジュアルドキュメント</strong>：アーキテクチャとフローの可視化のためのMermaid図

## 2025年8月18日

### ドキュメント包括的アップデート - MCP 2025-06-18標準

#### MCPセキュリティベストプラクティス (02-Security/) - 完全な近代化
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：MCP仕様2025-06-18に合わせた完全な書き換え
  - <strong>必須要件</strong>：公式仕様からの明示的なMUST/MUST NOT要件を視覚的に明確に追加
  - **12のコアセキュリティプラクティス**：15項目リストから包括的なセキュリティドメインに再構成
    - 外部IDプロバイダー統合を含むトークンセキュリティと認証
    - 暗号要件を含むセッション管理とトランスポートセキュリティ
    - Microsoft Prompt Shields統合を含むAI特有の脅威保護
    - 最小権限の原則に基づくアクセス制御と権限管理
    - Azure Content Safety統合を含むコンテンツの安全性と監視
    - 包括的なコンポーネント検証を含むサプライチェーンセキュリティ
    - PKCE実装によるOAuthセキュリティと混乱を防ぐ代理攻撃防止
    - 自動化機能を含むインシデント対応と復旧
    - 規制整合を含むコンプライアンスとガバナンス
    - ゼロトラストアーキテクチャを含む高度なセキュリティ制御
    - 包括的なソリューションを含むMicrosoftセキュリティエコシステム統合
    - 適応的プラクティスによる継続的なセキュリティ進化
  - **Microsoftセキュリティソリューション**：Prompt Shields、Azure Content Safety、Entra ID、GitHub Advanced Securityの統合ガイダンス強化
  - <strong>実装リソース</strong>：公式MCPドキュメント、Microsoftセキュリティソリューション、セキュリティ標準、実装ガイドによる体系的リンク集

#### 高度なセキュリティ制御 (02-Security/) - エンタープライズ実装
- **MCP-SECURITY-CONTROLS-2025.md**：企業レベルのセキュリティフレームワークを備えた完全なオーバーホール
  - **9つの包括的セキュリティドメイン**：基本制御から詳細な企業フレームワークへ拡大
    - Microsoft Entra ID統合による高度な認証と承認
    - 包括的検証を含むトークンセキュリティと不正経路制御
    - ハイジャック防止を含むセッションセキュリティ制御
    - プロンプトインジェクションおよびツールポイズニング防止を含むAI特有のセキュリティ制御
    - OAuthプロキシセキュリティを含む混乱を招く代理攻撃防止
    - サンドボックス化と分離を含むツール実行セキュリティ
    - 依存関係検証を含むサプライチェーンセキュリティ制御
    - SIEM統合を含む監視と検出制御
    - 自動化機能を含むインシデント対応と復旧
  - <strong>実装例</strong>：詳細なYAML設定ブロックとコード例を追加
  - **Microsoftソリューション統合**：Azureセキュリティサービス、GitHub Advanced Security、企業アイデンティティ管理の包括的カバー

#### 高度トピックセキュリティ (05-AdvancedTopics/mcp-security/) - 本番対応実装
- **README.md**：企業向けセキュリティ実装のための完全な書き換え
  - <strong>現行仕様整合</strong>：必須セキュリティ要件を含むMCP仕様2025-06-18に更新
  - <strong>強化された認証</strong>：Microsoft Entra ID統合および包括的な.NET、Java Spring Securityの例
  - **AIセキュリティ統合**：Microsoft Prompt Shields、Azure Content Safetyの実装と詳細なPython例
  - <strong>高度な脅威緩和</strong>：包括的な実装例
    - PKCEおよびユーザー同意検証を使用した混乱を招く代理攻撃防止
    - オーディエンス検証および安全なトークン管理によるトークン不正利用防止
    - 暗号的結合および行動分析を伴うセッションハイジャック防止
  - <strong>企業セキュリティ統合</strong>：Azure Application Insights監視、脅威検出パイプライン、およびサプライチェーンセキュリティ
  - <strong>実装チェックリスト</strong>：必須と推奨セキュリティ制御の明確化とMicrosoftセキュリティエコシステムの利点

### ドキュメント品質と標準整合
- <strong>仕様参照</strong>：すべての参照を最新MCP仕様2025-06-18に更新
- **Microsoftセキュリティエコシステム**：すべてのセキュリティ文書で統合ガイダンスを強化
- <strong>実践的実装</strong>：.NET、Java、Pythonでの詳細なコード例と企業パターンを追加
- <strong>リソース組織化</strong>：公式文書、セキュリティ標準、実装ガイドの体系的分類
- <strong>視覚的指標</strong>：必須要件と推奨プラクティスの明確なマークアップ


#### コアコンセプト (01-CoreConcepts/) - 完全近代化
- <strong>プロトコルバージョン更新</strong>：現在のMCP仕様2025-06-18への言及を更新（日付ベースのバージョニング - YYYY-MM-DD形式）
- <strong>アーキテクチャの洗練</strong>：現在のMCPアーキテクチャパターンを反映するホスト、クライアント、サーバーの説明を強化
  - ホストは複数のMCPクライアント接続を調整するAIアプリケーションとして明確に定義
  - クライアントは1対1のサーバー関係を維持するプロトコルコネクターとして説明
  - サーバーはローカルとリモートの展開シナリオで強化
- <strong>プリミティブの再構築</strong>：サーバーとクライアントのプリミティブの完全な見直し
  - サーバープリミティブ：リソース（データソース）、プロンプト（テンプレート）、ツール（実行可能関数）について詳細な説明と例を提供
  - クライアントプリミティブ：サンプリング（LLMの補完）、エリシテーション（ユーザー入力）、ロギング（デバッグ/監視）
  - 現在の発見（`*/list`）、取得（`*/get`）、実行（`*/call`）メソッドパターンに更新
- <strong>プロトコルアーキテクチャ</strong>：2層アーキテクチャモデルの導入
  - データ層：ライフサイクル管理とプリミティブを含むJSON-RPC 2.0基盤
  - トランスポート層：STDIO（ローカル）およびSSE付きストリーミングHTTP（リモート）トランスポート機構
- <strong>セキュリティフレームワーク</strong>：明示的ユーザー同意、データプライバシー保護、ツール実行の安全性、トランスポート層セキュリティを含む包括的セキュリティ原則
- <strong>通信パターン</strong>：初期化、発見、実行、通知のフローを示すプロトコルメッセージを更新
- <strong>コード例</strong>：現在のMCP SDKパターンを反映する多言語例（.NET、Java、Python、JavaScript）を更新

#### セキュリティ (02-Security/) - 包括的なセキュリティ刷新  
- <strong>標準整合</strong>：MCP仕様2025-06-18のセキュリティ要件と完全に整合
- <strong>認証の進化</strong>：カスタムOAuthサーバーから外部IDプロバイダー委任（Microsoft Entra ID）への進化を文書化
- **AI特有の脅威分析**：現代AI攻撃ベクトルのカバー範囲を強化
  - 実例を伴う詳細なプロンプトインジェクション攻撃シナリオ
  - ツールポイズニングメカニズムおよび「ラグプル」攻撃パターン
  - コンテキストウィンドウポイズニングおよびモデル混乱攻撃
- **Microsoft AIセキュリティソリューション**：Microsoftセキュリティエコシステムの包括的カバー
  - 高度な検出、スポットライト、区切り技術を用いたAI Prompt Shields
  - Azure Content Safety統合パターン
  - サプライチェーン保護のためのGitHub Advanced Security
- <strong>高度な脅威緩和</strong>：詳細なセキュリティ制御
  - MCP特有の攻撃シナリオと暗号的セッションID要件を含むセッションハイジャック防止
  - 明示的同意要件を含むMCPプロキシの混乱を招く代理問題
  - 必須検証制御を含むトークン不正経路防止
- <strong>サプライチェーンセキュリティ</strong>：基盤モデル、埋め込みサービス、コンテキスト提供者、第三者APIを含むAIサプライチェーンカバレッジの拡大
- <strong>基盤セキュリティ</strong>：ゼロトラストアーキテクチャおよびMicrosoftセキュリティエコシステムを含むエンタープライズセキュリティパターンとの統合強化
- <strong>リソース組織</strong>：タイプ別に公式ドキュメント、標準、研究、Microsoftソリューション、実装ガイドへ体系的に分類

### ドキュメント品質の改善
- <strong>構造化学習目標</strong>：特定かつ実行可能な成果を伴う学習目標を強化
- <strong>クロスリファレンス</strong>：関連するセキュリティとコアコンセプトトピック間のリンクを追加
- <strong>最新情報</strong>：すべての日付参照と仕様リンクを最新標準に更新
- <strong>実装ガイダンス</strong>：両セクション全体に具体的で実行可能な実装指針を追加

## 2025年7月16日

### READMEおよびナビゲーションの改善
- README.mdのカリキュラムナビゲーションを完全に再設計
- `<details>`タグをよりアクセスしやすいテーブルベース形式に置換
- 新しい"alternative_layouts"フォルダに代替レイアウトオプションを作成
- カードベース、タブスタイル、アコーディオンスタイルのナビゲーション例を追加
- 最新ファイルを含むリポジトリ構造セクションを更新
- 「このカリキュラムの使い方」セクションを明確な推奨により強化
- MCP仕様リンクを正しいURLに更新
- コンテキストエンジニアリングセクション（5.14）をカリキュラム構成に追加

### スタディガイドの更新
- 現在のリポジトリ構造に合わせてスタディガイドを完全改訂
- MCPクライアントとツール、人気のMCPサーバーの新セクションを追加
- すべてのトピックを正確に反映するビジュアルカリキュラムマップを更新
- すべての専門分野をカバーする高度トピックの説明を強化
- 実際の例を反映するケーススタディセクションを更新
- この包括的な変更履歴を追加

### コミュニティ貢献 (06-CommunityContributions/)
- 画像生成向けMCPサーバーの詳細情報を追加
- VSCode内でClaudeを使う包括的セクションを追加
- Clineターミナルクライアントのセットアップと使用方法の説明を追加
- すべての人気クライアントオプションを含むMCPクライアントセクションを更新
- より正確なコードサンプルで貢献例を強化

### 高度なトピック (05-AdvancedTopics/)
- 一貫した命名で専門トピックフォルダを編成
- コンテキストエンジニアリング資料と例を追加
- Foundryエージェント統合ドキュメントを追加
- Entra IDセキュリティ統合ドキュメントを強化

## 2025年6月11日

### 初版作成
- MCP for Beginnersカリキュラムの初版リリース

- 10のメインセクションすべての基本構造を作成
- ナビゲーション用のビジュアルカリキュラムマップを実装
- 複数のプログラミング言語で初期サンプルプロジェクトを追加

### はじめに (03-GettingStarted/)
- 最初のサーバー実装例を作成
- クライアント開発ガイダンスを追加
- LLMクライアント統合手順を含める
- VS Code統合のドキュメントを追加
- サーバー送信イベント（SSE）サーバー例を実装

### コアコンセプト (01-CoreConcepts/)
- クライアント－サーバーアーキテクチャの詳細解説を追加
- 主要なプロトコルコンポーネントのドキュメントを作成
- MCPにおけるメッセージングパターンを文書化

## 2025年5月23日

### リポジトリ構造
- 基本的なフォルダ構造でリポジトリを初期化
- 各主要セクションのREADMEファイルを作成
- 翻訳インフラをセットアップ
- 画像資産と図を追加

### ドキュメント
- カリキュラム概要の初期README.mdを作成
- CODE_OF_CONDUCT.mdとSECURITY.mdを追加
- 支援を受けるためのガイダンスを含むSUPPORT.mdをセットアップ
- 初期の学習ガイド構造を作成

## 2025年4月15日

### 計画とフレームワーク
- MCP for Beginnersカリキュラムの初期計画
- 学習目標とターゲットオーディエンスを定義
- カリキュラムの10セクション構成を概説
- 例とケーススタディの概念的フレームワークを開発
- 主要コンセプトの初期プロトタイプ例を作成

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# 変更履歴: MCP初心者向けカリキュラム

本ドキュメントは、Model Context Protocol (MCP) 初心者カリキュラムに対するすべての重要な変更を記録するものです。変更は逆時系列（最新の変更が最初）で記録されています。

## 2026年7月29日

### 新モジュール08付随: 信頼性サイドカーと安全なリトライ

実際の効果を生み出すMCPツール向けのベンダーニュートラルな付随レッスンを追加し、
最終的な `2026-07-28` 仕様に沿っています。

- <strong>新規</strong>: [信頼性サイドカー付随レッスン][reliability-sidecar] は、
  サポートチケットのストーリー1つ、Mermaidダイアグラム2つ、リトライ決定
  フローを使って、安定動作の鍵、アトミックな重複受付、
  調整、証拠、そしてTasks拡張境界を説明します。
- <strong>新規</strong>: 標準ライブラリのPythonとSQLiteによる障害注入演習では、
  別々の操作ストアとチケットストアを使い、外部効果のコミット後に
  応答が失われる例を示します。6つの決定的テストで、単純な
  重複、保護された再起動回復、ペイロード競合、キャッシュ結果、
  アクティブクレーム、同時重複受付をカバーします。
- <strong>更新</strong>: モジュール08は付随レッスンへのリンクを追加し、
  最終的な `2026-07-28` 無状態リクエストモデルを特定し、
  OpenTelemetry観測可能性を非推奨のMCPログ機能と区別し、
  汎用的なリトライ例は読み取り専用操作に限定されました。
- <strong>任意</strong>: レッスンは、ホストサービスやネットワーク呼び出しを
  演習部分に含めることなく、ポータブルな概念を1つのタグ付きコミュニティ
  実装にマッピングします。

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026年7月2日

### 新レッスン: 2026-07-28 MCP仕様リリース候補

近日リリース予定の `2026-07-28` MCP仕様リリース候補（2026年5月21日発表、最終リリースは2026年7月28日予定）をカバーする内容を追加しました。[公式発表ブログ記事](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)を要約しています。カリキュラムの基準は新バージョンがリリースされるまで **MCP仕様 2025-11-25** のままなので、これは既存レッスンの書き換えではなく将来に向けたガイダンスとして提示しています。

- <strong>新規</strong>: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — ステートレスプロトコルコア（`initialize`ハンドシェイクと`Mcp-Session-Id`の削除）、新しい`Mcp-Method`/`Mcp-Name`ルーティングヘッダー、`ttlMs`/`cacheScope`キャッシュメタデータ、_metaにおけるW3Cトレースコンテキスト、正式なExtensionsフレームワーク（MCPアプリと新しいTasks拡張）、6つの認可強化SEP、Roots/Sampling/Loggingの非推奨、ツールスキーマに向けた完全なJSON Schema 2020-12への移行をカバーする完全なレッスン。
- <strong>更新</strong>: 新レッスンへのリンクを含む将来を見据えた呼び出しで更新:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): プロトコルバージョンに関する注記、Sampling/Roots/Logging/Tasksのセクション、「次に何が来るか」

  - [02-Security/README.md](./02-Security/README.md): 認可強化のコールアウト
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): ステートレストランスポートのコールアウト
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): サンプリング非推奨のコールアウト
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): ロギング非推奨とTasks拡張のコールアウト
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): ステートレス/セッションルーティングのコールアウト
  - [README.md](./README.md): 仕様セクションの「今後の展望」ノートとカリキュラムモジュール表の新しい `1.1` エントリ
  - [study_guide.md](./study_guide.md): コアコンセプト概要の先見的な箇条書きと日付付き追加注記
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): ステートレスリクエストモデルの前にある `mcp-session-id` トランスポートマップに関するコールアウト
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): ルートコンテキスト/サンプリング非推奨およびTasks拡張に関するモジュール概要のコールアウト
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): 認可強化のコールアウト

## 2026年6月24日

### 新しいレッスン: CopilotアプリでのMCP利用

- [ツーリングセクション](./12-tooling/README.md) ツーリングセクションを追加しました。
- [CopilotアプリでのMCP](./12-tooling/01-copilot-app/README.md)

## 2026年6月16日

### MCP仕様の整合とサンプル検証

カリキュラムを現行の **MCP Specification 2025-11-25** と最新の公式SDKに対して検証し、残っていた古い仕様参照を修正し、コアサンプルがまだビルド・実行できることを確認しました。

#### 仕様バージョンの修正（2025-06-18 / 2025-03-26 → 2025-11-25）

古い仕様改訂を「現在の/最新の」標準として示していた英語コンテンツを更新し、リンクを正規の `modelcontextprotocol.io` 仕様パスに差し替えました：
- **05-AdvancedTopics/mcp-security/README.md**: 「Current Standard」バナー、イントロダクション、コアセキュリティ原則の見出し、必須要件の見出し、Microsoft Entra ID セクション、参考文献＆リソースリンク、終了セキュリティ通知（8件の参照）を2025-11-25に更新
- **05-AdvancedTopics/mcp-transport/README.md**: 追加リソースの仕様リンクと「Current Standard」バナーを2025-11-25に更新
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: 廃止された `2025-03-26` セキュリティ＆トラストリンクを現在の2025-11-25セキュリティベストプラクティスページに差し替え

- **03-GettingStarted/14-sampling/README.md**: 公式のサンプリングドキュメントのリンクを2025-11-25に更新しました

- **03-GettingStarted/05-stdio-server/README.md**: 現在の MCP 仕様の現在形の参照と追加リソースの仕様リンクを 2025-11-25 に更新（正確性のため従来の SSE 廃止メモはそのまま）

#### 現行 SDK に対するサンプルの検証

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` で `@modelcontextprotocol/sdk@1.29.0` を解決；`tsc --noEmit` は型エラーなしで成功 — 既存の `McpServer` / `StdioServerTransport` API は引き続き有効
- **Python (03-GettingStarted/01-first-server/solution/python)**: `mcp[cli]` (1.27.2) 付きの独立 `.venv` で検証；`py_compile` は成功し、`FastMCP.list_tools()` は正しく `add` と `subtract` ツールを返却
- すべてのサンプルの `@modelcontextprotocol/sdk` バージョン範囲（`>=1.26.0` / `^1.26.0` / `^1.27.0`）は現在の `1.29.0` に問題なく解決し、APIの非互換変更はなしを確認

#### 依存性ピンの整合（バージョン差の解消）

古い SDK ピンを引き上げてすべてのサンプルが現在の MCP リリースに追随、リポジトリ全体の方針に一致させた:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` を `^1.8.0` → `>=1.26.0` に引き上げ、古い `"updated for MCP 2025-06-18"` パッケージ説明を `"aligned with MCP Specification 2025-11-25"` に更新
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** と **lab4/code/github_mcp_server/pyproject.toml**: 厳密なピン `mcp==1.23.0` → `mcp>=1.26.0` に引き上げ。両方の `uv.lock` ファイルを再生成（`uv lock`）し、ロックファイルが現在の `mcp 1.27.2` を解決しマニフェストと同期するように維持

#### カリキュラムのギャップ分析 — 最新仕様の機能カバー範囲

MCP 2025-11-25 で導入・拡張されたすべてのプリミティブはすでにカリキュラムに含まれていることを検証し、内容のギャップはなし:
- **Sampling**: レッスン 03-GettingStarted/14-sampling と 05-AdvancedTopics/mcp-sampling
- **Elicitation (URL モードを含む)**: 01-CoreConcepts と 05-AdvancedTopics/mcp-protocol-features に文書化済み
- **Roots**: 00-Introduction、01-CoreConcepts、05-AdvancedTopics/mcp-root-contexts に文書化済み
- **Tasks (実験的、長時間実行オペレーション)**: 01-CoreConcepts と 05-AdvancedTopics/mcp-protocol-features に文書化済み
- <strong>ツールアノテーション</strong>（`readOnlyHint` / `destructiveHint`）: 01-CoreConcepts と 05-AdvancedTopics/mcp-protocol-features に文書化済み

### セキュリティ強化 & 依存性脆弱性修正

すべての依存性マニフェストとサンプルソースコードに対して包括的なセキュリティチェックを実施し、報告された npm アドバイザリと 1 件のコードレベルの指摘を修正。修正後は、監査対象のすべてのディレクトリで `npm audit` が<strong>脆弱性ゼロ</strong>を報告

#### npm 依存関係の脆弱性（間接的） — 解決済み

コミットされた 15 件の `package-lock.json` ファイルをすべて監査。脆弱性は、MCP Inspector 開発ツール、OpenAI クライアント、MCP SDK が引き込む間接依存関係に限定されていたが、いずれもサンプルを壊さず解決済み:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** と **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`) を引き上げ、バンドルされた `ajv`、`brace-expansion`、`diff`、`path-to-regexp`、`ws` のアドバイザリをクリア。npm の `overrides` エントリにより `shell-quote@1.8.4` のパッチ版を強制し、`concurrently` による残る重大アドバイザリを排除。両方のロックファイルを再生成し（現在は脆弱性ゼロ）
- **03-GettingStarted/samples/typescript**: `npm audit fix` により間接依存の `qs`（中程度）をパッチリリースに更新
- **03-GettingStarted/samples/javascript**: `npm audit fix` により間接依存の `hono`（中程度）をパッチリリースに更新
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` により間接依存の `form-data`（高リスク）をパッチリリースに更新
- **03-GettingStarted/11-simple-auth/solution/typescript**: 欠落していた `package-lock.json` を生成し、プロジェクトが再現可能かつ監査可能に（脆弱性ゼロ）

#### コードレベルのセキュリティ修正（OWASP A03: インジェクション）

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` ツールから `shell=True` を除去。以前の `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` は、フォルダパス内のシェルメタ文字を `cmd.exe` が解釈する可能性があり（コマンドインジェクションのリスク）、現在はシェルを介さず解決済みの `Code.exe` をフォルダ引数付きで直接起動。機能的に同等かつ安全

#### Python 依存関係監査

- すべての Python requirements セットを `pip-audit` で監査。`05-AdvancedTopics` および `03-GettingStarted/samples/python` は<strong>既知の脆弱性なし</strong>（`mcp` / `httpx` / `pydantic` / `python-dotenv` 範囲は現在のパッチ済みリリースに解決）
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` が間接依存の **`werkzeug` 3.1.1** に 3 件の `safe_join` Windows デバイス名 DoS 脆弱性を指摘 — `CVE-2025-66221`, `CVE-2026-21860`, `CVE-2026-27199`（いずれも 3.1.6 で修正済み）。明示的にセキュリティピン `werkzeug>=3.1.6` を追加してパッチ版を解決、`chainlit` / `mcp` / `semantic-kernel` スタックで制約が正しく解決されることを検証

### 製品名のリブランディング

すべてのカリキュラムコンテンツを Microsoft の製品リブランディングに合わせて更新


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord コミュニティリンクを更新

- **AGENTS.md**: Discordサーバー参照を更新
- **README.md**: 技術エコシステムの参照を更新
- **study_guide.md**: ケーススタディ参照を更新
- **05-AdvancedTopics/README.md**: モジュール 5.13 のタイトルと説明を更新
- **05-AdvancedTopics/mcp-integration/README.md**: セクションヘッダーと説明を更新
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: モジュールタイトルと内容を全面更新
- **05-AdvancedTopics/mcp-security-entra/README.md**: クロスリファレンスリンクを更新
- **07-LessonsfromEarlyAdoption/README.md**: ケーススタディ参照を更新
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: セクション9見出し、バッジ、機能を更新
- **08-BestPractices/README.md**: Discordコミュニティリンクを更新
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discordチャンネル参照を更新
- **09-CaseStudy/docs-mcp/solution/python/README.md**: モデルデプロイメント参照を更新
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AIサービス表を更新
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: リソース参照を更新

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: メインカリキュラム参照を更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: モジュールタイトル、概要、全モジュールヘッダーを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: タイトル、学習目標、セットアップ手順、リソースを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: タイトル、学習目標、MCPホスト表、クロスリファレンスを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: タイトル、バッジ、前提条件、リソースを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Agent Builder参照とフィードバックリンクを更新
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: 前提条件と拡張機能参照を更新

---

## 2026年4月11日

### 新しいレッスン、ドキュメント修正、依存関係のアップデート

#### 新カリキュラムコンテンツ追加

**モジュール 05 - 高度なトピック**
- **レッスン 5.17: MCPによる敵対的マルチエージェント推論** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): マルチエージェントシステムの敵対的議論パターンを網羅的に解説する新しいガイド
  - Mermaid アーキテクチャ図: 2つのエージェント → 共有MCPサーバー → 議論の記録 → 判定者 → 判決
  - PythonとTypeScriptで実装された共有MCPツールサーバー（`web_search` + `run_python`）
  - 明示的なツール使用要件を持つ賛成/反対/判定者のシステムプロンプト
  - 議論進行役をPython、TypeScript、C#で実装し、ラウンド管理と主張のルーティングを担当
  - MCP `ClientSession` をオーケストレーターの実際のツール呼び出しに接続
  - 利用シーン表（幻覚検出、脅威モデリング、API設計レビュー、事実検証、技術選定）
  - セキュリティ考慮点: サンドボックス実行、ツール呼び出し検証、レート制限、監査ログ
  - 3つの実践シナリオ（コードレビュー、アーキテクチャ決定、コンテンツモデレーション）を含む体系的演習

#### ドキュメント修正

**モジュール 03 - はじめに**
- **05-stdio-server/README.md**: Pythonおよび.NETの同じセクション例に合わせて、不完全だったTypeScriptのstdioサーバー例を修正 — 伝送インスタンス化（`new StdioServerTransport()`）と `server.connect(transport)` 呼び出しを追加
- **14-sampling/README.md**: タイポ修正 — `"Sampling is an davanced features"` を `"Sampling is an advanced feature"` に訂正

#### カリキュラム更新

**メイン README.md**
- 新レッスンに直接リンクしたカリキュラム表にエントリ 5.17（敵対的マルチエージェント推論）を追加

**05-AdvancedTopics/README.md**
- レッスン 5.17 行をレッスン表に追加

**study_guide.md**
- 高度なトピックのマインドマップと本文説明に敵対的マルチエージェント推論を追加

#### コードとセキュリティ修正

**モジュール 05 - 敵対的エージェント (`mcp-adversarial-agents`)**
- **セキュリティ修正 — コマンドインジェクション**: TypeScriptの `run_python` ツールで `execSync` のシェル補間を `execFile` + `promisify` に置き換え、コマンドインジェクションの脆弱性を排除（LLM制御コードはシェル未関与のリテラルargv要素として渡される）
- **MCPツールループの配線**: Pythonの議論オーケストレーターを更新し、ブロッキング同期の `Anthropic` を非同期の `AsyncAnthropic` クライアントに置換、各エージェントターンにライブの `ClientSession` を直接渡し、毎ターン `session.list_tools()` でツール定義を取得し、最終テキスト応答までループで `session.call_tool()` による `tool_use` ブロックをディスパッチ

#### 依存関係アップデート

- 複数パッケージ（03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows）で `hono` を 4.12.12 に更新
- TypeScriptパッケージで `@hono/node-server` を 1.19.11 から 1.19.13 に更新
- Pythonパッケージ（10-StreamliningAIWorkflowsラボ3および4）で `cryptography` を 46.0.5 から 46.0.7 に更新
- 10-StreamliningAIWorkflows インスペクターで `lodash` を 4.17.23 から 4.18.1 に更新

#### 翻訳更新

- 最新のソース変更に合わせて48言語以上の翻訳を同期（i18nアップデート）

---

## 2026年2月5日

### リポジトリ全体の検証とナビゲーション改善

#### 新カリキュラムコンテンツ追加

**モジュール 03 - はじめに**
- **12-mcp-hosts/README.md**: MCPホスト設定の包括的ガイドを新規追加
  - Claude Desktop、VS Code、Cursor、Cline、Windsurfの設定例
  - 主要ホストのJSON設定テンプレート
  - 伝送タイプ比較表（stdio、SSE/HTTP、WebSocket）
  - 一般的な接続問題のトラブルシューティング
  - ホスト設定のセキュリティベストプラクティス

- **13-mcp-inspector/README.md**: MCPインスペクターのデバッグガイド新規追加
  - インストール方法（npx、npm全体、ソースから）
  - stdioおよびHTTP/SSE経由のサーバー接続
  - テストツール、リソース、プロンプトワークフロー
  - VS CodeとMCPインスペクターの統合
  - 一般的なデバッグシナリオと解決策

**モジュール 04 - 実践的な実装**
- **pagination/README.md**: ページネーション実装ガイド新規追加
  - Python、TypeScript、Javaのカーソルベースページネーションパターン
  - クライアント側ページネーション処理
  - カーソル設計戦略（不透明なものと構造化されたもの）
  - パフォーマンス最適化推奨

**モジュール 05 - 高度なトピック**
- **mcp-protocol-features/README.md**: 新しいプロトコル機能の詳細解説
  - 進捗通知の実装
  - リクエストキャンセルパターン
  - URIパターンを用いたリソーステンプレート
  - サーバーライフサイクル管理
  - ロギングレベルの制御
  - JSON-RPCコードによるエラーハンドリングパターン

#### ナビゲーション修正（24ファイル以上更新）

**メインモジュールREADME**
 最初のレッスンおよび次モジュールへのリンクを追加

**02-Security サブファイル**
- 5つの補助的なセキュリティ文書すべてに「次は何か」ナビゲーションを追加

**09-CaseStudy ファイル**
- すべてのケーススタディファイルに連続したナビゲーションを追加

**10-StreamliningAI ラボ**
モジュール10概要およびモジュール11に「次は何か」セクションを追加

#### コードおよびコンテンツ修正

**SDKおよび依存関係アップデート**
空のopenaiバージョンを `^4.95.0` に修正
SDKを `^1.8.0` から `>=1.26.0` に更新
MCPバージョンのピン指定を `>=1.26.0` に更新

<strong>コード修正</strong>
無効なモデル `gpt-4o-mini` を `gpt-4.1-mini` に修正

<strong>コンテンツ修正</strong>
壊れたリンク `READMEmd` → `README.md`、カリキュラムヘッダー `Module 1-3` → `Module 0-3`、ケースセンシティブなパスを修正
重複した壊れたケーススタディ5コンテンツを削除

<strong>初心者向けガイダンス改善</strong>
適切な導入、学習目標、前提条件を追加

#### カリキュラム更新

**メイン README.md**
- カリキュラム表にエントリー 3.12 (MCP Hosts)、3.13 (MCP Inspector)、4.1 (Pagination)、5.16 (Protocol Features) を追加

**モジュール README**
レッスン 12 と 13 をレッスンリストに追加
ページネーションへのリンクを含む実践ガイドセクションを追加
レッスン 5.15 (Custom Transport) と 5.16 (Protocol Features) を追加

**study_guide.md**
- マインドマップに MCP Hosts Setup、MCP Inspector、Pagination Strategies、Protocol Features Deep Dive を追加

## 2026年1月28日

### MCP仕様 2025-11-25 準拠レビュー

#### コアコンセプトの強化 (01-CoreConcepts/)
- **新しいクライアントプリミティブ - Roots**: サーバーがファイルシステムの境界とアクセス許可を理解できるRootsクライアントプリミティブの包括的ドキュメントを追加
- <strong>ツール注釈</strong>: ツールの挙動注釈（`readOnlyHint`, `destructiveHint`）に関するドキュメントを追加し、より良いツール実行判断をサポート
- <strong>サンプリングにおけるツール呼び出し</strong>: サンプリングドキュメントにモデル駆動のツール呼び出し用パラメータ `tools` と `toolChoice` を追記
- **URLモード呼び出し**: サーバー発信の外部WebインタラクションのためのURLベース呼び出しに関するドキュメントを追加
- **タスク（実験的）**: 持続可能な実行ラッパーと遅延結果取得のための実験的タスク機能に関する新セクションを追加
- <strong>アイコンサポート</strong>: ツール、リソース、リソーステンプレート、プロンプトが追加のメタデータとしてアイコンを含められることを追記

#### ドキュメント更新
- **README.md**: MCP仕様 2025-11-25バージョン参照と日付ベースバージョニングの説明を追加
- **study_guide.md**: コアコンセプトセクションにタスクとツール注釈を含めてカリキュラムマップを更新、ドキュメントのタイムスタンプも更新

#### 仕様準拠確認
- <strong>プロトコルバージョン</strong>: ドキュメントが最新のMCP仕様 2025-11-25を参照していることを確認
- <strong>アーキテクチャ整合性</strong>: 二層アーキテクチャ（データレイヤ＋トランスポートレイヤ）ドキュメントの正確性を検証
- <strong>プリミティブドキュメント</strong>: サーバープリミティブ（リソース、プロンプト、ツール）およびクライアントプリミティブ（サンプリング、呼び出し、ロギング、Roots）を検証
- <strong>トランスポート手段</strong>: STDIOおよびストリーム可能HTTPトランスポートのドキュメント正確性を確認
- <strong>セキュリティ指針</strong>: 最新のMCPセキュリティベストプラクティスドキュメントと整合していることを確認

#### 主要なMCP 2025-11-25機能を文書化
- **OpenID Connectディスカバリー**: OIDCを通じた認証サーバーの検出
- **OAuthクライアントIDメタデータドキュメント**: クライアント登録機構の推奨
- **JSONスキーマ 2020-12**: MCPスキーマ定義のデフォルト方言
- **SDKティアリングシステム**: SDK機能サポートとメンテナンス要件の正式化
- <strong>ガバナンス構造</strong>: MCPガバナンスにおけるワーキンググループとインタレストグループの正式化

### セキュリティドキュメント大規模更新 (02-Security/)

#### MCPセキュリティサミットワークショップ (Sherpa) 統合
- <strong>新しいハンズオン研修リソース</strong>: すべてのセキュリティドキュメントにわたり [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) との包括的統合を追加
- <strong>遠征ルートカバレッジ</strong>: ベースキャンプからサミットまでの完全なキャンプ間進行をドキュメント化
- **OWASP整合**: すべてのセキュリティ指導がOWASP MCP Azureセキュリティガイドのリスクにマッピングされていることを確認

#### OWASP MCP トップ10統合
- <strong>新セクション</strong>: Azureの緩和策を含むOWASP MCPトップ10セキュリティリスク表をメインセキュリティREADMEに追加
- <strong>リスクベースドキュメント</strong>: mcp-security-controls-2025.mdを更新し、各セキュリティドメインにOWASP MCPリスク参照を追加
- <strong>参照アーキテクチャ</strong>: OWASP MCP Azureセキュリティガイドの参照アーキテクチャおよび実装パターンへのリンクを追加

#### セキュリティファイル更新
- **README.md**: Sherpaワークショップ概要、遠征ルート表、OWASP MCPトップ10リスク概要、ハンズオン研修セクションを追加
- **mcp-security-controls-2025.md**: 見出しを2026年2月に更新、OWASPリスク参照 (MCP01-MCP08) を追加、仕様バージョン不整合を修正
- **mcp-security-best-practices-2025.md**: SherpaおよびOWASPリソースセクションを追加、タイムスタンプを更新
- **mcp-best-practices.md**: ハンズオン研修セクションにSherpaおよびOWASPリンクを追加
- **azure-content-safety-implementation.md**: OWASP MCP06参照、Sherpaキャンプ3整合、追加リソースセクションを追加

#### 新規リソースリンク追加
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure セキュリティガイド](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP トップ10](https://owasp.org/www-project-mcp-top-10/)
- 個別のOWASP MCPリスクページ (MCP01-MCP10)

### カリキュラム全体のMCP仕様 2025-11-25整合

#### モジュール03 - はじめに
- **SDKドキュメント**: Go SDKを公式SDKリストに追加；全てのSDK参照をMCP仕様2025-11-25に合わせて更新
- <strong>トランスポートの明確化</strong>: STDIOおよびHTTPストリーミングトランスポートの説明を明示的な仕様参照で更新

#### モジュール04 - 実践的実装
- **SDK更新**: Go SDKを追加；SDKリストを仕様バージョン参照で更新
- <strong>認可仕様</strong>: MCP認可仕様リンクを最新の2025-11-25バージョンに更新

#### モジュール05 - 高度なトピック
- <strong>新機能</strong>: MCP仕様2025-11-25の新機能（タスク、ツール注釈、URLモードエリシテーション、ルーツ）に関する注記を追加
- <strong>セキュリティリソース</strong>: OWASP MCPトップ10およびSherpaワークショップリンクを追加参考文献に追加

#### モジュール06 - コミュニティ貢献
- **SDKリスト**: SwiftおよびRust SDKを追加；仕様リンクを2025-11-25に更新
- <strong>仕様参照</strong>: MCP仕様リンクを直接仕様URLに更新

#### モジュール07 - 早期採用からの教訓
- <strong>リソース更新</strong>: MCP仕様2025-11-25リンクおよびOWASP MCPトップ10を追加リソースに追加

#### モジュール08 - ベストプラクティス
- <strong>仕様バージョン</strong>: MCP仕様参照を2025-11-25に更新
- <strong>セキュリティリソース</strong>: OWASP MCPトップ10およびSherpaワークショップを追加参考文献に追加

#### モジュール10 - AIワークフローの合理化
- <strong>バッジ更新</strong>: MCPバージョンバッジをSDKバージョン(1.9.3)から仕様バージョン(2025-11-25)に変更
- <strong>リソースリンク</strong>: MCP仕様リンクを更新；OWASP MCPトップ10を追加

#### モジュール11 - MCPサーバーハンズオンラボ
- <strong>仕様参照</strong>: MCP仕様リンクを2025-11-25バージョンに更新
- <strong>セキュリティリソース</strong>: 公式リソースにOWASP MCPトップ10を追加

## 2025年12月18日

### セキュリティドキュメント更新 - MCP仕様 2025-11-25

#### MCPセキュリティベストプラクティス（02-Security/mcp-best-practices.md）- 仕様バージョン更新
- <strong>プロトコルバージョン更新</strong>: 最新MCP仕様2025-11-25（2025年11月25日リリース）への参照を更新
  - すべての仕様バージョン参照を2025-06-18から2025-11-25に更新
  - 文書の日付参照を2025年8月18日から2025年12月18日に更新
  - すべての仕様URLが最新ドキュメントを指していることを確認
- <strong>内容の検証</strong>: 最新標準に対するセキュリティベストプラクティスの包括的検証
  - **Microsoftセキュリティソリューション**: Prompt Shields（旧「Jailbreakリスク検出」）、Azure Content Safety、Microsoft Entra ID、Azure Key Vaultの現在の用語とリンクを検証
  - **OAuth 2.1セキュリティ**: 最新のOAuthセキュリティベストプラクティスとの整合性を確認
  - **OWASP標準**: LLM向けOWASPトップ10参照が最新のままであることを確認
  - **Azureサービス**: すべてのMicrosoft Azureドキュメントリンクとベストプラクティスを検証
- <strong>標準との整合性</strong>: 参照されたすべてのセキュリティ標準が最新であることを確認
  - NIST AIリスク管理フレームワーク
  - ISO 27001:2022
  - OAuth 2.1セキュリティベストプラクティス
  - Azureセキュリティおよびコンプライアンスフレームワーク
- <strong>実装リソース</strong>: すべての実装ガイドリンクとリソースを検証
  - Azure API Management 認証パターン
  - Microsoft Entra ID 統合ガイド
  - Azure Key Vault シークレット管理
  - DevSecOpsパイプラインとモニタリングソリューション

### ドキュメント品質保証
- <strong>仕様準拠</strong>: すべての必須MCPセキュリティ要件（MUST/MUST NOT）が最新仕様と整合していることを保証
- <strong>リソースの最新性</strong>: Microsoftドキュメント、セキュリティ標準、実装ガイドへのすべての外部リンクを検証
- <strong>ベストプラクティスの網羅性</strong>: 認証、認可、AI固有の脅威、サプライチェーンセキュリティ、エンタープライズパターンの包括的カバーを確認

## 2025年10月6日

### はじめにセクション拡張 – 高度なサーバー使用法＆シンプル認証

#### 高度なサーバー使用法（03-GettingStarted/10-advanced）
- <strong>新章追加</strong>: 一般的および低レベルサーバーアーキテクチャ両方をカバーする高度なMCPサーバー使用法の包括的ガイドを導入
  - <strong>一般サーバーと低レベルサーバーの比較</strong>: 両アプローチの詳細比較とPythonおよびTypeScriptのコード例
  - <strong>ハンドラー方式の設計</strong>: 拡張性と柔軟性のあるサーバー実装のためのツール／リソース／プロンプト管理のハンドラー方式の説明
  - <strong>実践的パターン</strong>: 低レベルサーバーパターンが高度な機能・アーキテクチャで有用な実例

#### シンプル認証（03-GettingStarted/11-simple-auth）
- <strong>新章追加</strong>: MCPサーバーにおけるシンプル認証実装のステップバイステップガイド
  - <strong>認証の基本概念</strong>: 認証と認可の違いや資格情報の取り扱いを明確に解説
  - **Basic Auth実装**: Python(Starlette)とTypeScript(Express)によるミドルウェアベース認証パターンとコード例
  - <strong>高度セキュリティへの進展</strong>: シンプル認証からOAuth 2.1やRBACへ進むための指針と高度セキュリティモジュール参照

これらの追加により、基礎概念から高度な実運用パターンまでつなぐ、より堅牢で安全かつ柔軟なMCPサーバー実装の実践的な指導が提供されます。

## 2025年9月29日

### MCPサーバーデータベース統合ラボ - 包括的ハンズオン学習パス

#### 11-MCPServerHandsOnLabs - 新完全データベース統合カリキュラム
- **完全な13ラボ学習パス**: PostgreSQLデータベース統合を伴う本番対応MCPサーバー構築の包括的ハンズオンカリキュラムを追加
  - <strong>実世界の実装例</strong>: Zava Retail分析ユースケースでのエンタープライズグレードパターンの紹介
  - <strong>構造化された学習進行</strong>:
    - **ラボ 00-03: 基礎** - 入門、コアアーキテクチャ、セキュリティ＆マルチテナンシー、環境構築
    - **ラボ 04-06: MCPサーバー構築** - データベース設計・スキーマ、MCPサーバー実装、ツール開発
    - **ラボ 07-09: 高度な機能** - セマンティック検索統合、テスト＆デバッグ、VS Code統合
    - **ラボ 10-12: 本番稼働＆ベストプラクティス** - 展開戦略、モニタリング＆可観測性、ベストプラクティス＆最適化
  - <strong>エンタープライズ技術</strong>: FastMCPフレームワーク、pgvector対応PostgreSQL、Azure OpenAI埋め込み、Azure Container Apps、Application Insights
  - <strong>高度機能</strong>: 行レベルセキュリティ（RLS）、セマンティック検索、マルチテナントデータアクセス、ベクトル埋め込み、リアルタイムモニタリング

#### 用語統一 - モジュールからラボへの名称変更
- <strong>ドキュメント全面更新</strong>: 11-MCPServerHandsOnLabs内すべてのREADMEファイルで「モジュール」名称を「ラボ」に体系的に変更
  - <strong>セクション見出し</strong>: 全13ラボにわたり「このモジュールが扱う内容」を「このラボが扱う内容」に更新
  - <strong>内容説明</strong>: ドキュメント内の「このモジュールは…」を「このラボは…」に変更
  - <strong>学習目標</strong>: 「このモジュールの終了時に…」を「このラボの終了時に…」に更新
  - <strong>ナビゲーションリンク</strong>: すべての「モジュールXX:」を「ラボXX:」に変更
  - <strong>完了追跡</strong>: 「このモジュールの完了後に…」を「このラボの完了後に…」に更新
  - <strong>技術的参照保持</strong>: 設定ファイル内のPythonモジュール参照（例："module": "mcp_server.main"）はそのまま維持

#### 学習ガイド強化（study_guide.md）
- <strong>視覚的カリキュラムマップ</strong>: 「11. データベース統合ラボ」セクションを新規追加し、詳細なラボ構造を視覚化
- <strong>リポジトリ構成</strong>: メインセクションを10から11に更新し、11-MCPServerHandsOnLabs詳細を追加
- <strong>学習パス案内</strong>: セクション00-11のナビゲーション案内を強化
- <strong>技術カバー</strong>: FastMCP、PostgreSQL、Azureサービス統合の詳細を追加
- <strong>学習成果</strong>: 本番対応サーバー開発、データベース統合パターン、エンタープライズセキュリティを強調

#### メインREADME構造強化
- <strong>ラボベース用語</strong>: 11-MCPServerHandsOnLabsのメインREADME.mdで一貫して「ラボ」構造を使用へ更新
- <strong>学習パス構成</strong>: 基礎概念から高度実装、本番展開までの明確な進行を示す
- <strong>実世界重視</strong>: エンタープライズグレード技術・パターンによる実践的ハンズオン学習を強調

### ドキュメント品質と一貫性向上
- <strong>ハンズオン学習強調</strong>: ドキュメント全体で実践的ラボ形式を強調
- <strong>エンタープライズパターン重視</strong>: 本番対応実装とエンタープライズセキュリティをフォーカス
- <strong>技術統合</strong>: モダンなAzureサービスとAI統合パターンを包括的にカバー
- <strong>学習進行</strong>: 基礎から本番展開までの明確で構造的なパスを提供

## 2025年9月26日

### ケーススタディ強化 - GitHub MCPレジストリ統合

#### ケーススタディ（09-CaseStudy/）- エコシステム開発重視
- **README.md**: GitHub MCPレジストリに関する包括的ケーススタディで大幅拡張
  - **GitHub MCPレジストリケーススタディ**: 2025年9月のGitHub MCPレジストリローンチを詳細に分析
    - <strong>課題分析</strong>: 断片化したMCPサーバー検出と展開の課題を詳細に検討
    - <strong>解決策アーキテクチャ</strong>: GitHubの集中型レジストリアプローチとワンクリックVS Codeインストール
    - <strong>ビジネスインパクト</strong>: 開発者オンボーディングと生産性の測定可能な改善
    - <strong>戦略的価値</strong>: モジュラー型エージェント展開とツール間相互運用性に注力
    - <strong>エコシステム開発</strong>: エージェント統合の基盤となるプラットフォームとしての位置づけ
  - <strong>ケーススタディ構成強化</strong>: 7つのケーススタディすべてを一貫したフォーマットと詳細な説明で更新
    - Azure AIトラベルエージェント: マルチエージェントオーケストレーションに重点
    - Azure DevOps統合: ワークフロー自動化中心
    - リアルタイムドキュメント検索: Pythonコンソールクライアント実装
    - 対話型学習プランジェネレータ: Chainlit対話型ウェブアプリ
    - エディター内ドキュメント: VS CodeおよびGitHub Copilot統合
    - Azure API Management: エンタープライズAPI統合パターン
    - GitHub MCPレジストリ: エコシステム開発とコミュニティプラットフォーム
  - <strong>包括的結論</strong>: 複数のMCP実装分野にわたる7つのケーススタディの結論部分を書き直し
    - エンタープライズ統合、マルチエージェントオーケストレーション、開発者生産性
    - エコシステム開発、教育アプリケーションの分類
    - アーキテクチャパターン、実装戦略、ベストプラクティスへの洞察を強化
    - MCPを成熟した本番対応プロトコルとして強調

#### 学習ガイド更新（study_guide.md）
- <strong>視覚的カリキュラムマップ</strong>: ケーススタディセクションにGitHub MCPレジストリを追加
- <strong>ケーススタディ説明</strong>: 一般的な説明から7件の包括的ケーススタディの詳細内訳に強化
- <strong>リポジトリ構成</strong>: セクション10を大幅なケーススタディカバレッジと具体的実装詳細に更新
- <strong>更新履歴統合</strong>: 2025年9月26日のGitHub MCPレジストリ追加およびケーススタディ強化の記録を追加
- <strong>日付更新</strong>: フッタータイムスタンプを最新改訂日（2025年9月26日）に更新

### ドキュメント品質向上
- <strong>一貫性向上</strong>: 7例のすべてでケーススタディのフォーマットと構成を標準化
- <strong>包括的カバレッジ</strong>: ケーススタディはエンタープライズ、開発者生産性、エコシステム開発の各シナリオを網羅
- <strong>戦略的ポジショニング</strong>: MCPをエージェントシステム展開の基盤プラットフォームとして強調
- <strong>リソース統合</strong>: 追加リソースにGitHub MCPレジストリリンクを含めて更新

## 2025年9月15日

### 高度なトピック拡張 - カスタムトランスポート＆コンテキストエンジニアリング

#### MCPカスタムトランスポート（05-AdvancedTopics/mcp-transport/） - 新高度実装ガイド
- **README.md**: カスタムMCPトランスポートメカニズムの完全な実装ガイド
  - **Azure Event Gridトランスポート**: 包括的なサーバーレスイベントドリブントランスポート実装
    - C#、TypeScript、Pythonの例とAzure Functions統合
    - スケーラブルなMCPソリューションのためのイベント駆動型アーキテクチャパターン
    - Webhook受信およびプッシュベースのメッセージ処理
  - **Azure Event Hubsトランスポート**: 高スループットストリーミングトランスポート実装
    - 低遅延シナリオのリアルタイムストリーミング機能
    - パーティショニング戦略とチェックポイント管理
    - メッセージバッチ処理とパフォーマンス最適化
  - <strong>エンタープライズ統合パターン</strong>: 本番対応アーキテクチャ例
    - 複数のAzure Functionsに分散したMCP処理
    - 複数トランスポートタイプを組み合わせたハイブリッドトランスポートアーキテクチャ
    - メッセージの耐久性、信頼性、エラー処理戦略
  - **セキュリティ＆モニタリング**: Azure Key Vault統合と観測性パターン
    - マネージドID認証と最小特権アクセス
    - Application Insightsによるテレメトリとパフォーマンス監視
    - サーキットブレーカーとフォールトトレランスパターン
  - <strong>テストフレームワーク</strong>: カスタムトランスポートの包括的テスト戦略
    - テストダブルおよびモッキングフレームワークによる単体テスト
    - Azure Test Containersを用いた統合テスト
    - パフォーマンスおよび負荷テストの考慮事項

#### コンテキストエンジニアリング（05-AdvancedTopics/mcp-contextengineering/） - 新興AI分野
- **README.md**: 新興分野としてのコンテキストエンジニアリングの包括的探求
  - <strong>核心原理</strong>: 完全なコンテキスト共有、行動決定認識、コンテキストウィンドウ管理

  - **MCPプロトコル整合性**：MCP設計がコンテキストエンジニアリングの課題にどのように対応しているか  
    - コンテキストウィンドウの制限と段階的読み込み戦略  
    - 関連性の判定と動的コンテキスト取得  
    - マルチモーダルコンテキスト処理とセキュリティ考慮事項  
  - <strong>実装アプローチ</strong>：シングルスレッド対マルチエージェントアーキテクチャ  
    - コンテキスト分割と優先順位付け技術  
    - 段階的コンテキスト読み込みと圧縮戦略  
    - 階層化コンテキストアプローチと取得最適化  
  - <strong>測定フレームワーク</strong>：コンテキスト有効性評価の新しい指標  
    - 入力効率、性能、品質、ユーザー体験の考慮事項  
    - コンテキスト最適化の実験的アプローチ  
    - 失敗分析と改善手法  

#### カリキュラムナビゲーションの更新 (README.md)  
- <strong>モジュール構造の拡充</strong>：新しい高度なトピックを含むカリキュラム表の更新  
  - コンテキストエンジニアリング(5.14)とカスタムトランスポート(5.15)を追加  
  - 全モジュールで一貫したフォーマットとナビゲーションリンク  
  - 現行のコンテンツ範囲を反映した説明文の更新  

### ディレクトリ構造の改善  
- <strong>命名規則の統一</strong>：「mcp transport」を他の高度トピックフォルダと整合する"mcp-transport"に名称変更  
- <strong>コンテンツ整理</strong>：すべての05-AdvancedTopicsフォルダが一貫した命名パターン（mcp-[トピック]）を採用  

### ドキュメント品質向上  
- **MCP仕様整合**：すべての新規コンテンツがMCP仕様2025-06-18に準拠  
- <strong>多言語サンプル</strong>：C#、TypeScript、Pythonの包括的なコード例  
- <strong>エンタープライズ重視</strong>：製品対応パターンとAzureクラウド統合を通じて提供  
- <strong>ビジュアルドキュメント</strong>：アーキテクチャとフローを可視化するMermaid図解  

## 2025年8月18日  

### ドキュメント包括的更新 - MCP 2025-06-18標準準拠  

#### MCPセキュリティベストプラクティス(02-Security/) - 完全近代化  
- **MCP-SECURITY-BEST-PRACTICES-2025.md**：MCP仕様2025-06-18準拠の完全再執筆  
  - <strong>必須要件</strong>：公式仕様からの明確なMUST/MUST NOT要件を視覚的インジケーター付きで追加  
  - **12のコアセキュリティプラクティス**：15項目リストから包括的なセキュリティドメインへ再構成  
    - トークンセキュリティ＆認証：外部アイデンティティプロバイダー統合  
    - セッション管理＆トランスポートセキュリティ：暗号要件含む  
    - AI特有の脅威防護：Microsoft Prompt Shields統合  
    - アクセスコントロール＆権限：最小権限の原則  
    - コンテンツ安全＆モニタリング：Azure Content Safety統合  
    - サプライチェーンセキュリティ：包括的なコンポーネント検証  
    - OAuthセキュリティ＆Confused Deputy防止：PKCE実装  
    - インシデント対応＆リカバリー：自動化機能  
    - コンプライアンス＆ガバナンス：規制適合  
    - 高度セキュリティコントロール：ゼロトラストアーキテクチャ  
    - Microsoftセキュリティエコシステム統合：包括的ソリューション  
    - セキュリティの継続的進化：適応型プラクティス  
  - **Microsoftセキュリティソリューション**：Prompt Shields、Azure Content Safety、Entra ID、GitHub Advanced Securityとの統合強化ガイダンス  
  - <strong>実装リソース</strong>：公式MCPドキュメント、Microsoftセキュリティソリューション、セキュリティ基準、実装ガイド別に包括的リソースリンクを分類  

#### 高度セキュリティコントロール(02-Security/) - エンタープライズ実装  
- **MCP-SECURITY-CONTROLS-2025.md**：エンタープライズ等級セキュリティフレームワークの総合的改訂  
  - **9つの包括的セキュリティドメイン**：基本コントロールから詳細なエンタープライズフレームワークへ拡張  
    - 高度認証＆認可：Microsoft Entra ID統合  
    - トークンセキュリティ＆アンチパススルーコントロール：包括的検証  
    - セッションセキュリティコントロール：ハイジャック防止  
    - AI特有セキュリティコントロール：プロンプトインジェクションとツールポイズニング防止  
    - Confused Deputy攻撃防止：OAuthプロキシセキュリティ  
    - ツール実行セキュリティ：サンドボックス及びアイソレーション  
    - サプライチェーンセキュリティコントロール：依存関係検証  
    - モニタリング＆検知コントロール：SIEM統合  
    - インシデント対応＆リカバリー：自動化機能  
  - <strong>実装例</strong>：詳細なYAML設定ブロックとコード例を追加  
  - **Microsoftソリューション統合**：Azureセキュリティサービス、GitHub Advanced Security、エンタープライズID管理の包括的カバレッジ  

#### 高度トピックセキュリティ(05-AdvancedTopics/mcp-security/) - 製品対応実装  
- **README.md**：エンタープライズセキュリティ実装の完全再執筆  
  - <strong>現行仕様整合</strong>：MCP仕様2025-06-18準拠と必須セキュリティ要件に更新  
  - <strong>強化認証</strong>：Microsoft Entra ID統合と包括的な.NET、Java Spring Security例  
  - **AIセキュリティ統合**：Microsoft Prompt Shields及びAzure Content Safety実装、詳細なPython例付き  
  - <strong>高度脅威軽減</strong>：包括的な実装例で  
    - PKCEユーザー同意検証付きのConfused Deputy攻撃防止  
    - オーディエンス検証と安全なトークン管理によるトークンパススルー防止  
    - 暗号バインディングと行動分析によるセッションハイジャック防止  
  - <strong>エンタープライズセキュリティ統合</strong>：Azure Application Insights監視、脅威検知パイプライン、サプライチェーンセキュリティ  
  - <strong>実装チェックリスト</strong>：必須・推奨セキュリティコントロールの明確な区分とMicrosoftセキュリティエコシステムの利点  

### ドキュメント品質と標準整合  
- <strong>仕様参照</strong>：すべての参照をMCP仕様2025-06-18に更新  
- **Microsoftセキュリティエコシステム**：全セキュリティドキュメントにおける統合ガイダンス強化  
- <strong>実践的実装</strong>：.NET、Java、Pythonでの詳細なコード例とエンタープライズパターン追加  
- <strong>リソース整理</strong>：公式ドキュメント、セキュリティ基準、実装ガイドの包括的分類  
- <strong>視覚的指標</strong>：必須要件と推奨プラクティスの明確なマーキング  


#### コアコンセプト(01-CoreConcepts/) - 完全近代化  
- <strong>プロトコルバージョン更新</strong>：YYYY-MM-DD形式の日付ベースのバージョニングでMCP仕様2025-06-18を参照  
- <strong>アーキテクチャ精緻化</strong>：ホスト、クライアント、サーバの記述更新で現行MCPアーキテクチャパターンを反映  
  - ホストは複数MCPクライアント接続を調整するAIアプリケーションとして明確に定義  
  - クライアントは1対1のサーバ関係を維持するプロトコルコネクタとして説明  
  - サーバはローカル対リモート展開シナリオで強化  
- <strong>プリミティブ再構築</strong>：サーバ・クライアントプリミティブの全面改訂  
  - サーバプリミティブ：リソース（データソース）、プロンプト（テンプレート）、ツール（実行関数）の詳細解説と例付き  
  - クライアントプリミティブ：サンプリング（LLM補完）、誘発（ユーザー入力）、ログ（デバッグ／監視）  
  - 現行の発見(`*/list`)、取得(`*/get`)、実行(`*/call`)メソッドパターンで更新  
- <strong>プロトコルアーキテクチャ</strong>：2層アーキテクチャモデル導入  
  - データ層：JSON-RPC 2.0基盤、ライフサイクル管理およびプリミティブ  
  - トランスポート層：STDIO（ローカル）、Streamable HTTPとSSE（リモート）トランスポート手段  
- <strong>セキュリティフレームワーク</strong>：明確なユーザー同意、データプライバシー保護、ツール実行安全性、トランスポート層セキュリティを含む包括的原則  
- <strong>通信パターン</strong>：初期化、発見、実行、通知フローを示すプロトコルメッセージ更新  
- <strong>コード例</strong>：現行MCP SDKパターン反映の多言語例（.NET、Java、Python、JavaScript）を刷新  

#### セキュリティ(02-Security/) - 包括的セキュリティ刷新  
- <strong>基準整合</strong>：MCP仕様2025-06-18のセキュリティ要件に完全準拠  
- <strong>認証の進化</strong>：カスタムOAuthサーバから外部アイデンティティプロバイダー（Microsoft Entra ID）委譲への進化を記述  
- **AI特有の脅威分析**：現代AI攻撃ベクトルの詳細強化  
  - 実例を伴う詳細なプロンプトインジェクション攻撃シナリオ  
  - ツールポイズニング機構と「ラグプル」攻撃パターン  
  - コンテキストウィンドウポイズニングとモデル混乱攻撃  
- **Microsoft AIセキュリティソリューション**：Microsoftセキュリティエコシステムの包括的カバレッジ  
  - AI Prompt Shields：高度な検知、スポットライト、デリミタ技術  
  - Azure Content Safety統合パターン  
  - GitHub Advanced Securityによるサプライチェーン保護  
- <strong>高度脅威軽減</strong>：以下の詳細なセキュリティコントロール  
  - MCP特有のセッションハイジャック攻撃シナリオと暗号セッションID要件  
  - MCPプロキシシナリオのConfused Deputy問題と明確な同意要件  
  - トークンパススルー脆弱性に対する必須検証コントロール  
- <strong>サプライチェーンセキュリティ</strong>：基盤モデル、埋め込みサービス、コンテキストプロバイダー、第三者APIを含むAIサプライチェーンの拡張  
- <strong>基盤セキュリティ</strong>：ゼロトラストアーキテクチャやMicrosoftセキュリティエコシステムを含むエンタープライズセキュリティパターンとの統合強化  
- <strong>リソース整理</strong>：公式ドキュメント、基準、研究、Microsoftソリューション、実装ガイド別に包括的リソースリンクを分類  

### ドキュメント品質向上  
- <strong>体系的学習目標</strong>：具体的かつ実践的な成果で学習目標を強化  
- <strong>相互参照</strong>：関連セキュリティとコアコンセプトトピック間のリンク追加  
- <strong>最新情報</strong>：すべての日付参照と仕様リンクを現行標準に更新  
- <strong>実装ガイダンス</strong>：両セクションで具体的で実践可能な実装指針を追加  

## 2025年7月16日  

### READMEおよびナビゲーションの改善  
- README.mdでカリキュラムナビゲーションを全面的に再設計  
- `<details>`タグからよりアクセスしやすいテーブルベース形式へ置換  
- 新たに"alternative_layouts"フォルダを作成し代替レイアウトオプションを実装  
- カード型、タブ形式、アコーディオン形式のナビゲーション例を追加  
- 最新ファイルをすべて含むリポジトリ構造セクションを更新  
- 「このカリキュラムの使い方」セクションを明確な推奨事項と共に強化  
- MCP仕様リンクを正しいURLに更新  
- カリキュラム構成にコンテキストエンジニアリングセクション(5.14)を追加  

### 学習ガイドの更新  
- 現行リポジトリ構造に合わせて学習ガイドを全面改訂  
- MCPクライアント・ツールおよび人気のMCPサーバに関する新セクションを追加  
- ビジュアルカリキュラムマップを全トピックを正確に反映するよう更新  
- 高度トピックの説明を強化し専門領域をカバー  
- ケーススタディセクションを実例に沿って更新  
- この包括的な変更ログを追加  

### コミュニティ貢献(06-CommunityContributions/)  
- 画像生成用MCPサーバに関する詳細情報を追加  
- VSCodeでのClaude利用に関する包括的セクションを追加  
- Clineターミナルクライアントのセットアップと利用手順を追加  
- MCPクライアントセクションをすべての人気クライアントオプションを含むよう更新  
- コントリビュート例をより正確なコードサンプルで強化  

### 高度トピック(05-AdvancedTopics/)  
- すべての専門トピックフォルダを一貫した命名で整理  
- コンテキストエンジニアリング資料と例を追加  
- Foundryエージェント統合ドキュメントを追加  
- Entra IDセキュリティ統合ドキュメントを強化  

## 2025年6月11日  

### 初版作成  
- MCP for Beginnersカリキュラムの初版をリリース  
- 主要10セクションの基本構成を作成  
- ナビゲーション用のビジュアルカリキュラムマップを実装  
- 複数プログラミング言語の初期サンプルプロジェクトを追加  

### はじめに(03-GettingStarted/)  
- 初期サーバ実装例を作成  
- クライアント開発ガイダンスを追加  
- LLMクライアント統合手順を含む  
- VS Code統合ドキュメントを追加  
- Server-Sent Events（SSE）サーバ例を実装  

### コアコンセプト(01-CoreConcepts/)  
- クライアント-サーバアーキテクチャの詳細説明を追加  
- 主要プロトコルコンポーネントのドキュメントを作成  
- MCPのメッセージングパターンを文書化  

## 2025年5月23日  

### リポジトリ構造  
- 基本フォルダ構造でリポジトリを初期化  
- 各主要セクションのREADMEファイルを作成  
- 翻訳基盤を整備  
- 画像資産と図解を追加  

### ドキュメント  
- カリキュラム概要を含む初期README.mdを作成  
- CODE_OF_CONDUCT.mdおよびSECURITY.mdを追加  
- 支援ガイドを含むSUPPORT.mdを設定  
- 予備的学習ガイド構造を作成  

## 2025年4月15日  

### 計画とフレームワーク  
- MCP for Beginnersカリキュラムの初期計画  
- 学習目標と対象読者を定義  
- 10セクション構成のカリキュラム概要を策定  
- 例とケーススタディの概念フレームワークを開発  
- 主要コンセプトの初期プロトタイプ例を作成  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
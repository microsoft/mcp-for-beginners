# 🚀 開発者の生産性を変革する10のMicrosoft MCPサーバー

## 🎯 このガイドで学べること

本実践ガイドでは、AIアシスタントとの開発作業を積極的に変革している10のMicrosoft MCPサーバーをご紹介します。MCPサーバーが「何ができるか」を説明するだけでなく、Microsoftやその他の現場で実際に日々の開発フローを変えつつあるサーバーの事例を示します。

本ガイドに登場するサーバーは、実際の利用例と開発者のフィードバックを元に選定されています。各サーバーの機能だけでなく、その重要性や自身のプロジェクトで最大限に活用する方法も学べます。MCP初心者も既存の環境を拡充したい方も、本ガイドのサーバーはMicrosoftエコシステムで最も実用的かつ効果的なツールの代表例です。

> **💡 クイックスタートのヒント**
> 
> MCPが初めてでもご安心ください！本ガイドは初心者に優しい設計です。概念は順を追って解説し、より深い背景は [Introduction to MCP](../00-Introduction/README.md) や [Core Concepts](../01-CoreConcepts/README.md) モジュールをいつでも参照できます。

## 概要

本総合ガイドは、開発者がAIアシスタントや外部ツールと連携する方法を革新している10のMicrosoft MCPサーバーを解説します。Azureのリソース管理からドキュメント処理まで、これらサーバーはModel Context Protocolの力を活かし、シームレスで生産性の高い開発ワークフローを実現しています。

## 学習目標

本ガイドの終了までに、以下を習得します：
- MCPサーバーが開発者の生産性をどのように高めるか理解する
- Microsoftの最も効果的なMCPサーバーの実装事例を知る
- 各サーバーの実用的なユースケースを発見する
- VS CodeやVisual Studioでのサーバー設定と構成方法を習得する
- 広範なMCPエコシステムと将来の展望を探る

## 🔧 MCPサーバーの基礎：初心者ガイド

### MCPサーバーとは？

Model Context Protocol (MCP) 初心者の皆さんは、「MCPサーバーって何？なぜ重要なの？」と思うかもしれません。まずは簡単な例え話から始めましょう。

MCPサーバーはAIコーディングアシスタント（例：GitHub Copilot）が外部ツールやサービスと連携できるようにサポートする専門アシスタントのようなものです。スマホで天気アプリやナビアプリ、銀行アプリなどを使い分けるように、MCPサーバーはAIアシスタントに様々な開発ツールやサービスとやり取りする能力を与えます。

### MCPサーバーが解決する問題

以前は、もしあなたが：
- Azureのリソースを確認したい
- GitHubのIssueを作成したい
- データベースにクエリをしたい
- ドキュメントを検索したい

そのたびにコーディングを中断し、ブラウザでサイトにアクセスして手動で操作していました。こうしたコンテキストの頻繁な切り替えは集中を妨げ、生産性を下げてしまいます。

### MCPサーバーが変える開発体験

MCPサーバーを使えば、VS CodeやVisual Studioなどの開発環境に居ながらAIアシスタントに直接これらの作業を任せられます。例えば：

**従来のワークフローでは：**
1. コーディングを止める
2. ブラウザを開く
3. Azureポータルにアクセス
4. ストレージアカウント情報を調べる
5. VS Codeに戻る
6. コーディング再開

**今はこうできます：**
1. AIに「Azureストレージアカウントの状態は？」と聞く
2. 提供された情報を活用してコーディングを続ける

### 初心者に嬉しい主な利点

#### 1. 🔄 <strong>集中を途切れさせない</strong>
- 複数アプリの切り替え不要
- 書いているコードに集中できる
- ツール管理の精神的な負担を軽減

#### 2. 🤖 <strong>複雑なコマンドではなく自然言語で指示</strong>
- SQL文法を覚える代わりに必要なデータを説明
- Azure CLIコマンドを覚える代わりにやりたいことを伝える
- 技術的詳細はAIに任せ、論理に集中

#### 3. 🔗 <strong>複数のツールを連携</strong>
- 様々なサービスを組み合わせた強力なワークフローを作れる
- 例：「最新のGitHub Issueを取得してAzure DevOpsの作業項目を作成」
- 複雑なスクリプトを書かずに自動化を実現

#### 4. 🌐 <strong>拡大し続けるエコシステムにアクセス</strong>
- Microsoft、GitHub、他企業のサーバーを利用可能
- 異なるベンダーのツールをシームレスに組み合わせ可能
- 各種AIアシスタント横断で使える標準化されたエコシステムに参加

#### 5. 🛠️ <strong>実践しながら学べる</strong>
- 既製のサーバーからスタートして概念を理解
- 慣れてきたら自分でサーバーを作成
- 利用可能なSDKやドキュメントを活用して学習を進める

### 初心者向けの実例

初めてのWeb開発プロジェクトに取り組んでいるときのMCPサーバー活用例です：

**従来の方法：**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCPサーバー使用時：**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### エンタープライズ標準のメリット

MCPは業界標準になりつつあり、以下の意味を持ちます：
- <strong>一貫性</strong>：異なるツールや企業でも似た体験
- <strong>相互運用性</strong>：異なるベンダーのサーバーが協調動作
- <strong>将来対応</strong>：習得済みスキルやセットアップを他のAIアシスタントで活用可能
- <strong>コミュニティ</strong>：共有の知識・リソースを持つ大規模なエコシステム

### 始め方：学ぶ内容

本ガイドでは、あらゆるレベルの開発者に便利な10のMicrosoft MCPサーバーを紹介します。各サーバーは：
- よくある開発課題を解決
- 繰り返し作業を軽減
- コード品質を向上
- 学習機会を拡大

> **💡 学習のコツ**
> 
> MCPが初めての方は、まず [Introduction to MCP](../00-Introduction/README.md) と [Core Concepts](../01-CoreConcepts/README.md) のモジュールを学習しましょう。次にここに戻り、Microsoftツールでの実践例をご覧ください。
>
> MCPの重要性についての追加情報はMaria Naggagaの投稿も参考にしてください：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## VS CodeとVisual StudioでMCPを始める 🚀

GitHub Copilot付きのVisual Studio CodeやVisual Studio 2022を使えば、MCPサーバーの設定は簡単です。

### VS Codeのセットアップ

基本的な手順は以下の通りです：

1. <strong>エージェントモードを有効化</strong>：VS CodeでCopilot Chatウィンドウのエージェントモードに切り替える
2. **MCPサーバーを設定**：VS Codeのsettings.jsonにサーバーの設定を追加
3. <strong>サーバーを起動</strong>：使いたいサーバーの「Start」ボタンをクリック
4. <strong>ツールを選択</strong>：現在のセッションで有効にするMCPサーバーを選ぶ

詳細な設定手順は [VS Code MCPドキュメント](https://code.visualstudio.com/docs/copilot/copilot-mcp) を参照してください。

> **💡 プロのコツ：MCPサーバー管理を極めよう！**
> 
> VS Codeの拡張機能ビューには、[インストール済みMCPサーバーを管理する便利な新UI](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)が追加されています！インストール済みMCPサーバーを簡単に起動・停止・管理できる明快なインターフェイスです。ぜひお試しください！

### Visual Studio 2022のセットアップ

Visual Studio 2022（バージョン17.14以降）では：

1. <strong>エージェントモードを有効化</strong>：GitHub Copilot Chatウィンドウの「Ask」ドロップダウンから「Agent」を選択
2. <strong>設定ファイル作成</strong>：ソリューションディレクトリに `.mcp.json` ファイルを作成（推奨場所は `<SOLUTIONDIR>\.mcp.json`）
3. <strong>サーバーを構成</strong>：標準MCP形式でMCPサーバー設定を追加
4. <strong>ツール承認</strong>：求められたら使用したいツールのスコープ権限を承認

詳細なVisual Studio設定手順は [Visual Studio MCPドキュメント](https://learn.microsoft.com/visualstudio/ide/mcp-servers) を参照してください。

各MCPサーバーは接続文字列や認証など独自の設定要件がありますが、両IDEでセットアップパターンは一貫しています。

## Microsoft MCPサーバーから学んだ教訓 🛠️

### 1. 📚 Microsoft Learn Docs MCPサーバー

[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>機能概要</strong>：Microsoft Learn Docs MCPサーバーはクラウドホストサービスで、AIアシスタントにModel Context Protocolを通じて公式Microsoftドキュメントへのリアルタイムアクセスを提供します。`https://learn.microsoft.com/api/mcp` に接続し、Microsoft Learn、Azureドキュメント、Microsoft 365ドキュメントなど公式情報の意味検索を可能にします。

<strong>有用性</strong>：「ドキュメントだけ」と思われがちですが、Microsoft技術を使うすべての開発者にとって必須のサーバーです。多くの.NET開発者がAIコードアシスタントが最新の.NETやC#の情報を持っていないと不満を持っていますが、このサーバーは最新のドキュメント、APIリファレンス、ベストプラクティスをリアルタイムで提供することでそれを解決します。最新のAzure SDK、C# 13の新機能、先端のAspireパターンの実装など、AIアシスタントが正確かつ最新の情報に基づいてコードを生成できるように支援します。

<strong>実利用例</strong>：「Microsoft公式Learnドキュメントに従いAzureコンテナアプリを作成するaz cliコマンドは？」「ASP.NET Coreで依存性注入を使ったEntity Frameworkの設定方法は？」「このコードがMicrosoft Learnドキュメントの性能推奨に合致しているか確認して」などの質問に対応。高度な意味検索でMicrosoft Learn、Azure、Microsoft 365ドキュメント全体を対象に最も関連する情報を取得し、記事タイトルとURLを含む最大10件の高品質コンテンツを返します。公開された最新ドキュメントに常にアクセス可能です。

<strong>代表例</strong>：`microsoft_docs_search` ツールがMicrosoft公式技術ドキュメントに対して意味検索を実行します。一度設定すれば「ASP.NET CoreでJWT認証を実装するには？」などの質問に対して、詳細な公式回答とソースへのリンクを得られます。検索品質は文脈を理解しているため、Azureの「container」と質問すればAzure Container Instancesのドキュメントを、.NETの文脈ならC#のコレクション情報が返るなど高精度です。

これは急速に変化する、あるいは最近アップデートされたライブラリやユースケースで特に有効です。例えば私が最近手掛けたAspireやMicrosoft.Extensions.AIの最新リリースを利用するプロジェクトにおいて、Microsoft Learn Docs MCPサーバーを導入することでAPIドキュメントだけでなく新たに公開されたウォークスルーやガイダンスも活用できました。

> **💡 プロのコツ**
> 
> ツールへのアクセスが可能なモデルでもMCPツール使用の促しは必要です！システムプロンプトや [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) に「`microsoft.docs.mcp` へのアクセスがあるため、C#、Azure、ASP.NET Core、Entity FrameworkなどMicrosoft技術の質問時はこのツールを使って最新公式ドキュメントを検索してください」といった指示を加えると良いでしょう。
>
> これを実践した優れた例はAwesome GitHub Copilotリポジトリの [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) にあります。このモードはMicrosoft Learn Docs MCPサーバーを活用し、最新パターンとベストプラクティスに則ったC#コードのクリーンアップとモダナイズを支援します。
### 2. ☁️ Azure MCPサーバー


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>機能概要</strong>: Azure MCP サーバーは、AI ワークフローに Azure エコシステム全体を取り込むための、15以上の専門的な Azure サービスコネクターを備えた包括的なスイートです。単一のサーバーに留まらず、リソース管理、データベース接続 (PostgreSQL、SQL Server)、KQL を用いた Azure Monitor ログ解析、Cosmos DB 統合など、多彩な機能を含む強力なコレクションです。

<strong>利点</strong>: Azure リソースの管理に留まらず、このサーバーは Azure SDK を使う際のコード品質を飛躍的に向上させます。Agent モードで Azure MCP を使用すると、単にコードを書くだけでなく、現在の認証パターン、エラーハンドリングのベストプラクティスを踏まえ、最新の SDK 機能を活用したより優れた Azure コードを書く手助けができます。動作するかもしれない汎用コードではなく、Azure が推奨する本番用ワークロードのパターンに沿ったコードを得られます。

<strong>主なモジュール</strong>：
- **🗄️ データベースコネクター**: Azure Database for PostgreSQL と SQL Server への自然言語による直接アクセス
- **📊 Azure Monitor**: KQL によるログ解析と運用インサイト
- **🌐 リソース管理**: Azure リソースのライフサイクル管理全般
- **🔐 認証**: DefaultAzureCredential とマネージド アイデンティティパターン
- **📦 ストレージサービス**: Blob ストレージ、キュー ストレージ、テーブル ストレージ操作
- **🚀 コンテナーサービス**: Azure Container Apps、コンテナー インスタンス、AKS 管理
- <strong>その他多くの専門的なコネクター</strong>

<strong>実際の使用例</strong>: 「Azure ストレージアカウントを一覧表示して」、「過去1時間のエラーをログアナリティクス ワークスペースでクエリして」、「適切な認証付きで Node.js を使った Azure アプリケーションを構築する手助けをして」

<strong>完全なデモシナリオ</strong>: ここでは、Azure MCP と VS Code の GitHub Copilot for Azure 拡張機能を組み合わせた強力なデモを紹介します。両方をインストール後、以下のプロンプトを入力します：

> 「DefaultAzureCredential 認証を用いて Azure Blob Storage にファイルをアップロードする Python スクリプトを作成してください。スクリプトは 'mycompanystorage' という名前の Azure ストレージアカウントに接続し、'documents' というコンテナーにアップロードします。現在のタイムスタンプを付けたテストファイルを作成し、エラーを適切に処理し有益な出力を提供し、Azure の認証とエラーハンドリングのベストプラクティスに従い、DefaultAzureCredential の動作方法を説明するコメントを含み、適切な関数とドキュメント付きで構造化されたスクリプトにしてください。」

Azure MCP サーバーは、以下を備えた本番対応の完全な Python スクリプトを生成します：
- 最新の Azure Blob Storage SDK を適切な非同期パターンで使用
- 包括的なフォールバックチェーンの説明付き DefaultAzureCredential の実装
- 特定の Azure 例外タイプによる強力なエラーハンドリング
- Azure SDK のリソース管理と接続処理のベストプラクティスに則る
- 詳細なログ出力と有益なコンソール情報
- 関数、ドキュメント、型ヒントを含む適切に構造化されたスクリプト

この特徴的な点は、Azure MCP がなければ動作するかもしれない汎用的な Blob ストレージコードが得られるだけですが、Azure MCP があれば最新の認証方法を活用し、Azure 特有のエラー処理を行い、Microsoft が推奨する本番アプリケーション向けのプラクティスに従ったコードを得られることです。

<strong>おすすめの例</strong>: 日常的に `az` や `azd` CLI のコマンドを思い出すのに苦労してきました。いつも最初に構文を調べてからコマンドを実行する二段階手順です。記憶できない CLI 構文を認めたくなくて、ポータルに飛んでクリック操作で済ませることもよくあります。欲しいことを自然に説明できるのは素晴らしく、その上 IDE を離れずにできるのはもっと良いです！

活用例の素晴らしいリストは [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) にあります。包括的なセットアップガイドや高度な設定オプションについては、[公式 Azure MCP ドキュメント](https://learn.microsoft.com/azure/developer/azure-mcp-server/) をご覧ください。

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

<strong>機能概要</strong>: 公式の GitHub MCP サーバーは、GitHub のエコシステム全体とシームレスに統合し、ホストされたリモートアクセスとローカル Docker 展開オプションの両方を提供します。基本的なリポジトリ操作だけでなく、GitHub Actions 管理、プルリクエストワークフロー、イシュー追跡、セキュリティスキャン、通知、そして高度な自動化機能を含む包括的なツールキットです。

<strong>利点</strong>: このサーバーは、GitHub の完全なプラットフォーム体験を開発環境に直接持ち込み、GitHub.com と VS Code を行き来することなく、プロジェクト管理、コードレビュー、CI/CD モニタリングを自然言語コマンドで行えるように変革します。

> **ℹ️ 注意: 'Agent' の種類の違い**
> 
> この GitHub MCP サーバーを、GitHub の Coding Agent（自動コーディングタスク用にイシューに割り当てられる AI エージェント）と混同しないでください。GitHub MCP サーバーは VS Code の Agent モード内で GitHub API 統合を提供するのに対し、Coding Agent は GitHub イシューに割り当てられたときにプルリクエストを作成する別の機能です。

<strong>主な機能</strong>：
- **⚙️ GitHub Actions**: 完全な CI/CD パイプライン管理、ワークフローモニタリング、アーティファクト操作
- **🔀 プルリクエスト**: 作成、レビュー、マージ、詳細なステータス追跡
- **🐛 イシュー**: 全イシューのライフサイクル管理、コメント、ラベル付け、割り当て
- **🔒 セキュリティ**: コードスキャンアラート、秘密情報検出、Dependabot 統合
- **🔔 通知**: スマートな通知管理とリポジトリ購読制御
- **📁 リポジトリ管理**: ファイル操作、ブランチ管理、リポジトリアドミニストレーション
- **👥 コラボレーション**: ユーザー・組織検索、チーム管理、アクセス制御

<strong>実際の使用例</strong>: 「機能ブランチからプルリクエストを作成して」、「今週の失敗した CI 実行をすべて表示して」、「リポジトリの開いているセキュリティアラートを一覧して」、「自分に割り当てられた全てのイシューを組織横断で見つけて」

<strong>完全なデモシナリオ</strong>: GitHub MCP サーバーの機能を示す強力なワークフローはこちらです：

> 「スプリントレビューの準備をしたい。今週作成した自分のプルリクエストをすべて見せて、CI/CD パイプラインの状態をチェックし、対応が必要なセキュリティアラートの概要を作成し、'feature' ラベル付きマージ済みプルリクエストに基づいてリリースノートのドラフト作成を手伝ってほしい。」

GitHub MCP サーバーは以下を行います：
- 最近のプルリクエストを詳細なステータス情報付きで照会
- ワークフロー実行を分析し、失敗やパフォーマンス問題を強調表示
- セキュリティスキャン結果をまとめ、重要度の高いアラートを優先提示
- マージされたプルリクエストから情報を抽出し、包括的なリリースノートを生成
- スプリント計画とリリース準備のための具体的な次のステップを提示

<strong>おすすめの例</strong>: コードレビューワークフローでの利用が気に入っています。VS Code、GitHub 通知、プルリクエストページ間を行き来する代わりに、「レビュー待ちのプルリクエストをすべて見せて」と言い、「プルリクエスト #123 に認証メソッドのエラーハンドリングについてコメントを追加して」と続けるだけです。サーバーは GitHub API 呼び出しを処理し、議論のコンテキストを維持し、より建設的なレビューコメントの作成も手伝ってくれます。

<strong>認証オプション</strong>: サーバーは OAuth（VS Code 内でシームレスに利用可能）と Personal Access Tokens をサポートし、必要な GitHub 機能のみを有効化できるツールセット設定があります。リモートホストサービスとして即時セットアップや、ローカル Docker での完全制御での実行が可能です。

> **💡 プロのヒント**
> 
> コンテキストサイズを削減し AI ツールの選択を改善するため、MCP サーバー設定の `--toolsets` パラメーターで必要なツールセットのみを有効にしましょう。例えば、コア開発ワークフローなら `"--toolsets", "repos,issues,pull_requests,actions"`、主に GitHub 監視機能が欲しい場合は `"--toolsets", "notifications, security"` を MCP 構成引数に追加します。
### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

<strong>機能概要</strong>: Azure DevOps サービスに接続し、包括的なプロジェクト管理、作業項目追跡、ビルドパイプライン管理、リポジトリ操作を行います。

<strong>利点</strong>: Azure DevOps を主要な DevOps プラットフォームとして使うチームにとって、この MCP サーバーは開発環境と Azure DevOps ウェブインターフェース間の切り替えをなくします。AI アシスタントから作業項目の管理、ビルド状態の確認、リポジトリのクエリ、プロジェクト管理が直接可能です。

<strong>実際の使用例</strong>: 「WebApp プロジェクトの現在のスプリントでアクティブな作業項目をすべて見せて」、「見つけたログイン問題のバグレポートを作成して」、「ビルドパイプラインの状態をチェックし最近の失敗を表示して」

<strong>おすすめの例</strong>: 「WebApp プロジェクトの現在のスプリントにおけるアクティブな作業項目をすべて見せて」や「見つけたログイン問題のバグレポートを作成して」という単純なクエリでチームの現在スプリント状況を簡単に確認できます。開発環境を離れる必要はありません。

### 5. 📝 MarkItDown MCP Server


[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

<strong>概要</strong>: MarkItDownは、多様なファイル形式を高品質なMarkdownに変換する包括的なドキュメント変換サーバーで、LLMの利用やテキスト分析ワークフローに最適化されています。

<strong>なぜ役立つか</strong>: モダンなドキュメントワークフローに必須！MarkItDownは見出し、リスト、表、リンクなどの重要なドキュメント構造を維持しつつ、幅広いファイル形式を処理します。単なるテキスト抽出ツールとは異なり、AI処理と人間の読みやすさの両方に価値のある意味論的な意味とフォーマットの保持に焦点を当てています。

<strong>対応ファイル形式</strong>:
- **Officeドキュメント**: PDF、PowerPoint(PPTX)、Word(DOCX)、Excel(XLSX/XLS)
- <strong>メディアファイル</strong>: 画像 (EXIFメタデータとOCR付き)、音声 (EXIFメタデータと音声文字起こし付き)
- **Webコンテンツ**: HTML、RSSフィード、YouTube URL、Wikipediaページ
- <strong>データ形式</strong>: CSV、JSON、XML、ZIPファイル（内容を再帰的に処理）
- <strong>出版フォーマット</strong>: EPub、Jupyterノートブック(.ipynb)
- <strong>メール</strong>: Outlookメッセージ(.msg)
- <strong>高度な機能</strong>: Azure Document Intelligence連携による高度なPDF処理

<strong>高度な機能</strong>: MarkItDownはOpenAIクライアントを利用したLLMベースの画像説明、Azure Document IntelligenceによるPDF強化処理、音声の文字起こし、さらに追加のファイル形式に対応するプラグインシステムをサポートしています。

<strong>実際の利用例</strong>: 「このPowerPointプレゼンテーションをMarkdownに変換してドキュメントサイト用に使いたい」「このPDFから適切な見出し構造でテキストを抽出したい」「このExcelスプレッドシートを読みやすい表形式に変換したい」など

<strong>注目の例</strong>: [MarkItDownのドキュメント](https://github.com/microsoft/markitdown#why-markdown)からの引用：

> Markdownは非常にプレーンテキストに近く、最小限のマークアップやフォーマットでありながら、重要なドキュメント構造を表現する方法を提供します。OpenAIのGPT-4oなどの主流LLMはMarkdownをネイティブに「話し」、多くはプロンプトなしにMarkdownを応答に取り入れます。これは大量のMarkdownフォーマットのテキストで訓練されていることを示唆しており、その理解も深いです。副次的な利点として、Markdownの慣習はトークン効率も非常に高いです。

MarkItDownはドキュメント構造の保持に非常に優れており、AIワークフローに重要です。たとえばPowerPointプレゼンテーション変換時には、スライドの構成を正しい見出しで保持し、表をMarkdown表として抽出し、画像には代替テキストを含み、スピーカーノートも処理します。チャートは読みやすいデータ表に変換され、生成されたMarkdownは元のプレゼンテーションの論理的な流れを保ちます。これにより、プレゼンテーションの内容をAIシステムに供給したり、既存スライドからドキュメントを作成したりするのに最適です。
### 6. 🗃️ SQL Server MCP Server

[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>概要</strong>: SQL Serverデータベース（オンプレミス、Azure SQL、またはFabric）への対話型アクセスを提供

<strong>なぜ役立つか</strong>: PostgreSQLサーバーに類似していますが、Microsoft SQLエコシステム向けです。接続文字列1つで接続し、自然言語でクエリを開始できるため、コンテキスト切替が不要です！

<strong>実際の利用例</strong>: 「過去30日間に完了していない全ての注文を検索する」という自然言語クエリが適切なSQLクエリに変換され、整形された結果を返します。

<strong>注目の例</strong>: データベース接続を設定すると、すぐにデータとの対話を始められます。ブログ記事では「接続中のデータベースは何か？」という単純な質問を例示。MCPサーバーは適切なデータベースツールを呼び出し、SQL Serverインスタンスに接続し、SQL文を1行も書かずに現在のデータベース接続情報を返します。スキーマ管理からデータ操作までの完全なデータベース操作を自然言語プロンプトでサポートします。VS CodeやClaude Desktopでのセットアップ手順や構成例は[Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)をご覧ください。


### 7. 🎭 Playwright MCP Server

[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

<strong>概要</strong>: AIエージェントがウェブページでテストや自動化操作を行えるようにします

> **ℹ️ GitHub Copilotに搭載**
> 
> Playwright MCP ServerはGitHub CopilotのCoding Agentにウェブ閲覧機能を提供しています！[この機能について詳しくはこちら](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

<strong>なぜ役立つか</strong>: 自然言語の説明による自動テストに最適。AIがウェブサイトをナビゲートし、フォームに入力、アクセシビリティのスナップショットを通じてデータを抽出できるのは非常に強力です！

<strong>実際の利用例</strong>: 「ログインフローをテストして、ダッシュボードが正しく読み込まれるか検証する」や「製品検索テストを生成して結果ページを検証する」を、アプリのソースコードなしで実行可能

<strong>注目の例</strong>: 私のチームメイト、デビー・オブライエンはPlaywright MCP Serverで素晴らしい成果をあげています！たとえば、彼女は最近、アプリのソースコードを一切持たずに完全なPlaywrightテストを生成する方法を示しました。彼女のシナリオでは、映画検索アプリのテストをCopilotに依頼し、サイトにアクセスして「Garfield」で検索し、結果にその映画が表示されることを確認しました。MCPはブラウザセッションを立ち上げ、DOMスナップショットでページ構造を調べ、適切なセレクターを特定し、初回実行で合格する完全なTypeScriptテストを生成しました。

これが非常に強力なのは、自然言語の指示と実行可能なテストコードの橋渡しをしている点です。従来の方法は手動のテスト作成か、コードベースへのアクセスが必要でしたが、Playwright MCPなら外部サイト、クライアントアプリケーション、コードアクセスできないブラックボックステストも可能になります。


### 8. 💻 Dev Box MCP Server

[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>概要</strong>: Microsoft Dev Box環境を自然言語で管理

<strong>なぜ役立つか</strong>: 開発環境管理が大幅に簡素化！特定のコマンドを覚えなくても、環境の作成・設定・管理ができます。

<strong>実際の利用例</strong>: 「最新の.NET SDKを備えた新しいDev Boxを作成し、プロジェクト用に設定する」「全開発環境の状態を確認する」「チームプレゼン用の標準デモ環境を作成する」など

<strong>注目の例</strong>: 私は個人的にDev Boxを開発用途でよく使っています。ジェームズ・モンテマーニョが、Dev Boxは会議デモに最適だと説明したのが大きな気づきでした。会議やホテル、飛行機のWi-Fi環境にかかわらず超高速イーサネット接続があるからです。実際、最近もブルージュからアントワープへバスで移動しながらスマホのホットスポット経由でノートPCを接続し、会議デモ練習をしました！次の課題は複数チームの開発環境管理や標準化されたデモ環境の掘り下げです。お客様や同僚からよく聞くもう一つの大きな利用ケースは、事前構成済み開発環境としてのDev Box利用です。どちらの場合も、MCPを使った自然言語でのDev Box設定・管理により、開発環境の中にいながら対話操作が可能です。

### 9. 🤖 Microsoft Foundry MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

<strong>内容</strong>: Microsoft Foundry MCP Server は、モデルカタログ、デプロイ管理、Azure AI Search を使った知識インデクシング、評価ツールなど、Azure の AI エコシステムへの包括的なアクセスを開発者に提供します。この実験的なサーバーは、AI 開発と Azure の強力な AI インフラストラクチャの橋渡しを行い、AI アプリケーションの構築、デプロイ、評価をより簡単にします。

<strong>有用性</strong>: このサーバーは、エンタープライズグレードの AI 機能を開発ワークフローに直接取り込み、Azure AI サービスの利用方法を変革します。Azure ポータルやドキュメント、IDE 間を切り替える代わりに、自然言語コマンドでモデルの探索、サービスのデプロイ、知識ベースの管理、AI パフォーマンスの評価が可能です。特に RAG（Retrieval-Augmented Generation）アプリケーションの構築、マルチモデルデプロイの管理、総合的な AI 評価パイプラインの実装に強力です。

<strong>主な開発者向け機能</strong>:
- **🔍 モデルの探索とデプロイ**: Microsoft Foundry のモデルカタログを探索し、コードサンプル付きで詳細情報を取得、モデルを Azure AI サービスへデプロイ
- **📚 知識管理**: Azure AI Search のインデックスを作成・管理し、ドキュメントを追加、インデクサーを設定し、高度な RAG システムを構築
- **⚡ AI エージェント統合**: Azure AI エージェントと接続し、エージェントを照会し、本番環境でエージェントのパフォーマンスを評価
- **📊 評価フレームワーク**: テキストとエージェントの包括的な評価を実行、マークダウンレポートを生成し、AI アプリケーションの品質保証を実装
- **🚀 プロトタイピングツール**: GitHub ベースのプロトタイプ設置手順を取得し、Microsoft Foundry Labs の最先端研究モデルにアクセス

<strong>実際の開発者利用例</strong>: 「Phi-4 モデルを Azure AI サービスにデプロイ」、「ドキュメントの RAG システム用に新しい検索インデックスを作成」、「エージェントの応答を品質指標で評価」、「複雑な分析タスクに最適な推論モデルを探す」

<strong>フルデモシナリオ</strong>: 強力な AI 開発ワークフローをご紹介します：

> 「カスタマーサポートエージェントを開発中。カタログから良い推論モデルを探し、Azure AI サービスにデプロイし、ドキュメントから知識ベースを作成し、応答品質をテストする評価フレームワークを設定し、その後 GitHub トークンを使った統合プロトタイプ構築を手伝ってほしい。」

Microsoft Foundry MCP Server は以下を行います：
- 要件に基づいて最適な推論モデルをモデルカタログから推奨
- 希望の Azure リージョンでのデプロイコマンドとクォータ情報を提供
- ドキュメント用に適切なスキーマを持つ Azure AI Search インデックスを設定
- 品質指標と安全チェックを設定した評価パイプラインを構築
- GitHub 認証付きのプロトタイピングコードを生成し、即時テストを可能に
- 特定の技術スタックに合わせた包括的なセットアップガイドを提供

<strong>特徴的な例</strong>: 私は利用可能な異なる LLM モデルの把握に苦労してきました。主要な数モデルは知っていますが、生産性と効率の向上を逃している気がしていました。トークンとクォータの管理もストレスで、適切なモデルを選んでいるのか予算を無駄に使っているのか分からないことが多かったです。James Montemagno からこの MCP Server の話を聞いて、使うのが楽しみです！モデル発見機能は、普通のモデル以外で特定タスクに最適化されたモデルを探したい私のような人に特に魅力的です。評価フレームワークは、単に新しいことを試すだけでなく、実際に良い結果が出ているか検証するのに役立つはずです。

> **ℹ️ 実験的状況**
> 
> この MCP サーバーは実験的で、積極的に開発中です。機能や API は変わる可能性があります。Azure AI の機能探索やプロトタイプ開発に最適ですが、本番利用時は安定性の検証が必要です。
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

<strong>内容</strong>: Microsoft 365 と Microsoft 365 Copilot と連携する AI エージェントやアプリケーションを構築するために必要なツールを提供します。スキーマバリデーション、サンプルコード取得、トラブルシューティング支援などが含まれます。

<strong>有用性</strong>: Microsoft 365 と Copilot 向けの開発は複雑なマニフェストスキーマと特有の開発パターンを伴います。この MCP サーバーは、スキーマの検証、サンプルコードの検索、よくある問題のトラブルシューティングをコーディング環境内で直接支援し、ドキュメント参照の手間を軽減します。

<strong>実際の利用例</strong>: 「宣言型エージェントマニフェストの検証とスキーマエラー修正」、「Microsoft Graph API プラグイン実装用のサンプルコード提示」、「Teams アプリの認証問題のトラブルシューティング支援」

<strong>特徴的な例</strong>: Build の際に友人の John Miller に M365 Agents について話したところ、この MCP を薦めてもらいました。ドキュメントに埋もれることなく、新しい開発者が使い始めるのに最適なテンプレート、サンプルコード、スキャフォールドが提供されます。スキーマバリデーション機能は、マニフェスト構造エラーを避けるために特に役立ち、長時間のデバッグを防止できます。

> **💡 プロのコツ**
> 
> このサーバーは Microsoft Learn Docs MCP Server と併用することで、包括的な M365 開発支援が可能です。一方は公式ドキュメント、もう一方は実践的な開発ツールとトラブルシューティング支援を提供します。


## 次のステップ 🔮

## 📋 結論

モデルコンテキストプロトコル（MCP）は、開発者が AI アシスタントや外部ツールとやり取りする方法を変革しています。これら 10 の Microsoft MCP サーバーは、強力な外部機能にアクセスしながら開発者の集中状態を維持するシームレスなワークフローを実現する標準化された AI 統合の力を示しています。

包括的な Azure エコシステム統合から、Playwright によるブラウザ自動化や MarkItDown によるドキュメント処理などの専門ツールまで、これらのサーバーは多様な開発シナリオで生産性を高める MCP の利点を示しています。標準化されたプロトコルにより、これらのツールはシームレスに連携し、統一された開発体験を創出します。

MCP エコシステムが進化し続ける中で、コミュニティとの関わりを持ち、新しいサーバーを探索し、カスタムソリューションを構築することが開発生産性最大化の鍵となります。MCP のオープンスタンダードの特性により、異なるベンダーのツールを組み合わせて特定のニーズに最適なワークフローを作成できます。

## 🔗 追加リソース

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand ](https://aka.ms/mcpdevdays)

## 🎯 演習

1. <strong>インストールと設定</strong>: お好きな MCP サーバーを VS Code 環境にセットアップし、基本機能をテストしてください。
2. <strong>ワークフロー統合</strong>: 少なくとも 3 つの異なる MCP サーバーを組み合わせた開発ワークフローを設計してください。
3. <strong>カスタムサーバー計画</strong>: 日々の開発ルーチンの中でカスタム MCP サーバーが役立つタスクを特定し、その仕様を作成してください。
4. <strong>パフォーマンス分析</strong>: 一般的な開発タスクで MCP サーバー使用と従来の方法の効率を比較してください。
5. <strong>セキュリティ評価</strong>: 開発環境で MCP サーバーを使用する際のセキュリティ面の影響を評価し、ベストプラクティスを提案してください。


次へ: [Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
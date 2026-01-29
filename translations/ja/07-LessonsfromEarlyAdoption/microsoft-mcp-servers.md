# 🚀 開発者の生産性を変革する10のMicrosoft MCPサーバー

## 🎯 このガイドで学べること

この実践的なガイドでは、開発者がAIアシスタントと連携して作業する方法を変革している10のMicrosoft MCPサーバーを紹介します。MCPサーバーが「できること」を説明するだけでなく、Microsoftやその周辺で実際に日々の開発ワークフローに変化をもたらしているサーバーをお見せします。

本ガイドに登場する各サーバーは、実際の利用状況や開発者のフィードバックに基づいて選定されています。各サーバーの機能だけでなく、その重要性や自分のプロジェクトで最大限に活用する方法も学べます。MCPが初めての方も、既存の環境を拡張したい方も、これらのサーバーはMicrosoftエコシステムで最も実用的かつ影響力のあるツールの一部です。

> **💡 クイックスタートのヒント**
> 
> MCPが初めてでも安心してください！このガイドは初心者向けに設計されています。進めながら概念を説明し、必要に応じて[Introduction to MCP](../00-Introduction/README.md)や[Core Concepts](../01-CoreConcepts/README.md)のモジュールを参照して理解を深められます。

## 概要

この包括的なガイドでは、開発者がAIアシスタントや外部ツールとやり取りする方法を革新している10のMicrosoft MCPサーバーを紹介します。Azureリソース管理からドキュメント処理まで、これらのサーバーはModel Context Protocolの力を活かし、シームレスで生産的な開発ワークフローを実現しています。

## 学習目標

このガイドを終える頃には、以下が理解できるようになります：
- MCPサーバーが開発者の生産性をどのように向上させるか
- Microsoftの最も影響力のあるMCPサーバーの実装例
- 各サーバーの実用的なユースケース
- VS CodeやVisual Studioでのサーバーのセットアップと設定方法
- MCPエコシステムの全体像と今後の展望

## 🔧 MCPサーバーとは？初心者向けガイド

### MCPサーバーとは何か？

Model Context Protocol（MCP）を初めて知る方は、「MCPサーバーって何？なぜ気にする必要があるの？」と思うかもしれません。簡単な例えから始めましょう。

MCPサーバーは、AIコーディングアシスタント（GitHub Copilotなど）が外部ツールやサービスと連携するための専門的なアシスタントのようなものです。スマホで天気アプリやナビアプリ、銀行アプリを使い分けるように、MCPサーバーはAIアシスタントにさまざまな開発ツールやサービスとやり取りする能力を与えます。

### MCPサーバーが解決する問題

MCPサーバーがなかった頃は、以下のような作業をするには：
- Azureリソースの確認
- GitHubのIssue作成
- データベースへのクエリ
- ドキュメントの検索

コードを書くのを中断し、ブラウザを開いて該当サイトにアクセスし、手動で操作する必要がありました。このような頻繁なコンテキスト切り替えは作業の流れを断ち、生産性を下げてしまいます。

### MCPサーバーが開発体験をどう変えるか

MCPサーバーを使えば、VS CodeやVisual Studioなどの開発環境に留まりながら、AIアシスタントにこれらの作業を任せられます。例えば：

**従来のワークフロー：**
1. コーディングを中断
2. ブラウザを開く
3. Azureポータルにアクセス
4. ストレージアカウントの詳細を調べる
5. VS Codeに戻る
6. コーディングを再開

**今はこうできる：**
1. AIに「Azureのストレージアカウントの状況は？」と尋ねる
2. 得た情報をもとにコーディングを続ける

### 初心者にとっての主なメリット

#### 1. 🔄 **作業の流れを途切れさせない**
- 複数のアプリを行き来する必要がなくなる
- 書いているコードに集中できる
- 複数ツールの管理による精神的負担を軽減

#### 2. 🤖 **複雑なコマンドの代わりに自然言語で操作**
- SQL構文を覚えなくても必要なデータを説明すればOK
- Azure CLIコマンドを覚えなくてもやりたいことを伝えればOK
- 技術的な詳細はAIに任せて、ロジックに集中できる

#### 3. 🔗 **複数ツールを連携させる**
- 異なるサービスを組み合わせて強力なワークフローを作成
- 例：「最近のGitHub Issueをすべて取得して対応するAzure DevOpsの作業項目を作成」
- 複雑なスクリプトを書かずに自動化を実現

#### 4. 🌐 **拡大するエコシステムにアクセス**
- MicrosoftやGitHub、他社が開発したサーバーを活用
- 異なるベンダーのツールをシームレスに組み合わせ可能
- 複数のAIアシスタントで共通して使える標準化されたエコシステムに参加

#### 5. 🛠️ **実践しながら学べる**
- 既成のサーバーから始めて概念を理解
- 慣れてきたら自分でサーバーを構築
- 利用可能なSDKやドキュメントを活用して学習を進める

### 初心者向けの実例

例えば、ウェブ開発が初めてで最初のプロジェクトに取り組んでいるとします。MCPサーバーがどのように役立つか：

**従来の方法：**
```
1. 機能をコーディングする
2. ブラウザを開く → GitHub へ移動
3. テスト用の Issue を作成
4. 別のタブを開く → Azure のドキュメントでデプロイメントを確認する
5. 3 つ目のタブを開く → データベース接続の例を調べる
6. VS Code に戻る
7. 何をしていたか思い出してみる
```

**MCPサーバーを使うと：**
```
1. 機能をコーディングする
2. AIに質問する：「このログイン機能をテストするためのGitHub Issueを作成してください」
3. AIに質問する：「ドキュメントに従って、これをAzureにデプロイするにはどうすればよいですか？」
4. AIに質問する：「データベースに接続する最適な方法を教えてください」
5. 必要な情報をすべて入力してコーディングを続ける
```

### エンタープライズ標準としての利点

MCPは業界標準になりつつあり、以下のメリットがあります：
- **一貫性**：異なるツールや企業間で似た体験が得られる
- **相互運用性**：異なるベンダーのサーバーが連携可能
- **将来性**：スキルや設定が異なるAIアシスタント間で移行可能
- **コミュニティ**：豊富な知識やリソースを共有する大規模なエコシステム

### はじめに：このガイドで学べること

本ガイドでは、あらゆるレベルの開発者に役立つ10のMicrosoft MCPサーバーを紹介します。各サーバーは以下を目的としています：
- よくある開発課題の解決
- 繰り返し作業の削減
- コード品質の向上
- 学習機会の拡充

> **💡 学習のヒント**
> 
> MCPがまったく初めてなら、まず[Introduction to MCP](../00-Introduction/README.md)と[Core Concepts](../01-CoreConcepts/README.md)のモジュールから始めましょう。その後、ここに戻ってMicrosoftの実際のツールで概念を体験してください。
>
> MCPの重要性についてはMaria Naggagaの投稿も参考にしてください：[Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)。

## VS CodeとVisual StudioでのMCPの始め方 🚀

GitHub Copilotを使っている場合、これらのMCPサーバーのセットアップは簡単です。

### VS Codeのセットアップ

基本的な手順は以下の通りです：

1. **エージェントモードを有効化**：VS CodeのCopilot Chatウィンドウでエージェントモードに切り替え
2. **MCPサーバーの設定**：VS Codeのsettings.jsonにサーバー設定を追加
3. **サーバー起動**：使いたいサーバーの「Start」ボタンをクリック
4. **ツール選択**：現在のセッションで有効にするMCPサーバーを選択

詳細なセットアップ手順は[VS Code MCPドキュメント](https://code.visualstudio.com/docs/copilot/copilot-mcp)を参照してください。

> **💡 プロのヒント：MCPサーバーをスマートに管理！**
> 
> VS Codeの拡張機能ビューに[インストール済みMCPサーバーを管理する便利なUI](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)が追加されました！起動・停止・管理が簡単にできるのでぜひ試してみてください。

### Visual Studio 2022のセットアップ

Visual Studio 2022（バージョン17.14以降）では：

1. **エージェントモードを有効化**：GitHub Copilot Chatウィンドウの「Ask」ドロップダウンから「Agent」を選択
2. **設定ファイル作成**：ソリューションディレクトリに`.mcp.json`ファイルを作成（推奨場所：`<SOLUTIONDIR>\.mcp.json`）
3. **サーバー設定**：標準のMCPフォーマットでサーバー設定を追加
4. **ツール承認**：使用するツールを適切なスコープ権限で承認

詳細は[Visual Studio MCPドキュメント](https://learn.microsoft.com/visualstudio/ide/mcp-servers)を参照してください。

各MCPサーバーは接続文字列や認証など独自の設定が必要ですが、両IDEでセットアップの流れは共通しています。

## Microsoft MCPサーバーからの教訓 🛠️

### 1. 📚 Microsoft Learn Docs MCPサーバー

[![VS Codeにインストール](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![VS Code Insidersにインストール](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**機能**：Microsoft Learn Docs MCPサーバーはクラウドホスト型サービスで、Model Context Protocolを通じてAIアシスタントにMicrosoft公式ドキュメントへのリアルタイムアクセスを提供します。`https://learn.microsoft.com/api/mcp`に接続し、Microsoft Learn、Azureドキュメント、Microsoft 365ドキュメントなどの公式情報をセマンティック検索で横断できます。

**有用性**：単なる「ドキュメント」以上の価値があります。AIコーディングアシスタントに関して.NET開発者からよく聞く不満の一つは、最新の.NETやC#のリリースに追いついていないことです。このサーバーは最新のドキュメント、APIリファレンス、ベストプラクティスにリアルタイムでアクセスできるため、その問題を解決します。最新のAzure SDKやC# 13の新機能、最先端の.NET Aspireパターンを扱う際も、AIアシスタントが正確で最新の情報を参照してコード生成できるようにします。

**実際の利用例**：「公式Microsoft Learnドキュメントに基づくAzureコンテナアプリ作成のaz cliコマンドは？」「ASP.NET Coreで依存性注入を使ったEntity Frameworkの設定方法は？」「このコードがMicrosoft Learnのパフォーマンス推奨に合っているかレビューして」など。サーバーはMicrosoft Learn、Azureドキュメント、Microsoft 365ドキュメントを対象に高度なセマンティック検索を行い、文脈に最も合った情報を最大10件の高品質なコンテンツチャンク（記事タイトルとURL付き）で返します。常に最新のドキュメントにアクセスしています。

**注目の例**：`microsoft_docs_search`ツールを公開しており、Microsoftの公式技術ドキュメントに対するセマンティック検索を実行します。設定後は「ASP.NET CoreでJWT認証を実装するには？」といった質問に対し、詳細かつ公式の回答とソースリンクを得られます。検索の質は文脈理解に優れており、Azureの「containers」ならAzure Container Instancesのドキュメントを、.NETの「containers」ならC#のコレクション情報を返します。

これは特に急速に変化する、または最近更新されたライブラリやユースケースで役立ちます。例えば、最近のプロジェクトで.NET AspireやMicrosoft.Extensions.AIの最新機能を活用したい場合、Microsoft Learn Docs MCPサーバーを組み込むことでAPIドキュメントだけでなく、新しく公開されたチュートリアルやガイダンスも活用できました。
> **💡 プロのコツ**
> 
> ツール対応モデルでも、MCPツールを使うには励ましが必要です！システムプロンプトや [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) に「`microsoft.docs.mcp` にアクセスできます。C#、Azure、ASP.NET Core、Entity FrameworkなどのMicrosoft技術に関する質問を扱う際は、このツールを使ってMicrosoftの最新公式ドキュメントを検索してください。」といった内容を追加することを検討してください。
>
> 実際の活用例としては、Awesome GitHub Copilotリポジトリの [C# .NET Janitorチャットモード](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) をご覧ください。このモードは特にMicrosoft Learn Docs MCPサーバーを活用し、最新のパターンやベストプラクティスを使ってC#コードのクリーンアップとモダナイズを支援します。
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**概要**: Azure MCP Serverは、15以上の専門的なAzureサービスコネクターを備えた包括的なスイートで、Azureのエコシステム全体をAIワークフローに統合します。単なるサーバーではなく、リソース管理、データベース接続（PostgreSQL、SQL Server）、KQLを使ったAzure Monitorログ解析、Cosmos DB統合など、多彩な機能を持つ強力なコレクションです。

**なぜ便利か**: Azureリソースの管理だけでなく、Azure SDKを使った開発時のコード品質を大幅に向上させます。AgentモードでAzure MCPを使うと、単にコードを書く手助けをするだけでなく、最新の認証パターンやエラーハンドリングのベストプラクティスに沿った、より良いAzureコードを生成します。動作するだけの一般的なコードではなく、本番環境向けに推奨されるAzureのパターンに従ったコードが得られます。

**主なモジュール**:
- **🗄️ データベースコネクター**: Azure Database for PostgreSQLとSQL Serverへの自然言語による直接アクセス
- **📊 Azure Monitor**: KQLを活用したログ解析と運用インサイト
- **🌐 リソース管理**: Azureリソースのライフサイクル全体の管理
- **🔐 認証**: DefaultAzureCredentialとマネージドIDパターン
- **📦 ストレージサービス**: Blob Storage、Queue Storage、Table Storageの操作
- **🚀 コンテナサービス**: Azure Container Apps、Container Instances、AKSの管理
- **その他多数の専門的なコネクター**

**実際の利用例**: 「Azureのストレージアカウントを一覧表示して」「過去1時間のLog Analyticsワークスペースのエラーをクエリして」「Node.jsで適切な認証を使ったAzureアプリケーションの構築を手伝って」

**フルデモシナリオ**: Azure MCPとGitHub Copilot for Azure拡張機能をVS Codeに両方インストールした状態で、以下のようにプロンプトを入力すると：

> 「DefaultAzureCredential認証を使ってAzure Blob StorageにファイルをアップロードするPythonスクリプトを作成してください。スクリプトは'mycompanystorage'という名前のAzureストレージアカウントに接続し、'documents'というコンテナにアップロードします。現在のタイムスタンプを使ったテストファイルを作成し、エラー処理は丁寧に行い、情報をわかりやすく出力してください。認証とエラーハンドリングはAzureのベストプラクティスに従い、DefaultAzureCredential認証の仕組みを説明するコメントを含め、関数やドキュメントで構造化されたスクリプトにしてください。」

Azure MCP Serverは以下を満たす、完全な本番対応のPythonスクリプトを生成します：
- 最新のAzure Blob Storage SDKを使い、適切な非同期パターンを実装
- DefaultAzureCredentialを包括的なフォールバックチェーンの説明付きで実装
- Azure固有の例外タイプを含む堅牢なエラーハンドリング
- Azure SDKのベストプラクティスに沿ったリソース管理と接続処理
- 詳細なログ出力とわかりやすいコンソール表示
- 関数、ドキュメント、型ヒントを備えた適切に構造化されたスクリプト

Azure MCPがない場合、動作はするものの最新のAzureパターンに沿わない一般的なBlob Storageコードが生成されることがありますが、Azure MCPを使うことで最新の認証方法を活用し、Azure特有のエラー処理を行い、Microsoft推奨の本番環境向けプラクティスに従ったコードが得られます。

**注目の例**: `az`や`azd` CLIのコマンドを覚えておくのが苦手で、いつもまず構文を調べてからコマンドを実行する二段階作業になってしまいます。CLIの構文を覚えていないことを認めたくなくて、ポータルに入ってクリックで作業を済ませることも多いです。欲しいことを自然言語で伝えられるのは素晴らしく、しかもIDEを離れずにできるのはさらに便利です！

[Azure MCPリポジトリ](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server)には使い始めに役立つユースケースのリストがあります。セットアップガイドや高度な設定オプションについては、[公式Azure MCPドキュメント](https://learn.microsoft.com/azure/developer/azure-mcp-server/)を参照してください。

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**概要**: 公式のGitHub MCP Serverは、GitHubのエコシステム全体とシームレスに統合し、ホスト型のリモートアクセスとローカルDocker展開の両方に対応しています。単なるリポジトリ操作だけでなく、GitHub Actions管理、プルリクエストワークフロー、イシュートラッキング、セキュリティスキャン、通知、そして高度な自動化機能を備えた包括的なツールキットです。

**なぜ便利か**: GitHubとのやり取りを開発環境内に取り込み、VS CodeとGitHub.comを行き来する手間を省きます。プロジェクト管理、コードレビュー、CI/CDの監視を自然言語コマンドで行い、コードに集中したまますべてを処理できます。

> **ℹ️ 注意: 'Agents'の種類について**
> 
> このGitHub MCP Serverは、GitHubのCoding Agent（イシューに割り当てて自動コーディングを行うAIエージェント）とは異なります。GitHub MCP ServerはVS CodeのAgentモードでGitHub API統合を提供し、Coding AgentはGitHubイシューに割り当てられた際にプルリクエストを作成する別機能です。

**主な機能**:
- **⚙️ GitHub Actions**: CI/CDパイプライン管理、ワークフローモニタリング、アーティファクト処理
- **🔀 プルリクエスト**: PRの作成、レビュー、マージ、ステータス管理
- **🐛 イシュー**: イシューのライフサイクル管理、コメント、ラベル付け、担当割り当て
- **🔒 セキュリティ**: コードスキャンアラート、シークレット検出、Dependabot連携
- **🔔 通知**: スマート通知管理とリポジトリ購読制御
- **📁 リポジトリ管理**: ファイル操作、ブランチ管理、リポジトリ管理
- **👥 コラボレーション**: ユーザー・組織検索、チーム管理、アクセス制御

**実際の利用例**: 「機能ブランチからプルリクエストを作成して」「今週の失敗したCI実行をすべて表示して」「リポジトリの未解決セキュリティアラートを一覧表示して」「自分に割り当てられた全イシューを組織横断で探して」

**フルデモシナリオ**: GitHub MCP Serverの機能を示す強力なワークフロー例：

> 「スプリントレビューの準備が必要です。今週自分が作成したプルリクエストをすべて表示し、CI/CDパイプラインの状況を確認し、対応すべきセキュリティアラートの概要を作成し、'feature'ラベルが付いたマージ済みPRを元にリリースノートの草案を手伝ってください。」

GitHub MCP Serverは以下を実行します：
- 最近のプルリクエストを詳細なステータス情報付きで取得
- ワークフロー実行を分析し、失敗やパフォーマンス問題を強調表示
- セキュリティスキャン結果をまとめ、重要なアラートを優先表示
- マージ済みPRから情報を抽出し、包括的なリリースノートを生成
- スプリント計画とリリース準備のための具体的な次のステップを提案

**注目の例**: コードレビューのワークフローで重宝しています。VS Code、GitHub通知、プルリクエストページを行き来する代わりに、「レビュー待ちのPRをすべて見せて」と言い、「PR #123に認証メソッドのエラーハンドリングについてコメントを追加して」と続けるだけで済みます。サーバーがGitHub APIを操作し、会話の文脈を保持し、より建設的なレビューコメントの作成も支援してくれます。

**認証オプション**: OAuth（VS Codeでシームレス）とPersonal Access Tokenの両方をサポートし、必要なGitHub機能だけを有効にするツールセット設定が可能です。リモートホスト型サービスとして即時セットアップできるほか、Dockerを使ったローカル展開で完全な制御も可能です。

> **💡 プロのコツ**
> 
> MCPサーバー設定の`--toolsets`パラメーターで必要なツールセットだけを有効にし、コンテキストサイズを減らしてAIツールの選択を最適化しましょう。例えば、コア開発ワークフローには`"--toolsets", "repos,issues,pull_requests,actions"`を、GitHubの監視機能中心なら`"--toolsets", "notifications, security"`を指定します。

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**概要**: Azure DevOpsサービスに接続し、プロジェクト管理、作業項目トラッキング、ビルドパイプライン管理、リポジトリ操作を包括的にサポートします。

**なぜ便利か**: Azure DevOpsを主要なDevOpsプラットフォームとして使うチームにとって、開発環境とAzure DevOpsのWebインターフェースを行き来する手間を省きます。作業項目の管理、ビルド状況の確認、リポジトリのクエリ、プロジェクト管理タスクをAIアシスタントから直接行えます。

**実際の利用例**: 「WebAppプロジェクトの現在のスプリントでアクティブな作業項目をすべて表示して」「今見つけたログイン問題のバグレポートを作成して」「ビルドパイプラインの状況を確認し、最近の失敗を教えて」

**注目の例**: 「WebAppプロジェクトの現在のスプリントでアクティブな作業項目をすべて表示して」や「今見つけたログイン問題のバグレポートを作成して」といった簡単なクエリで、開発環境を離れずにチームのスプリント状況を簡単に把握できます。

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**概要**: MarkItDownは、多様なファイル形式を高品質なMarkdownに変換する包括的なドキュメント変換サーバーで、LLMの利用やテキスト解析ワークフローに最適化されています。

**なぜ便利か**: 現代のドキュメントワークフローに欠かせません！MarkItDownは見出し、リスト、表、リンクなど重要なドキュメント構造を保持しつつ、幅広いファイル形式に対応します。単なるテキスト抽出ツールとは異なり、AI処理や人間の可読性に価値のある意味的な情報とフォーマットを維持することに重点を置いています。

**対応ファイル形式**:
- **Officeドキュメント**: PDF、PowerPoint (PPTX)、Word (DOCX)、Excel (XLSX/XLS)
- **メディアファイル**: 画像（EXIFメタデータとOCR対応）、音声（EXIFメタデータと音声文字起こし対応）
- **ウェブコンテンツ**: HTML、RSSフィード、YouTube URL、Wikipediaページ
- **データ形式**: CSV、JSON、XML、ZIPファイル（内容を再帰的に処理）
- **出版フォーマット**: EPub、Jupyterノートブック（.ipynb）
- **メール**: Outlookメッセージ（.msg）
- **高度な機能**: Azure Document Intelligence連携によるPDF処理の強化

**高度な機能**: OpenAIクライアントを利用したLLMによる画像説明、Azure Document IntelligenceによるPDF処理強化、音声文字起こし、追加ファイル形式対応のためのプラグインシステムをサポートしています。

**実際の利用例**: 「このPowerPointプレゼンテーションをドキュメントサイト用のMarkdownに変換」「このPDFから適切な見出し構造でテキストを抽出」「このExcelスプレッドシートを読みやすい表形式に変換」など。

**注目の例**: [MarkItDownドキュメント](https://github.com/microsoft/markitdown#why-markdown)からの引用：

> Markdownはほぼプレーンテキストに近く、最小限のマークアップやフォーマットで重要なドキュメント構造を表現できます。OpenAIのGPT-4oなどの主流LLMはMarkdownをネイティブに「理解」し、しばしば無意識にMarkdown形式で応答します。これは大量のMarkdownテキストで学習されていることを示し、Markdownのトークン効率の良さも副次的な利点です。

MarkItDownはドキュメント構造の保持に優れており、AIワークフローに重要です。例えばPowerPoint変換時には、スライドの構成を適切な見出しで保持し、表はMarkdown表として抽出、画像には代替テキストを含め、スピーカーノートも処理します。チャートは読みやすいデータ表に変換され、結果のMarkdownは元のプレゼンテーションの論理的な流れを維持します。これにより、プレゼン内容をAIシステムに取り込んだり、既存スライドからドキュメントを作成したりするのに最適です。

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**概要**: SQL Serverデータベース（オンプレミス、Azure SQL、Fabric）への対話型アクセスを提供します。

**なぜ便利か**: PostgreSQLサーバーに似ていますが、Microsoft SQLエコシステム向けです。シンプルな接続文字列で接続し、自然言語でクエリを実行できるため、コンテキスト切り替えが不要になります！

**実際の利用例**: 「過去30日間に未処理の注文をすべて見つける」という自然言語が適切なSQLクエリに変換され、整形された結果が返されます。

**注目の例**: データベース接続を設定すれば、すぐにデータとの対話が始められます。ブログ記事では「どのデータベースに接続していますか？」という簡単な質問で紹介されています。MCPサーバーは適切なデータベースツールを呼び出し、SQL Serverインスタンスに接続し、現在のデータベース接続情報を返します。SQL文を一行も書かずに済みます。スキーマ管理からデータ操作まで、自然言語プロンプトで包括的なデータベース操作をサポートします。VS CodeやClaude Desktopでのセットアップ手順や設定例は[Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)をご覧ください。

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**概要**: AIエージェントがウェブページと対話し、テストや自動化を行えるようにします。

> **ℹ️ GitHub Copilotの原動力**
> 
> Playwright MCP ServerはGitHub CopilotのCoding Agentにウェブブラウジング機能を提供しています！[この機能の詳細はこちら](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)。

**なぜ便利か**: 自然言語の説明で駆動される自動テストに最適です。AIはウェブサイトをナビゲートし、フォームに入力し、構造化されたアクセシビリティスナップショットを通じてデータを抽出できます。非常に強力な機能です！

**実際の利用例**: 「ログインフローをテストし、ダッシュボードが正しく読み込まれるか確認」や「商品検索のテストを生成し、結果ページを検証」など、アプリのソースコード不要で実行可能です。

**注目の例**: チームメイトのDebbie O'Brienは最近Playwright MCP Serverで素晴らしい成果を上げています。例えば、アプリのソースコードにアクセスせずに完全なPlaywrightテストを生成する方法を示しました。彼女のシナリオでは、映画検索アプリで「Garfield」を検索し、結果に映画が表示されることを検証するテストをCopilotに依頼。MCPはブラウザセッションを起動し、DOMスナップショットでページ構造を解析、適切なセレクターを特定し、初回実行で成功する完全なTypeScriptテストを生成しました。

この機能の強みは、自然言語の指示と実行可能なテストコードの橋渡しをする点です。従来は手動でテストを書くか、コードベースへのアクセスが必要でしたが、Playwright MCPなら外部サイトやクライアントアプリ、コードアクセスがないブラックボックステストも可能です。

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**概要**: Microsoft Dev Box環境を自然言語で管理します。

**なぜ便利か**: 開発環境の管理が格段に簡単に！特定のコマンドを覚えなくても、開発環境の作成、設定、管理が可能です。

**実際の利用例**: 「最新の.NET SDKを搭載した新しいDev Boxをセットアップし、プロジェクト用に設定」「すべての開発環境の状態を確認」「チームプレゼン用の標準化されたデモ環境を作成」など。

**注目の例**: 私は個人開発でDev Boxを愛用しています。James MontemagnoがDev Boxの素晴らしさを説明してくれたのがきっかけで、特にカンファレンスのデモに最適だと感じました。なぜなら、会場やホテル、飛行機のWi-Fi環境に関わらず超高速イーサネット接続が使えるからです。実際、最近はブルージュからアントワープへバス移動中にスマホのホットスポットに繋いでカンファレンスデモの練習をしました！次のステップは、複数の開発環境をチームで管理したり、標準化されたデモ環境を構築したりすることです。顧客や同僚からよく聞くもう一つの大きな用途は、事前設定済みの開発環境としてDev Boxを使うことです。どちらの場合も、MCPを使って自然言語でDev Boxを設定・管理できるので、開発環境から離れずに操作できます。

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**概要**: Azure AI Foundry MCP Serverは、モデルカタログ、デプロイ管理、Azure AI Searchによるナレッジインデックス作成、評価ツールなど、AzureのAIエコシステムへの包括的なアクセスを開発者に提供します。この実験的なサーバーは、AI開発とAzureの強力なAIインフラストラクチャの橋渡しを行い、AIアプリケーションの構築、デプロイ、評価をより簡単にします。

**利点**: このサーバーは、エンタープライズレベルのAI機能を開発ワークフローに直接取り込むことで、Azure AIサービスの利用方法を変革します。Azureポータルやドキュメント、IDEを行き来する代わりに、自然言語コマンドでモデルの検索、サービスのデプロイ、ナレッジベースの管理、AIパフォーマンスの評価が可能です。特にRAG（Retrieval-Augmented Generation）アプリケーションの開発、多モデルデプロイの管理、包括的なAI評価パイプラインの実装に強力です。

**主な開発者向け機能**:
- **🔍 モデルの検索とデプロイ**: Azure AI Foundryのモデルカタログを探索し、コードサンプル付きの詳細情報を取得、Azure AI Servicesへモデルをデプロイ
- **📚 ナレッジ管理**: Azure AI Searchのインデックス作成・管理、ドキュメント追加、インデクサー設定、複雑なRAGシステムの構築
- **⚡ AIエージェント連携**: Azure AI Agentsとの接続、既存エージェントへのクエリ、実運用でのエージェント性能評価
- **📊 評価フレームワーク**: テキストおよびエージェント評価の実行、マークダウンレポート生成、AIアプリケーションの品質保証実装
- **🚀 プロトタイピングツール**: GitHubベースのプロトタイピングセットアップ手順の提供と、最先端研究モデルを扱うAzure AI Foundry Labsへのアクセス

**実際の開発者利用例**: 「Phi-4モデルをAzure AI Servicesにデプロイしてアプリに組み込む」「ドキュメント用の新しい検索インデックスを作成する」「エージェントの応答を品質指標で評価する」「複雑な分析タスクに最適な推論モデルを探す」

**フルデモシナリオ**: 強力なAI開発ワークフローの例:


> 「カスタマーサポートエージェントを作っています。カタログから良い推論モデルを探し、Azure AI Servicesにデプロイし、ドキュメントからナレッジベースを作成し、応答品質をテストする評価フレームワークを設定して、最後にGitHubトークンを使った統合のプロトタイプ作成を手伝ってください。」

Azure AI Foundry MCP Serverは以下を行います：
- 要件に基づき最適な推論モデルをモデルカタログから推薦
- 希望のAzureリージョン向けのデプロイコマンドとクォータ情報を提供
- ドキュメント用に適切なスキーマでAzure AI Searchインデックスを設定
- 品質指標と安全チェックを含む評価パイプラインを構築
- GitHub認証付きのプロトタイピングコードを生成し即時テスト可能に
- 特定の技術スタックに合わせた包括的なセットアップガイドを提供

**注目の例**: 開発者として、様々なLLMモデルを追いかけるのは大変でした。主要なものは知っているものの、生産性や効率向上のチャンスを逃している気がしていました。トークンやクォータの管理もストレスで、適切なモデル選択ができているか不安でした。今回、チームメイトとMCP Serverの話をしている時にJames MontemagnoからこのMCP Serverを知り、使うのが楽しみです！モデル検索機能は、私のように定番以外のモデルを探して特定タスクに最適化されたものを見つけたい人に特に魅力的です。評価フレームワークは、単に新しいことを試すだけでなく、実際に成果が出ているか検証するのに役立ちそうです。

> **ℹ️ 実験的ステータス**
> 
> このMCPサーバーは実験段階であり、現在も活発に開発中です。機能やAPIは変更される可能性があります。Azure AIの機能を試したりプロトタイプを作るには最適ですが、本番利用時は安定性を十分に検証してください。

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**概要**: Microsoft 365およびMicrosoft 365 Copilotと連携するAIエージェントやアプリケーションの開発に必要なツールを提供します。スキーマ検証、サンプルコード取得、トラブルシューティング支援が含まれます。

**利点**: Microsoft 365やCopilot向けの開発は複雑なマニフェストスキーマや特有の開発パターンが必要です。このMCPサーバーは、スキーマ検証やサンプルコードの検索、よくある問題のトラブルシューティングをコーディング環境内で直接行えるようにし、ドキュメントを頻繁に参照する手間を減らします。

**実際の利用例**: 「宣言型エージェントマニフェストの検証とスキーマエラーの修正」「Microsoft Graph APIプラグイン実装のサンプルコードを見せて」「Teamsアプリの認証問題のトラブルシューティングを手伝って」

**注目の例**: BuildでM365 Agentsについて話した際に友人のJohn Millerに相談し、このMCPを勧められました。M365 Agents初心者にとって、テンプレートやサンプルコード、スキャフォールディングが提供されているので、ドキュメントに埋もれずに始められるのが良いと思います。特にマニフェスト構造のエラーを防ぐスキーマ検証機能は、数時間のデバッグを避けるのに役立ちそうです。

> **💡 プロのヒント**
> 
> このサーバーはMicrosoft Learn Docs MCP Serverと併用すると、包括的なM365開発サポートが得られます。公式ドキュメントはLearn Docs MCPが提供し、こちらは実践的な開発ツールとトラブルシューティング支援を担います。

## 次は？ 🔮

## 📋 まとめ

Model Context Protocol (MCP)は、開発者がAIアシスタントや外部ツールとやり取りする方法を変革しています。これら10のMicrosoft MCPサーバーは、標準化されたAI統合の力を示し、開発者が強力な外部機能にアクセスしながら作業の流れを途切れさせずに済むシームレスなワークフローを実現します。

包括的なAzureエコシステム統合から、ブラウザ自動化のPlaywrightやドキュメント処理のMarkItDownなどの専門ツールまで、これらのサーバーは多様な開発シナリオで生産性を向上させるMCPの可能性を示しています。標準化されたプロトコルにより、これらのツールは連携して動作し、一貫した開発体験を作り出します。

MCPエコシステムが進化し続ける中、コミュニティとの交流、新しいサーバーの探索、カスタムソリューションの構築が開発生産性を最大化する鍵となります。MCPのオープンスタンダードな性質により、異なるベンダーのツールを組み合わせて、自分のニーズに最適なワークフローを作り上げることが可能です。

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

1. **インストールと設定**: VS Code環境にMCPサーバーのいずれかをセットアップし、基本機能をテストする。
2. **ワークフロー統合**: 少なくとも3つの異なるMCPサーバーを組み合わせた開発ワークフローを設計する。
3. **カスタムサーバー計画**: 日常の開発作業でカスタムMCPサーバーが役立ちそうなタスクを特定し、その仕様を作成する。
4. **パフォーマンス分析**: MCPサーバーを使った場合と従来の方法での開発作業効率を比較する。
5. **セキュリティ評価**: 開発環境でMCPサーバーを使用する際のセキュリティ上の影響を評価し、ベストプラクティスを提案する。

次へ: [MCP開発のベストプラクティス](../08-BestPractices/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。

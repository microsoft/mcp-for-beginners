# 実践的な実装

[![How to Build, Test, and Deploy MCP Apps with Real Tools and Workflows](../../../translated_images/ja/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_（上の画像をクリックすると、このレッスンのビデオが表示されます）_

実践的な実装は、Model Context Protocol（MCP）の力が具体化する場所です。MCPの理論やアーキテクチャを理解することは重要ですが、実際にこれらの概念を適用して現実の問題を解決するソリューションを構築、テスト、デプロイするときに真の価値が現れます。この章では、概念的な知識とハンズオン開発のギャップを埋め、MCPベースのアプリケーションを実現するプロセスを案内します。

インテリジェントアシスタントの開発、ビジネスワークフローへのAI統合、データ処理のカスタムツール構築など、MCPは柔軟な基盤を提供します。言語非依存の設計と人気のあるプログラミング言語向けの公式SDKにより、幅広い開発者に利用可能です。これらのSDKを活用することで、異なるプラットフォームや環境で迅速にプロトタイピング、反復、スケーリングが可能になります。

以下のセクションでは、C#、Java（Spring付き）、TypeScript、JavaScript、PythonでのMCP実装の実例、サンプルコード、デプロイ戦略を紹介します。また、MCPサーバーのデバッグとテスト、API管理、Azureを使ったクラウドデプロイについても学びます。これらのハンズオンリソースは、学習を加速し、堅牢で本番対応可能なMCPアプリケーションを自信を持って構築できるよう設計されています。

## 概要

このレッスンは、複数のプログラミング言語にわたるMCP実装の実践的側面に焦点を当てています。C#、Java（Spring付き）、TypeScript、JavaScript、PythonのMCP SDKを使って堅牢なアプリケーションを構築し、MCPサーバーのデバッグとテスト、リソース・プロンプト・ツールの再利用可能な作成方法を探ります。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- 公式SDKを使って様々なプログラミング言語でMCPソリューションを実装する
- MCPサーバーを体系的にデバッグおよびテストする
- サーバー機能（リソース、プロンプト、ツール）を作成し利用する
- 複雑なタスクに対する効果的なMCPワークフローを設計する
- パフォーマンスと信頼性を最適化したMCP実装を行う

## 公式SDKリソース

Model Context Protocolは、複数言語の公式SDKを提供しています（[MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)準拠）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **注:** [Project Reactor](https://projectreactor.io)への依存が必要です。（[ディスカッション Issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246)を参照）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDKを使った開発

このセクションでは複数言語におけるMCP実装の実例を紹介します。`samples`ディレクトリに各言語別のサンプルコードがあります。

### 利用可能なサンプル

リポジトリには以下の言語での[サンプル実装](../../../04-PracticalImplementation/samples)が含まれています：

- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

各サンプルは特定の言語・エコシステム向けのMCPの主要概念と実装パターンを示します。

### 実践ガイド

追加の実践的なMCP実装ガイド：

- [ページネーションと大規模結果セット](./pagination/README.md) - ツール、リソース、大規模データセットのカーソルベースページネーションの処理

## コアサーバー機能

MCPサーバーは以下の機能の任意の組み合わせを実装できます：

### リソース

リソースはユーザーやAIモデルが使用するコンテキストやデータを提供します：

- ドキュメントリポジトリ
- ナレッジベース
- 構造化データソース
- ファイルシステム

### プロンプト

プロンプトはユーザー向けのテンプレート化されたメッセージやワークフローです：

- 事前定義された会話テンプレート
- ガイド付きインタラクションパターン
- 特殊な対話構造

### ツール

ツールはAIモデルが実行する関数です：

- データ処理ユーティリティ
- 外部API連携
- 計算機能
- 検索機能

## サンプル実装：C# 実装

公式C# SDKリポジトリには、MCPの異なる側面を示す複数のサンプル実装が含まれています：

- **基本的なMCPクライアント**：MCPクライアントの作成とツール呼び出しの単純例
- **基本的なMCPサーバー**：基本的なツール登録を含む最小限のサーバー実装
- **高度なMCPサーバー**：ツール登録、認証、エラーハンドリングを備えたフル機能のサーバー
- **ASP.NET連携**：ASP.NET Coreとの統合例
- **ツール実装パターン**：さまざまな複雑度のツール実装パターン集

C# MCP SDKはプレビュー段階であり、APIは変更される可能性があります。SDKの進化に合わせて本ブログを継続的に更新します。

### 主な特徴

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [はじめてのMCPサーバー構築](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

C#の完全な実装サンプルは、[公式C# SDKサンプルリポジトリ](https://github.com/modelcontextprotocol/csharp-sdk)を参照してください。

## サンプル実装：Java with Spring 実装

Java with Spring SDKはエンタープライズ対応機能を備えた堅牢なMCP実装オプションを提供します。

### 主な特徴

- Spring Frameworkとの統合
- 強力な型安全性
- リアクティブプログラミング対応
- 包括的なエラーハンドリング

完全なJava with Spring実装サンプルは、サンプルディレクトリ内の[Java with Springサンプル](samples/java/containerapp/README.md)を参照してください。

## サンプル実装：JavaScript 実装

JavaScript SDKは軽量で柔軟なMCP実装アプローチを提供します。

### 主な特徴

- Node.jsおよびブラウザ対応
- PromiseベースAPI
- Expressなどのフレームワークとの簡単な統合
- ストリーミング向けWebSocketサポート

完全なJavaScript実装サンプルはサンプルディレクトリの[JavaScriptサンプル](samples/javascript/README.md)を参照してください。

## サンプル実装：Python 実装

Python SDKはPythonらしいMCP実装アプローチを取り、優れたMLフレームワーク連携を提供します。

### 主な特徴

- asyncioによるasync/awaitサポート
- FastAPI統合
- シンプルなツール登録
- 人気のMLライブラリとのネイティブ統合

完全なPython実装サンプルはサンプルディレクトリの[Pythonサンプル](samples/python/README.md)を参照してください。

## API管理

Azure API ManagementはMCPサーバーをセキュアに保つための優れたソリューションです。アイデアは、Azure API ManagementインスタンスをMCPサーバーの前に置き、以下のような望ましい機能を担当させることです：

- レート制限
- トークン管理
- 監視
- ロードバランシング
- セキュリティ

### Azureサンプル

こちらはAzure API ManagementでMCPサーバーを作成しセキュア化するサンプルです：[MCPサーバーのAzure API Managementによるセキュア化](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

認証フローが以下の画像のように行われます：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

この画像で行われていること：

- Microsoft Entraによる認証／認可が行われる
- Azure API Managementがゲートウェイとして働き、ポリシーでトラフィックを制御管理
- Azure Monitorがすべてのリクエストをログに記録し分析に役立てる

#### 認可フロー

認可フローを詳細に見てみましょう：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP認可仕様

[MCP認可仕様](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)について詳しく学べます。

## リモートMCPサーバーのAzureへのデプロイ

先に述べたサンプルをデプロイしてみましょう：

1. リポジトリをクローン

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. `Microsoft.App` リソースプロバイダーを登録します。

   - Azure CLIを使う場合は、`az provider register --namespace Microsoft.App --wait`を実行します。
   - Azure PowerShell使用時は`Register-AzResourceProvider -ProviderNamespace Microsoft.App`を実行し、しばらくしてから`(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`で登録状態を確認します。

1. この[azd](https://aka.ms/azd)コマンドを実行し、API管理サービス、関数アプリ（コード含む）、その他必要なAzureリソースをプロビジョニングします。

    ```shell
    azd up
    ```

    このコマンドはAzure上のすべてのクラウドリソースをデプロイします。

### MCP Inspectorでサーバーをテスト

1. **新しいターミナルウィンドウ**でMCP Inspectorをインストールして起動します。

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    以下のようなインターフェースが表示されるはずです：

    ![Connect to Node inspector](../../../translated_images/ja/connect.141db0b2bd05f096.webp)

1. 表示されるURL（例：[http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）からMCP InspectorのWebアプリをCTRL＋クリックで開きます。
1. トランスポートタイプを`SSE`に設定します。
1. 実行中のAPI管理のSSEエンドポイントURLを`azd up`の後に表示されるものに設定し、**接続**をクリックします。

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **ツール一覧**を表示し、ツールを選択して**ツールを実行**します。

すべてのステップが成功すれば、MCPサーバーに接続されツール呼び出しができています。

## Azure向けMCPサーバー

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): これはPython、C# .NET、Node/TypeScriptでAzure Functionsを使い、カスタムのリモートMCPサーバーを構築・デプロイするためのクイックスタートテンプレートです。

このサンプルは開発者に完全なソリューションを提供し、以下を可能にします：

- ローカルで構築・実行: ローカルマシンでMCPサーバーの開発とデバッグ
- Azureへのデプロイ: シンプルな`azd up`コマンドでクラウドへ簡単デプロイ
- クライアントからの接続: VS CodeのCopilotエージェントモードやMCP Inspectorツールなど多様なクライアントからMCPサーバーに接続

### 主な特徴

- セキュリティを考慮した設計: MCPサーバーはキーとHTTPSで保護
- 認証オプション: 組み込み認証やAPI Managementを使ったOAuth対応
- ネットワーク分離: Azure Virtual Networks（VNET）によるネットワーク分離が可能
- サーバーレスアーキテクチャ: Azure Functionsを活用したスケーラブルなイベント駆動実行
- ローカル開発: 包括的なローカル開発・デバッグサポート
- 簡単なデプロイ: Azureへの展開プロセスが簡素化

リポジトリには、本番対応可能なMCPサーバー実装を素早く開始するための必要な構成ファイル、ソースコード、インフラ定義がすべて含まれています。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) — Pythonを使ったAzure FunctionsによるMCP実装サンプル
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) — C# .NETを使ったAzure FunctionsによるMCP実装サンプル
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) — Node/TypeScriptを使ったAzure FunctionsによるMCP実装サンプル

## まとめ

- MCP SDKは言語特有のツールを提供し、堅牢なMCPソリューションの実装を支援します。
- デバッグとテストのプロセスは信頼性の高いMCPアプリケーションに不可欠です。
- 再利用可能なプロンプトテンプレートにより一貫したAIインタラクションを可能にします。
- 洗練されたワークフローにより、複数のツールを使った複雑なタスクをオーケストレーションできます。
- MCPソリューション実装にはセキュリティ、性能、エラーハンドリングへの配慮が必要です。

## 演習

自分のドメインでの現実的な問題を解決する実践的なMCPワークフローを設計してみましょう：

1. この問題解決に役立つ3～4個のツールを特定する
2. これらのツールがどのように連携するかを示すワークフローダイアグラムを作成する
3. 好みの言語でツールの基本バージョンを実装する
4. モデルが効果的にツールを利用するためのプロンプトテンプレートを作成する

## 追加リソース

---

## 次へ

次： [Advanced Topics](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」(https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナルの文書が正本としての権威ある情報源となります。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用に起因するいかなる誤解や誤訳に対しても責任を負いかねますので、ご了承ください。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
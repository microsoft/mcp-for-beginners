# 実践的な実装

[![実際のツールとワークフローを使ったMCPアプリの構築、テスト、デプロイ方法](../../../translated_images/ja/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_（上の画像をクリックすると、このレッスンのビデオが視聴できます）_

実践的な実装は、Model Context Protocol (MCP) の力が具体的に現れる部分です。MCPの理論やアーキテクチャの理解は重要ですが、これらの概念を適用して実際の問題を解決するソリューションを構築し、テストし、デプロイすることで真の価値が生まれます。本章は、概念的な知識と実践的な開発の間のギャップを埋め、MCPベースのアプリケーションを実際に具現化するプロセスをガイドします。

インテリジェントアシスタントの開発、ビジネスワークフローへのAI統合、データ処理のためのカスタムツール構築など、どのような用途であっても、MCPは柔軟な基盤を提供します。その言語非依存の設計と人気のプログラミング言語向けの公式SDKにより、多様な開発者がアクセス可能です。これらのSDKを活用することで、異なるプラットフォームや環境にわたって迅速にプロトタイピング、繰り返し開発、スケーリングが可能になります。

以下のセクションでは、C#、Springを使ったJava、TypeScript、JavaScript、PythonにおけるMCPの実装、サンプルコード、デプロイ戦略を紹介します。また、MCPサーバのデバッグとテスト、API管理、Azureを使ったクラウドへのデプロイ方法についても学びます。これらの実践的なリソースは、学習を加速し、堅牢で本番用のMCPアプリケーションを自信を持って構築できるよう設計されています。

## 概要

このレッスンでは、複数のプログラミング言語に渡るMCP実装の実践的な側面に焦点を当てます。C#、Springを使ったJava、TypeScript、JavaScript、PythonのMCP SDKを使い、堅牢なアプリケーションの構築、MCPサーバのデバッグとテスト、再利用可能なリソースやプロンプト、ツールの作成方法を探ります。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- 公式SDKを使用して様々なプログラミング言語でMCPソリューションを実装する
- MCPサーバを体系的にデバッグおよびテストする
- サーバ機能（リソース、プロンプト、ツール）を作成し活用する
- 複雑なタスクのための効果的なMCPワークフローを設計する
- パフォーマンスと信頼性のためにMCP実装を最適化する

## 公式SDKリソース

Model Context Protocolは、複数の言語向けに公式SDKを提供しています（[MCP仕様 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) に準拠）：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Springを使ったJava SDK](https://github.com/modelcontextprotocol/java-sdk) **注意:** [Project Reactor](https://projectreactor.io) への依存が必要です。([ディスカッション 246](https://github.com/orgs/modelcontextprotocol/discussions/246) を参照)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDKの利用

このセクションでは、複数のプログラミング言語でのMCP実装の実践的な例を紹介します。`samples` ディレクトリに言語別のサンプルコードがあります。

### 利用可能なサンプル

リポジトリには以下の言語での[サンプル実装](../../../04-PracticalImplementation/samples)があります：

- [C#](./samples/csharp/README.md)
- [Springを使ったJava](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

各サンプルは、特定言語およびエコシステム向けの主要なMCPの概念と実装パターンを示しています。

### 実践ガイド

実用的なMCP実装のための追加ガイド：

- [ページネーションと大規模結果セット](./pagination/README.md) - ツール、リソース、および大規模データセットに対するカーソルベースページネーションの処理方法

## コアサーバ機能

MCPサーバは以下の機能の組み合わせを実装できます：

### リソース

リソースはユーザーまたはAIモデルのためのコンテキストとデータを提供します：

- ドキュメントリポジトリ
- ナレッジベース
- 構造化データソース
- ファイルシステム

### プロンプト

プロンプトはユーザーのためのテンプレート化されたメッセージとワークフローです：

- 事前定義された会話テンプレート
- ガイド付きインタラクションパターン
- 特殊な対話構造

### ツール

ツールはAIモデルが実行可能な機能です：

- データ処理ユーティリティ
- 外部API統合
- 計算能力
- 検索機能

## サンプル実装：C#実装

公式のC# SDKリポジトリには、MCPの様々な側面を示す複数のサンプル実装があります：

- **基本的なMCPクライアント**：MCPクライアントの作成方法とツール呼び出しの簡単な例
- **基本的なMCPサーバ**：ツール登録を含む最小限のサーバ実装
- **高度なMCPサーバ**：ツール登録、認証、エラー処理を備えたフル機能サーバ
- **ASP.NET統合**：ASP.NET Coreとの統合例
- **ツール実装パターン**：さまざまな複雑度のツール実装パターン

MCP C# SDKはプレビュー段階でありAPIが変更される可能性があります。SDKの進化を受けて当ブログも継続的に更新していきます。

### 主な機能

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [最初のMCPサーバ構築](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

C#の完全な実装サンプルは、[公式C# SDKサンプルリポジトリ](https://github.com/modelcontextprotocol/csharp-sdk) をご覧ください。

## サンプル実装：Springを使ったJava実装

Springを使ったJava SDKは、エンタープライズグレードの機能を備えた堅牢なMCP実装オプションを提供します。

### 主な機能

- Spring Framework統合
- 強力な型安全性
- リアクティブプログラミング対応
- 包括的なエラー処理

完全なJava with Springの実装サンプルは、samplesディレクトリの[Java with Springサンプル](samples/java/containerapp/README.md)を参照してください。

## サンプル実装：JavaScript実装

JavaScript SDKは、軽量で柔軟なMCP実装アプローチを提供します。

### 主な機能

- Node.jsおよびブラウザ対応
- PromiseベースのAPI
- Expressなどのフレームワークとの容易な統合
- ストリーミング用のWebSocketサポート

JavaScriptの完全な実装サンプルは、samplesディレクトリの[JavaScriptサンプル](samples/javascript/README.md)をご覧ください。

## サンプル実装：Python実装

Python SDKは、Python的手法で優れたMLフレームワーク統合を特徴とするMCP実装を提供します。

### 主な機能

- asyncioによるAsync/awaitサポート
- FastAPI統合
- シンプルなツール登録
- 人気のMLライブラリとのネイティブ統合

Pythonの完全な実装サンプルは、samplesディレクトリの[Pythonサンプル](samples/python/README.md)をご覧ください。

## API管理

Azure API ManagementはMCPサーバをセキュアにするための優れたソリューションです。アイデアは、MCPサーバの前にAzure API Managementインスタンスを置き、以下のような機能を提供することです：

- レートリミット
- トークン管理
- 監視
- 負荷分散
- セキュリティ

### Azureサンプル

Azureサンプルでは、まさにこれを実現しています。つまり [MCPサーバを作成しAzure API Managementで保護する](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) 例です。

以下の画像で認証フローが確認できます：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

上記画像では以下が行われています：

- Microsoft Entraを使用した認証／認可
- Azure API Managementがゲートウェイとして動作し、ポリシーによりトラフィックを管理
- Azure Monitorがすべてのリクエストをログ記録し、解析に活用

#### 認可フロー

認可フローの詳細を見てみましょう：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP認可仕様

[MCP認可仕様](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/) を詳しく学びましょう

## AzureへのリモートMCPサーバのデプロイ

先述のサンプルをデプロイしてみましょう：

1. リポジトリをクローン

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. `Microsoft.App` リソースプロバイダーを登録します。

   - Azure CLIを使っている場合は、 `az provider register --namespace Microsoft.App --wait` を実行。
   - Azure PowerShellを使っている場合は、 `Register-AzResourceProvider -ProviderNamespace Microsoft.App` を実行。しばらくしてから `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` で登録が完了しているか確認。

1. この[azd](https://aka.ms/azd)コマンドを実行してAPI管理サービス、関数アプリ（コード付き）、その他必要なAzureリソースをプロビジョニング

    ```shell
    azd up
    ```

    このコマンドによりAzure上のクラウドリソースがすべてデプロイされるはずです。

### MCP Inspectorによるサーバのテスト

1. **新しいターミナルウィンドウで**、MCP Inspectorをインストールして実行

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    以下のようなインターフェースが表示されるはずです：

    ![Node inspectorに接続](../../../translated_images/ja/connect.141db0b2bd05f096.webp)

1. アプリケーションに表示されたURL（例：[http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）を CTRLクリックしてMCP Inspectorウェブアプリを読み込み
1. トランスポートタイプを `SSE` に設定
1. azd up後に表示された実行中のAPI管理のSSEエンドポイントをURL欄に入力し、**接続**。

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **ツール一覧表示**。ツールをクリックして **ツールを実行**。

すべての手順が正しく実行されていれば、MCPサーバに接続しツールを呼び出せているはずです。

## Azure向けMCPサーバ

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：このリポジトリ群は、Python、C# .NET、Node/TypeScriptを使用してAzure FunctionsでカスタムリモートMCP（Model Context Protocol）サーバを構築・デプロイするためのクイックスタートテンプレートです。

このサンプルは開発者に以下を可能にします：

- ローカルで構築と実行：ローカルマシン上でMCPサーバを開発・デバッグ
- Azureへのデプロイ：単純なazd upコマンドでクラウドに簡単デプロイ
- クライアントからの接続：VS CodeのCopilotエージェントモードやMCP Inspectorツールなど多様なクライアントから接続

### 主な機能

- セキュリティ設計：MCPサーバはキーとHTTPSで保護
- 認証オプション：組み込み認証やAPI管理を使ったOAuth対応
- ネットワーク分離：Azure Virtual Network (VNET) によるネットワーク分離対応
- サーバーレスアーキテクチャ：スケーラブルなイベント駆動実行にAzure Functionsを活用
- ローカル開発：包括的なローカル開発・デバッグサポート
- 簡単デプロイメント：Azureへのシンプルなデプロイプロセス

本リポジトリは本番用MCPサーバ実装を素早く始めるための設定ファイル、ソースコード、インフラ定義をすべて含みます。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Pythonを使用したAzure FunctionsでのMCP実装サンプル
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NETを使用したAzure FunctionsでのMCP実装サンプル
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScriptを使用したAzure FunctionsでのMCP実装サンプル

## 重要なポイント

- MCP SDKは言語特化のツールを提供し堅牢なMCPソリューション実装を支援
- デバッグとテスト工程は信頼性の高いMCPアプリのために必須
- 再利用可能なプロンプトテンプレートは一貫したAI対話を可能にする
- よく設計されたワークフローは複数ツールを使った複雑なタスクを調整
- MCP実装時にはセキュリティ、パフォーマンス、エラーハンドリングを考慮する必要がある

## 演習

あなたのドメインでの実世界問題に対処する実践的なMCPワークフローを設計してください：

1. この問題解決に有用な3〜4つのツールを特定する
2. これらツールの相互作用を示すワークフローダイアグラムを作成する
3. 好みの言語でツールの基本バージョンを実装する
4. モデルが効果的にツールを使うためのプロンプトテンプレートを作成する

## 追加リソース

---

## 次に進む

次： [高度なトピック](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる場合があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な内容については、専門の人間による翻訳をお勧めします。本翻訳の利用により生じたいかなる誤解や誤訳についても当方は一切責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
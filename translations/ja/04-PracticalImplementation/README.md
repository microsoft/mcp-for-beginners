# 実践的な実装

[![実際のツールとワークフローを使用したMCPアプリの構築、テスト、デプロイ方法](../../../translated_images/ja/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(このレッスンのビデオを見るには上の画像をクリックしてください)_

実践的な実装は、Model Context Protocol (MCP) の力が具体的に感じられる場面です。MCPの理論やアーキテクチャを理解することは重要ですが、実際にこれらの概念を適用して、現実の問題を解決するソリューションを構築、テスト、デプロイすることで本当の価値が生まれます。この章では、概念的な知識と実際の開発のギャップを埋め、MCPを基にしたアプリケーションを実際に作り上げるプロセスを案内します。

インテリジェントアシスタントの開発、AIのビジネスワークフローへの統合、カスタムデータ処理ツールの構築など、どのような場合でもMCPは柔軟な基盤を提供します。その言語非依存の設計と、人気のプログラミング言語向けの公式SDKにより、多くの開発者にアクセス可能です。これらのSDKを活用すれば、異なるプラットフォームや環境で迅速にプロトタイプを作成し、反復し、スケールさせることができます。

次のセクションでは、C#、Java with Spring、TypeScript、JavaScript、PythonでのMCP実装の実例、サンプルコード、デプロイ戦略を紹介します。また、MCPサーバーのデバッグとテスト、API管理、Azureを使ったクラウドへのソリューションデプロイ方法についても学びます。これらの実践的なリソースは学習を加速し、自信を持って堅牢で本番対応可能なMCPアプリケーションを構築する助けとなります。

## 概要

本レッスンは複数のプログラミング言語にわたるMCP実装の実践的な側面に焦点を当てています。C#、Java with Spring、TypeScript、JavaScript、PythonでのMCP SDKの使用方法、堅牢なアプリケーションの構築、MCPサーバーのデバッグとテスト、再利用可能なリソース、プロンプト、ツールの作成方法を探ります。

## 学習目標

このレッスン終了時には、以下ができるようになります：

- 公式SDKを使用したMCPソリューションの実装（複数のプログラミング言語で）
- MCPサーバーの体系的なデバッグとテスト
- サーバー機能（リソース、プロンプト、ツール）の作成と利用
- 複雑なタスクのための効果的なMCPワークフローの設計
- パフォーマンスと信頼性を考慮したMCP実装の最適化

## 公式SDKリソース

Model Context Protocolは複数の言語向けの公式SDKを提供しています。SDKの
MCP `2026-07-28` のサポートは独立して展開されるため、各SDKの
リリースノートと例のパッケージバージョンを確認してからプロトコルの
互換性を仮定してください。[公式SDKリスト](https://modelcontextprotocol.io/docs/sdk)を参照してください：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **注意:** [Project Reactor](https://projectreactor.io)への依存が必要です。（[ディスカッションissue 246](https://github.com/orgs/modelcontextprotocol/discussions/246)参照）
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDKでの作業

このセクションでは、複数のプログラミング言語にわたるMCPの実装例を紹介します。サンプルコードは言語別に整理された`samples`ディレクトリにあります。

### 利用可能なサンプル

リポジトリには以下の言語での[サンプル実装](../../../04-PracticalImplementation/samples)が含まれています：


- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

各サンプルは、その特定の言語とエコシステムにおける主要なMCPの概念と実装パターンを示しています。

### 実践ガイド

実践的なMCP実装のための追加ガイド：

- [ページネーションと大規模結果セット](./pagination/README.md) - ツール、リソース、大規模データセットのカーソルベースのページネーションを扱う方法

## コアサーバー機能

MCPサーバーはこれらの機能の任意の組み合わせを実装できます：

### リソース

リソースはユーザーまたはAIモデルが使用するためのコンテキストとデータを提供します：

- ドキュメントリポジトリ
- ナレッジベース
- 構造化データソース
- ファイルシステム

### プロンプト

プロンプトはユーザーのためのテンプレート化されたメッセージとワークフローです：

- 事前定義された会話テンプレート
- ガイド付きインタラクションパターン
- 専門的な対話構造

### ツール

ツールはAIモデルが実行するための関数です：

- データ処理ユーティリティ
- 外部API統合
- 計算機能
- 検索機能

## サンプル実装：C#実装

公式のC# SDKリポジトリには、MCPの異なる側面を示すいくつかのサンプル実装が含まれています：

- **基本的なMCPクライアント**：MCPクライアントの作成とツール呼び出しの簡単な例
- **基本的なMCPサーバー**：基本的なツール登録を備えた最小限のサーバー実装
- **高度なMCPサーバー**：ツール登録、認証、エラーハンドリングを備えたフル機能サーバー
- **ASP.NET統合**：ASP.NET Coreとの統合を示す例
- <strong>ツール実装パターン</strong>：異なる複雑さのツールを実装するためのさまざまなパターン

MCP C# SDKはプレビュー段階であり、APIは変更される可能性があります。SDKの進化に伴い、このブログを継続的に更新していきます。

### 主な特徴

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [最初のMCPサーバーの構築](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

完全なC#実装サンプルについては、[公式C# SDKサンプルリポジトリ](https://github.com/modelcontextprotocol/csharp-sdk)をご覧ください。

## サンプル実装：Java with Spring実装

Java with Spring SDKは、エンタープライズグレードの機能を備えた堅牢なMCP実装オプションを提供します。

### 主な特徴

- Spring Framework統合
- 強力な型安全性
- リアクティブプログラミングサポート
- 包括的なエラーハンドリング

完全なJava with Spring実装サンプルは、samplesディレクトリの[Java with Spring sample](samples/java/containerapp/README.md)をご覧ください。

## サンプル実装：JavaScript実装

JavaScript SDKは軽量で柔軟なMCP実装アプローチを提供します。

### 主な特徴

- Node.jsとブラウザ対応
- PromiseベースのAPI
- Expressやその他のフレームワークとの簡単な統合
- ストリーミング向けWebSocketサポート

完全なJavaScript実装サンプルは、samplesディレクトリの[JavaScript sample](samples/javascript/README.md)をご覧ください。

## サンプル実装：Python実装

Python SDKは優れたMLフレームワーク統合を備え、PythonらしいMCP実装アプローチを提供します。

### 主な特徴

- asyncioによるAsync/awaitサポート
- FastAPI統合
- シンプルなツール登録
- 人気のあるMLライブラリとのネイティブ統合

完全なPython実装サンプルは、samplesディレクトリの[Python sample](samples/python/README.md)をご覧ください。


## API 管理


Azure API Management は、MCP サーバーをどのようにセキュリティで保護するかに対する優れた回答です。考え方は、Azure API Management インスタンスを MCP サーバーの前に配置し、以下のような必要とされそうな機能を担当させることです：

- レート制限
- トークン管理
- 監視
- 負荷分散
- セキュリティ

### Azure サンプル

ここに、まさにそれを行う Azure サンプルがあります。すなわち [MCP サーバーを作成し Azure API Management で保護する](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) 例です。

以下の画像で認可フローの流れをご覧ください：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

前述の画像では、以下のことが行われています：

- 認証/認可は Microsoft Entra を使用して実施されます。
- Azure API Management はゲートウェイとして機能し、ポリシーを使ってトラフィックを制御・管理します。
- Azure Monitor はすべてのリクエストをログに記録し、さらなる解析を行います。

#### 認可フロー

認可フローを詳細に見てみましょう：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 認可仕様

詳しくはこちらの
[MCP 認可仕様](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/)をご覧ください。

## リモート MCP サーバーを Azure にデプロイ

先ほどのサンプルをデプロイしてみましょう：

1. リポジトリをクローン

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. `Microsoft.App` リソースプロバイダーを登録します。

   - Azure CLI を使用している場合は、`az provider register --namespace Microsoft.App --wait` を実行します。
   - Azure PowerShell を使用している場合は、`Register-AzResourceProvider -ProviderNamespace Microsoft.App` を実行します。登録が完了しているか後で `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` を実行して確認してください。

1. この [azd](https://aka.ms/azd) コマンドを実行して、API Management サービス、Function App（コード付き）、およびその他必要な Azure リソースをプロビジョニングします

    ```shell
    azd up
    ```

    このコマンドは Azure 上のすべてのクラウドリソースをデプロイするはずです

### MCP Inspector でサーバーをテストする

1. <strong>新しいターミナルウィンドウ</strong>で MCP Inspector をインストールして実行します

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    次のようなインターフェースが表示されるはずです：

    ![Connect to Node inspector](../../../translated_images/ja/connect.141db0b2bd05f096.webp)

1. アプリに表示される URL（例: [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)）から MCP Inspector Web アプリを CTRL クリックしてロードします
1. トランスポートタイプを `SSE` に設定します
1. `azd up` 実行後に表示される、実行中の API Management SSE エンドポイントの URL を設定して <strong>接続</strong> します：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. <strong>ツール一覧</strong>。ツールをクリックして <strong>ツールを実行</strong> してください。  

すべての手順が成功すれば、MCP サーバーに接続され、ツールを呼び出せるようになっています。

## Azure 向け MCP サーバー

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): これは Azure Functions を使って Python、C# .NET、または Node/TypeScript でリモート MCP（Model Context Protocol）サーバーをビルドおよびデプロイするためのクイックスタートテンプレート群です。

このサンプルは、開発者に以下の包括的なソリューションを提供します：

- ローカルでのビルドと実行：ローカルマシンで MCP サーバーを開発およびデバッグ
- Azure へのデプロイ：簡単な azd up コマンドでクラウドへデプロイ
- クライアントからの接続：VS Code の Copilot エージェントモードや MCP Inspector ツールなど様々なクライアントから MCP サーバーへ接続可能

### 主要機能

- 設計段階からのセキュリティ：キーと HTTPS による MCP サーバーのセキュリティ保護
- 認証オプション：組み込み認証および/または API Management を用いた OAuth をサポート
- ネットワーク分離：Azure Virtual Networks（VNET）を利用したネットワーク分離をサポート
- サーバーレスアーキテクチャ：スケーラブルなイベント駆動実行のため Azure Functions を活用
- ローカル開発のサポート：包括的なローカル開発およびデバッグ支援
- 簡単なデプロイ：Azure へのストリームライン化されたデプロイプロセス

リポジトリには、生産準備が整った MCP サーバーの実装を迅速に始めるための、必要なすべての設定ファイル、ソースコード、インフラ定義が含まれています。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions を使った Python による MCP サンプル実装

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Azure Functions を使った C# .NET による MCP サンプル実装

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Azure Functions を使った Node/TypeScript による MCP サンプル実装

## 重要なポイント

- MCP SDK は堅牢な MCP ソリューション実装のための言語別ツールを提供
- デバッグおよびテストプロセスは信頼性ある MCP アプリケーションに不可欠
- 再利用可能なプロンプトテンプレートは一貫したAIインタラクションを可能にする
- よく設計されたワークフローは複数ツールを使った複雑なタスクをオーケストレーションできる
- MCP ソリューションの実装はセキュリティ、パフォーマンス、エラーハンドリングを考慮する必要がある

## 演習

あなたのドメインにおける実世界の問題に対応する実用的な MCP ワークフローを設計してください：

1. この問題解決に役立つ 3〜4 個のツールを特定する
2. これらツールの相互作用を示すワークフローダイアグラムを作成する
3. お好みの言語を使い、1つのツールの基本バージョンを実装する
4. モデルが効果的にツールを使うためのプロンプトテンプレートを作成する

## 追加リソース

---

## 次に学ぶこと

次へ: [Advanced Topics](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
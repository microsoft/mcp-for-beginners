# ChainlitとMicrosoft Learn Docs MCPを使った学習計画ジェネレーター

## 前提条件

- Python 3.8以上
- pip（Pythonパッケージマネージャー）
- Microsoft Learn Docs MCPサーバーに接続するためのインターネットアクセス

## インストール

1. このリポジトリをクローンするか、プロジェクトファイルをダウンロードします。
2. 必要な依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### シナリオ1: Docs MCPへの簡単なクエリ
Docs MCPサーバーに接続し、クエリを送信して結果を表示するコマンドラインクライアント。

1. スクリプトを実行します：
   ```bash
   python scenario1.py
   ```
2. プロンプトでドキュメントに関する質問を入力します。

### シナリオ2: 学習計画ジェネレーター（Chainlit Webアプリ）
Chainlitを使用したウェブベースのインターフェイスで、技術的なトピックに基づいた個別の週ごとの学習計画を生成できます。

1. Chainlitアプリを起動します：
   ```bash
   chainlit run scenario2.py
   ```
2. ターミナルに表示されるローカルURL（例: http://localhost:8000）をブラウザで開きます。
3. チャットウィンドウで学習トピックと学習期間（例: "AI-900認定試験、8週間"）を入力します。
4. アプリが週ごとの学習計画を返し、関連するMicrosoft Learnドキュメントへのリンクを含めて表示します。

**必要な環境変数:**

シナリオ2（Azure OpenAIを使用したChainlit Webアプリ）を利用するには、以下の環境変数を`python`ディレクトリ内の`.env`ファイルに設定する必要があります：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

これらの値をAzure OpenAIリソースの詳細で埋めた後、アプリを実行してください。

> [!TIP]
> [Azure AI Foundry](https://ai.azure.com/)を使用して、独自のモデルを簡単にデプロイできます。

### シナリオ3: VS CodeでMCPサーバーを使ったドキュメント参照

ブラウザタブを切り替えることなく、Microsoft Learn Docsを直接VS Codeに取り込むことができます。これにより以下が可能になります：
- コーディング環境を離れることなく、VS Code内でドキュメントを検索・閲覧。
- ドキュメントを参照し、リンクをREADMEやコースファイルに直接挿入。
- GitHub CopilotとMCPを組み合わせて、AIを活用したドキュメントワークフローを実現。

**使用例:**
- コースやプロジェクトドキュメントを作成中に、READMEに参照リンクを素早く追加。
- Copilotでコードを生成し、MCPで関連するドキュメントを即座に検索・引用。
- エディタ内で集中力を維持し、生産性を向上。

> [!IMPORTANT]
> ワークスペースに有効な[`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json)構成ファイルが必要です（場所は`.vscode/mcp.json`）。

## シナリオ2にChainlitを選んだ理由

Chainlitは、会話型ウェブアプリケーションを構築するための最新のオープンソースフレームワークです。Microsoft Learn Docs MCPサーバーなどのバックエンドサービスに接続するチャットベースのユーザーインターフェイスを簡単に作成できます。このプロジェクトではChainlitを使用して、リアルタイムで個別の学習計画を生成するシンプルでインタラクティブな方法を提供しています。Chainlitを活用することで、生産性と学習を向上させるチャットベースのツールを迅速に構築・デプロイできます。

## このアプリの機能

ユーザーがトピックと期間を入力するだけで、個別の学習計画を作成できます。アプリは入力内容を解析し、Microsoft Learn Docs MCPサーバーに関連コンテンツをクエリし、結果を週ごとの計画に整理します。各週の推奨事項はチャット内に表示され、進捗を簡単に追跡できます。この統合により、最新で最も関連性の高い学習リソースを常に取得できます。

## サンプルクエリ

チャットウィンドウで以下のクエリを試して、アプリの応答を確認してください：

- `AI-900認定試験、8週間`
- `Azure Functionsを学ぶ、4週間`
- `Azure DevOps、6週間`
- `Azureでのデータエンジニアリング、10週間`
- `Microsoftセキュリティ基礎、5週間`
- `Power Platform、7週間`
- `Azure AIサービス、12週間`
- `クラウドアーキテクチャ、9週間`

これらの例は、さまざまな学習目標や期間に対するアプリの柔軟性を示しています。

## 参考資料

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤認について、当社は一切の責任を負いません。
# Weather MCP サーバー

これは、モックレスポンスを使用した天気ツールを実装するPythonのサンプルMCPサーバーです。自身のMCPサーバーの足がかりとして利用できます。以下の機能が含まれています：

- **Weather Tool**：指定された場所に基づいてモックされた天気情報を提供するツール。
- **Agent Builderとの接続**：テストやデバッグのためにMCPサーバーをAgent Builderに接続できる機能。
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)でのデバッグ**：MCP Inspectorを使用してMCPサーバーをデバッグできる機能。

## Weather MCPサーバーテンプレートの始め方

> <strong>前提条件</strong>
>
> ローカル開発環境でMCPサーバーを実行するには、以下が必要です：
>
> - [Python](https://www.python.org/)
> - (*任意 - uvを利用する場合*) [uv](https://github.com/astral-sh/uv)
> - [Pythonデバッガー拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 環境の準備

このプロジェクトの環境設定には2つの方法があります。お好みに応じていずれかを選択してください。

> 注意：仮想環境を作成した後、VSCodeまたはターミナルを再読み込みして仮想環境のPythonが使用されるようにしてください。

| 方法 | 手順 |
| -------- | ----- |
| `uv`を使用 | 1. 仮想環境を作成：`uv venv` <br>2. VSCodeコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択 <br>3. 依存関係（開発依存を含む）をインストール：`uv pip install -r pyproject.toml --extra dev` |
| `pip`を使用 | 1. 仮想環境を作成：`python -m venv .venv` <br>2. VSCodeコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係（開発依存を含む）をインストール：`pip install -e .[dev]` | 

環境設定後は、ローカル開発機でAgent BuilderをMCPクライアントとして使用してサーバーを起動できます：
1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder`を選択するか、`F5`キーを押してMCPサーバーのデバッグを開始します。
2. Microsoft Foundry Toolkit Agent Builderを使用し、[このプロンプト](../../../../../../../../../../../open_prompt_builder)でサーバーをテストします。サーバーは自動的にAgent Builderに接続されます。
3. `Run`をクリックしてプロンプトでサーバーをテストします。

<strong>おめでとうございます</strong>！Agent BuilderをMCPクライアントとして使用し、ローカル開発機上でWeather MCPサーバーが正常に起動しました。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## テンプレートに含まれるもの

| フォルダー / ファイル | 内容                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | デバッグ用のVSCodeファイル                   |
| `.aitk`      | Microsoft Foundry Toolkitの設定                |
| `src`        | weather mcp サーバーのソースコード   |

## Weather MCPサーバーのデバッグ方法

> 注意：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector)はMCPサーバーのテストやデバッグ用のビジュアル開発ツールです。
> - すべてのデバッグモードはブレークポイントをサポートしており、ツールの実装コードにブレークポイントを追加できます。

| デバッグモード | 説明 | デバッグ手順 |
| ---------- | ----------- | --------------- |
| Agent Builder | Microsoft Foundry Toolkit経由でAgent Builder内のMCPサーバーをデバッグします。 | 1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder`を選択し、`F5`キーを押してMCPサーバーのデバッグを開始します。<br>2. `gpt-5.1`などのアクティブなFoundryデプロイメントを選択し、「What is the weather in Shanghai?」と入力します。サーバーへの接続が自動的に行われます。<br>3. `Run`をクリックしてプロンプトでサーバーをテストします。 |
| MCP Inspector | MCP Inspectorを使ってMCPサーバーをデバッグします。 | 1. [Node.js](https://nodejs.org/)をインストール<br>2. Inspectorをセットアップ：`cd inspector` && `npm install` <br>3. VS Codeのデバッグパネルを開き、`Debug SSE in Inspector (Edge)`または`Debug SSE in Inspector (Chrome)`を選択。F5を押してデバッグを開始。<br>4. MCP Inspectorがブラウザで起動したら、`Connect`ボタンをクリックしてこのMCPサーバーに接続。<br>5. その後、`List Tools`でツールを選択し、パラメーターを入力して`Run Tool`でサーバーコードのデバッグが可能です。<br> |

## デフォルトポートとカスタマイズ

| デバッグモード | ポート | 定義ファイル | カスタマイズ方法 | 備考 |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | 上記ポートを変更するには、[launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)を編集 | なし |
| MCP Inspector | 3001 (サーバー); 5173と3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | 上記ポートを変更するには、[launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)を編集 | なし |

## フィードバック

このテンプレートに関するフィードバックや提案があれば、[Microsoft Foundry Toolkit GitHubリポジトリ](https://github.com/microsoft/vscode-ai-toolkit/issues)でIssueを開いてください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

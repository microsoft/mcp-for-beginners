# Weather MCP Server

これは、モックレスポンスを使った天気ツールを実装したPythonのサンプルMCPサーバーです。自身のMCPサーバーの足がかりとして利用できます。以下の機能が含まれています：

- **Weather Tool**：指定された場所に基づいてモックの天気情報を提供するツール。
- **Agent Builderへの接続**：MCPサーバーをAgent Builderに接続してテストやデバッグを行う機能。
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)でのデバッグ**：MCP Inspectorを使ってMCPサーバーをデバッグする機能。

## Weather MCP Serverテンプレートの使い始め

> **前提条件**
>
> ローカル開発環境でMCPサーバーを実行するには、以下が必要です：
>
> - [Python](https://www.python.org/)
> - （任意 - uvを使いたい場合）[uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 環境の準備

このプロジェクトの環境構築には2つの方法があります。お好みに合わせてどちらかを選択してください。

> 注意：仮想環境を作成した後、VSCodeやターミナルを再起動して仮想環境のPythonが使われていることを確認してください。

| 方法 | 手順 |
| -------- | ----- |
| `uv`を使う場合 | 1. 仮想環境を作成：`uv venv` <br>2. VSCodeのコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係（開発用依存も含む）をインストール：`uv pip install -r pyproject.toml --extra dev` |
| `pip`を使う場合 | 1. 仮想環境を作成：`python -m venv .venv` <br>2. VSCodeのコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係（開発用依存も含む）をインストール：`pip install -e .[dev]` |

環境構築が完了したら、Agent BuilderをMCPクライアントとして使い、ローカル開発環境でサーバーを起動してみましょう：
1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder`を選択するか、`F5`キーを押してMCPサーバーのデバッグを開始します。
2. AI ToolkitのAgent Builderを使い、[このプロンプト](../../../../../../../../../../open_prompt_builder)でサーバーをテストします。サーバーは自動的にAgent Builderに接続されます。
3. `Run`をクリックしてプロンプトでサーバーをテストします。

**おめでとうございます**！Agent BuilderをMCPクライアントとして使い、ローカル開発環境でWeather MCP Serverを正常に起動できました。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## テンプレートに含まれるもの

| フォルダー / ファイル | 内容 |
| ------------ | -------------------------------------------- |
| `.vscode`    | デバッグ用のVSCode設定ファイル |
| `.aitk`      | AI Toolkitの設定ファイル |
| `src`        | weather mcp serverのソースコード |

## Weather MCP Serverのデバッグ方法

> 注意：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector)はMCPサーバーのテストやデバッグ用のビジュアル開発ツールです。
> - すべてのデバッグモードでブレークポイントがサポートされているため、ツール実装コードにブレークポイントを設定できます。

| デバッグモード | 説明 | デバッグ手順 |
| ---------- | ----------- | --------------- |
| Agent Builder | AI ToolkitのAgent Builder上でMCPサーバーをデバッグします。 | 1. VS Codeのデバッグパネルを開き、`Debug in Agent Builder`を選択して`F5`を押しMCPサーバーのデバッグを開始します。<br>2. AI ToolkitのAgent Builderを使い、[このプロンプト](../../../../../../../../../../open_prompt_builder)でサーバーをテストします。サーバーは自動的にAgent Builderに接続されます。<br>3. `Run`をクリックしてプロンプトでサーバーをテストします。 |
| MCP Inspector | MCP Inspectorを使ってMCPサーバーをデバッグします。 | 1. [Node.js](https://nodejs.org/)をインストールします。<br>2. Inspectorのセットアップ：`cd inspector` && `npm install` <br>3. VS Codeのデバッグパネルを開き、`Debug SSE in Inspector (Edge)`または`Debug SSE in Inspector (Chrome)`を選択し、`F5`を押してデバッグを開始します。<br>4. MCP Inspectorがブラウザで起動したら、`Connect`ボタンをクリックしてこのMCPサーバーに接続します。<br>5. その後、`List Tools`でツールを選択し、パラメーターを入力して`Run Tool`を実行し、サーバーコードをデバッグできます。<br> |

## デフォルトポートとカスタマイズ

| デバッグモード | ポート | 定義ファイル | カスタマイズ方法 | 備考 |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)を編集してポートを変更可能。 | なし |
| MCP Inspector | 3001（サーバー）；5173と3000（Inspector） | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)を編集してポートを変更可能。 | なし |

## フィードバック

このテンプレートに関するご意見やご提案がありましたら、[AI Toolkit GitHubリポジトリ](https://github.com/microsoft/vscode-ai-toolkit/issues)でIssueを開いてください。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
# Weather MCP Server

これは、Pythonで実装された天気ツールを含むサンプルMCPサーバーで、モックレスポンスを提供します。このテンプレートは、独自のMCPサーバーを構築するための足場として使用できます。以下の機能が含まれています：

- **Weather Tool**: 指定された場所に基づいてモックされた天気情報を提供するツール。
- **Git Clone Tool**: Gitリポジトリを指定されたフォルダにクローンするツール。
- **VS Code Open Tool**: フォルダをVS CodeまたはVS Code Insidersで開くツール。
- **Connect to Agent Builder**: MCPサーバーをAgent Builderに接続してテストやデバッグを行う機能。
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: MCP Inspectorを使用してMCPサーバーをデバッグする機能。

## Weather MCP Serverテンプレートの使い方

> **前提条件**
>
> MCPサーバーをローカル開発環境で実行するには、以下が必要です：
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repoツールに必要)
> - [VS Code](https://code.visualstudio.com/) または [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscodeツールに必要)
> - (*オプション - uvを好む場合*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 環境の準備

このプロジェクトの環境をセットアップする方法は2つあります。好みに応じてどちらかを選んでください。

> 注: 仮想環境を作成した後、VSCodeやターミナルを再読み込みして仮想環境のPythonが使用されるようにしてください。

| 方法 | 手順 |
| -------- | ----- |
| `uv`を使用 | 1. 仮想環境を作成: `uv venv` <br>2. VSCodeコマンド "***Python: Select Interpreter***" を実行し、作成した仮想環境のPythonを選択 <br>3. 依存関係をインストール (開発用依存関係を含む): `uv pip install -r pyproject.toml --extra dev` |
| `pip`を使用 | 1. 仮想環境を作成: `python -m venv .venv` <br>2. VSCodeコマンド "***Python: Select Interpreter***" を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係をインストール (開発用依存関係を含む): `pip install -e .[dev]` | 

環境をセットアップした後、Agent BuilderをMCPクライアントとして使用してローカル開発環境でサーバーを実行できます：
1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder`を選択するか、`F5`を押してMCPサーバーのデバッグを開始します。
2. AI Toolkit Agent Builderを使用して[このプロンプト](../../../../../../../../../../../open_prompt_builder)でサーバーをテストします。サーバーは自動的にAgent Builderに接続されます。
3. `Run`をクリックしてプロンプトでサーバーをテストします。

**おめでとうございます**！Agent BuilderをMCPクライアントとして使用して、ローカル開発環境でWeather MCP Serverを正常に実行できました。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## テンプレートに含まれる内容

| フォルダ / ファイル| 内容                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | デバッグ用のVSCodeファイル                   |
| `.aitk`      | AI Toolkitの設定                             |
| `src`        | Weather MCP Serverのソースコード             |

## Weather MCP Serverのデバッグ方法

> 注:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector)は、MCPサーバーのテストとデバッグ用のビジュアル開発ツールです。
> - すべてのデバッグモードはブレークポイントをサポートしているため、ツール実装コードにブレークポイントを追加できます。

## 利用可能なツール

### Weather Tool
`get_weather`ツールは、指定された場所のモックされた天気情報を提供します。

| パラメータ | 型 | 説明 |
| --------- | ---- | ----------- |
| `location` | string | 天気を取得する場所 (例: 都市名、州、または座標) |

### Git Clone Tool
`git_clone_repo`ツールは、Gitリポジトリを指定されたフォルダにクローンします。

| パラメータ | 型 | 説明 |
| --------- | ---- | ----------- |
| `repo_url` | string | クローンするGitリポジトリのURL |
| `target_folder` | string | リポジトリをクローンするフォルダのパス |

ツールは以下のJSONオブジェクトを返します：
- `success`: 操作が成功したかどうかを示すブール値
- `target_folder`または`error`: クローンされたリポジトリのパスまたはエラーメッセージ

### VS Code Open Tool
`open_in_vscode`ツールは、フォルダをVS CodeまたはVS Code Insidersアプリケーションで開きます。

| パラメータ | 型 | 説明 |
| --------- | ---- | ----------- |
| `folder_path` | string | 開くフォルダのパス |
| `use_insiders` | boolean (オプション) | 通常のVS CodeではなくVS Code Insidersを使用するかどうか |

ツールは以下のJSONオブジェクトを返します：
- `success`: 操作が成功したかどうかを示すブール値
- `message`または`error`: 確認メッセージまたはエラーメッセージ

| デバッグモード | 説明 | デバッグ手順 |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkitを介してAgent BuilderでMCPサーバーをデバッグします。 | 1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder`を選択し、`F5`を押してMCPサーバーのデバッグを開始します。<br>2. AI Toolkit Agent Builderを使用して[このプロンプト](../../../../../../../../../../../open_prompt_builder)でサーバーをテストします。サーバーは自動的にAgent Builderに接続されます。<br>3. `Run`をクリックしてプロンプトでサーバーをテストします。 |
| MCP Inspector | MCP Inspectorを使用してMCPサーバーをデバッグします。 | 1. [Node.js](https://nodejs.org/)をインストール<br> 2. Inspectorをセットアップ: `cd inspector` && `npm install` <br> 3. VS Codeのデバッグパネルを開きます。`Debug SSE in Inspector (Edge)`または`Debug SSE in Inspector (Chrome)`を選択します。`F5`を押してデバッグを開始します。<br> 4. MCP Inspectorがブラウザで起動したら、`Connect`ボタンをクリックしてこのMCPサーバーに接続します。<br> 5. `List Tools`を選択し、ツールを選び、パラメータを入力して`Run Tool`をクリックしてサーバーコードをデバッグします。 |

## デフォルトポートとカスタマイズ

| デバッグモード | ポート | 定義 | カスタマイズ | 注 |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json)を編集して上記ポートを変更できます。 | N/A |
| MCP Inspector | 3001 (サーバー); 5173と3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json)を編集して上記ポートを変更できます。| N/A |

## フィードバック

このテンプレートに関するフィードバックや提案がある場合は、[AI Toolkit GitHubリポジトリ](https://github.com/microsoft/vscode-ai-toolkit/issues)でIssueを開いてください。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。
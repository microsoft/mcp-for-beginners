# Weather MCP サーバー

これは、モックレスポンスを使った天気ツールを実装したPythonのサンプルMCPサーバーです。独自のMCPサーバーのスキャフォールドとして使用できます。以下の機能が含まれています：

- **Weather Tool**: 指定された場所に基づいてモックされた天気情報を提供するツール。
- **Git Clone Tool**: Gitリポジトリを指定したフォルダーにクローンするツール。
- **VS Code Open Tool**: フォルダーをVS CodeまたはVS Code Insidersで開くツール。
- **Agent Builderへの接続**: MCPサーバーをAgent Builderに接続してテストやデバッグを可能にする機能。
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)でのデバッグ**: MCP Inspectorを使ってMCPサーバーをデバッグする機能。

## Weather MCP Server テンプレートの開始方法

> **前提条件**
> 
> ローカル開発マシンでMCPサーバーを実行するには、以下が必要です：
> 
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/)（git_clone_repoツールで必要）
> - [VS Code](https://code.visualstudio.com/) または [VS Code Insiders](https://code.visualstudio.com/insiders/)（open_in_vscodeツールで必要）
> - （任意 - uvを好む場合）[uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 環境準備

このプロジェクトの環境設定には2つの方法があります。好みに応じてどちらかを選択してください。

> 注意：仮想環境作成後にVSCodeやターミナルをリロードして、仮想環境のPythonが使われるようにしてください。

| 方法 | 手順 |
| ------ | ----- |
| `uv` を使う | 1. 仮想環境を作成：`uv venv` <br>2. VSCodeコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係をインストール（dev依存も含む）：`uv pip install -r pyproject.toml --extra dev` |
| `pip` を使う | 1. 仮想環境を作成：`python -m venv .venv` <br>2. VSCodeコマンド「***Python: Select Interpreter***」を実行し、作成した仮想環境のPythonを選択<br>3. 依存関係をインストール（dev依存も含む）：`pip install -e .[dev]` |

環境設定後は、Agent BuilderをMCPクライアントとしてローカル開発マシンでサーバーを起動して始めましょう：
1. VS Codeのデバッグパネルを開きます。`Debug in Agent Builder` を選択するか、`F5`キーを押してMCPサーバーのデバッグを開始します。
2. Microsoft Foundry Toolkit for Visual Studio Code Agent Builder で、`gpt-5.1` などのアクティブな Foundry デプロイメントを選択し、「What is the weather in Shanghai?」と入力します。サーバーへの接続が自動的に行われます。
3. `Run` をクリックしてプロンプトでサーバーをテストします。

**おめでとうございます！** Agent BuilderをMCPクライアントとして使用し、ローカル開発マシンでWeather MCP Serverを正常に実行できました。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## テンプレートに含まれるもの

| フォルダー / ファイル | 内容                                      |
| ----------------- | ----------------------------------------- |
| `.vscode`         | デバッグ用のVSCodeファイル                   |
| `.aitk`           | AI Toolkit用の設定ファイル                   |
| `src`             | Weather MCPサーバーのソースコード              |

## Weather MCP Server のデバッグ方法

> 注意：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) はMCPサーバーのテストやデバッグ用のビジュアル開発ツールです。
> - すべてのデバッグモードでブレークポイントがサポートされており、ツール実装コードにブレークポイントを追加できます。

## 利用可能なツール

### Weather Tool
`get_weather` ツールは指定した場所のモックされた天気情報を提供します。

| パラメーター | 型 | 説明 |
| ---------- | --- | ---- |
| `location` | string | 天気情報を取得する場所（例：都市名、州、または座標） |

### Git Clone Tool
`git_clone_repo` ツールはGitリポジトリを指定したフォルダーにクローンします。

| パラメーター | 型 | 説明 |
| ----------- | --- | ---- |
| `repo_url` | string | クローンするGitリポジトリのURL |
| `target_folder` | string | リポジトリをクローンするフォルダーのパス |

ツールは以下のJSONオブジェクトを返します：
- `success`: 処理が成功したかを示すブール値
- `target_folder` または `error`: クローンされたリポジトリのパス、またはエラーメッセージ

### VS Code Open Tool
`open_in_vscode` ツールはフォルダーをVS CodeまたはVS Code Insidersアプリケーションで開きます。

| パラメーター | 型 | 説明 |
| ------------ | --- | ---- |
| `folder_path` | string | 開くフォルダーのパス |
| `use_insiders` | boolean (オプション) | 通常のVS CodeではなくVS Code Insidersを使うかどうか |

ツールは以下のJSONオブジェクトを返します：
- `success`: 処理が成功したかを示すブール値
- `message` または `error`: 確認メッセージまたはエラーメッセージ

| デバッグモード | 説明 | デバッグ手順 |
| -------------- | ---- | ----------- |
| Agent Builder | AI ToolkitのAgent Builder内でMCPサーバーをデバッグする。 | 1. VS Codeのデバッグパネルを開き、`Debug in Agent Builder` を選択し `F5` を押してMCPサーバーのデバッグを開始。<br>2. Select an active Foundry deployment such as `gpt-5.1`, then enter `What is the weather in Shanghai?`. The server will be connected automatically.<br>3. `Run` をクリックしてプロンプトでテスト。 |
| MCP Inspector | MCP Inspectorを使ってMCPサーバーをデバッグする。 | 1. [Node.js](https://nodejs.org/) をインストール<br>2. Inspectorをセットアップ：`cd inspector` && `npm install`<br>3. VS Codeのデバッグパネルを開き、`Debug SSE in Inspector (Edge)` または `Debug SSE in Inspector (Chrome)` を選択し、`F5`キーでデバッグ開始。<br>4. MCP Inspectorがブラウザで起動したら、`Connect`ボタンをクリックしてMCPサーバーに接続。<br>5. その後、`List Tools` でツールを選択し、パラメーターを入力し、`Run Tool` でサーバーコードをデバッグ。 |

## デフォルトポートとカスタマイズ

| デバッグモード | ポート | 定義ファイル | カスタマイズ方法 | 備考 |
| -------------- | ------ | ----------- | ---------------- | ---- |
| Agent Builder  | 3001   | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) を編集してポートを変更可能 | N/A |
| MCP Inspector  | 3001（サーバー）；5173 と 3000（Inspector） | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) を編集してポートを変更可能 | N/A |

## フィードバック

このテンプレートに関してフィードバックや提案がありましたら、[AI Toolkit GitHubリポジトリ](https://github.com/microsoft/vscode-ai-toolkit/issues)にIssueを投稿してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の確保に努めていますが、自動翻訳には誤りや不正確な箇所が含まれる場合があります。原文の母国語による文書を正本としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

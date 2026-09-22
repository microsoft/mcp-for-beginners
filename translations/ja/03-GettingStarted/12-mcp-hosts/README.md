# 人気のMCPホストクライアントの設定

> [!NOTE]
> `/sse`を指すホスト構成は、MCP `2025-11-25`用のレガシーなHTTP+SSEの例です。MCP `2026-07-28`の場合は、対応しているホストでStreamable HTTPを選択し、サーバーによって構成されたエンドポイントを使用してください。
> 
> 

このガイドは、人気のAIホストアプリケーションでMCPサーバーを構成および使用する方法を扱います。各ホストにはそれぞれの構成方法がありますが、一度設定すれば、すべて標準化されたプロトコルを使ってMCPサーバーと通信します。

## MCPホストとは？

<strong>MCPホスト</strong>とは、MCPサーバーに接続してその機能を拡張できるAIアプリケーションです。ユーザーが対話する「フロントエンド」として機能し、MCPサーバーは「バックエンド」としてツールやデータを提供します。

```mermaid
flowchart LR
    User[👤 ユーザー] --> Host[🖥️ MCPホスト]
    Host --> S1[MCPサーバーA]
    Host --> S2[MCPサーバーB]
    Host --> S3[MCPサーバーC]
    
    subgraph 「人気のホスト」
        H1[Claudeデスクトップ]
        H2[VSコード]
        H3[カーソル]
        H4[クライン]
        H5[ウィンドサーフ]
    end
```

## 前提条件

- 接続するMCPサーバー（[Module 3.1 - First Server](../01-first-server/README.md)参照）
- システムにインストールされたホストアプリケーション
- JSON構成ファイルの基本的な知識

---

## 1. Claude Desktop

<strong>Claude Desktop</strong>はAnthropicの公式デスクトップアプリケーションで、MCPをネイティブにサポートしています。

### インストール

1. [claude.ai/download](https://claude.ai/download)からClaude Desktopをダウンロードします
2. インストールしてAnthropicアカウントでサインインします

### 構成

Claude DesktopはJSON構成ファイルを使ってMCPサーバーを定義します。

**構成ファイルの場所：**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**構成例：**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### 構成オプション

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| `command` | 実行する実行ファイル | `"python"`, `"node"`, `"npx"` |
| `args` | コマンドライン引数 | `["-m", "my_server"]` |
| `env` | 環境変数 | `{"API_KEY": "xxx"}` |
| `cwd` | 作業ディレクトリ | `"/path/to/server"` |

### 設定のテスト

1. 構成ファイルを保存します
2. Claude Desktopを完全に再起動します（終了して再オープン）
3. 新しい会話を開きます
4. 接続済みサーバーを示す🔌アイコンを確認します
5. Claudeにツール使用を試みます

### Claude Desktopのトラブルシューティング

**サーバーが表示されない場合：**
- JSONバリデーターで構成ファイルの構文を確認します
- コマンドパスが正しいか確認します
- Claude Desktopのログをチェックします：ヘルプ → ログの表示

**起動時にサーバーがクラッシュする場合：**
- まずターミナルでサーバーを手動でテストします
- 環境変数が正しく設定されているか確認します
- すべての依存関係がインストールされているか確認します

---

## 2. GitHub Copilot付きVS Code

VS CodeはGitHub Copilot Chat拡張機能を通じてMCPをサポートしています。

### 前提条件

1. VS Code 1.99以上がインストールされていること
2. GitHub Copilot拡張機能がインストールされていること
3. GitHub Copilot Chat拡張機能がインストールされていること

### 構成

VS Codeはワークスペースまたはユーザー設定の `.vscode/mcp.json` を使用します。

<strong>ワークスペース構成</strong> (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

<strong>ユーザー設定</strong> (`settings.json`):

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### VS CodeでのMCPの使用

1. Copilot Chatパネルを開く（Ctrl+Shift+I / Cmd+Shift+I）
2. `@`と入力して利用可能なMCPツールを表示
3. 自然言語でツールを呼び出す : 「電卓で25 × 48を計算して」

### VS Codeのトラブルシューティング

**MCPサーバーが読み込まれない場合：**
- 出力パネル→「MCP」でエラーログを確認
- ウィンドウをリロード：Ctrl+Shift+P→「Developer: Reload Window」
- まずサーバーが単独で動作するか確認

---

## 3. Cursor

<strong>Cursor</strong>は、MCPサポートを組み込んだAI優先のコードエディターです。

### インストール

1. [cursor.sh](https://cursor.sh)からCursorをダウンロードします
2. インストールしてサインインします

### 構成

CursorはClaude Desktopと似た構成形式を使用します。

**構成ファイルの場所：**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**構成例：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### CursorでのMCPの使用

1. CursorのAIチャットを開く（Ctrl+L / Cmd+L）
2. MCPツールが自動的に提案に表示されます
3. 接続されたサーバーを使ってAIにタスクを依頼します

---

## 4. Cline（ターミナルベース）

<strong>Cline</strong>はターミナルベースのMCPクライアントで、コマンドライン作業に最適です。

### インストール

```bash
npm install -g @anthropic/cline
```

### 構成

Clineは環境変数とコマンドライン引数を使用します。

**環境変数を使用する場合：**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**コマンドライン引数を使用する場合：**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

<strong>構成ファイル</strong> (`~/.clinerc`):

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### Clineの使用方法

```bash
# インタラクティブセッションを開始する
cline

# MCPでの単一クエリ
cline "Calculate the square root of 144 using the calculator"

# 利用可能なツールをリストする
cline --list-tools
```

---

## 5. Windsurf

<strong>Windsurf</strong>は、MCPをサポートする別のAI搭載コードエディターです。

### インストール

1. [codeium.com/windsurf](https://codeium.com/windsurf)からWindsurfをダウンロードします
2. インストールしてアカウントを作成します

### 構成

Windsurfの構成は設定UIから管理します：

1. 設定を開く（Ctrl+, / Cmd+,）
2. 「MCP」を検索
3. 「settings.jsonで編集」をクリック

**構成例：**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## トランスポートタイプの比較

ホストによって対応するトランスポートメカニズムは異なります：

| ホスト | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio**（標準入出力）：ホストが開始するローカルサーバーに最適
**SSE/HTTP**：リモートサーバーまたは複数クライアントと共有されるサーバーに最適

---

## よくあるトラブルシューティング

### サーバーが起動しない

1. **まずサーバーを手動でテスト：**
   ```bash
   # Python用
   python -m your_server_module
   
   # Node.js用
   node /path/to/server/index.js
   ```

2. **コマンドパスの確認：**
   - 可能なら絶対パスを使用
   - 実行ファイルがPATHに含まれていることを確認

3. **依存関係の確認：**
   ```bash
   # パイソン
   pip list | grep mcp
   
   # ノード.js
   npm list @modelcontextprotocol/sdk
   ```

### サーバーには接続できるがツールが動作しない

1. <strong>サーバーログを確認</strong> - 多くのホストにログ機能があります
2. <strong>ツール登録の確認</strong> - MCP Inspectorでテスト
3. <strong>権限設定を確認</strong> - 一部ツールはファイル/ネットワークアクセスが必要

### 環境変数が渡されない

- 一部ホストは環境変数をサニタイズします
- `env`構成フィールドを明示的に使用してください
- 機密情報は設定ファイルに含めず（シークレット管理を使用）

---

## セキュリティのベストプラクティス

1. **APIキーを設定ファイルに絶対にコミットしないでください**
2. <strong>機密情報は環境変数で管理してください</strong>
3. <strong>サーバーの権限は必要最小限に制限してください</strong>
4. <strong>システムアクセスを許可する前にサーバーコードをレビューしてください</strong>
5. <strong>ファイルシステムやネットワークアクセスには許可リストを使用してください</strong>

---

## 次のステップ

- [3.13 - MCP Inspectorによるデバッグ](../13-mcp-inspector/README.md)
- [3.1 - 最初のMCPサーバーの作成](../01-first-server/README.md)
- [Module 5 - 高度なトピック](../../05-AdvancedTopics/README.md)

---

## 追加リソース

- [Claude Desktop MCPドキュメント](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP拡張機能](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP仕様 - トランスポート](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [公式MCPサーバーレジストリ](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
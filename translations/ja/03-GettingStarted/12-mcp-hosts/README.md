# 人気のあるMCPホストクライアントの設定

このガイドでは、人気のあるAIホストアプリケーションでMCPサーバーを設定および使用する方法について説明します。各ホストは独自の設定方式を持っていますが、一度設定すればすべて標準化されたプロトコルを使用してMCPサーバーと通信します。

## MCPホストとは何ですか？

**MCPホスト**は、機能拡張のためにMCPサーバーに接続できるAIアプリケーションです。これはユーザーが操作する「フロントエンド」と考え、MCPサーバーは「バックエンド」のツールやデータを提供します。

```mermaid
flowchart LR
    User[👤 ユーザー] --> Host[🖥️ MCP ホスト]
    Host --> S1[MCP サーバー A]
    Host --> S2[MCP サーバー B]
    Host --> S3[MCP サーバー C]
    
    subgraph "人気のホスト"
        H1[クロード デスクトップ]
        H2[VS コード]
        H3[カーソル]
        H4[クライン]
        H5[ウィンドサーフ]
    end
```
## 前提条件

- 接続するMCPサーバー（[Module 3.1 - First Server](../01-first-server/README.md)を参照）
- お使いのシステムにホストアプリケーションがインストールされていること
- JSON構成ファイルに関する基本的な知識

---

## 1. Claude Desktop

**Claude Desktop**はAnthropicの公式デスクトップアプリで、ネイティブにMCPをサポートしています。

### インストール

1. [claude.ai/download](https://claude.ai/download)からClaude Desktopをダウンロード
2. インストールしてAnthropicアカウントでサインイン

### 設定

Claude DesktopはMCPサーバーを定義するJSON構成ファイルを使います。

**構成ファイルの場所:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**設定例:**

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

### 設定オプション

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| `command` | 実行する実行ファイル | `"python"`, `"node"`, `"npx"` |
| `args` | コマンドライン引数 | `["-m", "my_server"]` |
| `env` | 環境変数 | `{"API_KEY": "xxx"}` |
| `cwd` | 作業ディレクトリ | `"/path/to/server"` |

### 設定のテスト

1. 構成ファイルを保存
2. Claude Desktopを完全に再起動（終了して再度開く）
3. 新しい会話を開く
4. 接続済みサーバーを示す🔌アイコンを確認
5. Claudeにツールの使用を頼んでみる

### Claude Desktopのトラブルシューティング

**サーバーが表示されない場合:**
- JSONバリデーターで構成ファイルの構文を確認
- コマンドパスが正しいか確認
- Claude Desktopログの確認：ヘルプ → ログを表示

**起動時にサーバーがクラッシュする場合:**
- 端末で手動でサーバーをテスト
- 環境変数が正しく設定されているか確認
- 依存関係が全てインストールされているか確認

---

## 2. GitHub Copilot搭載のVS Code

VS CodeはGitHub Copilot Chat拡張機能を通じてMCPをサポートしています。

### 前提条件

1. VS Code 1.99以上がインストールされていること
2. GitHub Copilot拡張機能がインストールされていること
3. GitHub Copilot Chat拡張機能がインストールされていること

### 設定

VS Codeはワークスペースまたはユーザー設定の`.vscode/mcp.json`を使用します。

**ワークスペース設定** (`.vscode/mcp.json`):

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

**ユーザー設定** (`settings.json`):

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

### VS CodeでのMCPの使い方

1. Copilot Chatパネルを開く（Ctrl+Shift+I / Cmd+Shift+I）
2. `@`を入力して利用可能なMCPツールを表示
3. 自然言語でツールを呼び出す：「計算機で25 * 48を計算して」

### VS Codeのトラブルシューティング

**MCPサーバーが読み込まれない:**
- 出力パネルの「MCP」タブでエラーログを確認
- ウィンドウをリロード：Ctrl+Shift+P → 「Developer: Reload Window」
- サーバーが単独で動作するか先に確認

---

## 3. Cursor

**Cursor**はMCPサポートが組み込まれたAIファーストのコードエディタです。

### インストール

1. [cursor.sh](https://cursor.sh)からCursorをダウンロード
2. インストールしてサインイン

### 設定

CursorはClaude Desktopに似た構成フォーマットを使用します。

**構成ファイルの場所:**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**設定例:**

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

### CursorでのMCPの使い方

1. CursorのAIチャットを開く（Ctrl+L / Cmd+L）
2. MCPツールが自動的に提案に表示される
3. 接続されたサーバーを使ってAIにタスクを依頼

---

## 4. Cline（ターミナルベース）

**Cline**はコマンドラインワークフローに最適な、ターミナルベースのMCPクライアントです。

### インストール

```bash
npm install -g @anthropic/cline
```

### 設定

Clineは環境変数とコマンドライン引数を使用します。

**環境変数の使用例:**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**コマンドライン引数の使用例:**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

**構成ファイル** (`~/.clinerc`):

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

# MCPを用いた単一クエリ
cline "Calculate the square root of 144 using the calculator"

# 利用可能なツールを一覧表示する
cline --list-tools
```

---

## 5. Windsurf

**Windsurf**はMCPサポート付きの別のAIコードエディタです。

### インストール

1. [codeium.com/windsurf](https://codeium.com/windsurf)からWindsurfをダウンロード
2. インストールしてアカウント作成

### 設定

Windsurfの設定はUIの設定画面から行います：

1. 設定を開く（Ctrl+, / Cmd+,）
2. 「MCP」で検索
3. 「settings.jsonで編集」をクリック

**設定例:**

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

## トランスポートタイプ比較

ホストごとに対応するトランスポート方式は異なります：

| ホスト | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio**（標準入出力）：ホストが起動するローカルサーバーに最適
**SSE/HTTP**: リモートサーバーや複数クライアントで共有するサーバーに最適

---

## よくあるトラブルシューティング

### サーバーが起動しない場合

1. **まずサーバーを手動でテスト:**
   ```bash
   # Python用
   python -m your_server_module
   
   # Node.js用
   node /path/to/server/index.js
   ```

2. **コマンドパスをチェック:**
   - 可能な限り絶対パスを使用
   - 実行ファイルがPATHにあることを確認

3. **依存関係を確認:**
   ```bash
   # Python用
   pip list | grep mcp
   
   # Node.js用
   npm list @modelcontextprotocol/sdk
   ```

### サーバーは接続するがツールが動作しない場合

1. **サーバーログを確認** - 多くのホストにロギング機能あり
2. **ツールの登録を確認** - MCP Inspectorでテスト可能
3. **権限を確認** - 一部ツールはファイルやネットワークアクセスが必要

### 環境変数が渡らない

- 一部ホストは環境変数をサニタイズする
- `env`設定フィールドを明示的に利用
- 構成ファイルに機密情報を入れない（シークレット管理を使用）

---

## セキュリティのベストプラクティス

1. **APIキーを構成ファイルに決してコミットしない**
2. **機密情報は環境変数で管理する**
3. **サーバー権限は必要最低限に限定する**
4. **サーバーコードをレビューしてからシステムにアクセス権を与える**
5. **ファイルシステムおよびネットワークアクセスには許可リストを利用する**

---

## 次に進むために

- [3.13 - MCP Inspectorでデバッグ](../13-mcp-inspector/README.md)
- [3.1 - 最初のMCPサーバーを作成](../01-first-server/README.md)
- [モジュール 5 - 高度なトピック](../../05-AdvancedTopics/README.md)

---

## 追加リソース

- [Claude Desktop MCPドキュメント](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP拡張機能](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP仕様 - トランスポート](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/)
- [公式MCPサーバーレジストリ](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本資料はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる場合があります。原文を権威ある情報源としてご参照ください。重要な情報については、専門の人間翻訳をご利用いただくことを推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->

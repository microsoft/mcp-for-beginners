# MCP stdioサーバー - TypeScriptソリューション

> **⚠️ 重要**: このソリューションは、MCP仕様2025-06-18で推奨されている**stdioトランスポート**を使用するように更新されています。従来のSSEトランスポートは非推奨となりました。

## 概要

このTypeScriptソリューションは、現在のstdioトランスポートを使用してMCPサーバーを構築する方法を示しています。stdioトランスポートは、非推奨となったSSEアプローチよりもシンプルで安全性が高く、パフォーマンスも向上しています。

## 前提条件

- Node.js 18以上
- npmまたはyarnパッケージマネージャー

## セットアップ手順

### ステップ1: 依存関係をインストールする

```bash
npm install
```

### ステップ2: プロジェクトをビルドする

```bash
npm run build
```

## サーバーの実行

stdioサーバーは、従来のSSEサーバーとは異なる方法で動作します。ウェブサーバーを起動する代わりに、stdin/stdoutを通じて通信します:

```bash
npm start
```

**重要**: サーバーが「ハング」しているように見えるかもしれませんが、これは正常です！stdinからのJSON-RPCメッセージを待機しています。

## サーバーのテスト

### 方法1: MCPインスペクターを使用する（推奨）

```bash
npm run inspector
```

これにより以下が実行されます:
1. サーバーをサブプロセスとして起動
2. テスト用のウェブインターフェースを開く
3. すべてのサーバーツールを対話的にテスト可能

### 方法2: コマンドラインで直接テスト

インスペクターを直接起動してテストすることもできます:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### 利用可能なツール

サーバーは以下のツールを提供します:

- **add(a, b)**: 2つの数値を加算
- **multiply(a, b)**: 2つの数値を乗算  
- **get_greeting(name)**: 個別の挨拶を生成
- **get_server_info()**: サーバー情報を取得

### Claude Desktopでのテスト

このサーバーをClaude Desktopで使用するには、以下の設定を`claude_desktop_config.json`に追加してください:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## プロジェクト構成

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## SSEとの主な違い

**stdioトランスポート（現在）:**
- ✅ シンプルなセットアップ - HTTPサーバー不要
- ✅ 高いセキュリティ - HTTPエンドポイント不要
- ✅ サブプロセスベースの通信
- ✅ stdin/stdoutを介したJSON-RPC
- ✅ 優れたパフォーマンス

**SSEトランスポート（非推奨）:**
- ❌ Expressサーバーのセットアップが必要
- ❌ 複雑なルーティングとセッション管理が必要
- ❌ 依存関係が多い（Express、HTTP処理）
- ❌ 追加のセキュリティ考慮が必要
- ❌ MCP 2025-06-18で非推奨

## 開発のヒント

- ログには`console.error()`を使用（`console.log()`はstdoutに書き込むため使用しない）
- テスト前に`npm run build`でビルドする
- インスペクターを使用して視覚的にデバッグする
- すべてのJSONメッセージが正しくフォーマットされていることを確認する
- サーバーはSIGINT/SIGTERMでの正常なシャットダウンを自動的に処理

このソリューションは、現在のMCP仕様に従い、TypeScriptを使用したstdioトランスポート実装のベストプラクティスを示しています。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。
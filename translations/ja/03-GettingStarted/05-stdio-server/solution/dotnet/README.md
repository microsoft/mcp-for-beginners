# MCP stdio サーバー - .NET ソリューション

> **⚠️ 重要**: このソリューションは、MCP仕様2025-06-18で推奨されている**stdioトランスポート**を使用するよう更新されています。従来のSSEトランスポートは廃止されました。

## 概要

この .NET ソリューションは、現在の stdio トランスポートを使用して MCP サーバーを構築する方法を示しています。stdio トランスポートは、廃止された SSE アプローチよりも簡単で安全性が高く、パフォーマンスも向上しています。

## 必要条件

- .NET 9.0 SDK 以降
- .NET の依存性注入に関する基本的な理解

## セットアップ手順

### ステップ 1: 依存関係を復元する

```bash
dotnet restore
```

### ステップ 2: プロジェクトをビルドする

```bash
dotnet build
```

## サーバーの実行

stdio サーバーは、従来の HTTP ベースのサーバーとは異なる方法で動作します。ウェブサーバーを起動する代わりに、標準入力/標準出力を通じて通信します:

```bash
dotnet run
```

**重要**: サーバーが停止しているように見えるかもしれませんが、これは正常です！標準入力からの JSON-RPC メッセージを待機しています。

## サーバーのテスト

### 方法 1: MCP インスペクターを使用する (推奨)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

これにより以下が可能になります:
1. サーバーをサブプロセスとして起動
2. テスト用のウェブインターフェースを開く
3. サーバーツールをインタラクティブにテスト

### 方法 2: コマンドラインで直接テスト

インスペクターを直接起動してテストすることもできます:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### 利用可能なツール

サーバーは以下のツールを提供します:

- **AddNumbers(a, b)**: 2つの数値を加算
- **MultiplyNumbers(a, b)**: 2つの数値を乗算  
- **GetGreeting(name)**: 個別の挨拶を生成
- **GetServerInfo()**: サーバー情報を取得

### Claude Desktop でのテスト

このサーバーを Claude Desktop で使用するには、以下の設定を `claude_desktop_config.json` に追加してください:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## プロジェクト構造

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE との主な違い

**stdio トランスポート (現在):**
- ✅ 簡単なセットアップ - ウェブサーバー不要
- ✅ 高いセキュリティ - HTTP エンドポイント不要
- ✅ `Host.CreateApplicationBuilder()` を使用 (`WebApplication.CreateBuilder()` の代わり)
- ✅ `WithStdioTransport()` を使用 (`WithHttpTransport()` の代わり)
- ✅ コンソールアプリケーションとして動作
- ✅ 高いパフォーマンス

**HTTP/SSE トランスポート (廃止):**
- ❌ ASP.NET Core ウェブサーバーが必要
- ❌ `app.MapMcp()` のルーティング設定が必要
- ❌ 設定と依存関係が複雑
- ❌ 追加のセキュリティ対策が必要
- ❌ MCP 2025-06-18 で廃止

## 開発機能

- **依存性注入**: サービスとログの完全な DI サポート
- **構造化ログ**: `ILogger<T>` を使用した標準エラーへの適切なログ記録
- **ツール属性**: `[McpServerTool]` 属性を使用したクリーンなツール定義
- **非同期サポート**: すべてのツールが非同期操作をサポート
- **エラー処理**: 優雅なエラー処理とログ記録

## 開発のヒント

- ログ記録には `ILogger` を使用 (標準出力に直接書き込まない)
- テスト前に `dotnet build` でビルド
- インスペクターを使用して視覚的にデバッグ
- すべてのログは自動的に標準エラーに送信
- サーバーは正常にシャットダウンするシグナルを処理

このソリューションは、現在の MCP 仕様に準拠しており、.NET を使用した stdio トランスポートの実装におけるベストプラクティスを示しています。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。
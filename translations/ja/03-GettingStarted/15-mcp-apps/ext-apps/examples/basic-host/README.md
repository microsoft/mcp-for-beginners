# 例：基本ホスト

MCPサーバーに接続し、安全なサンドボックス内でツールUIをレンダリングするMCPホストアプリケーションの構築方法を示すリファレンス実装です。

この基本ホストは、ローカル開発中にMCPアプリのテストにも使用できます。

## 主要ファイル

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - ツール選択、パラメータ入力、iframe管理を行うReact UIホスト
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - セキュリティ検証と双方向メッセージ中継を行う外側iframeプロキシ
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - コアロジック：サーバー接続、ツール呼び出し、AppBridge設定

## はじめに

```bash
npm install
npm run start
# http://localhost:8080 を開きます
```

デフォルトでは、ホストアプリケーションは`http://localhost:3001/mcp`のMCPサーバーに接続を試みます。この動作は、サーバーURLのJSON配列を`SERVERS`環境変数に設定することで変更できます：

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## アーキテクチャ

この例では、安全なUI分離のためにダブルiframeサンドボックスパターンを使用しています：

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**なぜ2つのiframeを使うのか？**

- 外側のiframeは別オリジン（ポート8081）で動作し、ホストへの直接アクセスを防止
- 内側のiframeは`srcdoc`経由でHTMLを受け取り、sandbox属性で制限されている
- メッセージは外側iframeを経由して双方向に検証・中継される

このアーキテクチャにより、たとえツールのUIコードが悪意あるものであっても、ホストアプリケーションのDOM、クッキー、JavaScriptコンテキストにアクセスできないことが保証されます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を用いて翻訳されています。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文は原言語の文書が正式な資料として扱われます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に伴う誤解や解釈の相違について、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
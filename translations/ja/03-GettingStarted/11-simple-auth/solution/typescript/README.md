# サンプルを実行

## 依存関係のインストール

```sh
npm install
```

## ビルド

```sh
npm run build
```

## トークンの生成

```sh
npm run generate
```

これにより、*.env* ファイルにトークンが作成されます。クライアントはこのファイルから読み取ります。

## コードの実行

サーバーを起動するには以下を実行します:

```sh
npm start
```

クライアントを別のターミナルで実行するには以下を実行します:

```sh
npm run client
```

サーバーのターミナルでは、以下のような出力が表示されるはずです:

```text
User exists
User has required scopes
Middleware executed
```

そして、クライアントのターミナルでは以下のような出力が表示されるはずです:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### 変更を加える

スコープを理解しているか確認しましょう。*server.ts* ファイルを見つけて、以下のコードを探してください:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

これは、渡されたトークンが "User.Read" を持つ必要があることを示しています。"User.Write" に変更してみましょう。その後、`npm run build` を実行し、サーバーを再起動 (`npm start`) してください。スコープが不足しているため認証が失敗することが確認できるはずです (現在のスコープは User.Read と Admin.Write です)。

クライアントは次のように表示します:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

そして、サーバーのターミナルでは次のように表示されます:

```text
User exists
```

これ以上進まないことが確認できます。

"User.Write" スコープを追加して `npm run generate` を実行し、クライアントを再実行するか、サーバーコードを元に戻してください。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。
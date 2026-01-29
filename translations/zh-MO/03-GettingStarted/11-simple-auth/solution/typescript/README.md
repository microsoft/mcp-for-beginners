# 執行範例

## 安裝依賴項

```sh
npm install
```

## 建置

```sh
npm run build
```

## 生成令牌

```sh
npm run generate
```

這會在檔案 *.env* 中創建一個令牌。客戶端將從此檔案中讀取。

## 執行程式碼

啟動伺服器：

```sh
npm start
```

在另一個終端中執行客戶端：

```sh
npm run client
```

在伺服器的終端中，你應該會看到類似以下的輸出：

```text
User exists
User has required scopes
Middleware executed
```

而在客戶端的終端中，你應該會看到類似以下的輸出：

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### 修改內容

讓我們確保了解範圍。找到檔案 *server.ts* 和以下程式碼：

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

這表示傳遞的令牌需要具有 "User.Read"，讓我們將其更改為 "User.Write"。現在執行 `npm run build` 並重新啟動伺服器 `npm start`。你現在應該會看到身份驗證失敗，因為我們沒有這個範圍（我們有 User.Read 和 Admin.Write）：

客戶端現在顯示

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

而你可以在伺服器的終端中看到它顯示：

```text
User exists
```

並且它不會超過這一點。

你可以選擇添加這個範圍 "User.Write"，然後執行 `npm run generate` 並重新執行客戶端，或者將伺服器程式碼改回原樣。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。
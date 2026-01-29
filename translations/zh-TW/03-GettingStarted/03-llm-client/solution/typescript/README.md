# 執行此範例

此範例需要在客戶端使用 LLM。LLM 需要你在 Codespaces 中執行，或是在 GitHub 設定個人存取權杖才能運作。

## -1- 安裝相依套件

```bash
npm install
```

## -3- 啟動伺服器

```bash
npm run build
```

## -4- 啟動客戶端

```sh
npm run client
```

你應該會看到類似以下的結果：

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
# 執行此範例

建議安裝 `uv`，但非必要，詳情請參考 [instructions](https://docs.astral.sh/uv/#highlights)

## -1- 安裝相依套件

```bash
npm install
```

## -3- 啟動伺服器

```bash
npm run build
```

## -4- 啟動用戶端

```sh
npm run client
```

你應該會看到類似以下的結果：

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
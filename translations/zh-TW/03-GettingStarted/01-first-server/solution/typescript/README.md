# 執行此範例

建議安裝 `uv`，但這並非必須，請參考[說明](https://docs.astral.sh/uv/#highlights)

## -1- 安裝依賴項目

```bash
npm install
```

## -3- 執行範例

```bash
npm run build
```

## -4- 測試範例

在一個終端機中啟動伺服器後，打開另一個終端機並執行以下指令：

```bash
npm run inspector
```

這將啟動一個帶有視覺介面的網頁伺服器，讓你可以測試此範例。

伺服器連線成功後：

- 嘗試列出工具並執行 `add`，參數為 2 和 4，你應該會在結果中看到 6。
- 前往資源和資源模板，調用 "greeting"，輸入一個名字，你應該會看到包含你提供名字的問候語。

### 在 CLI 模式下測試

你運行的檢查器實際上是一個 Node.js 應用程式，而 `mcp dev` 是其外層包裝。

你可以直接以 CLI 模式啟動它，執行以下指令：

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

這將列出伺服器中所有可用的工具。你應該會看到以下輸出：

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

要調用某個工具，請輸入：

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

你應該會看到以下輸出：

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> 通常以 CLI 模式運行檢查器會比在瀏覽器中快得多。
> 在[這裡](https://github.com/modelcontextprotocol/inspector)閱讀更多關於檢查器的資訊。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。
# 執行此範例

建議安裝 `uv`，但並非必須，請參閱[說明](https://docs.astral.sh/uv/#highlights)

## -1- 安裝依賴項目

```bash
npm install
```

## -3- 執行範例

```bash
npm run build
```

## -4- 測試範例

在一個終端啟動伺服器後，打開另一個終端並執行以下指令：

```bash
npm run inspector
```

這將啟動一個帶有視覺介面的網頁伺服器，讓你可以測試此範例。

伺服器連接後：

- 嘗試列出工具並執行 `add`，參數為 2 和 4，結果應顯示為 6。
- 前往資源和資源模板，調用 "greeting"，輸入一個名字，你應該會看到包含你提供名字的問候語。

### 在 CLI 模式下測試

你運行的檢查器實際上是一個 Node.js 應用程式，而 `mcp dev` 是其外層包裝。

你可以通過執行以下指令直接以 CLI 模式啟動它：

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

要調用工具，請輸入：

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
> 通常以 CLI 模式運行檢查器比在瀏覽器中快得多。
> 在[這裡](https://github.com/modelcontextprotocol/inspector)了解更多關於檢查器的資訊。

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
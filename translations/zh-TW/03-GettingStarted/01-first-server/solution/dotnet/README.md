# 執行此範例

## -1- 安裝依賴項目

```bash
dotnet restore
```

## -3- 執行範例

```bash
dotnet run
```

## -4- 測試範例

在一個終端中啟動伺服器後，打開另一個終端並執行以下命令：

```bash
npx @modelcontextprotocol/inspector dotnet run
```

這將啟動一個具有視覺介面的網頁伺服器，讓您可以測試此範例。

伺服器連接後：

- 嘗試列出工具並執行 `add`，使用參數 2 和 4，您應該在結果中看到 6。
- 前往資源和資源模板，調用 "greeting"，輸入一個名字，您應該會看到包含您提供名字的問候語。

### 在 CLI 模式中測試

您可以直接通過執行以下命令以 CLI 模式啟動：

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

這將列出伺服器中所有可用的工具。您應該會看到以下輸出：

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

要調用工具，請輸入：

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

您應該會看到以下輸出：

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> 通常在 CLI 模式中運行檢查器比在瀏覽器中快得多。
> 在 [這裡](https://github.com/modelcontextprotocol/inspector) 閱讀更多關於檢查器的資訊。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。
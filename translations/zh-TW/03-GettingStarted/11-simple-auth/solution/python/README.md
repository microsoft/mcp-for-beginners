# 執行範例

## 建立環境

```sh
python -m venv venv
source ./venv/bin/activate
```

## 安裝依賴項

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## 生成令牌

您需要生成一個令牌，供客戶端與伺服器進行通信。

執行：

```sh
python util.py
```

## 執行程式碼

使用以下指令執行程式碼：

```sh
python server.py
```

在另一個終端中輸入：

```sh
python client.py
```

在伺服器的終端中，您應該會看到類似以下的內容：

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

在客戶端窗口中，您應該會看到類似以下的文字：

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

這表示一切正常運作。

### 修改資訊以查看錯誤情況

在 *server.py* 中找到以下程式碼：

```python
 if not has_scope(has_header, "Admin.Write"):
```

將其更改為 "User.Write"。您目前的令牌沒有該權限級別，因此如果您重新啟動伺服器並再次嘗試執行客戶端，您應該會在伺服器終端中看到類似以下的錯誤：

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

您可以選擇將伺服器程式碼改回原樣，或者生成一個包含額外範圍的新令牌，這取決於您的需求。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
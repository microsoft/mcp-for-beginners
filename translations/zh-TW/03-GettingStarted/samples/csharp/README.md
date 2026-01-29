# Basic Calculator MCP Service

此服務透過 Model Context Protocol (MCP) 提供基本的計算機運算功能。它是為初學者學習 MCP 實作而設計的簡單範例。

更多資訊請參考 [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## 功能

此計算機服務具備以下功能：

1. **基本算術運算**：
   - 兩數相加
   - 一數減去另一數
   - 兩數相乘
   - 一數除以另一數（含除以零檢查）

## 使用 `stdio` 類型

## 設定

1. **設定 MCP 伺服器**：
   - 在 VS Code 中開啟您的工作區。
   - 在工作區資料夾中建立 `.vscode/mcp.json` 檔案以設定 MCP 伺服器。範例設定：

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - 系統會要求您輸入 GitHub 倉庫根目錄，可透過指令 `git rev-parse --show-toplevel` 取得。

## 使用此服務

此服務透過 MCP 協定提供以下 API 端點：

- `add(a, b)`: 將兩個數字相加
- `subtract(a, b)`: 從第一個數字中減去第二個數字
- `multiply(a, b)`: 將兩個數字相乘
- `divide(a, b)`: 將第一個數字除以第二個數字（含除以零檢查）
- isPrime(n): 檢查一個數字是否為質數

## 在 VS Code 中使用 Github Copilot Chat 測試

1. 嘗試使用 MCP 協定向服務發送請求。例如，您可以問：
   - 「加 5 和 3」
   - 「從 4 減去 10」
   - 「乘以 6 和 7」
   - 「將 8 除以 2」
   - 「37854 是質數嗎？」
   - 「4242 前後的三個質數是哪些？」
2. 為確保使用該工具，請在提示詞中加入 #MyCalculator。例如：
   - 「加 5 和 3 #MyCalculator」
   - 「從 4 減去 10 #MyCalculator」

## 容器化版本

當您已安裝 .NET SDK 且所有相依性都已就緒時，前述方案非常適合。不過，如果您想分享此方案或在不同環境執行，可以使用容器化版本。

1. 啟動 Docker 並確保其正在運行。
1. 從終端機切換到資料夾 `03-GettingStarted\samples\csharp\src`
1. 執行以下指令來建置計算機服務的 Docker 映像檔（請將 `<YOUR-DOCKER-USERNAME>` 替換為您的 Docker Hub 使用者名稱）：
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. 映像檔建置完成後，執行以下指令將其上傳至 Docker Hub：
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## 使用 Docker 版本

1. 在 `.vscode/mcp.json` 檔案中，將伺服器設定替換為以下內容：
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   從設定中可以看到，指令為 `docker`，參數為 `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`。`--rm` 參數確保容器停止後會被移除，`-i` 參數允許您與容器的標準輸入互動。最後一個參數是我們剛剛建置並推送到 Docker Hub 的映像檔名稱。

## 測試 Docker 版本

點擊 `"mcp-calc": {` 上方的小啟動按鈕啟動 MCP 伺服器，接著就可以像之前一樣請計算機服務幫您做數學運算。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
# Basic Calculator MCP Service

此服務透過 Model Context Protocol (MCP) 提供基本計算機運算功能。它是為初學者學習 MCP 實作而設計的簡單範例。

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
   - 在 VS Code 中開啟你的工作區。
   - 在工作區資料夾中建立 `.vscode/mcp.json` 檔案來設定 MCP 伺服器。範例設定如下：

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

   - 系統會要求你輸入 GitHub 倉庫根目錄，可透過指令 `git rev-parse --show-toplevel` 取得。

## 使用服務

此服務透過 MCP 協定提供以下 API 端點：

- `add(a, b)`：將兩個數字相加
- `subtract(a, b)`：將第二個數字從第一個數字中減去
- `multiply(a, b)`：將兩個數字相乘
- `divide(a, b)`：將第一個數字除以第二個數字（含除以零檢查）
- isPrime(n)：檢查一個數字是否為質數

## 在 VS Code 使用 Github Copilot Chat 測試

1. 嘗試使用 MCP 協定向服務發出請求。例如，你可以問：
   - 「Add 5 and 3」
   - 「Subtract 10 from 4」
   - 「Multiply 6 and 7」
   - 「Divide 8 by 2」
   - 「Does 37854 prime?」
   - 「What are the 3 prime numbers before after 4242?」
2. 為確保使用該工具，請在提示詞中加入 #MyCalculator。例如：
   - 「Add 5 and 3 #MyCalculator」
   - 「Subtract 10 from 4 #MyCalculator」

## 容器化版本

當你已安裝 .NET SDK 且所有相依套件就緒時，前述方案非常適合。不過，如果你想分享此方案或在不同環境執行，可以使用容器化版本。

1. 啟動 Docker 並確保其正在運行。
1. 從終端機切換到資料夾 `03-GettingStarted\samples\csharp\src`
1. 執行以下指令來建立計算機服務的 Docker 映像檔（請將 `<YOUR-DOCKER-USERNAME>` 替換成你的 Docker Hub 使用者名稱）：
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. 映像檔建立完成後，執行以下指令將其上傳至 Docker Hub：
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
   從設定中可以看到，指令是 `docker`，參數為 `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`。`--rm` 參數確保容器停止後會被移除，`-i` 參數允許你與容器的標準輸入互動。最後一個參數是我們剛建立並推送到 Docker Hub 的映像檔名稱。

## 測試 Docker 版本

點擊 `"mcp-calc": {` 上方的小啟動按鈕啟動 MCP 伺服器，接著就可以像之前一樣請計算機服務幫你做數學運算。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
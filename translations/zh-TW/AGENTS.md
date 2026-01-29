# AGENTS.md

## 專案概述

**MCP for Beginners** 是一個開源教育課程，旨在教授模型上下文協議（Model Context Protocol，MCP）——一個標準化框架，用於 AI 模型與客戶端應用之間的交互。本存儲庫提供全面的學習材料，並包含多種程式語言的實作範例。

### 核心技術

- **程式語言**：C#、Java、JavaScript、TypeScript、Python、Rust
- **框架與 SDK**：
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **資料庫**：PostgreSQL（含 pgvector 擴展）
- **雲端平台**：Azure（容器應用、OpenAI、內容安全、應用洞察）
- **建置工具**：npm、Maven、pip、Cargo
- **文件**：使用 Markdown，支援自動多語言翻譯（超過 48 種語言）

### 架構

- **11 個核心模組 (00-11)**：從基礎到高階主題的循序學習路徑
- **實作實驗室**：提供多語言完整解決方案的實作練習
- **範例專案**：包含 MCP 伺服器與客戶端的工作實作
- **翻譯系統**：透過 GitHub Actions 自動化工作流程支援多語言
- **圖片資源**：集中管理的圖片目錄，包含翻譯版本

## 設置指令

此存儲庫主要以文件為主，大部分設置在各個範例專案與實驗室中完成。

### 存儲庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 使用範例專案

範例專案位於：
- `03-GettingStarted/samples/` - 特定語言的範例
- `03-GettingStarted/01-first-server/solution/` - 首次伺服器實作
- `03-GettingStarted/02-client/solution/` - 客戶端實作
- `11-MCPServerHandsOnLabs/` - 綜合資料庫整合實驗室

每個範例專案都包含其專屬的設置指令：

#### TypeScript/JavaScript 專案
```bash
cd <project-directory>
npm install
npm start
```

#### Python 專案
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java 專案
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## 開發工作流程

### 文件結構

- **模組 00-11**：核心課程內容，按順序排列
- **translations/**：特定語言版本（自動生成，請勿直接編輯）
- **translated_images/**：本地化圖片版本（自動生成）
- **images/**：原始圖片與圖表

### 修改文件

1. 僅編輯根模組目錄（00-11）中的英文 Markdown 文件
2. 如有需要，更新 `images/` 目錄中的圖片
3. co-op-translator GitHub Action 會自動生成翻譯
4. 推送至主分支時會重新生成翻譯

### 使用翻譯

- **自動翻譯**：GitHub Actions 工作流程處理所有翻譯
- **請勿手動編輯** `translations/` 目錄中的文件
- 翻譯元數據嵌入在每個翻譯文件中
- 支援語言：超過 48 種，包括阿拉伯語、中文、法語、德語、印地語、日語、韓語、葡萄牙語、俄語、西班牙語等

## 測試指令

### 文件驗證

由於此存儲庫主要是文件，測試重點包括：

1. **連結驗證**：確保所有內部連結正常運作
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **程式碼範例驗證**：測試程式碼範例是否能編譯/執行
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown 格式檢查**：檢查格式一致性
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### 範例專案測試

每個特定語言的範例都包含其專屬的測試方法：

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## 程式碼風格指南

### 文件風格

- 使用清晰、適合初學者的語言
- 提供多語言的程式碼範例（如適用）
- 遵循 Markdown 最佳實踐：
  - 使用 ATX 標題（`#` 語法）
  - 使用帶語言標識的圍欄程式碼塊
  - 為圖片提供描述性替代文字
  - 保持合理的行長（無硬性限制，但需合理）

### 程式碼範例風格

#### TypeScript/JavaScript
- 使用 ES 模組（`import`/`export`）
- 遵循 TypeScript 嚴格模式規範
- 包含類型註解
- 目標 ES2022

#### Python
- 遵循 PEP 8 風格指南
- 適當使用類型提示
- 為函數和類提供 docstring
- 使用現代 Python 特性（3.8+）

#### Java
- 遵循 Spring Boot 規範
- 使用 Java 21 特性
- 遵循標準 Maven 專案結構
- 包含 Javadoc 註解

### 文件組織

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## 建置與部署

### 文件部署

存儲庫使用 GitHub Pages 或類似工具進行文件託管（如適用）。推送至主分支時觸發以下流程：

1. 翻譯工作流程（`.github/workflows/co-op-translator.yml`）
2. 自動翻譯所有英文 Markdown 文件
3. 根據需要進行圖片本地化

### 無需建置過程

此存儲庫主要包含 Markdown 文件，核心課程內容無需編譯或建置步驟。

### 範例專案部署

個別範例專案可能包含部署指令：
- 請參閱 `03-GettingStarted/09-deployment/` 了解 MCP 伺服器部署指南
- Azure 容器應用部署範例位於 `11-MCPServerHandsOnLabs/`

## 貢獻指南

### 拉取請求流程

1. **分叉並克隆**：分叉存儲庫並在本地克隆
2. **建立分支**：使用描述性分支名稱（例如 `fix/typo-module-3`、`add/python-example`）
3. **進行修改**：僅編輯英文 Markdown 文件（勿修改翻譯）
4. **本地測試**：確認 Markdown 正常渲染
5. **提交 PR**：使用清晰的 PR 標題與描述
6. **CLA**：按提示簽署 Microsoft 貢獻者許可協議

### PR 標題格式

使用清晰、描述性的標題：
- `[Module XX] 簡要描述` 用於模組特定修改
- `[Samples] 描述` 用於範例程式碼修改
- `[Docs] 描述` 用於一般文件更新

### 可貢獻內容

- 修正文件或程式碼範例中的錯誤
- 新增其他語言的程式碼範例
- 對現有內容進行澄清與改進
- 新增案例研究或實用範例
- 報告不清楚或錯誤的內容

### 禁止事項

- 請勿直接編輯 `translations/` 目錄中的文件
- 請勿編輯 `translated_images/` 目錄
- 未經討論請勿新增大型二進制文件
- 未經協調請勿更改翻譯工作流程文件

## 附加說明

### 存儲庫維護

- **更新日誌**：所有重大更改記錄於 `changelog.md`
- **學習指南**：使用 `study_guide.md` 獲取課程導航概述
- **問題模板**：使用 GitHub 問題模板提交錯誤報告與功能請求
- **行為準則**：所有貢獻者必須遵守 Microsoft 開源行為準則

### 學習路徑

按順序學習模組（00-11）以獲得最佳效果：
1. **00-02**：基礎知識（介紹、核心概念、安全性）
2. **03**：透過實作入門
3. **04-05**：實用實作與高階主題
4. **06-10**：社群、最佳實踐與實際應用
5. **11**：綜合資料庫整合實驗室（13 個循序實驗）

### 支援資源

- **文件**：https://modelcontextprotocol.io/
- **規範**：https://spec.modelcontextprotocol.io/
- **社群**：https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**：Microsoft Azure AI Foundry Discord 伺服器
- **相關課程**：請參閱 README.md 獲取其他 Microsoft 學習路徑

### 常見問題排解

**問：我的 PR 未通過翻譯檢查**
答：請確認您僅編輯了根模組目錄中的英文 Markdown 文件，未修改翻譯版本。

**問：如何新增語言？**
答：語言支援由 co-op-translator 工作流程管理。請開啟問題討論新增語言。

**問：程式碼範例無法運作**
答：請確認您已按照特定範例的 README 中的設置指令操作，並檢查是否安裝了正確版本的依賴項。

**問：圖片無法顯示**
答：請確認圖片路徑為相對路徑並使用正斜線。圖片應位於 `images/` 目錄或 `translated_images/` 目錄（本地化版本）。

### 性能考量

- 翻譯工作流程可能需要幾分鐘完成
- 大型圖片應在提交前進行優化
- 保持單個 Markdown 文件內容集中且大小合理
- 使用相對連結以提高可移植性

### 專案治理

此專案遵循 Microsoft 開源實踐：
- 程式碼與文件使用 MIT 許可證
- Microsoft 開源行為準則
- 貢獻需簽署 CLA
- 安全問題：請遵循 SECURITY.md 指南
- 支援：請參閱 SUPPORT.md 獲取幫助資源

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。
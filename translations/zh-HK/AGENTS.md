# AGENTS.md

## 項目概覽

**MCP for Beginners** 是一個開源教育課程，旨在教授模型上下文協議（Model Context Protocol，MCP）——一個標準化框架，用於 AI 模型與客戶端應用之間的交互。本存儲庫提供全面的學習材料，並包含多種編程語言的實操代碼示例。

### 核心技術

- **編程語言**：C#、Java、JavaScript、TypeScript、Python、Rust
- **框架與 SDK**：
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **數據庫**：PostgreSQL（帶 pgvector 擴展）
- **雲平台**：Azure（容器應用、OpenAI、內容安全、應用洞察）
- **構建工具**：npm、Maven、pip、Cargo
- **文檔**：使用 Markdown，支持自動多語言翻譯（超過 48 種語言）

### 架構

- **11 個核心模塊（00-11）**：從基礎到高級主題的循序漸進學習路徑
- **實操實驗室**：提供多語言完整解決方案代碼的實踐練習
- **示例項目**：包含 MCP 服務器和客戶端的工作實現
- **翻譯系統**：基於 GitHub Actions 的自動化多語言支持工作流
- **圖片資產**：集中管理的圖片目錄，包含翻譯版本

## 設置命令

這是一個以文檔為主的存儲庫。大部分設置在各個示例項目和實驗室中完成。

### 存儲庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 使用示例項目

示例項目位於：
- `03-GettingStarted/samples/` - 特定語言的示例
- `03-GettingStarted/01-first-server/solution/` - 首個服務器實現
- `03-GettingStarted/02-client/solution/` - 客戶端實現
- `11-MCPServerHandsOnLabs/` - 綜合數據庫集成實驗室

每個示例項目都包含自己的設置說明：

#### TypeScript/JavaScript 項目
```bash
cd <project-directory>
npm install
npm start
```

#### Python 項目
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java 項目
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## 開發工作流程

### 文檔結構

- **模塊 00-11**：核心課程內容，按順序排列
- **translations/**：特定語言版本（自動生成，請勿直接編輯）
- **translated_images/**：本地化圖片版本（自動生成）
- **images/**：源圖片和圖表

### 修改文檔

1. 只編輯根模塊目錄（00-11）中的英文 Markdown 文件
2. 如有需要，更新 `images/` 目錄中的圖片
3. co-op-translator GitHub Action 會自動生成翻譯
4. 推送到主分支時會重新生成翻譯

### 使用翻譯

- **自動翻譯**：GitHub Actions 工作流處理所有翻譯
- **請勿手動編輯** `translations/` 目錄中的文件
- 翻譯元數據嵌入在每個翻譯文件中
- 支持的語言：超過 48 種，包括阿拉伯語、中文、法語、德語、印地語、日語、韓語、葡萄牙語、俄語、西班牙語等

## 測試說明

### 文檔驗證

由於這主要是一個文檔存儲庫，測試重點包括：

1. **鏈接驗證**：確保所有內部鏈接正常工作
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **代碼示例驗證**：測試代碼示例是否能編譯/運行
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

### 示例項目測試

每個特定語言的示例都包含自己的測試方法：

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

## 代碼風格指南

### 文檔風格

- 使用清晰、適合初學者的語言
- 在適用的地方提供多語言代碼示例
- 遵循 Markdown 最佳實踐：
  - 使用 ATX 樣式標題（`#` 語法）
  - 使用帶語言標識的圍欄代碼塊
  - 為圖片提供描述性替代文字
  - 保持合理的行長（無硬性限制，但需合理）

### 代碼示例風格

#### TypeScript/JavaScript
- 使用 ES 模塊（`import`/`export`）
- 遵循 TypeScript 嚴格模式約定
- 包含類型註解
- 目標 ES2022

#### Python
- 遵循 PEP 8 風格指南
- 在適當的地方使用類型提示
- 為函數和類提供文檔字符串
- 使用現代 Python 特性（3.8+）

#### Java
- 遵循 Spring Boot 約定
- 使用 Java 21 特性
- 遵循標準 Maven 項目結構
- 包含 Javadoc 註釋

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

## 構建與部署

### 文檔部署

存儲庫使用 GitHub Pages 或類似工具進行文檔托管（如適用）。對主分支的更改會觸發：

1. 翻譯工作流（`.github/workflows/co-op-translator.yml`）
2. 所有英文 Markdown 文件的自動翻譯
3. 根據需要進行圖片本地化

### 無需構建過程

此存儲庫主要包含 Markdown 文檔。核心課程內容無需編譯或構建步驟。

### 示例項目部署

各個示例項目可能有自己的部署說明：
- 請參閱 `03-GettingStarted/09-deployment/` 了解 MCP 服務器部署指南
- Azure 容器應用部署示例位於 `11-MCPServerHandsOnLabs/`

## 貢獻指南

### 拉取請求流程

1. **Fork 並克隆**：Fork 存儲庫並在本地克隆你的 Fork
2. **創建分支**：使用描述性分支名稱（例如 `fix/typo-module-3`、`add/python-example`）
3. **進行修改**：僅編輯英文 Markdown 文件（不要編輯翻譯文件）
4. **本地測試**：驗證 Markdown 是否正確渲染
5. **提交 PR**：使用清晰的 PR 標題和描述
6. **CLA**：按提示簽署 Microsoft 貢獻者許可協議

### PR 標題格式

使用清晰、描述性的標題：
- `[Module XX] 簡要描述` 用於特定模塊的更改
- `[Samples] 描述` 用於示例代碼更改
- `[Docs] 描述` 用於一般文檔更新

### 可貢獻內容

- 修復文檔或代碼示例中的錯誤
- 添加其他語言的新代碼示例
- 對現有內容進行澄清和改進
- 添加新案例研究或實用示例
- 報告不清楚或錯誤的內容

### 不可進行的操作

- 不要直接編輯 `translations/` 目錄中的文件
- 不要編輯 `translated_images/` 目錄
- 未經討論不要添加大型二進制文件
- 未經協調不要更改翻譯工作流文件

## 附加說明

### 存儲庫維護

- **更新日誌**：所有重大更改記錄在 `changelog.md` 中
- **學習指南**：使用 `study_guide.md` 獲取課程導航概覽
- **問題模板**：使用 GitHub 問題模板提交錯誤報告和功能請求
- **行為準則**：所有貢獻者必須遵守 Microsoft 開源行為準則

### 學習路徑

按順序學習模塊（00-11）以獲得最佳學習效果：
1. **00-02**：基礎知識（介紹、核心概念、安全性）
2. **03**：通過實操實現入門
3. **04-05**：實際應用和高級主題
4. **06-10**：社區、最佳實踐和實際應用
5. **11**：綜合數據庫集成實驗室（13 個連續實驗）

### 支援資源

- **文檔**：https://modelcontextprotocol.io/
- **規範**：https://spec.modelcontextprotocol.io/
- **社區**：https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**：Microsoft Azure AI Foundry Discord 伺服器
- **相關課程**：請參閱 README.md 獲取其他 Microsoft 學習路徑

### 常見問題排查

**問：我的 PR 未通過翻譯檢查**
答：確保你只編輯了根模塊目錄中的英文 Markdown 文件，而不是翻譯版本。

**問：如何添加新語言？**
答：語言支持由 co-op-translator 工作流管理。請開啟問題討論添加新語言。

**問：代碼示例無法運行**
答：確保你已按照特定示例的 README 中的設置說明操作。檢查是否安裝了正確版本的依賴項。

**問：圖片無法顯示**
答：確認圖片路徑是相對路徑並使用正斜杠。圖片應位於 `images/` 目錄或 `translated_images/` 中的本地化版本。

### 性能考量

- 翻譯工作流可能需要幾分鐘完成
- 大型圖片應在提交前進行優化
- 保持單個 Markdown 文件內容集中且大小合理
- 使用相對鏈接以提高可移植性

### 項目治理

此項目遵循 Microsoft 開源實踐：
- 代碼和文檔使用 MIT 許可證
- Microsoft 開源行為準則
- 貢獻需簽署 CLA
- 安全問題：遵循 SECURITY.md 指南
- 支援：請參閱 SUPPORT.md 獲取幫助資源

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
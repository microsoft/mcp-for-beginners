# AGENTS.md

## 專案概覽

**初學者 MCP** 是一個開源的教學課程，用於學習模型上下文協議 (Model Context Protocol, MCP)——一個 AI 模型與客戶端應用程式之間交互的標準化框架。本儲存庫提供涵蓋多種程式語言的實作程式碼範例的完整學習材料。

### 主要技術

- <strong>程式語言</strong>: C#、Java、JavaScript、TypeScript、Python、Rust
- **框架與 SDK**:
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- <strong>資料庫</strong>: 搭配 pgvector 擴充套件的 PostgreSQL
- <strong>雲端平台</strong>: Azure（容器應用程式、OpenAI、內容安全、應用程式洞察）
- <strong>建置工具</strong>: npm、Maven、pip、Cargo
- <strong>文件</strong>: 使用 Markdown，並搭配自動化多語言翻譯（超過 48 種語言）

### 架構

- **11 個核心模組（00-11）**: 從基礎到進階的順序學習路徑
- <strong>實作實驗室</strong>: 多語言完整解決方案程式碼的實務練習
- <strong>範例專案</strong>: 可運作的 MCP 伺服器與客戶端實作
- <strong>翻譯系統</strong>: 用於多語言支援的自動 GitHub Actions 工作流程
- <strong>圖片資源</strong>: 集中管理圖片目錄並附有翻譯版本

## 設定指令

這是一個以文件為主的儲存庫，大多數設定工作發生在各個範例專案與實驗室中。

### 儲存庫設定

```bash
# 複製此程式庫
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 使用範例專案

範例專案位置為：
- `03-GettingStarted/samples/` - 特定語言範例
- `03-GettingStarted/01-first-server/solution/` - 第一個伺服器實作
- `03-GettingStarted/02-client/solution/` - 客戶端實作
- `11-MCPServerHandsOnLabs/` - 全面性資料庫整合實驗室

每個範例專案都有自己的設定說明：

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
# 或者
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

### MCP 7-28 準備事項

#### 儲存庫準備清單

- [x] <strong>新貢獻者清晰度</strong>：此文件定義儲存庫目的、
  結構、貢獻規則及範例設定路徑。
- [x] **精確標記的建置/測試/程式碼風格檢查指令**：
  - 儲存庫文件風格檢查：
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - 儲存庫文件連結模式稽核：
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript 範例驗證：
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python 範例驗證：
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java 範例驗證：
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **一個可以成為 MCP 工具的現實工作流程**：
  `validate_curriculum_change`
- [x] **輸入/輸出是明確的**（見下方規格）。
- [x] <strong>權限和失敗模式有記錄</strong>（見下方規格）。
- [x] **CI 測試性是明確的**（確定性命令、明確的
  退出代碼和機器可讀輸出）。

#### 候選 MCP 工具工作流程：`validate_curriculum_change`

##### 目標

驗證課程文件變更及代表性範例程式碼
健康狀況，於合併前。

##### 輸入

- `changed_paths: string[]`（必填）- PR 中變更的相對路徑。
- `run_docs_lint: boolean`（預設 `true`）
- `run_links_audit: boolean`（預設 `true`）
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  （預設全部為 `false`）

##### 輸出

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### 權限

- 僅讀取工作區檔案並寫入工具產生的產物（例如 lint
  報告、測試日誌）；不得寫入 `translations/` 或
  `translated_images/`。
- 執行本地 shell 命令。
- 網路存取僅限於套件還原（`npm ci`、
  `python -m pip install`、`mvn` 依賴解析）。
- 不允許推送、合併或修改 `translations/` 或
  `translated_images/`。

##### 失敗模式

- `E_NO_INPUT_PATHS`：`changed_paths` 為空。
- `E_INVALID_PATH`：輸入路徑逃出存儲庫根目錄。
- `E_LINT_FAILED`：markdown lint 以非零碼退出。
- `E_LINK_AUDIT_FAILED`：連結審核命令以非零碼退出。
- `E_SAMPLE_TEST_FAILED`：範例測試/構建以非零碼退出。
- `E_TIMEOUT`：命令超出設定的超時時限。

##### 推薦的 CI 合約

自動驗證時，配置 CI 作業以：

- 對觸及 `*.md`、範例程式碼或本檔案的拉取請求觸發。
- 執行上述完全相同的命令。
- 將日誌保存為產物。
- 任何非零退出碼導致作業失敗。

#### 若您從本存儲庫發佈 MCP 伺服器

- [ ] 閱讀 MCP 7-28 草案變更日誌：
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] 對 SDK beta 版執行您的伺服器：
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] 移除會話與握手假設；將每個請求視為
  自包含：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] 針對原始 HTTP 請求，發送 `Mcp-Method` 與 `Mcp-Name` 標頭：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] 審核硬編碼錯誤碼（`missing resource` 從 `-32002` 移至 `-32602`）。

- [ ] 標示並規劃棄用的根、抽樣及
  紀錄遷移：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] 遷移出實驗性的 `2025-11-25` Tasks API：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] 檢視 OAuth 和 OpenID Connect 強化授權：
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### 文件結構

- **模組 00-11**：按順序的核心課程內容
- **translations/**：特定語言版本（自動生成，不要直接編輯）
- **translated_images/**：本地化圖片版本（自動生成）
- **images/**：原始圖片及圖表

### 進行文件修改

1. 只修改根模組目錄（00-11）中的英文 markdown 檔案
2. 如有需要，更新 `images/` 目錄中的圖片
3. co-op-translator GitHub Action 將自動產生翻譯
4. 打包推送至 main 分支時自動重新產生翻譯

### 使用翻譯服務

- <strong>自動翻譯</strong>：由 GitHub Actions 工作流程管理所有翻譯
- <strong>切勿手動編輯</strong> `translations/` 目錄中的檔案
- 翻譯元資料已嵌入每個翻譯檔案中
- 支援語言：48 種以上，包括阿拉伯語、中文、法語、德語、印地語、日語、韓語、葡萄牙語、俄語、西班牙語及更多

## 測試說明

### 文件驗證

由於此主要是文件庫，測試重點為：

1. <strong>連結模式審核</strong>：列出 Markdown 連結以供檢查

   ```bash
   # 列出 Markdown 鏈接（模式審核）
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. <strong>程式範例驗證</strong>：確保程式範例能編譯/執行

   ```bash
   # 導航到特定範例並執行其測試
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown 格式檢查**：檢查格式一致性

   ```bash
   # 如有需要，請使用 markdownlint
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### 範例專案測試

每個語言的範例均包含其專屬的測試方法：

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

## 程式碼風格指引

### 文件風格

- 使用清晰、易懂的初學者友善語言
- 必要時包含多語言的程式範例
- 遵循 markdown 最佳實踐：
  - 使用 ATX 標題語法（`#`）
  - 使用帶語言標識的圍欄程式區塊
  - 為圖片提供具描述性的替代文字
  - 保持行長合理（無硬性限制，但需合理）

### 程式範例風格

#### TypeScript/JavaScript
- 使用 ES 模組（`import`/`export`）
- 遵循 TypeScript 嚴格模式慣例
- 加入類型註解
- 目標 ES2022

#### Python
- 遵循 PEP 8 風格指引
- 適當使用型別提示
- 函數與類別包含 docstrings
- 使用現代 Python 功能（3.8+）

#### Java
- 遵循 Spring Boot 慣例
- 使用 Java 21 功能
- 遵循標準 Maven 專案結構
- 包含 Javadoc 註解

### 檔案組織

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

本儲存庫使用 GitHub Pages 或類似服務承載文件（如適用）。對 main 分支的變更會觸發：

1. 翻譯工作流程（`.github/workflows/co-op-translator.yml`）
2. 對所有英文 markdown 檔案自動翻譯
3. 依需要進行圖片本地化

### 無需建置程序

本儲存庫主要包含 markdown 文件。核心課程內容不需要編譯或建置步驟。

### 範例專案部署

各範例專案可能有其部署說明：
- 請參閱 `03-GettingStarted/09-deployment/` 以獲得 MCP 伺服器部署指引
- `11-MCPServerHandsOnLabs/` 內的 Azure Container Apps 部署範例

## 貢獻指南

### Pull Request 流程

1. <strong>分叉並複製</strong>：Fork 儲存庫並在本機複製您的 Fork
2. <strong>建立分支</strong>：使用具描述性的分支名稱（如 `fix/typo-module-3`、`add/python-example`）
3. <strong>進行修改</strong>：僅編輯英文 markdown 檔案（不含翻譯版本）
4. <strong>本機測試</strong>：驗證 markdown 是否正常渲染
5. **提交 PR**：使用清楚的 PR 標題和描述
6. **簽署 CLA**：當提示時簽署 Microsoft 貢獻者授權協議

### PR 標題格式

使用清楚且描述性的標題：
- `[Module XX] 簡短描述` 用於模組專屬修改
- `[Samples] 描述` 用於範例程式碼修改
- `[Docs] 描述` 用於一般文件更新

### 可貢獻項目

- 文件或程式範例中的錯誤修正
- 新增其他語言的程式範例
- 針對現有內容的澄清與改進
- 新增案例研究或實務範例
- 對不清楚或錯誤內容發佈問題回報

### 不可為之事

- 不要直接編輯 `translations/` 目錄內檔案
- 不要修改 `translated_images/` 目錄
- 未經討論，不要添加大型二進位檔案
- 未經協調，不要改動翻譯工作流程文件

## 其他說明

### 儲存庫維護

- <strong>變更日誌</strong>：所有重大變更都會記錄在 `changelog.md`
- <strong>學習指南</strong>：使用 `study_guide.md` 瀏覽課程概覽
- <strong>問題模板</strong>：使用 GitHub 問題模板來回報錯誤與功能請求
- <strong>行為守則</strong>：所有貢獻者必須遵守 Microsoft 開源行為守則

### 學習路徑

按模組順序（00-11）學習以達最佳效果：
1. **00-02**：基礎（入門、核心概念、安全）
2. **03**：實務入門與操作
3. **04-05**：實務實作與進階主題
4. **06-10**：社群、最佳實踐與實際應用
5. **11**：全面的資料庫整合實驗室（13 個循序漸進實驗室）

### 支援資源

- <strong>文件</strong>： https://modelcontextprotocol.io/
- <strong>規範</strong>： https://spec.modelcontextprotocol.io/
- <strong>社群</strong>： https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**：Microsoft Foundry Discord 伺服器
- <strong>相關課程</strong>：請查看 README.md 其他 Microsoft 學習路徑

### 常見問題排除

**問：我的 PR 未通過翻譯檢查**
答：請確認只修改了根模組目錄中的英文 markdown 檔案，並非翻譯版本。

**問：如何新增一種語言？**
答：語言支援由 co-op-translator 工作流程管理。如要新增語言，請開 issue 討論。

**問：程式範例無法運作**

A: 確保您已遵循特定範例的 README 中的設定指示。檢查是否已安裝正確版本的相依項。

**Q: 圖片沒有顯示**
A: 驗證圖片路徑為相對路徑且使用正斜線。圖片應位於 `images/` 目錄或供本地化版本使用的 `translated_images/`。

### 效能考量

- 翻譯工作流程可能需要幾分鐘才會完成
- 大型圖片應在提交前進行優化
- 保持單一 Markdown 檔案專注且大小適中
- 使用相對連結以提高可攜性

### 專案治理

本專案遵循 Microsoft 開源作法：
- 程式碼及文件使用 MIT 授權
- Microsoft 開源行為準則
- 需簽署 CLA 以做出貢獻
- 安全性問題：遵循 SECURITY.md 指南
- 支援：請參考 SUPPORT.md 以取得協助資源

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
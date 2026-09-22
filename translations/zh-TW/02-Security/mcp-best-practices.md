# MCP 安全最佳實踐 - 2026 年 9 月更新

本綜合指南概述了根據
**MCP 規範 2026-07-28** 及當前行業標準，
實施模型上下文協議（MCP）系統的重要安全最佳實踐。這些
實踐涵蓋傳統安全問題以及 MCP 部署特有的 AI 專屬威脅。


## 關鍵安全要求

### 強制性安全控制（必須要求）

1. <strong>令牌驗證</strong>：MCP 伺服器 <strong>不得</strong> 接受任何非明確為該 MCP 伺服器簽發的令牌
2. <strong>授權驗證</strong>：實施授權的 MCP 伺服器 <strong>必須</strong> 驗證所有入站請求，且 <strong>不得</strong> 使用會話進行身份驗證  
3. <strong>用戶同意</strong>：使用靜態第三方客戶端 ID 的 MCP 代理伺服器 <strong>必須</strong> 在轉發授權流程前獲得每個 MCP 客戶端的明確同意
4. <strong>狀態句柄安全</strong>：MCP 伺服器 <strong>不得</strong> 將應用狀態句柄的持有視作身份驗證，且 <strong>必須</strong> 對每個使用句柄的請求進行授權



## 核心安全實踐

### 1. 輸入驗證與淨化
- <strong>全面輸入驗證</strong>：驗證並淨化所有輸入以防止注入攻擊、混淆代理問題及提示注入漏洞
- <strong>參數方案強制</strong>：對所有工具參數和 API 輸入實施嚴格的 JSON 方案驗證
- <strong>內容過濾</strong>：使用 Microsoft Prompt Shields 和 Azure Content Safety 過濾提示和回應中的惡意內容
- <strong>輸出淨化</strong>：在呈現給用戶或下游系統前驗證並淨化所有模型輸出

### 2. 身份驗證與授權卓越  
- <strong>外部身份提供者</strong>：將身份驗證委託給成熟身份提供者（Microsoft Entra ID、OAuth 2.1 提供者），避免自訂身份驗證
- <strong>客戶端註冊</strong>：優先使用客戶端 ID 元資料文件或預先註冊；僅為相容性使用已廢棄的動態客戶端註冊
- <strong>細粒度權限</strong>：基於最小權限原則實施粒度細緻的工具專屬權限
- <strong>令牌生命週期管理</strong>：使用短期存活的存取令牌，搭配安全輪換及適當的受眾驗證
- <strong>多因素身份驗證</strong>：對所有管理訪問和敏感操作要求啟用 MFA

### 3. 安全通訊協定
- <strong>傳輸層安全</strong>：遠端 HTTP MCP 通訊採用 HTTPS 且執行適當的憑證驗證
	本地 stdio 伺服器使用進程隔離及環境憑證

- <strong>端到端加密</strong>：對高度敏感的傳輸與靜態資料實施額外加密層
- <strong>憑證管理</strong>：維護妥善的憑證生命週期管理及自動續期流程
- <strong>協定版本強制</strong>：使用 MCP `2026-07-28`，在每個請求中包含必要的版本元資料，並拒絕不受支持版本


### 4. 進階速率限制與資源保護
- <strong>多層速率限制</strong>：根據用戶、憑證、操作、工具及資源實施速率限制以預防濫用

- <strong>自適應速率限制</strong>：使用機器學習基於使用模式及威脅指標適應速率限制
- <strong>資源配額管理</strong>：設定計算資源、記憶體使用和執行時間的適當限制
- **DDoS 防護**：部署完整的 DDoS 防護與流量分析系統

### 5. 全面日誌記錄與監控
- <strong>結構化審計日誌</strong>：為所有 MCP 操作、工具執行和安全事件實施詳細且可搜尋的日誌
- <strong>即時安全監控</strong>：部署 SIEM 系統，結合 AI 驅動的異常偵測應對 MCP 工作負載
- <strong>隱私合規日誌紀錄</strong>：記錄安全事件，同時尊重資料隱私要求及法規
- <strong>事件響應整合</strong>：將日誌系統與自動化事件響應工作流程相連接

### 6. 強化安全儲存實踐
- <strong>硬體安全模組</strong>：對關鍵密碼操作使用 HSM 支援的密鑰儲存（Azure Key Vault、AWS CloudHSM）
- <strong>加密密鑰管理</strong>：實施妥善的密鑰輪替、隔離及存取控制
- <strong>機密管理</strong>：將所有 API 金鑰、令牌和憑證存放於專用的祕密管理系統
- <strong>資料分類</strong>：根據敏感程度分類資料並採用相應的保護措施

### 7. 進階令牌管理
- <strong>防止令牌透傳</strong>：明確禁止繞過安全控管的令牌透傳模式
- <strong>受眾驗證</strong>：始終驗證令牌的受眾聲明與預期的 MCP 伺服器身份相符
- **基於 Claim 的授權**：根據令牌 claims 及用戶屬性實施細粒度授權
- <strong>令牌綁定</strong>：驗證令牌是否針對預期 MCP 資源，並在伺服器端將應用狀態句柄綁定於認證主體


### 8. 安全的應用狀態管理

- <strong>密碼狀態句柄</strong>：生成對應遍歷請求的難以預測且不透明的狀態句柄

- <strong>用戶專屬綁定</strong>：在伺服器端將每個句柄綁定至經身份驗證的主體；不信任客戶端提供的用戶 ID

- <strong>生命週期控管</strong>：過期及撤銷句柄，並定義調用方如何從過期狀態中恢復

- <strong>逐請求授權</strong>：每次使用句柄時重新檢查授權；句柄是名稱，而非憑證


### 9. AI 專屬安全控管
- <strong>提示注入防禦</strong>：部署 Microsoft Prompt Shields，使用聚光燈、分隔符及數據標記技術
- <strong>工具中毒防範</strong>：驗證工具元資料，監控動態變更，確保工具完整性
- <strong>模型輸出驗證</strong>：掃描模型輸出以防資料洩露、有害內容或安全政策違規
- <strong>上下文視窗防護</strong>：實施控制以防上下文視窗中毒及操控攻擊

### 10. 工具執行安全
- <strong>執行沙箱</strong>：在容器化、隔離環境中運行工具，設置資源限制
- <strong>權限分離</strong>：以最低必要權限執行工具並分離服務帳戶
- <strong>網路隔離</strong>：為工具執行環境實施網路分段
- <strong>執行監控</strong>：監控工具執行以偵測異常行為、資源使用和安全違規

### 11. 持續安全驗證
- <strong>自動化安全測試</strong>：將安全測試整合至 CI/CD 流程，使用如 GitHub Advanced Security 等工具
- <strong>漏洞管理</strong>：定期掃描所有相依性，包括 AI 模型與外部服務
- <strong>滲透測試</strong>：針對 MCP 實作定期進行安全評估
- <strong>安全程式碼審查</strong>：對所有 MCP 相關程式碼更動實施強制安全審查

### 12. AI 供應鏈安全
- <strong>元件驗證</strong>：驗證所有 AI 元件（模型、嵌入、API）的來源、完整性與安全性
- <strong>依賴管理</strong>：維護所有軟體及 AI 相依性清單與漏洞追蹤
- <strong>可信儲存庫</strong>：使用驗證且可信來源取得所有 AI 模型、函式庫與工具
- <strong>供應鏈監控</strong>：持續監控 AI 服務提供者與模型儲存庫是否遭受破壞

## 進階安全模式

### MCP 零信任架構
- **永不信任，持續驗證**：對所有 MCP 參與者實施持續驗證
- <strong>微分段</strong>：透過細粒度網路及身份控管隔離 MCP 元件
- <strong>條件訪問</strong>：實施基於風險的訪問控制，依據上下文和行為進行自適應調整
- <strong>持續風險評估</strong>：根據當前威脅指標動態評估安全狀態

### 隱私保護 AI 實作
- <strong>資料最小化</strong>：每個 MCP 操作僅暴露極少必要資料
- <strong>差分隱私</strong>：對敏感資料處理實施保護隱私技術
- <strong>同態加密</strong>：使用先進加密技術對加密資料執行安全計算
- <strong>聯邦學習</strong>：實施分散學習，以保留資料本地性與隱私

### AI 系統的事件響應
- **AI 特定事件程序**：制定針對 AI 與 MCP 特定威脅的事件響應程序
- <strong>自動化響應</strong>：對常見 AI 安全事件實施自動隔離與補救  
- <strong>取證能力</strong>：維持 AI 系統妥協和資料外洩的取證準備
- <strong>恢復程序</strong>：建立從 AI 模型中毒、提示注入攻擊和服務妥協中復原的程序

## 實作資源與標準

### 🏔️ 實作安全訓練
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - 在 Azure 上保護 MCP 伺服器的全面實作工作坊
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - 參考架構及 OWASP MCP Top 10 實作指導

### 官方 MCP 文件
- [MCP 規範 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 最新 MCP 協議規範
- [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 官方安全指引
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP 授權模式
- [MCP 傳輸](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - 傳輸需求

### 微軟安全解決方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 先進的提示注入防護
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面 AI 內容過濾
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企業身份與訪問管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 祕密與憑證安全管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供應鏈與程式碼安全掃描

### 安全標準與框架
- [OAuth 2.1 安全最佳實踐](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 當前 OAuth 安全指導
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 網頁應用安全風險
- [OWASP LLM Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 專屬安全風險
- [NIST AI 風險管理框架](https://www.nist.gov/itl/ai-risk-management-framework) - 全面 AI 風險管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 資訊安全管理系統

### 實作指南及教學
- [Azure API Management 作為 MCP 認證閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企業認證模式
- [Microsoft Entra ID 與 MCP 伺服器整合](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者整合
- [安全令牌儲存實作](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳實踐
- [AI 端到端加密](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 先進加密模式

### 進階安全資源
- [Microsoft 安全開發生命週期](https://www.microsoft.com/sdl) - 安全開發實踐
- [AI 紅隊指導](https://learn.microsoft.com/security/ai-red-team/) - AI 專屬安全測試
- [AI 系統威脅建模](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 威脅建模方法論
- [AI 隱私工程](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 保護隱私的 AI 技術

### 合規與治理
- [AI 的 GDPR 合規](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 系統中的隱私合規
- [AI 治理框架](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 負責任的 AI 實施
- [AI 服務提供者的 SOC 2](https://learn.microsoft.com/compliance/regulatory/offering-soc) - 安全控管
- [AI 的 HIPAA 合規](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 醫療 AI 合規要求

### DevSecOps 與自動化
- [AI 的 DevSecOps 管線](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全 AI 開發管線
- [自動安全測試](https://learn.microsoft.com/security/engineering/devsecops) - 持續安全驗證
- [基礎架構即代碼安全](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全基礎架構部署
- [AI 容器安全](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 工作負載容器化安全

### 監控與事件響應  
- [AI 工作負載的 Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/overview) - 綜合監控解決方案
- [AI 安全事件響應](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 專屬事件程序
- [AI 系統的 SIEM](https://learn.microsoft.com/azure/sentinel/overview) - 安全資訊與事件管理

- [AI 威脅情報](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威脅情報來源

## 🔄 持續改進

### 緊跟不斷演變的標準
- **MCP 規範更新**：監控官方 MCP 規範變更及安全公告
- <strong>威脅情報</strong>：訂閱 AI 安全威脅資訊和漏洞資料庫  
- <strong>社群參與</strong>：參加 MCP 安全社群討論和工作小組
- <strong>定期評估</strong>：每季進行安全態勢評估並相應更新做法

### 為 MCP 安全做出貢獻
- <strong>安全研究</strong>：參與 MCP 安全研究與漏洞揭露計劃
- <strong>最佳實踐分享</strong>：與社群分享安全實踐與經驗教訓
- <strong>標準制定</strong>：參與 MCP 規範開發與安全標準制定
- <strong>工具開發</strong>：開發並分享 MCP 生態系的安全工具和函式庫

---

*本文件反映截至 2026 年 9 月 9 日的 MCP 安全最佳實踐，
基於 MCP 規範 `2026-07-28`。隨著協議與威脅環境演變，應定期
審查安全實踐。*

## 下一步

- 閱讀：[MCP 安全最佳實踐](./mcp-security-best-practices.md)
- 返回：[安全模組總覽](./README.md)
- 繼續至：[模組 3：入門](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
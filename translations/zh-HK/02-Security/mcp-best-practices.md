# MCP 安全最佳實踐 - 2026 年 9 月更新

本綜合指南概述了根據
**MCP 規範 2026-07-28** 及當前行業標準實施模型上下文協議 (MCP) 系統的必要安全最佳實踐。這些
實踐涵蓋了傳統安全問題及 MCP 部署中獨有的 AI 特定威脅。



## 關鍵安全需求

### 強制性安全控制（必須要求）

1. <strong>令牌驗證</strong>：MCP 伺服器 <strong>不得</strong> 接受非專門為該 MCP 伺服器簽發的任何令牌
2. <strong>授權驗證</strong>：實施授權的 MCP 伺服器 <strong>必須</strong> 驗證所有入站請求，且<strong>不得</strong>使用會話作為身份驗證
3. <strong>用戶同意</strong>：使用靜態第三方客戶端 ID 的 MCP 代理伺服器 <strong>必須</strong> 在轉發授權流程前獲得每個 MCP 客戶端的明確同意
4. <strong>狀態處理憑證安全</strong>：MCP 伺服器 <strong>不得</strong> 將持有應用狀態處理憑證視為身份驗證，<strong>必須</strong> 對每個使用憑證的請求進行授權



## 核心安全實踐

### 1. 輸入驗證與淨化
- <strong>全面輸入驗證</strong>：驗證並淨化所有輸入以防止注入攻擊、混淆代理問題及提示注入漏洞
- <strong>參數結構強制</strong>：對所有工具參數及 API 輸入實施嚴格的 JSON 架構驗證
- <strong>內容過濾</strong>：使用 Microsoft Prompt Shields 和 Azure 內容安全篩選提示及回應中的惡意內容
- <strong>輸出淨化</strong>：在呈現給用戶或下游系統前驗證並淨化所有模型輸出

### 2. 認證與授權卓越
- <strong>外部身份提供者</strong>：將身份驗證委派給已建立的身份提供者（Microsoft Entra ID、OAuth 2.1 提供者），而非自建身份驗證
- <strong>客戶端註冊</strong>：優先使用客戶端 ID 元數據文件或預註冊；僅為兼容用途使用已棄用的動態客戶端註冊
- <strong>細粒度許可</strong>：按照最小權限原則實施細粒度、工具特定的許可
- <strong>令牌生命週期管理</strong>：使用短期存活存取令牌，配合安全輪換及正確的受眾驗證
- <strong>多因素認證</strong>：所有管理訪問及敏感操作必須要求 MFA

### 3. 安全通訊協定
- <strong>傳輸層安全</strong>：針對遠程 HTTP MCP 通訊使用 HTTPS 並正確驗證憑證
	；本地 stdio 伺服器則使用程序隔離和環境憑證
- <strong>端到端加密</strong>：對高度敏感的傳輸中及靜態資料實施附加加密層
- <strong>憑證管理</strong>：維護妥善的憑證生命週期管理，包括自動續期流程
- <strong>協議版本強制</strong>：採用 MCP `2026-07-28`，在每個請求中包含所需版本元資料，並拒絕不支援的版本



### 4. 高級率限與資源保護
- <strong>多層次率限</strong>：根據用戶、憑證、操作、工具及資源實施速率限制以防止濫用

- <strong>自適應率限</strong>：利用機器學習的速率限制，根據使用模式及威脅指標動態調整
- <strong>資源配額管理</strong>：設定計算資源、記憶體使用量及執行時間的適當限制
- **DDoS 防護**：部署完善的 DDoS 防護與流量分析系統

### 5. 全面日誌紀錄與監控
- <strong>結構化審核日誌</strong>：為所有 MCP 操作、工具執行及安全事件實施詳細、可搜索的日誌
- <strong>即時安全監控</strong>：部署支援 AI 异常偵測的 SIEM 系統監控 MCP 工作負載
- <strong>符合隱私的日誌紀錄</strong>：在尊重資料隱私要求與規範前提下記錄安全事件
- <strong>事件響應整合</strong>：將日誌系統連結至自動化事件響應流程

### 6. 強化安全儲存實踐
- <strong>硬體安全模組</strong>：對關鍵密碼操作使用 HSM 支援的密鑰儲存（Azure Key Vault、AWS CloudHSM）
- <strong>加密金鑰管理</strong>：實施妥善的金鑰輪換、隔離及存取控制
- <strong>密鑰管理</strong>：將所有 API 金鑰、令牌和憑證存放在專用的密鑰管理系統中
- <strong>資料分類</strong>：根據敏感度層級分類資料，並應用適當保護措施

### 7. 先進令牌管理
- <strong>禁止令牌轉發</strong>：明確禁止繞過安全控制的令牌直通使用模式
- <strong>受眾驗證</strong>：務必驗證令牌受眾聲明與預期的 MCP 伺服器身份匹配
- <strong>基於聲明的授權</strong>：根據令牌聲明及用戶屬性實施細粒度授權
- <strong>令牌綁定</strong>：驗證令牌目標為預期 MCP 資源，並將應用狀態處理憑證於伺服器端綁定至已驗證的主體


### 8. 安全應用狀態

- <strong>加密狀態處理憑證</strong>：為跨請求的狀態產生不透明、非決定性憑證

- <strong>用戶專屬綁定</strong>：將每個憑證伺服器端綁定至已認證主體；不信任由客戶端提供的用戶 ID
- <strong>生命週期控制</strong>：憑證到期與撤銷，並定義呼叫者如何復原陳舊狀態
- <strong>逐請求授權</strong>：每次使用憑證時重新檢查授權；憑證是名稱，而非憑證資料




### 9. AI 特定安全控制
- <strong>提示注入防禦</strong>：部署 Microsoft Prompt Shields，採用聚光燈、分隔符及資料標記技術
- <strong>工具中毒防範</strong>：驗證工具元資料，監控動態變更並核實工具完整性
- <strong>模型輸出驗證</strong>：掃描模型輸出以防止資料外洩、有害內容或安全政策違規
- <strong>上下文視窗保護</strong>：實施控制以防止上下文視窗中毒及操作攻擊

### 10. 工具執行安全
- <strong>執行沙箱化</strong>：在容器化、隔離環境中執行工具，並設置資源限制
- <strong>權限分離</strong>：以最低必要權限及分離服務帳戶執行工具
- <strong>網絡隔離</strong>：為工具執行環境實施網路分段
- <strong>執行監控</strong>：監控工具執行的異常行為、資源使用及安全違規

### 11. 持續安全驗證
- <strong>自動化安全測試</strong>：將安全測試整合於 CI/CD 管線，使用 GitHub Advanced Security 等工具
- <strong>漏洞管理</strong>：定期掃描所有依賴項，包括 AI 模型及外部服務
- <strong>滲透測試</strong>：定期進行針對 MCP 實施的安全評估
- <strong>安全程式碼審查</strong>：對所有 MCP 相關代碼變更實施強制安全審查

### 12. AI 供應鏈安全
- <strong>組件驗證</strong>：驗證所有 AI 組件（模型、嵌入、API）的來源、完整性及安全性
- <strong>依賴管理</strong>：維護所有軟件及 AI 依賴的最新清單，並追蹤漏洞
- <strong>可信倉庫</strong>：使用驗證的可信來源取得所有 AI 模型、庫及工具
- <strong>供應鏈監控</strong>：持續監控 AI 服務提供者及模型倉庫是否遭受攻擊


## 進階安全模式

### MCP 的零信任架構
- **永不信任，始終驗證**：對所有 MCP 參與者實施持續驗證
- <strong>微分段</strong>：使用細緻的網路和身份控管隔離 MCP 組件
- <strong>條件式存取</strong>：實施根據情境與行為調整的風險基礎存取控管
- <strong>持續風險評估</strong>：根據當前威脅指標動態評估安全態勢

### 隱私保護的 AI 實作
- <strong>資料最小化</strong>：僅揭露每個 MCP 操作所需的最少資料
- <strong>差分隱私</strong>：對敏感資料處理實施隱私保護技術
- <strong>同態加密</strong>：使用先進加密技術在加密資料上進行安全運算
- <strong>聯邦學習</strong>：實施分散式學習方法，保護資料在本地和隱私

### AI 系統的事件應變
- **AI 專屬事件程序**：制定針對 AI 及 MCP 特定威脅的事件應變程序
- <strong>自動化回應</strong>：對常見 AI 安全事件實施自動封鎖與修復  
- <strong>鑑識能力</strong>：維持對 AI 系統入侵與資料外洩的鑑識準備
- <strong>復原程序</strong>：建立從 AI 模型投毒、提示注入攻擊及服務破壞中復原的程序

## 實作資源與標準

### 🏔️ 實務安全訓練
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - 針對 Azure 中 MCP 伺服器安全的完整實務工作坊
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - 參考架構與 OWASP MCP 十大實作指南

### 官方 MCP 文件
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 最新 MCP 協議規範
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 官方安全指導
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP 授權模式
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - 傳輸需求

### 微軟安全解決方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 先進的提示注入防護
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面性的 AI 內容過濾
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企業身份與存取管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全的秘密與憑證管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供應鏈與程式碼安全掃描

### 安全標準與框架
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 最新 OAuth 安全指導
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 網頁應用程式安全風險
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 專屬安全風險
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 全面的 AI 風險管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 資訊安全管理系統

### 實作指南與教學
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企業身份驗證模式
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者整合
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳實踐
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 先進加密模式

### 進階安全資源
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 安全開發實務
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI 專屬安全測試
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 威脅建模方法論
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 隱私保護 AI 技術

### 合規與治理
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 系統的隱私合規
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 負責任 AI 實作
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 服務供應商的安全控管
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 醫療 AI 合規要求

### DevSecOps 與自動化
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全的 AI 開發流程
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 持續安全驗證
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全的基礎架構部署
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 工作負載的容器安全

### 監控與事件應變  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 全面監控解決方案
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 專屬事件程序
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - 安全資訊與事件管理

- [人工智能威脅情報](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威脅情報來源

## 🔄 持續改進

### 緊貼不斷演變的標準
- **MCP 規範更新**：監察官方 MCP 規範變更及安全公告
- <strong>威脅情報</strong>：訂閱 AI 安全威脅來源及漏洞資料庫  
- <strong>社群參與</strong>：參加 MCP 安全社群討論及工作小組
- <strong>定期評估</strong>：進行季度安全態勢評估並相應更新做法

### 為 MCP 安全作出貢獻
- <strong>安全研究</strong>：參與 MCP 安全研究及漏洞披露計劃
- <strong>最佳實踐分享</strong>：與社群分享安全實作及經驗教訓
- <strong>標準制定</strong>：參與 MCP 規範制定及安全標準創建
- <strong>工具開發</strong>：開發及分享適用於 MCP 生態系統的安全工具及庫

---

*本文件反映 MCP 安全最佳實踐至 2026 年 9 月 9 日，
基於 MCP 規範 `2026-07-28`。安全實踐應隨著協議及威脅環境演進
定期檢視。*

## 下一步

- 閱讀：[MCP 安全最佳實踐](./mcp-security-best-practices.md)
- 返回：[安全模組概述](./README.md)
- 繼續：[模組 3：入門指南](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
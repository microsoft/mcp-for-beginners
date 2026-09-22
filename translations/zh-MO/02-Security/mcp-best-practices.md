# MCP 安全最佳實踐 - 2026年9月更新

本綜合指南概述了基於
**MCP 規範 2026-07-28** 及當前行業標準的
Model Context Protocol (MCP) 系統實施的重要安全最佳實踐。這些
做法涵蓋了傳統安全問題及 MCP 部署特有的 AI 專屬威脅。


## 關鍵安全要求

### 強制性安全控制（必須要求）

1. <strong>令牌驗證</strong>：MCP 伺服器<strong>不得</strong>接受非明確為該 MCP 伺服器簽發的任何令牌
2. <strong>授權驗證</strong>：實施授權的 MCP 伺服器<strong>必須</strong>驗證所有入站請求，並<strong>不得</strong>使用會話進行身份驗證  
3. <strong>用戶同意</strong>：使用靜態第三方客戶端 ID 的 MCP 代理伺服器<strong>必須</strong>在轉發授權流程前獲取每個 MCP 客戶端的明確同意
4. <strong>狀態句柄安全</strong>：MCP 伺服器<strong>不得</strong>將應用狀態句柄的持有視為身份驗證，並且<strong>必須</strong>授權使用該句柄的每個請求



## 核心安全實踐

### 1. 輸入驗證與清理
- <strong>全面輸入驗證</strong>：驗證並清理所有輸入，以防止注入攻擊、代理混淆問題及提示注入漏洞
- <strong>參數結構約束</strong>：對所有工具參數及 API 輸入實施嚴格的 JSON 架構驗證
- <strong>內容過濾</strong>：使用 Microsoft Prompt Shields 與 Azure Content Safety 過濾提示與回應中的惡意內容
- <strong>輸出清理</strong>：在呈現給用戶或下游系統之前驗證並清理所有模型輸出

### 2. 身份驗證與授權卓越
- <strong>外部身份提供者</strong>：委託身份驗證給知名身份提供者（Microsoft Entra ID、OAuth 2.1 提供者），而非自訂實作
- <strong>客戶端註冊</strong>：優先使用 Client ID 元數據文件或預註冊；僅因兼容性使用已棄用的動態客戶端註冊
- <strong>細粒度權限</strong>：按最小權限原則實現細粒度、具工具特定性的權限
- <strong>令牌生命週期管理</strong>：使用短生命週期訪問令牌，並進行安全輪替及適當的受眾驗證
- <strong>多因素身份驗證</strong>：所有管理訪問與敏感操作均需多因素身份驗證

### 3. 安全通訊協議
- <strong>傳輸層安全</strong>：對遠端 HTTP MCP 通訊使用帶正確憑證驗證的 HTTPS  
；本地 stdio 伺服器則使用進程隔離與環境憑證  

- <strong>端到端加密</strong>：對高度敏感數據的傳輸及靜態狀態增設額外加密層
- <strong>憑證管理</strong>：實施完善的憑證生命週期管理與自動續期流程
- <strong>協議版本強制</strong>：使用 MCP `2026-07-28`，在每次請求中包含必須的版本元數據，並拒絕不支援版本


### 4. 先進速率限制與資源保護
- <strong>多層速率限制</strong>：按用戶、憑證、操作、工具及資源實施速率限制以防止濫用
- <strong>適應性速率限制</strong>：使用基於機器學習的速率限制，適應使用模式與威脅指標
- <strong>資源配額管理</strong>：為計算資源、記憶體使用與執行時間設定適當限制
- **DDoS 防護**：部署全面的 DDoS 防護與流量分析系統


### 5. 全面日誌記錄與監控
- <strong>結構化稽核日誌</strong>：對所有 MCP 操作、工具執行及安全事件實施詳細且可搜尋的日誌記錄
- <strong>即時安全監控</strong>：部署內建 AI 風險異常偵測的 SIEM 系統監控 MCP 工作負載
- <strong>隱私合規日誌</strong>：在尊重資料隱私要求及規範下記錄安全事件
- <strong>事件響應整合</strong>：將日誌系統連接自動化事件響應工作流程

### 6. 強化安全儲存實務
- <strong>硬體安全模組</strong>：關鍵密碼學操作應使用 HSM 支持的密鑰儲存（Azure Key Vault、AWS CloudHSM）
- <strong>加密金鑰管理</strong>：實施適當的金鑰輪替、分離及訪問控制
- <strong>秘密管理</strong>：所有 API 金鑰、令牌及憑證均儲存於專用秘密管理系統
- <strong>資料分級</strong>：基於敏感度對資料分類，並應用適當的保護措施

### 7. 先進令牌管理
- <strong>防止令牌轉發</strong>：明確禁止繞過安全控制的令牌轉發模式
- <strong>受眾驗證</strong>：始終驗證令牌的受眾權限宣告與目標 MCP 伺服器身份相符
- <strong>基於宣告的授權</strong>：根據令牌宣告與用戶屬性實施細粒度授權
- <strong>令牌綁定</strong>：驗證令牌是否針對指定的 MCP 資源，並在伺服器端將應用狀態句柄綁定至已驗證主體


### 8. 安全應用狀態

- <strong>加密狀態句柄</strong>：產生不透明且非決定性的句柄，用於跨請求狀態
- <strong>用戶特定綁定</strong>：在伺服器端將每個句柄綁定至已驗證主體；不信任由客戶端提供的用戶 ID
- <strong>生命週期控制</strong>：過期與撤銷句柄，並定義呼叫者如何從過期狀態恢復
- <strong>每請求授權</strong>：每次提供句柄時重新檢查授權；句柄是一個名稱，而非憑證





### 9. AI 專屬安全控制
- <strong>提示注入防禦</strong>：部署 Microsoft Prompt Shields，使用聚焦、定界符及資料標記技術
- <strong>工具污染預防</strong>：驗證工具元數據，監控動態變化，並驗證工具完整性
- <strong>模型輸出驗證</strong>：掃描模型輸出以防止資料外洩、有害內容或安全政策違規
- <strong>上下文窗口保護</strong>：實施控制防止上下文窗口中毒與操縱攻擊

### 10. 工具執行安全
- <strong>執行沙盒</strong>：在容器化隔離環境中執行工具，並設定資源限制
- <strong>權限分離</strong>：以最低必要權限執行工具，並分隔服務帳戶
- <strong>網路隔離</strong>：對工具執行環境實施網路分割
- <strong>執行監控</strong>：監控工具執行的異常行為、資源使用及安全違規

### 11. 持續安全驗證
- <strong>自動化安全測試</strong>：將安全測試整合至 CI/CD 流水線，使用如 GitHub Advanced Security 工具
- <strong>弱點管理</strong>：定期掃描所有依賴項，包含 AI 模型與外部服務
- <strong>滲透測試</strong>：定期執行針對 MCP 實作的安全評估
- <strong>安全程式碼審查</strong>：對所有 MCP 相關程式碼變更實施強制安全審核

### 12. AI 供應鏈安全
- <strong>元件驗證</strong>：驗證所有 AI 元件（模型、嵌入、API）的來源、完整性及安全性
- <strong>依賴管理</strong>：維護所有軟體及 AI 依賴的最新清單及弱點追蹤
- <strong>可信儲存庫</strong>：使用驗證且可信賴來源的 AI 模型、函式庫及工具
- <strong>供應鏈監控</strong>：持續監控 AI 服務提供商及模型儲存庫的安全狀況

## 高級安全模式

### MCP 零信任架構
- **永不信任，始終驗證**：對所有 MCP 參與者實施持續驗證
- <strong>微分段</strong>：以細粒度網路及身份控管隔離 MCP 組件
- <strong>條件訪問</strong>：實施依風險調整的訪問控制，適應上下文與行為
- <strong>持續風險評估</strong>：基於當前威脅指標動態評估安全狀態

### 隱私保護 AI 實作
- <strong>資料最小化</strong>：僅暴露每個 MCP 操作所需的最少資料
- <strong>差分隱私</strong>：對敏感資料處理實施隱私保護技術
- <strong>同態加密</strong>：運用先進加密技術以在加密資料上安全計算
- <strong>聯邦學習</strong>：實施分散式學習方法以保護資料本地性與隱私

### AI 系統事件響應
- **AI 專屬事件程序**：制定針對 AI 與 MCP 特殊威脅的事件響應程序
- <strong>自動響應</strong>：實施自動化遏制與修復常見 AI 安全事件  
- <strong>取證能力</strong>：維持 AI 系統妥協及資料外洩的取證準備
- <strong>復原程序</strong>：建立模型污染、提示注入攻擊及服務妥協的復原程序

## 實作資源與標準

### 🏔️ 實作安全訓練
- **[MCP 安全高峰工作坊 (Sherpa)](https://azure-samples.github.io/sherpa/)** - 全面性 Azure 上 MCP 伺服器安全實作工作坊
- **[OWASP MCP Azure 安全指南](https://microsoft.github.io/mcp-azure-security-guide/)** - 參考架構與 OWASP MCP 十大風險實踐指導

### 官方 MCP 文件
- [MCP 規範 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 最新 MCP 協議規範
- [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 官方安全指導
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP 授權模式
- [MCP 傳輸](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - 傳輸要求

### 微軟安全解決方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 先進提示注入防護
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面 AI 內容過濾
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企業身份與存取管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全秘密與憑證管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供應鏈與程式碼安全掃描

### 安全標準與框架
- [OAuth 2.1 安全最佳實踐](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 當前 OAuth 安全指導
- [OWASP 十大風險](https://owasp.org/www-project-top-ten/) - 網頁應用安全風險
- [LLM 專屬 OWASP 十大風險](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 專屬安全風險
- [NIST AI 風險管理框架](https://www.nist.gov/itl/ai-risk-management-framework) - 全面 AI 風險管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 資訊安全管理系統

### 實作指南與教學
- [Azure API Management 作為 MCP 授權閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企業認證模式
- [Microsoft Entra ID 與 MCP 伺服器整合](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者整合
- [安全令牌儲存實作](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳實踐
- [AI 端到端加密](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 高級加密模式

### 高級安全資源
- [Microsoft 安全開發生命週期](https://www.microsoft.com/sdl) - 安全開發實務
- [AI 紅隊指導](https://learn.microsoft.com/security/ai-red-team/) - AI 專屬安全測試
- [AI 系統威脅建模](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 威脅建模方法論
- [AI 隱私工程](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 隱私保護 AI 技術

### 合規與治理
- [AI 的 GDPR 合規](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 系統隱私合規
- [AI 治理框架](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 負責任 AI 實作
- [AI 服務的 SOC 2](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 服務提供者安全控制
- [AI 的 HIPAA 合規](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 醫療 AI 合規要求

### DevSecOps 與自動化
- [AI 的 DevSecOps 流水線](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全 AI 開發流程
- [自動安全測試](https://learn.microsoft.com/security/engineering/devsecops) - 持續安全驗證
- [基礎建設即代碼安全](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全基礎設施部署
- [AI 容器安全](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 工作負載容器化安全

### 監控與事件響應  
- [Azure 監控 AI 工作負載](https://learn.microsoft.com/azure/azure-monitor/overview) - 全面監控解決方案
- [AI 安全事件響應](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 專屬事件程序
- [AI 系統的 SIEM](https://learn.microsoft.com/azure/sentinel/overview) - 安全資訊與事件管理

- [人工智能威脅情報](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威脅情報來源

## 🔄 持續改進

### 跟進不斷演變的標準
- **MCP 規範更新**：監察官方 MCP 規範變更及安全公告
- <strong>威脅情報</strong>：訂閱 AI 安全威脅資訊及漏洞資料庫  
- <strong>社群參與</strong>：參與 MCP 安全社群討論及工作小組
- <strong>定期評估</strong>：進行季度安全態勢評估並相應更新做法

### 為 MCP 安全作出貢獻
- <strong>安全研究</strong>：貢獻 MCP 安全研究及漏洞披露計劃
- <strong>最佳做法分享</strong>：與社群分享安全實踐及經驗教訓
- <strong>標準制定</strong>：參與 MCP 規範開發及安全標準制訂
- <strong>工具開發</strong>：為 MCP 生態系統開發及分享安全工具和函式庫

---

*本文件反映截至 2026 年 9 月 9 日的 MCP 安全最佳實踐，
依據 MCP 規範 `2026-07-28`。安全實踐應隨協議和威脅環境演變進行
定期審視。*

## 接下來

- 閱讀：[MCP 安全最佳實踐](./mcp-security-best-practices.md)
- 返回至：[安全模組概述](./README.md)
- 繼續至：[模組 3：入門](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
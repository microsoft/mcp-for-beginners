# MCP 安全最佳實踐 2025

本綜合指南概述了基於最新 **MCP 規範 2025-11-25** 及當前行業標準，實施模型上下文協議（MCP）系統的關鍵安全最佳實踐。這些實踐涵蓋了傳統安全問題以及 MCP 部署中獨有的 AI 特定威脅。

## 關鍵安全需求

### 強制安全控制（必須要求）

1. **令牌驗證**：MCP 伺服器 **不得** 接受任何未明確為該 MCP 伺服器簽發的令牌
2. **授權驗證**：實施授權的 MCP 伺服器 **必須** 驗證所有入站請求，且 **不得** 使用會話進行身份驗證  
3. **用戶同意**：使用靜態客戶端 ID 的 MCP 代理伺服器 **必須** 為每個動態註冊的客戶端獲得明確的用戶同意
4. **安全會話 ID**：MCP 伺服器 **必須** 使用由安全隨機數生成器產生的密碼學安全、非確定性會話 ID

## 核心安全實踐

### 1. 輸入驗證與淨化
- **全面輸入驗證**：驗證並淨化所有輸入，以防止注入攻擊、混淆代理問題及提示注入漏洞
- **參數結構強制**：對所有工具參數和 API 輸入實施嚴格的 JSON 結構驗證
- **內容過濾**：使用 Microsoft Prompt Shields 和 Azure Content Safety 過濾提示和回應中的惡意內容
- **輸出淨化**：在呈現給用戶或下游系統前，驗證並淨化所有模型輸出

### 2. 身份驗證與授權卓越
- **外部身份提供者**：將身份驗證委派給已建立的身份提供者（Microsoft Entra ID、OAuth 2.1 提供者），而非自訂身份驗證
- **細粒度權限**：根據最小權限原則實施細粒度、工具特定的權限
- **令牌生命週期管理**：使用短期存取令牌，並進行安全輪換及適當的受眾驗證
- **多因素身份驗證**：所有管理存取和敏感操作均需 MFA

### 3. 安全通訊協議
- **傳輸層安全**：所有 MCP 通訊均使用 HTTPS/TLS 1.3，並進行適當的憑證驗證
- **端到端加密**：對高度敏感的傳輸和靜態資料實施額外加密層
- **憑證管理**：維護適當的憑證生命週期管理，並自動續期
- **協議版本強制**：使用當前 MCP 協議版本（2025-11-25），並進行適當的版本協商

### 4. 先進速率限制與資源保護
- **多層速率限制**：在用戶、會話、工具及資源層級實施速率限制以防止濫用
- **自適應速率限制**：使用基於機器學習的速率限制，根據使用模式和威脅指標調整
- **資源配額管理**：設定計算資源、記憶體使用和執行時間的適當限制
- **DDoS 防護**：部署全面的 DDoS 防護和流量分析系統

### 5. 全面日誌記錄與監控
- **結構化審計日誌**：為所有 MCP 操作、工具執行及安全事件實施詳細且可搜尋的日誌
- **即時安全監控**：部署具 AI 驅動異常檢測的 SIEM 系統監控 MCP 工作負載
- **隱私合規日誌**：在尊重資料隱私要求和法規的前提下記錄安全事件
- **事件響應整合**：將日誌系統連接至自動化事件響應工作流程

### 6. 強化安全儲存實踐
- **硬體安全模組**：使用 HSM 支援的金鑰儲存（Azure Key Vault、AWS CloudHSM）進行關鍵密碼操作
- **加密金鑰管理**：實施適當的金鑰輪換、隔離及存取控制
- **秘密管理**：將所有 API 金鑰、令牌和憑證存放於專用秘密管理系統
- **資料分類**：根據敏感度分類資料並採取相應保護措施

### 7. 先進令牌管理
- **禁止令牌直通**：明確禁止繞過安全控制的令牌直通模式
- **受眾驗證**：始終驗證令牌受眾聲明與目標 MCP 伺服器身份相符
- **基於聲明的授權**：根據令牌聲明和用戶屬性實施細粒度授權
- **令牌綁定**：在適當情況下將令牌綁定至特定會話、用戶或裝置

### 8. 安全會話管理
- **密碼學會話 ID**：使用密碼學安全的隨機數生成器產生會話 ID（非可預測序列）
- **用戶特定綁定**：使用安全格式如 `<user_id>:<session_id>` 將會話 ID 綁定至用戶特定資訊
- **會話生命週期控制**：實施適當的會話過期、輪換及失效機制
- **會話安全標頭**：使用適當的 HTTP 安全標頭保護會話

### 9. AI 特定安全控制
- **提示注入防禦**：部署 Microsoft Prompt Shields，採用聚光燈、分隔符及數據標記技術
- **工具中毒防範**：驗證工具元資料，監控動態變更，並核實工具完整性
- **模型輸出驗證**：掃描模型輸出以防止資料洩漏、有害內容或安全政策違規
- **上下文視窗保護**：實施控制以防止上下文視窗中毒及操控攻擊

### 10. 工具執行安全
- **執行沙箱**：在容器化、隔離環境中執行工具，並設置資源限制
- **權限分離**：以最低必要權限及分離服務帳戶執行工具
- **網路隔離**：對工具執行環境實施網路分段
- **執行監控**：監控工具執行的異常行為、資源使用及安全違規

### 11. 持續安全驗證
- **自動化安全測試**：將安全測試整合至 CI/CD 管線，使用 GitHub Advanced Security 等工具
- **漏洞管理**：定期掃描所有依賴，包括 AI 模型和外部服務
- **滲透測試**：定期針對 MCP 實作進行安全評估
- **安全程式碼審查**：對所有 MCP 相關程式碼變更實施強制安全審查

### 12. AI 供應鏈安全
- **元件驗證**：驗證所有 AI 元件（模型、嵌入、API）的來源、完整性及安全性
- **依賴管理**：維護所有軟體及 AI 依賴的最新清單並追蹤漏洞
- **可信倉庫**：使用經驗證的可信來源取得所有 AI 模型、函式庫及工具
- **供應鏈監控**：持續監控 AI 服務提供者及模型倉庫的安全狀況

## 先進安全模式

### MCP 零信任架構
- **永不信任，持續驗證**：對所有 MCP 參與者實施持續驗證
- **微分段**：以細粒度網路及身份控管隔離 MCP 組件
- **條件存取**：實施基於風險的存取控制，根據情境與行為調整
- **持續風險評估**：根據當前威脅指標動態評估安全態勢

### 隱私保護 AI 實作
- **資料最小化**：僅暴露每個 MCP 操作所需的最少資料
- **差分隱私**：對敏感資料處理實施隱私保護技術
- **同態加密**：使用先進加密技術對加密資料進行安全計算
- **聯邦學習**：實施分散式學習方法，保護資料本地性與隱私

### AI 系統事件響應
- **AI 特定事件程序**：制定針對 AI 及 MCP 特定威脅的事件響應程序
- **自動化響應**：對常見 AI 安全事件實施自動化遏制與修復  
- **鑑識能力**：維持 AI 系統妥協及資料外洩的鑑識準備
- **復原程序**：建立 AI 模型中毒、提示注入攻擊及服務妥協的復原程序

## 實作資源與標準

### 官方 MCP 文件
- [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - 當前 MCP 協議規範
- [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - 官方安全指導
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - 身份驗證與授權模式
- [MCP 傳輸安全](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - 傳輸層安全要求

### Microsoft 安全解決方案
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 先進提示注入防護
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 全面 AI 內容過濾
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 企業身份與存取管理
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 安全秘密與憑證管理
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 供應鏈與程式碼安全掃描

### 安全標準與框架
- [OAuth 2.1 安全最佳實踐](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 當前 OAuth 安全指導
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 網頁應用安全風險
- [OWASP LLMs Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 特定安全風險
- [NIST AI 風險管理框架](https://www.nist.gov/itl/ai-risk-management-framework) - 全面 AI 風險管理
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 資訊安全管理系統

### 實作指南與教學
- [Azure API Management 作為 MCP 認證閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 企業身份驗證模式
- [Microsoft Entra ID 與 MCP 伺服器](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 身份提供者整合
- [安全令牌儲存實作](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 令牌管理最佳實踐
- [AI 端到端加密](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 先進加密模式

### 先進安全資源
- [Microsoft 安全開發生命週期](https://www.microsoft.com/sdl) - 安全開發實踐
- [AI 紅隊指導](https://learn.microsoft.com/security/ai-red-team/) - AI 特定安全測試
- [AI 系統威脅建模](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 威脅建模方法
- [AI 隱私工程](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 隱私保護 AI 技術

### 合規與治理
- [AI GDPR 合規](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 系統隱私合規
- [AI 治理框架](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 負責任 AI 實作
- [AI 服務 SOC 2](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 服務提供者安全控制
- [AI HIPAA 合規](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 醫療 AI 合規要求

### DevSecOps 與自動化
- [AI DevSecOps 管線](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 安全 AI 開發管線
- [自動化安全測試](https://learn.microsoft.com/security/engineering/devsecops) - 持續安全驗證
- [基礎架構即程式碼安全](https://learn.microsoft.com/security/engineering/infrastructure-security) - 安全基礎架構部署
- [AI 容器安全](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 工作負載容器化安全

### 監控與事件響應  
- [Azure 監控 AI 工作負載](https://learn.microsoft.com/azure/azure-monitor/overview) - 全面監控解決方案
- [AI 安全事件響應](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 特定事件程序
- [AI 系統 SIEM](https://learn.microsoft.com/azure/sentinel/overview) - 安全資訊與事件管理
- [AI 威脅情報](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 威脅情報來源

## 🔄 持續改進

### 緊跟標準演進
- **MCP 規範更新**：監控官方 MCP 規範變更及安全公告
- **威脅情報**：訂閱 AI 安全威脅資訊及漏洞資料庫  
- **社群參與**：參與 MCP 安全社群討論及工作組
- **定期評估**：每季進行安全態勢評估並相應更新實踐

### 為 MCP 安全貢獻
- **安全研究**：參與 MCP 安全研究及漏洞揭露計畫
- **最佳實踐分享**：與社群分享安全實作與經驗教訓
- **標準開發**：參與 MCP 規範開發及安全標準制定
- **工具開發**：開發並分享 MCP 生態系統的安全工具與函式庫

---

*本文件反映截至 2025 年 12 月 18 日的 MCP 安全最佳實踐，基於 MCP 規範 2025-11-25。隨著協議與威脅環境的演變，安全實踐應定期檢視與更新。*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
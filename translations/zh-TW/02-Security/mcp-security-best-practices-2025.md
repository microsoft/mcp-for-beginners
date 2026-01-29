# MCP 安全最佳實踐 - 2025 年 12 月更新

> **重要**：本文件反映最新的 [MCP 規範 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) 安全要求及官方 [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)。請始終參考當前規範以獲取最新指引。

## MCP 實作的基本安全實務

Model Context Protocol 引入了超越傳統軟體安全的獨特安全挑戰。這些實務涵蓋基礎安全需求及 MCP 特有威脅，包括提示注入、工具中毒、會話劫持、混淆代理問題及令牌轉發漏洞。

### **強制性安全要求**

**MCP 規範中的關鍵要求：**

### **強制性安全要求**

**MCP 規範中的關鍵要求：**

> **不得**：MCP 伺服器**不得**接受未明確為該 MCP 伺服器簽發的任何令牌  
>  
> **必須**：實作授權的 MCP 伺服器**必須**驗證所有入站請求  
>  
> **不得**：MCP 伺服器**不得**使用會話進行身份驗證  
>  
> **必須**：使用靜態客戶端 ID 的 MCP 代理伺服器**必須**為每個動態註冊的客戶端取得使用者同意

---

## 1. **令牌安全與身份驗證**

**身份驗證與授權控管：**  
   - **嚴格授權審查**：全面審核 MCP 伺服器授權邏輯，確保僅授權預期使用者與客戶端存取資源  
   - **外部身份提供者整合**：使用 Microsoft Entra ID 等既有身份提供者，避免自訂身份驗證實作  
   - **令牌受眾驗證**：始終驗證令牌是否明確簽發給您的 MCP 伺服器，絕不接受上游令牌  
   - **適當令牌生命週期管理**：實作安全的令牌輪替、過期政策，防止令牌重放攻擊  

**受保護的令牌儲存：**  
   - 使用 Azure Key Vault 或類似安全憑證庫儲存所有機密  
   - 實施令牌靜態與傳輸加密  
   - 定期輪替憑證並監控未授權存取  

## 2. **會話管理與傳輸安全**

**安全會話實務：**  
   - **密碼學安全的會話 ID**：使用安全隨機數產生器生成非決定性會話 ID  
   - **使用者綁定**：使用 `<user_id>:<session_id>` 格式將會話 ID 綁定至使用者身份，防止跨使用者會話濫用  
   - **會話生命週期管理**：實作適當的過期、輪替與失效機制，限制漏洞窗口  
   - **HTTPS/TLS 強制**：所有通訊必須使用 HTTPS，防止會話 ID 被攔截  

**傳輸層安全：**  
   - 儘可能配置 TLS 1.3 並妥善管理憑證  
   - 對關鍵連線實施憑證釘選  
   - 定期輪替憑證並驗證有效性  

## 3. **AI 特定威脅防護** 🤖

**提示注入防禦：**  
   - **Microsoft 提示防護盾**：部署 AI 提示防護盾以進行惡意指令的高級偵測與過濾  
   - **輸入消毒**：驗證並消毒所有輸入，防止注入攻擊及混淆代理問題  
   - **內容邊界**：使用分隔符與資料標記系統區分可信指令與外部內容  

**工具中毒防範：**  
   - **工具元資料驗證**：實作工具定義完整性檢查並監控異常變更  
   - **動態工具監控**：監控執行時行為並設置異常執行模式警示  
   - **審核流程**：工具修改與能力變更需明確使用者批准  

## 4. **存取控制與權限**

**最小權限原則：**  
   - 僅授予 MCP 伺服器執行預期功能所需的最低權限  
   - 實作基於角色的存取控制 (RBAC) 並細分權限  
   - 定期審查權限並持續監控權限升級  

**執行時權限控管：**  
   - 設定資源限制以防止資源耗盡攻擊  
   - 使用容器隔離工具執行環境  
   - 實作即時存取以管理管理功能  

## 5. **內容安全與監控**

**內容安全實作：**  
   - **Azure 內容安全整合**：使用 Azure 內容安全偵測有害內容、越獄嘗試及政策違規  
   - **行為分析**：實作執行時行為監控以偵測 MCP 伺服器與工具執行異常  
   - **全面日誌記錄**：記錄所有身份驗證嘗試、工具調用及安全事件，並使用安全防篡改儲存  

**持續監控：**  
   - 即時警示可疑模式與未授權存取嘗試  
   - 與 SIEM 系統整合以集中管理安全事件  
   - 定期進行 MCP 實作的安全稽核與滲透測試  

## 6. **供應鏈安全**

**元件驗證：**  
   - **依賴掃描**：對所有軟體依賴與 AI 元件使用自動化漏洞掃描  
   - **來源驗證**：驗證模型、資料來源及外部服務的來源、授權與完整性  
   - **簽名套件**：使用加密簽名套件並於部署前驗證簽章  

**安全開發流程：**  
   - **GitHub 進階安全**：實作機密掃描、依賴分析及 CodeQL 靜態分析  
   - **CI/CD 安全**：在自動部署流程中整合安全驗證  
   - **工件完整性**：對部署工件與設定實作加密驗證  

## 7. **OAuth 安全與混淆代理防範**

**OAuth 2.1 實作：**  
   - **PKCE 實作**：所有授權請求使用授權碼交換驗證碼 (PKCE)  
   - **明確同意**：為每個動態註冊客戶端取得使用者同意，防止混淆代理攻擊  
   - **重定向 URI 驗證**：嚴格驗證重定向 URI 與客戶端識別碼  

**代理安全：**  
   - 防止透過靜態客戶端 ID 利用繞過授權  
   - 實作第三方 API 存取的適當同意流程  
   - 監控授權碼竊取與未授權 API 存取  

## 8. **事件回應與復原**

**快速回應能力：**  
   - **自動化回應**：實作自動化憑證輪替與威脅遏止系統  
   - **回滾程序**：能快速回復至已知良好配置與元件  
   - **鑑識能力**：詳細稽核軌跡與日誌以利事件調查  

**溝通與協調：**  
   - 明確的安全事件升級程序  
   - 與組織事件回應團隊整合  
   - 定期進行安全事件模擬與桌面演練  

## 9. **合規與治理**

**法規遵循：**  
   - 確保 MCP 實作符合產業特定要求（GDPR、HIPAA、SOC 2）  
   - 實作 AI 資料處理的資料分類與隱私控管  
   - 維護完整文件以供合規稽核  

**變更管理：**  
   - 所有 MCP 系統修改均需正式安全審查流程  
   - 配置變更需版本控制與審批流程  
   - 定期合規評估與差距分析  

## 10. **進階安全控管**

**零信任架構：**  
   - **永不信任，持續驗證**：持續驗證使用者、裝置與連線  
   - **微分段**：細緻網路控管隔離各 MCP 元件  
   - **條件存取**：基於風險的存取控管，依當前情境與行為調整  

**執行時應用防護：**  
   - **執行時應用自我防護 (RASP)**：部署 RASP 技術以即時威脅偵測  
   - **應用效能監控**：監控效能異常以偵測攻擊跡象  
   - **動態安全政策**：根據當前威脅態勢調整安全政策  

## 11. **Microsoft 安全生態系統整合**

**全面 Microsoft 安全：**  
   - **Microsoft Defender for Cloud**：MCP 工作負載的雲端安全態勢管理  
   - **Azure Sentinel**：雲端原生 SIEM 與 SOAR 功能，提供高級威脅偵測  
   - **Microsoft Purview**：AI 工作流程與資料來源的資料治理與合規  

**身份與存取管理：**  
   - **Microsoft Entra ID**：企業身份管理與條件存取政策  
   - **特權身份管理 (PIM)**：即時存取與管理功能審批流程  
   - **身份保護**：基於風險的條件存取與自動威脅回應  

## 12. **持續安全演進**

**保持最新：**  
   - **規範監控**：定期檢視 MCP 規範更新與安全指引變更  
   - **威脅情報**：整合 AI 特定威脅情報與妥協指標  
   - **安全社群參與**：積極參與 MCP 安全社群與漏洞揭露計畫  

**適應性安全：**  
   - **機器學習安全**：使用 ML 基異常偵測識別新型攻擊模式  
   - **預測性安全分析**：實作預測模型以主動識別威脅  
   - **安全自動化**：根據威脅情報與規範變更自動更新安全政策  

---

## **關鍵安全資源**

### **官方 MCP 文件**
- [MCP 規範 (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP 安全最佳實踐](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft 安全解決方案**
- [Microsoft 提示防護盾](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure 內容安全](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID 安全](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub 進階安全](https://github.com/security/advanced-security)

### **安全標準**
- [OAuth 2.0 安全最佳實踐 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP 大型語言模型十大風險](https://genai.owasp.org/)
- [NIST AI 風險管理框架](https://www.nist.gov/itl/ai-risk-management-framework)

### **實作指南**
- [Azure API 管理 MCP 身份驗證閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID 與 MCP 伺服器](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **安全通知**：MCP 安全實務快速演進。實作前請務必依據最新 [MCP 規範](https://spec.modelcontextprotocol.io/) 及 [官方安全文件](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) 進行驗證。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP 安全性：為 AI 系統提供全面保護

[![MCP Security Best Practices](../../../translated_images/zh-MO/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(點擊上方圖片觀看本課程影片)_

安全性是 AI 系統設計的基礎，因此我們將其列為第二章節的重點。這與微軟來自 [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/) 的 **Secure by Design** 原則相符。

Model Context Protocol (MCP) 為 AI 驅動的應用程式帶來強大新功能，同時引入超越傳統軟體風險的獨特安全挑戰。MCP 系統面臨既有的安全問題（安全編碼、最小權限、供應鏈安全）以及新的 AI 專屬威脅，包括提示注入、工具中毒、會話劫持、混淆代理攻擊、令牌直通漏洞和動態能力修改。

本課程探討 MCP 實作中最關鍵的安全風險——涵蓋身份驗證、授權、過度權限、間接提示注入、會話安全、混淆代理問題、令牌管理和供應鏈漏洞。您將學習可行的控管措施和最佳實務，以減輕這些風險，同時利用微軟解決方案如 Prompt Shields、Azure Content Safety 和 GitHub Advanced Security 強化您的 MCP 部署。

## 學習目標

完成本課程後，您將能夠：

- **識別 MCP 專屬威脅**：辨識 MCP 系統中獨特的安全風險，包括提示注入、工具中毒、過度權限、會話劫持、混淆代理問題、令牌直通漏洞和供應鏈風險
- **應用安全控管**：實施有效的緩解措施，包括強健的身份驗證、最小權限存取、安全令牌管理、會話安全控管和供應鏈驗證
- **利用微軟安全解決方案**：了解並部署微軟 Prompt Shields、Azure Content Safety 和 GitHub Advanced Security 以保護 MCP 工作負載
- **驗證工具安全性**：認識工具元資料驗證的重要性，監控動態變更，防禦間接提示注入攻擊
- **整合最佳實務**：結合既有安全基礎（安全編碼、伺服器強化、零信任）與 MCP 專屬控管，實現全面保護

# MCP 安全架構與控管

現代 MCP 實作需要分層安全方法，既涵蓋傳統軟體安全，也應對 AI 專屬威脅。快速演進的 MCP 規範持續成熟其安全控管，促進與企業安全架構及既有最佳實務的更佳整合。

來自 [Microsoft Digital Defense Report](https://aka.ms/mddr) 的研究顯示，**98% 的通報違規事件可透過強健的安全衛生措施防範**。最有效的保護策略結合基礎安全實務與 MCP 專屬控管——經證實的基線安全措施仍是降低整體安全風險的關鍵。

## 當前安全現況

> **注意：** 本資訊反映 MCP 安全標準截至 **2025 年 12 月 18 日**。MCP 協定持續快速演進，未來實作可能引入新的身份驗證模式與強化控管。請務必參考最新的 [MCP 規範](https://spec.modelcontextprotocol.io/)、[MCP GitHub 倉庫](https://github.com/modelcontextprotocol) 及 [安全最佳實務文件](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) 以取得最新指引。

### MCP 身份驗證演進

MCP 規範在身份驗證與授權方法上已有重大演進：

- **原始方法**：早期規範要求開發者實作自訂身份驗證伺服器，MCP 伺服器作為 OAuth 2.0 授權伺服器直接管理使用者身份驗證
- **現行標準（2025-11-25）**：更新規範允許 MCP 伺服器委派身份驗證給外部身份提供者（如 Microsoft Entra ID），提升安全態勢並降低實作複雜度
- **傳輸層安全**：加強對本地（STDIO）與遠端（Streamable HTTP）連線的安全傳輸機制與適當身份驗證模式支援

## 身份驗證與授權安全

### 當前安全挑戰

現代 MCP 實作面臨多項身份驗證與授權挑戰：

### 風險與威脅向量

- **授權邏輯錯誤配置**：MCP 伺服器授權實作缺陷可能暴露敏感資料並錯誤套用存取控管
- **OAuth 令牌外洩**：本地 MCP 伺服器令牌被竊取，攻擊者可冒充伺服器存取下游服務
- **令牌直通漏洞**：不當令牌處理造成安全控管繞過與責任追蹤缺失
- **過度權限**：MCP 伺服器權限過大違反最小權限原則，擴大攻擊面

#### 令牌直通：嚴重的反模式

**令牌直通在現行 MCP 授權規範中明確禁止**，因其帶來嚴重安全影響：

##### 安全控管繞過
- MCP 伺服器與下游 API 實施關鍵安全控管（速率限制、請求驗證、流量監控）依賴正確令牌驗證
- 客戶端直接使用 API 令牌繞過這些必要防護，破壞安全架構

##### 責任追蹤與稽核困難  
- MCP 伺服器無法區分使用上游發行令牌的客戶端，破壞稽核軌跡
- 下游資源伺服器日誌顯示誤導性請求來源，非實際 MCP 伺服器中介者
- 事件調查與合規稽核變得極為困難

##### 資料外洩風險
- 未驗證的令牌聲明允許持有被竊令牌的惡意者利用 MCP 伺服器作為資料外洩代理
- 信任邊界違反導致未授權存取模式繞過預期安全控管

##### 多服務攻擊向量
- 被接受的被竊令牌可用於多個服務，促成跨系統橫向移動
- 服務間信任假設在無法驗證令牌來源時可能遭破壞

### 安全控管與緩解措施

**關鍵安全要求：**

> **強制規定**：MCP 伺服器**不得接受非明確為該 MCP 伺服器發行的任何令牌**

#### 身份驗證與授權控管

- **嚴格授權審查**：全面稽核 MCP 伺服器授權邏輯，確保僅預期使用者與客戶端能存取敏感資源
  - **實作指南**：[Azure API Management 作為 MCP 伺服器身份驗證閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **身份整合**：[使用 Microsoft Entra ID 進行 MCP 伺服器身份驗證](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **安全令牌管理**：實施 [微軟令牌驗證與生命週期最佳實務](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - 驗證令牌受眾聲明與 MCP 伺服器身份相符
  - 實施適當的令牌輪替與過期政策
  - 防止令牌重放攻擊與未授權使用

- **受保護的令牌儲存**：令牌靜態與傳輸加密儲存
  - **最佳實務**：[安全令牌儲存與加密指南](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### 存取控管實作

- **最小權限原則**：僅授予 MCP 伺服器執行預期功能所需的最低權限
  - 定期檢視與更新權限，防止權限膨脹
  - **微軟文件**：[安全的最小權限存取](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **基於角色的存取控管 (RBAC)**：實施細緻角色分配
  - 嚴格限定角色範圍至特定資源與操作
  - 避免廣泛或不必要權限擴大攻擊面

- **持續權限監控**：實施持續存取稽核與監控
  - 監控權限使用模式異常
  - 及時修正過度或未使用權限

## AI 專屬安全威脅

### 提示注入與工具操控攻擊

現代 MCP 實作面臨複雜的 AI 專屬攻擊向量，傳統安全措施無法完全防範：

#### **間接提示注入（跨域提示注入）**

**間接提示注入** 是 MCP 啟用 AI 系統中最關鍵的漏洞之一。攻擊者將惡意指令嵌入外部內容——文件、網頁、電子郵件或資料來源，AI 系統隨後將其視為合法指令處理。

**攻擊場景：**
- **文件型注入**：惡意指令藏於處理文件中，觸發非預期 AI 行為
- **網頁內容利用**：被入侵網頁含嵌入提示，爬取時操控 AI 行為
- **電子郵件攻擊**：郵件中惡意提示導致 AI 助理洩漏資訊或執行未授權操作
- **資料來源污染**：被入侵的資料庫或 API 向 AI 系統提供受污染內容

**實際影響**：此類攻擊可能導致資料外洩、隱私違規、有害內容生成及使用者互動操控。詳見 [MCP 中的提示注入（Simon Willison）](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)。

![Prompt Injection Attack Diagram](../../../translated_images/zh-MO/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **工具中毒攻擊**

**工具中毒** 針對定義 MCP 工具的元資料，利用大型語言模型（LLM）解讀工具描述與參數以決定執行行為的方式進行攻擊。

**攻擊機制：**
- **元資料操控**：攻擊者將惡意指令注入工具描述、參數定義或使用範例
- **隱形指令**：工具元資料中隱藏的提示，AI 模型處理但人類用戶看不見
- **動態工具修改（「拉地毯」）**：用戶批准的工具後續被修改為執行惡意行為，使用者不知情
- **參數注入**：惡意內容嵌入工具參數結構，影響模型行為

**託管伺服器風險**：遠端 MCP 伺服器風險較高，因工具定義可在用戶初次批准後更新，導致先前安全工具變成惡意。詳見 [工具中毒攻擊（Invariant Labs）](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)。

![Tool Injection Attack Diagram](../../../translated_images/zh-MO/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **其他 AI 攻擊向量**

- **跨域提示注入 (XPIA)**：利用多域內容繞過安全控管的複雜攻擊
- **動態能力修改**：即時變更工具能力，逃避初期安全評估
- **上下文視窗中毒**：操控大型上下文視窗以隱藏惡意指令
- **模型混淆攻擊**：利用模型限制製造不可預測或不安全行為

### AI 安全風險影響

**高影響後果：**
- **資料外洩**：未授權存取與竊取企業或個人敏感資料
- **隱私違規**：個人識別資訊（PII）及機密商業資料曝光  
- **系統操控**：關鍵系統與工作流程遭非預期修改
- **憑證竊取**：身份驗證令牌與服務憑證遭入侵
- **橫向移動**：利用受損 AI 系統作為更廣泛網路攻擊的跳板

### 微軟 AI 安全解決方案

#### **AI Prompt Shields：針對注入攻擊的先進防護**

微軟 **AI Prompt Shields** 透過多層安全防護，全面防禦直接與間接提示注入攻擊：

##### **核心防護機制：**

1. **先進偵測與過濾**
   - 機器學習演算法與自然語言處理技術偵測外部內容中的惡意指令
   - 即時分析文件、網頁、電子郵件與資料來源的嵌入威脅
   - 理解合法與惡意提示模式的語境差異

2. **聚焦技術**  
   - 區分受信任系統指令與可能受損的外部輸入
   - 文字轉換方法提升模型相關性，同時隔離惡意內容
   - 協助 AI 系統維持正確指令層級，忽略注入命令

3. **分隔符與資料標記系統**
   - 明確定義受信任系統訊息與外部輸入文字的邊界
   - 特殊標記突顯受信任與不受信任資料來源間的界線
   - 清晰分隔防止指令混淆與未授權命令執行

4. **持續威脅情報**
   - 微軟持續監控新興攻擊模式並更新防禦措施
   - 主動威脅狩獵新注入技術與攻擊向量
   - 定期安全模型更新以維持對抗演進威脅的效能

5. **Azure Content Safety 整合**
   - 作為 Azure AI Content Safety 套件的一部分
   - 額外偵測越獄嘗試、有害內容與安全政策違規
   - AI 應用元件間統一安全控管

**實作資源**：[Microsoft Prompt Shields 文件](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/zh-MO/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## 進階 MCP 安全威脅

### 會話劫持漏洞

**會話劫持** 是有狀態 MCP 實作中的關鍵攻擊向量，未授權方取得並濫用合法會話識別碼，冒充客戶端執行未授權操作。

#### **攻擊場景與風險**

- **會話劫持提示注入**：攻擊者持有被竊會話 ID，向共享會話狀態的伺服器注入惡意事件，可能觸發有害行為或存取敏感資料
- **直接冒充**：被竊會話 ID 允許直接呼叫 MCP 伺服器，繞過身份驗證，將攻擊者視為合法使用者
- **可恢復串流遭破壞**：攻擊者可提前終止請求，導致合法客戶端恢復時接收潛在惡意內容

#### **會話管理安全控管**

**關鍵要求：**
- **授權驗證**：實作授權的 MCP 伺服器**必須**驗證所有入站請求，且**不得**依賴會話進行身份驗證  
- **安全會話產生**：使用密碼學安全、非決定性且由安全隨機數產生器生成的會話 ID  
- **用戶專屬綁定**：使用 `<user_id>:<session_id>` 等格式將會話 ID 綁定至用戶專屬資訊，以防止跨用戶會話濫用  
- **會話生命週期管理**：實施適當的過期、輪替與失效機制，以限制漏洞窗口  
- **傳輸安全**：所有通訊必須使用 HTTPS 以防止會話 ID 被攔截  

### 混淆代理問題

**混淆代理問題**發生於 MCP 伺服器作為客戶端與第三方服務間的身份驗證代理時，靜態客戶端 ID 的濫用可能導致授權繞過。

#### **攻擊機制與風險**

- **基於 Cookie 的同意繞過**：先前用戶身份驗證產生的同意 Cookie，攻擊者透過惡意授權請求與精心設計的重定向 URI 利用此 Cookie  
- **授權碼竊取**：現有同意 Cookie 可能導致授權伺服器跳過同意畫面，將授權碼重定向至攻擊者控制的端點  
- **未授權 API 存取**：竊取的授權碼可用於交換令牌並冒充用戶，無需明確批准  

#### **緩解策略**

**強制控制：**  
- **明確同意要求**：使用靜態客戶端 ID 的 MCP 代理伺服器**必須**為每個動態註冊的客戶端取得用戶同意  
- **OAuth 2.1 安全實作**：遵循當前 OAuth 安全最佳實踐，包括所有授權請求使用 PKCE（授權碼交換驗證碼）  
- **嚴格客戶端驗證**：實施嚴格的重定向 URI 與客戶端識別碼驗證以防止濫用  

### 令牌直通漏洞

**令牌直通**是一種明顯的反模式，指 MCP 伺服器在未經適當驗證的情況下接受客戶端令牌並轉發至下游 API，違反 MCP 授權規範。

#### **安全影響**

- **控制繞過**：客戶端直接使用令牌存取 API，繞過重要的速率限制、驗證與監控控制  
- **審計軌跡破壞**：上游發行的令牌使客戶端身份無法識別，破壞事件調查能力  
- **代理式資料外洩**：未驗證令牌使惡意行為者可利用伺服器作為未授權資料存取的代理  
- **信任邊界違反**：當無法驗證令牌來源時，下游服務的信任假設可能被破壞  
- **多服務攻擊擴散**：被接受於多個服務的受損令牌可用於橫向移動  

#### **必要安全控制**

**不可妥協要求：**  
- **令牌驗證**：MCP 伺服器**不得**接受非明確為 MCP 伺服器發行的令牌  
- **受眾驗證**：始終驗證令牌的受眾聲明與 MCP 伺服器身份相符  
- **適當令牌生命週期**：實施短期存取令牌並採用安全輪替機制  

## AI 系統供應鏈安全

供應鏈安全已超越傳統軟體依賴，涵蓋整個 AI 生態系統。現代 MCP 實作必須嚴格驗證與監控所有 AI 相關元件，因每個元件皆可能引入危害系統完整性的漏洞。

### 擴展的 AI 供應鏈元件

**傳統軟體依賴：**  
- 開源函式庫與框架  
- 容器映像與基礎系統  
- 開發工具與建置流程  
- 基礎設施元件與服務  

**AI 專屬供應鏈元素：**  
- **基礎模型**：來自多家供應商的預訓練模型，需驗證來源  
- **嵌入服務**：外部向量化與語義搜尋服務  
- **上下文提供者**：資料來源、知識庫與文件庫  
- **第三方 API**：外部 AI 服務、機器學習流程與資料處理端點  
- **模型工件**：權重、配置與微調模型變體  
- **訓練資料來源**：用於模型訓練與微調的資料集  

### 全面供應鏈安全策略

#### **元件驗證與信任**  
- **來源驗證**：整合前驗證所有 AI 元件的來源、授權與完整性  
- **安全評估**：對模型、資料來源與 AI 服務進行漏洞掃描與安全審查  
- **聲譽分析**：評估 AI 服務供應商的安全紀錄與實務  
- **合規驗證**：確保所有元件符合組織安全與法規要求  

#### **安全部署流程**  
- **自動化 CI/CD 安全**：在自動化部署流程中整合安全掃描  
- **工件完整性**：對所有部署工件（程式碼、模型、配置）實施密碼學驗證  
- **分階段部署**：採用漸進式部署策略，於每階段進行安全驗證  
- **可信工件倉庫**：僅從驗證且安全的工件註冊庫與倉庫部署  

#### **持續監控與回應**  
- **依賴掃描**：持續監控所有軟體與 AI 元件依賴的漏洞  
- **模型監控**：持續評估模型行為、性能漂移與安全異常  
- **服務健康追蹤**：監控外部 AI 服務的可用性、安全事件與政策變更  
- **威脅情報整合**：納入專屬 AI 與機器學習安全風險的威脅情報  

#### **存取控制與最小權限**  
- **元件層級權限**：根據業務需求限制對模型、資料與服務的存取  
- **服務帳號管理**：實施具最小必要權限的專用服務帳號  
- **網路分段**：隔離 AI 元件並限制服務間的網路存取  
- **API 閘道控管**：使用集中式 API 閘道控管與監控對外部 AI 服務的存取  

#### **事件回應與復原**  
- **快速回應程序**：建立修補或替換受損 AI 元件的流程  
- **憑證輪替**：自動化系統輪替密鑰、API 金鑰與服務憑證  
- **回滾能力**：能快速回復至先前已知良好版本的 AI 元件  
- **供應鏈違規復原**：針對上游 AI 服務受損的特定回應程序  

### Microsoft 安全工具與整合

**GitHub Advanced Security** 提供全面供應鏈保護，包括：  
- **秘密掃描**：自動偵測儲存庫中的憑證、API 金鑰與令牌  
- **依賴掃描**：開源依賴與函式庫的漏洞評估  
- **CodeQL 分析**：靜態程式碼分析以發現安全漏洞與程式碼問題  
- **供應鏈洞察**：依賴健康與安全狀態的可視化  

**Azure DevOps 與 Azure Repos 整合：**  
- 在 Microsoft 開發平台中無縫整合安全掃描  
- Azure Pipelines 中自動化 AI 工作負載的安全檢查  
- AI 元件安全部署的政策執行  

**Microsoft 內部實務：**  
Microsoft 在所有產品中實施廣泛的供應鏈安全實務。詳見 [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)。  

## 基礎安全最佳實務

MCP 實作繼承並建立於組織現有的安全態勢。強化基礎安全實務能顯著提升 AI 系統與 MCP 部署的整體安全性。

### 核心安全基礎

#### **安全開發實務**  
- **OWASP 合規**：防護 [OWASP Top 10](https://owasp.org/www-project-top-ten/) 網頁應用漏洞  
- **AI 專屬防護**：實施 [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) 控制措施  
- **安全秘密管理**：使用專用保管庫管理令牌、API 金鑰與敏感配置資料  
- **端對端加密**：在所有應用元件與資料流中實施安全通訊  
- **輸入驗證**：嚴格驗證所有用戶輸入、API 參數與資料來源  

#### **基礎設施強化**  
- **多因素驗證**：所有管理與服務帳號強制 MFA  
- **補丁管理**：自動且及時地為作業系統、框架與依賴套件打補丁  
- **身份提供者整合**：透過企業身份提供者（Microsoft Entra ID、Active Directory）集中管理身份  
- **網路分段**：邏輯隔離 MCP 元件以限制橫向移動風險  
- **最小權限原則**：所有系統元件與帳號僅授予必要最低權限  

#### **安全監控與偵測**  
- **全面日誌記錄**：詳細記錄 AI 應用活動，包括 MCP 用戶端與伺服器互動  
- **SIEM 整合**：集中式安全資訊與事件管理以偵測異常  
- **行為分析**：利用 AI 監控系統與用戶行為的異常模式  
- **威脅情報**：整合外部威脅情報與妥協指標（IOC）  
- **事件回應**：明確定義安全事件偵測、回應與復原程序  

#### **零信任架構**  
- **永不信任，持續驗證**：持續驗證用戶、裝置與網路連線  
- **微分段**：細緻的網路控管，隔離個別工作負載與服務  
- **身份中心安全**：基於驗證身份而非網路位置的安全政策  
- **持續風險評估**：根據當前情境與行為動態評估安全態勢  
- **條件存取**：根據風險因素、位置與裝置信任度調整存取控制  

### 企業整合模式

#### **Microsoft 安全生態系統整合**  
- **Microsoft Defender for Cloud**：全面的雲端安全態勢管理  
- **Azure Sentinel**：雲端原生 SIEM 與 SOAR 功能，保護 AI 工作負載  
- **Microsoft Entra ID**：企業身份與存取管理，具條件存取政策  
- **Azure Key Vault**：集中式秘密管理，具硬體安全模組（HSM）支援  
- **Microsoft Purview**：AI 資料來源與工作流程的資料治理與合規  

#### **合規與治理**  
- **法規對齊**：確保 MCP 實作符合產業特定合規要求（GDPR、HIPAA、SOC 2）  
- **資料分類**：妥善分類與處理 AI 系統處理的敏感資料  
- **審計軌跡**：全面日誌記錄以符合法規與鑑識調查需求  
- **隱私控管**：在 AI 系統架構中實施隱私設計原則  
- **變更管理**：對 AI 系統修改進行正式安全審查流程  

這些基礎實務建立堅實的安全基線，提升 MCP 專屬安全控制的效能，並為 AI 驅動應用提供全面保護。  

## 主要安全重點

- **分層安全策略**：結合基礎安全實務（安全程式碼、最小權限、供應鏈驗證、持續監控）與 AI 專屬控制，實現全面防護  
- **AI 專屬威脅環境**：MCP 系統面臨獨特風險，包括提示注入、工具中毒、會話劫持、混淆代理問題、令牌直通漏洞與過度權限，需專門緩解措施  
- **身份驗證與授權卓越**：使用外部身份提供者（Microsoft Entra ID）實施強健身份驗證，強制令牌驗證，絕不接受非明確為 MCP 伺服器發行的令牌  
- **AI 攻擊防護**：部署 Microsoft Prompt Shields 與 Azure Content Safety 防禦間接提示注入與工具中毒攻擊，同時驗證工具元資料並監控動態變化  
- **會話與傳輸安全**：使用密碼學安全、非決定性且綁定用戶身份的會話 ID，實施適當會話生命週期管理，且絕不使用會話作為身份驗證  
- **OAuth 安全最佳實務**：透過動態註冊客戶端的明確用戶同意、正確實作 OAuth 2.1 與 PKCE，以及嚴格重定向 URI 驗證，防止混淆代理攻擊  
- **令牌安全原則**：避免令牌直通反模式，驗證令牌受眾聲明，實施短期令牌與安全輪替，維護清晰信任邊界  
- **全面供應鏈安全**：對所有 AI 生態系統元件（模型、嵌入、上下文提供者、外部 API）採用與傳統軟體依賴相同的安全嚴謹度  
- **持續演進**：緊跟快速演進的 MCP 規範，參與安全社群標準制定，隨協議成熟維持適應性安全態勢  
- **Microsoft 安全整合**：利用 Microsoft 全面安全生態系統（Prompt Shields、Azure Content Safety、GitHub Advanced Security、Entra ID）強化 MCP 部署防護  

## 全面資源

### **官方 MCP 安全文件**  
- [MCP 規範（目前版本：2025-11-25）](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP 安全最佳實務](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP 授權規範](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [MCP GitHub 儲存庫](https://github.com/modelcontextprotocol)  

### **安全標準與最佳實務**  
- [OAuth 2.0 安全最佳實務 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 網頁應用安全](https://owasp.org/www-project-top-ten/)  
- [OWASP 大型語言模型 Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft 數位防禦報告](https://aka.ms/mddr)  

### **AI 安全研究與分析**  
- [MCP 中的提示注入 (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [工具中毒攻擊 (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP 安全研究簡報 (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft 安全解決方案**
- [Microsoft Prompt Shields 文件](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure 內容安全服務](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID 安全](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure 令牌管理最佳實踐](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub 進階安全](https://github.com/security/advanced-security)

### **實作指南與教學**
- [Azure API 管理作為 MCP 認證閘道](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID 與 MCP 伺服器認證](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [安全令牌儲存與加密 (影片)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps 與供應鏈安全**
- [Azure DevOps 安全](https://azure.microsoft.com/products/devops)
- [Azure Repos 安全](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft 供應鏈安全之旅](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **其他安全文件**

欲獲得完整安全指引，請參考本節中的專門文件：

- **[MCP 安全最佳實踐 2025](./mcp-security-best-practices-2025.md)** - MCP 實作的完整安全最佳實踐
- **[Azure 內容安全實作](./azure-content-safety-implementation.md)** - Azure 內容安全整合的實務範例  
- **[MCP 安全控管 2025](./mcp-security-controls-2025.md)** - MCP 部署的最新安全控管與技術
- **[MCP 最佳實踐快速參考](./mcp-best-practices.md)** - MCP 重要安全實務的快速參考指南

---

## 下一步

下一步: [第 3 章：入門](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起之任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
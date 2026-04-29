# MCP ការត្រួតពិនិត្យសុវត្ថិភាព - ការអាប់ដេតខែកុម្ភៈ ២០២៦

> **ស្តង់ដារបច្ចុប្បន្ន**៖ ឯកសារនេះសម្របសម្រួលតាម [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) នៃតម្រូវការសុវត្ថិភាព និង [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) ផ្លូវការដែលបានផ្សព្វផ្សាយ។

Model Context Protocol (MCP) បានវាស់វែងចម្រើនយ៉ាងច្រើនជាមួយនឹងការត្រួតពិនិត្យសុវត្ថិភាពរឹងមាំដែលគ្របដណ្ដប់ការពារ និងកាត់បន្ថយហានិភ័យទាំងនៃកម្មវិធីបុរាណ និងគ្រោះថ្នាក់ជាក់លាក់ AI។ ឯកសារនេះផ្តល់ជូននូវការត្រួតពិនិត្យសុវត្ថិភាពទូលំទូលាយសម្រាប់ការអនុវត្ត MCP ដែលមានសុវត្ថិភាព ធ្វើតាមស៊ុម​ទ្រូង​របស់ OWASP MCP Top 10។

## 🏔️ ការបណ្តុះបណ្តាលសុវត្ថិភាពដៃគូ

សម្រាប់បទពិសោធន៍អនុវត្តប្រាក់វាជាក់ស្តែង អនុញ្ញាតឲ្យយើងណែនាំនូវ **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** — ការប្រកួតជាអ្នកដឹកនាំយាយសណ្ឋានទូទេញក្នុងការការពារទីតាំងរបស់ MCP នៅលើ Azure ដោយប្រើវិធីសាស្រ្ត "ច្រោះ→ ផ្ទុក→ កែតម្រូវ→ ផ្ទៀងផ្ទាត់"។

ការត្រួតពិនិត្យសុវត្ថិភាពទាំងអស់នៅក្នុងឯកសារនេះស្របតាម **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** ដែលផ្តល់នូវរចនាសម្ព័ន្ធយោង និងមគ្គុទេសក៍អនុវត្ត Azure ជាក់លាក់ដើម្បីប្រយុទ្ធបំពេញហានិភ័យ OWASP MCP Top 10។

## **តម្រូវការសុវត្ថិភាព បាទបញ្ជាក់**

### **ការហាមឃាត់សំខាន់ៗពី MCP Specification៖**

> **ហាមឃាត់**៖ ម៉ាស៊ីនបម្រើ MCP **មិនត្រូវ** ទទួលយក token ទាំងអស់ដែលមិនត្រូវបានចេញផ្សាយយ៉ាងច្បាស់សម្រាប់ម៉ាស៊ីនបម្រើ MCP  
>
> **ហាមឃាត់**៖ ម៉ាស៊ីនបម្រើ MCP **មិនត្រូវ** ប្រើសម័យសម្រង់សម្រាប់ការផ្ទៀងផ្ទាត់  
>
> **ត្រូវការ**៖ ម៉ាស៊ីនបម្រើ MCP ដែលអនុវត្តការអនុញ្ញាត **ត្រូវតែ** បញ្ជាក់រាល់សំណើដែលចូលមកទាំងអស់  
>
> **បាទបញ្ជាក់**៖ ម៉ាស៊ីនបម្រើ MCP proxy ដែលប្រើ Client IDs ស្ថិតស្ថេរត្រូវតែទទួលយកការយល់ព្រមពីអ្នកប្រើសម្រាប់គ្រប់ client ដែលបានចុះបញ្ជីបែបទាញយក

---

## 1. **ការត្រួតពិនិត្យការផ្ទៀងផ្ទាត់ និងអនុញ្ញាត**

### **ការរួមបញ្ចូលអ្នកផ្តល់អត្តសញ្ញាណខាងក្រៅ**

**ស្តង់ដារ MCP បច្ចុប្បន្ន (2025-11-25)** អនុញ្ញាតឲ្យម៉ាស៊ីនបម្រើ MCP ចែកចាយកិច្ចការផ្ទៀងផ្ទាត់ទៅអ្នកផ្តល់អត្តសញ្ញាណខាងក្រៅ ដែលជាការវាស់វែងសុវត្ថិភាពយ៉ាងសំខាន់៖

**ហានិភ័យ OWASP MCP ដែលបានបញ្ចេញ**៖ [MCP07 - ការផ្ទៀងផ្ទាត់ និងការអនុញ្ញាតមិនគ្រប់គ្រាន់](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**អត្ថប្រយោជន៍សុវត្ថិភាព៖**  
1. **បញ្ចប់ហានិភ័យផ្ទៀងផ្ទាត់ផ្ទាល់ខ្លួន**៖ កាត់បន្ថយភាពងាយរងគ្រោះដោយជៀសវាងការអនុវត្តផ្ទៀងផ្ទាត់ផ្ទាល់ខ្លួន  
2. **សុវត្ថិភាពជាប្រភេទសហគ្រាស**៖ ប្រើប្រាស់អ្នកផ្តល់អត្តសញ្ញាណដែលមានស្ថិតស្ថេរដូចជា Microsoft Entra ID ជាមួយមុខងារសុវត្ថិភាពឆ្លាតវៃ  
3. **គ្រប់គ្រងអត្តសញ្ញាណមជ្ឈមណ្ឌល**៖ ធ្វើឲ្យការគ្រប់គ្រងជីវិតអ្នកប្រើ បច្ចុប្បន្នភាពចូល និងការត្រួតពិនិត្យការអនុវត្តបានកាន់តែងាយស្រួល  
4. **ការផ្ទៀងផ្ទាត់ពីមូលដ្ឋានច្រើន**៖ ទទួលបានសមត្ថភាព MFA ពីអ្នកផ្តល់អត្តសញ្ញាណសហគ្រាស  
5. **គោលនយោបាយចូលដោយមានលក្ខខណ្ឌ**៖ ទទួលបានអត្ថប្រយោជន៍ពីការត្រួតពិនិត្យចូលដោយសារហានិភ័យ និងការផ្ទៀងផ្ទាត់អត្រាកាលបរិច្ឆេទ

**តម្រូវការអនុវត្ត៖**  
- **បញ្ជាក់ Token Audience**៖ ផ្ទៀងផ្ទាត់ថា token ទាំងអស់ត្រូវបានចេញសម្រាប់ម៉ាស៊ីនបម្រើ MCP យ៉ាងច្បាស់  
- **បញ្ជាក់ Issuer**៖ ផ្ទៀងផ្ទាត់មនុស្សចេញ token ត្រូវតាមអ្នកផ្តល់អត្តសញ្ញាណដែលបានរំពឹងទុក  
- **បញ្ជាក់ហត្ថលេខា**៖ ផ្ទៀងផ្ទាត់គុណភាព token ដោយវិទ្យាសាស្ត្រកូដគ្រាប់  
- **ច្បាប់ផុតកំណត់**៖ អនុវត្តកាត់ទោសពេលកំណត់ token បញ្ចប់  
- **បញ្ជាក់វិមាត្រ**៖ បញ្ចាក់ថា token មានសិទ្ធិដែលត្រឹមត្រូវសម្រាប់ប្រតិបត្តិការដែលបានស្នើ

### **សុវត្ថិភាពច្បាប់អនុញ្ញាត**

**ការត្រួតពិនិត្យសំខាន់ៈ**  
- **ការត្រួតពិនិត្យអនុញ្ញាតទូលំទូលាយ**៖ ពិនិត្យសុវត្ថិភាពជារៀងរាល់ចំណុចសម្រេចចិត្តអនុញ្ញាតទាំងអស់  
- **លំនាំស្តង់ដារពុំអនុញ្ញាត**៖ បដិសេធការចូលប្រើពេលច្បាប់អនុញ្ញាតមិនអាចសម្រេចបាន  
- **ដែនកំណត់សិទ្ធិ**៖ បំបែកយ៉ាងច្បាស់រវាងកម្រិតអាទិភាពជាប្រភេទនិងការចូលប្រើធនធាន  
- **កំណត់ហេតុនិម្មិត**៖ ចុះកំណត់ហេតុការសម្រេចចិត្តអនុញ្ញាតទាំងអស់សម្រាប់ការត្រួតពិនិត្យសុវត្ថិភាព  
- **ការពិនិត្យចូលជារឿយៗ**៖ ផ្ទៀងផ្ទាត់សិទ្ធិអ្នកប្រើ និងការចាត់តាំងអាទិភាពបន្ថែមជារឿយៗ

## 2. **សុវត្ថិភាព Token និងការទប់ស្កាត់ Anti-Passthrough**

**ហានិភ័យ OWASP MCP ដែលបានបញ្ចេញ**៖ [MCP01 - ការគ្រប់គ្រង Token មិនត្រឹមត្រូវ និងការបង្ហាញអាថ៌កំបាំង](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **ការទប់ស្កាត់ Token Passthrough**

**Token passthrough ត្រូវបានហាមឃាត់យ៉ាងច្បាស់** នៅក្នុង MCP Authorization Specification ដោយសារហានិភ័យសុវត្ថិភាពសំខាន់ៈ

**ហានិភ័យសុវត្ថិភាពដែលបានបញ្ចេញ៖**  
- **លុបបំបាត់ការត្រួតពិនិត្យ**៖ ជៀសវាងការត្រួតពិនិត្យសុវត្ថិភាពដូចជាកំណត់អត្រា ការផ្ទៀងផ្ទាត់សំណើ និងការត្រួតពិនិត្យចរាចរណ៍  
- **បាត់បង់ការទទួលខុសត្រូវ**៖ ធ្វើឲ្យមិនអាចស្គាល់អតិថិជនបាន ដល់ការបំផ្លាញសេចក្តីថ្លៃថ្នូរអាណត្តិ និងការស៊ើបអង្កេតព្រឹត្តិការណ៍  
- **ការនាំចេញតាមម៉ាស៊ីនបម្រើ Proxy**៖ អ្នកជាបាលល្មើសប្រើម៉ាស៊ីនបម្រើជាច្រកបង្ហោះសម្រាប់ការចូលដំណើរការទិន្នន័យមិនបានអនុញ្ញាត  
- **ការបំពានដែនទំនុកចិត្ត**៖ បំបែកការជឿជាក់របស់សេវាកម្មក្រោមដែនអំពីប្រភព token  
- **ចលនាសំលាប់បំផ្លាញនៅជិត**៖ token ដែលបានខូចឆ្ងាយពីសេវាកម្មជាច្រើន អនុញ្ញាតឲ្យបង្កើតការវាយប្រហារជាច្រើនទៀត

**ការត្រួតពិនិត្យអនុវត្ត៖**  
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```
  
### **គំរូការគ្រប់គ្រង Token រឹងមាំ**

**អនុស្សរណៈល្អបំផុត៖**  
- **Token រយៈពេលខ្លី**៖ កាត់បន្ថយរយៈពេលមានឱកាសឆ្លងកាត់ ដោយប្ដូរ token ជាញឹកញាប់  
- **ចេញផ្សាយតែពេលចាំបាច់**៖ ចេញ token តែពេលដែលត្រូវការសម្រាប់ប្រតិបត្តិការเฉพาะ  
- **ផ្ទុកយ៉ាងរឹងមាំ**៖ ប្រើម៉ូឌុលសុវត្ថិភាពរឹង (HSM) ឬឃ្លាំងកូនសោរដែលមានសុវត្ថិភាព  
- **បង្ហាប់ Token**៖ បង្ហាប់ token ទៅកាន់អតិថិជន សម័យសម្រង់ ឬប្រតិបត្តិការ ដែលអាចធ្វើទៅបាន  
- **ត្រួតពិនិត្យ និងជូនដំណឹង**៖ ការស្គាល់ពេលវេលាពិតប្រាកដនៃការប្រើប្រាស់ token មិនត្រឹមត្រូវ ឬការចូលប្រើមិនបានអនុញ្ញាត

## 3. **ការត្រួតពិនិត្យសុវត្ថិភាពសម័យសម្រង់**

### **ការទប់ស្កាត់ការឆ្លងខ្សែសម័យសម្រង់**

**វិធីសាស្រ្តវាយប្រហារ៖**  
- **បញ្ចូល Prompt វាយប្រហារសម័យ**៖ ព្រឹត្តិការណ៍មិនល្អដែលដាក់ក្នុងសភាពសម័យសម្រង់រួម  
- **ក្លែងបន្លំសម័យ**៖ ការប្រើប្រាស់ session ID ដែលបានលួចក្នុងការជៀសវាងការផ្ទៀងផ្ទាត់  
- **វាយប្រហារបន្តស្ទ្រីមដែលអាចបន្តបាន**៖ ការបំពានលើការធ្វើកម្មវិធី server-sent event ដើម្បីបញ្ចូលខ្ទេចខ្ទីឡើងវិញ

**ការត្រួតពិនិត្យកំណត់សម័យរឹងមាំ៖**  
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```
  
**សុវត្ថិភាពការបញ្ជូន៖**  
- **បង្ខំ HTTPS**៖ ការប្រាស្រ័យទាក់ទងសម័យត្រូវធ្វើតាម TLS 1.3 ទាំងអស់  
- **គ្រឿងតម្លើងគូគ៊ីសុវត្ថិភាព**៖ HttpOnly, Secure, SameSite=Strict  
- **ការចងក្រងវិញ្ញាបនបត្រ**៖ សម្រាប់ការតភ្ជាប់សំខាន់ៗ ដើម្បីទប់ស្កាត់ការវាយប្រហារប្រភេទ MITM

### **ការពិចារណាទាក់ទង Stateful និង Stateless**

**សម្រាប់អនុវត្ត Stateful៖**  
- សភាពសម័យរួមត្រូវការការពារ​បន្ថែមពីការបញ្ចូលវាយប្រហារ  
- ការគ្រប់គ្រងសម័យផ្អែកលើជួរ ត្រូវការការផ្ទៀងផ្ទាត់សុវត្ថិភាព  
- ម៉ាស៊ីនបម្រើច្រើនត្រូវការសមលេខសម័យសំរាប់ធានាជម្រើសសម័យសុវត្ថិភាពជាមួយគ្នា

**សម្រាប់អនុវត្ត Stateless៖**  
- គ្រប់គ្រងសម័យដោយ JWT ឬ token ស្រដៀងគ្នា  
- ផ្ទៀងផ្ទាត់សុវត្ថិភាពសភាពសម័យដោយគណិតវិទ្យាកូដគ្រាប់  
- កាត់បន្ថយរាងហេតុវាយប្រហារ ប៉ុន្ត្រូវការការផ្ទៀងផ្ទាត់ token រឹងមាំ

## 4. **ការត្រួតពិនិត្យសុវត្ថិភាពជាក់លាក់ AI**

**ហានិភ័យ OWASP MCP ដែលបានបញ្ចេញ**៖  
- [MCP06 - ការបញ្ចូល Prompt តាមផ្ទាំង context](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)  
- [MCP03 - ការបំផ្លាញឧបករណ៍](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)  
- [MCP05 - ការបញ្ចូលបញ្ជា និងការអនុវត្ត](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **ការពារ Prompt Injection**

**ការរួមបញ្ចូល Microsoft Prompt Shields៖**  
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```
  
**ការត្រួតពិនិត្យអនុវត្ត៖**  
- **ការសំអាតបញ្ចូល**៖ ការផ្ទៀងផ្ទាត់ និងជម្រះវាយយ៉ាងទូលំទូលាយសម្រាប់បញ្ចូលអ្នកប្រើទាំងអស់  
- **ការកំណត់ដែនកំណត់មាតិកា**៖ បំបែកយ៉ាងច្បាស់រវាងសេចក្តីណែនាំប្រព័ន្ធ និងមាតិកាអ្នកប្រើ  
- **អំណាចលំដាប់ណែនាំ**៖ ច្បាប់អាទិភាពត្រឹមត្រូវសម្រាប់សេចក្តីណែនាំមិនស្របគ្នា  
- **ត្រួតពិនិត្យលទ្ធផល**៖ ការចាប់សញ្ញាពីលទ្ធផលដែលអាចមានគ្រោះថ្នាក់ ឬត្រូវបានគូវរ

### **ការទប់ស្កាត់ Tool Poisoning**

**សុវត្ថិភាពឧបករណ៍:**  
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```
  
**ការគ្រប់គ្រងឧបករណ៍ឌីណាមិច:**  
- **សហការកម្មការអនុម័ត**៖ ការយល់ព្រមអ្នកប្រើប្រាស់យ៉ាងច្បាស់សម្រាប់ការផ្លាស់ប្តូរឧបករណ៍  
- **សមត្ថភាព Rollback**៖ អាចត្រឡប់ទៅកាន់កំណែឧបករណ៍មុនៗបាន  
- **ការត្រួតពិនិត្យការផ្លាស់ប្តូរ**៖ កំណត់ប្រវត្តិពេញលេញនៃការផ្លាស់ប្តូរបញ្ជាក់ឧបករណ៍  
- **ការវាយតម្លៃហានិភ័យ**៖ ការវាយតម្លៃសុវត្ថិភាពឧបករណ៍ដោយស្វ័យប្រវត្តិ

## 5. **ការទប់ស្កាត់ការវាយប្រហារជាមួយ Confused Deputy**

### **សុវត្ថិភាព OAuth Proxy**

**ការត្រួតពិនិត្យទប់ស្កាត់វាយប្រហារ៖**  
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```
  
**តម្រូវការអនុវត្ត៖**  
- **បញ្ជាក់ការយល់ព្រមអ្នកប្រើ**៖ មិនអនុញ្ញាតឲ្យរំលងផ្ទាំងយល់ព្រមសម្រាប់ការចុះបញ្ជី client ឌីណាមិច  
- **បញ្ជាក់ Redirect URI**៖ ផ្ទៀងផ្ទាត់តាមបញ្ជីស្ដើងយ៉ាងเข้มឈិននៃគោលដៅបង្វិល  
- **ការពារកូដអនុញ្ញាត**៖ កូដមានរយៈពេលខ្លី ជាមួយការជំរះបទបញ្ជាដល់ការប្រើប្រាស់មួយដង  
- **បញ្ជាក់អត្តសញ្ញាណ client**៖ ផ្ទៀងផ្ទាត់យ៉ាងរឹងមាំនៃគ្រឿងចក្រ client និងមេតាដាទា

## 6. **សុវត្ថិភាពការអនុវត្តឧបករណ៍**

### **Sandboxing និងការបំបែក**

**ការបំបែកដោយ Container៖**  
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```
  
**ការបំបែកដំណើរការ៖**  
- **បរិបទដំណើរការផ្សេងគ្នា**៖ ការអនុវត្តឧបករណ៍នីមួយៗនៅក្នុងបរិបទដំណើរការផ្សេងពីគ្នា  
- **ការប្រាស្រ័យទាក់ទងរវាងដំណើរការ**៖ បច្ចេកទេស IPC ដែលមានសុវត្ថិភាពជាមួយការផ្ទៀងផ្ទាត់  
- **ការត្រួតពិនិត្យដំណើរការ**៖ ការវិភាគសកម្មភាពរត់ បញ្ហាគុណភាព និងការស្គាល់ករណីមិនធម្មតា  
- **ការអនុវត្តធនធាន**៖ កំណត់ដែនកំណត់ CPU, មេម៉ូរី និង I/O

### **អនុវត្តតិចតួចអាទិភាព**

**ការគ្រប់គ្រងសិទ្ធិ៖**  
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```
  
## 7. **ការត្រួតពិនិត្យសុវត្ថិភាពខ្សែផ្គត់ផ្គង់**

**ហានិភ័យ OWASP MCP ដែលបានបញ្ចេញ**៖ [MCP04 - ការវាយប្រហារខ្សែផ្គត់ផ្គង់](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **ការបញ្ជាក់ការពឹងផ្អែក**

**សុវត្ថិភាពរបស់គ្រឿងផ្សំទូលំទូលាយ៖**  
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```
  
### **ការត្រួតពិនិត្យជាប្រចាំ**

**ការចាប់សញ្ញាហានិភ័យខ្សែផ្គត់ផ្គង់៖**  
- **ការត្រួតពិនិត្យសុខភាពការពឹងផ្អែក**៖ វាយតម្លៃជាប្រចាំលើគ្រប់ការពឹងផ្អែកសម្រាប់បញ្ហាសុវត្ថិភាព  
- **ការរួមបញ្ចូលព័ត៌មានហានិភ័យ**៖ ឆ្នៃប្រឌិតពេលវេលាពិតប្រាកដនៃការផ្សាយការហានិភ័យខ្សែផ្គត់ផ្គង់កើតឡើងថ្មី  
- **វិភាគអាកប្បកិរិយា**៖ ចាប់សញ្ញាប្រព្រឹត្តិការណ៍អស្ចារ្យនៅក្នុងគ្រឿងផ្សំនៅក្រៅ  
- **ចម្លើយស្វ័យប្រវត្តិ**៖ ការចាប់ខ្ទប់បានភ្លាមភ្លាស់ នៃគ្រឿងផ្សំដែលបានចាប់ខ្ទប់

## 8. **ការត្រួតពិនិត្យ និងការចាប់សញ្ញា**

**ហានិភ័យ OWASP MCP ដែលបានបញ្ចេញ**៖ [MCP08 - ការខ្វះខាត Audit និង Telemetry](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Security Information and Event Management (SIEM)**

**យុទ្ធសាស្ត្រចុះកំណត់ហេតុទូលំទូលាយ៖**  
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```
  
### **ការចាប់សញ្ញាហានិភ័យពេលវេលាពិតប្រាកដ**

**វិភាគអាកប្បកិរិយា៖**  
- **User Behavior Analytics (UBA)**៖ ចាប់សញ្ញាប្រព្រឹត្តិការណ៍ចូលប្រើប្រាស់អ្នកប្រើប្រាស់ករណីខុសប្រក្រតី  
- **Entity Behavior Analytics (EBA)**៖ ត្រួតពិនិត្យសកម្មភាពម៉ាស៊ីនបម្រើ MCP និងឧបករណ៍  
- **ការស្គាល់ករណីកំហុសដោយ Machine Learning**៖ ការរកឃើញហានិភ័យសុវត្ថិភាពដោយ AI  
- **ការរួមបញ្ចូល Threat Intelligence**៖ ធៀបធៀបសកម្មភាពដែលបានមើលឃើញជាមួយលំនាំវាយប្រហារដែលស្គាល់ហើយ

## 9. **ការឆែកសំណើ និងការស្តារតម្រង**

### **សមត្ថភាពឆ្លើយតបស្វ័យប្រវត្តិ**

**សកម្មភាពឆ្លើយតបភ្លាមៗ៖**  
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```
  
### **សមត្ថភាពវិភាគហេតុ**

**គាំទ្រស៊ើបអង្កេត៖**  
- **រក្សាទុក Audit Trail**៖ កំណត់ហេតុមិនអាចកែប្រែបានជាមួយសុវត្ថិភាពគណិតវិទ្យា  
- **ប្រមូលភស្តុតាង**៖ ការប្រមូលផតថលសុវត្ថិភាពពាក់ព័ន្ធដោយស្វ័យប្រវត្តិ  
- **បង្រួចពេលវេលាព្រឹត្តិការណ៍**៖ សេចក្តីលម្អិតពីលំដាប់ព្រឹត្តិការណ៍ដែលនាំឲ្យមានហានិភ័យសុវត្ថិភាព  
- **ការវាយតម្លៃផលប៉ះពាល់**៖ ការវាយតម្លៃដែនកំណត់នៃការបំបែក និងការបង្ហាញទិន្នន័យ

## **គោលការណ៍សំណុំរចនាសម្ព័ន្ធសុវត្ថិភាពសំខាន់ៗ**

### **ការការពារជាបន្តបន្ទាប់**

- **ស្រទាប់សុវត្ថិភាពច្រើន**៖ គ្មានចំណុចខូចខាតតែមួយក្នុងរចនាសម្ព័ន្ធសុវត្ថិភាព  
- **ការគ្រប់គ្រងបញ្ឈប់មិនឲ្យដំណើរការ**៖ វិធានការសុវត្ថិភាពស្ទាក់ស្ទើរនៅលើមុខងារសំខាន់ៗ  
- **ប្រព័ន្ធឆ្ពោះទៅ ដើម្បីបរាជ័យដោយសុវត្ថិភាព**៖ ធ្វើឲ្យមានលំនាំដើមដែលមានសុវត្ថិភាពនៅពេលប្រព័ន្ធមានបញ្ហា ឬរងការវាយប្រហារ

### **អនុវត្តសម្ពាធសូន្យ**

- **មិនទុកចិត្តទាល់តែម្ដង តែងតែផ្ទៀងផ្ទាត់**៖ ផ្ទៀងផ្ទាត់ជាបន្តបន្ទាប់លើអត្ថិភាពនៃគ្រប់អង្គភាព និងសំណើ  
- **គោលការណ៍តិចតួចអាទិភាព**៖ កំណត់សិទ្ធិចូលប្រើតិចបំផុតសម្រាប់គ្រប់ភាគសមាជិក  
- **ការបំបែកតូចតាចរាចរណ៍ និងការចូលប្រើ**៖ ការគ្រប់គ្រងបណ្ដាញ និងចូលប្រើជាប់លំដាប់តូចតាច

### **ការវិវឌ្ឍសុវត្ថិភាពជាបន្តបន្ទាប់**

- **បង្វែរហានិភ័យ**៖ អាប់ដេតទៀងទាត់ដើម្បីប្រយុទ្ធនឹងហានិភ័យកំពុងកើតឡើង  
- **ប្រសិទ្ធិភាពការគ្រប់គ្រងសុវត្ថិភាព**៖ វាយតម្លៃ និងធ្វើឲ្យប្រសើរឡើងការត្រួតពិនិត្យជាបន្តបន្ទាប់  
- **ការអនុលោមតាមបញ្ជីគោលការណ៍**៖ ស្របតាមស្តង់ដារសុវត្ថិភាព MCP កំពុងអភិវឌ្ឍ

---

## **ធនធានអនុវត្ត**

### **ឯកសារផ្លូវការរបស់ MCP**  
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **ធនធានសុវត្ថិភាព OWASP MCP**  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 ដោយផ្តោតអនុវត្ត Azure  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - ហានិភ័យសុវត្ថិភាព OWASP MCP ផ្លូវការ  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - បណ្តុះបណ្តាលសុវត្ថិភាពដៃគូសម្រាប់ MCP នៅ Azure

### **ដំណោះស្រាយសុវត្ថិភាព Microsoft**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **ស្តង់ដារសុវត្ថិភាព**  
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)  
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **សំខាន់**៖ ការត្រួតពិនិត្យសុវត្ថិភាពទាំងនេះសម្របសម្រួលតាម MCP specification បច្ចុប្បន្ន (2025-11-25)។ សូមតាមដានយោងទៅ [ឯកសារផ្លូវការ](https://spec.modelcontextprotocol.io/) ជាប្រចាំ ពីព្រោះស្តង់ដារតែងតែមានការអភិវឌ្ឍយ៉ាងរហ័ស។

## អ្វីទីបន្ទាប់

- ត្រឡប់ទៅ៖ [Security Module Overview](./README.md)  
- បន្តទៅ៖ [Module 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ យើងខិតខំប្រឹងប្រែងដើម្បីឱ្យបានភាពត្រឹមត្រូវ ប៉ុន្តែសូមយល់ឲ្យបានថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគេអះអាងថាជាឯកសារដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញជាអ្នកមនុស្សត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
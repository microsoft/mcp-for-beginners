# ការត្រួតពិនិត្យសុវត្ថិភាព MCP - ធ្វើបច្ចុប្បន្នភាពខែកញ្ញារូបភាព២០២៦

> **ស្តង់ដារបច្ចុប្បន្ន៖** ឯកសារនេះបង្ហាញពី
> [លក្ខណៈពិសេស MCP ២០២៦-០៧-២៨](https://modelcontextprotocol.io/specification/2026-07-28/)
> និងផ្លូវការដ៏
> [ការអនុវត្តសុវត្ថិភាពល្អបំផុត MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)។

ពិធីការដំនើរការយោងវត្ថុ (MCP) មានការវិវត្តន៍យ៉ាងសំខាន់ជាមួយការត្រួតពិនិត្យសុវត្ថិភាពដែលបានបង្កើន សំរាប់ការពារទាំងសុវត្ថិភាពកម្មវិធីបែបបុរាវិទ្យា និងការគំរាមគំរោចជាក់លាក់សម្រាប់ AI ។ ឯកសារនេះផ្តល់នូវការត្រួតពិនិត្យសុវត្ថិភាពទូលំទូលាយសម្រាប់ការអនុវត្ត MCP ដែលមានសុវត្ថិភាព និងឆ្លើយតបនឹងស៊ុមគំរោង OWASP MCP Top 10។

## 🏔️ បណ្តុះបណ្តាលសុវត្ថិភាពប្រើប្រាស់ជាក់ស្តែង

សម្រាប់បទពិសោធន៍អនុវត្តសុវត្ថិភាពប្រើប្រាស់ជាក់ស្តែងយ៉ាងពេញលេញ យើងផ្ដល់អនុសាសន៍ **[សិក្ខាសាលាពិភាក្សាសុវត្ថិភាព MCP Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - ជាការដំណើរការដឹកនាំពេញលេញដើម្បីការពារម៉ាស៊ីនម៉ាស៊ីន MCP នៅលើ Azure ដោយប្រើវិធីសាស្ដ្ររួមមាន "ខ្សោយ → លោតប្រើ → កែលម្អ → ផ្ទៀងផ្ទាត់"។

ការត្រួតពិនិត្យសុវត្ថិភាពទាំងអស់ក្នុងឯកសារនេះត្រូវនឹង **[មគ្គុទេសក៍សុវត្ថិភាព OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** ដែលផ្តល់នូវរចនាសម្ព័ន្ធយោង និងមគ្គុទេសក៍អនុវត្តជាក់លាក់ក្នុង Azure សម្រាប់ហានិភ័យ OWASP MCP Top 10។

## **លក្ខខណ្ឌសុវត្ថិភាពចាំបាច់**

### **ការហាមឃាត់សំខាន់ៗពីលក្ខណៈពិសេស MCP:**

> **ហាមឃាត់**៖ ម៉ាស៊ីនម៉ាស៊ីន MCP **មិនត្រូវ** ទទួលយកសញ្ញាតំណាងណាដែលមិនត្រូវបានចេញសម្រាប់ម៉ាស៊ីន MCP ដោយច្បាស់
>
> **ហាមឃាត់**៖ ម៉ាស៊ីនម៉ាស៊ីន MCP **មិនគួរប្រើ** សម័យសម្រាប់ការផ្ទៀងផ្ទាត់
>
> **តម្រូវការ**៖ ម៉ាស៊ីនម៉ាស៊ីន MCP ដែលអនុវត្តការអនុញ្ញាត **ត្រូវ** ពិនិត្យរាល់សំណើចូលទាំងអស់
>
> **ចាំបាច់**៖ ម៉ាស៊ីនម៉ាស៊ីន MCP proxy ដែលប្រើប្រាស់ Client ID ពីភាគីទីបីថេរ
> **ត្រូវ** ទទួលបានការយល់ព្រមសម្រាប់មួយរាល់ MCP client មុនការផ្ញើការអនុញ្ញាត

---

## 1. **ការត្រួតពិនិត្យទទួលស្គាល់ និងអនុញ្ញាត**

### **ការរួមបញ្ចូលអ្នកផ្ដល់អត្តសញ្ញាណខាងក្រៅ**

**លក្ខណៈពិសេស MCP `2026-07-28`** អនុញ្ញាតឱ្យម៉ាស៊ីន MCP ផ្ទេរមុខភារកិច្ច
ការផ្ទៀងផ្ទាត់ទៅអ្នកផ្ដល់អត្តសញ្ញាណខាងក្រៅ។ ការអនុញ្ញាតសម្រាប់
ការដឹកជញ្ជូន HTTP ត្រូវបានបោះជើងតាមសំណើមួយមួយ; ម៉ាស៊ីន stdio ក្នុងតំបន់ទទួលយក
លិខិតសំគាល់ពីបរិយាកាសរបស់ខ្លួនជាផ្ទាល់វិញ។

**ហានិភ័យ OWASP MCP ដើម្បីដោះស្រាយ**៖ [MCP07 - ការបញ្ចុះការផ្ទៀងផ្ទាត់ និងអនុញ្ញាត](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**លោកអត្ថប្រយោជន៍សុវត្ថិភាព៖**
1. **កាត់បន្ថយហានិភ័យផ្ទៀងផ្ទាត់ផ្ទាល់ខ្លួន**៖ កាត់បន្ថយផ្ទៃហានិភ័យដោយជៀសវាងការអនុវត្តផ្ទៀងផ្ទាល់ខ្លួន
2. **សុវត្ថិភាពថ្នាក់ទេពកោសល្យ**៖ ប្រើប្រាស់អ្នកផ្ដល់អត្តសញ្ញាណដ៏ល្បីដូចជា Microsoft Entra ID ដែលមានមុខងារសុវត្ថិភាពកំពូល
3. **ការគ្រប់គ្រងអត្តសញ្ញាណមណ្ឌល**៖ ធ្វើឱ្យការគ្រប់គ្រងជីវិតអ្នកប្រើប្រាស់ ការគ្រប់គ្រងចូល និងការត្រួតពិនិត្យការចេះដឹងកាន់តែងាយស្រួល
4. **ការផ្ទៀងផ្ទាត់តាមហ្វ murti-facteurs**៖ ទទួលបានសមត្ថភាព MFA ពីអ្នកផ្ដល់អត្តសញ្ញាណនេះ
5. **គោលនយោបាយចូលដោយលក្ខខណ្ឌ**៖ ទទួលផលពីការគ្រប់គ្រងចូលផ្អែកលើហានិភ័យនិងការផ្ទៀងផ្ទាត់បត់បែន

**ការទាមទារ អនុវត្ត៖**
- **ការចុះបញ្ជីអតិថិជន**៖ ចូលចិត្តឯកសារ Metadata Client ID ឬ
  ការចុះបញ្ជីមុន; ប្រើការចុះបញ្ជីអតិថិជន Dynamic ដែលត្រូវបានបោះបង់តែសម្រាប់
  ការភ្ជាប់សមរម្យ
- **ការផ្ទៀងផ្ទាត់អ្នកទទួលសញ្ញាតំណាង**៖ ពិនិត្យមើលសញ្ញាតំណាងទាំងអស់បានចេញជាក់លាក់សម្រាប់ម៉ាស៊ីន MCP
- **ការផ្ទៀងផ្ទាត់អ្នកចេញ**៖ បញ្ជាក់អ្នកចេញសញ្ញាតំណាងផ្គូផ្គងនឹងអ្នកផ្ដល់អត្តសញ្ញាណដែលបានរំពឹងទុក
- **ការផ្ទៀងផ្ទាត់ហត្ថលេខា**៖ ការពិនិត្យគុណភាពសារពើភ័ណ្ឌនៃសញ្ញាតំណាងដោយប្រើអាល់ហ្គរីធម៍គ្រប់គ្រាន់
- **ការអនុវត្តអាយុកាលសញ្ញាតំណាង**៖ អនុវត្តយ៉ាងតឹងរឹងលើកំណត់អាយុកាលសញ្ញាតំណាង
- **ការផ្ទៀងផ្ទាត់វិសាលភាព**៖ ត្រូវប្រាកដថាសញ្ញាតំណាងមានសិទ្ធិគ្រប់គ្រាន់សម្រាប់ប្រតិបត្តិការដែលបានស្នើ

### **សុវត្ថិភាពនៃត្រួតពិនិត្យលទ្ធផលអនុញ្ញាត**


**ការត្រួតពិនិត្យសំខាន់ៗ:**
- **ការត្រួតពិនិត្យសេចក្តីអនុញ្ញាតជាសរុប**: ការត្រួតពិនិត្យសន្តិសុខជាប្រចាំនៃចំណុចសម្រេចអនុញ្ញាតទាំងអស់
- **លំនាំដើមដែលមានសុវត្ថិភាព**: បដិសេធការចូលប្រើពេលដែលហេតុលេខសម្រេចអនុញ្ញាតមិនអាចធ្វើការសម្រេចចិត្តច្បាស់លាស់បាន
- **ស្នូលសិទ្ធិ**: ការបំបែកច្បាស់លាស់រវាងកម្រិតអំណាចផ្សេងៗ និងការចូលប្រើធនធាន
- **កំណត់ហេតុត្រួតពិនិត្យ**: ការកត់ត្រាលម្អិតនៃសេចក្តីសម្រេចអនុញ្ញាតទាំងអស់សម្រាប់ការត្រួតពិនិត្យសន្តិសុខ
- **ការត្រួតពិនិត្យការចូលប្រើជាប្រចាំ**: ការផ្ទៀងផ្ទាត់កំណត់សិទ្ធិអ្នកប្រើ និងការចាត់ចែងអំណាចជាប្រចាំ

## 2. **សន្តិសុខ Token និងការត្រួតពិនិត្យប្រឆាំងនឹង Passthrough**

**ហានិភ័យ OWASP MCP ដែលបានដោះស្រាយ**: [MCP01 - ការគ្រប់គ្រង Token ខុស និងការបង្ហាញអាថ៌កំបាំង](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **ការពារការចេញ Token Passthrough**

**ការចេញ Token Passthrough ត្រូវបានហាមឃាត់យ៉ាងច្បាស់** ក្នុងការបញ្ជាក់ MCP Authorization ដោយសារហានិភ័យសន្តិសុខសំខាន់ៗ:

**ហានិភ័យសន្តិសុខដែលបានដោះស្រាយ៖**
- **ការឆ្លងកាត់ការត្រួតពិនិត្យ**: ជ្រាបញែកការត្រួតពិនិត្យសន្តិសុខសំខាន់ៗដូចជា ការកំណត់កំណត់អត្រា, ការផ្ទៀងផ្ទាត់សំណើរ និងការត្រួតពិនិត្យចរាចរណ៍
- **ការបែកបាក់ការទទួលខុសត្រូវ**: ធ្វើឲ្យការកំណត់អត្តសញ្ញាណអតិថិជនមិនអាចធ្វើបាន បំផ្លាញបណ្តាញត្រួតពិនិត្យ និងការស៊ើបអង្កេតហេតុការណ៍
- **ការប្រើប្រាស់ Proxy ដើម្បីលួចយកទិន្នន័យ**: អនុញ្ញាតឲ្យអ្នកបំផ្លាញប្រើម៉ាស៊ីនមេជាមធ្យោបាយសម្រាប់ចូលប្រើទិន្នន័យដោយគ្មានការអនុញ្ញាត
- **ការបំពានដែនកំណត់ទុកចិត្ត**: បំបែកការសន្មត់ទុកចិត្តនៃសេវាតាមរយៈ token ដើម
- **ការផ្លាស់ទីប្រេកង់**: Token ដែលត្រូវបានជាប់ឥណ្ឌិចលើសេវាច្រើនធ្វើឲ្យសមត្ថភាពលើកលែងកំហុសធំជាងមុន

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

### **លេខាប្រព័ន្ធគ្រប់គ្រង Token ដោយសុវត្ថិភាព**

**អនុវត្តន៍ល្អបំផុត:**
- **Token មានពេលវែងខ្លី**: កាត់បន្ថយរយៈពេលរំលាក់ដោយការបង្វិល token ជាប្រចាំ
- **ចេញ Token ត្រឹមពេលត្រូវការ**: ចេញ token មិនលើសពេលមានតែសម្រាប់ប្រតិបត្តិការ​ដាច់ខាត
- **ការផ្ទុកសុវត្ថិភាព**: ប្រើកម្រិតសុវត្ថិភាពរឹងមាំដូចជា hardware security modules (HSMs) ឬ key vaults ដែលមានសុវត្ថិភាព
- **ការចងភ្ជាប់ Token**: ផ្ទៀងផ្ទាត់ token audience និង អ្នកចេញសម្រាប់ MCP ដើម
  ធនធាន, អតិថិជន, និងប្រតិបត្តិការ
- **ការត្រួតពិនិត្យ និងការជូនដំណឹង**: ការរកឃើញពេលវេលាពីការប្រើ token មិនត្រឹមត្រូវឬលំនាំចូលប្រើគ្មានការអនុញ្ញាត

## 3. **ការត្រួតពិនិត្យសន្តិសុខស្ថានភាពកម្មវិធី**

### **ការទប់ទល់ការចាប់យក State Handle**

**វិធីប្រើប្រាស់ការវាយប្រហារដែលបានដោះស្រាយ:**
- **ការប៉ាន់ស្មាន Handle**: អត្តសញ្ញាណដែលអាចប៉ាន់មើលបានបង្ហាញ​ស្ថានភាពរបស់អ្នកហៅផ្សេងទៀត
- **ការចែករំលែកពេញមួយអ្នកប្រើ**: Handle ដែលត្រូវបានលួចបានប្រើជាមួយ​អត្តសញ្ញាណខុស
- **អនុញ្ញាតនៅលើការញៀនបំភ្លេច**: ការទទួលជាម្ចាស់ Handle ត្រូវបានចាត់ទុកខុស ទៅជាភស្តុតាងនៃការចូលប្រើ
 

**ការត្រួតពិនិត្យ State Handle:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**សន្តិសុខការដឹកជញ្ជូន:**
- **ការមានបន្ទុះ HTTPS**: បញ្ជាក់ឲ្យមាន HTTPS សម្រាប់ការដឹកជញ្ជូន HTTP ផ្នែកចម្ងាយ
- **ការគ្រប់គ្រងអត្តសញ្ញាណ**: ផ្ញើ និងផ្ទៀងផ្ទាត់ការអនុញ្ញាតើរៀងរាល់សំណើ HTTP
- **ការផ្ទៀងផ្ទាត់ stdio**: ការពារម៉ាស៊ីនមេ stdio មូលដ្ឋានតាមរយៈការបំបែកដំណើរការ និង
  ការគ្រប់គ្រងសញ្ជាតិសាកល្បងបរិយាកាស

### **ការពិចារណារវាង Stateful និង Stateless**

MCP `2026-07-28` គឺជា Stateless នៅកម្រិតពិធិការណ៍។ កម្មវិធីអាចនៅតែ
កាន់ស្ថានភាពដោយបញ្ចូន Handle ដោយច្បាស់ពីការហៅឧបករណ៍មួយ ហើយទទួលយកវាជាអាគុយម៉ង់ធម្មតាលើការហៅបន្ទាប់។


- ប្រាប់រក្សាស្ថានភាពដោយដាច់ដោយឡែកពីការតភ្ជាប់ដឹកជញ្ជូនណាមួយ។
- ចង Handle ស្ថានភាពទៅវិញឲ្យអត្តសញ្ញាណPrinciple ដែលបានផ្ទៀងផ្ទាត់ពីផ្នែកម៉ាស៊ីនមេ។
- រៀបចំ Handle ឲ្យដូចជាឈ្មោះ មិនមែនជាសញ្ញាអត្តសញ្ញាណ។
- កំណត់រយៈពេលផុតកំណត់ និងការបញ្ច្រាសសម្រាប់ Handle ដែលចាស់។

## 4. **ការត្រួតពិនិត្យសន្តិសុខជាក់លាក់សម្រាប់ AI**

**ហានិភ័យ OWASP MCP ដែលបានដោះស្រាយ**:

- [MCP06 - ការប្រឆាំងចរន្តចេតនា](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - ការបំប៉នឧបករណ៍](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - ការចាក់បញ្ចូល និងអនុវត្តបទបញ្ជា](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **ការពារការចាក់បញ្ចូលជំរុញ**

**ការសម្របសម្រួល Microsoft Prompt Shields:**
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

**ការគ្រប់គ្រងអនុវត្ត:**
- **ការសម្អាតបញ្ចូល**: ការត្រួតពិនិត្យ និងការជម្រះចេញយ៉ាងទូលំទូលាយនៃបញ្ចូលរបស់អ្នកប្រើទាំងអស់
- **ការកំណត់ដែនកំណត់មាតិកា**: ការបំបែកច្បាស់លាស់រវាងការណែនាំប្រព័ន្ធ និងមាតិកានៃអ្នកប្រើ
- **អាទិភាពនៃការណែនាំ**: វិន័យនៃអាទិភាពក្នុងករណីមានការប្រកួតប្រជែងនៅលើការណែនាំ
- **ការត្រួតពិនិត្យចេញ**: ការរកឃើញលទ្ធផលដែលអាចគ្រោះថ្នាក់ ឬត្រូវបានបំភ្លឺ

### **ការពារការបំប៉នឧបករណ៍**

**ស៊ុមសុវត្ថិភាពឧបករណ៍:**
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

**ការគ្រប់គ្រងឧបករណ៍ឆ្លាតវៃ:**
- **ស្របព្រឹត្តិការណ៍អនុម័ត**: ការយល់ព្រមយ៉ាងច្បាស់ពីអ្នកប្រើសម្រាប់ការផ្លាស់ប្តូរឧបករណ៍
- **សមត្ថភាពបិទត្រលប់**: សមត្ថភាពក្នុងការត្រឡប់ទៅកាន់កំណែឧបករណ៍មុន
- **ការត្រួតពិនិត្យការផ្លាស់ប្តូរ**: ប្រវត្តិពេញលេញនៃការផ្លាស់ប្តូរបរិយាយឧបករណ៍
- **ការវាយតម្លៃហានិភ័យ**: ការវាយតម្លៃសុវត្ថិភាពឧបករណ៍ដោយស្វ័យប្រវត្តិ

## 5. **ការពារការវាយប្រហារខកចិត្តការងារ**

### **សុវត្ថិភាព OAuth Proxy**

**ការគ្រប់គ្រងការពារវាយប្រហារ:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**តម្រូវការអនុវត្ត:**
- **ការចុះបញ្ជីអតិថិជន**: ជម្រើសចុះបញ្ជីមុនឬឯកសារទិន្នន័យអតិថិជន ID
  គួរព្យាយាមការចុះបញ្ជីអតិថិជនដYNAMICជា fallback ជំនួសការភាពសមរម្យ
- **ការបញ្ជាក់ត្រូវយល់ព្រមអ្នកប្រើ**: MCP proxies ប្រើអតិថិជនទីបីដែលមាន ID ស្ថិតស្ថេរ
  ត្រូវទទួលយកការយល់ព្រមក្នុងមួយអតិថិជនមុនពេលប្រារព្ធការអនុញ្ញាត
- **ការត្រួតពិនិត្យ URI ផ្តល់ទីតាំង**: ពិនិត្យ whitelist យ៉ាងតឹងរឹងចំពោះទីតាំងបញ្ជូនទៅ
- **ការពារកូដអនុញ្ញាត**: កូដមានអាយុកាលខ្លី និងអនុញ្ញាតឲ្យប្រើតែមួយដង
- **ការត្រួតពិនិត្យអត្តសញ្ញាណអតិថិជន**: ពិនិត្យយ៉ាងរឹងមាំលើគ្រឿងចក្រ និងព័តមានអតិថិជន

## 6. **សុវត្ថិភាពការអនុវត្តឧបករណ៍**

### **ការsandboxing និងបំបែក**

**ការបំបែកផ្អែកលើ container:**
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

**ការបំបែកដំណើរការ:**
- **បរិបទដំណើរការបំបែក**: ការអនុវត្តឧបករណ៍ក្នុងលក្ខណៈបំបែកដំណើរការ
- **ការទំនាក់ទំនងចន្លោះដំណើរការ**: វិធីសាស្រ្ត IPC ដែលមានសុវត្ថិភាព និងត្រួតពិនិត្យ
- **ការត្រួតពិនិត្យដំណើរការ**: ការវិភាគឥរិយាបថរត់ពេល និងរកឃើញអត្រាការលំបាក
- **ការអនុវត្តធនធាន**: កំណត់ដែនកម្រិតសម្រាប់ CPU, ការចងចាំ និងប្រតិបត្តិការបញ្ចូល/ចេញ

### **ការអនុវត្តសិទ្ធិទាបបំផុត**

**ការគ្រប់គ្រងសិទ្ធិ:**
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

## 7. **ការគ្រប់គ្រងសុវត្ថិភាពខ្សែផ្គត់ផ្គង់**

**ហានិភ័យ OWASP MCP ដែលពាក់ព័ន្ធ**: [MCP04 - វាយប្រហារខ្សែផ្គត់ផ្គង់កម្មវិធី និងការបំប្លែងពឹងផ្អែក](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **ការត្រួតពិនិត្យអាស្រ័យភាព**

**សុវត្ថិភាពគ្រឿងផ្សំទូលំទូលាយ:**
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

### **ការត្រួតពិនិត្យបន្តបន្ទាប់**

**ការស្វែងរកគំរាមកំហែងខ្សែផ្គត់ផ្គង់:**
- **ការត្រួតពិនិត្យសុខភាពអាស្រ័យភាព**: ការវាយតម្លៃជាបន្តបន្ទាប់នៃអាស្រ័យភាពទាំងអស់សម្រាប់បញ្ហាសុវត្ថិភាព
- **ការបញ្ចូលចំណេះដឹងគំរាមកំហែង**: ជំនួសពេលវេលាពីគំរាមកំហែងខ្សែផ្គត់ផ្គង់កំពុងកើតឡើង
- **វិភាគអាកប្បកិរិយា**: ការរកឃើញឥរិយាបថអត្រាអសកម្មក្នុងគ្រឿងផ្សំពីក្រៅ
- **ការឆ្លើយតបស្វ័យប្រវត្តិ**: ការចាប់ផ្តើមភ្ជាប់យ៉ាងរហ័សចំពោះគ្រឿងផ្សំដែលត្រូវបានជាប់ពាក់ព័ន្ធ

## 8. **ការត្រួតពិនិត្យ និងការរកឃើញ**

**ហានិភ័យ OWASP MCP ដែលពាក់ព័ន្ធ**: [MCP08 - ការខ្វះខាតនៃការត្រួតពិនិត្យ និងសំឡេងតាមដាន](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **ការគ្រប់គ្រងព័ត៌មានសុវត្ថិភាព និងព្រឹត្តិបត្រ (SIEM)**

**យុទ្ធសាស្ដ្រកំណត់ហេតុទូលំទូលាយ:**
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

### **ការរកឃើញគំរាមកំហែងពេលវេលាត្រួតពិនិត្យ**

**វិភាគអាកប្បកិរិយា:**
- **វិភាគអាកប្បកិរិយាអ្នកប្រើប្រាស់ (UBA)**: ការរកឃើញលំនាំចម្លើយដែលមិនធម្មតារបស់អ្នកប្រើ
- **វិភាគអាកប្បកិរិយាសកម្មភាព (EBA)**: ការត្រួតពិនិត្យអាកប្បកិរិយា MCP server និងឧបករណ៍
- **ការរកឃើញកំហុសដោយម៉ាស៊ីនលើកឡើង**: ការបញ្ជាក់ជាថ្មីដោយ AI នៃគំរាមកំហែងសុវត្ថិភាព
- **ការតភ្ជាប់ចំណេះដឹងគំរាមកំហែង**: ការតភ្ជាប់សកម្មភាពដែលមើលឃើញនិងលំនាំដទៃនៃការវាយប្រហារ

## 9. **ការឆ្លើយតប និងការស្តារឡើងវិញករណីហេតុការណ៍**

### **សមត្ថភាពឆ្លើយតបស្វ័យប្រវត្តិ**

**សកម្មភាពឆ្លើយតបភ្លាមៗ:**
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

### **សមត្ថភាពវេយ្យាករណ៍**

**ការគាំទ្រស្ទង់សំណួរ:**
- **ការរក្សាតាមដានតាមឡូក**: ការចុះបញ្ជីមិនអាចផ្លាស់ប្តូរជាមួយភាពអចិន្រ្តៃយ៍ភស្តុតាង
- **ការប្រមូលភស្តុតាង**: ការប្រមូលដោយស្វ័យប្រវត្តិនៃឯកសារសុវត្ថិភាពពាក់ព័ន្ធ
- **ការស្ដារប្រលោមបណ្ដាដៃ**: លំដាប់ព្រឹត្តិការណ៍លំអិតដែលនាំឲ្យមានហេតុការណ៍សុវត្ថិភាព
- **ការវាយតម្លៃឥទ្ធិពល**: ការវាយតម្លៃវិសាលភាពភាពបំផ្លាញ និងការបង្ហាញទិន្នន័យ

## **គោលការណ៍ស្ថាបត្យកម្មសុវត្ថិភាពសំខាន់ៗ**

### **ការពារជាបន្ទាទៀត**
- **ស្រទាប់សុវត្ថិភាពច្រើន**: គ្មានចំណុចខូចតែមួយនៅក្នុងស្ថាបត្យកម្មសុវត្ថិភាព
- **ការគ្រប់គ្រងមានការចំរូង**: វិធានសុវត្ថិភាពដែលរំលងគ្នាសម្រាប់មុខងារសំខាន់ៗ
- **យន្តការសុវត្ថិភាព Fail-Safe**: ការកំណត់លំនាំដើមសុវត្ថិភាពនៅពេលប្រព័ន្ធជួបប្រទៈកំហុសឬវិវាទ

### **ការអនុវត្ត Zero Trust**
- **មិនដែលជឿទុកចិត្ត តែងតែបញ្ចាក់**: ការត្រួតពិនិត្យបន្តបន្ទាប់របស់អង្គភាព និងសំណើរទាំងឡាយ
- **គោលការណ៍សិទ្ធិទាបបំផុត**: សិទ្ធិចូលប្រើតិចបំផុតសម្រាប់ធាតុទាំងអស់
- **ការបំបែកតូចចេញ**: ការគ្រប់គ្រងបណ្តាញ និងចូលប្រើយ៉ាងត្រឹមត្រូវ

### **ការវិវឌ្ឍសុវត្ថិភាពបន្តបន្ទាប់**
- **ការប្រែប្រួលលក្ខណៈគំរាមកំហែង**: ការអាប់ដេតទៀងទាត់ដើម្បីឆ្លើយតបគំរាមកំហែងកំពុងកើតឡើង
- **ប្រសិទ្ធភាពការគ្រប់គ្រងសុវត្ថិភាព**: ការវាយតម្លៃ និងអភិវឌ្ឍន៍ជាបន្តបន្ទាប់នៃវិធានការ
- **ការអនុវត្តស្តង់ដារ**: ការប្រកួតប្រជែងជាមួយស្តង់ដារ MCP សុវត្ថិភាពកំពុងអភិវឌ្ឍ

---

## **ធនធានអនុវត្ត**

### **ឯកសារផ្លូវការ MCP**
- [ពិពណ៌នាម៉ូឌယ် MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [អនុវត្តន៍សុវត្ថិភាពល្អបំផុត MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [ពិពណ៌នាអនុញ្ញាត MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **ធនធានសុវត្ថិភាព OWASP MCP**
- [មគ្គុទេសក៍សុវត្ថិភាព Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 ទូលំទូលាយជាមួយអនុវត្ត Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - បញ្ហាសុវត្ថិភាព OWASP MCP ផ្លូវការ
- [សិក្ខាសាលាស្តង់ដាសុវត្ថិភាព MCP Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - ការបណ្តុះបណ្តាលផ្នែកសុវត្ថិភាពហ្រ្វាស់ MCP លើ Azure

### **ដំណោះស្រាយសុវត្ថិភាព Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **ស្តង់ដារសុវត្ថិភាព**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP ១០ ចំណូលសំខាន់សម្រាប់គំរូភាសាធំៗ](https://genai.owasp.org/)

- [ស៊ុមសុវត្ថិភាព NIST](https://www.nist.gov/cyberframework)

---

> **សំខាន់៖** ការត្រួតពិនិត្យសុវត្ថិភាពទាំងនេះបង្ហាញពីការបញ្ជាក់ MCP
> `2026-07-28`។ តែងតែពិនិត្យឡើងវិញជាមួយ
> [ឯកសារផ្លូវការបច្ចុប្បន្ន](https://modelcontextprotocol.io/specification/2026-07-28/)
> ខណៈដែលស្តង់ដារត្រូវបានបន្តអភិវឌ្ឍ។

## តើជំហានបន្ទាប់ជាអ្វី

- ត្រឡប់ទៅ: [ទិដ្ឋភាពទូទៅនៃម៉ូឌុលសុវត្ថិភាព](./README.md)
- បន្តទៅ: [ម៉ូឌុល 3៖ ការចាប់ផ្តើម](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP Контроле безбедности - Ажурирање децембар 2025.

> **Тренутни стандард**: Овај документ одражава [MCP Спецификацију 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) безбедносне захтеве и званичне [MCP Најбоље праксе безбедности](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Протокол контекста модела (MCP) је значајно сазрео са побољшаним контролама безбедности које се баве како традиционалном безбедношћу софтвера тако и претњама специфичним за вештачку интелигенцију. Овај документ пружа свеобухватне контроле безбедности за сигурне имплементације MCP-а од децембра 2025.

## **ОБАВЕЗНИ Безбедносни Захтеви**

### **Критичне Забране из MCP Спецификације:**

> **ЗАБРАЊЕНО**: MCP сервери **НЕ СМЕЈУ** прихватати било какве токене који нису изричито издати за MCP сервер  
>
> **ЗАБРАЊЕНО**: MCP сервери **НЕ СМЕЈУ** користити сесије за аутентификацију  
>
> **ЗАХТЕВАНО**: MCP сервери који имплементирају ауторизацију **СМЕЈУ** верификовати СВЕ долазне захтеве  
>
> **ОБАВЕЗНО**: MCP прокси сервери који користе статичке ИД клијенте **СМЕЈУ** добити сагласност корисника за сваког динамички регистрованог клијента

---

## 1. **Контроле аутентификације и ауторизације**

### **Интеграција спољних провајдера идентитета**

**Тренутни MCP стандард (2025-06-18)** дозвољава MCP серверима да делегирају аутентификацију спољним провајдерима идентитета, што представља значајно побољшање безбедности:

### **Интеграција спољних провајдера идентитета**

**Тренутни MCP стандард (2025-11-25)** дозвољава MCP серверима да делегирају аутентификацију спољним провајдерима идентитета, што представља значајно побољшање безбедности:

**Безбедносне предности:**
1. **Уклања ризике прилагођене аутентификације**: Смањује површину рањивости избегавањем прилагођених имплементација аутентификације  
2. **Безбедност на нивоу предузећа**: Користи успостављене провајдере идентитета као што је Microsoft Entra ID са напредним безбедносним функцијама  
3. **Централизовано управљање идентитетом**: Једноставније управљање животним циклусом корисника, контролом приступа и ревизијом усаглашености  
4. **Мултифакторска аутентификација**: Наслеђује MFA могућности од провајдера идентитета предузећа  
5. **Политике условног приступа**: Користи контроле приступа засноване на ризику и адаптивну аутентификацију

**Захтеви за имплементацију:**
- **Валидација публике токена**: Верификовати да су сви токени изричито издати за MCP сервер  
- **Верификација издаваоца**: Потврдити да издаваоц токена одговара очекиваном провајдеру идентитета  
- **Верификација потписа**: Криптографска валидација интегритета токена  
- **Примена рока важења**: Строга примена ограничења трајања токена  
- **Валидација опсега**: Осигурати да токени садрже одговарајуће дозволе за тражене операције

### **Безбедност логике ауторизације**

**Критичне контроле:**
- **Свеобухватне ревизије ауторизације**: Редовни безбедносни прегледи свих тачака одлучивања о ауторизацији  
- **Подразумеване безбедне вредности**: Одбијање приступа када логика ауторизације не може донети дефинитивну одлуку  
- **Границе дозвола**: Јасна раздвојеност између различитих нивоа привилегија и приступа ресурсима  
- **Логовање ревизије**: Потпуно евидентирање свих одлука о ауторизацији за безбедносни надзор  
- **Редовни прегледи приступа**: Периодична валидација корисничких дозвола и додела привилегија

## 2. **Безбедност токена и контроле спречавања прослеђивања**

### **Спречавање прослеђивања токена**

**Прослеђивање токена је изричито забрањено** у MCP Спецификацији ауторизације због критичних безбедносних ризика:

**Ризици безбедности који се решавају:**
- **Заобилажење контрола**: Пробијање кључних безбедносних контрола као што су ограничење брзине, валидација захтева и праћење саобраћаја  
- **Прекид одговорности**: Онемогућава идентификацију клијента, кварећи трагове ревизије и истраге инцидената  
- **Извлачење података преко проксија**: Омогућава злонамерним актерима да користе сервере као проксије за неовлашћени приступ подацима  
- **Прекид граница поверења**: Крши претпоставке о пореклу токена у сервисима низводно  
- **Латерално кретање**: Компромитовани токени преко више сервиса омогућавају шире ширење напада

**Контроле имплементације:**
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

### **Обрасци безбедног управљања токенима**

**Најбоље праксе:**
- **Краткотрајни токени**: Минимизирати изложеност честом ротацијом токена  
- **Издавање по потреби**: Издавати токене само када су потребни за одређене операције  
- **Сигурно складиштење**: Користити хардверске безбедносне модуле (HSM) или сигурне складишта кључева  
- **Веза токена**: Везати токене за одређене клијенте, сесије или операције кад год је могуће  
- **Надзор и алармирање**: Детекција у реалном времену злоупотребе токена или неовлашћених образаца приступа

## 3. **Контроле безбедности сесија**

### **Спречавање отмице сесије**

**Вектори напада који се решавају:**
- **Убацивање злонамерних догађаја у сесију**: Злонамерни догађаји убацивани у заједничко стање сесије  
- **Имитација сесије**: Неовлашћена употреба украдених ИД-јева сесије за заобилажење аутентификације  
- **Напади наставка стрима**: Искоришћавање наставка догађаја послатих са сервера за убацивање злонамерног садржаја

**Обавезне контроле сесије:**
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

**Безбедност транспорта:**
- **Примена HTTPS-а**: Сва комуникација сесије преко TLS 1.3  
- **Сигурне атрибуте колачића**: HttpOnly, Secure, SameSite=Strict  
- **Пиновање сертификата**: За критичне везе ради спречавања MITM напада

### **Разматрања државних и бездржавних имплементација**

**За државне имплементације:**
- Заједничко стање сесије захтева додатну заштиту од убацивања  
- Управљање сесијом засновано на реду чекања захтева верификацију интегритета  
- Више инстанци сервера захтевају сигурну синхронизацију стања сесије

**За бездржавне имплементације:**
- Управљање сесијом засновано на JWT или сличним токенима  
- Криптографска верификација интегритета стања сесије  
- Смањена површина напада али захтева робусну валидацију токена

## 4. **Контроле безбедности специфичне за вештачку интелигенцију**

### **Одбрана од убацивања упита**

**Интеграција Microsoft Prompt Shields:**
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

**Контроле имплементације:**
- **Санитација уноса**: Свеобухватна валидација и филтрирање свих корисничких уноса  
- **Дефинисање граница садржаја**: Јасна раздвојеност између системских упутстава и корисничког садржаја  
- **Хијерархија упутстава**: Правилна правила првенства за конфликтна упутства  
- **Надзор излаза**: Детекција потенцијално штетних или манипулисаних излаза

### **Спречавање тровања алата**

**Оквир безбедности алата:**
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

**Динамичко управљање алатима:**
- **Радни токови одобрења**: Изричита сагласност корисника за измене алата  
- **Могућности враћања**: Способност повратка на претходне верзије алата  
- **Ревизија измена**: Потпуна историја измена дефиниција алата  
- **Процена ризика**: Аутоматизована процена безбедносног стања алата

## 5. **Спречавање напада конфузног заменика**

### **Безбедност OAuth проксија**

**Контроле спречавања напада:**
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

**Захтеви за имплементацију:**
- **Верификација сагласности корисника**: Никада не прескачите екране сагласности за динамичку регистрацију клијената  
- **Валидација URI за преусмеравање**: Строга валидација одредишта преусмеравања заснована на белој листи  
- **Заштита кода ауторизације**: Краткотрајни кодови са применом једнократне употребе  
- **Верификација идентитета клијента**: Робусна валидација акредитива и метаподатака клијента

## 6. **Безбедност извршавања алата**

### **Изолација и сандбоксинг**

**Изолација заснована на контејнерима:**
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

**Изолација процеса:**
- **Одвојени контексти процеса**: Сваки извршни алат у изолованом процесном простору  
- **Међупроцесна комуникација**: Сигурни IPC механизми са валидацијом  
- **Надзор процеса**: Анализа понашања у току рада и детекција аномалија  
- **Примена ограничења ресурса**: Тврде границе за CPU, меморију и I/O операције

### **Имплементација најмањих привилегија**

**Управљање дозволама:**
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

## 7. **Контроле безбедности ланца снабдевања**

### **Верификација зависности**

**Свеобухватна безбедност компоненти:**
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

### **Континуирани надзор**

**Детекција претњи у ланцу снабдевања:**
- **Надзор здравља зависности**: Континуирана процена свих зависности због безбедносних проблема  
- **Интеграција обавештајних података о претњама**: Ажурирања у реалном времену о новим претњама у ланцу снабдевања  
- **Анализа понашања**: Детекција необичног понашања у спољним компонентама  
- **Аутоматизовани одговор**: Одмахно сузбијање компромитованих компоненти

## 8. **Контроле надзора и детекције**

### **Систем за управљање безбедносним информацијама и догађајима (SIEM)**

**Свеобухватна стратегија евидентирања:**
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

### **Детекција претњи у реалном времену**

**Аналитика понашања:**
- **Аналитика понашања корисника (UBA)**: Детекција необичних образаца приступа корисника  
- **Аналитика понашања ентитета (EBA)**: Надзор понашања MCP сервера и алата  
- **Детекција аномалија машинским учењем**: AI-подржано препознавање безбедносних претњи  
- **Корелација обавештајних података о претњама**: Усклађивање посматраних активности са познатим обрасцима напада

## 9. **Одговор на инциденте и опоравак**

### **Аутоматизоване могућности одговора**

**Одмах предузете мере:**
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

### **Форензичке могућности**

**Подршка истрази:**
- **Чување трага ревизије**: Неменљиво евидентирање са криптографским интегритетом  
- **Прикупљање доказа**: Аутоматизовано прикупљање релевантних безбедносних артефаката  
- **Реконструкција временске линије**: Детаљан низ догађаја који су довели до безбедносних инцидената  
- **Процена утицаја**: Процена обима компромитације и изложености података

## **Кључни принципи безбедносне архитектуре**

### **Одбрана у дубини**
- **Више слојева безбедности**: Нема једне тачке квара у безбедносној архитектури  
- **Резервне контроле**: Преклапајуће мере безбедности за критичне функције  
- **Механизми безбедног понашања**: Сигурне подразумеване вредности када системи наиђу на грешке или нападе

### **Имплементација нултог поверења**
- **Никада не веруј, увек верификуј**: Континуирана валидација свих ентитета и захтева  
- **Принцип најмањих привилегија**: Минимална права приступа за све компоненте  
- **Микро-сегментација**: Грануларне контроле мреже и приступа

### **Континуирана еволуција безбедности**
- **Прилагођавање пејзажу претњи**: Редовна ажурирања за решавање нових претњи  
- **Ефикасност контрола безбедности**: Континуирана процена и унапређење контрола  
- **Усклађеност са спецификацијом**: Усклађеност са развијајућим MCP безбедносним стандардима

---

## **Ресурси за имплементацију**

### **Званична MCP документација**
- [MCP Спецификација (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Најбоље праксе безбедности](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Спецификација ауторизације](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft безбедносна решења**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Безбедносни стандарди**
- [OAuth 2.0 Најбоље праксе безбедности (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Топ 10 за велике језичке моделе](https://genai.owasp.org/)
- [NIST оквир за сајбер безбедност](https://www.nist.gov/cyberframework)

---

> **Важно**: Ове контроле безбедности одражавају тренутну MCP спецификацију (2025-06-18). Увек проверите најновију [званичну документацију](https://spec.modelcontextprotocol.io/) јер се стандарди брзо развијају.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
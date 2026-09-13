# MCP Безбедносне Контроле - Септембар 2026 Ажурирање

> **Тренутни стандард:** Овај документ одражава
> [MCP Спецификацију 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> и званичне
> [MCP Најбоље Безбедносне Практике](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Model Context Protocol (MCP) је значајно напредовао са побољшаним безбедносним контролама које се баве и традиционалном безбедношћу софтвера и претњама специфичним за вештачку интелигенцију. Овај документ пружа свеобухватне безбедносне контроле за безбедне MCP имплементације у складу са OWASP MCP Топ 10 оквиром.

## 🏔️ Практична Безбедносна Обука

За практично искуство у имплементацији безбедности, препоручујемо **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - свеобухватну вођену експедицију у обезбеђивању MCP сервера у Azure користећи методологију "рањив → експлоатисати → поправити → верификовати".

Све безбедносне контроле у овом документу усклађене су са **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, који пружа референтне архитектуре и смернице за имплементацију специфичну за Azure за OWASP MCP Топ 10 ризике.

## **ОБАВЕЗНИ Безбедносни Захтеви**

### **Критичне Забране из MCP Спецификације:**

> **ЗАБРАЊЕНО**: MCP сервери **НЕ СМЕЈУ** прихватати било какве токене који нису експлицитно издати за MCP сервер
>
> **ЗАБРАЊЕНО**: MCP сервери **НЕ СМЕЈУ** користити сесије за аутентификацију  
>
> **ЗАХТЕВАНО**: MCP сервери који имплементирају ауторизацију **ТРЕБА** да верификују СВЕ улазне захтеве
>
> **ОБАВЕЗНО**: MCP прокси сервери који користе статички трећи клијентски ИД
> **ТРЕБА** да добију пристанак за сваког MCP клијента пре прослеђивања ауторизације

---

## 1. **Контроле Аутентификације и Ауторизације**

### **Интеграција Спољног Провајдера Иденитета**

**MCP Спецификација `2026-07-28`** омогућава MCP серверима да делегирају
аутентификацију спољним провајдерима идентитета. Ауторизација за HTTP
трансопрте се процењује по захтеву; локални stdio сервери уместо тога добијају креденцијале
из свог окружења.

**OWASP MCP Ризик који се решава**: [MCP07 - Недовољна аутентификација и ауторизација](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Безбедносне Предности:**
1. **Уклонује Ризике Прилагођене Аутентификације**: Смањује површину рањивости избегавањем прилагођених имплементација аутентификације
2. **Безбедност на нивоу предузећа**: Користи успостављене провајдере идентитета као Microsoft Entra ID са напредним безбедносним функцијама
3. **Централизовано Управљање Идентитетом**: Поједностављује животни циклус корисника, контролу приступа и ревизију усаглашености
4. **Вишефакторска Аутентификација**: Наслеђује MFA могућности од провајдера иденитета предузећа
5. **Политике Условног Приступа**: Користи контроле приступа засноване на ризику и адаптивну аутентификацију

**Захтеви за Имплементацију:**
- **Регистрација Клијента**: Преферирати Клијентске ID Метадате Документе или
  претходну регистрацију; користити застарелу Динамичку Регистрацију Клијената само за
  компатибилност
- **Валидација Циљне Аудиторије Токена**: Потврдити да су сви токени експлицитно издати за MCP сервер
- **Провера Издаваоца**: Верификовати да издаваоц токена одговара очекиваном провајдеру идентитета
- **Провера Потписа**: Криптографска верификација интегритета токена
- **Примена Рока Важења**: Строга примена ограничења трајања токена
- **Провера Опсега**: Осигурати да токени садрже одговарајуће дозволе за тражене операције

### **Безбедност Логике Ауторизације**

**Критичне Контроле:**
- **Свеобухватни Аудити Ауторизације**: Редовни безбедносни прегледи свих тачака одлучивања ауторизације
- **Задате Вредности Безбедносног Фалирања**: Одбиј приступ када логика ауторизације не може донети дефинитивну одлуку
- **Границе Дозвола**: Јасна подела између различитих нивоа привилегија и приступа ресурсима
- **Аудит Логовање**: Комплетно бележење свих одлука ауторизације за безбедносно праћење
- **Редовни Прегледи Приступа**: Перiodично валидација корисничких дозвола и додела привилегија

## 2. **Безбедност Токена и Анти-Прослеђивање Контроле**

**OWASP MCP Ризик који се решава**: [MCP01 - Неправилно управљање токенима и откривање тајни](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Превенција Прослеђивања Токена**

**Прослеђивање токена је експлицитно забрањено** у MCP Спецификацији за Ауторизацију због критичних безбедносних ризика:

**Ризици Безбедности који се решавају:**
- **Заобилажење Контрола**: Прелази преко кључних безбедносних контрола као што су ограничење брзине, валидација захтева и праћење саобраћаја
- **Разбијање Одговорности**: Омогућава немогућност идентификације клијента, квари ревизијске записе и истраге инцидената
- **Експлоатација преко проксија**: Олакшава злоумљатељима да користе сервере као прокси за неовлашћени приступ подацима
- **Прекид Услова Поверења**: Крши претпоставке о пореклу токена у услужним системима у низу
- **Латерални Премештај**: Компромитовани токени између више услуга омогућавају шире ширење напада

**Контроле Имплементације:**
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

### **Обрасци за Безбедно Управљање Токеном**

**Најбоље Практике:**
- **Токени са Кратким Веклом**: Минимизирати експозицију учесталим ротирањем токена
- **Издавање По Потреби**: Издавати токене само када су потребни за одређене операције
- **Безбедно Складиштење**: Користити хардверске безбедносне модуле (HSM) или безбедне кључне ковчеге
- **Везивање Токена**: Верификовати публику и издаваоца токена за намењени MCP
  ресурс, клијента и операцију
- **Праћење и Алармирање**: Детекција злоупотребе токена или неовлашћених приступа у реалном времену

## 3. **Контроле Безбедности Стања Апликације**

### **Превенција Отмице држача стања**

**Вектори Напада који се решавају:**
- **Погађањедржача**: Прогнозиви идентификатори излажу стање другог позиваоца
- **Преклапајућа употреба између корисника**: Украдени држач се користи са другом личношћу
- **Имишљена Ауторизација**: Поседовање држача се погрешно третира као
  доказ приступа

**Контроле држача стања:**

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

**Безбедност Транспорта:**
- **Примена HTTPS**: Захтева HTTPS за удаљене HTTP транспорте
- **Руковање Креденцијалима**: Слање и валидација ауторизације по сваком HTTP захтеву
- **Изолација stdio**: Заштита локалних stdio сервера кроз изолацију процеса и
  контролу креденцијала окружења

### **Разматрања о стању и без стања**

MCP `2026-07-28` је без стања на нивоу протокола. Апликације ипак могу
одржавати стање враћајући експлицитни држач из једног позива алата и прихватајући
га као обичан аргумент у каснијим позивима.

- Чувајте стање независно од било које транспортне везе.
- Везујте држаче стања за аутентификованог главног сервера.
- Третирајте држач као име, а не као носиоца креденцијала.
- Дефинишите понашање истека и опоравка за застареле држаче.

## 4. **Безбедносне Контроле Специфичне за Вештачку Интелигенцију**

**OWASP MCP Ризици који се решавају**:

- [MCP06 - Субверзија тока намера](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Отровање алата](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Убацивање и извршавање команди](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Одбрана од убацивања у захтеве**

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
- **Хијерархија упутстава**: Правилно одређивање претходности за конфликтна упутства
- **Надзор излаза**: Детекција потенцијално штетних или манипулисаних излаза

### **Превенција отровања алата**

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
- **Радни токови одобрења**: Јасан кориснички пристанак за измене алата
- **Могућности повратка**: Способност враћања на претходне верзије алата
- **Ревизија измена**: Комплетна историја измена дефиниција алата
- **Процена ризика**: Аутоматизована процена стања безбедности алата

## 5. **Превенција напада конфузног повереника**

### **Сигурност OAuth проксија**

**Контроле превенције напада:**
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

**Захтеви за имплементацију:**
- **Регистрација клијената**: Предност дајте претходној регистрацији или метаподацима Client ID-а
  докумената; третирајте динамичку регистрацију клијената као опцију ускомпатибилности
- **Провера корисничког пристанка**: MCP проксији користе статички ID треће стране клијента
  и морају добити пристанак по клијенту пре прослеђивања ауторизације
- **Валидација Redirect URI**: Строга валидација на бази беле листе одредишта преусмеравања
- **Заштита ауторизационих кодова**: Краткотрајни кодови са применом једнократне употребе
- **Верификација идентитета клијента**: Робусна провера акредитива и метаподатака клијената

## 6. **Сигурност извршавања алата**

### **Изолација и окружење за извршавање**

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
- **Одвојени контексти процеса**: Сваки алат се извршава у изолованом процесном простору
- **Међупроцесна комуникација**: Безбедни IPC механизми са валидацијом
- **Надзор процеса**: Анализа понашања у раду и детекција аномалија
- **Спровођење ресурса**: Строга ограничења на CPU, меморију и I/O операције

### **Примена принципа најмањих привилегија**

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

**Ризик OWASP MCP-а који се решава**: [MCP04 - Напади на ланац снабдевања софтвером и манипулације зависностима](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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
- **Надзор здравља зависности**: Континуирана процена свих зависности у погледу безбедносних проблема
- **Интеграција интелигенције о претњама**: Ажурирања у реалном времену о новим претњама у ланцу снабдевања
- **Понашајна анализа**: Детекција неуобичајеног понашања у спољним компонентама
- **Аутоматизовани одговор**: Одмаховање компромитованих компоненти

## 8. **Контроле надзора и детекције**

**Ризик OWASP MCP-а који се решава**: [MCP08 - Недостатак ревизије и телеметрије](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Систем управљања безбедносним информацијама и догађајима (SIEM)**

**Свеобухватна стратегија логовања:**
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

**Понашајна аналитика:**
- **Аналитика корисничког понашања (UBA)**: Детекција необичних образаца корисничког приступа
- **Аналитика понашања ентитета (EBA)**: Надзор понашања MCP сервера и алата
- **Детекција аномалија машинским учењем**: Идентификација безбедносних претњи уз помоћ вештачке интелигенције
- **Корелација са претходним знањем о претњама**: Усклађивање посматраних активности са познатим шаблонима напада

## 9. **Одговор на инциденте и опоравак**

### **Аутоматизоване могућности реаговања**

**Акције тренутног одговора:**
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
- **Чување стазе ревизије**: Неменољиво логовање са криптографским интегритетом
- **Прикупљање доказа**: Аутоматизовано прикупљање релевантних безбедносних артефаката
- **Реконструкција временске линије**: Детаљан низ догађаја који воде до безбедносних инцидената
- **Процена утицаја**: Процена обима компромиса и изложености података

## **Кључни принципи архитектуре безбедности**

### **Одбрана у дубини**
- **Више слојева безбедности**: Није дозвољена појединачна тачка квара у архитектури безбедности
- **Редундантне контроле**: Преклапајуће мере безбедности за критичне функције
- **Механизми који спречавају квар**: Безбедне подразумеване вредности у случају грешака или напада

### **Примена Zero Trust-а**
- **Никад не веруј, увек верификуј**: Континуирана валидација свих ентитета и захтева
- **Принцип најмањих привилегија**: Минимална права приступа за све компоненте
- **Микроподела**: Грануларне контроле мреже и приступа

### **Континуирана еволуција безбедности**
- **Прилагођавање пејзажу претњи**: Редовна ажурирања за решавање нових претњи
- **Ефикасност безбедносних контрола**: Континуирана процена и унапређење контрола
- **Усклађеност са спецификацијом**: Усклађеност са еволуирајућим MCP безбедносним стандардима

---

## **Ресурси за имплементацију**

### **Званична MCP документација**
- [MCP спецификација (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Најбоље безбедносне праксе MCP-а](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP спецификација ауторизације](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP безбедносни ресурси**
- [OWASP MCP Azure водич за безбедност](https://microsoft.github.io/mcp-azure-security-guide/) - Свеобухватни OWASP MCP Top 10 са Azure имплементацијом
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Званични OWASP MCP безбедносни ризици
- [MCP Security Summit радионица (Sherpa)](https://azure-samples.github.io/sherpa/) - Практична обука о безбедности MCP-а на Azure

### **Microsoft безбедносна решења**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Стандарди безбедности**
- [Најбоље праксе OAuth 2.0 безбедности (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Топ 10 за велике језичке моделе](https://genai.owasp.org/)

- [NIST Okvir sajber bezbednosti](https://www.nist.gov/cyberframework)

---

> **Важно:** Ове контроле безбедности одражавају MCP спецификацију
> `2026-07-28`. Увек проверите са
> [тренутном службеном документацијом](https://modelcontextprotocol.io/specification/2026-07-28/)
> јер се стандарди настављају развијати.

## Шта следи

- Вратите се на: [Преглед безбедносног модула](./README.md)
- Наставите са: [Модул 3: Почетак рада](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
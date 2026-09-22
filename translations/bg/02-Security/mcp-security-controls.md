# MCP Контрол на сигурността - Актуализация септември 2026 г.

> **Текущ стандарт:** Този документ отразява
> [MCP Спецификация 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> и официалния
> [MCP Най-добри практики за сигурност](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Протоколът за контекст на модела (MCP) значително се усъвършенства с подобрени контролни мерки за сигурност, които обхващат както традиционната софтуерна сигурност, така и специфичните заплахи за ИИ. Този документ предоставя цялостни контролни мерки за сигурност за сигурни реализации на MCP, съобразени с рамката OWASP MCP Top 10.

## 🏔️ Практическо обучение по сигурност

За практически опит в прилагането на сигурност препоръчваме **[Работилница MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - изчерпателна ръководена експедиция за защита на MCP сървъри в Azure, използваща методологията "уязвимост → експлоатация → корекция → валидация".

Всички контролни мерки за сигурност в този документ са съгласувани с **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, който предоставя референтни архитектури и указания за реализация в Azure за рисковете от OWASP MCP Top 10.

## **ЗАДЪЛЖИТЕЛНИ изисквания за сигурност**

### **Критични забрани от MCP Спецификацията:**

> **ЗАБРАНЕНО**: MCP сървърите **НЕ ТРЯБВА** да приемат никакви токени, които не са изрично издадени за MCP сървъра
>
> **ЗАБРАНЕНО**: MCP сървърите **НЕ ТРЯБВА** да използват сесии за удостоверяване  
>
> **ИЗИСКВА СЕ**: MCP сървърите, които изпълняват упълномощаване, **ТРЯБВА** да проверяват ВСИЧКИ входящи заявки
>
> **ЗАДЪЛЖИТЕЛНО**: MCP прокси сървърите, използващи статичен външен клиентски идентификатор,  
> **ТРЯБВА** да получават съгласие за всеки MCP клиент преди пренасочване на упълномощаването

---

## 1. **Контроли за удостоверяване и упълномощаване**

### **Интеграция с външен доставчик на идентичност**

**MCP Спецификация `2026-07-28`** позволява на MCP сървърите да делегират
удостоверяването на външни доставчици на идентичност. Упълномощаването за HTTP
транспорта се оценява за всяка заявка; локалните stdio сървъри получават
удостоверителни данни от своята среда.

**Риск OWASP MCP, адресиран**: [MCP07 - Недостатъчно удостоверяване и упълномощаване](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Ползи за сигурността:**
1. **Премахване на рискове от персонализирано удостоверяване**: Намалява повърхността на уязвимост чрез избягване на персонализирани реализации на удостоверяване
2. **Сигурност на корпоративно ниво**: Използва утвърдени доставчици на идентичност като Microsoft Entra ID с усъвършенствани функции за сигурност
3. **Централизирано управление на идентичността**: Опрощава управлението на жизнения цикъл на потребителя, контрола на достъпа и одита на съответствието
4. **Многофакторно удостоверяване**: Наследява възможностите за MFA от корпоративните доставчици на идентичност
5. **Политики за условен достъп**: Възползва се от контрол на достъпа, базиран на риск, и адаптивно удостоверяване

**Изисквания за реализация:**
- **Регистрация на клиент**: Предпочитайте клиентски метаданни или
  предварителна регистрация; използвайте остарялата динамична клиентска регистрация само за
  съвместимост
- **Проверка на аудитория на токена**: Проверявайте дали всички токени са изрично издадени за MCP сървъра
- **Валидация на издател**: Валидирайте, че издателят на токена съответства на очаквания доставчик на идентичност
- **Валидация на подпис**: Криптографска валидация на цялостността на токена
- **Налагане на изтичане**: Строго прилагане на ограниченията за времето на валидност на токена
- **Валидация на обхват**: Уверете се, че токените съдържат подходящи права за поискани операции

### **Сигурност на логиката за упълномощаване**


**Критични Контроли:**
- **Пълни одити на оторизацията**: Редовни прегледи на всички точки за вземане на решения за оторизация
- **Безопасни по подразбиране**: Отказ на достъп, когато логиката за оторизация не може да вземе категорично решение
- **Граници на разрешения**: Ясно разделяне между различни нива на привилегии и достъпа до ресурси
- **Одитно логиране**: Пълно логиране на всички решения за оторизация за мониторинг на сигурността
- **Редовни прегледи на достъпа**: Периодична валидация на потребителските разрешения и присвоявания на привилегии

## 2. **Сигурност на токените и контроли срещу минаване на токени**

**Риск на OWASP MCP, който се адресира**: [MCP01 - Проблеми с управлението на токени и изтичане на тайни](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Предотвратяване на минаване на токени**

**Минаването на токени е изрично забранено** в Спецификацията за оторизация на MCP поради критичните рискове за сигурността:

**Адресирани рискове за сигурността:**
- **Заобикаляне на контроли**: Прескача основни контролни механизми като ограничаване на честотата, валидация на заявки и мониторинг на трафика
- **Разрушаване на отговорността**: Прави невъзможна идентификацията на клиента, разваляйки одитните следи и разследването на инциденти
- **Експлоатация чрез прокси**: Позволява на злонамерени актьори да използват сървъри като проксита за неоторизиран достъп до данни
- **Нарушения на границите на доверие**: Нарушава предположенията на downstream услугите за произхода на токена
- **Странично движение**: Откраднати токени в множество услуги позволяват по-широко разширение на атаките

**Контроли за изпълнение:**
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

### **Патерни за сигурно управление на токени**

**Най-добри практики:**
- **Краткотрайни токени**: Минимизиране на прозореца на излагане с честа ротация на токените
- **Издаване на токени точно навреме**: Издаване на токени само при необходимост за конкретни операции
- **Сигурно съхранение**: Използване на хардуерни модули за сигурност (HSM) или защитени хранилища за ключове
- **Свързване на токени**: Валидация на аудиторията и издателя на токена за съответния MCP
  ресурс, клиент и операция
- **Мониторинг и алармиране**: Откриване в реално време на злоупотреба с токени или неоторизирани модели на достъп

## 3. **Контроли за сигурност на състоянието на приложението**

### **Предотвратяване на отвличане на държава (state handle hijacking)**

**Адресирани вектори на атаки:**
- **Познати идентификатори**: Прогнозируеми идентификатори излагат състояние на друг потребител
- **Пренасочване между потребители**: Откраднат хендъл се използва с различна самоличност
- **Имплицитна оторизация**: Притежаването на хендъл се третира неправилно като
  доказателство за достъп

**Контроли върху хендъла на състоянието:**

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

**Сигурност на трансфера:**
- **Налагане на HTTPS**: Изисквайте HTTPS за отдалечени HTTP трансфери
- **Работа с идентификационни данни**: Изпращайте и валидирайте оторизация при всяка HTTP заявка
- **Изолация на stdio**: Защитете локални stdio сървъри чрез изолация на процеси и
  контрол върху идентификационните данни на средата

### **Разглеждане на stateful срещу stateless**

MCP `2026-07-28` е stateless на протоколната си прослойка. Въпреки това приложенията могат да
поддържат състояние чрез връщане на явен хендъл от един инструментален повик и приемането му като обикновен аргумент при по-късни повици.


- Съхранявайте състоянието независимо от каквато и да е транспортна връзка.
- Свържете state handle-ите със серверно удостоверения основен принцип.
- Третирайте хендъла като име, а не като носещ идентификационни данни.
- Дефинирайте поведение за изтичане на валидността и възстановяване за остарели хендъли.

## 4. **Специфични контроли за сигурност за ИИ**

**Адресирани рискове на OWASP MCP**:

- [MCP06 - Подкопаване на потока на намерението](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Отравяне на инструмент](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Инжектиране и изпълнение на команди](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

### **Защита срещу инжектиране на заявки**

**Интеграция на Microsoft Prompt Shields:**
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

**Контроли за внедряване:**
- **Санитизация на входните данни**: Изчерпателна проверка и филтриране на всички потребителски данни
- **Определяне на границите на съдържанието**: Ясно разделяне между системни инструкции и съдържание от потребителя
- **Йерархия на инструкциите**: Подходящи правила за предимство при конфликтни инструкции
- **Мониторинг на изходните данни**: Откриване на потенциално вредни или манипулирани изходни данни

### **Предотвратяване на отравяне на инструменти**

**Рамка за сигурност на инструментите:**
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

**Динамично управление на инструментите:**
- **Работни потоци за одобрение**: Ясно съгласие от потребителя за промени в инструментите
- **Възможност за връщане назад**: Възможност за връщане към предишни версии на инструментите
- **Одит на промените**: Пълна история на промени в дефинициите на инструментите
- **Оценка на риска**: Автоматизирана оценка на сигурността на инструментите

## 5. **Предотвратяване на атака от объркан представител**

### **Сигурност на OAuth прокси**

**Контроли за предотвратяване на атаки:**
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

**Изисквания за внедряване:**
- **Регистрация на клиент**: Предпочитано е предварителна регистрация или метаданни за клиентски идентификатор
  документи; третирайте динамичната регистрация на клиента като съвместимост по подразбиране
- **Проверка на потребителското съгласие**: MCP проксита, използващи статичен клиентски идентификатор на трета страна,
  трябва да получат съгласие от всеки клиент преди препращане на разрешението
- **Валидиране на URI за пренасочване**: Строга проверка на бели списъци на дестинациите за пренасочване
- **Защита на кода за разрешение**: Краткотрайни кодове с налагане на еднократна употреба
- **Проверка на идентичността на клиента**: Здрава проверка на клиентски креденциали и метаданни

## 6. **Сигурност при изпълнение на инструменти**

### **Пясъчник и изолация**

**Изолация на база контейнери:**
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

**Изолация на процеси:**
- **Отделни контексти на процеса**: Всяко изпълнение на инструмент в изолиран процесен обхват
- **Междупроцесна комуникация**: Сигурни IPC механизми с валидиране
- **Мониторинг на процеса**: Анализ на поведението по време на изпълнение и откриване на аномалии
- **Налагане на ресурси**: Строги лимити на CPU, памет и операции с I/O

### **Прилагане на принципа за най-малко привилегии**

**Управление на разрешенията:**
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

## 7. **Контроли за сигурност на веригата на доставки**

**Адресиран OWASP MCP риск**: [MCP04 - Атаки върху софтуерната верига на доставки и манипулиране на зависимости](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

### **Проверка на зависимостите**

**Изчерпателна сигурност на компонентите:**
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

### **Непрекъснат мониторинг**

**Откриване на заплахи във веригата на доставки:**
- **Мониторинг на здравето на зависимостите**: Непрекъсната оценка на всички зависимости за проблеми със сигурността
- **Интеграция на разузнаване за заплахи**: Актуализации в реално време за нововъзникващи заплахи във веригата на доставки
- **Анализ на поведението**: Откриване на необичайно поведение в външните компоненти
- **Автоматизирано реагиране**: Незабавно ограничаване на компрометирани компоненти

## 8. **Контроли за мониторинг и откриване**

**Адресиран OWASP MCP риск**: [MCP08 - Липса на одит и телеметрия](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Управление на информацията за сигурност и събития (SIEM)**

**Изчерпателна стратегия за записване на събития:**
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

### **Откриване на заплахи в реално време**

**Анализ на поведението:**
- **Анализ на поведението на потребителя (UBA)**: Откриване на необичайни модели на достъп на потребителя
- **Анализ на поведението на обекта (EBA)**: Мониторинг на поведението на MCP сървъра и инструменти
- **Откриване на аномалии чрез машинно обучение**: AI-управлявано идентифициране на заплахи за сигурността
- **Корелация с разузнаване за заплахи**: Съвпадение на наблюдавани дейности с известни модели на атаки

## 9. **Реагиране при инциденти и възстановяване**

### **Автоматизирани възможности за реагиране**

**Незабавни действия при реагиране:**
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

### **Възможности за криминалистика**

**Поддръжка на разследвания:**
- **Запазване на одиторски следи**: Непроменимо записване с криптографска цялост
- **Събиране на доказателства**: Автоматизирано събиране на релевантни артефакти за сигурност
- **Възстановяване на времева линия**: Подробна последователност на събитията, довели до инциденти със сигурността
- **Оценка на въздействието**: Оценка на обхвата на компрометиране и излагане на данни

## **Основни принципи при архитектурата на сигурността**

### **Защита в дълбочина**
- **Множество слоеве сигурност**: Няма единична точка на провал в архитектурата на сигурността
- **Резервни контроли**: Припокриващи се мерки за сигурност за критични функции
- **Механизми за защитен отказ**: Сигурни настройки по подразбиране при грешки или атаки в системите

### **Прилагане на Zero Trust**
- **Никога не вярвай, винаги проверявай**: Постоянна верификация на всички субекти и заявки
- **Принцип на най-малко привилегии**: Минимални права за достъп за всички компоненти
- **Микро-сегментация**: Грануларни мрежови и достъпни контроли

### **Постоянна еволюция на сигурността**
- **Адаптация към пейзажа на заплахите**: Редовни актуализации за справяне с нововъзникващи заплахи
- **Ефективност на контрола на сигурността**: Непрекъсната оценка и подобрение на контролите
- **Спазване на спецификациите**: Съответствие с развиващите се MCP стандарти за сигурност

---

## **Ресурси за внедряване**

### **Официална документация на MCP**
- [MCP Спецификация (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Най-добри практики за сигурност](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Спецификация за разрешения](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP ресурси за сигурност**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Изчерпателен OWASP MCP Top 10 с внедряване в Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Официални рискове за сигурност на OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Практическо обучение по сигурност за MCP в Azure

### **Microsoft решения за сигурност**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Стандарти за сигурност**
- [Най-добри практики за сигурност на OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)

- [OWASP Топ 10 за Големи Езикови Модели](https://genai.owasp.org/)

- [Рамка за киберсигурност на NIST](https://www.nist.gov/cyberframework)

---

> **Важно:** Тези мерки за сигурност отразяват MCP Спецификация
> `2026-07-28`. Винаги проверявайте спрямо
> [актуалната официална документация](https://modelcontextprotocol.io/specification/2026-07-28/)
> тъй като стандартите продължават да се развиват.

## Какво следва

- Върнете се към: [Преглед на модула за сигурност](./README.md)
- Продължете към: [Модул 3: Започване](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
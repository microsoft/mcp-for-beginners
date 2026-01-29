# MCP Контрол на сигурността - Актуализация декември 2025

> **Текущ стандарт**: Този документ отразява изискванията за сигурност на [MCP Спецификация 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) и официалните [MCP Най-добри практики за сигурност](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Протоколът за контекст на модела (MCP) е значително усъвършенстван с подобрени контроли за сигурност, които адресират както традиционната софтуерна сигурност, така и специфичните за ИИ заплахи. Този документ предоставя изчерпателни контроли за сигурност за сигурни реализации на MCP към декември 2025.

## **ЗАДЪЛЖИТЕЛНИ изисквания за сигурност**

### **Критични забрани от MCP Спецификацията:**

> **ЗАБРАНЕНО**: MCP сървърите **НЕ ТРЯБВА** да приемат никакви токени, които не са изрично издадени за MCP сървъра  
>
> **ЗАБРАНЕНО**: MCP сървърите **НЕ ТРЯБВА** да използват сесии за удостоверяване  
>
> **ИЗИСКВА СЕ**: MCP сървърите, които прилагат авторизация, **ТРЯБВА** да проверяват ВСИЧКИ входящи заявки  
>
> **ЗАДЪЛЖИТЕЛНО**: MCP прокси сървърите, използващи статични клиентски идентификатори, **ТРЯБВА** да получават съгласие от потребителя за всеки динамично регистриран клиент

---

## 1. **Контроли за удостоверяване и авторизация**

### **Интеграция с външен доставчик на идентичност**

**Текущ MCP стандарт (2025-06-18)** позволява на MCP сървърите да делегират удостоверяването на външни доставчици на идентичност, което представлява значително подобрение в сигурността:

### **Интеграция с външен доставчик на идентичност**

**Текущ MCP стандарт (2025-11-25)** позволява на MCP сървърите да делегират удостоверяването на външни доставчици на идентичност, което представлява значително подобрение в сигурността:

**Ползи за сигурността:**
1. **Премахва рисковете от персонализирано удостоверяване**: Намалява повърхността на уязвимост, като избягва персонализирани реализации на удостоверяване  
2. **Сигурност на корпоративно ниво**: Използва утвърдени доставчици на идентичност като Microsoft Entra ID с усъвършенствани функции за сигурност  
3. **Централизирано управление на идентичността**: Опрощава управлението на жизнения цикъл на потребителите, контрола на достъпа и одита за съответствие  
4. **Многофакторно удостоверяване**: Наследява възможностите за МФА от корпоративните доставчици на идентичност  
5. **Политики за условен достъп**: Възползва се от контрол на достъпа, базиран на риска, и адаптивно удостоверяване

**Изисквания за изпълнение:**
- **Проверка на аудиторията на токена**: Проверете всички токени, че са изрично издадени за MCP сървъра  
- **Проверка на издателя**: Валидирайте, че издателят на токена съвпада с очаквания доставчик на идентичност  
- **Проверка на подписа**: Криптографска валидация на целостта на токена  
- **Прилагане на срок на валидност**: Строго прилагане на ограниченията за живот на токена  
- **Проверка на обхвата**: Уверете се, че токените съдържат подходящи разрешения за заявените операции

### **Сигурност на логиката за авторизация**

**Критични контроли:**
- **Изчерпателни одити на авторизацията**: Редовни прегледи на сигурността на всички точки за вземане на решения за авторизация  
- **Безопасни по подразбиране**: Отказ на достъп, когато логиката за авторизация не може да вземе категорично решение  
- **Граници на разрешенията**: Ясно разделяне между различните нива на привилегии и достъп до ресурси  
- **Логване на одита**: Пълно регистриране на всички решения за авторизация за мониторинг на сигурността  
- **Редовни прегледи на достъпа**: Периодична валидация на потребителските разрешения и разпределения на привилегии

## 2. **Сигурност на токените и контроли срещу пропускане на токени**

### **Предотвратяване на пропускане на токени**

**Пропускането на токени е изрично забранено** в MCP Спецификацията за авторизация поради критични рискове за сигурността:

**Адресирани рискове за сигурността:**
- **Заобикаляне на контроли**: Пропуска основни контроли за сигурност като ограничаване на честотата, валидация на заявки и мониторинг на трафика  
- **Нарушаване на отчетността**: Прави невъзможна идентификацията на клиента, което компрометира одитните следи и разследването на инциденти  
- **Изтичане чрез прокси**: Позволява на злонамерени лица да използват сървъри като проксита за неоторизиран достъп до данни  
- **Нарушаване на границите на доверие**: Нарушава предположенията за доверие на downstream услугите относно произхода на токените  
- **Латерално движение**: Компрометирани токени в множество услуги позволяват по-широко разпространение на атаката

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
- **Краткотрайни токени**: Минимизиране на времето на излагане чрез честа ротация на токените  
- **Издаване точно навреме**: Издаване на токени само когато са необходими за конкретни операции  
- **Сигурно съхранение**: Използване на хардуерни модули за сигурност (HSM) или сигурни хранилища за ключове  
- **Свързване на токени**: Свързване на токените с конкретни клиенти, сесии или операции, когато е възможно  
- **Мониторинг и алармиране**: Откриване в реално време на злоупотреба с токени или неоторизирани модели на достъп

## 3. **Контроли за сигурност на сесиите**

### **Предотвратяване на отвличане на сесии**

**Адресирани вектори на атака:**
- **Инжектиране на злонамерени събития в сесията**: Злонамерени събития, инжектирани в споделеното състояние на сесията  
- **Имперсонация на сесия**: Неоторизирана употреба на откраднати идентификатори на сесии за заобикаляне на удостоверяването  
- **Атаки с възобновяване на потоци**: Използване на възобновяване на събития, изпратени от сървъра, за инжектиране на злонамерено съдържание

**Задължителни контроли за сесии:**
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

**Сигурност на транспорта:**
- **Прилагане на HTTPS**: Цялата комуникация на сесията да е през TLS 1.3  
- **Сигурни атрибути на бисквитките**: HttpOnly, Secure, SameSite=Strict  
- **Закотвяне на сертификати**: За критични връзки с цел предотвратяване на MITM атаки

### **Съображения за състояние на сесията**

**За реализации със състояние:**
- Споделеното състояние на сесията изисква допълнителна защита срещу инжекционни атаки  
- Управлението на сесии чрез опашки изисква проверка на целостта  
- Множество сървърни инстанции изискват сигурна синхронизация на състоянието на сесията

**За реализации без състояние:**
- Управление на сесии чрез JWT или подобни токени  
- Криптографска проверка на целостта на състоянието на сесията  
- Намалена повърхност на атака, но изисква здрава валидация на токените

## 4. **Специфични контроли за сигурност на ИИ**

### **Защита срещу инжектиране на подсказки**

**Интеграция с Microsoft Prompt Shields:**
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

**Контроли за изпълнение:**
- **Санитизация на входа**: Изчерпателна валидация и филтриране на всички потребителски входове  
- **Определяне на граници на съдържанието**: Ясно разделяне между системни инструкции и потребителско съдържание  
- **Йерархия на инструкциите**: Правилни правила за приоритет при конфликтни инструкции  
- **Мониторинг на изхода**: Откриване на потенциално вредни или манипулирани изходи

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
- **Работни потоци за одобрение**: Изрично съгласие на потребителя за модификации на инструментите  
- **Възможности за връщане назад**: Възможност за връщане към предишни версии на инструментите  
- **Одит на промените**: Пълна история на модификациите на дефинициите на инструментите  
- **Оценка на риска**: Автоматизирана оценка на сигурността на инструментите

## 5. **Предотвратяване на атаки тип "объркан заместник"**

### **Сигурност на OAuth прокси**

**Контроли за предотвратяване на атаки:**
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

**Изисквания за изпълнение:**
- **Проверка на съгласието на потребителя**: Никога не пропускайте екрани за съгласие при динамична регистрация на клиенти  
- **Валидация на Redirect URI**: Строга валидация на дестинациите за пренасочване на база бяла листа  
- **Защита на кода за авторизация**: Краткотрайни кодове с прилагане на еднократна употреба  
- **Проверка на идентичността на клиента**: Здрава валидация на клиентските идентификационни данни и метаданни

## 6. **Сигурност при изпълнение на инструменти**

### **Пясъчник и изолация**

**Изолация на базата на контейнери:**
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
- **Отделни контексти на процесите**: Всяко изпълнение на инструмент в изолиран процес  
- **Междупроцесна комуникация**: Сигурни IPC механизми с валидация  
- **Мониторинг на процесите**: Анализ на поведението по време на изпълнение и откриване на аномалии  
- **Прилагане на ресурси**: Строги лимити на CPU, памет и I/O операции

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

### **Проверка на зависимости**

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
- **Анализ на поведението**: Откриване на необичайно поведение в външни компоненти  
- **Автоматизиран отговор**: Незабавно ограничаване на компрометирани компоненти

## 8. **Контроли за мониторинг и откриване**

### **Система за управление на информацията и събитията за сигурност (SIEM)**

**Изчерпателна стратегия за логване:**
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
- **Анализ на поведението на потребителите (UBA)**: Откриване на необичайни модели на достъп на потребителите  
- **Анализ на поведението на обекти (EBA)**: Мониторинг на поведението на MCP сървъра и инструментите  
- **Откриване на аномалии с машинно обучение**: ИИ-базирано идентифициране на заплахи за сигурността  
- **Корелация с разузнаване за заплахи**: Съпоставяне на наблюдаваните дейности с известни модели на атаки

## 9. **Отговор при инциденти и възстановяване**

### **Автоматизирани възможности за отговор**

**Незабавни действия при отговор:**
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
- **Запазване на одитни следи**: Непроменяемо логване с криптографска цялост  
- **Събиране на доказателства**: Автоматизирано събиране на релевантни артефакти за сигурността  
- **Възстановяване на хронологията**: Подробна последователност на събитията, довели до инциденти със сигурността  
- **Оценка на въздействието**: Оценка на обхвата на компрометиране и излагане на данни

## **Ключови принципи на архитектурата за сигурност**

### **Защита в дълбочина**
- **Множество слоеве на сигурност**: Няма единична точка на провал в архитектурата за сигурност  
- **Излишни контроли**: Наслагване на мерки за сигурност за критични функции  
- **Механизми за безопасност**: Сигурни настройки по подразбиране при грешки или атаки

### **Прилагане на Zero Trust**
- **Никога не се доверявай, винаги проверявай**: Непрекъсната валидация на всички субекти и заявки  
- **Принцип на най-малко привилегии**: Минимални права за достъп за всички компоненти  
- **Микро-сегментация**: Гранулирани мрежови и контрол на достъпа

### **Непрекъсната еволюция на сигурността**
- **Адаптация към пейзажа на заплахите**: Редовни актуализации за адресиране на нововъзникващи заплахи  
- **Ефективност на контролите за сигурност**: Постоянна оценка и подобрение на контролите  
- **Съответствие със спецификациите**: Съгласуваност с развиващите се MCP стандарти за сигурност

---

## **Ресурси за изпълнение**

### **Официална MCP документация**
- [MCP Спецификация (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Най-добри практики за сигурност](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Спецификация за авторизация](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft решения за сигурност**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Стандарти за сигурност**
- [OAuth 2.0 Най-добри практики за сигурност (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Топ 10 за големи езикови модели](https://genai.owasp.org/)
- [NIST Киберсигурност рамка](https://www.nist.gov/cyberframework)

---

> **Важно**: Тези контроли за сигурност отразяват текущата MCP спецификация (2025-06-18). Винаги проверявайте спрямо най-новата [официална документация](https://spec.modelcontextprotocol.io/), тъй като стандартите се развиват бързо.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
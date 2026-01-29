# Контроль безпеки MCP - оновлення грудня 2025 року

> **Поточний стандарт**: Цей документ відображає вимоги безпеки [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) та офіційні [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Протокол контексту моделі (MCP) значно вдосконалився з розширеними заходами безпеки, що охоплюють як традиційну безпеку програмного забезпечення, так і специфічні загрози ШІ. Цей документ надає комплексні заходи безпеки для безпечних реалізацій MCP станом на грудень 2025 року.

## **ОБОВ’ЯЗКОВІ вимоги безпеки**

### **Критичні заборони з MCP Specification:**

> **ЗАБОРОНЕНО**: Сервери MCP **НЕ ПОВИННІ** приймати будь-які токени, які не були явно видані для сервера MCP  
>
> **ЗАБОРОНЕНО**: Сервери MCP **НЕ ПОВИННІ** використовувати сесії для автентифікації  
>
> **ПОТРІБНО**: Сервери MCP, що реалізують авторизацію, **ПОВИННІ** перевіряти ВСІ вхідні запити  
>
> **ОБОВ’ЯЗКОВО**: Проксі-сервери MCP, що використовують статичні ідентифікатори клієнтів, **ПОВИННІ** отримувати згоду користувача для кожного динамічно зареєстрованого клієнта

---

## 1. **Контроль автентифікації та авторизації**

### **Інтеграція зовнішніх провайдерів ідентичності**

**Поточний стандарт MCP (2025-06-18)** дозволяє серверам MCP делегувати автентифікацію зовнішнім провайдерам ідентичності, що є значним покращенням безпеки:

### **Інтеграція зовнішніх провайдерів ідентичності**

**Поточний стандарт MCP (2025-11-25)** дозволяє серверам MCP делегувати автентифікацію зовнішнім провайдерам ідентичності, що є значним покращенням безпеки:

**Переваги безпеки:**
1. **Усунення ризиків власної автентифікації**: Зменшує вразливість, уникаючи власних реалізацій автентифікації  
2. **Безпека корпоративного рівня**: Використання перевірених провайдерів ідентичності, таких як Microsoft Entra ID, з розширеними функціями безпеки  
3. **Централізоване управління ідентичністю**: Спрощує управління життєвим циклом користувачів, контроль доступу та аудит відповідності  
4. **Багатофакторна автентифікація**: Спадкування можливостей MFA від корпоративних провайдерів ідентичності  
5. **Політики умовного доступу**: Використання контролю доступу на основі ризиків та адаптивної автентифікації

**Вимоги до реалізації:**
- **Перевірка аудиторії токена**: Переконатися, що всі токени явно видані для сервера MCP  
- **Перевірка видавця**: Підтвердження, що видавець токена відповідає очікуваному провайдеру ідентичності  
- **Перевірка підпису**: Криптографічна перевірка цілісності токена  
- **Дотримання терміну дії**: Строге дотримання обмежень часу життя токена  
- **Перевірка обсягу**: Переконатися, що токени містять відповідні дозволи для запитуваних операцій

### **Безпека логіки авторизації**

**Критичні заходи контролю:**
- **Комплексні аудити авторизації**: Регулярні перевірки безпеки всіх точок прийняття рішень авторизації  
- **Безпечні за замовчуванням**: Відмова в доступі, якщо логіка авторизації не може прийняти остаточне рішення  
- **Межі дозволів**: Чітке розмежування між різними рівнями привілеїв та доступом до ресурсів  
- **Журналювання аудиту**: Повне логування всіх рішень авторизації для моніторингу безпеки  
- **Регулярні перевірки доступу**: Періодична валідація дозволів користувачів та призначень привілеїв

## 2. **Безпека токенів та контроль проти передачі токенів**

### **Запобігання передачі токенів**

**Передача токенів категорично заборонена** у специфікації авторизації MCP через критичні ризики безпеки:

**Вирішувані ризики безпеки:**
- **Обхід контролю**: Уникає важливих заходів безпеки, таких як обмеження частоти, перевірка запитів і моніторинг трафіку  
- **Відсутність відповідальності**: Унеможливлює ідентифікацію клієнта, псує аудиторські сліди та розслідування інцидентів  
- **Експлуатація проксі**: Дозволяє зловмисникам використовувати сервери як проксі для несанкціонованого доступу до даних  
- **Порушення меж довіри**: Порушує припущення про походження токенів у нижчестоячих службах  
- **Бічний рух**: Компрометовані токени між кількома службами дозволяють розширити атаку

**Заходи реалізації:**
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

### **Безпечні патерни управління токенами**

**Кращі практики:**
- **Короткотривалі токени**: Мінімізувати вік експозиції шляхом частої ротації токенів  
- **Видача за потребою**: Видавати токени лише для конкретних операцій  
- **Безпечне зберігання**: Використовувати апаратні модулі безпеки (HSM) або захищені сховища ключів  
- **Прив’язка токенів**: Прив’язувати токени до конкретних клієнтів, сесій або операцій, де можливо  
- **Моніторинг і оповіщення**: Виявлення в режимі реального часу зловживань токенами або несанкціонованих шаблонів доступу

## 3. **Контроль безпеки сесій**

### **Запобігання викраденню сесій**

**Вектори атак:**
- **Ін’єкція подій викрадення сесії**: Зловмисні події, впроваджені у спільний стан сесії  
- **Імітація сесії**: Несанкціоноване використання викрадених ідентифікаторів сесії для обходу автентифікації  
- **Атаки з відновленням потоків**: Використання відновлення серверних подій для впровадження шкідливого контенту

**Обов’язкові заходи контролю сесій:**
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

**Безпека транспорту:**
- **Вимога HTTPS**: Весь трафік сесії через TLS 1.3  
- **Безпечні атрибути cookie**: HttpOnly, Secure, SameSite=Strict  
- **Фіксація сертифікатів**: Для критичних з’єднань, щоб запобігти атакам MITM

### **Розгляд стану сесії: станова vs безстанова**

**Для станових реалізацій:**
- Спільний стан сесії потребує додаткового захисту від ін’єкцій  
- Управління сесіями на основі черг потребує перевірки цілісності  
- Кілька серверних інстанцій потребують безпечної синхронізації стану сесії

**Для безстанових реалізацій:**
- Управління сесіями на основі JWT або подібних токенів  
- Криптографічна перевірка цілісності стану сесії  
- Зменшена площа атаки, але потребує надійної валідації токенів

## 4. **Специфічні заходи безпеки для ШІ**

### **Захист від ін’єкції підказок**

**Інтеграція Microsoft Prompt Shields:**
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

**Заходи реалізації:**
- **Санітизація введення**: Комплексна валідація та фільтрація всіх користувацьких введень  
- **Визначення меж контенту**: Чітке розмежування між системними інструкціями та користувацьким контентом  
- **Ієрархія інструкцій**: Правильні правила пріоритету для конфліктних інструкцій  
- **Моніторинг виводу**: Виявлення потенційно шкідливих або маніпульованих результатів

### **Запобігання отруєнню інструментів**

**Рамки безпеки інструментів:**
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

**Динамічне управління інструментами:**
- **Процеси затвердження**: Явна згода користувача на зміни інструментів  
- **Можливість відкату**: Здатність повертатися до попередніх версій інструментів  
- **Аудит змін**: Повна історія змін визначень інструментів  
- **Оцінка ризиків**: Автоматизована оцінка безпеки інструментів

## 5. **Запобігання атаці "заплутаного посередника"**

### **Безпека OAuth проксі**

**Заходи запобігання атакам:**
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

**Вимоги до реалізації:**
- **Перевірка згоди користувача**: Ніколи не пропускати екрани згоди для динамічної реєстрації клієнтів  
- **Валідація Redirect URI**: Строге перевіряння за білим списком цілей перенаправлення  
- **Захист коду авторизації**: Короткотривалі коди з одноразовим використанням  
- **Перевірка ідентичності клієнта**: Надійна валідація облікових даних та метаданих клієнта

## 6. **Безпека виконання інструментів**

### **Пісочниця та ізоляція**

**Ізоляція на основі контейнерів:**
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

**Ізоляція процесів:**
- **Окремі контексти процесів**: Кожне виконання інструменту в ізольованому процесі  
- **Міжпроцесна взаємодія**: Безпечні механізми IPC з валідацією  
- **Моніторинг процесів**: Аналіз поведінки в реальному часі та виявлення аномалій  
- **Обмеження ресурсів**: Жорсткі ліміти на CPU, пам’ять та операції вводу/виводу

### **Реалізація принципу найменших привілеїв**

**Управління дозволами:**
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

## 7. **Контроль безпеки ланцюга постачання**

### **Перевірка залежностей**

**Комплексна безпека компонентів:**
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

### **Безперервний моніторинг**

**Виявлення загроз ланцюга постачання:**
- **Моніторинг стану залежностей**: Безперервна оцінка всіх залежностей на предмет проблем безпеки  
- **Інтеграція розвідки про загрози**: Оновлення в реальному часі про нові загрози ланцюга постачання  
- **Аналіз поведінки**: Виявлення аномальної поведінки зовнішніх компонентів  
- **Автоматична реакція**: Негайне локалізування скомпрометованих компонентів

## 8. **Контроль моніторингу та виявлення**

### **Система управління інформацією та подіями безпеки (SIEM)**

**Комплексна стратегія логування:**
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

### **Виявлення загроз у реальному часі**

**Аналітика поведінки:**
- **Аналітика поведінки користувачів (UBA)**: Виявлення аномальних патернів доступу користувачів  
- **Аналітика поведінки сутностей (EBA)**: Моніторинг поведінки серверів MCP та інструментів  
- **Виявлення аномалій за допомогою машинного навчання**: Ідентифікація загроз безпеці на основі ШІ  
- **Кореляція з розвідкою про загрози**: Порівняння спостережуваних дій з відомими шаблонами атак

## 9. **Реагування на інциденти та відновлення**

### **Автоматизовані можливості реагування**

**Негайні дії реагування:**
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

### **Можливості судово-технічного розслідування**

**Підтримка розслідувань:**
- **Збереження аудиторського сліду**: Незмінне логування з криптографічною цілісністю  
- **Збір доказів**: Автоматизований збір релевантних артефактів безпеки  
- **Відтворення хронології подій**: Детальний послідовний опис подій, що призвели до інцидентів  
- **Оцінка впливу**: Аналіз масштабу компрометації та витоку даних

## **Ключові принципи архітектури безпеки**

### **Глибокий захист**
- **Багатошаровий захист**: Відсутність єдиної точки відмови в архітектурі безпеки  
- **Резервні контролі**: Перекриваючі заходи безпеки для критичних функцій  
- **Безпечні механізми за замовчуванням**: Захищені налаштування при помилках або атаках

### **Реалізація Zero Trust**
- **Ніколи не довіряй, завжди перевіряй**: Постійна валідація всіх сутностей і запитів  
- **Принцип найменших привілеїв**: Мінімальні права доступу для всіх компонентів  
- **Мікросегментація**: Детальний контроль мережі та доступу

### **Безперервна еволюція безпеки**
- **Адаптація до ландшафту загроз**: Регулярні оновлення для протидії новим загрозам  
- **Ефективність контролю безпеки**: Постійна оцінка та вдосконалення заходів  
- **Відповідність специфікаціям**: Узгодженість з оновленими стандартами безпеки MCP

---

## **Ресурси для реалізації**

### **Офіційна документація MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Рішення Microsoft для безпеки**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Стандарти безпеки**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Важливо**: Ці заходи безпеки відображають поточну специфікацію MCP (2025-06-18). Завжди перевіряйте за останньою [офіційною документацією](https://spec.modelcontextprotocol.io/), оскільки стандарти швидко розвиваються.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
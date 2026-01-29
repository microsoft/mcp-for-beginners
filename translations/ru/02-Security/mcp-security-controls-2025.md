# MCP Контроль Безопасности - Обновление Декабрь 2025

> **Текущий Стандарт**: Этот документ отражает требования безопасности [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) и официальные [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Протокол Контекста Модели (MCP) значительно развился с улучшенными мерами безопасности, охватывающими как традиционные угрозы программного обеспечения, так и специфические угрозы ИИ. Этот документ предоставляет комплексные меры безопасности для безопасных реализаций MCP по состоянию на декабрь 2025 года.

## **ОБЯЗАТЕЛЬНЫЕ Требования Безопасности**

### **Критические Запреты из Спецификации MCP:**

> **ЗАПРЕЩЕНО**: MCP серверы **НЕ ДОЛЖНЫ** принимать любые токены, которые не были явно выданы для MCP сервера  
>
> **ЗАПРЕЩЕНО**: MCP серверы **НЕ ДОЛЖНЫ** использовать сессии для аутентификации  
>
> **ТРЕБУЕТСЯ**: MCP серверы, реализующие авторизацию, **ДОЛЖНЫ** проверять ВСЕ входящие запросы  
>
> **ОБЯЗАТЕЛЬНО**: MCP прокси-серверы, использующие статические client ID, **ДОЛЖНЫ** получать согласие пользователя для каждого динамически зарегистрированного клиента

---

## 1. **Контроль Аутентификации и Авторизации**

### **Интеграция с Внешним Провайдером Идентификации**

**Текущий Стандарт MCP (2025-06-18)** позволяет MCP серверам делегировать аутентификацию внешним провайдерам идентификации, что представляет значительное улучшение безопасности:

### **Интеграция с Внешним Провайдером Идентификации**

**Текущий Стандарт MCP (2025-11-25)** позволяет MCP серверам делегировать аутентификацию внешним провайдерам идентификации, что представляет значительное улучшение безопасности:

**Преимущества Безопасности:**
1. **Исключение Рисков Пользовательской Аутентификации**: Снижает поверхность уязвимостей, избегая пользовательских реализаций аутентификации  
2. **Безопасность Корпоративного Уровня**: Использует проверенных провайдеров идентификации, таких как Microsoft Entra ID, с расширенными функциями безопасности  
3. **Централизованное Управление Идентификацией**: Упрощает управление жизненным циклом пользователей, контроль доступа и аудит соответствия  
4. **Многофакторная Аутентификация**: Наследует возможности MFA от корпоративных провайдеров идентификации  
5. **Политики Условного Доступа**: Использует контроль доступа на основе риска и адаптивную аутентификацию

**Требования к Реализации:**
- **Проверка Аудитории Токена**: Проверять, что все токены явно выданы для MCP сервера  
- **Проверка Издателя**: Валидировать, что издатель токена соответствует ожидаемому провайдеру идентификации  
- **Проверка Подписи**: Криптографическая проверка целостности токена  
- **Контроль Срока Действия**: Строгое соблюдение ограничений срока действия токена  
- **Проверка Областей (Scope)**: Убедиться, что токены содержат соответствующие разрешения для запрашиваемых операций

### **Безопасность Логики Авторизации**

**Критические Контроли:**
- **Полные Аудиты Авторизации**: Регулярные проверки безопасности всех точек принятия решений по авторизации  
- **Безопасные По Умолчанию**: Отказ в доступе, если логика авторизации не может принять однозначное решение  
- **Границы Разрешений**: Четкое разделение между разными уровнями привилегий и доступом к ресурсам  
- **Логирование Аудита**: Полное логирование всех решений по авторизации для мониторинга безопасности  
- **Регулярные Проверки Доступа**: Периодическая валидация разрешений пользователей и назначений привилегий

## 2. **Безопасность Токенов и Контроль Анти-Проследования**

### **Запрет на Проследование Токенов**

**Проследование токенов строго запрещено** в Спецификации Авторизации MCP из-за критических рисков безопасности:

**Риски Безопасности:**
- **Обход Контролей**: Обходит важные меры безопасности, такие как ограничение скорости, проверка запросов и мониторинг трафика  
- **Нарушение Ответственности**: Делает невозможным идентификацию клиента, нарушая аудит и расследование инцидентов  
- **Эксплуатация через Прокси**: Позволяет злоумышленникам использовать серверы как прокси для несанкционированного доступа к данным  
- **Нарушение Границ Доверия**: Нарушает предположения downstream-сервисов о происхождении токенов  
- **Латеральное Распространение**: Компрометированные токены в нескольких сервисах расширяют возможности атаки

**Контроль Реализации:**
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

### **Паттерны Безопасного Управления Токенами**

**Лучшие Практики:**
- **Краткоживущие Токены**: Минимизировать окно экспозиции за счет частой ротации токенов  
- **Выдача По Требованию**: Выдавать токены только при необходимости для конкретных операций  
- **Безопасное Хранение**: Использовать аппаратные модули безопасности (HSM) или защищенные хранилища ключей  
- **Привязка Токенов**: Привязывать токены к конкретным клиентам, сессиям или операциям, где возможно  
- **Мониторинг и Оповещения**: Обнаружение в реальном времени злоупотреблений токенами или несанкционированных паттернов доступа

## 3. **Контроль Безопасности Сессий**

### **Предотвращение Захвата Сессий**

**Векторы Атак:**
- **Внедрение Зловредных Запросов в Сессию**: Внедрение вредоносных событий в общий статус сессии  
- **Имитация Сессии**: Несанкционированное использование украденных идентификаторов сессий для обхода аутентификации  
- **Атаки с Возобновлением Потока**: Эксплуатация возобновления серверных событий для внедрения вредоносного контента

**Обязательные Контроли Сессий:**
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

**Безопасность Транспорта:**
- **Обязательное HTTPS**: Вся сессионная коммуникация через TLS 1.3  
- **Безопасные Атрибуты Кук**: HttpOnly, Secure, SameSite=Strict  
- **Пиннинг Сертификатов**: Для критических соединений, чтобы предотвратить MITM-атаки

### **Государственные vs Бездержавные Реализации**

**Для Государственных Реализаций:**
- Общий статус сессии требует дополнительной защиты от инъекций  
- Управление сессиями на основе очередей требует проверки целостности  
- Несколько серверных инстансов требуют безопасной синхронизации состояния сессии

**Для Бездержавных Реализаций:**
- Управление сессиями на основе JWT или аналогичных токенов  
- Криптографическая проверка целостности состояния сессии  
- Сниженная поверхность атаки, но требует надежной валидации токенов

## 4. **Специфические Контроли Безопасности для ИИ**

### **Защита от Внедрения Запросов**

**Интеграция Microsoft Prompt Shields:**
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

**Контроль Реализации:**
- **Санитизация Входных Данных**: Комплексная проверка и фильтрация всех пользовательских вводов  
- **Определение Границ Контента**: Четкое разделение системных инструкций и пользовательского контента  
- **Иерархия Инструкций**: Правила приоритета для конфликтующих инструкций  
- **Мониторинг Выходных Данных**: Обнаружение потенциально вредоносных или манипулированных результатов

### **Предотвращение Отравления Инструментов**

**Фреймворк Безопасности Инструментов:**
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

**Динамическое Управление Инструментами:**
- **Процессы Одобрения**: Явное согласие пользователя на изменения инструментов  
- **Возможности Отката**: Возможность возврата к предыдущим версиям инструментов  
- **Аудит Изменений**: Полная история изменений определений инструментов  
- **Оценка Рисков**: Автоматическая оценка безопасности инструментов

## 5. **Предотвращение Атаки "Смущённый Депутат"**

### **Безопасность OAuth Прокси**

**Контроли Предотвращения Атак:**
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

**Требования к Реализации:**
- **Проверка Согласия Пользователя**: Никогда не пропускать экраны согласия при динамической регистрации клиентов  
- **Валидация Redirect URI**: Строгая проверка по белому списку перенаправлений  
- **Защита Авторизационных Кодoв**: Коды с коротким сроком действия и одноразовым использованием  
- **Проверка Идентичности Клиента**: Надежная валидация учетных данных и метаданных клиента

## 6. **Безопасность Выполнения Инструментов**

### **Песочница и Изоляция**

**Изоляция на основе Контейнеров:**
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

**Изоляция Процессов:**
- **Отдельные Контексты Процессов**: Каждое выполнение инструмента в изолированном пространстве процесса  
- **Межпроцессное Взаимодействие**: Безопасные механизмы IPC с проверкой  
- **Мониторинг Процессов**: Анализ поведения во время выполнения и обнаружение аномалий  
- **Ограничения Ресурсов**: Жесткие лимиты на CPU, память и операции ввода-вывода

### **Реализация Принципа Минимальных Привилегий**

**Управление Разрешениями:**
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

## 7. **Контроль Безопасности Цепочки Поставок**

### **Проверка Зависимостей**

**Комплексная Безопасность Компонентов:**
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

### **Непрерывный Мониторинг**

**Обнаружение Угроз Цепочки Поставок:**
- **Мониторинг Состояния Зависимостей**: Постоянная оценка всех зависимостей на предмет проблем безопасности  
- **Интеграция Разведки Угроз**: Обновления в реальном времени о новых угрозах цепочки поставок  
- **Анализ Поведения**: Обнаружение аномалий в поведении внешних компонентов  
- **Автоматический Ответ**: Немедленное ограничение скомпрометированных компонентов

## 8. **Контроль Мониторинга и Обнаружения**

### **Системы Управления Информацией и Событиями Безопасности (SIEM)**

**Комплексная Стратегия Логирования:**
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

### **Обнаружение Угроз в Реальном Времени**

**Аналитика Поведения:**
- **Аналитика Поведения Пользователей (UBA)**: Обнаружение необычных паттернов доступа пользователей  
- **Аналитика Поведения Сущностей (EBA)**: Мониторинг поведения MCP сервера и инструментов  
- **Обнаружение Аномалий с Машинным Обучением**: ИИ-основанное выявление угроз безопасности  
- **Корреляция Разведки Угроз**: Сопоставление наблюдаемых действий с известными шаблонами атак

## 9. **Реагирование на Инциденты и Восстановление**

### **Автоматизированные Возможности Реагирования**

**Немедленные Действия:**
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

### **Возможности Судебной Экспертизы**

**Поддержка Расследований:**
- **Сохранение Аудит Трейла**: Неизменяемое логирование с криптографической целостностью  
- **Сбор Доказательств**: Автоматический сбор релевантных артефактов безопасности  
- **Восстановление Хронологии**: Детальная последовательность событий, приведших к инцидентам  
- **Оценка Влияния**: Анализ масштаба компрометации и утечки данных

## **Ключевые Принципы Архитектуры Безопасности**

### **Защита в Глубину**
- **Многоуровневая Безопасность**: Отсутствие единой точки отказа в архитектуре безопасности  
- **Резервные Контроли**: Перекрывающиеся меры безопасности для критических функций  
- **Безопасные По Умолчанию Механизмы**: Защищенные настройки при ошибках или атаках

### **Реализация Модели Нулевого Доверия**
- **Никогда не доверять, всегда проверять**: Постоянная валидация всех сущностей и запросов  
- **Принцип Минимальных Привилегий**: Минимальные права доступа для всех компонентов  
- **Микросегментация**: Гранулярный контроль сети и доступа

### **Постоянное Эволюционирование Безопасности**
- **Адаптация к Ландшафту Угроз**: Регулярные обновления для борьбы с новыми угрозами  
- **Эффективность Контролей Безопасности**: Постоянная оценка и улучшение мер безопасности  
- **Соответствие Спецификациям**: Соответствие развивающимся стандартам безопасности MCP

---

## **Ресурсы для Реализации**

### **Официальная Документация MCP**
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Решения Безопасности Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Стандарты Безопасности**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Важно**: Эти меры безопасности отражают текущую спецификацию MCP (2025-06-18). Всегда проверяйте актуальность в последней [официальной документации](https://spec.modelcontextprotocol.io/), так как стандарты быстро развиваются.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
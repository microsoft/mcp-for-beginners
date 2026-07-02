```mermaid
sequenceDiagram
    actor User
    participant WebApp as Веб-приложение<br/>(ContentSafetyController)
    participant SafetyService as Служба безопасности контента
    participant AzureAPI as API безопасности контента Azure
    participant LangChain as LangChain4j
    participant McpClient as Клиент MCP
    participant McpServer as Сервер калькулятора MCP<br/>(Порт 8080)
    participant CalcService as Служба калькулятора

    %% Взаимодействие с пользователем
    User->>WebApp: Введите запрос на вычисление
    WebApp->>WebApp: Создать PromptRequest

    %% Проверка безопасности контента
    WebApp->>SafetyService: processPrompt(prompt)
    SafetyService->>AzureAPI: analyzeText(prompt)
    AzureAPI-->>SafetyService: AnalyzeTextResult
    SafetyService->>SafetyService: Проверить, безопасно ли содержимое<br/>(уровень < 2 для всех категорий)

    %% Процесс обработки - безопасный контент
    alt Контент безопасен
        SafetyService->>LangChain: Передать запрос в Bot.chat()
        LangChain->>McpClient: Обработать запрос
        McpClient->>McpServer: Вызвать соответствующий инструмент калькулятора через SSE
        McpServer->>CalcService: Выполнить вычисление<br/>(сложение, вычитание, умножение и т.д.)
        CalcService-->>McpServer: Результат вычисления
        McpServer-->>McpClient: Результат выполнения инструмента
        McpClient-->>LangChain: Результат инструмента
        LangChain-->>SafetyService: Ответ бота
        SafetyService-->>WebApp: Вернуть карту результатов<br/>{isSafe: "true", botResponse: результат, safetyResult: детали}
        WebApp-->>User: Показать результат вычисления и информацию о безопасности
    else Контент небезопасен
        SafetyService-->>WebApp: Вернуть карту результатов<br/>{isSafe: "false", safetyResult: детали}
        WebApp-->>User: Показать предупреждение о безопасности<br/>(без вычислений)
    end
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
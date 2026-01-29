```mermaid
sequenceDiagram
    actor User
    participant WebApp as Web App<br/>(ContentSafetyController)
    participant SafetyService as Content Safety Service
    participant AzureAPI as Azure Content Safety API
    participant LangChain as LangChain4j
    participant McpClient as MCP Client
    participant McpServer as MCP Calculator Server<br/>(Port 8080)
    participant CalcService as Calculator Service

    %% User Interaction
    User->>WebApp: Enter calculation prompt
    WebApp->>WebApp: Create PromptRequest

    %% Content Safety Check
    WebApp->>SafetyService: processPrompt(prompt)
    SafetyService->>AzureAPI: analyzeText(prompt)
    AzureAPI-->>SafetyService: AnalyzeTextResult
    SafetyService->>SafetyService: Check if content is safe<br/>(severity < 2 for all categories)

    %% Processing Flow - Safe Content
    alt Content is safe
        SafetyService->>LangChain: Pass prompt to Bot.chat()
        LangChain->>McpClient: Process prompt
        McpClient->>McpServer: Call appropriate calculator tool via SSE
        McpServer->>CalcService: Execute calculation<br/>(add, subtract, multiply, etc.)
        CalcService-->>McpServer: Calculation result
        McpServer-->>McpClient: Tool execution result
        McpClient-->>LangChain: Tool result
        LangChain-->>SafetyService: Bot response
        SafetyService-->>WebApp: Return result map<br/>{isSafe: "true", botResponse: result, safetyResult: details}
        WebApp-->>User: Display calculation result and safety info
    else Content is unsafe
        SafetyService-->>WebApp: Return result map<br/>{isSafe: "false", safetyResult: details}
        WebApp-->>User: Display safety warning<br/>(without calculation)
    end
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
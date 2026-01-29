## Dynamické směrování nástrojů

Směrování nástrojů zajišťuje, že volání nástrojů jsou směrována na nejvhodnější službu podle kontextu. Například volání nástroje pro počasí může být směrováno na regionální koncový bod podle polohy uživatele, nebo kalkulační nástroj může potřebovat použít specifickou verzi API.

Podívejme se na příklad implementace, který demonstruje dynamické směrování nástrojů na základě analýzy požadavku, regionálních koncových bodů a podpory verzování.

## Architektura vzorkování a směrování v MCP

Vzorkování je klíčovou součástí Model Context Protocol (MCP), která umožňuje efektivní zpracování a směrování požadavků. Zahrnuje analýzu příchozích požadavků za účelem určení nejvhodnějšího modelu nebo služby, která je zpracuje, na základě různých kritérií, jako je typ obsahu, uživatelský kontext a zatížení systému.

Vzorkování a směrování lze kombinovat k vytvoření robustní architektury, která optimalizuje využití zdrojů a zajišťuje vysokou dostupnost. Proces vzorkování může být použit k třídění požadavků, zatímco směrování je nasměruje na příslušné modely nebo služby.

Níže uvedený diagram ilustruje, jak vzorkování a směrování spolupracují v komplexní architektuře MCP:

```mermaid
flowchart TB
    Client([MCP Client])
    
    subgraph "Request Processing"
        Router{Request Router}
        Analyzer[Content Analyzer]
        Sampler[Sampling Configurator]
    end
    
    subgraph "Server Selection"
        LoadBalancer{Load Balancer}
        ModelSelector[Model Selector]
        ServerPool[(Server Pool)]
    end
    
    subgraph "Model Processing"
        ModelA[Specialized Model A]
        ModelB[Specialized Model B]
        ModelC[General Model]
    end
    
    subgraph "Tool Execution"
        ToolRouter{Tool Router}
        ToolRegistryA[(Primary Tools)]
        ToolRegistryB[(Regional Tools)]
    end
    
    Client -->|Request| Router
    Router -->|Analyze| Analyzer
    Analyzer -->|Configure| Sampler
    Router -->|Route Request| LoadBalancer
    LoadBalancer --> ServerPool
    ServerPool --> ModelSelector
    ModelSelector --> ModelA
    ModelSelector --> ModelB
    ModelSelector --> ModelC
    
    ModelA -->|Tool Calls| ToolRouter
    ModelB -->|Tool Calls| ToolRouter
    ModelC -->|Tool Calls| ToolRouter
    
    ToolRouter --> ToolRegistryA
    ToolRouter --> ToolRegistryB
    
    ToolRegistryA -->|Results| ModelA
    ToolRegistryA -->|Results| ModelB
    ToolRegistryA -->|Results| ModelC
    ToolRegistryB -->|Results| ModelA
    ToolRegistryB -->|Results| ModelB
    ToolRegistryB -->|Results| ModelC
    
    ModelA -->|Response| Client
    ModelB -->|Response| Client
    ModelC -->|Response| Client
    
    style Client fill:#d5e8f9,stroke:#333
    style Router fill:#f9d5e5,stroke:#333
    style LoadBalancer fill:#f9d5e5,stroke:#333
    style ToolRouter fill:#f9d5e5,stroke:#333
    style ModelA fill:#c2f0c2,stroke:#333
    style ModelB fill:#c2f0c2,stroke:#333
    style ModelC fill:#c2f0c2,stroke:#333
```

## Co bude dál

- [5.6 Sampling](../mcp-sampling/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
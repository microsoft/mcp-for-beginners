## Dynamisk verktygsdirigering

Verktygsdirigering säkerställer att verktygsanrop skickas till den mest lämpliga tjänsten baserat på kontext. Till exempel kan ett väderverktygsanrop behöva dirigeras till en regional slutpunkt baserat på användarens plats, eller ett kalkylatorverktyg kan behöva använda en specifik version av API:et.

Låt oss titta på ett exempel som visar dynamisk verktygsdirigering baserat på förfrågningsanalys, regionala slutpunkter och versionsstöd.

## Sampling och dirigeringsarkitektur i MCP

Sampling är en viktig del av Model Context Protocol (MCP) som möjliggör effektiv hantering och dirigering av förfrågningar. Det innebär att analysera inkommande förfrågningar för att avgöra vilken modell eller tjänst som är mest lämplig att hantera dem, baserat på olika kriterier som innehållstyp, användarkontext och systembelastning.

Sampling och dirigering kan kombineras för att skapa en robust arkitektur som optimerar resursanvändning och säkerställer hög tillgänglighet. Samplingsprocessen kan användas för att klassificera förfrågningar, medan dirigering skickar dem till rätt modeller eller tjänster.

Diagrammet nedan visar hur sampling och dirigering samverkar i en omfattande MCP-arkitektur:

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

## Vad händer härnäst

- [5.6 Sampling](../mcp-sampling/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
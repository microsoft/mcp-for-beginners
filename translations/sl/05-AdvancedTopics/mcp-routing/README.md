## Dinamično usmerjanje orodij

Usmerjanje orodij zagotavlja, da so klici orodij usmerjeni na najbolj ustrezno storitev glede na kontekst. Na primer, klic orodja za vreme je morda treba usmeriti na regionalno točko glede na lokacijo uporabnika, ali pa mora orodje za kalkulator uporabljati določeno različico API-ja.

Poglejmo primer implementacije, ki prikazuje dinamično usmerjanje orodij na podlagi analize zahtevka, regionalnih točk in podpore za različice.

## Arhitektura vzorčenja in usmerjanja v MCP

Vzorčenje je ključni del Model Context Protocol (MCP), ki omogoča učinkovito obdelavo in usmerjanje zahtevkov. Vključuje analizo dohodnih zahtevkov za določitev najbolj primernega modela ali storitve za njihovo obravnavo, glede na različne kriterije, kot so vrsta vsebine, uporabniški kontekst in obremenitev sistema.

Vzorčenje in usmerjanje lahko združimo v robustno arhitekturo, ki optimizira izrabo virov in zagotavlja visoko razpoložljivost. Proces vzorčenja se lahko uporabi za klasifikacijo zahtevkov, medtem ko jih usmerjanje vodi do ustreznih modelov ali storitev.

Spodnja shema prikazuje, kako vzorčenje in usmerjanje delujeta skupaj v celoviti arhitekturi MCP:

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

## Kaj sledi

- [5.6 Sampling](../mcp-sampling/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
## Dinamikus eszközirányítás

Az eszközirányítás biztosítja, hogy az eszközhívások a kontextus alapján a legmegfelelőbb szolgáltatáshoz kerüljenek. Például egy időjárás-eszköz hívását a felhasználó helyzete alapján egy regionális végpontra kell irányítani, vagy egy számológép eszköznek egy adott API verziót kell használnia.

Nézzünk egy példát, amely bemutatja a dinamikus eszközirányítást a kérés elemzése, a regionális végpontok és a verziókezelés alapján.

## Mintavételezés és irányítás az MCP-ben

A mintavételezés a Model Context Protocol (MCP) egyik kulcsfontosságú eleme, amely lehetővé teszi a hatékony kérésfeldolgozást és irányítást. Ez magában foglalja a bejövő kérések elemzését annak érdekében, hogy meghatározzuk a legmegfelelőbb modellt vagy szolgáltatást, amely kezelni tudja azokat, különböző szempontok alapján, mint például a tartalom típusa, a felhasználói kontextus és a rendszer terheltsége.

A mintavételezés és az irányítás kombinálásával egy robusztus architektúra hozható létre, amely optimalizálja az erőforrások kihasználását és biztosítja a magas rendelkezésre állást. A mintavételezési folyamat a kérések osztályozására használható, míg az irányítás a megfelelő modellekhez vagy szolgáltatásokhoz irányítja azokat.

Az alábbi ábra szemlélteti, hogyan működik együtt a mintavételezés és az irányítás egy átfogó MCP architektúrában:

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

## Mi következik

- [5.6 Mintavételezés](../mcp-sampling/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
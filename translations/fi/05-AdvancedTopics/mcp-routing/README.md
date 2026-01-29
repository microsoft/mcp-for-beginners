## Dynaaminen työkalujen reititys

Työkalujen reititys varmistaa, että työkalukutsut ohjataan kontekstin perusteella sopivimpaan palveluun. Esimerkiksi säätyökalukutsu saattaa tarvita ohjauksen alueelliselle päätepisteelle käyttäjän sijainnin mukaan, tai laskin-työkalu saattaa tarvita tietyn version API:sta.

Katsotaan esimerkkitoteutusta, joka havainnollistaa dynaamista työkalujen reititystä pyyntöanalyysin, alueellisten päätepisteiden ja versiotuen perusteella.

## Näytteenotto ja reititys MCP:ssä

Näytteenotto on keskeinen osa Model Context Protocolia (MCP), joka mahdollistaa tehokkaan pyyntöjen käsittelyn ja reitityksen. Se tarkoittaa saapuvien pyyntöjen analysointia sopivimman mallin tai palvelun määrittämiseksi, perustuen erilaisiin kriteereihin kuten sisältötyyppi, käyttäjäkonteksti ja järjestelmän kuormitus.

Näytteenotto ja reititys voidaan yhdistää luomaan vankka arkkitehtuuri, joka optimoi resurssien käytön ja varmistaa korkean käytettävyyden. Näytteenottoprosessia voidaan käyttää pyyntöjen luokitteluun, kun taas reititys ohjaa ne sopiville malleille tai palveluille.

Alla oleva kaavio havainnollistaa, miten näytteenotto ja reititys toimivat yhdessä kattavassa MCP-arkkitehtuurissa:

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

## Mitä seuraavaksi

- [5.6 Näytteenotto](../mcp-sampling/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
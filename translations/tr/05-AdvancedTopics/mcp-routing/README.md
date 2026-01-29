## Dinamik Araç Yönlendirme

Araç yönlendirme, araç çağrılarının bağlama göre en uygun hizmete yönlendirilmesini sağlar. Örneğin, bir hava durumu aracı çağrısı, kullanıcının konumuna bağlı olarak bölgesel bir uç noktaya yönlendirilmesi gerekebilir veya bir hesap makinesi aracı, belirli bir API sürümünü kullanmak zorunda olabilir.

Aşağıda, istek analizi, bölgesel uç noktalar ve sürüm desteğine dayalı dinamik araç yönlendirmeyi gösteren bir örnek uygulamaya bakalım.

## MCP'de Örnekleme ve Yönlendirme Mimarisi

Örnekleme, Model Context Protocol (MCP) içinde verimli istek işleme ve yönlendirme sağlayan kritik bir bileşendir. Gelen isteklerin içerik türü, kullanıcı bağlamı ve sistem yükü gibi çeşitli kriterlere göre en uygun model veya hizmete yönlendirilmesini belirlemek için analiz edilmesini içerir.

Örnekleme ve yönlendirme birleştirilerek kaynak kullanımını optimize eden ve yüksek erişilebilirlik sağlayan sağlam bir mimari oluşturulabilir. Örnekleme süreci istekleri sınıflandırmak için kullanılırken, yönlendirme onları uygun model veya hizmetlere yönlendirir.

Aşağıdaki diyagram, örnekleme ve yönlendirmenin kapsamlı bir MCP mimarisinde nasıl birlikte çalıştığını göstermektedir:

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

## Sonraki Adımlar

- [5.6 Sampling](../mcp-sampling/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
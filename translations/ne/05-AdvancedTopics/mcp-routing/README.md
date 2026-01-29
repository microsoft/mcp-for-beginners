## बुद्धिमानी लोड ब्यालेन्सिङ

लोड ब्यालेन्सिङले स्रोतहरूको उपयोगलाई अनुकूल बनाउँछ र MCP सेवाहरूको उच्च उपलब्धता सुनिश्चित गर्दछ। लोड ब्यालेन्सिङ लागू गर्ने विभिन्न तरिकाहरू छन्, जस्तै राउन्ड-रबिन, तौलित प्रतिक्रिया समय, वा सामग्री-चेतन रणनीतिहरू।

तलको उदाहरणले निम्न रणनीतिहरू प्रयोग गरेको छ:

- **राउन्ड रबिन**: उपलब्ध सर्भरहरूमा अनुरोधहरू समान रूपमा वितरण गर्छ।
- **तौलित प्रतिक्रिया समय**: सर्भरहरूको औसत प्रतिक्रिया समयको आधारमा अनुरोधहरू मार्गनिर्देशन गर्छ।
- **सामग्री-चेतन**: अनुरोधको सामग्रीको आधारमा विशेष सर्भरहरूमा अनुरोधहरू पठाउँछ।

## गतिशील उपकरण मार्गनिर्देशन

उपकरण मार्गनिर्देशनले उपकरण कलहरू सन्दर्भको आधारमा सबैभन्दा उपयुक्त सेवामा पठाउन सुनिश्चित गर्छ। उदाहरणका लागि, मौसम उपकरण कल प्रयोगकर्ताको स्थानको आधारमा क्षेत्रीय अन्तबिन्दुमा पठाउन आवश्यक पर्न सक्छ, वा क्यालकुलेटर उपकरणले API को विशेष संस्करण प्रयोग गर्नुपर्ने हुन सक्छ।

तलको उदाहरणले अनुरोध विश्लेषण, क्षेत्रीय अन्तबिन्दुहरू, र संस्करण समर्थनको आधारमा गतिशील उपकरण मार्गनिर्देशन कसरी गर्ने देखाउँछ।

## MCP मा नमुना र मार्गनिर्देशन वास्तुकला

नमुना लिनु Model Context Protocol (MCP) को एक महत्वपूर्ण अङ्ग हो जसले प्रभावकारी अनुरोध प्रशोधन र मार्गनिर्देशनलाई सम्भव बनाउँछ। यसले आउने अनुरोधहरूको विश्लेषण गरेर सबैभन्दा उपयुक्त मोडेल वा सेवा निर्धारण गर्छ, जस्तै सामग्री प्रकार, प्रयोगकर्ता सन्दर्भ, र प्रणाली लोडका आधारमा।

नमुना र मार्गनिर्देशनलाई संयोजन गरेर एक बलियो वास्तुकला तयार गर्न सकिन्छ जसले स्रोतहरूको उपयोग अनुकूल बनाउँछ र उच्च उपलब्धता सुनिश्चित गर्छ। नमुना प्रक्रिया अनुरोधहरू वर्गीकरण गर्न प्रयोग गर्न सकिन्छ भने मार्गनिर्देशनले तिनीहरूलाई उपयुक्त मोडेल वा सेवामा पठाउँछ।

तलको चित्रले कसरी नमुना र मार्गनिर्देशनले संयुक्त रूपमा व्यापक MCP वास्तुकलामा काम गर्छन् देखाउँछ:

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

## के छ अर्को

- [5.6 नमुना लिनु](../mcp-sampling/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
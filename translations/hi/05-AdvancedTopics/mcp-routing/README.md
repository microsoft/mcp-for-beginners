## MCP में सैंपलिंग और रूटिंग आर्किटेक्चर

सैंपलिंग मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) का एक महत्वपूर्ण हिस्सा है जो कुशल अनुरोध प्रसंस्करण और रूटिंग की अनुमति देता है। इसमें आने वाले अनुरोधों का विश्लेषण करना शामिल है ताकि विभिन्न मानदंडों जैसे सामग्री का प्रकार, उपयोगकर्ता संदर्भ, और सिस्टम लोड के आधार पर सबसे उपयुक्त मॉडल या सेवा निर्धारित की जा सके।

सैंपलिंग और रूटिंग को मिलाकर एक मजबूत आर्किटेक्चर बनाया जा सकता है जो संसाधनों के उपयोग को अनुकूलित करता है और उच्च उपलब्धता सुनिश्चित करता है। सैंपलिंग प्रक्रिया का उपयोग अनुरोधों को वर्गीकृत करने के लिए किया जा सकता है, जबकि रूटिंग उन्हें उपयुक्त मॉडल या सेवाओं की ओर निर्देशित करता है।

नीचे दिया गया आरेख दिखाता है कि कैसे सैंपलिंग और रूटिंग मिलकर एक व्यापक MCP आर्किटेक्चर में काम करते हैं:

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

## आगे क्या है

- [5.6 Sampling](../mcp-sampling/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
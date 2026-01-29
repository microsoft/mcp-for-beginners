## MCP میں سیمپلنگ اور روٹنگ کا فن تعمیر

سیمپلنگ ماڈل کانٹیکسٹ پروٹوکول (MCP) کا ایک اہم جزو ہے جو مؤثر درخواست کی پروسیسنگ اور روٹنگ کی اجازت دیتا ہے۔ اس میں آنے والی درخواستوں کا تجزیہ شامل ہے تاکہ مختلف معیار جیسے مواد کی قسم، صارف کا سیاق و سباق، اور نظام کا بوجھ کی بنیاد پر سب سے مناسب ماڈل یا سروس کا تعین کیا جا سکے۔

سیمپلنگ اور روٹنگ کو ملا کر ایک مضبوط فن تعمیر بنایا جا سکتا ہے جو وسائل کے استعمال کو بہتر بناتا ہے اور اعلی دستیابی کو یقینی بناتا ہے۔ سیمپلنگ کا عمل درخواستوں کی درجہ بندی کے لیے استعمال کیا جا سکتا ہے، جبکہ روٹنگ انہیں مناسب ماڈلز یا خدمات کی طرف بھیجتی ہے۔

نیچے دیا گیا خاکہ دکھاتا ہے کہ MCP کے جامع فن تعمیر میں سیمپلنگ اور روٹنگ کس طرح مل کر کام کرتے ہیں:

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

## آگے کیا ہے

- [5.6 Sampling](../mcp-sampling/README.md)

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
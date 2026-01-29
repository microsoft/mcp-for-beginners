## التوازن الذكي للحمل

يعمل توازن الحمل على تحسين استخدام الموارد وضمان توفر عالي لخدمات MCP. هناك طرق مختلفة لتنفيذ توازن الحمل، مثل التوزيع بالتناوب (round-robin)، أو استنادًا إلى زمن الاستجابة المرجح، أو استراتيجيات تعتمد على محتوى الطلب.

لننظر إلى مثال تنفيذ أدناه يستخدم الاستراتيجيات التالية:

- **التوزيع بالتناوب**: يوزع الطلبات بالتساوي عبر الخوادم المتاحة.
- **زمن الاستجابة المرجح**: يوجه الطلبات إلى الخوادم بناءً على متوسط زمن استجابتها.
- **الوعي بالمحتوى**: يوجه الطلبات إلى خوادم متخصصة بناءً على محتوى الطلب.

## التوجيه الديناميكي للأدوات

يضمن توجيه الأدوات أن يتم توجيه استدعاءات الأدوات إلى الخدمة الأنسب بناءً على السياق. على سبيل المثال، قد يحتاج استدعاء أداة الطقس إلى التوجيه إلى نقطة نهاية إقليمية بناءً على موقع المستخدم، أو قد تحتاج أداة الحاسبة إلى استخدام إصدار معين من واجهة برمجة التطبيقات.

لنلقي نظرة على مثال تنفيذ يوضح التوجيه الديناميكي للأدوات استنادًا إلى تحليل الطلب، ونقاط النهاية الإقليمية، ودعم الإصدارات.

## هندسة العينة والتوجيه في MCP

العينة هي مكون حيوي في بروتوكول سياق النموذج (MCP) يسمح بمعالجة الطلبات وتوجيهها بكفاءة. تتضمن عملية العينة تحليل الطلبات الواردة لتحديد النموذج أو الخدمة الأنسب للتعامل معها، بناءً على معايير مختلفة مثل نوع المحتوى، وسياق المستخدم، وحمل النظام.

يمكن دمج العينة والتوجيه لإنشاء هندسة قوية تعمل على تحسين استخدام الموارد وضمان توفر عالي. يمكن استخدام عملية العينة لتصنيف الطلبات، بينما يقوم التوجيه بتوجيهها إلى النماذج أو الخدمات المناسبة.

يوضح الرسم البياني أدناه كيف تعمل العينة والتوجيه معًا في هندسة MCP شاملة:

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

## ما التالي

- [5.6 العينة](../mcp-sampling/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
## สถาปัตยกรรมการสุ่มตัวอย่างและการกำหนดเส้นทางใน MCP

การสุ่มตัวอย่างเป็นส่วนสำคัญของ Model Context Protocol (MCP) ที่ช่วยให้การประมวลผลและการกำหนดเส้นทางคำขอเป็นไปอย่างมีประสิทธิภาพ โดยจะวิเคราะห์คำขอที่เข้ามาเพื่อกำหนดโมเดลหรือบริการที่เหมาะสมที่สุดในการจัดการคำขอนั้น ๆ โดยพิจารณาจากเกณฑ์ต่าง ๆ เช่น ประเภทเนื้อหา บริบทของผู้ใช้ และภาระงานของระบบ

การสุ่มตัวอย่างและการกำหนดเส้นทางสามารถรวมกันเพื่อสร้างสถาปัตยกรรมที่แข็งแกร่งซึ่งช่วยเพิ่มประสิทธิภาพการใช้ทรัพยากรและรับประกันความพร้อมใช้งานสูง กระบวนการสุ่มตัวอย่างสามารถใช้ในการจำแนกคำขอ ขณะที่การกำหนดเส้นทางจะนำคำขอไปยังโมเดลหรือบริการที่เหมาะสม

แผนภาพด้านล่างแสดงให้เห็นว่าการสุ่มตัวอย่างและการกำหนดเส้นทางทำงานร่วมกันอย่างไรในสถาปัตยกรรม MCP ที่ครอบคลุม:

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

## ต่อไปคืออะไร

- [5.6 การสุ่มตัวอย่าง](../mcp-sampling/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
## MCP တွင် Sampling နှင့် Routing အဆောက်အအုံ

Sampling သည် Model Context Protocol (MCP) ၏ အရေးကြီးသော အစိတ်အပိုင်းဖြစ်ပြီး၊ ထိရောက်စွာ တောင်းဆိုမှုများကို ဆောင်ရွက်ရန်နှင့် routing ပြုလုပ်ရန် အသုံးပြုသည်။ ၎င်းသည် လာရောက်သော တောင်းဆိုမှုများကို အကြောင်းအရာအမျိုးအစား၊ အသုံးပြုသူအခြေအနေ၊ စနစ်ပေါ်လွှမ်းမှု စသည့် အချက်အလက်များအပေါ် မူတည်၍ အကောင်းဆုံး မော်ဒယ် သို့မဟုတ် ဝန်ဆောင်မှုကို သတ်မှတ်ရန် စိစစ်ခြင်းကို ပါဝင်သည်။

Sampling နှင့် routing ကို ပေါင်းစပ်၍ အရင်းအမြစ် အသုံးပြုမှုကို ထိရောက်စွာ စီမံခန့်ခွဲနိုင်ပြီး၊ ဝန်ဆောင်မှုများ အမြဲရရှိနိုင်မှုကို သေချာစေသော ခိုင်မာသော အဆောက်အအုံတစ်ခု ဖန်တီးနိုင်သည်။ Sampling လုပ်ငန်းစဉ်သည် တောင်းဆိုမှုများကို အမျိုးအစားခွဲခြားရာတွင် အသုံးပြုနိုင်ပြီး၊ routing သည် ၎င်းတို့ကို သင့်တော်သော မော်ဒယ်များ သို့မဟုတ် ဝန်ဆောင်မှုများသို့ ဦးတည်ပေးသည်။

အောက်ပါ ပုံက MCP ၏ စုံလင်သော အဆောက်အအုံတွင် sampling နှင့် routing များ ဘယ်လို ပူးပေါင်းလုပ်ဆောင်ကြောင်း ဖော်ပြထားသည်-

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

## နောက်တစ်ဆင့်

- [5.6 Sampling](../mcp-sampling/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
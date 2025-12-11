<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f12fc94cee9ed16a5eddf9f51fba755",
  "translation_date": "2025-12-11T16:36:39+00:00",
  "source_file": "04-PracticalImplementation/samples/javascript/README.md",
  "language_code": "te"
}
-->
# Sample

ఇది MCP సర్వర్ కోసం ఒక జావాస్క్రిప్ట్ నమూనా

ఇక్కడ ఒక టూల్ రిజిస్ట్రేషన్ ఉదాహరణ ఉంది, ఇందులో మేము LLM కు మాక్ కాల్ చేసే టూల్‌ను రిజిస్టర్ చేస్తాము:

```javascript
this.mcpServer.tool(
    'completion',
    {
    model: z.string(),
    prompt: z.string(),
    options: z.object({
        temperature: z.number().optional(),
        max_tokens: z.number().optional(),
        stream: z.boolean().optional()
    }).optional()
    },
    async ({ model, prompt, options }) => {
    console.log(`Processing completion request for model: ${model}`);
    
    // మోడల్‌ను ధృవీకరించండి
    if (!this.models.includes(model)) {
        throw new Error(`Model ${model} not supported`);
    }
    
    // మానిటరింగ్/మెట్రిక్స్ కోసం ఈవెంట్‌ను విడుదల చేయండి
    this.events.emit('request', { 
        type: 'completion', 
        model, 
        timestamp: new Date() 
    });
    
    // నిజమైన అమలులో, ఇది AI మోడల్‌ను పిలుస్తుంది
    // ఇక్కడ మేము అభ్యర్థన భాగాలను మాక్ ప్రతిస్పందనతో తిరిగి ఇస్తాము
    const response = {
        id: `mcp-resp-${Date.now()}`,
        model,
        text: `This is a response to: ${prompt.substring(0, 30)}...`,
        usage: {
        promptTokens: prompt.split(' ').length,
        completionTokens: 20,
        totalTokens: prompt.split(' ').length + 20
        }
    };
    
    // నెట్‌వర్క్ ఆలస్యం అనుకరించండి
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // పూర్తి ఈవెంట్‌ను విడుదల చేయండి
    this.events.emit('completion', {
        model,
        timestamp: new Date()
    });
    
    return {
        content: [
        {
            type: 'text',
            text: JSON.stringify(response)
        }
        ]
    };
    }
);
```

## ఇన్‌స్టాల్ చేయండి

క్రింది కమాండ్‌ను నడపండి:

```bash
npm install
```

## నడపండి

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులుండవచ్చు. మూల డాక్యుమెంట్ దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
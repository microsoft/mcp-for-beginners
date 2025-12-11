<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f7a8ffd07682d554929968dfc6ae2ecb",
  "translation_date": "2025-12-11T16:34:05+00:00",
  "source_file": "04-PracticalImplementation/samples/typescript/README.md",
  "language_code": "kn"
}
-->
# ಮಾದರಿ

ಇದು MCP ಸರ್ವರ್‌ಗಾಗಿ ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್ ಮಾದರಿಯಾಗಿದೆ

ಇಲ್ಲಿ ಒಂದು ಸಾಧನ ರಚನೆಯ ಉದಾಹರಣೆ ಇದೆ:

```typescript
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

    // ಮಾದರಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
    if (!this.models.includes(model)) {
        throw new Error(`Model ${model} not supported`);
    }

    // ಮಾನಿಟರಿಂಗ್/ಮೆಟ್ರಿಕ್ಸ್‌ಗಾಗಿ ಘಟನೆ ಹೊರತುಮಾಡಿ
    this.events.emit('request', { 
        type: 'completion', 
        model, 
        timestamp: new Date() 
    });

    // ನಿಜವಾದ ಅನುಷ್ಠಾನದಲ್ಲಿ, ಇದು AI ಮಾದರಿಯನ್ನು ಕರೆಮಾಡುತ್ತದೆ
    // ಇಲ್ಲಿ ನಾವು ವಿನಂತಿಯ ಭಾಗಗಳನ್ನು ನಕಲಿ ಪ್ರತಿಕ್ರಿಯೆಯೊಂದಿಗೆ ಮಾತ್ರ ಪ್ರತಿಧ್ವನಿಸುತ್ತೇವೆ
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

    // ಜಾಲತಾಣ ವಿಳಂಬವನ್ನು ಅನುಕರಿಸಿ
    await new Promise(resolve => setTimeout(resolve, 500));

    // ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ ಘಟನೆ ಹೊರತುಮಾಡಿ
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

## ಸ್ಥಾಪನೆ

ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```bash
npm install
```

## ಚಾಲನೆ

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
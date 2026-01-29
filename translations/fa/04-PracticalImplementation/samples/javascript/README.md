# نمونه

این یک نمونه جاوااسکریپت برای یک سرور MCP است

در اینجا مثالی از ثبت یک ابزار آورده شده است که در آن ابزاری را ثبت می‌کنیم که یک تماس ساختگی با یک LLM برقرار می‌کند:

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
    
    // Validate model
    if (!this.models.includes(model)) {
        throw new Error(`Model ${model} not supported`);
    }
    
    // Emit event for monitoring/metrics
    this.events.emit('request', { 
        type: 'completion', 
        model, 
        timestamp: new Date() 
    });
    
    // In a real implementation, this would call an AI model
    // Here we just echo back parts of the request with a mock response
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
    
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Emit completion event
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

## نصب

دستور زیر را اجرا کنید:

```bash
npm install
```

## اجرا

```bash
npm start
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
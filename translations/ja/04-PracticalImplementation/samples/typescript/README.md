# サンプル

これはMCPサーバー用のTypeScriptサンプルです

ツール作成の例はこちら：

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

## インストール

以下のコマンドを実行してください：

```bash
npm install
```

## 実行

```bash
npm start
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
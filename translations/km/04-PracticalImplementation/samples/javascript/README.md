# គំរូ

នេះគឺជា​គំរូ JavaScript សម្រាប់​ម៉ាស៊ីន​បម្រើ MCP

នេះ​គឺជាឧទាហរណ៍នៃ​ការចុះឈ្មោះ​ឧបករណ៍ ដែល​យើង​ចុះឈ្មោះឧបករណ៍​មួយ​ដែលធ្វើ​ការហៅ​ចម្លែក​ទៅកាន់ LLM៖

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
    
    // ត្រួតពិនិត្យម៉ូដែល
    if (!this.models.includes(model)) {
        throw new Error(`Model ${model} not supported`);
    }
    
    // ផ្សាយព្រឹត្តិការណ៍សម្រាប់ត្រួតពិនិត្យ/មេត្រិច
    this.events.emit('request', { 
        type: 'completion', 
        model, 
        timestamp: new Date() 
    });
    
    // ក្នុងការអនុវត្តជាក់ស្តែង នេះនឹងហៅម៉ូដែល AI
    // នៅទីនេះយើងគ្រាន់តែតបស្នើសុំជាមួយចម្លើយក្លែងក្លាយ
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
    
    // សន្ទនា ពេលយឺតបណ្តាញ
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // ផ្សាយព្រឹត្តិការណ៍បញ្ចប់
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

## ដំឡើង

រត់ពាក្យបញ្ជាខាងក្រោម៖

```bash
npm install
```

## ដំណើរការ

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការប្រកាសច្បាស់**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ប៉ុន្តែនៅពេលដែលយើងខិតខំរក្សាបានភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យក័ន្ធអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមួយដែលវាត្រូវបានសរសេរជាមូលដ្ឋានគួរត្រូវបានគេរាប់បញ្ចូលថាជា ប្រភពផ្លូវការដែលមានសិទ្ធិ។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ សូមផ្តល់អនុសាសន៍ឲ្យប្រើការបកប្រែដោយមុខរូបមនុស្សដែលមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកកំណត់ខុសឆ្គងណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
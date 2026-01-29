# यो नमुना चलाउनुहोस्

> [!NOTE]
> यो नमुना मान्छ कि तपाईं GitHub Codespaces प्रयोग गर्दै हुनुहुन्छ। यदि तपाईंले यो स्थानीय रूपमा चलाउन चाहनुहुन्छ भने, तपाईंले GitHub मा व्यक्तिगत पहुँच टोकन (PAT) सेटअप गर्न आवश्यक छ।
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## पुस्तकालयहरू स्थापना गर्नुहोस्

```sh
dotnet restore
```

तलका पुस्तकालयहरू स्थापना गर्नुपर्छ: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## चलाउनुहोस्

```sh 
dotnet run
```

तपाईंले निम्न जस्तो आउटपुट देख्नु पर्नेछ:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

धेरै आउटपुट डिबगिङका लागि हो तर महत्वपूर्ण कुरा यो हो कि तपाईं MCP Server बाट उपकरणहरू सूचीबद्ध गर्दै हुनुहुन्छ, तीलाई LLM उपकरणहरूमा परिणत गर्दै हुनुहुन्छ र अन्ततः MCP क्लाइन्ट प्रतिक्रिया "Sum 6" प्राप्त गर्दै हुनुहुन्छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
# हा नमुना चालवा

> [!NOTE]
> हा नमुना गिटहब कोडस्पेसेस इंस्टन्स वापरत असल्याचे गृहीत धरतो. जर तुम्हाला हा स्थानिकपणे चालवायचा असेल, तर तुम्हाला GitHub वर वैयक्तिक प्रवेश टोकन (PAT) सेट करावे लागेल.
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

## लायब्ररी इन्स्टॉल करा

```sh
dotnet restore
```

खालील लायब्ररी इन्स्टॉल कराव्यात: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## चालवा

```sh 
dotnet run
```

तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

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

आउटपुटमधील बरेच काही फक्त डिबगिंगसाठी आहे, पण महत्त्वाचे म्हणजे तुम्ही MCP सर्व्हरमधून टूल्सची यादी करत आहात, त्यांना LLM टूल्समध्ये रूपांतरित करत आहात आणि शेवटी तुम्हाला MCP क्लायंटचा प्रतिसाद "Sum 6" मिळतो.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
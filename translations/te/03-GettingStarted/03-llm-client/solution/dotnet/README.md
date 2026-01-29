# ఈ నమూనాను నడపండి

> [!NOTE]
> ఈ నమూనా మీరు GitHub Codespaces ఉదాహరణను ఉపయోగిస్తున్నారని అనుకుంటుంది. మీరు దీన్ని స్థానికంగా నడపాలనుకుంటే, GitHub లో వ్యక్తిగత యాక్సెస్ టోకెన్ (PAT) సెట్ చేయాలి.
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

## లైబ్రరీలను ఇన్‌స్టాల్ చేయండి

```sh
dotnet restore
```

క్రింది లైబ్రరీలను ఇన్‌స్టాల్ చేయాలి: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## నడపండి

```sh 
dotnet run
```

మీరు ఈ విధంగా అవుట్‌పుట్ చూడాలి:

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

అధిక భాగం అవుట్‌పుట్ డీబగ్గింగ్ మాత్రమే కానీ ముఖ్యమైనది మీరు MCP సర్వర్ నుండి టూల్స్ జాబితా చేస్తున్నారని, వాటిని LLM టూల్స్ గా మార్చడం మరియు మీరు MCP క్లయింట్ స్పందన "Sum 6" పొందడం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
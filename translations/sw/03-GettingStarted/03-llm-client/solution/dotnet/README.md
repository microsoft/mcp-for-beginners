# Endesha sampuli hii

> [!NOTE]
> Sampuli hii inadhani unatumia mfano wa GitHub Codespaces. Ikiwa unataka kuendesha hii kwa ndani ya kompyuta yako, unahitaji kuanzisha tokeni ya upatikanaji binafsi (PAT) kwenye GitHub.
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

## Sakinisha maktaba

```sh
dotnet restore
```

Inapaswa kusakinisha maktaba zifuatazo: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## Endesha

```sh 
dotnet run
```

Unapaswa kuona matokeo yanayofanana na:

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

Sehemu kubwa ya matokeo ni kwa ajili ya utambuzi wa makosa lakini kinachojali ni kwamba unataja zana kutoka kwa MCP Server, kuzibadilisha kuwa zana za LLM na mwisho unapata jibu la mteja wa MCP "Sum 6".

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
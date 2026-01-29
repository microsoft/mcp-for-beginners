# ഈ സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക

> [!NOTE]
> ഈ സാമ്പിൾ നിങ്ങൾ GitHub Codespaces ഇൻസ്റ്റൻസ് ഉപയോഗിക്കുന്നതായി കരുതുന്നു. നിങ്ങൾ ഇത് ലോക്കലായി പ്രവർത്തിപ്പിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, GitHub-ൽ ഒരു വ്യക്തിഗത ആക്‌സസ് ടോക്കൺ (PAT) സജ്ജീകരിക്കേണ്ടതുണ്ട്.
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

## ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```sh
dotnet restore
```

താഴെപ്പറയുന്ന ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യണം: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## പ്രവർത്തിപ്പിക്കുക

```sh 
dotnet run
```

നിങ്ങൾക്ക് താഴെപോലൊരു ഔട്ട്പുട്ട് കാണാം:

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

ഏറെയുള്ള ഔട്ട്പുട്ട് ഡീബഗ്ഗിംഗിനായാണ്, എന്നാൽ പ്രധാനമായത് നിങ്ങൾ MCP സെർവറിൽ നിന്നുള്ള ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുകയാണ്, അവ LLM ടൂളുകളാക്കി മാറ്റുന്നു, അതിനുശേഷം നിങ്ങൾക്ക് MCP ക്ലയന്റ് പ്രതികരണം "Sum 6" ലഭിക്കുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
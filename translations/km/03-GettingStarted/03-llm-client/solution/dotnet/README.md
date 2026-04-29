# រត់គំរូនេះ

> [!NOTE]
> គំរូនេះសន្មត់ថាអ្នកកំពុងប្រើប្រាស់ instance GitHub Codespaces ។ ប្រសិនបើអ្នកចង់រត់វាជាន់ខាងក្នុងអ្នកត្រូវតែតំឡើងប៊ិចសញ្ញា <Personal Access Token> (PAT) នៅលើ GitHub។
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

## តំឡើងបណ្ណាល័យ

```sh
dotnet restore
```

គួរតែតំឡើងបណ្ណាល័យដូចខាងក្រោម៖ Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## រត់

```sh 
dotnet run
```

អ្នកគួរតែឃើញលទ្ធផលដូចជា៖

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

ច្រើននៃលទ្ធផលគឺសម្រាប់បញ្ឆោតកំហុស ប៉ុន្តេចំណុចសំខាន់គឺអ្នកកំពុងរាយបញ្ជីឧបករណ៍ពី MCP Server បម្លែងវាទៅជាឧបករណ៍ LLM ហើយអ្នកទទួលបានចម្លើយ MCP client "Sum 6"។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែជាមួយសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំដើម្បីឱ្យបានភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬចំនុចខុសឆ្គង។ ឯកសារដើមនៅក្នុងភាសាមង្កត់ដៃគួរត្រូវបានចាត់ទុកជាមូលដ្ឋានដែលមានសិទ្ធិអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
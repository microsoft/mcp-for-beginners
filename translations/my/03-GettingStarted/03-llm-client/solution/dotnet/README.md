# ဒီနမူနာကို chạy လုပ်ပါ

> [!NOTE]
> ဒီနမူနာမှာ GitHub Codespaces instance ကို သုံးထားတယ်လို့ သတ်မှတ်ထားပါတယ်။ ဒါကို ကိုယ်ပိုင်စက်မှာ chạy လုပ်ချင်ရင် GitHub ပေါ်မှာ personal access token (PAT) တစ်ခု ပြင်ဆင်ထားဖို့ လိုပါတယ်။
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

## စာကြည့်တိုက်များ ထည့်သွင်းခြင်း

```sh
dotnet restore
```

အောက်ပါ စာကြည့်တိုက်များကို ထည့်သွင်းရမယ် - Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## chạy လုပ်ခြင်း

```sh 
dotnet run
```

အောက်ပါအတိုင်း output ကို တွေ့ရပါမယ် -

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

output အများစုက debugging အတွက်ပဲ ဖြစ်ပေမယ့် အရေးကြီးတာက MCP Server ကနေ tools တွေကို စာရင်းပြုစုပြီး၊ အဲဒီ tools တွေကို LLM tools အဖြစ် ပြောင်းပြီး MCP client ရဲ့ "Sum 6" ဆိုတဲ့ တုံ့ပြန်ချက်ကို ရရှိတာပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
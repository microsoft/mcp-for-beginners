# Chainlit နှင့် Microsoft Learn Docs MCP ဖြင့် သင်ကြားမှုအစီအစဉ် ဖန်တီးခြင်း

## လိုအပ်ချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- pip (Python package manager)
- Microsoft Learn Docs MCP server သို့ ချိတ်ဆက်ရန် အင်တာနက်

## တပ်ဆင်ခြင်း

1. ဒီ repository ကို clone လုပ်ပါ သို့မဟုတ် project ဖိုင်များကို download လုပ်ပါ။
2. လိုအပ်သော dependencies များကို တပ်ဆင်ပါ။

   ```bash
   pip install -r requirements.txt
   ```

## အသုံးပြုခြင်း

### အခြေအနေ ၁: Docs MCP သို့ ရိုးရိုး Query ပေးခြင်း
Docs MCP server သို့ ချိတ်ဆက်ပြီး query ပေးကာ ရလဒ်ကို print လုပ်ပေးသော command-line client တစ်ခု။

1. script ကို run လုပ်ပါ။
   ```bash
   python scenario1.py
   ```
2. prompt တွင် သင်၏ documentation မေးခွန်းကို ထည့်သွင်းပါ။

### အခြေအနေ ၂: သင်ကြားမှုအစီအစဉ် ဖန်တီးခြင်း (Chainlit Web App)
Chainlit ကို အသုံးပြုသော web-based interface တစ်ခုဖြစ်ပြီး သင်ကြားမှုအကြောင်းအရာတစ်ခုအတွက် တစ်ပတ်စီ အစီအစဉ်ကို ကိုယ်ပိုင်ဖန်တီးနိုင်သည်။

1. Chainlit app ကို စတင်ပါ။
   ```bash
   chainlit run scenario2.py
   ```
2. terminal တွင် ပေးထားသော local URL (ဥပမာ - http://localhost:8000) ကို browser တွင် ဖွင့်ပါ။
3. chat window တွင် သင်ကြားမှုအကြောင်းအရာနှင့် သင်ကြားလိုသော အပတ်အရေအတွက်ကို ထည့်သွင်းပါ (ဥပမာ - "AI-900 certification, 8 weeks")။
4. app သည် Microsoft Learn documentation နှင့် သက်ဆိုင်သော တစ်ပတ်စီ အစီအစဉ်ကို ပြန်လည်ပေးပါမည်။

**လိုအပ်သော Environment Variables:**

အခြေအနေ ၂ (Azure OpenAI ဖြင့် Chainlit web app) ကို အသုံးပြုရန် `.env` ဖိုင်ကို `python` directory တွင် ဖန်တီးပြီး အောက်ပါ environment variables များကို သတ်မှတ်ရမည်။

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

ဒီ values များကို Azure OpenAI resource details ဖြင့် ဖြည့်စွက်ပြီး app ကို run လုပ်ပါ။

> [!TIP]
> [Azure AI Foundry](https://ai.azure.com/) ကို အသုံးပြု၍ သင်၏ ကိုယ်ပိုင် models များကို အလွယ်တကူ deploy လုပ်နိုင်သည်။

### အခြေအနေ ၃: VS Code တွင် MCP Server ဖြင့် Docs ကို အသုံးပြုခြင်း

Browser tabs များကို ပြောင်းရန် မလိုဘဲ Microsoft Learn Docs ကို VS Code တွင် တိုက်ရိုက် အသုံးပြုနိုင်သည်။ ဒါဟာ အောက်ပါအတိုင်း အကျိုးကျေးဇူးများပေးသည်။
- VS Code တွင် coding environment ထဲမှ documentation ကို ရှာဖွေဖတ်ရှုနိုင်သည်။
- README သို့မဟုတ် course ဖိုင်များတွင် reference links များကို တိုက်ရိုက် ထည့်သွင်းနိုင်သည်။
- GitHub Copilot နှင့် MCP ကို ပေါင်းစပ်အသုံးပြု၍ documentation workflow ကို AI-powered အဖြစ် seamless ဖြစ်စေသည်။

**အသုံးပြုမှု ဥပမာများ:**
- README တွင် reference links များကို အလျင်အမြန် ထည့်သွင်းခြင်း။
- Copilot ကို အသုံးပြု၍ code ဖန်တီးပြီး MCP ကို documentation ရှာဖွေဖတ်ရှုရန် အသုံးပြုခြင်း။
- editor တွင် အာရုံစိုက်ပြီး ထိရောက်မှုကို မြှင့်တင်ခြင်း။

> [!IMPORTANT]
> သင်၏ workspace တွင် [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration တစ်ခုရှိရန် သေချာပါ (တည်နေရာမှာ `.vscode/mcp.json` ဖြစ်သည်)။

## အခြေအနေ ၂ အတွက် Chainlit ကို ရွေးချယ်ရသည့် အကြောင်းအရင်း

Chainlit သည် conversational web applications ဖန်တီးရန် အခေတ်မီ open-source framework တစ်ခုဖြစ်သည်။ Microsoft Learn Docs MCP server နှင့် backend services များကို ချိတ်ဆက်ထားသော chat-based user interfaces များကို အလွယ်တကူ ဖန်တီးနိုင်သည်။ ဒီ project သည် Chainlit ကို အသုံးပြု၍ ကိုယ်ပိုင် သင်ကြားမှုအစီအစဉ်ကို အချိန်နှင့်တပြေးညီ ဖန်တီးနိုင်သော interactive နည်းလမ်းကို ပေးသည်။ Chainlit ကို အသုံးပြုခြင်းအားဖြင့် chat-based tools များကို အလျင်အမြန် ဖန်တီးပြီး productivity နှင့် သင်ယူမှုကို မြှင့်တင်နိုင်သည်။

## ဒီ app ဘာလုပ်ပေးသလဲ

ဒီ app သည် သင်ကြားမှုအကြောင်းအရာနှင့် အချိန်ကာလကို ရိုက်ထည့်ခြင်းဖြင့် ကိုယ်ပိုင် သင်ကြားမှုအစီအစဉ်ကို ဖန်တီးပေးသည်။ app သည် သင်၏ input ကို parse လုပ်ပြီး Microsoft Learn Docs MCP server ကို query ပေးကာ သက်ဆိုင်သော content များကို ရှာဖွေပြီး တစ်ပတ်စီ structured အစီအစဉ်အဖြစ် စီစဉ်ပေးသည်။ တစ်ပတ်စီ၏ အကြံပြုချက်များကို chat တွင် ပြသပေးပြီး သင်၏ တိုးတက်မှုကို လွယ်ကူစွာ လိုက်နာနိုင်သည်။ ဒီ integration သည် သင်၏ သင်ယူမှုအတွက် အရေးပါသော အရင်းအမြစ်များကို အမြဲတမ်း update ဖြစ်စေသည်။

## Query ဥပမာများ

chat window တွင် အောက်ပါ queries များကို စမ်းသုံးပါ။

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

ဒီဥပမာများသည် သင်ကြားမှုရည်မှန်းချက်များနှင့် အချိန်ကာလများအတွက် app ၏ flexibility ကို ပြသသည်။

## References

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
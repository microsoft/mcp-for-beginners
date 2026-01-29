# Azure Content Safety ဖြင့် အဆင့်မြင့် MCP လုံခြုံရေး

Azure Content Safety သည် သင့် MCP အကောင်အထည်ဖော်မှုများ၏ လုံခြုံရေးကို တိုးတက်စေမည့် အင်အားကြီးကိရိယာများစွာကို ပံ့ပိုးပေးပါသည်။

## Prompt Shields

Microsoft ၏ AI Prompt Shields သည် တိုက်ရိုက်နှင့် အတိုက်မရောက်သော prompt injection တိုက်ခိုက်မှုများကို အောက်ပါနည်းလမ်းများဖြင့် ခိုင်မာစွာကာကွယ်ပေးပါသည်-

1. **အဆင့်မြင့် ရှာဖွေမှု** - မကောင်းသောညွှန်ကြားချက်များကို အကြောင်းအရာထဲတွင် ထည့်သွင်းထားသည်ကို စက်သင်ယူမှုဖြင့် ရှာဖွေသည်။
2. **အလင်းပြခြင်း** - AI စနစ်များအတွက် မှန်ကန်သောညွှန်ကြားချက်များနှင့် ပြင်ပထည့်သွင်းချက်များကို ခွဲခြားနိုင်ရန် အထောက်အကူပြုရန် စာသားကို ပြောင်းလဲပေးသည်။
3. **Delimiters နှင့် Datamarking** - ယုံကြည်ရသော ဒေတာနှင့် မယုံကြည်ရသော ဒေတာအကြား နယ်နိမိတ်များကို အမှတ်အသားပြုသည်။
4. **Content Safety ပေါင်းစပ်မှု** - Azure AI Content Safety နှင့် ပူးပေါင်း၍ jailbreak ကြိုးစားမှုများနှင့် အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေသည်။
5. **ဆက်လက် အပ်ဒိတ်များ** - Microsoft သည် ဖြစ်ပေါ်လာသော အန္တရာယ်အသစ်များအတွက် ကာကွယ်မှုစနစ်များကို ပုံမှန် အပ်ဒိတ်လုပ်ပေးသည်။

## MCP နှင့် Azure Content Safety ကို အကောင်အထည်ဖော်ခြင်း

ဤနည်းလမ်းသည် အလွှာအများအပြားဖြင့် ကာကွယ်မှုကို ပေးပါသည်-
- အလုပ်လုပ်မတိုင်မီ ထည့်သွင်းချက်များကို စစ်ဆေးခြင်း
- ပြန်လည်ထုတ်ပေးမည့် အချက်အလက်များကို အတည်ပြုခြင်း
- သိရှိထားသော အန္တရာယ်ရှိသော ပုံစံများအတွက် blocklists အသုံးပြုခြင်း
- Azure ၏ ဆက်လက် အပ်ဒိတ်လုပ်နေသော content safety မော်ဒယ်များကို အသုံးပြုခြင်း

## Azure Content Safety အရင်းအမြစ်များ

သင့် MCP ဆာဗာများတွင် Azure Content Safety ကို အကောင်အထည်ဖော်ရန် ပိုမိုသိရှိလိုပါက အောက်ပါ တရားဝင် အရင်းအမြစ်များကို ကြည့်ရှုနိုင်ပါသည်-

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety အတွက် တရားဝင် စာတမ်းများ။
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - prompt injection တိုက်ခိုက်မှုများကို ကာကွယ်နည်းများ။
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety ကို အကောင်အထည်ဖော်ရာတွင် အသုံးပြုနိုင်သော API အသေးစိတ်။
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ဖြင့် အမြန်ဆုံး အကောင်အထည်ဖော်ခြင်း လမ်းညွှန်။
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - အမျိုးမျိုးသော programming ဘာသာစကားများအတွက် client libraries များ။
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - jailbreak ကြိုးစားမှုများကို ရှာဖွေကာကွယ်နည်း။
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - content safety ကို ထိရောက်စွာ အကောင်အထည်ဖော်ရန် အကောင်းဆုံး လုပ်ထုံးလုပ်နည်းများ။

ပိုမိုအသေးစိတ် အကောင်အထည်ဖော်မှုအတွက် ကျွန်ုပ်တို့၏ [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) ကို ကြည့်ရှုနိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
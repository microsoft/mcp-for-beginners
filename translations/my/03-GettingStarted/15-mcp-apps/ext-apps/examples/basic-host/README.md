# နမူနာ - အခြေခံ Host

MCP ဆာဗာများနှင့် ချိတ်ဆက်ပြီး တပ်ဆင်လုံခြုံသော sandbox တွင် ကိရိယာ UI များကို ပြသသည့် MCP host အက်ပလီကေးရှင်းကို တည်ဆောက်နည်း ကို ပြသသည့် ကိစ္စရပ်အကြောင်း။

ဒီ အခြေခံ host ကိုလည်း ဒေသီးယားဖွံ့ဖြိုးတိုးတက်မှုအတွင်း MCP Apps များကို စမ်းသပ်ရန်အသုံးပြုနိုင်သည်။

## အဓိကဖိုင်များ

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - ကိရိယာ ရွေးချယ်မှု၊ ပါရာမီတာထည့်သွင်းမှုနှင့် iframe စီမံခန့်ခွဲမှု ရှိသော React UI host
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - လုံခြုံရေးအတည်ပြုခြင်းနှင့် နှစ်ဖက်စာတိုက် ပို့ဆောင်မှု ရှိသော အပြင်အက်ဖရေမ်း proxy
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - ကိုးရီး logic: ဆာဗာချိတ်ဆက်မှု၊ ကိရိယာခေါ်ဆိုမှုနှင့် AppBridge တည်ဆောက်မှု

## စတင်ရန်

```bash
npm install
npm run start
# http://localhost:8080 ကို ဖွင့်ပါ။
```

စံနှုန်းအနေဖြင့် host အက်ပလီကေးရှင်းသည် MCP ဆာဗာသို့ `http://localhost:3001/mcp` မှ ချိတ်ဆက်ရန် ကြိုးစားမည်။ ထိုအပြုအမူကို `SERVERS` environment variable တွင် ဆာဗာ URL များပါသော JSON စာရင်းမှ ပြင်ဆင်နိုင်သည်။

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## စီမံခန့်ခွဲမှုပုံစံ

ဤနမူနာတွင် လုံခြုံသော UI လွတ်လပ်မှုအတွက် နှစ်ထပ် iframe sandbox ပုံစံကို အသုံးပြုထားသည်။

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**iframe နှစ်ခုလောက်တွင် မည်သို့?**

- အပြင်ဖရေမ်း iframe သည် သီးခြား origin (port 8081) တွင် လည်ပတ်ပြီး host သို့ တိုက်ရိုက်ဝင်ရောက်မှုကို ကန့်သတ်သည်
- အတွင်း iframe သည် `srcdoc` မှ HTML ကို လက်ခံပြီး sandbox attribute များဖြင့် ကန့်သတ်ထားသည်
- စာတိုက်ပို့မှုများကို အပြင် iframe မှ ကိစ္စဖြင့် အတည်ပြုပြီး နှစ်ဖက် relay ပြုလုပ်သည်

ဤ စီမံခန့်ခွဲမှုသည် tool UI ကုဒ် အချက်အလက် မကောင်းခဲ့လည်း host အက်ပလီကေးရှင်း၏ DOM၊ ကွန်ကီများ သို့မဟုတ် JavaScript အခြေအနေကို ဝင်ရောက်မရပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ကြေညာချက်**  
ဤစာရွက်ကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းပေမယ့် အလိုအလျောက် ဘာသာပြန်ခြင်းအတွက် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်ကို မိခင်ဘာသာဖြင့် အသိအမှတ်ပြုရမည့် အမြတ်တရ स्रोत အနေဖြင့် သတ်မှတ်ရန် လိုအပ်ပါသည်။ အရေးပေါ် သတင်းအချက်အလက်များအတွက် ဆန်းစစ်ကောင်းမွန်သော လူကိုယ်တိုင် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုမှ ဖြစ်ပေါ်နိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းသဘောထားများအတွက် ကျနော်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# ဤနမူနာကို chạyခြင်း

ဤနမူနာတွင် client ပေါ်တွင် LLM တစ်ခုရှိသည်။ LLM သည် သင်ကို Codespaces တွင် chạyရန် သို့မဟုတ် GitHub တွင် personal access token တစ်ခု စတင်တပ်ဆင်ရန် လိုအပ်သည်။

## -1- လိုအပ်သော dependencies များကို 설치ပါ

```bash
npm install
```

## -3- server ကို chạyပါ

```bash
npm run build
```

## -4- client ကို chạyပါ

```sh
npm run client
```

သင်သည် အောက်ပါအတိုင်း ရလဒ်တစ်ခုကို မြင်ရမည်ဖြစ်သည်-

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
# နမူနာကို အလုပ်လုပ်စေပါ

## လိုအပ်သော dependencies များကို ထည့်သွင်းပါ

```sh
npm install
```

## Build လုပ်ပါ

```sh
npm run build
```

## Token များကို ဖန်တီးပါ

```sh
npm run generate
```

ဒါက *.env* ဖိုင်ထဲမှာ token တစ်ခုကို ဖန်တီးပေးပါမယ်။ Client က ဒီဖိုင်ထဲကနေ ဖတ်မယ်။

## Code ကို အလုပ်လုပ်စေပါ

Server ကို စတင်ရန်:

```sh
npm start
```

Client ကို တခြား terminal မှာ အလုပ်လုပ်စေပါ:

```sh
npm run client
```

Server ရဲ့ terminal မှာ အောက်ပါ output နမူနာကို တွေ့ရပါမယ်:

```text
User exists
User has required scopes
Middleware executed
```

Client ရဲ့ terminal မှာတော့ အောက်ပါ output နမူနာကို တွေ့ရပါမယ်:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### အရာများကို ပြောင်းလဲခြင်း

Scopes တွေကို နားလည်စေဖို့ ကြိုးစားကြမယ်။ *server.ts* ဖိုင်ကို ရှာပြီး ဒီ code ကို ရှာပါ:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

ဒီ code က token ကို "User.Read" ရှိဖို့ လိုအပ်တယ်လို့ ပြောပါတယ်။ ဒါကို "User.Write" လို့ ပြောင်းလိုက်ပါ။ အခု `npm run build` ကို ပြန်လည်လုပ်ပြီး server ကို `npm start` နဲ့ ပြန်စတင်ပါ။ အခုတော့ auth fail ဖြစ်တာကို တွေ့ရပါမယ်၊ အကြောင်းကတော့ ဒီ scope (User.Read နဲ့ Admin.Write) မရှိလို့ပါ။

Client က အခုတော့ ဒီလိုပြောပါတယ်:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

Server ရဲ့ terminal မှာတော့ ဒီလိုပြောပါတယ်:

```text
User exists
```

ဒါနဲ့ ဒီနေရာကို ကျော်မသွားနိုင်ပါဘူး။

"User.Write" scope ကို ထည့်ပြီး `npm run generate` ကို ပြန်လုပ်ပြီး client ကို ပြန်လည်အလုပ်လုပ်စေပါ။ ဒါမှမဟုတ် server code ကို ပြန်လည်ပြောင်းပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
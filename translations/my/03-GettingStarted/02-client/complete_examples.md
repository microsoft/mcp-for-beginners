# MCP Client အပြည့်အစုံ နမူနာများ

ဒီဖိုင်တွင် မတူညီသော programming language များဖြင့် ရေးသားထားသော MCP client များ၏ အပြည့်အစုံ၊ အလုပ်လုပ်နေသော နမူနာများ ပါဝင်သည်။ Client တစ်ခုစီသည် အဓိက README.md သင်ခန်းစာတွင် ဖော်ပြထားသော လုပ်ဆောင်ချက်များအားလုံးကို ပြသထားသည်။

## ရရှိနိုင်သော Client များ

### 1. Java Client (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) over HTTP
- **Target Server**: `http://localhost:8080`
- **Features**:
  - ချိတ်ဆက်မှု စတင်ခြင်းနှင့် ping
  - Tool များစာရင်း
  - Calculator လုပ်ဆောင်ချက်များ (add, subtract, multiply, divide, help)
  - အမှားများကို ကိုင်တွယ်ခြင်းနှင့် ရလဒ်ထုတ်ယူခြင်း

**Run ဖို့:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local .NET MCP server via dotnet run
- **Features**:
  - stdio transport ဖြင့် server ကို အလိုအလျောက် စတင်ခြင်း
  - Tool နှင့် resource များစာရင်း
  - Calculator လုပ်ဆောင်ချက်များ
  - JSON ရလဒ်ကို parse လုပ်ခြင်း
  - အပြည့်အစုံ အမှားကိုင်တွယ်မှု

**Run ဖို့:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transport**: Stdio (Standard Input/Output)
- **Target Server**: Local Node.js MCP server
- **Features**:
  - MCP protocol အားလုံးကို ပံ့ပိုးမှု
  - Tool, resource, နှင့် prompt လုပ်ဆောင်ချက်များ
  - Calculator လုပ်ဆောင်ချက်များ
  - Resource ဖတ်ခြင်းနှင့် prompt အကောင်အထည်ဖော်ခြင်း
  - ခိုင်မာသော အမှားကိုင်တွယ်မှု

**Run ဖို့:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Transport**: Stdio (Standard Input/Output)  
- **Target Server**: Local Python MCP server
- **Features**:
  - Async/await ပုံစံဖြင့် လုပ်ဆောင်မှုများ
  - Tool နှင့် resource ရှာဖွေမှု
  - Calculator လုပ်ဆောင်ချက်များ စမ်းသပ်ခြင်း
  - Resource အကြောင်းအရာ ဖတ်ရှုခြင်း
  - Class အခြေခံ စီမံမှု

**Run ဖို့:**

```bash
python client_example_python.py
```

## Client အားလုံးတွင် ရှိသော ပုံမှန် Features

Client တစ်ခုစီတွင် ပြသထားသည်မှာ:

1. **ချိတ်ဆက်မှု စီမံမှု**
   - MCP server သို့ ချိတ်ဆက်မှု စတင်ခြင်း
   - ချိတ်ဆက်မှု အမှားများကို ကိုင်တွယ်ခြင်း
   - သင့်တော်သော resource စီမံမှုနှင့် ရှင်းလင်းမှု

2. **Server ရှာဖွေမှု**
   - ရရှိနိုင်သော tool များစာရင်း
   - ရရှိနိုင်သော resource များစာရင်း (ပံ့ပိုးထားပါက)
   - ရရှိနိုင်သော prompt များစာရင်း (ပံ့ပိုးထားပါက)

3. **Tool အသုံးပြုမှု**
   - အခြေခံ calculator လုပ်ဆောင်ချက်များ (add, subtract, multiply, divide)
   - Server အချက်အလက်များအတွက် help command
   - သင့်တော်သော argument ပေးပို့ခြင်းနှင့် ရလဒ်ကို ကိုင်တွယ်ခြင်း

4. **အမှားကိုင်တွယ်မှု**
   - ချိတ်ဆက်မှု အမှားများ
   - Tool အကောင်အထည်ဖော်မှု အမှားများ
   - သင့်တော်သော အဆင်မပြေမှုနှင့် အသုံးပြုသူ အကြောင်းကြားမှု

5. **ရလဒ် ကိုင်တွယ်မှု**
   - တုံ့ပြန်မှုများမှ စာသားအကြောင်းအရာ ထုတ်ယူခြင်း
   - ဖတ်ရှုရလွယ်ကူသော output ဖော်ပြမှု
   - မတူညီသော တုံ့ပြန်မှု ပုံစံများကို ကိုင်တွယ်ခြင်း

## လိုအပ်ချက်များ

ဒီ client များကို run မလုပ်မီ သေချာစေရန်:

1. **သင့်လိုအပ်သော MCP server ကို run လုပ်ထားရန်** (`../01-first-server/` မှ)
2. **သင့်ရွေးချယ်သော programming language အတွက် လိုအပ်သော dependencies များကို install လုပ်ထားရန်**
3. **သင့်တော်သော network ချိတ်ဆက်မှု** (HTTP-based transport များအတွက်)

## Implementation များအကြား အဓိက ကွာခြားချက်များ

| Language   | Transport | Server Startup | Async Model | Key Libraries       |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | External       | Sync        | WebFlux, MCP SDK    |
| C#         | Stdio     | Automatic      | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Automatic      | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Automatic      | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Automatic      | Async/Await | Rust MCP SDK, Tokio |

## နောက်တစ်ဆင့်များ

ဒီ client နမူနာများကို စူးစမ်းပြီးနောက်:

1. **Client များကို ပြင်ဆင်ပြီး feature အသစ်များ ထည့်သွင်းပါ**
2. **သင့်ကိုယ်ပိုင် server တစ်ခု ဖန်တီးပြီး ဒီ client များနှင့် စမ်းသပ်ပါ**
3. **မတူညီသော transport များ (SSE နှင့် Stdio) ကို စမ်းသပ်ပါ**
4. **MCP လုပ်ဆောင်ချက်များ ပေါင်းစပ်ထားသော ပိုမိုရှုပ်ထွေးသော application တစ်ခု တည်ဆောက်ပါ**

## ပြဿနာဖြေရှင်းခြင်း

### ပုံမှန် ပြဿနာများ

1. **Connection refused**: MCP server သည် မျှော်မှန်းထားသော port/path တွင် run လုပ်နေကြောင်း သေချာပါစေ
2. **Module not found**: သင့် programming language အတွက် လိုအပ်သော MCP SDK ကို install လုပ်ပါ
3. **Permission denied**: stdio transport အတွက် ဖိုင်ခွင့်များကို စစ်ဆေးပါ
4. **Tool not found**: Server သည် မျှော်မှန်းထားသော tool များကို အကောင်အထည်ဖော်ထားကြောင်း အတည်ပြုပါ

### Debug Tips

1. **သင့် MCP SDK တွင် verbose logging ကို ဖွင့်ပါ**
2. **Server logs ကို စစ်ဆေးပါ** အမှားစာရင်းများအတွက်
3. **Tool အမည်များနှင့် လက်မှတ်များ** client နှင့် server အကြား ကိုက်ညီကြောင်း အတည်ပြုပါ
4. **MCP Inspector ဖြင့် စမ်းသပ်ပါ** server လုပ်ဆောင်ချက်ကို အတည်ပြုရန်

## ဆက်စပ် Documentation

- [Main Client Tutorial](./README.md)
- [MCP Server Examples](../../../../03-GettingStarted/01-first-server)
- [MCP with LLM Integration](../../../../03-GettingStarted/03-llm-client)
- [Official MCP Documentation](https://modelcontextprotocol.io/)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။ 
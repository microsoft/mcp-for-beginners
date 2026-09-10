# ကယ်လ်က्युလိတ်တာ LLM ဖောက်သည်

LangChain4j ကို အသုံးပြု၍ MiniMax OpenAI-ကိုက်ညီသော API မှတဆင့် MCP (Model Context Protocol) ကယ်လ်က्युလိတ်တာ ဝန်ဆောင်မှုသို့ ချိတ်ဆက်သည့် နမူနာ Java အက်ပလီ케ရှင်း။

## လိုအပ်ချက်များ

- Java 21 သို့မဟုတ် အထက်
- Maven 3.6+ (သို့မဟုတ် ပါဝင်သော Maven wrapper ကို သုံးရန်)
- MiniMax API key တစ်ခု
- `http://localhost:8080` တွင် လည်ပတ်နေသော MCP ကယ်လ်က्युလိတ်တာ ဝန်ဆောင်မှု

## API Key ရယူခြင်း

ဤအက်ပလီကေးရှင်းသည် MiniMax OpenAI-ကိုက်ညီသော API ကို အသုံးပြုသည်။ သင်၏ key နှင့် endpoint ရယူရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။

### ၁။ Endpoint ရွေးချယ်ခြင်း
၁။ ကမ္ဘာလုံးဆိုင်ရာ endpoint အတွက် `https://api.minimax.io/v1` ကို သုံးပါ
၂။ တရုတ် endpoint အတွက် `https://api.minimaxi.com/v1` ကို သုံးပါ

### ၂။ API key ဖန်တီးခြင်း
၁။ သင့် MiniMax အကောင့်မှ MiniMax API key တစ်ခု ဖန်တီးပါ
၂။ key ကို လုံခြုံစွာ သိမ်းဆည်းထားပါ

### ၃။ ပတ်ဝန်းကျင် မရောက်မီ variable များ သတ်မှတ်ခြင်း

#### Windows (Command Prompt) မှာ:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell) မှာ:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux မှာ:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## တပ်ဆင်ခြင်းနှင့် စတင်အသုံးပြုခြင်း

၁။ **ပရောဂျက် ဖိုဒါသို့ Clone ရယူ သို့မဟုတ် သွားပါ**

၂။ **လိုအပ်သော dependencies များ တပ်ဆင်ပါ**:
   ```cmd
   mvnw clean install
   ```
   သို့မဟုတ် Maven ကို တစ်နည်းတစ်ပုံဖြင့် သိမ်းဆည်းထားပါက:
   ```cmd
   mvn clean install
   ```

၃။ **ပတ်ဝန်းကျင် မရောက်မီ variable များ သတ်မှတ်ပါ** (အထက်ပါ "API Key ရယူခြင်း" အပိုင်းကြည့်ပါ)

၄။ **MCP ကယ်လ်က्युလိတ်တာ ဝန်ဆောင်မှု စတင်ပါ**:
   chapter 1 ရဲ့ MCP ကယ်လ်က्युလိတ်တာ ဝန်ဆောင်မှုရှိသည့် `http://localhost:8080/sse` တွင် လည်ပတ်နေမှု အတည်ပြုပါ။ ဝန်ဆောင်မှု သွားရောက်ပြီးမှ client ကို စတင်ပါ။

## အက်ပလီကေးရှင်းကို လည်ပတ်ခြင်း

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## အက်ပလီကေးရှင်း၏ လုပ်ဆောင်ချက်

အက်ပလီကေးရှင်းသည် ကယ်လ်က्युလိတ်တာ ဝန်ဆောင်မှုနှင့် ဆက်သွယ်၍ အဓိက အလုပ်လုပ်မှု သုံးခုကို ဖော်ပြသည် -

၁။ **ခြွင်းချက်ပမာဏထုတ်ခြင်း (Addition)**: 24.5 နှင့် 17.3 ၏ စုစုပေါင်းတွက်ချက်ပေးသည်
၂။ **အရွယ်အစားဝိုင်း ပြုလုပ်ခြင်း (Square Root)**: 144 ၏ အရွယ်အစားဝိုင်းတွက်ချက်ပေးသည်
၃။ **အကူအညီ (Help)**: ရရှိနိုင်သော ကယ်လ်ကျူးလိတ်တာ လုပ်ဆောင်ချက်များ ပြသသည်

## မျှော်မှန်းထားသော တုံ့ပြန်မှု

အောင်မြင်စွာ လည်ပတ်သောအခါ အောက်ပါအတိုင်း output တွေ့ရပါမည် -

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ပြဿနာဖြေရှင်းခြင်း

### အသုံးပြုရလွယ်ကူသော ပြဿနာများ

၁။ **"OPENAI_API_KEY environment variable မသတ်မှတ်ရသေး"**
   - `OPENAI_API_KEY` environment variable ကို သတ်မှတ်ခဲ့ပြီး စစ်ဆေးပါ
   - Variable သတ်မှတ်ပြီးနောက် terminal သို့မဟုတ် command prompt ကို ပြန်စတင်ပါ

၂။ **"localhost:8080 သို့ ချိတ်ဆက်မှု ငြင်းဆန်ခြင်း"**
   - MCP ကယ်လ်ကျူးလိတ်တာ ဝန်ဆောင်မှုကို port 8080 တွင် လည်ပတ်နေမှု အတည်ပြုပါ
   - port 8080 ကို အခြားစနစ်တစ်ခုက အသုံးပြုနေနိုင်ခြင်း ရှိမရှိ စစ်ဆေးပါ

၃။ **"အတည်အကျပ် မအောင်မြင်ခြင်း"**
   - သင့် API key မှန်ကန်မှု အတည်ပြုပါ
   - သင့်ရဲ့ `OPENAI_BASE_URL` သည် အသုံးပြုမည့် endpoint နှင့် ကိုက်ညီမှု ရှိနိုင်စေရန် စစ်ဆေးပါ

၄။ **Maven build လုပ်စဉ် ပြဿနာများ**
   - သင့်တွင် Java 21 သို့မဟုတ် အထက်ရှိခြင်း အတည်ပြုရန်: `java -version`
   - Build ကို သန့်ရှင်းရေးလုပ်ရန် ကြိုးစားပါ: `mvnw clean`

### ပဋိညာဉ်ဆန်းစစ်ခြင်း (Debugging)

Debug log များဖွင့်လိုပါက အောက်ပါ JVM argument ကို ပေး၍ လည်ပတ်ပါ -
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ပြင်ဆင်မှုများ

အက်ပလီကေးရှင်းကို အောက်ပါအတိုင်း ဖွဲ့စည်းထားသည် -
- ပုံမှန်အားဖြင့် MiniMax-M3 ကိုအသုံးပြုပါသည်; `MINIMAX_MODEL_ID` ဖြင့် MiniMax-M3 သို့မဟုတ် MiniMax-M2.7 ကိုရွေးချယ်နိုင်ပါသည်
- `OPENAI_BASE_URL` သတ်မှတ်ထားလျှင် အသုံးပြုသည်။ မသတ်မှတ်လျှင် `MINIMAX_REGION=cn_zh` ဖြစ်လျှင် `https://api.minimaxi.com/v1`၊ မဟုတ်လျှင် ကမ္ဘာလုံးဆိုင်ရာ အတွက် `https://api.minimax.io/v1` ကိုအသုံးပြုသည်
- `http://localhost:8080/sse` တွင် MCP ဝန်ဆောင်မှုသို့ ချိတ်ဆက်သည်
- တောင်းဆိုမှုများအတွက် ၆၀ စက္ကန့် Timeout သတ်မှတ်ထားသည်

## မူလအချက်အလက်များ (Dependencies)

ဒီပရောဂျက်တွင် အသုံးပြုသော အဓိက dependency များ -
- **LangChain4j**: AI ပေါင်းစည်းမှုနှင့် ကိရိယာစီမံခန့်ခွဲမှုအတွက်
- **LangChain4j MCP**: Model Context Protocol အတွက် ထောက်ပံ့မှု
- **LangChain4j OpenAI official**: MiniMax OpenAI-ကိုက်ညီသော API ပေါင်းစည်းမှုအတွက်
- **Spring Boot**: အက်ပလီကေးရှင်း ပုံစံနှင့် dependency injection အတွက်

## ရရှိထားသောလိုင်စင်

ဒီပရောဂျက်ကို Apache License 2.0 အောက်မှာလိုင်စင်ပြုထားသည် - အသေးစိတ်အတွက် [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ဖိုင် ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
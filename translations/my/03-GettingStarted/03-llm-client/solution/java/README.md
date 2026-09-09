# ကယ်လ်ကူလေးတာ LLM Client

LangChain4j ကို အသုံးပြုကာ MiniMax OpenAI-compatible API မှတဆင့် MCP (Model Context Protocol) ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှုနှင့် ချိတ်ဆက်ပြသသည့် Java အပလီကေးရှင်းတစ်ခု။

## လိုအပ်ချက်များ

- Java 21 သို့အထက်
- Maven 3.6+ (ဒါမှမဟုတ် ပါဝင်လာသော Maven wrapper ကိုအသုံးပြုပါ)
- MiniMax API key တစ်ခု
- `http://localhost:8080` တွင် ပွင့်နေသော MCP ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှု

## API Key ရယူခြင်း

ဤအပလီကေးရှင်းသည် MiniMax OpenAI-compatible API ကို အသုံးပြုပါသည်။ သင့်၏ key နှင့် endpoint ရယူရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။

### 1. Endpoint ရွေးချယ်ခြင်း
1. ကမ္ဘာလုံးဆိုင်ရာ endpoint အတွက် `https://api.minimax.io/v1` ကို အသုံးပြုပါ
2. တရုတ် endpoint အတွက် `https://api.minimaxi.com/v1` ကို အသုံးပြုပါ

### 2. API key ဖန်တီးခြင်း
1. သင့် MiniMax အကောင့်မှ MiniMax API key သစ်တစ်ခု ဖန်တီးပါ
2. key ကို လုံခြုံစွာထားရှိပါ

### 3. ပတ်ဝန်းကျင် အပြောင်းအလဲများ သတ်မှတ်ခြင်း

#### Windows တွင် (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows တွင် (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux တွင်:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## တပ်ဆင်ခြင်းနှင့် ပြင်ဆင်ခြင်း

1. **ပရောဂျက်ဖိုင်ဒေါင်းလိုက် သို့မဟုတ် ဖိုင်ဒေါ်ခ်တာသို့ သွားပါ**

2. **လိုအပ်သော ပက်ကေ့ဂျ်များ တပ်ဆင်ပါ**:
   ```cmd
   mvnw clean install
   ```
   သို့မဟုတ် Maven ကို အခြေပြု၍ တပ်ဆင်ပါ:
   ```cmd
   mvn clean install
   ```

3. **ပတ်ဝန်းကျင်အပြောင်းအလဲများ သတ်မှတ်ပါ** ("API Key ရယူခြင်း" အပိုဒ်ကို ကြည့်ပါ)

4. **MCP ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှု စတင်လိုက်ပါ**:
   `http://localhost:8080/sse` တွင် တတ်နိုင်သမျှ chapter 1 ၏ MCP ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှုပြေးနေစေလိုက်ပါ။ ဤကွင်းဆက်ပြင်ဆင်ပြီး client ကိုစတင်ပါ။

## အပလီကေးရှင်းကို ပြေးဆွဲခြင်း

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## အပလီကေးရှင်း လုပ်ဆောင်ချက်များ

အပလီကေးရှင်းသည် ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှုနှင့်ပတ်သက်သည့် အဓိက အပြန်အလှန်သုံးခုကို ပြသပါသည်။

1. **ပေါင်းခြင်း**: 24.5 နှင့် 17.3 ကို ပေါင်းခြင်းတွက်ချက်သည်
2. **ရိုးနှင့် အမျိုးအနွယ်**: 144 ၏ အညီတူ ရွှေ့ထုတ်သည်
3. **အကူအညီ**: အသုံးပြုနိုင်သော ကယ်လ်ကူလေးတာ ဖင်ခ်ရှင်းများ ပြပါ

## မျှော်မှန်း ထွက်ရှိမှု

အောင်မြင်စွာ စတင်ပြေးဆွဲပါက အောက်ပါကဲ့သို့သော ထွက်ရှိမှုကို တွေ့ရပါမည်။

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ပြဿနာဖြေရှင်းခြင်း

### ရိုးရိုးရှုံးရှုံး ပြဿနာများ

1. **"OPENAI_API_KEY environment variable သတ်မှတ်ထားခြင်းမရှိပါ"**
   - `OPENAI_API_KEY` ပတ်ဝန်းကျင် သတ်မှတ်ချက် ပြုလုပ်ထားသည်ကို သေချာစေပါ။
   - သတ်မှတ်ပြီးနောက် terminal/command prompt ကို ပြန်စတင်ပါ။

2. **"localhost:8080 သို့ ချိတ်ဆက်မှု ပယ်ချခြင်း"**
   - MCP ကယ်လ်ကူလေးတာ ဝန်ဆောင်မှုသည် port 8080 တွင် ထိန်းသိမ်း ထားမှုရှိသည်ကို သေချာစေပါ။
   - အခြားဝန်ဆောင်မှုတစ်ခုမှ port 8080 ကို အသုံးပြုနေမနေစစ်ဆေးပါ။

3. **"အတည်ပြုလက်မှတ် မအောင်မြင်ခြင်း"**
   - API key သင့်တော်မှုကို အတည်ပြုပါ။
   - သင်ရွေးချယ်ထားသည့် endpoint နှင့် `OPENAI_BASE_URL` သက်ဆိုင်မှုကို စစ်ဆေးပါ။

4. **Maven build အမှားများ**
   - Java 21 သို့အထက်ကို အသုံးပြုနေမှုကို တောင်းဆိုပါ: `java -version`
   - build ကို သန့်ရှင်းစေဖို့ ရှင်းလင်းပါ: `mvnw clean`

### မှားယွင်းချက်ရှာဖွေရေး

debug logging ကိုဖွင့်လိုပါက လည်ပတ်စဉ် JVM argument အောက်ပါအတိုင်း ထည့်ပါ:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ပြင်ဆင်မှုများ

အပလီကေးရှင်းသည် အောက်ပါအတိုင်း ပြင်ဆင်ထားပါသည်။
- ပုံမှန်အားဖြင့် MiniMax-M3 ကို အသုံးပြုသည်၊ သို့မဟုတ် `MINIMAX_MODEL_ID` သတ်မှတ်ထားပါက MiniMax-M2.7 ကို အသုံးပြုသည်။
- `OPENAI_BASE_URL` သတ်မှတ်ထားပါက ၎င်းကို ချိတ်ဆက်သုံးဆောင်၊ မဟုတ်ပါက `MINIMAX_REGION=cn_zh` ဖြစ်ပါက `https://api.minimaxi.com/v1` သို့မဟုတ် ပုံမှန်အားဖြင့် `https://api.minimax.io/v1` ကို သုံးသည်။
- MCP ဝန်ဆောင်မှုကို `http://localhost:8080/sse` တွင် ဆက်သွယ်သည်။
- တောင်းဆိုမှုများအတွက် 60-စက္ကန့် အချိန်ကန့်သတ်ချက်ကို သတ်မှတ်ထားသည်။

## မူလပက္ကေ့ဂျ်များ

ဒီပရောဂျက်တွင် အသုံးပြုထားသော အဓိက မူလပက္ကေ့ဂျ်များ။
- **LangChain4j**: AI ချိတ်ဆက်မှုနှင့် ကိရိယာထိန်းချုပ်မှုအတွက်
- **LangChain4j MCP**: Model Context Protocol ကို ထောက်ပံ့မှုအတွက်
- **LangChain4j OpenAI official**: MiniMax OpenAI-compatible API ချိတ်ဆက်မှုအတွက်
- **Spring Boot**: အပလီကေးရှင်း ဖွဲ့စည်းမှုနှင့် အားထည့်ချက် ထည့်သွင်းမှုအတွက်

## လိုင်စင်

ဤပရောဂျက်ကို Apache License 2.0 အောက်တွင် လိုင်စင်ပြုထားသည် - အသေးစိတ်အတွက် [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ဖိုင်ကို ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Calculator LLM Client

> [!NOTE]
> ဤ ဖြေရှင်းချက်သည် သင်တန်း၏ အဟောင်း HTTP+SSE ကယ်ယူရေးစက်ဝန်ဆောင်မှုနှင့် ချိတ်ဆက်ပြီး
> MCP `2025-11-25` SDK API များကို ရည်ရွယ်သည်။ ၎င်းသည် `2026-07-28` Streamable HTTP
> ဥပမာ မဟုတ်ပါ။

LangChain4j ကို အသုံးပြု၍ MiniMax OpenAI-လိုက်ဖက်သော API မှတဆင့် MCP (Model Context Protocol) ကယ်ယူရေးစက်ဝန်ဆောင်မှုနှင့် ချိတ်ဆက်ပုံကို ဖော်ပြသည့် Java အပလီကေးရှင်းတစ်ခု။

## လိုအပ်ချက်များ

- Java 21 နှင့် အထက်
- Maven 3.6+ (သို့) ထည့်သွင်းထားသော Maven wrapper ကို သုံးပါ
- MiniMax API key တစ်ခု
- MCP ကယ်ယူရေးစက်ဝန်ဆောင်မှု `http://localhost:8080` တွင် လည်ပတ်နေသော

## API Key ရယူနည်း

ဤ အပလီကေးရှင်းသည် MiniMax OpenAI-လိုက်ဖက် API ကို အသုံးပြုသည်။ သင့် key နှင့် endpoint ကို ရရန် အဆင့်များကို လိုက်နာပါ -

### 1. Endpoint ရွေးချယ်ရန်
1. ကမ္ဘာလုံးဆိုင်ရာ endpoint အတွက် `https://api.minimax.io/v1` ကို သုံးပါ
2. တရုတ် endpoint အတွက် `https://api.minimaxi.com/v1` ကို သုံးပါ

### 2. API key ဖန်တီးရန်
1. သင့် MiniMax အကောင့်မှ MiniMax API key တစ်ခု ဖန်တီးပါ
2. key ကို ကိုယ်လုံခြုံစွာ သိမ်းဆည်းထားပါ

### 3. ပတ်ဝန်းကျင်အဆက်အသွယ် များ သတ်မှတ်ရန်

#### Windows (Command Prompt) တွင်:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell) တွင်:
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

1. **ပရောဂျက်ဖိုလ်ဒါသို့ clone ပြုလုပ်မည် (သို့) သွားရောက်မည်**

2. **လိုအပ်သောစာကြည့်တမ်းများ install ပြုလုပ်မည်**:
   ```cmd
   mvnw clean install
   ```
   ဒါမှမဟုတ် Maven ကို ကမ္ဘာလုံးဆိုင်ရာ ဖြည့်သွင်းပြီးသား болса:
   ```cmd
   mvn clean install
   ```

3. **ပတ်ဝန်းကျင်အဆက်အသွယ်များ သတ်မှတ်ရန်** ("Getting the API Key" အပိုင်းကို ကြည့်ပါ)

4. **MCP ကယ်ယူရေးစက်ဝန်ဆောင်မှု ပြေးရန်**:
   သင့်တွင် ပထမအခန်း MCP ကယ်ယူရေးစက်ဝန်ဆောင်မှု `http://localhost:8080/sse` တွင် လည်ပတ်နေသည်ကို သေချာစေပါ။ ၎င်းသည် client ပိတ် လုပ်ရန်မတိုင်မီ ပြေးထားရန်လိုအပ်သည်။

## အပလီကေးရှင်းကို စတင် ပြေးရန်

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## အပလီကေးရှင်း လုပ်ဆောင်ချက်များ

အပလီကေးရှင်းသည် ကယ်ယူရေးစက်ဝန်ဆောင်မှုနှင့် တုံ့ပြန်မှု သုံးမျိုးကို ဖော်ပြသည်-

1. **တိုးခြင်း (Addition)**: 24.5 နှင့် 17.3 တို့၏ ပေါင်းထုတ်ခြင်း
2. **မြစ်မိုင်းခြင်း (Square Root)**: 144 ၏ အမြစ်မိုင်းထုတ်ခြင်း
3. **ကူညီမှု (Help)**: ရရှိနိုင်သော ကယ်ယူရေးစက်လုပ်ဆောင်ချက်များ ပြ မည်

## မျှော်လင့်ထားသော အထွက်

အောင်မြင်စွာ ပြေးစဉ် တွင် အောက်ပါ ကဲ့သို့ အထွက် တွေ့မြင်ရမည် -

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ပြဿနာဖြေရှင်းခြင်း

### အထူးပြဿနာများ

1. **"OPENAI_API_KEY environment variable မသတ်မှတ်ရသေးခြင်း"**
   - `OPENAI_API_KEY` ပတ်ဝန်းကျင်ပြောင်းနိုင်မှုကို သတ်မှတ်ထားသည်ကို သေချာစေပါ
   - ပြောင်းလဲပြီးနောက် terminal/command prompt ကို ပြန်စဖွင့်ပါ

2. **"localhost:8080 သို့ ချိတ်ဆက်မှု ပယ်ဖျက်ခြင်း"**
   - MCP ကယ်ယူရေးစက် ဝန်ဆောင်မှုသည် port 8080 တွင် လည်ပတ်နေသည်ကို သေချာစေပါ
   - အခြားဝန်ဆောင်မှုတစ်ခု port 8080 ကို သုံးနေသည်မဟုတ်ကြောင်း စစ်ဆေးပါ

3. **"အသိအမှတ်ပြုခြင်း မအောင်မြင်ခြင်း"**
   - သင်၏ API key မှန်ကန်ကြောင်း စစ်ဆေးပါ
   - သင်အသုံးပြုရန် ရည်ရွယ်ထားသော endpoint နှင့် `OPENAI_BASE_URL` ကို ကိုက်ညီစေပါ

4. **Maven build အမှားများ**
   - Java 21 သို့ အထက်ကို အသုံးပြုနေသည်ကို သေချာစေပါ: `java -version`
   - build ကို သန့်ရှင်းစေဖို့ စမ်းသပ်ပါ: `mvnw clean`

### ပိုမိုလေ့လာ စစ်ဆေးခြင်း

debug logging အား ဖွင့်လိုလျှင် လည်ပတ်စဉ် JVM argument ကို ထည့်ပါ:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ဖော်ပြချက်များ

အပလီကေးရှင်းအား အောက်ပါအတိုင်း ပြင်ဆင်ထားပါသည် -
- ပုံမှန်အားဖြင့် MiniMax-M3 ကို အသုံးပြုသည်; `MINIMAX_MODEL_ID` ဖြင့် `MiniMax-M3` သို့မဟုတ် `MiniMax-M2.7` ကို ရွေးချယ်နိုင်သည်
- `OPENAI_BASE_URL` သတ်မှတ်ထားလျှင် ချိတ်ဆက်သည်; မဟုတ်ပါက `MINIMAX_REGION=cn_zh` ဖြစ်လျှင် `https://api.minimaxi.com/v1` ကို သုံးပြီး မဟုတ်လျှင် ကမ္ဘာလုံးဆိုင်ရာအဖြစ် `https://api.minimax.io/v1` ကို သုံးသည်
- MCP ဝန်ဆောင်မှုနှင့် `http://localhost:8080/sse` တွင် ချိတ်ဆက်သည်
- တောင်းဆိုမှုများအတွက် ၆၀ စက္ကန့် အချိန်ကုန်ဆုံးမှုရှိသည်

## လိုအပ်ချက်များ

ဒီပရောဂျက်တွင် အသုံးပြုသော အဓိကလိုအပ်ချက်များ -
- **LangChain4j**: AI ပေါင်းစည်းမှု နှင့် ကိရိယာစီမံခန့်ခွဲမှုအတွက်
- **LangChain4j MCP**: Model Context Protocol ကို ထောက်ပံ့ပေးရန်
- **LangChain4j OpenAI official**: MiniMax OpenAI-လိုက်ဖက် API ပေါင်းစည်းမှုအတွက်
- **Spring Boot**: အပလီကေးရှင်း ဖွဲ့စည်းမှုနှင့် မှီခိုမှု ထည့်သွင်းနိုင်မှုအတွက်

## အခွင့်အရေး

ဒီပရောဂျက်ကို Apache License 2.0 အောက်တွင်လိုင်စင်ပြုထားသည် - အသေးစိတ်အတွက် [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ဖိုင်ကို ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
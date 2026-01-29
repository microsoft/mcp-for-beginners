# Calculator LLM Client

LangChain4j ကို အသုံးပြုပြီး MCP (Model Context Protocol) ကိန်းဂဏန်းဝန်ဆောင်မှုနှင့် GitHub Models ပေါင်းစပ်အသုံးပြုနည်းကို Java အပလီကေးရှင်းတစ်ခုဖြင့် ပြသထားသည်။

## လိုအပ်ချက်များ

- Java 21 သို့မဟုတ် အထက်
- Maven 3.6+ (သို့မဟုတ် ပါဝင်သော Maven wrapper ကို အသုံးပြုပါ)
- GitHub Models အသုံးပြုခွင့်ရှိသော GitHub အကောင့်
- `http://localhost:8080` တွင် MCP ကိန်းဂဏန်းဝန်ဆောင်မှု တက်နေခြင်း

## GitHub Token ရယူနည်း

ဤအပလီကေးရှင်းသည် GitHub Models ကို အသုံးပြုသဖြင့် GitHub personal access token လိုအပ်သည်။ Token ရယူရန် အောက်ပါအဆင့်များကို လိုက်နာပါ-

### 1. GitHub Models သို့ ဝင်ရောက်ခြင်း
1. [GitHub Models](https://github.com/marketplace/models) သို့ သွားပါ
2. သင့် GitHub အကောင့်ဖြင့် လော့ဂ်အင် ဝင်ပါ
3. GitHub Models အသုံးပြုခွင့် မရှိသေးပါက တောင်းဆိုပါ

### 2. Personal Access Token ဖန်တီးခြင်း
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) သို့ သွားပါ
2. "Generate new token" → "Generate new token (classic)" ကို နှိပ်ပါ
3. Token အမည်ကို ဖော်ပြပါ (ဥပမာ- "MCP Calculator Client")
4. သတ်မှတ်ချိန်ကာလကို လိုအပ်သလို သတ်မှတ်ပါ
5. အောက်ပါ scopes များကို ရွေးချယ်ပါ-
   - `repo` (ပုဂ္ဂလိက repository များသုံးမည်ဆိုလျှင်)
   - `user:email`
6. "Generate token" ကို နှိပ်ပါ
7. **အရေးကြီး**: Token ကို ချက်ချင်း ကူးယူပါ - နောက်မှ မမြင်ရတော့ပါ!

### 3. ပတ်ဝန်းကျင် အပြောင်းအလဲ သတ်မှတ်ခြင်း

#### Windows (Command Prompt) တွင်:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) တွင်:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux တွင်:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## တပ်ဆင်ခြင်းနှင့် ပြင်ဆင်ခြင်း

1. **Project ဖိုလ်ဒါကို Clone လုပ်ခြင်း သို့မဟုတ် သွားရောက်ခြင်း**

2. **လိုအပ်သော dependency များ ထည့်သွင်းခြင်း**:
   ```cmd
   mvnw clean install
   ```
   သို့မဟုတ် Maven ကို global အနေဖြင့် ထည့်သွင်းထားပါက-
   ```cmd
   mvn clean install
   ```

3. **ပတ်ဝန်းကျင် အပြောင်းအလဲ သတ်မှတ်ခြင်း** (အထက်ပါ "GitHub Token ရယူနည်း" အပိုင်းကို ကြည့်ပါ)

4. **MCP Calculator Service ကို စတင်ပါ**:
   chapter 1 တွင် ဖော်ပြထားသည့် MCP calculator service ကို `http://localhost:8080/sse` တွင် တက်နေစေရန် သေချာပါစေ။ Client ကို စတင်မပြုမီ ဝန်ဆောင်မှုသည် တက်နေသင့်သည်။

## အပလီကေးရှင်းကို လည်ပတ်ခြင်း

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## အပလီကေးရှင်း၏ လုပ်ဆောင်ချက်များ

အဆိုပါ အပလီကေးရှင်းသည် ကိန်းဂဏန်းဝန်ဆောင်မှုနှင့် အဓိက အပြန်အလှန်ဆက်သွယ်မှု ၃ မျိုးကို ပြသသည်-

1. **ပေါင်းခြင်း**: 24.5 နှင့် 17.3 ကို ပေါင်းတွက်ချက်ခြင်း
2. **စတုရန်းမြစ်**: 144 ၏ စတုရန်းမြစ်တွက်ချက်ခြင်း
3. **အကူအညီ**: ရနိုင်သော ကိန်းဂဏန်းလုပ်ဆောင်ချက်များ ပြသခြင်း

## မျှော်မှန်းထားသော အထွက်

အောင်မြင်စွာ လည်ပတ်သောအခါ အောက်ပါအတိုင်း အထွက်ကို တွေ့ရမည်-

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ပြဿနာဖြေရှင်းခြင်း

### ပုံမှန် ဖြစ်ပေါ်တတ်သော ပြဿနာများ

1. **"GITHUB_TOKEN environment variable not set"**
   - `GITHUB_TOKEN` ပတ်ဝန်းကျင်အပြောင်းအလဲ သတ်မှတ်ထားကြောင်း သေချာစေပါ
   - သတ်မှတ်ပြီးနောက် terminal/command prompt ကို ပြန်စတင်ပါ

2. **"Connection refused to localhost:8080"**
   - MCP calculator service သည် port 8080 တွင် တက်နေကြောင်း သေချာစေပါ
   - အခြားဝန်ဆောင်မှုတစ်ခုက port 8080 ကို အသုံးပြုနေမနေ စစ်ဆေးပါ

3. **"Authentication failed"**
   - GitHub token သည် မှန်ကန်ပြီး လိုအပ်သော ခွင့်ပြုချက်များ ရှိကြောင်း စစ်ဆေးပါ
   - GitHub Models အသုံးပြုခွင့် ရှိကြောင်း သေချာစေပါ

4. **Maven build အမှားများ**
   - Java 21 သို့မဟုတ် အထက်ကို အသုံးပြုနေကြောင်း စစ်ဆေးပါ- `java -version`
   - Build ကို သန့်ရှင်းစေပါ- `mvnw clean`

### Debugging

Debug logging ကို ဖွင့်ရန် အောက်ပါ JVM argument ကို အသုံးပြုပါ-
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ဖွဲ့စည်းမှု

အပလီကေးရှင်းသည် အောက်ပါအတိုင်း ဖွဲ့စည်းထားသည်-
- GitHub Models ကို `gpt-4.1-nano` မော်ဒယ်ဖြင့် အသုံးပြုသည်
- MCP ဝန်ဆောင်မှုကို `http://localhost:8080/sse` တွင် ချိတ်ဆက်သည်
- တောင်းဆိုမှုများအတွက် ၆၀ စက္ကန့် အချိန်ကန့်သတ်ထားသည်
- Debugging အတွက် တောင်းဆိုမှု/တုံ့ပြန်မှု မှတ်တမ်းတင်မှု ဖွင့်ထားသည်

## လိုအပ်သော dependency များ

ဤ project တွင် အသုံးပြုသော အဓိက dependency များ-
- **LangChain4j**: AI ပေါင်းစပ်ခြင်းနှင့် ကိရိယာစီမံခန့်ခွဲမှုအတွက်
- **LangChain4j MCP**: Model Context Protocol အထောက်အပံ့အတွက်
- **LangChain4j GitHub Models**: GitHub Models ပေါင်းစပ်ခြင်းအတွက်
- **Spring Boot**: အပလီကေးရှင်း ဖွဲ့စည်းမှုနှင့် dependency injection အတွက်

## လိုင်စင်

ဤ project သည် Apache License 2.0 အောက်တွင် လိုင်စင်ရရှိထားသည် - အသေးစိတ်အချက်အလက်များအတွက် [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ဖိုင်ကို ကြည့်ပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
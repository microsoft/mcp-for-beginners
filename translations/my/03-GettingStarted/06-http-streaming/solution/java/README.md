# Calculator HTTP Streaming Demo

ဤပရောဂျက်သည် Spring Boot WebFlux ဖြင့် Server-Sent Events (SSE) ကို အသုံးပြု၍ HTTP streaming ကို ပြသသည်။ အောက်ပါ အပလီကေးရှင်း နှစ်ခု ပါဝင်သည်-

- **Calculator Server**: တွက်ချက်မှုများ ပြုလုပ်ပြီး SSE ဖြင့် ရလဒ်များကို စီးဆင်းပေးသည့် reactive web service
- **Calculator Client**: streaming endpoint ကို အသုံးပြုသည့် client application

## လိုအပ်ချက်များ

- Java 17 သို့မဟုတ် အထက်
- Maven 3.6 သို့မဟုတ် အထက်

## ပရောဂျက် ဖွဲ့စည်းပုံ

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## လုပ်ဆောင်ပုံ

1. **Calculator Server** သည် `/calculate` endpoint ကို ဖော်ပြပြီး-
   - query parameters များကို လက်ခံသည်- `a` (နံပါတ်), `b` (နံပါတ်), `op` (လုပ်ဆောင်ချက်)
   - ထောက်ခံသော လုပ်ဆောင်ချက်များ- `add`, `sub`, `mul`, `div`
   - တွက်ချက်မှု တိုးတက်မှုနှင့် ရလဒ်များကို Server-Sent Events အဖြစ် ပြန်ပေးပို့သည်

2. **Calculator Client** သည် server နှင့် ချိတ်ဆက်ပြီး-
   - `7 * 5` တွက်ချက်ရန် တောင်းဆိုသည်
   - streaming ဖြင့် ပြန်လာသော တုံ့ပြန်ချက်ကို စားသုံးသည်
   - တစ်ခုချင်းစီသော event များကို console တွင် ပုံနှိပ်ပြသည်

## အပလီကေးရှင်းများကို စတင်အသုံးပြုခြင်း

### ရွေးချယ်စရာ ၁: Maven ဖြင့် (အကြံပြု)

#### ၁။ Calculator Server ကို စတင်ပါ

terminal တစ်ခု ဖွင့်ပြီး server directory သို့ သွားပါ-

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

server သည် `http://localhost:8080` တွင် စတင်လည်ပတ်မည်

အောက်ပါအတိုင်း output ကို မြင်ရမည်-
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### ၂။ Calculator Client ကို လည်ပတ်ပါ

terminal အသစ်တစ်ခု ဖွင့်ပြီး client directory သို့ သွားပါ-

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

client သည် server နှင့် ချိတ်ဆက်ပြီး တွက်ချက်မှုကို ပြုလုပ်ကာ streaming ရလဒ်များကို ပြသမည်။

### ရွေးချယ်စရာ ၂: Java ကို တိုက်ရိုက် အသုံးပြုခြင်း

#### ၁။ server ကို compile ပြီး run ပါ-

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### ၂။ client ကို compile ပြီး run ပါ-

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Server ကို လက်ဖြင့် စမ်းသပ်ခြင်း

web browser သို့မဟုတ် curl ဖြင့် server ကို စမ်းသပ်နိုင်သည်-

### web browser အသုံးပြုခြင်း
သွားရောက်ရန်- `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl အသုံးပြုခြင်း
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## မျှော်မှန်းထားသော output

client ကို run လုပ်သောအခါ streaming output ကို အောက်ပါအတိုင်း မြင်ရမည်-

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## ထောက်ခံသော လုပ်ဆောင်ချက်များ

- `add` - ပေါင်းခြင်း (a + b)
- `sub` - ဖြုတ်ခြင်း (a - b)
- `mul` - မြှောက်ခြင်း (a * b)
- `div` - ခွဲခြင်း (a / b, b = 0 ဖြစ်ပါက NaN ပြန်ပေးသည်)

## API ကို ရည်ညွှန်းချက်

### GET /calculate

**Parameters:**
- `a` (လိုအပ်သည်): ပထမနံပါတ် (double)
- `b` (လိုအပ်သည်): ဒုတိယနံပါတ် (double)
- `op` (လိုအပ်သည်): လုပ်ဆောင်ချက် (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- တွက်ချက်မှု တိုးတက်မှုနှင့် ရလဒ်များကို Server-Sent Events အဖြစ် ပြန်ပေးပို့သည်

**ဥပမာ တောင်းဆိုမှု:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**ဥပမာ တုံ့ပြန်မှု:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## ပြဿနာဖြေရှင်းခြင်း

### ပုံမှန် ဖြစ်ပေါ်နိုင်သော ပြဿနာများ

1. **Port 8080 ကို အခြား application တစ်ခု အသုံးပြုနေခြင်း**
   - port 8080 ကို အသုံးပြုနေသော အခြား application များကို ပိတ်ပါ
   - ဒါမှမဟုတ် `calculator-server/src/main/resources/application.yml` တွင် server port ကို ပြောင်းပါ

2. **ချိတ်ဆက်မှု ပယ်ချခြင်း**
   - client စတင်မလုပ်မီ server သည် လည်ပတ်နေသည်ကို သေချာစေပါ
   - server သည် port 8080 တွင် အောင်မြင်စွာ စတင်လည်ပတ်နေသည်ကို စစ်ဆေးပါ

3. **parameter name ပြဿနာများ**
   - ဤပရောဂျက်တွင် Maven compiler configuration တွင် `-parameters` flag ပါဝင်သည်
   - parameter binding ပြဿနာများ ဖြစ်ပါက ဤ configuration ဖြင့် ပရောဂျက်ကို ပြန်လည်တည်ဆောက်ပါ

### အပလီကေးရှင်းများကို ရပ်တန့်ခြင်း

- တစ်ခုချင်းစီ လည်ပတ်နေသော terminal တွင် `Ctrl+C` ကို နှိပ်ပါ
- ဒါမှမဟုတ် background process အဖြစ် run လျှင် `mvn spring-boot:stop` ကို အသုံးပြုပါ

## နည်းပညာ Stack

- **Spring Boot 3.3.1** - အပလီကေးရှင်း framework
- **Spring WebFlux** - Reactive web framework
- **Project Reactor** - Reactive streams စာကြည့်တိုက်
- **Netty** - Non-blocking I/O server
- **Maven** - Build tool
- **Java 17+** - Programming language

## နောက်တစ်ဆင့်များ

ကုဒ်ကို ပြင်ဆင်ကြည့်ပါ-
- သင်္ချာဆိုင်ရာ လုပ်ဆောင်ချက်များ ပိုမိုထည့်သွင်းရန်
- မှားယွင်းသော လုပ်ဆောင်ချက်များအတွက် error handling ထည့်သွင်းရန်
- တောင်းဆိုမှု/တုံ့ပြန်မှု logging ထည့်သွင်းရန်
- authentication ကို အကောင်အထည်ဖော်ရန်
- unit test များ ထည့်သွင်းရန်

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
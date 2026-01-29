# MCP Java Client - ကိန်းဂဏန်းတွက်စက် မျှဝေမှု

ဤပရောဂျက်သည် MCP (Model Context Protocol) ဆာဗာနှင့် ချိတ်ဆက်ပြီး အပြန်အလှန် ဆက်သွယ်နိုင်သော Java client တစ်ခုကို ဖန်တီးပုံကို ပြသသည်။ ဤဥပမာတွင် Chapter 01 မှ ကိန်းဂဏန်းတွက်စက် ဆာဗာနှင့် ချိတ်ဆက်ကာ အမျိုးမျိုးသော သင်္ချာဆိုင်ရာ လုပ်ဆောင်ချက်များကို ပြုလုပ်မည်ဖြစ်သည်။

## လိုအပ်ချက်များ

ဤ client ကို စတင်အသုံးပြုရန် မတိုင်မီ အောက်ပါအချက်များ လိုအပ်ပါသည်-

1. **Chapter 01 မှ ကိန်းဂဏန်းတွက်စက် ဆာဗာကို စတင်ပါ** -
   - ကိန်းဂဏန်းတွက်စက် ဆာဗာ ဖိုင်လမ်းကြောင်းသို့ သွားပါ - `03-GettingStarted/01-first-server/solution/java/`
   - ဆာဗာကို တည်ဆောက်ပြီး စတင်ပါ -
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - ဆာဗာသည် `http://localhost:8080` တွင် လည်ပတ်နေသင့်သည်

2. သင့်စနစ်တွင် **Java 21 သို့မဟုတ် အထက်** ထည့်သွင်းထားရန်
3. **Maven** (Maven Wrapper ဖြင့် ပါဝင်သည်)

## SDKClient ဆိုတာဘာလဲ?

`SDKClient` သည် Java အပလီကေးရှင်းတစ်ခုဖြစ်ပြီး အောက်ပါအချက်များကို ပြသသည်-
- Server-Sent Events (SSE) သယ်ယူပို့ဆောင်မှုဖြင့် MCP ဆာဗာနှင့် ချိတ်ဆက်ခြင်း
- ဆာဗာမှ ရနိုင်သော ကိရိယာများ စာရင်းပြခြင်း
- ကိန်းဂဏန်းတွက်စက် လုပ်ဆောင်ချက်များကို ဝေးလံမှ ခေါ်ယူခြင်း
- တုံ့ပြန်ချက်များကို ကိုင်တွယ်ပြီး ရလဒ်များ ပြသခြင်း

## လုပ်ဆောင်ပုံ

Client သည် Spring AI MCP framework ကို အသုံးပြုကာ-

1. **ချိတ်ဆက်ခြင်း** - ကိန်းဂဏန်းတွက်စက် ဆာဗာနှင့် ချိတ်ဆက်ရန် WebFlux SSE client transport တစ်ခု ဖန်တီးသည်
2. **Client စတင်ခြင်း** - MCP client ကို စတင်ပြီး ချိတ်ဆက်မှုကို တည်ဆောက်သည်
3. **ကိရိယာများ ရှာဖွေခြင်း** - ရနိုင်သော ကိန်းဂဏန်းတွက်စက် လုပ်ဆောင်ချက်များအားလုံးကို စာရင်းပြသည်
4. **လုပ်ဆောင်ချက်များ ဆောင်ရွက်ခြင်း** - နမူနာဒေတာဖြင့် သင်္ချာဆိုင်ရာ လုပ်ဆောင်ချက်များ ခေါ်ယူသည်
5. **ရလဒ် ပြသခြင်း** - တစ်ခုချင်းစီ၏ ရလဒ်များကို ပြသသည်

## ပရောဂျက် ဖွဲ့စည်းပုံ

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## အဓိက အားထားရမည့် Dependencies များ

ပရောဂျက်တွင် အောက်ပါ အဓိက Dependencies များကို အသုံးပြုသည်-

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

ဤ dependency သည် အောက်ပါအရာများကို ပံ့ပိုးပေးသည်-
- `McpClient` - အဓိက client အင်တာဖေ့စ်
- `WebFluxSseClientTransport` - ဝက်ဘ်အခြေပြု ဆက်သွယ်မှုအတွက် SSE သယ်ယူပို့ဆောင်မှု
- MCP protocol schemas နှင့် တောင်းဆိုမှု/တုံ့ပြန်မှု အမျိုးအစားများ

## ပရောဂျက် တည်ဆောက်ခြင်း

Maven wrapper ကို အသုံးပြု၍ ပရောဂျက်ကို တည်ဆောက်ပါ-

```cmd
.\mvnw clean install
```

## Client ကို စတင်အသုံးပြုခြင်း

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Note**: ဤ command များကို အကောင်အထည်ဖော်မည့်အခါ `http://localhost:8080` တွင် ကိန်းဂဏန်းတွက်စက် ဆာဗာ လည်ပတ်နေသည်ကို သေချာစေပါ။

## Client ၏ လုပ်ဆောင်ချက်များ

Client ကို စတင်အသုံးပြုသောအခါ-

1. `http://localhost:8080` တွင် ကိန်းဂဏန်းတွက်စက် ဆာဗာနှင့် ချိတ်ဆက်သည်
2. **ကိရိယာများ စာရင်းပြခြင်း** - ရနိုင်သော ကိန်းဂဏန်းတွက်စက် လုပ်ဆောင်ချက်များအားလုံးကို ပြသသည်
3. **တွက်ချက်မှုများ ဆောင်ရွက်ခြင်း** -
   - ပေါင်းခြင်း: 5 + 3 = 8
   - ဖြုတ်ခြင်း: 10 - 4 = 6
   - မြှောက်ခြင်း: 6 × 7 = 42
   - ခွဲခြင်း: 20 ÷ 4 = 5
   - အင်အားမြှောက်ခြင်း: 2^8 = 256
   - စတုရန်းမြစ်: √16 = 4
   - အပြည့်အစုံတန်ဖိုး: |-5.5| = 5.5
   - အကူအညီ: ရနိုင်သော လုပ်ဆောင်ချက်များ ပြသသည်

## မျှော်မှန်းထားသော ထွက်ရှိမှု

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Note**: Maven သည် အဆုံးတွင် thread များ ကျန်ရှိနေသည်ဟု သတိပေးချက်များ ပြသနိုင်သည် - ၎င်းသည် reactive application များတွင် သာမန်ဖြစ်ပြီး အမှားမဟုတ်ပါ။

## ကုဒ်ကို နားလည်ခြင်း

### 1. သယ်ယူပို့ဆောင်မှု စတင်ခြင်း
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
ဤသည်က ကိန်းဂဏန်းတွက်စက် ဆာဗာနှင့် ချိတ်ဆက်ရန် SSE (Server-Sent Events) သယ်ယူပို့ဆောင်မှု တစ်ခု ဖန်တီးသည်။

### 2. Client ဖန်တီးခြင်း
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Synchronous MCP client တစ်ခု ဖန်တီးပြီး ချိတ်ဆက်မှုကို စတင်သည်။

### 3. ကိရိယာများ ခေါ်ယူခြင်း
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"a=5.0" နှင့် "b=3.0" ပါသော "add" ကိရိယာကို ခေါ်ယူသည်။

## ပြဿနာဖြေရှင်းခြင်း

### ဆာဗာ မလည်ပတ်ခြင်း
ချိတ်ဆက်မှု အမှားများ ဖြစ်ပါက Chapter 01 မှ ကိန်းဂဏန်းတွက်စက် ဆာဗာ လည်ပတ်နေသည်ကို သေချာစေပါ-
```
Error: Connection refused
```
**ဖြေရှင်းနည်း**: ပထမဦးဆုံး ကိန်းဂဏန်းတွက်စက် ဆာဗာကို စတင်ပါ။

### Port 8080 ကို အသုံးပြုနေခြင်း
Port 8080 ကို အခြား application များ အသုံးပြုနေပါက-
```
Error: Address already in use
```
**ဖြေရှင်းနည်း**: Port 8080 ကို အသုံးပြုနေသော အခြား application များကို ရပ်တန့်ပါ သို့မဟုတ် ဆာဗာကို အခြား port တစ်ခုသို့ ပြောင်းပါ။

### တည်ဆောက်မှု အမှားများ
တည်ဆောက်မှု အမှားများ ဖြစ်ပါက-
```cmd
.\mvnw clean install -DskipTests
```

## ပိုမိုလေ့လာလိုပါက

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပညာရှင်များ၏ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။
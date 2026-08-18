# Model Context Protocol (MCP) ဖြင့် HTTPS Streaming

ဤခေါင်းစဉ်တွင် Model Context Protocol (MCP) ကို အသုံးပြုပြီး HTTPS ဖြင့် လုံခြုံပြီး၊ တိုးချဲ့နိုင်သော၊ အချိန်နောက်ကျမှုမရှိသော streaming ကို ဖန်တီးသည့် လမ်းညွှန်ချက်များကို အပြည့်အစုံပေးထားသည်။ streaming အတွက် အကြောင်းပြချက်များ၊ သယ်ယူပို့ဆောင်မှုနည်းလမ်းများ၊ MCP တွင် streamable HTTP ကို အကောင်အထည်ဖော်နည်း၊ လုံခြုံရေး အကောင်းဆုံးလေ့လာမှုများ၊ SSE မှ ထွက်ခွာခြင်းနှင့် သင့်ကိုယ်ပိုင် streaming MCP အက်ပလီကေးရှင်းများ တည်ဆောက်ရာတွင် လက်တွေ့အကြံပြုချက်များကို ပါဝင်သည်။

> **ရှေ့ဆက်ကြည့်ရန်:** ဤသင်ခန်းစာတွင် **MCP Specification 2025-11-25** အောက်ရှိ Streamable HTTP ကို ဖော်ပြသည်။ ထို specification တွင် session ကို `initialize` အချိန်တွင် ဖွင့်ပြီး `Mcp-Session-Id` header ဖြင့် ချိတ်ဆက်ထားသည်။ `2026-07-28` ထုတ်ပြန်ရန်မီ candidate မှာ ချိတ်ဆက်မှုနှင့် session ID ကို ဖယ်ရှားသွားပြီး၊ သဘောတူညီချက်မလိုဘဲ တောင်းဆိုမှုတိုင်းကို တစ်ကိုယ်ရိုက် အလုပ်လုပ်နိုင်ပြီး မည်သည့် server instance မှပင် ရောက်အောင် ဖြန့်ဝေသည်။ အသေးစိတ်အတွက် [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) ကို ကြည့်ပါ။

## MCP တွင် သယ်ယူပို့ဆောင်မှုနည်းလမ်းများနှင့် Streaming

ဤအပိုင်းတွင် MCP တွင် ပါဝင်သည့် မတူကွဲပြားသည့် သယ်ယူပို့ဆောင်မှုနည်းလမ်းများနှင့် ၎င်းတို့သည် client နှင့် server များအကြား အချိန်နောက်ကျမှုမရှိသော ဆက်သွယ်ရေးအတွက် streaming စွမ်းဆောင်ရည် ရရှိစေရန် အသုံးပြုမှုကို ရှင်းလင်းမည်။

### သယ်ယူပို့ဆောင်မှုနည်းလမ်း ဆိုတာဘာလဲ?

သယ်ယူပို့ဆောင်မှုနည်းလမ်းသည် client နှင့် server တို့အကြား ဒေတာ လွှဲပြောင်းပေးပို့ပုံကို ဖော်ပြသည်။ MCP သည် ပတ်ဝန်းကျင်နှင့် လိုအပ်ချက်များကို စိတ်တိုင်းကျဖြေရှင်းနိုင်ရန် သယ်ယူပို့ဆောင်မှုအမျိုးအစားများစွာကို ထောက်ခံသည်။

- **stdio**: ပြင်ပကွန်ပြူတာတွင် သို့မဟုတ် CLI အခြေပြုကိရိယာများအတွက် သင့်တော်သည်။ ပိုမိုရိုးရှင်းသော်လည်း web သို့ cloud အတွက် မသင့်တော်ပါ။
- **SSE (Server-Sent Events)**: Server က client ကို HTTP ဖြင့် အချိန်နောက်ကျမှုမရှိဘဲ မက်ဆေ့များ ပို့ခွင့်ပြုသည်။ web UI များအတွက် ကောင်းမွန်သော်လည်း တိုးချဲ့မှုနှင့် လွယ်ကူမှုကနည်းသည်။ MCP Specification 2025-06-18 တွင် standalone SSE သယ်ယူပို့ဆောင်မှုကို ရပ်ဆိုင်းပြီး "Streamable HTTP" သယ်ယူပို့ဆောင်မှုဖြင့် အစားထိုးထားသည်။
- **Streamable HTTP**: နောက်ဆုံးပေါ် HTTP အခြေခံ streaming သယ်ယူပို့ဆောင်မှုဖြစ်ပြီး နှိုးဆော်ချက်များနှင့် တိုးချဲ့နိုင်မှုကောင်းမွန်သည်။ များသော ထုတ်လုပ်မှုနှင့် cloud သုံးမှုအတွက် အကြံပြုသည်။

### နှိုင်းယှဉ်ဇယား

ဤဇယားမှတဆင့် သယ်ယူပို့ဆောင်မှုနည်းလမ်းများ၏ ကွာခြားချက်များကို နားလည်နိုင်ပါသည်။

| သယ်ယူပို့ဆောင်မှု | အချိန်နောက်ကျမှုမရှိသော အပ်ဒိတ်များ | Streaming | တိုးချဲ့နိုင်မှု | အသုံးပြုမှုအနေအထား          |
|-------------------|----------------------------|-----------|-------------|-------------------------------|
| stdio             | မရှိ                        | မဖြစ်      | နည်း          | ဒေသခံ CLI ကိရိယာများ         |
| SSE               | ရှိ                         | ရှိ         | အလယ်အလတ်     | Web, အချိန်နောက်ကျမှုမရှိသော အပ်ဒိတ်များ |
| Streamable HTTP   | ရှိ                         | ရှိ         | မြင့်မားသော   | Cloud, များစွာသော client များ |

> **အကြံပြုချက်:** သင့်လျော်သော သယ်ယူပို့ဆောင်မှုကို ရွေးချယ်ခြင်းမှာ စွမ်းဆောင်ရည်၊ တိုးချဲ့နိုင်မှုနှင့် အသုံးပြုသူ အတွေ့အကြုံအပေါ် ထိရောက်မှုရှိသည်။ **Streamable HTTP** ကို နောက်ဆုံးပေါ်၊ တိုးချဲ့နိုင်ပြီး cloud ဖြင့် ပြင်ဆင်ထားသော အက်ပလီကေးရှင်းများအတွက် အကြံပြုပါသည်။

ယခင်အပိုင်းများတွင် stdio နှင့် SSE သယ်ယူပို့ဆောင်မှုပုံစံများကို မြင်ပြီးဖြစ်ပြီး အခုအပိုင်းတွင်တော့ streamable HTTP သယ်ယူပို့ဆောင်မှုအား ဖော်ပြထားသည်။

## Streaming: အကြောင်းအရင်းနှင့် အဓိပ္ပာယ်

Streaming ၏ အခြေခံ အယူအဆများနှင့် အဓိပ္ပာယ်များကို နားလည်ခြင်းသည် အချိန်နောက်ကျမှုမရှိသော ဆက်သွယ်ရေးစနစ်များ ဖန်တီးရာတွင် အရေးကြီးသည်။

**Streaming** သည် network programming တွင် ဒေတာကို တခြားနည်းဖြင့် စုစုပေါင်း အဖြေကို စောင့်ဆိုင်းခြင်းမပြုဘဲ ကျယ်ပြန့်သော အပိုင်းဒေတာများ သို့မဟုတ် ဖြစ်ရပ်စဉ်များအဖြစ် သယ်ဆောင်ပို့ဆောင်နိုင်စေသော နည်းဖြစ်သည်။ ၎င်းသည် အထူးသဖြင့် အတွက် အသုံးဝင်သည်-

- အကြီးစား ဖိုင်များ သို့မဟုတ် ဒေတာစုစည်းမှုများ။
- အချိန်နောက်ကျမှုမရှိသော အပ်ဒိတ်များ (ဥပမာ၊ စကားပြောခြင်း၊ တိုးတက်မှု စာရင်းများ)။
- အသုံးပြုသူကို သတင်းပေးမည့် ရေရှည်တွင် တွက်ချက်မှုများ။

Streaming အကြောင်း အခြေခံအားဖြင့် သိထားသင့်သည်မှာ-

- ဒေတာကို အစိတ်အပိုင်းဖြင့် တစ်စက်ချင်း မပြတ်ပို့ပေးသည်။
- client သည် ရောက်ရှိသည့် ဒေတာကို အချိန်တိုင်း ပိုင်နိုင်သည်။
- စိတ်ထင်မြင်ချက်ကို လျော့ချပေးကာ အသုံးပြုသူ အတွေ့အကြုံကောင်းမွန်စေသည်။

### Streaming ကို ဘာကြောင့်အသုံးပြုသလဲ?

Streaming သုံးစွဲသည့် အကြောင်းအရင်းများမှာ-

- အသုံးပြုသူများ မျက်နှာချင်းဆိုင် တုံ့ပြန်ချက်ကို အမြန်ရရှိစေသည်။
- အချိန်နောက်ကျမှုမရှိသော အက်ပလီကေးရှင်းများနှင့် တုံ့ပြန်မှုရှိသော UI များ ဖန်တီးနိုင်စေသည်။
- Network နှင့် ကွန်ပျူတာဆန်းပြားမှုများကို ထိရောက်စွာ အသုံးပြုနိုင်သည်။

### ရိုးရှင်းသော ဥပမာ- HTTP Streaming Server နှင့် Client

Streaming ကို မည်သို့ ကြိုးစားတည်ဆောက်နိုင်သည်ကို ရိုးရှင်းစွာ ဖော်ပြခြင်း။

#### Python

**Server (Python, FastAPI နှင့် StreamingResponse အသုံးပြု):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Client (Python, requests အသုံးပြု):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

ဥပမာတွင် server သည် မက်ဆေ့များအားလုံး ရှိတုန်း မစောင့်ဘဲ အသစ်ရရှိသည်အတိုင်း ဖောက်သည်ထံ ပို့သည်။

**မည်သို့ လုပ်ဆောင်သည်**

- Server သည် မက်ဆေ့တိုင်း ပြင်ဆင်ပြီး ရရှိသည်နှင့် ပေးပို့သည်။
- Client သည် မက်ဆေ့အစိတ်အပိုင်းတိုင်း ရောက်ရှိသည့်အခါ လက်ခံပြီး ပုံနှိပ်သည်။

**လိုအပ်ချက်များ**

- Server သည် streaming response ကို အသုံးပြုရမည် (ဥပမာ၊ FastAPI တွင် `StreamingResponse`)။
- Client သည် response ကို stream အနေဖြင့် စီမံရမည် (`stream=True` in requests)။
- Content-Type သည် အများအားဖြင့် `text/event-stream` သို့မဟုတ် `application/octet-stream` ဖြစ်သည်။

#### Java

**Server (Java, Spring Boot နှင့် Server-Sent Events အသုံးပြု):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Client (Java, Spring WebFlux WebClient အသုံးပြု):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Java Implementation မှတ်စုများ**

- Spring Boot ၏ reactive stack ကို `Flux` ဖြင့် အသုံးပြုပြီး streaming လုပ်ဆောင်သည်။
- `ServerSentEvent` သည် event များအား အမျိုးအစားပေးပြီး event streaming ကို ဖွဲ့စည်းပုံတကျ ပံ့ပိုးသည်။
- `WebClient` တွင် `bodyToFlux()` ကို အသုံးပြုပြီး reactive streaming လက်ခံသည်။
- `delayElements()` သည် event တို့အကြား အချိန်ကြာမြင့်မှု ကို သရုပ်ပြသည်။
- Event များတွင် improved client handling အတွက် အမျိုးအစား (`info`, `result`) ပါနိုင်သည်။

### နှိုင်းယှဉ်ချက် - ရိုးရာ Streaming နှင့် MCP Streaming

"ရိုးရာ" streaming နှင့် MCP streaming ၏ ထူးခြားချက်များကို အောက်တွင် ဖော်ပြထားသည်။

| လက္ခဏာ                | ရိုးရာ HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| မူလ ဖြေကြားချက်          | အစိတ်အပိုင်းဖြင့်                 | တစ်ခုတည်း၊ အဆုံးတွင်ပေးသည်              |
| တိုးတက်မှု အပ်ဒိတ်များ      | ဒေတာ chunks အဖြစ် ပေးပို့သည်      | နှိုးဆော်ချက်များအဖြစ် ပေးပို့သည်             |
| Client အတွက်လိုအပ်ချက်    | stream ကို လက်ခံကြည့်ရန်          | မက်ဆေ့ handler တည်ဆောက်ရန်               |
| အသုံးပြုမှု              | အကြီးစား ဖိုင်များ၊ AI token streams | တိုးတက်မှု၊ စာရင်းများ၊ အချိန်နောက်ကျမှုမရှိသော တုံ့ပြန်ချက်  |

### အဓိကကွာခြားချက်များ

ထို့အပြင် အခြားအဓိကကွာခြားချက်များမှာ-

- **ဆက်သွယ်မှု ပုံစံ:**
  - ရိုးရာ HTTP streaming: ဒေတာအား အစိတ်အပိုင်းများဖြင့် ပို့သွင်းခြင်း
  - MCP streaming: JSON-RPC protocol ကို အသုံးပြုပြီး ဖွဲ့စည်းထားသော notification စနစ်

- **မက်ဆေ့ဖော်မြူလာ:**
  - ရိုးရာ HTTP: newlines ပါရှိသည့် ပလိန်းမြစတက် chunk များ
  - MCP: metadata ပါရှိသည့် LoggingMessageNotification ဖွဲ့စည်းမှု

- **Client တည်ဆောက်ခြင်း:**
  - ရိုးရာ HTTP: streaming response များကို ရိုးရှင်းစွာ လက်ခံနိုင်သည့် client
  - MCP: မက်ဆေ့ handler ဖြင့် မက်ဆေ့အမျိုးအစားများကို ခွဲခြားစီမံနိုင်သော client

- **တိုးတက်မှု အပ်ဒိတ်များ:**
  - ရိုးရာ HTTP: တိုးတက်မှုသည် မူလ response stream ၏ အစိတ်အပိုင်းတစ်ခုဖြစ်သည်
  - MCP: တိုးတက်မှုကို နှိုးဆော်ချက် မက်ဆေ့များဖြင့် ပေးပို့ပြီး မူလ response ကို အဆုံးတွင်ပေးသည်

### အကြံပြုချက်များ

ရိုးရာ streaming (ဥပမာ `/stream` endpoint မှတဆင့်) နှင့် MCP streaming တို့မှ တစ်ခုကို ရွေးချယ်ရာတွင် အောက်ပါအကြံပြုချက်များရှိသည်။

- **ရိုးရှင်းသော streaming လိုအပ်ချက်များအတွက်:** ရိုးရာ HTTP streaming သည် ရိုးရှင်းပြီး အခြေခံ streaming အတွက် လုံလောက်သည်။

- **ရှုပ်ထွေးပြီး တွယ်ဂျာ interactive အက်ပလီကေးရှင်းများအတွက်:** MCP streaming မှ metadata နှင့် နှိုးဆော်ချက် မက်ဆေ့နှင့် နောက်ဆုံးရလဒ်ကို ခွဲခြားထားသည့် ပို၍ ဖွဲ့စည်းမှုရှိသော နည်းလမ်းဖြစ်သည်။

- **AI အပလီကေးရှင်းများအတွက်:** MCP ၏ နှိုးဆော်ချက် စနစ်သည် ရေရှည် AI ဝန်းရံမှုအတွက် အသုံးဝင်ပြီး အသုံးပြုသူများအား တိုးတက်မှုကို သတိပေးနိုင်သည်။

## MCP တွင် Streaming

ဤအထိ ရိုးရာ streaming နှင့် MCP streaming ၏ ကွာခြားချက်နှင့် အကြံပြုချက်များကို ကြည့်ရှုသိရှိထားပြီ ဖြစ်သည်။ ယခု MCP တွင် streaming ကို မည်သို့ အသုံးချနိုင်သည့်အသေးစိတ်ကို သွားရောက် လေ့လာပါမည်။

MCP ဖရိမ်ဝတ်အတွင်း streaming ၏ လည်ပတ်ပုံကို နားလည်ခြင်းသည် ရေရှည်ဆောင်ရွက်မှုအတွင်း အသုံးပြုသူများအား အချိန်နောက်ကျမှုမရှိသော တုံ့ပြန်မှုများပေးသော responsive applications ဖန်တီးရာတွင် အရေးကြီးသည်။

MCP တွင် streaming ဆိုသည်မှာ မူလ response ကို အစိတ်အပိုင်းဖြင့် ပေးပို့ခြင်းမဟုတ်ဘဲ၊ ကိရိယာ တစ်ခုသည် တောင်းဆိုမှုကို လုပ်ဆောင်နေစဉ် client ထံ သတင်းပို့ခြင်း (notifications) ဖြစ်သည်။ ထိုသတင်းပို့ခြင်းများတွင် တိုးတက်မှု အပ်ဒိတ်များ၊ အစီရင်ခံစာများ သို့မဟုတ် အခြား ဖြစ်ရပ်များ ပါဝင်နိုင်သည်။

### မည်သို့ လုပ်ဆောင်သည်

မူလရလဒ်ကို တစ်ခုတည်းသော response အဖြစ် ပေးပို့သေးဆဲဖြစ်သည်။ သို့သော် တိုးတက်မှုနှင့် အခြား သတင်းပို့ချက်များကို စီမံကိန်းလုပ်ဆောင်ချိန်တွင် သီးခြား message များအနေဖြင့် ပေးပို့၍ client ကို အချိန်နောက်ကျမှုမရှိဘဲ သတင်းပို့နိုင်သည်။ client သည် သတင်းပို့ချက်များကို လက်ခံပြသနိုင်ရမည်။

## Notification ဆိုတာဘာလဲ?

"Notification" ဟူသော စကားလုံးကို MCP context တွင် ဘာလဲ ဆိုတာ ရှင်းပြပါမည်။

Notification သည် ရေရှည် တာဝန်ရှိ ဆက်လက်လုပ်ဆောင်မှုအတွင်း တိုးတက်မှု၊ နေရာအခြေအနေ သို့မဟုတ် အခြားဖြစ်ရပ်များ အကြောင်း server မှ client ထံ ပို့သော message တစ်ခုဖြစ်သည်။ Notification များက transparency နှင့် အသုံးပြုသူ အတွေ့အကြုံကို တိုးတက်စေသည်။

ဥပမာ - client တစ်ခုသည် server နှင့် ပထမဆုံး handshake ပြုလုပ်ပြီးနောက် notification တစ်ခု ပေးပို့ရမည်။

Notification များသည် JSON message အဖြစ် အောက်ပါအတိုင်း ဖြစ်နိုင်သည်။

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifications သည် MCP တွင် ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) ဟု ခေါ်သော ခေါင်းစဉ်တစ်ခုအောက် ဖြစ်သည်။

> **မှတ်ချက်:** `2026-07-28` MCP specification release candidate မှ logging primitive ကို stdio transport များအတွက် `stderr` နှင့် ဖွဲ့စည်းထားသော observability အတွက် OpenTelemetry ဖြင့် အစားထိုးပြီး deprecated လုပ်သည်။ Logging သည် `2025-11-25` နှင့် တရားဝင် deprecated ပြောင်းလဲမှု အနည်းဆုံး တစ်နှစ်ကြာဆက်လက် အလုပ်လုပ်မည်။ အသေးစိတ်အတွက် [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) ကို ကြည့်ပါ။

Logging ကို လုပ်ဆောင်နိုင်ရန် server သည် အောက်ပါအတိုင်း feature/capability အဖြစ် ဖွင့်ထားရမည်။

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> အသုံးပြုမည့် SDK အပေါ် မူတည်၍ logging သည် ပုံမှန်အားဖြင့် အလိုအလျောက် ဖွင့်ထားနိုင်ပါသည် သို့မဟုတ် server configuration တွင် ထိထိရောက်ရောက် ဖွင့်ရပါမည်။

Notification များအမျိုးအစား များကွဲပြားသည်။

| အဆင့်      | ဖော်ပြချက်                      | ဥပမာအသုံးပြုမှု               |
|------------|------------------------------|--------------------------------|
| debug      | အသေးစိတ် debugging အချက်အလက်များ  | function ဝင်/ထွက် နေရာများ     |
| info       | အထွေထွေ သတင်းအချက်အလက် မက်ဆေ့များ | လုပ်ငန်း တိုးတက်မှု အပ်ဒိတ်များ  |
| notice     | သာမာန် သို့မဟုတ် အဓိက ဖြစ်ရပ်များ   | ပြင်ဆင်မှု အပြောင်းအလဲများ        |
| warning    | သတိပေးချက် အခြေနေများ            | အသုံးမပြုသင့် feature များကို အသုံးပြုခြင်း |
| error      | အမှား လုပ်ဆောင်မှုများ             | လုပ်ငန်း မအောင်မြင်မှုများ        |
| critical   | အရေးပေါ် အခြေအနေများ             | စနစ် အစိတ်အပိုင်း မအောင်မြင်မှုများ  |
| alert      | ယခုခဏ လုပ်ဆောင်ရမည့် အချက်များ     | ဒေတာ ပျက်စီးမှု တွေ့ရှိခြင်း    |
| emergency  | စနစ် မသုံးနိုင်ဖြစ်နေသည်             | စနစ် တစ်ခုလုံး ပျက်စီးမှု       |

## MCP တွင် Notification အကောင်အထည်ဖော်ခြင်း

MCP တွင် notification များကို ဖန်တီးရန် server နှင့် client အပိုင်းနှစ်ခုလုံးကို စီမံဆောင်ရွက်ရမည်၊ ၎င်းက application ကို ရေရှည်လုပ်ဆောင်စဉ်များအတွင်း အသုံးပြုသူများအား ချက်ချင်း တုံ့ပြန်မှု ပေးနိုင်စေသည်။

### Server အပိုင်း - Notification ပေးပို့ခြင်း

server အပိုင်းမှစတင်ပါ။ MCP တွင် tools များကို တောင်းဆိုမှုများ လုပ်ဆောင်နေစဉ် notification ပို့နိုင်စေရန် စီမံထားသည်။ Server သည် context မူရင်း (ပုံမှန်အားဖြင့် `ctx`) ကို အသုံးပြုပြီး client သို့ မက်ဆေ့ပို့သည်။

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

ယခင် ဥပမာတွင် `process_files` tool သည် ဖိုင်တစ်ခုစီကို လုပ်ဆောင်သိမ်းဆည်းသည့်အချိန် client သို့ notification သုံးချက် ပို့သည်။ `ctx.info()` နည်းလမ်းအား သတင်းအချက်အလက် message ပို့ရာတွင် အသုံးပြုသည်။

ထို့အပြင် notification ရစေရန် server သည် streaming transport (ဥပမာ `streamable-http`) ကို အသုံးပြုရမည်။ client သည် notification မက်ဆေ့တွေကို တုံ့ပြန်နိုင်ရန် message handler တည်ဆောက်ရမည်။ Streaming transport ကို အသုံးပြုရန် server ကို အောက်ပါအတိုင်း ပြင်ဆင်နိုင်သည်။

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

.NET ဥပမာတွင် `ProcessFiles` tool ကို `Tool` attribute ဖြင့် အမှတ်အသားပြုထားပြီး ဖိုင်တစ်ခုစီ တိတိကျကျ ဆောင်ရွက်သည့်အခါ client သို့ notification သုံးချက် ပေးပို့သည်။ `ctx.Info()` သည် သတင်းအချက်အလက် မက်ဆေ့ ပို့ရန် အသုံးပြုသည်။

.NET MCP server တွင် notification များ ဖွင့်ရန် streaming transport ကို အသုံးပြု ပါရန် သေချာစေရန်။

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client အပိုင်း - Notification လက်ခံခြင်း

client သည် ရောက်ရှိသော notification မက်ဆေ့များ အား လက်ခံပြီး ပြသနိုင်ရန် message handler တည်ဆောက်ရမည်။

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

ယခင် code တွင် `message_handler` function သည် လက်ရှိ message တစ်ခုသည် notification ဖြစ်သည်ကို စစ်ဆေးကာ ဖြစ်ပါက ထုတ်ပြန်သည်။ မဟုတ်လျှင် မူရင်း server message အဖြစ် စီမံသည်။ ClientSession ကို `message_handler` ဖြင့် စတင်ထားသည်ကို သိရှိရန်။

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

.NET ဥပမာတွင် `MessageHandler` function သည် incoming message ကို notification ဖြစ်/မဖြစ် စစ်ဆေးကာ ဖေါ်ပြသည်။ မဟုတ်ပါက server message အဖြစ် လုပ်ဆောင်သည်။ `ClientSession` ကို `ClientSessionOptions` ဖြင့် message handler ဖြင့် စတင်ထားသည်။

Notification များ ဖွင့်ရန် server သည် streaming transport (ဥပမာ `streamable-http`) ကို အသုံးပြုရမည်ဟု သေချာစေရန် ရှိသည်။ Client သည် notification မက်ဆေ့များကို စီမံရာတွင် message handler လည်း ပါဝင်ရမည်။

## တိုးတက်မှု Notification များနှင့် ဖြစ်ပေါ်ပုံများ

ဤအပိုင်းတွင် MCP တွင် တိုးတက်မှု notification များဆိုသည့် အဓိပ္ပာယ်၊ ထိရောက်မှုနှင့် Streamable HTTP ဖြင့် အကောင်အထည်ဖော်နည်းကို ရှင်းလင်းပြသသည်။ သင်၏နားလည်မှုကို ခိုင်မာစေရန် လက်တွေ့ကိစ္စတစ်ခုပါ ပါဝင်သည်။

တိုးတက်မှု notification များသည် ရေရှည်လုပ်ဆောင်နေစဉ် server မှ client ကို အချိန်နောက်ကျမှုမရှိဘဲ လက်ရှိ အခြေအနေကို သတင်းပေးသော message များဖြစ်သည်။ စုစုပေါင်းလုပ်ဆောင်မှု ပြီးစီးမှ စောင့်ဆိုင်းခြင်းမရှိဘဲ လည်ပတ်မှုတွင် client ကို သတင်းပေးသည်။ ၎င်းကနေ transparency, အသုံးပြုသူ အတွေ့အကြုံ နှင့် debug လုပ်ခြင်း လွယ်ကူမှု တိုးတက်စေသည်။

**ဥပမာ:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### တိုးတက်မှု Notification များကို ဘာကြောင့် အသုံးပြုသနည်း?

တိုးတက်မှု notification များသည် အောက်ပါအကြောင်းအရင်းများကြောင့် အရေးကြီးသည်။

- **အသုံးပြုသူ အတွေ့အကြုံ ကောင်းမွန်စေခြင်း:** တိုးတက်ဖြစ်စဉ်အတိုင်း အသုံးပြုသူများ ထောက်ထားကြည့်နိုင်သည်။
- **အချိန်နောက်ကျမှုမရှိသော တုံ့ပြန်မှု:** client တွင် တိုးတက်မှုရေးဇယား သို့မဟုတ် စာရင်းများ ပြသနိုင်ပြီး အက်ပလီကေးရှင်း ကို တုံ့ပြန်မှုရှိစေသည်။
- **debug နှင့် မျှဝေရေး လွယ်ကူစေခြင်း:** ဖွံ့ဖြိုးသူများနှင့် အသုံးပြုသူများသည် လုပ်ဆောင်မှု ဘယ်နေရာတွင် အဆင်မပြေ သို့မဟုတ် ရပ်တန့်နေသည် ကြည့်ရှုနိုင်သည်။

### တိုးတက်မှု Notification များ ကို မည်သည့်ပုံစံဖြင့် ဖန်တီးရမည်

MCP တွင် တိုးတက်မှု notification များ အောက်ပါအတိုင်း ဖန်တီးနိုင်သည်-

- **Server ပိုင်းတွင်:** `ctx.info()` သို့ `ctx.log()` ကို အသုံးပြု၍ ပိုစတာ (items) တစ်ခုချင်းစီရေးစဉ် သတင်းပို့ရန်။ ၎င်းသည် မူလရလဒ် ပြီးစီးခင် client ကို သတင်းပို့ခြင်း။
- **Client ပိုင်းတွင်:** အသိပေးချက်များ လက်ခံပြီး ပြသနိုင်ရန် message handler တည်ဆောက်ရန်။ handler သည် notification မက်ဆေ့များနှင့် နောက်ဆုံးရလဒ်ကို ခွဲခြားစီမံသည်။

**Server ဥပမာ:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Client Example:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## လုံခြုံရေး စဉ်းစားချက်များ

Server များကို အကောင်အထည်ဖော်ရာတွင်၊ အထူးသဖြင့် MCP တွင် Streamable HTTP ကဲ့သို့သော HTTP အခြေပြု ပို့ဆောင်မှုများကို အသုံးပြုသောအခါ လုံခြုံရေးသည် ထိပ်တန်း ဦးစားပေးမှုဖြစ်ရမည်။

MCP server များကို HTTP အခြေပြု ပို့ဆောင်မှုဖြင့် အကောင်အထည်ဖော်သောအခါ၊ လုံခြုံရေးသည် အလွန်အရေးကြီးပြီး ရာရှည် တိုက်ခိုက်မှုများနှင့် ကာကွယ်ရေး မက်ခရိုနစ်များကို ဂရုစိုက်ရန် လိုအပ်သည်။

### အကျဉ်းချုပ်

MCP server များကို HTTP မှတဆင့် ဖော်ပြသောအခါ လုံခြုံရေးသည် အရေးပါသည်။ Streamable HTTP သည် အသစ်သော တိုက်ခိုက်နိုင်သည့် နေရာများကို မိတ်ဆက်ပေးပြီး မျှတသော သတ်မှတ်ချက်များလိုအပ်သည်။

ဤမှာ အဓိက လုံခြုံရေး စဉ်းစားချက်များအနည်းငယ်ဖြစ်ပါသည်-

- **Origin Header စစ်ဆေးခြင်း**: DNS rebinding တိုက်ခိုက်မှုများကို ကာကွယ်ရန် `Origin` header ကို အမြဲစစ်ဆေးပါ။
- **Localhost Binding**: ဒေသခံဖွံ့ဖြိုးတိုးတက်မှုအတွက် server များကို `localhost` သို့ ပိတ်ဆို့၍ လူအများအပေါ် ရှိသော အင်တာနက်မှ ခွဲထွက်ခြင်းမှ ကာကွယ်ပါ။
- **Authentication**: ထုတ်လုပ်မှု သို့သွင်းမှုများအတွက် authentication (ဥပမာ၊ API keys, OAuth) ကို အကောင်အထည်ဖော်ပါ။
- **CORS**: ခြားနားသော Origin များမှ အသုံးပြုမှုကို ကန့်သတ်ရန် Cross-Origin Resource Sharing (CORS) မှတ်တမ်းပေါင်းမှုများ စီစဉ်ပါ။
- **HTTPS**: မူပိုင်ရုံတွင် HTTPS ကို အသုံးပြုပြီး သယ်ယူပို့ဆောင်မှုများကို စာလုံးကူးဒေတာဖြင့် လုံခြုံစေပါ။

### ကောင်းမွန်သော အလေ့အကျင်းများ

ထို့ပြင် MCP streaming server တွင် လုံခြုံရေးဆိုင်ရာ အကောင်အထည်ဖော်ရာတွင် လိုက်နာသင့်သည့် အကောင်းဆုံး အလေ့အကျင့်များမှာ -

- ထိုက်တန်မှုမရှိသော မဟုတ်သော တောင်းဆိုမှုများကို မယုံကြည်ပါနှင့်။
- လက်လှမ်းမမီမှု နှင့် အမှားများကို မှတ်တမ်းတင်စောင့်ကြည့်ပါ။
- လုံခြုံရေးအားထိခိုက်မှုများကို patches ဖြင့် ပြင်ဆင်ရန် ရေတိုင်း dependency များကို နေ့စဉ် update လုပ်ပါ။

### စိန်ခေါ်မှုများ

MCP streaming server များတွင် လုံခြုံရေး များကို အကောင်အထည်ဖော်ရာတွင် ကြုံတွေ့ရမည့် စိန်ခေါ်မှုများမှာ -

- လုံခြုံရေးနှင့် ဖွံ့ဖြိုးတိုးတက်ရေး လွယ်ကူမှုပြသာနာ များကို ထိန်းညှိခြင်း
- ဖြည့်ဆည်းသော client ပတ်ဝန်းကျင် များနှင့် လိုက်ဖက်မှုကို သေချာစေရန်


## SSE မှ Streamable HTTP သို့ အဆင့်မြှင့်ခြင်း

လက်ရှိ Server-Sent Events (SSE) ကို အသုံးပြုနေသော အက်ပလီကေးရှင်းများအတွက် Streamable HTTP သို့ အပြောင်းအလဲပြုလုပ်ခြင်းမှာ MCP အသုံးပြုမှုတွင် ပိုမိုတိုးတက်သော စွမ်းဆောင်ရည်များနှင့် ရေရှည် ထိန်းသိမ်းနိုင်မှုကို ပေးစွမ်းသည်။

### အဆင့်မြှင့်ရန် အကြောင်းရင်း

SSE မှ Streamable HTTP သို့ အဆင့်မြှင့်ရန် အကြောင်းရင်းက -

- Streamable HTTP သည် SSE ထက် ပိုမို ကျယ်ပြန့်သော တိုးတက်မှု၊ လိုက်ဖက်မှုနှင့် ကြေငြာမှု ပံ့ပိုးမှုများ ပေးသည်။
- MCP အသစ်များအတွက် အကြံပြုထားသော သယ်ယူပို့ဆောင်ရေးဖြစ်သည်။

### ပြောင်းရွှေ့ရန် အဆင့်များ

MCP applications များတွင် SSE မှ Streamable HTTP သို့ ပြောင်းရွှေ့ခြင်းအတွက် နည်းလမ်းများမှာ -

- **Server code ကို update** ပြုလုပ်၍ `mcp.run()` တွင် `transport="streamable-http"` ကို သတ်မှတ်ပါ။
- **Client code ကို update** ပြုလုပ်၍ SSE client အစား `streamablehttp_client` ကို အသုံးပြုပါ။
- **Client တွင် message handler** တစ်ခု တပ်ဆင်ပြီး ကြေငြာချက်များကို ဆန်းစစ်ဆောင်ရွက်ပါ။
- ပစ္စည်းခွဲခြမ်းစိတ်ဖြာမှုများနှင့် workflow များနှင့် လိုက်ဖက်မှုကို စမ်းသပ်ပါ။

### လိုက်ဖက်မှု များ ထိန်းသိမ်းခြင်း

ပြောင်းရွှေ့နည်းအတွင်း သင့်ရဲ့ SSE client များနှင့် လိုက်ဖက်မှုကို ထိန်းသိမ်းထားရန် အကြံပြုထားပါသည်။ ဒီအတွက် အကြံဉာဏ်များမှာ:

- SSE နှင့် Streamable HTTP နှစ်မျိုးလုံးကို endpoint မျိုးစုံဖြင့် ပေါင်းစပ်ထောက်ပံ့နိုင်ပါသည်။
- Client များကို تدريجيအားဖြင့် ထည့်သွင်းစဉ်ဆက်ပြောင်းရွှေ့ပါ။

### စိန်ခေါ်မှုများ

ပြောင်းရွှေ့ခြင်းအတွင်း မဖြစ်မနေ ဖြေရှင်းရမည့် စိန်ခေါ်မှုများမှာ -

- Client အားလုံးကို အဆင့်မြှင့်ပေးခြင်း သေချာစေရန်
- ကြေငြာချက် ပို့ဆောင်မှု ကွဲပြားချက်များကို ကိုင်တွယ်နိုင်ရန်

### လုပ်ငန်းတာဝန်: ကိုယ်ပိုင် Streaming MCP အက်ပ်ကိုတည်ဆောက်ပါ

**အခြေအနေ:**
MCP server တစ်ခုကို တည်ဆောက်ပြီး၊ server သည် အရာဝတ္ထုစာရင်းတစ်ခု (ဥပမာ၊ ဖိုင် သို့မဟုတ် စာရွက်စာတမ်းများ) ကို အလုပ်လုပ်ဆောင်ပြီး၊ ယင်းအရာဝတ္ထု တစ်ခုစီအတွက် ကြေငြာချက် တစ်ခု ပေးပို့ပါမည်။ Client သည် အဆိုပါ ကြေငြာချက်တိုင်းကို အချိန်နဲ့တပြေးညီ ပြသရမည်။

**အဆင့်များ:**

1. အရာဝတ္ထုစာရင်းကို အလုပ်လုပ်ဆောင်ပြီး အရာဝတ္ထုတစ်ခုစီအား ကြေငြာချက် ပေးပို့သော server ကိရိယာ တစ်ခု အကောင်အထည်ဖော်ပါ။
2. ကြေငြာချက်များကို အချိန်နဲ့တပြေးညီ ပြသနိုင်ရန် message handler ပါဝင်သော client တစ်ခုကို တည်ဆောက်ပါ။
3. Server နှင့် client နှစ်ခုစလုံး မောင်းနှင်ပြီး ကြေငြာချက်များကို ကြည့်ရှုစမ်းသပ်ပါ။

[Solution](./solution/README.md)

## ဆက်လက်လေ့လာရန်နှင့် နောက်တစ်ဆင့် ဘာများလုပ်မည်နည်း?

MCP streaming နှင့် ပိုမိုတိုးတက်သော အသိပညာ ရရှိစေရေးအတွက် ဤပိုင်းတွင် အပိုဆောင်း အရင်းအမြစ်များနှင့် အသုံးပြုရန် ပိုမိုခက်ခဲသော အက်ပ်များ တည်ဆောက်ခြင်းအတွက် အကြံပြုချက်များ ပါဝင်သည်။

### ဆက်လက်လေ့လာရန်

- [Microsoft: HTTP စီးဆင်းမှု မိတ်ဆက်](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core တွင် CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### နောက်တစ်ဆင့်

- တိုက်ရိုက် စာရင်း များ၊ စကားပြော၊ သို့မဟုတ် ပူးပေါင်း တည်းဖြတ်ခြင်းများအတွက် streaming ကို အသုံးပြုသော ပိုမိုတိုးတက်သော MCP ကိရိယာများ တည်ဆောက်ရန် ကြိုးစားပါ။
- MCP streaming ကို frontend framework များ (React, Vue, စသည်) နှင့် ပေါင်းစည်း၍ UI ကို တိုက်ရိုက် ပြောင်းလဲမှုများ ပြုလုပ်ပါ။
- နောက်တစ်ကြောင်း: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# HTTPS Streaming with Model Context Protocol (MCP)

ဤအခန်းတွင် Model Context Protocol (MCP) ကို အသုံးပြု၍ HTTPS ဖြင့် လုံခြုံမှုရှိပြီး၊ အတိုင်းအတာကျပြီး၊ အချိန်နှင့်တပြေးညီ စီးဆင်းမှုကို အကောင်အထည်ဖော်ရန် လမ်းညွှန်ချက်များကို ဖော်ပြထားသည်။ စီးဆင်းမှု၏ အဓိကရည်ရွယ်ချက်၊ အသုံးပြုနိုင်သော သယ်ဆောင်မှု Mechanisms များ၊ MCP တွင် Streamable HTTP ကို အကောင်အထည်ဖော်နည်း၊ လုံခြုံမှုအကောင်းဆုံး လုပ်ထုံးလုပ်နည်းများ၊ SSE မှ ပြောင်းရွှေ့ခြင်းနှင့် MCP စီးဆင်းမှု အက်ပလီကေးရှင်းများကို တည်ဆောက်ရန် လက်တွေ့လမ်းညွှန်ချက်များကို ဖော်ပြထားသည်။

## MCP တွင် သယ်ဆောင်မှု Mechanisms နှင့် Streaming

ဤအပိုင်းတွင် MCP တွင် ရရှိနိုင်သော သယ်ဆောင်မှု Mechanisms များနှင့် Client နှင့် Server အကြား အချိန်နှင့်တပြေးညီ ဆက်သွယ်မှုကို အကောင်အထည်ဖော်ရန် ၎င်းတို့၏ အခန်းကဏ္ဍကို လေ့လာပါမည်။

### သယ်ဆောင်မှု Mechanism ဆိုတာဘာလဲ?

သယ်ဆောင်မှု Mechanism သည် Client နှင့် Server အကြား ဒေတာကို ဘယ်လို လဲလှယ်မည်ကို သတ်မှတ်သည်။ MCP သည် ပတ်ဝန်းကျင်နှင့် လိုအပ်ချက်များအလိုက် သင့်လျော်သော သယ်ဆောင်မှုအမျိုးအစားများစွာကို ပံ့ပိုးပေးသည်။

- **stdio**: Standard input/output, ဒေသတွင်းနှင့် CLI-based tools များအတွက် သင့်လျော်သည်။ ရိုးရှင်းသော်လည်း web သို့မဟုတ် cloud အတွက် မသင့်လျော်ပါ။
- **SSE (Server-Sent Events)**: Server များက Client များကို HTTP ဖြင့် အချိန်နှင့်တပြေးညီ update များကို push လုပ်ပေးနိုင်သည်။ Web UI များအတွက် သင့်လျော်သော်လည်း အတိုင်းအတာကျမှုနှင့် လွယ်ကူမှုမှာ ကန့်သတ်ချက်ရှိသည်။
- **Streamable HTTP**: ခေတ်မီ HTTP-based streaming transport, notification များနှင့် အတိုင်းအတာကျမှုကို ပံ့ပိုးပေးသည်။ အများဆုံး production နှင့် cloud scenarios များအတွက် အကြံပြုသည်။

### နှိုင်းယှဉ်ဇယား

အောက်ပါ နှိုင်းယှဉ်ဇယားကို ကြည့်ပြီး သယ်ဆောင်မှု Mechanisms များ၏ ကွာခြားချက်များကို နားလည်ပါ။

| Transport         | အချိန်နှင့်တပြေးညီ Update | Streaming | အတိုင်းအတာကျမှု | အသုံးပြုမှု                  |
|-------------------|--------------------------|-----------|------------------|-----------------------------|
| stdio             | မရှိပါ                   | မရှိပါ    | အနိမ့်           | ဒေသတွင်း CLI tools         |
| SSE               | ရှိသည်                   | ရှိသည်    | အလယ်အလတ်        | Web, အချိန်နှင့်တပြေးညီ update |
| Streamable HTTP   | ရှိသည်                   | ရှိသည်    | အမြင့်           | Cloud, multi-client         |

> **Tip:** သင့် transport ရွေးချယ်မှုသည် performance, scalability, နှင့် user experience ကို သက်ရောက်စေသည်။ **Streamable HTTP** သည် ခေတ်မီ၊ အတိုင်းအတာကျပြီး cloud-ready application များအတွက် အကြံပြုသည်။

## Streaming: အယူအဆများနှင့် ရည်ရွယ်ချက်

Streaming ၏ အခြေခံအယူအဆများနှင့် ရည်ရွယ်ချက်များကို နားလည်ခြင်းသည် အချိန်နှင့်တပြေးညီ ဆက်သွယ်မှုစနစ်များကို အကျိုးရှိစွာ အကောင်အထည်ဖော်ရန် အရေးကြီးသည်။

**Streaming** သည် network programming တွင် ဒေတာကို တစ်ခုပြီးတစ်ခု အဆင့်ဆင့်ပို့ခြင်း သို့မဟုတ် အဖြစ်အပျက်များအနေနှင့် ပို့ခြင်းဖြင့် လုပ်ဆောင်သည့်နည်းလမ်းဖြစ်သည်။ ဒါဟာ အောက်ပါအခြေအနေများအတွက် အထူးအသုံးဝင်သည်-

- ဖိုင်များ သို့မဟုတ် ဒေတာအစုအဝေးများ ကြီးမားသောအခါ
- အချိန်နှင့်တပြေးညီ update များ (ဥပမာ chat, progress bar များ)
- အချိန်ကြာမြင့်သော computation များတွင် user ကို update ပေးလိုသောအခါ

### Streaming ကို ဘာကြောင့် အသုံးပြုသင့်သလဲ?

Streaming ကို အသုံးပြုရန် အကြောင်းအရင်းများမှာ-

- User များသည် အဆုံးသတ်မတိုင်မီ feedback ရရှိနိုင်သည်။
- အချိန်နှင့်တပြေးညီ application များနှင့် တုံ့ပြန်မှုရှိသော UI များကို ဖန်တီးနိုင်သည်။
- Network နှင့် compute resources ကို ပိုမိုထိရောက်စွာ အသုံးပြုနိုင်သည်။

### ရိုးရှင်းသော Streaming Server နှင့် Client ဥပမာ

#### Python

**Server (Python, FastAPI နှင့် StreamingResponse ကို အသုံးပြုခြင်း):**

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

**Client (Python, requests ကို အသုံးပြုခြင်း):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

ဤဥပမာသည် Server က message များကို အဆင့်ဆင့်ပို့ပြီး Client က message များကို ရရှိသည့်အတိုင်း print လုပ်ပေးသည်။

#### Java

**Server (Java, Spring Boot နှင့် Server-Sent Events ကို အသုံးပြုခြင်း):**

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

**Client (Java, Spring WebFlux WebClient ကို အသုံးပြုခြင်း):**

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

Java implementation မှတ်ချက်များ:

- Spring Boot ၏ reactive stack ကို အသုံးပြုသည်။
- `ServerSentEvent` သည် structured event streaming ကို ပံ့ပိုးပေးသည်။
- `WebClient` သည် `bodyToFlux()` ဖြင့် reactive streaming consumption ကို ပံ့ပိုးပေးသည်။

## MCP တွင် Streaming

MCP framework တွင် streaming ကို ဘယ်လို အသုံးပြုရမည်ဆိုတာကို နားလည်ခြင်းသည် အချိန်ကြာမြင့်သော လုပ်ငန်းစဉ်များအတွင်း user များကို real-time feedback ပေးနိုင်သော responsive application များကို တည်ဆောက်ရန် အရေးကြီးသည်။

MCP တွင် streaming သည် main response ကို chunk များအနေနှင့် ပို့ခြင်းမဟုတ်ပါ။ **Notification** များကို tool တစ်ခု processing လုပ်နေစဉ် Client သို့ ပို့ခြင်းဖြင့် လုပ်ဆောင်သည်။

### Notification ဆိုတာဘာလဲ?

Notification သည် Server မှ Client သို့ progress, status, သို့မဟုတ် အခြားအဖြစ်အပျက်များကို အချိန်ကြာမြင့်သော လုပ်ငန်းစဉ်အတွင်း သတင်းပို့ရန် အသုံးပြုသော message ဖြစ်သည်။ Notification များသည် transparency နှင့် user experience ကို တိုးတက်စေသည်။

Notification များသည် MCP ၏ ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) ဟုခေါ်သော topic တွင် ပါဝင်သည်။

## Notification များကို MCP တွင် အကောင်အထည်ဖော်ခြင်း

### Server-side: Notification ပို့ခြင်း

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
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

### Client-side: Notification ရရှိခြင်း

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

## Progress Notification များနှင့် Scenarios

Progress notification များသည် Server မှ Client သို့ အချိန်ကြာမြင့်သော လုပ်ငန်းစဉ်များအတွင်း real-time message များကို ပို့ခြင်းဖြင့် transparency နှင့် user experience ကို တိုးတက်စေသည်။

**ဥပမာ:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Progress Notification များကို MCP တွင် အကောင်အထည်ဖော်နည်း

#### Server-side

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

#### Client-side

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## လုံခြုံမှုအရေးယူမှုများ

Streamable HTTP သည် attack surface အသစ်များကို ဖန်တီးနိုင်သဖြင့် MCP server များကို HTTP-based transport ဖြင့် expose လုပ်ရာတွင် လုံခြုံမှုကို အထူးဂရုပြုရမည်။

### အဓိကအချက်များ

- **Origin Header Validation**: DNS rebinding attack များကို ကာကွယ်ရန် `Origin` header ကို validate လုပ်ပါ။
- **Localhost Binding**: Development အတွက် server များကို `localhost` တွင် bind လုပ်ပါ။
- **Authentication**: Production deployment များအတွက် authentication ကို အကောင်အထည်ဖော်ပါ။
- **CORS**: Cross-Origin Resource Sharing (CORS) policies ကို configure လုပ်ပါ။
- **HTTPS**: Production တွင် traffic ကို encrypt လုပ်ရန် HTTPS ကို အသုံးပြုပါ။

### အကောင်းဆုံး လုပ်ထုံးလုပ်နည်းများ

- Validation မရှိသော request များကို ယုံကြည်မထားပါနှင့်။
- Access နှင့် error များအားလုံးကို log လုပ်ပါ။
- Security vulnerability များကို patch လုပ်ရန် dependency များကို regular update လုပ်ပါ။

## SSE မှ Streamable HTTP သို့ Upgrade လုပ်ခြင်း

Server-Sent Events (SSE) ကို အသုံးပြုနေသော application များအတွက် Streamable HTTP သို့ ပြောင်းရွှေ့ခြင်းသည် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည်နှင့် ရေရှည်တည်တံ့မှုကို ပေးစွမ်းနိုင်သည်။

### Upgrade လုပ်ရန် အကြောင်းအရင်း
SSE မှ Streamable HTTP သို့ upgrade လုပ်ရန်အတွက် အရေးကြီးသောအကြောင်းအရာနှစ်ခုရှိသည်။

- Streamable HTTP သည် SSE ထက် scalability, compatibility, နှင့် notification ပိုမိုချောမွေ့စွာပေးနိုင်မှုတို့ကို ပိုမိုကောင်းမွန်စေသည်။
- ဒါဟာ MCP application အသစ်များအတွက် အကြံပြုထားသော transport ဖြစ်သည်။

### ပြောင်းလဲမှုအဆင့်များ

MCP application များတွင် SSE မှ Streamable HTTP သို့ ပြောင်းလဲရန်အဆင့်များမှာ အောက်ပါအတိုင်းဖြစ်သည်-

- **Server code ကို update လုပ်ပါ** - `mcp.run()` တွင် `transport="streamable-http"` ကို အသုံးပြုပါ။
- **Client code ကို update လုပ်ပါ** - SSE client အစား `streamablehttp_client` ကို အသုံးပြုပါ။
- **Message handler တစ်ခုကို client တွင် implement လုပ်ပါ** - notification များကို process လုပ်ရန်။
- **Existing tools နှင့် workflows များနှင့် compatibility ရှိ/မရှိ စမ်းသပ်ပါ**။

### Compatibility ထိန်းသိမ်းခြင်း

SSE client များနှင့် compatibility ကို ပြောင်းလဲမှုအတွင်း ထိန်းသိမ်းထားရန် အကြံပြုထားသည်။ အောက်ပါနည်းလမ်းများကို အသုံးပြုနိုင်သည်-

- SSE နှင့် Streamable HTTP နှစ်ခုလုံးကို support လုပ်ရန် endpoint များကွဲပြားစွာ run လုပ်နိုင်သည်။
- Gradual client migration ကို ပြုလုပ်ပါ။

### စိန်ခေါ်မှုများ

ပြောင်းလဲမှုအတွင်း အောက်ပါစိန်ခေါ်မှုများကို ဖြေရှင်းရန် သေချာစွာလုပ်ဆောင်ပါ-

- Client များအားလုံးကို update လုပ်ရန်
- Notification delivery တွင် ကွာခြားမှုများကို handle လုပ်ရန်

## လုံခြုံရေးအရေးယူမှုများ

MCP server များကို HTTP-based transport များဖြင့် implement လုပ်ရာတွင် လုံခြုံရေးသည် အရေးကြီးဆုံးဖြစ်သည်။

HTTP-based transport များဖြင့် MCP server များကို implement လုပ်ရာတွင် attack vectors များနှင့် ကာကွယ်မှု mechanism များကို သေချာစွာဂရုစိုက်ရန် လိုအပ်သည်။

### အကျဉ်းချုပ်

MCP server များကို HTTP ဖြင့် expose လုပ်ရာတွင် လုံခြုံရေးသည် အရေးကြီးသည်။ Streamable HTTP သည် attack surface အသစ်များကို ဖန်တီးပြီး သေချာစွာ configuration လုပ်ရန် လိုအပ်သည်။

အရေးကြီးသော လုံခြုံရေးအချက်များမှာ-

- **Origin Header Validation**: DNS rebinding attack များကို ကာကွယ်ရန် `Origin` header ကို အမြဲ validate လုပ်ပါ။
- **Localhost Binding**: Local development အတွက် server များကို `localhost` တွင် bind လုပ်ပါ။
- **Authentication**: Production deployment များအတွက် authentication (API keys, OAuth စသည်) ကို implement လုပ်ပါ။
- **CORS**: Cross-Origin Resource Sharing (CORS) policy များကို configure လုပ်ပြီး access ကို ကန့်သတ်ပါ။
- **HTTPS**: Production တွင် traffic ကို encrypt လုပ်ရန် HTTPS ကို အသုံးပြုပါ။

### အကောင်းဆုံးအလေ့အကျင့်များ

MCP streaming server တွင် လုံခြုံရေးကို implement လုပ်ရာတွင် အောက်ပါအလေ့အကျင့်များကို လိုက်နာပါ-

- Validation မရှိသော incoming request များကို မယုံပါနှင့်။
- Access နှင့် error များအားလုံးကို log လုပ်ပြီး monitor လုပ်ပါ။
- Security vulnerability များကို patch လုပ်ရန် dependency များကို regular update လုပ်ပါ။

### စိန်ခေါ်မှုများ

MCP streaming server များတွင် လုံခြုံရေးကို implement လုပ်ရာတွင် အောက်ပါစိန်ခေါ်မှုများကို ရင်ဆိုင်ရမည်-

- Development အဆင့်ကို လွယ်ကူစေခြင်းနှင့် လုံခြုံရေးအကြား balance လုပ်ရန်
- Client environment များနှင့် compatibility ရှိစေရန်

### အလုပ်ပေးမှု: သင့်ကိုယ်ပိုင် Streaming MCP App တည်ဆောက်ပါ

**အခြေအနေ:**
MCP server နှင့် client တစ်ခုကို တည်ဆောက်ပါ။ Server သည် item များ (ဥပမာ- ဖိုင်များ သို့မဟုတ် စာရွက်များ) စာရင်းကို process လုပ်ပြီး process လုပ်ပြီးသော item တစ်ခုစီအတွက် notification ပေးပါမည်။ Client သည် notification များကို real-time တွင် ပြသရမည်။

**အဆင့်များ:**

1. Item စာရင်းကို process လုပ်ပြီး item တစ်ခုစီအတွက် notification ပေးသော server tool တစ်ခုကို implement လုပ်ပါ။
2. Notification များကို real-time တွင် ပြသရန် message handler ပါသော client တစ်ခုကို implement လုပ်ပါ။
3. Server နှင့် client ကို run လုပ်ပြီး notification များကို စမ်းသပ်ပါ။

[Solution](./solution/README.md)

## ထပ်မံဖတ်ရှုရန်နှင့် နောက်တစ်ဆင့်

MCP streaming နှင့် ပိုမိုအဆင့်မြင့် application များတည်ဆောက်ရန် သင်၏အသိပညာကို တိုးချဲ့ရန် အပိုင်းတွင် ထပ်မံဖတ်ရှုရန် resource များနှင့် အကြံပြုချက်များကို ပေးထားသည်။

### ထပ်မံဖတ်ရှုရန်

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### နောက်တစ်ဆင့်

- Real-time analytics, chat, သို့မဟုတ် collaborative editing အတွက် streaming ကို အသုံးပြုသော MCP tool များကို တည်ဆောက်ရန် ကြိုးစားပါ။
- Live UI updates အတွက် MCP streaming ကို frontend frameworks (React, Vue စသည်) နှင့် ပေါင်းစပ်ရန် စမ်းသပ်ပါ။
- နောက်တစ်ဆင့်: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
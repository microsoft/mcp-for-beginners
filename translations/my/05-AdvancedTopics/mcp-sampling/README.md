> [!WARNING]
> Sampling ကို MCP `2026-07-28` မှာ အသုံးမပြုတော့ပါ။ ဒီသင်ခန်းစာကို
> အတိတ်ကာလမှာ အသုံးပြုထားတဲ့ ပုံစံများအတွက်သာ ထိန်းသိမ်းထားတာဖြစ်ပါတယ်။ ဆာဗာအသစ်တွေက LLM
> ပံ့ပိုးသူ API နဲ့ တိုက်ရိုက် ပေါင်းစည်းသင့်ပါတယ်။

# Model Context Protocol တွင် Sampling

> Sampling ကို `2026-07-28` သတ်မှတ်ချက်ထဲမှာ ဆက်လက်ထည့်သွင်းထားပြီး အဆက်အသွယ်နှင့်
> ကိုက်ညီမှုအတွက်ဖြစ်ကာ ၂၀၂၇ ခုနှစ် ဇူလိုင်လ ၂၈ ရက်မတိုင်မီ သို့မဟုတ် ပြီးနောက်ထုတ်
> ပေးမယ့် ပထမဆုံး ပြင်ဆင်မှုမှာ ဖယ်ရှားသွားနိုင်ပါတယ်။ ဒီသင်ခန်းစာရဲ့ နမူနာတွေမှာ `2025-11-25`
> ကို အကောင်အထည်ဖော်ထားတဲ့ SDK API တွေကို အသုံးပြုထားနိုင်ပါတယ်။ [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md) ကို ကြည့်ပါ။

အတိတ် MCP အကောင်အထည်ဖော်မှုတွေမှာ Sampling က ဆာဗာတွေကို client မှတဆင့် LLM
ဖြည့်တင်းချက်များကို တောင်းဆိုခွင့်ပေးပါတယ်။ ဒီသင်ခန်းစာက ပဟေဋိဖြစ်ပြီး အသိအမှတ်ပြုမူနှင့်
မိုင်ဂရိတ်လုပ်ငန်းများအတွက် ရှောင်တခင်ပြီး သတ်မှတ်ထားတဲ့ protocol ပြများကို ရှင်းပြပေးထားပါတယ်။

## နိဒါန်း

ဒီသင်ခန်းစာမှာ MCP တောင်းဆိုမှုတွေထဲ Sampling parameter တွေကို ဘယ်လို ပြင်ဆင်ရမယ်နဲ့ Sampling နောက်ခံ protocol ကို ဘယ်လို လည်ပတ်တယ်ဆိုတာ လေ့လာကြမယ်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာတစ်ခု ပြီးသွားတဲ့အခါ၊ သင်သည် အောက်ပါအချက်များကို နားလည်နိုင်ပါမယ်။

- MCP တွင် ရနိုင်သည့် အဓိက sampling parameter များကို နားလည်နိုင်ရန်။
- အသုံးအနှုန်းအမျိုးမျိုးအတွက် sampling parameter များကို ပြင်ဆင်နိုင်ရန်။
- ပြန်လည်ထုတ်ယူနိုင်ဖို့ deterministic sampling ကို လုပ်ဆောင်နိုင်ရန်။
- context နှင့် အသုံးပြုသူနှစ်သက်မှုအပေါ်မူတည်၍ sampling parameter များကို အလိုအလျောက်ပြောင်းလဲလုပ်ဆောင်နိုင်ရန်။
- မတူညီသည့် နယ်ပယ်များတွင် မော်ဒယ်စွမ်းဆောင်ရည်ကို မြှင့်တင်ပေးရန် sampling နည်းဗျူဟာများကို သုံးနိုင်ရန်။
- MCP ၏ client-server လည်ပတ်မှု၌ sampling က ဘယ်လိုအလုပ်လုပ်သည်ကို နားလည်နိုင်ရန်။

## MCP တွင် Sampling ၏ လည်ပတ်ပုံ

MCP တွင် sampling flow သည် အောက်ပါအဆင့်များအတိုင်း လည်ပတ်သည်။

1. ဆာဗာက client ထံသို့ `sampling/createMessage` တောင်းဆိုမှု ပေးပို့သည်။
2. client က တောင်းဆိုမှုကို ပြန်လည်ဆန်းစစ်ပြီး ပြုပြင်နိုင်သည်။
3. client က LLM မှ sampling လုပ်သည်။
4. client က ဖြည့်တင်းချက်ကို ပြန်လည်ဆန်းစစ်သည်။
5. client က ရလာဒ်ကို ဆာဗာထံ ပြန်ပို့သည်။

ယင်း human-in-the-loop ဒီဇိုင်းသည် အသုံးပြုသူများအား LLM ကြည့်ရှု၍ ဖန်တီးသည့် အရာများကို ထိန်းချုပ်ခွင့် ပေးပါသည်။

## Sampling Parameter များအကြောင်း အနှစ်ချုပ်

MCP သည် client မှ တောင်းဆိုမှုများတွင် ပြင်ဆင်နိုင်သည့် sampling parameter များကို အောက်ပါအတိုင်း သတ်မှတ်ထားသည်။

| Parameter | ဖော်ပြချက် | သာမန် အကွာအဝေး |
|-----------|-------------|---------------|
| `temperature` | token ရွေးချယ်ရာတွင် မပြည့်မစုံမှုကို ထိန်းချုပ်သည် | 0.0 - 1.0 |
| `maxTokens` | ထုတ်ပေးမည့် token အများဆုံး အရေအတွက် | အရေအတွက် တန်ဖိုး |
| `stopSequences` | တွေ့ရှိသောအခါ ထုတ်ပေးမှုကို ရပ်စဲသည့် ပုံစံစွဲများ | string များပါသော array |
| `metadata` | ပံ့ပိုးသူအလိုက် ထပ်ဆောင်း ပါရာမီတာများ | JSON object |

အများအပြား LLM ပံ့ပိုးသူများက `metadata` ကဏ္ဍမှတဆင့် ထပ်ဆောင်း parameter များကို ထောက်ပံ့ပေးပြီး အောက်ပါအတိုင်း ဖြစ်နိုင်ပါသည်။

| Common Extension Parameter | ဖော်ပြချက် | သာမန် အကွာအဝေး |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - token များကို အမြင့်ဆုံးစုစုပေါင်းဖြစ်နိုင်ချေတန်ဖိုးအထိ အကန့်အသတ် သတ်မှတ်ခြင်း | 0.0 - 1.0 |
| `top_k` | token ရွေးချယ်မှုကို အထိပ်ဆုံး K များထိ အကန့်အသတ်ဝင်စေခြင်း | 1 - 100 |
| `presence_penalty` | ယခင်စာသားတွင် ပါဝင်မှုအပေါ်မူတည်၍ token များအား ဒဏ်ကြေးပေးခြင်း | -2.0 - 2.0 |
| `frequency_penalty` | ယခင်စာသားတွင် ထပ်ရေမြင့်မှုအပေါ်မူတည်၍ token များအား ဒဏ်ကြေးပေးခြင်း | -2.0 - 2.0 |
| `seed` | ပြန်လည်ထုတ်ယူနိုင်စေရန် အတိအကျ random seed တန်ဖိုး | အရေအတွက် တန်ဖိုး |

## နမူနာ တောင်းဆိုမှု ဖော်မတ်

MCP မှ client မှ sampling တောင်းဆိုတာရဲ့ နမူနာပုံစံဖြစ်သည်။

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## ပြန်ကြားချက် ဖော်မတ်

client သည် ဖြည့်တင်းချက်ရလဒ်ကို ပြန်လည်ပေးပို့သည်။

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## လိမ့်လည် ထိန်းချုပ်မှုများ

MCP sampling ကို လူ့စောင့်ကြည့်မှုနှင့် ဆောင်ရွက်ရန် ဒီဇိုင်းဆွဲထားသည်။


- **ပရောမ့်များအတွက်**:
  - Clients များသည် အသုံးပြုသူများအား အကြံပြုထားသော ပရောမ့်ကို ပြသသင့်သည်
  - အသုံးပြုသူများသည် ပရောမ့်များကို ပြင်ဆင်ခြင်း သို့မဟုတ် ငြင်းဆန်ခြင်း ပြုလုပ်နိုင်သင့်သည်
  - စနစ်ပရောမ့်များကို စစ်ထုတ်ခြင်း သို့မဟုတ် ပြင်ဆင်ခြင်း ပြုလုပ်နိုင်သည်
  - အကြောင်းအရာ ထည့်သွင်းဖော်ပြခြင်းကို Client မှ ထိန်းချုပ်သည်

- **ပြီးစီးမှုများအတွက်**:
  - Clients များသည် အသုံးပြုသူများအား ပြီးစီးမှုကို ပြသသင့်သည်
  - အသုံးပြုသူများသည် ပြီးစီးမှုများကို ပြင်ဆင်ခြင်း သို့မဟုတ် ငြင်းဆန်ခြင်း ပြုလုပ်နိုင်သင့်သည်
  - Clients များသည် ပြီးစီးမှုများကို စစ်ထုတ်ခြင်း သို့မဟုတ် ပြင်ဆင်ခြင်း ပြုလုပ်နိုင်သည်
  - အသုံးပြုသူများသည် အသုံးပြုမည့် မော်ဒယ်ကို ထိန်းချုပ်သည်

ဒီအယူအဆများကို ထည့်သွင်းစဉ်းစားပြီး LLM ပံ့ပိုးသူများအကြား အများဆုံး ထောက်ခံပေးသည့် parameters များအား ဦးတည်ပြီး sampling ကို အမျိုးမျိုးသော programming ဘာသာစကားများတွင် မည်သို့ အကောင်အထည်ဖော်မည်ကို ကြည့်ကြမယ်။

## လုံခြုံရေး စဉ်းစားမှုများ

MCP တွင် sampling အကောင်အထည်ဖော်ရာတွင် ဒီလုံခြုံရေး အကောင်းဆုံး လုပ်နည်းများကို စဉ်းစားပါ။

- **Client ကို ပို့ရန် မက်ဆေ့ခ်ျအကြောင်းအရာအားလုံးကို အတည်ပြုပါ**
- **ပရောမ့်များနှင့် ပြီးစီးမှုများမှ စိစစ်ရန် အသုံးပြုသော sensitive အချက်အလက်များကို သန့်စင်ပါ**
- **အကန့်အသတ်များကို ထပ်မံ သတ်မှတ်ခြင်းဖြင့် မမှန်သော အသုံးပြုမှုများကို တားဆီးပါ**
- **Sampling အသုံးပြုမှုကို ထူးခြားသော ပုံစံများအတွက် စောင့်ကြည့်ပါ**
- **လုံခြုံသော protocol များဖြင့် အချက်အလက်များကို ကုန်လမ်းအသက်သွားရာတွင် ကွပ်ကဲသိမ်းဆည်းပါ**
- **အသုံးပြုသူဒေတာ ကို ဆိုင်ရာ စည်းမျဉ်းစည်းကမ်းများအတိုင်း ထိန်းသိမ်းပါ**
- **Sampling အမိန့်များကို လိုက်နာမှုနှင့် လုံခြုံရေးအတွက် စစ်ဆေးပါ**
- **ကုန်ကျစရိတ်ပမာဏကို သင့်တော်သည့်အကန့်အသတ်များဖြင့် ထိန်းချုပ်ပါ**
- **Sampling request များအတွက် အချိန်ပိတ်ဆိုင်းမှု ထည့်သွင်းပါ**
- **မော်ဒယ်အမှားများကို သေချာစွာ ကိုင်တွယ်ပြီး သင့်တော်သည့် fallback များဖြင့် ဖြေရှင်းပါ**

Sampling parameters များသည် ဘာသာစကားမော်ဒယ်များ၏ အပြုအမူကို ညှိနှိုင်းရန် အခွင့်အလမ်းပေးပြီး ရလဒ်များတွင် ရိုးရှင်းမှုနှင့် ဖန်တီးမှုကြားဖြတ်၍ လိုအပ်သည့် ညှိအမျိုးအစားကို ရရှိစေရန် ဖြစ်သည်။

ဒီ parameters များကို programming ဘာသာစကားများအလိုက် မည်သို့ ပြင်ဆင်ရမည်ကို ကြည့်မယ်။

# [.NET](#tab-dotnet)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

အထက်ပါ ကုဒ်တွင်

- အထူးသတ်မှတ်ထားသော server URL ဖြင့် MCP client တစ်ခု ဖန်တီးခဲ့သည်။
- `temperature`, `top_p`, နှင့် `top_k` ကဲ့သို့သော sampling parameters များဖြင့် request တစ်ခုကို ပြင်ဆင်ခဲ့သည်။
- 요청을 전송하고 생성된 텍스트를 인쇄했습니다.
- အသုံးပြုခဲ့သည်မှာ
    - `allowedTools` ကို မော်ဒယ်သည် ဖန်တီးမှု့တွင် အသုံးပြုနိုင်သည့် tools များ ဖော်ပြရန် သုံးပြီး ဒီအကွာအဝေးတွင် `ideaGenerator` နှင့် `marketAnalyzer` tools များကို ဖန်တီးမှု app အကြံများ ထုတ်ဖော်ရာတွင် ကူညီခဲ့သည်။
    - `frequencyPenalty` နှင့် `presencePenalty` ကို ထွက်ရှိရာမှာ ထပ်တလဲလဲမှုနှင့် မတူညီမှုကို ထိန်းချုပ်ရန် သုံးခဲ့သည်။
    - `temperature` ကို ထွက်ရှိသော အဖြေ၏ အကြမ်းစားမှုကို ထိန်းချုပ်ရာတွင် အသုံးပြုသည်၊ တန်ဖိုးမြင့်သည့်အခါ ပိုမိုဖန်တီးမှုဖြစ်စေသည်။
    - `top_p` ကို အထိရောက်ဆုံး ပြုတ်ထွက်မှု mass ပါဝင်သော token များကို အများစုရွေးချယ်ခြင်းမှ လျှော့ချရန် အသုံးပြုသည်၊ ထောက်ပံ့သော စာသားအရည်အသွေးမြင့်စေသည်။
    - `top_k` ကို အကြွန်းအနီဆုံး token အပေါင်း K အတွင်းသာ မော်ဒယ်ကို ထိန်းချုပ်ပြီး ပိုမိုကိုက်ညီသော အဖြေထုတ်ရန် ကူညီသည်။
    - `frequencyPenalty` နှင့် `presencePenalty` ကို ထပ်တလဲလဲမှုကို လျော့နည်းစေပြီး ထွက်ရှိမှုအမျိုးမျိုးကို ကြိုးပမ်းစေသည်။

# [JavaScript](#tab/javascript)

```javascript
// JavaScript နမူနာ။ အပူချိန်နှင့် Top-P စမ်းသပ်မှုအစီအစဉ်
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP client ကို စတင်သတ်မှတ်ခြင်း
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // sampling parameter များ မတူညီသည့် request များ ကို ပြင်ဆင်ခြင်း
  const creativeSampling = {
    temperature: 0.9,    // အပူချိန်မြင့်မားခြင်း = ရောမတ်စွမ်းအင်/တီထွင်ဆန်းသစ်မှု အများအပြား
    topP: 0.92,          // အလားအလာ ၉၂% အထိ token များကို စဉ်းစားပါ
    frequencyPenalty: 0.6, // token အစဉ်များ ပြန်ထပ်ဖြစ်ပေါ်မှု လျော့နည်းစေပါ
    presencePenalty: 0.4   // ယခုစာပိုဒ်တွင် ပေါ်နေသော token များအား ဒဏ်ခတ်ပါ
  };
  
  const factualSampling = {
    temperature: 0.2,    // အပူချိန်နိမ့်ခြင်း = တိကျမှန်ကန်မှု/အချက်အလက် ပိုများခြင်း
    topP: 0.85,          // token ရွေးချယ်မှု သာတူတင့်တယ်မှု နည်းနည်းပိုများခြင်း
    frequencyPenalty: 0.2, // ပြန်ထပ်မှုဒဏ်ခတ်မှု အနည်းဆုံး
    presencePenalty: 0.1   // ပေါ်ပေါက်မှုဒဏ်ခတ်မှု အနည်းဆုံး
  };
  
  try {
    // sampling configuration မတူညီသည့် request နှစ်ခု ပို့ပါ
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

အထက်ပါ ကုဒ်တွင်

- server URL နှင့် API key ပါရှိသည့် MCP client ကို စတင်ပြုလုပ်ခဲ့သည်။
- ဖန်တီးမှု သွယ်ဝိုက်မှုများနှင့် သက်ဆိုင်သော အလုပ်များအတွက် sampling parameters နှစ်ခု ခွဲခြားသတ်မှတ်ခဲ့သည်။
- အဲ့ဒီ သတ်မှတ်ချက်များဖြင့် မော်ဒယ်ကို တ ါချိန်တည်းတွင် အထူး tools များ အသုံးပြုရာ request များ ပို့ခဲ့သည်။
- ကွဲပြားသော sampling parameters များ၏ သက်ရောက်မှုကို ပြသရန် ထွက်ရှိလာသော အဖြေများကို ပုံနှိပ်ပြသခဲ့သည်။
- `allowedTools` ကို မော်ဒယ်သည် ဖန်တီးမှုအတွက် အသုံးပြုခဲ့သော tools များကို ဖော်ပြရန် သုံးခဲ့သည်၊ ဒီအခါမှာ `ideaGenerator` နှင့် `environmentalImpactTool` ကို ဖန်တီးမှုအတွက်၊ နှင့် `factChecker` နှင့် `dataAnalysisTool` ကို သက်ဆိုင်ရာ အချက်အလက်အမှုများအတွက် အသုံးပြုခဲ့သည်။
- အဖြေ၏ အကြမ်းစားမှုရှိခြင်းကို ထိန်းချုပ်ရန် `temperature` ကို သုံးခဲ့သည်၊ တန်ဖိုးမြင့်လျှင် ပိုမိုဖန်တီးမှု့ဖြစ်စေသည်။

- စနစ်တကျ ရွေးချယ်မှုအတွက် `top_p` ကိုအသုံးပြုခဲ့သည်၊ ထိုကွောငျ့ ထုတ်လုပ်လိုက်သောစာသား၏အရည်အသွေး တိုးတက်စေရန် အထက်ဆုံး စုစုပေါင်း ဖြစ်နိုင်ချေ အဖုံးကို ထည့်သွင်းပါသည်။
- ထွက်ရှိမှုတွင် ထပ်တလဲလဲမှု ပြည့်မှီခြင်းကို လျှော့ချဖို့နှင့် မတူကွဲပြားမှုကိုထောက်ပံ့ဖို့ `frequencyPenalty` နှင့် `presencePenalty` ကိုအသုံးပြုခဲ့သည်။
- ပိုမိုဆင်ခြင်ချက်ရှိသော တုံ့ပြန်မှုများ ပြုလုပ်နိုင်ရန်အတွက် စနစ်အား အမြင့်ဆုံး ဖြစ်နိုင်ချေရှိသော ကုဒ်တံဆိပ်များ (token) K ခုအတွင်း သတ်မှတ်ဖို့ `top_k` ကိုအသုံးပြုခဲ့သည်။

---

## သတ်မှတ်နေရာ sampling

အမြဲတမ်းတူညီသော ထွက်ရှိမှုများလိုအပ်သော အပလီကေးရှင်းများအတွက် သတ်မှတ်နေရာ sampling သည် တူညီသောရလဒ်များထုတ်ပေးရန် အာမခံသည်။ ဤသည်ကို အလုပ်လုပ်ပုံမှာ fixed random seed ကို အသုံးပြုပြီး temperature ကို သုညထားခြင်းဖြစ်သည်။

ဘာသာစကားအစီအစဉ်များ အမျိုးမျိုးတွင် သတ်မှတ်နေရာ sampling ကို ပြသရန် အောက်ပါ နမူနာအကောင်အထည် ဖော်ဟန်ချက်ကို ကြည့်ကြရအောင်။

# [Java](#tab/java)

```java
// Java ဥပမာ: သတ်မှတ်ထားသော Seed ဖြင့် သေချာသော တုံ႔ပြန်မှုများ
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // သတ်မှတ်ထားသော ရလဒ်များအတွက် fixed seed ကို အသုံးပြုခြင်း
        
        // fixed seed ဖြင့် ပထမဆုံး တောင်းဆိုမှု
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // အများဆုံး သေချာမှုအတွက် အပူချိန် သုည
            .build();
            
        // အတူတူ seed ဖြင့် ဒုတိယ တောင်းဆိုမှု
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // တောင်းဆိုမှု နှစ်ခုလုံး ကို အကောင်အထည်ဖော်ရန်
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // seed နှင့် အပူချိန်=0 ကြောင့် တုံ့ပြန်မှုများ တူညီရမည်
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည်-

- သတ်မှတ်ထားသော server URL ဖြင့် MCP client ကို ဖန်တီးခဲ့သည်။
- တူညီသော prompt၊ fixed seed နှင့် temperature သုည ဖြစ်သော တောင်းဆိုချက် ၂ ခုကို သတ်မှတ်ခဲ့သည်။
- နှစ်ခုလုံးဟာ တောင်းဆိုချက်များကို ပို့ပြီး ထုတ်လုပ်ထားသောစာသားကို ပုံနှိပ်ပြသခဲ့သည်။
- sampling configuration ၏ သတ်မှတ်ချက်ကြောင့် (seed နဲ့ temperature တူလို့) တုံ့ပြန်မှုများမှာ တူညီကြောင်း ပြသခဲ့သည်။
- `setSeed` ကို အသုံးပြုပြီး fixed random seed ကို သတ်မှတ်ခဲ့သည်၊ ထို့ကြောင့် အချိန်တိုင်းတွင် တူညီသော input အတွက် တူညီသော output ကို စက်စနစ်ထုတ်ပေးနိုင်ရန်။
- `temperature` ကို သုညထားပြီး အလွန်မြင့်မားသော သတ်မှတ်ချက်ရှိမှုအခြေအနေ ဖြစ်သွားစေရန်၊ ထို့ကြောင့် စနစ်သည် အမြဲအလွန်ဖြစ်နိုင်ခြေရှိသော နောက်ထပ် token ကိုသာ ရွေးချယ်မည်ဖြစ်သည်။

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript နမူနာ - Seed ထိန်းချုပ်မှုဖြင့် သေချာသောတုံ့ပြန်မှုများ
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // ပထမဆုံးတောင်းဆိုမှု - သတ်မှတ်ထားသော seed ဖြင့်
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // အမြင့်ဆုံး သေချာမှုအတွက် အပူချိန်အသုံးပြုမှုကို ဇီုရိုထားခြင်း
    });
    
    // ဒုတိယတောင်းဆိုမှု - တူညီသော seed နှင့် အပူချိန်ဖြင့်
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // တတိယတောင်းဆိုမှု - seed ကွဲပြားသော်လည်း အပူချိန်တူညီသော
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည်-

- server URL ဖြင့် MCP client ကို စတင်ရှေ့ဆောင်ထားသည်။
- တူညီသော prompt နှင့် fixed seed နဲ့ temperature သုညရှိသော တောင်းဆိုချက် ၂ ခုကို သတ်မှတ်ခဲ့သည်။
- တောင်းဆိုချက် ၂ ခုလုံးကို ပို့ပြီး ထုတ်ပေးထားသော စာသားကို ပုံနှိပ်ပြသခဲ့သည်။
- sampling configuration ၏ သတ်မှတ်ချက်ကြောင့် (seed နဲ့ temperature တူလို့) တုံ့ပြန်မှုများမှာ တူညီကြောင်း ပြသခဲ့သည်။
- `seed` ကို ဖြည့်သွင်းသုံးပြီး fixed random seed ကို သတ်မှတ်ပြီး input တူသော အခါ output တူစေရန်။
- `temperature` ကို သုညထားကာ အပြောင်းအလဲမရှိသော sampling ဖြစ်စေရန် သတ်မှတ်ခဲ့သည်။
- တတိယတောင်းဆိုချက်အတွက် ကွဲပြားသော seed ကို အသုံးပြုပြီး prompt နှင့် temperature တူရှိသော်လည်း output မတူကြောင်း ပြသခဲ့သည်။

---

## စွမ်းဆောင်ရည်အလိုက် Sampling ပြင်ဆင်မှု

သံစဉ်ပေါ်မူတည်၍ sampling ပါရာမီတာများကို ချိန်ညှိခြင်းဖြစ်သည်။ ဤသည်မှာ အလုပ်လုပ်ပုံအလိုက်၊ အသုံးပြုသူ၏နှစ်သက်ချက်များ၊ သို့မဟုတ် သမိုင်းပြတ်ထားမှုများအပါအဝင် sampling ပါရာမီတာများကို dynamic အညီ ပြောင်းလဲခြင်းဖြစ်သည်။

ဘာသာစကားအစီအစဉ် အမျိုးမျိုးတွင် စွမ်းဆောင်ရည်အလိုက် sampling ဆောင်ရွက်သည့် နည်းလမ်းကို ကြည့်ကြရအောင်။

# [Python](#tab/python)

```python
# Python ဥပမာ - မေးလ်ညွှန်ကြားမှုအခြေအနေအပေါ် အခြေခံသော dynamic sampling
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # အလုပ်အမျိုးအစားများအတွက် sampling preset များသတ်မှတ်ပါ
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # အခြေခံ preset ကို ရွေးချယ်ပါ
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # အသုံးပြုသူ စိတ်ကြိုက်မှုများ ရှိပါက ပြင်ဆင်ပါ
        if user_preferences:
            if "creativity_level" in user_preferences:
                # ဖန်တီးမှုနှုန်း (1-10) အပေါ် အပူချိန်ကို စံချိန်ညှိပါ
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # အလိုရှိသော တုံ့ပြန်မှု မျိုးစုံစေမှုအတွက် top_p ကို ညှိပါ
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # စိတ်ကြိုက် sampling parameter များဖြင့် မေးလ်ပို့ဆောင်ပါ
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # ထင်ရှားမှုအတွက် sampling metadata ပါသော တုံ့ပြန်ချက်ကို ညွှန်ပြန်ပါ
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည်-

- sampling ကိုပြောင်းလဲမှုအလိုက် စီမံခန့်ခွဲသော `DynamicSamplingService` ခရစ်(ကလပ်) တည်ဆောက်ခဲ့သည်။
- အလုပ်အမျိုးအစားအလိုက် sampling preset များကို သတ်မှတ်ခဲ့သည် (ဖန်တီးမှု၊ သမိုင်းတင်ပြမှု၊ ကုဒ်ရေးခြင်း၊ သုံးသပ်မှု)။
- အလုပ်အမျိုးအစားအလိုက် ကိုယ်တိုင် sampling preset တစ်ခုကို ရွေးချယ်ခဲ့သည်။
- အသုံးပြုသူနှစ်သက်ချက်များအပေါ် မူတည်၍ sampling ပါရာမီတာများကို ချိန်ညှိခဲ့သည်၊ ဥပမာ ဖန်တီးမှုအဆင့် နှင့် မတူကွဲပြားမှု။
- dynamic sampling ပါရာမီတာဖြင့် တောင်းဆိုချက်ကို ပို့ခဲ့သည်။
- ထုတ်လုပ်ထားသော စာသားနှင့် sampling ပါရာမီတာများ၊ အလုပ်အမျိုးအစားကို ပြန်လည်ထုတ်ပေးခဲ့သည်။
- ထွက်ရှိမှုတွင် အလှည့်အပြောင်းရှိမှုကို ထိန်းချုပ်ရန် `temperature` ကို အသုံးပြုခဲ့သည်၊ တန်ဖိုးမြင့်မားလာမှသာ ပိုမိုဖန်တီးမှုရှိသော တုံ့ပြန်မှုများသို့ ဦးတည်သည်။
- စနစ်မွန်ကန်စွာ ထုတ်ပေးနိုင်ဖို့အတွက် စုစုပေါင်း ဖြစ်နိုင်ချေ အဖုံးထဲရှိ token များ၏ ရွေးချယ်မှုကို `top_p` ဖြင့် ကန့်သတ်သုံးစွဲခဲ့သည်။
- ထပ်တလဲလဲမှုနည်းစေဖို့နှင့် မတူကွဲပြားမှုကို ပိုမိုပံ့ပိုးဖို့အတွက် `frequency_penalty` ကိုအသုံးပြုခဲ့သည်။
- အသုံးပြုသူ သတ်မှတ်ချက်များအရ စနစ် sampling ပါရာမီတာများကို ကိုယ်တိုင်ညှိနှိုင်းနိုင်ရန် `user_preferences` ကို အသုံးပြုခဲ့သည်။
- တောင်းဆိုချက်အမျိုးအစားအပေါ်မူတည်၍ sampling နည်းလမ်းကို သတ်မှတ်ရန် `task_type` ကို အသုံးပြုခဲ့သည်၊ ထိုကွောငျ့ အလုပ်အမျိုးအစားအလိုက် ပိုမိုသင့်လျော်သော တုံ့ပြန်မှုရရှိနိုင်သည်။
- ကိုက်ညီသော sampling ပါရာမီတာများဖြင့် prompt ကို ပို့ရန် `send_request` နည်းလမ်းကိုအသုံးပြုခဲ့သည်၊ ထို့ကြောင့် စနစ်သည် သတ်မှတ်ချက်နှင့် ကိုက်ညီသော စာသားများ ထုတ်ပေးနိုင်ပါသည်။
- စနစ်၏တုံ့ပြန်ချက်ဖြစ်သော `generated_text` ကို ရယူပြီး sampling ပါရာမီတာများနှင့် အလုပ်အမျိုးအစားနှင့်အတူ ပြန်လည်ထုတ်ပေးခဲ့သည်။
- အသုံးပြုသူနှစ်သက်ချက်များကို ဂဏန်းကွဲလမ်းအတွင်းတွင်ထားရန် `min` နှင့် `max` function များကို အသုံးပြုပြီး sampling ပုံစံလွဲမှားခြင်းမဖြစ်စေရန် ထိန်းသိမ်းခဲ့သည်။

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript နမူနာ - အသုံးပြုသူ အခြေအနေအပေါ် မူတည်၍ dynamic sampling configuration ကို ပြုလုပ်ခြင်း
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // မူလ sampling ပရိုဖိုင်းများကို သတ်မှတ်ပါ
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // သမိုင်းဝင် လုပ်ဆောင်ချက်များကို စောင့်ကြည့်ပါ
    this.performanceHistory = [];
  }
  
  // prompt မှ တာဝန်အမျိုးအစားကို ဖော်ထုတ်ပါ
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // ရိုးရှင်းသော heuristic ဖော်ထုတ်ခြင်း - ML classification ဖြင့် တိုးမြှင့်နိုင်သည်
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // ပုံမှန်ထားပါ၊ အမျိုးအစားမရှင်းလင်းပါက စကားဝိုင်းအဖြစ် သတ်မှတ်ပါ
    return 'conversational';
  }
  
  // context နှင့် အသုံးပြုသူနှစ်သက်မှုများအပေါ် မူတည်၍ sampling parameter များတွက်ချက်ပါ
  getSamplingParameters(prompt, context = {}) {
    // တာဝန်အမျိုးအစားကို ဖော်ထုတ်ပါ
    const taskType = this.detectTaskType(prompt, context);
    
    // မူလပရိုဖိုင်းကို ရယူပါ
    let params = {...this.samplingProfiles[taskType]};
    
    // အသုံးပြုသူနှစ်သက်မှုအပေါ် အဆင်ပြေစေရန် ညှိနှိုင်းပါ
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 မှ သင့်တော်သော အပူချိန်ပြင်ပားအထိ အတိုင်းအတာ တိုးချဲ့ပါ
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // အတိအကျမြင့်မားခြင်းသည် topP ကို လျော့နည်းစေသည် (ရွေးချယ်မှု ပိုမို စူးစမ်းမှုရှိစေသည်)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // တည်ငြိမ်မှုမြင့်မှုသည် ဒဏ်သတ်မှုများကို လျော့စေသည်
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // လုပ်ဆောင်ချက်သမိုင်းမှ သင်ယူထားသော ပြင်ဆင်မှုများကို သက်ရောက်စေပါ
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // ရိုးရှင်းသော ကိုက်ညီမှု စည်းမျဉ်း - ပိုမိုရှုပ်ထွေးသည့် calculation များဖြင့် တိုးတက်စေနိုင်သည်
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // နောက်ဆုံးသုံးသိန်းသမိုင်းကိုသာ ဂရုစိုက်ပါ
    
    if (relevantHistory.length > 0) {
      // မျှတသောလုပ်ဆောင်ချက် အမှတ်များကိုတွက်ချက်ပါ
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // လုပ်ဆောင်ချက် threshold အောက်ရှိပါက parameter များကို ပြင်ဆင်ပါ
      if (avgScore < 0.7) {
        // ဘေးကင်းသော တန်ဖိုးများဘက်သို့ နည်းငယ်ပြင်ဆင်ပါ
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // အနာဂတ် ပြင်ဆင်မှုများအတွက် တုံ့ပြန်မှုလုပ်ဆောင်ချက်များကို မှတ်တမ်းတင်ပါ
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // တုံ့ပြန်မှု အရည်အသွေး 0-1 အဆင့်
    });
    
    // သမိုင်းအရွယ်အစားကို အကန့်အသတ်ထားပါ
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // ကောင်းမွန်ဆုံး sampling parameter များရယူပါ
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // ကောင်းမွန်သော parameter များဖြင့် တောင်းဆိုမှု ပို့ပါ
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // အသုံးပြုသူ သုံးသပ်ချက်အခုဖြစ်ပါက အနာဂတ် optimization အတွက် မှတ်တမ်းတင်ပါ
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// နမူနာ အသုံးပြုမှု
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // အသုံးပြုသူနှစ်သက်ချက်ဖြင့် ဖန်တီးမှုအလုပ်
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // ဖန်တီးမှု မြင့်မားခြင်း (1-10)
          consistency: 3  // တည်ငြိမ်မှု နိမ့်ကျခြင်း (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // ကုဒ်ဖန်တီးခြင်း အလုပ်
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // ဖန်တီးမှု နိမ့်ကျခြင်း
          precision: 8,   // အတိအကျ မြင့်မားခြင်း
          consistency: 9  // တည်ငြိမ်မှု မြင့်မားခြင်း
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည်-

- task type နှင့် user preferences များအရ dynamic sampling ကို စီမံခန့်ခွဲသော `AdaptiveSamplingManager` ခရစ်(ကလပ်) တည်ဆောက်ခဲ့သည်။
- အလုပ်အမျိုးအစားအလိုက် sampling profile များကို သတ်မှတ်ထားသည် (ဖန်တီးမှု၊ သမိုင်းတင်ပြမှု၊ ကုဒ်ရေးခြင်း၊ စကားပြောဆိုမှု)။
- prompt မှ task type ကို ရိုးရှင်းသော heuristic များဖြင့် ရှာဖွေသာ နည်းလမ်း တစ်ခုကို အကောင်အထည်ဖော်ခဲ့သည်။
- task type ရှာဖွေရေးနှင့် user preferences အပေါ်မူတည်၍ sampling ပါရာမီတာများကိုတွက်ချက်ခဲ့သည်။
- သမိုင်းရဲ့စွမ်းဆောင်မှုအတိုင်း သိရှိရသည့် ပြောင်းလဲမှုများကို အသုံးပြုပြီး sampling ပါရာမီတာများကို တိုးတက်အောင် ဆောင်ရွက်ခဲ့သည်။
- နောက်ထပ် ပြောင်းလဲမှုများအတွက် အတိတ်စွမ်းဆောင်မှုများကို မှတ်တမ်းတင်ပြီး စနစ်အနေဖြင့် အတွေ့အကြုံများမှ သင်ယူဖို့။
- dynamic sampling ပါရာမီတာများဖြင့် တောင်းဆိုချက်များကို ပို့ပြီး ထုတ်လွှင့်ထားသော စာသားများနှင့် ပါရာမီတာများ၊ ရှာဖွေတွေ့ရှိထားသော task type ကို ပြန်လည်ထုတ်ပေးခဲ့သည်။
- အသုံးပြုခဲ့သည် -
    - `userPreferences` ကို အသုံးပြုသူ သတ်မှတ်ချက်ဖြင့် ဖန်တီးမှု၊ တိကျမှု၊ ကိုက်ညီမှု များ အပေါ်မူတည်၍ sampling ပါရာမီတာ များကို ကိုယ်တိုင်ညှိနှိုင်းရန်။
    - `detectTaskType` ကို prompt အပေါ်မူတည်၍ task အမျိုးအစားကို သတ်မှတ်ရန်၊ ဤနည်းလမ်းဖြင့် ပိုမိုသင့်တော်သော တုံ့ပြန်မှုများ ရရှိစေလိမ့်မည်။
    - `recordPerformance` ကို ဖန်တီးထားသော တုံ့ပြန်မှု စွမ်းဆောင်မှုမှတ်တမ်းများကို မှတ်တမ်းတင်ပြီး စနစ်အနေဖြင့် တိုးတက်ရန်သင်ယူမှု။
    - `applyLearnedAdjustments` ကို သမိုင်းတာဝန်ထမ်းဆောင်မှုအပေါ်မှာ အခြေခံ၍ sampling ပါရာမီတာများ ပြောင်းလဲပေးကာ စနစ်၏ အရည်အသွေးမြင့်တုံ့ပြန်ပေးနိုင်ဖို့။
    - `generateResponse` ကို adaptive sampling နှင့်အတူ တုံ့ပြန်မှု ထုတ်လုပ်မှု လုပ်ငန်းစဉ်တစ်ခုလုံးကို encapsulate ဖော်ထုတ်ထားခြင်း၊ အခြား prompt နှင့် context များဖြင့် လွယ်ကူစွာခေါ်နိုင်မှု။
    - `allowedTools` ကို စနစ်ထုတ်လုပ်မှုလုပ်စဉ်တွင် အသုံးပြုနိုင်သည့် ကိရိယာများကို သတ်မှတ်ရန်၊ ပိုမို context ကို တွေးခေါ်နိုင်သော တုံ့ပြန်မှုများ ရရှိစေရန်။
    - `feedbackScore` ကို အသုံးပြုသူများထံမှ ထုတ်လုပ်ထားသောတုံ့ပြန်မှုအရည်အသွေးအပေါ် မှတ်ချက်များ ပေးနိုင်ရန်၊ ထို့ကြောင့် စနစ်၏ စွမ်းဆောင်ရည် တိုးတက်မှုကို ပိုမိုကောင်းမွန်အောင် တိုးတက်စေခြင်း။
    - `performanceHistory` ကို အတိတ်၏ အတွေ့အကြုံများကို ကောင်းမွန်စွာ မှတ်တမ်းတင်ထားခြင်း၊ စနစ်အနေဖြင့် အရပ်ဘက်မှ သင်ယူနိုင်ရန်။
    - `getSamplingParameters` ကို တောင်းဆိုချက်၏ အခြေအနေရေးရာအပေါ် မူတည်၍ sampling ပါရာမီတာများကို ဒိုင်နမစ်ပြောင်းလဲနိုင်စေရန်။
    - `detectTaskType` ကို prompt အပေါ် မူတည်၍ အလုပ်အမျိုးအစားအား သတ်မှတ်ရာတွင် အသုံးပြု၊ request အမျိုးအစားအသီးသီးအတွက် sampling နည်းလမ်းများကို သုံးစွဲရန်။
    - `samplingProfiles` ကို အလုပ်အမျိုးအစားအလိုက် အခြေခံ sampling ပုံစံများ သတ်မှတ်ထားခြင်း၊ ဒါမှ တောင်းဆိုချက်၏ ကိုယ်အပေါ်အခြေခံ ချိန်ညှိနိုင်စေရန်။

---

## နောက်တစ်ချက်

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
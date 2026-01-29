# Sampling in Model Context Protocol

Sampling သည် MCP ၏ အင်အားကြီးသော feature တစ်ခုဖြစ်ပြီး၊ server များသည် client မှတဆင့် LLM completions များကို request ပြုလုပ်နိုင်စေပြီး၊ agentic behaviors များကို တိုးတက်စေသည့်အပြင် security နှင့် privacy ကိုလည်း ထိန်းသိမ်းပေးသည်။ သင့်တော်သော sampling configuration သည် response အရည်အသွေးနှင့် performance ကို အလွန်ကောင်းမွန်စေသည်။ MCP သည် မော်ဒယ်များသည် စာသားများကို random, creative နှင့် coherent ဖြစ်စေရန် သတ်မှတ်ထားသော parameters များဖြင့် ဘယ်လို generate လုပ်မည်ကို စံပြနည်းဖြင့် ထိန်းချုပ်ပေးသည်။

## နိဒါန်း

ဒီသင်ခန်းစာတွင် MCP requests တွင် sampling parameters များကို ဘယ်လို configure လုပ်ရမည်နှင့် sampling ၏ underlying protocol mechanics များကို လေ့လာမည်ဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးချိန်တွင် သင်သည် -

- MCP တွင် ရရှိနိုင်သည့် sampling parameters အဓိကများကို နားလည်နိုင်မည်။
- အသုံးပြုမှုအမျိုးမျိုးအတွက် sampling parameters များကို configure လုပ်နိုင်မည်။
- ပြန်လည်ထုတ်ယူနိုင်သော ရလဒ်များအတွက် deterministic sampling ကို အကောင်အထည်ဖော်နိုင်မည်။
- context နှင့် user preferences အပေါ် မူတည်၍ sampling parameters များကို dynamic ပြောင်းလဲနိုင်မည်။
- မော်ဒယ် performance ကို တိုးတက်စေရန် sampling strategies များကို အသုံးပြုနိုင်မည်။
- MCP ၏ client-server flow တွင် sampling ၏ လည်ပတ်ပုံကို နားလည်နိုင်မည်။

## MCP တွင် Sampling လည်ပတ်ပုံ

MCP ၏ sampling flow သည် အောက်ပါအဆင့်များဖြင့် လိုက်နာသည် -

1. Server မှ client သို့ `sampling/createMessage` request ပို့သည်
2. Client သည် request ကို ပြန်လည်သုံးသပ်ပြီး ပြင်ဆင်နိုင်သည်
3. Client သည် LLM မှ sample ရယူသည်
4. Client သည် completion ကို ပြန်လည်သုံးသပ်သည်
5. Client သည် ရလဒ်ကို server သို့ ပြန်ပို့သည်

ဒီ human-in-the-loop ဒီဇိုင်းသည် အသုံးပြုသူများအား LLM ၏ input နှင့် output ကို ထိန်းချုပ်နိုင်စေသည်။

## Sampling Parameters အကျဉ်းချုပ်

MCP သည် client requests တွင် configure ပြုလုပ်နိုင်သည့် sampling parameters များကို အောက်ပါအတိုင်း သတ်မှတ်ထားသည် -

| Parameter | ဖော်ပြချက် | ပုံမှန် အကွာအဝေး |
|-----------|-------------|---------------|
| `temperature` | token ရွေးချယ်မှုတွင် randomness ကို ထိန်းချုပ်သည် | 0.0 - 1.0 |
| `maxTokens` | generate ပြုလုပ်မည့် token အများဆုံး အရေအတွက် | အနုတ်လက္ခဏာမပါသော အရေအတွက် |
| `stopSequences` | generate ရပ်တန့်စေမည့် စာကြောင်းများ | စာကြောင်းများ စုစည်းမှု |
| `metadata` | ပံ့ပိုးသူအလိုက် ထပ်ဆောင်း parameters များ | JSON object |

အများသော LLM ပံ့ပိုးသူများသည် `metadata` field မှတဆင့် ထပ်ဆောင်း parameters များကို ထောက်ပံ့သည်၊ ဥပမာ -

| Common Extension Parameter | ဖော်ပြချက် | ပုံမှန် အကွာအဝေး |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - token များကို top cumulative probability အတွင်း သတ်မှတ်သည် | 0.0 - 1.0 |
| `top_k` | token ရွေးချယ်မှုကို top K options အတွင်း သတ်မှတ်သည် | 1 - 100 |
| `presence_penalty` | စာသားတွင် ရှိနေမှုအပေါ် အပြစ်ပေးသည် | -2.0 - 2.0 |
| `frequency_penalty` | စာသားတွင် ထပ်ခါထပ်ခါ ဖြစ်ပေါ်မှုအပေါ် အပြစ်ပေးသည် | -2.0 - 2.0 |
| `seed` | ပြန်လည်ထုတ်ယူနိုင်သော ရလဒ်အတွက် သတ်မှတ် random seed | အနုတ်လက္ခဏာမပါသော အရေအတွက် |

## ဥပမာ Request ပုံစံ

MCP တွင် client မှ sampling request တင်သည့် ဥပမာ -

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

## Response ပုံစံ

Client မှ completion ရလဒ် ပြန်ပေးပုံ -

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

## Human in the Loop ထိန်းချုပ်မှုများ

MCP sampling သည် လူ့ကြီးကြပ်မှုဖြင့် ဒီဇိုင်းရေးဆွဲထားသည် -

- **Prompt များအတွက်**:
  - Client များသည် အသုံးပြုသူများအား အကြံပြု prompt ကို ပြသသင့်သည်
  - အသုံးပြုသူများသည် prompt များကို ပြင်ဆင် သို့မဟုတ် ငြင်းဆန်နိုင်ရမည်
  - System prompt များကို စစ်ထုတ် သို့မဟုတ် ပြင်ဆင်နိုင်သည်
  - Context ထည့်သွင်းမှုကို client က ထိန်းချုပ်သည်

- **Completion များအတွက်**:
  - Client များသည် အသုံးပြုသူများအား completion ကို ပြသသင့်သည်
  - အသုံးပြုသူများသည် completion များကို ပြင်ဆင် သို့မဟုတ် ငြင်းဆန်နိုင်ရမည်
  - Client များသည် completion များကို စစ်ထုတ် သို့မဟုတ် ပြင်ဆင်နိုင်သည်
  - အသုံးပြုသူများသည် မော်ဒယ်ရွေးချယ်မှုကို ထိန်းချုပ်သည်

ဒီအခြေခံသဘောတရားများနှင့်အတူ LLM ပံ့ပိုးသူများအကြား ပုံမှန်ထောက်ခံသော parameters များကို အခြေခံ၍ sampling ကို programming languages များတွင် ဘယ်လို အကောင်အထည်ဖော်မည်ကို ကြည့်ကြမည်။

## လုံခြုံရေးဆိုင်ရာ စဉ်းစားချက်များ

MCP တွင် sampling ကို အကောင်အထည်ဖော်ရာတွင် အောက်ပါ လုံခြုံရေးအကောင်းဆုံး လုပ်ထုံးလုပ်နည်းများကို စဉ်းစားပါ -

- **message အကြောင်းအရာအားလုံးကို client သို့ ပို့မီ စစ်ဆေးပါ**
- **prompt နှင့် completion များမှ sensitive အချက်အလက်များကို သန့်ရှင်းစေပါ**
- **အလွန်အသုံးပြုမှုကို ကာကွယ်ရန် rate limits ထည့်သွင်းပါ**
- **sampling အသုံးပြုမှုကို မမှန်ကန်သော ပုံစံများအတွက် စောင့်ကြည့်ပါ**
- **ဒေတာများကို လုံခြုံစွာ ပို့ဆောင်ရန် encryption ကို အသုံးပြုပါ**
- **အသုံးပြုသူ ဒေတာ privacy ကို သက်ဆိုင်ရာ စည်းမျဉ်းများအတိုင်း ကိုင်တွယ်ပါ**
- **sampling requests များကို compliance နှင့် security အတွက် audit လုပ်ပါ**
- **ကုန်ကျစရိတ် ထိန်းချုပ်မှုအတွက် သင့်တော်သော ကန့်သတ်ချက်များ ထားရှိပါ**
- **sampling requests များအတွက် timeout များ ထည့်သွင်းပါ**
- **မော်ဒယ် အမှားများကို သင့်တော်စွာ ကိုင်တွယ်ပြီး fallback များ ထည့်သွင်းပါ**

Sampling parameters များသည် language models ၏ အပြုအမူကို အတိအကျနှင့် ဖန်တီးမှုအကြား သင့်တော်သော ညှိနှိုင်းမှု ရရှိစေရန် အတိအကျ ပြင်ဆင်နိုင်စေသည်။

ဒီ parameters များကို programming languages များတွင် ဘယ်လို configure လုပ်မည်ကို ကြည့်ကြမည်။

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

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

အထက်ပါ ကုဒ်တွင် -

- သတ်မှတ်ထားသော server URL ဖြင့် MCP client တစ်ခု ဖန်တီးထားသည်။
- `temperature`, `top_p`, `top_k` ကဲ့သို့ sampling parameters များဖြင့် request ကို configure ပြုလုပ်ထားသည်။
- request ကို ပို့ပြီး generate ပြုလုပ်သော စာသားကို ပုံနှိပ်ပြထားသည်။
- `allowedTools` ကို အသုံးပြု၍ မော်ဒယ်သည် generate လုပ်စဉ်တွင် အသုံးပြုနိုင်သည့် tools များကို သတ်မှတ်ထားသည်။ ဤနေရာတွင် `ideaGenerator` နှင့် `marketAnalyzer` tools များကို ဖန်တီးမှုဆိုင်ရာ app ideas များအတွက် ခွင့်ပြုထားသည်။
- `frequencyPenalty` နှင့် `presencePenalty` ကို ထပ်ခါထပ်ခါဖြစ်မှုနှင့် မတူညီမှုကို ထိန်းချုပ်ရန် အသုံးပြုထားသည်။
- `temperature` ကို output ၏ randomness ကို ထိန်းချုပ်ရန် အသုံးပြုထားပြီး၊ တန်ဖိုးမြင့်သည့်အခါ ဖန်တီးမှုပိုများစေသည်။
- `top_p` ကို token ရွေးချယ်မှုကို top cumulative probability mass အတွင်း သတ်မှတ်ရန် အသုံးပြုထားသည်၊ စာသားအရည်အသွေး တိုးတက်စေသည်။
- `top_k` ကို မော်ဒယ်အား အလားအလာအမြင့်ဆုံး token K ခုအတွင်း သတ်မှတ်ရန် အသုံးပြုထားသည်၊ ပိုမိုတိကျသော response များ ရရှိစေသည်။
- `frequencyPenalty` နှင့် `presencePenalty` ကို ထပ်ခါထပ်ခါဖြစ်မှု လျော့နည်းစေပြီး မတူညီမှုကို မြှင့်တင်ရန် အသုံးပြုထားသည်။

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
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

အထက်ပါ ကုဒ်တွင် -

- Server URL နှင့် API key ဖြင့် MCP client တစ်ခု စတင်ဖန်တီးထားသည်။
- Creative task များနှင့် factual task များအတွက် sampling parameters နှစ်ခုကို configure ပြုလုပ်ထားသည်။
- ထို configurations များဖြင့် requests များ ပို့ပြီး မော်ဒယ်အား task အလိုက် သတ်မှတ်ထားသော tools များ အသုံးပြုခွင့်ပြုထားသည်။
- generate ပြုလုပ်သော responses များကို ပုံနှိပ်ပြထားပြီး sampling parameters မတူညီမှု၏ သက်ရောက်မှုကို ပြသထားသည်။
- `allowedTools` ကို အသုံးပြု၍ မော်ဒယ်သည် generate လုပ်စဉ်တွင် အသုံးပြုနိုင်သည့် tools များကို သတ်မှတ်ထားသည်။ ဤနေရာတွင် creative tasks အတွက် `ideaGenerator` နှင့် `environmentalImpactTool` များ၊ factual tasks အတွက် `factChecker` နှင့် `dataAnalysisTool` များကို ခွင့်ပြုထားသည်။
- `temperature` ကို output ၏ randomness ထိန်းချုပ်ရန် အသုံးပြုထားပြီး၊ တန်ဖိုးမြင့်သည့်အခါ ဖန်တီးမှုပိုများစေသည်။
- `top_p` ကို token ရွေးချယ်မှုကို top cumulative probability mass အတွင်း သတ်မှတ်ရန် အသုံးပြုထားသည်၊ စာသားအရည်အသွေး တိုးတက်စေသည်။
- `frequencyPenalty` နှင့် `presencePenalty` ကို ထပ်ခါထပ်ခါဖြစ်မှု လျော့နည်းစေပြီး မတူညီမှုကို မြှင့်တင်ရန် အသုံးပြုထားသည်။
- `top_k` ကို မော်ဒယ်အား အလားအလာအမြင့်ဆုံး token K ခုအတွင်း သတ်မှတ်ရန် အသုံးပြုထားသည်၊ ပိုမိုတိကျသော response များ ရရှိစေသည်။

---

## Deterministic Sampling

တူညီသော output များလိုအပ်သော applications များအတွက် deterministic sampling သည် ပြန်လည်ထုတ်ယူနိုင်သော ရလဒ်များကို သေချာစေသည်။ ၎င်းသည် fixed random seed ကို အသုံးပြုခြင်းနှင့် temperature ကို သုညထားခြင်းဖြင့် ဖြစ်ပေါ်သည်။

အောက်တွင် programming languages များတွင် deterministic sampling ကို ပြသသည့် ဥပမာကို ကြည့်ပါ။

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

အထက်ပါ ကုဒ်တွင် -

- သတ်မှတ်ထားသော server URL ဖြင့် MCP client တစ်ခု ဖန်တီးထားသည်။
- တူညီသော prompt နှင့် fixed seed, zero temperature ဖြင့် requests နှစ်ခု configure ပြုလုပ်ထားသည်။
- requests နှစ်ခုကို ပို့ပြီး generate ပြုလုပ်သော စာသားကို ပုံနှိပ်ပြထားသည်။
- sampling configuration ၏ deterministic သဘော (seed နှင့် temperature တူညီခြင်း) ကြောင့် responses များသည် တူညီကြောင်း ပြသထားသည်။
- `setSeed` ကို fixed random seed သတ်မှတ်ရန် အသုံးပြုထားသည်၊ ထို seed ဖြင့် မော်ဒယ်သည် တူညီသော input အတွက် တူညီသော output ကို generate ပြုလုပ်မည်ဖြစ်သည်။
- `temperature` ကို သုညထား၍ အများဆုံး deterministic ဖြစ်စေရန် သတ်မှတ်ထားသည်၊ မော်ဒယ်သည် randomness မပါဘဲ အလားအလာအမြင့်ဆုံး token ကိုသာ ရွေးချယ်မည်ဖြစ်သည်။

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
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

အထက်ပါ ကုဒ်တွင် -

- Server URL ဖြင့် MCP client တစ်ခု စတင်ဖန်တီးထားသည်။
- တူညီသော prompt နှင့် fixed seed, zero temperature ဖြင့် requests နှစ်ခု configure ပြုလုပ်ထားသည်။
- requests နှစ်ခုကို ပို့ပြီး generate ပြုလုပ်သော စာသားကို ပုံနှိပ်ပြထားသည်။
- sampling configuration ၏ deterministic သဘောကြောင့် responses များသည် တူညီကြောင်း ပြသထားသည်။
- `seed` ကို fixed random seed သတ်မှတ်ရန် အသုံးပြုထားသည်၊ ထို seed ဖြင့် မော်ဒယ်သည် တူညီသော input အတွက် တူညီသော output ကို generate ပြုလုပ်မည်ဖြစ်သည်။
- `temperature` ကို သုညထား၍ အများဆုံး deterministic ဖြစ်စေရန် သတ်မှတ်ထားသည်။
- တတိယ request အတွက် seed ကို မတူညီသော တန်ဖိုးဖြင့် သတ်မှတ်ထားပြီး၊ seed ပြောင်းလဲခြင်းကြောင့် တူညီသော prompt နှင့် temperature ဖြစ်သော်လည်း output မတူညီကြောင်း ပြသထားသည်။

---

## Dynamic Sampling Configuration

အသိပညာရှိ sampling သည် context နှင့် တောင်းဆိုမှုလိုအပ်ချက်များအပေါ် မူတည်၍ parameters များကို အလိုအလျောက် ပြောင်းလဲသည်။ ၎င်းသည် temperature, top_p, penalties ကဲ့သို့သော parameters များကို task အမျိုးအစား၊ user preferences သို့မဟုတ် အတိတ် performance အပေါ် မူတည်၍ dynamic ပြောင်းလဲခြင်းဖြစ်သည်။

အောက်တွင် programming languages များတွင် dynamic sampling ကို အကောင်အထည်ဖော်သည့် ဥပမာကို ကြည့်ပါ။

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

အထက်ပါ ကုဒ်တွင် -

- adaptive sampling ကို စီမံခန့်ခွဲသည့် `DynamicSamplingService` class ကို ဖန်တီးထားသည်။
- task အမျိုးအစားအလိုက် (creative, factual, code, analytical) sampling presets များ သတ်မှတ်ထားသည်။
- task အမျိုးအစားအပေါ် မူတည်၍ base sampling preset ကို ရွေးချယ်ထားသည်။
- user preferences (ဖန်တီးမှုနှင့် မတူညီမှု အဆင့်များ) အပေါ် မူတည်၍ sampling parameters များကို ပြင်ဆင်ထားသည်။
- dynamic sampling parameters ဖြင့် request ကို ပို့ထားသည်။
- generate ပြုလုပ်သော စာသားနှင့် sampling parameters, task အမျိုးအစားကို transparency အတွက် ပြန်လည်ပေးပို့ထားသည်။
- `temperature` ကို output ၏ randomness ထိန်းချုပ်ရန် အသုံးပြုထားသည်၊ တန်ဖိုးမြင့်သည့်အခါ ဖန်တီးမှုပိုများစေသည်။
- `top_p` ကို token ရွေးချယ်မှုကို top cumulative probability mass အတွင်း သတ်မှတ်ရန် အသုံးပြုထားသည်၊ စာသားအရည်အသွေး တိုးတက်စေသည်။
- `frequency_penalty` ကို ထပ်ခါထပ်ခါဖြစ်မှု လျော့နည်းစေပြီး မတူညီမှုကို မြှင့်တင်ရန် အသုံးပြုထားသည်။
- `user_preferences` ကို အသုံးပြုသူ သတ်မှတ်ထားသော ဖန်တီးမှုနှင့် မတူညီမှု အဆင့်များအပေါ် မူတည်၍ sampling parameters များကို စိတ်ကြိုက်ပြင်ဆင်နိုင်စေရန် အသုံးပြုထားသည်။
- `task_type` ကို request အတွက် သင့်တော်သော sampling strategy ကို သတ်မှတ်ရန် အသုံးပြုထားသည်။
- `send_request` method ဖြင့် configured sampling parameters များနှင့် prompt ကို ပို့ပြီး မော်ဒယ်သည် သတ်မှတ်ချက်အတိုင်း စာသား generate ပြုလုပ်စေသည်။
- `generated_text`

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
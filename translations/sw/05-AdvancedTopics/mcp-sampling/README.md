> [!WARNING]
> Kutoa sampuli kumeachwa katika MCP `2026-07-28`. Somo hili linahifadhiwa kwa ajili ya
> utekelezaji wa urithi. Seva mpya zinapaswa kuunganisha moja kwa moja na API ya
> mtoa huduma wa LLM.

# Kutoa Sampuli katika Itifaki ya Muktadha wa Mfano

> Kutoa sampuli bado kuna katika sifa ya `2026-07-28` kwa ajili ya ulinganifu na ni
> sifa ya kuondolewa katika marekebisho ya kwanza yatakayotolewa kufikia au baada ya Julai 28,
> 2027. Mifano katika somo hili inaweza kutumia API za SDK zinazotekeleza `2025-11-25`.
> Angalia [Nini Kimebadilika katika MCP: Sifa ya 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Katika utekelezaji wa urithi wa MCP, Kutoa Sampuli huruhusu seva kuomba ukamilishaji wa LLM
kupitia mteja. Somo hili linaelezea mtiririko wa itifaki uliovunjika wa zamani
kwa ajili ya ulinganifu na kazi ya uhamishaji.

## Utangulizi

Katika somo hili, tutaangazia jinsi ya kusanidi vigezo vya kutoa sampuli katika maombi ya MCP na kuelewa mbinu za msingi za itifaki ya kutoa sampuli.

## Malengo ya Kujifunza

Mwisho wa somo hili, utakuwa na uwezo wa:

- Kuelewa vigezo muhimu vya kutoa sampuli vinavyopatikana katika MCP.
- Kusanidi vigezo vya kutoa sampuli kwa matumizi mbalimbali.
- Kutekeleza kutoa sampuli kwa usahihi kwa matokeo yanayoweza kurudiwa.
- Kurekebisha vigezo vya kutoa sampuli kwa nguvu kulingana na muktadha na mapendeleo ya mtumiaji.
- Kutumia mikakati ya kutoa sampuli kuboresha utendaji wa mfano katika hali mbalimbali.
- Kuelewa jinsi kutoa sampuli kunavyofanya kazi katika mtiririko wa mteja-seva wa MCP.

## Jinsi Kutoa Sampuli Kwanza KCP Kunavyofanya Kazi

Mtiririko wa kutoa sampuli katika MCP unafuata hatua hizi:

1. Seva inatuma ombi la `sampling/createMessage` kwa mteja
2. Mteja anakagua ombi na anaweza kulibadilisha
3. Mteja huchukua sampuli kutoka kwa LLM
4. Mteja anakagua ukamilishaji
5. Mteja hurudisha matokeo kwa seva

Muundo huu wa mtu-kuingilia-mdogo huhakikisha watumiaji wanadhibiti kile ambacho LLM inaona na inazalisha.

## Muhtasari wa Vigezo vya Kutoa Sampuli

MCP inafafanua vigezo vifuatavyo vya kutoa sampuli ambavyo vinaweza kusanidiwa katika maombi ya mteja:

| Kigezo | Maelezo | Anuwai ya Kawaida |
|-----------|-------------|---------------|
| `temperature` | Hukontrol randomness katika uteuzi wa tokeni | 0.0 - 1.0 |
| `maxTokens` | Idadi kubwa ya tokeni kuzalisha | Thamani ya nambari nzima |
| `stopSequences` | Mfuatano maalum unaoacha uzalishaji ukiukikumbwa | Safu ya mstringi |
| `metadata` | Vigezo vya ziada maalum kwa mtoa huduma | Kifaa cha JSON |

Watoa huduma wengi wa LLM huunga mkono vigezo vya ziada kupitia uwanja wa `metadata`, ambao unaweza kujumuisha:

| Kigezo cha Kiongezaji Cha Kawaida | Maelezo | Anuwai ya Kawaida |
|-----------|-------------|---------------|
| `top_p` | Sampuli ya nyuklia - hukomo tokeni kwa uwezekano wa juu zaidi kwa pamoja | 0.0 - 1.0 |
| `top_k` | Hukomo chaguo za tokeni hadi K za juu | 1 - 100 |
| `presence_penalty` | Hukemea tokeni kulingana na uwepo wao katika maandishi hadi sasa | -2.0 - 2.0 |
| `frequency_penalty` | Hukemea tokeni kulingana na mara ngapi zimeonekana katika maandishi hadi sasa | -2.0 - 2.0 |
| `seed` | Mbegu maalum ya bahati nasibu kwa matokeo yanayoweza kurudiwa | Thamani ya nambari nzima |

## Mfano wa Muundo wa Ombi

Hapa ni mfano wa kuomba sampuli kutoka kwa mteja katika MCP:

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

## Muundo wa Jibu

Mteja hurudisha matokeo ya ukamilishaji:

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

## Udhibiti wa Mtu Katika Mzunguko

Sampuli ya MCP imeundwa kwa kufikiria usimamizi wa binadamu:

- **Kwa maagizo**:
  - Wateja wanapaswa kuonyesha watumiaji maombi yaliyopendekezwa
  - Watumiaji wanapaswa kuwa na uwezo wa kubadilisha au kukataa maagizo
  - Maagizo ya mfumo yanaweza kuchujwa au kubadilishwa
  - Ujumuishaji wa muktadha unadhibitiwa na mteja

- **Kwa ukamilishaji**:
  - Wateja wanapaswa kuonyesha watumiaji ukamilishaji
  - Watumiaji wanapaswa kuwa na uwezo wa kubadilisha au kukataa ukamilishaji
  - Wateja wanaweza kuchuja au kubadilisha ukamilishaji
  - Watumiaji wanadhibiti mfano gani unatumika

Pamoja na kanuni hizi akilini, tutaangalia jinsi ya kutekeleza kutoa sampuli katika lugha mbalimbali za programu, tukizingatia vigezo vinavyounga mkono kwa kawaida watoa huduma wa LLM.

## Mambo ya Usalama

Unapotekeleza kutoa sampuli katika MCP, zingatia taratibu hizi bora za usalama:

- **Thibitisha maudhui yote ya ujumbe** kabla ya kuyatuma kwa mteja
- **Safisha taarifa nyeti** kutoka kwa maagizo na ukamilishaji
- **Tekeleza mipaka ya kiwango** ili kuzuia matumizi mabaya
- **Simamia matumizi ya sampuli** kwa mifumo isiyo ya kawaida
- **Fichua data ikiwa inasafiri** kwa kutumia itifaki salama
- **Shughulikia faragha ya data ya mtumiaji** kulingana na kanuni husika
- **Fanya ukaguzi wa maombi ya sampuli** kwa ajili ya uzingatiaji na usalama
- **Dhibiti uwekaji wa gharama** kwa mipaka inayofaa
- **Tekeleza mipaka ya muda** kwa maombi ya sampuli
- **Shughulikia makosa ya mfano kwa hati safi** na mbadala unaofaa

Vigezo vya kutoa sampuli huruhusu kurekebisha kwa uangalifu mwenendo wa mifano ya lugha ili kufikia usawa unaotaka kati ya matokeo ya uhakika na ya ubunifu.

Tuchunguze jinsi ya kusanidi vigezo hivi katika lugha mbalimbali za programu.

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

Katika msimbo uliopita tumefanya:

- Kuunda mteja wa MCP na URL maalum ya seva.
- Kusanidi ombi lenye vigezo vya kutoa sampuli kama `temperature`, `top_p`, na `top_k`.
- Kutuma ombi na kuchapisha maandishi yaliyotengenezwa.
- Kutumia:
    - `allowedTools` kubainisha zana ambazo mfano unaweza kutumia wakati wa uzalishaji. Katika kesi hii, tuliwaruhusu zana `ideaGenerator` na `marketAnalyzer` kusaidia katika kuzalisha mawazo ya programu za ubunifu.
    - `frequencyPenalty` na `presencePenalty` kudhibiti kurudiwa na utofauti wa matokeo.
    - `temperature` kudhibiti randomness ya matokeo, ambapo thamani kubwa huleta majibu ya ubunifu zaidi.
    - `top_p` kupunguza uteuzi wa tokeni kwa zile zinazochangia uzito mkubwa wa uwezekano, kuboresha ubora wa maandishi yaliyotengenezwa.
    - `top_k` kuzuia mfano kufunguliwa kwa tokeni K zilizohesabiwa kuwa za juu zaidi, kusaidia kuzalisha majibu yaliyo na muktadha mzuri zaidi.
    - `frequencyPenalty` na `presencePenalty` kupunguza kurudiwa na kuhimiza utofauti wa maandishi yaliyotengenezwa.

# [JavaScript](#tab/javascript)

```javascript
// Mfano wa JavaScript: Hali ya joto na usanidi wa sampuli za Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Anzisha mteja wa MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Sanidi ombi kwa vigezo tofauti vya sampuli
  const creativeSampling = {
    temperature: 0.9,    // Joto kubwa zaidi = upotevu/bunifu zaidi
    topP: 0.92,          // Angalia tokeni zenye uzito wa uwezekano wa asilimia 92
    frequencyPenalty: 0.6, // Punguza kurudiwa kwa mfululizo wa tokeni
    presencePenalty: 0.4   // Adhabu tokeni zilizojitokeza katika maandishi hadi sasa
  };
  
  const factualSampling = {
    temperature: 0.2,    // Joto la chini = zaidi thabiti/kwenye ukweli
    topP: 0.85,          // Uchaguzi kidogo zaidi wa tokeni wenye umakini
    frequencyPenalty: 0.2, // Adhabu ndogo sana ya kurudiwa
    presencePenalty: 0.1   // Adhabu ndogo sana ya kuwepo
  };
  
  try {
    // Tuma maombi mawili yenye usanidi tofauti wa sampuli
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

Katika msimbo uliopita tumefanya:

- Kuanza mteja wa MCP na URL ya seva na funguo ya API.
- Kusanidi seti mbili za vigezo vya kutoa sampuli: moja kwa kazi za ubunifu na nyingine kwa kazi za ukweli.
- Kutuma maombi yenye usanidi huo, kuruhusu mfano kutumia zana maalum kwa kila kazi.
- Kuchapisha majibu yaliyotengenezwa kuonyesha athari za vigezo tofauti vya kutoa sampuli.
- Kutumia `allowedTools` kubainisha zana ambazo mfano unaweza kutumia wakati wa uzalishaji. Katika kesi hii, tuliwaruhusu `ideaGenerator` na `environmentalImpactTool` kwa kazi za ubunifu, na `factChecker` na `dataAnalysisTool` kwa kazi za ukweli.
- Kutumia `temperature` kudhibiti randomness ya matokeo, ambapo thamani kubwa huleta majibu ya ubunifu zaidi.
- Kutumia `top_p` kupunguza uteuzi wa tokeni kwa zile zinazochangia uzito mkubwa wa uwezekano, kuboresha ubora wa maandishi yaliyotengenezwa.
- Kutumia `frequencyPenalty` na `presencePenalty` kupunguza kurudiwa na kuhimiza utofauti wa matokeo.
- Kutumia `top_k` kuzuia mfano kufunguliwa kwa tokeni K zilizohesabiwa kuwa za juu zaidi, kusaidia kuzalisha majibu yaliyo na muktadha mzuri zaidi.

---

## Kutoa Sampuli kwa Usahihi

Kwa programu zinazohitaji matokeo thabiti, kutoa sampuli kwa usahihi huhakikisha matokeo yanayoweza kurudiwa. Hufanya hivyo kwa kutumia mbegu thabiti ya bahati nasibu na kuweka joto (temperature) hadi sifuri.

Tuchunguze utekelezaji wa sampuli sahihi katika lugha mbalimbali za programu hapa chini.

# [Java](#tab/java)

```java
// Mfano wa Java: Majibu ya uhakika kwa mbegu iliyowekwa
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Kutumia mbegu iliyowekwa kwa matokeo ya uhakika
        
        // Ombi la kwanza kwa mbegu iliyowekwa
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Joto sifuri kwa uhakika wa juu kabisa
            .build();
            
        // Ombi la pili kwa mbegu ile ile
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Tekeleza maombi yote mawili
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Majibu yanapaswa kuwa sawa kutokana na mbegu na joto=0 sawa
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Katika msimbo uliopita tumefanya:

- Kuunda mteja wa MCP na URL ya seva iliyotajwa.
- Kusanidi maombi mawili yenye prompt sawa, mbegu thabiti, na joto sifuri.
- Kutuma maombi yote na kuchapisha maandishi yaliyotengenezwa.
- Kuonyesha kuwa majibu ni sawa kutokana na asili ya usahihi katika usanidi wa sampuli (mbegu na joto sawa).
- Kutumia `setSeed` kubainisha mbegu thabiti ya bahati nasibu, kuhakikisha mfano unazalisha matokeo sawa kwa data sawa kila wakati.
- Kuweka `temperature` hadi sifuri kuhakikisha usahihi wa hali ya juu, ikimaanisha mfano kila mara atachagua tokeni inayoweza kutarajiwa zaidi bila randomness.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Mfano wa JavaScript: Majibu ya kuamua kwa udhibiti wa mbegu
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Ombi la kwanza lenye mbegu iliyowekwa
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Joto sifuri kwa udhaifu wa juu kabisa
    });
    
    // Ombi la pili lenye mbegu na joto sawa
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Ombi la tatu lenye mbegu tofauti lakini joto sawa
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

Katika msimbo uliopita tumefanya:

- Kuanza mteja wa MCP na URL ya seva.
- Kusanidi maombi mawili yenye prompt sawa, mbegu thabiti, na joto sifuri.
- Kutuma maombi yote na kuchapisha maandishi yaliyotengenezwa.
- Kuonyesha kuwa majibu ni sawa kutokana na asili ya usahihi katika usanidi wa sampuli (mbegu na joto sawa).
- Kutumia `seed` kubainisha mbegu thabiti ya bahati nasibu, kuhakikisha mfano unazalisha matokeo sawa kwa data sawa kila wakati.
- Kuweka `temperature` hadi sifuri kuhakikisha usahihi wa hali ya juu, ikimaanisha mfano kila mara atachagua tokeni inayoweza kutarajiwa zaidi bila randomness.
- Kutumia mbegu tofauti kwa ombi la tatu kuonyesha kuwa kubadilisha mbegu husababisha matokeo tofauti, hata kwa prompt na joto sawa.

---

## Usanidi wa Kutoa Sampuli kwa Msururu

Sampuli ya akili hubadilisha vigezo kulingana na muktadha na mahitaji ya kila ombi. Hii inamaanisha kurekebisha kwa nguvu vigezo kama joto (temperature), top_p, na vikwazo kulingana na aina ya kazi, mapendeleo ya mtumiaji, au utendaji wa kihistoria.

Tuchunguze jinsi ya kutekeleza kutoa sampuli kwa msururu katika lugha mbalimbali za programu.

# [Python](#tab/python)

```python
# Mfano wa Python: Sampuli ya mabadiliko kulingana na muktadha wa ombi
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Eleza presets za sampuli kwa aina mbalimbali za kazi
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Chagua preset msingi
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Rekebisha kulingana na mapendeleo ya mtumiaji ikiwa yatatolewa
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Pima joto kulingana na upendeleo wa ubunifu (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Rekebisha top_p kulingana na utofauti unaotakiwa wa majibu
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Unda na tuma ombi kwa vigezo maalum vya sampuli
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Rudisha jibu na metadata ya sampuli kwa uwazi
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Katika msimbo uliopita tumefanya:

- Kuunda darasa la `DynamicSamplingService` linalosimamia utoaji wa sampuli unaobadilika.
- Kufafanua mapreset ya kutoa sampuli kwa aina tofauti za kazi (ubunifu, ukweli, msimbo, uchambuzi).
- Kuchagua preset ya msingi ya sampuli kulingana na aina ya kazi.
- Kurekebisha vigezo vya sampuli kulingana na mapendeleo ya mtumiaji, kama viwango vya ubunifu na utofauti.
- Kutuma ombi lenye vigezo vya sampuli vilivyopangwa kwa njia ya msururu.
- Kurudisha maandishi yaliyotengenezwa pamoja na vigezo vya sampuli vilivyotumika na aina ya kazi kwa uwazi zaidi.
- Kutumia `temperature` kudhibiti randomness ya matokeo, ambapo thamani kubwa huleta majibu ya ubunifu zaidi.
- Kutumia `top_p` kupunguza uteuzi wa tokeni kwa zile zinazochangia uzito mkubwa wa uwezekano, kuboresha ubora wa maandishi yaliyotengenezwa.
- Kutumia `frequency_penalty` kupunguza kurudiwa na kuhimiza utofauti wa matokeo.
- Kutumia `user_preferences` kuruhusu kubinafsisha vigezo vya sampuli kulingana na viwango vya ubunifu na utofauti vilivyoainishwa na mtumiaji.
- Kutumia `task_type` kuamua mkakati wa sampuli unaofaa kwa ombi, kuruhusu majibu yaliyo na muktadha wa aina ya kazi.
- Kutumia njia ya `send_request` kutuma prompt na vigezo vya sampuli vilivyopangwa, kuhakikisha mfano unazalisha maandishi kulingana na mahitaji yaliyobainishwa.
- Kutumia `generated_text` kupata jibu la mfano, ambalo hurudishwa pamoja na vigezo vya sampuli na aina ya kazi kwa uchambuzi au maonyesho zaidi.
- Kutumia kazi za `min` na `max` kuhakikisha mapendeleo ya mtumiaji yamefikiriwa ndani ya anuwai halali, kuzuzuia usanidi batili wa sampuli.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Mfano wa JavaScript: Mipangilio ya sampuli inayobadilika kulingana na muktadha wa mtumiaji
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Eleza profaili za msingi za sampuli
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Fuata utendaji wa kihistoria
    this.performanceHistory = [];
  }
  
  // Tambua aina ya kazi kutoka kwenye tamko
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Ugunduzi rahisi wa kanuni - unaweza kuboreshwa kwa uainishaji wa ML
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
    
    // Chagua mazungumzo kwa default endapo hakuna aina wazi inayotambulika
    return 'conversational';
  }
  
  // Hesabu vigezo vya sampuli kulingana na muktadha na mapendeleo ya mtumiaji
  getSamplingParameters(prompt, context = {}) {
    // Tambua aina ya kazi
    const taskType = this.detectTaskType(prompt, context);
    
    // Pata profaili ya msingi
    let params = {...this.samplingProfiles[taskType]};
    
    // Rekebisha kulingana na mapendeleo ya mtumiaji
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Pima kutoka 1-10 hadi kiwango kinachofaa cha joto
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Usahihi mkubwa unamaanisha topP ndogo (uchaguzi ulio makini zaidi)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Uthabiti mkubwa unamaanisha adhabu ndogo
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Weka marekebisho yaliyojifunza kutoka historia ya utendaji
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Mantiki rahisi inayobadilika - inaweza kuboreshwa kwa algoriti za hali ya juu zaidi
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Chukulia tu historia ya karibuni
    
    if (relevantHistory.length > 0) {
      // Hesabu wastani wa alama za utendaji
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Ikiwa utendaji uko chini ya kikomo, rekebisha vigezo
      if (avgScore < 0.7) {
        // Marekebisho kidogo kuelekea thamani salama
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Rekodi utendaji kwa marekebisho ya baadaye
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Kiwango cha 0-1 cha ubora wa jibu
    });
    
    // Punguza ukubwa wa historia
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Pata vigezo vya sampuli vilivyo bora zaidi
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Tuma ombi kwa vigezo vilivyo bora zaidi
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Ikiwa mtumiaji anatoa maoni, yazingalie kwa uboreshaji wa baadaye
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

// Mifano ya matumizi
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kazi ya ubunifu na mapendeleo maalum ya mtumiaji
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Ubunifu mkubwa (1-10)
          consistency: 3  // Uthabiti mdogo (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Kazi ya kuzalisha msimbo
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Ubunifu mdogo
          precision: 8,   // Usahihi mkubwa
          consistency: 9  // Uthabiti mkubwa
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

Katika msimbo uliopita tumefanya:

- Kuunda darasa la `AdaptiveSamplingManager` linalosimamia sampuli ya msururu kulingana na aina ya kazi na mapendeleo ya mtumiaji.
- Kufafanua profaili za sampuli kwa aina tofauti za kazi (ubunifu, kweli, msimbo, mazungumzo).
- Kutekeleza njia ya kugundua aina ya kazi kutoka kwa prompt kwa kutumia heuristics rahisi.
- Kuhesabu vigezo vya sampuli kulingana na aina ya kazi iliyobaini na mapendeleo ya mtumiaji.
- Kutumia marekebisho yaliyopatikana kutoka kwa utendaji wa kihistoria kuboresha vigezo vya sampuli.
- Kurekodi utendaji kwa marekebisho ya baadaye, kuruhusu mfumo kujifunza kutokana na mwingiliano ya zamani.
- Kutuma maombi yenye vigezo vya sampuli vilivyopangwa na kurudisha maandishi yaliyotengenezwa pamoja na vigezo vilivyotumika na aina ya kazi iliyogunduliwa.
- Kutumia:
    - `userPreferences` kuruhusu kubinafsisha vigezo vya sampuli kulingana na viwango vya ubunifu, usahihi, na uthabiti vilivyoainishwa na mtumiaji.
    - `detectTaskType` kuamua asili ya kazi kulingana na prompt, kuruhusu majibu yaliyo na muktadha wa aina ya kazi.
    - `recordPerformance` kurekodi utendaji wa majibu yaliyotengenezwa, kuwezesha mfumo kubadilika na kuboresha kwa muda.
    - `applyLearnedAdjustments` kubadilisha vigezo vya sampuli kulingana na utendaji wa kihistoria, kuboresha uwezo wa mfano kuzalisha majibu bora.
    - `generateResponse` kuzingatia mchakato mzima wa kutoa jibu kwa sampuli ya msururu, kurahisisha kuita kazi kwa promoti na muktadha tofauti.
    - `allowedTools` kubainisha zana zinazoweza kutumika na mfano wakati wa uzalishaji, kuruhusu majibu yaliyo na uelewa mzito wa muktadha.
    - `feedbackScore` kuruhusu watumiaji kutoa maoni juu ya ubora wa jibu lililotengenezwa, ambalo linaweza kutumika kuboresha zaidi utendaji wa mfano kwa muda.
    - `performanceHistory` kuhifadhi rekodi ya mwingiliano ya zamani, kuwezesha mfumo kujifunza kutokana na mafanikio na kushindwa kwa awali.
    - `getSamplingParameters` kurekebisha vigezo vya sampuli kwa msururu kulingana na muktadha wa ombi, kuruhusu mwenendo wa mfano kuwa bendi na jibu zaidi.
    - `detectTaskType` kutambua kazi kulingana na prompt, kuwezesha mfumo kutumia mikakati inayofaa ya sampuli kwa aina tofauti za maombi.
    - `samplingProfiles` kufafanua usanidi wa msingi wa sampuli kwa aina tofauti za kazi, kuruhusu marekebisho ya haraka kulingana na asili ya ombi.

---

## Nini kinachofuata

- [5.7 Kupanua](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
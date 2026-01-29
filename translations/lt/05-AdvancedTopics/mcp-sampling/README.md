# Modelio konteksto protokolo pavyzdžių ėmimas

Pavyzdžių ėmimas yra galinga MCP funkcija, leidžianti serveriams per klientą prašyti LLM užbaigimų, taip suteikiant sudėtingą agentinį elgesį, išlaikant saugumą ir privatumą. Tinkama pavyzdžių ėmimo konfigūracija gali žymiai pagerinti atsakymų kokybę ir našumą. MCP suteikia standartizuotą būdą kontroliuoti, kaip modeliai generuoja tekstą, naudojant specifinius parametrus, kurie daro įtaką atsitiktinumui, kūrybiškumui ir nuoseklumui.

## Įvadas

Šioje pamokoje nagrinėsime, kaip konfigūruoti pavyzdžių ėmimo parametrus MCP užklausose ir suprasti pavyzdžių ėmimo protokolo mechaniką.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Suprasti pagrindinius pavyzdžių ėmimo parametrus MCP.
- Konfigūruoti pavyzdžių ėmimo parametrus skirtingiems naudojimo atvejams.
- Įgyvendinti deterministinį pavyzdžių ėmimą, kad gautumėte atkuriamus rezultatus.
- Dinamiškai koreguoti pavyzdžių ėmimo parametrus pagal kontekstą ir vartotojo pageidavimus.
- Taikyti pavyzdžių ėmimo strategijas, kad pagerintumėte modelio našumą įvairiose situacijose.
- Suprasti, kaip pavyzdžių ėmimas veikia MCP klientų-serverių sraute.

## Kaip veikia pavyzdžių ėmimas MCP

Pavyzdžių ėmimo srautas MCP vyksta šiais etapais:

1. Serveris siunčia `sampling/createMessage` užklausą klientui.
2. Klientas peržiūri užklausą ir gali ją modifikuoti.
3. Klientas atlieka pavyzdžių ėmimą iš LLM.
4. Klientas peržiūri užbaigimą.
5. Klientas grąžina rezultatą serveriui.

Šis žmogaus įsitraukimo dizainas užtikrina, kad vartotojai išlaiko kontrolę, ką LLM mato ir generuoja.

## Pavyzdžių ėmimo parametrų apžvalga

MCP apibrėžia šiuos pavyzdžių ėmimo parametrus, kuriuos galima konfigūruoti klientų užklausose:

| Parametras | Aprašymas | Tipinis diapazonas |
|------------|-----------|--------------------|
| `temperature` | Valdo atsitiktinumą pasirenkant žodžius | 0.0 - 1.0 |
| `maxTokens` | Maksimalus generuojamų žodžių skaičius | Sveikasis skaičius |
| `stopSequences` | Specialios sekos, kurios sustabdo generavimą, kai aptinkamos | Eilučių masyvas |
| `metadata` | Papildomi tiekėjo specifiniai parametrai | JSON objektas |

Daugelis LLM tiekėjų palaiko papildomus parametrus per `metadata` lauką, kurie gali apimti:

| Papildomas parametras | Aprašymas | Tipinis diapazonas |
|-----------------------|-----------|--------------------|
| `top_p` | Branduolio pavyzdžių ėmimas - apriboja žodžius iki viršutinės kumuliacinės tikimybės | 0.0 - 1.0 |
| `top_k` | Apriboja žodžių pasirinkimą iki viršutinių K variantų | 1 - 100 |
| `presence_penalty` | Baudžia žodžius pagal jų buvimą tekste iki šiol | -2.0 - 2.0 |
| `frequency_penalty` | Baudžia žodžius pagal jų dažnį tekste iki šiol | -2.0 - 2.0 |
| `seed` | Specifinis atsitiktinis sėklos skaičius atkuriamiems rezultatams | Sveikasis skaičius |

## Užklausos formato pavyzdys

Štai pavyzdys, kaip prašyti pavyzdžių ėmimo iš kliento MCP:

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

## Atsakymo formatas

Klientas grąžina užbaigimo rezultatą:

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

## Žmogaus įsitraukimo kontrolė

MCP pavyzdžių ėmimas sukurtas su žmogaus priežiūra:

- **Dėl užklausų**:
  - Klientai turėtų parodyti vartotojams siūlomą užklausą.
  - Vartotojai turėtų galėti modifikuoti arba atmesti užklausas.
  - Sistemos užklausos gali būti filtruojamos arba modifikuojamos.
  - Konteksto įtraukimas kontroliuojamas klientu.

- **Dėl užbaigimų**:
  - Klientai turėtų parodyti vartotojams užbaigimą.
  - Vartotojai turėtų galėti modifikuoti arba atmesti užbaigimus.
  - Klientai gali filtruoti arba modifikuoti užbaigimus.
  - Vartotojai kontroliuoja, kuris modelis naudojamas.

Turint šiuos principus omenyje, pažvelkime, kaip įgyvendinti pavyzdžių ėmimą skirtingomis programavimo kalbomis, sutelkiant dėmesį į parametrus, kurie dažniausiai palaikomi LLM tiekėjų.

## Saugumo aspektai

Įgyvendinant pavyzdžių ėmimą MCP, atsižvelkite į šias saugumo geriausias praktikas:

- **Patikrinkite visą pranešimų turinį** prieš siunčiant jį klientui.
- **Išvalykite jautrią informaciją** iš užklausų ir užbaigimų.
- **Įgyvendinkite užklausų limitus**, kad išvengtumėte piktnaudžiavimo.
- **Stebėkite pavyzdžių ėmimo naudojimą** dėl neįprastų modelių.
- **Šifruokite duomenis perdavimo metu** naudodami saugius protokolus.
- **Tvarkykite vartotojų duomenų privatumą** pagal atitinkamus reglamentus.
- **Audituokite pavyzdžių ėmimo užklausas** dėl atitikties ir saugumo.
- **Kontroliuokite išlaidų riziką** su tinkamais limitais.
- **Įgyvendinkite užklausų laiko limitus**.
- **Tvarkykite modelio klaidas tinkamai** su atitinkamais atsarginiais sprendimais.

Pavyzdžių ėmimo parametrai leidžia tiksliai sureguliuoti kalbos modelių elgesį, kad būtų pasiektas norimas balansas tarp deterministinių ir kūrybinių rezultatų.

Pažvelkime, kaip konfigūruoti šiuos parametrus skirtingomis programavimo kalbomis.

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

Ankstesniame kode mes:

- Sukūrėme MCP klientą su specifiniu serverio URL.
- Konfigūravome užklausą su pavyzdžių ėmimo parametrais, tokiais kaip `temperature`, `top_p` ir `top_k`.
- Išsiuntėme užklausą ir atspausdinome sugeneruotą tekstą.
- Naudojome:
    - `allowedTools`, kad nurodytume, kokius įrankius modelis gali naudoti generavimo metu. Šiuo atveju leidome naudoti `ideaGenerator` ir `marketAnalyzer` įrankius, kad padėtų generuoti kūrybines programų idėjas.
    - `frequencyPenalty` ir `presencePenalty`, kad kontroliuotume pasikartojimą ir įvairovę išvestyje.
    - `temperature`, kad kontroliuotume atsitiktinumą išvestyje, kur didesnės vertės lemia kūrybiškesnius atsakymus.
    - `top_p`, kad apribotume žodžių pasirinkimą iki tų, kurie prisideda prie viršutinės kumuliacinės tikimybės masės, taip pagerindami sugeneruoto teksto kokybę.
    - `top_k`, kad apribotume modelį iki viršutinių K labiausiai tikėtinų žodžių, kas gali padėti generuoti nuoseklesnius atsakymus.
    - `frequencyPenalty` ir `presencePenalty`, kad sumažintume pasikartojimą ir paskatintume įvairovę sugeneruotame tekste.

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

Ankstesniame kode mes:

- Inicializavome MCP klientą su serverio URL ir API raktu.
- Konfigūravome du pavyzdžių ėmimo parametrų rinkinius: vieną kūrybinėms užduotims, kitą faktinėms užduotims.
- Išsiuntėme užklausas su šiomis konfigūracijomis, leisdami modeliui naudoti specifinius įrankius kiekvienai užduočiai.
- Atspausdinome sugeneruotus atsakymus, kad pademonstruotume skirtingų pavyzdžių ėmimo parametrų poveikį.
- Naudojome `allowedTools`, kad nurodytume, kokius įrankius modelis gali naudoti generavimo metu. Šiuo atveju leidome naudoti `ideaGenerator` ir `environmentalImpactTool` kūrybinėms užduotims, o `factChecker` ir `dataAnalysisTool` faktinėms užduotims.
- Naudojome `temperature`, kad kontroliuotume atsitiktinumą išvestyje, kur didesnės vertės lemia kūrybiškesnius atsakymus.
- Naudojome `top_p`, kad apribotume žodžių pasirinkimą iki tų, kurie prisideda prie viršutinės kumuliacinės tikimybės masės, taip pagerindami sugeneruoto teksto kokybę.
- Naudojome `frequencyPenalty` ir `presencePenalty`, kad sumažintume pasikartojimą ir paskatintume įvairovę išvestyje.
- Naudojome `top_k`, kad apribotume modelį iki viršutinių K labiausiai tikėtinų žodžių, kas gali padėti generuoti nuoseklesnius atsakymus.

---

## Deterministinis pavyzdžių ėmimas

Programoms, kurioms reikalingi nuoseklūs rezultatai, deterministinis pavyzdžių ėmimas užtikrina atkuriamus rezultatus. Tai pasiekiama naudojant fiksuotą atsitiktinę sėklą ir nustatant temperatūrą į nulį.

Pažvelkime į žemiau pateiktą pavyzdį, kaip įgyvendinti deterministinį pavyzdžių ėmimą skirtingomis programavimo kalbomis.

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

Ankstesniame kode mes:

- Sukūrėme MCP klientą su nurodytu serverio URL.
- Konfigūravome dvi užklausas su tuo pačiu užklausos tekstu, fiksuota sėkla ir nuline temperatūra.
- Išsiuntėme abi užklausas ir atspausdinome sugeneruotą tekstą.
- Pademonstravome, kad atsakymai yra identiški dėl deterministinio pavyzdžių ėmimo konfigūracijos (ta pati sėkla ir temperatūra).
- Naudojome `setSeed`, kad nurodytume fiksuotą atsitiktinę sėklą, užtikrinant, kad modelis generuotų tą patį rezultatą už tą pačią įvestį kiekvieną kartą.
- Nustatėme `temperature` į nulį, kad užtikrintume maksimalų determinizmą, reiškiantį, kad modelis visada pasirinks labiausiai tikėtiną kitą žodį be atsitiktinumo.

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

Ankstesniame kode mes:

- Inicializavome MCP klientą su serverio URL.
- Konfigūravome dvi užklausas su tuo pačiu užklausos tekstu, fiksuota sėkla ir nuline temperatūra.
- Išsiuntėme abi užklausas ir atspausdinome sugeneruotą tekstą.
- Pademonstravome, kad atsakymai yra identiški dėl deterministinio pavyzdžių ėmimo konfigūracijos (ta pati sėkla ir temperatūra).
- Naudojome `seed`, kad nurodytume fiksuotą atsitiktinę sėklą, užtikrinant, kad modelis generuotų tą patį rezultatą už tą pačią įvestį kiekvieną kartą.
- Nustatėme `temperature` į nulį, kad užtikrintume maksimalų determinizmą, reiškiantį, kad modelis visada pasirinks labiausiai tikėtiną kitą žodį be atsitiktinumo.
- Naudojome kitą sėklą trečiai užklausai, kad parodytume, jog keičiant sėklą gaunami skirtingi rezultatai, net ir su ta pačia užklausa ir temperatūra.

---

## Dinaminė pavyzdžių ėmimo konfigūracija

Protingas pavyzdžių ėmimas pritaiko parametrus pagal kiekvienos užklausos kontekstą ir reikalavimus. Tai reiškia dinamišką parametrų, tokių kaip temperatūra, top_p ir baudos, koregavimą pagal užduoties tipą, vartotojo pageidavimus ar istorinius rezultatus.

Pažvelkime, kaip įgyvendinti dinaminį pavyzdžių ėmimą skirtingomis programavimo kalbomis.

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

Ankstesniame kode mes:

- Sukūrėme `DynamicSamplingService` klasę, kuri valdo adaptacinį pavyzdžių ėmimą.
- Apibrėžėme pavyzdžių ėmimo išankstinius nustatymus skirtingiems užduočių tipams (kūrybinėms, faktinėms, kodavimo, analitinėms).
- Pasirinkome bazinį pavyzdžių ėmimo išankstinį nustatymą pagal užduoties tipą.
- Koregavome pavyzdžių ėmimo parametrus pagal vartotojo pageidavimus, tokius kaip kūrybiškumo lygis ir įvairovė.
- Išsiuntėme užklausą su dinamiškai konfigūruotais pavyzdžių ėmimo parametrais.
- Grąžinome sugeneruotą tekstą kartu su taikytais pavyzdžių ėmimo parametrais ir užduoties tipu, siekiant skaidrumo.
- Naudojome `temperature`, kad kontroliuotume atsitiktinumą išvestyje, kur didesnės vertės lemia kūrybiškesnius atsakymus.
- Naudojome `top_p`, kad apribotume žodžių pasirinkimą iki tų, kurie prisideda prie viršutinės kumuliacinės tikimybės masės, taip pagerindami sugeneruoto teksto kokybę.
- Naudojome `frequency_penalty`, kad sumažintume pasikartojimą ir paskatintume įvairovę išvestyje.
- Naudojome `user_preferences`, kad leistume vartotojams pritaikyti pavyzdžių ėmimo parametrus pagal jų apibrėžtą kūrybiškumo ir įvairovės lygį.
- Naudojome `task_type`, kad nustatytume tinkamą pavyzdžių ėmimo strategiją užklausai, leidžiant labiau pritaikytus atsakymus pagal užduoties pobūdį.
- Naudojome `send_request` metodą, kad išsiųstume užklausą su konfigūruotais pavyzdžių ėmimo parametrais, užtikrinant, kad modelis generuotų tekstą pagal nurodytus reikalavimus.
- Naudojome `generated_text`, kad gautume modelio atsakymą, kuris vėliau grąžinamas kartu su pavyzdžių ėmimo parametrais ir užduoties tipu tolesnei analizei ar rodymui.
- Naudojome `min` ir `max` funkcijas, kad užtikrintume, jog vartotojo pageidavimai būtų ribojami galiojančiuose diapazonuose, užkertant kelią neteisingoms pavyzdžių ėmimo konfigūracijoms.

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
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
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
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

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
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

Ankstesniame kode mes:

- Sukūrėme `AdaptiveSamplingManager` klasę, kuri valdo dinaminį pavyzdžių ėmimą pagal užduoties tipą ir vartotojo pageidavimus.
- Apibrėžėme pavyzdžių ėmimo profilius skirtingiems užduočių tipams (kūrybinėms, faktinėms, kodavimo,

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
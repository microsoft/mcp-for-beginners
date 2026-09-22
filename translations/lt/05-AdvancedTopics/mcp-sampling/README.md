> [!WARNING]
> Imties ėmimas MCP `2026-07-28` versijoje yra nebenaudojamas. Šis pamokos turinys išlaikytas skirtas
> paveldėtosioms įgyvendinimo versijoms. Nauji serveriai turėtų tiesiogiai integruotis su LLM
> tiekėjo API.

# Imties ėmimas Modelio Konteksto Protokole

> Imties ėmimas išlieka `2026-07-28` specifikacijoje siekiant suderinamumo ir gali būti pašalintas pirmojoje peržiūroje,
> išleistos ne anksčiau kaip 2027 m. liepos 28 d. Šios pamokos pavyzdžiai gali naudoti SDK API, įgyvendinančius `2025-11-25`.
> Žr. [Kas pasikeitė MCP: 2026-07-28 specifikacija](../../01-CoreConcepts/mcp-2026-07-28.md).


rezultatų per klientą. Ši pamoka paaiškina šį nebenaudojamą protokolo
srautą suderinamumo ir migracijos darbams.




protokolo mechanizmus.

## Mokymosi tikslai

Pasibaigus šiai pamokai, jūs galėsite:

- Suprasti pagrindinius MCP prieinamus imties ėmimo parametrus.
- Konfigūruoti imties ėmimo parametrus skirtingiems naudojimo atvejams.
- Įgyvendinti determinuotą imties ėmimą siekiant pakartotinumo.
- Dinamiškai reguliuoti imties ėmimo parametrus pagal kontekstą ir vartotojo nuostatas.
- Taikyti imties ėmimo strategijas modelio našumo gerinimui įvairiose scenarijose.
- Suprasti, kaip imties ėmimas veikia kliento-serverio MCP sraute.

## Kaip imties ėmimas veikia MCP

Imties ėmimo srautas MCP vyksta taip:

1. Serveris siunčia `sampling/createMessage` užklausą klientui
2. Klientas peržiūri užklausą ir gali ją keisti
3. Klientas imasi imties iš LLM
4. Klientas peržiūri rezultatą
5. Klientas grąžina rezultatą serveriui

Šis žmogaus įtrauktas dizainas užtikrina, kad vartotojai išlaiko kontrolę, ką LLM mato ir generuoja.

## Imties ėmimo parametrų apžvalga

MCP apibrėžia šiuos imties ėmimo parametrus, kuriuos galima konfigūruoti kliento užklausose:

| Parametras | Aprašymas | Tipinis diapazonas |
|-----------|-------------|---------------|
| `temperature` | Valdo atsitiktinumą pasirenkant žodžius | 0.0 - 1.0 |
| `maxTokens` | Maksimalus sugeneruotų žodžių kiekis | Sveikasis skaičius |
| `stopSequences` | Pasirinktinių sekų, kurios stabdo generavimą, masyvas | Eilutės masyvas |
| `metadata` | Papildomi parametrai, priklausantys tiekėjui | JSON objektas |

Daugelis LLM tiekėjų palaiko papildomus parametrus per `metadata` lauką, kurie gali apimti:

| Dažnas išplėtimo parametras | Aprašymas | Tipinis diapazonas |
|-----------|-------------|---------------|
| `top_p` | Nucleus imties ėmimas – riboja žodžius pagal viršutinę kumuliatyvią tikimybę | 0.0 - 1.0 |
| `top_k` | Riboja žodžių pasirinkimą iki top K variantų | 1 - 100 |
| `presence_penalty` | Skaudina žodžius pagal jų pasirodymą tekste | -2.0 - 2.0 |
| `frequency_penalty` | Skaudina žodžius pagal jų dažnumą tekste | -2.0 - 2.0 |
| `seed` | Konkretus atsitiktinis sėklos skaičius pakartojamiems rezultatams | Sveikasis skaičius |

## Užklausos formatas pavyzdyje

Štai pavyzdys, kaip prašyti imties iš kliento MCP:

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

Klientas grąžina užbaigtą rezultatą:

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

## Žmogaus įtraukimo valdymas

MCP imties ėmimas yra sukurtas su žmogiškuoju priežiūros požiūriu:

- **Dėl užklausų**:
  - Klientai turėtų parodyti vartotojams siūlomą užklausą
  - Vartotojai turėtų galėti keisti arba atmesti užklausas
  - Sisteminės užklausos gali būti filtruojamos arba keičamos
  - Konteksto įtraukimas valdomas kliento

- **Dėl rezultatų**:
  - Klientai turėtų parodyti vartotojams gautą rezultatą
  - Vartotojai turėtų galėti modifikuoti arba atmesti rezultatus
  - Klientai gali filtruoti arba keisti rezultatus
  - Vartotojai kontroliuoja, kuris modelis naudojamas

Laikydamiesi šių principų pažvelkime, kaip įgyvendinti imties ėmimą įvairiomis programavimo kalbomis, sutelkiant dėmesį į parametrus, kuriuos įprastai palaiko LLM tiekėjai.

## Saugumo svarstymai

Įgyvendinant MCP imties ėmimą, apsvarstykite šias saugumo gerąsias praktikas:

- **Patikrinkite visą pranešimo turinį** prieš siųsdami jį klientui
- **Saugokite jautrią informaciją** užklausose ir rezultatuose
- **Įgyvendinkite užklausų dažnio ribas** siekiant išvengti piktnaudžiavimo
- **Stebėkite imties panaudojimą** netipiniams atvejams identifikuoti
- **Šifruokite duomenis perdavimo metu** naudodami saugius protokolus
- **Rūpinkitės vartotojų duomenų privatumu** pagal aktualius reglamentus
- **Atlikite imties užklausų auditą** siekiant užtikrinti atitiktį ir saugumą
- **Valdykite kaštų riziką** nustatant tinkamas ribas
- **Įgyvendinkite užklausų laikmačius** imčiai gauti
- **Tvarkykite modelio klaidas** tinkamai suteikiant atsargines galimybes

Imties ėmimo parametrai leidžia tiksliai reguliuoti kalbos modelių elgesį, siekiant norimo balanso tarp determinuoto ir kūrybiško rezultato.

Pažiūrėkime, kaip konfigūruoti šiuos parametrus skirtingose programavimo kalbose.

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

Ankstesniame kode mes:

- Sukūrėme MCP klientą su konkrečiu serverio URL.
- Suplanavome užklausą su imties ėmimo parametrais, tokiais kaip `temperature`, `top_p` ir `top_k`.
- Išsiuntėme užklausą ir atspausdinome sugeneruotą tekstą.
- Naudojome:
    - `allowedTools` nurodyti, kokios priemonės modelis gali naudoti generavimui. Šiuo atveju leidome `ideaGenerator` ir `marketAnalyzer`, kad padėtų generuoti kūrybiškas aplikacijų idėjas.
    - `frequencyPenalty` ir `presencePenalty` valdyti pasikartojimus ir įvairovę išvestyje.
    - `temperature` kontroliuoti atsitiktinumą išvestyje, kai didesnės reikšmės lemia kūrybiškesnius atsakymus.
    - `top_p` apriboti žodžių pasirinkimą tik tiems, kurie sudaro viršutinę kumuliatyvią tikimybę, gerinant sugeneruoto teksto kokybę.
    - `top_k` apriboti modelį pasirinkti tik iš top K tikėtiniausių žodžių, kas padeda kurti nuoseklesnius atsakymus.
    - `frequencyPenalty` ir `presencePenalty` sumažinti pasikartojimus ir skatinti įvairovę generuotame tekste.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript pavyzdys: temperatūros ir Top-P mėginių ėmimo konfigūracija
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializuokite MCP klientą
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigūruokite užklausą su skirtingais mėginių ėmimo parametrais
  const creativeSampling = {
    temperature: 0.9,    // Aukštesnė temperatūra = daugiau atsitiktinumo/kūrybiškumo
    topP: 0.92,          // Apsvarstykite žodžius su viršutiniu 92% tikimybės masės
    frequencyPenalty: 0.6, // Sumažinkite žodžių sekų pasikartojimą
    presencePenalty: 0.4   // Bauduokite žodžius, kurie jau pasirodė tekste
  };
  
  const factualSampling = {
    temperature: 0.2,    // Žemesnė temperatūra = daugiau deterministinis/faktiškas
    topP: 0.85,          // Šiek tiek labiau susikoncentravęs žodžių pasirinkimas
    frequencyPenalty: 0.2, // Minimalus pasikartojimo baudos dydis
    presencePenalty: 0.1   // Minimalus buvimo baudos dydis
  };
  
  try {
    // Pateikite dvi užklausas su skirtingomis mėginių ėmimo konfigūracijomis
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

- Inicijavome MCP klientą su serverio URL ir API raktu.
- Suplanavome du imties ėmimo parametrų rinkinius: vieną kūrybiniams, kitą faktiniams darbams.
- Išsiuntėme užklausas su šiomis konfigūracijomis, leidžiant modeliui naudoti specifines priemones kiekvienam užduoties tipui.
- Atspausdinome sugeneruotus atsakymus, kad parodytume skirtingų imties ėmimo parametrų poveikį.
- Naudojome `allowedTools`, kad nurodytume, kokios priemonės modelis gali naudoti generavimui. Šiuo atveju kūrybiniams darbams leidome `ideaGenerator` ir `environmentalImpactTool`, o faktiniams darbams – `factChecker` ir `dataAnalysisTool`.
- Naudojome `temperature` kontroliuoti atsitiktinumą išvestyje, kai didesnės reikšmės lemia kūrybiškesnius atsakymus.
- Naudojome `top_p` apriboti žodžių pasirinkimą tiems, kurie sudaro viršutinę kumuliatyvią tikimybę, gerinant teksto kokybę.
- Naudojome `frequencyPenalty` ir `presencePenalty` sumažinti pasikartojimus ir skatinti įvairovę išvestyje.
- Naudojome `top_k` apriboti modelį iki top K tikėtiniausių žodžių, kas padeda generuoti nuoseklesnius atsakymus.

---

## Determinuotas imties ėmimas

Programėlėms, kurioms reikia nuoseklių rezultatų, determinuotas imties ėmimas užtikrina pakartojamus rezultatus. Tai veikia naudojant fiksuotą atsitiktinę sėklą ir nustatant temperatūrą nuliui.

Pažiūrėkime toliau pateiktą pavyzdinę realizaciją demonstravimui determinuotam imties ėmimui skirtingose programavimo kalbose.

# [Java](#tab/java)

```java
// Java pavyzdys: deterministiniai atsakymai su fiksuotu sėklu
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Naudojant fiksuotą sėklą deterministinėms rezultatams
        
        // Pirmas užklausimas su fiksuota sėkla
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nulinė temperatūra maksimaliam deterministiškumui
            .build();
            
        // Antras užklausimas su ta pačia sėkla
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Vykdyti abu užklausimus
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Atsakymai turėtų būti identiški dėl tos pačios sėklos ir temperatūros=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Ankstesniame kode mes:

- Sukūrėme MCP klientą su nurodytu serverio URL.
- Sukonfigūravome dvi užklausas su ta pačia užklausa, fiksuota sėkla ir nulinė temperatūra.
- Išsiuntėme abi užklausas ir atspausdinome sugeneruotą tekstą.
- Pademonstravome, kad atsakymai yra identiški dėl determinuoto imties ėmimo konfigūracijos (ta pati sėkla ir temperatūra).
- Naudojome `setSeed` nurodyti fiksuotą atsitiktinę sėklą, užtikrinant, kad modelis kiekvieną kartą gaus tą patį rezultatą to paties įvesties atveju.
- Nustatėme `temperature` į nulį, kad užtikrintume maksimalų determinizmą — modelis visada pasirinks tikimybę turintį artimiausią kitą žodį be atsitiktinumo.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript pavyzdys: deterministiniai atsakymai su sėklos valdymu
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Pirmasis užklausimas su fiksuota sėkla
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nulinė temperatūra maksimaliam determinizmui
    });
    
    // Antrasis užklausimas su ta pačia sėkla ir temperatūra
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Trečiasis užklausimas su skirtinga sėkla, bet ta pačia temperatūra
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

- Inicijavome MCP klientą su serverio URL.
- Suplanavome dvi užklausas su ta pačia užklausa, fiksuota sėkla ir nulinė temperatūra.
- Išsiuntėme abi užklausas ir atspausdinome sugeneruotą tekstą.
- Pademonstravome, kad atsakymai yra identiški dėl determinuoto imties ėmimo konfigūracijos (ta pati sėkla ir temperatūra).
- Naudojome `seed` nurodyti fiksuotą atsitiktinę sėklą, užtikrinant, kad modelis kiekvieną kartą sugeneruos tą patį rezultatą to paties įvesties atveju.
- Nustatėme `temperature` į nulį, užtikrindami maksimalų determinizmą.
- Trečiajai užklausai panaudojome kitokią sėklą, kad parodytume, jog sėklos keitimas lemia skirtingus rezultatus, nors užklausa ir temperatūra lieka tos pačios.

---

## Dinaminė imties ėmimo konfigūracija

Išmani imtis prisitaiko prie konteksto ir užklausų reikalavimų, dinamiškai keisdama parametrus, tokius kaip temperatūra, top_p ir baudos, priklausomai nuo užduoties tipo, vartotojo nuostatų ar istorinės našumo analizės.

Pažiūrėkime, kaip įgyvendinti dinaminę imtį skirtingomis programavimo kalbomis.

# [Python](#tab/python)

```python
# Python pavyzdys: dinaminių atrankų pagrindu remiantis užklausos kontekstu
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Apibrėžkite atrankų iš anksto nustatytas reikšmes skirtingiems užduočių tipams
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Pasirinkite pagrindinę iš anksto nustatytą reikšmę
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Pakoreguokite pagal vartotojo pageidavimus, jei jie pateikti
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Koreguokite temperatūrą atsižvelgiant į kūrybiškumo pageidavimus (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Pakoreguokite top_p pagal pageidaujamą atsakymų įvairovę
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Sukurkite ir išsiųskite užklausą su pasirinktiniais atrankų parametrais
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Grąžinkite atsakymą su atrankų metaduomenimis skaidrumui užtikrinti
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Ankstesniame kode mes:

- Sukūrėme `DynamicSamplingService` klasę, kuri valdo adaptacinį imties ėmimą.
- Apibrėžėme imties nustatymus skirtingiems užduočių tipams (kūrybinės, faktinės, kodo, analitinės).
- Pasirinkome bazinį imties rinkinį pagal užduoties tipą.
- Koregavome imties parametrus pagal vartotojo nuostatas, pavyzdžiui, kūrybiškumo ir įvairovės lygius.
- Išsiuntėme užklausą su dinamiškai sukonfigūruotais imties parametrais.
- Grąžinome sugeneruotą tekstą kartu su pritaikytais imties parametrais ir užduoties tipu skaidrumui užtikrinti.
- Naudojome `temperature` kontroliuoti atsitiktinumą išvestyje, kai didesnės reikšmės lemia kūrybiškesnius atsakymus.
- Naudojome `top_p` apriboti žodžių pasirinkimą tiems, kurie sudaro viršutinę kumuliatyvią tikimybę, gerinant teksto kokybę.
- Naudojome `frequency_penalty` sumažinti pasikartojimus ir skatinti įvairovę išvestyje.
- Naudojome `user_preferences`, kad leistume pritaikyti imties parametrus pagal vartotojo nurodytus kūrybiškumo ir įvairovės lygius.
- Naudojome `task_type` nustatyti tinkamą imties strategiją užklausai, leidžiant labiau pritaikytus atsakymus pagal užduoties pobūdį.
- Naudojome `send_request` metodą siųsti užklausą su sukonfigūruotais imties parametrais, garantuojant, kad modelis sugeneruotų tekstą pagal nurodytus reikalavimus.
- Naudojome `generated_text` gauti modelio atsakymui, kuris vėliau grąžinamas kartu su imties parametrais ir užduoties tipu tolesnei analizei arba pristatymui.
- Naudojome `min` ir `max` funkcijas, kad užtikrintume, jog vartotojo nuostatos būtų ribojamos galiojančiuose diapazonuose, neleidžiant neteisingoms imties konfigūracijoms.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript pavyzdys: dinaminė atrankos konfigūracija pagal naudotojo kontekstą
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Apibrėžti pagrindinius atrankos profilius
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Stebėti istorinius rezultatus
    this.performanceHistory = [];
  }
  
  // Aptikti užduoties tipą iš užklausos
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Paprasta heuristinė aptikimo sistema – gali būti patobulinta naudojant ML klasifikaciją
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
    
    // Pagal nutylėjimą laikyti pokalbiu, jei aiškus tipas neaptiktas
    return 'conversational';
  }
  
  // Apskaičiuoti atrankos parametrus pagal kontekstą ir naudotojo pageidavimus
  getSamplingParameters(prompt, context = {}) {
    // Aptikti užduoties tipą
    const taskType = this.detectTaskType(prompt, context);
    
    // Gauti pagrindinį profilį
    let params = {...this.samplingProfiles[taskType]};
    
    // Koreguoti pagal naudotojo pageidavimus
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Pakeisti skalę nuo 1 iki 10 į tinkamą temperatūros diapazoną
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Didesnis tikslumas reiškia mažesnį topP (daugiau fokusuota atranka)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Didesnis nuoseklumas reiškia mažesnius baudimus
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Taikyti išmoktas korekcijas iš našumo istorijos
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Paprasta adaptacinė logika – gali būti patobulinta naudojant sudėtingesnius algoritmus
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Apsvarstyti tik neseną istoriją
    
    if (relevantHistory.length > 0) {
      // Apskaičiuoti vidutinius našumo balus
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Jei našumas žemesnis už ribą, koreguoti parametrus
      if (avgScore < 0.7) {
        // Švelni korekcija link saugesnių reikšmių
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Fiksuoti našumą būsimoms korekcijoms
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 atsakymo kokybės įvertinimas
    });
    
    // Apriboti istorijos dydį
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Gauti optimizuotus atrankos parametrus
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Siųsti užklausą su optimizuotais parametrais
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Jei naudotojas pateikia atsiliepimą, įrašyti jį būsimai optimizacijai
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

// Pavyzdinis naudojimas
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kūrybinė užduotis su vartotojo pageidavimais
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Aukšta kūrybiškumas (1-10)
          consistency: 3  // Žemas nuoseklumas (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Kodo generavimo užduotis
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Žemas kūrybiškumas
          precision: 8,   // Aukštas tikslumas
          consistency: 9  // Aukštas nuoseklumas
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

- Sukūrėme `AdaptiveSamplingManager` klasę, kuri valdo dinaminį imties ėmimą pagal užduoties tipą ir vartotojo nuostatas.
- Apibrėžėme imties profilius skirtingiems užduočių tipams (kūrybinės, faktinės, kodo, pokalbių).
- Įgyvendinome metodą užduoties tipui nustatyti iš užklausos, naudojant paprastus heuristinius metodus.
- Apskaičiavome imties parametrus pagal nustatytą užduoties tipą ir vartotojo nuostatas.
- Pritaikėme istorinius nustatymus pagal istorinę kokybę, optimizuodami imties parametrus.
- Užfiksavome našumą būsimoms korekcijoms, leidžiant sistemai mokytis iš praeities sąveikų.
- Išsiuntėme užklausas su dinamiškai sukonfigūruotais imties parametrais ir grąžinome sugeneruotą tekstą kartu su pritaikytais parametrais ir nustatytu užduoties tipu.
- Naudojome:
    - `userPreferences` leisti pritaikyti imties parametrus pagal vartotojo nurodytus kūrybiškumo, tikslumo ir nuoseklumo lygius.
    - `detectTaskType` nustatyti užduoties pobūdį pagal užklausą, leidžiant labiau suasmenintus atsakymus.
    - `recordPerformance` registruoti generuotų atsakymų našumą, leidžiant sistemai prisitaikyti ir tobulėti.
    - `applyLearnedAdjustments` modifikuoti imties parametrus pagal istorinį našumą, gerinant modelio gebėjimą generuoti aukštos kokybės atsakymus.
    - `generateResponse` apibrėžti visą atsakymo generavimo procesą su adaptaciniu imties ėmimu, palengvinant iškvietimą su skirtingomis užklausomis ir kontekstais.
    - `allowedTools` nurodyti, kokias priemones modelis gali naudoti generavimui, leidžiant labiau kontekstui pritaikytus atsakymus.
    - `feedbackScore` leisti vartotojams pateikti atsiliepimus apie sugeneruoto atsakymo kokybę, kuris gali būti naudojamas modelio našumo tobulinimui.
    - `performanceHistory` palaikyti ankstesnių sąveikų įrašą, leidžiant sistemai mokytis iš sėkmių ir nesėkmių.
    - `getSamplingParameters` dinamiškai koreguoti imties parametrus pagal užklausos kontekstą, leidžiant lanksčiau ir nuosekliau valdyti modelio elgesį.
    - `detectTaskType` klasifikuoti užduotį pagal užklausą, leidžiant sistemai taikyti tinkamas imties strategijas skirtingiems užklausų tipams.
    - `samplingProfiles` apibrėžti bazines imties konfigūracijas skirtingiems užduočių tipams, leidžiant greitai koreguoti pagal užduoties pobūdį.

---

## Kas toliau

- [5.7 Mastelio keitimas](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
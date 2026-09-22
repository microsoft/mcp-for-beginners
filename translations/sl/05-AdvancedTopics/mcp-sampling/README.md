> [!WARNING]
> Vzorcevanje je v MCP `2026-07-28` zastarelo. Ta lekcija je ohranjena za
> zastarele implementacije. Novi strežniki naj se neposredno povežejo z API
> ponudnika LLM.

# Vzorcevanje v protokolu kontekstov modela

> Vzorcevanje ostaja v specifikaciji `2026-07-28` zaradi združljivosti in je
> upravičeno do odstranitve v prvi reviziji, izdani na ali po 28. juliju,
> 2027. Primeri v tej lekciji lahko uporabljajo SDK API-je, ki izvajajo `2025-11-25`.
> Glej [Kaj se je spremenilo v MCP: specifikacija 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

V zastarelih implementacijah MCP omogoča Sampling strežnikom, da zahtevajo dokončanja LLM
prek klienta. Ta lekcija pojasnjuje ta zastareli potek protokola
za združljivost in migracijsko delo.

## Uvod

V tej lekciji bomo raziskali, kako konfigurirati parametre vzorcevanja v zahtevkih MCP in razumeti osnovno mehaniko protokola vzorcevanja.

## Cilji učenja

Do konca te lekcije boste znali:

- Razumeti ključne parametre vzorcevanja, ki so na voljo v MCP.
- Konfigurirati parametre vzorcevanja za različne primere uporabe.
- Izvesti deterministično vzorcevanje za ponovljive rezultate.
- Dinamično prilagajati parametre vzorcevanja na podlagi konteksta in uporabniških nastavitev.
- Uporabiti strategije vzorcevanja za izboljšanje zmogljivosti modela v različnih scenarijih.
- Razumeti, kako vzorcevanje deluje v poteku klient-strežnik MCP.

## Kako vzorcevanje deluje v MCP

Potek vzorcevanja v MCP sledi tem korakom:

1. Strežnik pošlje zahtevek `sampling/createMessage` klientu
2. Klient pregleda zahtevek in ga lahko spremeni
3. Klient vzorči iz LLM
4. Klient pregleda dokončanje
5. Klient vrne rezultat strežniku

Ta zasnova z vključenim človekom zagotavlja, da imajo uporabniki nadzor nad tem, kaj LLM vidi in generira.

## Pregled parametrov vzorcevanja

MCP določa naslednje parametre vzorcevanja, ki jih je mogoče konfigurirati v zahtevkih klienta:

| Parameter | Opis | Tipični razpon |
|-----------|-------------|---------------|
| `temperature` | Nadzoruje naključnost pri izbiri tokenov | 0,0 - 1,0 |
| `maxTokens` | Največje število tokenov, ki jih je treba generirati | Celo število |
| `stopSequences` | Prilagojeni nizi, ki ustavijo generiranje, ko se pojavijo | Tabela nizov |
| `metadata` | Dodatni parametri, specifični za ponudnika | JSON objekt |

Veliko ponudnikov LLM podpira dodatne parametre preko polja `metadata`, ki lahko vključujejo:

| Pogost razširitveni parameter | Opis | Tipični razpon |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - omejuje tokene na zgornjo kumulativno verjetnost | 0,0 - 1,0 |
| `top_k` | Omejuje izbiro tokenov na vrhunskih K možnosti | 1 - 100 |
| `presence_penalty` | Kaznuje tokene glede na njihovo prisotnost v besedilu do sedaj | -2,0 - 2,0 |
| `frequency_penalty` | Kaznuje tokene glede na njihovo frekvenco v besedilu do sedaj | -2,0 - 2,0 |
| `seed` | Posebno naključno seme za ponovljive rezultate | Celo število |

## Primer oblikovanja zahtevka

Tukaj je primer zahtevka za vzorcevanje od klienta v MCP:

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

## Oblika odgovora

Klient vrne rezultat dokončanja:

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

## Nadzor s človekom v zanki

Vzorcevanje MCP je zasnovano z miselnostjo nadzora s strani človeka:

- **Za pozive**:
  - Klienti naj uporabnikom pokažejo predlagani poziv
  - Uporabniki naj bodo sposobni spreminjati ali zavrniti pozive
  - Sistemske pozive je mogoče filtrirati ali spremeniti
  - Vključevanje konteksta nadzoruje klient

- **Za dokončanja**:
  - Klienti naj uporabnikom pokažejo dokončanje
  - Uporabniki naj bodo sposobni spreminjati ali zavrniti dokončanja
  - Klienti lahko filtrirajo ali spreminjajo dokončanja
  - Uporabniki nadzorujejo, kateri model se uporablja

S temi načeli v mislih si oglejmo, kako uvesti vzorcevanje v različnih programskih jezikih, s poudarkom na parametrih, ki jih večina ponudnikov LLM pogosto podpira.

## Varnostni premisleki

Pri izvajanju vzorcevanja v MCP upoštevajte naslednje varnostne najboljše prakse:

- **Preverite vsebino sporočil** pred pošiljanjem klientu
- **Očistite občutljive informacije** iz pozivov in dokončanj
- **Uvedite omejitve hitrosti** za preprečevanje zlorab
- **Nadzirajte uporabo vzorcevanja** za nenavadne vzorce
- **Šifrirajte podatke med prenosom** z uporabo varnih protokolov
- **Ravnajte z zasebnostjo uporabniških podatkov** v skladu z veljavnimi predpisi
- **Revidirajte zahtevke za vzorcevanje** za skladnost in varnost
- **Nadzorujte izpostavljenost stroškov** z ustreznimi omejitvami
- **Uvedite časovne omejitve** za zahtevke vzorcevanja
- **Prijazno obravnavajte napake modela** z ustreznimi nadomestnimi rešitvami

Parametri vzorcevanja omogočajo natančno prilagajanje vedenja jezikovnih modelov za doseganje želene ravnotežja med determinističnimi in ustvarjalnimi izhodi.

Oglejmo si, kako konfigurirati te parametre v različnih programskih jezikih.

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

V zgornji kodi smo:

- Ustvarili MCP klienta z določenim URL strežnika.
- Konfigurirali zahtevek s parametri vzorcevanja, kot so `temperature`, `top_p` in `top_k`.
- Poslali zahtevek in izpisali generirano besedilo.
- Uporabili:
    - `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem. V tem primeru smo dovolili orodja `ideaGenerator` in `marketAnalyzer` za pomoč pri ustvarjanju kreativnih idej za aplikacije.
    - `frequencyPenalty` in `presencePenalty` za nadzor ponavljanja in raznolikosti izhoda.
    - `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj ustvarjalnih odgovorov.
    - `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k zgornji kumulativni verjetnosti, kar izboljša kakovost generiranega besedila.
    - `top_k` za omejitev modela na top K najbolj verjetnih tokenov, kar lahko pomaga pri generiranju bolj koherentnih odgovorov.
    - `frequencyPenalty` in `presencePenalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v generiranem besedilu.

# [JavaScript](#tab/javascript)

```javascript
// Primer JavaScript: konfiguracija temperature in Top-P vzorčenja
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializirajte MCP odjemalca
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurirajte zahtevo z različnimi parametri vzorčenja
  const creativeSampling = {
    temperature: 0.9,    // Višja temperatura = več naključnosti/kreativnosti
    topP: 0.92,          // Upoštevajte tokene z najvišjo 92 % verjetnostno maso
    frequencyPenalty: 0.6, // Zmanjšajte ponavljanje zaporedij tokenov
    presencePenalty: 0.4   // Kaznujte tokene, ki so se do zdaj pojavili v besedilu
  };
  
  const factualSampling = {
    temperature: 0.2,    // Nižja temperatura = bolj determinističen/faktičen
    topP: 0.85,          // Malce bolj osredotočena izbira tokenov
    frequencyPenalty: 0.2, // Minimalna kazen za ponavljanje
    presencePenalty: 0.1   // Minimalna kazen za prisotnost
  };
  
  try {
    // Pošljite dve zahtevi z različnimi konfiguracijami vzorčenja
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

V zgornji kodi smo:

- Inicializirali MCP klienta z URL strežnika in API ključem.
- Konfigurirali dve skupini parametrov vzorcevanja: eno za ustvarjalne naloge in drugo za dejanske naloge.
- Poslali zahtevke s temi konfiguracijami, kar je modelu omogočilo uporabo določenih orodij za vsako nalogo.
- Izpisali generirane odgovore za pokazati učinke različnih parametrov vzorcevanja.
- Uporabili `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem. V tem primeru smo dovolili `ideaGenerator` in `environmentalImpactTool` za ustvarjalne naloge, in `factChecker` ter `dataAnalysisTool` za dejanske naloge.
- Uporabili `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj ustvarjalnih odgovorov.

- Uporabljeno `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k najvišji kumulativni verjetnostni masi, kar izboljšuje kakovost generiranega besedila.
- Uporabljeno `frequencyPenalty` in `presencePenalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v izhodu.
- Uporabljeno `top_k` za omejitev modela na top K najverjetnejših tokenov, kar lahko pomaga pri generiranju bolj koherentnih odgovorov.

---

## Deterministični vzorčenje

Za aplikacije, ki zahtevajo konsistentne izhode, deterministični vzorec zagotavlja ponovljive rezultate. To doseže z uporabo fiksne naključne semenske vrednosti in nastavitvijo temperature na nič.

Oglejmo si spodnjo vzorčno implementacijo, ki prikazuje deterministični vzorec v različnih programskih jezikih.

# [Java](#tab/java)

```java
// Java primer: Deterministični odgovori s fiksnim semenom
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Uporaba fiksnega semena za deterministične rezultate
        
        // Prvi zahtevek s fiksnim semenom
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatura nič za največjo determinističnost
            .build();
            
        // Drugi zahtevek z istim semenom
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Izvedi oba zahtevka
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Odgovori bi morali biti enaki zaradi istega semena in temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

V zgornji kodi smo:

- Ustvarili MCP odjemalca z določenim URL strežnika.
- Konfigurirali dva zahtevka z enakim pozivom, fiksno semensko vrednostjo in temperaturo nič.
- Poslali oba zahtevka in izpisali generirano besedilo.
- Demonstrirali, da so odgovori enaki zaradi deterministične narave konfiguracije vzorčenja (isti semenski vrednosti in temperatura).
- Uporabljeno `setSeed` za določitev fiksne naključne semenske vrednosti, ki zagotavlja, da model vedno generira isti izhod za isti vhod.
- Nastavljena `temperature` na nič za zagotovitev maksimalne determinističnosti, kar pomeni, da bo model vedno izbral najbolj verjeten naslednji token brez naključnosti.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Primer JavaScript: Deterministični odzivi s kontrolo semena
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Prvi zahtevek z fiksnim semenom
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura nič za maksimalno determinističnost
    });
    
    // Drugi zahtevek z enakim semenom in temperaturo
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Tretji zahtevek z drugačnim semenom, a enako temperaturo
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

V zgornji kodi smo:

- Inicializirali MCP odjemalca z URL strežnika.
- Konfigurirali dva zahtevka z enakim pozivom, fiksno semensko vrednostjo in temperaturo nič.
- Poslali oba zahtevka in izpisali generirano besedilo.
- Demonstrirali, da so odgovori enaki zaradi deterministične narave konfiguracije vzorčenja (isti semenski vrednosti in temperatura).
- Uporabljeno `seed` za določitev fiksne naključne semenske vrednosti, ki zagotavlja, da model vedno generira isti izhod za isti vhod.
- Nastavljena `temperature` na nič za zagotovitev maksimalne determinističnosti, kar pomeni, da bo model vedno izbral najbolj verjeten naslednji token brez naključnosti.
- Uporabljen drugačen semenski vrednost za tretji zahtevek, da pokažemo, da sprememba semenske vrednosti povzroči različne izhode, tudi z istim pozivom in temperaturo.

---

## Dinamična konfiguracija vzorčenja

Pametno vzorčenje prilagaja parametre glede na kontekst in zahteve posameznega zahtevka. To pomeni dinamično prilagajanje parametrov, kot so temperatura, top_p in kazni, glede na vrsto naloge, uporabniške preference ali zgodovinsko uspešnost.

Oglejmo si, kako implementirati dinamično vzorčenje v različnih programskih jezikih.

# [Python](#tab/python)

```python
# Python primer: Dinamično vzorčenje na podlagi konteksta zahteve
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Določite prednastavitve vzorčenja za različne vrste nalog
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Izberite osnovno prednastavitev
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Prilagodite glede na uporabniške nastavitve, če so na voljo
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Prilagodite temperaturo glede na željo po kreativnosti (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Prilagodite top_p glede na želeno raznolikost odgovorov
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Ustvarite in pošljite zahtevo z lastnimi parametri vzorčenja
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Vrni odgovor z metapodatki vzorčenja za preglednost
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

V zgornji kodi smo:

- Ustvarili razred `DynamicSamplingService`, ki upravlja prilagodljivo vzorčenje.
- Določili prednastavitve vzorčenja za različne vrste nalog (kreativne, faktačne, koda, analitične).
- Izbrali osnovno prednastavitev vzorčenja glede na vrsto naloge.
- Prilagodili parametre vzorčenja glede na uporabniške preference, kot sta stopnja kreativnosti in raznolikost.
- Poslali zahtevek z dinamično konfiguriranimi parametri vzorčenja.
- Vrnil generirano besedilo skupaj z uporabo parametrov vzorčenja in vrsto naloge za preglednost.
- Uporabljeno `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj kreativnih odgovorov.
- Uporabljeno `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k najvišji kumulativni verjetnostni masi, kar izboljšuje kakovost generiranega besedila.
- Uporabljeno `frequency_penalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v izhodu.
- Uporabljeno `user_preferences` za možnost prilagajanja parametrov vzorčenja glede na uporabniško definirane stopnje kreativnosti in raznolikosti.
- Uporabljeno `task_type` za določitev ustrezne strategije vzorčenja za zahtevek, kar omogoča bolj prilagojene odgovore glede na naravo naloge.
- Uporabljena metoda `send_request` za pošiljanje poziva z konfiguriranimi parametri vzorčenja, kar zagotavlja, da model generira besedilo v skladu z določenimi zahtevami.
- Uporabljeno `generated_text` za pridobitev odgovora modela, ki se nato vrne skupaj s parametri vzorčenja in vrsto naloge za nadaljnjo analizo ali prikaz.
- Uporabljeni funkciji `min` in `max` za zagotovitev, da so uporabniške preference omejene na veljavne vrednosti, s čimer preprečimo neveljavne konfiguracije vzorčenja.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript primer: Dinamična konfiguracija vzorčenja na podlagi uporabniškega konteksta
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Določi osnovne profile vzorčenja
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Sledi zgodovinski uspešnosti
    this.performanceHistory = [];
  }
  
  // Prepoznaj vrsto naloge iz poziva
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Enostavna hevristična detekcija - lahko se izboljša z ML klasifikacijo
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
    
    // Privzeto na pogovorno, če ni zaznana jasna vrsta
    return 'conversational';
  }
  
  // Izračunaj parametre vzorčenja na podlagi konteksta in uporabniških nastavitev
  getSamplingParameters(prompt, context = {}) {
    // Prepoznaj vrsto naloge
    const taskType = this.detectTaskType(prompt, context);
    
    // Pridobi osnovni profil
    let params = {...this.samplingProfiles[taskType]};
    
    // Prilagodi na podlagi uporabniških nastavitev
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Prilagodi temperaturo iz razpona 1-10 na ustrezno vrednost
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Višja natančnost pomeni nižji topP (bolj osredotočen izbor)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Višja konsistentnost pomeni manjše kazni
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Uveljavi prilagoditve, naučene iz zgodovine uspešnosti
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Enostavna prilagodljiva logika - lahko bi jo izboljšali z bolj sofisticiranimi algoritmi
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Upoštevaj le nedavno zgodovino
    
    if (relevantHistory.length > 0) {
      // Izračunaj povprečne ocene uspešnosti
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Če je uspešnost pod pragom, prilagodi parametre
      if (avgScore < 0.7) {
        // Rahla prilagoditev proti varnejšim vrednostim
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Zabeleži uspešnost za prihodnje prilagoditve
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Ocena kakovosti odgovora od 0 do 1
    });
    
    // Omeji velikost zgodovine
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Pridobi optimizirane parametre vzorčenja
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Pošlji zahtevek z optimiziranimi parametri
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Če uporabnik poda povratno informacijo, jo zabeleži za prihodnjo optimizacijo
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

// Primer uporabe
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Ustvarjalna naloga z uporabniškimi nastavitvami po meri
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Visoka ustvarjalnost (1-10)
          consistency: 3  // Nizka konsistentnost (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Naloga generiranja kode
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Nizka ustvarjalnost
          precision: 8,   // Visoka natančnost
          consistency: 9  // Visoka konsistentnost
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

V zgornji kodi smo:

- Ustvarili razred `AdaptiveSamplingManager`, ki upravlja dinamično vzorčenje glede na vrsto naloge in uporabniške preference.
- Določili vzorčne profile za različne vrste nalog (kreativne, faktačne, koda, pogovorne).
- Implementirali metodo za zaznavo vrste naloge iz poziva z uporabo enostavnih hevristik.
- Izračunali parametre vzorčenja glede na zaznano vrsto naloge in uporabniške preference.
- Uporabili naučene prilagoditve na podlagi zgodovinske uspešnosti za optimizacijo parametrov vzorčenja.
- Beležili uspešnost za prihodnje prilagoditve, kar sistemu omogoča učenje iz preteklih interakcij.
- Poslali zahtevke z dinamično konfiguriranimi parametri vzorčenja in vrnili generirano besedilo skupaj z uporabo parametrov in zaznano vrsto naloge.
- Uporaba:
    - `userPreferences` za omogočanje prilagajanja parametrov vzorčenja glede na uporabniško določene stopnje kreativnosti, natančnosti in konsistentnosti.
    - `detectTaskType` za določitev narave naloge na podlagi poziva, kar omogoča bolj prilagojene odgovore.
    - `recordPerformance` za beleženje uspešnosti generiranih odgovorov, kar sistemu omogoča prilagajanje in izboljševanje skozi čas.
    - `applyLearnedAdjustments` za spreminjanje parametrov vzorčenja na podlagi zgodovinske uspešnosti, s čimer izboljšujemo sposobnost modela za generiranje kakovostnih odgovorov.
    - `generateResponse` za zajem celotnega procesa generiranja odziva z adaptivnim vzorčenjem, kar olajša klic z različnimi pozivi in konteksti.
    - `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem, kar omogoča odgovore z boljšo kontekstualno zavednostjo.
    - `feedbackScore` za omogočanje uporabnikom, da podajo povratne informacije o kakovosti generiranega odgovora, ki se lahko uporabijo za nadaljnje izboljšanje delovanja modela skozi čas.
    - `performanceHistory` za vzdrževanje evidence preteklih interakcij, kar omogoča sistemu učenje iz preteklih uspehov in neuspehov.
    - `getSamplingParameters` za dinamično prilagajanje parametrov vzorčenja glede na kontekst zahtevka, kar omogoča bolj prilagodljivo in odzivno vedenje modela.
    - `detectTaskType` za razvrščanje naloge glede na poziv, kar sistemu omogoča uporabo ustreznih strategij vzorčenja za različne vrste zahtevkov.
    - `samplingProfiles` za določitev osnovnih konfiguracij vzorčenja za različne vrste nalog, kar omogoča hitre prilagoditve glede na naravo zahtevka.

---

## Kaj sledi

- [5.7 Skaliranje](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
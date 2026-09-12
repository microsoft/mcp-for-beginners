> [!WARNING]
> Odběr vzorků je v MCP `2026-07-28` zastaraný. Táto lekcia je zachovaná pre
> staršie implementácie. Nové servery by sa mali priamo integrovať s API poskytovateľa LLM.


# Odběr vzorků v protokole Model Context

> Odběr vzorků zostáva v špecifikácii `2026-07-28` pre kompatibilitu a je
> oprávnený na odstránenie v prvej revízii vydanej po 28. júli
> 2027. Príklady v tejto lekcii môžu používať SDK API, ktoré implementujú `2025-11-25`.
> Pozri [Čo sa zmenilo v MCP: Špecifikácia 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

V starších implementáciách MCP umožňuje odběr vzorků serverom požadovať dokončenia LLM
prostredníctvom klienta. Táto lekcia vysvetľuje tento zastaraný tok protokolu
pre účely kompatibility a migrácie.

## Úvod

V tejto lekcii preskúmame, ako nakonfigurovať parametre odběru vzorků v požiadavkách MCP a pochopiť základné mechanizmy protokolu odběru vzorků.

## Ciele učenia

Po skončení tejto lekcie budete schopní:

- Pochopiť kľúčové parametre odběru vzorků dostupné v MCP.
- Konfigurovať parametre odběru vzorků pre rôzne použitia.
- Implementovať deterministický odběr vzorků pre reprodukovateľné výsledky.
- Dynamicky prispôsobovať parametre odběru vzorků na základe kontextu a preferencií užívateľa.
- Používať stratégie odběru vzorků na zlepšenie výkonu modelu v rôznych scenároch.
- Pochopiť, ako odběr vzorků funguje v klient-serverový tok MCP.

## Ako funguje odběr vzorků v MCP

Tok odběru vzorků v MCP nasleduje tieto kroky:

1. Server odošle požiadavku `sampling/createMessage` klientovi
2. Klient skontroluje požiadavku a môže ju upraviť
3. Klient vykoná odběr vzorků z LLM
4. Klient skontroluje dokončenie
5. Klient vráti výsledok serveru

Tento návrh s človekom v slučke zabezpečuje, že používatelia majú kontrolu nad tým, čo LLM vidí a generuje.

## Prehľad parametrov odběru vzorků

MCP definuje nasledujúce parametre odběru vzorků, ktoré sa dajú konfigurovať v požiadavkách klienta:

| Parameter | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `temperature` | Riadi náhodnosť výberu tokenov | 0.0 - 1.0 |
| `maxTokens` | Maximálny počet generovaných tokenov | Celé číslo |
| `stopSequences` | Vlastné sekvencie, ktorými sa generovanie zastaví | Pole reťazcov |
| `metadata` | Dodatočné parametre špecifické pre poskytovateľa | JSON objekt |

Mnoho poskytovateľov LLM podporuje dodatočné parametre prostredníctvom poľa `metadata`, ktoré môžu obsahovať:

| Bežný rozšírený parameter | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - obmedzuje tokeny na najvyššie kumulatívne pravdepodobnosti | 0.0 - 1.0 |
| `top_k` | Obmedzuje výber tokenov na najlepších K možností | 1 - 100 |
| `presence_penalty` | Penalizuje tokeny podľa ich prítomnosti v texte doteraz | -2.0 - 2.0 |
| `frequency_penalty` | Penalizuje tokeny podľa ich frekvencie v texte doteraz | -2.0 - 2.0 |
| `seed` | Konkrétne náhodné semeno pre reprodukovateľné výsledky | Celé číslo |

## Príklad formátu požiadavky

Tu je príklad požiadavky na odběr vzorků od klienta v MCP:

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

## Formát odpovede

Klient vráti výsledok dokončenia:

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

## Ovládanie s človekom v slučke

Odběr vzorků v MCP je navrhnutý s dôrazom na ľudský dohľad:

- **Pre výzvy**:
  - Klienti by mali zobraziť užívateľom navrhovanú výzvu
  - Užívateľ by mal mať možnosť výzvy upraviť alebo odmietnuť
  - Systémové výzvy môžu byť filtrované alebo upravené
  - Zaradenie kontextu kontroluje klient

- **Pre dokončenia**:
  - Klienti by mali užívateľom ukázať dokončenie
  - Užívateľ by mal mať možnosť dokončenia upraviť alebo odmietnuť
  - Klienti môžu filtrovať alebo upravovať dokončenia
  - Užívateľ riadi, ktorý model sa použije

S týmito zásadami sa pozrime, ako implementovať odběr vzorků v rôznych programovacích jazykoch, so zameraním na parametre bežne podporované u poskytovateľov LLM.

## Bezpečnostné úvahy

Pri implementácii odběru vzorků v MCP zvážte tieto bezpečnostné najlepšie praktiky:

- **Validovať celý obsah správ** pred odoslaním klientovi
- **Sanitovať citlivé informácie** z výziev a dokončení
- **Implementovať limity rýchlosti** proti zneužitiu
- **Monitorovať používanie odběru vzorků** pre nezvyčajné vzory
- **Šifrovať dáta počas prenosu** pomocou bezpečných protokolov
- **Zaobchádzať s ochranou súkromia užívateľa** podľa príslušných predpisov
- **Auditovať požiadavky na odběr vzorků** pre súlad a bezpečnosť
- **Kontrolovať vystavenie nákladov** vhodnými limitmi
- **Implementovať časové limity** pre požiadavky odběru vzorků
- **Spracovať chyby modelu s vhodnými záložnými mechanizmami**

Parametre odběru vzorků umožňujú jemné doladenie správania jazykových modelov, aby sa dosiahol požadovaný balans medzi deterministickými a kreatívnymi výstupmi.

Pozrime sa, ako nastaviť tieto parametre v rôznych programovacích jazykoch.

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

V predchádzajúcom kóde sme:

- Vytvorili klienta MCP so špecifickou URL servera.
- Nakonfigurovali požiadavku s parametrami odběru vzorků ako `temperature`, `top_p` a `top_k`.
- Odooslali požiadavku a vytlačili vygenerovaný text.
- Použili sme:
    - `allowedTools` na špecifikáciu nástrojov, ktoré môže model počas generovania použiť. V tomto prípade sme povolili nástroje `ideaGenerator` a `marketAnalyzer` na asistenciu pri generovaní kreatívnych nápadov na aplikácie.
    - `frequencyPenalty` a `presencePenalty` na kontrolu opakovania a rozmanitosti v výstupe.
    - `temperature` na riadenie náhodnosti výstupu, kde vyššie hodnoty vedú ku kreatívnejším odpovediam.
    - `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnosti, čím sa zlepší kvalita generovaného textu.
    - `top_k` na obmedzenie modelu na najpravdepodobnejších K tokenov, čo môže pomôcť pri generovaní súdržnejších odpovedí.
    - `frequencyPenalty` a `presencePenalty` na zníženie opakovania a podporu rozmanitosti generovaného textu.

# [JavaScript](#tab/javascript)

```javascript
// Príklad JavaScriptu: Konfigurácia teploty a Top-P vzorkovania
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializujte MCP klienta
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Nakonfigurujte požiadavku s rôznymi parametrami vzorkovania
  const creativeSampling = {
    temperature: 0.9,    // Vyššia teplota = väčšia náhodnosť/kreativita
    topP: 0.92,          // Zvážte tokeny s pravdepodobnostnou hmotnosťou top 92 %
    frequencyPenalty: 0.6, // Znížte opakovanie sekvencií tokenov
    presencePenalty: 0.4   // Penalizujte tokeny, ktoré sa zatiaľ v texte objavili
  };
  
  const factualSampling = {
    temperature: 0.2,    // Nižšia teplota = viac deterministické/faktické
    topP: 0.85,          // Mierne viac zameraný výber tokenov
    frequencyPenalty: 0.2, // Minimálny trest za opakovanie
    presencePenalty: 0.1   // Minimálny trest za prítomnosť
  };
  
  try {
    // Odoslať dve požiadavky s rôznymi konfiguráciami vzorkovania
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

V predchádzajúcom kóde sme:

- Inicializovali klienta MCP s URL servera a API kľúčom.
- Nakonfigurovali dve sady parametrov odběru vzorků: jednu pre kreatívne úlohy a druhú pre faktické úlohy.
- Odooslali požiadavky s týmito konfiguráciami, čo modelu umožnilo použiť špecifické nástroje pre každú úlohu.
- Vytlačili generované odpovede, aby sme demonštrovali účinky rôznych parametrov odběru vzorků.
- Použili sme `allowedTools` na špecifikáciu nástrojov, ktoré môže model počas generovania použiť. V tomto prípade sme povolili `ideaGenerator` a `environmentalImpactTool` pre kreatívne úlohy, a `factChecker` a `dataAnalysisTool` pre faktické úlohy.
- Použili sme `temperature` na riadenie náhodnosti výstupu, kde vyššie hodnoty vedú ku kreatívnejším odpovediam.

- Použité `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnostnej hmote, čím sa zvyšuje kvalita generovaného textu.
- Použité `frequencyPenalty` a `presencePenalty` na zníženie opakovania a podporu rozmanitosti výstupu.
- Použité `top_k` na obmedzenie modelu na top K najpravdepodobnejších tokenov, čo môže pomôcť pri generovaní koherentnejších odpovedí.

---

## Deterministické vzorkovanie

Pre aplikácie vyžadujúce konzistentné výstupy zabezpečuje deterministické vzorkovanie reprodukovateľné výsledky. Umožňuje to použitie pevne stanoveného náhodného semienka a nastavenie teploty na nulu.

Pozrime sa na nasledujúcu ukážkovú implementáciu deterministického vzorkovania v rôznych programovacích jazykoch.

# [Java](#tab/java)

```java
// Java príklad: Deterministické odpovede s pevne nastavým ziarnom
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Použitie pevného ziarna pre deterministické výsledky
        
        // Prvý dopyt s pevným ziarnom
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nulová teplota pre maximálny determinizmus
            .build();
            
        // Druhý dopyt s rovnakým ziarnom
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Vykonať oba dopyty
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Odpovede by mali byť identické kvôli rovnakému ziaru a teplote=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

V predchádzajúcom kóde sme:

- Vytvorili klienta MCP s určenou URL servera.
- Nastavili dve požiadavky s rovnakým promptom, pevným semienkom a nulovou teplotou.
- Odooslali obe požiadavky a vytlačili generovaný text.
- Ukázali, že odpovede sú identické kvôli deterministickej povahe konfigurácie vzorkovania (rovnaké semienko a teplota).
- Použili `setSeed` na určenie pevného náhodného semienka, čím sa zabezpečilo, že model vždy vygeneruje rovnaký výstup pre rovnaký vstup.
- Nastavili `temperature` na nulu pre maximálnu deterministickosť, čo znamená, že model vždy vyberie najpravdepodobnejší nasledujúci token bez náhody.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Príklad JavaScriptu: Deterministické odpovede s riadením semienka
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Prvá požiadavka s pevným semienkom
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nulová teplota pre maximálny determinizmus
    });
    
    // Druhá požiadavka s rovnakým semienkom a teplotou
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Tretia požiadavka s iným semienkom, ale rovnakou teplotou
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

V predchádzajúcom kóde sme:

- Inicializovali klienta MCP s URL servera.
- Nastavili dve požiadavky s rovnakým promptom, pevným semienkom a nulovou teplotou.
- Odooslali obe požiadavky a vytlačili generovaný text.
- Ukázali, že odpovede sú identické kvôli deterministickej povahe konfigurácie vzorkovania (rovnaké semienko a teplota).
- Použili `seed` na určenie pevného náhodného semienka, čím sa zabezpečilo, že model vždy vygeneruje rovnaký výstup pre rovnaký vstup.
- Nastavili `temperature` na nulu pre maximálnu deterministickosť, čo znamená, že model vždy vyberie najpravdepodobnejší nasledujúci token bez náhody.
- Použili iné semienko pre tretiu požiadavku, aby sme ukázali, že zmena semienka vedie k odlišným výstupom, aj pri rovnakom promte a teplote.

---

## Dynamická konfigurácia vzorkovania

Inteligentné vzorkovanie prispôsobuje parametre podľa kontextu a požiadaviek každej požiadavky. Znamená to dynamické nastavenie parametrov ako teplota, top_p a penalty podľa typu úlohy, preferencií používateľa alebo historického výkonu.

Pozrime sa, ako implementovať dynamické vzorkovanie v rôznych programovacích jazykoch.

# [Python](#tab/python)

```python
# Príklad v Pythone: Dynamické vzorkovanie na základe kontextu požiadavky
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definujte prednastavenia vzorkovania pre rôzne typy úloh
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Vyberte základné prednastavenie
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Upravte na základe preferencií používateľa, ak sú poskytnuté
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Nastavte teplotu podľa preferencie kreativity (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Upravte top_p podľa požadovanej rôznorodosti odpovede
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Vytvorte a odošlite požiadavku s vlastnými parametrami vzorkovania
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Vráťte odpoveď s metadátami vzorkovania pre transparentnosť
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

V predchádzajúcom kóde sme:

- Vytvorili triedu `DynamicSamplingService`, ktorá spravuje adaptívne vzorkovanie.
- Definovali prednastavenia vzorkovania pre rôzne typy úloh (kreatívne, faktické, kódové, analytické).
- Vybrali základné prednastavenie vzorkovania podľa typu úlohy.
- Upravili parametre vzorkovania na základe preferencií používateľa, ako sú úroveň kreativity a rozmanitosti.
- Odooslali požiadavku s dynamicky nakonfigurovanými parametrami vzorkovania.
- Vrátili generovaný text spolu s použitými parametrami vzorkovania a typom úlohy pre prehľadnosť.
- Použili `temperature` na riadenie náhodnosti výstupu, pričom vyššie hodnoty vedú k tvorivejším odpovediam.
- Použili `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnostnej hmote, čím sa zvyšuje kvalita generovaného textu.
- Použili `frequency_penalty` na zníženie opakovania a podporu rozmanitosti výstupu.
- Použili `user_preferences` na umožnenie prispôsobenia parametrov vzorkovania na základe používateľom definovanej úrovne kreativity a rozmanitosti.
- Použili `task_type` na určenie vhodnej stratégie vzorkovania pre požiadavku, čo umožňuje prispôsobenejšie odpovede podľa povahy úlohy.
- Použili metódu `send_request` na odoslanie promptu s nakonfigurovanými parametrami vzorkovania, čím sa zabezpečilo, že model generuje text podľa stanovených požiadaviek.
- Použili `generated_text` na získanie odpovede modelu, ktorá je následne vrátená spolu s parametrami vzorkovania a typom úlohy na ďalšiu analýzu alebo zobrazenie.
- Použili funkcie `min` a `max` na zabezpečenie, že preferencie používateľa sú ohraničené platným rozsahom, čím sa zabráni neplatnej konfigurácii vzorkovania.

# [JavaScript Dynamické](#tab/javascript-dynamic)

```javascript
// Príklad JavaScriptu: Dynamická konfigurácia sampling-u založená na kontexte používateľa
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definujte základné profily sampling-u
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Sledovať historický výkon
    this.performanceHistory = [];
  }
  
  // Detegovať typ úlohy z promptu
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Jednoduchá heuristická detekcia - môže byť vylepšená klasifikáciou ML
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
    
    // Predvolená konverzačná voľba, ak nie je detegovaný jasný typ
    return 'conversational';
  }
  
  // Vypočítať parametre sampling-u na základe kontextu a preferencií používateľa
  getSamplingParameters(prompt, context = {}) {
    // Detegovať typ úlohy
    const taskType = this.detectTaskType(prompt, context);
    
    // Získať základný profil
    let params = {...this.samplingProfiles[taskType]};
    
    // Upravte podľa preferencií používateľa
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Prekonať škálu od 1-10 na vhodný rozsah teploty
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Vyššia presnosť znamená nižšie topP (viac zameraný výber)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Vyššia konzistencia znamená nižšie penalizácie
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplikovať naučené úpravy z histórie výkonu
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Jednoduchá adaptívna logika - môže byť vylepšená sofistikovanejšími algoritmami
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Zohľadniť iba nedávnu históriu
    
    if (relevantHistory.length > 0) {
      // Vypočítať priemerné skóre výkonu
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Ak výkon je pod prahom, upraviť parametre
      if (avgScore < 0.7) {
        // Jemná úprava smerom k bezpečnejším hodnotám
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Zaznamenať výkon pre budúce úpravy
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Hodnotenie kvality odpovede od 0 do 1
    });
    
    // Obmedziť veľkosť histórie
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Získať optimalizované parametre sampling-u
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Odoslať požiadavku s optimalizovanými parametrami
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Ak používateľ poskytne spätnú väzbu, zaznamenať ju pre budúcu optimalizáciu
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

// Príklad použitia
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreatívna úloha s vlastnými preferenciami používateľa
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Vysoká kreativita (1-10)
          consistency: 3  // Nízka konzistencia (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Úloha generovania kódu
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Nízka kreativita
          precision: 8,   // Vysoká presnosť
          consistency: 9  // Vysoká konzistencia
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

V predchádzajúcom kóde sme:

- Vytvorili triedu `AdaptiveSamplingManager`, ktorá spravuje dynamické vzorkovanie podľa typu úlohy a preferencií používateľa.
- Definovali profily vzorkovania pre rôzne typy úloh (kreatívne, faktické, kódové, konverzačné).
- Implementovali metódu na detekciu typu úlohy z promptu pomocou jednoduchých heuristík.
- Vypočítali parametre vzorkovania podľa detegovaného typu úlohy a používateľských preferencií.
- Aplikovali naučené úpravy na základe historického výkonu na optimalizáciu parametrov vzorkovania.
- Zaznamenali výkon pre budúce úpravy, čo umožňuje systému učiť sa z minulých interakcií.
- Odooslali požiadavky s dynamicky nakonfigurovanými parametrami vzorkovania a vrátili generovaný text spolu s použitými parametrami a detegovaným typom úlohy.
- Použili:
    - `userPreferences` na umožnenie prispôsobenia parametrov vzorkovania na základe používateľom definovanej kreativity, presnosti a konzistentnosti.
    - `detectTaskType` na určenie povahy úlohy podľa promptu, čo umožňuje prispôsobenejšie odpovede.
    - `recordPerformance` na zaznamenávanie výkonu generovaných odpovedí, čo umožňuje systému adaptovať sa a zlepšovať v čase.
    - `applyLearnedAdjustments` na úpravu parametrov vzorkovania na základe historického výkonu, čím sa zvyšuje schopnosť modelu generovať kvalitné odpovede.
    - `generateResponse` na zapuzdrenie celého procesu generovania odpovede s adaptívnym vzorkovaním, čo uľahčuje volanie s rôznymi promptmi a kontextami.
    - `allowedTools` na určenie, ktoré nástroje môže model použiť počas generovania, čo umožňuje kontextovo uvážlivé odpovede.
    - `feedbackScore` na umožnenie používateľom poskytovať spätnú väzbu o kvalite generovanej odpovede, ktorá môže byť použitá na ďalšie zdokonaľovanie výkonu modelu v čase.
    - `performanceHistory` na udržiavanie záznamu o minulých interakciách, čo umožňuje systému učiť sa z predchádzajúcich úspechov a neúspechov.
    - `getSamplingParameters` na dynamickú úpravu parametrov vzorkovania podľa kontextu požiadavky, čo umožňuje flexibilnejšie a reagujúce správanie modelu.
    - `detectTaskType` na klasifikáciu úlohy podľa promptu, čo umožňuje systému aplikovať vhodné stratégie vzorkovania pre rôzne typy požiadaviek.
    - `samplingProfiles` na definovanie základných konfigurácií vzorkovania pre rôzne typy úloh, čo umožňuje rýchle úpravy podľa povahy požiadavky.

---

## Čo ďalej

- [5.7 Škálovanie](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
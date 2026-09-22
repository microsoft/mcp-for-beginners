> [!WARNING]
> Vzorkování je v MCP `2026-07-28` zastaralé. Tato lekce je ponechána pro
> starší implementace. Nové servery by měly integrovat přímo s API poskytovatele LLM.


# Vzorkování v Model Context Protocol

> Vzorkování zůstává ve specifikaci `2026-07-28` pro kompatibilitu a
> může být odstraněno při první revizi vydané po 28. červenci
> 2027. Příklady v této lekci mohou používat SDK API implementující `2025-11-25`.
> Viz [Co se změnilo v MCP: Specifikace 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Ve starších implementacích MCP umožňuje vzorkování serverům požadovat dokončení LLM
přes klienta. Tato lekce vysvětluje tento zastaralý protokol
pro kompatibilitu a práci s migrací.

## Úvod

V této lekci prozkoumáme, jak konfigurovat parametry vzorkování v požadavcích MCP a pochopit základní protokolovou mechaniku vzorkování.

## Výukové cíle

Na konci této lekce budete schopni:

- Pochopit klíčové parametry vzorkování dostupné v MCP.
- Konfigurovat parametry vzorkování pro různé případy použití.
- Implementovat deterministické vzorkování pro reprodukovatelné výsledky.
- Dynamicky upravovat parametry vzorkování podle kontextu a preferencí uživatele.
- Použít strategie vzorkování ke zlepšení výkonu modelu v různých scénářích.
- Pochopit, jak vzorkování funguje v klient-server toku MCP.

## Jak vzorkování funguje v MCP

Tok vzorkování v MCP probíhá následujícími kroky:

1. Server odešle požadavek `sampling/createMessage` klientovi
2. Klient požadavek zhodnotí a může jej upravit
3. Klient provede vzorkování z LLM
4. Klient přezkoumá dokončení
5. Klient vrátí výsledek serveru

Tento návrh s lidským zásahem zajišťuje, že uživatelé mají kontrolu nad tím, co LLM vidí a generuje.

## Přehled parametrů vzorkování

MCP definuje následující parametry vzorkování, které lze konfigurovat v požadavcích klienta:

| Parametr | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `temperature` | Řídí náhodnost při výběru tokenů | 0.0 - 1.0 |
| `maxTokens` | Maximální počet generovaných tokenů | Celé číslo |
| `stopSequences` | Vlastní sekvence, které zastaví generování při nalezení | Pole řetězců |
| `metadata` | Další parametry specifické pro poskytovatele | JSON objekt |

Mnoho poskytovatelů LLM podporuje další parametry přes pole `metadata`, které mohou zahrnovat:

| Běžný parametr rozšíření | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - omezuje tokeny na kumulativní pravděpodobnost | 0.0 - 1.0 |
| `top_k` | Omezuje výběr tokenů na top K možností | 1 - 100 |
| `presence_penalty` | Penalizuje tokeny podle jejich výskytu v textu | -2.0 - 2.0 |
| `frequency_penalty` | Penalizuje tokeny podle jejich frekvence v textu | -2.0 - 2.0 |
| `seed` | Specifické náhodné semínko pro reprodukovatelné výsledky | Celé číslo |

## Ukázkový formát požadavku

Zde je příklad požadavku na vzorkování od klienta v MCP:

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

## Formát odpovědi

Klient vrací výsledek dokončení:

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

## Ovládání s lidským zásahem

MCP vzorkování je navrženo s ohledem na lidský dohled:


- **Pro výzvy**:
  - Klienti by měli uživatelům zobrazovat navrhovanou výzvu
  - Uživatelé by měli mít možnost výzvy upravit nebo odmítnout
  - Systémové výzvy lze filtrovat nebo upravovat
  - Za zahrnutí kontextu odpovídá klient

- **Pro dokončování**:
  - Klienti by měli uživatelům zobrazovat dokončení
  - Uživatelé by měli mít možnost dokončení upravit nebo odmítnout
  - Klienti mohou filtrovat nebo upravovat dokončení
  - Uživatelé mají kontrolu nad tím, který model se použije

S těmito zásadami na paměti se podívejme, jak implementovat vzorkování v různých programovacích jazycích se zaměřením na parametry běžně podporované poskytovateli LLM.

## Bezpečnostní úvahy

Při implementaci vzorkování v MCP zvažte tyto nejlepší bezpečnostní postupy:

- **Ověřte veškerý obsah zpráv** před jeho odesláním klientovi
- **Sanitizujte citlivé informace** z výzev a dokončení
- **Implementujte limity rychlosti** pro prevenci zneužití
- **Sledujte využití vzorkování** kvůli neobvyklým vzorcům
- **Šifrujte data při přenosu** pomocí bezpečných protokolů
- **Zabezpečte ochranu osobních údajů uživatelů** podle příslušných nařízení
- **Auditujte požadavky na vzorkování** za účelem souladu a bezpečnosti
- **Kontrolujte vystavení nákladům** s vhodnými limity
- **Implementujte časové limity** pro požadavky na vzorkování
- **Elegantně řešte chyby modelu** vhodnými záložními mechanismy

Parametry vzorkování umožňují jemné ladění chování jazykových modelů k dosažení požadované rovnováhy mezi deterministickými a kreativními výstupy.

Podívejme se, jak nakonfigurovat tyto parametry v různých programovacích jazycích.

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

V předchozím kódu jsme:

- Vytvořili klienta MCP s konkrétní URL serveru.
- Nakonfigurovali požadavek s parametry vzorkování jako `temperature`, `top_p` a `top_k`.
- Odeslali požadavek a vytiskli vygenerovaný text.
- Použili jsme:
    - `allowedTools` k určení nástrojů, které může model během generování používat. V tomto případě jsme povolili nástroje `ideaGenerator` a `marketAnalyzer` pro pomoc při generování kreativních nápadů na aplikace.
    - `frequencyPenalty` a `presencePenalty` pro kontrolu opakování a rozmanitosti výstupu.
    - `temperature` ke kontrole náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.
    - `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnostní hmotě, čímž se zlepšuje kvalita generovaného textu.
    - `top_k` k omezení modelu na top K nejpravděpodobnějších tokenů, což může pomoci při generování koherentnějších odpovědí.
    - `frequencyPenalty` a `presencePenalty` ke snížení opakování a podpoře rozmanitosti v generovaném textu.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript příklad: Konfigurace teploty a Top-P vzorkování
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inicializace MCP klienta
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurace požadavku s různými parametry vzorkování
  const creativeSampling = {
    temperature: 0.9,    // Vyšší teplota = více náhodnosti/kreativity
    topP: 0.92,          // Zahrnout tokeny s pravděpodobnostní hmotou top 92 %
    frequencyPenalty: 0.6, // Snížit opakování sekvencí tokenů
    presencePenalty: 0.4   // Penalizovat tokeny, které se již v textu objevily
  };
  
  const factualSampling = {
    temperature: 0.2,    // Nižší teplota = více deterministické/faktické
    topP: 0.85,          // Mírně více zaměřený výběr tokenů
    frequencyPenalty: 0.2, // Minimální penalizace opakování
    presencePenalty: 0.1   // Minimální penalizace přítomnosti
  };
  
  try {
    // Odeslat dva požadavky s různou konfigurací vzorkování
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

V předchozím kódu jsme:

- Inicializovali klienta MCP s URL serveru a API klíčem.
- Nakonfigurovali dva soubory parametrů vzorkování: jeden pro kreativní úlohy a druhý pro faktické úlohy.
- Odeslali požadavky s těmito konfiguracemi, což umožnilo modelu používat specifické nástroje pro každou úlohu.
- Vytiskli vygenerované odpovědi, abychom ukázali efekty různých parametrů vzorkování.
- Použili `allowedTools` k určení, které nástroje může model během generování používat. V tomto případě jsme povolili `ideaGenerator` a `environmentalImpactTool` pro kreativní úlohy a `factChecker` a `dataAnalysisTool` pro faktické úlohy.
- Použili `temperature` ke kontrole náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.

- Použili jsme `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnostní hmotě, čímž jsme zlepšili kvalitu generovaného textu.
- Použili jsme `frequencyPenalty` a `presencePenalty` ke snížení opakování a podpoře rozmanitosti výstupu.
- Použili jsme `top_k` k omezení modelu na top K nejpravděpodobnějších tokenů, což může pomoci při generování soudržnějších odpovědí.

---

## Deterministické vzorkování

Pro aplikace, které vyžadují konzistentní výstupy, zajišťuje deterministické vzorkování reprodukovatelné výsledky. Dělá to pomocí pevného náhodného semínka a nastavením teploty na nulu.

Podívejme se na níže uvedenou ukázkovou implementaci, která demonstruje deterministické vzorkování v různých programovacích jazycích.

# [Java](#tab/java)

```java
// Java příklad: Deterministické odpovědi s pevně nastaveným semínkem
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Použití pevně nastaveného semínka pro deterministické výsledky
        
        // První požadavek s pevným semínkem
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nulová teplota pro maximální determinismus
            .build();
            
        // Druhý požadavek se stejným semínkem
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Proveďte oba požadavky
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Odpovědi by měly být identické díky stejnému semínku a teplotě=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

V předchozím kódu jsme:

- Vytvořili klienta MCP s určenou URL serveru.
- Nakonfigurovali dva požadavky se stejným promptem, pevným semínkem a nulovou teplotou.
- Odeslali oba požadavky a vytiskli generovaný text.
- Ukázali, že odpovědi jsou identické díky deterministické povaze konfigurace vzorkování (stejné semínko a teplota).
- Použili `setSeed` k určení pevného náhodného semínka, čímž jsme zajistili, že model pokaždé vygeneruje stejný výstup pro stejný vstup.
- Nastavili `temperature` na nulu pro zajištění maximální determinismu, což znamená, že model vždy vybere nejpravděpodobnější následující token bez náhodnosti.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Příklad JavaScriptu: Deterministické odpovědi s řízením semínka
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // První požadavek s pevně nastaveným semínkem
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nulová teplota pro maximální determinismus
    });
    
    // Druhý požadavek se stejným semínkem a teplotou
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Třetí požadavek s odlišným semínkem, ale stejnou teplotou
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

V předchozím kódu jsme:

- Inicializovali klienta MCP s URL serveru.
- Nakonfigurovali dva požadavky se stejným promptem, pevným semínkem a nulovou teplotou.
- Odeslali oba požadavky a vytiskli generovaný text.
- Ukázali, že odpovědi jsou totožné díky deterministické povaze konfigurace vzorkování (stejné semínko a teplota).
- Použili `seed` k určení pevného náhodného semínka, čímž jsme zajistili, že model pokaždé vygeneruje stejný výstup pro stejný vstup.
- Nastavili `temperature` na nulu pro zajištění maximální determinismu, což znamená, že model vždy vybere nejpravděpodobnější následující token bez náhodnosti.
- Ve třetím požadavku použili jiné semínko, aby se ukázalo, že změna semínka vede k odlišným výstupům, i když je stejný prompt a teplota.

---

## Dynamická konfigurace vzorkování

Inteligentní vzorkování přizpůsobuje parametry na základě kontextu a požadavků každého požadavku. To znamená dynamické nastavování parametrů jako teplota, top_p a penalizace podle typu úkolu, uživatelských preferencí nebo historické výkonnosti.

Podívejme se, jak implementovat dynamické vzorkování v různých programovacích jazycích.

# [Python](#tab/python)

```python
# Python příklad: Dynamické vzorkování založené na kontextu požadavku
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definujte přednastavení vzorkování pro různé typy úloh
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Vyberte základní přednastavení
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Upravte podle uživatelských preferencí, pokud jsou k dispozici
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Škálujte teplotu na základě preference kreativity (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Upravte top_p na základě požadované rozmanitosti odpovědi
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Vytvořte a odešlete požadavek s vlastními parametry vzorkování
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Vraťte odpověď s metadaty vzorkování pro transparentnost
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

V předchozím kódu jsme:

- Vytvořili třídu `DynamicSamplingService`, která spravuje adaptivní vzorkování.
- Definovali přednastavené vzorkování pro různé typy úkolů (kreativní, faktické, kódové, analytické).
- Vybrali základní přednastavení vzorkování na základě typu úkolu.
- Upravil parametry vzorkování na základě uživatelských preferencí, jako je úroveň kreativity a rozmanitosti.
- Odeslali požadavek s dynamicky nakonfigurovanými parametry vzorkování.
- Vrátili generovaný text spolu s použitými parametry vzorkování a typem úkolu pro přehlednost.
- Použili `temperature` ke kontrole náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.
- Použili `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnostní hmotě, čímž jsme zlepšili kvalitu generovaného textu.
- Použili `frequency_penalty` ke snížení opakování a podpoře rozmanitosti výstupu.
- Použili `user_preferences` k umožnění přizpůsobení parametrů vzorkování na základě uživatelem definované úrovně kreativity a rozmanitosti.
- Použili `task_type` k určení vhodné strategie vzorkování pro požadavek, což umožňuje více přizpůsobené odpovědi podle povahy úkolu.
- Použili metodu `send_request` k odeslání promptu s nakonfigurovanými parametry vzorkování, což zajišťuje, že model generuje text podle specifikovaných požadavků.
- Použili `generated_text` pro získání odpovědi modelu, která je poté vrácena spolu s parametry vzorkování a typem úkolu pro další analýzu nebo zobrazení.
- Použili funkce `min` a `max` k zajištění, že uživatelské preference jsou omezeny na platné hodnoty, čímž zabráníme neplatným konfiguracím vzorkování.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript příklad: Dynamická konfigurace vzorkování na základě uživatelského kontextu
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definovat základní profily vzorkování
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Sledovat historický výkon
    this.performanceHistory = [];
  }
  
  // Detekovat typ úkolu z promptu
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Jednoduchá heuristická detekce - může být vylepšena ML klasifikací
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
    
    // Výchozí na konverzační, pokud není detekován žádný jasný typ
    return 'conversational';
  }
  
  // Vypočítat parametry vzorkování na základě kontextu a uživatelských preferencí
  getSamplingParameters(prompt, context = {}) {
    // Detekovat typ úkolu
    const taskType = this.detectTaskType(prompt, context);
    
    // Získat základní profil
    let params = {...this.samplingProfiles[taskType]};
    
    // Upravit na základě uživatelských preferencí
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Převést ze škály 1-10 na odpovídající rozsah teploty
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Vyšší přesnost znamená nižší topP (více zaměřený výběr)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Vyšší konzistence znamená nižší penalizace
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplikovat naučené úpravy z historie výkonu
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Jednoduchá adaptivní logika - může být vylepšena složitějšími algoritmy
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Zohlednit pouze nedávnou historii
    
    if (relevantHistory.length > 0) {
      // Vypočítat průměrné skóre výkonu
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Pokud je výkon pod prahem, upravit parametry
      if (avgScore < 0.7) {
        // Jemná úprava směrem k bezpečnějším hodnotám
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Zaznamenat výkon pro budoucí úpravy
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Hodnocení kvality odpovědi od 0 do 1
    });
    
    // Omezit velikost historie
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Získat optimalizované parametry vzorkování
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Odeslat požadavek s optimalizovanými parametry
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Pokud uživatel poskytne zpětnou vazbu, zaznamenat ji pro budoucí optimalizaci
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

// Příklad použití
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreativní úkol s vlastními uživatelskými preferencemi
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Vysoká kreativita (1-10)
          consistency: 3  // Nízká konzistence (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Úkol generování kódu
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Nízká kreativita
          precision: 8,   // Vysoká přesnost
          consistency: 9  // Vysoká konzistence
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

V předchozím kódu jsme:

- Vytvořili třídu `AdaptiveSamplingManager`, která spravuje dynamické vzorkování podle typu úkolu a uživatelských preferencí.
- Definovali profily vzorkování pro různé typy úkolů (kreativní, faktické, kódové, konverzační).
- Implementovali metodu pro detekci typu úkolu z promptu pomocí jednoduchých heuristik.
- Vypočítali parametry vzorkování na základě detekovaného typu úkolu a uživatelských preferencí.
- Aplikovali naučené úpravy na základě historické výkonnosti k optimalizaci parametrů vzorkování.
- Zaznamenali výkonnost pro budoucí úpravy, což umožňuje systému učit se z minulých interakcí.
- Odeslali požadavky s dynamicky nakonfigurovanými parametry vzorkování a vrátili generovaný text spolu s použitými parametry a detekovaným typem úkolu.
- Použili:
    - `userPreferences` k umožnění přizpůsobení parametrů vzorkování na základě uživatelem definovaných úrovní kreativity, přesnosti a konzistence.
    - `detectTaskType` k určení povahy úkolu na základě promptu, což umožňuje více přizpůsobené odpovědi.
    - `recordPerformance` k zaznamenání výkonnosti generovaných odpovědí, což systému umožňuje přizpůsobovat se a zlepšovat v čase.
    - `applyLearnedAdjustments` k úpravě parametrů vzorkování na základě historické výkonnosti, čímž se zlepšuje schopnost modelu generovat vysoce kvalitní odpovědi.
    - `generateResponse` k zabalení celého procesu generování odpovědi s adaptivním vzorkováním, což usnadňuje volání s různými prompty a kontexty.
    - `allowedTools` k určení, které nástroje může model během generování použít, což umožňuje více kontextově uvědomělé odpovědi.
    - `feedbackScore` k umožnění uživatelům poskytovat zpětnou vazbu na kvalitu generované odpovědi, kterou lze použít k dalšímu zdokonalení výkonu modelu v čase.
    - `performanceHistory` k uchovávání záznamů o minulých interakcích, což systému umožňuje učit se z předchozích úspěchů a neúspěchů.
    - `getSamplingParameters` k dynamickému přizpůsobení parametrů vzorkování na základě kontextu požadavku, což umožňuje flexibilnější a reaktivnější chování modelu.
    - `detectTaskType` k zařazení úkolu na základě promptu, což systému umožňuje aplikovat vhodné strategie vzorkování pro různé typy požadavků.
    - `samplingProfiles` k definování základních konfigurací vzorkování pro různé typy úkolů, což umožňuje rychlé úpravy na základě povahy požadavku.

---

## Co bude dál

- [5.7 Škálování](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
> [!WARNING]
> A mintavételezés elavult az MCP `2026-07-28` verziójában. Ez a lecke a
> régi megvalósítások miatt maradt meg. Az új szervereknek közvetlenül egy LLM
> szolgáltató API-jával kell integrálódniuk.

# Mintavételezés a Model Context Protocol-ban

> A mintavételezés továbbra is része a `2026-07-28` specifikációnak a kompatibilitás érdekében, és
> eltávolítható az első, 2027. július 28-a utáni revízióban. A leckében szereplő példák az
> SDK API-kat használhatják, amelyek a `2025-11-25` verziót valósítják meg.
> Lásd: [Mi változott az MCP-ben: A 2026-07-28 specifikáció](../../01-CoreConcepts/mcp-2026-07-28.md).

A régi MCP megvalósításokban a mintavételezés lehetővé teszi a szerverek számára, hogy
LLM kéréseket kezdeményezzenek az ügyfélen keresztül. Ez a lecke elmagyarázza ezt az
elavult protokollt a kompatibilitás és a migráció érdekében.

## Bevezetés

Ebben a leckében megvizsgáljuk, hogyan kell konfigurálni a mintavételezési paramétereket MCP kérésekben, és megértjük a mintavételezés mögötti protokollmechanikát.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni az MCP-ben elérhető kulcsfontosságú mintavételezési paramétereket.
- Különböző használati esetekhez konfigurálni a mintavételezési paramétereket.
- Determinisztikus mintavételezést megvalósítani az ismételhető eredményekhez.
- Dinamikusan állítani a mintavételezési paramétereket a kontextus és a felhasználói preferenciák alapján.
- Mintavételezési stratégiákat alkalmazni a modell teljesítményének javításához különféle helyzetekben.
- Megérteni, hogyan működik a mintavételezés az MCP kliens-szerver folyamatában.

## Hogyan működik a mintavételezés az MCP-ben

Az MCP mintavételezési folyamata a következő lépéseket követi:

1. A szerver elküld egy `sampling/createMessage` kérést az ügyfélnek
2. Az ügyfél átvizsgálja a kérést és módosíthatja azt
3. Az ügyfél mintavételez egy LLM-ből
4. Az ügyfél átvizsgálja a kimenetet
5. Az ügyfél visszaküldi az eredményt a szervernek

Ez az emberi felügyeletet tartalmazó tervezés biztosítja, hogy a felhasználók irányításuk alatt tartsák, mit lát és generál az LLM.

## Mintavételezési paraméterek áttekintése

Az MCP a következő mintavételezési paramétereket definiálja, melyeket be lehet állítani a kliens kérésekben:

| Paraméter | Leírás | Tipikus értéktartomány |
|-----------|-------------|---------------|
| `temperature` | A véletlenszerűség vezérlése a token kiválasztásban | 0,0 - 1,0 |
| `maxTokens` | A generált tokenek maximum száma | Egész szám |
| `stopSequences` | Egyedi szekvenciák, amelyek megállítják a generálást, ha előfordulnak | Karakterlánc tömb |
| `metadata` | További, szolgáltató-specifikus paraméterek | JSON objektum |

Számos LLM szolgáltató további paramétereket támogat a `metadata` mezőn keresztül, például:

| Gyakori kiegészítő paraméter | Leírás | Tipikus értéktartomány |
|-----------|-------------|---------------|
| `top_p` | Nucleus mintavételezés - a tokeneket a top kumulatív valószínűség korlátozza | 0,0 - 1,0 |
| `top_k` | Token kiválasztást korlátozza a legjobb K lehetőségre | 1 - 100 |
| `presence_penalty` | Bünteti a tokeneket a szövegben való megjelenésük alapján | -2,0 - 2,0 |
| `frequency_penalty` | Bünteti a tokeneket a szövegben való előfordulási gyakoriságuk alapján | -2,0 - 2,0 |
| `seed` | Specifikus véletlenszám-generátor mag az ismételhető eredményekhez | Egész szám |

## Példa kérés formátumra

Íme egy példa arra, hogyan kérhetünk mintavételezést egy MCP kliensből:

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

## Válasz formátum

Az ügyfél egy befejezést ad vissza:

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

## Ember a folyamatban vezérlések

Az MCP mintavételezés emberi felügyelet mellett készült:

- **Kérések esetén**:
  - Az ügyfelek meg kell, hogy mutassák a javasolt kérést a felhasználóknak
  - A felhasználók módosíthatják vagy elutasíthatják a kéréseket
  - A rendszerüzenetek szűrhetők vagy módosíthatók
  - A kontextus bevonása az ügyfélnél kontrollált

- **Befejezések esetén**:
  - Az ügyfelek meg kell, hogy mutassák a befejezést a felhasználóknak
  - A felhasználók módosíthatják vagy elutasíthatják a befejezéseket
  - Az ügyfelek szűrhetik vagy módosíthatják a befejezéseket
  - A felhasználók szabályozzák, mely modell kerül használatra

Ezekkel az elvekkel az MCP mintavételezés megvalósítása különböző programozási nyelvekben következik, fókuszálva az LLM szolgáltatók által általánosan támogatott paraméterekre.

## Biztonsági szempontok

Az MCP mintavételezés megvalósításakor vegyük figyelembe az alábbi biztonsági legjobb gyakorlatokat:

- **Ellenőrizzük az összes üzenet tartalmát** mielőtt elküldjük az ügyfélnek
- **Tisztítsuk meg az érzékeny információkat** a kérésekből és befejezésekből
- **Valósítsunk meg korlátozásokat** az abúzus megelőzése érdekében
- **Figyeljük a mintavételezés használatát** a szokatlan minták azonosítására
- **Titkosítsuk az adatátvitelt** biztonságos protokollokkal
- **Kezeljük a felhasználói adatvédelmet** a vonatkozó szabályozásoknak megfelelően
- **Auditáljuk a mintavételezési kérelmeket** a megfelelőség és biztonság érdekében
- **Szabályozzuk a költségkitettséget** megfelelő korlátokkal
- **Valósítsunk meg időkorlátokat** a mintavételezési kérésekhez
- **Kezeljük a modellhibákat** megfelelő tartalék megoldásokkal

A mintavételezési paraméterek lehetővé teszik a nyelvi modellek viselkedésének finomhangolását, hogy megvalósítható legyen a determinisztikus és kreatív kimenetek kívánt egyensúlya.

Nézzük meg, hogyan állíthatók be ezek a paraméterek különböző programozási nyelvekben.

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

A korábbi kódban:

- Létrehoztunk egy MCP klienst egy adott szerver URL-lel.
- Beállítottunk egy kérést mintavételezési paraméterekkel, például `temperature`, `top_p`, és `top_k`.
- Elküldtük a kérést, majd kiírtuk a generált szöveget.
- Használtuk:
    - Az `allowedTools` paramétert, hogy meghatározzuk, mely eszközöket használhatja a modell a generáláshoz. Ebben az esetben engedélyeztük az `ideaGenerator` és `marketAnalyzer` eszközöket a kreatív alkalmazás ötletek generálásához.
    - A `frequencyPenalty` és `presencePenalty` paramétereket a kimenet ismétlésének és sokszínűségének szabályozására.
    - A `temperature` paramétert a kimenet véletlenszerűségének vezérlésére, ahol a magasabb értékek kreatívabb válaszokat eredményeznek.
    - A `top_p` paramétert a tokenek kiválasztásának korlátozására az összesített legjobb valószínűség alapján a generált szöveg minőségének javításához.
    - A `top_k` paramétert, hogy a modellt a legvalószínűbb K tokenre korlátozzuk, ami segítheti az összefüggőbb válaszok előállítását.
    - A `frequencyPenalty` és `presencePenalty` paramétereket az ismétlődés csökkentésére és a sokszínűséget előmozdító kimenet érdekében.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript példa: Hőmérséklet és Top-P mintavételezési konfiguráció
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP kliens inicializálása
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Kérés konfigurálása különböző mintavételezési paraméterekkel
  const creativeSampling = {
    temperature: 0.9,    // Magasabb hőmérséklet = több véletlenszerűség/kreativitás
    topP: 0.92,          // A tokeneket a legvalószínűbb 92%-os valószínűségi tömeg alapján figyelembe véve
    frequencyPenalty: 0.6, // A token sorozatok ismétlődésének csökkentése
    presencePenalty: 0.4   // Büntesd az eddig a szövegben megjelent tokeneket
  };
  
  const factualSampling = {
    temperature: 0.2,    // Alacsonyabb hőmérséklet = inkább determinisztikus/tényalapú
    topP: 0.85,          // Enyhén fókuszáltabb token kiválasztás
    frequencyPenalty: 0.2, // Minimális ismétlődési büntetés
    presencePenalty: 0.1   // Minimális jelenlét büntetés
  };
  
  try {
    // Két kérés küldése különböző mintavételezési konfigurációkkal
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

A korábbi kódban:

- Inicializáltunk egy MCP klienst szerver URL-lel és API kulccsal.
- Két külön mintavételezési paraméterkészletet konfiguráltunk: egyet kreatív feladatokhoz, egyet tényalapú feladatokhoz.
- Elküldtük a kéréseket ezekkel a beállításokkal, lehetővé téve, hogy a modell adott eszközöket használjon minden feladathoz.
- Kiírtuk a generált válaszokat, hogy bemutassuk a különböző mintavételezési paraméterek hatását.
- Használtuk az `allowedTools` paramétert, hogy meghatározzuk, mely eszközöket használhat a modell a generálás során. Ebben az esetben a kreatív feladatokhoz az `ideaGenerator` és az `environmentalImpactTool` eszközöket engedélyeztük, míg a tényalapú feladatokhoz a `factChecker` és a `dataAnalysisTool` eszközöket.
- Használtuk a `temperature` paramétert a kimenet véletlenszerűségének vezérlésére, ahol a magasabb értékek kreatívabb válaszokat eredményeznek.

- A `top_p` használata annak korlátozására, hogy csak azok a tokenek kerüljenek kiválasztásra, amelyek a legnagyobb kumulatív valószínűségi tömeghez járulnak hozzá, ezzel növelve a generált szöveg minőségét.
- A `frequencyPenalty` és `presencePenalty` használata az ismétlések csökkentésére és a kimenet diverzitásának ösztönzésére.
- A `top_k` használata a modell korlátozására az top K legvalószínűbb tokenre, amely segíthet koherensebb válaszok generálásában.

---

## Determinisztikus mintavételezés

Olyan alkalmazásoknál, ahol következetes kimenetek szükségesek, a determinisztikus mintavételezés garantálja az ismételhető eredményeket. Ezt úgy éri el, hogy fix véletlenszerű magot (seed) használ, és a hőmérsékletet nullára állítja.

Nézzük meg az alábbi mintakódot, amely különböző programozási nyelveken mutatja be a determinisztikus mintavételezést.

# [Java](#tab/java)

```java
// Java példa: Determinisztikus válaszok rögzített maggal
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Rögzített mag használata determinisztikus eredményekhez
        
        // Első kérés rögzített maggal
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nulla hőmérséklet a maximális determinisztikusságért
            .build();
            
        // Második kérés ugyanazzal a maggal
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Mindkét kérés végrehajtása
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // A válaszoknak azonosaknak kell lenniük a ugyanaz a mag és hőmérséklet=0 miatt
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Az előző kódban:

- Létrehoztunk egy MCP klienst egy megadott szerver URL-lel.
- Beállítottunk két kérést ugyanazzal a prompttal, fix seeddel és nulla hőmérséklettel.
- Mindkét kérést elküldtük, és kiírtuk a generált szöveget.
- Megmutattuk, hogy a válaszok azonosak a mintavételezés konfigurációja miatt (ugyanaz a seed és hőmérséklet).
- A `setSeed` használatával meghatároztuk a fix véletlenszerű magot, biztosítva, hogy a modell mindig ugyanazt a kimenetet generálja ugyanarra a bemenetre.
- A `temperature` értékét nullára állítottuk, hogy maximális determinizmust érjünk el, vagyis a modell mindig a legvalószínűbb következő tokent választja véletlenszerűség nélkül.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript példa: Determinisztikus válaszok magvezérléssel
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Első kérés rögzített maggal
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nulla hőmérséklet a maximális determinisztikusságért
    });
    
    // Második kérés ugyanazzal a maggal és hőmérséklettel
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Harmadik kérés különböző maggal, de ugyanazzal a hőmérséklettel
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

Az előző kódban:

- Inicializáltunk egy MCP klienst egy szerver URL-lel.
- Két kérést konfiguráltunk ugyanazzal a prompttal, fix seeddel és nulla hőmérséklettel.
- Mindkét kérést elküldtük, és kiírtuk a generált szöveget.
- Megmutattuk, hogy a válaszok azonosak a mintavételezés determinisztikus jellege miatt (ugyanaz a seed és hőmérséklet).
- A `seed` használatával meghatároztuk a fix véletlenszerű magot, biztosítva, hogy a modell mindig ugyanazt a kimenetet generálja ugyanarra a bemenetre.
- A `temperature` értékét nullára állítottuk, hogy maximális determinizmust érjünk el, vagyis a modell mindig a legvalószínűbb következő tokent választja véletlenszerűség nélkül.
- A harmadik kéréshez másik seedet használtunk, hogy megmutassuk, a seed megváltoztatása eltérő kimenetet eredményez, még ugyanazzal a prompttal és hőmérséklettel.

---

## Dinamikus mintavételezési konfiguráció

Az intelligens mintavételezés a paramétereket az egyes kérések kontextusa és követelményei alapján igazítja. Ez azt jelenti, hogy dinamikusan állítjuk be a hőmérsékletet, top_p-t és a büntetéseket a feladat típusa, a felhasználói preferenciák vagy a korábbi teljesítmény alapján.

Nézzük meg, hogyan valósítható meg a dinamikus mintavételezés különböző programozási nyelveken.

# [Python](#tab/python)

```python
# Python példa: Dinamikus mintavételezés a kérés kontextusa alapján
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Mintavételi előbeállítások definiálása különböző feladattípusokhoz
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Bázis előbeállítás kiválasztása
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Igény szerint felhasználói preferenciák alapján módosítás
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Hőmérséklet skálázása a kreativitás preferencia alapján (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # top_p módosítása a kívánt válaszdiverzitás alapján
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Egyéni mintavételi paraméterekkel kérés létrehozása és küldése
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Válasz visszaadása mintavételi metaadatokkal a átláthatóság érdekében
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Az előző kódban:

- Létrehoztunk egy `DynamicSamplingService` osztályt, amely az adaptív mintavételezést kezeli.
- Meghatároztunk mintavételezési előbeállításokat különböző feladattípusokhoz (kreatív, tényalapú, kód, analitikus).
- Kiválasztottunk egy alap mintavételezési előbeállítást a feladattípus alapján.
- A felhasználói preferenciák (például kreativitás szintje és diverzitás) alapján beállítottuk a mintavételezési paramétereket.
- Elküldtük a kérést a dinamikusan konfigurált mintavételezési paraméterekkel.
- Visszaadtuk a generált szöveget a használt mintavételezési paraméterekkel és a feladattípussal együtt átláthatóság céljából.
- A `temperature` a kimenet véletlenszerűségének szabályozására szolgált, ahol magasabb értékek kreatívabb válaszokhoz vezetnek.
- A `top_p` használata korlátozta a tokenek kiválasztását azok alapján, amelyek a legnagyobb kumulatív valószínűségi tömeghez járulnak hozzá, ezzel javítva a generált szöveg minőségét.
- A `frequency_penalty` csökkentette az ismétléseket és ösztönözte a diverzitást a kimenetben.
- A `user_preferences` engedélyezte a mintavételezési paraméterek testreszabását a felhasználó által meghatározott kreativitás és diverzitás szintek alapján.
- A `task_type` meghatározta a megfelelő mintavételezési stratégiát a kéréshez, lehetővé téve személyre szabottabb válaszokat a feladat jellegének megfelelően.
- A `send_request` metódus használatával elküldtük a promptot a konfigurált mintavételezési paraméterekkel, biztosítva, hogy a modell a megadott követelmények szerint generáljon szöveget.
- A `generated_text`-tel lekértük a modell válaszát, amelyet visszaadtunk együtt a mintavételezési paraméterekkel és a feladattípussal további elemzés vagy megjelenítés céljából.
- A `min` és `max` függvényeket használtuk, hogy a felhasználói preferenciák érvényes tartományba szoruljanak, megelőzve érvénytelen mintavételezési konfigurációkat.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript példa: Dinamikus mintavételi konfiguráció felhasználói kontextus alapján
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Alap mintavételi profilok meghatározása
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Történelmi teljesítmény követése
    this.performanceHistory = [];
  }
  
  // Feladattípus felismerése a prompt alapján
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Egyszerű heuristikus felismerés - gépi tanulási osztályozással tovább fejleszthető
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
    
    // Alapértelmezettként beszélgetős mód, ha nincs egyértelmű típus felismerve
    return 'conversational';
  }
  
  // Mintavételi paraméterek kiszámítása kontextus és felhasználói preferenciák alapján
  getSamplingParameters(prompt, context = {}) {
    // A feladat típusának felismerése
    const taskType = this.detectTaskType(prompt, context);
    
    // Alapprofil lekérése
    let params = {...this.samplingProfiles[taskType]};
    
    // Felhasználói preferenciák szerinti beállítás
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Átméretezés 1-10 között a megfelelő hőmérsékleti tartományra
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Magasabb pontosság alacsonyabb topP-t jelent (fókuszáltabb kiválasztás)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Magasabb konzisztencia alacsonyabb büntetést jelent
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // A teljesítménytörténetből tanult korrekciók alkalmazása
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Egyszerű adaptív logika - fejlettebb algoritmusokkal tovább fejleszthető
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Csak a legutóbbi történelem figyelembevétele
    
    if (relevantHistory.length > 0) {
      // Átlagos teljesítményértékek kiszámítása
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Ha a teljesítmény a küszöb alatt van, paraméterek módosítása
      if (avgScore < 0.7) {
        // Enyhe korrekció biztonságosabb értékek felé
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Teljesítmény rögzítése jövőbeli módosításokhoz
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 közötti értékelés a válasz minőségére
    });
    
    // Történetméret korlátozása
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Optimalizált mintavételi paraméterek lekérése
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Kérés küldése optimalizált paraméterekkel
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Ha a felhasználó visszajelzést ad, rögzítse azt a jövőbeli optimalizáláshoz
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

// Használati példa
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreatív feladat egyedi felhasználói preferenciákkal
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Magas kreativitás (1-10)
          consistency: 3  // Alacsony konzisztencia (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Kódgenerálási feladat
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Alacsony kreativitás
          precision: 8,   // Magas pontosság
          consistency: 9  // Magas konzisztencia
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

Az előző kódban:

- Létrehoztunk egy `AdaptiveSamplingManager` osztályt, amely kezeli a dinamikus mintavételezést a feladattípus és a felhasználói preferenciák alapján.
- Meghatároztunk mintavételezési profilokat különböző feladattípusokhoz (kreatív, tényalapú, kód, beszélgetés).
- Implementáltunk egy metódust, amely egyszerű heurisztikák alapján felismeri a feladattípust a promptból.
- Kiszámoltuk a mintavételezési paramétereket a felismert feladattípus és a felhasználói preferenciák alapján.
- Alkalmaztunk tanult beállításokat a korábbi teljesítmény alapján a mintavételezési paraméterek optimalizálására.
- Rögzítettük a teljesítményt a jövőbeni beállításokhoz, lehetővé téve, hogy a rendszer tanuljon a múltbeli interakciókból.
- Dinamikusan konfigurált mintavételezési paraméterekkel küldtünk kéréseket és visszaadtuk a generált szöveget az alkalmazott paraméterekkel és a felismert feladattípussal együtt.
- Használtuk:
    - `userPreferences` a mintavételezési paraméterek testreszabására a felhasználó által meghatározott kreativitás, pontosság és következetesség szintek alapján.
    - `detectTaskType` a feladat jellegének meghatározására a prompt alapján, lehetővé téve személyre szabottabb válaszokat.
    - `recordPerformance` a generált válaszok teljesítményének naplózására, amely lehetővé teszi a rendszer számára az alkalmazkodást és fejlődést idővel.
    - `applyLearnedAdjustments` a mintavételezési paraméterek módosítására a korábbi teljesítmény alapján, javítva a modell képességét a magas minőségű válaszok generálására.
    - `generateResponse` a teljes válaszgenerálási folyamat kapszulázására adaptív mintavételezéssel, megkönnyítve a hívást különböző promptokkal és kontextusokkal.
    - `allowedTools` annak meghatározására, hogy mely eszközöket használhatja a modell a generálás közben, lehetővé téve kontextusérzékenyebb válaszokat.
    - `feedbackScore` a felhasználók számára, hogy visszajelzést adjanak a generált válasz minőségéről, amelyet a modell teljesítményének további finomhangolására használhatnak idővel.
    - `performanceHistory` a múltbeli interakciók nyilvántartására, lehetővé téve, hogy a rendszer tanuljon korábbi sikerekből és kudarcokból.
    - `getSamplingParameters` a mintavételezési paraméterek dinamikus igazítására a kérés kontextusa alapján, rugalmasabb és reagálóképesebb modellviselkedés érdekében.
    - `detectTaskType` a feladattípus osztályozására a prompt alapján, lehetővé téve, hogy a rendszer megfelelő mintavételezési stratégiákat alkalmazzon a különböző típusú kérésekhez.
    - `samplingProfiles` az alap mintavételezési konfigurációk meghatározására különböző feladattípusokhoz, gyors beállításokat engedve a kérés jellegének megfelelően.

---

## Mi következik

- [5.7 Méretezés](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
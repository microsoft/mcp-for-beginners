> [!WARNING]
> Mäluvõtmine on MCP `2026-07-28` versioonis aegunud. Seda õppust säilitatakse
> pärandrakenduste jaoks. Uued serverid peaksid integreerima otse LLM
> pakkuja API-ga.

# Mäluvõtmine Mudeli Konteksti Protokollis

> Mäluvõtmine jääb alles `2026-07-28` spetsifikatsiooni ühilduvuse tagamiseks ning võib
> esmase ülevaatuse käigus, mis toimub 28. juulil 2027 või pärast seda, eemaldada.
> Selle õppetunni näited võivad kasutada SDK API-sid, mis rakendavad `2025-11-25`.
> Vaata [Mis on MCP-s muutunud: 2026-07-28 spetsifikatsioon](../../01-CoreConcepts/mcp-2026-07-28.md).

Pärand MCP rakendustes võimaldab Mäluvõtmine serveritel päringuid teha LLM
täitmiseks kliendi kaudu. See õppetund selgitab aegunud protokolli
voogu ühilduvuse ja migratsioonitöö jaoks.

## Sissejuhatus

Selles õppetükis uurime, kuidas konfigureerida mäluvõtu parameetreid MCP päringutes ning mõista mäluvõtu protokolli põhimõtteid.

## Õpieesmärgid

Selle õppetunni lõpuks saad:

- Mõista MCP-s saadaolevaid peamisi mäluvõtu parameetreid.
- Konfigureerida mäluvõtu parameetreid erinevate kasutusjuhtude jaoks.
- Rakendada deterministlikku mäluvõttu korduvate tulemuste saavutamiseks.
- Dünaamiliselt reguleerida mäluvõtu parameetreid vastavalt kontekstile ja kasutaja eelistustele.
- Rakendada mäluvõtu strateegiaid mudeli jõudluse parandamiseks eri olukordades.
- Mõista, kuidas mäluvõtt toimib MCP kliendi-serveri voos.

## Kuidas Mäluvõtt MCP-s Töötab

Mäluvõtu voog MCP-s järgib neid samme:

1. Server saadab kliendile `sampling/createMessage` päringu
2. Klient vaatab päringu üle ja võib seda muuta
3. Klient võtab valimi LLM-ist
4. Klient vaatab täitmise üle
5. Klient tagastab tulemuse serverile

See inimsekkumisega disain tagab, et kasutajad säilitavad kontrolli selle üle, mida LLM näeb ja genereerib.

## Mäluvõtu Parameetrite Ülevaade

MCP määratleb järgmised mäluvõtu parameetrid, mida saab kliendi päringutes konfigureerida:

| Parameeter | Kirjeldus | Tavapärane Vahemik |
|-----------|-------------|---------------|
| `temperature` | Kontrollib juhuslikkust tokeni valikus | 0.0 - 1.0 |
| `maxTokens` | Maksimaalne genereeritavate tokenite arv | Täisarvuline väärtus |
| `stopSequences` | Kohandatud jadad, mis peatavad genereerimise kokkupuutel | Märgistringide massiiv |
| `metadata` | Täiendavad pakkujapõhised parameetrid | JSON objekt |

Paljud LLM pakkujad toetavad täiendavaid parameetreid `metadata` väljale, mis võivad sisaldada:

| Levinud Laienduse Parameeter | Kirjeldus | Tavapärane Vahemik |
|-----------|-------------|---------------|
| `top_p` | Tuumavõtt - piirab tokenite valikut tipptõenäosusega | 0.0 - 1.0 |
| `top_k` | Piirab tokenite valiku kõrgeimate K valikuteni | 1 - 100 |
| `presence_penalty` | Karistab tokeneid nende esinemise põhjal tekstis seni | -2.0 - 2.0 |
| `frequency_penalty` | Karistab tokeneid nende sageduse põhjal tekstis seni | -2.0 - 2.0 |
| `seed` | Kindel juhuslik seeme korduvate tulemuste jaoks | Täisarvuline väärtus |

## Näidis Päringu Vorming

Siin on näide, kuidas teha MCP-s kliendi kaudu mäluvõtu päring:

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

## Vastuse Vorming

Klient tagastab täitmise tulemuse:

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

## Inimene Sees tsüklis Kontrollid

MCP mäluvõtt on disainitud inimliku järelevalvega:

- **Sõnumite puhul**:
  - Kliendid peaksid kasutajatele näitama ettepanekut
  - Kasutajad peaksid saama sõnumit muuta või tagasi lükata
  - Süsteemisõnumeid võib filtreerida või muuta
  - Konteksti lisamine on kliendi kontrolli all

- **Täitmiste puhul**:
  - Kliendid peaksid kasutajatele näitama täitmist
  - Kasutajad peaksid saama täitmisi muuta või tagasi lükata
  - Kliendid võivad täitmisi filtreerida või muuta
  - Kasutajad kontrollivad, millist mudelit kasutatakse

Neid põhimõtteid silmas pidades vaatame, kuidas rakendada mäluvõttu erinevates programmeerimiskeeltes, keskendudes parameetritele, mida sageli toetavad kõigi LLM pakkujad.

## Turvaküsimused

MCP-s mäluvõtu rakendamisel kaalu selliseid turvalisuse parimaid tavasid:

- **Kinnita kogu sõnumi sisu** enne saatmist kliendile
- **Puhasta tundlik info** sõnumitest ja täitmistest
- **Rakenda piirmäärasid** kuritarvituste vältimiseks
- **Jälgi mäluvõtu kasutust** ebaharilike mustrite tuvastamiseks
- **Krüpteeri andmed edastamisel** turvaliste protokollidega
- **Käsitle kasutajaandmete privaatsust** vastavalt kehtivatele regulatsioonidele
- **Auditõpi mäluvõtu päringuid** vastavuse ja turvalisuse tagamiseks
- **Kontrolli kulutuste ulatust** asjakohaste piirangutega
- **Rakenda taimerid** mäluvõtu päringutele
- **Käsitle mudeli vigu elegantseks** asjakohaste varuplaanidega

Mäluvõtu parameetrid võimaldavad täpselt seadistada keelemudelite käitumist, et saavutada soovitud tasakaal deterministlike ja loominguliste väljundite vahel.

Vaatame, kuidas neid parameetreid seadistada eri programmeerimiskeeltes.

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

Eelnevas koodis me oleme:

- Loonud MCP kliendi konkreetse serveri URL-iga.
- Konfigureerinud päringu mäluvõtu parameetritega nagu `temperature`, `top_p` ja `top_k`.
- Saatnud päringu ja väljastanud genereeritud teksti.
- Kasutanud:
    - `allowedTools` määrab, milliseid tööriistu mudel saab genereerimise ajal kasutada. Selles näites lubasime `ideaGenerator` ja `marketAnalyzer` tööriistad aidata loominguliste rakendusideede loomisel.
    - `frequencyPenalty` ja `presencePenalty` korduste ja mitmekesisuse kontrollimiseks väljundis.
    - `temperature` juhuslikkuse kontrollimiseks, kus kõrgemad väärtused toovad kaasa loomingulisemad vastused.
    - `top_p` piirab tokenite valikut nendele, mis annavad kumulatiivse tõenäosuse tipu, parandades genereeritud teksti kvaliteeti.
    - `top_k` piirab mudeli valikut kõrgeimate tõenäosustega tokenitele, aidates toota koherentsemaid vastuseid.
    - `frequencyPenalty` ja `presencePenalty` korduste vähendamiseks ja mitmekesisuse soodustamiseks genereeritud tekstis.

# [JavaScript](#tab-javascript)

```javascript
// JavaScript Näide: Temperatuuri ja Top-P valimi konfiguratsioon
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Algatage MCP klient
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigureerige päring erinevate valimiparameetritega
  const creativeSampling = {
    temperature: 0.9,    // Kõrgem temperatuur = rohkem juhuslikkust/loovust
    topP: 0.92,          // Võtke arvesse tipp-92% tõenäosusmassiga tokeneid
    frequencyPenalty: 0.6, // Vähendage tokenijadade kordusi
    presencePenalty: 0.4   // Karistage tokeneid, mis on tekstis seni ilmunud
  };
  
  const factualSampling = {
    temperature: 0.2,    // Madalam temperatuur = täpsem/tegelikum
    topP: 0.85,          // Veidi rohkem keskendunud tokeni valik
    frequencyPenalty: 0.2, // Minimaalne korduste karistus
    presencePenalty: 0.1   // Minimaalne esinemise karistus
  };
  
  try {
    // Saatke kaks päringut erinevate valimikonfiguratsioonidega
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

Eelnevas koodis me oleme:

- Initsialiseerinud MCP kliendi serveri URL-i ja API võtmega.
- Konfigureerinud kaks mäluvõtu parameetrite komplekti: ühe loominguliste ülesannete ja teise faktipõhiste ülesannete jaoks.
- Saatnud päringuid nende konfiguratsioonidega, võimaldades mudelil kasutada konkreetseid tööriistu iga ülesande jaoks.
- Väljastasime genereeritud vastused, et demonstreerida erinevate mäluvõtu parameetrite mõju.
- Kasutasime `allowedTools` määramaks, milliseid tööriistu mudel võib genereerimise ajal kasutada. Selles kontekstis lubati loominguliste ülesannete jaoks `ideaGenerator` ja `environmentalImpactTool`, faktipõhiste ülesannete jaoks `factChecker` ja `dataAnalysisTool`.
- Kasutasime `temperature` väljundi juhuslikkuse kontrollimiseks, kus kõrgemad väärtused toovad kaasa loomingulisemad vastused.
- Kasutasime `top_p` piiramaks tokenite valikut nendele, mis moodustavad kõrgeima kumulatiivse tõenäosuse massi, parandades genereeritud teksti kvaliteeti.
- Kasutasime `frequencyPenalty` ja `presencePenalty` korduste vähendamiseks ja mitmekesisuse julgustamiseks väljundis.
- Kasutasime `top_k` mudeli piiramiseks tõenäolisemate K tokenite hulka, aidates parandada vastuste koherentsust.

---

## Deterministlik Mäluvõtt

Rakenduste jaoks, mis vajavad järjepidevaid väljundeid, tagab deterministlik mäluvõtt korduvate tulemuste saavutamise. Seda tehakse, kasutades fikseeritud juhuslikku seemet ja temperatuuri väärtust null.

Vaatame allpool näidisrakendust, mis demonstreerib deterministlikku mäluvõttu erinevates programmeerimiskeeltes.

# [Java](#tab-java)

```java
// Java näide: Deterministlikud vastused fikseeritud seemnega
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Deterministlike tulemite saavutamiseks fikseeritud seemne kasutamine
        
        // Esimene päring fikseeritud seemnega
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Maksimaalse determinismi jaoks null temperatuur
            .build();
            
        // Teine päring sama seemnega
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Mõlema päringu täitmine
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Vastused peaksid olema identsed sama seemne ja temperatuuriga 0 tõttu
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Eelnevas koodis me oleme:

- Loonud MCP kliendi määratud serveri URL-iga.
- Konfigureerinud kaks päringut sama sõnumiga, fikseeritud seemne ja null temperatuuri väärtusega.
- Saatnud mõlemad päringud ja väljastanud genereeritud teksti.
- Demonstreerinud, et vastused on identsed tänu deterministlikule mäluvõtu konfiguratsioonile (sama seeme ja temperatuur).
- Kasutanud `setSeed` kindla juhusliku seemne määramiseks, tagades mudeli sama väljundi iga kord sama sisendi korral.
- Seatud `temperature` nulli, et tagada maksimaalne determinism, mis tähendab, et mudel valib alati kõige tõenäolisema järgmise tokeni ilma juhuslikkuseta.

# [JavaScript](#tab-javascript-deterministic)

```javascript
// JavaScript näide: deterministlikud vastused seemnekontrolliga
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Esimene päring fikseeritud seemnega
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Null temperatuuri maksimaalseks determinismiks
    });
    
    // Teine päring sama seemne ja temperatuuriga
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Kolmas päring erineva seemnega, kuid sama temperatuuriga
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

Eelnevas koodis me oleme:

- Initsialiseerinud MCP kliendi serveri URL-iga.
- Konfigureerinud kaks päringut sama sõnumi, fikseeritud seemne ja null temperatuuri väärtusega.
- Saatnud mõlemad päringud ja väljastanud genereeritud teksti.
- Demonstreerinud, et vastused on identsed tänu deterministlikule mäluvõtu konfiguratsioonile (sama seeme ja temperatuur).
- Kasutanud `seed` kindla juhusliku seemne määramiseks, tagades mudelile sama väljundi iga identse sisendi korral.
- Seatud `temperature` nulli maksimaalse determinismi tagamiseks, nii et mudel valib alati kõige tõenäolisema järgmise tokeni.
- Kasutanud erinevat seemet kolmandal päringul, et näidata, et seemne muutmine annab eri väljundid, isegi kui sõnum ja temperatuur on samad.

---

## Dünaamiline Mäluvõtu Konfiguratsioon

Intelligentsed mäluvõtu parameetrid kohanduvad dünaamiliselt iga päringu konteksti ja nõudmiste põhjal. See tähendab mäluvõtu parameetrite nagu temperature, top_p ja karistuste kohandamist vastavalt ülesande tüübile, kasutaja eelistustele või ajaloolisele jõudlusele.

Vaatame, kuidas rakendada dünaamilist mäluvõttu eri programmeerimiskeeltes.

# [Python](#tab-python)

```python
# Python näide: dünaamiline proovivõtt päringu konteksti põhjal
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Määra proovivõtu eelseaded erinevate tööülesannete tüüpidele
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Vali baas-eelseade
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Kohanda kasutaja eelistuste põhjal, kui need on esitatud
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skaaleeri temperatuur loomingulisuse eelistuse põhjal (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Kohanda top_p soovitud vastuse mitmekesisuse põhjal
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Loo ja saada päring kohandatud proovivõtuga parameetritega
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Tagasta vastus koos proovivõtu metaandmetega läbipaistvuse tagamiseks
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Eelnevas koodis me oleme:

- Loonud `DynamicSamplingService` klassi, mis haldab adaptiivset mäluvõttu.
- Määratlenud mäluvõtu eelseaded erinevatele ülesandeliikidele (loominguline, faktipõhine, kood, analüütiline).
- Valinud põhijoone mäluvõtu vastavalt ülesande tüübile.
- Kohandanud mäluvõtu parameetreid kasutaja eelistuste põhjal, nagu loovuse ja mitmekesisuse tasemed.
- Saatnud päringu dünaamiliselt konfigureeritud mäluvõtu parameetritega.
- Tagastanud genereeritud teksti koos rakendatud mäluvõtu parameetrite ja ülesande tüübiga läbipaistvuse huvides.
- Kasutanud `temperature` väljundi juhuslikkuse juhtimiseks, kus kõrgemad väärtused annavad loomingulisemad vastused.
- Kasutanud `top_p` piirama tokenite valikut nendele, mis moodustavad tipptõenäosuse massi, parandades genereeritud teksti kvaliteeti.
- Kasutanud `frequency_penalty` korduste vähendamiseks ja mitmekesisuse soodustamiseks kasutuses.
- Kasutanud `user_preferences` võimaldamaks mäluvõtu parameetrite kohandamist kasutaja määratud loovuse ja mitmekesisuse tasemete alusel.
- Kasutanud `task_type` sobiva mäluvõtu strateegia määramiseks päringu jaoks, võimaldades rohkem kohandatud vastuseid vastavalt ülesande olemusele.
- Kasutanud `send_request` meetodit märguande saatmiseks koos konfigureeritud mäluvõtu parameetritega, tagades mudelile soovitud nõuete kohase teksti genereerimise.
- Kasutanud `generated_text` mudeli vastuse kohta, mis tagastatakse koos mäluvõtu parameetrite ja ülesande kategooriaga täiendavaks analüüsiks või kuvamiseks.
- Kasutanud `min` ja `max` funktsioone, et hoida kasutaja eelistused kehtlikes piirides, vältides kehtetuid mäluvõtu seadistusi.

# [JavaScript Dünaamiline](#tab-javascript-dynamic)

```javascript
// JavaScripti näide: dünaamiline valimi konfiguratsioon kasutajakonteksti põhjal
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Määra baasvaliku profiilid
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Jälgi ajaloolist jõudlust
    this.performanceHistory = [];
  }
  
  // Tuleta ülesande tüüp vihje põhjal
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Lihtne heuristiline tuvastus - võiks täiendada ML klassifikatsiooniga
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
    
    // Vaikimisi vestluseks, kui selget tüüpi ei tuvastata
    return 'conversational';
  }
  
  // Arvuta valikuparameetrid konteksti ja kasutaja eelistuste põhjal
  getSamplingParameters(prompt, context = {}) {
    // Tuvasta ülesande tüüp
    const taskType = this.detectTaskType(prompt, context);
    
    // Hangi baasprofiil
    let params = {...this.samplingProfiles[taskType]};
    
    // Kohanda kasutaja eelistuste põhjal
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Skaala 1-10 sobivaks temperatuuri vahemikuks
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Kõrgem täpsus tähendab madalamat topP (fookustatud valik)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Kõrgem järjepidevus tähendab madalamaid karistusi
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Rakenda jõudlusajaloo põhjal õpitud kohandused
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Lihtne adaptiivne loogika - võiks täiendada keerukamate algoritmidega
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Arvesta ainult hiljutist ajalugu
    
    if (relevantHistory.length > 0) {
      // Arvuta keskmised jõudluse hinded
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Kui jõudlus on künnisest madalam, kohanda parameetreid
      if (avgScore < 0.7) {
        // Veidi kohanda turvalisemate väärtuste suunas
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Salvesta jõudlus tulevasteks kohandusteks
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 vastuse kvaliteedi hinnang
    });
    
    // Piira ajaloo suurust
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Hangi optimeeritud valikuparameetrid
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Saada päring optimeeritud parameetritega
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Kui kasutaja annab tagasisidet, salvesta see tulevaseks optimeerimiseks
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

// Näidiskasutus
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Loominguline ülesanne kohandatud kasutaja eelistustega
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Kõrge loovus (1-10)
          consistency: 3  // Madal järjepidevus (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Koodi genereerimise ülesanne
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Madal loovus
          precision: 8,   // Kõrge täpsus
          consistency: 9  // Kõrge järjepidevus
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

Eelnevas koodis me oleme:

- Loonud `AdaptiveSamplingManager` klassi, mis haldab dünaamilist mäluvõttu vastavalt ülesande tüübile ja kasutaja eelistustele.
- Määratlenud profiilid erinevateks ülesandetüüpideks (loominguline, faktipõhine, kood, vestlus).
- Rakendanud meetodi ülesandetüübi tuvastamiseks sõnumist lihtsate heuristikate abil.
- Arvutanud mäluvõtu parameetrid tuvastatud ülesandetüübi ja kasutaja eelistuste põhjal.
- Rakendanud ajalooliste tulemuste põhjal õpitud kohandusi, et optimeerida mäluvõtu parameetreid.
- Salvestanud tulemusi tulevaste kohanduste jaoks, võimaldades süsteemil õppida varasematest interaktsioonidest.
- Saatnud päringud dünaamiliselt konfigureeritud mäluvõtu parameetritega ja tagastanud genereeritud teksti koos rakendatud parameetrite ja ülesannetüübiga.
- Kasutatud:
    - `userPreferences` võimaldamaks mäluvõtu parameetrite kohandamist kasutaja määratud loovuse, täpsuse ja järjepidevuse tasemete alusel.
    - `detectTaskType` ülesande olemuse kindlakstegemiseks sõnumi põhjal, võimaldades kohandatumaid vastuseid.
    - `recordPerformance` genereeritud vastuste tulemuste logimiseks, võimaldades süsteemil kohanduda ja areneda aja jooksul.
    - `applyLearnedAdjustments` mäluvõtu parameetrite muutmiseks ajalooliste tulemuste põhjal, parandades mudeli suutlikkust toota kvaliteetseid vastuseid.
    - `generateResponse` kogu protsessi kapseldamiseks, võimaldades lihtsalt kutsuda vastust dünaamilise mäluvõtuga erinevate sõnumite ja kontekstide puhul.
    - `allowedTools` määramaks, milliseid tööriistu mudel genereerimisel kasutada saab, võimaldades kontekstitundlikumaid vastuseid.
    - `feedbackScore` kasutajate tagasiside võimaldamiseks genereeritud vastuse kvaliteedi kohta, mida saab kasutada mudeli jõudluse täiendavaks parandamiseks.
    - `performanceHistory` varasemate interaktsioonide andmete hoidmiseks, võimaldades süsteemil õppida varasematest õnnestumistest ja ebaõnnestumistest.
    - `getSamplingParameters` mäluvõtu parameetrite dünaamiliseks kohandamiseks päringu kontekstist lähtuvalt, võimaldades paindlikumat ja reageerivamat mudelikäitumist.
    - `detectTaskType` ülesande klassifitseerimiseks sõnumi põhjal, võimaldades süsteemil rakendada sobivaid mäluvõtu strateegiaid erinevatele päringu tüüpidele.
    - `samplingProfiles` põhiliste mäluvõtu seadistuste määratlemiseks eri ülesannetüüpidele, võimaldades kiireid kohandusi päringu olemusest lähtuvalt.

---

## Järgmised sammud

- [5.7 Skaalamine](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
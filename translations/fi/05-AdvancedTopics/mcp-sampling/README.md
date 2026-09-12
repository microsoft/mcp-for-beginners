> [!WARNING]
> Otanta on vanhentunut MCP:ssä `2026-07-28`. Tämä aihe säilytetään
> vanhojen toteutusten vuoksi. Uusien palvelimien tulisi integroitua suoraan LLM
> -toimittajan API:in.

# Otanta Model Context Protocolissa

> Otanta säilyy `2026-07-28` -määrittelyssä yhteensopivuuden varmistamiseksi ja sen
> poistaminen on mahdollista ensimmäisessä tarkistuksessa 28. heinäkuuta 2027 tai sen
> jälkeen julkaistussa versiossa. Tämän oppitunnin esimerkeissä voidaan käyttää SDK:n
> API:a, joka toteuttaa `2025-11-25`. Katso [Mitä MCP:ssä on muuttunut: 2026-07-28 määrittely](../../01-CoreConcepts/mcp-2026-07-28.md).

Legacy MCP -toteutuksissa otanta sallii palvelimien pyytää LLM:n täydennyksiä
asiakkaan kautta. Tässä oppitunnissa selitetään kyseinen vanhentunut protokollavirtaus
yhteensopivuuden ja siirtymisen tukemiseksi.

## Johdanto

Tässä oppitunnissa tutustumme, miten otantaparametrit määritetään MCP-pyynnöissä ja ymmärrämme otannan taustalla olevan protokollamekaniikan.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Ymmärtää MCP:ssä käytettävissä olevat tärkeät otantaparametrit.
- Määrittää otantaparametrit eri käyttötapauksia varten.
- Toteuttaa deterministinen otanta toistettaviin tuloksiin.
- Säätää otantaparametreja dynaamisesti kontekstin ja käyttäjäasetusten mukaan.
- Soveltaa otantastrategioita mallin suorituskyvyn parantamiseksi eri tilanteissa.
- Ymmärtää, miten otanta toimii client-server -virrassa MCP:ssä.

## Miten otanta toimii MCP:ssä

Otantaprosessi MCP:ssä etenee seuraavasti:

1. Palvelin lähettää `sampling/createMessage` pyynnön asiakkaalle
2. Asiakas tarkistaa pyynnön ja voi muokata sitä
3. Asiakas ottaa otoksen LLM:stä
4. Asiakas tarkistaa täydennyksen
5. Asiakas palauttaa tuloksen palvelimelle

Tämä ihmisen ohjaama suunnittelu varmistaa, että käyttäjät säilyttävät hallinnan siitä, mitä LLM näkee ja tuottaa.

## Otantaparametrien yleiskatsaus

MCP määrittelee seuraavat otantaparametrit, joita voidaan konfiguroida asiakaspyynnöissä:

| Parametri | Kuvaus | Tyypillinen arvoalue |
|-----------|-------------|---------------|
| `temperature` | Hallitsee satunnaisuutta token-valinnassa | 0.0 - 1.0 |
| `maxTokens` | Maksimi generoiden tokenien määrä | Kokonaisluku |
| `stopSequences` | Mukautetut sekvenssit, jotka pysäyttävät generoinnin kohdatessaan | Merkkijonotaulukko |
| `metadata` | Lisätoimittajasidonnaiset parametrit | JSON-objekti |

Monet LLM-toimittajat tukevat lisäparametreja `metadata`-kentän kautta, jotka voivat sisältää:

| Yleinen laajennusparametri | Kuvaus | Tyypillinen arvoalue |
|-----------|-------------|---------------|
| `top_p` | Nucleus-otanta – rajoittaa tokenit top kumulatiiviseen todennäköisyyteen | 0.0 - 1.0 |
| `top_k` | Rajoittaa token-valinnan top K vaihtoehtoihin | 1 - 100 |
| `presence_penalty` | Rankaiseminen tokenien esiintymisen mukaan tekstissä tähän asti | -2.0 - 2.0 |
| `frequency_penalty` | Rankaiseminen tokenien esiintymistiheyden mukaan tekstissä tähän asti | -2.0 - 2.0 |
| `seed` | Tietty satunnainen siemen toistettaville tuloksille | Kokonaisluku |

## Esimerkkipyyntöjen muoto

Tässä esimerkki pyynnöstä asiakkaalta MCP:ssä:

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

## Vastausmuoto

Asiakas palauttaa täydennystuloksen:

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

## Ihmisen ohjaus

MCP:n otanta on suunniteltu ihmisen valvonnalla:

- **Promptien osalta**:
  - Asiakkaiden tulee näyttää käyttäjille ehdotettu prompt
  - Käyttäjien tulee voida muokata tai hylätä promptit
  - Järjestelmäprompteja voidaan suodattaa tai muokata
  - Kontekstin sisällytys on asiakkaan hallinnassa

- **Täydennysten osalta**:
  - Asiakkaiden tulee näyttää käyttäjille täydennys
  - Käyttäjien tulee voida muokata tai hylätä täydennyksiä
  - Asiakkaat voivat suodattaa tai muokata täydennyksiä
  - Käyttäjät hallitsevat, mitä mallia käytetään

Näiden periaatteiden pohjalta tarkastellaan, miten otanta toteutetaan eri ohjelmointikielillä keskittyen yleisimmin tuettuihin parametreihin LLM-toimittajien kesken.

## Turvallisuusnäkökohdat

Kun toteutat otantaa MCP:ssä, ota huomioon seuraavat turvallisuuskäytännöt:

- **Tarkista kaikki viestisisällöt** ennen niiden lähettämistä asiakkaalle
- **Puhdista arkaluontoiset tiedot** prompteista ja täydennyksistä
- **Toteuta käyttörajoitukset** väärinkäytösten estämiseksi
- **Seuraa otannan käyttöä** poikkeavuuksien varalta
- **Salaa tiedonsiirto** turvallisin protokollin
- **Käsittele käyttäjien tietosuoja** soveltuvien säädösten mukaisesti
- **Auditoi otantapyynnöt** vaatimustenmukaisuuden ja turvallisuuden varmistamiseksi
- **Hallinnoi kustannusriskit** asettamalla asianmukaiset rajat
- **Toteuta aikakatkaisut** otantopyynnöille
- **Käsittele mallin virheet tyylikkäästi** asianmukaisilla varajärjestelmillä

Otantaparametrit mahdollistavat kielimallin käyttäytymisen hienosäädön halutun tasapainon saavuttamiseksi deterministisen ja luovan tuotoksen välillä.

Katsotaan, miten nämä parametrit määritetään eri ohjelmointikielillä.

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

Edellä olevassa koodissa olemme:

- Luoneet MCP-asiakkaan tiettyyn palvelimen URL-osoitteeseen.
- Määrittäneet pyynnön otantaparametreilla kuten `temperature`, `top_p` ja `top_k`.
- Lähettäneet pyynnön ja tulostaneet generoidun tekstin.
- Käyttäneet:
    - `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnin aikana. Tässä tapauksessa salliimme `ideaGenerator`- ja `marketAnalyzer`-työkalujen avustaa luovien sovellusideoiden generoinnissa.
    - `frequencyPenalty` ja `presencePenalty` toistojen ja monipuolisuuden hallintaan tuotoksessa.
    - `temperature` hallitsemaan tuloksen satunnaisuutta, jossa korkeammat arvot johtavat luovempiin vastauksiin.
    - `top_p` rajoittamaan token-valinnan top kumulatiiviseen todennäköisyyteen, parantaen generoidun tekstin laatua.
    - `top_k` rajoittamaan mallin token-valinnan top K todennäköisimpään, mikä auttaa tuottamaan johdonmukaisempia vastauksia.
    - `frequencyPenalty` ja `presencePenalty` vähentämään toistoa ja kannustamaan monipuolisuuteen generoidussa tekstissä.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript-esimerkki: Lämpötilan ja Top-P-näytteenottokokoonpano
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Alusta MCP-asiakas
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Määritä pyyntö eri näytteenottoparametreilla
  const creativeSampling = {
    temperature: 0.9,    // Korkeampi lämpötila = enemmän satunnaisuutta/luovuutta
    topP: 0.92,          // Ota huomioon tokenit, joiden kokonaiskertoimena on 92 %
    frequencyPenalty: 0.6, // Vähennä token-jaksojen toistumista
    presencePenalty: 0.4   // Rangaise tokeneita, jotka ovat jo esiintyneet tekstissä
  };
  
  const factualSampling = {
    temperature: 0.2,    // Alhaisempi lämpötila = enemmän määräävää/tosiasiallista
    topP: 0.85,          // Hieman fokusoituimpi token-valinta
    frequencyPenalty: 0.2, // Minimaalinen toistopakko
    presencePenalty: 0.1   // Minimaalinen esiintymisrangaistus
  };
  
  try {
    // Lähetä kaksi pyyntöä eri näytteenottokokoonpanoilla
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

Edellisessä koodissa olemme:

- Alustaneet MCP-asiakkaan käyttämällä palvelimen URL:ia ja API-avainta.
- Määrittäneet kaksi otantaparametrien konfiguraatiota: yhden luoville tehtäville ja toisen faktapohjaisille tehtäville.
- Lähettäneet pyynnöt näillä kokoonpanoilla, mahdollistaen mallin käyttää tiettyjä työkaluja kustakin tehtävästä riippuen.
- Tulostaneet generoidut vastaukset demonstroidaksemme erilaisten otantaparametrien vaikutuksia.
- Käyttäneet `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnissa. Tässä tapauksessa salliimme `ideaGenerator` ja `environmentalImpactTool` luovissa tehtävissä, sekä `factChecker` ja `dataAnalysisTool` faktapohjaisissa tehtävissä.
- Käyttäneet `temperature` hallitsemaan tuloksen satunnaisuutta, jossa korkeammat arvot johtavat luovempiin vastauksiin.
- Käyttäneet `top_p` rajoittamaan token-valinnan top kumulatiiviseen todennäköisyyteen, parantaen generoidun tekstin laatua.
- Käyttäneet `frequencyPenalty` ja `presencePenalty` vähentämään toistoa ja kannustamaan monipuolisuuteen tuotoksessa.
- Käyttäneet `top_k` rajoittamaan mallin token-valinnan top K todennäköisimpään, mikä auttaa tuottamaan johdonmukaisempia vastauksia.

---

## Deterministinen otanta

Sovelluksissa, joissa vaaditaan johdonmukaisia tuloksia, deterministinen otanta takaa toistettavat lopputulokset. Tämä tehdään käyttämällä kiinteää satunnaissiementä ja asettamalla lämpötila nollaan.

Tarkastellaan alla olevaa esimerkkitoteutusta, joka havainnollistaa determinististä otantaa eri ohjelmointikielillä.

# [Java](#tab/java)

```java
// Java-esimerkki: Deterministiset vastaukset kiinteällä siemenellä
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Kiinteän siemenen käyttäminen deterministisiin tuloksiin
        
        // Ensimmäinen pyyntö kiinteällä siemenellä
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nolla lämpötila maksimaaliseen determinismiin
            .build();
            
        // Toinen pyyntö samalla siemenellä
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Suorita molemmat pyynnöt
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Vastauksien tulisi olla identtisiä saman siemenen ja lämpötilan=0 takia
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Edellisessä koodissa olemme:

- Luoneet MCP-asiakkaan määritellyllä palvelimen URL-osoitteella.
- Määrittäneet kaksi pyyntöä samalla promptilla, kiinteällä siemenellä ja nollalämpötilalla.
- Lähettäneet molemmat pyynnöt ja tulostaneet generoidun tekstin.
- Demonstroineet, että vastaukset ovat identtiset deterministisen otantakonfiguraation (sama siemen ja lämpötila) vuoksi.
- Käyttäneet `setSeed` määrittämään kiinteän satunnaissiementä, mikä varmistaa, että malli tuottaa saman tuloksen samaa syötettä kohti joka kerta.
- Asetettu `temperature` nollaksi maksimaalisen determinismin varmistamiseksi, jolloin malli valitsee aina todennäköisimmän seuraavan tokenin ilman satunnaisuutta.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript-esimerkki: Deterministiset vastaukset siemenohjauksella
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Ensimmäinen pyyntö kiinteällä siemenellä
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nolla lämpötila maksimaaliselle determinismille
    });
    
    // Toinen pyyntö samalla siemenellä ja lämpötilalla
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Kolmas pyyntö eri siemenellä mutta samalla lämpötilalla
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

Edellisessä koodissa olemme:

- Alustaneet MCP-asiakkaan palvelimen URL:illa.
- Määrittäneet kaksi pyyntöä samalla promptilla, kiinteällä siemenellä ja nollalämpötilalla.
- Lähettäneet molemmat pyynnöt ja tulostaneet generoidun tekstin.
- Demonstroineet, että vastaukset ovat identtiset deterministisen otantakonfiguraation (sama siemen ja lämpötila) vuoksi.
- Käyttäneet `seed` määrittämään kiinteän satunnaissiementä, mikä varmistaa saman tuloksen saman syötteen kohdalla joka kerta.
- Asetettu `temperature` nollaan maksimaalisen determinismin saavuttamiseksi, jolloin malli valitsee aina todennäköisimmän seuraavan tokenin ilman satunnaisuutta.
- Käytetty eri siementä kolmannessa pyynnössä osoittamaan, että siemenen muuttaminen tuottaa erilaisia tuloksia, vaikka prompt ja lämpötila pysyisivät samoina.

---

## Dynaaminen otantakonfiguraatio

Älykäs otanta mukauttaa parametreja pyynnön kontekstin ja vaatimusten mukaan. Tämä tarkoittaa parametrien, kuten temperature, top_p ja rangaistukset, säätämistä dynaamisesti tehtävätyypin, käyttäjäasetusten tai aiemman suorituskyvyn perusteella.

Katsotaan, miten dynaaminen otanta toteutetaan eri ohjelmointikielillä.

# [Python](#tab/python)

```python
# Python-esimerkki: Dynaaminen otanta perustuen pyyntöyhteyteen
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Määrittele otannan asetukset eri tehtävätyypeille
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Valitse perusasetus
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Säädä käyttäjän mieltymysten mukaan, jos annettu
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skaalaa lämpötila luovuuden mieltymyksen perusteella (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Säädä top_p halutun vastausmonimuotoisuuden mukaan
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Luo ja lähetä pyyntö mukautetuilla otanta-parametreilla
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Palauta vastaus otantametadata kanssa läpinäkyvyyden takaamiseksi
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Edellisessä koodissa olemme:

- Luoneet `DynamicSamplingService`-luokan, joka hallinnoi adaptiivista otantaa.
- Määrittäneet otantavalmisteluja eri tehtävätyypeille (luova, faktapohjainen, koodi, analyyttinen).
- Valinneet perusotantaprofiilin tehtävätyypin perusteella.
- Muokanneet otantaparametreja käyttäjän mieltymysten, kuten luovuustason ja monipuolisuuden, mukaan.
- Lähettäneet pyynnön dynaamisesti konfiguroiduilla otantaparametreilla.
- Palauttaneet generoidun tekstin sekä käytetyt otantaparametrit ja tehtävätyypin läpinäkyvyyden vuoksi.
- Käyttäneet `temperature` hallitsemaan satunnaisuutta, jossa korkeampi arvo johtaa luovempiin vastauksiin.
- Käyttäneet `top_p` rajoittamaan token-valinnan top kumulatiiviseen todennäköisyyteen, parantaen generoidun tekstin laatua.
- Käyttäneet `frequency_penalty` vähentämään toistoa ja kannustamaan monipuolisuuteen.
- Käyttäneet `user_preferences` mahdollistamaan otantaparametrien mukauttamisen käyttäjän määrittämien luovuus- ja monipuolisuustasojen mukaan.
- Käyttäneet `task_type` määrittämään sopivan otantastrategian pyynnölle, mahdollistaen paremmin räätälöidyt vastaukset tehtävän luonteesta riippuen.
- Käyttäneet `send_request` -metodia lähettämään promptin konfiguroiduilla otantaparametreilla varmistaen mallin tuottavan tekstiä vaadittujen ehtojen mukaisesti.
- Käyttäneet `generated_text` hakemaan mallin vastauksen, joka palautetaan yhdessä otantaparametrien ja tehtävätyypin kanssa jatkoanalyysiä tai näyttämistä varten.
- Käyttäneet `min` ja `max` -funktioita varmistamaan, että käyttäjäasetukset pysyvät sallituissa rajoissa, estäen virheelliset otantakonfiguraatiot.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript-esimerkki: Dynaaminen otantakonfiguraatio käyttäjäkontekstin perusteella
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Määrittele perusotantaprofiilit
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Seuraa aikaisempaa suorituskykyä
    this.performanceHistory = [];
  }
  
  // Tunnista tehtävätyyppi kehotteesta
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Yksinkertainen heuristinen tunnistus – voitaisiin parantaa ML-luokittelulla
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
    
    // Oletuksena keskustelu, jos tyyppiä ei tunnisteta selvästi
    return 'conversational';
  }
  
  // Laske otanta-parametrit kontekstin ja käyttäjäasetusten perusteella
  getSamplingParameters(prompt, context = {}) {
    // Tunnista tehtävätyyppi
    const taskType = this.detectTaskType(prompt, context);
    
    // Hae perusprofiili
    let params = {...this.samplingProfiles[taskType]};
    
    // Säädä käyttäjäasetusten mukaan
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Skaalaa 1-10 sopivalle lämpötilavälille
        params.temperature = 0.1 + (creativity * 0.09); // 0,1-1,0
      }
      
      if (precision !== undefined) {
        // Korkeampi tarkkuus tarkoittaa pienempää topP-arvoa (tarkempi valinta)
        params.topP = 1.0 - (precision * 0.05); // 0,5-1,0
      }
      
      if (consistency !== undefined) {
        // Korkea johdonmukaisuus tarkoittaa pienempiä rangaistuksia
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0,1-0,9
      }
    }
    
    // Käytä oppimia säätöjä suorituskykyhistoriasta
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Yksinkertainen adaptiivinen logiikka – voisi parantua monimutkaisemmilla algoritmeilla
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Huomioi vain viimeaikainen historia
    
    if (relevantHistory.length > 0) {
      // Laske keskimääräiset suorituskykypisteet
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Jos suoritus on alle kynnysarvon, säädä parametreja
      if (avgScore < 0.7) {
        // Pieni säätö kohti turvallisempia arvoja
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Tallenna suoritus tulevia säätöjä varten
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0–1 arvio vastauskvaliteetista
    });
    
    // Rajaa historian koko
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Hae optimoidut otanta-parametrit
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Lähetä pyyntö optimoiduilla parametreilla
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Jos käyttäjä antaa palautetta, tallenna se tulevaa optimointia varten
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

// Esimerkin käyttö
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Luova tehtävä, jossa räätälöidyt käyttäjäasetukset
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Korkea luovuus (1-10)
          consistency: 3  // Matala johdonmukaisuus (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Koodin generointitehtävä
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Matala luovuus
          precision: 8,   // Korkea tarkkuus
          consistency: 9  // Korkea johdonmukaisuus
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

Edellisessä koodissa olemme:

- Luoneet `AdaptiveSamplingManager`-luokan, joka hallinnoi dynaamista otantaa tehtävätyypin ja käyttäjäasetusten mukaan.
- Määrittäneet otantaprofiilit eri tehtävätyypeille (luova, faktapohjainen, koodi, keskustelu).
- Toteuttaneet menetelmän, joka havaitsee tehtävätyypin promptista yksinkertaisilla heuristiikoilla.
- Laskeneet otantaparametreja havaittuun tehtävätyyppiin ja käyttäjäasetuksiin perustuen.
- Soveltaneet opittuja säätöjä aiemman suorituskyvyn pohjalta optimoiden otantaparametreja.
- Tallentaneet suorituskykyä tulevia säätöjä varten, mahdollistaen järjestelmän oppia aiemmista vuorovaikutuksista.
- Lähettäneet pyynnöt dynaamisesti konfiguroiduilla otantaparametreilla ja palauttaneet generoidun tekstin yhdessä käytettyjen parametrien ja havaitun tehtävätyypin kanssa.
- Käyttäneet:
    - `userPreferences` mahdollistamaan otantaparametrien räätälöinnin käyttäjän määrittelemien luovuuden, täsmällisyyden ja johdonmukaisuuden tasojen perusteella.
    - `detectTaskType` määrittämään tehtävän luonteen promptin perusteella, mahdollistaen räätälöidymmät vastaukset.
    - `recordPerformance` kirjaamaan generoituja vastausten suorituskykyä, mahdollistaen järjestelmän sopeutumisen ja parantamisen ajan myötä.
    - `applyLearnedAdjustments` muokkaamaan otantaparametreja historiallisen suorituskyvyn perusteella, parantaen mallin kykyä tuottaa laadukkaita vastauksia.
    - `generateResponse` kapseloimaan koko generointiprosessin adaptiivisen otannan kanssa, helpottaen sen kutsumista eri promtpeilla ja konteksteilla.
    - `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnin aikana mahdollistaen kontekstin paremman huomioimisen vastauksissa.
    - `feedbackScore` mahdollistamaan käyttäjien antaman palautteen generoidun vastauksen laadusta, jota voidaan käyttää mallin suorituskyvyn jatkokehitykseen.
    - `performanceHistory` ylläpitämään tietoa aiemmista vuorovaikutuksista, mahdollistaen järjestelmän oppia menneistä onnistumisista ja epäonnistumisista.
    - `getSamplingParameters` säätämään otantaparametreja dynaamisesti pyynnön kontekstin mukaan, mahdollistaen joustavamman ja reagoivan mallin käyttäytymisen.
    - `detectTaskType` luokittelemaan tehtävän promptin perusteella, mahdollistaen sopivien otantastrategioiden käyttöönoton eri pyyntötyypeille.
    - `samplingProfiles` määrittelemään perusotantakonfiguraatiot eri tehtävätyypeille, mahdollistaen nopean säädön pyynnön luonteen mukaan.

---

## Mitä seuraavaksi

- [5.7 Skaalaus](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
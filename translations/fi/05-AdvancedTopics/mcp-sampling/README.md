# Otanta Model Context Protocolissa

Otanta on tehokas MCP-ominaisuus, joka mahdollistaa palvelimien pyytää LLM-valmisteluja asiakkaan kautta, mahdollistaen kehittyneet agenttikäyttäytymiset samalla kun turvataan turvallisuus ja yksityisyys. Oikea otantakonfiguraatio voi merkittävästi parantaa vastausten laatua ja suorituskykyä. MCP tarjoaa standardoidun tavan hallita, miten mallit tuottavat tekstiä tietyillä parametreilla, jotka vaikuttavat satunnaisuuteen, luovuuteen ja johdonmukaisuuteen.

## Johdanto

Tässä oppitunnissa tutustumme siihen, miten otantaparametreja konfiguroidaan MCP-pyynnöissä ja ymmärrämme otannan taustalla olevat protokollamekanismit.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Ymmärtää MCP:n keskeiset otantaparametrit.
- Konfiguroida otantaparametreja eri käyttötarkoituksiin.
- Toteuttaa deterministisen otannan toistettavien tulosten saamiseksi.
- Säätää otantaparametreja dynaamisesti kontekstin ja käyttäjäasetusten mukaan.
- Soveltaa otantastrategioita mallin suorituskyvyn parantamiseksi eri tilanteissa.
- Ymmärtää, miten otanta toimii MCP:n asiakas-palvelin -virrassa.

## Miten otanta toimii MCP:ssä

MCP:n otantaprosessi etenee seuraavasti:

1. Palvelin lähettää `sampling/createMessage` -pyynnön asiakkaalle
2. Asiakas tarkistaa pyynnön ja voi muokata sitä
3. Asiakas ottaa otannan LLM:stä
4. Asiakas tarkistaa valmistelun
5. Asiakas palauttaa tuloksen palvelimelle

Tämä ihmisen ohjaama malli varmistaa, että käyttäjät säilyttävät kontrollin siitä, mitä LLM näkee ja tuottaa.

## Otantaparametrien yleiskatsaus

MCP määrittelee seuraavat otantaparametrit, joita voidaan konfiguroida asiakaspyynnöissä:

| Parametri | Kuvaus | Tyypillinen arvoalue |
|-----------|--------|---------------------|
| `temperature` | Hallitsee satunnaisuutta token-valinnassa | 0.0 - 1.0 |
| `maxTokens` | Maksimimäärä tuotettavia tokeneita | Kokonaisluku |
| `stopSequences` | Mukautetut sekvenssit, jotka pysäyttävät generoinnin kohdatessaan | Merkkijonotaulukko |
| `metadata` | Lisäparametrit palveluntarjoajakohtaisesti | JSON-objekti |

Monet LLM-palveluntarjoajat tukevat lisäparametreja `metadata`-kentän kautta, jotka voivat sisältää:

| Yleinen laajennusparametri | Kuvaus | Tyypillinen arvoalue |
|----------------------------|--------|---------------------|
| `top_p` | Nucleus-otanta – rajoittaa tokenit kumulatiivisen todennäköisyyden huippuun | 0.0 - 1.0 |
| `top_k` | Rajoittaa token-valinnan top K vaihtoehtoihin | 1 - 100 |
| `presence_penalty` | Rankaiseminen tokenien esiintymisen perusteella tekstissä | -2.0 - 2.0 |
| `frequency_penalty` | Rankaiseminen tokenien esiintymistiheyden perusteella tekstissä | -2.0 - 2.0 |
| `seed` | Kiinteä satunnaissiementä toistettaville tuloksille | Kokonaisluku |

## Esimerkkipyyntömuoto

Tässä esimerkki otantapyynnöstä asiakkaalle MCP:ssä:

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

Asiakas palauttaa valmistelutuloksen:

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

## Ihminen ohjauksessa

MCP:n otanta on suunniteltu ihmisen valvonnalla:

- **Kehotteille**:
  - Asiakkaiden tulisi näyttää käyttäjille ehdotettu kehotte
  - Käyttäjien tulisi voida muokata tai hylätä kehotteet
  - Järjestelmäkehotteita voidaan suodattaa tai muokata
  - Kontekstin sisällyttäminen on asiakkaan hallinnassa

- **Valmisteluille**:
  - Asiakkaiden tulisi näyttää käyttäjille valmistelu
  - Käyttäjien tulisi voida muokata tai hylätä valmistelut
  - Asiakkaat voivat suodattaa tai muokata valmisteluja
  - Käyttäjät hallitsevat, mitä mallia käytetään

Näiden periaatteiden pohjalta tarkastellaan, miten otanta toteutetaan eri ohjelmointikielillä, keskittyen yleisesti LLM-palveluntarjoajien tukemiin parametreihin.

## Turvallisuusnäkökohdat

Otantaa toteutettaessa MCP:ssä huomioi seuraavat turvallisuuskäytännöt:

- **Varmista kaikkien viestien sisältö** ennen lähettämistä asiakkaalle
- **Puhdista arkaluonteiset tiedot** kehotteista ja valmisteluista
- **Ota käyttöön käyttörajoitukset** väärinkäytösten estämiseksi
- **Seuraa otannan käyttöä** epätavallisten mallien varalta
- **Salaa tiedonsiirto** turvallisilla protokollilla
- **Käsittele käyttäjätietojen yksityisyyttä** sovellettavien säädösten mukaisesti
- **Tarkasta otantapyynnöt** vaatimustenmukaisuuden ja turvallisuuden varmistamiseksi
- **Hallinnoi kustannuksia** sopivilla rajoituksilla
- **Käytä aikakatkaisuja** otantapyynnöille
- **Käsittele mallivirheet joustavasti** sopivilla varajärjestelyillä

Otantaparametrit mahdollistavat kielimallien käyttäytymisen hienosäädön halutun tasapainon saavuttamiseksi determinististen ja luovien vastausten välillä.

Tarkastellaan, miten näitä parametreja konfiguroidaan eri ohjelmointikielillä.

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

Edellisessä koodissa olemme:

- Luoneet MCP-asiakkaan tietylle palvelin-URL:lle.
- Konfiguroineet pyynnön otantaparametreilla kuten `temperature`, `top_p` ja `top_k`.
- Lähettäneet pyynnön ja tulostaneet tuotetun tekstin.
- Käyttäneet:
    - `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnin aikana. Tässä tapauksessa sallimme `ideaGenerator`- ja `marketAnalyzer`-työkalut auttamaan luovien sovellusideoiden tuottamisessa.
    - `frequencyPenalty` ja `presencePenalty` toistojen hallintaan ja monimuotoisuuden lisäämiseen tuotoksessa.
    - `temperature` hallitsemaan tuotoksen satunnaisuutta, korkeammat arvot johtavat luovempiin vastauksiin.
    - `top_p` rajoittamaan token-valinnan niihin, jotka muodostavat kumulatiivisen todennäköisyyden huipun, parantaen tuotetun tekstin laatua.
    - `top_k` rajoittamaan mallin valitsemaan top K todennäköisintä tokenia, mikä auttaa tuottamaan johdonmukaisempia vastauksia.
    - `frequencyPenalty` ja `presencePenalty` vähentämään toistoa ja kannustamaan monimuotoisuuteen tuotetussa tekstissä.

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

Edellisessä koodissa olemme:

- Alustaneet MCP-asiakkaan palvelin-URL:llä ja API-avaimella.
- Konfiguroineet kaksi otantaparametrien sarjaa: yhden luoville tehtäville ja toisen faktapohjaisille tehtäville.
- Lähettäneet pyynnöt näillä konfiguraatioilla, sallien mallin käyttää tiettyjä työkaluja kullekin tehtävälle.
- Tulostaneet tuotetut vastaukset havainnollistaaksemme eri otantaparametrien vaikutuksia.
- Käyttäneet `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnin aikana. Tässä tapauksessa sallimme `ideaGenerator` ja `environmentalImpactTool` luoville tehtäville, sekä `factChecker` ja `dataAnalysisTool` faktapohjaisille tehtäville.
- Käyttäneet `temperature` hallitsemaan tuotoksen satunnaisuutta, korkeammat arvot johtavat luovempiin vastauksiin.
- Käyttäneet `top_p` rajoittamaan token-valinnan niihin, jotka muodostavat kumulatiivisen todennäköisyyden huipun, parantaen tuotetun tekstin laatua.
- Käyttäneet `frequencyPenalty` ja `presencePenalty` vähentämään toistoa ja kannustamaan monimuotoisuuteen tuotoksessa.
- Käyttäneet `top_k` rajoittamaan mallin valitsemaan top K todennäköisintä tokenia, mikä auttaa tuottamaan johdonmukaisempia vastauksia.

---

## Deterministinen otanta

Sovelluksissa, jotka vaativat johdonmukaisia tuloksia, deterministinen otanta takaa toistettavat tulokset. Tämä saavutetaan käyttämällä kiinteää satunnaissiementä ja asettamalla temperature nollaan.

Tarkastellaan alla olevaa esimerkkitoteutusta, joka havainnollistaa determinististä otantaa eri ohjelmointikielillä.

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

Edellisessä koodissa olemme:

- Luoneet MCP-asiakkaan määritellyllä palvelin-URL:llä.
- Konfiguroineet kaksi pyyntöä samalla kehotteella, kiinteällä siemenellä ja nollalla temperature-arvolla.
- Lähettäneet molemmat pyynnöt ja tulostaneet tuotetun tekstin.
- Havainnollistaneet, että vastaukset ovat identtisiä deterministisen otantakonfiguraation (sama siemen ja temperature) vuoksi.
- Käyttäneet `setSeed` määrittämään kiinteän satunnaissiementä, varmistaen, että malli tuottaa saman tuloksen samalla syötteellä joka kerta.
- Asettaneet `temperature` arvoksi nolla maksimaalisen determinismin varmistamiseksi, eli malli valitsee aina todennäköisimmän seuraavan tokenin ilman satunnaisuutta.

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

Edellisessä koodissa olemme:

- Alustaneet MCP-asiakkaan palvelin-URL:llä.
- Konfiguroineet kaksi pyyntöä samalla kehotteella, kiinteällä siemenellä ja nollalla temperature-arvolla.
- Lähettäneet molemmat pyynnöt ja tulostaneet tuotetun tekstin.
- Havainnollistaneet, että vastaukset ovat identtisiä deterministisen otantakonfiguraation (sama siemen ja temperature) vuoksi.
- Käyttäneet `seed` määrittämään kiinteän satunnaissiementä, varmistaen, että malli tuottaa saman tuloksen samalla syötteellä joka kerta.
- Asettaneet `temperature` arvoksi nolla maksimaalisen determinismin varmistamiseksi, eli malli valitsee aina todennäköisimmän seuraavan tokenin ilman satunnaisuutta.
- Käyttäneet eri siementä kolmannessa pyynnössä osoittaaksemme, että siemenen vaihtaminen johtaa erilaisiin tuloksiin, vaikka kehotte ja temperature pysyvät samoina.

---

## Dynaaminen otantakonfiguraatio

Älykäs otanta mukauttaa parametreja kontekstin ja pyynnön vaatimusten mukaan. Tämä tarkoittaa temperature-, top_p- ja rangaistusten dynaamista säätämistä tehtävätyypin, käyttäjäasetusten tai aiemman suorituskyvyn perusteella.

Tarkastellaan, miten dynaaminen otanta toteutetaan eri ohjelmointikielillä.

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

Edellisessä koodissa olemme:

- Luoneet `DynamicSamplingService`-luokan, joka hallinnoi adaptiivista otantaa.
- Määritelleet otantapresetit eri tehtävätyypeille (luova, faktapohjainen, koodi, analyyttinen).
- Valinneet perusotantapresetin tehtävätyypin perusteella.
- Säätäneet otantaparametreja käyttäjäasetusten, kuten luovuuden ja monimuotoisuuden, mukaan.
- Lähettäneet pyynnön dynaamisesti konfiguroiduilla otantaparametreilla.
- Palauttaneet tuotetun tekstin sekä käytetyt otantaparametrit ja tehtävätyypin läpinäkyvyyden vuoksi.
- Käyttäneet `temperature` hallitsemaan tuotoksen satunnaisuutta, korkeammat arvot johtavat luovempiin vastauksiin.
- Käyttäneet `top_p` rajoittamaan token-valinnan niihin, jotka muodostavat kumulatiivisen todennäköisyyden huipun, parantaen tuotetun tekstin laatua.
- Käyttäneet `frequency_penalty` vähentämään toistoa ja kannustamaan monimuotoisuuteen tuotoksessa.
- Käyttäneet `user_preferences` mahdollistamaan otantaparametrien mukautuksen käyttäjän määrittelemien luovuus- ja monimuotoisuustasojen mukaan.
- Käyttäneet `task_type` määrittämään sopivan otantastrategian pyynnölle, mahdollistaen räätälöidympiä vastauksia tehtävän luonteen perusteella.
- Käyttäneet `send_request`-metodia lähettämään kehotteen konfiguroiduilla otantaparametreilla, varmistaen, että malli tuottaa tekstiä määriteltyjen vaatimusten mukaisesti.
- Käyttäneet `generated_text` hakemaan mallin vastauksen, joka palautetaan yhdessä otantaparametrien ja tehtävätyypin kanssa jatkoanalyysiä tai näyttöä varten.
- Käyttäneet `min` ja `max` -funktioita varmistamaan, että käyttäjäasetukset pysyvät sallituissa rajoissa, estäen virheelliset otantakonfiguraatiot.

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

Edellisessä koodissa olemme:

- Luoneet `AdaptiveSamplingManager`-luokan, joka hallinnoi dynaamista otantaa tehtävätyypin ja käyttäjäasetusten perusteella.
- Määritelleet otantaprofiilit eri tehtävätyypeille (luova, faktapohjainen, koodi, keskustelu).
- Toteuttaneet menetelmän tehtävätyypin tunnistamiseksi kehotteesta yksinkertaisin heuristiikoin.
- Laskeneet otantaparametrit tunnistetun tehtävätyypin ja käyttäjäasetusten perusteella.
- Soveltaneet opittuja säätöjä aiemman suorituskyvyn perusteella optimoidakseen otantaparametreja.
- Tallentaneet suorituskykytiedot tulevia säätöjä varten, mahdollistaen järjestelmän oppimisen aiemmista vuorovaikutuksista.
- Lähettäneet pyynnöt dynaamisesti konfiguroiduilla otantaparametreilla ja palauttaneet tuotetun tekstin sekä käytetyt parametrit ja tunnistetun tehtävätyypin.
- Käyttäneet:
    - `userPreferences` mahdollistamaan otantaparametrien mukautuksen käyttäjän määrittelemien luovuus-, tarkkuus- ja johdonmukaisuustasojen mukaan.
    - `detectTaskType` määrittämään tehtävän luonteen kehotteen perusteella, mahdollistaen räätälöidympiä vastauksia.
    - `recordPerformance` kirjaamaan tuotettujen vastausten suorituskyvyn, mahdollistaen järjestelmän sopeutumisen ja parantamisen ajan myötä.
    - `applyLearnedAdjustments` muokkaamaan otantaparametreja aiemman suorituskyvyn perusteella, parantaen mallin kykyä tuottaa laadukkaita vastauksia.
    - `generateResponse` kapseloimaan koko prosessin vastauksen tuottamiseksi adaptiivisella otannalla, tehden siitä helpon kutsua eri kehotteilla ja konteksteilla.
    - `allowedTools` määrittämään, mitä työkaluja malli voi käyttää generoinnin aikana, mahdollistaen kontekstin huomioivia vastauksia.
    - `feedbackScore` antamaan käyttäjille mahdollisuuden antaa palautetta tuotetun vastauksen laadusta, jota voidaan käyttää mallin suorituskyvyn jatkokehitykseen.
    - `performanceHistory` ylläpitämään tietoja aiemmista vuorovaikutuksista, mahdollistaen järjestelmän oppimisen menestyksistä ja epäonnistumisista.
    - `getSamplingParameters` dynaamisesti säätämään otantaparametreja pyynnön kontekstin mukaan, mahdollistaen joustavamman ja reagoivamman mallikäyttäytymisen.
    - `detectTaskType` luokittelemaan tehtävän kehotteen perusteella, mahdollistaen sopivien otantastrategioiden soveltamisen eri pyyntötyypeille.
    - `samplingProfiles` määrittelemään perusotantakonfiguraatiot eri tehtävä

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
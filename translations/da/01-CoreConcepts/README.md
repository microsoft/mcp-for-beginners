# MCP Core Concepts: Mestring af Model Context Protocol til AI-integration

[![MCP Core Concepts](../../../translated_images/da/02.8203e26c6fb5a797f38a10012061013ec66c95bb3260f6c9cfd2bf74b00860e1.png)](https://youtu.be/earDzWGtE84)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

[Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) er en kraftfuld, standardiseret ramme, der optimerer kommunikationen mellem store sprogmodeller (LLM'er) og eksterne værktøjer, applikationer og datakilder.  
Denne guide vil føre dig gennem de grundlæggende koncepter i MCP. Du vil lære om dens klient-server-arkitektur, væsentlige komponenter, kommunikationsmekanik og bedste praksis for implementering.

- **Udtrykkeligt bruger samtykke**: Al dataadgang og operationer kræver udtrykkeligt brugerens godkendelse før udførelse. Brugere skal klart forstå, hvilke data der vil blive tilgået, og hvilke handlinger der vil blive udført, med detaljeret kontrol over tilladelser og autorisationer.

- **Beskyttelse af dataprivatliv**: Brugerdata eksponeres kun med udtrykkeligt samtykke og skal beskyttes af robuste adgangskontroller gennem hele interaktionslivscyklussen. Implementeringer skal forhindre uautoriseret dataoverførsel og opretholde strenge privatlivsgrænser.

- **Sikkerhed ved værktøjsudførelse**: Hver værktøjsanmodning kræver udtrykkeligt brugerens samtykke med klar forståelse af værktøjets funktionalitet, parametre og potentielle konsekvenser. Robuste sikkerhedsgrænser skal forhindre utilsigtet, usikker eller ondsindet værktøjsudførelse.

- **Transportlagsikkerhed**: Alle kommunikationskanaler bør anvende passende kryptering og autentificeringsmekanismer. Fjernforbindelser bør implementere sikre transportprotokoller og korrekt håndtering af legitimationsoplysninger.

#### Implementeringsretningslinjer:

- **Tilladelsesstyring**: Implementer detaljerede tilladelsessystemer, der giver brugere kontrol over, hvilke servere, værktøjer og ressourcer der er tilgængelige  
- **Autentificering & Autorisation**: Brug sikre autentificeringsmetoder (OAuth, API-nøgler) med korrekt tokenhåndtering og udløb  
- **Inputvalidering**: Valider alle parametre og datainput i henhold til definerede skemaer for at forhindre injektionsangreb  
- **Audit-logning**: Vedligehold omfattende logfiler over alle operationer til sikkerhedsovervågning og overholdelse

## Oversigt

Denne lektion udforsker den grundlæggende arkitektur og de komponenter, der udgør Model Context Protocol (MCP) økosystemet. Du vil lære om klient-server-arkitekturen, nøglekomponenter og kommunikationsmekanismer, der driver MCP-interaktioner.

## Centrale læringsmål

Ved slutningen af denne lektion vil du:

- Forstå MCP klient-server-arkitekturen.  
- Identificere roller og ansvar for Hosts, Clients og Servers.  
- Analysere de kernefunktioner, der gør MCP til et fleksibelt integrationslag.  
- Lære, hvordan information flyder inden for MCP-økosystemet.  
- Få praktiske indsigter gennem kodeeksempler i .NET, Java, Python og JavaScript.

## MCP Arkitektur: Et dybere kig

MCP-økosystemet er bygget på en klient-server-model. Denne modulære struktur tillader AI-applikationer at interagere effektivt med værktøjer, databaser, API'er og kontekstuelle ressourcer. Lad os opdele denne arkitektur i dens kernekomponenter.

I sin kerne følger MCP en klient-server-arkitektur, hvor en host-applikation kan forbinde til flere servere:

```mermaid
flowchart LR
    subgraph "Din Computer"
        Host["Vært med MCP (Visual Studio, VS Code, IDE'er, Værktøjer)"]
        S1["MCP Server A"]
        S2["MCP Server B"]
        S3["MCP Server C"]
        Host <-->|"MCP Protokol"| S1
        Host <-->|"MCP Protokol"| S2
        Host <-->|"MCP Protokol"| S3
        S1 <--> D1[("Lokal\Data Kilde A")]
        S2 <--> D2[("Lokal\Data Kilde B")]
    end
    subgraph "Internet"
        S3 <-->|"Web API'er"| D3[("Fjern\Tjenester")]
    end
```
- **MCP Hosts**: Programmer som VSCode, Claude Desktop, IDE'er eller AI-værktøjer, der ønsker at tilgå data via MCP  
- **MCP Clients**: Protokolklienter, der opretholder 1:1-forbindelser med servere  
- **MCP Servers**: Letvægtsprogrammer, der hver eksponerer specifikke funktioner gennem den standardiserede Model Context Protocol  
- **Lokale datakilder**: Din computers filer, databaser og tjenester, som MCP-servere sikkert kan tilgå  
- **Fjernservices**: Eksterne systemer tilgængelige over internettet, som MCP-servere kan forbinde til via API'er.

MCP-protokollen er en udviklende standard, der bruger datobaseret versionsstyring (YYYY-MM-DD format). Den nuværende protokolversion er **2025-11-25**. Du kan se de seneste opdateringer til [protokolspecifikationen](https://modelcontextprotocol.io/specification/2025-11-25/)

### 1. Hosts

I Model Context Protocol (MCP) er **Hosts** AI-applikationer, der fungerer som det primære interface, hvorigennem brugere interagerer med protokollen. Hosts koordinerer og administrerer forbindelser til flere MCP-servere ved at oprette dedikerede MCP-klienter for hver serverforbindelse. Eksempler på Hosts inkluderer:

- **AI-applikationer**: Claude Desktop, Visual Studio Code, Claude Code  
- **Udviklingsmiljøer**: IDE'er og kodeeditorer med MCP-integration  
- **Specialbyggede applikationer**: Formålsbyggede AI-agenter og værktøjer

**Hosts** er applikationer, der koordinerer AI-modelinteraktioner. De:

- **Orkestrerer AI-modeller**: Udfører eller interagerer med LLM'er for at generere svar og koordinere AI-arbejdsgange  
- **Administrerer klientforbindelser**: Opretter og vedligeholder én MCP-klient per MCP-serverforbindelse  
- **Kontrollerer brugergrænsefladen**: Håndterer samtaleflow, brugerinteraktioner og præsentation af svar  
- **Håndhæver sikkerhed**: Kontrollerer tilladelser, sikkerhedsbegrænsninger og autentificering  
- **Håndterer brugersamtykke**: Administrerer brugerens godkendelse til datadeling og værktøjsudførelse

### 2. Clients

**Clients** er essentielle komponenter, der opretholder dedikerede én-til-én-forbindelser mellem Hosts og MCP-servere. Hver MCP-klient instantieres af Host for at forbinde til en specifik MCP-server, hvilket sikrer organiserede og sikre kommunikationskanaler. Flere klienter gør det muligt for Hosts at forbinde til flere servere samtidigt.

**Clients** er forbindelseskomponenter inden for host-applikationen. De:

- **Protokolkommunikation**: Sender JSON-RPC 2.0-forespørgsler til servere med prompts og instruktioner  
- **Kapabilitetsforhandling**: Forhandler understøttede funktioner og protokolversioner med servere under initialisering  
- **Værktøjsudførelse**: Håndterer værktøjsudførelsesanmodninger fra modeller og behandler svar  
- **Real-time opdateringer**: Håndterer notifikationer og realtidsopdateringer fra servere  
- **Svarbehandling**: Behandler og formaterer serversvar til visning for brugere

### 3. Servers

**Servers** er programmer, der leverer kontekst, værktøjer og funktioner til MCP-klienter. De kan køre lokalt (på samme maskine som Host) eller eksternt (på eksterne platforme) og er ansvarlige for at håndtere klientanmodninger og levere strukturerede svar. Servere eksponerer specifik funktionalitet gennem den standardiserede Model Context Protocol.

**Servers** er tjenester, der leverer kontekst og funktioner. De:

- **Funktionregistrering**: Registrerer og eksponerer tilgængelige primitive (ressourcer, prompts, værktøjer) til klienter  
- **Forespørgselsbehandling**: Modtager og udfører værktøjskald, ressourceanmodninger og promptanmodninger fra klienter  
- **Kontekstlevering**: Leverer kontekstuel information og data for at forbedre modelsvar  
- **Tilstandsstyring**: Vedligeholder sessionsstatus og håndterer tilstandsfulde interaktioner efter behov  
- **Real-time notifikationer**: Sender notifikationer om kapabilitetsændringer og opdateringer til tilsluttede klienter

Servere kan udvikles af alle for at udvide modelkapabiliteter med specialiseret funktionalitet, og de understøtter både lokale og fjernudrulningsscenarier.

### 4. Server Primitives

Servere i Model Context Protocol (MCP) leverer tre kerne-**primitive**, der definerer de fundamentale byggesten for rige interaktioner mellem klienter, hosts og sprogmodeller. Disse primitive specificerer typerne af kontekstuel information og handlinger, der er tilgængelige gennem protokollen.

MCP-servere kan eksponere enhver kombination af følgende tre kerneprimitive:

#### Ressourcer

**Ressourcer** er datakilder, der leverer kontekstuel information til AI-applikationer. De repræsenterer statisk eller dynamisk indhold, der kan forbedre modelforståelse og beslutningstagning:

- **Kontekstuel data**: Struktureret information og kontekst til AI-modelkonsum  
- **Vidensbaser**: Dokumentarkiver, artikler, manualer og forskningspapirer  
- **Lokale datakilder**: Filer, databaser og lokal systeminformation  
- **Ekstern data**: API-svar, webservices og fjernsystemdata  
- **Dynamisk indhold**: Realtidsdata, der opdateres baseret på eksterne forhold

Ressourcer identificeres ved URI'er og understøtter opdagelse via `resources/list` og hentning via `resources/read` metoder:

```text
file://documents/project-spec.md
database://production/users/schema
api://weather/current
```

#### Prompts

**Prompts** er genanvendelige skabeloner, der hjælper med at strukturere interaktioner med sprogmodeller. De leverer standardiserede interaktionsmønstre og skabelonbaserede arbejdsgange:

- **Skabelonbaserede interaktioner**: Forudstrukturerede beskeder og samtalestartere  
- **Arbejdsgangsskabeloner**: Standardiserede sekvenser til almindelige opgaver og interaktioner  
- **Få-skud-eksempler**: Eksempelbaserede skabeloner til modelinstruktion  
- **Systemprompts**: Grundlæggende prompts, der definerer modeladfærd og kontekst  
- **Dynamiske skabeloner**: Parameteriserede prompts, der tilpasses specifikke kontekster

Prompts understøtter variabelsubstitution og kan opdages via `prompts/list` og hentes med `prompts/get`:

```markdown
Generate a {{task_type}} for {{product}} targeting {{audience}} with the following requirements: {{requirements}}
```

#### Værktøjer

**Værktøjer** er eksekverbare funktioner, som AI-modeller kan påkalde for at udføre specifikke handlinger. De repræsenterer "verberne" i MCP-økosystemet, der gør det muligt for modeller at interagere med eksterne systemer:

- **Eksekverbare funktioner**: Diskrete operationer, som modeller kan påkalde med specifikke parametre  
- **Integration med eksterne systemer**: API-kald, databaseforespørgsler, filoperationer, beregninger  
- **Unik identitet**: Hvert værktøj har et særskilt navn, beskrivelse og parameterskema  
- **Struktureret I/O**: Værktøjer accepterer validerede parametre og returnerer strukturerede, typede svar  
- **Handlingskapabiliteter**: Gør det muligt for modeller at udføre virkelige handlinger og hente live data

Værktøjer defineres med JSON Schema til parameter-validering og opdages via `tools/list` og eksekveres via `tools/call`:

```typescript
server.tool(
  "search_products", 
  {
    query: z.string().describe("Search query for products"),
    category: z.string().optional().describe("Product category filter"),
    max_results: z.number().default(10).describe("Maximum results to return")
  }, 
  async (params) => {
    // Udfør søgning og returner strukturerede resultater
    return await productService.search(params);
  }
);
```

## Klientprimitive

I Model Context Protocol (MCP) kan **klienter** eksponere primitive, der gør det muligt for servere at anmode om yderligere kapabiliteter fra host-applikationen. Disse klient-side primitive tillader rigere, mere interaktive serverimplementeringer, der kan tilgå AI-modelkapabiliteter og brugerinteraktioner.

### Sampling

**Sampling** tillader servere at anmode om sprogmodelkompletteringer fra klientens AI-applikation. Denne primitive gør det muligt for servere at tilgå LLM-kapabiliteter uden at indlejre deres egne modelafhængigheder:

- **Modeluafhængig adgang**: Servere kan anmode om kompletteringer uden at inkludere LLM SDK'er eller håndtere modeladgang  
- **Serverinitieret AI**: Gør det muligt for servere autonomt at generere indhold ved hjælp af klientens AI-model  
- **Rekursive LLM-interaktioner**: Understøtter komplekse scenarier, hvor servere har brug for AI-assistance til behandling  
- **Dynamisk indholdsgenerering**: Tillader servere at skabe kontekstuelle svar ved hjælp af hostens model

Sampling initieres gennem `sampling/complete` metoden, hvor servere sender kompletteringsanmodninger til klienter.

### Elicitation

**Elicitation** gør det muligt for servere at anmode om yderligere information eller bekræftelse fra brugere via klientgrænsefladen:

- **Brugerinputanmodninger**: Servere kan bede om yderligere information, når det er nødvendigt for værktøjsudførelse  
- **Bekræftelsesdialoger**: Anmoder om brugerens godkendelse til følsomme eller betydningsfulde operationer  
- **Interaktive arbejdsgange**: Gør det muligt for servere at skabe trin-for-trin brugerinteraktioner  
- **Dynamisk parameterindsamling**: Indsamler manglende eller valgfrie parametre under værktøjsudførelse

Elicitation-anmodninger foretages ved hjælp af `elicitation/request` metoden for at indsamle brugerinput via klientens interface.

### Logning

**Logning** tillader servere at sende strukturerede logbeskeder til klienter til debugging, overvågning og operationel synlighed:

- **Debugging-support**: Gør det muligt for servere at levere detaljerede eksekveringslogs til fejlfinding  
- **Operationel overvågning**: Sender statusopdateringer og ydelsesmetrikker til klienter  
- **Fejlrapportering**: Leverer detaljeret fejlkontekst og diagnostisk information  
- **Audit-trails**: Opretter omfattende logfiler over serveroperationer og beslutninger

Logbeskeder sendes til klienter for at give gennemsigtighed i serveroperationer og lette debugging.

## Informationsflow i MCP

Model Context Protocol (MCP) definerer et struktureret informationsflow mellem hosts, klienter, servere og modeller. Forståelse af dette flow hjælper med at klarlægge, hvordan brugerforespørgsler behandles, og hvordan eksterne værktøjer og data integreres i modelsvar.

- **Host initierer forbindelse**  
  Host-applikationen (såsom en IDE eller chatinterface) etablerer en forbindelse til en MCP-server, typisk via STDIO, WebSocket eller en anden understøttet transport.

- **Kapabilitetsforhandling**  
  Klienten (indlejret i hosten) og serveren udveksler information om deres understøttede funktioner, værktøjer, ressourcer og protokolversioner. Dette sikrer, at begge parter forstår, hvilke kapabiliteter der er tilgængelige for sessionen.

- **Brugerforespørgsel**  
  Brugeren interagerer med hosten (f.eks. indtaster en prompt eller kommando). Hosten indsamler dette input og sender det til klienten til behandling.

- **Brug af ressource eller værktøj**  
  - Klienten kan anmode om yderligere kontekst eller ressourcer fra serveren (såsom filer, databaseposter eller vidensbaseartikler) for at berige modellens forståelse.  
  - Hvis modellen vurderer, at et værktøj er nødvendigt (f.eks. for at hente data, udføre en beregning eller kalde en API), sender klienten en værktøjsanmodning til serveren med angivelse af værktøjets navn og parametre.

- **Serverudførelse**  
  Serveren modtager ressource- eller værktøjsanmodningen, udfører de nødvendige operationer (såsom at køre en funktion, forespørge en database eller hente en fil) og returnerer resultaterne til klienten i et struktureret format.

- **Svargenerering**  
  Klienten integrerer serverens svar (ressourcedata, værktøjsoutput osv.) i den igangværende modelinteraktion. Modellen bruger disse oplysninger til at generere et omfattende og kontekstuelt relevant svar.

- **Resultatpræsentation**  
  Hosten modtager det endelige output fra klienten og præsenterer det for brugeren, ofte inklusive både modellens genererede tekst og eventuelle resultater fra værktøjsudførelser eller ressourceopslag.

Dette flow gør det muligt for MCP at understøtte avancerede, interaktive og kontekstbevidste AI-applikationer ved sømløst at forbinde modeller med eksterne værktøjer og datakilder.

## Protokolarkitektur & lag

MCP består af to distinkte arkitekturlag, der arbejder sammen for at levere en komplet kommunikationsramme:

### Datalag

**Datalaget** implementerer den kerne MCP-protokol ved hjælp af **JSON-RPC 2.0** som fundament. Dette lag definerer beskedstruktur, semantik og interaktionsmønstre:

#### Kernekomponenter:

- **JSON-RPC 2.0 Protokol**: Al kommunikation bruger standardiseret JSON-RPC 2.0 beskedformat til metodekald, svar og notifikationer
- **Livscyklusstyring**: Håndterer forbindelsesinitialisering, kapabilitetsforhandling og sessionsafslutning mellem klienter og servere  
- **Serverprimitiver**: Muliggør, at servere kan levere kernefunktionalitet gennem værktøjer, ressourcer og prompts  
- **Klientprimitiver**: Muliggør, at servere kan anmode om sampling fra LLM'er, fremkalde brugerinput og sende logbeskeder  
- **Real-time Notifikationer**: Understøtter asynkrone notifikationer for dynamiske opdateringer uden polling  

#### Nøglefunktioner:

- **Protokolversionsforhandling**: Bruger datobaseret versionering (ÅÅÅÅ-MM-DD) for at sikre kompatibilitet  
- **Kapabilitetsopdagelse**: Klienter og servere udveksler understøttede funktionsoplysninger under initialisering  
- **Stateful Sessions**: Opretholder forbindelsesstatus på tværs af flere interaktioner for kontekstuel kontinuitet  

### Transportlag

**Transportlaget** styrer kommunikationskanaler, beskedindramning og autentificering mellem MCP-deltagere:

#### Understøttede transportmekanismer:

1. **STDIO Transport**:  
   - Bruger standard input/output-strømme til direkte proceskommunikation  
   - Optimalt til lokale processer på samme maskine uden netværksomkostninger  
   - Almindeligt anvendt til lokale MCP-serverimplementeringer  

2. **Streambar HTTP Transport**:  
   - Bruger HTTP POST til klient-til-server beskeder  
   - Valgfri Server-Sent Events (SSE) til server-til-klient streaming  
   - Muliggør fjernserverkommunikation på tværs af netværk  
   - Understøtter standard HTTP-autentificering (bearer tokens, API-nøgler, brugerdefinerede headers)  
   - MCP anbefaler OAuth til sikker tokenbaseret autentificering  

#### Transportabstraktion:

Transportlaget abstraherer kommunikationsdetaljer fra datalaget, hvilket muliggør samme JSON-RPC 2.0 beskedformat på tværs af alle transportmekanismer. Denne abstraktion tillader applikationer at skifte problemfrit mellem lokale og fjernservere.

### Sikkerhedsovervejelser

MCP-implementeringer skal overholde flere kritiske sikkerhedsprincipper for at sikre sikre, pålidelige og trygge interaktioner på tværs af alle protokoloperationer:

- **Brugersamtykke og kontrol**: Brugere skal give eksplicit samtykke, før data tilgås eller operationer udføres. De skal have klar kontrol over, hvilke data der deles, og hvilke handlinger der autoriseres, understøttet af intuitive brugergrænseflader til gennemgang og godkendelse af aktiviteter.

- **Dataprivatliv**: Brugerdata må kun eksponeres med eksplicit samtykke og skal beskyttes af passende adgangskontroller. MCP-implementeringer skal forhindre uautoriseret dataoverførsel og sikre, at privatliv opretholdes gennem alle interaktioner.

- **Værktøjssikkerhed**: Før ethvert værktøj påkaldes, kræves eksplicit brugersamtykke. Brugere skal have en klar forståelse af hvert værktøjs funktionalitet, og robuste sikkerhedsgrænser skal håndhæves for at forhindre utilsigtet eller usikker værktøjsudførelse.

Ved at følge disse sikkerhedsprincipper sikrer MCP brugerens tillid, privatliv og sikkerhed på tværs af alle protokolinteraktioner, samtidig med at kraftfulde AI-integrationer muliggøres.

## Kodeeksempler: Nøglekomponenter

Nedenfor er kodeeksempler i flere populære programmeringssprog, der illustrerer, hvordan man implementerer nøglekomponenter og værktøjer til MCP-servere.

### .NET Eksempel: Oprettelse af en simpel MCP-server med værktøjer

Her er et praktisk .NET-kodeeksempel, der demonstrerer, hvordan man implementerer en simpel MCP-server med brugerdefinerede værktøjer. Dette eksempel viser, hvordan man definerer og registrerer værktøjer, håndterer forespørgsler og forbinder serveren ved hjælp af Model Context Protocol.

```csharp
using System;
using System.Threading.Tasks;
using ModelContextProtocol.Server;
using ModelContextProtocol.Server.Transport;
using ModelContextProtocol.Server.Tools;

public class WeatherServer
{
    public static async Task Main(string[] args)
    {
        // Create an MCP server
        var server = new McpServer(
            name: "Weather MCP Server",
            version: "1.0.0"
        );
        
        // Register our custom weather tool
        server.AddTool<string, WeatherData>("weatherTool", 
            description: "Gets current weather for a location",
            execute: async (location) => {
                // Call weather API (simplified)
                var weatherData = await GetWeatherDataAsync(location);
                return weatherData;
            });
        
        // Connect the server using stdio transport
        var transport = new StdioServerTransport();
        await server.ConnectAsync(transport);
        
        Console.WriteLine("Weather MCP Server started");
        
        // Keep the server running until process is terminated
        await Task.Delay(-1);
    }
    
    private static async Task<WeatherData> GetWeatherDataAsync(string location)
    {
        // This would normally call a weather API
        // Simplified for demonstration
        await Task.Delay(100); // Simulate API call
        return new WeatherData { 
            Temperature = 72.5,
            Conditions = "Sunny",
            Location = location
        };
    }
}

public class WeatherData
{
    public double Temperature { get; set; }
    public string Conditions { get; set; }
    public string Location { get; set; }
}
```

### Java Eksempel: MCP-serverkomponenter

Dette eksempel demonstrerer den samme MCP-server og værktøjsregistrering som .NET-eksemplet ovenfor, men implementeret i Java.

```java
import io.modelcontextprotocol.server.McpServer;
import io.modelcontextprotocol.server.McpToolDefinition;
import io.modelcontextprotocol.server.transport.StdioServerTransport;
import io.modelcontextprotocol.server.tool.ToolExecutionContext;
import io.modelcontextprotocol.server.tool.ToolResponse;

public class WeatherMcpServer {
    public static void main(String[] args) throws Exception {
        // Opret en MCP-server
        McpServer server = McpServer.builder()
            .name("Weather MCP Server")
            .version("1.0.0")
            .build();
            
        // Registrer et vejrværktøj
        server.registerTool(McpToolDefinition.builder("weatherTool")
            .description("Gets current weather for a location")
            .parameter("location", String.class)
            .execute((ToolExecutionContext ctx) -> {
                String location = ctx.getParameter("location", String.class);
                
                // Hent vejrdata (forenklet)
                WeatherData data = getWeatherData(location);
                
                // Returner formateret svar
                return ToolResponse.content(
                    String.format("Temperature: %.1f°F, Conditions: %s, Location: %s", 
                    data.getTemperature(), 
                    data.getConditions(), 
                    data.getLocation())
                );
            })
            .build());
        
        // Forbind serveren ved hjælp af stdio-transport
        try (StdioServerTransport transport = new StdioServerTransport()) {
            server.connect(transport);
            System.out.println("Weather MCP Server started");
            // Hold serveren kørende indtil processen afsluttes
            Thread.currentThread().join();
        }
    }
    
    private static WeatherData getWeatherData(String location) {
        // Implementeringen ville kalde en vejr-API
        // Forenklet til eksemplificeringsformål
        return new WeatherData(72.5, "Sunny", location);
    }
}

class WeatherData {
    private double temperature;
    private String conditions;
    private String location;
    
    public WeatherData(double temperature, String conditions, String location) {
        this.temperature = temperature;
        this.conditions = conditions;
        this.location = location;
    }
    
    public double getTemperature() {
        return temperature;
    }
    
    public String getConditions() {
        return conditions;
    }
    
    public String getLocation() {
        return location;
    }
}
```

### Python Eksempel: Opbygning af en MCP-server

Dette eksempel bruger fastmcp, så sørg venligst for at installere det først:

```python
pip install fastmcp
```
Kodeeksempel:

```python
#!/usr/bin/env python3
import asyncio
from fastmcp import FastMCP
from fastmcp.transports.stdio import serve_stdio

# Opret en FastMCP-server
mcp = FastMCP(
    name="Weather MCP Server",
    version="1.0.0"
)

@mcp.tool()
def get_weather(location: str) -> dict:
    """Gets current weather for a location."""
    return {
        "temperature": 72.5,
        "conditions": "Sunny",
        "location": location
    }

# Alternativ tilgang ved brug af en klasse
class WeatherTools:
    @mcp.tool()
    def forecast(self, location: str, days: int = 1) -> dict:
        """Gets weather forecast for a location for the specified number of days."""
        return {
            "location": location,
            "forecast": [
                {"day": i+1, "temperature": 70 + i, "conditions": "Partly Cloudy"}
                for i in range(days)
            ]
        }

# Registrer klasseværktøjer
weather_tools = WeatherTools()

# Start serveren
if __name__ == "__main__":
    asyncio.run(serve_stdio(mcp))
```

### JavaScript Eksempel: Oprettelse af en MCP-server

Dette eksempel viser oprettelse af en MCP-server i JavaScript og hvordan man registrerer to vejrværktøjer.

```javascript
// Brug af den officielle Model Context Protocol SDK
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod"; // Til parameter validering

// Opret en MCP server
const server = new McpServer({
  name: "Weather MCP Server",
  version: "1.0.0"
});

// Definer et vejrværktøj
server.tool(
  "weatherTool",
  {
    location: z.string().describe("The location to get weather for")
  },
  async ({ location }) => {
    // Dette ville normalt kalde en vejr-API
    // Forenklet til demonstration
    const weatherData = await getWeatherData(location);
    
    return {
      content: [
        { 
          type: "text", 
          text: `Temperature: ${weatherData.temperature}°F, Conditions: ${weatherData.conditions}, Location: ${weatherData.location}` 
        }
      ]
    };
  }
);

// Definer et prognoseværktøj
server.tool(
  "forecastTool",
  {
    location: z.string(),
    days: z.number().default(3).describe("Number of days for forecast")
  },
  async ({ location, days }) => {
    // Dette ville normalt kalde en vejr-API
    // Forenklet til demonstration
    const forecast = await getForecastData(location, days);
    
    return {
      content: [
        { 
          type: "text", 
          text: `${days}-day forecast for ${location}: ${JSON.stringify(forecast)}` 
        }
      ]
    };
  }
);

// Hjælpefunktioner
async function getWeatherData(location) {
  // Simuler API-kald
  return {
    temperature: 72.5,
    conditions: "Sunny",
    location: location
  };
}

async function getForecastData(location, days) {
  // Simuler API-kald
  return Array.from({ length: days }, (_, i) => ({
    day: i + 1,
    temperature: 70 + Math.floor(Math.random() * 10),
    conditions: i % 2 === 0 ? "Sunny" : "Partly Cloudy"
  }));
}

// Forbind serveren ved hjælp af stdio transport
const transport = new StdioServerTransport();
server.connect(transport).catch(console.error);

console.log("Weather MCP Server started");
```

Dette JavaScript-eksempel demonstrerer, hvordan man opretter en MCP-klient, der forbinder til en server, sender en prompt og behandler svaret inklusive eventuelle værktøjskald, der blev foretaget.

## Sikkerhed og autorisation

MCP inkluderer flere indbyggede koncepter og mekanismer til håndtering af sikkerhed og autorisation gennem hele protokollen:

1. **Værktøjstilladelseskontrol**:  
   Klienter kan specificere, hvilke værktøjer en model må bruge under en session. Dette sikrer, at kun eksplicit autoriserede værktøjer er tilgængelige, hvilket reducerer risikoen for utilsigtede eller usikre operationer. Tilladelser kan konfigureres dynamisk baseret på brugerpræferencer, organisationspolitikker eller konteksten for interaktionen.

2. **Autentificering**:  
   Servere kan kræve autentificering, før adgang til værktøjer, ressourcer eller følsomme operationer gives. Dette kan involvere API-nøgler, OAuth-tokens eller andre autentificeringsordninger. Korrekt autentificering sikrer, at kun betroede klienter og brugere kan påkalde serverfunktioner.

3. **Validering**:  
   Parameter-validering håndhæves for alle værktøjspåkalder. Hvert værktøj definerer forventede typer, formater og begrænsninger for sine parametre, og serveren validerer indkommende forespørgsler i overensstemmelse hermed. Dette forhindrer fejlbehæftet eller ondsindet input i at nå værktøjsimplementeringerne og hjælper med at opretholde operationernes integritet.

4. **Ratebegrænsning**:  
   For at forhindre misbrug og sikre fair brug af serverressourcer kan MCP-servere implementere ratebegrænsning for værktøjskald og ressourceadgang. Ratebegrænsninger kan anvendes pr. bruger, pr. session eller globalt og hjælper med at beskytte mod denial-of-service-angreb eller overdreven ressourceforbrug.

Ved at kombinere disse mekanismer giver MCP et sikkert fundament for integration af sprogmodeller med eksterne værktøjer og datakilder, samtidig med at brugere og udviklere får detaljeret kontrol over adgang og brug.

## Protokolbeskeder & kommunikationsflow

MCP-kommunikation bruger strukturerede **JSON-RPC 2.0** beskeder for at muliggøre klare og pålidelige interaktioner mellem værter, klienter og servere. Protokollen definerer specifikke beskedmønstre for forskellige typer operationer:

### Kernebeskedtyper:

#### **Initialiseringsbeskeder**
- **`initialize` Request**: Etablerer forbindelse og forhandler protokolversion og kapabiliteter  
- **`initialize` Response**: Bekræfter understøttede funktioner og serverinformation  
- **`notifications/initialized`**: Signaliserer, at initialisering er fuldført, og sessionen er klar  

#### **Opdagelsesbeskeder**
- **`tools/list` Request**: Opdager tilgængelige værktøjer fra serveren  
- **`resources/list` Request**: Lister tilgængelige ressourcer (datakilder)  
- **`prompts/list` Request**: Henter tilgængelige promptskabeloner  

#### **Eksekveringsbeskeder**  
- **`tools/call` Request**: Udfører et specifikt værktøj med angivne parametre  
- **`resources/read` Request**: Henter indhold fra en specifik ressource  
- **`prompts/get` Request**: Henter en promptskabelon med valgfrie parametre  

#### **Klientsidebeskeder**
- **`sampling/complete` Request**: Server anmoder om LLM-komplettering fra klienten  
- **`elicitation/request`**: Server anmoder om brugerinput via klientgrænsefladen  
- **Logningsbeskeder**: Server sender strukturerede logbeskeder til klienten  

#### **Notifikationsbeskeder**
- **`notifications/tools/list_changed`**: Server underretter klient om ændringer i værktøjslisten  
- **`notifications/resources/list_changed`**: Server underretter klient om ændringer i ressourcelisten  
- **`notifications/prompts/list_changed`**: Server underretter klient om ændringer i promptlisten  

### Beskedstruktur:

Alle MCP-beskeder følger JSON-RPC 2.0 format med:  
- **Forespørgselsbeskeder**: Indeholder `id`, `method` og valgfrie `params`  
- **Svarbeskeder**: Indeholder `id` og enten `result` eller `error`  
- **Notifikationsbeskeder**: Indeholder `method` og valgfrie `params` (ingen `id` eller svar forventes)  

Denne strukturerede kommunikation sikrer pålidelige, sporbare og udvidelige interaktioner, der understøtter avancerede scenarier som realtidsopdateringer, værktøjskæder og robust fejlhåndtering.

## Vigtige pointer

- **Arkitektur**: MCP bruger en klient-server arkitektur, hvor værter håndterer flere klientforbindelser til servere  
- **Deltagere**: Økosystemet inkluderer værter (AI-applikationer), klienter (protokolforbindelser) og servere (kapabilitetsudbydere)  
- **Transportmekanismer**: Kommunikation understøtter STDIO (lokal) og Streambar HTTP med valgfri SSE (fjern)  
- **Kerneprimitiver**: Servere eksponerer værktøjer (eksekverbare funktioner), ressourcer (datakilder) og prompts (skabeloner)  
- **Klientprimitiver**: Servere kan anmode om sampling (LLM-kompletteringer), elicitation (brugerinput) og logning fra klienter  
- **Protokolgrundlag**: Bygget på JSON-RPC 2.0 med datobaseret versionering (nuværende: 2025-11-25)  
- **Real-time kapabiliteter**: Understøtter notifikationer til dynamiske opdateringer og realtids-synkronisering  
- **Sikkerhed først**: Eksplicit brugersamtykke, dataprivatlivsbeskyttelse og sikker transport er kernekrav  

## Øvelse

Design et simpelt MCP-værktøj, der ville være nyttigt i dit domæne. Definér:  
1. Hvad værktøjet skal hedde  
2. Hvilke parametre det skal acceptere  
3. Hvilket output det skal returnere  
4. Hvordan en model kunne bruge dette værktøj til at løse brugerproblemer  

---

## Hvad er næste

Næste: [Kapitel 2: Sikkerhed](../02-Security/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
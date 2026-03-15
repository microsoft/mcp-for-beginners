# Praktisk Implementering

[![Sådan bygger, tester og deployer du MCP-apps med rigtige værktøjer og workflows](../../../translated_images/da/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klik på billedet ovenfor for at se video af denne lektion)_

Praktisk implementering er, hvor kraften i Model Context Protocol (MCP) bliver håndgribelig. Mens det er vigtigt at forstå teorien og arkitekturen bag MCP, opstår den reelle værdi, når du anvender disse koncepter til at bygge, teste og deploye løsninger, der løser virkelige problemer. Dette kapitel bygger bro mellem konceptuel viden og praktisk udvikling og guider dig gennem processen med at bringe MCP-baserede applikationer til live.

Uanset om du udvikler intelligente assistenter, integrerer AI i forretningsarbejdsgange eller bygger tilpassede værktøjer til databehandling, giver MCP en fleksibel grundlag. Dets sprog-agnostiske design og officielle SDK'er til populære programmeringssprog gør det tilgængeligt for en bred vifte af udviklere. Ved at udnytte disse SDK'er kan du hurtigt prototype, iterere og skalere dine løsninger på tværs af forskellige platforme og miljøer.

I de følgende afsnit finder du praktiske eksempler, eksempel-kode og deploymentsstrategier, der viser, hvordan du implementerer MCP i C#, Java med Spring, TypeScript, JavaScript og Python. Du lærer også, hvordan du fejlfinder og tester dine MCP-servere, håndterer API'er og deployer løsninger til skyen ved hjælp af Azure. Disse praktiske ressourcer er designet til at accelerere din læring og hjælpe dig med at bygge robuste, produktionsklare MCP-applikationer med selvtillid.

## Oversigt

Denne lektion fokuserer på praktiske aspekter af MCP-implementering på tværs af flere programmeringssprog. Vi vil udforske, hvordan man bruger MCP SDK'er i C#, Java med Spring, TypeScript, JavaScript og Python til at bygge robuste applikationer, fejlsøge og teste MCP-servere og skabe genanvendelige ressourcer, prompts og værktøjer.

## Læringsmål

Efter denne lektion vil du kunne:

- Implementere MCP-løsninger ved hjælp af officielle SDK'er i forskellige programmeringssprog
- Fejlsøge og teste MCP-servere systematisk
- Oprette og bruge serverfunktioner (Ressourcer, Prompter og Værktøjer)
- Designe effektive MCP-workflows til komplekse opgaver
- Optimere MCP-implementeringer for ydeevne og pålidelighed

## Officielle SDK-ressourcer

Model Context Protocol tilbyder officielle SDK'er til flere sprog (i overensstemmelse med [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java med Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Bemærk:** kræver afhængighed af [Project Reactor](https://projectreactor.io). (Se [diskussions-issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Arbejde med MCP SDK'er

Dette afsnit giver praktiske eksempler på implementering af MCP på tværs af flere programmeringssprog. Du kan finde eksempel-kode i `samples`-mappen organiseret efter sprog.

### Tilgængelige eksempler

Repositoryet indeholder [eksempelimplementeringer](../../../04-PracticalImplementation/samples) i følgende sprog:

- [C#](./samples/csharp/README.md)
- [Java med Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Hvert eksempel demonstrerer nøglekoncepter og implementeringsmønstre for MCP for det specifikke sprog og økosystem.

### Praktiske guider

Yderligere guider til praktisk MCP-implementering:

- [Pagination og store resultatsæt](./pagination/README.md) - Håndtering af cursor-baseret pagination for værktøjer, ressourcer og store datasæt

## Centrale serverfunktioner

MCP-servere kan implementere enhver kombination af følgende funktioner:

### Ressourcer

Ressourcer leverer kontekst og data til brugeren eller AI-modellen:

- Dokumentrepositoryer
- Vidensbaser
- Strukturerede datakilder
- Filsystemer

### Prompter

Prompter er skabelonerede beskeder og workflows til brugere:

- Foruddefinerede samtaleskabeloner
- Guidede interaktionsmønstre
- Specialiserede dialogstrukturer

### Værktøjer

Værktøjer er funktioner, som AI-modellen kan udføre:

- Data-behandlingsværktøjer
- Eksterne API-integrationer
- Beregningskapaciteter
- Søgefunktionalitet

## Eksempelimplementeringer: C# Implementering

Det officielle C# SDK-repository indeholder flere eksempelimplementeringer, der viser forskellige aspekter af MCP:

- **Basic MCP Client**: Simpelt eksempel, der viser, hvordan man opretter en MCP-klient og kalder værktøjer
- **Basic MCP Server**: Minimal serverimplementering med grundlæggende værktøjsregistrering
- **Advanced MCP Server**: Fuldfunktionel server med værktøjsregistrering, autentificering og fejlhåndtering
- **ASP.NET Integration**: Eksempler, der demonstrerer integration med ASP.NET Core
- **Værktøjsimplementeringsmønstre**: Forskellige mønstre til implementering af værktøjer med varierende kompleksitetsniveauer

MCP C# SDK er i preview, og API'er kan ændre sig. Vi vil løbende opdatere denne blog, efterhånden som SDK'en udvikler sig.

### Nøglefunktioner

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Byg din [første MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

For komplette C# implementeringseksempler, besøg det [officielle C# SDK-eksemperepository](https://github.com/modelcontextprotocol/csharp-sdk)

## Eksempelimplementering: Java med Spring Implementering

Java med Spring SDK tilbyder robuste MCP-implementeringsmuligheder med enterprise-grade funktioner.

### Nøglefunktioner

- Spring Framework integration
- Stærk typesikkerhed
- Reaktivt programmeringsunderstøttelse
- Omfattende fejlhåndtering

For et komplet Java med Spring implementeringseksempel, se [Java med Spring eksempel](samples/java/containerapp/README.md) i samples-mappen.

## Eksempelimplementering: JavaScript Implementering

JavaScript SDK tilbyder en let og fleksibel tilgang til MCP-implementering.

### Nøglefunktioner

- Node.js og browserunderstøttelse
- Promise-baseret API
- Nem integration med Express og andre frameworks
- WebSocket-understøttelse til streaming

For et komplet JavaScript implementeringseksempel, se [JavaScript eksempel](samples/javascript/README.md) i samples-mappen.

## Eksempelimplementering: Python Implementering

Python SDK tilbyder en Pythonisk tilgang til MCP-implementering med fremragende ML-framework-integrationer.

### Nøglefunktioner

- Async/await-understøttelse med asyncio
- FastAPI-integration
- Enkel værktøjsregistrering
- Indbygget integration med populære ML-biblioteker

For et komplet Python implementeringseksempel, se [Python eksempel](samples/python/README.md) i samples-mappen.

## API-administration

Azure API Management er en god løsning på, hvordan vi kan sikre MCP-servere. Ideen er at placere en Azure API Management-instans foran din MCP-server og lade den håndtere funktioner, du sandsynligvis vil have brug for såsom:

- rate limiting
- tokenstyring
- overvågning
- belastningsbalancering
- sikkerhed

### Azure Eksempel

Her er et Azure-eksempel, der gør netop det, dvs. [opretter en MCP-server og sikrer den med Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Se hvordan autorisationsflowet foregår i billedet nedenfor:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

I billedet ovenfor sker følgende:

- Autentificering/Autorisation foregår ved hjælp af Microsoft Entra.
- Azure API Management fungerer som en gateway og bruger policies til at dirigere og administrere trafik.
- Azure Monitor logger alle forespørgsler til yderligere analyse.

#### Autorisationsflow

Lad os se nærmere på autorisationsflowet:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorisationsspecifikation

Lær mere om [MCP Authorization specification](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Deploy Remote MCP Server til Azure

Lad os se, om vi kan deploye det eksempel, vi nævnte tidligere:

1. Klon repositoriet

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrer `Microsoft.App` resource provider.

   - Hvis du bruger Azure CLI, kør `az provider register --namespace Microsoft.App --wait`.
   - Hvis du bruger Azure PowerShell, kør `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kør derefter `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` efter noget tid for at tjekke, om registreringen er færdig.

1. Kør denne [azd](https://aka.ms/azd) kommando for at provisionere api management-tjenesten, function app (med kode) og alle andre nødvendige Azure-ressourcer

    ```shell
    azd up
    ```

    Denne kommando skal deploye alle skyressourcerne på Azure

### Test af din server med MCP Inspector

1. I et **nyt terminalvindue**, installer og kør MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Du burde se et interface lignende:

    ![Connect to Node inspector](../../../translated_images/da/connect.141db0b2bd05f096.webp)

1. CTRL klik for at åbne MCP Inspector webappen fra URL'en vist af appen (fx [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Sæt transporttypen til `SSE`
1. Sæt URL'en til din kørende API Management SSE-endpoint vist efter `azd up` og **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **List Tools**. Klik på et værktøj og **Run Tool**.

Hvis alle trin er lykkedes, skulle du nu være forbundet til MCP-serveren og have kunnet kalde et værktøj.

## MCP-servere til Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dette sæt repositories er en quickstart-skabelon til at bygge og deploye tilpassede remote MCP (Model Context Protocol) servere ved hjælp af Azure Functions med Python, C# .NET eller Node/TypeScript.

Samples giver en komplet løsning, der tillader udviklere at:

- Bygge og køre lokalt: Udvikle og fejlsøge en MCP-server på en lokal maskine
- Deploye til Azure: Nem deployment til skyen med en simpel azd up-kommando
- Forbinde fra klienter: Forbinde til MCP-serveren fra forskellige klienter, herunder VS Code's Copilot agent-mode og MCP Inspector værktøjet

### Nøglefunktioner

- Sikkerhed by design: MCP-serveren er sikret med nøgler og HTTPS
- Autentificeringsmuligheder: Understøtter OAuth ved brug af indbygget autentificering og/eller API Management
- Netværk isolation: Muliggør netværksisolation ved brug af Azure Virtual Networks (VNET)
- Serverløs arkitektur: Udnytter Azure Functions for skalerbar, eventdrevet udførelse
- Lokal udvikling: Omfattende support til lokal udvikling og fejlsøgning
- Enkel deployment: Strømlinet deploymentsproces til Azure

Repositoryet inkluderer alle nødvendige konfigurationsfiler, kildekode og infrastrukturoversigter for hurtigt at komme i gang med en produktionsklar MCP-serverimplementering.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Eksempelimplementering af MCP ved hjælp af Azure Functions med Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Eksempelimplementering af MCP ved hjælp af Azure Functions med C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Eksempelimplementering af MCP ved hjælp af Azure Functions med Node/TypeScript.

## Nøglepunkter

- MCP SDK'er tilbyder sprogspecifikke værktøjer til implementering af robuste MCP-løsninger
- Fejlsøgnings- og testprocessen er kritisk for pålidelige MCP-applikationer
- Genanvendelige promptskabeloner muliggør konsistente AI-interaktioner
- Godt designede workflows kan orkestrere komplekse opgaver ved brug af flere værktøjer
- Implementering af MCP-løsninger kræver overvejelse af sikkerhed, ydeevne og fejlhåndtering

## Øvelse

Design en praktisk MCP-workflow, der adresserer et virkeligt problem inden for dit domæne:

1. Identificer 3-4 værktøjer, der ville være nyttige til at løse dette problem
2. Lav et workflow-diagram, der viser, hvordan disse værktøjer interagerer
3. Implementer en basal version af et af værktøjerne ved hjælp af dit foretrukne sprog
4. Opret en promptskabelon, der hjælper modellen med effektivt at anvende dit værktøj

## Yderligere ressourcer

---

## Hvad er Næste

Næste: [Avancerede Emner](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget skal betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
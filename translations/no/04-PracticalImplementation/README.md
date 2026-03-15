# Praktisk implementering

[![Hvordan bygge, teste og distribuere MCP-apper med ekte verktøy og arbeidsflyter](../../../translated_images/no/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klikk på bildet over for å se videoen av denne leksjonen)_

Praktisk implementering er der kraften i Model Context Protocol (MCP) blir håndgripelig. Mens det er viktig å forstå teorien og arkitekturen bak MCP, oppstår den virkelige verdien når du anvender disse konseptene for å bygge, teste og distribuere løsninger som løser virkelige problemer. Dette kapitlet bygger bro mellom konseptuell kunnskap og praktisk utvikling, og veileder deg gjennom prosessen med å bringe MCP-baserte applikasjoner til liv.

Enten du utvikler intelligente assistenter, integrerer AI i forretningsarbeidsflyter, eller bygger tilpassede verktøy for databehandling, gir MCP et fleksibelt fundament. Dets språkagnostiske design og offisielle SDK-er for populære programmeringsspråk gjør det tilgjengelig for et bredt spekter av utviklere. Ved å utnytte disse SDK-ene kan du raskt prototype, iterere og skalere løsningene dine på tvers av forskjellige plattformer og miljøer.

I de følgende seksjonene finner du praktiske eksempler, eksempelkode og distribusjonsstrategier som viser hvordan du implementerer MCP i C#, Java med Spring, TypeScript, JavaScript og Python. Du vil også lære hvordan du feilsøker og tester dine MCP-servere, administrerer API-er og distribuerer løsninger til skyen med Azure. Disse praktiske ressursene er designet for å akselerere læringen og hjelpe deg med å bygge robuste, produksjonsklare MCP-applikasjoner med selvtillit.

## Oversikt

Denne leksjonen fokuserer på praktiske aspekter ved MCP-implementering på flere programmeringsspråk. Vi skal utforske hvordan du bruker MCP SDK-er i C#, Java med Spring, TypeScript, JavaScript og Python for å bygge robuste applikasjoner, feilsøke og teste MCP-servere, samt lage gjenbrukbare ressurser, prompts og verktøy.

## Læringsmål

Innen slutten av denne leksjonen vil du kunne:

- Implementere MCP-løsninger ved hjelp av offisielle SDK-er i ulike programmeringsspråk
- Feilsøke og teste MCP-servere systematisk
- Lage og bruke serverfunksjoner (Ressurser, Prompts og Verktøy)
- Designe effektive MCP-arbeidsflyter for komplekse oppgaver
- Optimere MCP-implementeringer for ytelse og pålitelighet

## Offisielle SDK-ressurser

Model Context Protocol tilbyr offisielle SDK-er for flere språk (i samsvar med [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java med Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Merk:** krever avhengighet til [Project Reactor](https://projectreactor.io). (Se [diskusjonsutgave 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Arbeide med MCP SDK-er

Denne seksjonen gir praktiske eksempler på implementering av MCP på flere programmeringsspråk. Du kan finne eksempelkode i `samples`-mappen organisert etter språk.

### Tilgjengelige eksempler

Repositoryen inkluderer [eksempelimplementeringer](../../../04-PracticalImplementation/samples) i følgende språk:

- [C#](./samples/csharp/README.md)
- [Java med Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Hvert eksempel viser nøkkelkonsepter og implementeringsmønstre for MCP for det spesifikke språket og økosystemet.

### Praktiske guider

Ekstra guider for praktisk MCP-implementering:

- [Paginering og store resultatssett](./pagination/README.md) - Håndterer markørbasert paginering for verktøy, ressurser og store datasett

## Kjernefunksjoner for servere

MCP-servere kan implementere en hvilken som helst kombinasjon av disse funksjonene:

### Ressurser

Ressurser gir kontekst og data for brukeren eller AI-modellen å bruke:

- Dokumentarkiver
- Kunnskapsbaser
- Strukturerte datakilder
- Filsystemer

### Prompts

Prompts er malbaserte meldinger og arbeidsflyter for brukere:

- Forhåndsdefinerte samtalemaler
- Veiledede interaksjonsmønstre
- Spesialiserte dialogstrukturer

### Verktøy

Verktøy er funksjoner som AI-modellen kan utføre:

- Verktøy for databehandling
- Integrasjoner med eksterne API-er
- Beregningskapasiteter
- Søke-funksjonalitet

## Eksempelimplementeringer: C#-implementering

Det offisielle C# SDK-repositoriet inneholder flere eksempelimplementeringer som demonstrerer forskjellige aspekter av MCP:

- **Grunnleggende MCP-klient**: Enkelt eksempel som viser hvordan man lager en MCP-klient og kaller verktøy
- **Grunnleggende MCP-server**: Minimal serverimplementering med grunnleggende verktøyregistrering
- **Avansert MCP-server**: Fullverdig server med verktøyregistrering, autentisering og feilhåndtering
- **ASP.NET-integrasjon**: Eksempler som demonstrerer integrasjon med ASP.NET Core
- **Mønstere for verktøyimplementering**: Ulike mønstre for å implementere verktøy med ulike kompleksitetsnivåer

MCP C# SDK er i forhåndsvisning, og API-er kan endres. Vi vil kontinuerlig oppdatere denne bloggen etter hvert som SDK-en utvikler seg.

### Nøkkelfunksjoner

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Bygg din [første MCP-server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

For komplette C# implementeringseksempler, besøk det [offisielle C# SDK-eksempelrepositoriet](https://github.com/modelcontextprotocol/csharp-sdk)

## Eksempelimplementering: Java med Spring-implementering

Java med Spring SDK tilbyr robuste MCP-implementeringsmuligheter med enterprise-funksjoner.

### Nøkkelfunksjoner

- Spring Framework-integrasjon
- Sterk typesikkerhet
- Støtte for reaktiv programmering
- Omfattende feilhåndtering

For en komplett Java med Spring implementeringseksempel, se [Java med Spring-eksempel](samples/java/containerapp/README.md) i samples-mappen.

## Eksempelimplementering: JavaScript-implementering

JavaScript SDK tilbyr en lettvekts og fleksibel tilnærming til MCP-implementering.

### Nøkkelfunksjoner

- Støtte for Node.js og nettleser
- Promise-basert API
- Enkel integrasjon med Express og andre rammeverk
- WebSocket-støtte for streaming

For en komplett JavaScript implementeringseksempel, se [JavaScript-eksempel](samples/javascript/README.md) i samples-mappen.

## Eksempelimplementering: Python-implementering

Python SDK tilbyr en pythonisk tilnærming til MCP-implementering med utmerket integrasjon med ML-rammeverk.

### Nøkkelfunksjoner

- Async/await-støtte med asyncio
- FastAPI-integrasjon
- Enkel verktøyregistrering
- Native integrasjon med populære ML-biblioteker

For en komplett Python implementeringseksempel, se [Python-eksempel](samples/python/README.md) i samples-mappen.

## API-administrasjon

Azure API Management er et godt svar på hvordan vi kan sikre MCP-servere. Ideen er å sette en Azure API Management-instans foran din MCP-server og la den håndtere funksjoner du sannsynligvis vil ønske som:

- hastighetsbegrensning
- tokenadministrasjon
- overvåkning
- lastbalansering
- sikkerhet

### Azure-eksempel

Her er et Azure-eksempel som gjør akkurat det, altså [oppretter en MCP-server og sikrer den med Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Se hvordan autorisasjonsflyten skjer i bildet under:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

I det foregående bildet skjer følgende:

- Autentisering/autorisasjon utføres ved hjelp av Microsoft Entra.
- Azure API Management fungerer som en gateway og bruker policyer for å styre og administrere trafikk.
- Azure Monitor logger alle forespørsler for videre analyse.

#### Autorisasjonsflyt

La oss se nærmere på autorisasjonsflyten:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorisasjonsspesifikasjon

Lær mer om [MCP autorisasjonsspesifikasjonen](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Distribuer fjern-MCP-server til Azure

La oss se om vi kan distribuere eksemplet vi nevnte tidligere:

1. Klon repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrer `Microsoft.App` ressursleverandør.

   - Hvis du bruker Azure CLI, kjør `az provider register --namespace Microsoft.App --wait`.
   - Hvis du bruker Azure PowerShell, kjør `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kjør deretter `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` etter en stund for å sjekke om registreringen er fullført.

1. Kjør denne [azd](https://aka.ms/azd)-kommandoen for å opprette API-management-tjenesten, funksjonsappen (med kode) og alle andre nødvendige Azure-ressurser

    ```shell
    azd up
    ```

    Denne kommandoen skal distribuere alle skyressurser på Azure

### Test serveren din med MCP Inspector

1. I et **nytt terminalvindu**, installer og kjør MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Du bør se et grensesnitt som dette:

    ![Connect to Node inspector](../../../translated_images/no/connect.141db0b2bd05f096.webp)

1. CTRL-klikk for å laste MCP Inspector web-appen fra URL-en vist av appen (f.eks. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Sett transporttypen til `SSE`
1. Sett URL til ditt kjørende API Management SSE-endepunkt vist etter `azd up` og **Koble til**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **List verktøy**. Klikk på et verktøy og **Kjør verktøy**.  

Hvis alle trinnene har fungert, skal du nå være koblet til MCP-serveren og kunne kalle et verktøy.

## MCP-servere for Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dette settet av repositorier er en hurtigstartmal for å bygge og distribuere tilpassede fjern-MCP (Model Context Protocol) servere ved bruk av Azure Functions med Python, C# .NET eller Node/TypeScript.

Eksemplene gir en komplett løsning som lar utviklere:

- Bygge og kjøre lokalt: Utvikle og feilsøke en MCP-server på en lokal maskin
- Distribuere til Azure: Enkelt distribuere til skyen med en enkel azd up-kommando
- Koble til fra klienter: Koble til MCP-serveren fra ulike klienter inkludert VS Codes Copilot agent modus og MCP Inspector-verktøyet

### Nøkkelfunksjoner

- Sikkerhet ved design: MCP-serveren er sikret med nøkler og HTTPS
- Autentiseringsmuligheter: Støtter OAuth ved bruk av innebygd autentisering og/eller API Management
- Nettverksisolasjon: Tillater nettverksisolasjon ved bruk av Azure Virtual Networks (VNET)
- Serverløs arkitektur: Utnytter Azure Functions for skalerbar, hendelsesdrevet utførelse
- Lokal utvikling: Omfattende støtte for lokal utvikling og feilsøking
- Enkel distribusjon: Strømlinjeformet distribusjonsprosess til Azure

Repositoriet inkluderer alle nødvendige konfigurasjonsfiler, kildekode og infrastrukturoppsett for raskt å komme i gang med en produksjonsklar MCP-serverimplementering.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Eksempelimplementering av MCP ved bruk av Azure Functions med Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Eksempelimplementering av MCP ved bruk av Azure Functions med C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Eksempelimplementering av MCP ved bruk av Azure Functions med Node/TypeScript.

## Viktige punkter

- MCP SDK-er gir språkspesifikke verktøy for å implementere robuste MCP-løsninger
- Feilsøkings- og testprosessen er kritisk for pålitelige MCP-applikasjoner
- Gjenbrukbare prompt-maler muliggjør konsistente AI-interaksjoner
- Godt designede arbeidsflyter kan orkestrere komplekse oppgaver med flere verktøy
- Implementering av MCP-løsninger krever vurdering av sikkerhet, ytelse og feilhåndtering

## Øvelse

Design en praktisk MCP-arbeidsflyt som adresserer et virkelighetsnært problem i ditt domene:

1. Identifiser 3-4 verktøy som ville vært nyttige for å løse dette problemet
2. Lag et arbeidsflytdiagram som viser hvordan disse verktøyene samhandler
3. Implementer en grunnleggende versjon av ett av verktøyene med ditt foretrukne språk
4. Lag en prompt-mal som vil hjelpe modellen å bruke ditt verktøy effektivt

## Ytterligere ressurser

---

## Hva kommer nå

Neste: [Avanserte temaer](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på det opprinnelige språket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
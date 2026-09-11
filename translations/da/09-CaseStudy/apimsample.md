# Case Study: Eksponer REST API i API Management som en MCP-server

Azure API Management er en tjeneste, der leverer en Gateway oven på dine API Endpoints. Måden det fungerer på er, at Azure API Management fungerer som en proxy foran dine API'er og kan beslutte, hvad der skal ske med indkommende forespørgsler.

Ved at bruge det tilføjer du en masse funktioner som:

- **Sikkerhed**, du kan bruge alt fra API-nøgler, JWT til managed identity.
- **Ratebegrænsning**, en fantastisk funktion er at kunne beslutte, hvor mange opkald der går igennem per en bestemt tidsenhed. Dette hjælper med at sikre, at alle brugere får en god oplevelse, og at din tjeneste ikke bliver overbelastet med forespørgsler.
- **Skalering & Load balancing**. Du kan opsætte et antal endpoints til at fordele belastningen, og du kan også beslutte, hvordan du vil "load balance".
- **AI-funktioner som semantisk caching**, tokenbegrænsning og tokenovervågning samt mere. Disse er fremragende funktioner, der forbedrer responstiden samt hjælper dig med at holde styr på dit tokenforbrug. [Læs mere her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol bliver hurtigt en standard for agentiske AI-apps og måder at eksponere værktøjer og data på en ensartet måde. Azure API Management er et naturligt valg, når du har brug for at "styre" API'er. MCP-servere integrerer ofte med andre API'er for at løse forespørgsler til et værktøj, for eksempel. Derfor giver det meget mening at kombinere Azure API Management og MCP.

## Oversigt

I denne specifikke brugssag lærer vi at eksponere API endpoints som en MCP Server. Ved at gøre dette kan vi nemt gøre disse endpoints til en del af en agentisk app samtidig med, at vi udnytter funktionerne fra Azure API Management.

## Nøglefunktioner

- Du vælger de endpoint-metoder, du ønsker eksponeret som værktøjer.
- De ekstra funktioner, du får, afhænger af, hvad du konfigurerer i politiksektionen for dit API. Men her vil vi vise dig, hvordan du kan tilføje ratebegrænsning.

## Fortrin: importér et API

Hvis du allerede har et API i Azure API Management, er det fantastisk, så kan du springe dette trin over. Hvis ikke, kan du tjekke dette link, [import af et API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponer API som MCP Server

For at eksponere API endpoints, følg disse trin:

1. Naviger til Azure Portal og følgende adresse <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Naviger til din API Management instans.

1. I venstremenuen, vælg APIs > MCP Servers > + Opret ny MCP Server.

1. I API vælger du et REST API til at eksponere som en MCP server.

1. Vælg en eller flere API Operationer til at eksponere som værktøjer. Du kan vælge alle operationer eller kun specifikke operationer.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Vælg **Opret**.

1. Naviger til menupunktet **API'er** og **MCP Servers**, du skulle nu se følgende:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er oprettet, og API operationerne er eksponeret som værktøjer. MCP-serveren vises i MCP Servers-panelet. URL-kolonnen viser endpoint'et for MCP-serveren, som du kan kalde til test eller inden for en klientapplikation.

## Valgfrit: Konfigurer politikker

Azure API Management har kernekonceptet politikker, hvor du opsætter forskellige regler for dine endpoints som for eksempel ratebegrænsning eller semantisk caching. Disse politikker defineres i XML.

Sådan kan du opsætte en politik til at ratebegrænse din MCP Server:

1. I portalen, under APIs, vælg **MCP Servers**.

1. Vælg den MCP-server, du oprettede.

1. I venstremenuen, under MCP, vælg **Politikker**.

1. I politikeditoren, tilføj eller rediger de politikker, du ønsker skal gælde for MCP-serverens værktøjer. Politikkerne defineres i XML-format. For eksempel kan du tilføje en politik til at begrænse kald til MCP-serverens værktøjer (i dette eksempel 5 kald per 30 sekunder per client IP-adresse). Her er XML, der vil forårsage ratebegrænsning:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et billede af politikeditoren:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prøv det af

Lad os sikre, at vores MCP Server fungerer som forventet.

> [!NOTE]
> Azure API Management eksponerer i øjeblikket denne server gennem Streamable
> HTTP `/mcp` endpoint. Den ældre HTTP+SSE `/sse` transport er forældet og
> bør kun bruges med ældre klienter.

Til dette vil vi bruge Visual Studio Code og GitHub Copilot i dets Agent-tilstand. Vi tilføjer MCP-serveren til en *mcp.json*. Ved at gøre dette vil Visual Studio Code fungere som klient med agentiske kapaciteter, og slutbrugere vil kunne skrive en prompt og interagere med denne server.

Lad os se hvordan, for at tilføje MCP-serveren i Visual Studio Code:

1. Brug MCP: **Tilføj Server-kommandoen fra Kommandopaletten**.

1. Når du bliver bedt om det, vælg servertypen: **HTTP (HTTP eller Server Sent Events)**.

1. Indtast Streamable HTTP URL'en vist for MCP-serveren i API Management.
    For eksempel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Indtast et server-id efter eget valg. Dette er ikke en vigtig værdi, men det vil hjælpe dig med at huske, hvad denne serverinstans er.

1. Vælg om konfigurationen skal gemmes i dine workspace-indstillinger eller brugerindstillinger.

  - **Workspace-indstillinger** - Serverkonfigurationen gemmes i en .vscode/mcp.json fil, som kun er tilgængelig i det nuværende workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Brugerindstillinger** - Serverkonfigurationen tilføjes til din globale *settings.json* fil og er tilgængelig i alle workspaces. Konfigurationen ser omtrent sådan ud:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du skal også tilføje en konfiguration, et headerfelt for at sikre, at den godkender korrekt mod Azure API Management. Den bruger et header kaldet **Ocp-Apim-Subscription-Key**.

    - Sådan kan du tilføje det til indstillinger:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil medføre, at en prompt vises, som beder om din API-nøgle, som du kan finde i Azure Portalen for din Azure API Management instans.

   - For at tilføje det til *mcp.json* i stedet, kan du tilføje det sådan:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Brug Agent-tilstand

Nu er vi klar i enten indstillinger eller i *.vscode/mcp.json*. Lad os prøve det.

Der burde være et Ikon for Værktøjer som her, hvor de eksponerede værktøjer fra din server er listet:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik på værktøjsikonet, og du skulle se en liste over værktøjer som her:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Indtast en prompt i chatten for at kalde værktøjet. For eksempel, hvis du har valgt et værktøj til at få information om en ordre, kan du spørge agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nu få vist et værktøjsikon, der beder dig fortsætte med at kalde værktøjet. Vælg at fortsætte med at køre værktøjet, og du burde nu se et output som her:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Det du ser ovenfor afhænger af, hvilke værktøjer du har sat op, men idéen er, at du får et tekstbaseret svar som ovenfor**


## Referencer

Her er hvordan du kan lære mere:

- [Tutorial om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python eksempel: Sikker fjern-MCP-servere ved hjælp af Azure API Management (eksperimentel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP klient autorisations-laboratorium](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Brug Azure API Management udvidelsen til VS Code til import og håndtering af API'er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og find fjern-MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Fantastisk repository, der viser mange AI-funktioner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Indeholder workshops ved brug af Azure Portal, hvilket er en god måde at begynde at evaluere AI-funktioner på.

## Hvad er det næste

- Tilbage til: [Case Studies Oversigt](./README.md)
- Næste: [Azure AI Rejseagenter](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
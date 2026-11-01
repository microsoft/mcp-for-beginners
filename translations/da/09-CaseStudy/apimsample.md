# Case Study: Eksponer REST API i API Management som en MCP-server

Azure API Management er en tjeneste, der leverer en Gateway oven på dine API-endpoints. Sådan fungerer det, at Azure API Management agerer som en proxy foran dine API'er og kan beslutte, hvad der skal ske med indkommende forespørgsler.

Ved at bruge det tilføjer du en hel række funktioner som:

- **Sikkerhed**, du kan bruge alt fra API-nøgler, JWT til managed identity.
- **Begrænsning af antal kald**, en stor fordel er muligheden for at bestemme, hvor mange kald der må passere per en bestemt tidsenhed. Dette hjælper med at sikre, at alle brugere får en god oplevelse, og at din tjeneste ikke overbelastes med forespørgsler.
- **Skalering og load balancing**. Du kan opsætte flere endpoints for at fordele belastningen, og du kan også bestemme, hvordan "load balancing" skal foregå.
- **AI-funktioner som semantisk caching**, tokenbegrænsning og tokenovervågning med mere. Disse er fantastiske funktioner, der forbedrer responsiviteten samt hjælper dig med at holde styr på dine token-forbrug. [Læs mere her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol er ved at blive en standard for agentiske AI-apps og hvordan man eksponerer værktøjer og data på en ensartet måde. Azure API Management er et naturligt valg, når du har brug for at "styre" API'er. MCP Servers integrerer ofte med andre API'er for eksempelvis at løse forespørgsler til et værktøj. Derfor giver det god mening at kombinere Azure API Management og MCP.

## Oversigt

I denne specifikke brugssag lærer vi at eksponere API-endpoints som en MCP-server. Ved at gøre dette kan vi nemt gøre disse endpoints til en del af en agentisk app samtidig med, at vi udnytter funktionerne fra Azure API Management.

## Nøglefunktioner

- Du vælger de endpoint-metoder, du ønsker skal eksponeres som værktøjer.
- De ekstra funktioner, du får, afhænger af, hvad du konfigurerer i policy-sektionen for dit API. Men her vil vi vise, hvordan du kan tilføje begrænsning af antal kald.

## Fortrin: importer en API

Hvis du allerede har en API i Azure API Management, er det fint – så kan du springe dette trin over. Hvis ikke, kan du tjekke dette link, [import af en API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponer API som MCP-server

For at eksponere API-endpoints følger vi disse trin:

1. Naviger til Azure Portal og adressen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Naviger til din API Management-instans.

1. Vælg i venstremenuen APIs > MCP Servers > + Opret ny MCP Server.

1. Vælg i API et REST API, som skal eksponeres som en MCP-server.

1. Vælg en eller flere API-operationer, der skal eksponeres som værktøjer. Du kan vælge alle operationer eller kun bestemte operationer.

    ![Vælg metoder til eksponering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Vælg **Opret**.

1. Naviger til menuvalget **APIs** og **MCP Servers**, du burde se følgende:

    ![Se MCP Server i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er oprettet, og API-operationerne er eksponeret som værktøjer. MCP-serveren er listet i MCP Servers-panelet. URL-kolonnen viser endpointet for MCP-serveren, som du kan kalde til test eller fra en klientapplikation.

## Valgfrit: Konfigurer politikker

Azure API Management har kernebegrebet politikker, hvor du kan sætte forskellige regler for dine endpoints, som for eksempel begrænsning af antal kald eller semantisk caching. Disse politikker skrives i XML.

Sådan kan du opsætte en politik til at begrænse antal kald på din MCP-server:

1. I portalen under APIs, vælg **MCP Servers**.

1. Vælg den MCP-server, du oprettede.

1. I venstremenuen under MCP, vælg **Policies**.

1. I policy-editoren tilføj eller rediger de politikker, du ønsker at anvende på MCP-serverens værktøjer. Politikkerne defineres i XML-format. For eksempel kan du tilføje en politik, der begrænser kald til MCP-serverens værktøjer (i dette eksempel 5 kald pr. 30 sekunder per klient-IP-adresse). Her er XML, der vil forårsage denne begrænsning:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et billede af policy-editoren:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prøv det af

Lad os sikre, at vores MCP-server fungerer som tiltænkt.

> [!NOTE]
> Azure API Management eksponerer i øjeblikket denne server via Streamable
> HTTP `/mcp` endpoint. Den ældre HTTP+SSE `/sse` transport er forældet og
> bør kun bruges med legacy-klienter.

Til dette vil vi bruge Visual Studio Code og GitHub Copilot med dets Agent-mode. Vi tilføjer MCP-serveren til en *mcp.json*-fil. På den måde fungerer Visual Studio Code som en klient med agentiske kapaciteter, og slutbrugere kan skrive en prompt og interagere med den pågældende server.

Lad os se, hvordan man tilføjer MCP-serveren i Visual Studio Code:

1. Brug kommandoen MCP: **Add Server fra Command Palette**.

1. Når du bliver bedt om det, vælg servertype: **HTTP (HTTP eller Server Sent Events)**.

1. Indtast den Streamable HTTP-URL, der vises for MCP-serveren i API Management.
    For eksempel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Indtast et valgfrit server-ID. Det er ikke afgørende, men hjælper dig med at huske, hvad denne serverinstans er.

1. Vælg, om konfigurationen skal gemmes i dine workspace-indstillinger eller brugerindstillinger.

    - **Workspace settings** - Serverkonfigurationen gemmes i en `.vscode/mcp.json` fil, som kun er tilgængelig i det aktuelle workspace.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - Serverkonfigurationen tilføjes til din globale *settings.json*-fil og er tilgængelig på tværs af alle workspaces. Konfigurationen ser omtrent således ud:

      ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du skal også tilføje en konfigurationsheader for at sikre, at der autentificeres korrekt mod Azure API Management. Den bruger en header kaldet **Ocp-Apim-Subscription-Key**.

    - Sådan tilføjer du den til indstillinger:


    ![Tilføj header for autentificering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil fremkalde en prompt, der beder dig om API-nøglens værdi, som du kan finde i Azure Portal for din Azure API Management-instans.

   - For at tilføje den til *mcp.json* i stedet, kan du gøre det således:

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

### Brug Agent Mode

Nu er vi sat op enten i indstillinger eller i *.vscode/mcp.json*. Lad os prøve det.

Der burde være et Værktøjer-ikon som dette, hvor de eksponerede værktøjer fra din server er vist:

![Værktøjer fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik på værktøjsikonet, og du burde se en liste over værktøjer som følger:

    ![Værktøjer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Indtast en prompt i chatten for at aktivere værktøjet. For eksempel, hvis du valgte et værktøj til at få oplysninger om en ordre, kan du spørge agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nu blive præsenteret for et værktøjsikon, der spørger, om du vil fortsætte med at kalde værktøjet. Vælg at fortsætte, og du burde nu se et output som dette:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Det, du ser ovenfor, afhænger af, hvilke værktøjer du har sat op, men idéen er, at du får et tekstbaseret svar som ovenfor**


## Referencer

Her kan du lære mere:

- [Tutorial om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python eksempel: Sikker fjern-MCP-servere ved hjælp af Azure API Management (eksperimentelt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP klient-autorisation lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Brug Azure API Management-udvidelsen til VS Code til at importere og administrere API'er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og opdag fjern-MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Fantastisk repo, der viser mange AI-kapaciteter med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Indeholder workshops ved brug af Azure Portal, som er en god måde at starte evaluering af AI-kapaciteter på.

## Hvad nu?

- Tilbage til: [Case Studies Oversigt](./README.md)
- Næste: [Azure AI Rejseagenter](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
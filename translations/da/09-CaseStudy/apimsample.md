# Case Study: Eksponér REST API i API Management som en MCP-server

Azure API Management er en tjeneste, der giver en Gateway oven på dine API-endepunkter. Det fungerer ved, at Azure API Management agerer som en proxy foran dine API'er og kan beslutte, hvad der skal ske med indkommende forespørgsler.

Ved at bruge det får du en lang række funktioner som:

- **Sikkerhed**, du kan bruge alt fra API-nøgler og JWT til managed identity.
- **Hastighedsbegrænsning**, en fantastisk funktion, der gør det muligt at bestemme, hvor mange kald der kan foretages inden for en bestemt tidsenhed. Dette hjælper med at sikre, at alle brugere får en god oplevelse, og at din tjeneste ikke bliver overbelastet med forespørgsler.
- **Skalering og Load balancing**. Du kan opsætte flere endepunkter for at fordele belastningen og også bestemme, hvordan "load balancing" skal foregå.
- **AI-funktioner som semantisk caching**, tokenbegrænsning, tokenovervågning og mere. Disse funktioner forbedrer responsiviteten og hjælper dig med at holde styr på dit tokenforbrug. [Læs mere her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol bliver hurtigt en standard for agentbaserede AI-apps og måden at eksponere værktøjer og data på en konsistent måde. Azure API Management er et naturligt valg, når du skal "administrere" API'er. MCP-servere integrerer ofte med andre API'er for at løse forespørgsler til et værktøj, for eksempel. Derfor giver det god mening at kombinere Azure API Management og MCP.

## Oversigt

I dette specifikke use case vil vi lære at eksponere API-endepunkter som en MCP-server. Ved at gøre dette kan vi nemt gøre disse endepunkter til en del af en agentbaseret app og samtidig udnytte funktionerne fra Azure API Management.

## Nøglefunktioner

- Du vælger de endepunktsmetoder, du vil eksponere som værktøjer.
- De ekstra funktioner, du får, afhænger af, hvad du konfigurerer i politiksektionen for dit API. Her vil vi dog vise, hvordan du kan tilføje hastighedsbegrænsning.

## Forberedelse: Importér et API

Hvis du allerede har et API i Azure API Management, er det fantastisk, og du kan springe dette trin over. Hvis ikke, kan du tjekke dette link: [importere et API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponér API som MCP-server

For at eksponere API-endepunkterne skal vi følge disse trin:

1. Gå til Azure Portal og følgende adresse <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Naviger til din API Management-instans.

1. I venstremenuen skal du vælge **APIs > MCP Servers > + Create new MCP Server**.

1. Under API skal du vælge et REST API, der skal eksponeres som en MCP-server.

1. Vælg en eller flere API-operationer, der skal eksponeres som værktøjer. Du kan vælge alle operationer eller kun specifikke operationer.

    ![Vælg metoder, der skal eksponeres](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Vælg **Create**.

1. Naviger til menuindstillingen **APIs** og **MCP Servers**, hvor du bør se følgende:

    ![Se MCP-serveren i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er oprettet, og API-operationerne er eksponeret som værktøjer. MCP-serveren er opført i MCP Servers-panelet. URL-kolonnen viser endepunktet for MCP-serveren, som du kan kalde til test eller i en klientapplikation.

## Valgfrit: Konfigurer politikker

Azure API Management har et kernekoncept kaldet politikker, hvor du opsætter forskellige regler for dine endepunkter, som for eksempel hastighedsbegrænsning eller semantisk caching. Disse politikker skrives i XML.

Sådan opsætter du en politik for at begrænse hastigheden på din MCP-server:

1. I portalen, under **APIs**, vælg **MCP Servers**.

1. Vælg den MCP-server, du har oprettet.

1. I venstremenuen, under MCP, vælg **Policies**.

1. I politikeditoren skal du tilføje eller redigere de politikker, du vil anvende på MCP-serverens værktøjer. Politikkerne defineres i XML-format. For eksempel kan du tilføje en politik for at begrænse kald til MCP-serverens værktøjer (i dette eksempel 5 kald pr. 30 sekunder pr. klient-IP-adresse). Her er XML, der vil forårsage hastighedsbegrænsning:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et billede af politikeditoren:

    ![Politikeditor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Prøv det af

Lad os sikre, at vores MCP-server fungerer som forventet.

Til dette vil vi bruge Visual Studio Code og GitHub Copilot i dets Agent-tilstand. Vi tilføjer MCP-serveren til en *mcp.json*-fil. Ved at gøre dette vil Visual Studio Code fungere som en klient med agentbaserede funktioner, og slutbrugere vil kunne skrive en prompt og interagere med serveren.

Sådan tilføjer du MCP-serveren i Visual Studio Code:

1. Brug MCP: **Add Server-kommandoen fra Command Palette**.

1. Når du bliver bedt om det, skal du vælge servertypen: **HTTP (HTTP eller Server Sent Events)**.

1. Indtast URL'en til MCP-serveren i API Management. Eksempel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE-endepunkt) eller **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP-endepunkt), bemærk forskellen mellem transporterne er `/sse` eller `/mcp`.

1. Indtast et server-ID efter eget valg. Dette er ikke en vigtig værdi, men det vil hjælpe dig med at huske, hvad denne serverinstans er.

1. Vælg, om konfigurationen skal gemmes i dine arbejdsområdesindstillinger eller brugersettings.

  - **Arbejdsområdesindstillinger** - Serverkonfigurationen gemmes i en .vscode/mcp.json-fil, der kun er tilgængelig i det aktuelle arbejdsområde.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    eller hvis du vælger streaming HTTP som transport, vil det være lidt anderledes:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Brugersettings** - Serverkonfigurationen tilføjes til din globale *settings.json*-fil og er tilgængelig i alle arbejdsområder. Konfigurationen ser ud som følger:

    ![Brugerindstilling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du skal også tilføje en konfiguration, en header, for at sikre, at den autentificerer korrekt mod Azure API Management. Den bruger en header kaldet **Ocp-Apim-Subscription-Key**.

    - Sådan tilføjer du den til settings:

    ![Tilføj header til autentificering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil få en prompt til at blive vist, hvor du bliver bedt om at indtaste API-nøgleværdien, som du kan finde i Azure Portal for din Azure API Management-instans.

   - For at tilføje den til *mcp.json* i stedet, kan du tilføje den som følger:

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

Nu er vi klar i enten settings eller *.vscode/mcp.json*. Lad os prøve det af.

Der bør være et værktøjsikon som dette, hvor de eksponerede værktøjer fra din server er opført:

![Værktøjer fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik på værktøjsikonet, og du bør se en liste over værktøjer som dette:

    ![Værktøjer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Indtast en prompt i chatten for at aktivere værktøjet. For eksempel, hvis du har valgt et værktøj til at få oplysninger om en ordre, kan du spørge agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nu blive præsenteret for et værktøjsikon, der beder dig om at fortsætte med at kalde et værktøj. Vælg at fortsætte med at køre værktøjet, og du bør nu se et output som dette:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Hvad du ser ovenfor afhænger af, hvilke værktøjer du har opsat, men ideen er, at du får et tekstbaseret svar som ovenfor.**

## Referencer

Her kan du lære mere:

- [Tutorial om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-eksempel: Sikre eksterne MCP-servere ved hjælp af Azure API Management (eksperimentel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klientautorisationslab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Brug Azure API Management-udvidelsen til VS Code til at importere og administrere API'er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og opdag eksterne MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Fantastisk repo, der viser mange AI-funktioner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Indeholder workshops ved hjælp af Azure Portal, som er en fantastisk måde at begynde at evaluere AI-funktioner.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
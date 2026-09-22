# Case Study: Eksponere REST API i API Management som en MCP-server

Azure API Management er en tjeneste som tilbyr en gateway på toppen av API-endepunktene dine. Slik fungerer det: Azure API Management fungerer som en proxy foran API-ene dine og kan bestemme hva som skal gjøres med innkommende forespørsler.

Ved å bruke det får du en rekke funksjoner som:

- **Sikkerhet**, du kan bruke alt fra API-nøkler, JWT til administrert identitet.
- **Ratebegrensning**, en flott funksjon er å kunne bestemme hvor mange kall som skal slippe gjennom per gitt tidsenhet. Dette hjelper med å sikre en god opplevelse for alle brukere og at tjenesten din ikke overveldes av forespørsler.
- **Skalering og lastbalansering**. Du kan sette opp flere endepunkter for å balansere lasten, og du kan også bestemme hvordan du vil "lastbalansere".
- **AI-funksjoner som semantisk caching**, tokenbegrensning og tokenovervåking med mer. Dette er flotte funksjoner som forbedrer responstiden og hjelper deg med å ha kontroll på token-forbruket ditt. [Les mer her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Hvorfor MCP + Azure API Management?

Model Context Protocol blir raskt en standard for agentbaserte AI-apper og hvordan verktøy og data eksponeres på en konsistent måte. Azure API Management er et naturlig valg når du trenger å "administrere" API-er. MCP-servere integrerer ofte med andre API-er for å løse forespørsler til et verktøy, for eksempel. Derfor er det svært fornuftig å kombinere Azure API Management og MCP.

## Oversikt

I dette spesifikke tilfellet skal vi lære å eksponere API-endepunkter som en MCP-server. Ved å gjøre dette kan vi enkelt gjøre disse endepunktene til en del av en agentbasert app, samtidig som vi utnytter funksjonene i Azure API Management.

## Nøkkelfunksjoner

- Du velger hvilke endepunktmetoder du vil eksponere som verktøy.
- De tilleggsegenskapene du får, avhenger av hva du konfigurerer i policy-delen for API-en din. Men her viser vi hvordan du kan legge til ratebegrensning.

## Forberedelsestrinn: importer en API

Hvis du allerede har en API i Azure API Management, flott, da kan du hoppe over dette trinnet. Hvis ikke, sjekk denne lenken, [importere en API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponer API som MCP-server

Følg disse trinnene for å eksponere API-endepunktene:

1. Gå til Azure-portalen og denne adressen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Naviger til API Management-instansen din.

1. Velg i venstremenyen APIs > MCP Servers > + Create new MCP Server.

1. Velg en REST API for å eksponere som en MCP-server.

1. Velg en eller flere API-operasjoner å eksponere som verktøy. Du kan velge alle operasjoner eller bare spesifikke operasjoner.

    ![Velg metoder å eksponere](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Velg **Create**.

1. Naviger til menyvalget **APIs** og **MCP Servers**, du bør se følgende:

    ![Se MCP-serveren i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er opprettet og API-operasjonene er eksponert som verktøy. MCP-serveren vises i MCP Servers-panelet. URL-kolonnen viser endepunktet til MCP-serveren som du kan kalle for testing eller inne i en klientapplikasjon.

## Valgfritt: Konfigurer policies

Azure API Management har kjernebegrepet policies hvor du setter opp ulike regler for endepunktene dine, som for eksempel ratebegrensning eller semantisk caching. Disse policyene skrives i XML.

Slik setter du opp en policy for å ratebegrense MCP-serveren din:

1. I portalen, under APIs, velg **MCP Servers**.

1. Velg MCP-serveren du opprettet.

1. I venstremenyen, under MCP, velg **Policies**.

1. I policy-editoren legger du til eller redigerer de policyene du vil bruke på MCP-serverens verktøy. Policyene defineres i XML-format. For eksempel kan du legge til en policy som begrenser kall til MCP-serverens verktøy (i dette eksemplet 5 kall per 30 sekunder per klient-IP-adresse). Her er XML som vil håndheve ratebegrensningen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et bilde av policy-editoren:

    ![Policy-editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prøv det ut

La oss sikre at MCP-serveren vår fungerer som tiltenkt.

> [!NOTE]
> Azure API Management eksponerer for øyeblikket denne serveren gjennom Streamable
> HTTP `/mcp` endepunktet. Den eldre HTTP+SSE `/sse` transporten er avviklet og
> bør kun brukes med legacy-klienter.

For dette skal vi bruke Visual Studio Code og GitHub Copilot med Agent-modus. Vi legger til MCP-serveren i en *mcp.json*-fil. På denne måten fungerer Visual Studio Code som en klient med agentiske funksjoner, og sluttbrukere kan skrive en prompt og samhandle med serveren.

Slik legger du til MCP-serveren i Visual Studio Code:

1. Bruk MCP: **Add Server-kommandoen fra Command Palette**.

1. Når du blir spurt, velg servertype: **HTTP (HTTP eller Server Sent Events)**.

1. Tast inn den Streamable HTTP-URL som vises for MCP-serveren i API Management.
    For eksempel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Angi en server-ID etter eget valg. Dette er ikke en viktig verdi, men det hjelper deg å huske hva denne serverinstansen er.

1. Velg om konfigurasjonen skal lagres i arbeidsområdet eller globalt i brukerinnstillingene.

  - **Arbeidsområdeinnstillinger** - Serverkonfigurasjonen lagres i en .vscode/mcp.json-fil som kun er tilgjengelig i det gjeldende arbeidsområdet.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Brukerinnstillinger** - Serverkonfigurasjonen legges til i din globale *settings.json*-fil og er tilgjengelig i alle arbeidsområder. Konfigurasjonen ser omtrent slik ut:

    ![Brukerinnstilling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du må også legge til konfigurasjon, en header for å sikre at autentisering mot Azure API Management fungerer som den skal. Den bruker en header kalt **Ocp-Apim-Subscription-Key*. 

    - Slik kan du legge det til i instillingene:

    ![Legge til header for autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil føre til at en prompt vises for å be om API-nøkkelverdien, som du finner i Azure-portalen for din Azure API Management-instans.

   - For å legge det til i *mcp.json* i stedet, kan du legge det til slik:

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

### Bruk Agent-modus

Nå er vi klare enten i innstillingene eller i *.vscode/mcp.json*. La oss prøve det.

Det skal være et verktøyikon slik som dette, hvor verktøyene eksponert fra serveren din vises:

![Verktøy fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikk på verktøyikonet, og du skal se en liste over verktøy slik:

    ![Verktøy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Tast inn en prompt i chatten for å aktivere verktøyet. For eksempel, hvis du valgte et verktøy for å hente informasjon om en ordre, kan du spørre agenten om informasjon om en ordre. Her er et eksempel på prompt:

    ```text
    get information from order 2
    ```

    Du vil nå få opp et verktøyikon som spør deg om du vil fortsette med å kalle et verktøy. Velg å fortsette kjøringen av verktøyet, og du skal se et slikt resultat:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Det du ser ovenfor avhenger av hvilke verktøy du har satt opp, men idéen er at du får et tekstbasert svar som vist**


## Referanser

Slik kan du lære mer:

- [Veiledning om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-eksempel: Sikre fjern-MCP-servere ved bruk av Azure API Management (eksperimentelt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klientautorisasjonslab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Bruk Azure API Management-utvidelsen for VS Code for å importere og administrere API-er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og oppdag fjern-MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Flott repo som viser mange AI-funksjoner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Inneholder workshops som bruker Azure-portalen, en flott måte å begynne å evaluere AI-funksjonalitet på.

## Hva nå?

- Tilbake til: [Case Studies Oversikt](./README.md)
- Neste: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
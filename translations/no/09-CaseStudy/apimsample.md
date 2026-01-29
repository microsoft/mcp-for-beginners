# Case Study: Eksponere REST API i API Management som en MCP-server

Azure API Management er en tjeneste som gir en Gateway på toppen av dine API-endepunkter. Hvordan det fungerer er at Azure API Management opptrer som en proxy foran dine API-er og kan bestemme hva som skal gjøres med innkommende forespørsler.

Ved å bruke det, får du en rekke funksjoner som:

- **Sikkerhet**, du kan bruke alt fra API-nøkler, JWT til administrert identitet.
- **Begrensning av antall forespørsler**, en flott funksjon er muligheten til å bestemme hvor mange forespørsler som slipper gjennom per en viss tidsenhet. Dette hjelper med å sikre at alle brukere får en god opplevelse og at tjenesten din ikke blir overveldet av forespørsler.
- **Skalering og lastbalansering**. Du kan sette opp flere endepunkter for å balansere lasten, og du kan også bestemme hvordan du vil "lastbalansere".
- **AI-funksjoner som semantisk caching**, tokenbegrensning og tokenovervåking og mer. Disse er flotte funksjoner som forbedrer responsen og hjelper deg med å holde oversikt over tokenforbruket. [Les mer her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol blir raskt en standard for agentbaserte AI-apper og hvordan man eksponerer verktøy og data på en konsistent måte. Azure API Management er et naturlig valg når du trenger å "administrere" API-er. MCP-servere integreres ofte med andre API-er for å løse forespørsler til et verktøy, for eksempel. Derfor gir det mye mening å kombinere Azure API Management og MCP.

## Oversikt

I dette spesifikke brukstilfellet skal vi lære å eksponere API-endepunkter som en MCP-server. Ved å gjøre dette kan vi enkelt gjøre disse endepunktene til en del av en agentbasert app, samtidig som vi utnytter funksjonene fra Azure API Management.

## Nøkkelfunksjoner

- Du velger hvilke endepunktmetoder du vil eksponere som verktøy.
- De ekstra funksjonene du får avhenger av hva du konfigurerer i policyseksjonen for ditt API. Her vil vi vise hvordan du kan legge til begrensning av antall forespørsler.

## Forberedelse: importere et API

Hvis du allerede har et API i Azure API Management, flott, da kan du hoppe over dette trinnet. Hvis ikke, sjekk ut denne lenken, [importere et API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponere API som MCP-server

For å eksponere API-endepunktene, følg disse trinnene:

1. Gå til Azure Portal og følgende adresse <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Naviger til din API Management-instans.

1. I venstre meny, velg APIs > MCP Servers > + Create new MCP Server.

1. I API, velg et REST API som skal eksponeres som en MCP-server.

1. Velg én eller flere API-operasjoner som skal eksponeres som verktøy. Du kan velge alle operasjoner eller bare spesifikke operasjoner.

    ![Velg metoder som skal eksponeres](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Velg **Create**.

1. Naviger til menyvalget **APIs** og **MCP Servers**, du bør se følgende:

    ![Se MCP-serveren i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er opprettet, og API-operasjonene er eksponert som verktøy. MCP-serveren er oppført i MCP Servers-panelet. URL-kolonnen viser endepunktet til MCP-serveren som du kan bruke for testing eller i en klientapplikasjon.

## Valgfritt: Konfigurere policies

Azure API Management har kjernekonseptet policies der du setter opp ulike regler for dine endepunkter, som for eksempel begrensning av antall forespørsler eller semantisk caching. Disse policies er skrevet i XML.

Slik kan du sette opp en policy for å begrense antall forespørsler til din MCP-server:

1. I portalen, under APIs, velg **MCP Servers**.

1. Velg MCP-serveren du opprettet.

1. I venstre meny, under MCP, velg **Policies**.

1. I policyeditoren, legg til eller rediger policies du vil bruke på MCP-serverens verktøy. Policies er definert i XML-format. For eksempel kan du legge til en policy for å begrense antall forespørsler til MCP-serverens verktøy (i dette eksempelet, 5 forespørsler per 30 sekunder per klient-IP-adresse). Her er XML som vil forårsake begrensning:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et bilde av policyeditoren:

    ![Policyeditor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Test det ut

La oss sikre at MCP-serveren vår fungerer som den skal.

For dette vil vi bruke Visual Studio Code og GitHub Copilot i Agent-modus. Vi vil legge til MCP-serveren i en *mcp.json*-fil. Ved å gjøre dette vil Visual Studio Code fungere som en klient med agentbaserte funksjoner, og sluttbrukere vil kunne skrive inn en prompt og interagere med serveren.

Slik legger du til MCP-serveren i Visual Studio Code:

1. Bruk MCP: **Add Server command fra Command Palette**.

1. Når du blir bedt om det, velg servertypen: **HTTP (HTTP eller Server Sent Events)**.

1. Skriv inn URL-en til MCP-serveren i API Management. Eksempel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE-endepunkt) eller **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP-endepunkt), merk forskjellen mellom transportene `/sse` eller `/mcp`.

1. Skriv inn en server-ID etter eget valg. Dette er ikke en viktig verdi, men det vil hjelpe deg med å huske hva denne serverinstansen er.

1. Velg om du vil lagre konfigurasjonen til arbeidsområdets innstillinger eller brukerinnstillinger.

  - **Arbeidsområdets innstillinger** - Serverkonfigurasjonen lagres i en .vscode/mcp.json-fil som kun er tilgjengelig i det aktuelle arbeidsområdet.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    eller hvis du velger streaming HTTP som transport, vil det være litt annerledes:

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

1. Du må også legge til en header for å sikre at den autentiserer riktig mot Azure API Management. Den bruker en header kalt **Ocp-Apim-Subscription-Key**.

    - Slik kan du legge den til innstillingene:

    ![Legge til header for autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil føre til at en prompt vises for å be deg om API-nøkkelverdien, som du finner i Azure Portal for din Azure API Management-instans.

   - For å legge den til *mcp.json* i stedet, kan du legge den til slik:

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

Nå er vi klare, enten i innstillinger eller i *.vscode/mcp.json*. La oss teste det ut.

Det bør være et verktøyikon som ser slik ut, der de eksponerte verktøyene fra serveren din er oppført:

![Verktøy fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikk på verktøyikonet, og du bør se en liste over verktøy som ser slik ut:

    ![Verktøy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Skriv inn en prompt i chatten for å bruke verktøyet. For eksempel, hvis du valgte et verktøy for å hente informasjon om en ordre, kan du spørre agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nå bli presentert med et verktøyikon som ber deg om å fortsette med å bruke et verktøy. Velg å fortsette med å kjøre verktøyet, og du bør nå se et output som ser slik ut:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Hva du ser ovenfor avhenger av hvilke verktøy du har satt opp, men ideen er at du får et tekstlig svar som ovenfor.**

## Referanser

Her er hvordan du kan lære mer:

- [Tutorial om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-eksempel: Sikre eksterne MCP-servere ved bruk av Azure API Management (eksperimentell)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klientautorisering lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Bruk Azure API Management-utvidelsen for VS Code for å importere og administrere API-er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og oppdag eksterne MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Flott repo som viser mange AI-funksjoner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Inneholder workshops ved bruk av Azure Portal, som er en flott måte å begynne å evaluere AI-funksjoner.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
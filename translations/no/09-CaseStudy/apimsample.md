# Casestudie: Eksponer REST API i API Management som en MCP-server

Azure API Management er en tjeneste som tilbyr en gateway på toppen av API-endepunktene dine. Slik fungerer det at Azure API Management opptrer som en proxy foran API-ene dine og kan bestemme hva som skal gjøres med innkommende forespørsler.

Ved å bruke den legger du til en rekke funksjoner som:

- **Sikkerhet**, du kan bruke alt fra API-nøkler, JWT til administrert identitet.
- **Ratelimiting**, en flott funksjon er å kunne bestemme hvor mange kall som slippes gjennom per en viss tidsenhet. Dette hjelper til med å sikre at alle brukere får en god opplevelse, og at tjenesten din ikke overveldes av forespørsler.
- **Skalering og lastbalansering**. Du kan sette opp flere endepunkter for å fordele belastningen, og du kan også bestemme hvordan du vil "lastbalansere".
- **AI-funksjoner som semantisk caching**, token-grense og token-overvåking og mer. Dette er flotte funksjoner som forbedrer responstiden og hjelper deg å ha kontroll på token-bruken din. [Les mer her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol blir raskt en standard for agentiske AI-apper og for hvordan man eksponerer verktøy og data på en konsistent måte. Azure API Management er et naturlig valg når du trenger å "administrere" API-er. MCP-servere integrerer ofte med andre API-er for å løse forespørsler til et verktøy, for eksempel. Derfor gir det mye mening å kombinere Azure API Management og MCP.

## Oversikt

I dette spesifikke brukstilfellet lærer vi hvordan vi kan eksponere API-endepunkter som en MCP-server. Ved å gjøre dette kan vi enkelt gjøre disse endepunktene til en del av en agentisk app samtidig som vi utnytter funksjonene fra Azure API Management.

## Nøkkelfunksjoner

- Du velger hvilke endepunktmetoder du vil eksponere som verktøy.
- De ekstra funksjonene du får, avhenger av hva du konfigurerer i policyseksjonen for API-et ditt. Her vil vi vise hvordan du kan legge til ratelimiting.

## Forberedende steg: importer et API

Hvis du allerede har et API i Azure API Management, flott – da kan du hoppe over dette steget. Hvis ikke, sjekk ut denne lenken, [importere et API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponer API som MCP-server

For å eksponere API-endepunktene, følg disse stegene:

1. Naviger til Azure Portal og adressen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Naviger til din API Management-instans.

1. I venstremenyen, velg APIs > MCP Servers > + Opprett ny MCP-server.

1. Under API, velg et REST API som skal eksponeres som MCP-server.

1. Velg en eller flere API-operasjoner som skal eksponeres som verktøy. Du kan velge alle operasjoner eller bare spesifikke operasjoner.

    ![Velg metoder å eksponere](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Velg **Opprett**.

1. Naviger til menyalternativet **APIs** og deretter **MCP Servers**, du skal da se følgende:

    ![Se MCP-serveren i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er opprettet og API-operasjonene er eksponert som verktøy. MCP-serveren listes i MCP Servers-panelet. Kolonnen URL viser endepunktet til MCP-serveren som du kan bruke til testing eller i en klientapplikasjon.

## Valgfritt: Konfigurer retningslinjer (policies)

Azure API Management har et kjernekonsept for policies hvor du setter opp forskjellige regler for endepunktene dine som for eksempel ratelimiting eller semantisk caching. Disse retningslinjene defineres i XML.

Slik kan du sette opp en policy for ratelimiting på MCP-serveren din:

1. I portalen, under APIs, velg **MCP Servers**.

1. Velg MCP-serveren du opprettet.

1. I venstremenyen under MCP, velg **Policies**.

1. I policyredigereren legger du til eller endrer de policyene du ønsker å bruke på MCP-serverens verktøy. Policyene defineres i XML-format. For eksempel kan du legge til en policy som begrenser kall til MCP-serverens verktøy (i dette eksempelet 5 kall per 30 sekunder per klient-IP-adresse). Her er XML som gjør at det settes ratelimiting:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et bilde av policyredigereren:

    ![Policyredigerer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prøv det ut

La oss sikre at MCP-serveren vår fungerer som forventet.

> [!NOTE]
> Azure API Management eksponerer for tiden denne serveren gjennom Streamable
> HTTP `/mcp` endepunktet. Den eldre HTTP+SSE `/sse` transporten er utfaset og
> bør kun brukes med eldre klienter.

Til dette vil vi bruke Visual Studio Code og GitHub Copilot med Agent-modus. Vi vil legge til MCP-serveren i en *mcp.json* fil. På denne måten vil Visual Studio Code opptre som en klient med agentiske evner, og sluttbrukere vil kunne skrive en prompt og interagere med denne serveren.

La oss se hvordan vi legger til MCP-serveren i Visual Studio Code:

1. Bruk MCP: **Legg til server-kommandoen fra kommandopaletten**.

1. Når du blir spurt, velg servertype: **HTTP (HTTP eller Server Sent Events)**.

1. Tast inn Streamable HTTP-URL som vises for MCP-serveren i API Management.
    For eksempel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Skriv inn et server-ID etter eget ønske. Dette er ikke en viktig verdi, men det hjelper deg å huske hva denne serverinstansen er.

1. Velg om du vil lagre konfigurasjonen til arbeidsområdeinnstillinger eller brukerinnstillinger.

    - **Arbeidsområdeinnstillinger** - serverkonfigurasjonen lagres i en `.vscode/mcp.json` fil, som kun er tilgjengelig i det nåværende arbeidsområdet.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Brukerinnstillinger** - serverkonfigurasjonen legges til i din globale *settings.json* fil og er tilgjengelig på tvers av alle arbeidsområder. Konfigurasjonen ser omtrent slik ut:

      ![Brukerinnstilling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du må også legge til en konfigurasjonsheader for å sikre at autentisering mot Azure API Management fungerer riktig. Den bruker en header kalt **Ocp-Apim-Subscription-Key**.

    - Slik kan du legge den til i innstillingene:


    ![Legge til header for autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil føre til at det vises en prompt som ber deg om API-nøkkelverdien du finner i Azure Portal for din Azure API Management-instans.

   - For å legge den til i *mcp.json* i stedet, kan du legge den til slik:

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

Nå er vi klare både i innstillingene eller i *.vscode/mcp.json*. La oss prøve det ut. 

Det skal være et Verktøy-ikon som dette, der verktøyene som er eksponert fra serveren din listes opp:

![Verktøy fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikk på verktøyikonet så skal du se en liste over verktøy som dette:

    ![Verktøy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Skriv inn en prompt i chatten for å kalle verktøyet. For eksempel, hvis du har valgt et verktøy for å hente informasjon om en ordre, kan du spørre agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nå se et verktøyikon som spør om du vil fortsette å kjøre verktøyet. Velg å fortsette, og da skal du se et resultat som dette:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Hva du ser ovenfor avhenger av hvilke verktøy du har satt opp, men ideen er at du får et tekstbasert svar som vist ovenfor**


## Referanser

Slik kan du lære mer:

- [Veiledning om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-eksempel: Sikre eksterne MCP-servere med Azure API Management (eksperimentelt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klient autorisasjonslab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Bruk Azure API Management-utvidelsen for VS Code til å importere og administrere API-er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og oppdag eksterne MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Flott repo som viser mange AI-muligheter med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Inneholder workshops med Azure Portal, som er en flott måte å begynne å evaluere AI-funksjonalitet på.

## Hva skjer videre

- Tilbake til: [Oversikt over casestudier](./README.md)
- Neste: [Azure AI Reiseagenter](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
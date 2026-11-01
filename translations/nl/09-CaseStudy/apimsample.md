# Case Study: REST API blootstellen in API Management als een MCP-server

Azure API Management is een dienst die een Gateway bovenop je API-eindpunten biedt. Azure API Management fungeert als een proxy voor je API's en kan bepalen wat er met binnenkomende verzoeken gebeurt.

Door het te gebruiken voeg je een hele reeks functies toe, zoals:

- **Beveiliging**, je kunt alles gebruiken van API-sleutels, JWT tot beheerde identiteit.
- **Rate limiting**, een geweldige functie waarmee je kunt bepalen hoeveel oproepen per tijdseenheid worden toegelaten. Dit helpt te verzekeren dat alle gebruikers een goede ervaring hebben en dat je service niet overweldigd raakt door verzoeken.
- **Schaalbaarheid & Load balancing**. Je kunt een aantal eindpunten instellen om de belasting te verdelen en je kunt ook bepalen hoe je wilt "load balancen".
- **AI-functies zoals semantische caching**, tokenlimiet en tokenmonitoring en meer. Dit zijn geweldige functies die de reactietijd verbeteren en je helpen om je tokenverbruik te beheersen. [Lees hier meer](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Waarom MCP + Azure API Management?

Model Context Protocol wordt snel de standaard voor agentische AI-apps en hoe tools en data op een consistente manier bloot te stellen. Azure API Management is een logische keuze wanneer je API's moet "beheren". MCP-servers integreren vaak met andere API's om verzoeken bijvoorbeeld aan een tool door te geven. Daarom is de combinatie van Azure API Management en MCP heel logisch.

## Overzicht

In deze specifieke use case leren we API-eindpunten blootstellen als een MCP-server. Zo kunnen we deze eindpunten eenvoudig onderdeel maken van een agentische app en tegelijkertijd profiteren van de functies van Azure API Management.

## Belangrijkste functies

- Je selecteert de eindpuntmethoden die je als tools wilt blootstellen.
- De extra functies die je krijgt zijn afhankelijk van wat je configureert in het beleidsgedeelte voor je API. Hier tonen we hoe je rate limiting kunt toevoegen.

## Voorafgaande stap: importeer een API

Als je al een API in Azure API Management hebt, prima, dan kun je deze stap overslaan. Zo niet, bekijk dan deze link, [API importeren in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API blootstellen als MCP-server

Volg deze stappen om de API-eindpunten bloot te stellen:

1. Navigeer naar Azure Portal en de volgende adres <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Ga naar je API Management instantie.

1. Selecteer in het linkermenu APIs > MCP Servers > + Maak nieuwe MCP Server aan.

1. Selecteer bij API een REST API om bloot te stellen als een MCP-server.

1. Selecteer een of meer API-operaties om bloot te stellen als tools. Je kunt alle operaties selecteren of alleen specifieke operaties.

    ![Selecteer methoden om bloot te stellen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selecteer **Maken**.

1. Navigeer naar de menuopties **APIs** en **MCP Servers**, je zou het volgende moeten zien:

    ![Zie de MCP Server in het hoofdscherm](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    De MCP-server is gemaakt en de API-operaties zijn blootgesteld als tools. De MCP-server staat vermeld in het MCP Servers-paneel. De URL-kolom toont het eindpunt van de MCP-server dat je kunt aanroepen voor testen of binnen een clientapplicatie.

## Optioneel: Beleid configureren

Azure API Management heeft het kernconcept van policies waarbij je verschillende regels instelt voor je eindpunten, zoals rate limiting of semantische caching. Deze policies worden geschreven in XML.

Hier is hoe je een policy kunt instellen om je MCP-server te rate limiten:

1. Selecteer in de portal onder APIs **MCP Servers**.

1. Selecteer de MCP-server die je hebt gemaakt.

1. Selecteer in het linkermenu onder MCP **Policies**.

1. Voeg in de policy-editor de policies toe of bewerk deze die je wilt toepassen op de tools van de MCP-server. De policies zijn in XML-formaat. Bijvoorbeeld, je kunt een policy toevoegen om oproepen naar de tools van de MCP-server te beperken (in dit voorbeeld 5 oproepen per 30 seconden per client IP-adres). Hier is de XML die hiervoor zorgt:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hier is een afbeelding van de policy-editor:

    ![Policy-editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Probeer het uit

Laten we controleren of onze MCP Server werkt zoals bedoeld.

> [!NOTE]
> Azure API Management stelt deze server momenteel bloot via de Streamable
> HTTP `/mcp` eindpunt. Het oudere HTTP+SSE `/sse` transport is verouderd en
> moet alleen met legacy clients worden gebruikt.

Hiervoor gebruiken we Visual Studio Code en GitHub Copilot in Agent-modus. We voegen de MCP-server toe aan een *mcp.json*-bestand. Hierdoor fungeert Visual Studio Code als client met agentische mogelijkheden en kunnen eindgebruikers een prompt typen en met deze server communiceren.

Zo voeg je de MCP-server toe in Visual Studio Code:

1. Gebruik de MCP: **Server toevoegen-commando vanuit de Command Palette**.

1. Kies wanneer daarom gevraagd wordt het servertype: **HTTP (HTTP of Server Sent Events)**.

1. Voer de Streamable HTTP-URL in die wordt weergegeven voor de MCP-server in API Management.
    Bijvoorbeeld:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Voer een server-ID naar keuze in. Dit is geen belangrijke waarde, maar helpt je te onthouden wat deze serverinstantie is.

1. Kies of je de configuratie opslaat in je werkruimteinstellingen of gebruikersinstellingen.

    - **Werkruimteinstellingen** - De serverconfiguratie wordt opgeslagen in een `.vscode/mcp.json`-bestand, dat alleen beschikbaar is in het huidige werkruimte.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Gebruikersinstellingen** - De serverconfiguratie wordt toegevoegd aan je globale *settings.json*-bestand en is beschikbaar in alle werkruimten. De configuratie ziet er ongeveer als volgt uit:

      ![Gebruikersinstelling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Je moet ook een configuratieheader toevoegen om zeker te zijn dat authenticatie correct verloopt richting Azure API Management. Het gebruikt een header genaamd **Ocp-Apim-Subscription-Key**.

    - Zo voeg je het toe aan de instellingen:


    ![Header toevoegen voor authenticatie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hierdoor verschijnt een prompt waarin je wordt gevraagd om de API-sleutelwaarde die je kunt vinden in Azure Portal voor je Azure API Management-instantie.

   - Om het aan *mcp.json* toe te voegen, kun je het als volgt doen:

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

### Gebruik Agentmodus

Nu zijn we helemaal ingesteld, ofwel in instellingen of in *.vscode/mcp.json*. Laten we het uitproberen.

Er zou een Tools-pictogram moeten zijn, waar de blootgestelde tools van je server worden weergegeven:

![Tools van de server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik op het tools-pictogram en je zou een lijst met tools moeten zien zoals deze:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Typ een prompt in de chat om de tool aan te roepen. Bijvoorbeeld, als je een tool hebt geselecteerd om informatie over een bestelling te krijgen, kun je de agent naar een bestelling vragen. Hier is een voorbeeldprompt:

    ```text
    get information from order 2
    ```

    Nu verschijnt er een tools-pictogram dat je vraagt om door te gaan met het aanroepen van een tool. Selecteer om door te gaan met de tool, je zou nu zoiets als een resultaat moeten zien:

    ![Resultaat van prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Wat je hierboven ziet hangt af van welke tools je hebt ingesteld, maar het idee is dat je een tekstuele reactie zoals hierboven krijgt**


## Referenties

Hier is hoe je meer kunt leren:

- [Tutorial over Azure API Management en MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Pythonvoorbeeld: beveilig remotes MCP-servers met Azure API Management (experimenteel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client autorisatie lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gebruik de Azure API Management-extensie voor VS Code om API's te importeren en beheren](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreer en ontdek remote MCP-servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Geweldige repository met veel AI-mogelijkheden met Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Bevat workshops met gebruik van Azure Portal, wat een geweldige manier is om AI-mogelijkheden te evalueren.

## Wat volgt

- Terug naar: [Case Studies Overzicht](./README.md)
- Volgende: [Azure AI Reisagenten](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
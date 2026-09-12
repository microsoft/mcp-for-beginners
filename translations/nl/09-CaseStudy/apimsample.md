# Case Study: REST API blootstellen in API Management als een MCP-server

Azure API Management is een dienst die een Gateway biedt bovenop je API-eindpunten. Hoe het werkt is dat Azure API Management fungeert als een proxy voor je API's en kan beslissen wat te doen met binnenkomende verzoeken.

Door het te gebruiken voeg je allerlei functies toe zoals:

- **Beveiliging**, je kunt alles gebruiken van API-sleutels, JWT tot managed identity.
- **Rate limiting**, een geweldige functie is dat je kunt bepalen hoeveel oproepen er binnen een bepaalde tijdseenheid doorgaan. Dit helpt ervoor te zorgen dat alle gebruikers een geweldige ervaring hebben en dat je service niet wordt overladen met verzoeken.
- **Schaalbaarheid & Load balancing**. Je kunt een aantal eindpunten instellen om de belasting te verdelen en je kunt ook bepalen hoe je de "load balance" wilt uitvoeren.
- **AI-functies zoals semantische caching**, tokenlimiet en tokenmonitoring en meer. Dit zijn geweldige functies die zowel de reactietijd verbeteren als je helpen inzicht te krijgen in je tokenverbruik. [Lees hier meer](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Waarom MCP + Azure API Management?

Model Context Protocol wordt snel een standaard voor agentische AI-apps en hoe je tools en data op een consistente manier blootstelt. Azure API Management is een natuurlijke keuze wanneer je API's moet "beheerden". MCP-servers integreren vaak met andere API's om verzoeken naar een tool op te lossen bijvoorbeeld. Daarom is het combineren van Azure API Management en MCP zeer logisch.

## Overzicht

In deze specifieke use case leren we hoe we API-eindpunten kunnen blootstellen als een MCP-server. Door dit te doen kunnen we gemakkelijk deze eindpunten onderdeel maken van een agentische app terwijl we ook de functies van Azure API Management benutten.

## Belangrijkste Kenmerken

- Je selecteert de eindpuntmethoden die je wilt blootstellen als tools.
- De extra functies die je krijgt zijn afhankelijk van wat je configureert in het beleidsgedeelte van je API. Maar hier laten we je zien hoe je rate limiting kunt toevoegen.

## Voorafgaande stap: een API importeren

Als je al een API in Azure API Management hebt, geweldig, dan kun je deze stap overslaan. Zo niet, bekijk dan deze link, [een API importeren in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API blootstellen als MCP-server

Om de API-eindpunten bloot te stellen volgen we deze stappen:

1. Ga naar de Azure Portal en naar het volgende adres <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigeer naar je API Management instantie.

1. Kies in het linkermenu APIs > MCP Servers > + Create new MCP Server.

1. Selecteer bij API een REST API die je als MCP server wilt blootstellen.

1. Selecteer een of meer API-bewerkingen die je als tools wilt blootstellen. Je kunt alle bewerkingen selecteren of alleen specifieke bewerkingen.

    ![Selecteer methoden om bloot te stellen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Selecteer **Create**.

1. Ga naar de menuoptie **APIs** en **MCP Servers**, je zou het volgende moeten zien:

    ![Zie de MCP-server in het hoofdvenster](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    De MCP-server is gemaakt en de API-bewerkingen zijn blootgesteld als tools. De MCP-server staat vermeld in het MCP Servers-paneel. De URL-kolom toont het eindpunt van de MCP-server die je kunt aanroepen voor testen of binnen een clienttoepassing.

## Optioneel: Beleid configureren

Azure API Management heeft het kernconcept van beleid waarbij je verschillende regels instelt voor je eindpunten zoals bijvoorbeeld rate limiting of semantische caching. Deze beleidsregels zijn opgesteld in XML.

Zo kun je een beleid instellen om je MCP-server te beperken in het aantal verzoeken:

1. Kies in de portal onder APIs, **MCP Servers**.

1. Selecteer de MCP-server die je hebt gemaakt.

1. Selecteer in het linkermenu onder MCP, **Policies**.

1. Voeg in de beleid-editor de beleidsregels toe of bewerk ze die je wilt toepassen op de tools van de MCP-server. De beleidsregels zijn gedefinieerd in XML-formaat. Bijvoorbeeld, je kunt een beleid toevoegen om oproepen naar de tools van de MCP-server te limiteren (in dit voorbeeld 5 oproepen per 30 seconden per client IP-adres). Hier is XML die ervoor zorgt dat het rate-limiting toepast:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hier is een afbeelding van de beleid-editor:

    ![Beleid-editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Probeer het uit

Laten we controleren of onze MCP-server werkt zoals bedoeld.

> [!NOTE]
> Azure API Management stelt deze server momenteel bloot via de Streamable
> HTTP `/mcp` endpoint. Het oudere HTTP+SSE `/sse` transport is verouderd en
> zou alleen met legacy clients gebruikt moeten worden.

Hiervoor gebruiken we Visual Studio Code en GitHub Copilot en de Agent-modus. We voegen de MCP-server toe aan een *mcp.json* bestand. Door dit te doen zal Visual Studio Code fungeren als een client met agentische mogelijkheden en kunnen eindgebruikers een prompt typen en met die server interactie hebben.

Laten we zien hoe, om de MCP-server toe te voegen in Visual Studio Code:

1. Gebruik de MCP: **Add Server command uit de Command Palette**.

1. Kies bij de prompt het servertype: **HTTP (HTTP of Server Sent Events)**.

1. Voer de Streamable HTTP URL in die voor de MCP-server wordt weergegeven in API Management.
    Bijvoorbeeld:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Voer een server-ID naar keuze in. Dit is geen belangrijke waarde maar helpt je herinneren wat deze server-instance is.

1. Kies of je de configuratie opslaat in je workspace-instellingen of gebruikersinstellingen.

  - **Workspace settings** - De serverconfiguratie wordt opgeslagen in een .vscode/mcp.json bestand, alleen beschikbaar in de huidige workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - De serverconfiguratie wordt toegevoegd aan je globale *settings.json* bestand en is beschikbaar in alle workspaces. De configuratie ziet er ongeveer zo uit:

    ![Gebruikersinstelling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Je moet ook configuratie toevoegen, een header om ervoor te zorgen dat het correct authenticatie doet naar Azure API Management. Het gebruikt een header genaamd **Ocp-Apim-Subscription-Key**.

    - Zo voeg je deze toe aan de instellingen:

    ![Header toevoegen voor authenticatie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hierdoor verschijnt een prompt om je om de API-sleutelwaarde te vragen die je in de Azure Portal voor je Azure API Management instantie kunt vinden.

   - Om het toe te voegen aan *mcp.json* in plaats daarvan kun je het als volgt toevoegen:

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

### Gebruik Agent-modus

Nu zijn we helemaal ingesteld in ofwel de instellingen of in *.vscode/mcp.json*. Laten we het uitproberen.

Er zou een Tools-icoon moeten zijn zoals hieronder, waar de blootgestelde tools van je server worden getoond:

![Tools van de server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik op het tools-icoon en je zou een lijst met tools moeten zien zoals hieronder:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Voer een prompt in de chat in om de tool aan te roepen. Bijvoorbeeld, als je een tool hebt geselecteerd om informatie over een bestelling op te vragen, kun je de agent iets over een bestelling vragen. Hier is een voorbeeldprompt:

    ```text
    get information from order 2
    ```

    Je krijgt nu een tools-icoon te zien die vraagt om door te gaan met het aanroepen van een tool. Selecteer doorgaan om de tool uit te voeren, je zou nu een uitvoer moeten zien zoals hieronder:

    ![Resultaat van de prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **wat je hierboven ziet hangt af van welke tools je hebt ingesteld, maar het idee is dat je een tekstuele reactie krijgt zoals hierboven**


## Referenties

Zo kun je meer leren:

- [Tutorial over Azure API Management en MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python voorbeeld: Beveilig remote MCP-servers met Azure API Management (experimenteel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client autorisatie lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gebruik de Azure API Management extensie voor VS Code om API's te importeren en beheren](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreer en ontdek remote MCP-servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Geweldige repo die veel AI-mogelijkheden met Azure API Management toont
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Bevat workshops met Azure Portal, wat een geweldige manier is om AI-mogelijkheden te evalueren.

## Wat volgt

- Terug naar: [Case Studies Overzicht](./README.md)
- Volgende: [Azure AI Reisagenten](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Casestudy: REST API blootstellen in API Management als een MCP-server

Azure API Management is een service die een Gateway biedt bovenop je API-eindpunten. Het werkt als een proxy voor je API's en kan bepalen wat er met inkomende verzoeken gebeurt.

Door het te gebruiken, voeg je een hele reeks functies toe, zoals:

- **Beveiliging**, je kunt alles gebruiken van API-sleutels, JWT tot managed identity.
- **Rate limiting**, een geweldige functie waarmee je kunt bepalen hoeveel oproepen er per bepaalde tijdseenheid worden verwerkt. Dit zorgt ervoor dat alle gebruikers een goede ervaring hebben en voorkomt dat je service wordt overspoeld met verzoeken.
- **Schalen & Load balancing**. Je kunt meerdere eindpunten instellen om de belasting te verdelen en ook bepalen hoe je wilt "load balancen".
- **AI-functies zoals semantische caching**, tokenlimieten, tokenmonitoring en meer. Dit zijn geweldige functies die de responsiviteit verbeteren en je helpen je tokengebruik bij te houden. [Lees hier meer](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Waarom MCP + Azure API Management?

Model Context Protocol wordt snel een standaard voor agentische AI-apps en hoe tools en data op een consistente manier worden blootgesteld. Azure API Management is een logische keuze wanneer je API's moet "beheren". MCP-servers integreren vaak met andere API's om verzoeken naar een tool op te lossen. Daarom is het combineren van Azure API Management en MCP een logische stap.

## Overzicht

In dit specifieke gebruiksscenario leren we hoe we API-eindpunten kunnen blootstellen als een MCP-server. Door dit te doen, kunnen we deze eindpunten eenvoudig onderdeel maken van een agentische app en tegelijkertijd profiteren van de functies van Azure API Management.

## Belangrijkste functies

- Je selecteert de eindpuntmethoden die je wilt blootstellen als tools.
- De extra functies die je krijgt, zijn afhankelijk van wat je configureert in de beleidssectie voor je API. Hier laten we zien hoe je rate limiting kunt toevoegen.

## Voorbereiding: een API importeren

Als je al een API in Azure API Management hebt, kun je deze stap overslaan. Zo niet, bekijk dan deze link: [een API importeren in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API blootstellen als MCP-server

Om de API-eindpunten bloot te stellen, volg je deze stappen:

1. Navigeer naar de Azure Portal via <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>.  
   Navigeer naar je API Management-instantie.

1. Selecteer in het linkermenu **API's > MCP-servers > + Nieuwe MCP-server maken**.

1. Selecteer bij API een REST API om bloot te stellen als een MCP-server.

1. Selecteer een of meer API-operaties om bloot te stellen als tools. Je kunt alle operaties selecteren of alleen specifieke operaties.

    ![Selecteer methoden om bloot te stellen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selecteer **Maken**.

1. Navigeer naar de menuoptie **API's** en **MCP-servers**, je zou het volgende moeten zien:

    ![Bekijk de MCP-server in het hoofdvenster](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    De MCP-server is gemaakt en de API-operaties zijn blootgesteld als tools. De MCP-server wordt weergegeven in het MCP-serverspaneel. De URL-kolom toont het eindpunt van de MCP-server dat je kunt gebruiken voor testen of binnen een clientapplicatie.

## Optioneel: Beleidsregels configureren

Azure API Management heeft het kernconcept van beleidsregels waarmee je verschillende regels kunt instellen voor je eindpunten, zoals bijvoorbeeld rate limiting of semantische caching. Deze beleidsregels worden geschreven in XML.

Hier is hoe je een beleidsregel kunt instellen om je MCP-server te rate-limiten:

1. Selecteer in de portal onder API's **MCP-servers**.

1. Selecteer de MCP-server die je hebt gemaakt.

1. Selecteer in het linkermenu onder MCP **Beleidsregels**.

1. Voeg in de beleidseditor de beleidsregels toe of bewerk ze die je wilt toepassen op de tools van de MCP-server. De beleidsregels worden gedefinieerd in XML-formaat. Bijvoorbeeld, je kunt een beleidsregel toevoegen om oproepen naar de tools van de MCP-server te beperken (in dit voorbeeld, 5 oproepen per 30 seconden per client-IP-adres). Hier is XML die dit zal veroorzaken:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hier is een afbeelding van de beleidseditor:

    ![Beleidseditor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Probeer het uit

Laten we ervoor zorgen dat onze MCP-server werkt zoals bedoeld.

Hiervoor gebruiken we Visual Studio Code en GitHub Copilot in de Agent-modus. We voegen de MCP-server toe aan een *mcp.json*-bestand. Door dit te doen, zal Visual Studio Code fungeren als een client met agentische mogelijkheden en kunnen eindgebruikers een prompt typen en interactie hebben met de server.

Laten we zien hoe je de MCP-server toevoegt in Visual Studio Code:

1. Gebruik de MCP: **Server toevoegen-opdracht vanuit de Command Palette**.

1. Wanneer daarom wordt gevraagd, selecteer het servertype: **HTTP (HTTP of Server Sent Events)**.

1. Voer de URL van de MCP-server in API Management in. Voorbeeld: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (voor SSE-eindpunt) of **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (voor MCP-eindpunt), let op het verschil tussen de transporten: `/sse` of `/mcp`.

1. Voer een server-ID naar keuze in. Dit is geen belangrijke waarde, maar het helpt je herinneren wat deze serverinstantie is.

1. Selecteer of je de configuratie wilt opslaan in je werkruimte-instellingen of gebruikersinstellingen.

  - **Werkruimte-instellingen** - De serverconfiguratie wordt opgeslagen in een .vscode/mcp.json-bestand dat alleen beschikbaar is in de huidige werkruimte.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    of als je streaming HTTP als transport kiest, zou het iets anders zijn:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Gebruikersinstellingen** - De serverconfiguratie wordt toegevoegd aan je globale *settings.json*-bestand en is beschikbaar in alle werkruimtes. De configuratie ziet er ongeveer zo uit:

    ![Gebruikersinstelling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Je moet ook een configuratie toevoegen, een header om ervoor te zorgen dat het correct authenticeert met Azure API Management. Het gebruikt een header genaamd **Ocp-Apim-Subscription-Key**.

    - Hier is hoe je het kunt toevoegen aan instellingen:

    ![Header toevoegen voor authenticatie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dit zal een prompt veroorzaken om je te vragen naar de API-sleutelwaarde die je kunt vinden in Azure Portal voor je Azure API Management-instantie.

   - Om het toe te voegen aan *mcp.json*, kun je het als volgt toevoegen:

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

### Agent-modus gebruiken

Nu zijn we helemaal ingesteld in instellingen of in *.vscode/mcp.json*. Laten we het proberen.

Er zou een Tools-icoon moeten zijn zoals hieronder, waar de blootgestelde tools van je server worden weergegeven:

![Tools van de server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik op het tools-icoon en je zou een lijst met tools moeten zien zoals hieronder:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Voer een prompt in de chat in om de tool aan te roepen. Bijvoorbeeld, als je een tool hebt geselecteerd om informatie over een bestelling op te halen, kun je de agent vragen naar een bestelling. Hier is een voorbeeldprompt:

    ```text
    get information from order 2
    ```

    Je krijgt nu een tools-icoon te zien dat je vraagt om door te gaan met het aanroepen van een tool. Selecteer om door te gaan met het uitvoeren van de tool, je zou nu een output moeten zien zoals hieronder:

    ![Resultaat van prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Wat je hierboven ziet, hangt af van welke tools je hebt ingesteld, maar het idee is dat je een tekstuele reactie krijgt zoals hierboven.**

## Referenties

Hier kun je meer leren:

- [Tutorial over Azure API Management en MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python voorbeeld: Beveilig externe MCP-servers met Azure API Management (experimenteel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client autorisatie lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gebruik de Azure API Management-extensie voor VS Code om API's te importeren en beheren](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreer en ontdek externe MCP-servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Geweldige repo die veel AI-mogelijkheden toont met Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Bevat workshops met gebruik van Azure Portal, wat een geweldige manier is om te beginnen met het evalueren van AI-mogelijkheden.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
# Fallstudie: Exponera REST API i API Management som en MCP-server

Azure API Management är en tjänst som tillhandahåller en gateway ovanpå dina API-slutpunkter. Den fungerar som en proxy framför dina API:er och kan bestämma vad som ska göras med inkommande förfrågningar.

Genom att använda den får du tillgång till en mängd funktioner som:

- **Säkerhet**, du kan använda allt från API-nycklar och JWT till hanterad identitet.
- **Hastighetsbegränsning**, en fantastisk funktion som låter dig bestämma hur många anrop som får göras under en viss tidsenhet. Detta hjälper till att säkerställa att alla användare får en bra upplevelse och att din tjänst inte överbelastas med förfrågningar.
- **Skalning och lastbalansering**. Du kan konfigurera flera slutpunkter för att balansera belastningen och även bestämma hur "lastbalanseringen" ska ske.
- **AI-funktioner som semantisk caching**, tokenbegränsning och tokenövervakning med mera. Dessa är utmärkta funktioner som förbättrar responsiviteten och hjälper dig att hålla koll på din tokenanvändning. [Läs mer här](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Varför MCP + Azure API Management?

Model Context Protocol blir snabbt en standard för agentiska AI-appar och hur man exponerar verktyg och data på ett konsekvent sätt. Azure API Management är ett naturligt val när du behöver "hantera" API:er. MCP-servrar integreras ofta med andra API:er för att lösa förfrågningar till exempelvis ett verktyg. Därför är det logiskt att kombinera Azure API Management och MCP.

## Översikt

I detta specifika användningsfall kommer vi att lära oss att exponera API-slutpunkter som en MCP-server. Genom att göra detta kan vi enkelt göra dessa slutpunkter till en del av en agentisk app samtidigt som vi drar nytta av funktionerna i Azure API Management.

## Viktiga funktioner

- Du väljer vilka slutpunktsmetoder som ska exponeras som verktyg.
- De ytterligare funktioner du får beror på vad du konfigurerar i policydelen för ditt API. Här kommer vi att visa hur du kan lägga till hastighetsbegränsning.

## Förberedelse: importera ett API

Om du redan har ett API i Azure API Management är det bra, då kan du hoppa över detta steg. Om inte, kolla in denna länk: [importera ett API till Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exponera API som MCP-server

För att exponera API-slutpunkterna, följ dessa steg:

1. Gå till Azure-portalen och följande adress <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Navigera till din API Management-instans.

1. I vänstermenyn, välj **APIs > MCP Servers > + Create new MCP Server**.

1. Under API, välj ett REST API att exponera som en MCP-server.

1. Välj en eller flera API-operationer att exponera som verktyg. Du kan välja alla operationer eller endast specifika.

    ![Välj metoder att exponera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Välj **Create**.

1. Navigera till menyalternativet **APIs** och **MCP Servers**, du bör se följande:

    ![Se MCP-servern i huvudpanelen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-servern är skapad och API-operationerna är exponerade som verktyg. MCP-servern listas i MCP Servers-panelen. Kolumnen URL visar slutpunkten för MCP-servern som du kan anropa för testning eller inom en klientapplikation.

## Valfritt: Konfigurera policies

Azure API Management har ett kärnkoncept som kallas policies där du ställer in olika regler för dina slutpunkter, som exempelvis hastighetsbegränsning eller semantisk caching. Dessa policies skrivs i XML.

Så här ställer du in en policy för att begränsa hastigheten på din MCP-server:

1. I portalen, under **APIs**, välj **MCP Servers**.

1. Välj den MCP-server du skapade.

1. I vänstermenyn, under MCP, välj **Policies**.

1. I policyredigeraren, lägg till eller redigera de policies du vill tillämpa på MCP-serverns verktyg. Policies definieras i XML-format. Till exempel kan du lägga till en policy för att begränsa anrop till MCP-serverns verktyg (i detta exempel, 5 anrop per 30 sekunder per klient-IP-adress). Här är XML som orsakar hastighetsbegränsning:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Här är en bild av policyredigeraren:

    ![Policyredigerare](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Testa

Låt oss säkerställa att vår MCP-server fungerar som avsett.

För detta kommer vi att använda Visual Studio Code och GitHub Copilot i dess Agent-läge. Vi kommer att lägga till MCP-servern i en *mcp.json*-fil. Genom att göra detta kommer Visual Studio Code att fungera som en klient med agentiska funktioner, och slutanvändare kommer att kunna skriva en prompt och interagera med servern.

Så här lägger du till MCP-servern i Visual Studio Code:

1. Använd kommandot **MCP: Add Server** från kommandopaletten.

1. När du blir ombedd, välj servertyp: **HTTP (HTTP eller Server Sent Events)**.

1. Ange URL:en för MCP-servern i API Management. Exempel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (för SSE-slutpunkt) eller **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (för MCP-slutpunkt), notera skillnaden mellan transporterna `/sse` eller `/mcp`.

1. Ange ett server-ID efter eget val. Detta är inte ett viktigt värde men hjälper dig att komma ihåg vad denna serverinstans är.

1. Välj om du vill spara konfigurationen till dina arbetsytainställningar eller användarinställningar.

  - **Arbetsytainställningar** - Serverkonfigurationen sparas i en .vscode/mcp.json-fil som endast är tillgänglig i den aktuella arbetsytan.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    eller om du väljer streaming HTTP som transport ser det något annorlunda ut:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Användarinställningar** - Serverkonfigurationen läggs till i din globala *settings.json*-fil och är tillgänglig i alla arbetsytor. Konfigurationen ser ut så här:

    ![Användarinställning](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du behöver också lägga till en konfiguration, en header för att säkerställa att autentisering sker korrekt mot Azure API Management. Den använder en header som heter **Ocp-Apim-Subscription-Key**.

    - Så här kan du lägga till den i inställningarna:

    ![Lägga till header för autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), detta kommer att visa en prompt som ber dig ange API-nyckelvärdet som du hittar i Azure-portalen för din Azure API Management-instans.

   - För att lägga till den i *mcp.json* istället, kan du lägga till den så här:

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

### Använd Agent-läge

Nu är vi redo, antingen i inställningarna eller i *.vscode/mcp.json*. Låt oss testa.

Det bör finnas en verktygsikon där de exponerade verktygen från din server listas:

![Verktyg från servern](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicka på verktygsikonen och du bör se en lista med verktyg som så här:

    ![Verktyg](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Ange en prompt i chatten för att anropa verktyget. Till exempel, om du valde ett verktyg för att hämta information om en order, kan du fråga agenten om en order. Här är ett exempel på en prompt:

    ```text
    get information from order 2
    ```

    Du kommer nu att presenteras med en verktygsikon som ber dig fortsätta att anropa ett verktyg. Välj att fortsätta köra verktyget, och du bör nu se ett resultat som så här:

    ![Resultat från prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Vad du ser ovan beror på vilka verktyg du har konfigurerat, men tanken är att du får ett textbaserat svar som ovan.**

## Referenser

Här kan du lära dig mer:

- [Handledning om Azure API Management och MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-exempel: Säkerställ fjärr-MCP-servrar med Azure API Management (experimentellt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klientautentiseringslab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Använd Azure API Management-tillägget för VS Code för att importera och hantera API:er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrera och upptäck fjärr-MCP-servrar i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Fantastiskt repo som visar många AI-funktioner med Azure API Management
- [AI Gateway-workshops](https://azure-samples.github.io/AI-Gateway/) Innehåller workshops med Azure-portalen, vilket är ett utmärkt sätt att börja utvärdera AI-funktioner.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
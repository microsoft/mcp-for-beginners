# Fallstudie: Exponera REST API i API Management som en MCP-server

Azure API Management är en tjänst som tillhandahåller en Gateway ovanpå dina API-slutpunkter. Det fungerar så att Azure API Management agerar som en proxy framför dina API:er och kan bestämma vad som ska göras med inkommande förfrågningar.

Genom att använda detta får du en mängd funktioner som:

- **Säkerhet**, du kan använda allt från API-nycklar, JWT till hanterad identitet.
- **Begränsning av anrop**, en fantastisk funktion är att kunna bestämma hur många anrop som tillåts per viss tidsenhet. Detta hjälper till att säkerställa att alla användare får en bra upplevelse och att din tjänst inte överbelastas med förfrågningar.
- **Skalning och lastbalansering**. Du kan konfigurera ett antal slutpunkter för att balansera belastningen och du kan även bestämma hur "lastbalanseringen" ska ske.
- **AI-funktioner som semantisk cachning**, tokenbegränsning och tokenövervakning med mera. Dessa är utmärkta funktioner som förbättrar svarstiden samt hjälper dig att ha kontroll över din tokenanvändning. [Läs mer här](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Varför MCP + Azure API Management?

Model Context Protocol håller snabbt på att bli en standard för agentbaserade AI-appar och hur man exponera verktyg och data på ett konsekvent sätt. Azure API Management är ett naturligt val när du behöver "hantera" API:er. MCP-servrar integreras ofta med andra API:er för att till exempel lösa förfrågningar mot ett verktyg. Därför är det mycket logiskt att kombinera Azure API Management och MCP.

## Översikt

I detta specifika användningsfall ska vi lära oss att exponera API-slutpunkter som en MCP-server. Genom att göra detta kan vi enkelt göra dessa slutpunkter till en del av en agentbaserad app samtidigt som vi utnyttjar funktionerna från Azure API Management.

## Nyckelfunktioner

- Du väljer vilka slutpunktsmetoder du vill exponera som verktyg.
- De ytterligare funktioner du får beror på vad du konfigurerar i policies-sektionen för ditt API. Här visar vi hur du kan lägga till begränsning av anrop (rate limiting).

## Förberedande steg: importera ett API

Om du redan har ett API i Azure API Management kan du hoppa över detta steg. Om inte, kolla in denna länk, [importera ett API till Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exponera API som MCP-server

För att exponera API-slutpunkterna, följ dessa steg:

1. Navigera till Azure-portalen och följande adress <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navigera till din API Management-instans.

1. I vänstermenyn, välj APIs > MCP Servers > + Skapa ny MCP Server.

1. I API väljer du ett REST API som du vill exponera som MCP-server.

1. Välj en eller flera API-åtgärder att exponera som verktyg. Du kan välja alla åtgärder eller endast specifika.

    ![Välj metoder att exponera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Välj **Skapa**.

1. Navigera till menyalternativen **APIs** och **MCP Servers**, du bör se följande:

    ![Se MCP Server i huvudpanelen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-servern är skapad och API-åtgärderna är exponerade som verktyg. MCP-servern visas i panelen MCP Servers. Kolumnen URL visar slutpunkten för MCP-servern som du kan anropa för testning eller i en klientapplikation.

## Valfritt: Konfigurera policies

Azure API Management har ett kärnbegrepp som kallas policies där du sätter upp olika regler för dina slutpunkter, till exempel begränsning av anrop eller semantisk cachning. Dessa policies skrivs med XML.

Så här kan du konfigurera en policy för att begränsa anrop till din MCP-server:

1. I portalen, under APIs, välj **MCP Servers**.

1. Välj den MCP-server du skapade.

1. I vänstermenyn, under MCP, välj **Policies**.

1. I policyeditorn, lägg till eller redigera de policies du vill applicera på MCP-serverns verktyg. Policies definieras i XML-format. Till exempel kan du lägga till en policy som begränsar anrop till MCP-serverns verktyg (i detta exempel, 5 anrop per 30 sekunder per klient-IP-adress). Här är XML som gör detta:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Här är en bild av policyeditorn:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prova det

Låt oss säkerställa att vår MCP-server fungerar som avsett.

> [!NOTE]
> Azure API Management exponerar för närvarande denna server via Streamable
> HTTP `/mcp`-slutpunkten. Den äldre HTTP+SSE `/sse`-transporten är föråldrad och
> bör endast användas med äldre klienter.

För detta kommer vi använda Visual Studio Code och GitHub Copilot i Agent-läget. Vi kommer att lägga till MCP-servern i en *mcp.json*. Genom att göra detta kommer Visual Studio Code att agera som en klient med agentbaserade funktioner och slutanvändare kommer att kunna skriva in en prompt och interagera med servern.

Så här lägger du till MCP-servern i Visual Studio Code:

1. Använd MCP: **Add Server-kommandot från kommandopaletten**.

1. När du blir tillfrågad, välj servertypen: **HTTP (HTTP eller Server Sent Events)**.

1. Ange den Streamable HTTP-URL som visas för MCP-servern i API Management.
    Till exempel:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Ange ett server-ID efter eget val. Detta är inte ett viktigt värde men det hjälper dig att komma ihåg vilken serverinstans det är.

1. Välj om konfigurationen ska sparas i arbetsytans inställningar eller i användarinställningar.

  - **Arbetsyteinställningar** - Serverkonfigurationen sparas i en .vscode/mcp.json-fil som endast är tillgänglig i den aktuella arbetsytan.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Användarinställningar** - Serverkonfigurationen läggs till i din globala *settings.json*-fil och är tillgänglig i alla arbetsytor. Konfigurationen ser ut ungefär så här:

    ![Användarinställning](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du behöver också lägga till konfiguration, en header för att säkerställa att autentiseringen mot Azure API Management fungerar korrekt. Den använder en header som heter **Ocp-Apim-Subscription-Key**.

    - Så här kan du lägga till den i inställningarna:

    ![Lägga till header för autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), detta kommer att visa en prompt som ber om API-nyckelns värde som du kan hitta i Azure-portalen för din Azure API Management-instans.

   - För att istället lägga till det i *mcp.json* kan du göra så här:

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

### Använd Agent-läget

Nu är vi helt klara, antingen i inställningarna eller i *.vscode/mcp.json*. Låt oss prova.

Det ska finnas en Verktygsikon (Tools) som visar de exponera verktygen från din server:

![Verktyg från servern](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicka på verktygsikonen och du bör se en lista över verktyg enligt nedan:

    ![Verktyg](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Skriv en prompt i chatten för att anropa verktyget. Till exempel, om du valt ett verktyg för att få information om en beställning, kan du fråga agenten om en beställning. Här är ett exempel på prompt:

    ```text
    get information from order 2
    ```

    Nu kommer du få en verktygsikon som frågar om du vill fortsätta att anropa verktyget. Välj att fortsätta köra verktyget, du bör då se ett utdata som nedan:

    ![Resultat från prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Vad du ser ovan beror på vilka verktyg du har konfigurerat, men tanken är att du får ett textbaserat svar som ovan**


## Referenser

Här kan du lära dig mer:

- [Handledning om Azure API Management och MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-exempel: Säker fjärrstyrning av MCP-servrar med Azure API Management (experimentellt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klientauktoriserings-labb](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Använd Azure API Management-tillägget för VS Code för att importera och hantera API:er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrera och upptäck fjärrstyrda MCP-servrar i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Utmärkt repo som visar många AI-funktioner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Innehåller workshops med Azure-portalen, vilket är ett utmärkt sätt att börja utvärdera AI-funktioner.

## Vad är nästa steg

- Tillbaka till: [Översikt över fallstudier](./README.md)
- Nästa: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
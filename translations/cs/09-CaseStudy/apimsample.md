# Případová studie: Zpřístupnění REST API v API Management jako MCP server

Azure API Management je služba, která poskytuje bránu nad vašimi API koncovými body. Funguje tak, že Azure API Management působí jako proxy před vašimi API a rozhoduje, co dělat s příchozími požadavky.

Použitím této služby získáte celou řadu funkcí, jako například:

- **Zabezpečení** – můžete využít vše od API klíčů, JWT až po spravovanou identitu.
- **Omezení rychlosti** – skvělá funkce, která umožňuje rozhodnout, kolik volání projde za určitou časovou jednotku. To pomáhá zajistit skvělý uživatelský zážitek a zároveň chrání vaši službu před přetížením požadavky.
- **Škálování a vyvažování zátěže** – můžete nastavit několik koncových bodů pro vyvážení zátěže a také rozhodnout, jakým způsobem bude zátěž vyvažována.
- **AI funkce jako sémantická cache**, limit tokenů, monitorování tokenů a další. Tyto funkce zlepšují odezvu a pomáhají vám mít přehled o spotřebě tokenů. [Více informací zde](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Proč MCP + Azure API Management?

Model Context Protocol (MCP) se rychle stává standardem pro agentní AI aplikace a způsobem, jak konzistentně zpřístupnit nástroje a data. Azure API Management je přirozenou volbou, když potřebujete "spravovat" API. MCP servery často integrují další API pro zpracování požadavků na nástroje. Proto kombinace Azure API Management a MCP dává velký smysl.

## Přehled

V tomto konkrétním příkladu se naučíme zpřístupnit API koncové body jako MCP server. Tímto způsobem můžeme snadno začlenit tyto koncové body do agentní aplikace a zároveň využít funkcí Azure API Management.

## Klíčové funkce

- Můžete vybrat metody koncových bodů, které chcete zpřístupnit jako nástroje.
- Další funkce závisí na tom, co nakonfigurujete v sekci politik pro vaše API. Zde vám ukážeme, jak přidat omezení rychlosti.

## Předkrok: import API

Pokud již máte API v Azure API Management, můžete tento krok přeskočit. Pokud ne, podívejte se na tento odkaz: [import API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Zpřístupnění API jako MCP server

Pro zpřístupnění API koncových bodů postupujte podle těchto kroků:

1. Přejděte na Azure Portal na následující adresu: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>.  
   Přejděte do instance vašeho API Management.

1. V levém menu vyberte **APIs > MCP Servers > + Create new MCP Server**.

1. V sekci API vyberte REST API, které chcete zpřístupnit jako MCP server.

1. Vyberte jednu nebo více operací API, které chcete zpřístupnit jako nástroje. Můžete vybrat všechny operace nebo jen konkrétní.

    ![Vyberte metody ke zpřístupnění](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Klikněte na **Create**.

1. Přejděte do menu **APIs** a **MCP Servers**, měli byste vidět následující:

    ![Zobrazení MCP serveru v hlavním panelu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je vytvořen a operace API jsou zpřístupněny jako nástroje. MCP server je uveden v panelu MCP Servers. Sloupec URL zobrazuje koncový bod MCP serveru, který můžete použít pro testování nebo v klientské aplikaci.

## Volitelné: Konfigurace politik

Azure API Management má základní koncept politik, kde nastavujete různé pravidla pro vaše koncové body, například omezení rychlosti nebo sémantickou cache. Tyto politiky jsou psány ve formátu XML.

Zde je postup, jak nastavit politiku pro omezení rychlosti vašeho MCP serveru:

1. V portálu, v sekci **APIs**, vyberte **MCP Servers**.

1. Vyberte MCP server, který jste vytvořili.

1. V levém menu, pod MCP, vyberte **Policies**.

1. V editoru politik přidejte nebo upravte politiky, které chcete aplikovat na nástroje MCP serveru. Politiky jsou definovány ve formátu XML. Například můžete přidat politiku, která omezuje volání nástrojů MCP serveru (v tomto příkladu 5 volání za 30 sekund na jednu IP adresu klienta). Zde je XML, které způsobí omezení rychlosti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Zde je obrázek editoru politik:

    ![Editor politik](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Vyzkoušení

Ujistěme se, že náš MCP server funguje podle očekávání.

K tomu použijeme Visual Studio Code a GitHub Copilot v režimu agenta. Přidáme MCP server do souboru *mcp.json*. Tímto způsobem bude Visual Studio Code fungovat jako klient s agentními schopnostmi a koncoví uživatelé budou moci zadávat výzvy a interagovat s tímto serverem.

Postup přidání MCP serveru do Visual Studio Code:

1. Použijte příkaz **MCP: Add Server** z Command Palette.

1. Když budete vyzváni, vyberte typ serveru: **HTTP (HTTP nebo Server Sent Events)**.

1. Zadejte URL MCP serveru v API Management. Příklad: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (pro SSE endpoint) nebo **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (pro MCP endpoint). Všimněte si rozdílu mezi transporty `/sse` nebo `/mcp`.

1. Zadejte ID serveru dle vašeho výběru. Toto není důležitá hodnota, ale pomůže vám si zapamatovat, co je tato instance serveru.

1. Vyberte, zda chcete konfiguraci uložit do nastavení pracovního prostoru nebo uživatelského nastavení.

  - **Nastavení pracovního prostoru** – Konfigurace serveru je uložena do souboru .vscode/mcp.json, který je dostupný pouze v aktuálním pracovním prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    nebo pokud zvolíte streaming HTTP jako transport, bude to mírně odlišné:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Uživatelské nastavení** – Konfigurace serveru je přidána do vašeho globálního souboru *settings.json* a je dostupná ve všech pracovních prostorech. Konfigurace vypadá podobně jako následující:

    ![Uživatelské nastavení](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Také musíte přidat konfiguraci, hlavičku pro správné ověření vůči Azure API Management. Používá se hlavička nazvaná **Ocp-Apim-Subscription-Key**.

    - Zde je postup, jak ji přidat do nastavení:

    ![Přidání hlavičky pro ověření](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). Tím se zobrazí výzva k zadání hodnoty API klíče, kterou najdete v Azure Portalu pro vaši instanci Azure API Management.

   - Pokud ji chcete přidat do *mcp.json*, můžete ji přidat takto:

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

### Použití režimu agenta

Nyní máme vše nastaveno buď v nastavení, nebo v *.vscode/mcp.json*. Vyzkoušejme to.

Měla by se zobrazit ikona nástrojů, kde jsou uvedeny zpřístupněné nástroje z vašeho serveru:

![Nástroje ze serveru](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikněte na ikonu nástrojů a měli byste vidět seznam nástrojů, jako je tento:

    ![Nástroje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Zadejte výzvu do chatu pro spuštění nástroje. Například pokud jste vybrali nástroj pro získání informací o objednávce, můžete se agenta zeptat na objednávku. Zde je příklad výzvy:

    ```text
    get information from order 2
    ```

    Nyní se zobrazí ikona nástrojů, která vás vyzve k pokračování v volání nástroje. Vyberte pokračování, měli byste nyní vidět výstup, jako je tento:

    ![Výsledek výzvy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **To, co vidíte výše, závisí na tom, jaké nástroje jste nastavili, ale myšlenka je, že dostanete textovou odpověď jako výše.**

## Odkazy

Zde se můžete dozvědět více:

- [Návod na Azure API Management a MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python ukázka: Zabezpečení vzdálených MCP serverů pomocí Azure API Management (experimentální)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratoř autorizace MCP klienta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Použití rozšíření Azure API Management pro VS Code k importu a správě API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrace a objevování vzdálených MCP serverů v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Skvělý repozitář ukazující mnoho AI schopností s Azure API Management
- [Workshopy AI Gateway](https://azure-samples.github.io/AI-Gateway/) Obsahuje workshopy využívající Azure Portal, což je skvělý způsob, jak začít hodnotit AI schopnosti.

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
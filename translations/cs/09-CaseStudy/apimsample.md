# Studie případu: Zveřejnění REST API v API Management jako MCP server

Azure API Management je služba, která poskytuje bránu nad vašimi API koncovými body. Funguje tak, že Azure API Management působí jako proxy před vašimi API a může rozhodnout, co dělat s příchozími požadavky.

Při jeho použití získáte celou řadu funkcí, jako například:

- **Bezpečnost**, můžete použít vše od API klíčů, JWT až po spravovanou identitu.
- **Omezení rychlosti (Rate limiting)**, skvělou funkcí je možnost rozhodnout, kolik volání projde za určitou časovou jednotku. To pomáhá zajistit, aby všichni uživatelé měli skvělý zážitek a také aby vaše služba nebyla přetížená požadavky.
- **Škálování a vyvažování zátěže**. Můžete nastavit několik koncových bodů pro rozložení zátěže a také můžete rozhodnout, jak "vyvažovat zátěž".
- **AI funkce jako sémantické cachování**, limit tokenů, monitorování tokenů a další. Jsou to skvělé funkce které zlepšují odezvu a také pomáhají mít přehled o spotřebě tokenů. [Přečtěte si více zde](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Proč MCP + Azure API Management?

Model Context Protocol se rychle stává standardem pro agentické AI aplikace a jak vystavit nástroje a data konzistentním způsobem. Azure API Management je přirozená volba, když potřebujete "spravovat" API. MCP servery se často integrují s dalšími API, aby například vyřešily požadavky na nástroj. Proto dává kombinace Azure API Management a MCP velký smysl.

## Přehled

V tomto konkrétním případu použití se naučíme vystavit API koncové body jako MCP Server. Tímto způsobem můžeme snadno začlenit tyto koncové body do agentní aplikace a zároveň využívat funkce Azure API Management.

## Klíčové funkce

- Vyberete metody koncového bodu, které chcete vystavit jako nástroje.
- Další funkce, které získáte, závisí na tom, co nakonfigurujete v sekci politik pro vaše API. Zde vám však ukážeme, jak přidat omezení rychlosti.

## Předkrok: import API

Pokud již máte API v Azure API Management, skvělé, můžete tento krok přeskočit. Pokud ne, podívejte se na tento odkaz, [import API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Zveřejnění API jako MCP Server

Pro vystavení API koncových bodů postupujte podle těchto kroků:

1. Přejděte do Azure Portálu na adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Navigujte do vaší instance API Managementu.

1. V levém menu vyberte APIs > MCP Servers > + Vytvořit nový MCP Server.

1. V API vyberte REST API, které chcete vystavit jako MCP server.

1. Vyberte jednu nebo více operací API, které chcete vystavit jako nástroje. Můžete vybrat všechny operace nebo jen konkrétní.

    ![Vyberte metody k vystavení](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Vyberte **Vytvořit**.

1. Přejděte do menu **APIs** a **MCP Servers**, měli byste vidět následující:

    ![Zobrazit MCP Server v hlavním panelu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je vytvořen a API operace jsou vystaveny jako nástroje. MCP server je uveden v panelu MCP Servers. Sloupec URL ukazuje koncový bod MCP serveru, který můžete volat pro testování nebo v klientské aplikaci.

## Volitelné: Konfigurace politik

Azure API Management má základní koncept politik, kde nastavujete různá pravidla pro vaše koncové body, například omezení rychlosti nebo sémantické cachování. Tyto politiky jsou vytvářeny v XML.

Zde je návod, jak nastavit politiku pro omezení rychlosti vašeho MCP Serveru:

1. V portálu, v sekci APIs, vyberte **MCP Servers**.

1. Vyberte MCP server, který jste vytvořili.

1. V levém menu, pod MCP, vyberte **Policies**.

1. V editoru politik přidejte nebo upravte politiky, které chcete aplikovat na nástroje MCP serveru. Politiky jsou definovány ve formátu XML. Například můžete přidat politiku, která omezuje volání nástrojů MCP serveru (v tomto příkladu 5 volání za 30 sekund na IP adresu klienta). Zde je XML, které to způsobí:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Zde je obrázek editoru politik:

    ![Editor politik](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Vyzkoušejte to

Ujistěme se, že náš MCP Server funguje, jak má.

> [!NOTE]
> Azure API Management aktuálně vystavuje tento server přes Streamable
> HTTP `/mcp` endpoint. Starší HTTP+SSE `/sse` transport je zastaralý a
> měl by být používán pouze s legacy klienty.

Pro tento účel použijeme Visual Studio Code a GitHub Copilot v agentním režimu. Přidáme MCP server do souboru *mcp.json*. Tím Visual Studio Code bude fungovat jako klient s agentními schopnostmi a koncoví uživatelé budou moci zadat prompt a interagovat s tímto serverem.

Podívejme se, jak přidat MCP server ve Visual Studio Code:

1. Použijte příkaz MCP: **Add Server z Command Palette**.

1. Když jste vyzváni, vyberte typ serveru: **HTTP (HTTP nebo Server Sent Events)**.

1. Zadejte URL Streamable HTTP uvedenou pro MCP server v API Management.
    Například:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Zadejte ID serveru dle vlastního výběru. Není to důležitá hodnota, ale pomůže vám zapamatovat si, co tato instance serveru představuje.

1. Vyberte, zda chcete konfiguraci uložit do nastavení workspace nebo uživatele.

  - **Nastavení workspace** - Konfigurace serveru je uložena pouze do souboru .vscode/mcp.json dostupného v aktuálním workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Nastavení uživatele** - Konfigurace serveru je přidána do globálního souboru *settings.json* a je dostupná ve všech workspacech. Konfigurace vypadá přibližně takto:

    ![Nastavení uživatele](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Můžete také přidat konfiguraci v hlavičce, aby se správně autentizoval vůči Azure API Management. Používá hlavičku nazvanou **Ocp-Apim-Subscription-Key**.

    - Zde je, jak ji můžete přidat do nastavení:

    ![Přidání hlavičky pro autentizaci](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), toto způsobí zobrazení výzvy k zadání hodnoty API klíče, kterou najdete v Azure Portálu pro vaši instanci Azure API Management.

   - Pokud ji chcete přidat přímo do *mcp.json*, můžete to udělat takto:

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

### Použijte agentní režim

Nyní jsme vše nastavili v nastavení nebo v *.vscode/mcp.json*. Zkusme to.

Měla by se zobrazit ikona Nástrojů, kde jsou vypsány vystavené nástroje z vašeho serveru:

![Nástroje ze serveru](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikněte na ikonu nástrojů, měli byste vidět seznam nástrojů takto:

    ![Nástroje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Zadejte prompt do chatu pro zavolání nástroje. Například pokud jste vybrali nástroj pro získání informací o objednávce, můžete se agenta zeptat na objednávku. Zde je ukázkový prompt:

    ```text
    get information from order 2
    ```

    Nyní bude zobrazena ikona nástrojů s výzvou pokračovat ve volání nástroje. Vyberte pokračovat ve spouštění nástroje, měli byste vidět výstup takto:

    ![Výsledek z promptu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **to, co vidíte výše, záleží na nástrojích, které jste nastavili, ale jde o to, že dostanete textovou odpověď jako výše**


## Reference

Zde se můžete dozvědět více:

- [Tutorial k Azure API Management a MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python příklad: Bezpečné vzdálené MCP servery pomocí Azure API Management (experimentální)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratoř autorizace MCP klienta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Použití rozšíření Azure API Management ve VS Code pro import a správu API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrace a objevování vzdálených MCP serverů v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Skvělý repozitář, který ukazuje mnoho AI schopností s Azure API Management
- [Workshopy AI Gateway](https://azure-samples.github.io/AI-Gateway/) Obsahuje workshopy přes Azure Portal, což je skvělý způsob, jak začít hodnotit schopnosti AI.

## Co dál

- Zpět na: [Přehled studií případů](./README.md)
- Dále: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
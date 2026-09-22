# Prípadová štúdia: Zverejnenie REST API v API Management ako MCP server

Azure API Management je služba, ktorá poskytuje bránu nad vašimi API Endpoints. Funguje tak, že Azure API Management pôsobí ako proxy pred vašimi API a môže rozhodovať, čo robiť s prichádzajúcimi požiadavkami.

Používaním pridáte množstvo funkcií, ako napríklad:

- **Bezpečnosť**, môžete použiť všetko od API kľúčov, JWT až po spravovanú identitu.
- **Obmedzenie rýchlosti (Rate limiting)**, skvelá funkcia, ktorá umožňuje rozhodnúť, koľko volaní prejde za určitú časovú jednotku. Pomáha zabezpečiť, aby mali všetci používatelia skvelý zážitok a zároveň aby vaša služba nebola preťažená požiadavkami.
- **Škálovanie a vyrovnávanie záťaže**. Môžete nastaviť počet endpointov na rozloženie záťaže a tiež rozhodnúť, ako sa bude vykonávať „load balancing“.
- **Funkcie AI ako sémantické cachovanie**, limit tokenov a monitorovanie tokenov a ďalšie. Tieto skvelé funkcie zlepšujú odozvu a zároveň pomáhajú mať prehľad o vašom míňaní tokenov. [Čítajte viac tu](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Prečo MCP + Azure API Management?

Model Context Protocol sa rýchlo stáva štandardom pre agentné AI aplikácie a spôsob, ako konzistentne zverejňovať nástroje a dáta. Azure API Management je prirodzená voľba, keď potrebujete „spravovať“ API. MCP servery často integrujú iné API na vyriešenie požiadaviek, napríklad na nástroj. Preto kombinácia Azure API Management a MCP dáva veľký zmysel.

## Prehľad

V tejto konkrétnej prípadovej štúdii sa naučíme zverejniť API endpointy ako MCP server. Týmto spôsobom môžeme ľahko spraviť tieto endpointy súčasťou agentnej aplikácie a zároveň využiť funkcie Azure API Management.

## Kľúčové funkcie

- Vyberiete metódy endpointu, ktoré chcete zverejniť ako nástroje.
- Ďalšie funkcie, ktoré získate, závisia od toho, čo nastavíte v sekcii politiky pre vaše API. Tu vám ukážeme, ako pridať obmedzenie rýchlosti (rate limiting).

## Predkrok: import API

Ak už máte API v Azure API Management, skvelé, tento krok môžete preskočiť. Ak nie, pozrite si tento odkaz: [import API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Zverejnenie API ako MCP server

Na zverejnenie API endpointov postupujte podľa týchto krokov:

1. Prejdite do Azure portálu na adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Prejdite na svoju inštanciu API Management.

1. V ľavom menu vyberte APIs > MCP Servers > + Vytvoriť nový MCP Server.

1. V API vyberte REST API, ktoré chcete zverejniť ako MCP server.

1. Vyberte jednu alebo viac operácií API, ktoré chcete zverejniť ako nástroje. Môžete vybrať všetky operácie alebo len určité.

    ![Vyberte metódy na zverejnenie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Vyberte **Vytvoriť**.

1. Prejdite do menu **APIs** a **MCP Servers**, mali by ste vidieť nasledujúce:

    ![Zobrazte MCP Server v hlavnej časti](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je vytvorený a operácie API sú zverejnené ako nástroje. MCP server je uvedený v paneli MCP Servers. Stĺpec URL zobrazuje endpoint MCP servera, ktorý môžete volať na testovanie alebo v klientskej aplikácii.

## Voliteľné: Konfigurácia politík

Azure API Management má základný koncept politík, v ktorých nastavujete rôzne pravidlá pre vaše endpointy, napríklad obmedzenie rýchlosti alebo sémantické cachovanie. Tieto politiky sa píšu v XML.

Takto môžete nastaviť politiku na obmedzenie rýchlosti vášho MCP servera:

1. V portáli, pod APIs, vyberte **MCP Servers**.

1. Vyberte MCP server, ktorý ste vytvorili.

1. V ľavom menu, pod MCP, vyberte **Policies**.

1. V editore politiky pridajte alebo upravte politiky, ktoré chcete aplikovať na nástroje MCP servera. Politiky sú definované v XML formáte. Napríklad môžete pridať politiku na obmedzenie volaní nástrojov MCP servera (v tomto príklade 5 volaní za 30 sekúnd na IP adresu klienta). Tu je XML, ktorý to spôsobí obmedzenie rýchlosti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tu je obrázok editora politík:

    ![Editor politík](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Vyskúšajte to

Uistime sa, že náš MCP server funguje podľa očakávania.

> [!NOTE]
> Azure API Management aktuálne zverejňuje tento server cez Streamable
> HTTP `/mcp` endpoint. Starší HTTP+SSE `/sse` prenos je zastaraný a
> mal by sa používať iba s legacy klientmi.

Na to použijeme Visual Studio Code a GitHub Copilot a jeho agentný režim. Pridáme MCP server do súboru *mcp.json*. Týmto spôsobom bude Visual Studio Code fungovať ako klient s agentnými schopnosťami a koncoví používatelia budú môcť zadať prompt a komunikovať s daným serverom.

Pozrime sa, ako pridať MCP server vo Visual Studio Code:

1. Použite príkaz MCP: **Add Server z Command Palette**.

1. Keď budete vyzvaní, vyberte typ servera: **HTTP (HTTP alebo Server Sent Events)**.

1. Zadajte Streamable HTTP URL zobrazené pre MCP server v API Management.
    Napríklad:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Zadajte ID servera podľa vlastného výberu. Nie je to dôležitá hodnota, ale pomôže vám zapamätať si, čo táto inštancia servera je.

1. Vyberte, či chcete uložiť konfiguráciu do nastavení pracovného priestoru alebo používateľa.

  - **Nastavenia pracovného priestoru** - Konfigurácia servera sa uloží do súboru .vscode/mcp.json, ktorý je dostupný len v aktuálnom pracovnom priestore.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Nastavenia používateľa** - Konfigurácia servera sa pridá do vášho globálneho súboru *settings.json* a je dostupná vo všetkých pracovných priestoroch. Konfigurácia vyzerá podobne ako nasledujúco:

    ![Nastavenie používateľa](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Tiež musíte pridať konfiguráciu, hlavičku, aby sa zabezpečila správna autentifikácia voči Azure API Management. Používa hlavičku s názvom **Ocp-Apim-Subscription-Key**.

    - Takto ju môžete pridať do nastavení:

    ![Pridanie hlavičky na autentifikáciu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), toto spôsobí zobrazenie promptu, ktorý si vyžiada hodnotu API kľúča, ktorú nájdete v portáli Azure pre vašu inštanciu Azure API Management.

   - Ak ju chcete pridať do *mcp.json*, môžete ju pridať takto:

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

### Použitie agentného režimu

Teraz sme pripravení v nastaveniach alebo v *.vscode/mcp.json*. Vyskúšajme to.

Mala by sa zobraziť ikona Nástroje, kde sú uvedené zverejnené nástroje z vášho servera:

![Nástroje zo servera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite na ikonu nástrojov a mali by ste vidieť zoznam nástrojov ako takýto:

    ![Nástroje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Zadajte prompt v chate na vyvolanie nástroja. Napríklad, ak ste vybrali nástroj na získanie informácií o objednávke, môžete sa agenta opýtať na objednávku. Tu je príklad promptu:

    ```text
    get information from order 2
    ```

    Teraz sa vám zobrazí ikona nástrojov s výzvou pokračovať vo volaní nástroja. Vyberte pokračovanie v spustení nástroja, mali by ste vidieť výstup ako takýto:

    ![Výsledok z promptu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Čo vidíte vyššie, závisí od toho, aké nástroje ste nastavili, ale ide o to, že dostanete textovú odpoveď ako vyššie**


## Referencie

Tu sa môžete dozvedieť viac:

- [Návod na Azure API Management a MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python príklad: Bezpečné vzdialené MCP servery pomocou Azure API Management (experimentálne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratórium na autorizáciu MCP klienta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Použite rozšírenie Azure API Management pre VS Code na import a správu API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrácia a zisťovanie vzdialených MCP serverov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Skvelé repozitár, ktorý ukazuje mnohé AI funkcie s Azure API Management
- [AI Gateway workshopy](https://azure-samples.github.io/AI-Gateway/) Obsahuje workshopy využívajúce Azure Portal, čo je skvelý spôsob, ako začať hodnotiť AI funkcie.

## Čo bude ďalej

- Späť na: [Prehľad prípadových štúdií](./README.md)
- Ďalej: [Azure AI cestovné agenti](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
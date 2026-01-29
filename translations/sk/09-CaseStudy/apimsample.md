# Prípadová štúdia: Zverejnenie REST API v API Management ako MCP server

Azure API Management je služba, ktorá poskytuje bránu nad vašimi API koncovými bodmi. Funguje tak, že Azure API Management pôsobí ako proxy pred vašimi API a rozhoduje, čo robiť s prichádzajúcimi požiadavkami.

Použitím tejto služby získate množstvo funkcií, ako napríklad:

- **Bezpečnosť** – môžete využiť všetko od API kľúčov, JWT až po spravovanú identitu.
- **Obmedzenie rýchlosti** – skvelá funkcia, ktorá umožňuje rozhodnúť, koľko volaní prejde za určitú časovú jednotku. To pomáha zabezpečiť skvelý zážitok pre všetkých používateľov a zároveň chráni vašu službu pred preťažením požiadavkami.
- **Škálovanie a vyvažovanie záťaže** – môžete nastaviť viacero koncových bodov na vyvažovanie záťaže a rozhodnúť, ako sa má záťaž vyvažovať.
- **AI funkcie ako sémantické cachovanie**, limit tokenov, monitorovanie tokenov a ďalšie. Tieto funkcie zlepšujú odozvu a pomáhajú vám mať prehľad o spotrebe tokenov. [Prečítajte si viac tu](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Prečo MCP + Azure API Management?

Model Context Protocol (MCP) sa rýchlo stáva štandardom pre agentické AI aplikácie a spôsob, ako konzistentne sprístupniť nástroje a dáta. Azure API Management je prirodzenou voľbou, keď potrebujete „spravovať“ API. MCP servery často integrujú iné API na riešenie požiadaviek na nástroje. Preto kombinácia Azure API Management a MCP dáva veľký zmysel.

## Prehľad

V tomto konkrétnom prípade sa naučíme, ako zverejniť API koncové body ako MCP server. Týmto spôsobom môžeme tieto koncové body jednoducho začleniť do agentickej aplikácie a zároveň využiť funkcie Azure API Management.

## Kľúčové funkcie

- Vyberiete si metódy koncových bodov, ktoré chcete zverejniť ako nástroje.
- Dodatočné funkcie závisia od toho, čo nakonfigurujete v sekcii politiky pre vaše API. Tu vám však ukážeme, ako pridať obmedzenie rýchlosti.

## Predkrok: Import API

Ak už máte API v Azure API Management, môžete tento krok preskočiť. Ak nie, pozrite si tento odkaz: [importovanie API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Zverejnenie API ako MCP server

Na zverejnenie API koncových bodov postupujte podľa týchto krokov:

1. Prejdite na Azure Portal na nasledujúcu adresu: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Prejdite na svoju inštanciu API Management.

1. V ľavom menu vyberte **APIs > MCP Servers > + Create new MCP Server**.

1. V sekcii API vyberte REST API, ktoré chcete zverejniť ako MCP server.

1. Vyberte jednu alebo viac operácií API, ktoré chcete zverejniť ako nástroje. Môžete vybrať všetky operácie alebo len konkrétne operácie.

    ![Výber metód na zverejnenie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Kliknite na **Create**.

1. Prejdite do menu **APIs** a **MCP Servers**, kde by ste mali vidieť nasledujúce:

    ![Zobrazenie MCP servera v hlavnom paneli](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je vytvorený a operácie API sú zverejnené ako nástroje. MCP server je uvedený v paneli MCP Servers. Stĺpec URL zobrazuje koncový bod MCP servera, ktorý môžete použiť na testovanie alebo v klientských aplikáciách.

## Voliteľné: Konfigurácia politík

Azure API Management má základný koncept politík, kde nastavujete rôzne pravidlá pre vaše koncové body, napríklad obmedzenie rýchlosti alebo sémantické cachovanie. Tieto politiky sú vytvárané v XML.

Tu je postup, ako nastaviť politiku na obmedzenie rýchlosti pre váš MCP server:

1. V portáli, v sekcii **APIs**, vyberte **MCP Servers**.

1. Vyberte MCP server, ktorý ste vytvorili.

1. V ľavom menu, v sekcii MCP, vyberte **Policies**.

1. V editore politík pridajte alebo upravte politiky, ktoré chcete aplikovať na nástroje MCP servera. Politiky sú definované vo formáte XML. Napríklad môžete pridať politiku na obmedzenie volaní na nástroje MCP servera (v tomto príklade 5 volaní za 30 sekúnd na jednu IP adresu klienta). Tu je XML, ktoré spôsobí obmedzenie rýchlosti:

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

Uistime sa, že náš MCP server funguje podľa očakávaní.

Na tento účel použijeme Visual Studio Code a GitHub Copilot v režime Agent. Pridáme MCP server do súboru *mcp.json*. Týmto spôsobom bude Visual Studio Code fungovať ako klient s agentickými schopnosťami a koncoví používatelia budú môcť zadať výzvu a interagovať s daným serverom.

Pozrime sa, ako pridať MCP server vo Visual Studio Code:

1. Použite príkaz **MCP: Add Server** z Command Palette.

1. Keď budete vyzvaní, vyberte typ servera: **HTTP (HTTP alebo Server Sent Events)**.

1. Zadajte URL MCP servera v API Management. Príklad: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (pre SSE endpoint) alebo **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (pre MCP endpoint), všimnite si rozdiel medzi transportmi `/sse` alebo `/mcp`.

1. Zadajte ID servera podľa vášho výberu. Táto hodnota nie je dôležitá, ale pomôže vám zapamätať si, o aký server ide.

1. Vyberte, či chcete konfiguráciu uložiť do nastavení pracovného priestoru alebo používateľských nastavení.

  - **Nastavenia pracovného priestoru** – Konfigurácia servera sa uloží do súboru .vscode/mcp.json, ktorý je dostupný iba v aktuálnom pracovnom priestore.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    alebo ak si vyberiete streaming HTTP ako transport, bude to mierne odlišné:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Používateľské nastavenia** – Konfigurácia servera sa pridá do vášho globálneho súboru *settings.json* a je dostupná vo všetkých pracovných priestoroch. Konfigurácia vyzerá podobne ako nasledujúce:

    ![Používateľské nastavenie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Tiež musíte pridať konfiguráciu, hlavičku na správne overenie voči Azure API Management. Používa sa hlavička s názvom **Ocp-Apim-Subscription-Key**.

    - Tu je postup, ako ju pridať do nastavení:

    ![Pridanie hlavičky na autentifikáciu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), toto spôsobí, že sa zobrazí výzva na zadanie hodnoty API kľúča, ktorú nájdete v Azure Portal pre vašu inštanciu Azure API Management.

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

### Použitie režimu Agent

Teraz sme všetko nastavili buď v nastaveniach, alebo v *.vscode/mcp.json*. Poďme to vyskúšať.

Mala by sa zobraziť ikona nástrojov, kde sú uvedené nástroje z vášho servera:

![Nástroje zo servera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite na ikonu nástrojov a mali by ste vidieť zoznam nástrojov, ako je tento:

    ![Nástroje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Zadajte výzvu do chatu na vyvolanie nástroja. Napríklad, ak ste vybrali nástroj na získanie informácií o objednávke, môžete sa agenta opýtať na objednávku. Tu je príklad výzvy:

    ```text
    get information from order 2
    ```

    Teraz by sa mala zobraziť ikona nástrojov, ktorá vás vyzve na pokračovanie v spustení nástroja. Vyberte možnosť pokračovať v spustení nástroja, mali by ste teraz vidieť výstup, ako je tento:

    ![Výsledok z výzvy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **To, čo vidíte vyššie, závisí od toho, aké nástroje ste nastavili, ale myšlienka je, že dostanete textovú odpoveď, ako je uvedené vyššie.**

## Referencie

Tu sa môžete dozvedieť viac:

- [Tutoriál o Azure API Management a MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python ukážka: Zabezpečenie vzdialených MCP serverov pomocou Azure API Management (experimentálne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratórium autorizácie MCP klienta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Použitie rozšírenia Azure API Management pre VS Code na import a správu API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrácia a objavovanie vzdialených MCP serverov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Skvelé úložisko, ktoré ukazuje mnoho AI schopností s Azure API Management
- [AI Gateway workshopy](https://azure-samples.github.io/AI-Gateway/) Obsahuje workshopy využívajúce Azure Portal, čo je skvelý spôsob, ako začať hodnotiť AI schopnosti.

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
# Esettanulmány: REST API közzététele API Management-ben MCP szerverként

Az Azure API Management egy olyan szolgáltatás, amely kaput biztosít az API végpontjaid fölött. Működése során az Azure API Management úgy viselkedik, mint egy proxy az API-k előtt, és eldöntheti, mit tegyen a bejövő kérésekkel.

Használatával számos funkciót adhatsz hozzá, például:

- **Biztonság**, használhatsz mindent az API kulcsoktól, JWT-n át a kezelt identitásig.
- **Híváskorlátozás**, egy nagyszerű funkció, hogy meg tudod határozni, hány hívás juthat át egy adott időegységen belül. Ez segít biztosítani, hogy minden felhasználó kiváló élményben részesüljön, és hogy a szolgáltatásod ne legyen túlterhelve kérésekkel.
- **Skálázás és terheléselosztás**. Több végpontot is beállíthatsz a terhelés kiegyensúlyozására, és dönthetsz arról is, hogyan történjen a "terhelés elosztás".
- **AI funkciók, például szemantikus gyorsítótárazás**, tokenlimit és tokenfigyelés, és még sok más. Ezek nagyszerű funkciók, amelyek javítják a válaszidőt, valamint segítenek nyomon követni a token felhasználást. [További információ itt](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miért MCP + Azure API Management?

A Model Context Protocol gyorsan szabvánnyá válik az ügynöki AI alkalmazások és eszközök, valamint adatok következetes kitettségére. Az Azure API Management természetes választás, amikor API-kat kell "kezelni". Az MCP szerverek gyakran integrálódnak más API-kkal, hogy például egy eszköz kérését kezeljék. Ezért az Azure API Management és az MCP kombinálása nagyon logikus.

## Áttekintés

Ebben a konkrét esetben megtanuljuk, hogyan tehetjük elérhetővé az API végpontokat MCP szerverként. Ezzel könnyedén integrálhatjuk ezeket az végpontokat ügynöki alkalmazás részévé, miközben kihasználjuk az Azure API Management funkcióit.

## Főbb jellemzők

- Kiválasztod azokat a végpont metódusokat, amelyeket eszközként szeretnél elérhetővé tenni.
- A további funkciók attól függnek, hogy milyen beállításokat adsz meg az API szabályzat részében. Itt például megmutatjuk, hogyan adhatsz hozzá híváskorlátozást.

## Előzetes lépés: API importálása

Ha már van API-d az Azure API Management-ben, az nagyszerű, átugorhatod ezt a lépést. Ha nincs, nézd meg ezt a linket: [API importálása az Azure API Management-be](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API közzététele MCP szerverként

Az API végpontok közzétételéhez kövesd az alábbi lépéseket:

1. Navigálj az Azure Portalra a következő címen: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Lépj be az API Management példányodhoz.

1. A bal oldali menüben válaszd az APIs > MCP Servers > + Új MCP Server létrehozása menüpontot.

1. Az API-nál válassz egy REST API-t, amelyet MCP szerverként szeretnél közzétenni.

1. Válassz egy vagy több API műveletet, amelyeket eszközként szeretnél elérhetővé tenni. Kiválaszthatod az összes műveletet vagy csak bizonyosakat.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Válaszd a **Létrehozás** gombot.

1. Navigálj az **APIs** és **MCP Servers** menüpontokhoz, az alábbiakat kell látnod:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Az MCP szerver létrejött és az API műveletek eszközként elérhetővé váltak. Az MCP szerver megjelenik az MCP Servers panelen. Az URL oszlopban látható az MCP szerver végpontja, amelyet teszteléshez vagy ügyfélalkalmazásban hívhatsz.

## Opcionális: Szabályzatok beállítása

Az Azure API Management alapvető koncepciója a szabályzatok rendszere, ahol különböző szabályokat adhatsz meg végpontjaidhoz, például híváskorlátozást vagy szemantikus gyorsítótárazást. Ezeket a szabályzatokat XML-ben írják.

Így állíthatsz be egy szabályzatot az MCP szervered híváskorlátozására:

1. A portálon, az APIs alatt válaszd az **MCP Servers**-t.

1. Válaszd ki a létrehozott MCP szervert.

1. A bal oldali menüben, az MCP alatt válaszd a **Policies** lehetőséget.

1. A szabályzat szerkesztőben add hozzá vagy szerkeszd azokat a szabályzatokat, amelyeket az MCP szerver eszközeihez alkalmazni szeretnél. A szabályzatokat XML formátumban definiálják. Például hozzáadhatsz egy szabályzatot, amely korlátozza a hívások számát az MCP szerver eszközeihez (ebben a példában 5 hívás 30 másodpercenként ügyfelenként IP címenként). Íme az XML, amely ezt megvalósítja:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Íme egy kép a szabályzat szerkesztőről:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Próbáld ki

Ellenőrizzük, hogy az MCP szerverünk rendeltetésszerűen működik.

> [!NOTE]
> Az Azure API Management jelenleg ezen szervert a Streamable
> HTTP `/mcp` végponton keresztül teszi elérhetővé. A régebbi HTTP+SSE `/sse` szállítási mód elavult,
> és csak régi ügyfelekkel kell használni.

Ehhez a Visual Studio Code-ot és a GitHub Copilot ügynök módját használjuk. Hozzáadjuk az MCP szervert egy *mcp.json* fájlhoz. Ezzel a Visual Studio Code egy ügynöki képességekkel rendelkező kliensként viselkedik, és a végfelhasználók beírhatnak egy promptot és interakcióba léphetnek a szerverrel.

Nézzük, hogyan adhatod hozzá az MCP szervert Visual Studio Code-ban:

1. Használd az MCP: **Szerver hozzáadása parancsot a Parancspalettából**.

1. A felkérésre válaszd ki a szerver típusát: **HTTP (HTTP vagy Server Sent Events)**.

1. Írd be az MCP szerverhez az Azure API Management-ben látott Streamable HTTP URL-t.
    Például:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Írj be egy tetszőleges szerverazonosítót. Ez nem létfontosságú érték, de segít emlékezni, hogy melyik szerver példányról van szó.

1. Válaszd ki, hogy a konfigurációt a munkaterület beállításaiba vagy a felhasználói beállításokba mented-e.

  - **Munkaterület beállítások** - A szerver konfiguráció csak a jelenlegi munkaterületen elérhető .vscode/mcp.json fájlba kerül mentésre.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Felhasználói beállítások** - A szerver konfiguráció a globális *settings.json* fájlba kerül hozzáadásra, és minden munkaterületen elérhető. A konfiguráció hasonlóan néz ki, mint az alábbi:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Adnod kell még hozzá egy fejlécet is a konfigurációhoz, hogy helyesen hitelesítsen az Azure API Management felé. Ehhez egy **Ocp-Apim-Subscription-Key** nevű fejlécet használ.

    - Így adhatod hozzá beállításként:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ez megjelenít egy promptot, amelyben meg kell adnod az API kulcs értékét, amelyet az Azure Portálon találhatsz meg az Azure API Management példányodhoz.

   - Ha inkább a *mcp.json*-hez szeretnéd hozzáadni, így teheted meg:

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

### Ügynök mód használata

Most, hogy mindent beállítottunk a beállításokban vagy a *.vscode/mcp.json* fájlban, próbáljuk ki.

Egy eszköz ikon kell, hogy megjelenjen, ahol a szerver által közzétett eszközök listája látható:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kattints az eszköz ikonra, és egy ilyen eszközök listáját kell látnod:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Írj be egy promptot a csevegőbe az eszköz meghívásához. Például ha kiválasztottál egy eszközt egy megrendeléssel kapcsolatos információ lekérésére, megkérdezheted az ügynöktől a megrendelésről. Íme egy példa prompt:

    ```text
    get information from order 2
    ```

    Most megjelenik egy eszköz ikon, amely rákérdez, hogy folytatod-e az eszköz hívását. Válaszd a folytatást, és az alábbihoz hasonló eredményt kell látnod:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **A fenti eredmény attól függ, milyen eszközöket állítottál be, de az ötlet az, hogy szöveges választ kapsz, mint a fenti.**


## Hivatkozások

Íme, hol tudsz többet tanulni:

- [Útmutató az Azure API Management és MCP használatához](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python példa: Távoli MCP szerverek biztonságos használata Azure API Management-tel (kísérleti)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliens jogosultság labor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Az Azure API Management bővítmény használata VS Code-ban API-k importálására és kezelésére](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Távoli MCP szerverek regisztrálása és felfedezése az Azure API Centerben](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Kiváló repó, amely számos AI funkciót mutat be Azure API Management-tel
- [AI Gateway műhelyek](https://azure-samples.github.io/AI-Gateway/) Tartalmaz Azure Portal használatával készült műhelyeket, amelyek remek kiindulópontok az AI képességek kiértékeléséhez.

## Mi a következő lépés

- Vissza: [Esettanulmányok áttekintése](./README.md)
- Következő: [Azure AI utazási ügynökök](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
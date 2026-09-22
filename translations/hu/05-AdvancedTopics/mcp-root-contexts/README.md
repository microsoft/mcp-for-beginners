# MCP Gyökerek (Elavult funkció)

> [!WARNING]
> A gyökerek az MCP `2026-07-28` verziója óta elavultak. Ez a felülvizsgálat továbbra is tartalmazza őket
> kompatibilitás miatt, és eltávolításra kerülhet az első olyan specifikációs
> felülvizsgálatban, amely 2027. július 28-án vagy azután jelenik meg. Az új megvalósításoknak
> könyvtárakat vagy fájlokat kell átadniuk eszközparamétereken, erőforrás-URI-kon vagy szerver-
> konfiguráción keresztül.

## Áttekintés

A gyökerek lehetővé teszik, hogy egy MCP kliens a szervernek megmondja, mely fájlrendszer-helyek relevánsak
az aktuális kéréshez. Egy gyökér tartalmaz egy kötelező `file://` URI-t és egy opcionális
ember számára olvasható nevet.

A gyökerek információs javaslatok. Nem tartalmaznak beszélgetési előzményeket,
protokollmunkameneteket, vagy hozzáférés-ellenőrzési mechanizmust. A protokoll nem
írja elő, hogy a szerver kizárólag a listázott gyökerek között maradjon.

## Tanulási célok

A lecke végére képes leszel:

- Elmagyarázni, mit jelentenek az MCP gyökerek, és mit nem jelentenek.
- Felismerni a jelenlegi `roots/list` többkörös kommunikációs folyamatát.
- Biztonsági vezérlőket alkalmazni a gyökerektől függetlenül.
- Átállni az új megvalósítások esetében támogatott alternatívákra.

## Gyökéradatok

Egy kliens minden gyökeret egy `file://` URI-ként ad vissza, opcionális megjelenítési névvel:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

A klienseknek csak a felhasználó által jóváhagyott helyeket szabad feltüntetniük. A szervereknek az
eredményt iránymutatásként kell kezelniük a releváns fájlokról, nem jogosultsági bizonyítékként.

## MCP 2026-07-28 folyamat

Egy gyökereket támogató kliens minden kérésben bejelenti a képességet:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Egy klienskérés feldolgozása közben a szerver visszaadhat egy
`InputRequiredResult`-et, amely egy `roots/list` bemeneti kérést tartalmaz:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

A kliens összegyűjti a jóváhagyott gyökereket, és újrapróbálja az eredeti kérést a
megfelelő `inputResponses`-szel és változatlan `requestState`-tel. Ez a többkörös
mintázat állapotmentessé teszi a protokollt; nincs inicializációs kézfogás vagy
protokollszintű munkamenet.

## Régi, 2025-11-25 viselkedés

Az MCP `2025-11-25` verziójában a kliensek a gyökereket a inicializáció során hirdették. Egy szerver
közvetlen `roots/list` kérést indíthatott, és a kliens küldhetett
`notifications/roots/list_changed` értesítést, amikor a gyökerek megváltoztak.

Ez az életciklus régi viselkedésnek számít. Ne kombinálja az inicializációs vagy
értesítési példáit a `2026-07-28` implementációval.

## Ajánlott helyettesítők

### Eszközparaméterek

Tegye egyértelművé a szükséges könyvtárat vagy fájlt az eszköz sémájában:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### Erőforrás URI-k

Használja az MCP Erőforrásokat, amikor a szerver stabil URI-kon keresztül tudja elérhetővé tenni a releváns fájlokat.
Ez egyértelművé teszi a felfedezést és elérést.

### Szerverkonfiguráció

Fix telepítések esetén konfigurálja az engedélyezett könyvtárakat a szerver indításakor.
Ez gyakran tisztább, mint azokat eszközhívás közben felfedezni.

## Biztonsági követelmények

Bármit is választ helyettesítésként:

- Szerezze be a felhasználó beleegyezését a fájlrendszer-helyek feltüntetése előtt.
- Kanonizálja és ellenőrizze az elérési útvonalakat, hogy megakadályozza az átnavigálást.
- Külön kezelje a jogosultságot és a sandboxolást a gyökérértékektől függetlenül.
- Ellenőrizze újra a jogosultságokat, amikor egy fájlhoz hozzáférnek, ne csak amikor listázzák.
- Kerülje a érzékeny elérési utak visszaküldését naplókba vagy hibaüzenetekbe.

## Főbb tanulságok

- A gyökerek leírják a releváns fájlrendszer-helyeket; nem tárolnak beszélgetési
  állapotot.
- A gyökerek iránymutatások, nem hozzáférés-ellenőrzési határok.
- Az MCP `2026-07-28` minden kérésben továbbítja ezt a képességet, és
  `InputRequiredResult`-et használ a `roots/list` esetén.
- Az új megvalósításoknak inkább eszközparamétereket, erőforrás URI-kat vagy szerver-
  konfigurációt kell használniuk.

## További erőforrások

- [Gyökerek az MCP 2026-07-28 verziójában](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Elavult funkciók listája](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Mi változott az MCP-ben: A 2026-07-28 specifikáció](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
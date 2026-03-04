# Példa: Alap Host

Egy referencia-implementáció, amely megmutatja, hogyan lehet MCP host alkalmazást készíteni, amely MCP szerverekhez csatlakozik és eszköz UI-kat renderel biztonságos homokozóban.

Ez az alap host alkalmazás helyi fejlesztés alatt MCP alkalmazások tesztelésére is használható.

## Kulcsfontosságú fájlok

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host eszközválasztóval, paraméterbevitel és iframe kezeléssel
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Külső iframe proxy biztonsági ellenőrzések és kétirányú üzenetátvitel kezelésével
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Alapvető logika: szerver kapcsolat, eszköz hívás, és AppBridge beállítás

## Kezdés

```bash
npm install
npm run start
# Nyisd meg a http://localhost:8080 címet
```

Alapértelmezés szerint a host alkalmazás az `http://localhost:3001/mcp` címen próbál csatlakozni egy MCP szerverhez. Ezt a működést a `SERVERS` környezeti változó beállításával tudod konfigurálni, amely egy JSON tömböt vár a szerver URL-ekkel:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektúra

Ez a példa egy dupla-iframe homokozó mintát használ a biztonságos UI izoláció érdekében:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Miért két iframe?**

- A külső iframe külön eredeten fut (8081-es port), megakadályozva a közvetlen hozzáférést a hosthoz
- A belső iframe `srcdoc` segítségével kap HTML-t és a sandbox attribútumok korlátozzák
- Az üzenetek a külső iframe-en keresztül mennek, amely hitelesíti és kétirányúan továbbítja azokat

Ez az architektúra biztosítja, hogy még ha az eszköz UI kódja rosszindulatú is, nem férhet hozzá a host alkalmazás DOM-jához, cookie-khoz vagy JavaScript kontextushoz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár pontos fordításra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
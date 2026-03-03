# Příklad: Základní Hostitel

Referenční implementace ukazující, jak vytvořit MCP hostitelskou aplikaci, která se připojuje k MCP serverům a vykresluje uživatelská rozhraní nástrojů v bezpečném sandboxu.

Tento základní hostitel může být také použit k testování MCP aplikací během lokálního vývoje.

## Klíčové soubory

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI hostitel s výběrem nástrojů, zadáváním parametrů a správou iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Vnější iframe proxy s bezpečnostní validací a obousměrným přeposíláním zpráv
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Jádro logiky: připojení k serveru, volání nástrojů a nastavení AppBridge

## Začínáme

```bash
npm install
npm run start
# Otevřete http://localhost:8080
```

Ve výchozím nastavení se hostitelská aplikace pokusí připojit k MCP serveru na adrese `http://localhost:3001/mcp`. Toto chování můžete nakonfigurovat nastavením proměnné prostředí `SERVERS` s JSON polem URL serverů:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektura

Tento příklad používá vzor dvou iframe sandboxů pro bezpečnou izolaci uživatelského rozhraní:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Proč dva iframy?**

- Vnější iframe běží na samostatném původu (port 8081), což zabraňuje přímému přístupu k hostiteli
- Vnitřní iframe přijímá HTML přes `srcdoc` a je omezen atributy sandboxu
- Zprávy proudí přes vnější iframe, který je ověřuje a obousměrně přeposílá

Tato architektura zajišťuje, že i když je kód uživatelského rozhraní nástroje škodlivý, nemůže získat přístup k DOM hostitelské aplikace, cookie ani JavaScriptovému kontextu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro zásadní informace je doporučen profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady, které mohou vzniknout použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
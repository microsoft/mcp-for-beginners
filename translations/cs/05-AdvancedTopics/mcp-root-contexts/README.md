# MCP Roots (Legacy funkce)

> [!WARNING]
> Roots jsou zastaralé od MCP `2026-07-28`. V této revizi zůstávají pro
> kompatibilitu a mohou být odstraněny v první revizi specifikace
> vydané 28. července 2027 nebo později. Nové implementace by měly předávat
> adresáře nebo soubory pomocí parametrů nástroje, URI zdrojů nebo konfigurace serveru.


## Přehled

Roots umožňují MCP klientovi sdělit serveru, které umístění v souborovém systému jsou relevantní
pro aktuální požadavek. Root obsahuje povinné `file://` URI a volitelný
lidsky čitelný název.

Roots jsou informační nápovědy. Nejsou to kontejnery historie konverzace,
protokolové relace nebo mechanismus řízení přístupu. Protokol neukládá
, že by server musel zůstat uvnitř uvedených roots.

## Cíle učení

Na konci této lekce budete schopni:

- Vysvětlit, co reprezentují MCP Roots a co nereprezentují.
- Rozpoznat aktuální vícekrokový tok `roots/list`.
- Aplikovat bezpečnostní kontroly nezávisle na Root.
- Migrovat nové implementace na podporované alternativy.

## Data Root

Klient vrací každý root jako `file://` URI s volitelným zobrazovaným názvem:

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

Klienti by měli zpřístupnit pouze umístění schválená uživatelem. Servery by měly
považovat výsledek za vodítko o relevantních souborech, nikoli za důkaz autorizace.

## MCP Tok 2026-07-28

Klient, který podporuje Roots, deklaruje tuto schopnost v každém požadavku:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Při zpracování požadavku klienta může server vrátit
`InputRequiredResult` obsahující vstupní požadavek `roots/list`:

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

Klient shromáždí schválené roots a opakuje původní požadavek se
odpovídajícími `inputResponses` a beze změny `requestState`. Tento vícekrokový
vzor zachovává protokol bezstavový; neexistuje žádné přivítání `initialize` nebo
protokolová relace.

## Legacy chování 2025-11-25

V MCP `2025-11-25` klienti oznamovali Roots během inicializace. Server mohl
odeslat přímý požadavek `roots/list` a klient mohl odesílat
`notifications/roots/list_changed`, když se jeho roots změnily.

Tento životní cyklus je legacy chování. Neukládejte příklady inicializace ani
notifikace dohromady s implementací `2026-07-28`.

## Doporučené náhrady

### Parametry nástroje

Explicitně uveďte požadovaný adresář nebo soubor ve schématu nástroje:

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

### URI zdrojů

Použijte MCP Resources, pokud server může zpřístupnit relevantní soubory přes stabilní
URI. Toto udržuje objevování a získávání explicitní.

### Konfigurace serveru

Pro pevné nasazení nastavte povolené adresáře při startu serveru.
Často je to jasnější než je objevovat během volání nástroje.

## Bezpečnostní požadavky

Ať už zvolíte jakoukoli náhradu:

- Získejte souhlas uživatele před zpřístupněním umístění v souborovém systému.
- Kanonizujte a validujte cesty, aby se zabránilo průchodu mimo určené oblasti.
- Uplatňujte autorizaci a sandboxing nezávisle na hodnotách root.
- Překontrolujte oprávnění při přístupu k souboru, nejen při jeho výpisu.
- Vyvarujte se vracení citlivých cest v protokolech nebo chybových zprávách.

## Klíčové poznatky

- Roots popisují relevantní umístění v souborovém systému; neukládají stav konverzace.

- Roots jsou vodítko, ne hranice řízení přístupu.
- MCP `2026-07-28` přenáší schopnost na každý požadavek a používá
  `InputRequiredResult` pro `roots/list`.
- Nové implementace by měly místo toho používat parametry nástroje, URI zdrojů nebo konfiguraci serveru.


## Další zdroje

- [Roots v MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registr zastaralých funkcí](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Co se změnilo v MCP: Specifikace 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
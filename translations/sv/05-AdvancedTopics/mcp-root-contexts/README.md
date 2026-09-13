# MCP Roots (Legacy-funktion)

> [!WARNING]
> Roots är föråldrade från och med MCP `2026-07-28`. De finns kvar i denna revision för
> kompatibilitet och är berättigade till borttagning i den första specifikations-
> revisionen som släpps den 28 juli 2027 eller senare. Nya implementationer bör skicka
> kataloger eller filer via verktygsparametrar, resurs-URI:er eller server-
> konfiguration.

## Översikt

Roots låter en MCP-klient tala om för en server vilka filsystemplatser som är relevanta
för den aktuella förfrågan. En root innehåller en obligatorisk `file://` URI och ett valfritt
människoläsbart namn.

Roots är informationsledtrådar. De är inte samtalshistorik-behållare,
protokollsessions eller en åtkomstkontrollmekanism. Protokollet
kräver inte att en server håller sig inom de listade roots.

## Lärandemål

I slutet av denna lektion ska du kunna:

- Förklara vad MCP Roots representerar och vad de inte representerar.
- Känna igen det aktuella `roots/list` flödet med flera rundresor.
- Tillämpa säkerhetskontroller oberoende av Roots.
- Migrera nya implementationer till stödda alternativ.

## Root-data

En klient returnerar varje root som en `file://` URI med ett valfritt visningsnamn:

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

Klienter bör endast exponera platser godkända av användaren. Servrar bör betrakta
resultatet som vägledning om relevanta filer, inte som bevis på auktorisering.

## MCP 2026-07-28 Flöde

En klient som stödjer Roots anger kapaciteten i varje förfrågan:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Under hantering av en klientförfrågan kan en server returnera ett
`InputRequiredResult` som innehåller en `roots/list` inmatningsförfrågan:

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

Klienten samlar in de godkända roots och försöker igen med den ursprungliga förfrågan med de
matchande `inputResponses` och oförändrat `requestState`. Detta flöde med flera rundresor
håller protokollet statslöst; det finns ingen `initialize` handskakning eller
protokollnivåsession.

## Legacy-beteende 2025-11-25

I MCP `2025-11-25` annonserade klienter Roots under initialisering. En server
kunde utfärda en direkt `roots/list` förfrågan, och en klient kunde skicka
`notifications/roots/list_changed` när dess roots ändrades.

Den livscykeln är legacy-beteende. Kombinera inte dess initialisering eller
notifieringsexempel med en `2026-07-28` implementation.

## Rekommenderade ersättningar

### Verktygsparametrar

Gör den obligatoriska katalogen eller filen explicit i verktygsschemat:

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

### Resurs-URI:er

Använd MCP Resources när servern kan exponera relevanta filer via stabila
URI:er. Detta håller upptäckt och hämtning explicit.

### Serverkonfiguration

För fasta distributioner, konfigurera tillåtna kataloger när servern startar.
Detta är ofta tydligare än att upptäcka dem under ett verktygsanrop.

## Säkerhetskrav

Oavsett vilken ersättning du väljer:

- Skaffa användarens samtycke innan filsystemplatser exponeras.
- Kanonisera och validera sökvägar för att förhindra traversal.
- Verkställ auktorisering och sandboxing oberoende av root-värden.
- Kontrollera behörigheter igen när en fil nås, inte bara när den listas.
- Undvik att returnera känsliga sökvägar i loggar eller felmeddelanden.

## Viktiga slutsatser

- Roots beskriver relevanta filsystemplatser; de lagrar inte konversations-
  tillstånd.
- Roots är vägledning, inte en åtkomstkontrollgräns.
- MCP `2026-07-28` bär kapabiliteten per förfrågan och använder
  `InputRequiredResult` för `roots/list`.
- Nya implementationer bör använda verktygsparametrar, resurs-URI:er eller server-
  konfiguration istället.

## Ytterligare resurser

- [Roots i MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register över föråldrade funktioner](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Vad som ändrats i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
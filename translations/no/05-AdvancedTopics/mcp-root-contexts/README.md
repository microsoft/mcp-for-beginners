# MCP Roots (Eldre funksjon)

> [!WARNING]
> Roots er foreldet fra og med MCP `2026-07-28`. De forblir i denne revisjonen for
> kompatibilitet og kan fjernes i den første spesifikasjons-
> revisjonen som utgis 28. juli 2027 eller senere. Nye implementasjoner bør sende
> kataloger eller filer gjennom verktøyparametere, ressurs-URIer eller server-
> konfigurasjon.

## Oversikt

Roots lar en MCP-klient fortelle en server hvilke filsystemplasseringer som er relevante
for den nåværende forespørselen. En root inneholder en obligatorisk `file://` URI og et valgfritt
menneskelig-lesbart navn.

Roots er informasjonsindikatorer. De er ikke samtalehistorikk-beholdere,
protokollsamtaler eller en tilgangskontrollmekanisme. Protokollen håndhever ikke
at en server oppholder seg innenfor de oppførte rootene.

## Læringsmål

Mot slutten av denne leksjonen vil du kunne:

- Forklare hva MCP Roots representerer og hva de ikke representerer.
- Gjenkjenne den nåværende `roots/list` multi-rundetur flyten.
- Anvende sikkerhetskontroller uavhengig av Roots.
- Migrere nye implementasjoner til støttede alternativer.

## Root-data

En klient returnerer hver root som en `file://` URI med et valgfritt visningsnavn:

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

Klienter bør bare eksponere steder godkjent av brukeren. Servere bør behandle
resultatet som veiledning om relevante filer, ikke som bevis for autorisasjon.

## MCP 2026-07-28 flyt

En klient som støtter Roots erklærer denne kapasiteten i hver forespørsel:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Mens en server behandler en klientforespørsel, kan den returnere et
`InputRequiredResult` som inneholder en `roots/list` input-forespørsel:

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

Klienten samler de godkjente roots og prøver den opprinnelige forespørselen på nytt med de
samsvarende `inputResponses` og uendret `requestState`. Denne multi-rundetur
mønsteret holder protokollen stateless; det finnes ikke noe `initialize` håndtrykk eller
protokollnivå-sesjon.

## Eldre oppførsel fra 2025-11-25

I MCP `2025-11-25` annonserte klienter Roots under initialisering. En server
kunne sende en direkte `roots/list` forespørsel, og en klient kunne sende
`notifications/roots/list_changed` når dets roots endret seg.

Den livssyklusen er eldre oppførsel. Ikke kombiner initialiserings- eller
varslings-eksemplene med en `2026-07-28` implementering.

## Anbefalte erstatninger

### Verktøyparametere

Gjør den nødvendige katalogen eller filen eksplisitt i verktøyskjemaet:

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

### Ressurs-URIer

Bruk MCP Resources når serveren kan eksponere de relevante filene gjennom stabile
URIer. Dette gjør oppdagelse og henting eksplisitt.

### Serverkonfigurasjon

For faste distribusjoner, konfigurer tillatte kataloger når serveren starter.
Dette er ofte klarere enn å oppdage dem under et verktøyskall.

## Sikkerhetskrav

Uansett hvilken erstatning du velger:

- Skaff brukerens samtykke før du eksponerer filsystemlokasjoner.
- Kanoniser og valider stier for å hindre traversering.
- Håndhev autorisasjon og sandkasse uavhengig av root-verdier.
- Kontroller tillatelser på nytt når en fil åpnes, ikke bare ved oppføring.
- Unngå å returnere sensitive stier i logger eller feilmeldinger.

## Viktige poenger

- Roots beskriver relevante filsystemlokasjoner; de lagrer ikke samtale
  tilstand.
- Roots er veiledning, ikke en tilgangskontrollgrense.
- MCP `2026-07-28` bærer kapasiteten per forespørsel og bruker
  `InputRequiredResult` for `roots/list`.
- Nye implementasjoner bør bruke verktøyparametere, ressurs-URIer eller server-
  konfigurasjon i stedet.

## Ytterligere ressurser

- [Roots i MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register over foreldede funksjoner](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Hva som er endret i MCP: Spesifikasjonen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
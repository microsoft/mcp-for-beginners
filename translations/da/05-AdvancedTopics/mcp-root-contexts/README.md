# MCP Roots (Ældre Funktion)

> [!WARNING]
> Roots er forældede fra og med MCP `2026-07-28`. De forbliver i denne revision for
> kompatibilitet og kan fjernes i den første specifikationsrevision,
> der udgives den 28. juli 2027 eller senere. Nye implementeringer bør videresende
> mapper eller filer gennem værktøjsparametre, resource-URI'er eller server-
> konfiguration.

## Oversigt

Roots lader en MCP-klient fortælle en server, hvilke filsystemplaceringer der er relevante
for den aktuelle anmodning. En root indeholder en påkrævet `file://` URI og et valgfrit
menneskeligt læsbart navn.

Roots er informationshint. De er ikke samtale-historik-beholdere,
protokol-sessioner eller en adgangskontrolmekanisme. Protokollen håndhæver ikke,
at en server forbliver inden for de listede roots.

## Læringsmål

Når du er færdig med dette modul, vil du kunne:

- Forklare hvad MCP Roots repræsenterer og hvad de ikke repræsenterer.
- Genkende den aktuelle `roots/list` multi-round-trip flow.
- Anvende sikkerhedskontroller uafhængigt af Roots.
- Migrere nye implementeringer til understøttede alternativer.

## Root Data

En klient returnerer hver root som en `file://` URI med et valgfrit visningsnavn:

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

Klienter bør kun eksponere placeringer godkendt af brugeren. Servere bør betragte
resultatet som vejledning om relevante filer, ikke som bevis på autorisation.

## MCP 2026-07-28 Flow

En klient, der understøtter Roots, erklærer kapabiliteten i hver anmodning:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Under behandling af en klientanmodning kan en server returnere et
`InputRequiredResult` som indeholder en `roots/list` input-anmodning:

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

Klienten samler de godkendte roots og forsøgte den oprindelige anmodning igen med de
matchende `inputResponses` og uændret `requestState`. Dette multi-round-trip
mønster holder protokollen stateless; der er ikke noget `initialize` håndtryk eller
protokolniveau-session.

## Ældre Adfærd fra 2025-11-25

I MCP `2025-11-25` annoncerede klienter Roots under initialisering. En server
kunne udsende en direkte `roots/list` anmodning, og en klient kunne sende
`notifications/roots/list_changed`, når dens roots ændredes.

Den livscyklus er ældre adfærd. Kombiner ikke dets initialiserings- eller
notifikations-eksempler med en `2026-07-28` implementering.

## Anbefalede Erstatninger

### Værktøjsparametre

Gør den påkrævede mappe eller fil eksplicit i værktøjsschemaet:

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

### Resource URI'er

Brug MCP Ressourcer, når serveren kan eksponere de relevante filer gennem stabile
URI'er. Dette holder opdagelse og hentning eksplicit.

### Serverkonfiguration

For faste implementeringer, konfigurer tilladte mapper ved serverstart.
Dette er ofte klarere end at opdage dem under et værktøjsopkald.

## Sikkerhedskrav

Uanset hvilken erstatning du vælger:

- Opnå brugerens samtykke før eksponering af filsystemplaceringer.
- Kanoniser og valider stier for at forhindre traversal.
- Håndhæv autorisation og sandboxing uafhængigt af root-værdier.
- Genkontroller tilladelser, når en fil tilgås, ikke kun når den listes.
- Undgå at returnere følsomme stier i logs eller fejlmeddelelser.

## Vigtige Pointer

- Roots beskriver relevante filsystemplaceringer; de gemmer ikke samtalestatus.

- Roots er vejledning, ikke en adgangskontrolgrænse.
- MCP `2026-07-28` angiver kapabiliteten per anmodning og bruger
  `InputRequiredResult` for `roots/list`.
- Nye implementeringer bør anvende værktøjsparametre, resource-URI'er eller server-
  konfiguration i stedet.

## Yderligere Ressourcer

- [Roots i MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register over forældede funktioner](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Hvad er ændret i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
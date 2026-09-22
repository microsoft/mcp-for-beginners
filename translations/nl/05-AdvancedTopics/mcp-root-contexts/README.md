# MCP Roots (Verouderde functie)

> [!WARNING]
> Roots zijn vervallen sinds MCP `2026-07-28`. Ze blijven in deze revisie voor
> compatibiliteit en kunnen worden verwijderd in de eerste specificatierevisie
> die wordt uitgebracht op of na 28 juli 2027. Nieuwe implementaties moeten
> mappen of bestanden doorgeven via toolparameters, resource-URI's, of server-
> configuratie.

## Overzicht

Roots laten een MCP-client aan een server vertellen welke bestandslocaties relevant zijn
voor het huidige verzoek. Een root bevat een verplichte `file://` URI en een optionele
mensleesbare naam.

Roots zijn informatieve aanwijzingen. Ze zijn geen containers voor conversatiegeschiedenis,
protocol-sessies, of een toegangscontrolemechanisme. Het protocol dwingt niet af
dat een server binnen de genoemde roots blijft.

## Leerdoelen

Aan het einde van deze les kun je:

- Uitleggen wat MCP Roots vertegenwoordigen en wat ze niet vertegenwoordigen.
- Herkennen van de huidige `roots/list` multi-round-trip flow.
- Onafhankelijk van Roots beveiligingscontroles toepassen.
- Nieuwe implementaties migreren naar ondersteunde alternatieven.

## Rootgegevens

Een client retourneert elke root als een `file://` URI met een optionele weergavenaam:

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

Clients mogen alleen locaties blootstellen die door de gebruiker zijn goedgekeurd. Servers moeten
het resultaat zien als richtlijn voor relevante bestanden, niet als bewijs van autorisatie.

## MCP 2026-07-28 Flow

Een client die Roots ondersteunt, declareert deze mogelijkheid in elk verzoek:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Tijdens het verwerken van een clientverzoek kan een server een
`InputRequiredResult` retourneren met een `roots/list` invoerverzoek:

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

De client verzamelt de goedgekeurde roots en probeert het oorspronkelijke verzoek opnieuw met
overeenkomende `inputResponses` en ongewijzigde `requestState`. Dit multi-round-trip
patroon houdt het protocol stateless; er is geen `initialize` handshake of
protocolniveau-sessie.

## Legacy gedrag 2025-11-25

In MCP `2025-11-25` adverteerden clients Roots tijdens initialisatie. Een server
kon direct een `roots/list` verzoek doen en een client kon
`notifications/roots/list_changed` verzenden wanneer de roots veranderden.

Die levenscyclus is legacy gedrag. Combineer de initialisatie- of
notificatievoorbeelden niet met een `2026-07-28` implementatie.

## Aanbevolen vervangingen

### Toolparameters

Maak de vereiste map of het bestand expliciet in het toolschema:

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

### Resource-URI's

Gebruik MCP Resources wanneer de server de relevante bestanden kan blootstellen via stabiele
URI's. Dit maakt ontdekking en ophalen expliciet.

### Serverconfiguratie

Configureer voor vaste implementaties toegestane mappen bij het opstarten van de server.
Dit is vaak duidelijker dan ze ontdekken tijdens een toolaanroep.

## Beveiligingseisen

Welke vervanging je ook kiest:

- Verkrijg toestemming van de gebruiker voordat bestandslocaties worden blootgesteld.
- Canonicaliseer en valideer paden om traversals te voorkomen.
- Dwing autorisatie en sandboxing af, los van rootwaarden.
- Controleer permissies opnieuw wanneer een bestand wordt benaderd, niet alleen wanneer het wordt vermeld.
- Vermijd het teruggeven van gevoelige paden in logs of foutmeldingen.

## Belangrijkste punten

- Roots beschrijven relevante bestandslocaties; ze slaan geen conversatiestatus op.

- Roots zijn richtlijnen, geen toegangscontroledrempel.
- MCP `2026-07-28` draagt de mogelijkheid per verzoek en gebruikt
  `InputRequiredResult` voor `roots/list`.
- Nieuwe implementaties moeten in plaats daarvan toolparameters, resource-URI's of server-
  configuratie gebruiken.

## Aanvullende bronnen

- [Roots in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register met verouderde functies](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Wat is veranderd in MCP: De 2026-07-28 specificatie](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
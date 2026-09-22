# Distribuere MCP-servere

> [!NOTE]
> Konfigurasjonseksempler som bruker en `/sse` endepunkt retter seg mot det gamle HTTP+SSE
> transportlaget. MCP `2026-07-28` eksterne servere bruker Streamable HTTP, normalt på et
> serverdefinert endepunkt som `/mcp`.

Å distribuere MCP-serveren din gjør det mulig for andre å få tilgang til verktøy og ressurser utover ditt lokale miljø. Det finnes flere distribusjonsstrategier å vurdere, avhengig av dine krav til skalerbarhet, pålitelighet og enkel administrasjon. Nedenfor finner du veiledning for å distribuere MCP-servere lokalt, i containere og til skyen.

## Oversikt

Denne leksjonen dekker hvordan du distribuerer appen din MCP Server.

## Læringsmål

Etter denne leksjonen vil du kunne:

- Vurdere ulike distribusjonstilnærminger.
- Distribuere appen din.

## Lokal utvikling og distribusjon

Hvis serveren din skal brukes ved å kjøre den på brukerens maskin, kan du følge følgende trinn:

1. **Last ned serveren**. Hvis du ikke har skrevet serveren, last den ned først til maskinen din.
1. **Start serverprosessen**: Kjør MCP-serverapplikasjonen din

For SSE (ikke nødvendig for stdio-type server)

1. **Konfigurer nettverk**: Sørg for at serveren er tilgjengelig på forventet port
1. **Koble til klienter**: Bruk lokale tilkoblings-URLer som `http://localhost:3000`

## Distribusjon til skyen

MCP-servere kan distribueres på flere skyplattformer:

- **Serverløse funksjoner**: Distribuer lette MCP-servere som serverløse funksjoner
- **Container-tjenester**: Bruk tjenester som Azure Container Apps, AWS ECS eller Google Cloud Run
- **Kubernetes**: Distribuer og administrer MCP-servere i Kubernetes-klynger for høy tilgjengelighet

### Eksempel: Azure Container Apps

Azure Container Apps støtter distribusjon av MCP-servere. Det er fortsatt under utvikling og støtter for øyeblikket SSE-servere.

Slik kan du gå fram:

1. Klon et repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kjør det lokalt for å teste:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. For å prøve det lokalt, lag en *mcp.json*-fil i en *.vscode*-mappe og legg til følgende innhold:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

Når SSE-serveren er startet, kan du klikke på avspillingsikonet i JSON-filen, du skal nå se verktøy på serveren bli plukket opp av GitHub Copilot, se Verktøy-ikonet.

1. For å distribuere, kjør følgende kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Dermed har du det, distribuer det lokalt, distribuer det til Azure via disse trinnene.

## Ytterligere ressurser

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps-artikkel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Hva er neste

- Neste: [Avanserte servertemaer](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
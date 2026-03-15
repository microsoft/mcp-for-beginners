# Distribuering av MCP-servere

Distribuering av MCP-serveren din gjør det mulig for andre å få tilgang til verktøyene og ressursene dens utover ditt lokale miljø. Det finnes flere distribueringsstrategier å vurdere, avhengig av dine krav til skalerbarhet, pålitelighet og håndteringsvennlighet. Nedenfor finner du veiledning for distribusjon av MCP-servere lokalt, i containere og til skyen.

## Oversikt

Denne leksjonen dekker hvordan du distribuerer MCP Server-appen din.

## Læringsmål

Etter denne leksjonen vil du kunne:

- Vurdere ulike distribusjonsmetoder.
- Distribuere appen din.

## Lokal utvikling og distribusjon

Hvis serveren din er ment å brukes ved å kjøre den på brukerens maskin, kan du følge disse trinnene:

1. **Last ned serveren**. Hvis du ikke skrev serveren, last den først ned til maskinen din.
1. **Start serverprosessen**: Kjør MCP-serverapplikasjonen din

For SSE (ikke nødvendig for stdio-type server)

1. **Konfigurer nettverk**: Sørg for at serveren er tilgjengelig på forventet port
1. **Koble til klienter**: Bruk lokale tilkoblings-URLer som `http://localhost:3000`

## Distribuering til skyen

MCP-servere kan distribueres til ulike skyplattformer:

- **Serverløse funksjoner**: Distribuer lette MCP-servere som serverløse funksjoner
- **Container-tjenester**: Bruk tjenester som Azure Container Apps, AWS ECS eller Google Cloud Run
- **Kubernetes**: Distribuer og administrer MCP-servere i Kubernetes-klynger for høy tilgjengelighet

### Eksempel: Azure Container Apps

Azure Container Apps støtter distribusjon av MCP-servere. Det er fortsatt et pågående arbeid og støtter foreløpig SSE-servere.

Slik kan du gjøre det:

1. Klon et repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Kjør det lokalt for å teste ting:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. For å prøve det lokalt, opprett en *mcp.json*-fil i en *.vscode*-mappe og legg til følgende innhold:

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

  Når SSE-serveren er startet, kan du klikke på avspillingsikonet i JSON-filen, du bør nå se verktøy på serveren som blir plukket opp av GitHub Copilot, se verktøyikonet.

1. For å distribuere, kjør følgende kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Der har du det, distribuer det lokalt, distribuer det til Azure gjennom disse stegene.

## Ytterligere ressurser

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Artikkel om Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Hva er neste

- Neste: [Avanserte serveremner](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Distribuere MCP-servere

Å distribuere MCP-serveren din gjør det mulig for andre å få tilgang til verktøyene og ressursene utenfor ditt lokale miljø. Det finnes flere distribusjonsstrategier å vurdere, avhengig av dine krav til skalerbarhet, pålitelighet og enkel administrasjon. Nedenfor finner du veiledning for å distribuere MCP-servere lokalt, i containere og i skyen.

## Oversikt

Denne leksjonen dekker hvordan du distribuerer MCP Server-appen din.

## Læringsmål

Når du er ferdig med denne leksjonen, vil du kunne:

- Vurdere ulike distribusjonsmetoder.
- Distribuere appen din.

## Lokal utvikling og distribusjon

Hvis serveren din er ment å brukes ved å kjøre den på brukerens maskin, kan du følge disse stegene:

1. **Last ned serveren**. Hvis du ikke har skrevet serveren selv, last den ned til maskinen din først.  
1. **Start serverprosessen**: Kjør MCP-serverapplikasjonen din.

For SSE (ikke nødvendig for stdio-type server)

1. **Konfigurer nettverk**: Sørg for at serveren er tilgjengelig på forventet port.  
1. **Koble til klienter**: Bruk lokale tilkoblings-URLer som `http://localhost:3000`.

## Distribusjon i skyen

MCP-servere kan distribueres til ulike skyplattformer:

- **Serverless Functions**: Distribuer lette MCP-servere som serverløse funksjoner.  
- **Container-tjenester**: Bruk tjenester som Azure Container Apps, AWS ECS eller Google Cloud Run.  
- **Kubernetes**: Distribuer og administrer MCP-servere i Kubernetes-klynger for høy tilgjengelighet.

### Eksempel: Azure Container Apps

Azure Container Apps støtter distribusjon av MCP-servere. Dette er fortsatt under utvikling, og støtter for øyeblikket SSE-servere.

Slik kan du gå frem:

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

  Når SSE-serveren er startet, kan du klikke på avspillingsikonet i JSON-filen. Du skal nå se at verktøyene på serveren blir plukket opp av GitHub Copilot, se verktøyikonet.

1. For å distribuere, kjør følgende kommando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Der har du det, distribuer det lokalt eller til Azure ved å følge disse stegene.

## Ekstra ressurser

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps artikkel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Hva nå

- Neste: [Praktisk implementering](../../04-PracticalImplementation/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
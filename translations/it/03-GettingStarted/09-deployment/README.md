# Distribuire i server MCP

Distribuire il tuo server MCP consente ad altri di accedere ai suoi strumenti e risorse al di fuori del tuo ambiente locale. Ci sono diverse strategie di distribuzione da considerare, a seconda delle tue esigenze di scalabilità, affidabilità e facilità di gestione. Di seguito troverai indicazioni per distribuire i server MCP localmente, in container e sul cloud.

## Panoramica

Questa lezione spiega come distribuire la tua app MCP Server.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Valutare diversi approcci di distribuzione.
- Distribuire la tua app.

## Sviluppo e distribuzione locale

Se il tuo server è pensato per essere utilizzato eseguendolo sulla macchina degli utenti, puoi seguire i seguenti passaggi:

1. **Scarica il server**. Se non hai scritto il server, scaricalo prima sulla tua macchina. 
1. **Avvia il processo del server**: Esegui la tua applicazione MCP server 

Per SSE (non necessario per server di tipo stdio)

1. **Configura la rete**: Assicurati che il server sia accessibile sulla porta prevista 
1. **Connetti i client**: Usa URL di connessione locale come `http://localhost:3000`

## Distribuzione sul cloud

I server MCP possono essere distribuiti su varie piattaforme cloud:

- **Funzioni Serverless**: Distribuisci server MCP leggeri come funzioni serverless
- **Servizi Container**: Usa servizi come Azure Container Apps, AWS ECS o Google Cloud Run
- **Kubernetes**: Distribuisci e gestisci i server MCP in cluster Kubernetes per alta disponibilità

### Esempio: Azure Container Apps

Azure Container Apps supporta la distribuzione di server MCP. È ancora un lavoro in corso e attualmente supporta server SSE.

Ecco come puoi procedere:

1. Clona un repository:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Eseguilo localmente per testare:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Per provarlo localmente, crea un file *mcp.json* in una directory *.vscode* e aggiungi il seguente contenuto:

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

  Una volta avviato il server SSE, puoi cliccare sull'icona play nel file JSON; ora dovresti vedere che gli strumenti sul server vengono riconosciuti da GitHub Copilot, vedi l'icona Tool. 

1. Per distribuire, esegui il seguente comando:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ecco fatto, distribuiscilo localmente, distribuiscilo su Azure seguendo questi passaggi.

## Risorse aggiuntive

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Articolo su Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repository Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Cosa c'è dopo

- Successivo: [Argomenti avanzati sul server](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
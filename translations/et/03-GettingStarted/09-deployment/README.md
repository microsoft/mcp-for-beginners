# MCP serverite juurutamine

MCP serveri juurutamine võimaldab teistel juurdepääsu saada selle tööriistadele ja ressurssidele väljaspool teie kohalikku keskkonda. Juurutamise strateegiaid on mitmeid, sõltuvalt skaleeritavuse, töökindluse ja haldamise lihtsuse nõuetest. Allpool leiate juhiseid MCP serverite juurutamiseks kohapeal, konteinerites ja pilve.

## Ülevaade

See õppetund käsitleb, kuidas MCP Serveri rakendust juurutada.

## Õpieesmärgid

Selle õppetunni lõpuks oskate:

- Hinnata erinevaid juurutusmeetodeid.
- Juurutada oma rakendust.

## Kohalik arendus ja juurutamine

Kui teie server on mõeldud kasutamiseks otse kasutaja masinas, saate järgida järgmisi samme:

1. **Laadige server alla**. Kui te serverit ei kirjutanud, laadige see esmalt oma masinasse alla.  
1. **Käivitage serveriprotsess**: Käivitage oma MCP serveri rakendus 

SSE jaoks (ei ole vajalik stdio tüüpi serveri puhul)

1. **Konfigureerige võrk**: Tagage, et server on juurdepääsetav oodatud pordil  
1. **Ühendage kliendid**: Kasutage kohalikke ühenduse URL-e nagu `http://localhost:3000`

## Pilve juurutamine

MCP servereid saab juurutada mitmetesse pilveplatvormidesse:

- **Serverivabad funktsioonid**: Juurutage kergekaalulisi MCP servereid serverivabade funktsioonidena  
- **Konteineriteenused**: Kasutage teenuseid nagu Azure Container Apps, AWS ECS või Google Cloud Run  
- **Kubernetes**: Juurutage ja haldage MCP servereid Kubernetes klastrites kõrge kättesaadavuse tagamiseks

### Näide: Azure Container Apps

Azure Container Apps toetab MCP Serverite juurutamist. See on veel pooleli ja toetab hetkel SSE servereid.

Siin on, kuidas seda teha:

1. Klooni reposti:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Käivitage see kohapeal, et asja proovida:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Kohapeal proovimiseks looge kataloogi *.vscode* fail *mcp.json* ja lisage sinna järgmine sisu:

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

  Kui SSE server on käivitatud, võite JSON-failis vajutada esitusikooni, nüüd peaks GitHub Copilot tuvastama serveri tööriistad, vaadake tööriista ikooni.

1. Juurutamiseks käivitage järgmine käsk:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```
  
Nii see ongi, juurutage see kohapeal, juurutage see Azure'i sellisel viisil.

## Täiendavad ressursid

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps artikkel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Mis järgmisena

- Järgmine: [Täpsemad serveri teemad](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud AI tõlke teenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun pidage meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
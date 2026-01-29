# MCP Serverite juurutamine

MCP serveri juurutamine võimaldab teistel pääseda ligi selle tööriistadele ja ressurssidele väljaspool teie kohalikku keskkonda. Sõltuvalt teie vajadustest skaleeritavuse, töökindluse ja haldamise lihtsuse osas on mitmeid juurutusstrateegiaid, mida kaaluda. Allpool leiate juhised MCP serverite juurutamiseks kohapeal, konteinerites ja pilves.

## Ülevaade

See õppetund käsitleb, kuidas juurutada oma MCP Serveri rakendust.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- Hinnata erinevaid juurutusmeetodeid.
- Juurutada oma rakenduse.

## Kohalik arendus ja juurutamine

Kui teie server on mõeldud kasutamiseks kasutaja arvutis, saate järgida järgmisi samme:

1. **Laadige server alla**. Kui te ei loonud serverit ise, laadige see esmalt oma arvutisse.
1. **Käivitage serveriprotsess**: Käivitage oma MCP serveri rakendus.

SSE jaoks (ei ole vajalik stdio tüüpi serveri puhul)

1. **Võrgu seadistamine**: Veenduge, et server oleks juurdepääsetav oodatud pordi kaudu.
1. **Ühendage kliendid**: Kasutage kohalikke ühenduse URL-e, näiteks `http://localhost:3000`.

## Pilve juurutamine

MCP servereid saab juurutada erinevatele pilveplatvormidele:

- **Serverivabad funktsioonid**: Juurutage kergeid MCP servereid serverivabade funktsioonidena.
- **Konteineriteenused**: Kasutage teenuseid nagu Azure Container Apps, AWS ECS või Google Cloud Run.
- **Kubernetes**: Juurutage ja hallake MCP servereid Kubernetes'i klastrites, et tagada kõrge kättesaadavus.

### Näide: Azure Container Apps

Azure Container Apps toetab MCP serverite juurutamist. See on veel arendamisel ja praegu toetab SSE servereid.

Siin on, kuidas seda teha:

1. Kloonige repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Käivitage see kohapeal, et asju testida:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Kohapeal proovimiseks looge *mcp.json* fail kaustas *.vscode* ja lisage järgmine sisu:

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

  Kui SSE server on käivitatud, saate klõpsata JSON-failis esitusikoonil. Nüüd peaksite nägema, et serveri tööriistad on GitHub Copiloti poolt tuvastatud, vaadake Tööriista ikooni.

1. Juurutamiseks käivitage järgmine käsk:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ja ongi kõik, juurutage see kohapeal, juurutage see Azure'i nende sammude abil.

## Lisamaterjalid

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps artikkel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Mis edasi?

- Järgmine: [Praktiline rakendamine](../../04-PracticalImplementation/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
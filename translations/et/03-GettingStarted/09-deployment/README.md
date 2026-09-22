# MCP serverite juurutamine

> [!NOTE]
> Konfiguratsiooninäited, mis kasutavad lõpp-punkti `/sse`, sihivad pärand HTTP+SSE
> transporti. MCP `2026-07-28` kaugserverid kasutavad tavaliselt serveri määratud
> lõpp-punkti nagu `/mcp` streamitavat HTTP-d.

MCP serveri juurutamine võimaldab teistel ligipääsu selle tööriistadele ja ressurssidele väljaspool teie kohalikku keskkonda. Võimalike juurutamisstrateegiate valik sõltub teie skaleeritavuse, töökindluse ja haldusmugavuse nõuetest. Allpool leiate juhiseid MCP serverite juurutamiseks kohapeal, konteinerites ja pilves.

## Ülevaade

See õppetund käsitleb, kuidas juurutada oma MCP serverirakendus.

## Õpieesmärgid

Selle õppetunni lõpuks oskate:

- Hinnata erinevaid juurutamisviise.
- Oma rakendust juurutada.

## Kohalik arendus ja juurutamine

Kui teie server on mõeldud kasutamiseks otse kasutaja arvutis, saate järgida järgmisi samme:

1. **Laadige server alla**. Kui te ei kirjutanud serverit ise, siis laadige see esmalt oma masinasse alla.
1. **Käivitage serveri protsess**: Käivitage oma MCP serverirakendus

SSE jaoks (ei ole vajalik stdio tüüpi serveri puhul)

1. **Konfigureerige võrgustik**: Veenduge, et server oleks ligipääsetav oodatud pordil
1. **Ühendage kliendid**: Kasutage kohalikke ühenduse URL-e nagu `http://localhost:3000`

## Pilvejuurutus

MCP serverid saab juurutada mitmetesse pilveplatvormidesse:

- **Serverita funktsioonid**: Juurutage kergekaalulised MCP serverid serverita funktsioonidena
- **Konteineriteenused**: Kasutage teenuseid nagu Azure Container Apps, AWS ECS või Google Cloud Run
- **Kubernetes**: Juurutage ja haldage MCP servereid Kubernetes klastrites kõrge kättesaadavuse tagamiseks

### Näide: Azure Container Apps

Azure Container Apps toetab MCP serverite juurutamist. See on endiselt arengujärgus ning toetab praegu SSE servereid.

Siin on, kuidas saate seda teha:

1. Kloneerige repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Käivitage see kohapeal, et proovida asju:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Kohaliku proovimise jaoks looge *mcp.json* fail kataloogi *.vscode* ja lisage järgmine sisu:

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

  Kui SSE server on käivitatud, saate JSON faili mängimisikooni klõpsata, peaks nüüd nägema, et tööriistad serveris võetakse GitHub Copiloti poolt kasutusele – vaadake tööriista ikooni. 

1. Juurutamiseks käivitage järgmine käsk:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Siin see on, juurutage kohalikult, juurutage Azure’i kaudu nende sammude abil.

## Täiendavad ressursid

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps artikkel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Mis järgmiseks

- Järgmine: [Täpsemad serveriteemad](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
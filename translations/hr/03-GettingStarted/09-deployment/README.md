# Implementacija MCP servera

Implementacija vašeg MCP servera omogućuje drugima pristup njegovim alatima i resursima izvan vašeg lokalnog okruženja. Postoji nekoliko strategija implementacije koje treba razmotriti, ovisno o vašim zahtjevima za skalabilnost, pouzdanost i jednostavnost upravljanja. Ispod ćete pronaći upute za implementaciju MCP servera lokalno, u kontejnerima i u oblaku.

## Pregled

Ova lekcija pokriva kako implementirati vašu MCP Server aplikaciju.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Procijeniti različite pristupe implementaciji.
- Implementirati svoju aplikaciju.

## Lokalni razvoj i implementacija

Ako je vaš server namijenjen za korištenje na korisničkom računalu, možete slijediti sljedeće korake:

1. **Preuzmite server**. Ako niste napisali server, prvo ga preuzmite na svoje računalo. 
1. **Pokrenite proces servera**: Pokrenite svoju MCP server aplikaciju 

Za SSE (nije potrebno za stdio tip servera)

1. **Konfigurirajte mrežu**: Osigurajte da je server dostupan na očekivanom portu 
1. **Povežite klijente**: Koristite lokalne URL-ove za povezivanje poput `http://localhost:3000`

## Implementacija u oblaku

MCP serveri mogu se implementirati na razne cloud platforme:

- **Serverless funkcije**: Implementirajte lagane MCP servere kao serverless funkcije
- **Usluge kontejnera**: Koristite usluge poput Azure Container Apps, AWS ECS ili Google Cloud Run
- **Kubernetes**: Implementirajte i upravljajte MCP serverima u Kubernetes klasterima za visoku dostupnost

### Primjer: Azure Container Apps

Azure Container Apps podržava implementaciju MCP servera. Još je u tijeku razvoj i trenutno podržava SSE servere.

Evo kako to možete napraviti:

1. Klonirajte repozitorij:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Pokrenite lokalno za testiranje:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Za lokalno isprobavanje, kreirajte *mcp.json* datoteku u direktoriju *.vscode* i dodajte sljedeći sadržaj:

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

  Kada se SSE server pokrene, možete kliknuti na ikonu za reprodukciju u JSON datoteci, sada biste trebali vidjeti da GitHub Copilot prepoznaje alate na serveru, vidite ikonu alata.

1. Za implementaciju, pokrenite sljedeću naredbu:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Eto, implementirajte lokalno, implementirajte u Azure slijedeći ove korake.

## Dodatni resursi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Članak o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorij](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Što slijedi

- Sljedeće: [Napredne teme servera](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nerazumijevanja ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
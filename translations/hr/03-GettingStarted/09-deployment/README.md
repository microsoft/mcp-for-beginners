# Postavljanje MCP poslužitelja

Postavljanje vašeg MCP poslužitelja omogućuje drugima pristup njegovim alatima i resursima izvan vaše lokalne okoline. Postoji nekoliko strategija postavljanja koje treba razmotriti, ovisno o vašim zahtjevima za skalabilnošću, pouzdanošću i jednostavnošću upravljanja. U nastavku ćete pronaći upute za postavljanje MCP poslužitelja lokalno, u kontejnerima i u oblaku.

## Pregled

Ova lekcija objašnjava kako postaviti vašu MCP Server aplikaciju.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Procijeniti različite pristupe postavljanju.
- Postaviti svoju aplikaciju.

## Lokalni razvoj i postavljanje

Ako je vaš poslužitelj namijenjen za korištenje na korisničkom računalu, možete slijediti sljedeće korake:

1. **Preuzmite poslužitelj**. Ako niste vi napisali poslužitelj, prvo ga preuzmite na svoje računalo.  
1. **Pokrenite poslužiteljski proces**: Pokrenite vašu MCP server aplikaciju

Za SSE (nije potrebno za stdio tip poslužitelja)

1. **Konfigurirajte mrežu**: Provjerite je li poslužitelj dostupan na očekivanom portu  
1. **Povežite klijente**: Koristite lokalne URL-ove poput `http://localhost:3000`

## Postavljanje u oblaku

MCP poslužitelji mogu se postaviti na različite cloud platforme:

- **Serverless funkcije**: Postavite lagane MCP poslužitelje kao serverless funkcije  
- **Usluge kontejnera**: Koristite usluge poput Azure Container Apps, AWS ECS ili Google Cloud Run  
- **Kubernetes**: Postavite i upravljajte MCP poslužiteljima u Kubernetes klasterima za visoku dostupnost

### Primjer: Azure Container Apps

Azure Container Apps podržava postavljanje MCP poslužitelja. Još je u fazi razvoja i trenutno podržava SSE poslužitelje.

Evo kako to možete napraviti:

1. Klonirajte repozitorij:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Pokrenite ga lokalno za testiranje:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Za lokalno testiranje, kreirajte *mcp.json* datoteku u *.vscode* direktoriju i dodajte sljedeći sadržaj:

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

  Nakon što se SSE poslužitelj pokrene, možete kliknuti na ikonu za pokretanje u JSON datoteci, sada biste trebali vidjeti da GitHub Copilot prepoznaje alate na poslužitelju, pogledajte ikonu alata.

1. Za postavljanje, pokrenite sljedeću naredbu:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Eto, postavite ga lokalno ili na Azure slijedeći ove korake.

## Dodatni resursi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Članak o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorij](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Što slijedi

- Sljedeće: [Praktična implementacija](../../04-PracticalImplementation/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
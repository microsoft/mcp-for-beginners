# Postavljanje MCP poslužitelja

> [!NOTE]
> Primjeri konfiguracija koji koriste `/sse` krajnu točku ciljaju na naslijeđeni HTTP+SSE
> transport. MCP `2026-07-28` udaljeni poslužitelji koriste Streamable HTTP, obično na
> poslužitelju definiranoj krajnjoj točki poput `/mcp`.

Postavljanje vašeg MCP poslužitelja omogućuje drugima pristup njegovim alatima i resursima izvan vaše lokalne okoline. Postoji nekoliko strategija postavljanja koje treba razmotriti, ovisno o vašim zahtjevima za skalabilnost, pouzdanost i jednostavnost upravljanja. U nastavku ćete pronaći smjernice za postavljanje MCP poslužitelja lokalno, u kontejnerima i u oblaku.

## Pregled

Ova lekcija obuhvaća kako postaviti vašu MCP Server aplikaciju.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Procijeniti različite pristupe postavljanju.
- Postaviti vašu aplikaciju.

## Lokalni razvoj i postavljanje

Ako je vaš poslužitelj namijenjen za korištenje na korisničkom računalu, možete slijediti sljedeće korake:

1. **Preuzmite poslužitelj**. Ako niste vi napisali poslužitelj, prvo ga preuzmite na svoje računalo.
1. **Pokrenite poslužiteljski proces**: Pokrenite vašu MCP server aplikaciju

Za SSE (nije potrebno za stdio tip poslužitelja)

1. **Konfigurirajte mrežu**: Osigurajte da je poslužitelj dostupan na očekivanom portu
1. **Povežite klijente**: Koristite lokalne veze poput `http://localhost:3000`

## Postavljanje u oblaku

MCP poslužitelji mogu se postaviti na raznim platformama u oblaku:

- **Bez poslužitelja (Serverless) funkcije**: Postavite lagane MCP poslužitelje kao bezposlužiteljske funkcije
- **Usluge kontejnera**: Koristite usluge poput Azure Container Apps, AWS ECS ili Google Cloud Run
- **Kubernetes**: Postavite i upravljajte MCP poslužiteljima u Kubernetes klasterima za visoku dostupnost

### Primjer: Azure Container Apps

Azure Container Apps podržava postavljanje MCP poslužitelja. Još je u razvoju i trenutno podržava SSE poslužitelje.

Evo kako to možete učiniti:

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

1. Za lokalno testiranje, stvorite datoteku *mcp.json* u direktoriju *.vscode* i dodajte sljedeći sadržaj:

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

  Nakon što se SSE poslužitelj pokrene, možete kliknuti ikonu za pokretanje u JSON datoteci, sada biste trebali vidjeti alate na poslužitelju koje prepoznaje GitHub Copilot, pogledajte ikonu alata.

1. Za postavljanje, pokrenite sljedeću naredbu:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Eto, postavite ga lokalno, postavite ga u Azure slijedeći ove korake.

## Dodatni resursi

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Članak o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorij](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Što slijedi

- Sljedeće: [Napredne teme o poslužiteljima](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
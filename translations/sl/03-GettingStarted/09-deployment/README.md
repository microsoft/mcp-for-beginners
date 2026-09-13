# Namestitev MCP strežnikov

> [!NOTE]
> Konfiguracijski primeri, ki uporabljajo `/sse` konektor, ciljajo na staro transportno kodo HTTP+SSE.
> Oddaljeni MCP strežniki `2026-07-28` uporabljajo Streamable HTTP, običajno na
> na konektorju, ki ga definira strežnik, na primer `/mcp`.

Namestitev vašega MCP strežnika omogoča drugim dostop do njegovih orodij in virov onkraj vašega lokalnega okolja. Obstaja več strategij namestitve, ki jih je treba upoštevati, odvisno od vaših zahtev glede razširljivosti, zanesljivosti in enostavnosti upravljanja. Spodaj boste našli navodila za namestitev MCP strežnikov lokalno, v zabojnikih in v oblak.

## Pregled

Ta lekcija pokriva, kako namestiti vašo MCP Server aplikacijo.

## Cilji učenja

Do konca te lekcije boste znali:

- Oceniti različne pristope namestitve.
- Namestiti vašo aplikacijo.

## Lokalni razvoj in namestitev

Če je vaš strežnik namenjen uporabi na uporabnikovi napravi, lahko sledite naslednjim korakom:

1. **Prenesite strežnik**. Če niste napisali strežnika, ga najprej prenesite na vaše računalnik.
1. **Zaženite strežniški proces**: Zaženite vašo MCP strežniško aplikacijo.

Za SSE (ni potrebno za stdio tip strežnika)

1. **Nastavite omrežje**: Poskrbite, da je strežnik dostopen na pričakovanem priključku.
1. **Povežite odjemalce**: Uporabite lokalne URL-je povezave, kot je `http://localhost:3000`.

## Namestitev v oblak

MCP strežniki se lahko nameščajo na različne oblačne platforme:

- **Brezstrežniške funkcije**: Namestite lahke MCP strežnike kot brezstrežniške funkcije.
- **Zabojniške storitve**: Uporabite storitve, kot so Azure Container Apps, AWS ECS ali Google Cloud Run.
- **Kubernetes**: Namestite in upravljajte MCP strežnike v Kubernetes grozdih za visoko razpoložljivost.

### Primer: Azure Container Apps

Azure Container Apps podpira namestitev MCP strežnikov. Še vedno je delo v teku in trenutno podpira SSE strežnike.

Tukaj je, kako lahko začnete:

1. Klonirajte repozitorij:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Zaženite ga lokalno za testiranje:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Da preizkusite lokalno, ustvarite datoteko *mcp.json* v imeniku *.vscode* in dodajte naslednjo vsebino:

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

Ko je SSE strežnik zagnan, lahko kliknete ikono za predvajanje v datoteki JSON, zdaj bi morali videti orodja na strežniku, ki jih prevzame GitHub Copilot, glejte ikono orodja.

1. Za namestitev zaženite naslednji ukaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

To je to, namestite lokalno, namestite v Azure s temi koraki.

## Dodatni viri

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Članek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repozitorij](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Kaj sledi

- Naslednje: [Napredne teme strežnika](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
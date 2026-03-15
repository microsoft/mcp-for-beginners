# Nameščanje strežnikov MCP

Nameščanje vašega MCP strežnika omogoča drugim dostop do njegovih orodij in virov onkraj vašega lokalnega okolja. Obstaja več strategij nameščanja, ki jih lahko upoštevate glede na vaše zahteve po razširljivosti, zanesljivosti in enostavnosti upravljanja. Spodaj boste našli navodila za nameščanje strežnikov MCP lokalno, v kontejnerjih in v oblaku.

## Pregled

Ta lekcija zajema, kako namestiti vašo aplikacijo MCP Server.

## Cilji učenja

Do konca te lekcije boste znali:

- Ovrednotiti različne pristope nameščanja.
- Namestiti vašo aplikacijo.

## Lokalni razvoj in nameščanje

Če je vaš strežnik namenjen za uporabo na računalniku uporabnika, lahko sledite naslednjim korakom:

1. **Prenesite strežnik**. Če niste vi napisali strežnika, ga najprej prenesite na svoj računalnik.  
1. **Zaženite proces strežnika**: Zaženite vašo aplikacijo MCP strežnika.

Za SSE (ni potrebno za strežnik tipa stdio)

1. **Konfigurirajte omrežje**: Poskrbite, da je strežnik dostopen na pričakovani vratih.  
1. **Povežite odjemalce**: Uporabite lokalne povezovalne URL-je, kot je `http://localhost:3000`

## Namestitev v oblaku

MCP strežnike je mogoče namestiti na različnih oblačnih platformah:

- **Brezstrežni funkciji**: Namestite lahke MCP strežnike kot brezstrežne funkcije  
- **Kontejnerske storitve**: Uporabite storitve, kot so Azure Container Apps, AWS ECS ali Google Cloud Run  
- **Kubernetes**: Namestite in upravljajte MCP strežnike v Kubernetes grozdih za visoko razpoložljivost

### Primer: Azure Container Apps

Azure Container Apps podpirajo namestitev MCP strežnikov. Projekt je še v teku in trenutno podpira SSE strežnike.

Tukaj je, kako lahko to naredite:

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

1. Za lokalno preizkušanje ustvarite datoteko *mcp.json* v mapi *.vscode* in vnesite naslednjo vsebino:

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

  Ko je SSE strežnik zagnan, lahko kliknete na ikono predvajanja v JSON datoteki; orodja na strežniku bi morala biti zdaj zaznana s strani GitHub Copilot, glejte ikono orodja.

1. Za nameščanje zaženite naslednji ukaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

To je to, namestite ga lokalno ali v Azure preko teh korakov.

## Dodatni viri

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Članek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repositorij Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Kaj sledi

- Naslednje: [Napredne teme o strežnikih](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem matičnem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod s strani človeka. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
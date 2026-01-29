# Namestitev MCP strežnikov

Namestitev vašega MCP strežnika omogoča drugim dostop do njegovih orodij in virov tudi izven vašega lokalnega okolja. Obstaja več strategij namestitve, ki jih je treba upoštevati glede na vaše zahteve po razširljivosti, zanesljivosti in enostavnosti upravljanja. Spodaj boste našli navodila za namestitev MCP strežnikov lokalno, v vsebnikih in v oblaku.

## Pregled

Ta lekcija zajema, kako namestiti vašo MCP Server aplikacijo.

## Cilji učenja

Do konca te lekcije boste znali:

- Oceniti različne pristope namestitve.
- Namestiti svojo aplikacijo.

## Lokalni razvoj in namestitev

Če je vaš strežnik namenjen uporabi na uporabnikovem računalniku, lahko sledite naslednjim korakom:

1. **Prenesite strežnik**. Če strežnika niste napisali sami, ga najprej prenesite na svoj računalnik.  
1. **Zaženite strežniški proces**: Zaženite svojo MCP strežniško aplikacijo.

Za SSE (ni potrebno za strežnik tipa stdio)

1. **Konfigurirajte omrežje**: Poskrbite, da je strežnik dostopen na pričakovanem vratih.  
1. **Povežite odjemalce**: Uporabite lokalne povezovalne URL-je, kot je `http://localhost:3000`.

## Namestitev v oblak

MCP strežnike lahko namestite na različne oblačne platforme:

- **Serverless Functions**: Namestite lahke MCP strežnike kot brezstrežniške funkcije.  
- **Storitve vsebnikov**: Uporabite storitve, kot so Azure Container Apps, AWS ECS ali Google Cloud Run.  
- **Kubernetes**: Namestite in upravljajte MCP strežnike v Kubernetes grozdih za visoko razpoložljivost.

### Primer: Azure Container Apps

Azure Container Apps podpirajo namestitev MCP strežnikov. Projekt je še v razvoju in trenutno podpira SSE strežnike.

Tukaj je, kako lahko to storite:

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

1. Za lokalno preizkušanje ustvarite datoteko *mcp.json* v mapi *.vscode* in dodajte naslednjo vsebino:

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

  Ko je SSE strežnik zagnan, lahko kliknete ikono za predvajanje v JSON datoteki, zdaj bi morali videti, da orodja na strežniku zazna GitHub Copilot, glejte ikono orodja.

1. Za namestitev zaženite naslednji ukaz:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Tako, namestite ga lokalno ali v Azure s temi koraki.

## Dodatni viri

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Članek o Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repozitorij](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Kaj sledi

- Naslednje: [Praktična izvedba](../../04-PracticalImplementation/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
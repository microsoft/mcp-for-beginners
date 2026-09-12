# Pag-deploy ng mga MCP Server

> [!NOTE]
> Ang mga halimbawa ng configuration na gumagamit ng `/sse` endpoint ay tumutukoy sa legacy HTTP+SSE
> transport. Ang mga MCP `2026-07-28` na remote server ay gumagamit ng Streamable HTTP, karaniwang nasa
> server-defined endpoint tulad ng `/mcp`.

Ang pag-deploy ng iyong MCP server ay nagpapahintulot sa iba na ma-access ang mga kagamitan at mapagkukunan nito lampas sa iyong lokal na kapaligiran. Mayroong ilang mga estratehiya sa pag-deploy na dapat isaalang-alang, depende sa iyong mga pangangailangan para sa scalability, reliability, at kadalian ng pamamahala. Makikita mo sa ibaba ang mga patnubay para sa pag-deploy ng mga MCP server nang lokal, sa mga container, at sa cloud.

## Pangkalahatang-ideya

Sinasaklaw ng araling ito kung paano i-deploy ang iyong MCP Server app.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Suriin ang iba't ibang mga pamamaraan ng pag-deploy.
- I-deploy ang iyong app.

## Lokal na pag-develop at pag-deploy

Kung ang iyong server ay para gamitin sa pagpapatakbo sa makina ng mga gumagamit, maaari mong sundin ang mga sumusunod na hakbang:

1. **I-download ang server**. Kung hindi ikaw ang gumawa ng server, i-download muna ito sa iyong makina.
1. **Simulan ang proseso ng server**: Patakbuhin ang iyong MCP server application

Para sa SSE (hindi kailangan para sa stdio type server)

1. **I-configure ang networking**: Siguraduhing ma-access ang server sa inaasahang port
1. **Ikonekta ang mga kliyente**: Gumamit ng mga lokal na URL ng koneksyon tulad ng `http://localhost:3000`

## Pag-deploy sa Cloud

Maaaring i-deploy ang mga MCP server sa iba't ibang mga cloud platform:

- **Serverless Functions**: Mag-deploy ng magaang MCP server bilang serverless functions
- **Container Services**: Gumamit ng mga serbisyo tulad ng Azure Container Apps, AWS ECS, o Google Cloud Run
- **Kubernetes**: Mag-deploy at mag-manage ng MCP servers sa Kubernetes clusters para sa mataas na availability

### Halimbawa: Azure Container Apps

Sinusuportahan ng Azure Container Apps ang pag-deploy ng MCP Servers. Ito ay nasa proseso pa at kasalukuyang sumusuporta sa mga SSE server.

Narito kung paano mo ito magagawa:

1. I-clone ang repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Patakbuhin ito nang lokal upang subukan ang mga bagay:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Para subukan sa lokal, gumawa ng *mcp.json* na file sa loob ng *.vscode* na direktoryo at idagdag ang sumusunod na nilalaman:

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

  Kapag naumpisahan na ang SSE server, maaari mong i-click ang play icon sa JSON file, makikita mo na ngayon ang mga tool sa server na kinikilala ng GitHub Copilot, tingnan ang Tool icon.

1. Para i-deploy, patakbuhin ang sumusunod na utos:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ayan na, i-deploy ito nang lokal, i-deploy ito sa Azure gamit ang mga hakbang na ito.

## Karagdagang mga Mapagkukunan

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Ano ang Susunod

- Susunod: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
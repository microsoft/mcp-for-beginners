# Deploying MCP Servers

Ang pag-deploy ng iyong MCP server ay nagbibigay daan sa iba na ma-access ang mga tools at resources nito lampas sa iyong lokal na kapaligiran. Mayroong ilang mga estratehiya sa pag-deploy na dapat isaalang-alang, depende sa iyong mga pangangailangan para sa scalability, reliability, at kadalian sa pamamahala. Sa ibaba makikita mo ang mga gabay para sa pag-deploy ng MCP servers nang lokal, sa mga container, at sa cloud.

## Overview

Sinasaklaw ng leksyon na ito kung paano ideploy ang iyong MCP Server app.

## Learning Objectives

Sa pagtatapos ng leksyon na ito, magagawa mong:

- Suriin ang iba't ibang pamamaraan ng pag-deploy.
- Ideploy ang iyong app.

## Local development and deployment

Kung ang iyong server ay nilalayong gamitin sa pamamagitan ng pagpapatakbo nito sa makina ng mga gumagamit, maaari mong sundin ang mga sumusunod na hakbang:

1. **I-download ang server**. Kung hindi ikaw ang sumulat ng server, i-download muna ito sa iyong makina.
1. **Simulan ang proseso ng server**: Patakbuhin ang iyong MCP server application.

Para sa SSE (hindi kailangan para sa stdio type server)

1. **I-configure ang networking**: Siguraduhing maa-access ang server sa inaasahang port.
1. **Ikonekta ang mga kliyente**: Gamitin ang mga lokal na connection URL tulad ng `http://localhost:3000`.

## Cloud Deployment

Maaaring ideploy ang mga MCP server sa iba't ibang cloud platforms:

- **Serverless Functions**: Ideploy ang mga magagaan na MCP server bilang serverless functions.
- **Container Services**: Gamitin ang mga serbisyo tulad ng Azure Container Apps, AWS ECS, o Google Cloud Run.
- **Kubernetes**: Ideploy at pamahalaan ang MCP servers sa Kubernetes clusters para sa mataas na availability.

### Example: Azure Container Apps

Sinusuportahan ng Azure Container Apps ang pag-deploy ng MCP Servers. Ito ay nasa proseso pa ng pagbuo at kasalukuyang sinusuportahan ang mga SSE server.

Narito kung paano mo ito magagawa:

1. I-clone ang isang repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Patakbuhin ito nang lokal para subukan:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Para subukan ito nang lokal, gumawa ng *mcp.json* file sa loob ng *.vscode* directory at idagdag ang sumusunod na nilalaman:

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

  Kapag nagsimula na ang SSE server, maaari mong i-click ang play icon sa JSON file, makikita mo ngayon na kinikilala ng GitHub Copilot ang mga tools sa server, tingnan ang Tool icon.

1. Para mag-deploy, patakbuhin ang sumusunod na command:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ayun, ideploy ito nang lokal, ideploy sa Azure gamit ang mga hakbang na ito.

## Additional Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## What's Next

- Next: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsasaysay ng Paunawa**:
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na maaaring may mga pagkakamali o kamalian ang awtomatikong pagsasalin. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami responsable sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
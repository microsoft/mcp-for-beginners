# MCP szerverek telepítése

Az MCP szerver telepítése lehetővé teszi mások számára, hogy a helyi környezeteden kívül is hozzáférjenek annak eszközeihez és erőforrásaihoz. Több telepítési stratégia létezik, amelyeket a méretezhetőség, megbízhatóság és kezelhetőség igényei alapján érdemes megfontolni. Az alábbiakban útmutatást találsz az MCP szerverek helyi, konténeres és felhőbe történő telepítéséhez.

## Áttekintés

Ebben a leckében azt fedezzük fel, hogyan telepítheted az MCP Server alkalmazásodat.

## Tanulási célok

A lecke végére képes leszel:

- Különböző telepítési megközelítéseket értékelni.
- Telepíteni az alkalmazásodat.

## Helyi fejlesztés és telepítés

Ha a szervered úgy van kialakítva, hogy a felhasználók gépén fusson, akkor a következő lépéseket követheted:

1. **Töltsd le a szervert**. Ha te nem írtad a szervert, először töltsd le a gépedre.  
1. **Indítsd el a szerver folyamatát**: Futtasd az MCP szerver alkalmazásodat.

SSE esetén (nem szükséges stdio típusú szerverhez)

1. **Hálózat konfigurálása**: Gondoskodj róla, hogy a szerver az elvárt porton legyen elérhető.  
1. **Csatlakoztasd az ügyfeleket**: Használj helyi kapcsolat URL-eket, pl. `http://localhost:3000`.

## Felhőbeli telepítés

Az MCP szerverek különböző felhőplatformokra telepíthetők:

- **Serverless Functions**: Könnyű MCP szervereket telepíthetsz serverless funkcióként.
- **Konténer szolgáltatások**: Használhatsz olyan szolgáltatásokat, mint az Azure Container Apps, AWS ECS vagy Google Cloud Run.
- **Kubernetes**: MCP szervereket telepíthetsz és kezelhetsz Kubernetes klaszterekben a nagy rendelkezésre állás érdekében.

### Példa: Azure Container Apps

Az Azure Container Apps támogatja az MCP szerverek telepítését. Ez még fejlesztés alatt áll, és jelenleg SSE szervereket támogat.

Így kezdhetsz hozzá:

1. Klónozz egy repót:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```
  
1. Futtasd helyileg, hogy kipróbáld:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```
  
1. Helyi kipróbáláshoz hozz létre egy *mcp.json* fájlt egy *.vscode* könyvtárban, és add hozzá a következő tartalmat:

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
  
  Amint elindul az SSE szerver, a JSON fájlban kattints a lejátszás ikonra, ekkor a GitHub Copilot fel fogja ismerni a szerveren lévő eszközöket, lásd az Eszköz ikont.

1. A telepítéshez futtasd a következő parancsot:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```
  
Így van kész, helyileg telepítetted, illetve az Azure-ba is ezeken a lépéseken keresztül.

## További források

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps cikk](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Mi következik

- Következő: [Speciális szerver témák](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
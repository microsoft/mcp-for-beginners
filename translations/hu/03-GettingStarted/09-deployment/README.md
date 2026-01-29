# MCP szerverek telepítése

Az MCP szerver telepítése lehetővé teszi, hogy mások is hozzáférjenek az eszközeihez és erőforrásaihoz a helyi környezeteden kívül. Többféle telepítési stratégia létezik, amelyeket a skálázhatóság, megbízhatóság és a kezelhetőség szempontjai alapján érdemes mérlegelni. Az alábbiakban útmutatót találsz az MCP szerverek helyi, konténeres és felhő alapú telepítéséhez.

## Áttekintés

Ebben a leckében azt tanulhatod meg, hogyan telepítsd az MCP Server alkalmazásodat.

## Tanulási célok

A lecke végére képes leszel:

- Különböző telepítési megközelítéseket értékelni.
- Telepíteni az alkalmazásodat.

## Helyi fejlesztés és telepítés

Ha a szerveredet úgy tervezted, hogy a felhasználók gépén fusson, kövesd az alábbi lépéseket:

1. **Töltsd le a szervert**. Ha nem te írtad a szervert, először töltsd le a gépedre.  
1. **Indítsd el a szerver folyamatot**: Futtasd az MCP szerver alkalmazásodat.

SSE esetén (nem szükséges stdio típusú szerverhez)

1. **Hálózat beállítása**: Győződj meg róla, hogy a szerver elérhető a várt porton.  
1. **Csatlakoztasd az ügyfeleket**: Használj helyi kapcsolati URL-eket, például `http://localhost:3000`.

## Felhő alapú telepítés

Az MCP szerverek különböző felhőplatformokra telepíthetők:

- **Serverless Functions**: Könnyű MCP szerverek telepítése serverless funkcióként  
- **Konténer szolgáltatások**: Használj olyan szolgáltatásokat, mint az Azure Container Apps, AWS ECS vagy Google Cloud Run  
- **Kubernetes**: MCP szerverek telepítése és kezelése Kubernetes klaszterekben a magas rendelkezésre állás érdekében

### Példa: Azure Container Apps

Az Azure Container Apps támogatja az MCP szerverek telepítését. Ez még fejlesztés alatt áll, jelenleg SSE szervereket támogat.

Így csinálhatod:

1. Klónozz egy repót:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Futtasd helyben a teszteléshez:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Helyi próbához hozz létre egy *mcp.json* fájlt a *.vscode* könyvtárban, és illeszd be a következő tartalmat:

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

  Miután az SSE szerver elindult, kattints a JSON fájlban a lejátszás ikonra, így a GitHub Copilot már fel fogja ismerni a szerveren elérhető eszközöket, lásd az Eszköz ikont.

1. A telepítéshez futtasd a következő parancsot:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ennyi az egész, telepítsd helyben, vagy az Azure-ra a fenti lépésekkel.

## További források

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps cikk](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Mi következik

- Következő: [Gyakorlati megvalósítás](../../04-PracticalImplementation/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
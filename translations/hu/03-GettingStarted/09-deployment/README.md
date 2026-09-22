# MCP szerverek telepítése

> [!NOTE]
> A `/sse` végpontot használó konfigurációs példák a régi HTTP+SSE
> továbbítást célozzák. A MCP `2026-07-28` távoli szerverek a Streamable HTTP-t használják, általában
> egy szerver által meghatározott végponton, például a `/mcp`-n.

Az MCP szervered telepítése lehetővé teszi mások számára, hogy hozzáférjenek az eszközeihez és erőforrásaihoz a helyi környezeteden túl. Több telepítési stratégia is létezik, amelyeket érdemes megfontolni a skálázhatóság, megbízhatóság és a kezelés egyszerűsége alapján. Az alábbiakban útmutatót találsz az MCP szerverek helyi, konténerekben és felhőben történő telepítéséhez.

## Áttekintés

Ez a lecké azt mutatja be, hogyan telepítsd az MCP Server alkalmazásodat.

## Tanulási célok

A lecke végére képes leszel:

- Különböző telepítési megközelítések értékelése.
- Az alkalmazásod telepítése.

## Helyi fejlesztés és telepítés

Ha a szervered úgy van tervezve, hogy a felhasználók gépén fusson, a következő lépéseket követheted:

1. **Töltsd le a szervert**. Ha nem te írtad a szervert, először töltsd le a gépedre.
1. **Indítsd el a szerver folyamatot**: Futtasd az MCP szerver alkalmazásodat

SSE esetén (stdio típusú szervernél nem szükséges)

1. **Állítsd be a hálózatot**: Biztosítsd, hogy a szerver elérhető legyen a várt porton
1. **Csatlakoztasd az ügyfeleket**: Használj helyi elérési URL-eket, például `http://localhost:3000`

## Felhő alapú telepítés

MCP szerverek több felhőplatformra is telepíthetők:

- **Serverless Functions**: Könnyű MCP szerverek telepítése serverless funkcióként
- **Konténer szolgáltatások**: Használj olyan szolgáltatásokat, mint az Azure Container Apps, AWS ECS vagy Google Cloud Run
- **Kubernetes**: MCP szerverek telepítése és kezelése Kubernetes klaszterekben magas rendelkezésre állásért

### Példa: Azure Container Apps

Az Azure Container Apps támogatja az MCP szerverek telepítését. Ez még fejlesztés alatt áll, és jelenleg SSE szervereket támogat.

Így kezdhetsz hozzá:

1. Klónozz egy repót:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Futtasd helyben a kipróbáláshoz:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Helyi kipróbáláshoz hozz létre egy *mcp.json* fájlt a *.vscode* mappában, és illeszd be a következő tartalmat:

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

  Miután elindítottad az SSE szervert, a JSON fájlban kattints a lejátszás ikonra, most már látnod kell, hogy a GitHub Copilot felveszi a szerveren lévő eszközöket, lásd az Eszköz ikont.

1. A telepítéshez futtasd a következő parancsot:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Ennyi az egész, így telepítheted helyben, illetve Azure-ra a fentiek alapján.

## További források

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps cikk](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Mi következik

- Következő: [Haladó szerver témák](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
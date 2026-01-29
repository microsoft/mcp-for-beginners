# Weather MCP Server

Ez egy példa MCP Server Pythonban, amely időjárás eszközöket valósít meg hamis válaszokkal. Használható kiindulópontként a saját MCP Serveredhez. A következő funkciókat tartalmazza:

- **Weather Tool**: Egy eszköz, amely adott hely alapján hamisított időjárási információkat szolgáltat.
- **Kapcsolódás az Agent Builderhez**: Egy funkció, amely lehetővé teszi az MCP szerver csatlakoztatását az Agent Builderhez tesztelés és hibakeresés céljából.
- **Hibakeresés a [MCP Inspector](https://github.com/modelcontextprotocol/inspector) segítségével**: Egy funkció, amely lehetővé teszi az MCP Server hibakeresését az MCP Inspector használatával.

## Kezdés a Weather MCP Server sablonnal

> **Előfeltételek**
>
> Az MCP Server futtatásához a helyi fejlesztői gépeden szükséged lesz:
>
> - [Python](https://www.python.org/)
> - (*Opcionális - ha az uv-t részesíted előnyben*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Környezet előkészítése

Kétféle módon állíthatod be a környezetet ehhez a projekthez. Választhatsz a preferenciád szerint.

> Megjegyzés: A virtuális környezet létrehozása után töltsd újra a VSCode-ot vagy a terminált, hogy a virtuális környezet Pythonja legyen használatban.

| Módszer | Lépések |
| -------- | ----- |
| `uv` használata | 1. Hozd létre a virtuális környezetet: `uv venv` <br>2. Futtasd a VSCode parancsot "***Python: Select Interpreter***", és válaszd ki a létrehozott virtuális környezet Pythonját <br>3. Telepítsd a függőségeket (beleértve a fejlesztői függőségeket is): `uv pip install -r pyproject.toml --extra dev` |
| `pip` használata | 1. Hozd létre a virtuális környezetet: `python -m venv .venv` <br>2. Futtasd a VSCode parancsot "***Python: Select Interpreter***", és válaszd ki a létrehozott virtuális környezet Pythonját<br>3. Telepítsd a függőségeket (beleértve a fejlesztői függőségeket is): `pip install -e .[dev]` |

A környezet beállítása után a szervert a helyi fejlesztői gépeden az Agent Builder segítségével, MCP kliensként futtathatod a kezdéshez:
1. Nyisd meg a VS Code Hibakereső panelt. Válaszd a `Debug in Agent Builder` opciót vagy nyomd meg az `F5`-öt az MCP szerver hibakeresésének elindításához.
2. Használd az AI Toolkit Agent Buildert a szerver teszteléséhez [ezzel a prompttal](../../../../../../../../../../open_prompt_builder). A szerver automatikusan csatlakozik az Agent Builderhez.
3. Kattints a `Run` gombra, hogy a prompttal teszteld a szervert.

**Gratulálunk**! Sikeresen futtattad a Weather MCP Servert a helyi fejlesztői gépeden az Agent Builder segítségével MCP kliensként.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mi található a sablonban

| Mappa / Fájl | Tartalom                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode fájlok a hibakereséshez               |
| `.aitk`      | Konfigurációk az AI Toolkithez                |
| `src`        | Forráskód a weather mcp szerverhez            |

## Hogyan hibakeressük a Weather MCP Servert

> Megjegyzések:
> - A [MCP Inspector](https://github.com/modelcontextprotocol/inspector) egy vizuális fejlesztői eszköz az MCP szerverek teszteléséhez és hibakereséséhez.
> - Minden hibakeresési mód támogatja a töréspontokat, így adhatsz töréspontokat az eszköz megvalósítási kódjához.

| Hibakeresési mód | Leírás | Hibakeresési lépések |
| ---------- | ----------- | --------------- |
| Agent Builder | Az MCP szerver hibakeresése az Agent Builderben az AI Toolkit segítségével. | 1. Nyisd meg a VS Code Hibakereső panelt. Válaszd a `Debug in Agent Builder` opciót, majd nyomd meg az `F5`-öt az MCP szerver hibakeresésének elindításához.<br>2. Használd az AI Toolkit Agent Buildert a szerver teszteléséhez [ezzel a prompttal](../../../../../../../../../../open_prompt_builder). A szerver automatikusan csatlakozik az Agent Builderhez.<br>3. Kattints a `Run` gombra, hogy a prompttal teszteld a szervert. |
| MCP Inspector | Az MCP szerver hibakeresése az MCP Inspector segítségével. | 1. Telepítsd a [Node.js-t](https://nodejs.org/)<br> 2. Állítsd be az Inspectort: `cd inspector` && `npm install` <br> 3. Nyisd meg a VS Code Hibakereső panelt. Válaszd a `Debug SSE in Inspector (Edge)` vagy `Debug SSE in Inspector (Chrome)` opciót. Nyomd meg az F5-öt a hibakeresés elindításához.<br> 4. Amikor az MCP Inspector elindul a böngészőben, kattints a `Connect` gombra, hogy csatlakoztasd ezt az MCP szervert.<br> 5. Ezután használhatod a `List Tools` funkciót, választhatsz eszközt, megadhatod a paramétereket, és a `Run Tool` gombbal hibakeresheted a szerver kódját.<br> |

## Alapértelmezett portok és testreszabások

| Hibakeresési mód | Portok | Meghatározások | Testreszabások | Megjegyzés |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Szerkeszd a [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) fájlokat a portok módosításához. | Nincs |
| MCP Inspector | 3001 (Szerver); 5173 és 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Szerkeszd a [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) fájlokat a portok módosításához. | Nincs |

## Visszajelzés

Ha bármilyen visszajelzésed vagy javaslatod van ehhez a sablonhoz, kérjük, nyiss egy issue-t az [AI Toolkit GitHub tárhelyén](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
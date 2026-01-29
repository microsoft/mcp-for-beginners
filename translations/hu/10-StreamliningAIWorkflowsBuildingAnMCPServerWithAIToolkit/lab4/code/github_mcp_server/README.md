# Weather MCP Szerver

Ez egy Pythonban írt mintaszerver, amely időjárási eszközöket valósít meg mock válaszokkal. Használható saját MCP szerver alapjaként. Az alábbi funkciókat tartalmazza:

- **Időjárási eszköz**: Egy eszköz, amely mock időjárási információkat nyújt a megadott hely alapján.
- **Git Clone eszköz**: Egy eszköz, amely egy git repozitóriumot klónoz egy megadott mappába.
- **VS Code Open eszköz**: Egy eszköz, amely megnyit egy mappát a VS Code vagy VS Code Insiders alkalmazásban.
- **Kapcsolódás az Agent Builderhez**: Egy funkció, amely lehetővé teszi az MCP szerver csatlakoztatását az Agent Builderhez tesztelés és hibakeresés céljából.
- **Hibakeresés a [MCP Inspector](https://github.com/modelcontextprotocol/inspector) segítségével**: Egy funkció, amely lehetővé teszi az MCP szerver hibakeresését az MCP Inspector használatával.

## Kezdje el a Weather MCP Szerver sablonnal

> **Előfeltételek**
>
> Az MCP szerver futtatásához a helyi fejlesztői gépen szüksége lesz:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Szükséges a git_clone_repo eszközhöz)
> - [VS Code](https://code.visualstudio.com/) vagy [VS Code Insiders](https://code.visualstudio.com/insiders/) (Szükséges az open_in_vscode eszközhöz)
> - (*Opcionális - ha az uv-t preferálja*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Környezet előkészítése

Két megközelítés van a projekt környezetének beállítására. Válassza ki az Önnek legmegfelelőbbet.

> Megjegyzés: Indítsa újra a VSCode-t vagy a terminált, hogy biztosítsa a virtuális környezet Pythonjának használatát a virtuális környezet létrehozása után.

| Megközelítés | Lépések |
| ------------ | ------- |
| `uv` használata | 1. Virtuális környezet létrehozása: `uv venv` <br>2. Futtassa a VSCode parancsot "***Python: Select Interpreter***", és válassza ki a létrehozott virtuális környezet Pythonját <br>3. Függőségek telepítése (beleértve a fejlesztési függőségeket): `uv pip install -r pyproject.toml --extra dev` |
| `pip` használata | 1. Virtuális környezet létrehozása: `python -m venv .venv` <br>2. Futtassa a VSCode parancsot "***Python: Select Interpreter***", és válassza ki a létrehozott virtuális környezet Pythonját <br>3. Függőségek telepítése (beleértve a fejlesztési függőségeket): `pip install -e .[dev]` |

A környezet beállítása után futtathatja a szervert a helyi fejlesztői gépen az Agent Builder segítségével MCP kliensként, hogy elkezdhesse:
1. Nyissa meg a VS Code Debug panelt. Válassza a `Debug in Agent Builder` opciót, vagy nyomja meg az `F5` gombot az MCP szerver hibakeresésének elindításához.
2. Használja az AI Toolkit Agent Buildert a szerver teszteléséhez [ezzel a prompttal](../../../../../../../../../../../open_prompt_builder). A szerver automatikusan csatlakozik az Agent Builderhez.
3. Kattintson a `Run` gombra a szerver teszteléséhez a prompttal.

**Gratulálunk**! Sikeresen futtatta a Weather MCP szervert a helyi fejlesztői gépen az Agent Builder segítségével MCP kliensként.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mi található a sablonban?

| Mappa / Fájl | Tartalom                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode fájlok hibakereséshez                 |
| `.aitk`      | Konfigurációk az AI Toolkithez               |
| `src`        | A Weather MCP szerver forráskódja            |

## Hogyan lehet hibakeresni a Weather MCP szervert?

> Megjegyzések:
> - A [MCP Inspector](https://github.com/modelcontextprotocol/inspector) egy vizuális fejlesztői eszköz MCP szerverek teszteléséhez és hibakereséséhez.
> - Minden hibakeresési mód támogatja a töréspontokat, így hozzáadhat töréspontokat az eszköz implementációs kódjához.

## Elérhető eszközök

### Időjárási eszköz
A `get_weather` eszköz mock időjárási információkat nyújt egy megadott helyre.

| Paraméter | Típus | Leírás |
| --------- | ----- | ------ |
| `location` | string | A hely, amelyre az időjárást lekérdezi (pl. városnév, állam vagy koordináták) |

### Git Clone eszköz
A `git_clone_repo` eszköz egy git repozitóriumot klónoz egy megadott mappába.

| Paraméter | Típus | Leírás |
| --------- | ----- | ------ |
| `repo_url` | string | A klónozandó git repozitórium URL-je |
| `target_folder` | string | Az útvonal, ahová a repozitóriumot klónozni kell |

Az eszköz egy JSON objektumot ad vissza:
- `success`: Boolean, amely jelzi, hogy a művelet sikeres volt-e
- `target_folder` vagy `error`: A klónozott repozitórium útvonala vagy egy hibaüzenet

### VS Code Open eszköz
Az `open_in_vscode` eszköz megnyit egy mappát a VS Code vagy VS Code Insiders alkalmazásban.

| Paraméter | Típus | Leírás |
| --------- | ----- | ------ |
| `folder_path` | string | Az útvonal a megnyitandó mappához |
| `use_insiders` | boolean (opcionális) | Megadja, hogy a VS Code Insiders-t használja-e a normál VS Code helyett |

Az eszköz egy JSON objektumot ad vissza:
- `success`: Boolean, amely jelzi, hogy a művelet sikeres volt-e
- `message` vagy `error`: Egy megerősítő üzenet vagy egy hibaüzenet

| Hibakeresési mód | Leírás | Hibakeresési lépések |
| ---------------- | ------ | -------------------- |
| Agent Builder | Az MCP szerver hibakeresése az Agent Builderben az AI Toolkit segítségével. | 1. Nyissa meg a VS Code Debug panelt. Válassza a `Debug in Agent Builder` opciót, és nyomja meg az `F5` gombot az MCP szerver hibakeresésének elindításához.<br>2. Használja az AI Toolkit Agent Buildert a szerver teszteléséhez [ezzel a prompttal](../../../../../../../../../../../open_prompt_builder). A szerver automatikusan csatlakozik az Agent Builderhez.<br>3. Kattintson a `Run` gombra a szerver teszteléséhez a prompttal. |
| MCP Inspector | Az MCP szerver hibakeresése az MCP Inspector segítségével. | 1. Telepítse a [Node.js](https://nodejs.org/) alkalmazást<br> 2. Állítsa be az Inspectort: `cd inspector` && `npm install` <br> 3. Nyissa meg a VS Code Debug panelt. Válassza a `Debug SSE in Inspector (Edge)` vagy `Debug SSE in Inspector (Chrome)` opciót. Nyomja meg az F5 gombot a hibakeresés elindításához.<br> 4. Amikor az MCP Inspector elindul a böngészőben, kattintson a `Connect` gombra az MCP szerver csatlakoztatásához.<br> 5. Ezután `List Tools`, válasszon egy eszközt, adja meg a paramétereket, és `Run Tool` a szerver kódjának hibakereséséhez.<br> |

## Alapértelmezett portok és testreszabások

| Hibakeresési mód | Portok | Meghatározások | Testreszabások | Megjegyzés |
| ---------------- | ------ | -------------- | -------------- | ---------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Szerkessze a [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) fájlokat a portok módosításához. | N/A |
| MCP Inspector | 3001 (Szerver); 5173 és 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Szerkessze a [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) fájlokat a portok módosításához. | N/A |

## Visszajelzés

Ha bármilyen visszajelzése vagy javaslata van a sablonnal kapcsolatban, nyisson meg egy hibajegyet az [AI Toolkit GitHub repozitóriumában](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
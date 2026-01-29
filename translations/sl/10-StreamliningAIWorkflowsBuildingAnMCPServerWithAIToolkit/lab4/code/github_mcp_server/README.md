# Weather MCP Strežnik

To je vzorčni MCP strežnik v Pythonu, ki implementira orodja za vreme z lažnimi odgovori. Uporabite ga lahko kot osnovo za svoj MCP strežnik. Vključuje naslednje funkcionalnosti:

- **Orodje za vreme**: Orodje, ki ponuja lažne informacije o vremenu glede na podano lokacijo.
- **Orodje za kloniranje Git repozitorija**: Orodje, ki klonira Git repozitorij v določeno mapo.
- **Orodje za odpiranje v VS Code**: Orodje, ki odpre mapo v VS Code ali VS Code Insiders.
- **Povezava z Agent Builderjem**: Funkcija, ki omogoča povezavo MCP strežnika z Agent Builderjem za testiranje in odpravljanje napak.
- **Odpravljanje napak v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcija, ki omogoča odpravljanje napak MCP strežnika z uporabo MCP Inspectorja.

## Začetek z Weather MCP strežnikom

> **Predpogoji**
>
> Za zagon MCP strežnika na lokalnem razvojnem računalniku potrebujete:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (zahtevano za orodje git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ali [VS Code Insiders](https://code.visualstudio.com/insiders/) (zahtevano za orodje open_in_vscode)
> - (*Neobvezno - če uporabljate uv*) [uv](https://github.com/astral-sh/uv)
> - [Razširitev za odpravljanje napak v Pythonu](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprava okolja

Za nastavitev okolja za ta projekt sta na voljo dva pristopa. Izberite tistega, ki vam najbolj ustreza.

> Opomba: Po ustvarjanju virtualnega okolja ponovno zaženite VSCode ali terminal, da zagotovite uporabo Python-a iz virtualnega okolja.

| Pristop | Koraki |
| -------- | ----- |
| Uporaba `uv` | 1. Ustvarite virtualno okolje: `uv venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite Python iz ustvarjenega virtualnega okolja <br>3. Namestite odvisnosti (vključno z odvisnostmi za razvoj): `uv pip install -r pyproject.toml --extra dev` |
| Uporaba `pip` | 1. Ustvarite virtualno okolje: `python -m venv .venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite Python iz ustvarjenega virtualnega okolja<br>3. Namestite odvisnosti (vključno z odvisnostmi za razvoj): `pip install -e .[dev]` | 

Po nastavitvi okolja lahko strežnik zaženete na lokalnem razvojnem računalniku prek Agent Builderja kot MCP odjemalca za začetek:
1. Odprite Debug panel v VS Code. Izberite `Debug in Agent Builder` ali pritisnite `F5` za začetek odpravljanja napak MCP strežnika.
2. Uporabite AI Toolkit Agent Builder za testiranje strežnika z [tem pozivom](../../../../../../../../../../../open_prompt_builder). Strežnik bo samodejno povezan z Agent Builderjem.
3. Kliknite `Run` za testiranje strežnika s pozivom.

**Čestitamo**! Uspešno ste zagnali Weather MCP strežnik na lokalnem razvojnem računalniku prek Agent Builderja kot MCP odjemalca.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Kaj je vključeno v predlogo

| Mapa / Datoteka | Vsebina                                     |
| --------------- | ------------------------------------------- |
| `.vscode`       | Datoteke VSCode za odpravljanje napak       |
| `.aitk`         | Konfiguracije za AI Toolkit                |
| `src`           | Izvorna koda za Weather MCP strežnik       |

## Kako odpravljati napake v Weather MCP strežniku

> Opombe:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualno orodje za razvijalce za testiranje in odpravljanje napak MCP strežnikov.
> - Vsi načini odpravljanja napak podpirajo točke prekinitve, zato lahko dodate točke prekinitve v kodo implementacije orodja.

## Razpoložljiva orodja

### Orodje za vreme
Orodje `get_weather` ponuja lažne informacije o vremenu za določeno lokacijo.

| Parameter | Tip | Opis |
| --------- | ---- | ---- |
| `location` | string | Lokacija, za katero želite pridobiti informacije o vremenu (npr. ime mesta, država ali koordinate) |

### Orodje za kloniranje Git repozitorija
Orodje `git_clone_repo` klonira Git repozitorij v določeno mapo.

| Parameter | Tip | Opis |
| --------- | ---- | ---- |
| `repo_url` | string | URL Git repozitorija, ki ga želite klonirati |
| `target_folder` | string | Pot do mape, kamor naj bo repozitorij kloniran |

Orodje vrne JSON objekt z:
- `success`: Boolean, ki označuje, ali je operacija uspela
- `target_folder` ali `error`: Pot kloniranega repozitorija ali sporočilo o napaki

### Orodje za odpiranje v VS Code
Orodje `open_in_vscode` odpre mapo v aplikaciji VS Code ali VS Code Insiders.

| Parameter | Tip | Opis |
| --------- | ---- | ---- |
| `folder_path` | string | Pot do mape, ki jo želite odpreti |
| `use_insiders` | boolean (neobvezno) | Ali naj se uporabi VS Code Insiders namesto običajnega VS Code |

Orodje vrne JSON objekt z:
- `success`: Boolean, ki označuje, ali je operacija uspela
- `message` ali `error`: Potrditveno sporočilo ali sporočilo o napaki

| Način odpravljanja napak | Opis | Koraki za odpravljanje napak |
| ------------------------ | ----- | --------------------------- |
| Agent Builder | Odpravljanje napak MCP strežnika v Agent Builderju prek AI Toolkit. | 1. Odprite Debug panel v VS Code. Izberite `Debug in Agent Builder` in pritisnite `F5` za začetek odpravljanja napak MCP strežnika.<br>2. Uporabite AI Toolkit Agent Builder za testiranje strežnika z [tem pozivom](../../../../../../../../../../../open_prompt_builder). Strežnik bo samodejno povezan z Agent Builderjem.<br>3. Kliknite `Run` za testiranje strežnika s pozivom. |
| MCP Inspector | Odpravljanje napak MCP strežnika z uporabo MCP Inspectorja. | 1. Namestite [Node.js](https://nodejs.org/)<br> 2. Nastavite Inspector: `cd inspector` && `npm install` <br> 3. Odprite Debug panel v VS Code. Izberite `Debug SSE in Inspector (Edge)` ali `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za začetek odpravljanja napak.<br> 4. Ko se MCP Inspector zažene v brskalniku, kliknite gumb `Connect`, da povežete ta MCP strežnik.<br> 5. Nato lahko `List Tools`, izberete orodje, vnesete parametre in `Run Tool` za odpravljanje napak v kodi strežnika.<br> |

## Privzeta vrata in prilagoditve

| Način odpravljanja napak | Vrata | Definicije | Prilagoditve | Opomba |
| ------------------------ | ----- | ---------- | ------------ | ------ |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za spremembo zgornjih vrat. | N/A |
| MCP Inspector | 3001 (strežnik); 5173 in 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za spremembo zgornjih vrat.| N/A |

## Povratne informacije

Če imate kakršne koli povratne informacije ali predloge za to predlogo, odprite težavo na [GitHub repozitoriju AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.
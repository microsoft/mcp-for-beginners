# Strežnik za vremenski MCP

To je primer strežnika MCP v Pythonu, ki izvaja vremenska orodja z navideznimi odgovori. Uporablja se lahko kot osnova za vaš lasten strežnik MCP. Vključuje naslednje funkcije:

- **Vremensko orodje**: Orodje, ki zagotavlja navidezne informacije o vremenu glede na določeno lokacijo.
- **Orodje za kloniranje Gita**: Orodje, ki klonira git repozitorij v določeno mapo.
- **Orodje za odpiranje v VS Code**: Orodje, ki odpre mapo v VS Code ali VS Code Insiders.
- **Povezava z Agent Builderjem**: Funkcija, ki omogoča povezavo strežnika MCP z Agent Builderjem za testiranje in odpravljanje napak.
- **Odpravljanje napak v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcija, ki omogoča odpravljanje napak strežnika MCP z uporabo MCP Inspector.

## Začetek z vzorcem Strežnika za vremenski MCP

> **Pogoji**
>
> Za zagon strežnika MCP na lokalnem razvojno računalniku potrebujete:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (potreben za orodje git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ali [VS Code Insiders](https://code.visualstudio.com/insiders/) (potrebno za orodje open_in_vscode)
> - (*Neobvezno - če imate raje uv*) [uv](https://github.com/astral-sh/uv)
> - [Razširitev za Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprava okolja

Obstajata dva pristopa za nastavitev okolja za ta projekt. Izberete lahko enega glede na vaše želje.

> Opomba: Ponovno naložite VSCode ali terminal, da se zagotovi uporaba pythona iz virtualnega okolja po ustvarjanju virtualnega okolja.

| Pristop | Koraki |
| -------- | ----- |
| Z uporabo `uv` | 1. Ustvarite virtualno okolje: `uv venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite python iz ustvarjenega virtualnega okolja <br>3. Namestite odvisnosti (vključno z dev odvisnostmi): `uv pip install -r pyproject.toml --extra dev` |
| Z uporabo `pip` | 1. Ustvarite virtualno okolje: `python -m venv .venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite python iz ustvarjenega virtualnega okolja<br>3. Namestite odvisnosti (vključno z dev odvisnostmi): `pip install -e .[dev]` | 

Po nastavitvi okolja lahko strežnik zaženete na lokalnem razvojno računalniku preko Agent Builderja kot MCP odjemalec za začetek:
1. Odprite VS Code panel za odpravljanje napak. Izberite `Debug in Agent Builder` ali pritisnite `F5` za začetek odpravljanja napak strežnika MCP.
2. V Microsoft Foundry Toolkit za Visual Studio Code Agent Builder izberite aktivno namensko postavitev, kot je `gpt-5.1`, nato vnesite: `What is the weather in Shanghai?` Strežnik se bo samodejno povezal.
3. Kliknite `Run` za testiranje strežnika z ukazom.

**Čestitamo**! Uspešno ste zagnali Strežnik za vremenski MCP na lokalnem razvojnem računalniku preko Agent Builderja kot MCP odjemalec.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Kaj je vključeno v vzorcu

| Mapa / Datoteka | Vsebina                                  |
| ------------- | ---------------------------------------- |
| `.vscode`    | Datoteke VSCode za odpravljanje napak    |
| `.aitk`      | Konfiguracija Microsoft Foundry Toolkit  |
| `src`        | Izvorna koda vremenskega mcp strežnika    |

## Kako odpravljati napake v Strežniku za vremenski MCP

> Opombe:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualno orodje za razvijalce za testiranje in odpravljanje napak MCP strežnikov.
> - Vsi načini odpravljanja napak podpirajo prelomne točke, tako da lahko dodate prelomne točke v kodo orodja.

## Na voljo orodja

### Vremensko orodje
Orodje `get_weather` zagotavlja navidezne informacije o vremenu za določeno lokacijo.

| Parameter | Tip | Opis |
| --------- | ---- | ----- |
| `location` | niz | Lokacija za preverjanje vremena (npr. ime mesta, država ali koordinate) |

### Orodje za kloniranje Git
Orodje `git_clone_repo` klonira git repozitorij v določeno mapo.

| Parameter | Tip | Opis |
| --------- | ---- | ----- |
| `repo_url` | niz | URL git repozitorija, ki ga želite klonirati |
| `target_folder` | niz | Pot do mape, kamor naj se repozitorij klonira |

Orodje vrne JSON objekt z:
- `success`: Boolean, ki označuje, ali je bila operacija uspešna
- `target_folder` ali `error`: Pot kloniranega repozitorija ali sporočilo o napaki

### Orodje za odpiranje v VS Code
Orodje `open_in_vscode` odpre mapo v aplikaciji VS Code ali VS Code Insiders.

| Parameter | Tip | Opis |
| --------- | ---- | ----- |
| `folder_path` | niz | Pot do mape, ki jo želite odpreti |
| `use_insiders` | boolean (neobvezno) | Ali uporabiti VS Code Insiders namesto običajnega VS Code |

Orodje vrne JSON objekt z:
- `success`: Boolean, ki označuje, ali je bila operacija uspešna
- `message` ali `error`: Potrditveno sporočilo ali sporočilo o napaki

| Način odpravljanja napak | Opis | Koraki za odpravljanje napak |
| ---------------------- | ----- | ------------------------- |
| Agent Builder | Odpravljanje napak MCP strežnika prek Agent Builderja preko Microsoft Foundry Toolkit za Visual Studio Code. | 1. Odprite VS Code panel za odpravljanje napak. Izberite `Debug in Agent Builder` in pritisnite `F5` za začetek odpravljanja napak strežnika MCP.<br>2. Izberite aktivno postavitev Foundry, kot je `gpt-5.1`, nato vnesite `What is the weather in Shanghai?`. Strežnik se bo povezal samodejno.<br>3. Kliknite `Run` za testiranje strežnika z ukazom. |
| MCP Inspector | Odpravljanje napak strežnika MCP z uporabo MCP Inspector. | 1. Namestite [Node.js](https://nodejs.org/)<br> 2. Nastavite Inspector: `cd inspector` && `npm install` <br> 3. Odprite VS Code panel za odpravljanje napak. Izberite `Debug SSE in Inspector (Edge)` ali `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za začetek odpravljanja napak.<br> 4. Ko se MCP Inspector zažene v brskalniku, kliknite gumb `Connect` za povezavo tega strežnika MCP.<br> 5. Nato lahko `List Tools`, izberete orodje, vnesete parametre in `Run Tool` za odpravljanje napak vaše kode strežnika.<br> |

## Privzeti priključki in prilagoditve

| Način odpravljanja napak | Priključki | Definicije | Prilagoditve | Opomba |
| ---------------------- | --------- | ---------- | ----------- | ------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za spremembo zgornjih priključkov. | Nič |
| MCP Inspector | 3001 (strežnik); 5173 in 3000 (inspektor) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za spremembo zgornjih priključkov. | Nič |

## Povratne informacije

Če imate kakršnekoli povratne informacije ali predloge za ta vzorec, prosim odprite zadevo v [Microsoft Foundry Toolkit za Visual Studio Code GitHub repozitoriju](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Weather MCP Server

To je primer MCP strežnika v Pythonu, ki implementira vremenska orodja z lažnimi odgovori. Uporabite ga lahko kot osnovo za svoj lasten MCP strežnik. Vključuje naslednje funkcije:

- **Weather Tool**: Orodje, ki zagotavlja lažne vremenske informacije glede na podano lokacijo.
- **Povezava z Agent Builderjem**: Funkcija, ki omogoča povezavo MCP strežnika z Agent Builderjem za testiranje in odpravljanje napak.
- **Odpravljanje napak v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcija, ki omogoča odpravljanje napak MCP strežnika z uporabo MCP Inspectorja.

## Začnite z Weather MCP Server predlogo

> **Pogoji**
>
> Za zagon MCP strežnika na lokalnem razvojnem računalniku potrebujete:
>
> - [Python](https://www.python.org/)
> - (*Neobvezno - če raje uporabljate uv*) [uv](https://github.com/astral-sh/uv)
> - [Razširitev za Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprava okolja

Za nastavitev okolja za ta projekt obstajata dva pristopa. Izberete lahko tistega, ki vam bolj ustreza.

> Opomba: Ponovno naložite VSCode ali terminal, da zagotovite uporabo Pythona iz virtualnega okolja po njegovi ustvaritvi.

| Pristop       | Koraki                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------- |
| Uporaba `uv`  | 1. Ustvarite virtualno okolje: `uv venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite Python iz ustvarjenega virtualnega okolja <br>3. Namestite odvisnosti (vključno z razvojnimi): `uv pip install -r pyproject.toml --extra dev` |
| Uporaba `pip` | 1. Ustvarite virtualno okolje: `python -m venv .venv` <br>2. Zaženite ukaz v VSCode "***Python: Select Interpreter***" in izberite Python iz ustvarjenega virtualnega okolja <br>3. Namestite odvisnosti (vključno z razvojnimi): `pip install -e .[dev]` |

Po nastavitvi okolja lahko strežnik zaženete na lokalnem razvojnem računalniku preko Agent Builderja kot MCP klienta, da začnete:
1. Odprite razhroščevalno ploščo v VS Code. Izberite `Debug in Agent Builder` ali pritisnite `F5` za začetek razhroščevanja MCP strežnika.
2. Uporabite AI Toolkit Agent Builder za testiranje strežnika z [tem pozivom](../../../../../../../../../../open_prompt_builder). Strežnik bo samodejno povezan z Agent Builderjem.
3. Kliknite `Run` za testiranje strežnika s pozivom.

**Čestitke**! Uspešno ste zagnali Weather MCP Server na svojem lokalnem razvojnem računalniku preko Agent Builderja kot MCP klienta.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Kaj je vključeno v predlogo

| Mapa / Datoteka | Vsebina                                  |
| --------------- | ---------------------------------------- |
| `.vscode`       | Datoteke za razhroščevanje v VSCode     |
| `.aitk`         | Konfiguracije za AI Toolkit              |
| `src`           | Izvorna koda za weather mcp strežnik    |

## Kako razhroščevati Weather MCP Server

> Opombe:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualno orodje za razvijalce za testiranje in odpravljanje napak MCP strežnikov.
> - Vsi načini razhroščevanja podpirajo točke prekinitve, zato lahko dodate točke prekinitve v kodo implementacije orodja.

| Način razhroščevanja | Opis | Koraki za razhroščevanje |
| -------------------- | ---- | ------------------------ |
| Agent Builder        | Razhroščevanje MCP strežnika v Agent Builderju preko AI Toolkit. | 1. Odprite razhroščevalno ploščo v VS Code. Izberite `Debug in Agent Builder` in pritisnite `F5` za začetek razhroščevanja MCP strežnika.<br>2. Uporabite AI Toolkit Agent Builder za testiranje strežnika z [tem pozivom](../../../../../../../../../../open_prompt_builder). Strežnik bo samodejno povezan z Agent Builderjem.<br>3. Kliknite `Run` za testiranje strežnika s pozivom. |
| MCP Inspector        | Razhroščevanje MCP strežnika z uporabo MCP Inspectorja. | 1. Namestite [Node.js](https://nodejs.org/)<br>2. Nastavite Inspector: `cd inspector` && `npm install` <br>3. Odprite razhroščevalno ploščo v VS Code. Izberite `Debug SSE in Inspector (Edge)` ali `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za začetek razhroščevanja.<br>4. Ko se MCP Inspector zažene v brskalniku, kliknite gumb `Connect` za povezavo s tem MCP strežnikom.<br>5. Nato lahko `List Tools`, izberete orodje, vnesete parametre in `Run Tool` za razhroščevanje vaše kode strežnika.<br> |

## Privzeti porti in prilagoditve

| Način razhroščevanja | Porti                  | Definicije                      | Prilagoditve                                                                 | Opomba |
| -------------------- | ---------------------- | ------------------------------ | --------------------------------------------------------------------------- | ------ |
| Agent Builder        | 3001                   | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) za spremembo zgornjih portov. | N/A    |
| MCP Inspector        | 3001 (strežnik); 5173 in 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) za spremembo zgornjih portov. | N/A    |

## Povratne informacije

Če imate kakršnekoli povratne informacije ali predloge za to predlogo, prosimo, odprite zadevo na [AI Toolkit GitHub repozitoriju](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
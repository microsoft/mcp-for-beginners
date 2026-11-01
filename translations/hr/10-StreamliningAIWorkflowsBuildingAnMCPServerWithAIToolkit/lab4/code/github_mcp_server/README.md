# Weather MCP Server

Ovo je primjer MCP Servera u Pythonu koji implementira vremenske alate s lažnim odgovorima. Može se koristiti kao kostur za vaš vlastiti MCP Server. Uključuje sljedeće značajke: 

- **Weather Tool**: Alat koji pruža lažne vremenske informacije na temelju zadane lokacije.
- **Git Clone Tool**: Alat koji klonira git repozitorij u određeni direktorij.
- **VS Code Open Tool**: Alat koji otvara direktorij u VS Code ili VS Code Insiders.
- **Connect to Agent Builder**: Značajka koja omogućuje povezivanje MCP servera s Agent Builderom za testiranje i ispravljanje pogrešaka.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Značajka koja omogućuje ispravljanje pogrešaka MCP Servera pomoću MCP Inspectora.

## Početak rada s predloškom Weather MCP Servera

> **Preduvjeti**
>
> Za pokretanje MCP Servera na vašem lokalnom razvojnom računalu trebate:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Potrebno za alat git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ili [VS Code Insiders](https://code.visualstudio.com/insiders/) (Potrebno za alat open_in_vscode)
> - (*Opcionalno - ako preferirate uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprema okoline

Postoje dva pristupa za postavljanje okoline za ovaj projekt. Možete odabrati bilo koji za koji se odlučite.

> Napomena: Ponovno učitajte VSCode ili terminal kako biste osigurali da se koristi python iz virtualnog okruženja nakon njegovog kreiranja.

| Pristup | Koraci |
| -------- | ----- |
| Korištenje `uv` | 1. Izradite virtualno okruženje: `uv venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite python iz kreiranog virtualnog okruženja <br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `uv pip install -r pyproject.toml --extra dev` |
| Korištenje `pip` | 1. Izradite virtualno okruženje: `python -m venv .venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite python iz kreiranog virtualnog okruženja<br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `pip install -e .[dev]` | 

Nakon postavljanja okoline, možete pokrenuti server na svom lokalnom razvojnom računalu putem Agent Buildera kao MCP klijenta da započnete:
1. Otvorite VS Code Debug ploču. Odaberite `Debug in Agent Builder` ili pritisnite `F5` za pokretanje ispravljanja pogrešaka MCP servera.
2. U Microsoft Foundry Toolkit for Visual Studio Code Agent Builderu odaberite aktivnu Foundry distribuciju kao što je `gpt-5.1`, zatim unesite: `What is the weather in Shanghai?` Server će se automatski povezati.
3. Kliknite `Run` za testiranje servera s promptom.

**Čestitamo**! Uspješno ste pokrenuli Weather MCP Server na svom lokalnom razvojnom računalu putem Agent Buildera kao MCP klijent.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Što je uključeno u predložak

| Mapa / Datoteka| Sadržaj                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode datoteke za ispravljanje pogrešaka                   |
| `.aitk`      | Konfiguracija Microsoft Foundry Toolkita                     |
| `src`        | Izvorni kod za weather mcp server                             |

## Kako ispravljati pogreške Weather MCP Servera

> Bilješke:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualni razvojni alat za testiranje i ispravljanje pogrešaka MCP servera.
> - Svi načini ispravljanja pogrešaka podržavaju breakpointe, tako da možete dodati breakpointe u kod alata.

## Dostupni alati

### Weather Tool
Alat `get_weather` pruža lažne vremenske informacije za određenu lokaciju.

| Parametar | Tip | Opis |
| --------- | ---- | ----------- |
| `location` | string | Lokacija za koju se dobivaju vremenske informacije (npr. ime grada, država ili koordinate) |

### Git Clone Tool
Alat `git_clone_repo` klonira git repozitorij u određeni direktorij.

| Parametar | Tip | Opis |
| --------- | ---- | ----------- |
| `repo_url` | string | URL git repozitorija koji se klonira |
| `target_folder` | string | Putanja do direktorija u koji se repozitorij treba klonirati |

Alat vraća JSON objekt s:
- `success`: Boolean koji označava je li operacija bila uspješna
- `target_folder` ili `error`: Putanja kloniranog repozitorija ili poruka o pogrešci

### VS Code Open Tool
Alat `open_in_vscode` otvara direktorij u VS Code ili VS Code Insiders aplikaciji.

| Parametar | Tip | Opis |
| --------- | ---- | ----------- |
| `folder_path` | string | Putanja do direktorija koji se otvara |
| `use_insiders` | boolean (opcijski) | Treba li se koristiti VS Code Insiders umjesto običnog VS Code-a |

Alat vraća JSON objekt s:
- `success`: Boolean koji označava je li operacija bila uspješna
- `message` ili `error`: Poruka potvrde ili poruka o pogrešci

| Način ispravljanja | Opis | Koraci za ispravljanje pogrešaka |
| ---------- | ----------- | --------------- |
| Agent Builder | Ispravljanje pogrešaka MCP servera u Agent Builderu preko Microsoft Foundry Toolkita za Visual Studio Code. | 1. Otvorite VS Code Debug ploču. Odaberite `Debug in Agent Builder` i pritisnite `F5` za početak ispravljanja pogrešaka MCP servera.<br>2. Odaberite aktivnu Foundry distribuciju kao što je `gpt-5.1`, zatim unesite `What is the weather in Shanghai?`. Server će se automatski povezati.<br>3. Kliknite `Run` za testiranje servera s promptom. |
| MCP Inspector | Ispravljanje pogrešaka MCP servera korištenjem MCP Inspectora. | 1. Instalirajte [Node.js](https://nodejs.org/)<br> 2. Postavite Inspector: `cd inspector` && `npm install` <br> 3. Otvorite VS Code Debug ploču. Odaberite `Debug SSE in Inspector (Edge)` ili `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za početak ispravljanja pogrešaka.<br> 4. Kad se MCP Inspector pokrene u pregledniku, kliknite na gumb `Connect` za povezivanje ovog MCP servera.<br> 5. Tada možete `List Tools`, odabrati alat, unijeti parametre i `Run Tool` za ispravljanje koda servera.<br> |

## Zadani portovi i prilagodbe

| Način ispravljanja | Portovi | Definicije | Prilagodbe | Napomena |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za promjenu navedenih portova. | N/A |
| MCP Inspector | 3001 (Server); 5173 i 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za promjenu navedenih portova.| N/A |

## Povratne informacije

Ako imate povratne informacije ili prijedloge za ovaj predložak, otvorite problem na [Microsoft Foundry Toolkit for Visual Studio Code GitHub repozitoriju](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
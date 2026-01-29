# Weather MCP Server

Ovo je primjer MCP Servera u Pythonu koji implementira alate za vremensku prognozu s lažnim odgovorima. Može se koristiti kao osnova za vaš vlastiti MCP Server. Uključuje sljedeće značajke:

- **Alat za vremensku prognozu**: Alat koji pruža lažne informacije o vremenu na temelju zadane lokacije.
- **Alat za kloniranje Git repozitorija**: Alat koji klonira Git repozitorij u određenu mapu.
- **Alat za otvaranje u VS Code-u**: Alat koji otvara mapu u VS Code-u ili VS Code Insiders.
- **Povezivanje s Agent Builderom**: Značajka koja omogućuje povezivanje MCP servera s Agent Builderom za testiranje i otklanjanje pogrešaka.
- **Otklanjanje pogrešaka u [MCP Inspectoru](https://github.com/modelcontextprotocol/inspector)**: Značajka koja omogućuje otklanjanje pogrešaka MCP Servera pomoću MCP Inspectora.

## Početak rada s predloškom Weather MCP Servera

> **Preduvjeti**
>
> Za pokretanje MCP Servera na vašem lokalnom razvojnom računalu trebat će vam:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Potrebno za alat git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) ili [VS Code Insiders](https://code.visualstudio.com/insiders/) (Potrebno za alat open_in_vscode)
> - (*Opcionalno - ako preferirate uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Priprema okruženja

Postoje dva pristupa za postavljanje okruženja za ovaj projekt. Možete odabrati bilo koji na temelju svojih preferencija.

> Napomena: Ponovno učitajte VSCode ili terminal kako biste osigurali da se koristi Python iz virtualnog okruženja nakon što ga kreirate.

| Pristup | Koraci |
| ------- | ------ |
| Korištenje `uv` | 1. Kreirajte virtualno okruženje: `uv venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite Python iz kreiranog virtualnog okruženja <br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `uv pip install -r pyproject.toml --extra dev` |
| Korištenje `pip` | 1. Kreirajte virtualno okruženje: `python -m venv .venv` <br>2. Pokrenite VSCode naredbu "***Python: Select Interpreter***" i odaberite Python iz kreiranog virtualnog okruženja <br>3. Instalirajte ovisnosti (uključujući razvojne ovisnosti): `pip install -e .[dev]` |

Nakon postavljanja okruženja, možete pokrenuti server na svom lokalnom razvojnom računalu putem Agent Buildera kao MCP Klijenta za početak rada:
1. Otvorite VS Code Debug panel. Odaberite `Debug in Agent Builder` ili pritisnite `F5` za pokretanje otklanjanja pogrešaka MCP servera.
2. Koristite AI Toolkit Agent Builder za testiranje servera s [ovim upitom](../../../../../../../../../../../open_prompt_builder). Server će se automatski povezati s Agent Builderom.
3. Kliknite `Run` za testiranje servera s upitom.

**Čestitamo**! Uspješno ste pokrenuli Weather MCP Server na svom lokalnom razvojnom računalu putem Agent Buildera kao MCP Klijenta.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Što je uključeno u predložak

| Mapa / Datoteka | Sadržaj                                     |
| --------------- | ------------------------------------------- |
| `.vscode`       | VSCode datoteke za otklanjanje pogrešaka    |
| `.aitk`         | Konfiguracije za AI Toolkit                |
| `src`           | Izvorni kod za Weather MCP Server          |

## Kako otkloniti pogreške na Weather MCP Serveru

> Napomene:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizualni alat za razvoj za testiranje i otklanjanje pogrešaka MCP servera.
> - Svi načini otklanjanja pogrešaka podržavaju točke prekida, tako da možete dodati točke prekida u kod implementacije alata.

## Dostupni alati

### Alat za vremensku prognozu
Alat `get_weather` pruža lažne informacije o vremenu za određenu lokaciju.

| Parametar | Tip | Opis |
| --------- | ---- | ---- |
| `location` | string | Lokacija za koju se traži vremenska prognoza (npr. naziv grada, država ili koordinate) |

### Alat za kloniranje Git repozitorija
Alat `git_clone_repo` klonira Git repozitorij u određenu mapu.

| Parametar | Tip | Opis |
| --------- | ---- | ---- |
| `repo_url` | string | URL Git repozitorija koji se klonira |
| `target_folder` | string | Putanja do mape u koju se repozitorij treba klonirati |

Alat vraća JSON objekt s:
- `success`: Boolean koji označava je li operacija bila uspješna
- `target_folder` ili `error`: Putanja kloniranog repozitorija ili poruka o pogrešci

### Alat za otvaranje u VS Code-u
Alat `open_in_vscode` otvara mapu u aplikaciji VS Code ili VS Code Insiders.

| Parametar | Tip | Opis |
| --------- | ---- | ---- |
| `folder_path` | string | Putanja do mape koja se otvara |
| `use_insiders` | boolean (opcionalno) | Koristi li se VS Code Insiders umjesto običnog VS Code-a |

Alat vraća JSON objekt s:
- `success`: Boolean koji označava je li operacija bila uspješna
- `message` ili `error`: Poruka potvrde ili poruka o pogrešci

| Način otklanjanja pogrešaka | Opis | Koraci za otklanjanje pogrešaka |
| --------------------------- | ---- | ------------------------------ |
| Agent Builder | Otklanjanje pogrešaka MCP servera u Agent Builderu putem AI Toolkita. | 1. Otvorite VS Code Debug panel. Odaberite `Debug in Agent Builder` i pritisnite `F5` za pokretanje otklanjanja pogrešaka MCP servera.<br>2. Koristite AI Toolkit Agent Builder za testiranje servera s [ovim upitom](../../../../../../../../../../../open_prompt_builder). Server će se automatski povezati s Agent Builderom.<br>3. Kliknite `Run` za testiranje servera s upitom. |
| MCP Inspector | Otklanjanje pogrešaka MCP servera pomoću MCP Inspectora. | 1. Instalirajte [Node.js](https://nodejs.org/)<br> 2. Postavite Inspector: `cd inspector` && `npm install` <br> 3. Otvorite VS Code Debug panel. Odaberite `Debug SSE in Inspector (Edge)` ili `Debug SSE in Inspector (Chrome)`. Pritisnite F5 za pokretanje otklanjanja pogrešaka.<br> 4. Kada MCP Inspector pokrene u pregledniku, kliknite gumb `Connect` za povezivanje ovog MCP servera.<br> 5. Zatim možete `List Tools`, odabrati alat, unijeti parametre i `Run Tool` za otklanjanje pogrešaka u kodu servera.<br> |

## Zadani portovi i prilagodbe

| Način otklanjanja pogrešaka | Portovi | Definicije | Prilagodbe | Napomena |
| --------------------------- | ------- | ---------- | ---------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za promjenu gore navedenih portova. | N/A |
| MCP Inspector | 3001 (Server); 5173 i 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Uredite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) za promjenu gore navedenih portova. | N/A |

## Povratne informacije

Ako imate povratne informacije ili prijedloge za ovaj predložak, otvorite problem na [AI Toolkit GitHub repozitoriju](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
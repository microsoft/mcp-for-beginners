# Server MCP Meteo

Acesta este un exemplu de server MCP în Python care implementează instrumente meteo cu răspunsuri simulate. Poate fi utilizat ca bază pentru propriul server MCP. Include următoarele funcționalități:

- **Instrument Meteo**: Un instrument care oferă informații meteo simulate pe baza locației specificate.
- **Instrument Clonare Git**: Un instrument care clonează un depozit git într-un folder specificat.
- **Instrument Deschidere VS Code**: Un instrument care deschide un folder în VS Code sau VS Code Insiders.
- **Conectare la Agent Builder**: O funcționalitate care permite conectarea serverului MCP la Agent Builder pentru testare și depanare.
- **Depanare în [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: O funcționalitate care permite depanarea serverului MCP utilizând MCP Inspector.

## Începeți cu șablonul Server MCP Meteo

> **Prerechizite**
>
> Pentru a rula serverul MCP pe mașina dvs. de dezvoltare locală, veți avea nevoie de:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Necesar pentru instrumentul git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) sau [VS Code Insiders](https://code.visualstudio.com/insiders/) (Necesar pentru instrumentul open_in_vscode)
> - (*Opțional - dacă preferați uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensia Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Pregătirea mediului

Există două abordări pentru configurarea mediului pentru acest proiect. Puteți alege oricare dintre ele, în funcție de preferințele dvs.

> Notă: Reîncărcați VSCode sau terminalul pentru a vă asigura că python-ul din mediul virtual este utilizat după crearea mediului virtual.

| Abordare | Pași |
| -------- | ----- |
| Utilizând `uv` | 1. Creați mediul virtual: `uv venv` <br>2. Rulați comanda VSCode "***Python: Select Interpreter***" și selectați python-ul din mediul virtual creat <br>3. Instalați dependențele (inclusiv dependențele de dezvoltare): `uv pip install -r pyproject.toml --extra dev` |
| Utilizând `pip` | 1. Creați mediul virtual: `python -m venv .venv` <br>2. Rulați comanda VSCode "***Python: Select Interpreter***" și selectați python-ul din mediul virtual creat<br>3. Instalați dependențele (inclusiv dependențele de dezvoltare): `pip install -e .[dev]` | 

După configurarea mediului, puteți rula serverul pe mașina dvs. de dezvoltare locală prin Agent Builder ca MCP Client pentru a începe:
1. Deschideți panoul de depanare din VS Code. Selectați `Debug in Agent Builder` sau apăsați `F5` pentru a începe depanarea serverului MCP.
2. Utilizați AI Toolkit Agent Builder pentru a testa serverul cu [acest prompt](../../../../../../../../../../../open_prompt_builder). Serverul va fi conectat automat la Agent Builder.
3. Apăsați `Run` pentru a testa serverul cu promptul.

**Felicitări**! Ați rulat cu succes serverul MCP Meteo pe mașina dvs. de dezvoltare locală prin Agent Builder ca MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Ce este inclus în șablon

| Folder / Fișier | Conținut                                     |
| ---------------- | -------------------------------------------- |
| `.vscode`        | Fișiere VSCode pentru depanare               |
| `.aitk`          | Configurații pentru AI Toolkit               |
| `src`            | Codul sursă pentru serverul MCP Meteo        |

## Cum să depanați serverul MCP Meteo

> Note:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) este un instrument vizual pentru dezvoltatori destinat testării și depanării serverelor MCP.
> - Toate modurile de depanare suportă puncte de întrerupere, astfel încât să puteți adăuga puncte de întrerupere în codul de implementare al instrumentului.

## Instrumente disponibile

### Instrument Meteo
Instrumentul `get_weather` oferă informații meteo simulate pentru o locație specificată.

| Parametru | Tip | Descriere |
| --------- | ---- | ----------- |
| `location` | string | Locația pentru care se dorește informația meteo (de exemplu, numele orașului, statul sau coordonatele) |

### Instrument Clonare Git
Instrumentul `git_clone_repo` clonează un depozit git într-un folder specificat.

| Parametru | Tip | Descriere |
| --------- | ---- | ----------- |
| `repo_url` | string | URL-ul depozitului git care trebuie clonat |
| `target_folder` | string | Calea către folderul unde ar trebui clonat depozitul |

Instrumentul returnează un obiect JSON cu:
- `success`: Boolean care indică dacă operațiunea a fost realizată cu succes
- `target_folder` sau `error`: Calea depozitului clonat sau un mesaj de eroare

### Instrument Deschidere VS Code
Instrumentul `open_in_vscode` deschide un folder în aplicația VS Code sau VS Code Insiders.

| Parametru | Tip | Descriere |
| --------- | ---- | ----------- |
| `folder_path` | string | Calea către folderul care trebuie deschis |
| `use_insiders` | boolean (opțional) | Dacă se utilizează VS Code Insiders în loc de VS Code obișnuit |

Instrumentul returnează un obiect JSON cu:
- `success`: Boolean care indică dacă operațiunea a fost realizată cu succes
- `message` sau `error`: Un mesaj de confirmare sau un mesaj de eroare

| Mod de depanare | Descriere | Pași pentru depanare |
| ---------------- | ----------- | ------------------- |
| Agent Builder | Depanați serverul MCP în Agent Builder prin AI Toolkit. | 1. Deschideți panoul de depanare din VS Code. Selectați `Debug in Agent Builder` și apăsați `F5` pentru a începe depanarea serverului MCP.<br>2. Utilizați AI Toolkit Agent Builder pentru a testa serverul cu [acest prompt](../../../../../../../../../../../open_prompt_builder). Serverul va fi conectat automat la Agent Builder.<br>3. Apăsați `Run` pentru a testa serverul cu promptul. |
| MCP Inspector | Depanați serverul MCP utilizând MCP Inspector. | 1. Instalați [Node.js](https://nodejs.org/)<br> 2. Configurați Inspector: `cd inspector` && `npm install` <br> 3. Deschideți panoul de depanare din VS Code. Selectați `Debug SSE in Inspector (Edge)` sau `Debug SSE in Inspector (Chrome)`. Apăsați F5 pentru a începe depanarea.<br> 4. Când MCP Inspector se lansează în browser, apăsați butonul `Connect` pentru a conecta acest server MCP.<br> 5. Apoi puteți `List Tools`, selectați un instrument, introduceți parametrii și `Run Tool` pentru a depana codul serverului.<br> |

## Porturi implicite și personalizări

| Mod de depanare | Porturi | Definiții | Personalizări | Notă |
| ---------------- | ------- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Editați [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pentru a modifica porturile de mai sus. | N/A |
| MCP Inspector | 3001 (Server); 5173 și 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Editați [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pentru a modifica porturile de mai sus.| N/A |

## Feedback

Dacă aveți feedback sau sugestii pentru acest șablon, vă rugăm să deschideți o problemă pe [repository-ul GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
# Weather MCP Server

Acesta este un exemplu de MCP Server în Python care implementează unelte meteo cu răspunsuri simulate. Poate fi folosit ca schelet pentru propriul tău MCP Server. Include următoarele funcționalități:

- **Weather Tool**: O unealtă care oferă informații meteo simulate bazate pe locația dată.
- **Conectare la Agent Builder**: O funcție care îți permite să conectezi MCP serverul la Agent Builder pentru testare și depanare.
- **Depanare în [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: O funcție care îți permite să depanezi MCP Serverul folosind MCP Inspector.

## Începe cu șablonul Weather MCP Server

> **Prerechizite**
>
> Pentru a rula MCP Serverul pe mașina ta locală de dezvoltare, vei avea nevoie de:
>
> - [Python](https://www.python.org/)
> - (*Opțional - dacă preferi uv*) [uv](https://github.com/astral-sh/uv)
> - [Extensia Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Pregătirea mediului

Există două metode pentru a configura mediul pentru acest proiect. Poți alege oricare dintre ele, în funcție de preferințe.

> Notă: Reîncarcă VSCode sau terminalul pentru a te asigura că este folosit python-ul din mediul virtual după crearea acestuia.

| Metodă | Pași |
| -------- | ----- |
| Folosind `uv` | 1. Creează mediul virtual: `uv venv` <br>2. Rulează comanda VSCode "***Python: Select Interpreter***" și selectează python-ul din mediul virtual creat <br>3. Instalează dependențele (inclusiv cele de dezvoltare): `uv pip install -r pyproject.toml --extra dev` |
| Folosind `pip` | 1. Creează mediul virtual: `python -m venv .venv` <br>2. Rulează comanda VSCode "***Python: Select Interpreter***" și selectează python-ul din mediul virtual creat<br>3. Instalează dependențele (inclusiv cele de dezvoltare): `pip install -e .[dev]` |

După configurarea mediului, poți rula serverul pe mașina ta locală de dezvoltare prin Agent Builder ca MCP Client pentru a începe:
1. Deschide panoul de Debug din VS Code. Selectează `Debug in Agent Builder` sau apasă `F5` pentru a începe depanarea MCP serverului.
2. Folosește AI Toolkit Agent Builder pentru a testa serverul cu [acest prompt](../../../../../../../../../../open_prompt_builder). Serverul se va conecta automat la Agent Builder.
3. Apasă `Run` pentru a testa serverul cu promptul.

**Felicitări**! Ai rulat cu succes Weather MCP Server pe mașina ta locală de dezvoltare prin Agent Builder ca MCP Client.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Ce include șablonul

| Folder / Fișier | Conținut                                  |
| --------------- | ----------------------------------------- |
| `.vscode`       | Fișiere VSCode pentru depanare            |
| `.aitk`         | Configurări pentru AI Toolkit              |
| `src`           | Codul sursă pentru weather mcp server     |

## Cum să depanezi Weather MCP Server

> Note:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) este un instrument vizual pentru dezvoltatori, destinat testării și depanării serverelor MCP.
> - Toate modurile de depanare suportă puncte de întrerupere, astfel încât poți adăuga breakpoint-uri în codul de implementare al uneltei.

| Mod de depanare | Descriere | Pași pentru depanare |
| --------------- | --------- | -------------------- |
| Agent Builder | Depanează MCP serverul în Agent Builder prin AI Toolkit. | 1. Deschide panoul de Debug din VS Code. Selectează `Debug in Agent Builder` și apasă `F5` pentru a începe depanarea MCP serverului.<br>2. Folosește AI Toolkit Agent Builder pentru a testa serverul cu [acest prompt](../../../../../../../../../../open_prompt_builder). Serverul se va conecta automat la Agent Builder.<br>3. Apasă `Run` pentru a testa serverul cu promptul. |
| MCP Inspector | Depanează MCP serverul folosind MCP Inspector. | 1. Instalează [Node.js](https://nodejs.org/)<br> 2. Configurează Inspector: `cd inspector` && `npm install` <br> 3. Deschide panoul de Debug din VS Code. Selectează `Debug SSE in Inspector (Edge)` sau `Debug SSE in Inspector (Chrome)`. Apasă F5 pentru a începe depanarea.<br> 4. Când MCP Inspector se deschide în browser, apasă butonul `Connect` pentru a conecta acest MCP server.<br> 5. Apoi poți `List Tools`, selecta o unealtă, introduce parametrii și `Run Tool` pentru a depana codul serverului.<br> |

## Porturi implicite și personalizări

| Mod de depanare | Porturi | Definiții | Personalizări | Notă |
| --------------- | ------- | --------- | ------------- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Editează [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pentru a schimba porturile de mai sus. | N/A |
| MCP Inspector | 3001 (Server); 5173 și 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Editează [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pentru a schimba porturile de mai sus. | N/A |

## Feedback

Dacă ai feedback sau sugestii pentru acest șablon, te rugăm să deschizi un issue pe [repository-ul AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
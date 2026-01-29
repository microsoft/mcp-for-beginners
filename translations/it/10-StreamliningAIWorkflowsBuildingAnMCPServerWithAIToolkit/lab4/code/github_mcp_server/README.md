# Weather MCP Server

Questo è un esempio di MCP Server in Python che implementa strumenti meteo con risposte simulate. Può essere utilizzato come base per il tuo MCP Server. Include le seguenti funzionalità:

- **Strumento Meteo**: Uno strumento che fornisce informazioni meteo simulate basate sulla posizione fornita.
- **Strumento Clonazione Git**: Uno strumento che clona un repository git in una cartella specificata.
- **Strumento Apertura VS Code**: Uno strumento che apre una cartella in VS Code o VS Code Insiders.
- **Connessione a Agent Builder**: Una funzionalità che consente di collegare il server MCP a Agent Builder per test e debug.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Una funzionalità che consente di eseguire il debug del server MCP utilizzando MCP Inspector.

## Inizia con il template Weather MCP Server

> **Prerequisiti**
>
> Per eseguire il MCP Server sulla tua macchina di sviluppo locale, avrai bisogno di:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Richiesto per lo strumento git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) o [VS Code Insiders](https://code.visualstudio.com/insiders/) (Richiesto per lo strumento open_in_vscode)
> - (*Opzionale - se preferisci uv*) [uv](https://github.com/astral-sh/uv)
> - [Estensione Debugger Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepara l'ambiente

Ci sono due approcci per configurare l'ambiente per questo progetto. Puoi scegliere quello che preferisci.

> Nota: Ricarica VSCode o il terminale per assicurarti che venga utilizzato il Python dell'ambiente virtuale dopo averlo creato.

| Approccio | Passaggi |
| --------- | -------- |
| Usando `uv` | 1. Crea un ambiente virtuale: `uv venv` <br>2. Esegui il comando di VSCode "***Python: Select Interpreter***" e seleziona il Python dall'ambiente virtuale creato <br>3. Installa le dipendenze (incluse le dipendenze di sviluppo): `uv pip install -r pyproject.toml --extra dev` |
| Usando `pip` | 1. Crea un ambiente virtuale: `python -m venv .venv` <br>2. Esegui il comando di VSCode "***Python: Select Interpreter***" e seleziona il Python dall'ambiente virtuale creato <br>3. Installa le dipendenze (incluse le dipendenze di sviluppo): `pip install -e .[dev]` |

Dopo aver configurato l'ambiente, puoi eseguire il server sulla tua macchina di sviluppo locale tramite Agent Builder come MCP Client per iniziare:
1. Apri il pannello di debug di VS Code. Seleziona `Debug in Agent Builder` o premi `F5` per avviare il debug del server MCP.
2. Usa AI Toolkit Agent Builder per testare il server con [questo prompt](../../../../../../../../../../../open_prompt_builder). Il server sarà automaticamente connesso a Agent Builder.
3. Clicca su `Run` per testare il server con il prompt.

**Congratulazioni**! Hai eseguito con successo il Weather MCP Server sulla tua macchina di sviluppo locale tramite Agent Builder come MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Cosa è incluso nel template

| Cartella / File | Contenuti                                   |
| --------------- | ------------------------------------------- |
| `.vscode`       | File VSCode per il debug                   |
| `.aitk`         | Configurazioni per AI Toolkit              |
| `src`           | Il codice sorgente per il server MCP meteo |

## Come eseguire il debug del Weather MCP Server

> Note:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) è uno strumento visivo per sviluppatori per testare e fare il debug dei server MCP.
> - Tutte le modalità di debug supportano i breakpoint, quindi puoi aggiungere breakpoint al codice di implementazione dello strumento.

## Strumenti disponibili

### Strumento Meteo
Lo strumento `get_weather` fornisce informazioni meteo simulate per una posizione specificata.

| Parametro  | Tipo   | Descrizione                                      |
| ---------- | ------ | ------------------------------------------------ |
| `location` | string | Posizione per cui ottenere le informazioni meteo (es. nome della città, stato o coordinate) |

### Strumento Clonazione Git
Lo strumento `git_clone_repo` clona un repository git in una cartella specificata.

| Parametro       | Tipo   | Descrizione                                      |
| --------------- | ------ | ------------------------------------------------ |
| `repo_url`      | string | URL del repository git da clonare                |
| `target_folder` | string | Percorso della cartella dove il repository sarà clonato |

Lo strumento restituisce un oggetto JSON con:
- `success`: Booleano che indica se l'operazione è stata completata con successo
- `target_folder` o `error`: Il percorso del repository clonato o un messaggio di errore

### Strumento Apertura VS Code
Lo strumento `open_in_vscode` apre una cartella nell'applicazione VS Code o VS Code Insiders.

| Parametro      | Tipo    | Descrizione                                      |
| -------------- | ------- | ------------------------------------------------ |
| `folder_path`  | string  | Percorso della cartella da aprire                |
| `use_insiders` | boolean (opzionale) | Indica se utilizzare VS Code Insiders invece di VS Code normale |

Lo strumento restituisce un oggetto JSON con:
- `success`: Booleano che indica se l'operazione è stata completata con successo
- `message` o `error`: Un messaggio di conferma o un messaggio di errore

| Modalità di Debug | Descrizione | Passaggi per il debug |
| ----------------- | ----------- | --------------------- |
| Agent Builder     | Esegui il debug del server MCP in Agent Builder tramite AI Toolkit. | 1. Apri il pannello di debug di VS Code. Seleziona `Debug in Agent Builder` e premi `F5` per avviare il debug del server MCP.<br>2. Usa AI Toolkit Agent Builder per testare il server con [questo prompt](../../../../../../../../../../../open_prompt_builder). Il server sarà automaticamente connesso a Agent Builder.<br>3. Clicca su `Run` per testare il server con il prompt. |
| MCP Inspector     | Esegui il debug del server MCP utilizzando MCP Inspector. | 1. Installa [Node.js](https://nodejs.org/)<br> 2. Configura Inspector: `cd inspector` && `npm install` <br> 3. Apri il pannello di debug di VS Code. Seleziona `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Premi F5 per avviare il debug.<br> 4. Quando MCP Inspector si avvia nel browser, clicca sul pulsante `Connect` per connettere questo server MCP.<br> 5. Poi puoi `List Tools`, selezionare uno strumento, inserire i parametri e `Run Tool` per eseguire il debug del codice del server.<br> |

## Porte predefinite e personalizzazioni

| Modalità di Debug | Porte | Definizioni | Personalizzazioni | Nota |
| ----------------- | ----- | ----------- | ----------------- | ---- |
| Agent Builder     | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Modifica [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) per cambiare le porte sopra indicate. | N/A |
| MCP Inspector     | 3001 (Server); 5173 e 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Modifica [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) per cambiare le porte sopra indicate. | N/A |

## Feedback

Se hai feedback o suggerimenti per questo template, apri un problema sul [repository GitHub di AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
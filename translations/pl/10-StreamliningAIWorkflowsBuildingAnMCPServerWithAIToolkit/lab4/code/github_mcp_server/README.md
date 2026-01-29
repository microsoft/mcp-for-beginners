# Serwer MCP Pogoda

To przykładowy serwer MCP napisany w Pythonie, który implementuje narzędzia pogodowe z odpowiedziami testowymi. Może być używany jako szkielet do stworzenia własnego serwera MCP. Obejmuje następujące funkcje:

- **Narzędzie Pogoda**: Narzędzie dostarczające testowe informacje pogodowe na podstawie podanej lokalizacji.
- **Narzędzie Klonowanie Git**: Narzędzie, które klonuje repozytorium git do określonego folderu.
- **Narzędzie Otwórz w VS Code**: Narzędzie, które otwiera folder w aplikacji VS Code lub VS Code Insiders.
- **Połącz z Agent Builder**: Funkcja umożliwiająca połączenie serwera MCP z Agent Builder w celu testowania i debugowania.
- **Debugowanie w [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcja umożliwiająca debugowanie serwera MCP za pomocą MCP Inspector.

## Rozpocznij pracę z szablonem serwera MCP Pogoda

> **Wymagania wstępne**
>
> Aby uruchomić serwer MCP na lokalnym komputerze deweloperskim, potrzebujesz:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Wymagane dla narzędzia git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) lub [VS Code Insiders](https://code.visualstudio.com/insiders/) (Wymagane dla narzędzia open_in_vscode)
> - (*Opcjonalnie - jeśli preferujesz uv*) [uv](https://github.com/astral-sh/uv)
> - [Rozszerzenie Debuggera Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Przygotowanie środowiska

Istnieją dwa podejścia do skonfigurowania środowiska dla tego projektu. Możesz wybrać dowolne z nich w zależności od swoich preferencji.

> Uwaga: Po utworzeniu wirtualnego środowiska zrestartuj VSCode lub terminal, aby upewnić się, że używany jest Python z wirtualnego środowiska.

| Podejście | Kroki |
| --------- | ----- |
| Korzystanie z `uv` | 1. Utwórz wirtualne środowisko: `uv venv` <br>2. Uruchom polecenie VSCode "***Python: Select Interpreter***" i wybierz Pythona z utworzonego wirtualnego środowiska <br>3. Zainstaluj zależności (w tym zależności deweloperskie): `uv pip install -r pyproject.toml --extra dev` |
| Korzystanie z `pip` | 1. Utwórz wirtualne środowisko: `python -m venv .venv` <br>2. Uruchom polecenie VSCode "***Python: Select Interpreter***" i wybierz Pythona z utworzonego wirtualnego środowiska<br>3. Zainstaluj zależności (w tym zależności deweloperskie): `pip install -e .[dev]` | 

Po skonfigurowaniu środowiska możesz uruchomić serwer na lokalnym komputerze deweloperskim za pomocą Agent Builder jako klienta MCP, aby rozpocząć:
1. Otwórz panel debugowania w VS Code. Wybierz `Debug in Agent Builder` lub naciśnij `F5`, aby rozpocząć debugowanie serwera MCP.
2. Użyj AI Toolkit Agent Builder, aby przetestować serwer za pomocą [tego promptu](../../../../../../../../../../../open_prompt_builder). Serwer zostanie automatycznie połączony z Agent Builder.
3. Kliknij `Run`, aby przetestować serwer za pomocą promptu.

**Gratulacje**! Pomyślnie uruchomiłeś serwer MCP Pogoda na lokalnym komputerze deweloperskim za pomocą Agent Builder jako klienta MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Co zawiera szablon

| Folder / Plik | Zawartość                                     |
| ------------- | --------------------------------------------- |
| `.vscode`     | Pliki VSCode do debugowania                   |
| `.aitk`       | Konfiguracje dla AI Toolkit                   |
| `src`         | Kod źródłowy serwera MCP Pogoda               |

## Jak debugować serwer MCP Pogoda

> Uwagi:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) to wizualne narzędzie deweloperskie do testowania i debugowania serwerów MCP.
> - Wszystkie tryby debugowania obsługują punkty przerwania, więc możesz dodawać punkty przerwania do kodu implementacji narzędzi.

## Dostępne narzędzia

### Narzędzie Pogoda
Narzędzie `get_weather` dostarcza testowe informacje pogodowe dla określonej lokalizacji.

| Parametr   | Typ    | Opis                                   |
| ---------- | ------ | -------------------------------------- |
| `location` | string | Lokalizacja, dla której chcesz uzyskać informacje pogodowe (np. nazwa miasta, stan lub współrzędne) |

### Narzędzie Klonowanie Git
Narzędzie `git_clone_repo` klonuje repozytorium git do określonego folderu.

| Parametr        | Typ    | Opis                                           |
| --------------- | ------ | ---------------------------------------------- |
| `repo_url`      | string | URL repozytorium git, które ma zostać sklonowane |
| `target_folder` | string | Ścieżka do folderu, w którym repozytorium ma zostać sklonowane |

Narzędzie zwraca obiekt JSON zawierający:
- `success`: Wartość logiczna wskazująca, czy operacja zakończyła się sukcesem
- `target_folder` lub `error`: Ścieżka do sklonowanego repozytorium lub komunikat o błędzie

### Narzędzie Otwórz w VS Code
Narzędzie `open_in_vscode` otwiera folder w aplikacji VS Code lub VS Code Insiders.

| Parametr       | Typ    | Opis                                           |
| -------------- | ------ | ---------------------------------------------- |
| `folder_path`  | string | Ścieżka do folderu, który ma zostać otwarty    |
| `use_insiders` | boolean (opcjonalny) | Czy użyć VS Code Insiders zamiast zwykłego VS Code |

Narzędzie zwraca obiekt JSON zawierający:
- `success`: Wartość logiczna wskazująca, czy operacja zakończyła się sukcesem
- `message` lub `error`: Potwierdzenie lub komunikat o błędzie

| Tryb debugowania | Opis | Kroki debugowania |
| ---------------- | ---- | ----------------- |
| Agent Builder    | Debugowanie serwera MCP w Agent Builder za pomocą AI Toolkit. | 1. Otwórz panel debugowania w VS Code. Wybierz `Debug in Agent Builder` i naciśnij `F5`, aby rozpocząć debugowanie serwera MCP.<br>2. Użyj AI Toolkit Agent Builder, aby przetestować serwer za pomocą [tego promptu](../../../../../../../../../../../open_prompt_builder). Serwer zostanie automatycznie połączony z Agent Builder.<br>3. Kliknij `Run`, aby przetestować serwer za pomocą promptu. |
| MCP Inspector    | Debugowanie serwera MCP za pomocą MCP Inspector. | 1. Zainstaluj [Node.js](https://nodejs.org/)<br> 2. Skonfiguruj Inspector: `cd inspector` && `npm install` <br> 3. Otwórz panel debugowania w VS Code. Wybierz `Debug SSE in Inspector (Edge)` lub `Debug SSE in Inspector (Chrome)`. Naciśnij F5, aby rozpocząć debugowanie.<br> 4. Gdy MCP Inspector uruchomi się w przeglądarce, kliknij przycisk `Connect`, aby połączyć ten serwer MCP.<br> 5. Następnie możesz `List Tools`, wybrać narzędzie, wprowadzić parametry i `Run Tool`, aby debugować kod serwera.<br> |

## Domyślne porty i dostosowania

| Tryb debugowania | Porty | Definicje | Dostosowania | Uwagi |
| ---------------- | ----- | --------- | ------------ |------- |
| Agent Builder    | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edytuj [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), aby zmienić powyższe porty. | N/A |
| MCP Inspector    | 3001 (Serwer); 5173 i 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edytuj [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), aby zmienić powyższe porty.| N/A |

## Opinie

Jeśli masz jakiekolwiek uwagi lub sugestie dotyczące tego szablonu, otwórz zgłoszenie w [repozytorium GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
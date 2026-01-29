# 🔧 Moduł 3: Zaawansowany rozwój MCP z AI Toolkit

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Cele nauki

Po ukończeniu tego laboratorium będziesz potrafił:

- ✅ Tworzyć niestandardowe serwery MCP za pomocą AI Toolkit
- ✅ Konfigurować i korzystać z najnowszego MCP Python SDK (v1.9.3)
- ✅ Ustawiać i wykorzystywać MCP Inspector do debugowania
- ✅ Debugować serwery MCP zarówno w Agent Builder, jak i w Inspector
- ✅ Zrozumieć zaawansowane procesy tworzenia serwerów MCP

## 📋 Wymagania wstępne

- Ukończenie Laboratorium 2 (Podstawy MCP)
- VS Code z zainstalowanym rozszerzeniem AI Toolkit
- Środowisko Python 3.10+
- Node.js i npm do konfiguracji Inspector

## 🏗️ Co zbudujesz

W tym laboratorium stworzysz **Weather MCP Server**, który pokaże:
- Niestandardową implementację serwera MCP
- Integrację z AI Toolkit Agent Builder
- Profesjonalne procesy debugowania
- Nowoczesne wzorce użycia MCP SDK

---

## 🔧 Przegląd kluczowych komponentów

### 🐍 MCP Python SDK
Model Context Protocol Python SDK stanowi podstawę do tworzenia niestandardowych serwerów MCP. Użyjesz wersji 1.9.3 z rozszerzonymi możliwościami debugowania.

### 🔍 MCP Inspector
Potężne narzędzie do debugowania, które oferuje:
- Monitorowanie serwera w czasie rzeczywistym
- Wizualizację wykonywania narzędzi
- Inspekcję żądań i odpowiedzi sieciowych
- Interaktywne środowisko testowe

---

## 📖 Implementacja krok po kroku

### Krok 1: Utwórz WeatherAgent w Agent Builder

1. **Uruchom Agent Builder** w VS Code przez rozszerzenie AI Toolkit
2. **Stwórz nowego agenta** z następującą konfiguracją:
   - Nazwa agenta: `WeatherAgent`

![Agent Creation](../../../../translated_images/pl/Agent.c9c33f6a412b4cdedfb973fe5448bdb33de3f400055603111b875610e9b917ab.png)

### Krok 2: Zainicjuj projekt serwera MCP

1. **Przejdź do Tools** → **Add Tool** w Agent Builder
2. **Wybierz "MCP Server"** z dostępnych opcji
3. **Wybierz "Create A new MCP Server"**
4. **Wybierz szablon `python-weather`**
5. **Nazwij swój serwer:** `weather_mcp`

![Python Template Selection](../../../../translated_images/pl/Pythontemplate.9d0a2913c6491500bd673430f024dc44676af2808a27b5da9dcc0eb7063adc28.png)

### Krok 3: Otwórz i przeanalizuj projekt

1. **Otwórz wygenerowany projekt** w VS Code
2. **Przejrzyj strukturę projektu:**
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### Krok 4: Uaktualnij do najnowszego MCP SDK

> **🔍 Dlaczego aktualizacja?** Chcemy korzystać z najnowszego MCP SDK (v1.9.3) oraz usługi Inspector (0.14.0) dla lepszych funkcji i możliwości debugowania.

#### 4a. Aktualizacja zależności Pythona

**Edytuj `pyproject.toml`:** aktualizacja [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4b. Aktualizacja konfiguracji Inspector

**Edytuj `inspector/package.json`:** aktualizacja [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Aktualizacja zależności Inspector

**Edytuj `inspector/package-lock.json`:** aktualizacja [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Uwaga:** Ten plik zawiera rozbudowane definicje zależności. Poniżej znajduje się podstawowa struktura – pełna zawartość zapewnia prawidłowe rozwiązywanie zależności.

> **⚡ Pełny package-lock:** Kompletny package-lock.json zawiera około 3000 linii definicji zależności. Powyżej pokazano kluczową strukturę – użyj dostarczonego pliku dla pełnego rozwiązywania zależności.

### Krok 5: Konfiguracja debugowania w VS Code

*Uwaga: Skopiuj plik w podanej ścieżce, aby zastąpić odpowiadający lokalny plik*

#### 5a. Aktualizacja konfiguracji uruchamiania

**Edytuj `.vscode/launch.json`:**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**Edytuj `.vscode/tasks.json`:**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```

---

## 🚀 Uruchamianie i testowanie serwera MCP

### Krok 6: Instalacja zależności

Po wprowadzeniu zmian konfiguracyjnych uruchom następujące polecenia:

**Zainstaluj zależności Pythona:**
```bash
uv sync
```

**Zainstaluj zależności Inspector:**
```bash
cd inspector
npm install
```

### Krok 7: Debugowanie w Agent Builder

1. **Naciśnij F5** lub wybierz konfigurację **"Debug in Agent Builder"**
2. **Wybierz konfigurację compound** z panelu debugowania
3. **Poczekaj na uruchomienie serwera** i otwarcie Agent Builder
4. **Przetestuj swój serwer weather MCP** za pomocą zapytań w języku naturalnym

Wprowadź zapytanie takie jak poniżej

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/pl/Result.6ac570f7d2b1d5389c561ab0566970fe0f13e75bdd976b6a7f0270bc715d07f8.png)

### Krok 8: Debugowanie z MCP Inspector

1. **Użyj konfiguracji "Debug in Inspector"** (Edge lub Chrome)
2. **Otwórz interfejs Inspector** pod adresem `http://localhost:6274`
3. **Eksploruj interaktywne środowisko testowe:**
   - Przeglądaj dostępne narzędzia
   - Testuj wykonanie narzędzi
   - Monitoruj żądania sieciowe
   - Debuguj odpowiedzi serwera

![MCP Inspector Interface](../../../../translated_images/pl/Inspector.5672415cd02fe8731774586cc0a1083e3275d2f8491602aecc8ac4d61f2c0d57.png)

---

## 🎯 Kluczowe efekty nauki

Po ukończeniu tego laboratorium:

- [x] **Stworzyłeś niestandardowy serwer MCP** korzystając z szablonów AI Toolkit
- [x] **Zaktualizowałeś do najnowszego MCP SDK** (v1.9.3) dla rozszerzonej funkcjonalności
- [x] **Skonfigurowałeś profesjonalne procesy debugowania** dla Agent Builder i Inspector
- [x] **Ustawiłeś MCP Inspector** do interaktywnego testowania serwera
- [x] **Opanowałeś konfiguracje debugowania w VS Code** dla rozwoju MCP

## 🔧 Zaawansowane funkcje, które poznano

| Funkcja | Opis | Przykład użycia |
|---------|-------|-----------------|
| **MCP Python SDK v1.9.3** | Najnowsza implementacja protokołu | Nowoczesny rozwój serwera |
| **MCP Inspector 0.14.0** | Interaktywne narzędzie do debugowania | Testowanie serwera w czasie rzeczywistym |
| **Debugowanie w VS Code** | Zintegrowane środowisko programistyczne | Profesjonalny proces debugowania |
| **Integracja z Agent Builder** | Bezpośrednie połączenie z AI Toolkit | Kompleksowe testowanie agenta |

## 📚 Dodatkowe materiały

- [MCP Python SDK Documentation](https://modelcontextprotocol.io/docs/sdk/python)
- [AI Toolkit Extension Guide](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code Debugging Documentation](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Gratulacje!** Ukończyłeś Laboratorium 3 i teraz potrafisz tworzyć, debugować oraz wdrażać niestandardowe serwery MCP korzystając z profesjonalnych procesów rozwojowych.

### 🔜 Przejdź do następnego modułu

Gotowy, by zastosować swoje umiejętności MCP w praktycznym środowisku? Kontynuuj do **[Modułu 4: Praktyczny rozwój MCP - niestandardowy serwer klonowania GitHub](../lab4/README.md)**, gdzie:
- Zbudujesz produkcyjny serwer MCP automatyzujący operacje na repozytoriach GitHub
- Wdrożysz funkcjonalność klonowania repozytoriów GitHub przez MCP
- Zintegrujesz niestandardowe serwery MCP z VS Code i trybem agenta GitHub Copilot
- Przetestujesz i wdrożysz niestandardowe serwery MCP w środowiskach produkcyjnych
- Nauczysz się praktycznej automatyzacji procesów dla programistów

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
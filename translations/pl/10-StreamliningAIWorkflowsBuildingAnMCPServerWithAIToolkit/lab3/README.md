# 🔧 Moduł 3: Zaawansowany rozwój MCP z Microsoft Foundry Toolkit

> [!NOTE]
> Adresy URL Inspektora w tym laboratorium używają przestarzałego punktu końcowego `/sse` i celują w
> przypięte zależności MCP SDK `1.9.3` oraz Inspektora `0.14.0`. Nie są to
> aktualne przykłady Streamable HTTP na `2026-07-28`.

![Czas trwania](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Cele nauki

Na koniec tego laboratorium będziesz potrafił:

- ✅ Tworzyć niestandardowe serwery MCP za pomocą Microsoft Foundry Toolkit
- ✅ Konfigurować i używać najnowszego MCP Python SDK (w. 1.9.3)
- ✅ Skonfigurować i wykorzystać MCP Inspectora do debugowania
- ✅ Debugować serwery MCP zarówno w Agent Builder, jak i w środowisku Inspectora
- ✅ Zrozumieć zaawansowane przepływy pracy przy rozwoju serwerów MCP

## 📋 Wymagania wstępne

- Ukończenie Laboratorium 2 (Podstawy MCP)
- VS Code z zainstalowanym rozszerzeniem Microsoft Foundry Toolkit
- Środowisko Python 3.10+
- Node.js i npm do konfiguracji Inspektora

## 🏗️ Co zbudujesz

W tym laboratorium stworzysz **Weather MCP Server**, który demonstruje:
- Niestandardową implementację serwera MCP
- Integrację z Microsoft Foundry Toolkit Agent Builder
- Profesjonalne przepływy pracy debugowania
- Wzorce nowoczesnego użycia MCP SDK

---

## 🔧 Przegląd głównych komponentów

### 🐍 MCP Python SDK
Model Context Protocol Python SDK zapewnia podstawę do budowy własnych serwerów MCP. Użyjesz wersji 1.9.3 z rozszerzonymi możliwościami debugowania.

### 🔍 MCP Inspector
Potężne narzędzie do debugowania, które oferuje:
- Monitorowanie serwera w czasie rzeczywistym
- Wizualizację wykonywania narzędzi
- Inspekcję żądań/odpowiedzi sieciowych
- Interaktywne środowisko testowe

---

## 📖 Implementacja krok po kroku

### Krok 1: Utwórz WeatherAgent w Agent Builder

1. **Uruchom Agent Builder** w VS Code przez rozszerzenie Microsoft Foundry Toolkit
2. **Utwórz nowego agenta** z następującą konfiguracją:
   - Nazwa agenta: `WeatherAgent`

![Tworzenie agenta](../../../../translated_images/pl/Agent.c9c33f6a412b4cde.webp)

### Krok 2: Zainicjuj projekt serwera MCP

1. **Przejdź do Narzędzia** → **Dodaj narzędzie** w Agent Builder
2. **Wybierz "MCP Server"** z dostępnych opcji
3. **Wybierz "Utwórz nowy serwer MCP"**
4. **Wybierz szablon `python-weather`**
5. **Nadaj nazwę serwerowi:** `weather_mcp`

![Wybór szablonu Python](../../../../translated_images/pl/Pythontemplate.9d0a2913c6491500.webp)

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

### Krok 4: Uaktualnij MCP SDK do najnowszej wersji

> **🔍 Dlaczego uaktualniać?** Chcemy użyć najnowszego MCP SDK (w. 1.9.3) i usługi Inspektora (0.14.0)  dla rozszerzonych funkcji i lepszych możliwości debugowania.

#### 4a. Aktualizacja zależności Pythona

**Edytuj `pyproject.toml`:** aktualizacja [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Aktualizacja konfiguracji Inspektora

**Edytuj `inspector/package.json`:** aktualizacja [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Aktualizacja zależności Inspektora

**Edytuj `inspector/package-lock.json`:** aktualizacja [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Uwaga:** Ten plik zawiera rozbudowane definicje zależności. Poniżej znajduje się podstawowa struktura - pełna zawartość zapewnia właściwe rozwiązywanie zależności.


> **⚡ Pełny pakiet blokujący:** Kompletny package-lock.json zawiera ~3000 linii definicji zależności. Powyżej pokazano kluczową strukturę - użyj dostarczonego pliku dla pełnego rozwiązania zależności.

### Krok 5: Skonfiguruj debugowanie w VS Code

*Uwaga: Skopiuj proszę plik we wskazanej ścieżce aby zastąpić odpowiedni lokalny plik*

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

Po dokonaniu zmian konfiguracyjnych wykonaj następujące polecenia:

**Zainstaluj zależności Pythona:**
```bash
uv sync
```

**Zainstaluj zależności Inspektora:**
```bash
cd inspector
npm install
```

### Krok 7: Debugowanie z Agent Builder

1. **Naciśnij F5** lub użyj konfiguracji **"Debug in Agent Builder"**
2. **Wybierz konfigurację złożoną** z panelu debugowania
3. **Poczekaj na uruchomienie serwera** i otwarcie Agent Builder
4. **Testuj swój serwer weather MCP** za pomocą zapytań w naturalnym języku

Wprowadź prompt jak poniżej

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Wynik debugowania Agent Builder](../../../../translated_images/pl/Result.6ac570f7d2b1d538.webp)

### Krok 8: Debugowanie z MCP Inspector

1. **Użyj konfiguracji "Debug in Inspector"** (Edge lub Chrome)
2. **Otwórz interfejs Inspektora** pod adresem `http://localhost:6274`
3. **Przeglądaj interaktywne środowisko testowe:**
   - Podgląd dostępnych narzędzi
   - Testowanie wykonania narzędzi
   - Monitorowanie żądań sieciowych
   - Debugowanie odpowiedzi serwera

![Interfejs MCP Inspector](../../../../translated_images/pl/Inspector.5672415cd02fe873.webp)

---

## 🎯 Kluczowe wyniki nauki

Ukończenie tego laboratorium pozwoliło Ci:

- [x] **Stworzyć niestandardowy serwer MCP** za pomocą szablonów Microsoft Foundry Toolkit
- [x] **Uaktualnić do najnowszego MCP SDK** (w. 1.9.3) dla lepszej funkcjonalności
- [x] **Skonfigurować profesjonalne przepływy pracy debugowania** zarówno dla Agent Builder, jak i Inspectora
- [x] **Skonfigurować MCP Inspectora** do interaktywnego testowania serwera
- [x] **Opanować konfiguracje debugowania w VS Code** dla rozwoju MCP

## 🔧 Zbadane zaawansowane funkcje

| Funkcja | Opis | Przypadek użycia |
|---------|-------------|---------------|
| **MCP Python SDK w. 1.9.3** | Najnowsza implementacja protokołu | Nowoczesny rozwój serwera |
| **MCP Inspector 0.14.0** | Interaktywne narzędzie debugowania | Testowanie serwera w czasie rzeczywistym |
| **Debugowanie w VS Code** | Zintegrowane środowisko programistyczne | Profesjonalny przepływ debugowania |
| **Integracja z Agent Builder** | Bezpośrednie połączenie Microsoft Foundry Toolkit | Testowanie agenta end-to-end |

## 📚 Dodatkowe zasoby

- [Dokumentacja MCP Python SDK](https://modelcontextprotocol.io/docs/sdk/python)
- [Przewodnik rozszerzenia Microsoft Foundry Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [Dokumentacja debugowania VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Specyfikacja Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Gratulacje!** Ukończyłeś Laboratorium 3 i teraz potrafisz tworzyć, debugować oraz wdrażać niestandardowe serwery MCP za pomocą profesjonalnych przepływów rozwojowych.

### 🔜 Kontynuuj do następnego modułu

Gotowy, by zastosować swoje umiejętności MCP w realnym środowisku deweloperskim? Kontynuuj do **[Modułu 4: Praktyczny rozwój MCP - Niestandardowy serwer klonowania GitHub](../lab4/README.md)**, gdzie:
- Zbudujesz produkcyjny serwer MCP automatyzujący operacje na repozytoriach GitHub
- Wdrożysz funkcjonalność klonowania repozytoriów GitHub przez MCP
- Zintegrujesz niestandardowe serwery MCP z VS Code oraz trybem agenta GitHub Copilot
- Przetestujesz i wdrożysz niestandardowe serwery MCP w środowiskach produkcyjnych
- Nauczysz się praktycznej automatyzacji przepływów pracy dla programistów

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
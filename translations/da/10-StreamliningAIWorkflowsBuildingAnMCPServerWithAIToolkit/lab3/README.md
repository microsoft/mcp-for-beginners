# 🔧 Modul 3: Avanceret MCP-udvikling med Microsoft Foundry Toolkit

> [!NOTE]
> Inspector-URL'er i dette laboratorium bruger den ældre `/sse` endpoint og retter sig mod
> den fastlåste MCP SDK `1.9.3` og Inspector `0.14.0` afhængigheder. De er ikke
> aktuelle `2026-07-28` Streamable HTTP-eksempler.

![Varighed](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Læringsmål

Når du er færdig med dette laboratorium, vil du kunne:

- ✅ Oprette tilpassede MCP-servere ved hjælp af Microsoft Foundry Toolkit
- ✅ Konfigurere og bruge den nyeste MCP Python SDK (v1.9.3)
- ✅ Opsætte og anvende MCP Inspector til debugging
- ✅ Debugge MCP-servere i både Agent Builder og Inspector-miljøer
- ✅ Forstå avancerede udviklingsarbejdsgange for MCP-servere

## 📋 Forudsætninger

- Gennemførelse af Laboratorium 2 (MCP Fundamentaler)
- VS Code med Microsoft Foundry Toolkit-udvidelsen installeret
- Python 3.10+ miljø
- Node.js og npm til Inspector-installation

## 🏗️ Hvad du skal bygge

I dette laboratorium skaber du en **Weather MCP Server**, der demonstrerer:
- Tilpasset MCP-serverimplementering
- Integration med Microsoft Foundry Toolkit Agent Builder
- Professionelle debugging-arbejdsgange
- Moderne MCP SDK-brugsmønstre

---

## 🔧 Oversigt over kernekomponenter

### 🐍 MCP Python SDK
Model Context Protocol Python SDK leverer fundamentet for at bygge tilpassede MCP-servere. Du vil bruge version 1.9.3 med forbedrede debugging-muligheder.

### 🔍 MCP Inspector
Et kraftfuldt debugging-værktøj, der tilbyder:
- Real-time serverovervågning
- Visualisering af værktøjsudførelse
- Inspektion af netværksanmodninger/svar
- Interaktiv testmiljø

---

## 📖 Trin-for-trin implementering

### Trin 1: Opret en WeatherAgent i Agent Builder

1. **Start Agent Builder** i VS Code gennem Microsoft Foundry Toolkit-udvidelsen
2. **Opret en ny agent** med følgende konfiguration:
   - Agentnavn: `WeatherAgent`

![Agent Oprettelse](../../../../translated_images/da/Agent.c9c33f6a412b4cde.webp)

### Trin 2: Initialiser MCP-serverprojektet

1. **Gå til Tools** → **Add Tool** i Agent Builder
2. **Vælg "MCP Server"** blandt de tilgængelige muligheder
3. **Vælg "Create A new MCP Server"**
4. **Vælg `python-weather` skabelonen**
5. **Navngiv din server:** `weather_mcp`

![Valg af Python-skabelon](../../../../translated_images/da/Pythontemplate.9d0a2913c6491500.webp)

### Trin 3: Åbn og undersøg projektet

1. **Åbn det genererede projekt** i VS Code
2. **Gennemgå projektstrukturen:**
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

### Trin 4: Opgrader til seneste MCP SDK

> **🔍 Hvorfor opgradere?** Vi ønsker at bruge den nyeste MCP SDK (v1.9.3) og Inspector-service (0.14.0) for forbedrede funktioner og bedre debugging-muligheder.

#### 4a. Opdater Python-afhængigheder

**Rediger `pyproject.toml`:** opdater [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Opdater Inspector-konfiguration

**Rediger `inspector/package.json`:** opdater [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Opdater Inspector-afhængigheder

**Rediger `inspector/package-lock.json`:** opdater [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Bemærk:** Denne fil indeholder omfattende afhængighedsdefinitioner. Nedenfor er den væsentlige struktur - det fulde indhold sikrer korrekt afhængighedsopløsning.


> **⚡ Fuld Package Lock:** Den komplette package-lock.json indeholder ~3000 linjer med afhængighedsdefinitioner. Ovenstående viser nøglestrukturen - brug den medfølgende fil for komplet afhængighedsopløsning.

### Trin 5: Konfigurer VS Code debugging

*Bemærk: Kopiér venligst filen i den angivne sti for at erstatte den tilsvarende lokale fil*

#### 5a. Opdater Launch-konfiguration

**Rediger `.vscode/launch.json`:**

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

**Rediger `.vscode/tasks.json`:**

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

## 🚀 Kørsel og test af din MCP-server

### Trin 6: Installer afhængigheder

Efter at have foretaget konfigurationsændringerne skal du køre følgende kommandoer:

**Installer Python-afhængigheder:**
```bash
uv sync
```

**Installer Inspector-afhængigheder:**
```bash
cd inspector
npm install
```

### Trin 7: Debug med Agent Builder

1. **Tryk på F5** eller brug **"Debug in Agent Builder"** konfigurationen
2. **Vælg den sammensatte konfiguration** i debugpanelet
3. **Vent på at serveren starter** og Agent Builder åbner
4. **Test din weather MCP-server** med forespørgsler i naturligt sprog

Indtast prompt som denne

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Resultat](../../../../translated_images/da/Result.6ac570f7d2b1d538.webp)

### Trin 8: Debug med MCP Inspector

1. **Brug "Debug in Inspector"** konfigurationen (Edge eller Chrome)
2. **Åbn Inspector-interface** på `http://localhost:6274`
3. **Udforsk det interaktive testmiljø:**
   - Se tilgængelige værktøjer
   - Test værktøjsudførelse
   - Overvåg netværksanmodninger
   - Debug server-svar

![MCP Inspector Interface](../../../../translated_images/da/Inspector.5672415cd02fe873.webp)

---

## 🎯 Centrale læringsresultater

Ved at gennemføre dette laboratorium har du:

- [x] **Oprettet en tilpasset MCP-server** ved hjælp af Microsoft Foundry Toolkit-skabeloner
- [x] **Opgraderet til den nyeste MCP SDK** (v1.9.3) for forbedret funktionalitet
- [x] **Konfigureret professionelle debugging-arbejdsgange** for både Agent Builder og Inspector
- [x] **Opsat MCP Inspector** til interaktiv servertest
- [x] **Behersket VS Code debugging-konfigurationer** til MCP-udvikling

## 🔧 Avancerede funktioner udforsket

| Funktion | Beskrivelse | Brugstilfælde |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | Seneste protokolimplementering | Moderne serverudvikling |
| **MCP Inspector 0.14.0** | Interaktivt debugging-værktøj | Real-time servertest |
| **VS Code Debugging** | Integreret udviklingsmiljø | Professionel debugging-arbejdsgang |
| **Agent Builder Integration** | Direkte Microsoft Foundry Toolkit-forbindelse | End-to-end agenttest |

## 📚 Yderligere ressourcer

- [MCP Python SDK Dokumentation](https://modelcontextprotocol.io/docs/sdk/python)
- [Microsoft Foundry Toolkit Udvidelsesvejledning](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code Debugging Dokumentation](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol Specifikation](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Tillykke!** Du har gennemført Laboratorium 3 og kan nu oprette, debugge og implementere tilpassede MCP-servere med professionelle udviklingsarbejdsgange.

### 🔜 Fortsæt til næste modul

Klar til at anvende dine MCP-færdigheder i en reel udviklingsarbejdsgang? Fortsæt til **[Modul 4: Praktisk MCP-udvikling - Tilpasset GitHub Clone Server](../lab4/README.md)**, hvor du vil:
- Bygge en produktionsklar MCP-server, der automatiserer GitHub-repository-operationer
- Implementere GitHub repository-klonfunktionalitet via MCP
- Integrere tilpassede MCP-servere med VS Code og GitHub Copilot Agent Mode
- Teste og implementere tilpassede MCP-servere i produktionsmiljøer
- Lære praktisk workflow-automatisering for udviklere

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
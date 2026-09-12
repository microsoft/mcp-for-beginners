# 🔧 Modul 3: Avancerad MCP-utveckling med Microsoft Foundry Toolkit

> [!NOTE]
> Inspektör-URL:er i detta laboratorium använder den äldre `/sse`-ändpunkten och riktar sig mot
> fastställda MCP SDK `1.9.3` och Inspektör `0.14.0` beroenden. De är inte
> aktuella `2026-07-28` Streamable HTTP-exempel.

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Lärandemål

I slutet av detta laboratorium kommer du att kunna:

- ✅ Skapa anpassade MCP-servrar med Microsoft Foundry Toolkit
- ✅ Konfigurera och använda den senaste MCP Python SDK (v1.9.3)
- ✅ Sätta upp och använda MCP Inspektör för felsökning
- ✅ Felsöka MCP-servrar i både Agent Builder och Inspektör-miljöer
- ✅ Förstå avancerade arbetsflöden för MCP-serverutveckling

## 📋 Förkunskaper

- Avslutat Laboratorium 2 (MCP Grundläggande)
- VS Code med Microsoft Foundry Toolkit-tillägg installerat
- Python 3.10+ miljö
- Node.js och npm för inspektörssetup

## 🏗️ Vad du kommer att bygga

I detta labb kommer du att skapa en **Weather MCP Server** som demonstrerar:
- Anpassad MCP-serverimplementation
- Integration med Microsoft Foundry Toolkit Agent Builder
- Professionella felsökningsarbetsflöden
- Moderna MCP SDK-användningsmönster

---

## 🔧 Översikt av kärnkomponenter

### 🐍 MCP Python SDK
Model Context Protocol Python SDK utgör grunden för att bygga anpassade MCP-servrar. Du kommer att använda version 1.9.3 med förbättrade felsökningsmöjligheter.

### 🔍 MCP Inspektör
Ett kraftfullt felsökningsverktyg som erbjuder:
- Realtidsövervakning av server
- Visualisering av verktygsexekvering
- Inspektion av nätverksförfrågningar/svar
- Interaktiv testmiljö

---

## 📖 Steg-för-steg-implementering

### Steg 1: Skapa en WeatherAgent i Agent Builder

1. **Starta Agent Builder** i VS Code via Microsoft Foundry Toolkit-tillägget
2. **Skapa en ny agent** med följande konfiguration:
   - Agentnamn: `WeatherAgent`

![Agent Creation](../../../../translated_images/sv/Agent.c9c33f6a412b4cde.webp)

### Steg 2: Initiera MCP Server-projektet

1. **Navigera till Verktyg** → **Lägg till verktyg** i Agent Builder
2. **Välj "MCP Server"** från de tillgängliga alternativen
3. **Välj "Skapa en ny MCP Server"**
4. **Välj mallen `python-weather`**
5. **Namnge din server:** `weather_mcp`

![Python Template Selection](../../../../translated_images/sv/Pythontemplate.9d0a2913c6491500.webp)

### Steg 3: Öppna och granska projektet

1. **Öppna det genererade projektet** i VS Code
2. **Granska projektstrukturen:**
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

### Steg 4: Uppgradera till senaste MCP SDK

> **🔍 Varför uppgradera?** Vi vill använda den senaste MCP SDK (v1.9.3) och Inspektör-tjänsten (0.14.0) för förbättrade funktioner och bättre felsökningsmöjligheter.

#### 4a. Uppdatera Python-beroenden

**Redigera `pyproject.toml`:** uppdatera [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Uppdatera Inspektör-konfiguration

**Redigera `inspector/package.json`:** uppdatera [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Uppdatera Inspektör-beroenden

**Redigera `inspector/package-lock.json`:** uppdatera [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Notera:** Denna fil innehåller omfattande beroendedefinitioner. Nedan är den väsentliga strukturen – det fulla innehållet säkerställer korrekt beroendelösning.


> **⚡ Komplett Package Lock:** Den fullständiga package-lock.json innehåller ~3000 rader med beroendedefinitioner. Ovan visas nyckelstrukturen – använd den medföljande filen för komplett beroendelösning.

### Steg 5: Konfigurera VS Code-felsökning

*Notera: Vänligen kopiera filen i angiven sökväg för att ersätta motsvarande lokala fil*

#### 5a. Uppdatera startkonfiguration

**Redigera `.vscode/launch.json`:**

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

**Redigera `.vscode/tasks.json`:**

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

## 🚀 Köra och testa din MCP-server

### Steg 6: Installera beroenden

Efter att ha gjort konfigurationsändringarna, kör följande kommandon:

**Installera Python-beroenden:**
```bash
uv sync
```

**Installera Inspektör-beroenden:**
```bash
cd inspector
npm install
```

### Steg 7: Felsök med Agent Builder

1. **Tryck på F5** eller använd **"Felsök i Agent Builder"**-konfigurationen
2. **Välj sammansatt konfiguration** från felsökningspanelen
3. **Vänta på att servern startar** och att Agent Builder öppnas
4. **Testa din weather MCP-server** med naturliga språkfrågor

Skriv in prompten så här

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/sv/Result.6ac570f7d2b1d538.webp)

### Steg 8: Felsök med MCP Inspektör

1. **Använd "Felsök i Inspektör"**-konfigurationen (Edge eller Chrome)
2. **Öppna Inspektör-gränssnittet** på `http://localhost:6274`
3. **Utforska den interaktiva testmiljön:**
   - Visa tillgängliga verktyg
   - Testa verktygsexekvering
   - Övervaka nätverksförfrågningar
   - Felsök serverrespons

![MCP Inspector Interface](../../../../translated_images/sv/Inspector.5672415cd02fe873.webp)

---

## 🎯 Viktiga lärandemål

Genom att ha genomfört detta laboratorium har du:

- [x] **Skapat en anpassad MCP-server** med Microsoft Foundry Toolkit-mallar
- [x] **Uppgraderat till senaste MCP SDK** (v1.9.3) för förbättrad funktionalitet
- [x] **Konfigurerat professionella felsökningsarbetsflöden** för både Agent Builder och Inspektör
- [x] **Satt upp MCP Inspektör** för interaktiv servertestning
- [x] **Behärskat VS Code-felsökningskonfigurationer** för MCP-utveckling

## 🔧 Avancerade funktioner som utforskats

| Funktion | Beskrivning | Användningsfall |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | Senaste protokollimplementationen | Modern serverutveckling |
| **MCP Inspektör 0.14.0** | Interaktivt felsökningsverktyg | Realtids servertestning |
| **VS Code Felsökning** | Integrerad utvecklingsmiljö | Professionellt felsökningsarbetsflöde |
| **Agent Builder Integration** | Direkt Microsoft Foundry Toolkit-anslutning | Helhets-Test av agent |

## 📚 Ytterligare resurser

- [MCP Python SDK Dokumentation](https://modelcontextprotocol.io/docs/sdk/python)
- [Microsoft Foundry Toolkit Tilläggsguide](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code Felsökningsdokumentation](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol Specifikation](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Grattis!** Du har framgångsrikt genomfört Laboratorium 3 och kan nu skapa, felsöka och distribuera anpassade MCP-servrar med professionella utvecklingsarbetsflöden.

### 🔜 Fortsätt till nästa modul

Redo att tillämpa dina MCP-kunskaper i ett verkligt utvecklingsarbetsflöde? Fortsätt till **[Modul 4: Praktisk MCP-utveckling - Anpassad GitHub-klonserver](../lab4/README.md)** där du kommer att:
- Bygga en produktionsklar MCP-server som automatiserar GitHub-repositorieoperationer
- Implementera GitHub-repositoriekloning via MCP
- Integrera anpassade MCP-servrar med VS Code och GitHub Copilot Agent-läge
- Testa och distribuera anpassade MCP-servrar i produktionsmiljöer
- Lära dig praktisk arbetsflödesautomation för utvecklare

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
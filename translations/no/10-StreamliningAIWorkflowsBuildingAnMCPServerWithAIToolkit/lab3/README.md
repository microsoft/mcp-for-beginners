# 🔧 Modul 3: Avansert MCP-utvikling med Microsoft Foundry Toolkit

> [!NOTE]
> Inspector-URL-er i dette laboratoriet bruker den gamle `/sse` endepunktet og sikter mot
> den låste MCP SDK `1.9.3` og Inspector `0.14.0` avhengighetene. De er ikke
> nåværende `2026-07-28` Streamable HTTP-eksempler.

![Varighet](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Læringsmål

Ved slutten av dette laboratoriet vil du kunne:

- ✅ Lage egendefinerte MCP-servere ved bruk av Microsoft Foundry Toolkit
- ✅ Konfigurere og bruke den nyeste MCP Python SDK (v1.9.3)
- ✅ Sette opp og bruke MCP Inspector for feilsøking
- ✅ Feilsøke MCP-servere i både Agent Builder og Inspector-miljøer
- ✅ Forstå avanserte arbeidsflyter for MCP-serverutvikling

## 📋 Forutsetninger

- Ferdigstillelse av Lab 2 (MCP Grunnleggende)
- VS Code med Microsoft Foundry Toolkit-utvidelsen installert
- Python 3.10+ miljø
- Node.js og npm for Inspector-oppsett

## 🏗️ Hva du skal bygge

I dette laboratoriet skal du lage en **Weather MCP Server** som demonstrerer:
- Egendefinert MCP-serverimplementasjon
- Integrasjon med Microsoft Foundry Toolkit Agent Builder
- Profesjonelle feilsøkingsarbeidsflyter
- Moderne MCP SDK-bruksmønstre

---

## 🔧 Oversikt over kjernekomponenter

### 🐍 MCP Python SDK
Model Context Protocol Python SDK gir fundamentet for å bygge egendefinerte MCP-servere. Du vil bruke versjon 1.9.3 med forbedrede feilsøkingsmuligheter.

### 🔍 MCP Inspector
Et kraftig feilsøkingsverktøy som tilbyr:
- Sanntidsovervåking av server
- Visualisering av verktøyutførelse
- Inspeksjon av nettverksforespørsler/-responser
- Interaktiv testmiljø

---

## 📖 Trinnvis implementering

### Trinn 1: Lag en WeatherAgent i Agent Builder

1. **Start Agent Builder** i VS Code gjennom Microsoft Foundry Toolkit-utvidelsen
2. **Opprett en ny agent** med følgende konfigurasjon:
   - Agentnavn: `WeatherAgent`

![Agent Opprettelse](../../../../translated_images/no/Agent.c9c33f6a412b4cde.webp)

### Trinn 2: Initialiser MCP Server Project

1. **Naviger til Tools** → **Add Tool** i Agent Builder
2. **Velg "MCP Server"** fra tilgjengelige alternativer
3. **Velg "Create A new MCP Server"**
4. **Velg malen `python-weather`**
5. **Gi serveren ditt navn:** `weather_mcp`

![Python Malvalg](../../../../translated_images/no/Pythontemplate.9d0a2913c6491500.webp)

### Trinn 3: Åpne og undersøk prosjektet

1. **Åpne det genererte prosjektet** i VS Code
2. **Gå gjennom prosjektstrukturen:**
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

### Trinn 4: Oppgrader til nyeste MCP SDK

> **🔍 Hvorfor oppgradere?** Vi ønsker å bruke nyeste MCP SDK (v1.9.3) og Inspector-tjenesten (0.14.0) for forbedrede funksjoner og bedre feilsøkingsmuligheter.

#### 4a. Oppdater Python-avhengigheter

**Rediger `pyproject.toml`:** oppdater [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Oppdater Inspector-konfigurasjon

**Rediger `inspector/package.json`:** oppdater [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Oppdater Inspector-avhengigheter

**Rediger `inspector/package-lock.json`:** oppdater [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Merk:** Denne filen inneholder omfattende avhengighetsdefinisjoner. Nedenfor er den essensielle strukturen - fullstendig innhold sikrer korrekt avhengighetsløsning.


> **⚡ Full Package Lock:** Den komplette package-lock.json inneholder omtrent 3000 linjer med avhengighetsdefinisjoner. Ovenfor vises nøkkelstrukturen - bruk den medfølgende filen for fullstendig avhengighetsløsning.

### Trinn 5: Konfigurer VS Code feilsøking

*Merk: Kopier filen i angitt bane for å erstatte tilsvarende lokal fil*

#### 5a. Oppdater oppstartskonfigurasjon

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

## 🚀 Kjøre og teste din MCP Server

### Trinn 6: Installer avhengigheter

Etter å ha gjort konfigurasjonsendringene, kjør følgende kommandoer:

**Installer Python-avhengigheter:**
```bash
uv sync
```

**Installer Inspector-avhengigheter:**
```bash
cd inspector
npm install
```

### Trinn 7: Feilsøk med Agent Builder

1. **Trykk F5** eller bruk **"Debug in Agent Builder"** konfigurasjon
2. **Velg den sammensatte konfigurasjonen** fra feilsøkingspanelet
3. **Vent på at serveren starter** og Agent Builder åpnes
4. **Test din weather MCP server** med naturlige språkspørsmål

Skriv inn forespørsel slik

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Feilsøkingsresultat](../../../../translated_images/no/Result.6ac570f7d2b1d538.webp)

### Trinn 8: Feilsøk med MCP Inspector

1. **Bruk "Debug in Inspector"** konfigurasjon (Edge eller Chrome)
2. **Åpne Inspector-grensesnittet** på `http://localhost:6274`
3. **Utforsk det interaktive testmiljøet:**
   - Se tilgjengelige verktøy
   - Test verktøyutførelse
   - Overvåk nettverksforespørsler
   - Feilsøk serverresponser

![MCP Inspector-grensesnitt](../../../../translated_images/no/Inspector.5672415cd02fe873.webp)

---

## 🎯 Viktige læringsresultater

Ved å fullføre dette laboratoriet har du:

- [x] **Opprettet en egendefinert MCP-server** ved bruk av Microsoft Foundry Toolkit-maler
- [x] **Oppgradert til nyeste MCP SDK** (v1.9.3) for forbedret funksjonalitet
- [x] **Konfigurert profesjonelle feilsøkingsarbeidsflyter** for både Agent Builder og Inspector
- [x] **Satt opp MCP Inspector** for interaktiv servertesting
- [x] **Behersket VS Code feilsøkingskonfigurasjoner** for MCP-utvikling

## 🔧 Utforskede avanserte funksjoner

| Funksjon | Beskrivelse | Brukstilfelle |
|---------|-------------|--------------|
| **MCP Python SDK v1.9.3** | Nyeste protokollimplementasjon | Moderne serverutvikling |
| **MCP Inspector 0.14.0** | Interaktivt feilsøkingsverktøy | Sanntids servertesting |
| **VS Code Debugging** | Integrert utviklingsmiljø | Profesjonell feilsøkingsarbeidsflyt |
| **Agent Builder Integration** | Direkte Microsoft Foundry Toolkit-tilkobling | Helhetlig agenttesting |

## 📚 Ekstra ressurser

- [MCP Python SDK Dokumentasjon](https://modelcontextprotocol.io/docs/sdk/python)
- [Microsoft Foundry Toolkit Utvidelsesguide](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code Feilsøkingsdokumentasjon](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol Spesifikasjon](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Gratulerer!** Du har fullført Lab 3 vellykket og kan nå opprette, feilsøke og distribuere egendefinerte MCP-servere ved hjelp av profesjonelle utviklingsarbeidsflyter.

### 🔜 Fortsett til neste modul

Klar til å bruke dine MCP-ferdigheter i en ekte utviklingsarbeidsflyt? Fortsett til **[Modul 4: Praktisk MCP-utvikling - Egendefinert GitHub Clone Server](../lab4/README.md)** hvor du vil:
- Bygge en produksjonsklar MCP-server som automatiserer GitHub-repositoriumoperasjoner
- Implementere GitHub-repositoriumkloning via MCP
- Integrere egendefinerte MCP-servere med VS Code og GitHub Copilot Agent Mode
- Teste og distribuere egendefinerte MCP-servere i produksjonsmiljøer
- Lære praktisk arbeidsflytautomatisering for utviklere

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
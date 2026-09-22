# 🔧 Modul 3: Pokročilý vývoj MCP s Microsoft Foundry Toolkit

> [!NOTE]
> URL inspektora v tomto labu používají starý `/sse` endpoint a cílují na
> pevné závislosti MCP SDK `1.9.3` a Inspector `0.14.0`. Nejsou to
> aktuální příklady Streamable HTTP z `2026-07-28`.

![Délka](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Výukové cíle

Na konci tohoto laboratoře budete schopni:

- ✅ Vytvořit vlastní MCP servery pomocí Microsoft Foundry Toolkit
- ✅ Nakonfigurovat a použít nejnovější MCP Python SDK (v1.9.3)
- ✅ Nastavit a využít MCP Inspector pro ladění
- ✅ Ladit MCP servery jak v Agent Builder, tak v Inspector prostředích
- ✅ Pochopit pokročilé pracovní postupy vývoje MCP serverů

## 📋 Předpoklady

- Dokončení Laboratoře 2 (Základy MCP)
- VS Code s nainstalovaným rozšířením Microsoft Foundry Toolkit
- Prostředí Python 3.10+
- Node.js a npm pro nastavení Inspectoru

## 🏗️ Co vytvoříte

V tomto labu vytvoříte **Weather MCP Server**, který demonstruje:
- Vlastní implementaci MCP serveru
- Integraci s Microsoft Foundry Toolkit Agent Builder
- Profesionální pracovní postupy ladění
- Moderní vzory používání MCP SDK

---

## 🔧 Přehled hlavních komponent

### 🐍 MCP Python SDK
Model Context Protocol Python SDK poskytuje základ pro vytváření vlastních MCP serverů. Použijete verzi 1.9.3 s rozšířenými možnostmi ladění.

### 🔍 MCP Inspector
Výkonný nástroj pro ladění, který přináší:
- Monitorování serveru v reálném čase
- Vizualizaci vykonávání nástrojů
- Inspekci síťových požadavků/odpovědí
- Interaktivní testovací prostředí

---

## 📖 Krok za krokem implementace

### Krok 1: Vytvoření WeatherAgenta v Agent Builder

1. **Spusťte Agent Builder** ve VS Code přes rozšíření Microsoft Foundry Toolkit
2. **Vytvořte nového agenta** s následující konfigurací:
   - Název agenta: `WeatherAgent`

![Vytvoření agenta](../../../../translated_images/cs/Agent.c9c33f6a412b4cde.webp)

### Krok 2: Inicializace MCP Server Projektu

1. **Přejděte na Nástroje** → **Přidat nástroj** v Agent Builder
2. **Vyberte "MCP Server"** z dostupných možností
3. **Zvolte "Vytvořit nový MCP Server"**
4. **Vyberte šablonu `python-weather`**
5. **Pojmenujte server:** `weather_mcp`

![Výběr Python šablony](../../../../translated_images/cs/Pythontemplate.9d0a2913c6491500.webp)

### Krok 3: Otevřete a Prozkoumejte Projekt

1. **Otevřete vygenerovaný projekt** ve VS Code
2. **Prohlédněte si strukturu projektu:**
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

### Krok 4: Aktualizace na nejnovější MCP SDK

> **🔍 Proč aktualizovat?** Chceme použít nejnovější MCP SDK (v1.9.3) a Inspector službu (0.14.0) pro rozšířené funkce a lepší ladění.

#### 4a. Aktualizace Python závislostí

**Upravte `pyproject.toml`:** aktualizace [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. Aktualizace konfigurace Inspectoru

**Upravte `inspector/package.json`:** aktualizace [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Aktualizace závislostí Inspectoru

**Upravte `inspector/package-lock.json`:** aktualizace [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Poznámka:** Tento soubor obsahuje rozsáhlé definice závislostí. Níže je klíčová struktura - kompletní obsah zajišťuje správné vyřešení závislostí.


> **⚡ Kompletní package-lock:** Celý package-lock.json obsahuje ~3000 řádků definic závislostí. Výše je ukázána klíčová struktura - použijte dodaný soubor pro kompletní vyřešení závislostí.

### Krok 5: Konfigurace ladění ve VS Code

*Poznámka: Prosím, zkopírujte soubor na uvedenou cestu a nahraďte odpovídající lokální soubor*

#### 5a. Aktualizace konfiguračního souboru spuštění

**Upravte `.vscode/launch.json`:**

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

**Upravte `.vscode/tasks.json`:**

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

## 🚀 Spuštění a testování vašeho MCP serveru

### Krok 6: Instalace závislostí

Po provedení změn konfigurace spusťte následující příkazy:

**Instalujte Python závislosti:**
```bash
uv sync
```

**Instalujte závislosti Inspectoru:**
```bash
cd inspector
npm install
```

### Krok 7: Ladění pomocí Agent Builder

1. **Stiskněte F5** nebo použijte konfiguraci **"Debug in Agent Builder"**
2. **Vyberte složenou konfiguraci** v ladicím panelu
3. **Počkejte na spuštění serveru** a otevření Agent Builderu
4. **Otestujte svůj weather MCP server** přirozenými dotazy

Například vstupní prompt

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Výsledek ladění v Agent Builder](../../../../translated_images/cs/Result.6ac570f7d2b1d538.webp)

### Krok 8: Ladění pomocí MCP Inspector

1. **Použijte konfiguraci "Debug in Inspector"** (Edge nebo Chrome)
2. **Otevřete rozhraní Inspectoru** na `http://localhost:6274`
3. **Prozkoumejte interaktivní testovací prostředí:**
   - Prohlédněte dostupné nástroje
   - Testujte vykonávání nástrojů
   - Sledujte síťové požadavky
   - Ladění odpovědí serveru

![Rozhraní MCP Inspector](../../../../translated_images/cs/Inspector.5672415cd02fe873.webp)

---

## 🎯 Klíčové výstupy učení

Dokončením této laboratoře jste:

- [x] **Vytvořili vlastní MCP server** pomocí šablon Microsoft Foundry Toolkit
- [x] **Aktualizovali na nejnovější MCP SDK** (v1.9.3) pro rozšířené funkce
- [x] **Nakonfigurovali profesionální pracovní postupy ladění** jak pro Agent Builder, tak Inspector
- [x] **Nastavili MCP Inspector** pro interaktivní testování serveru
- [x] **Ovládáte ladicí konfigurace ve VS Code** pro vývoj MCP

## 🔧 Prozkoumané pokročilé funkce

| Funkce | Popis | Použití |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | Nejnovější implementace protokolu | Moderní vývoj serveru |
| **MCP Inspector 0.14.0** | Interaktivní nástroj pro ladění | Testování serveru v reálném čase |
| **Ladění ve VS Code** | Integrované vývojové prostředí | Profesionální pracovní postup ladění |
| **Integrace Agent Builder** | Přímé propojení s Microsoft Foundry Toolkit | Testování agenta od začátku do konce |

## 📚 Další zdroje

- [Dokumentace MCP Python SDK](https://modelcontextprotocol.io/docs/sdk/python)
- [Průvodce rozšířením Microsoft Foundry Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [Dokumentace ladění ve VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Specifikace Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Gratulujeme!** Úspěšně jste dokončili Laboratoř 3 a nyní můžete vytvářet, ladit a nasazovat vlastní MCP servery pomocí profesionálních pracovních postupů vývoje.

### 🔜 Pokračujte do dalšího modulu

Připraveni aplikovat své MCP dovednosti v reálném vývojovém pracovním postupu? Pokračujte do **[Modul 4: Praktický vývoj MCP - Vlastní GitHub klonovací server](../lab4/README.md)**, kde budete:
- Vytvářet produkčně připravený MCP server automatizující operace s GitHub repozitáři
- Implementovat funkci klonování GitHub repozitářů přes MCP
- Integrovat vlastní MCP servery s VS Code a GitHub Copilot Agent Mode
- Testovat a nasazovat vlastní MCP servery v produkčním prostředí
- Naučit se praktickou automatizaci pracovních postupů pro vývojáře

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
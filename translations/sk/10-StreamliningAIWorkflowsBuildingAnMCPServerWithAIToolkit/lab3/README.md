# 🔧 Modul 3: Pokročilý vývoj MCP s AI Toolkit

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 Ciele učenia

Na konci tohto laboratória budete schopní:

- ✅ Vytvárať vlastné MCP servery pomocou AI Toolkit
- ✅ Konfigurovať a používať najnovšiu verziu MCP Python SDK (v1.9.3)
- ✅ Nastaviť a využiť MCP Inspector na ladenie
- ✅ Ladiť MCP servery v prostredí Agent Builder aj Inspector
- ✅ Pochopiť pokročilé pracovné postupy vývoja MCP serverov

## 📋 Predpoklady

- Dokončenie Lab 2 (Základy MCP)
- VS Code s nainštalovaným rozšírením AI Toolkit
- Prostredie Python 3.10+
- Node.js a npm pre nastavenie Inspector

## 🏗️ Čo si vytvoríte

V tomto laboratóriu vytvoríte **Weather MCP Server**, ktorý demonštruje:
- Implementáciu vlastného MCP servera
- Integráciu s AI Toolkit Agent Builder
- Profesionálne pracovné postupy ladenia
- Moderné vzory používania MCP SDK

---

## 🔧 Prehľad hlavných komponentov

### 🐍 MCP Python SDK
Model Context Protocol Python SDK poskytuje základ pre tvorbu vlastných MCP serverov. Použijete verziu 1.9.3 s vylepšenými možnosťami ladenia.

### 🔍 MCP Inspector
Výkonný nástroj na ladenie, ktorý ponúka:
- Monitorovanie servera v reálnom čase
- Vizualizáciu vykonávania nástrojov
- Kontrolu sieťových požiadaviek a odpovedí
- Interaktívne testovacie prostredie

---

## 📖 Krok za krokom: Implementácia

### Krok 1: Vytvorte WeatherAgent v Agent Builder

1. **Spustite Agent Builder** vo VS Code cez rozšírenie AI Toolkit
2. **Vytvorte nového agenta** s nasledujúcou konfiguráciou:
   - Názov agenta: `WeatherAgent`

![Agent Creation](../../../../translated_images/sk/Agent.c9c33f6a412b4cdedfb973fe5448bdb33de3f400055603111b875610e9b917ab.png)

### Krok 2: Inicializujte projekt MCP servera

1. **Prejdite do Tools** → **Add Tool** v Agent Builder
2. **Vyberte "MCP Server"** z dostupných možností
3. **Zvoľte "Create A new MCP Server"**
4. **Vyberte šablónu `python-weather`**
5. **Pomenujte svoj server:** `weather_mcp`

![Python Template Selection](../../../../translated_images/sk/Pythontemplate.9d0a2913c6491500bd673430f024dc44676af2808a27b5da9dcc0eb7063adc28.png)

### Krok 3: Otvorte a preskúmajte projekt

1. **Otvorte vygenerovaný projekt** vo VS Code
2. **Prezrite si štruktúru projektu:**
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

### Krok 4: Aktualizujte na najnovšie MCP SDK

> **🔍 Prečo aktualizovať?** Chceme použiť najnovšiu verziu MCP SDK (v1.9.3) a službu Inspector (0.14.0) pre rozšírené funkcie a lepšie možnosti ladenia.

#### 4a. Aktualizujte Python závislosti

**Upravte `pyproject.toml`:** aktualizujte [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4b. Aktualizujte konfiguráciu Inspector

**Upravte `inspector/package.json`:** aktualizujte [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. Aktualizujte závislosti Inspector

**Upravte `inspector/package-lock.json`:** aktualizujte [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 Poznámka:** Tento súbor obsahuje rozsiahle definície závislostí. Nižšie je základná štruktúra – kompletný obsah zabezpečuje správne vyriešenie závislostí.

> **⚡ Kompletný package-lock:** Celý package-lock.json obsahuje približne 3000 riadkov definícií závislostí. Vyššie je zobrazená kľúčová štruktúra – pre úplné vyriešenie závislostí použite poskytnutý súbor.

### Krok 5: Nastavte ladenie vo VS Code

*Poznámka: Skopírujte súbor na uvedenú cestu, aby ste nahradili príslušný lokálny súbor*

#### 5a. Aktualizujte konfiguráciu spustenia

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

## 🚀 Spustenie a testovanie MCP servera

### Krok 6: Inštalácia závislostí

Po vykonaní zmien v konfigurácii spustite nasledujúce príkazy:

**Inštalácia Python závislostí:**
```bash
uv sync
```

**Inštalácia závislostí Inspector:**
```bash
cd inspector
npm install
```

### Krok 7: Ladenie v Agent Builder

1. **Stlačte F5** alebo použite konfiguráciu **"Debug in Agent Builder"**
2. **Vyberte zloženú konfiguráciu** v debug paneli
3. **Počkajte na spustenie servera** a otvorenie Agent Builder
4. **Otestujte svoj weather MCP server** pomocou prirodzených jazykových dotazov

Zadajte prompt ako tento

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/sk/Result.6ac570f7d2b1d5389c561ab0566970fe0f13e75bdd976b6a7f0270bc715d07f8.png)

### Krok 8: Ladenie s MCP Inspector

1. **Použite konfiguráciu "Debug in Inspector"** (Edge alebo Chrome)
2. **Otvorte rozhranie Inspector** na adrese `http://localhost:6274`
3. **Preskúmajte interaktívne testovacie prostredie:**
   - Prezrite si dostupné nástroje
   - Otestujte vykonávanie nástrojov
   - Sledujte sieťové požiadavky
   - Ladiť odpovede servera

![MCP Inspector Interface](../../../../translated_images/sk/Inspector.5672415cd02fe8731774586cc0a1083e3275d2f8491602aecc8ac4d61f2c0d57.png)

---

## 🎯 Kľúčové výsledky učenia

Dokončením tohto laboratória ste:

- [x] **Vytvorili vlastný MCP server** pomocou šablón AI Toolkit
- [x] **Aktualizovali na najnovšie MCP SDK** (v1.9.3) pre rozšírenú funkcionalitu
- [x] **Nakonfigurovali profesionálne pracovné postupy ladenia** pre Agent Builder aj Inspector
- [x] **Nastavili MCP Inspector** pre interaktívne testovanie servera
- [x] **Ovládli konfigurácie ladenia vo VS Code** pre vývoj MCP

## 🔧 Preskúmané pokročilé funkcie

| Funkcia | Popis | Použitie |
|---------|--------|----------|
| **MCP Python SDK v1.9.3** | Najnovšia implementácia protokolu | Moderný vývoj servera |
| **MCP Inspector 0.14.0** | Interaktívny nástroj na ladenie | Testovanie servera v reálnom čase |
| **VS Code Debugging** | Integrované vývojové prostredie | Profesionálny pracovný postup ladenia |
| **Integrácia Agent Builder** | Priame prepojenie s AI Toolkit | Komplexné testovanie agenta |

## 📚 Dodatočné zdroje

- [MCP Python SDK Dokumentácia](https://modelcontextprotocol.io/docs/sdk/python)
- [Sprievodca rozšírením AI Toolkit](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [Dokumentácia ladenia vo VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Špecifikácia Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 Gratulujeme!** Úspešne ste dokončili Lab 3 a teraz viete vytvárať, ladiť a nasadzovať vlastné MCP servery pomocou profesionálnych pracovných postupov vývoja.

### 🔜 Pokračujte do ďalšieho modulu

Ste pripravení aplikovať svoje MCP zručnosti v reálnom vývojovom prostredí? Pokračujte do **[Modul 4: Praktický vývoj MCP - Vlastný GitHub Clone Server](../lab4/README.md)**, kde budete:
- Stavať produkčne pripravený MCP server, ktorý automatizuje operácie s GitHub repozitármi
- Implementovať funkciu klonovania GitHub repozitárov cez MCP
- Integrovať vlastné MCP servery s VS Code a GitHub Copilot Agent Mode
- Testovať a nasadzovať vlastné MCP servery v produkčnom prostredí
- Naučiť sa praktickú automatizáciu pracovných postupov pre vývojárov

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
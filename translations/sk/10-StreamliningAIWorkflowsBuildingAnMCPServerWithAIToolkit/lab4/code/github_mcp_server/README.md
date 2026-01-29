# Weather MCP Server

Toto je ukážkový MCP Server v Pythone, ktorý implementuje nástroje na prácu s počasím s fiktívnymi odpoveďami. Môže byť použitý ako základ pre váš vlastný MCP Server. Obsahuje nasledujúce funkcie:

- **Nástroj na počasie**: Nástroj, ktorý poskytuje fiktívne informácie o počasí na základe zadanej lokality.
- **Nástroj na klonovanie Git repozitára**: Nástroj, ktorý klonuje git repozitár do určeného priečinka.
- **Nástroj na otvorenie VS Code**: Nástroj, ktorý otvorí priečinok vo VS Code alebo VS Code Insiders.
- **Pripojenie k Agent Builder**: Funkcia, ktorá umožňuje pripojiť MCP server k Agent Builder na testovanie a ladenie.
- **Ladenie v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkcia, ktorá umožňuje ladiť MCP Server pomocou MCP Inspector.

## Začnite s šablónou Weather MCP Server

> **Predpoklady**
>
> Na spustenie MCP Serveru na vašom lokálnom vývojovom počítači budete potrebovať:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Povinné pre nástroj git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) alebo [VS Code Insiders](https://code.visualstudio.com/insiders/) (Povinné pre nástroj open_in_vscode)
> - (*Voliteľné - ak preferujete uv*) [uv](https://github.com/astral-sh/uv)
> - [Rozšírenie Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Príprava prostredia

Existujú dva spôsoby nastavenia prostredia pre tento projekt. Môžete si vybrať ktorýkoľvek podľa vašich preferencií.

> Poznámka: Po vytvorení virtuálneho prostredia reštartujte VSCode alebo terminál, aby sa použil python z virtuálneho prostredia.

| Prístup | Kroky |
| -------- | ----- |
| Použitie `uv` | 1. Vytvorte virtuálne prostredie: `uv venv` <br>2. Spustite príkaz vo VSCode "***Python: Select Interpreter***" a vyberte python z vytvoreného virtuálneho prostredia <br>3. Nainštalujte závislosti (vrátane vývojových závislostí): `uv pip install -r pyproject.toml --extra dev` |
| Použitie `pip` | 1. Vytvorte virtuálne prostredie: `python -m venv .venv` <br>2. Spustite príkaz vo VSCode "***Python: Select Interpreter***" a vyberte python z vytvoreného virtuálneho prostredia<br>3. Nainštalujte závislosti (vrátane vývojových závislostí): `pip install -e .[dev]` | 

Po nastavení prostredia môžete spustiť server na vašom lokálnom vývojovom počítači cez Agent Builder ako MCP Client a začať:
1. Otvorte panel Debug vo VS Code. Vyberte `Debug in Agent Builder` alebo stlačte `F5` na spustenie ladenia MCP serveru.
2. Použite AI Toolkit Agent Builder na testovanie serveru s [týmto promptom](../../../../../../../../../../../open_prompt_builder). Server bude automaticky pripojený k Agent Builder.
3. Kliknite na `Run` na testovanie serveru s promptom.

**Gratulujeme**! Úspešne ste spustili Weather MCP Server na vašom lokálnom vývojovom počítači cez Agent Builder ako MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Čo je zahrnuté v šablóne

| Priečinok / Súbor | Obsah                                     |
| ----------------- | ----------------------------------------- |
| `.vscode`         | Súbory VSCode na ladenie                 |
| `.aitk`           | Konfigurácie pre AI Toolkit              |
| `src`             | Zdrojový kód pre Weather MCP Server      |

## Ako ladiť Weather MCP Server

> Poznámky:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizuálny nástroj pre vývojárov na testovanie a ladenie MCP serverov.
> - Všetky režimy ladenia podporujú breakpointy, takže môžete pridávať breakpointy do kódu implementácie nástrojov.

## Dostupné nástroje

### Nástroj na počasie
Nástroj `get_weather` poskytuje fiktívne informácie o počasí pre určenú lokalitu.

| Parameter | Typ | Popis |
| --------- | ---- | ----- |
| `location` | string | Lokalita, pre ktorú chcete získať informácie o počasí (napr. názov mesta, štátu alebo súradnice) |

### Nástroj na klonovanie Git repozitára
Nástroj `git_clone_repo` klonuje git repozitár do určeného priečinka.

| Parameter | Typ | Popis |
| --------- | ---- | ----- |
| `repo_url` | string | URL git repozitára, ktorý chcete klonovať |
| `target_folder` | string | Cesta k priečinku, kam má byť repozitár klonovaný |

Nástroj vracia JSON objekt s:
- `success`: Boolean indikujúci, či operácia bola úspešná
- `target_folder` alebo `error`: Cesta ku klonovanému repozitáru alebo chybová správa

### Nástroj na otvorenie VS Code
Nástroj `open_in_vscode` otvorí priečinok vo VS Code alebo aplikácii VS Code Insiders.

| Parameter | Typ | Popis |
| --------- | ---- | ----- |
| `folder_path` | string | Cesta k priečinku, ktorý chcete otvoriť |
| `use_insiders` | boolean (voliteľné) | Či použiť VS Code Insiders namiesto bežného VS Code |

Nástroj vracia JSON objekt s:
- `success`: Boolean indikujúci, či operácia bola úspešná
- `message` alebo `error`: Potvrdzujúca správa alebo chybová správa

| Režim ladenia | Popis | Kroky na ladenie |
| ------------- | ----- | ---------------- |
| Agent Builder | Ladiť MCP server v Agent Builder cez AI Toolkit. | 1. Otvorte panel Debug vo VS Code. Vyberte `Debug in Agent Builder` a stlačte `F5` na spustenie ladenia MCP serveru.<br>2. Použite AI Toolkit Agent Builder na testovanie serveru s [týmto promptom](../../../../../../../../../../../open_prompt_builder). Server bude automaticky pripojený k Agent Builder.<br>3. Kliknite na `Run` na testovanie serveru s promptom. |
| MCP Inspector | Ladiť MCP server pomocou MCP Inspector. | 1. Nainštalujte [Node.js](https://nodejs.org/)<br> 2. Nastavte Inspector: `cd inspector` && `npm install` <br> 3. Otvorte panel Debug vo VS Code. Vyberte `Debug SSE in Inspector (Edge)` alebo `Debug SSE in Inspector (Chrome)`. Stlačte F5 na spustenie ladenia.<br> 4. Keď sa MCP Inspector spustí v prehliadači, kliknite na tlačidlo `Connect` na pripojenie tohto MCP serveru.<br> 5. Potom môžete `List Tools`, vybrať nástroj, zadať parametre a `Run Tool` na ladenie kódu serveru.<br> |

## Predvolené porty a prispôsobenia

| Režim ladenia | Porty | Definície | Prispôsobenia | Poznámka |
| ------------- | ----- | --------- | ------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Upraviť [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) na zmenu vyššie uvedených portov. | N/A |
| MCP Inspector | 3001 (Server); 5173 a 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Upraviť [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) na zmenu vyššie uvedených portov.| N/A |

## Spätná väzba

Ak máte akékoľvek pripomienky alebo návrhy k tejto šablóne, otvorte issue na [GitHub repozitári AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
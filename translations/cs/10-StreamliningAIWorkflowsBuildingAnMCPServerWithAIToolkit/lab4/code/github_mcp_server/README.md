# Weather MCP Server

Toto je ukázkový MCP Server v Pythonu, který implementuje nástroje pro počasí s falešnými odpověďmi. Může být použit jako základ pro váš vlastní MCP Server. Obsahuje následující funkce:

- **Nástroj pro počasí**: Nástroj, který poskytuje falešné informace o počasí na základě zadané lokace.
- **Nástroj pro klonování Git repozitáře**: Nástroj, který klonuje git repozitář do určené složky.
- **Nástroj pro otevření ve VS Code**: Nástroj, který otevře složku ve VS Code nebo VS Code Insiders.
- **Připojení k Agent Builderu**: Funkce, která umožňuje připojit MCP server k Agent Builderu pro testování a ladění.
- **Ladění v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkce, která umožňuje ladit MCP Server pomocí MCP Inspectoru.

## Začínáme s šablonou Weather MCP Server

> **Předpoklady**
>
> Pro spuštění MCP Serveru na vašem lokálním vývojovém stroji budete potřebovat:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Vyžadováno pro nástroj git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) nebo [VS Code Insiders](https://code.visualstudio.com/insiders/) (Vyžadováno pro nástroj open_in_vscode)
> - (*Volitelné - pokud preferujete uv*) [uv](https://github.com/astral-sh/uv)
> - [Rozšíření Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Příprava prostředí

Existují dva způsoby, jak nastavit prostředí pro tento projekt. Můžete si vybrat ten, který vám více vyhovuje.

> Poznámka: Po vytvoření virtuálního prostředí restartujte VSCode nebo terminál, aby se zajistilo použití pythonu z virtuálního prostředí.

| Přístup | Kroky |
| -------- | ----- |
| Použití `uv` | 1. Vytvořte virtuální prostředí: `uv venv` <br>2. Spusťte příkaz ve VSCode "***Python: Select Interpreter***" a vyberte python z vytvořeného virtuálního prostředí <br>3. Nainstalujte závislosti (včetně vývojových závislostí): `uv pip install -r pyproject.toml --extra dev` |
| Použití `pip` | 1. Vytvořte virtuální prostředí: `python -m venv .venv` <br>2. Spusťte příkaz ve VSCode "***Python: Select Interpreter***" a vyberte python z vytvořeného virtuálního prostředí<br>3. Nainstalujte závislosti (včetně vývojových závislostí): `pip install -e .[dev]` | 

Po nastavení prostředí můžete server spustit na svém lokálním vývojovém stroji prostřednictvím Agent Builderu jako MCP Client a začít:
1. Otevřete panel ladění ve VS Code. Vyberte `Debug in Agent Builder` nebo stiskněte `F5` pro spuštění ladění MCP serveru.
2. Použijte AI Toolkit Agent Builder k testování serveru s [tímto promptem](../../../../../../../../../../../open_prompt_builder). Server bude automaticky připojen k Agent Builderu.
3. Klikněte na `Run` pro testování serveru s promptem.

**Gratulujeme**! Úspěšně jste spustili Weather MCP Server na svém lokálním vývojovém stroji prostřednictvím Agent Builderu jako MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Co je součástí šablony

| Složka / Soubor | Obsah                                     |
| ---------------- | ----------------------------------------- |
| `.vscode`        | VSCode soubory pro ladění                |
| `.aitk`          | Konfigurace pro AI Toolkit               |
| `src`            | Zdrojový kód pro Weather MCP Server      |

## Jak ladit Weather MCP Server

> Poznámky:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizuální nástroj pro vývojáře pro testování a ladění MCP serverů.
> - Všechny režimy ladění podporují breakpointy, takže můžete přidávat breakpointy do kódu implementace nástrojů.

## Dostupné nástroje

### Nástroj pro počasí
Nástroj `get_weather` poskytuje falešné informace o počasí pro zadanou lokalitu.

| Parametr | Typ | Popis |
| --------- | ---- | ----------- |
| `location` | string | Lokalita, pro kterou chcete získat informace o počasí (např. název města, stát nebo souřadnice) |

### Nástroj pro klonování Git repozitáře
Nástroj `git_clone_repo` klonuje git repozitář do určené složky.

| Parametr | Typ | Popis |
| --------- | ---- | ----------- |
| `repo_url` | string | URL git repozitáře, který chcete klonovat |
| `target_folder` | string | Cesta ke složce, kam má být repozitář klonován |

Nástroj vrací JSON objekt obsahující:
- `success`: Boolean indikující, zda operace byla úspěšná
- `target_folder` nebo `error`: Cestu ke klonovanému repozitáři nebo chybovou zprávu

### Nástroj pro otevření ve VS Code
Nástroj `open_in_vscode` otevře složku ve VS Code nebo aplikaci VS Code Insiders.

| Parametr | Typ | Popis |
| --------- | ---- | ----------- |
| `folder_path` | string | Cesta ke složce, kterou chcete otevřít |
| `use_insiders` | boolean (volitelné) | Zda použít VS Code Insiders místo běžného VS Code |

Nástroj vrací JSON objekt obsahující:
- `success`: Boolean indikující, zda operace byla úspěšná
- `message` nebo `error`: Potvrzující zprávu nebo chybovou zprávu

| Režim ladění | Popis | Kroky pro ladění |
| ------------ | ----------- | --------------- |
| Agent Builder | Ladění MCP serveru v Agent Builderu prostřednictvím AI Toolkit. | 1. Otevřete panel ladění ve VS Code. Vyberte `Debug in Agent Builder` a stiskněte `F5` pro spuštění ladění MCP serveru.<br>2. Použijte AI Toolkit Agent Builder k testování serveru s [tímto promptem](../../../../../../../../../../../open_prompt_builder). Server bude automaticky připojen k Agent Builderu.<br>3. Klikněte na `Run` pro testování serveru s promptem. |
| MCP Inspector | Ladění MCP serveru pomocí MCP Inspectoru. | 1. Nainstalujte [Node.js](https://nodejs.org/)<br> 2. Nastavte Inspector: `cd inspector` && `npm install` <br> 3. Otevřete panel ladění ve VS Code. Vyberte `Debug SSE in Inspector (Edge)` nebo `Debug SSE in Inspector (Chrome)`. Stiskněte F5 pro spuštění ladění.<br> 4. Když se MCP Inspector spustí v prohlížeči, klikněte na tlačítko `Connect` pro připojení tohoto MCP serveru.<br> 5. Poté můžete `List Tools`, vybrat nástroj, zadat parametry a `Run Tool` pro ladění kódu serveru.<br> |

## Výchozí porty a přizpůsobení

| Režim ladění | Porty | Definice | Přizpůsobení | Poznámka |
| ------------ | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Upravte [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pro změnu výše uvedených portů. | N/A |
| MCP Inspector | 3001 (Server); 5173 a 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Upravte [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) pro změnu výše uvedených portů.| N/A |

## Zpětná vazba

Pokud máte jakoukoli zpětnou vazbu nebo návrhy pro tuto šablonu, otevřete prosím issue na [GitHub repozitáři AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
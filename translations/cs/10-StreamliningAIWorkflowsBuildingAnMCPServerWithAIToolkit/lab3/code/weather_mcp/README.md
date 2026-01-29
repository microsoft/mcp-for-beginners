# Weather MCP Server

Toto je ukázkový MCP Server v Pythonu, který implementuje nástroje pro počasí s falešnými odpověďmi. Může sloužit jako základ pro váš vlastní MCP Server. Obsahuje následující funkce:

- **Weather Tool**: Nástroj, který poskytuje simulované informace o počasí na základě zadané lokality.
- **Připojení k Agent Builderu**: Funkce umožňující připojit MCP server k Agent Builderu pro testování a ladění.
- **Ladění v [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Funkce umožňující ladit MCP Server pomocí MCP Inspectoru.

## Začínáme s šablonou Weather MCP Serveru

> **Požadavky**
>
> Pro spuštění MCP Serveru na vašem lokálním vývojovém počítači budete potřebovat:
>
> - [Python](https://www.python.org/)
> - (*Volitelné - pokud preferujete uv*) [uv](https://github.com/astral-sh/uv)
> - [Rozšíření Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Příprava prostředí

Existují dva způsoby, jak nastavit prostředí pro tento projekt. Vyberte si ten, který vám více vyhovuje.

> Poznámka: Po vytvoření virtuálního prostředí znovu načtěte VSCode nebo terminál, aby se používal python z virtuálního prostředí.

| Přístup | Kroky |
| -------- | ----- |
| Použití `uv` | 1. Vytvořte virtuální prostředí: `uv venv` <br>2. Spusťte příkaz ve VSCode "***Python: Select Interpreter***" a vyberte python z vytvořeného virtuálního prostředí <br>3. Nainstalujte závislosti (včetně vývojových): `uv pip install -r pyproject.toml --extra dev` |
| Použití `pip` | 1. Vytvořte virtuální prostředí: `python -m venv .venv` <br>2. Spusťte příkaz ve VSCode "***Python: Select Interpreter***" a vyberte python z vytvořeného virtuálního prostředí<br>3. Nainstalujte závislosti (včetně vývojových): `pip install -e .[dev]` |

Po nastavení prostředí můžete spustit server na svém lokálním vývojovém počítači přes Agent Builder jako MCP klienta a začít:
1. Otevřete panel ladění ve VS Code. Vyberte `Debug in Agent Builder` nebo stiskněte `F5` pro spuštění ladění MCP serveru.
2. Použijte AI Toolkit Agent Builder k otestování serveru s [tímto promptem](../../../../../../../../../../open_prompt_builder). Server se automaticky připojí k Agent Builderu.
3. Klikněte na `Run` pro otestování serveru s promptem.

**Gratulujeme**! Úspěšně jste spustili Weather MCP Server na svém lokálním vývojovém počítači přes Agent Builder jako MCP klienta.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Co šablona obsahuje

| Složka / Soubor | Obsah                                      |
| --------------- | ------------------------------------------ |
| `.vscode`       | Soubory VSCode pro ladění                   |
| `.aitk`         | Konfigurace pro AI Toolkit                   |
| `src`           | Zdrojový kód Weather MCP serveru             |

## Jak ladit Weather MCP Server

> Poznámky:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) je vizuální nástroj pro vývojáře pro testování a ladění MCP serverů.
> - Všechny režimy ladění podporují breakpointy, takže můžete přidávat breakpointy do kódu implementace nástroje.

| Režim ladění | Popis | Kroky ladění |
| ------------ | ------ | ------------ |
| Agent Builder | Ladění MCP serveru v Agent Builderu přes AI Toolkit. | 1. Otevřete panel ladění ve VS Code. Vyberte `Debug in Agent Builder` a stiskněte `F5` pro spuštění ladění MCP serveru.<br>2. Použijte AI Toolkit Agent Builder k otestování serveru s [tímto promptem](../../../../../../../../../../open_prompt_builder). Server se automaticky připojí k Agent Builderu.<br>3. Klikněte na `Run` pro otestování serveru s promptem. |
| MCP Inspector | Ladění MCP serveru pomocí MCP Inspectoru. | 1. Nainstalujte [Node.js](https://nodejs.org/)<br>2. Nastavte Inspector: `cd inspector` && `npm install` <br>3. Otevřete panel ladění ve VS Code. Vyberte `Debug SSE in Inspector (Edge)` nebo `Debug SSE in Inspector (Chrome)`. Stiskněte F5 pro spuštění ladění.<br>4. Po spuštění MCP Inspectoru v prohlížeči klikněte na tlačítko `Connect` pro připojení tohoto MCP serveru.<br>5. Poté můžete `List Tools`, vybrat nástroj, zadat parametry a `Run Tool` pro ladění vašeho serverového kódu.<br> |

## Výchozí porty a přizpůsobení

| Režim ladění | Porty | Definice | Přizpůsobení | Poznámka |
| ------------ | ----- | -------- | ------------ | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Upravte [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pro změnu těchto portů. | Není k dispozici |
| MCP Inspector | 3001 (Server); 5173 a 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Upravte [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) pro změnu těchto portů. | Není k dispozici |

## Zpětná vazba

Pokud máte jakoukoli zpětnou vazbu nebo návrhy k této šabloně, otevřete prosím issue na [AI Toolkit GitHub repozitáři](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
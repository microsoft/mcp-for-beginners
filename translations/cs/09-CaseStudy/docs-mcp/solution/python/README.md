# Generátor studijního plánu s Chainlit & Microsoft Learn Docs MCP

## Předpoklady

- Python 3.8 nebo vyšší
- pip (správce balíčků pro Python)
- Přístup k internetu pro připojení k serveru Microsoft Learn Docs MCP

## Instalace

1. Naklonujte tento repozitář nebo stáhněte soubory projektu.
2. Nainstalujte požadované závislosti:

   ```bash
   pip install -r requirements.txt
   ```

## Použití

### Scénář 1: Jednoduchý dotaz na Docs MCP
Klient příkazového řádku, který se připojí k serveru Docs MCP, odešle dotaz a zobrazí výsledek.

1. Spusťte skript:
   ```bash
   python scenario1.py
   ```
2. Zadejte svou otázku týkající se dokumentace do výzvy.

### Scénář 2: Generátor studijního plánu (webová aplikace Chainlit)
Webové rozhraní (využívající Chainlit), které umožňuje uživatelům vytvořit personalizovaný studijní plán rozdělený po týdnech pro jakékoli technické téma.

1. Spusťte aplikaci Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Otevřete místní URL, které se zobrazí ve vašem terminálu (např. http://localhost:8000), ve vašem prohlížeči.
3. V chatovacím okně zadejte své studijní téma a počet týdnů, které chcete studovat (např. "certifikace AI-900, 8 týdnů").
4. Aplikace odpoví týdenním studijním plánem, včetně odkazů na relevantní dokumentaci Microsoft Learn.

**Požadované proměnné prostředí:**

Pro použití scénáře 2 (webová aplikace Chainlit s Azure OpenAI) je nutné nastavit následující proměnné prostředí v souboru `.env` ve složce `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Vyplňte tyto hodnoty detaily svého Azure OpenAI zdroje před spuštěním aplikace.

> [!TIP]
> Svůj vlastní model můžete snadno nasadit pomocí [Azure AI Foundry](https://ai.azure.com/).

### Scénář 3: Dokumentace v editoru s MCP serverem ve VS Code

Namísto přepínání mezi záložkami pro hledání dokumentace můžete přinést Microsoft Learn Docs přímo do svého VS Code pomocí MCP serveru. To vám umožní:
- Vyhledávat a číst dokumentaci přímo ve VS Code bez opuštění prostředí pro psaní kódu.
- Vkládat odkazy na dokumentaci přímo do README nebo souborů kurzu.
- Používat GitHub Copilot a MCP společně pro plynulý, AI-poháněný pracovní postup s dokumentací.

**Příklady použití:**
- Rychle přidávat referenční odkazy do README při psaní kurzu nebo projektové dokumentace.
- Používat Copilot k generování kódu a MCP k okamžitému nalezení a citování relevantní dokumentace.
- Zůstat soustředěný ve svém editoru a zvýšit produktivitu.

> [!IMPORTANT]
> Ujistěte se, že máte platnou konfiguraci [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) ve svém pracovním prostoru (umístění je `.vscode/mcp.json`).

## Proč Chainlit pro scénář 2?

Chainlit je moderní open-source framework pro vytváření konverzačních webových aplikací. Umožňuje snadno vytvářet chatovací uživatelská rozhraní, která se připojují k backendovým službám, jako je server Microsoft Learn Docs MCP. Tento projekt využívá Chainlit k poskytování jednoduchého, interaktivního způsobu generování personalizovaných studijních plánů v reálném čase. Díky Chainlit můžete rychle vytvářet a nasazovat chatovací nástroje, které zvyšují produktivitu a podporují učení.

## Co tato aplikace dělá

Tato aplikace umožňuje uživatelům vytvořit personalizovaný studijní plán jednoduše zadáním tématu a délky trvání. Aplikace zpracuje váš vstup, dotáže se serveru Microsoft Learn Docs MCP na relevantní obsah a uspořádá výsledky do strukturovaného plánu rozděleného po týdnech. Doporučení pro každý týden jsou zobrazena v chatu, což usnadňuje sledování a plnění vašich cílů. Integrace zajišťuje, že vždy získáte nejnovější a nejrelevantnější vzdělávací zdroje.

## Ukázkové dotazy

Vyzkoušejte tyto dotazy v chatovacím okně a podívejte se, jak aplikace reaguje:

- `certifikace AI-900, 8 týdnů`
- `Naučit se Azure Functions, 4 týdny`
- `Azure DevOps, 6 týdnů`
- `Datové inženýrství na Azure, 10 týdnů`
- `Microsoft základy bezpečnosti, 5 týdnů`
- `Power Platform, 7 týdnů`
- `Azure AI služby, 12 týdnů`
- `Cloudová architektura, 9 týdnů`

Tyto příklady ukazují flexibilitu aplikace pro různé studijní cíle a časové rámce.

## Reference

- [Chainlit Dokumentace](https://docs.chainlit.io/)
- [MCP Dokumentace](https://github.com/MicrosoftDocs/mcp)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
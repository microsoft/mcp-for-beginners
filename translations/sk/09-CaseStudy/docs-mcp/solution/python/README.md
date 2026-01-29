# Generátor študijného plánu s Chainlit & Microsoft Learn Docs MCP

## Predpoklady

- Python 3.8 alebo novší
- pip (správca balíkov pre Python)
- Prístup na internet na pripojenie k serveru Microsoft Learn Docs MCP

## Inštalácia

1. Naklonujte toto úložisko alebo stiahnite súbory projektu.
2. Nainštalujte potrebné závislosti:

   ```bash
   pip install -r requirements.txt
   ```

## Použitie

### Scenár 1: Jednoduchý dotaz na Docs MCP
Klient príkazového riadku, ktorý sa pripojí k serveru Docs MCP, odošle dotaz a zobrazí výsledok.

1. Spustite skript:
   ```bash
   python scenario1.py
   ```
2. Zadajte svoju otázku týkajúcu sa dokumentácie do výzvy.

### Scenár 2: Generátor študijného plánu (webová aplikácia Chainlit)
Webové rozhranie (využívajúce Chainlit), ktoré umožňuje používateľom generovať personalizovaný, týždeň po týždni štruktúrovaný študijný plán pre akúkoľvek technickú tému.

1. Spustite aplikáciu Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Otvorte lokálnu URL adresu uvedenú vo vašom termináli (napr. http://localhost:8000) vo vašom prehliadači.
3. V chatovom okne zadajte svoju študijnú tému a počet týždňov, ktoré chcete študovať (napr. "certifikácia AI-900, 8 týždňov").
4. Aplikácia odpovie týždeň po týždni štruktúrovaným študijným plánom vrátane odkazov na relevantnú dokumentáciu Microsoft Learn.

**Požadované premenné prostredia:**

Na použitie Scenára 2 (webová aplikácia Chainlit s Azure OpenAI) musíte nastaviť nasledujúce premenné prostredia v súbore `.env` v adresári `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Vyplňte tieto hodnoty podrobnosťami o vašom Azure OpenAI zdroji pred spustením aplikácie.

> [!TIP]
> Svoje vlastné modely môžete jednoducho nasadiť pomocou [Azure AI Foundry](https://ai.azure.com/).

### Scenár 3: Dokumentácia v editore s MCP serverom vo VS Code

Namiesto prepínania medzi kartami prehliadača na vyhľadávanie dokumentácie môžete priniesť Microsoft Learn Docs priamo do vášho VS Code pomocou MCP servera. To vám umožňuje:
- Vyhľadávať a čítať dokumentáciu priamo vo VS Code bez opustenia vášho pracovného prostredia.
- Vkladať odkazy na dokumentáciu priamo do vášho README alebo súborov kurzu.
- Používať GitHub Copilot a MCP spoločne pre plynulý, AI-poháňaný pracovný tok dokumentácie.

**Príklady použitia:**
- Rýchlo pridávať referenčné odkazy do README pri písaní kurzu alebo projektovej dokumentácie.
- Používať Copilot na generovanie kódu a MCP na okamžité vyhľadanie a citovanie relevantnej dokumentácie.
- Zostať sústredený vo vašom editore a zvýšiť produktivitu.

> [!IMPORTANT]
> Uistite sa, že máte platnú konfiguráciu [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) vo vašom pracovnom priestore (umiestnenie je `.vscode/mcp.json`).

## Prečo Chainlit pre Scenár 2?

Chainlit je moderný open-source rámec na tvorbu konverzačných webových aplikácií. Umožňuje jednoducho vytvárať chatové používateľské rozhrania, ktoré sa pripájajú k backendovým službám, ako je server Microsoft Learn Docs MCP. Tento projekt využíva Chainlit na poskytovanie jednoduchého, interaktívneho spôsobu generovania personalizovaných študijných plánov v reálnom čase. Vďaka Chainlit môžete rýchlo vytvárať a nasadzovať chatové nástroje, ktoré zlepšujú produktivitu a učenie.

## Čo táto aplikácia robí

Táto aplikácia umožňuje používateľom vytvoriť personalizovaný študijný plán jednoduchým zadaním témy a trvania. Aplikácia spracuje váš vstup, odošle dotaz na server Microsoft Learn Docs MCP na relevantný obsah a usporiada výsledky do štruktúrovaného plánu týždeň po týždni. Odporúčania na každý týždeň sa zobrazia v chate, čo uľahčuje sledovanie a napredovanie. Integrácia zaručuje, že vždy získate najnovšie a najrelevantnejšie vzdelávacie zdroje.

## Ukážkové dotazy

Vyskúšajte tieto dotazy v chatovom okne, aby ste videli, ako aplikácia reaguje:

- `certifikácia AI-900, 8 týždňov`
- `Naučiť sa Azure Functions, 4 týždne`
- `Azure DevOps, 6 týždňov`
- `Dátové inžinierstvo na Azure, 10 týždňov`
- `Microsoft základy bezpečnosti, 5 týždňov`
- `Power Platform, 7 týždňov`
- `Azure AI služby, 12 týždňov`
- `Cloudová architektúra, 9 týždňov`

Tieto príklady demonštrujú flexibilitu aplikácie pre rôzne vzdelávacie ciele a časové rámce.

## Referencie

- [Chainlit Dokumentácia](https://docs.chainlit.io/)
- [MCP Dokumentácia](https://github.com/MicrosoftDocs/mcp)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
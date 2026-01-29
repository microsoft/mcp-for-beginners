# Pokročilá bezpečnost MCP s Azure Content Safety

Azure Content Safety nabízí několik výkonných nástrojů, které mohou výrazně zvýšit bezpečnost vašich implementací MCP:

## Prompt Shields

Microsoft AI Prompt Shields poskytují silnou ochranu proti přímým i nepřímým útokům typu prompt injection díky:

1. **Pokročilé detekci**: Využívá strojové učení k identifikaci škodlivých instrukcí vložených do obsahu.
2. **Zvýraznění**: Přetváří vstupní text, aby AI systémy lépe rozlišily platné instrukce od vnějších vstupů.
3. **Oddělovačům a označování dat**: Označuje hranice mezi důvěryhodnými a nedůvěryhodnými daty.
4. **Integraci s Content Safety**: Spolupracuje s Azure AI Content Safety při detekci pokusů o jailbreak a škodlivého obsahu.
5. **Průběžným aktualizacím**: Microsoft pravidelně aktualizuje ochranné mechanismy proti novým hrozbám.

## Implementace Azure Content Safety s MCP

Tento přístup nabízí vícestupňovou ochranu:
- Kontrola vstupů před zpracováním
- Validace výstupů před jejich vrácením
- Používání blokovacích seznamů pro známé škodlivé vzory
- Využití neustále aktualizovaných modelů Azure Content Safety

## Zdroje pro Azure Content Safety

Pro více informací o implementaci Azure Content Safety s vašimi MCP servery využijte tyto oficiální zdroje:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Oficiální dokumentace Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Naučte se, jak zabránit útokům typu prompt injection.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Podrobná API reference pro implementaci Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Rychlý průvodce implementací v C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientské knihovny pro různé programovací jazyky.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specifické pokyny pro detekci a prevenci pokusů o jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Nejlepší postupy pro efektivní implementaci content safety.

Pro podrobnější implementaci si prohlédněte náš [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
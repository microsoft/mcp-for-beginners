# Implementace Azure Content Safety s MCP

Pro zvýšení bezpečnosti MCP proti prompt injection, tool poisoning a dalším specifickým zranitelnostem AI se důrazně doporučuje integrace Azure Content Safety.

## Integrace s MCP serverem

Pro integraci Azure Content Safety s vaším MCP serverem přidejte filtr content safety jako middleware do zpracovatelského řetězce požadavků:

1. Inicializujte filtr při spuštění serveru  
2. Validujte všechny příchozí požadavky na nástroje před jejich zpracováním  
3. Kontrolujte všechny odchozí odpovědi před jejich odesláním klientům  
4. Logujte a upozorňujte na porušení bezpečnostních pravidel  
5. Implementujte vhodné zpracování chyb při neúspěšných kontrolách content safety  

Tím zajistíte silnou ochranu proti:  
- útokům typu prompt injection  
- pokusům o tool poisoning  
- exfiltraci dat pomocí škodlivých vstupů  
- generování škodlivého obsahu  

## Nejlepší postupy pro integraci Azure Content Safety

1. **Vlastní bloklisty**: Vytvořte vlastní bloklisty speciálně pro MCP injection vzory  
2. **Ladění závažnosti**: Přizpůsobte prahové hodnoty závažnosti podle konkrétního použití a úrovně rizika  
3. **Komplexní pokrytí**: Aplikujte kontroly content safety na všechny vstupy i výstupy  
4. **Optimalizace výkonu**: Zvažte implementaci cache pro opakované kontroly content safety  
5. **Náhradní mechanismy**: Definujte jasné fallback chování pro případy nedostupnosti služeb content safety  
6. **Zpětná vazba uživatelům**: Poskytujte uživatelům jasné informace, když je obsah zablokován kvůli bezpečnostním důvodům  
7. **Nepřetržité zlepšování**: Pravidelně aktualizujte bloklisty a vzory na základě nově vznikajících hrozeb

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
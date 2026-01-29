# Implementácia Azure Content Safety s MCP

Pre zvýšenie bezpečnosti MCP proti prompt injection, tool poisoning a ďalším špecifickým zraniteľnostiam AI sa dôrazne odporúča integrácia Azure Content Safety.

## Integrácia s MCP serverom

Pre integráciu Azure Content Safety s vaším MCP serverom pridajte filter content safety ako middleware do vášho spracovateľského reťazca požiadaviek:

1. Inicializujte filter počas spustenia servera  
2. Overte všetky prichádzajúce požiadavky na nástroje pred ich spracovaním  
3. Skontrolujte všetky odchádzajúce odpovede pred ich odoslaním klientom  
4. Logujte a upozorňujte na porušenia bezpečnosti  
5. Implementujte vhodné spracovanie chýb pri neúspešných kontrolách content safety  

Týmto zabezpečíte silnú ochranu proti:  
- útokom prompt injection  
- pokusom o tool poisoning  
- exfiltrácii dát cez škodlivé vstupy  
- generovaniu škodlivého obsahu  

## Najlepšie postupy pre integráciu Azure Content Safety

1. **Vlastné blokovacie zoznamy**: Vytvorte vlastné blokovacie zoznamy špecificky pre MCP injection vzory  
2. **Nastavenie závažnosti**: Prispôsobte prahové hodnoty závažnosti podľa vášho konkrétneho prípadu použitia a tolerancie rizika  
3. **Komplexné pokrytie**: Aplikujte kontroly content safety na všetky vstupy aj výstupy  
4. **Optimalizácia výkonu**: Zvážte implementáciu cache pre opakované kontroly content safety  
5. **Náhradné mechanizmy**: Definujte jasné náhradné správanie, keď služby content safety nie sú dostupné  
6. **Spätná väzba pre používateľov**: Poskytujte používateľom jasnú spätnú väzbu, keď je obsah zablokovaný z dôvodu bezpečnostných obáv  
7. **Kontinuálne zlepšovanie**: Pravidelne aktualizujte blokovacie zoznamy a vzory na základe nových hrozieb

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
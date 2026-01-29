# Pokročilá bezpečnosť MCP s Azure Content Safety

Azure Content Safety ponúka niekoľko výkonných nástrojov, ktoré môžu výrazne zvýšiť bezpečnosť vašich implementácií MCP:

## Prompt Shields

AI Prompt Shields od Microsoftu poskytujú silnú ochranu proti priamym aj nepriamym útokom typu prompt injection prostredníctvom:

1. **Pokročilá detekcia**: Využíva strojové učenie na identifikáciu škodlivých inštrukcií vložených v obsahu.
2. **Zvýraznenie**: Transformuje vstupný text, aby AI systémy vedeli rozlíšiť platné inštrukcie od externých vstupov.
3. **Delimitery a označovanie dát**: Označuje hranice medzi dôveryhodnými a nedôveryhodnými dátami.
4. **Integrácia s Content Safety**: Spolupracuje s Azure AI Content Safety na detekciu pokusov o jailbreak a škodlivého obsahu.
5. **Priebežné aktualizácie**: Microsoft pravidelne aktualizuje ochranné mechanizmy proti novým hrozbám.

## Implementácia Azure Content Safety s MCP

Tento prístup poskytuje viacvrstvovú ochranu:
- Skenovanie vstupov pred spracovaním
- Overovanie výstupov pred ich vrátením
- Používanie bloklistov pre známe škodlivé vzory
- Využitie neustále aktualizovaných modelov Azure Content Safety

## Zdroje pre Azure Content Safety

Ak chcete získať viac informácií o implementácii Azure Content Safety s vašimi MCP servermi, pozrite si tieto oficiálne zdroje:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Oficiálna dokumentácia k Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Naučte sa, ako predchádzať útokom typu prompt injection.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Podrobná API referencia pre implementáciu Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Rýchly návod na implementáciu pomocou C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientské knižnice pre rôzne programovacie jazyky.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Špecifické odporúčania na detekciu a prevenciu pokusov o jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Najlepšie postupy pre efektívnu implementáciu content safety.

Pre podrobnejšiu implementáciu si pozrite náš [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
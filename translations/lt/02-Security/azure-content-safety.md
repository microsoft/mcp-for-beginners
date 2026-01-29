# Pažangi MCP sauga su Azure Content Safety

Azure Content Safety siūlo keletą galingų įrankių, kurie gali sustiprinti jūsų MCP įgyvendinimų saugumą:

## Prompt Shields

Microsoft AI Prompt Shields užtikrina patikimą apsaugą nuo tiesioginių ir netiesioginių prompt injection atakų per:

1. **Pažangų aptikimą**: Naudoja mašininį mokymąsi, kad identifikuotų kenksmingas instrukcijas, įterptas į turinį.
2. **Spotlighting**: Transformuoja įvesties tekstą, kad AI sistemos galėtų atskirti galiojančias instrukcijas nuo išorinių įvesties duomenų.
3. **Ribotuvus ir duomenų žymėjimą**: Žymi ribas tarp patikimų ir nepatikimų duomenų.
4. **Integraciją su Content Safety**: Veikia kartu su Azure AI Content Safety, kad aptiktų jailbreak bandymus ir kenksmingą turinį.
5. **Nuolatinius atnaujinimus**: Microsoft reguliariai atnaujina apsaugos mechanizmus prieš naujas grėsmes.

## Azure Content Safety įgyvendinimas MCP

Šis metodas užtikrina daugiapakopę apsaugą:
- Įvesties nuskaitymas prieš apdorojimą
- Išvesties patikrinimas prieš pateikimą
- Žinomų kenksmingų šablonų blokavimas
- Azure nuolat atnaujinamų turinio saugumo modelių naudojimas

## Azure Content Safety ištekliai

Norėdami sužinoti daugiau apie Azure Content Safety įgyvendinimą su jūsų MCP serveriais, peržiūrėkite šiuos oficialius išteklius:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Oficialūs dokumentai apie Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Sužinokite, kaip išvengti prompt injection atakų.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Išsamus API vadovas Content Safety įgyvendinimui.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Greito įgyvendinimo vadovas naudojant C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientų bibliotekos įvairioms programavimo kalboms.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Konkretūs patarimai, kaip aptikti ir užkirsti kelią jailbreak bandymams.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Geriausios praktikos efektyviam turinio saugumui įgyvendinti.

Norėdami gauti išsamesnį įgyvendinimo vadovą, peržiūrėkite mūsų [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.
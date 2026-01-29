# Azure Content Safety diegimas su MCP

Norint sustiprinti MCP saugumą nuo užklausų injekcijų, įrankių užnuodijimo ir kitų AI specifinių pažeidžiamumų, labai rekomenduojama integruoti Azure Content Safety.

## Integracija su MCP serveriu

Norėdami integruoti Azure Content Safety su savo MCP serveriu, pridėkite turinio saugos filtrą kaip tarpinius programinės įrangos sluoksnius užklausų apdorojimo grandinėje:

1. Inicijuokite filtrą serverio paleidimo metu
2. Patikrinkite visas gaunamas įrankių užklausas prieš jas apdorodami
3. Patikrinkite visus siunčiamus atsakymus prieš juos grąžindami klientams
4. Registruokite ir praneškite apie saugumo pažeidimus
5. Įgyvendinkite tinkamą klaidų tvarkymą, jei turinio saugos patikrinimai nepavyksta

Tai užtikrina patikimą apsaugą nuo:
- Užklausų injekcijų atakų
- Įrankių užnuodijimo bandymų
- Duomenų nutekėjimo per kenkėjiškus įvesties duomenis
- Kenksmingo turinio generavimo

## Geriausios praktikos Azure Content Safety integracijai

1. **Individualūs blokavimo sąrašai**: Sukurkite individualius blokavimo sąrašus, skirtus MCP injekcijų modeliams
2. **Sunkumo lygio reguliavimas**: Koreguokite sunkumo slenksčius pagal savo specifinį naudojimo atvejį ir rizikos toleranciją
3. **Visapusiška aprėptis**: Taikykite turinio saugos patikrinimus visoms įvestims ir išvestims
4. **Našumo optimizavimas**: Apsvarstykite galimybę įdiegti talpyklą pakartotiniams turinio saugos patikrinimams
5. **Atsarginiai mechanizmai**: Apibrėžkite aiškų veiksmų planą, kai turinio saugos paslaugos tampa nepasiekiamos
6. **Vartotojų atsiliepimai**: Suteikite aiškų grįžtamąjį ryšį vartotojams, kai turinys yra blokuojamas dėl saugumo priežasčių
7. **Nuolatinis tobulinimas**: Reguliariai atnaujinkite blokavimo sąrašus ir modelius, atsižvelgdami į naujas grėsmes

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
# MCP stdio serverio sprendimai

> **⚠️ Svarbu**: Šie sprendimai buvo atnaujinti, kad naudotų **stdio transportą**, kaip rekomenduojama MCP specifikacijoje 2025-06-18. Originalus SSE (Server-Sent Events) transportas buvo pasenęs.

Čia pateikiami pilni sprendimai, kaip kurti MCP serverius naudojant stdio transportą kiekvienoje vykdymo aplinkoje:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Pilnas stdio serverio įgyvendinimas
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Python stdio serveris su asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - .NET stdio serveris su priklausomybių injekcija

Kiekviename sprendime pademonstruojama:
- Stdio transporto nustatymas
- Serverio įrankių apibrėžimas
- Tinkamas JSON-RPC žinučių apdorojimas
- Integracija su MCP klientais, tokiais kaip Claude

Visi sprendimai atitinka dabartinę MCP specifikaciją ir naudoja rekomenduojamą stdio transportą, siekiant užtikrinti optimalų našumą ir saugumą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
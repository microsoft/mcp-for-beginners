# Avancerad MCP-säkerhet med Azure Content Safety

Azure Content Safety erbjuder flera kraftfulla verktyg som kan förbättra säkerheten i dina MCP-implementationer:

## Prompt Shields

Microsofts AI Prompt Shields ger starkt skydd mot både direkta och indirekta promptinjektionsattacker genom:

1. **Avancerad detektion**: Använder maskininlärning för att identifiera skadliga instruktioner inbäddade i innehåll.
2. **Spotlighting**: Omvandlar inmatad text för att hjälpa AI-system att skilja mellan giltiga instruktioner och externa indata.
3. **Avgränsare och datamärkning**: Markerar gränser mellan betrodda och obetrodda data.
4. **Integration med Content Safety**: Samarbetar med Azure AI Content Safety för att upptäcka jailbreak-försök och skadligt innehåll.
5. **Kontinuerliga uppdateringar**: Microsoft uppdaterar regelbundet skyddsmekanismer mot nya hot.

## Implementering av Azure Content Safety med MCP

Denna metod ger ett flerskiktat skydd:
- Skanning av indata innan bearbetning
- Validering av utdata innan de returneras
- Användning av blocklistor för kända skadliga mönster
- Utnyttjande av Azures kontinuerligt uppdaterade modeller för innehållssäkerhet

## Azure Content Safety-resurser

För att lära dig mer om hur du implementerar Azure Content Safety med dina MCP-servrar, se dessa officiella resurser:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Officiell dokumentation för Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Lär dig hur du förhindrar promptinjektionsattacker.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detaljerad API-referens för att implementera Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Snabbguide för implementation med C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientbibliotek för olika programmeringsspråk.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specifika riktlinjer för att upptäcka och förhindra jailbreak-försök.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Bästa praxis för effektiv implementering av innehållssäkerhet.

För en mer djupgående implementation, se vår [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
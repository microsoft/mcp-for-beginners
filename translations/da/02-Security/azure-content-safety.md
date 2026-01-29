# Avanceret MCP-sikkerhed med Azure Content Safety

Azure Content Safety tilbyder flere kraftfulde værktøjer, der kan styrke sikkerheden i dine MCP-implementeringer:

## Prompt Shields

Microsofts AI Prompt Shields giver solid beskyttelse mod både direkte og indirekte prompt-injektionsangreb gennem:

1. **Avanceret detektion**: Bruger maskinlæring til at identificere skadelige instruktioner indlejret i indhold.
2. **Spotlighting**: Omformer inputtekst for at hjælpe AI-systemer med at skelne mellem gyldige instruktioner og eksterne input.
3. **Afgrænsere og datamarkering**: Marker grænser mellem betroede og utroværdige data.
4. **Integration med Content Safety**: Arbejder sammen med Azure AI Content Safety for at opdage jailbreak-forsøg og skadeligt indhold.
5. **Løbende opdateringer**: Microsoft opdaterer regelmæssigt beskyttelsesmekanismer mod nye trusler.

## Implementering af Azure Content Safety med MCP

Denne tilgang giver flerlagsbeskyttelse:
- Scanning af input før behandling
- Validering af output før returnering
- Brug af bloklister for kendte skadelige mønstre
- Udnyttelse af Azures løbende opdaterede content safety-modeller

## Azure Content Safety-ressourcer

For at lære mere om implementering af Azure Content Safety med dine MCP-servere, kan du konsultere disse officielle ressourcer:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Officiel dokumentation for Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Lær hvordan du forhindrer prompt-injektionsangreb.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detaljeret API-reference til implementering af Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Hurtig implementeringsguide med C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientbiblioteker til forskellige programmeringssprog.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specifik vejledning til at opdage og forhindre jailbreak-forsøg.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Bedste praksis for effektiv implementering af content safety.

For en mere dybdegående implementering, se vores [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
# Avansert MCP-sikkerhet med Azure Content Safety

Azure Content Safety tilbyr flere kraftige verktøy som kan styrke sikkerheten i dine MCP-implementasjoner:

## Prompt Shields

Microsofts AI Prompt Shields gir solid beskyttelse mot både direkte og indirekte prompt-injeksjonsangrep gjennom:

1. **Avansert deteksjon**: Bruker maskinlæring for å identifisere ondsinnede instruksjoner skjult i innhold.
2. **Spotlighting**: Omformer inndata for å hjelpe AI-systemer med å skille mellom gyldige instruksjoner og eksterne input.
3. **Avgrensere og datamerking**: Marker grenser mellom pålitelig og upålitelig data.
4. **Integrasjon med Content Safety**: Samarbeider med Azure AI Content Safety for å oppdage jailbreak-forsøk og skadelig innhold.
5. **Kontinuerlige oppdateringer**: Microsoft oppdaterer jevnlig beskyttelsesmekanismer mot nye trusler.

## Implementering av Azure Content Safety med MCP

Denne tilnærmingen gir flerlagsbeskyttelse:
- Skanning av input før behandling
- Validering av output før retur
- Bruk av blokkeringlister for kjente skadelige mønstre
- Utnyttelse av Azures kontinuerlig oppdaterte modeller for innholdssikkerhet

## Azure Content Safety-ressurser

For å lære mer om hvordan du implementerer Azure Content Safety med dine MCP-servere, se disse offisielle ressursene:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Offisiell dokumentasjon for Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Lær hvordan du kan forhindre prompt-injeksjonsangrep.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detaljert API-referanse for implementering av Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Rask implementeringsguide med C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klientbiblioteker for ulike programmeringsspråk.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Spesifikk veiledning for å oppdage og forhindre jailbreak-forsøk.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Beste praksis for effektiv implementering av innholdssikkerhet.

For en mer grundig implementering, se vår [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
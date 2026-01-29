# Studieplan-generator med Chainlit & Microsoft Learn Docs MCP

## Forutsetninger

- Python 3.8 eller nyere
- pip (Python-pakkebehandler)
- Internett-tilgang for å koble til Microsoft Learn Docs MCP-serveren

## Installasjon

1. Klon dette repositoriet eller last ned prosjektfilene.
2. Installer nødvendige avhengigheter:

   ```bash
   pip install -r requirements.txt
   ```

## Bruk

### Scenario 1: Enkel spørring til Docs MCP
En kommandolinjeklient som kobler til Docs MCP-serveren, sender en spørring og viser resultatet.

1. Kjør skriptet:
   ```bash
   python scenario1.py
   ```
2. Skriv inn ditt dokumentasjonsspørsmål i terminalen.

### Scenario 2: Studieplan-generator (Chainlit webapp)
Et nettbasert grensesnitt (ved bruk av Chainlit) som lar brukere generere en personlig, uke-for-uke studieplan for et hvilket som helst teknisk emne.

1. Start Chainlit-appen:
   ```bash
   chainlit run scenario2.py
   ```
2. Åpne den lokale URL-en som vises i terminalen (f.eks. http://localhost:8000) i nettleseren din.
3. I chat-vinduet, skriv inn ditt studietema og antall uker du ønsker å studere (f.eks. "AI-900 sertifisering, 8 uker").
4. Appen vil svare med en uke-for-uke studieplan, inkludert lenker til relevant Microsoft Learn-dokumentasjon.

**Nødvendige miljøvariabler:**

For å bruke Scenario 2 (Chainlit webapp med Azure OpenAI), må du sette følgende miljøvariabler i en `.env`-fil i `python`-katalogen:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fyll inn disse verdiene med detaljene for din Azure OpenAI-ressurs før du kjører appen.

> [!TIP]
> Du kan enkelt distribuere dine egne modeller ved å bruke [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Dokumentasjon i editor med MCP-server i VS Code

I stedet for å bytte nettleserfaner for å søke etter dokumentasjon, kan du få Microsoft Learn Docs direkte inn i VS Code ved hjelp av MCP-serveren. Dette lar deg:
- Søke og lese dokumentasjon inne i VS Code uten å forlate kodeeditoren.
- Referere til dokumentasjon og sette inn lenker direkte i README- eller kursfiler.
- Bruke GitHub Copilot og MCP sammen for en sømløs, AI-drevet dokumentasjonsarbeidsflyt.

**Eksempler på bruk:**
- Raskt legge til referanselenker i en README mens du skriver kurs- eller prosjekt-dokumentasjon.
- Bruke Copilot til å generere kode og MCP til å finne og sitere relevant dokumentasjon umiddelbart.
- Holde fokus i editoren og øke produktiviteten.

> [!IMPORTANT]
> Sørg for at du har en gyldig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json)-konfigurasjon i arbeidsområdet ditt (plassering er `.vscode/mcp.json`).

## Hvorfor bruke Chainlit for Scenario 2?

Chainlit er et moderne, åpen kildekode-rammeverk for å bygge samtalebaserte webapplikasjoner. Det gjør det enkelt å lage chat-baserte brukergrensesnitt som kobler til backend-tjenester som Microsoft Learn Docs MCP-serveren. Dette prosjektet bruker Chainlit for å tilby en enkel, interaktiv måte å generere personlige studieplaner i sanntid. Ved å bruke Chainlit kan du raskt bygge og distribuere chat-baserte verktøy som forbedrer produktivitet og læring.

## Hva denne appen gjør

Denne appen lar brukere lage en personlig studieplan ved å bare skrive inn et tema og en varighet. Appen analyserer inputen din, sender spørringer til Microsoft Learn Docs MCP-serveren for relevant innhold, og organiserer resultatene i en strukturert, uke-for-uke plan. Hver ukes anbefalinger vises i chatten, noe som gjør det enkelt å følge og spore fremgangen din. Integrasjonen sikrer at du alltid får de nyeste og mest relevante læringsressursene.

## Eksempelspørringer

Prøv disse spørringene i chat-vinduet for å se hvordan appen svarer:

- `AI-900 sertifisering, 8 uker`
- `Lær Azure Functions, 4 uker`
- `Azure DevOps, 6 uker`
- `Data engineering på Azure, 10 uker`
- `Microsoft sikkerhetsgrunnlag, 5 uker`
- `Power Platform, 7 uker`
- `Azure AI-tjenester, 12 uker`
- `Skyarkitektur, 9 uker`

Disse eksemplene viser fleksibiliteten til appen for ulike læringsmål og tidsrammer.

## Referanser

- [Chainlit Dokumentasjon](https://docs.chainlit.io/)
- [MCP Dokumentasjon](https://github.com/MicrosoftDocs/mcp)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
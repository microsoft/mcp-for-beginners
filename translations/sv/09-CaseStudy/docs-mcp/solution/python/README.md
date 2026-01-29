# Studieplan Generator med Chainlit & Microsoft Learn Docs MCP

## Förutsättningar

- Python 3.8 eller högre
- pip (Python-pakethanterare)
- Internetanslutning för att koppla upp mot Microsoft Learn Docs MCP-servern

## Installation

1. Klona detta repository eller ladda ner projektfilerna.
2. Installera de nödvändiga beroendena:

   ```bash
   pip install -r requirements.txt
   ```

## Användning

### Scenario 1: Enkel fråga till Docs MCP
En kommandoradsklient som ansluter till Docs MCP-servern, skickar en fråga och skriver ut resultatet.

1. Kör skriptet:
   ```bash
   python scenario1.py
   ```
2. Ange din dokumentationsfråga vid prompten.

### Scenario 2: Studieplan Generator (Chainlit Web App)
Ett webbaserat gränssnitt (med Chainlit) som låter användare skapa en personlig, veckovis studieplan för valfritt tekniskt ämne.

1. Starta Chainlit-appen:
   ```bash
   chainlit run scenario2.py
   ```
2. Öppna den lokala URL:en som visas i din terminal (t.ex. http://localhost:8000) i din webbläsare.
3. I chattfönstret, ange ditt studietema och antalet veckor du vill studera (t.ex. "AI-900 certifiering, 8 veckor").
4. Appen svarar med en veckovis studieplan, inklusive länkar till relevant Microsoft Learn-dokumentation.

**Nödvändiga miljövariabler:**

För att använda Scenario 2 (Chainlit-webbappen med Azure OpenAI) måste du ange följande miljövariabler i en `.env`-fil i `python`-katalogen:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fyll i dessa värden med dina Azure OpenAI-resursuppgifter innan du kör appen.

> [!TIP]
> Du kan enkelt distribuera dina egna modeller med [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Dokumentation i editor med MCP-server i VS Code

Istället för att växla mellan webbläsarflikar för att söka dokumentation kan du ta med Microsoft Learn Docs direkt in i din VS Code med MCP-servern. Detta gör det möjligt att:
- Söka och läsa dokumentation direkt i VS Code utan att lämna din kodmiljö.
- Referera dokumentation och infoga länkar direkt i din README eller kursfiler.
- Använda GitHub Copilot och MCP tillsammans för ett smidigt, AI-drivet dokumentationsflöde.

**Exempel på användningsområden:**
- Snabbt lägga till referenslänkar i en README medan du skriver kurs- eller projekt-dokumentation.
- Använda Copilot för att generera kod och MCP för att direkt hitta och citera relevant dokumentation.
- Hålla fokus i din editor och öka produktiviteten.

> [!IMPORTANT]
> Se till att du har en giltig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json)-konfiguration i din arbetsyta (platsen är `.vscode/mcp.json`).

## Varför Chainlit för Scenario 2?

Chainlit är ett modernt open source-ramverk för att bygga konversationsbaserade webbapplikationer. Det gör det enkelt att skapa chattbaserade användargränssnitt som ansluter till backend-tjänster som Microsoft Learn Docs MCP-servern. Detta projekt använder Chainlit för att erbjuda ett enkelt, interaktivt sätt att skapa personliga studieplaner i realtid. Genom att använda Chainlit kan du snabbt bygga och distribuera chattbaserade verktyg som förbättrar produktivitet och lärande.

## Vad gör denna app?

Denna app låter användare skapa en personlig studieplan genom att helt enkelt ange ett ämne och en tidsperiod. Appen analyserar din input, frågar Microsoft Learn Docs MCP-servern om relevant innehåll och organiserar resultaten i en strukturerad, veckovis plan. Varje veckas rekommendationer visas i chatten, vilket gör det enkelt att följa och spåra din framsteg. Integrationen säkerställer att du alltid får de senaste och mest relevanta lärresurserna.

## Exempel på frågor

Prova dessa frågor i chattfönstret för att se hur appen svarar:

- `AI-900 certifiering, 8 veckor`
- `Lär dig Azure Functions, 4 veckor`
- `Azure DevOps, 6 veckor`
- `Data engineering på Azure, 10 veckor`
- `Microsoft säkerhetsgrunder, 5 veckor`
- `Power Platform, 7 veckor`
- `Azure AI-tjänster, 12 veckor`
- `Molnarkitektur, 9 veckor`

Dessa exempel visar appens flexibilitet för olika lärandemål och tidsramar.

## Referenser

- [Chainlit Dokumentation](https://docs.chainlit.io/)
- [MCP Dokumentation](https://github.com/MicrosoftDocs/mcp)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
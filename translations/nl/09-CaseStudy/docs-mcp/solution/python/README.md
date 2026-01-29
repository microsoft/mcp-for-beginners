# Studieplangenerator met Chainlit & Microsoft Learn Docs MCP

## Vereisten

- Python 3.8 of hoger
- pip (Python package manager)
- Internettoegang om verbinding te maken met de Microsoft Learn Docs MCP-server

## Installatie

1. Clone deze repository of download de projectbestanden.
2. Installeer de benodigde afhankelijkheden:

   ```bash
   pip install -r requirements.txt
   ```

## Gebruik

### Scenario 1: Eenvoudige Query naar Docs MCP
Een command-line client die verbinding maakt met de Docs MCP-server, een query verstuurt en het resultaat weergeeft.

1. Voer het script uit:
   ```bash
   python scenario1.py
   ```
2. Voer je documentatievraag in bij de prompt.

### Scenario 2: Studieplangenerator (Chainlit Web App)
Een webinterface (met Chainlit) waarmee gebruikers een gepersonaliseerd, week-tot-week studieplan kunnen genereren voor elk technisch onderwerp.

1. Start de Chainlit-app:
   ```bash
   chainlit run scenario2.py
   ```
2. Open de lokale URL die in je terminal wordt weergegeven (bijv. http://localhost:8000) in je browser.
3. Voer in het chatvenster je studiethema en het aantal weken in dat je wilt studeren (bijv. "AI-900 certificering, 8 weken").
4. De app reageert met een week-tot-week studieplan, inclusief links naar relevante Microsoft Learn-documentatie.

**Vereiste Omgevingsvariabelen:**

Om Scenario 2 (de Chainlit-webapp met Azure OpenAI) te gebruiken, moet je de volgende omgevingsvariabelen instellen in een `.env`-bestand in de `python`-directory:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Vul deze waarden in met de details van je Azure OpenAI-resource voordat je de app uitvoert.

> [!TIP]
> Je kunt eenvoudig je eigen modellen implementeren met [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Documentatie in de Editor met MCP-server in VS Code

In plaats van te schakelen tussen browsertabbladen om documentatie te zoeken, kun je Microsoft Learn Docs rechtstreeks in je VS Code brengen met behulp van de MCP-server. Dit stelt je in staat om:
- Documentatie te zoeken en te lezen binnen VS Code zonder je ontwikkelomgeving te verlaten.
- Verwijzingen naar documentatie toe te voegen en links direct in je README of cursusbestanden in te voegen.
- GitHub Copilot en MCP samen te gebruiken voor een naadloze, AI-gestuurde documentatieworkflow.

**Voorbeelden van Gebruikssituaties:**
- Snel referentielinks toevoegen aan een README tijdens het schrijven van een cursus of projectdocumentatie.
- Copilot gebruiken om code te genereren en MCP om direct relevante documentatie te vinden en te citeren.
- Gefocust blijven in je editor en je productiviteit verhogen.

> [!IMPORTANT]
> Zorg ervoor dat je een geldige [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuratie hebt in je werkruimte (locatie is `.vscode/mcp.json`).

## Waarom Chainlit voor Scenario 2?

Chainlit is een modern open-source framework voor het bouwen van conversatiegerichte webapplicaties. Het maakt het eenvoudig om chatgebaseerde gebruikersinterfaces te creëren die verbinding maken met back-endservices zoals de Microsoft Learn Docs MCP-server. Dit project gebruikt Chainlit om een eenvoudige, interactieve manier te bieden om in real-time gepersonaliseerde studieplannen te genereren. Door gebruik te maken van Chainlit kun je snel chatgebaseerde tools bouwen en implementeren die productiviteit en leren verbeteren.

## Wat Deze App Doet

Deze app stelt gebruikers in staat om een gepersonaliseerd studieplan te maken door simpelweg een onderwerp en een duur in te voeren. De app verwerkt je invoer, doet een query naar de Microsoft Learn Docs MCP-server voor relevante inhoud, en organiseert de resultaten in een gestructureerd, week-tot-week plan. De aanbevelingen per week worden weergegeven in de chat, waardoor het eenvoudig is om te volgen en je voortgang bij te houden. De integratie zorgt ervoor dat je altijd de meest actuele en relevante leermiddelen krijgt.

## Voorbeeldvragen

Probeer deze vragen in het chatvenster om te zien hoe de app reageert:

- `AI-900 certificering, 8 weken`
- `Leer Azure Functions, 4 weken`
- `Azure DevOps, 6 weken`
- `Data engineering op Azure, 10 weken`
- `Microsoft security fundamentals, 5 weken`
- `Power Platform, 7 weken`
- `Azure AI-services, 12 weken`
- `Cloudarchitectuur, 9 weken`

Deze voorbeelden tonen de flexibiliteit van de app voor verschillende leerdoelen en tijdschema's.

## Referenties

- [Chainlit Documentatie](https://docs.chainlit.io/)
- [MCP Documentatie](https://github.com/MicrosoftDocs/mcp)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
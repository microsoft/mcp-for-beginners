# சுயபயிற்சி திட்ட உருவாக்கி (Study Plan Generator) - Chainlit & Microsoft Learn Docs MCP

## முன்பதிவுகள்

- Python 3.8 அல்லது அதற்கு மேல்
- pip (Python package manager)
- Microsoft Learn Docs MCP சர்வருடன் இணைக்க இணைய அணுகல்

## நிறுவல்

1. இந்த repository-யை clone செய்யவும் அல்லது திட்ட கோப்புகளை பதிவிறக்கவும்.
2. தேவையான dependencies-ஐ நிறுவவும்:

   ```bash
   pip install -r requirements.txt
   ```

## பயன்பாடு

### நிலை 1: Docs MCP-க்கு எளிய கேள்வி
Docs MCP சர்வருடன் இணைக்கும் ஒரு command-line client, கேள்வியை அனுப்பி, முடிவுகளை அச்சிடுகிறது.

1. ஸ்கிரிப்டை இயக்கவும்:
   ```bash
   python scenario1.py
   ```
2. உங்களின் ஆவண கேள்வியை prompt-ல் உள்ளிடவும்.

### நிலை 2: சுயபயிற்சி திட்ட உருவாக்கி (Chainlit Web App)
Chainlit-ஐ பயன்படுத்தி, எந்த தொழில்நுட்ப தலைப்பிற்கும் தனிப்பயன் வார வார பயிற்சி திட்டத்தை உருவாக்க அனுமதிக்கும் ஒரு வலை அடிப்படையிலான இடைமுகம்.

1. Chainlit app-ஐ தொடங்கவும்:
   ```bash
   chainlit run scenario2.py
   ```
2. உங்களின் browser-ல் terminal-ல் வழங்கப்பட்ட உள்ளூர் URL-ஐ (எ.கா., http://localhost:8000) திறக்கவும்.
3. Chat window-ல் உங்களின் பயிற்சி தலைப்பையும், நீங்கள் படிக்க விரும்பும் வாரங்களின் எண்ணிக்கையையும் உள்ளிடவும் (எ.கா., "AI-900 certification, 8 weeks").
4. App, Microsoft Learn ஆவணங்களுக்கான இணைப்புகளை உள்ளடக்கிய வார வார பயிற்சி திட்டத்தை பதிலளிக்கும்.

**தேவையான சூழல் மாறிகள்:**

Scenario 2 (Azure OpenAI உடன் Chainlit web app) பயன்படுத்த, `.env` கோப்பில் பின்வரும் சூழல் மாறிகளை `python` கோப்பகத்தில் அமைக்க வேண்டும்:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

App-ஐ இயக்குவதற்கு முன், உங்கள் Azure OpenAI resource விவரங்களை இங்கு நிரப்பவும்.

> [!TIP]
> [Azure AI Foundry](https://ai.azure.com/) பயன்படுத்தி உங்கள் சொந்த மாடல்களை எளிதாக deploy செய்யலாம்.

### நிலை 3: VS Code-ல் MCP சர்வருடன் உள்ள ஆவணங்கள்

ஆவணங்களை தேட browser tabs-ஐ மாற்றுவதற்கு பதிலாக, Microsoft Learn Docs-ஐ நேரடியாக உங்கள் VS Code-ல் கொண்டு வரலாம். இது உங்களுக்கு:
- உங்கள் coding சூழலில் இருந்து விலகாமல் ஆவணங்களை தேடவும், படிக்கவும் உதவுகிறது.
- README அல்லது course கோப்புகளில் இணைப்புகளை நேரடியாக சேர்க்கவும்.
- GitHub Copilot மற்றும் MCP-ஐ இணைத்து seamless, AI-powered ஆவண வேலைப்பாடுகளை உருவாக்கவும்.

**உதாரண பயன்பாடுகள்:**
- ஒரு course அல்லது திட்ட ஆவணத்தை எழுதும் போது README-க்கு reference links-ஐ விரைவாக சேர்க்கவும்.
- Code உருவாக்க Copilot-ஐ பயன்படுத்தி, MCP மூலம் உடனடியாக தொடர்புடைய ஆவணங்களை கண்டறிந்து மேற்கோள் இடவும்.
- உங்கள் editor-ல் கவனம் செலுத்தி உற்பத்தியை அதிகரிக்கவும்.

> [!IMPORTANT]
> உங்கள் workspace-ல் செல்லுபடியாகும் [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration (இடம் `.vscode/mcp.json`) இருக்க வேண்டும்.

## Scenario 2-க்கு Chainlit ஏன்?

Chainlit என்பது conversational web applications உருவாக்குவதற்கான ஒரு நவீன open-source framework ஆகும். Microsoft Learn Docs MCP server போன்ற backend சேவைகளுடன் இணைக்கும் chat-based user interfaces உருவாக்க Chainlit-ஐ பயன்படுத்த எளிதாக உள்ளது. இந்த திட்டம் Chainlit-ஐ பயன்படுத்தி தனிப்பயன் பயிற்சி திட்டங்களை real-time-ல் உருவாக்க ஒரு எளிய, interactive வழியை வழங்குகிறது. Chainlit-ஐ பயன்படுத்துவதன் மூலம், உற்பத்தி மற்றும் கற்றலை மேம்படுத்த chat-based tools-ஐ விரைவாக உருவாக்கி deploy செய்யலாம்.

## இது என்ன செய்கிறது

இந்த app, ஒரு தலைப்பையும், கால அளவையும் உள்ளிடுவதன் மூலம் தனிப்பயன் பயிற்சி திட்டத்தை உருவாக்க அனுமதிக்கிறது. App உங்கள் உள்ளீட்டை parse செய்து, Microsoft Learn Docs MCP server-ஐ தொடர்புடைய உள்ளடக்கத்திற்காக query செய்து, முடிவுகளை ஒரு கட்டமைக்கப்பட்ட வார வார திட்டமாக அமைக்கிறது. ஒவ்வொரு வாரத்தின் பரிந்துரைகள் chat-ல் காட்டப்படும், இது உங்கள் முன்னேற்றத்தை பின்தொடர எளிதாக செய்கிறது. இந்த ஒருங்கிணைப்பு, நீங்கள் எப்போதும் சமீபத்திய மற்றும் தொடர்புடைய கற்றல் வளங்களை பெறுவதை உறுதிசெய்கிறது.

## மாதிரி கேள்விகள்

App எப்படி பதிலளிக்கிறது என்பதை பார்க்க chat window-ல் இந்த கேள்விகளை முயற்சிக்கவும்:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

இந்த உதாரணங்கள், app-இன் பல்திறனையும், பல்வேறு கற்றல் இலக்குகள் மற்றும் கால அளவுகளுக்கு ஏற்ப பயன்படுத்தும் திறனையும் காட்டுகின்றன.

## குறிப்புகள்

- [Chainlit ஆவணங்கள்](https://docs.chainlit.io/)
- [MCP ஆவணங்கள்](https://github.com/MicrosoftDocs/mcp)

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியக்குறைவுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.
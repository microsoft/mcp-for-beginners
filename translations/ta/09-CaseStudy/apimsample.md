# சம்பவ ஆய்வு: REST API ஐ API மேலாண்மையில் MCP சர்வர் ஆக வெளிப்படுத்துதல்

Azure API Management என்பது உங்கள் API கோட்புள்ளிகளுக்கு மேல் ஒரு வாயிலாகக் குறிக்கப்படும் சேவையாகும். Azure API Management உங்கள் APIs முன் ஒரு பிரதிநிதியாக செயல்பட்டு வரும் கோரிக்கைகளுடன் என்ன செய்ய வேண்டும் என்பதை தீர்மானிக்க முடியும்.

இதை பயன்படுத்துவதன் மூலம், நீங்கள் இதுபோன்ற பல அம்சங்களைச் சேர்க்கலாம்:

- **பாதுகாப்பு**, API விசைகள், JWT முதல் நிர்வகிக்கப்பட்ட அடையாளம் வரை அனைத்தையும் பயன்படுத்தலாம்.
- **அளவில் கட்டுப்பாடு**, ஒரு குறிப்பிட்ட நேர அளவுக்குள் எத்தனை கால் செல்லக்கூடும் என்பதை நிர்ணயிக்க முடியும். இது அனைத்து பயனர்களுக்கும் சிறந்த அனுபவத்தை வழங்குவதற்கு உதவுகிறது மற்றும் உங்கள் சேவை கோரிக்கைகளால் இதயம் பாதிக்கப்படாமல் இருக்கிறது.
- **பரிமாணம் & பல்கைச் சுமை சமநிலை**. நீங்கள் பல கோட்புள்ளிகளை அமைத்து சுமையை சமநிலைப்படுத்தலாம் மற்றும் "சுமை சமநிலை" எப்படியாக இருக்கும் என்பதையும் தேர்வுசெய்யலாம்.
- **செயற்கை நுண்ணறிவு அம்சங்கள் போன்று பொருள் நினைவகம்**, டோக்கன் வரம்பு மற்றும் டோக்கன் கண்காணிப்பு மற்றும் மேலும். இவை பதிலளிப்பை மேம்படுத்துவதற்கு மிக சிறந்த அம்சங்கள் மற்றும் உங்கள் டோக்கன் செலவையும் கவனிக்க உதவுகின்றன. [மேலும் படியுங்கள்](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## ஏன் MCP + Azure API Management?

Model Context Protocol விரைவாக முகவர் செயற்கை நுண்ணறிவு செயலிகளுக்கு ஒரு தரநிலை ஆக மாறுகிறது மற்றும் கருவிகள் மற்றும் தரவுகளை ஒத்துழைப்பு வழியில் வெளிப்படுத்தும் வழி ஆக உள்ளது. APIயை "மேலாண்மை" செய்ய வேண்டும் என்றால் Azure API Management இயல்பான தேர்வு ஆகும். MCP சர்வர்கள் பொதுவாக மற்ற APIகளோடு சேர்ந்து ஒரு கருவிக்கு கோரிக்கைகளை தீர்க்க உதவுகின்றன. ஆகவே Azure API Management மற்றும் MCP ஒன்றுகூடுதல் ஒரு நல்ல யோசனை.

## மேலோட்டம்

இந்த குறிப்பிட்ட பயன்படுத்தும் வழக்கில், API கோட்புள்ளிகளை MCP சர்வராக வெளிப்படுத்த கற்றுக்கொள்கிறோம். இதனால், இக்கோட்புள்ளிகள் முகவர் செயலி ஒரு பகுதியாக எளிதாக சேர்க்கப்பட்டு Azure API Management அம்சங்களையும் பயன்படுத்த முடியும்.

## முக்கிய அம்சங்கள்

- நீங்கள் உருவாக்க விரும்பும் கோட்புள்ளி முறைகளை கருவிகளாக தேர்வு செய்கிறீர்கள்.
- நீங்கள் பெறும் கூடுதல் அம்சங்கள் உங்கள் APIக்கு கொடுத்த கொள்கைப் பகுதியிலிருந்து அமைக்கப்படுகின்றன. இங்கு எவ்வாறு அளவில் கட்டுப்பாடு சேர்க்கலாம் என்பதை காண்போம்.

## முன்னணி படி: ஒரு API ஐ இறக்குமதி செய்யவும்

ஏற்கனவே Azure API Management இல் API இருக்கின் சிறப்பாகும், அப்பாடு இந்த படியைக் கடக்கலாம். இல்லையெனில் இந்த இணைப்பைப் பாருங்கள், [Azure API Management இல் API இறக்குமதி செய்யல்](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API யை MCP சர்வராக வெளிப்படுத்து

API கோட்புள்ளிகளை வெளிப்படுத்த, பின்வரும் படிகளை பின்பற்றுவோம்:

1. Azure போர்டலை உலா, பின்வரும் முகவரிக்கு செல்லவும் <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
உங்கள் API மேலாண்மை நிகழ்நிலை செல்லவும்.

1. இடது மெனுவில் APIs > MCP Servers > + புதிய MCP சர்வர் உருவாக்கம் என்பதனை தேர்வு செய்யவும்.

1. API இல் MCP சர்வராக வெளிப்படுத்த வேண்டிய REST API ஐ தேர்வு செய்யவும்.

1. கருவிகளாக வெளிப்படுத்த ஒரு அல்லது பல API செயல்பாடுகளை தேர்ந்தெடுக்கவும். நீங்கள் அனைத்து செயல்பாடுகளையும் அல்லது குறிப்பிட்ட செயல்பாடுகளை மட்டும் தேர்வு செய்யலாம்.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** என்பதனை தேர்வு செய்யவும்.

1. மெனு விருப்பமாக **APIs** மற்றும் **MCP Servers** செல்லவும், பின்வரிசையானவை காண்பீர்கள்:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP சர்வர் உருவாக்கப்பட்டுள்ளது மற்றும் API செயல்பாடுகள் கருவிகளாக வெளிப்படுத்தப்படுள்ளன. MCP சர்வர் MCP Servers பக்கத்தில் பட்டியலிடப்பட்டுள்ளது. URL பத்தி, மொழியாளர்களுக்குத் தானாக சோதனை அல்லது உள்ளிடல் செயலியில் அழைக்க பயன்படுத்தக்கூடிய MCP சர்வர் முகவரியை காட்டுகிறது.

## விருப்பமாக: கொள்கைகளை அமைக்கவும்

Azure API Management கொள்கைகள் என்ற முக்கிய கொள்கையை கொண்டுள்ளது, இதில் நீங்கள் உங்கள் கோட்புள்ளிகளுக்கு விதிகள்களை அமைக்கலாம், உதாரணமாக அளவுக் கட்டுப்பாடு அல்லது பொருள் நினைவகம். இவை XML வடிவில் எழுதப்பட்டுள்ளன.

உங்கள் MCP சர்வரின் அளவுக் கட்டுப்பாட்டை அமைப்பது எப்படி என்பது இங்கே உள்ளது:

1. போர்டலில் APIs கீழ் **MCP Servers** ஐ தேர்வு செய்யவும்.

1. நீங்கள் உருவாக்கிய MCP சர்வரை தேர்வு செய்யவும்.

1. இடது மெனு MCP கீழ் **Policies** ஐ தேர்வு செய்யவும்.

1. கொள்கை தொகுப்பியில், MCP சர்வரின் கருவிகளுக்கு பொருந்தும் கொள்கைகளைச் சேர்க்க அல்லது மாற்றவும். கொள்கைகள் XML வடிவில் வரையறுக்கப்படுகின்றன. உதாரணமாக, நீங்கள் MCP கருவிகளுக்கு அழைப்புகளை 5 அழைப்புகள் 30 வினாடிக்குள் IP முகவரிக்கு என்றே வரம்பிட ஒரு கொள்கையைச் சேர்க்கலாம். இந்த XML கீழே உள்ளது:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    கொள்கை தொகுப்பியின் படத்தை இங்கே பார்க்கலாம்:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## முயற்சி செய்

நமது MCP சர்வர் நியாயமாக செயல்பட்டுள்ளதா என்று உறுதிசெய்வோம்.

> [!NOTE]
> Azure API Management தற்போது இந்த சர்வரை Streamable
> HTTP `/mcp` கோட்புள்ளியாயாக வெளிப்படுத்துகிறது. பழைய HTTP+SSE `/sse` போக்குவரத்து பழைய வாடிக்கையாளர்களுக்கு மட்டுமே பயன்படுத்த வேண்டும்.
>

இதற்காக, Visual Studio Code மற்றும் GitHub Copilot Agent முறையைப் பயன்படுத்துவோம். MCP சர்வரை *mcp.json* இல் சேர்க்கப் போகிறோம். இதனால் Visual Studio Code முகவர் திறன்களுடன் வாடிக்கையாளர் போல செயல்படும் மற்றும் இறுதிய பயனர் ஒரு முன்மொழிவை எழுதிப் interacting முடியும்.

Visual Studio Code இல் MCP சர்வரைச் சேர்ப்பதைப் பார்ப்போம்:

1. கமாண்ட் பேலட்டில் இருந்து MCP: **Add Server கட்டளையைப் பயன்படுத்தவும்**.

1. கேட்டபோது சர்வர் வகையை தேர்ந்தெடுக்கவும்: **HTTP (HTTP அல்லது Server Sent Events)**.

1. API மேலாண்மையில் MCP சர்வருக்கான Streamable HTTP URL ஐ உள்ளிடவும்.
    உதாரணமாக:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. உங்கள் விருப்பப்படி சர்வர் ID யை உள்ளிடவும். இது முக்கியமான மதிப்பு அல்ல, ஆனால் அந்த சர்வர் அலகை நினைவில் வைத்துக்கொள்ள உதவும்.

1. அமைப்பை உங்கள் வேலைத் தள அமைப்புகள் அல்லது பயனர் அமைப்புகளில் சேமிக்க தேர்வு செய்யவும்.

  - **வேலைத் தளம் அமைப்புகள்** - சர்வர் அமைப்பு தற்போதைய வேலைத் தளத்தில் மட்டும் கிடைக்கும் .vscode/mcp.json கோப்பில் சேமிக்கப்படும்.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **பயனர் அமைப்புகள்** - சர்வர் அமைப்பு உங்கள் உலகளாவிய *settings.json* கோப்பில் சேர்க்கப்பட்டு அனைத்து வேலைத் தளங்களிலும் கிடைக்கும். அமைப்பு கீழ் போல இருக்கிறது:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. மேலும் Azure API Management நோக்கி சரியான அங்கீகாரம் உறுதி செய்ய ஒரு தலைப்பு (header) சேர்க்கவேண்டும். இது **Ocp-Apim-Subscription-Key** என்ற தலைப்பை பயன்படுத்துகிறது.

    - இதைப் பயனர் அமைப்புகளில் சேர்ப்பது எப்படி:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), இது API விசை மதிப்பை கேட்டு தயார் செய்யும், அதை Azure போர்டலில் Azure API Management நிகழ்நிலையிலிருந்து பெறலாம்.

   - *mcp.json* இல் சேர்க்க விரும்பினால், இதுபோல் சேர்க்கலாம்:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### முகவர் (Agent) முறையைப் பயன்படுத்துதல்

இப்போது நாம் அமைப்பு முறைகளில் அல்லது *.vscode/mcp.json* இல் அனைத்து அமைப்பும் முடிந்துவிட்டது. முயற்சிப் பார்க்கலாம்.

கருவிகள் ஐகான் இங்கேவிதமாக இருப்பது காண வேண்டும், உங்கள் சர்வர் வெளிப்படுத்திய கருவிகள் பட்டியலிடப்பட்டிருக்கும்:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. கருவிகள் ஐகானைக் கிளிக் செய்யவும், பின்னர் இப்படி கருவிகள் பட்டியலை காண்பீர்கள்:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. கருவியை செயல்படுத்த உரையாடலில் ஒரு முன்மொழிவை உள்ளிடவும். எடுத்துக்காட்டாக, நீங்கள் ஒரு ஆர்டருக்கான தகவலைக் கேட்க கருவியை தேர்ந்தெடுத்திருந்தால், முகவரிடம் ஒரு ஆர்டர் குறித்து கேட்கலாம். ஒரு முன்மொழிவு உதாரணம் கீழே:

    ```text
    get information from order 2
    ```

    இப்போது ஒரு கருவி ஐகான் தோன்றும், கருவியை இயக்க தொடர நீங்கள் தேர்வு செய்யலாம். அப்போது இதுபோன்ற வெளிப்பாடு காண்பீர்கள்:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **மேலே நீங்கள் காணும் விஷயங்கள் நீங்கள் அமைத்த கருவிகளின் மேல் منحصر, ஆனால் கருத்து இதுவே - மேலே போன்ற உரை பதில்களை நீங்கள் பெறுவீர்கள்**


## குறிப்பு இலவசங்கள்

மேலும் அறிய இங்கே பாருங்கள்:

- [Azure API Management மற்றும் MCP மீது பயிற்சி](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python மாதிரி: Azure API Management கொண்டு தொலை தளம் பாதுகாக்கப்பட்ட MCP சர்வர்கள் (சோதனை)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP வாடிக்கையாளர் அங்கீகார ஆய்வகம்](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code க்கான Azure API Management நீட்டிப்பை பயன்படுத்தி APIகளை இறக்குமதி மற்றும் மேலாண்மை](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center இல் தொலை MCP சர்வர்களை பதிவு மற்றும் கண்டறி](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management உடன் பல AI திறன்களை காட்டும் அற்புதக் காலண்டர்.
- [AI Gateway பணிமனைகள்](https://azure-samples.github.io/AI-Gateway/) Azure போர்டல் பயன்படுத்தி பணிமனைகள், இது AI திறன்களை மதிப்பீடு செய்ய சிறந்த வழி.

## அடுத்ததாக என்ன உள்ளது

- திரும்ப: [சம்பவ ஆய்வுகளின் மேலோட்டம்](./README.md)
- அடுத்து: [Azure AI பயண முகவர்கள்](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
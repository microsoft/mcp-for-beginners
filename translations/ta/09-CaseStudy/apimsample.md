# வழக்குக் கதை: API மேலாண்மையில் REST API-ஐ MCP சர்வராக வெளிப்படுத்துதல்

Azure API Management என்பது உங்கள் API முடிவுகளுக்கு மேல் ஒரு Gateway வழங்கும் சேவையாகும். இது செயல்படுவது எப்படி என்றால், Azure API Management உங்கள் API-களுக்கு முன் ஒரு proxy போல செயல்பட்டு, வரும் கோரிக்கைகளுடன் என்ன செய்ய வேண்டும் என்பதை முடிவு செய்யும்.

இதைப் பயன்படுத்துவதன் மூலம், நீங்கள் பல அம்சங்களைச் சேர்க்கலாம்:

- **பாதுகாப்பு**, API கீக்கள், JWT முதல் நிர்வகிக்கப்பட்ட அடையாளம் வரை அனைத்தையும் பயன்படுத்தலாம்.
- **விகித வரையறை**, ஒரு குறிப்பிட்ட நேர அளவுக்குள் எத்தனை அழைப்புகள் செல்ல வேண்டும் என்பதை முடிவு செய்ய முடியும். இது அனைத்து பயனர்களும் சிறந்த அனுபவத்தை பெறவும், உங்கள் சேவை கோரிக்கைகளால் அதிகமாக சுமையடையாமல் இருக்கவும் உதவுகிறது.
- **மிகைப்படுத்தல் மற்றும் சுமை சமநிலை**. சுமையை சமநிலைப்படுத்த பல முடிவுகளை அமைக்கலாம், மேலும் "சுமை சமநிலை" எப்படி செய்ய வேண்டும் என்பதை முடிவு செய்யலாம்.
- **AI அம்சங்கள், semantic caching, token limit மற்றும் token monitoring போன்றவை**. இவை பதிலளிப்பு வேகத்தை மேம்படுத்துவதுடன், உங்கள் token செலவுகளை மேலாண்மை செய்ய உதவுகின்றன. [மேலும் படிக்க](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ஏன் MCP + Azure API Management?

Model Context Protocol என்பது agentic AI பயன்பாடுகளுக்கான ஒரு தரமாக விரைவாக உருவாகி வருகிறது, மேலும் கருவிகள் மற்றும் தரவுகளை ஒரே மாதிரியான முறையில் வெளிப்படுத்த உதவுகிறது. API-களை "மேலாண்மை" செய்ய Azure API Management ஒரு இயல்பான தேர்வாகும். MCP சர்வர்கள், உதாரணமாக, ஒரு கருவிக்கு கோரிக்கைகளை தீர்க்க பிற API-களுடன் அடிக்கடி ஒருங்கிணைக்கின்றன. எனவே Azure API Management மற்றும் MCP-ஐ இணைப்பது மிகவும் பொருத்தமாக உள்ளது.

## மேற்பார்வை

இந்த குறிப்பிட்ட பயன்பாட்டில், API முடிவுகளை MCP Server ஆக வெளிப்படுத்த கற்றுக்கொள்வோம். இதைச் செய்வதன் மூலம், இந்த முடிவுகளை agentic பயன்பாட்டின் ஒரு பகுதியாக எளிதாக மாற்றலாம், மேலும் Azure API Management-இன் அம்சங்களைப் பயன்படுத்தலாம்.

## முக்கிய அம்சங்கள்

- நீங்கள் கருவிகளாக வெளிப்படுத்த விரும்பும் முடிவு முறைகளைத் தேர்ந்தெடுக்கலாம்.
- நீங்கள் பெறும் கூடுதல் அம்சங்கள் உங்கள் API-க்கான கொள்கை பிரிவில் நீங்கள் அமைக்கிறீர்கள் என்பதைப் பொறுத்தது. ஆனால் இங்கு விகித வரையறையைச் சேர்ப்பது எப்படி என்பதை நாம் காண்போம்.

## முன்னோட்டம்: API-ஐ இறக்குமதி செய்யுங்கள்

Azure API Management-இல் ஏற்கனவே API இருந்தால், இந்த படியைத் தவிர்க்கலாம். இல்லையெனில், இந்த இணைப்பைப் பாருங்கள், [Azure API Management-க்கு API-ஐ இறக்குமதி செய்தல்](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API-ஐ MCP Server ஆக வெளிப்படுத்துதல்

API முடிவுகளை MCP Server ஆக வெளிப்படுத்த, இந்த படிகளைப் பின்பற்றுங்கள்:

1. Azure Portal-க்கு செல்லுங்கள், <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> என்ற முகவரிக்கு செல்லுங்கள். உங்கள் API Management instance-ஐத் தேர்ந்தெடுக்கவும்.

1. இடது மெனுவில், **APIs > MCP Servers > + Create new MCP Server** என்பதைத் தேர்ந்தெடுக்கவும்.

1. API-யில், MCP Server ஆக வெளிப்படுத்த REST API-யைத் தேர்ந்தெடுக்கவும்.

1. கருவிகளாக வெளிப்படுத்த API செயல்பாடுகளை ஒன்றை அல்லது ஒன்றுக்கு மேற்பட்டவற்றைத் தேர்ந்தெடுக்கவும். அனைத்து செயல்பாடுகளையும் அல்லது குறிப்பிட்ட செயல்பாடுகளை மட்டும் தேர்ந்தெடுக்கலாம்.

    ![வெளிப்படுத்த முறைகளைத் தேர்ந்தெடுக்கவும்](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** என்பதைத் தேர்ந்தெடுக்கவும்.

1. **APIs** மற்றும் **MCP Servers** மெனு விருப்பத்திற்கு செல்லுங்கள், நீங்கள் பின்வருவதைப் பார்க்க வேண்டும்:

    ![முதன்மை பக்கத்தில் MCP Server-ஐப் பார்க்கவும்](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP Server உருவாக்கப்பட்டு, API செயல்பாடுகள் கருவிகளாக வெளிப்படுத்தப்படுகின்றன. MCP Servers பக்கத்தில் MCP Server பட்டியலிடப்பட்டுள்ளது. URL பத்தியில் MCP Server-இன் முடிவுகளை நீங்கள் சோதனை செய்ய அல்லது ஒரு கிளையன்ட் பயன்பாட்டில் அழைக்க முடியும்.

## விருப்பம்: கொள்கைகளை அமைக்கவும்

Azure API Management-இல் கொள்கைகள் என்ற முக்கிய கருத்து உள்ளது, இதில் உங்கள் முடிவுகளுக்கு விதிகளை அமைக்கலாம், உதாரணமாக விகித வரையறை அல்லது semantic caching. இந்த கொள்கைகள் XML-ல் எழுதப்படுகின்றன.

MCP Server-க்கு விகித வரையறை கொள்கையை அமைப்பது எப்படி என்பதை இங்கே காணலாம்:

1. போர்ட்டலில், APIs கீழ், **MCP Servers** என்பதைத் தேர்ந்தெடுக்கவும்.

1. நீங்கள் உருவாக்கிய MCP Server-ஐத் தேர்ந்தெடுக்கவும்.

1. இடது மெனுவில், MCP கீழ், **Policies** என்பதைத் தேர்ந்தெடுக்கவும்.

1. கொள்கை தொகுப்பியில், MCP Server-இன் கருவிகளுக்கு நீங்கள் பயன்படுத்த விரும்பும் கொள்கைகளைச் சேர்க்கவும் அல்லது திருத்தவும். XML வடிவத்தில் கொள்கைகள் வரையறுக்கப்படுகின்றன. உதாரணமாக, MCP Server-இன் கருவிகளுக்கு அழைப்புகளை வரையறுக்க கொள்கையைச் சேர்க்கலாம் (இந்த உதாரணத்தில், 30 வினாடிக்கு ஒரு கிளையன்ட் IP முகவரிக்கு 5 அழைப்புகள்). XML இங்கே:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    கொள்கை தொகுப்பியின் படத்தை இங்கே காணலாம்:

    ![கொள்கை தொகுப்பி](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## சோதனை செய்யுங்கள்

MCP Server எதிர்பார்த்தபடி செயல்படுகிறதா என்பதை உறுதிப்படுத்துவோம்.

இதற்காக, Visual Studio Code மற்றும் GitHub Copilot மற்றும் அதன் Agent mode-ஐப் பயன்படுத்துவோம். MCP Server-ஐ *mcp.json* கோப்பில் சேர்ப்போம். இதனால், Visual Studio Code ஒரு கிளையன்ட் ஆக செயல்பட்டு, இறுதி பயனர்கள் ஒரு prompt-ஐ உள்ளீடு செய்து அந்த சர்வருடன் தொடர்பு கொள்ள முடியும்.

Visual Studio Code-ல் MCP Server-ஐச் சேர்ப்பது எப்படி என்பதைப் பார்ப்போம்:

1. **Command Palette**-இல் இருந்து MCP: **Add Server command**-ஐப் பயன்படுத்தவும்.

1. கேட்கப்பட்டால், சர்வர் வகையைத் தேர்ந்தெடுக்கவும்: **HTTP (HTTP or Server Sent Events)**.

1. API Management-இல் MCP Server-இன் URL-ஐ உள்ளிடவும். உதாரணம்: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE முடிவுக்கு) அல்லது **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP முடிவுக்கு), `/sse` அல்லது `/mcp` ஆகியவற்றின் இடைவெளி எப்படி மாறுகிறது என்பதை கவனிக்கவும்.

1. உங்கள் விருப்பத்தின் சர்வர் ID-ஐ உள்ளிடவும். இது முக்கியமான மதிப்பு அல்ல, ஆனால் இந்த சர்வர் instance என்ன என்பதை நினைவில் கொள்ள உதவும்.

1. அமைப்பை உங்கள் workspace settings அல்லது user settings-க்கு சேமிக்க விரும்புகிறீர்களா என்பதைத் தேர்ந்தெடுக்கவும்.

  - **Workspace settings** - சர்வர் அமைப்பு தற்போதைய workspace-இல் மட்டுமே கிடைக்கும் .vscode/mcp.json கோப்பில் சேமிக்கப்படுகிறது.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    அல்லது நீங்கள் streaming HTTP-ஐ போக்குவரத்தாகத் தேர்ந்தெடுத்தால், இது சிறிது மாறுபடும்:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - சர்வர் அமைப்பு உங்கள் global *settings.json* கோப்பில் சேர்க்கப்படுகிறது மற்றும் அனைத்து workspace-களிலும் கிடைக்கிறது. அமைப்பு பின்வருவதைப் போன்றதாக இருக்கும்:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management-க்கு சரியாக அங்கீகரிக்க ஒரு header சேர்க்கவும். இது **Ocp-Apim-Subscription-Key** என்ற header-ஐப் பயன்படுத்துகிறது.

    - இதை settings-க்கு சேர்ப்பது எப்படி என்பதை இங்கே காணலாம்:

    ![அங்கீகாரத்திற்கான header சேர்த்தல்](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), இது API key மதிப்பை கேட்க prompt-ஐ காட்டும், இது Azure Portal-ல் உங்கள் Azure API Management instance-க்கு கிடைக்கிறது.

   - *mcp.json*-க்கு சேர்க்க, இதைப் போலச் சேர்க்கலாம்:

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

### Agent mode-ஐப் பயன்படுத்துங்கள்

இப்போது நாம் settings அல்லது *.vscode/mcp.json*-ல் அமைத்துள்ளோம். அதைச் சோதிக்க முயற்சிக்கலாம்.

உங்கள் சர்வரிலிருந்து வெளிப்படுத்தப்பட்ட கருவிகள் பட்டியலிடப்பட்டுள்ள Tools ஐகான் போன்றது இருக்க வேண்டும்:

![சர்வரிலிருந்து கருவிகள்](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools ஐகானை கிளிக் செய்யவும், நீங்கள் பின்வருவதைப் போன்ற கருவிகள் பட்டியலைப் பார்க்க வேண்டும்:

    ![கருவிகள்](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. கருவியை இயக்க prompt-ஐ chat-ல் உள்ளிடவும். உதாரணமாக, ஒரு ஆர்டரைப் பற்றிய தகவலைப் பெற ஒரு கருவியைத் தேர்ந்தெடுத்தால், நீங்கள் agent-ஐ அந்த ஆர்டரைப் பற்றி கேட்கலாம். இங்கே ஒரு உதாரண prompt:

    ```text
    get information from order 2
    ```

    நீங்கள் கருவியை அழைக்க தொடர prompt-ஐக் காட்டும் Tools ஐகானை காண்பீர்கள். கருவியை இயக்கத் தொடரத் தேர்ந்தெடுக்கவும், நீங்கள் பின்வருவதைப் போன்ற output-ஐப் பார்க்க வேண்டும்:

    ![Prompt-இன் முடிவு](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **மேலே நீங்கள் காண்பது நீங்கள் அமைத்துள்ள கருவிகளைப் பொறுத்தது, ஆனால் கருத்து இது போன்ற உரை பதில்களைப் பெறுவது**

## குறிப்புகள்

மேலும் அறிய இங்கே:

- [Azure API Management மற்றும் MCP பற்றிய டுடோரியல்](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python உதாரணம்: Azure API Management-ஐப் பயன்படுத்தி பாதுகாப்பான தொலை MCP சர்வர்கள் (சோதனை)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP கிளையன்ட் அங்கீகார லேப்](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Visual Studio Code-க்கு Azure API Management நீட்டிப்பைப் பயன்படுத்த API-களை இறக்குமதி செய்து மேலாண்மை செய்யுங்கள்](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center-இல் தொலை MCP சர்வர்களை பதிவு செய்து கண்டறியுங்கள்](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management-இன் பல AI திறன்களை காட்டும் சிறந்த repo
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Azure Portal-ஐப் பயன்படுத்தும் workshops-ஐ உள்ளடக்கியது, இது AI திறன்களை மதிப்பீடு செய்ய தொடங்க சிறந்த வழி.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
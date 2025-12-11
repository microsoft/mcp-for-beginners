<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2228721599c0c8673de83496b4d7d7a9",
  "translation_date": "2025-12-11T10:33:20+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "te"
}
-->
# కేసు అధ్యయనం: API మేనేజ్‌మెంట్‌లో REST APIని MCP సర్వర్‌గా ప్రదర్శించడం

Azure API Management అనేది మీ API ఎండ్‌పాయింట్లపై గేట్వేను అందించే సేవ. ఇది ఎలా పనిచేస్తుందంటే Azure API Management మీ APIs ముందు ప్రాక్సీగా పనిచేస్తుంది మరియు వచ్చే అభ్యర్థనలతో ఏమి చేయాలో నిర్ణయించగలదు.

దీనిని ఉపయోగించడం ద్వారా, మీరు ఈ క్రింది లక్షణాలను పొందవచ్చు:

- **భద్రత**, మీరు API కీలు, JWT నుండి మేనేజ్‌డ్ ఐడెంటిటీ వరకు అన్ని విధాలుగా ఉపయోగించవచ్చు.
- **రేట్ లిమిటింగ్**, ఒక గొప్ప ఫీచర్ ఏమిటంటే ఒక నిర్దిష్ట కాల యూనిట్‌కు ఎంత కాల్స్ అనుమతించాలో నిర్ణయించుకోవచ్చు. ఇది అన్ని వినియోగదారులకు మంచి అనుభవం కల్పించడంలో సహాయపడుతుంది మరియు మీ సేవ అభ్యర్థనలతో ఒత్తిడికి గురవకుండా చేస్తుంది.
- **స్కేలింగ్ & లోడ్ బ్యాలెన్సింగ్**. మీరు లోడ్‌ను సమతుల్యం చేయడానికి అనేక ఎండ్‌పాయింట్లను సెట్ చేయవచ్చు మరియు "లోడ్ బ్యాలెన్స్" ఎలా చేయాలో కూడా నిర్ణయించవచ్చు.
- **సెమాంటిక్ క్యాచింగ్ వంటి AI ఫీచర్లు**, టోకెన్ పరిమితి మరియు టోకెన్ మానిటరింగ్ మరియు మరిన్ని. ఇవి ప్రతిస్పందనను మెరుగుపరుస్తాయి మరియు మీ టోకెన్ ఖర్చులపై మీరు నియంత్రణలో ఉండటానికి సహాయపడతాయి. [ఇక్కడ మరింత చదవండి](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ఎందుకు MCP + Azure API Management?

మోడల్ కాంటెక్స్ట్ ప్రోటోకాల్ త్వరగా ఏజెంటిక్ AI యాప్స్ కోసం ఒక ప్రమాణంగా మారుతోంది మరియు సాధనాలు మరియు డేటాను సुसంగతమైన విధంగా ప్రదర్శించడానికి. Azure API Management "APIsని నిర్వహించడానికి" సహజమైన ఎంపిక. MCP సర్వర్లు తరచుగా ఇతర APIsతో సమగ్రత కలిగి ఉంటాయి, ఉదాహరణకు సాధనానికి అభ్యర్థనలను పరిష్కరించడానికి. అందువల్ల Azure API Management మరియు MCP కలిపి ఉపయోగించడం చాలా అర్థవంతం.

## అవలోకనం

ఈ ప్రత్యేక ఉపయోగ సందర్భంలో, మనం API ఎండ్‌పాయింట్లను MCP సర్వర్‌గా ప్రదర్శించడం నేర్చుకుంటాము. దీని ద్వారా, ఈ ఎండ్‌పాయింట్లు ఏజెంటిక్ యాప్ భాగంగా సులభంగా మారతాయి మరియు Azure API Management నుండి ఫీచర్లను కూడా ఉపయోగించుకోవచ్చు.

## ముఖ్య లక్షణాలు

- మీరు సాధనాలుగా ప్రదర్శించదలచుకున్న ఎండ్‌పాయింట్ పద్ధతులను ఎంచుకుంటారు.
- మీరు పొందే అదనపు ఫీచర్లు మీ API కోసం పాలసీ విభాగంలో మీరు ఎలా కాన్ఫిగర్ చేస్తారో ఆధారపడి ఉంటాయి. కానీ ఇక్కడ మనం రేట్ లిమిటింగ్ ఎలా జోడించాలో చూపిస్తాము.

## ముందస్తు దశ: APIని దిగుమతి చేసుకోండి

మీకు Azure API Managementలో ఇప్పటికే API ఉంటే బాగుంది, ఈ దశను దాటవేయవచ్చు. లేకపోతే, ఈ లింక్ చూడండి, [Azure API Managementకి APIని దిగుమతి చేసుకోవడం](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## APIని MCP సర్వర్‌గా ప్రదర్శించండి

API ఎండ్‌పాయింట్లను ప్రదర్శించడానికి, ఈ దశలను అనుసరించండి:

1. Azure పోర్టల్‌కు వెళ్లి ఈ చిరునామా <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> ను సందర్శించండి  
మీ API మేనేజ్‌మెంట్ ఇన్స్టాన్స్‌కు వెళ్లండి.

1. ఎడమ మెనూలో, APIs > MCP Servers > + Create new MCP Server ఎంచుకోండి.

1. APIలో, MCP సర్వర్‌గా ప్రదర్శించడానికి REST APIని ఎంచుకోండి.

1. సాధనాలుగా ప్రదర్శించడానికి ఒకటి లేదా ఎక్కువ API ఆపరేషన్లను ఎంచుకోండి. మీరు అన్ని ఆపరేషన్లను లేదా కొన్ని ప్రత్యేక ఆపరేషన్లను ఎంచుకోవచ్చు.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** ఎంచుకోండి.

1. మెనూ ఎంపిక **APIs** మరియు **MCP Servers**కి వెళ్లండి, మీరు క్రింది దృశ్యాన్ని చూడగలరు:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP సర్వర్ సృష్టించబడింది మరియు API ఆపరేషన్లు సాధనాలుగా ప్రదర్శించబడ్డాయి. MCP సర్వర్ MCP Servers ప్యానెల్లో జాబితా చేయబడింది. URL కాలమ్ MCP సర్వర్ ఎండ్‌పాయింట్‌ను చూపుతుంది, దీన్ని మీరు పరీక్షించడానికి లేదా క్లయింట్ యాప్‌లో కాల్ చేయవచ్చు.

## ఐచ్ఛికం: పాలసీలను కాన్ఫిగర్ చేయండి

Azure API Managementలో పాలసీలు అనే మూల భావన ఉంది, ఇందులో మీరు మీ ఎండ్‌పాయింట్లకు వివిధ నియమాలను సెట్ చేయవచ్చు, ఉదాహరణకు రేట్ లిమిటింగ్ లేదా సెమాంటిక్ క్యాచింగ్. ఈ పాలసీలు XMLలో రచించబడతాయి.

మీ MCP సర్వర్‌కు రేట్ లిమిట్ విధించడానికి పాలసీని ఎలా సెట్ చేయాలో ఇక్కడ ఉంది:

1. పోర్టల్‌లో, APIs కింద, **MCP Servers** ఎంచుకోండి.

1. మీరు సృష్టించిన MCP సర్వర్ ఎంచుకోండి.

1. ఎడమ మెనూలో, MCP కింద, **Policies** ఎంచుకోండి.

1. పాలసీ ఎడిటర్‌లో, మీరు MCP సర్వర్ సాధనాలకు వర్తింపజేయదలచిన పాలసీలను జోడించండి లేదా సవరించండి. పాలసీలు XML ఫార్మాట్‌లో నిర్వచించబడ్డాయి. ఉదాహరణకు, MCP సర్వర్ సాధనాలకు కాల్స్ పరిమితం చేయడానికి పాలసీని జోడించవచ్చు (ఈ ఉదాహరణలో, ప్రతి క్లయింట్ IP చిరునామాకు 30 సెకన్లకు 5 కాల్స్). ఇది రేట్ లిమిట్ చేయడానికి XML:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```
  
    పాలసీ ఎడిటర్ యొక్క చిత్రం ఇక్కడ ఉంది:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ప్రయత్నించండి

మన MCP సర్వర్ ఉద్దేశించిన విధంగా పనిచేస్తుందో లేదో నిర్ధారించుకుందాం.

దీనికోసం, మనం Visual Studio Code మరియు GitHub Copilot మరియు దాని ఏజెంట్ మోడ్ ఉపయోగిస్తాము. మనం MCP సర్వర్‌ను *mcp.json*లో జోడిస్తాము. ఇలా చేయడం ద్వారా, Visual Studio Code ఏజెంటిక్ సామర్థ్యాలతో క్లయింట్‌గా పనిచేస్తుంది మరియు చివరి వినియోగదారులు ప్రాంప్ట్ టైప్ చేసి ఆ సర్వర్‌తో పరస్పర చర్య చేయగలుగుతారు.

Visual Studio Codeలో MCP సర్వర్‌ను ఎలా జోడించాలో చూద్దాం:

1. కమాండ్ ప్యాలెట్ నుండి MCP: **Add Server command** ఉపయోగించండి.

1. ప్రాంప్ట్ వచ్చినప్పుడు, సర్వర్ రకాన్ని ఎంచుకోండి: **HTTP (HTTP లేదా Server Sent Events)**.

1. API మేనేజ్‌మెంట్‌లో MCP సర్వర్ URLని నమోదు చేయండి. ఉదాహరణ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE ఎండ్‌పాయింట్ కోసం) లేదా **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP ఎండ్‌పాయింట్ కోసం), ట్రాన్స్‌పోర్ట్స్ మధ్య తేడా `/sse` లేదా `/mcp` అని గమనించండి.

1. మీ ఇష్టానుసారం సర్వర్ IDని నమోదు చేయండి. ఇది ముఖ్యమైన విలువ కాదు కానీ ఈ సర్వర్ ఇన్స్టాన్స్ ఏదో గుర్తు పెట్టుకోవడానికి సహాయపడుతుంది.

1. కాన్ఫిగరేషన్‌ను వర్క్‌స్పేస్ సెట్టింగ్స్ లేదా యూజర్ సెట్టింగ్స్‌లో సేవ్ చేయాలా ఎంచుకోండి.

  - **వర్క్‌స్పేస్ సెట్టింగ్స్** - సర్వర్ కాన్ఫిగరేషన్ .vscode/mcp.json ఫైల్‌లో సేవ్ అవుతుంది, ఇది ప్రస్తుత వర్క్‌స్పేస్‌లో మాత్రమే అందుబాటులో ఉంటుంది.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```
  
    లేదా మీరు స్ట్రీమింగ్ HTTPని ట్రాన్స్‌పోర్ట్‌గా ఎంచుకుంటే ఇది కొంచెం భిన్నంగా ఉంటుంది:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```
  
  - **యూజర్ సెట్టింగ్స్** - సర్వర్ కాన్ఫిగరేషన్ మీ గ్లోబల్ *settings.json* ఫైల్‌లో జోడించబడుతుంది మరియు అన్ని వర్క్‌స్పేస్‌లలో అందుబాటులో ఉంటుంది. కాన్ఫిగరేషన్ ఈ విధంగా ఉంటుంది:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. మీరు Azure API Management వైపు సరిగ్గా ధృవీకరించడానికి హెడర్‌ను కూడా జోడించాలి. ఇది **Ocp-Apim-Subscription-Key** అనే హెడర్‌ను ఉపయోగిస్తుంది.

    - సెట్టింగ్స్‌లో దీన్ని ఎలా జోడించాలో ఇక్కడ ఉంది:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ఇది API కీ విలువ కోసం ప్రాంప్ట్ చూపిస్తుంది, మీరు Azure పోర్టల్‌లో మీ Azure API Management ఇన్స్టాన్స్ కోసం దాన్ని కనుగొనవచ్చు.

   - *mcp.json*లో జోడించాలంటే, ఇలా చేయవచ్చు:

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
  
### ఏజెంట్ మోడ్ ఉపయోగించండి

ఇప్పుడు మనం సెట్టింగ్స్ లేదా *.vscode/mcp.json*లో అన్ని సెట్ చేసుకున్నాము. ప్రయత్నిద్దాం.

మీ సర్వర్ నుండి ప్రదర్శించబడిన సాధనాలు జాబితా చేయబడినట్లు, ఈ విధంగా ఒక Tools ఐకాన్ ఉండాలి:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools ఐకాన్‌పై క్లిక్ చేయండి, మీరు ఈ విధంగా సాధనాల జాబితా చూడగలరు:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. సాధనాన్ని పిలవడానికి చాట్‌లో ప్రాంప్ట్ నమోదు చేయండి. ఉదాహరణకు, మీరు ఆర్డర్ గురించి సమాచారం పొందడానికి సాధనాన్ని ఎంచుకున్నట్లయితే, ఏజెంట్‌ను ఆర్డర్ గురించి అడగవచ్చు. ఇక్కడ ఒక ఉదాహరణ ప్రాంప్ట్ ఉంది:

    ```text
    get information from order 2
    ```
  
    ఇప్పుడు మీరు సాధనాన్ని పిలవమని అడిగే Tools ఐకాన్‌ను చూడగలరు. సాధనాన్ని కొనసాగించడానికి ఎంచుకోండి, మీరు ఈ విధంగా అవుట్‌పుట్ చూడగలరు:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **మీరు పైగా చూసేది మీరు సెట్ చేసిన సాధనాలపై ఆధారపడి ఉంటుంది, కాని ఆలోచన ఏమిటంటే మీరు పై విధంగా టెక్స్టువల్ ప్రతిస్పందన పొందుతారు**

## సూచనలు

ఇంకా తెలుసుకోవడానికి:

- [Azure API Management మరియు MCP పై ట్యుటోరియల్](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python నమూనా: Azure API Management ఉపయోగించి రిమోట్ MCP సర్వర్లను సురక్షితం చేయడం (ప్రయోగాత్మక)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP క్లయింట్ ఆథరైజేషన్ ల్యాబ్](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code కోసం Azure API Management ఎక్స్‌టెన్షన్ ఉపయోగించి APIs దిగుమతి చేసుకోవడం మరియు నిర్వహించడం](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Centerలో రిమోట్ MCP సర్వర్లను నమోదు చేయడం మరియు కనుగొనడం](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI గేట్వే](https://github.com/Azure-Samples/AI-Gateway) Azure API Managementతో అనేక AI సామర్థ్యాలను చూపించే గొప్ప రిపోజిటరీ
- [AI గేట్వే వర్క్‌షాప్‌లు](https://azure-samples.github.io/AI-Gateway/) Azure పోర్టల్ ఉపయోగించి వర్క్‌షాప్‌లు, AI సామర్థ్యాలను అంచనా వేయడం ప్రారంభించడానికి గొప్ప మార్గం.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
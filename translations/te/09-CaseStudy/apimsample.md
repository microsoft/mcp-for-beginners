# కేస్ స్టడీ: API మేనేజ్మెంట్‌లో MCP సర్వర్‌గా REST APIని ఎక్స్‌పోజ్ చేయండి

Azure API Management అనేది మీ API ఎండ్‌పాయింట్లపై గేట్‌వేగా పనిచేస్తున్న సేవ. ఇది ఎలా పని చేస్తుంది అంటే Azure API Management మీ APIs ముందు ప్రోక్సీగా పనిచేస్తుంది మరియు ముట్టడించు అభ్యర్థనలతో ఏం చేయాలో నిర్ణయించవచ్చు.

దీన్ని ఉపయోగించి, మీరు ఈ విధమైన అనేక ఫీచర్లు పొందవచ్చు:

- **భద్రత**, మీరు API కీలు, JWT నుంచి మ్యానేజ్‌డ్ ఐడెంటిటీ వరకు అన్నిటినీ ఉపయోగించవచ్చు.
- **రేటు పరిమితి**, ఒక గొప్ప ఫీచర్ ప్రతి నిర్దిష్ట కాలంలో ఎన్ని కాల్స్ చేయబడతాయో నిర్ణయించగలగడం. ఇది అన్ని వినియోగదారులకు మంచి అనుభవాన్ని మరియు మీ సేవ అభ్యర్థనలతో భారం పడకుండా కాపాడుతుంది.
- **స్కేలింగ్ & లోడ్ బలెన్సింగ్**. మీరు పలు ఎండ్‌పాయింట్లను అమర్చుకొని లోడ్‌ని సమతుల్యం చేయవచ్చు మరియు "లోడ్ బలెన్స్" ఎలా చేయాలో నిర్ణయించవచ్చు.
- **AI ఫీచర్లు వంటి సెమాంటిక్ క్యాచింగ్**, టోకెన్ పరిమితి మరియు టోకెన్ మానిటరింగ్ మరియు ఇంకా అనేకం. ఇవి సద్వినియోగాన్ని మెరుగుపరుస్తూ మీ టోకెన్ ఖర్చుపై నియంత్రణను అందిస్తాయి. [ఇక్కడ మరింత చదవండి](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## ఎందుకు MCP + Azure API Management?

మోడల్ కాన్టెక్ట్ ప్రోటోకాల్(ఎంపిసి) వేగంగా ఏజెంటిక్ AI యాప్స్ కోసం ప్రామాణికంగా మారుతోంది, సాధనాలు మరియు డేటాను నిర్ధిష్ట తీరుగా ఎక్స్‌పోజ్ చేయడానికి. మీరు APIs ను "మేనేజ్" చేయాల్సిన సమయములో Azure API Management సహజమైన ఎంపిక. MCP సర్వర్లు తరచుగా ఇతర APIs తో ఇంటిగ్రేట్ అయి సాధనాల అవసరాలకు అభ్యర్థనలను పరిష్కరిస్తాయి. అందుచేత Azure API Management మరియు MCP కలిపి వాడటం చాలా సరైనదే.

## అవలోకనం

ఈ ప్రత్యేక ఉపయోగ సందర్భంలో మనం API ఎండ్‌పాయింట్లు MCP సర్వర్‌గా ఎక్స్‌పోజ్ చేయడం నేర్చుకుంటాము. ఈ విధంగా, మనం ఈ ఎండ్‌పాయింట్లను ఏజెంటిక్ యాప్ భాగంగా సులభంగా చేయగలము, అలాగే Azure API Management ఫీచర్లను కూడా ఉపయోగించవచ్చు.

## ముఖ్యమైన ఫీచర్లు

- మీరు టూల్స్‌గా ఎక్స్‌పోజ్ చేయదలచిన ఎండ్‌పాయింట్ విధానాలను ఎంచుకుంటారు.
- పొందే అదనపు ఫీచర్లు మీ API యొక్క పాలసీ విభాగంలో మీరు ఏర్పాటు చేసే విధానాలపై ఆధారపడి ఉంటాయి. కానీ ఇక్కడ మనం రేటు పరిమితిని ఎలా జోడించాలో చూపించుకుంటాము.

## ముందస్తు దశ: APIను దిగుమతి చేసుకోండి

మీరు ఇప్పటికే Azure API Managementలో API ఉంటే బాగుంది, అప్పుడే ఈ దశ వదిలేయండి. లేనిద అయితే, ఈ లింక్ చూడండి, [Azure API Managementకు API దిగుమతి](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## APIని MCP సర్వర్‌గా ఎక్స్‌పోజ్ చేయండి

API ఎండ్‌పాయింట్లను ఎక్స్‌పోజ్ చేయడానికి, ఈ దశలను అనుసరించండి:

1. Azure పోర్టల్ మరియు ఈ అడ్రస్ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> కు వెళ్ళండి
మీ API మేనేజ్మెంట్ ఇన్స్టెన్స్‌కు వెళ్ళండి.

1. ఎడమ మెనూలో APIs > MCP Servers > + Create new MCP Server ఎంచుకోండి.

1. APIలో, MCP సర్వర్‌గా ఎక్స్‌పోజ్ చేయడానికి ఒక REST APIని ఎంచుకోండి.

1. టూల్స్‌గా ఎక్స్‌పోజ్ చేయడానికి ఒకటి లేదా ఎక్కువ API ఆపరేషన్లను ఎంచుకోండి. మీరు అన్ని ఆపరేషన్లు లేదా కొన్ని మాత్రమే ఎంచుకోవచ్చు.

    ![ఎక్స్‌పోజ్ చేయడానికి విధానాలను ఎంచుకోండి](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create**ను ఎంచుకోండి.

1. మెనూ ఎంపిక APIs మరియు MCP Servers కు వెళ్ళండి, మీరు క్రింది దాన్ని చూడగలరు:

    ![ముఖ్యపు విడ్జెట్‌లో MCP సర్వర్ చూడండి](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP సర్వర్ సృష్టించబడినట్లుగా, API ఆపరేషన్లు టూల్స్‌గా ఎక్స్‌పోజ్ చేయబడినవి. MCP సర్వర్ MCP Servers వరసలో లిస్టవుంది. URL కాలమ్ MCP సర్వర్ యొక్క ఎండ్పాయింట్ చూపిస్తుంది, దీన్ని పరీక్ష కోసం లేదా క్లయింట్ యాప్‌లో పిలవవచ్చు.

## ఐచ్ఛికం: పాలసీలను సెట్ చేయండి

Azure API Managementకు పాలసీల అనే మూల భావన ఉంది, ఇందులో మీరు మీ ఎండ్‌పాయింట్లకు ప్రతి విధమైన నియమాలు సెట్ చేయవచ్చు, ఉదాహరణకి రేటు పరిమితి లేదా సెమాంటిక్ క్యాచింగ్ వంటి. ఈ పాలసీలు XMLలో రచించబడతాయి.

ఎలా మీ MCP సర్వర్‌కు రేటు పరిమితి కలిగించే పాలసీ సెట్ చేయాలో ఇలా ఉంది:

1. పోర్టల్‌లో APIs క్రింద **MCP Servers** ఎంచుకోండి.

1. మీరు సృష్టించిన MCP సర్వర్ ఎంచుకోండి.

1. ఎడమ మెనూలో MCP కింద **Policies** ఎంచుకోండి.

1. పాలసీ ఎడిటర్‌లో, MCP సర్వర్ టూల్స్‌కు వర్తించదలచిన పాలసీలను జోడించండి లేదా ఎడిట్ చేయండి. పాలసీలు XML ఫార్మాట్‌లో నిర్వచించబడ్డాయి. ఉదాహరణకి, MCP సర్వర్ టూల్స్‌కు పిలవబడే కాల్స్ గణనను పరిమితం చేయడానికి ఒక పాలసీ జోడించవచ్చు (ఈ ఉదాహరణలో ఒక్కో క్లయింట్ IPకి 30 సెకన్లలో 5 కాల్స్). దీనికి XML ఈ విధంగా ఉంటుంది:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ఇదిగో పాలసీ ఎడిటర్ చిత్రం:

    ![పాలసీ ఎడిటర్](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ప్రయత్నించండి

మన MCP సర్వర్ ఉద్దేశించినట్లు పనిచేస్తుందో లేదో చూద్దాం.

> [!NOTE]
> Azure API Management ప్రస్తుతం ఈ సర్వర్‌ను Streamable HTTP `/mcp` ఎండ్‌పాయింట్ ద్వారా ఎక్స్‌పోజ్ చేస్తుంది. పాత HTTP+SSE `/sse` ట్రాన్స్‌పోర్ట్ ఆపివేయబడింది మరియు
> వేలెన్సీ క్లయింట్లతో మాత్రమే ఉపయోగించండి.
> 

దీని కోసం, మనం Visual Studio Code మరియు GitHub Copilot మరియు దాని ఏజెంట్ మోడ్‌ను ఉపయోగిస్తాము. మనం MCP సర్వర్‌ను *mcp.json*లో జోడిస్తాము. ఇలావుంటే Visual Studio Code ఏజెంటిక్ సామర్థ్యాలతో క్లయింట్గా పనిచేస్తుంది మరియు ఎండ్ యూజర్స్ ప్రాంప్ట్ టైప్ చేసి ఆ సర్వర్‌తో పరస్పరం చేసుకోవచ్చు.

ఎలా MCP సర్వర్‌ను Visual Studio Codeలో జోడించాలో చూద్దాం:

1. కమాండ్ ప్యాలెట్ నుండి MCP: **Add Server కమెండ్** ఉపయోగించండి.

1. ప్రాంప్ట్ వచ్చినప్పుడు సర్వర్ టైప్ ఎంచుకోండి: **HTTP (HTTP లేదా Server Sent Events)**.

1. API Managementలో MCP సర్వర్‌కు చూపిన Streamable HTTP URLని ఇన్పుట్ చేయండి.
    ఉదాహరణకి:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. మీ ఇష్టమైన సర్వర్ ID ని ఎంటర్ చేయండి. ఇది ముఖ్యమైన విలువ కాదు కానీ ఈ సర్వర్ ఇన్స్టెన్స్ గుర్తుంచుకునేందుకు ఇది సహాయపడుతుంది.

1. కాన్ఫిగరేషన్‌ని వర్క్‌స్పేస్ సెట్టింగ్స్ లేదా యూజర్ సెట్టింగ్స్‌లో సేవ్ చేయాలా అని ఎంచుకోండి.

  - **వర్క్‌స్పేస్ సెట్టింగ్స్** - సర్వర్ కాన్ఫిగరేషన్ .vscode/mcp.json ఫైల్‌లో మాత్రమే సేవ్ అవుతుంది, ప్రస్తుత వర్క్‌స్పేస్‌లో మాత్రమే అందుబాటులో ఉంటుంది.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **యూజర్ సెట్టింగ్స్** - సర్వర్ కాన్ఫిగరేషన్ మీ గ్లోబల్ *settings.json* ఫైల్‌లో చేర్చబడుతుంది మరియు అన్ని వర్క్‌స్పేస్‌లలో అందుబాటులో ఉంటుంది. కాన్ఫిగరేషన్ ఈ విధంగా ఉంటుంది:

    ![యూజర్ సెట్టింగ్](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. మీరు Azure API Management వైపు సరిగ్గా ప్రామాణికత పొందడానికి ఒక హెడ్డర్ జోడించాలి, ఇది **Ocp-Apim-Subscription-Key* అని పిలవబడుతుంది.

    - దీన్ని సెట్టింగ్స్‌లో ఎలా జోడించాలో ఇలా ఉంది:

    ![ఆథెంటికేషన్ కోసం హెడ్డర్ జోడించడం](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), దీనితో API కీ విలువ కోసం ప్రాంప్ట్ వచ్చి మీరు Azure పోర్టల్ మీద మీ Azure API Management ఇన్స్టెన్స్ కు సంబంధించిన కీలను పొందవచ్చు.

   - దీనిని *mcp.json*లో జోడించాలంటే, ఇలా చేయండి:

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

ఇప్పుడు మేము సెట్టింగ్స్ లేదా *.vscode/mcp.json*లో అన్ని సెట్ చేశాము. దీన్ని ప్రయత్నించుకుందాం.

ఈ విధంగా టూల్స్ ఐకాన్ కనిపించాలి, అందులో సర్వర్ నుంచి ఎక్స్‌పోజ్ చేసిన టూల్స్ లిస్ట్ గా ఉంటాయి:

![సర్వర్ నుంచి టూల్స్](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. టూల్స్ ఐకాన్ క్లిక్ చేయండి, మీరు ఈ విధంగా టూల్స్ జాబితాను చూడగలరు:

    ![టూల్స్](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. చాట్ లో ప్రాంప్ట్ ఎంటర్ చేసి టూల్‌ను పిలవండి. ఉదాహరణకి, మీరు ఆర్డర్ గురించి సమాచారం పొందడానికి టూల్ ఎంచుకున్నా, మీరు ఏజెంట్‌ని ఆ ఆర్డర్ గురించి అడగవచ్చు. ఇక్కడ ఒక ఉదాహరణ ప్రాంప్ట్ ఉంది:

    ```text
    get information from order 2
    ```

    ఇప్పుడు మీకు టూల్స్ ఐకాన్ తో టూల్ నడపమని ప్రాంప్ట్ వస్తుంది. కొనసాగించడానికి ఎంచుకోండి, ఇప్పుడు మీరు ఇలాంటిది అవుట్పుట్ చూడగలరు:

    ![ప్రాంప్ట్ ఫలితం](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **మీరు పైన ఏమి చూస్తున్నారో మీరు సెటప్ చేసిన టూల్స్‌పై ఆధారపడి ఉంటుంది, కానీ ఆలోచన ఏంటంటే మీరు ఇలాంటиба టెక్స్టువల్ ప్రతిస్పందన పొందుతారు**


## సూచనలు

ఇలా మీరు మరింత తెలుసుకోవచ్చు:

- [Azure API Management మరియు MCP పై ట్యుటోరియల్](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python నమూనా: Azure API Management ఉపయోగించి రిమోట్ MCP సర్వర్‌లను భద్రపరచడం (ప్రయోగాత్మకం)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP క్లయింట్ ఆథరైజేషన్ ల్యాబ్](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS కోడ్ కోసం Azure API Management విస్తరణ ఉపయోగించి APIs దిగుమతి మరియు నిర్వహణ](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Centerలో రిమోట్ MCP సర్వర్‌లను నమోదు చేయడం మరియు కనుగొనడం](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI గేట్‌వే](https://github.com/Azure-Samples/AI-Gateway) Azure API Managementతో అనేక AI సామర్థ్యాలను చూపించే అద్భుతమైన రీపో.
- [AI గేట్‌వే వర్క్షాప్‌లు](https://azure-samples.github.io/AI-Gateway/) Azure పోర్టల్ ఉపయోగించి, AI సామర్థ్యాలను అంచనా వేయటం ప్రారంభించడానికి గొప్ప మార్గం.

## తరువాతి చర్య

- తిరుగు: [కేస్ స్టడీస్ అవలోకనం](./README.md)
- తదుపరి: [Azure AI ట్రావల్ ఏజెంట్స్](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
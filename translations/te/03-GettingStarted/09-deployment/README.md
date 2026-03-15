# MCP సర్వర్‌లను అమలు చేయడం

మీ MCP సర్వర్‌ను అమలు చేయడం ద్వారా ఇతరులు మీ స్థానిక పర్యావరణంతో పాటు దాని ఉపకరణాలు మరియు వనరులను యాక్సెస్ చేయగలుగుతారు. మీ విస్తరణా, విశ్వసనీయత, మరియు నిర్వహణ సౌకర్యంపై ఆధారపడిన deployment వ్యూహాలను పరిగణనలోకి తీసుకోవాలి. దిగువ మీరు MCP సర్వర్‌లను స్థానికంగా, కంటైనర్‌లలో మరియు క్లౌడ్‌లో అమలు చేయడానికి మార్గనిర్దేశం పొందబోతున్నారు.

## అవలోకనం

ఈ పాఠం మీ MCP సర్వర్ యాప్‌ను ఎలా అమలు చేయాలో తెలుపుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసే సమయం వరకు, మీరు క్రింది పనులను చేయగలుగుతారు:

- వివిధ deployment దృష్టాంతాలను పరిశీలించండి.
- మీ యాప్‌ను అమలు చేయండి.

## స్థానిక అభివృద్ధి మరియు deployment

మీ సర్వర్ వినియోగదారుల యంత్రంలో నడపబడేందుకు ఉద్దేశించబడినట్లయితే, మీరు క్రింద పేర్కొన్న దశలను అనుసరించవచ్చు:

1. **సర్వర్‌ను డౌన్లోడ్ చేయండి**. మీరు సర్వర్‌ను రాయకపోతే, మొదట దానిని మీ యంత్రంలో డౌన్లోడ్ చేసుకోండి.
1. **సర్వర్ ప్రాసెస్‌ను ప్రారంభించండి**: మీ MCP సర్వర్ అప్లికేషన్‌ను నడపండి

SSE కోసం (stdio తరహా సర్వర్‌కు అవసరం లేదు)

1. **నెట్వర్కింగ్‌ను కాన్ఫిగర్ చేయండి**: సర్వర్‌ను ఆశించిన పోర్ట్‌లో అందుబాటులో ఉంచండి
1. **క్లయింట్‌లను కనెక్ట్ చేయండి**: `http://localhost:3000` వంటి స్థానిక కనెక్షన్ URLs ఉపయోగించండి

## క్లౌడ్ deployment

MCP సర్వర్‌లను వివిధ క్లౌడ్ ప్లాట్‌ఫామ్లలో అమలు చేయవచ్చు:

- **సర్వర్‌లెస్ ఫంక్షన్స్**: లైట్ వెయిట్ MCP సర్వర్‌లను సర్వర్‌లెస్ ఫంక్షన్‌లుగా అమలు చేయండి
- **కంటైనర్ సర్వీసులు**: Azure Container Apps, AWS ECS, లేదా Google Cloud Run వంటి సర్వీసులను ఉపయోగించండి
- **కుబెర్నెటెస్**: MCP సర్వర్‌లను హై అవైలబిలిటీ కోసం కుబెర్నెటెస్ క్లస్టర్లలో అమలు మరియు నిర్వహించండి

### ఉదాహరణ: Azure Container Apps

Azure Container Apps MCP సర్వర్‌ల deploymentని మద్దతు ఇస్తుంది. ఇది ఇంకా అభివృద్ది లో ఉంది మరియు ప్రస్తుతం SSE సర్వర్‌లను మద్దతు ఇస్తుంది.

ఇలా చేయవచ్చు:

1. ఒక రిపోను క్లోన్ చేయండి:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. విషయాలను పరీక్షించడానికి స్థానికంగా నడపండి:

  ```sh
  uv venv
  uv sync

  # లీనక్స్/మ్యాక్OS
  export API_KEYS=<AN_API_KEY>
  # విండోస్
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. దీనిని స్థానికంగా ప్రయత్నించడానికి, *.vscode* డైరెక్టరీలో *mcp.json* ఫైల్ సృష్టించి క్రింది కంటెంట్‌ను జోడించండి:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  SSE సర్వర్ ప్రారంభించిన తర్వాత, మీరు JSON ఫైల్‌లో ప్లే آئికాన్‌పై క్లిక్ చేయండి, మీరు ఇప్పుడు సర్వర్‌పై GitHub Copilot ద్వారా ఉపకరణాలు ఎరిగిపోగా కనిపిస్తాయి, Tool ఐకాన్‌ని చూడండి.

1. Deployment చేయడానికి, క్రింది కమాండ్ను అమలు చేయండి:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

ఇక్కడ ఉంది, స్థానికంగా deploy చేయండి, Azureకు ఈ దశల ద్వారా deploy చేయండి.

## అదనపు వనరులు

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## తదుపరి ఏమిటి

- తదుపరి: [అధ్యత్య Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**డిస్క్లెయిమర్**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మనము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో లోపాలు లేదా అసంపూర్ణతలు ఉండవచ్చు. మూల పత్రం దాని స్వీయ భాషలో అధికారిక మూలంగా పరిగణించాలి. ప్రధానమైన సమాచారం కోసం, వృత్తిపరమైన మనిషి అనువాదాన్ని ఆలోచించడం మంచిది. ఈ అనువాదం ఉపయోగం వల్ల వచ్చిన ఏవైనా ভুল అర్థం చేసుకోలాపులు లేదా తప్పుదెబ్బలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP सर्वर तैनात करना

अपने MCP सर्वर को तैनात करने से अन्य लोग आपके स्थानीय वातावरण से बाहर इसके उपकरणों और संसाधनों तक पहुंच सकते हैं। आपके पैमाने, विश्वसनीयता और प्रबंधन की आसानी की आवश्यकताओं के आधार पर तैनाती के कई रणनीतियाँ हैं। नीचे आपको स्थानीय, कंटेनरों में, और क्लाउड में MCP सर्वर तैनात करने के लिए मार्गदर्शन मिलेगा।

## अवलोकन

यह पाठ आयुक्त MCP सर्वर ऐप को तैनात करने के तरीके को कवर करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- विभिन्न तैनाती दृष्टिकोणों का मूल्यांकन करें।
- अपना ऐप तैनात करें।

## स्थानीय विकास और तैनाती

यदि आपका सर्वर उपयोगकर्ता के कंप्यूटर पर चलाकर उपभोग करने के लिए है, तो आप निम्नलिखित चरणों का पालन कर सकते हैं:

1. **सर्वर डाउनलोड करें**। यदि आपने सर्वर नहीं लिखा है, तो पहले इसे अपनी मशीन पर डाउनलोड करें।  
1. **सर्वर प्रक्रिया शुरू करें**: अपना MCP सर्वर एप्लिकेशन चलाएं

SSE के लिए (stdio प्रकार के सर्वर के लिए आवश्यक नहीं)

1. **नेटवर्किंग कॉन्फ़िगर करें**: सुनिश्चित करें कि सर्वर अपेक्षित पोर्ट पर सुलभ है  
1. **क्लाइंट कनेक्ट करें**: `http://localhost:3000` जैसे स्थानीय कनेक्शन URL का उपयोग करें

## क्लाउड तैनाती

MCP सर्वर विभिन्न क्लाउड प्लेटफॉर्म पर तैनात किए जा सकते हैं:

- **सर्वरलेस फंक्शंस**: हल्के MCP सर्वरों को सर्वरलेस फंक्शंस के रूप में तैनात करें  
- **कंटेनर सेवाएं**: Azure Container Apps, AWS ECS, या Google Cloud Run जैसी सेवाओं का उपयोग करें  
- **कुबेरनेटिस**: उच्च उपलब्धता के लिए कुबेरनेटिस क्लस्टर में MCP सर्वरों को तैनात और प्रबंधित करें

### उदाहरण: Azure Container Apps

Azure Container Apps MCP सर्वरों की तैनाती का समर्थन करते हैं। यह अभी भी प्रगति पर है और वर्तमान में SSE सर्वरों का समर्थन करता है।

आप इसे इस प्रकार कर सकते हैं:

1. एक रिपोजिटरी क्लोन करें:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. इसे स्थानीय रूप से चलाकर परीक्षण करें:

  ```sh
  uv venv
  uv sync

  # लिनक्स/macOS
  export API_KEYS=<AN_API_KEY>
  # विंडोज
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. इसे स्थानीय रूप से आजमाने के लिए, *.vscode* निर्देशिका में एक *mcp.json* फ़ाइल बनाएं और निम्नलिखित सामग्री जोड़ें:

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
  
   एक बार SSE सर्वर शुरू होने के बाद, आप JSON फ़ाइल में प्ले आइकन पर क्लिक कर सकते हैं, अब आपको सर्वर पर उपकरण GitHub Copilot द्वारा उठाए गए दिखाई देंगे, उपकरण आइकन देखें।

1. तैनात करने के लिए, निम्नलिखित कमांड चलाएं:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```
  
बस हो गया, इसे स्थानीय रूप से तैनात करें, इन चरणों के माध्यम से इसे Azure पर तैनात करें।

## अतिरिक्त संसाधन

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps लेख](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP रिपो](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## अगला क्या है

- अगले: [एडवांस्ड सर्वर टॉपिक्स](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियां या असंगतताएं हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की अनुशंसा की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या भ्रम के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
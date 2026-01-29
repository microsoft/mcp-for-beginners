# MCP सर्वर तैनात करना

अपने MCP सर्वर को तैनात करने से अन्य लोग आपके स्थानीय वातावरण से बाहर इसके टूल और संसाधनों तक पहुंच सकते हैं। आपकी आवश्यकताओं के अनुसार, जैसे कि स्केलेबिलिटी, विश्वसनीयता, और प्रबंधन की आसानी, कई तैनाती रणनीतियाँ हैं। नीचे आपको स्थानीय, कंटेनरों में, और क्लाउड में MCP सर्वर तैनात करने के लिए मार्गदर्शन मिलेगा।

## अवलोकन

यह पाठ आपके MCP Server ऐप को तैनात करने के तरीके को कवर करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- विभिन्न तैनाती दृष्टिकोणों का मूल्यांकन करना।
- अपना ऐप तैनात करना।

## स्थानीय विकास और तैनाती

यदि आपका सर्वर उपयोगकर्ताओं के मशीन पर चलाने के लिए है, तो आप निम्नलिखित चरणों का पालन कर सकते हैं:

1. **सर्वर डाउनलोड करें**। यदि आपने सर्वर नहीं लिखा है, तो पहले इसे अपनी मशीन पर डाउनलोड करें।  
1. **सर्वर प्रक्रिया शुरू करें**: अपना MCP सर्वर एप्लिकेशन चलाएं।

SSE के लिए (stdio प्रकार के सर्वर के लिए आवश्यक नहीं)

1. **नेटवर्किंग कॉन्फ़िगर करें**: सुनिश्चित करें कि सर्वर अपेक्षित पोर्ट पर सुलभ है।  
1. **क्लाइंट कनेक्ट करें**: स्थानीय कनेक्शन URL जैसे `http://localhost:3000` का उपयोग करें।

## क्लाउड तैनाती

MCP सर्वर विभिन्न क्लाउड प्लेटफॉर्म पर तैनात किए जा सकते हैं:

- **Serverless Functions**: हल्के MCP सर्वर को serverless functions के रूप में तैनात करें।  
- **Container Services**: Azure Container Apps, AWS ECS, या Google Cloud Run जैसी सेवाओं का उपयोग करें।  
- **Kubernetes**: उच्च उपलब्धता के लिए Kubernetes क्लस्टर में MCP सर्वर तैनात और प्रबंधित करें।

### उदाहरण: Azure Container Apps

Azure Container Apps MCP Servers की तैनाती का समर्थन करते हैं। यह अभी भी विकासाधीन है और वर्तमान में SSE सर्वरों का समर्थन करता है।

इसे करने का तरीका इस प्रकार है:

1. एक रिपॉजिटरी क्लोन करें:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. इसे स्थानीय रूप से चलाकर परीक्षण करें:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. स्थानीय रूप से आज़माने के लिए, *.vscode* डायरेक्टरी में *mcp.json* फ़ाइल बनाएं और निम्नलिखित सामग्री जोड़ें:

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

  एक बार SSE सर्वर शुरू हो जाने पर, आप JSON फ़ाइल में प्ले आइकन पर क्लिक कर सकते हैं, अब आपको GitHub Copilot द्वारा सर्वर पर टूल्स को पहचाना जाना चाहिए, टूल आइकन देखें।

1. तैनात करने के लिए, निम्नलिखित कमांड चलाएं:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

बस, इसे स्थानीय रूप से तैनात करें, या इन चरणों के माध्यम से Azure पर तैनात करें।

## अतिरिक्त संसाधन

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps लेख](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP रिपॉजिटरी](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## आगे क्या है

- अगला: [व्यावहारिक कार्यान्वयन](../../04-PracticalImplementation/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
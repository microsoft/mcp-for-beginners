# MCP सर्व्हर्सची तैनाती

तुमचा MCP सर्व्हर तैनात केल्याने इतर लोकांना त्याच्या साधनां आणि संसाधनांपर्यंत तुमच्या स्थानिक वातावरणाबाहेरही प्रवेश मिळू शकतो. स्केलेबिलिटी, विश्वासार्हता आणि व्यवस्थापन सुलभतेच्या गरजेनुसार विविध तैनाती धोरणे विचारात घेता येतात. खाली तुम्हाला स्थानिक, कंटेनरमध्ये आणि क्लाउडवर MCP सर्व्हर्स तैनात करण्यासाठी मार्गदर्शन मिळेल.

## आढावा

हा धडा तुमचा MCP Server अॅप कसा तैनात करायचा हे शिकवतो.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- वेगवेगळ्या तैनाती पद्धतींचे मूल्यमापन करणे.
- तुमचा अॅप तैनात करणे.

## स्थानिक विकास आणि तैनाती

जर तुमचा सर्व्हर वापरकर्त्यांच्या संगणकावर चालवण्यासाठी असेल, तर तुम्ही खालील पायऱ्या अनुसरू शकता:

1. **सर्व्हर डाउनलोड करा**. जर तुम्ही सर्व्हर लिहिला नसेल, तर प्रथम तो तुमच्या संगणकावर डाउनलोड करा.
1. **सर्व्हर प्रक्रिया सुरू करा**: तुमचा MCP सर्व्हर अॅप्लिकेशन चालवा.

SSE साठी (stdio प्रकारच्या सर्व्हरसाठी आवश्यक नाही)

1. **नेटवर्किंग कॉन्फिगर करा**: सर्व्हर अपेक्षित पोर्टवर प्रवेशयोग्य आहे याची खात्री करा.
1. **क्लायंट कनेक्ट करा**: `http://localhost:3000` सारख्या स्थानिक कनेक्शन URL वापरा.

## क्लाउड तैनाती

MCP सर्व्हर्स विविध क्लाउड प्लॅटफॉर्मवर तैनात करता येतात:

- **सर्व्हरलेस फंक्शन्स**: हलक्या MCP सर्व्हर्सना सर्व्हरलेस फंक्शन्स म्हणून तैनात करा.
- **कंटेनर सेवा**: Azure Container Apps, AWS ECS, किंवा Google Cloud Run सारख्या सेवांचा वापर करा.
- **कुबेरनेट्स**: उच्च उपलब्धतेसाठी कुबेरनेट्स क्लस्टरमध्ये MCP सर्व्हर्स तैनात आणि व्यवस्थापित करा.

### उदाहरण: Azure Container Apps

Azure Container Apps MCP Servers ची तैनाती समर्थित करतात. हे अजून प्रगतीच्या टप्प्यात आहे आणि सध्या SSE सर्व्हर्सना समर्थन देते.

हे कसे करायचे:

1. एक रेपो क्लोन करा:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. स्थानिकपणे चालवून तपासा:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. स्थानिकपणे वापरण्यासाठी, *.vscode* फोल्डरमध्ये *mcp.json* फाइल तयार करा आणि खालील सामग्री जोडा:

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

  SSE सर्व्हर सुरू झाल्यानंतर, JSON फाइलमधील प्ले आयकॉनवर क्लिक करा, तुम्हाला आता GitHub Copilot द्वारे सर्व्हरवरील साधने दिसतील, Tool आयकॉन पहा.

1. तैनात करण्यासाठी, खालील कमांड चालवा:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

असे करून तुम्ही स्थानिकपणे किंवा Azure वर या पायऱ्यांद्वारे तैनात करू शकता.

## अतिरिक्त संसाधने

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps लेख](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP रेपो](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## पुढे काय

- पुढे: [Practical Implementation](../../04-PracticalImplementation/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
# केस स्टडी: API Management में MCP सर्वर के रूप में REST API को एक्सपोज़ करें

Azure API Management, एक सेवा है जो आपके API एंडपॉइंट्स के ऊपर गेटवे प्रदान करती है। इसका काम यह है कि Azure API Management आपके APIs के सामने एक प्रॉक्सी की तरह काम करता है और पता लगाता है कि आने वाले अनुरोधों के साथ क्या करना है।

इसका उपयोग करके, आप कई सुविधाएं जोड़ते हैं जैसे:

- **सुरक्षा**, आप API keys, JWT से लेकर managed identity तक सब कुछ उपयोग कर सकते हैं।
- **रेट लिमिटिंग**, एक शानदार सुविधा है यह निर्धारित करना कि प्रति निश्चित समय इकाई में कितनी कॉल्स गुजर सकती हैं। यह सुनिश्चित करता है कि सभी उपयोगकर्ताओं को एक अच्छा अनुभव मिले और आपकी सेवा अनुरोधों से अभिभूत न हो।
- **स्केलिंग और लोड बैलेंसिंग**। आप कई एंडपॉइंट सेट कर सकते हैं लोड बैलेंस करने के लिए और आप यह भी तय कर सकते हैं कि "लोड बैलेंस" कैसे करना है।
- **AI सुविधाएँ जैसे सेमांटिक कैशिंग**, टोकन लिमिट और टोकन मॉनिटरिंग और भी बहुत कुछ। ये शानदार फीचर्स हैं जो प्रतिक्रिया क्षमता को बेहतर बनाते हैं और साथ ही आपके टोकन खर्च पर नियंत्रण रखने में मदद करते हैं। [यहाँ और पढ़ें](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## MCP + Azure API Management क्यों?

मॉडल कॉन्टेक्स्ट प्रोटोकॉल तेजी से एजेंटिक AI ऐप्स के लिए एक मानक बन रहा है और इसे टूल्स और डेटा को एक सुसंगत तरीके से एक्सपोज़ करने के लिए उपयोग किया जाता है। जब आपको APIs "प्रबंधित" करने की आवश्यकता होती है तो Azure API Management एक स्वाभाविक विकल्प है। MCP सर्वर अक्सर अन्य APIs के साथ एकीकृत होता है ताकि अनुरोधों को टूल तक हल किया जा सके। इसलिए Azure API Management और MCP को मिलाना बहुत सार्थक है।

## अवलोकन

इस विशिष्ट उपयोग मामले में हम सीखेंगे कि कैसे API एंडपॉइंट्स को MCP सर्वर के रूप में एक्सपोज़ किया जाए। ऐसा करके, हम आसानी से इन एंडपॉइंट्स को एक एजेंटिक ऐप का हिस्सा बना सकते हैं साथ ही Azure API Management की सुविधाओं का लाभ उठा सकते हैं।

## मुख्य विशेषताएँ

- आप उन एंडपॉइंट मेथड्स का चयन करते हैं जिन्हें आप टूल्स के रूप में एक्सपोज़ करना चाहते हैं।
- जो अतिरिक्त सुविधाएं आपको मिलती हैं, वे इस बात पर निर्भर करती हैं कि आप अपनी API के पॉलिसी सेक्शन में क्या कॉन्फ़िगर करते हैं। लेकिन यहाँ हम आपको दिखाएंगे कि आप रेट लिमिट कैसे जोड़ सकते हैं।

## पूर्व-चरण: API इम्पोर्ट करें

यदि आपके पास पहले से Azure API Management में कोई API है तो बहुत बढ़िया, आप इस चरण को छोड़ सकते हैं। यदि नहीं, तो इस लिंक को देखें, [Azure API Management में API इम्पोर्ट करना](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API को MCP सर्वर के रूप में एक्सपोज़ करें

API एंडपॉइंट्स को एक्सपोज़ करने के लिए, निम्न चरणों का पालन करें:

1. Azure पोर्टल पर जाएं और इस पता पर नेविगेट करें <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
अपनी API Management इंस्टेंस पर जाएं।

1. बाएं मेनू में, APIs > MCP Servers > + Create new MCP Server चुनें।

1. API में, एक REST API को चयनित करें जिसे MCP सर्वर के रूप में एक्सपोज़ करना हो।

1. एक या अधिक API ऑपरेशन्स को टूल्स के रूप में एक्सपोज़ करने के लिए चुनें। आप सभी ऑपरेशन्स या केवल कुछ विशिष्ट ऑपरेशन्स चुन सकते हैं।

    ![एक्सपोज़ करने के लिए मेथड्स चुनें](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** चुनें।

1. मेनू विकल्प **APIs** और **MCP Servers** पर नेविगेट करें, आपको निम्न दिखना चाहिए:

    ![मुख्य पेन में MCP सर्वर देखें](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्वर बन गया है और API ऑपरेशन्स टूल्स के रूप में एक्सपोज़ किए गए हैं। MCP सर्वर MCP Servers पैन में सूचीबद्ध है। URL कॉलम MCP सर्वर के एंडपॉइंट को दिखाता है जिसे आप परीक्षण के लिए या क्लाइंट एप्लिकेशन में कॉल कर सकते हैं।

## वैकल्पिक: नीतियाँ कॉन्फ़िगर करें

Azure API Management में पॉलिसीज़ का मूल कॉन्सेप्ट है जहाँ आप अपने एंडपॉइंट्स के लिए विभिन्न नियम सेट करते हैं जैसे कि रेट लिमिटिंग या सेमांटिक कैशिंग। ये नीतियाँ XML में निर्मित होती हैं।

यहाँ बताया गया है कि आप अपनी MCP सर्वर के लिए रेट लिमिट लागू करने के लिए नीति कैसे सेट कर सकते हैं:

1. पोर्टल में, APIs के अंतर्गत, **MCP Servers** चुनें।

1. उस MCP सर्वर का चयन करें जिसे आपने बनाया है।

1. बाएं मेनू में, MCP के अंतर्गत **Policies** चुनें।

1. नीति संपादक में, उन नीतियों को जोड़ें या संपादित करें जिन्हें आप MCP सर्वर के टूल्स पर लागू करना चाहते हैं। नीतियां XML प्रारूप में परिभाषित होती हैं। उदाहरण के लिए, आप एक नीति जोड़ सकते हैं जो MCP सर्वर के टूल्स के कॉल्स को सीमित करती है (इस उदाहरण में, प्रति क्लाइंट IP पते 30 सेकंड में 5 कॉल्स)। XML कुछ यूं दिखेगा:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    नीति संपादक की एक छवि यहाँ है:

    ![नीति संपादक](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## इसे आज़माएँ

आइए सुनिश्चित करें कि हमारा MCP सर्वर इच्छित रूप से काम कर रहा है।

> [!NOTE]
> Azure API Management वर्तमान में इस सर्वर को Streamable
> HTTP `/mcp` एंडपॉइंट के माध्यम से एक्सपोज़ करता है। पुराना HTTP+SSE `/sse` ट्रांसपोर्ट असमर्थित है और
> इसे केवल पुराने क्लाइंट्स के साथ उपयोग किया जाना चाहिए।

इसके लिए, हम Visual Studio Code और GitHub Copilot के Agent मोड का उपयोग करेंगे। हम MCP सर्वर को *mcp.json* में जोड़ेंगे। ऐसा करने से, Visual Studio Code एजेंटिक क्षमताओं वाला क्लाइंट के रूप में कार्य करेगा और अंतिम उपयोगकर्ता एक प्रांप्ट टाइप करके उस सर्वर के साथ इंटरैक्ट कर पाएंगे।

आइए देखें कि Visual Studio Code में MCP सर्वर कैसे जोड़ा जाए:

1. कमांड पैलेट से MCP: **Add Server कमांड का उपयोग करें**।

1. जब पूछा जाए, तो सर्वर प्रकार चुनें: **HTTP (HTTP या Server Sent Events)**।

1. API Management में MCP सर्वर के लिए दिखाए गए Streamable HTTP URL दर्ज करें।
    उदाहरण के लिए:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`।

1. अपनी पसंद का सर्वर ID दर्ज करें। यह महत्वपूर्ण मान नहीं है लेकिन इससे आपको यह याद रखने में मदद मिलेगी कि यह सर्वर इंस्टेंस क्या है।

1. निर्धारित करें कि कॉन्फ़िगरेशन को आपकी वर्कस्पेस सेटिंग्स में या यूज़र सेटिंग्स में सेव करना है।

- **वर्कस्पेस सेटिंग्स** - सर्वर कॉन्फ़िगरेशन केवल वर्तमान वर्कस्पेस में उपलब्ध .vscode/mcp.json फ़ाइल में सेव होता है।

*mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

- **यूज़र सेटिंग्स** - सर्वर कॉन्फ़िगरेशन आपकी वैश्विक *settings.json* फ़ाइल में जोड़ा जाता है और सभी वर्कस्पेसेस में उपलब्ध होता है। कॉन्फ़िगरेशन इस प्रकार दिखती है:

    ![यूज़र सेटिंग](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. आपको एक हेडर भी जोड़ना होगा ताकि यह Azure API Management के प्रति सही तरीके से प्रमाणीकृत हो सके। इसका उपयोग होता है एक हेडर जिसका नाम है **Ocp-Apim-Subscription-Key*।

    - सेटिंग्स में इसे जोड़ने का तरीका यहाँ है:

    ![प्रमाणीकरण के लिए हेडर जोड़ना](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), इससे एक प्रांप्ट दिखाई देगा जो आपसे API key का मान पूछेगा जिसे आप Azure पोर्टल में अपनी Azure API Management इंस्टेंस के लिए पा सकते हैं।

   - इसे *mcp.json* में जोड़ने के लिए, आप इसे इस प्रकार जोड़ सकते हैं:

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

### एजेंट मोड का उपयोग करें

अब हम सेटिंग्स में या *.vscode/mcp.json* में पूरी तरह से सेटअप हो चुके हैं। इसे आज़माएँ।

एक टूल्स आइकन होना चाहिए, जहाँ आपके सर्वर से एक्सपोज़ किए गए टूल्स सूचीबद्ध हों:

![सर्वर से टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. टूल्स आइकन पर क्लिक करें, आपको टूल्स की एक सूची इस प्रकार दिखनी चाहिए:

    ![टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. टूल को कॉल करने के लिए चैट में एक प्रांप्ट डालें। उदाहरण के लिए, यदि आपने एक टूल चुना है जो एक ऑर्डर के बारे में जानकारी देता है, तो आप एजेंट से ऑर्डर के बारे में पूछ सकते हैं। यहाँ एक उदाहरण प्रांप्ट है:

    ```text
    get information from order 2
    ```

    अब आपको एक टूल्स आइकन दिखाई देगा जो आपसे टूल कॉल करने को कहेगा। टूल चलाने के लिए चयन करें, आपको अब इस प्रकार का आउटपुट दिखाई देगा:

    ![प्रांप्ट से परिणाम](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **आपको ऊपर जो दिख रहा है वह इस बात पर निर्भर करता है कि आपने कौन से टूल्स सेटअप किए हैं, लेकिन विचार यह है कि आपको ऊपर दिखाए गए जैसे एक टेक्स्टुअल प्रतिक्रिया प्राप्त होती है।**


## संदर्भ

यहाँ आप अधिक जान सकते हैं:

- [Azure API Management और MCP पर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python उदाहरण: Azure API Management का उपयोग करके सुरक्षित रिमोट MCP सर्वर (प्रयोगात्मक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लाइंट प्राधिकरण लैब](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code के लिए Azure API Management एक्सटेंशन का उपयोग कर API इम्पोर्ट और प्रबंधित करें](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center में रिमोट MCP सर्वर को रजिस्टर और डिस्कवर करें](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) एक बेहतरीन रिपॉजिटरी जो Azure API Management के साथ कई AI क्षमताएँ दर्शाती है
- [AI Gateway कार्यशालाएँ](https://azure-samples.github.io/AI-Gateway/) जिसमें Azure पोर्टल का उपयोग करके कार्यशालाएँ शामिल हैं, जो AI क्षमताओं का मूल्यांकन शुरू करने का एक बेहतरीन तरीका है।

## अगला क्या है

- वापिस जाएं: [केस स्टडीज़ अवलोकन](./README.md)
- अगला: [Azure AI ट्रैवल एजेंट्स](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
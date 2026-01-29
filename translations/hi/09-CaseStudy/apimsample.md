# केस स्टडी: API मैनेजमेंट में REST API को MCP सर्वर के रूप में एक्सपोज़ करना

Azure API Management एक सेवा है जो आपके API एंडपॉइंट्स के ऊपर एक गेटवे प्रदान करती है। यह इस तरह काम करता है कि Azure API Management आपके APIs के सामने एक प्रॉक्सी की तरह कार्य करता है और यह तय करता है कि आने वाले अनुरोधों के साथ क्या करना है।

इसे उपयोग करने से आप कई सुविधाएँ जोड़ सकते हैं, जैसे:

- **सुरक्षा**, आप API कीज़, JWT से लेकर मैनेज्ड आइडेंटिटी तक सब कुछ उपयोग कर सकते हैं।
- **रेट लिमिटिंग**, यह एक शानदार फीचर है जो यह तय करने में मदद करता है कि एक निश्चित समय इकाई में कितने कॉल्स को अनुमति दी जाए। यह सुनिश्चित करता है कि सभी उपयोगकर्ताओं को एक अच्छा अनुभव मिले और आपकी सेवा अनुरोधों से अभिभूत न हो।
- **स्केलिंग और लोड बैलेंसिंग**, आप लोड को संतुलित करने के लिए कई एंडपॉइंट्स सेट कर सकते हैं और यह भी तय कर सकते हैं कि "लोड बैलेंस" कैसे किया जाए।
- **AI फीचर्स जैसे सेमांटिक कैशिंग**, टोकन लिमिट और टोकन मॉनिटरिंग। ये शानदार फीचर्स हैं जो प्रतिक्रिया समय को बेहतर बनाते हैं और आपके टोकन खर्च पर नज़र रखने में मदद करते हैं। [यहाँ और पढ़ें](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## MCP + Azure API Management क्यों?

Model Context Protocol (MCP) तेजी से एजेंटिक AI ऐप्स के लिए एक मानक बन रहा है और टूल्स और डेटा को एक सुसंगत तरीके से एक्सपोज़ करने का तरीका प्रदान करता है। जब आपको APIs को "मैनेज" करना हो, तो Azure API Management एक स्वाभाविक विकल्प है। MCP सर्वर अक्सर अन्य APIs के साथ इंटीग्रेट होते हैं ताकि किसी टूल के लिए अनुरोधों को हल किया जा सके। इसलिए Azure API Management और MCP का संयोजन बहुत समझदारी भरा है।

## अवलोकन

इस विशेष उपयोग केस में, हम सीखेंगे कि API एंडपॉइंट्स को MCP सर्वर के रूप में कैसे एक्सपोज़ किया जाए। ऐसा करके, हम इन एंडपॉइंट्स को एक एजेंटिक ऐप का हिस्सा आसानी से बना सकते हैं और साथ ही Azure API Management की सुविधाओं का लाभ उठा सकते हैं।

## मुख्य विशेषताएँ

- आप उन एंडपॉइंट मेथड्स को चुन सकते हैं जिन्हें आप टूल्स के रूप में एक्सपोज़ करना चाहते हैं।
- अतिरिक्त सुविधाएँ इस पर निर्भर करती हैं कि आपने अपनी API के लिए पॉलिसी सेक्शन में क्या कॉन्फ़िगर किया है। लेकिन यहाँ हम आपको दिखाएंगे कि रेट लिमिटिंग कैसे जोड़ी जा सकती है।

## प्रारंभिक चरण: एक API आयात करें

यदि आपके पास पहले से ही Azure API Management में एक API है, तो यह शानदार है, आप इस चरण को छोड़ सकते हैं। यदि नहीं, तो इस लिंक को देखें: [Azure API Management में API आयात करना](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API को MCP सर्वर के रूप में एक्सपोज़ करें

API एंडपॉइंट्स को एक्सपोज़ करने के लिए, निम्न चरणों का पालन करें:

1. Azure पोर्टल पर जाएँ और इस पते पर नेविगेट करें: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>। अपनी API Management इंस्टेंस पर जाएँ।

1. बाएँ मेनू में, **APIs > MCP Servers > + Create new MCP Server** चुनें।

1. API में, एक REST API चुनें जिसे MCP सर्वर के रूप में एक्सपोज़ करना है।

1. एक या अधिक API ऑपरेशंस को टूल्स के रूप में एक्सपोज़ करने के लिए चुनें। आप सभी ऑपरेशंस या केवल विशिष्ट ऑपरेशंस का चयन कर सकते हैं।

    ![एक्सपोज़ करने के लिए मेथड्स चुनें](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** चुनें।

1. मेनू विकल्प **APIs** और **MCP Servers** पर जाएँ, आपको निम्नलिखित दिखाई देगा:

    ![मुख्य पैन में MCP सर्वर देखें](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्वर बनाया गया है और API ऑपरेशंस को टूल्स के रूप में एक्सपोज़ किया गया है। MCP सर्वर MCP Servers पैन में सूचीबद्ध है। URL कॉलम MCP सर्वर का एंडपॉइंट दिखाता है जिसे आप परीक्षण या क्लाइंट एप्लिकेशन के भीतर कॉल कर सकते हैं।

## वैकल्पिक: पॉलिसी कॉन्फ़िगर करें

Azure API Management में पॉलिसीज़ का मुख्य कॉन्सेप्ट है, जहाँ आप अपने एंडपॉइंट्स के लिए विभिन्न नियम सेट कर सकते हैं, जैसे रेट लिमिटिंग या सेमांटिक कैशिंग। ये पॉलिसीज़ XML में लिखी जाती हैं।

यहाँ बताया गया है कि आप अपने MCP सर्वर के लिए रेट लिमिटिंग पॉलिसी कैसे सेट कर सकते हैं:

1. पोर्टल में, **APIs** के तहत, **MCP Servers** चुनें।

1. उस MCP सर्वर को चुनें जिसे आपने बनाया है।

1. बाएँ मेनू में, MCP के तहत, **Policies** चुनें।

1. पॉलिसी एडिटर में, उन पॉलिसीज़ को जोड़ें या संपादित करें जिन्हें आप MCP सर्वर के टूल्स पर लागू करना चाहते हैं। पॉलिसीज़ XML फॉर्मेट में परिभाषित की जाती हैं। उदाहरण के लिए, आप एक पॉलिसी जोड़ सकते हैं जो MCP सर्वर के टूल्स पर कॉल्स को सीमित करती है (इस उदाहरण में, प्रति क्लाइंट IP एड्रेस 30 सेकंड में 5 कॉल्स)। यहाँ XML है जो इसे रेट लिमिट करेगा:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    पॉलिसी एडिटर की एक छवि:

    ![पॉलिसी एडिटर](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## इसे आज़माएँ

आइए सुनिश्चित करें कि हमारा MCP सर्वर सही तरीके से काम कर रहा है।

इसके लिए, हम Visual Studio Code और GitHub Copilot और इसके Agent मोड का उपयोग करेंगे। हम MCP सर्वर को एक *mcp.json* फ़ाइल में जोड़ेंगे। ऐसा करने से, Visual Studio Code एक क्लाइंट के रूप में कार्य करेगा जिसमें एजेंटिक क्षमताएँ होंगी और अंतिम उपयोगकर्ता एक प्रॉम्प्ट टाइप करके सर्वर के साथ इंटरैक्ट कर सकेंगे।

आइए देखें कि Visual Studio Code में MCP सर्वर कैसे जोड़ें:

1. कमांड पैलेट से MCP: **Add Server कमांड** का उपयोग करें।

1. जब पूछा जाए, तो सर्वर प्रकार चुनें: **HTTP (HTTP या Server Sent Events)**।

1. Azure API Management में MCP सर्वर का URL दर्ज करें। उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE एंडपॉइंट के लिए) या **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP एंडपॉइंट के लिए), ध्यान दें कि ट्रांसपोर्ट के बीच अंतर `/sse` या `/mcp` है।

1. अपनी पसंद का एक सर्वर ID दर्ज करें। यह एक महत्वपूर्ण मान नहीं है लेकिन यह आपको याद रखने में मदद करेगा कि यह सर्वर इंस्टेंस क्या है।

1. तय करें कि कॉन्फ़िगरेशन को अपने वर्कस्पेस सेटिंग्स में सहेजना है या उपयोगकर्ता सेटिंग्स में।

  - **वर्कस्पेस सेटिंग्स** - सर्वर कॉन्फ़िगरेशन केवल वर्तमान वर्कस्पेस में उपलब्ध .vscode/mcp.json फ़ाइल में सहेजा जाता है।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    या यदि आप ट्रांसपोर्ट के रूप में स्ट्रीमिंग HTTP चुनते हैं तो यह थोड़ा अलग होगा:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **उपयोगकर्ता सेटिंग्स** - सर्वर कॉन्फ़िगरेशन आपके वैश्विक *settings.json* फ़ाइल में जोड़ा जाता है और सभी वर्कस्पेस में उपलब्ध होता है। कॉन्फ़िगरेशन निम्नलिखित के समान दिखता है:

    ![उपयोगकर्ता सेटिंग](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. आपको एक हेडर भी जोड़ने की आवश्यकता है ताकि यह Azure API Management के प्रति सही तरीके से प्रमाणित हो सके। यह **Ocp-Apim-Subscription-Key** नामक हेडर का उपयोग करता है।

    - यहाँ बताया गया है कि आप इसे सेटिंग्स में कैसे जोड़ सकते हैं:

    ![प्रमाणीकरण के लिए हेडर जोड़ना](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), यह एक प्रॉम्प्ट प्रदर्शित करेगा जो आपसे API कुंजी मान पूछेगा जिसे आप Azure पोर्टल में अपनी Azure API Management इंस्टेंस के लिए पा सकते हैं।

   - इसे *mcp.json* में जोड़ने के लिए, आप इसे इस तरह जोड़ सकते हैं:

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

अब हम या तो सेटिंग्स में या *.vscode/mcp.json* में पूरी तरह से सेटअप हो गए हैं। आइए इसे आज़माएँ।

वहाँ एक टूल्स आइकन होना चाहिए, जहाँ आपके सर्वर से एक्सपोज़ किए गए टूल्स सूचीबद्ध होंगे:

![सर्वर से टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. टूल्स आइकन पर क्लिक करें और आपको टूल्स की एक सूची दिखाई देनी चाहिए:

    ![टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. टूल को इनवोक करने के लिए चैट में एक प्रॉम्प्ट दर्ज करें। उदाहरण के लिए, यदि आपने किसी ऑर्डर के बारे में जानकारी प्राप्त करने के लिए एक टूल चुना है, तो आप एजेंट से ऑर्डर के बारे में पूछ सकते हैं। यहाँ एक उदाहरण प्रॉम्प्ट है:

    ```text
    get information from order 2
    ```

    अब आपको एक टूल्स आइकन दिखाई देगा जो आपको टूल को कॉल करने के लिए आगे बढ़ने के लिए कहेगा। टूल को चलाने के लिए जारी रखें चुनें, अब आपको इस तरह का आउटपुट दिखाई देना चाहिए:

    ![प्रॉम्प्ट का परिणाम](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ऊपर जो आप देखते हैं वह इस पर निर्भर करता है कि आपने कौन से टूल्स सेटअप किए हैं, लेकिन विचार यह है कि आपको ऊपर जैसा टेक्स्टुअल रिस्पॉन्स मिले।**

## संदर्भ

यहाँ आप और अधिक सीख सकते हैं:

- [Azure API Management और MCP पर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python उदाहरण: Azure API Management का उपयोग करके रिमोट MCP सर्वर्स को सुरक्षित करें (प्रायोगिक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लाइंट ऑथराइजेशन लैब](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management एक्सटेंशन का उपयोग करके APIs को आयात और प्रबंधित करें](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center में रिमोट MCP सर्वर्स को रजिस्टर और डिस्कवर करें](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI गेटवे](https://github.com/Azure-Samples/AI-Gateway) - एक शानदार रिपॉजिटरी जो Azure API Management के साथ कई AI क्षमताएँ दिखाती है।
- [AI गेटवे वर्कशॉप्स](https://azure-samples.github.io/AI-Gateway/) - Azure पोर्टल का उपयोग करके वर्कशॉप्स शामिल हैं, जो AI क्षमताओं का मूल्यांकन शुरू करने का एक शानदार तरीका है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
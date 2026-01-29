# केस स्टडी: API Management मध्ये REST API MCP सर्व्हर म्हणून उघडणे

Azure API Management ही एक सेवा आहे जी तुमच्या API Endpoints वर गेटवे प्रदान करते. याचे कार्य असे आहे की Azure API Management तुमच्या API च्या समोर एक प्रॉक्सी म्हणून काम करते आणि येणाऱ्या विनंत्यांवर काय करायचे ते ठरवते.

याचा वापर करून, तुम्ही खालीलप्रमाणे अनेक वैशिष्ट्ये जोडू शकता:

- **सुरक्षा**, तुम्ही API कीज, JWT पासून मॅनेज्ड आयडेंटिटीपर्यंत सर्वकाही वापरू शकता.
- **रेट लिमिटिंग**, एक उत्तम वैशिष्ट्य म्हणजे ठराविक वेळेत किती कॉल्स होऊ शकतात हे ठरवणे. यामुळे सर्व वापरकर्त्यांना चांगला अनुभव मिळतो आणि तुमची सेवा विनंत्यांनी भारावून जात नाही.
- **स्केलिंग आणि लोड बॅलन्सिंग**, तुम्ही लोड बॅलन्स करण्यासाठी अनेक एंडपॉइंट्स सेट करू शकता आणि "लोड बॅलन्स" कसे करायचे ते ठरवू शकता.
- **AI वैशिष्ट्ये जसे की सेमॅंटिक कॅशिंग**, टोकन लिमिट आणि टोकन मॉनिटरिंग इत्यादी. ही वैशिष्ट्ये प्रतिसादक्षमता सुधारतात तसेच तुमच्या टोकन खर्चावर नियंत्रण ठेवण्यास मदत करतात. [येथे अधिक वाचा](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## MCP + Azure API Management का?

Model Context Protocol (MCP) हे एजंटिक AI अॅप्ससाठी आणि साधने व डेटा सुसंगत पद्धतीने उघडण्यासाठी लवकरच एक मानक बनत आहे. जेव्हा तुम्हाला API "मॅनेज" करायचे असते तेव्हा Azure API Management हा नैसर्गिक पर्याय आहे. MCP सर्व्हर्स अनेकदा इतर API शी एकत्रित होऊन, उदाहरणार्थ, टूल्ससाठी विनंत्या सोडवतात. त्यामुळे Azure API Management आणि MCP यांचे संयोजन खूप उपयुक्त ठरते.

## आढावा

या विशिष्ट उपयोग प्रकरणात आपण API एंडपॉइंट्स MCP सर्व्हर म्हणून उघडण्याचे शिकू. असे केल्याने, आपण सहजपणे हे एंडपॉइंट्स एजंटिक अॅपचा भाग बनवू शकतो आणि Azure API Management मधील वैशिष्ट्यांचा लाभ घेऊ शकतो.

## मुख्य वैशिष्ट्ये

- तुम्ही कोणते एंडपॉइंट मेथड्स टूल्स म्हणून उघडायचे आहेत ते निवडता.
- तुम्हाला मिळणारी अतिरिक्त वैशिष्ट्ये तुमच्या API साठी पॉलिसी विभागात तुम्ही काय कॉन्फिगर करता यावर अवलंबून असतात. परंतु येथे आम्ही तुम्हाला रेट लिमिटिंग कसे जोडायचे ते दाखवू.

## पूर्वतयारी: API आयात करा

जर तुमच्याकडे Azure API Management मध्ये आधीच API असेल तर उत्तम, तुम्ही हा टप्पा वगळू शकता. अन्यथा, [Azure API Management मध्ये API आयात करणे](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api) या लिंकला भेट द्या.

## API MCP सर्व्हर म्हणून उघडणे

API एंडपॉइंट्स उघडण्यासाठी, खालील चरणांचे अनुसरण करा:

1. Azure पोर्टलवर जा आणि खालील पत्त्यावर जा: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
तुमच्या API Management इंस्टन्सवर जा.

1. डाव्या मेनूमध्ये, **APIs > MCP Servers > + Create new MCP Server** निवडा.

1. API मध्ये, MCP सर्व्हर म्हणून उघडण्यासाठी REST API निवडा.

1. टूल्स म्हणून उघडण्यासाठी एक किंवा अधिक API ऑपरेशन्स निवडा. तुम्ही सर्व ऑपरेशन्स किंवा फक्त विशिष्ट ऑपरेशन्स निवडू शकता.

    ![उघडण्यासाठी मेथड्स निवडा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** निवडा.

1. **APIs** आणि **MCP Servers** मेनू पर्यायावर जा, तुम्हाला खालीलप्रमाणे दिसेल:

    ![मुख्य पॅनमध्ये MCP सर्व्हर पहा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्व्हर तयार केला गेला आहे आणि API ऑपरेशन्स टूल्स म्हणून उघडले गेले आहेत. MCP Servers पॅनमध्ये MCP सर्व्हर सूचीबद्ध आहे. URL कॉलममध्ये MCP सर्व्हरचा एंडपॉइंट दर्शविला जातो, जो तुम्ही चाचणीसाठी किंवा क्लायंट अॅप्लिकेशनमध्ये वापरू शकता.

## पर्यायी: पॉलिसी कॉन्फिगर करा

Azure API Management मध्ये पॉलिसी हा मुख्य संकल्पना आहे जिथे तुम्ही तुमच्या एंडपॉइंट्ससाठी विविध नियम सेट करू शकता, जसे की रेट लिमिटिंग किंवा सेमॅंटिक कॅशिंग. या पॉलिसी XML मध्ये लिहिल्या जातात.

MCP सर्व्हरवर रेट लिमिट पॉलिसी कशी सेट करायची ते येथे आहे:

1. पोर्टलमध्ये, **APIs > MCP Servers** निवडा.

1. तुम्ही तयार केलेला MCP सर्व्हर निवडा.

1. डाव्या मेनूमध्ये, **Policies** निवडा.

1. पॉलिसी संपादकात, MCP सर्व्हरच्या टूल्ससाठी लागू करायच्या पॉलिसी जोडा किंवा संपादित करा. पॉलिसी XML स्वरूपात परिभाषित केल्या जातात. उदाहरणार्थ, MCP सर्व्हरच्या टूल्ससाठी कॉल्स मर्यादित करण्यासाठी पॉलिसी जोडा (या उदाहरणात, प्रति क्लायंट IP पत्ता 30 सेकंदात 5 कॉल्स). खालील XML रेट लिमिटिंग करेल:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    पॉलिसी संपादकाचे चित्र:

    ![पॉलिसी संपादक](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## प्रयत्न करा

आपला MCP सर्व्हर अपेक्षेप्रमाणे कार्यरत आहे का ते तपासूया.

यासाठी, आपण Visual Studio Code आणि GitHub Copilot चा Agent मोड वापरू. आपण MCP सर्व्हर *mcp.json* फाईलमध्ये जोडू. असे केल्याने, Visual Studio Code क्लायंट म्हणून कार्य करेल आणि अंतिम वापरकर्ते प्रॉम्प्ट टाइप करून त्या सर्व्हरशी संवाद साधू शकतील.

Visual Studio Code मध्ये MCP सर्व्हर जोडण्यासाठी:

1. **Command Palette** मधून MCP: **Add Server** कमांड वापरा.

1. विचारले असता, सर्व्हर प्रकार निवडा: **HTTP (HTTP किंवा Server Sent Events)**.

1. API Management मधील MCP सर्व्हरचा URL प्रविष्ट करा. उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE एंडपॉइंटसाठी) किंवा **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP एंडपॉइंटसाठी), `/sse` किंवा `/mcp` यामधील फरक लक्षात घ्या.

1. तुमच्या पसंतीचा सर्व्हर ID प्रविष्ट करा. हा महत्त्वाचा मूल्य नाही, परंतु तुम्हाला त्या सर्व्हर इंस्टन्सची आठवण ठेवण्यास मदत होईल.

1. कॉन्फिगरेशन तुमच्या वर्कस्पेस सेटिंग्जमध्ये किंवा युजर सेटिंग्जमध्ये जतन करायचे आहे का ते निवडा.

  - **वर्कस्पेस सेटिंग्ज** - सर्व्हर कॉन्फिगरेशन फक्त सध्याच्या वर्कस्पेसमध्ये उपलब्ध असलेल्या .vscode/mcp.json फाईलमध्ये जतन केले जाते.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    किंवा तुम्ही स्ट्रीमिंग HTTP ट्रान्सपोर्ट निवडल्यास ते थोडे वेगळे असेल:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **युजर सेटिंग्ज** - सर्व्हर कॉन्फिगरेशन तुमच्या ग्लोबल *settings.json* फाईलमध्ये जोडले जाते आणि सर्व वर्कस्पेसमध्ये उपलब्ध असते. कॉन्फिगरेशन खालीलप्रमाणे दिसते:

    ![युजर सेटिंग](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management कडे योग्यरित्या प्रमाणीकरण करण्यासाठी हेडर जोडणे आवश्यक आहे. यासाठी **Ocp-Apim-Subscription-Key** नावाचा हेडर वापरला जातो.

    - सेटिंग्जमध्ये हेडर कसा जोडायचा ते येथे आहे:

    ![प्रमाणीकरणासाठी हेडर जोडणे](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), यामुळे API की मूल्य विचारणारा प्रॉम्प्ट दिसेल, जे तुम्हाला Azure पोर्टलमध्ये तुमच्या Azure API Management इंस्टन्ससाठी सापडेल.

   - *mcp.json* मध्ये जोडण्यासाठी, तुम्ही असे करू शकता:

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

### Agent मोड वापरा

आता आपण सेटिंग्ज किंवा *.vscode/mcp.json* मध्ये सर्व सेटअप पूर्ण केले आहे. प्रयत्न करूया.

तुम्हाला खालीलप्रमाणे टूल्स आयकॉन दिसेल, जिथे तुमच्या सर्व्हरमधून उघडलेली टूल्स सूचीबद्ध असतील:

![सर्व्हरमधील टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. टूल्स आयकॉनवर क्लिक करा आणि तुम्हाला खालीलप्रमाणे टूल्सची यादी दिसेल:

    ![टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. चॅटमध्ये प्रॉम्प्ट प्रविष्ट करा आणि टूल चालवण्यासाठी एजंटला विचार करा. उदाहरणार्थ, जर तुम्ही ऑर्डरबद्दल माहिती मिळवण्यासाठी टूल निवडले असेल, तर तुम्ही एजंटला ऑर्डरबद्दल विचारू शकता. उदाहरण प्रॉम्प्ट:

    ```text
    get information from order 2
    ```

    तुम्हाला आता टूल चालवण्यासाठी विचारणारा टूल्स आयकॉन दिसेल. टूल चालवणे सुरू ठेवण्यासाठी निवडा, तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

    ![प्रॉम्प्टचा परिणाम](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **वरील काय दिसते ते तुम्ही सेटअप केलेल्या टूल्सवर अवलंबून आहे, परंतु कल्पना अशी आहे की तुम्हाला वरीलप्रमाणे टेक्स्ट स्वरूपात प्रतिसाद मिळतो.**

## संदर्भ

येथे तुम्ही अधिक जाणून घेऊ शकता:

- [Azure API Management आणि MCP वर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमुना: Azure API Management वापरून रिमोट MCP सर्व्हर्स सुरक्षित करा (प्रायोगिक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लायंट अधिकृतता लॅब](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management विस्तार वापरून VS Code मध्ये API आयात करा आणि व्यवस्थापित करा](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center मध्ये रिमोट MCP सर्व्हर्स नोंदणी करा आणि शोधा](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) - Azure API Management सह अनेक AI क्षमता दर्शविणारा उत्कृष्ट रिपॉजिटरी
- [AI Gateway कार्यशाळा](https://azure-samples.github.io/AI-Gateway/) - Azure पोर्टल वापरून कार्यशाळा, AI क्षमता मूल्यांकन सुरू करण्याचा उत्तम मार्ग.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
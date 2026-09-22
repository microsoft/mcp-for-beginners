# केस स्टडी: API Management मध्ये REST API ला MCP सर्व्हर म्हणून एक्सपोज करा

Azure API Management ही एक सेवा आहे जी तुमच्या API Endpoints वर गेटवे प्रदान करते. ते कसे कार्य करते म्हणजे Azure API Management तुमच्या APIs च्या समोर एक प्रॉक्सी सारखे काम करते आणि येणाऱ्या विनंत्यांसोबत काय करायचे ते ठरवू शकते.

त्याचा वापर करून, तुम्ही अशा अनेक वैशिष्ट्यांचा फायदा घेता:

- **सुरक्षा**, तुम्ही API कीज, JWT ते मॅनेज्ड ओळखीसह सर्वकाही वापरू शकता.
- **रेट लिमिटिंग**, एक उत्तम वैशिष्ट्य म्हणजे ठराविक काळात किती कॉल्स होऊ शकतात हे ठरविण्याची क्षमता. हे सर्व वापरकर्त्यांना उच्च दर्जाचा अनुभव देण्यास मदत करते तसेच तुमच्या सेवेवर विनंत्यांचा ओघ आलेला नाही याची खात्री करते.
- **स्केलिंग व लोड बॅलन्सिंग**. तुम्ही लोड संतुलित करण्यासाठी अनेक endpoints सेट करू शकता व "लोड बॅलन्स कसे करायचे" हे देखील ठरवू शकता.
- **सेमँटिक कॅशिंग सारखी AI वैशिष्ट्ये**, टोकन लिमिट आणि टोकन मोनिटरिंग आणि बरेच काही. ही वैशिष्ट्ये प्रतिसादक्षमता सुधारतात तसेच तुम्हाला टोकन खर्चावर नियंत्रण ठेवण्यास मदत करतात. [येथे अधिक वाचा](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## का MCP + Azure API Management?

Model Context Protocol एजंटिक AI अ‍ॅपसाठी आणि साधने व डेटा सुसंगत पद्धतीने एक्सपोज करण्यासाठी लवकरच एक मानक म्हणून उभरतो आहे. जेव्हा तुम्हाला APIs "मॅनेज" करायच्या असतात, तेव्हा Azure API Management ही नैसर्गिक निवड आहे. MCP Servers अनेकदा अन्य APIs सह एकत्र जोडले जातात जेणेकरून एखाद्या टूलसाठी विनंत्या सोडवता येतील. म्हणून Azure API Management आणि MCP एकत्र करणे खूपच अर्थपूर्ण आहे.

## आढावा

या विशिष्ट केसमध्ये आपण API endpoints ला MCP Server म्हणून कसे एक्सपोज करायचे हे शिकू. यामुळे आपण सहजपणे हे endpoints एजंटिक अ‍ॅपचा भाग बनवू शकतो तसेच Azure API Management चे वैशिष्ट्ये वापरू शकतो.

## मुख्य वैशिष्ट्ये

- तुम्ही ज्या endpoint पद्धती साधने म्हणून एक्सपोज करू इच्छिता ती निवडा.
- तुम्हाला मिळणारी अतिरिक्त वैशिष्ट्ये तुमच्या API साठी पॉलिसी विभागात काय कॉन्फिगर केले आहे त्यावर अवलंबून असतात. पण येथे तुम्हाला रेट लिमिटिंग कशी वापरावी ते दाखवू.

## पूर्व-पायरी: API इम्पोर्ट करा

तुमच्या कडे Azure API Management मध्ये API आधीपासून असल्यास उत्तम, तर हा पायरी वगळा. नसल्यास, हा दुवा पहा, [Azure API Management मध्ये API इम्पोर्ट करणे](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API MCP Server म्हणून एक्सपोज करा

API endpoints एक्सपोज करण्यासाठी, या चरणांचे अनुसरण करूया:

1. Azure Portal वर जा आणि पुढील पत्ता वापरा <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
तुमच्या API Management इंस्टन्सवर चला.

1. डाव्या मेनूमध्ये, APIs > MCP Servers > + Create new MCP Server निवडा.

1. API मध्ये, REST API निवडा ज्या MCP सर्व्हर म्हणून एक्सपोज करायचे आहे.

1. एक किंवा अधिक API ऑपरेशन्स निवडा ज्या साधने म्हणून एक्सपोज करायच्या आहेत. तुम्ही सर्व ऑपरेशन्स किंवा काही विशिष्ट ऑपरेशन्स निवडू शकता.

    ![एक्सपोज करण्यासाठी पद्धती निवडा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** निवडा.

1. मेनू मध्ये **APIs** आणि **MCP Servers** वर जा, तुम्हाला पुढील दिसावे:

    ![मुख्य पॅनमध्ये MCP Server पहा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्व्हर तयार झाला आहे आणि API ऑपरेशन्स साधने म्हणून एक्सपोज झाले आहेत. MCP सर्व्हर MCP Servers पॅनमध्ये दाखवला जातो. URL कॉलममध्ये MCP सर्व्हरचा endpoint असतो ज्याला तुम्ही टेस्टिंगसाठी किंवा क्लायंट अ‍ॅप्लिकेशनमध्ये कॉल करू शकता.

## ऐच्छिक: पॉलिसी कॉन्फिगर करा

Azure API Management मध्ये पॉलिसींची मुख्य संकल्पना आहे जिथे तुम्ही तुमच्या endpoints साठी विविध नियम सेट करता जसे की रेट लिमिटिंग किंवा सेमँटिक कॅशिंग. या पॉलिसीज XML मध्ये लिहिल्या जातात.

तुमच्या MCP सर्व्हरला रेट लिमिट करण्यासाठी पॉलिसी कशी सेट कराल ते खालीलप्रमाणे:

1. पोर्टलमध्ये, APIs अंतर्गत, **MCP Servers** निवडा.

1. तुम्ही तयार केलेला MCP सर्व्हर निवडा.

1. डाव्या मेनू मध्ये, MCP अंतर्गत, **Policies** निवडा.

1. पॉलिसी संपादकात, MCP सर्व्हरच्या साधनांवर लागू करायच्या पॉलिसीज जोडा किंवा संपादित करा. पॉलिसीज XML फॉर्मॅटमध्ये परिभाषित केल्या जातात. उदाहरणार्थ, तुम्ही MCP सर्व्हरच्या साधनांसाठी कॉल मर्यादा (उदाहरणार्थ, प्रत्येक client IP पत्ता प्रति 30 सेकंद 5 कॉल) साठी पॉलिसी जोडू शकता. रेट लिमिटिंगसाठी खालील XML आहे:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    पॉलिसी संपादकाचा एक प्रतिमाही:

    ![पॉलिसी संपादक](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## प्रयत्न करुया

चला सुनिश्चित करूया की आपला MCP सर्व्हर नियोजितप्रमाणे काम करतोय.

> [!NOTE]
> Azure API Management सध्या हा सर्व्हर Streamable HTTP `/mcp` endpoint द्वारे एक्सपोज करतो. जुन्या HTTP+SSE `/sse` ट्रान्सपोर्टला बंद करण्यात आले आहे आणि ते फक्त लिगसी क्लायंटसाठी वापरावे.

 

यासाठी, आपण Visual Studio Code आणि GitHub Copilot चे Agent मोड वापरणार आहोत. आपण MCP सर्व्हर *mcp.json* मध्ये जोडणार आहोत. यामुळे Visual Studio Code एजंटिक क्षमता असलेला क्लायंट म्हणून कार्य करेल आणि अंतिम वापरकर्ते एक प्रॉम्प्ट टाइप करून त्या सर्व्हरशी संवाद साधू शकतील.

पाहूया Visual Studio Code मध्ये MCP सर्व्हर कसा जोडायचा:

1. Command Palette मधून MCP: **Add Server कमांड** वापरा.

1. विचारले गेल्यास, सर्व्हर प्रकार निवडा: **HTTP (HTTP किंवा Server Sent Events)**.

1. API Management मधील MCP सर्व्हरसाठी दिलेला Streamable HTTP URL प्रविष्ट करा.
    उदाहरणार्थ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. तुमच्या आवडीनुसार एक सर्व्हर ID टाका. ही महत्त्वाची किंमत नाही पण तुम्हाला सर्व्हरची झपाटलेली आठवण ठेवण्यात मदत होईल.

1. कॉन्फिगरेशन तुम्ही workspace सेटिंग्जमध्ये साठवायचा आहे की user सेटिंग्जमध्ये हे निवडा.

  - **Workspace सेटिंग्ज** - सर्व्हर कॉन्फिगरेशन सध्या असलेल्या workspace मधील .vscode/mcp.json फाइलमध्ये साठवली जाते.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User सेटिंग्ज** - सर्व्हर कॉन्फिगरेशन तुमच्या वैश्विक *settings.json* फाइलमध्ये जोडले जाते आणि सर्व workspace साठी उपलब्ध असते. कॉन्फिगरेशन खालील प्रमाणे दिसते:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. तुम्हाला अजून एक कॉन्फिगरेशन जोडावी लागेल, हेडर जेणेकरून Azure API Management कडे योग्यरीत्या प्रमाणीकरण होईल. ते **Ocp-Apim-Subscription-Key** नावाचा हेडर वापरते.

    - सेटिंग्जमध्ये तो कसा जोडता येईल:

    ![प्रमाणीकरणासाठी हेडर जोडणे](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), यांच्या परिणामी प्रॉम्प्ट दिसेल ज्यात API कीची किंमत विचारली जाईल जी तुम्हाला Azure Portal मधील तुमच्या Azure API Management इंस्टन्ससाठी सापडेल.

   - *mcp.json* मध्ये जोडण्यासाठी, खालीलप्रमाणे करू शकता:

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

### एजंट मोड वापरा

आता आपण सेटिंग्जमध्ये किंवा *.vscode/mcp.json* मध्ये सर्व सेटअप पूर्ण केले आहे. चला प्रयत्न करुया.

तिथे एक Tools चिन्ह असावे, जिथे तुमच्या सर्व्हरमधील एक्सपोज केलेल्या साधनांची यादी दिसेल:

![सर्व्हरमधून साधने](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools चिन्हावर क्लिक करा आणि तुम्हाला साधनेची यादी पुढीलप्रमाणे दिसेल:

    ![साधने](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. चॅटमध्ये प्रॉम्प्ट टाका जेणेकरून साधन कॉल करता येईल. उदाहरणार्थ, जर तुम्ही ऑर्डरविषयी माहिती घेण्यासाठी साधन निवडले असेल, तर तुम्ही एजंटला ऑर्डरविषयी विचारू शकता. प्रॉम्प्टचे उदाहरण:

    ```text
    get information from order 2
    ```

    आता तुम्हाला एक साधनेचा चिन्ह दिसेल ज्यावरून साधन कॉल करण्याचा पर्याय येईल. साधन चालू ठेवण्यासाठी निवडा, तुम्हाला खालीलप्रमाणे आऊटपुट दिसेल:

    ![प्रॉम्प्टमधून निकाल](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **वरील जे तुम्ही पाहता ते तुमच्या सेट केल्या साधनांवर अवलंबून असते, पण कल्पना अशी की तुम्हाला वरील प्रमाणे मजकूरात्मक प्रतिसाद मिळतो**


## संदर्भ

अधिक जाणून घेण्यासाठी:

- [Azure API Management आणि MCP वर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमुना: Azure API Management वापरून रिमोट MCP सर्व्हर सुरक्षित करा (प्रयोगात्मक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लायंट ऑथराइजेशन प्रयोगशाळा](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code साठी Azure API Management विस्ताराचा वापर करुन APIs इम्पोर्ट व मॅनेज करा](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center मध्ये रिमोट MCP सर्व्हर नोंदणी व शोधा](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management सह अनेक AI क्षमता दाखवणारे उत्कृष्ट रेपो
- [AI Gateway वर्कशॉप्स](https://azure-samples.github.io/AI-Gateway/) Azure Portal वापरून वर्कशॉप्स ज्यामुळे AI क्षमता तपासायला सुरुवात करण्याचा एक उत्तम मार्ग आहे.

## पुढचे काय

- परत जा: [केस स्टडीज आढावा](./README.md)
- पुढे: [Azure AI ट्रॅव्हल एजंट्स](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
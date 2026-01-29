# केस स्टडी: API Management मा REST API लाई MCP सर्भरको रूपमा एक्सपोज गर्नुहोस्

Azure API Management एउटा सेवा हो जसले तपाईंको API Endpoints माथि Gateway प्रदान गर्दछ। यसको काम गर्ने तरिका यस्तो छ कि Azure API Management तपाईंको API हरूको अगाडि proxy को रूपमा काम गर्छ र आउने अनुरोधहरूसँग के गर्ने भनेर निर्णय गर्न सक्छ।

यसलाई प्रयोग गर्दा तपाईंले धेरै सुविधाहरू थप्न सक्नुहुन्छ, जस्तै:

- **सुरक्षा (Security)**, तपाईं API keys, JWT देखि managed identity सम्म सबै प्रयोग गर्न सक्नुहुन्छ।
- **रेट लिमिटिंग (Rate limiting)**, यो सुविधा धेरै उपयोगी छ जसले निश्चित समय अवधिमा कति कलहरू अनुमति दिने भनेर निर्णय गर्न मद्दत गर्छ। यसले सबै प्रयोगकर्ताहरूलाई राम्रो अनुभव दिन्छ र तपाईंको सेवा धेरै अनुरोधहरूले ओभरलोड हुनबाट जोगाउँछ।
- **स्केलिंग र लोड ब्यालेन्सिङ (Scaling & Load balancing)**। तपाईंले लोड ब्यालेन्स गर्नका लागि धेरै endpoints सेटअप गर्न सक्नुहुन्छ र कसरी "लोड ब्यालेन्स" गर्ने भनेर निर्णय गर्न सक्नुहुन्छ।
- **AI सुविधाहरू जस्तै सेम्यान्टिक क्यासिङ (semantic caching)**, टोकन लिमिट र टोकन मोनिटरिङ। यी सुविधाहरूले प्रतिक्रिया समय सुधार गर्छ र तपाईंलाई टोकन खर्चको ट्र्याक राख्न मद्दत गर्छ। [यहाँ थप पढ्नुहोस्](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## किन MCP + Azure API Management?

Model Context Protocol (MCP) एजेन्टिक AI एप्सका लागि उपकरण र डेटा एकसमान तरिकाले एक्सपोज गर्नको लागि छिटो मानक बन्दैछ। Azure API Management "API हरूलाई व्यवस्थापन" गर्न आवश्यक पर्दा स्वाभाविक विकल्प हो। MCP सर्भरहरूले प्रायः अन्य API हरूसँग एकीकृत भएर उपकरणहरूको अनुरोध समाधान गर्छन्। त्यसैले Azure API Management र MCP लाई संयोजन गर्नु धेरै उपयोगी हुन्छ।

## अवलोकन

यस विशेष प्रयोग केसमा हामी API endpoints लाई MCP सर्भरको रूपमा कसरी एक्सपोज गर्ने भन्ने सिक्नेछौं। यसो गर्दा, हामी यी endpoints लाई सजिलै एजेन्टिक एपको भाग बनाउन सक्छौं र Azure API Management का सुविधाहरूको फाइदा लिन सक्छौं।

## मुख्य सुविधाहरू

- तपाईंले कुन endpoint मेथडहरूलाई उपकरणको रूपमा एक्सपोज गर्ने निर्णय गर्न सक्नुहुन्छ।
- तपाईंले पाउने थप सुविधाहरू तपाईंले आफ्नो API को नीति (policy) सेक्सनमा के कन्फिगर गर्नुभएको छ भन्नेमा निर्भर गर्दछ। तर यहाँ हामी तपाईंलाई रेट लिमिटिंग कसरी थप्ने देखाउनेछौं।

## प्रारम्भिक चरण: API आयात गर्नुहोस्

यदि तपाईंको Azure API Management मा पहिले नै API छ भने, यो चरण छोड्न सक्नुहुन्छ। यदि छैन भने, यो लिंक हेर्नुहोस्: [Azure API Management मा API आयात गर्ने](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API लाई MCP सर्भरको रूपमा एक्सपोज गर्नुहोस्

API endpoints लाई एक्सपोज गर्न, यी चरणहरू पालना गर्नुहोस्:

1. Azure Portal मा जानुहोस् र यो ठेगाना खोल्नुहोस्: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>। आफ्नो API Management instance मा जानुहोस्।

1. बाँया मेनुमा, **APIs > MCP Servers > + Create new MCP Server** चयन गर्नुहोस्।

1. API मा, MCP सर्भरको रूपमा एक्सपोज गर्न REST API चयन गर्नुहोस्।

1. उपकरणको रूपमा एक्सपोज गर्न एक वा धेरै API अपरेसनहरू चयन गर्नुहोस्। तपाईं सबै अपरेसनहरू वा केवल विशिष्ट अपरेसनहरू चयन गर्न सक्नुहुन्छ।

    ![मेथडहरू चयन गर्नुहोस्](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** चयन गर्नुहोस्।

1. मेनु विकल्प **APIs** र **MCP Servers** मा जानुहोस्, तपाईंले निम्न देख्नुहुनेछ:

    ![मुख्य प्यानलमा MCP सर्भर हेर्नुहोस्](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्भर सिर्जना गरिएको छ र API अपरेसनहरू उपकरणको रूपमा एक्सपोज गरिएको छ। MCP सर्भर MCP Servers प्यानलमा सूचीबद्ध छ। URL स्तम्भले MCP सर्भरको endpoint देखाउँछ जसलाई तपाईं परीक्षण गर्न वा क्लाइन्ट एप्लिकेसन भित्र प्रयोग गर्न कल गर्न सक्नुहुन्छ।

## वैकल्पिक: नीतिहरू कन्फिगर गर्नुहोस्

Azure API Management मा नीतिहरू (policies) को मुख्य अवधारणा छ, जहाँ तपाईं आफ्नो endpoints का लागि विभिन्न नियमहरू सेटअप गर्न सक्नुहुन्छ, जस्तै रेट लिमिटिंग वा सेम्यान्टिक क्यासिङ। यी नीतिहरू XML मा लेखिन्छन्।

MCP सर्भरको लागि रेट लिमिट सेटअप गर्न यसरी गर्नुहोस्:

1. पोर्टलमा, **APIs** अन्तर्गत **MCP Servers** चयन गर्नुहोस्।

1. तपाईंले सिर्जना गर्नुभएको MCP सर्भर चयन गर्नुहोस्।

1. बाँया मेनुमा, **Policies** चयन गर्नुहोस्।

1. नीति सम्पादकमा, तपाईंले MCP सर्भरका उपकरणहरूमा लागू गर्न चाहनुभएको नीतिहरू थप्नुहोस् वा सम्पादन गर्नुहोस्। नीतिहरू XML ढाँचामा परिभाषित गरिन्छ। उदाहरणका लागि, तपाईंले MCP सर्भरका उपकरणहरूमा कलहरू सीमित गर्न नीति थप्न सक्नुहुन्छ (यस उदाहरणमा, प्रति क्लाइन्ट IP ठेगानामा ३० सेकेन्डमा ५ कलहरू)। यहाँ XML छ जसले रेट लिमिट गर्नेछ:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    नीति सम्पादकको छवि:

    ![नीति सम्पादक](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## परीक्षण गर्नुहोस्

आउनुहोस्, हाम्रो MCP सर्भरले अपेक्षाअनुसार काम गरिरहेको छ कि छैन भनेर सुनिश्चित गरौं।

यसका लागि, हामी Visual Studio Code र GitHub Copilot को Agent मोड प्रयोग गर्नेछौं। हामी MCP सर्भरलाई *mcp.json* फाइलमा थप्नेछौं। यसो गर्दा, Visual Studio Code क्लाइन्टको रूपमा एजेन्टिक क्षमतासहित काम गर्नेछ र अन्त प्रयोगकर्ताहरूले प्रम्प्ट टाइप गरेर उक्त सर्भरसँग अन्तरक्रिया गर्न सक्नेछन्।

Visual Studio Code मा MCP सर्भर थप्न यसरी गर्नुहोस्:

1. **Command Palette** बाट MCP: **Add Server command** प्रयोग गर्नुहोस्।

1. सोधिएको बेला, सर्भर प्रकार चयन गर्नुहोस्: **HTTP (HTTP or Server Sent Events)**।

1. API Management मा MCP सर्भरको URL प्रविष्ट गर्नुहोस्। उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint का लागि) वा **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint का लागि), ध्यान दिनुहोस् कि ट्रान्सपोर्टको भिन्नता `/sse` वा `/mcp` मा छ।

1. आफ्नो रोजाइको सर्भर ID प्रविष्ट गर्नुहोस्। यो महत्त्वपूर्ण मान छैन तर यसले तपाईंलाई यो सर्भर instance के हो भनेर सम्झन मद्दत गर्नेछ।

1. कन्फिगरेसनलाई आफ्नो workspace settings वा user settings मा सुरक्षित गर्ने निर्णय गर्नुहोस्।

  - **Workspace settings** - सर्भर कन्फिगरेसन *mcp.json* फाइलमा सुरक्षित हुन्छ, जुन केवल हालको workspace मा उपलब्ध हुन्छ।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    वा यदि तपाईंले ट्रान्सपोर्टको रूपमा streaming HTTP चयन गर्नुभयो भने यो अलि फरक हुनेछ:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - सर्भर कन्फिगरेसन तपाईंको global *settings.json* फाइलमा थपिन्छ र सबै workspace हरूमा उपलब्ध हुन्छ। कन्फिगरेसन यस प्रकार देखिन्छ:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. तपाईंले Azure API Management तर्फ सही रूपमा प्रमाणिकरण गर्न सुनिश्चित गर्न हेडर थप्न आवश्यक छ। यसले **Ocp-Apim-Subscription-Key** नामक हेडर प्रयोग गर्छ।

    - यसलाई सेटिङ्समा यसरी थप्न सकिन्छ:

    ![प्रमाणिकरणका लागि हेडर थप्दै](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), यसले API key मान सोध्ने प्रम्प्ट देखाउनेछ, जुन तपाईं Azure Portal मा आफ्नो Azure API Management instance का लागि पाउन सक्नुहुन्छ।

   - यसलाई *mcp.json* मा थप्न यसरी गर्न सकिन्छ:

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

### एजेन्ट मोड प्रयोग गर्नुहोस्

अब हामी सेटिङ्स वा *.vscode/mcp.json* मा सेटअप गरिसकेका छौं। आउनुहोस्, यसलाई परीक्षण गरौं।

त्यहाँ एउटा उपकरण आइकन देखिनु पर्छ, जहाँ तपाईंको सर्भरबाट एक्सपोज गरिएका उपकरणहरू सूचीबद्ध हुन्छन्:

![सर्भरबाट उपकरणहरू](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. उपकरण आइकनमा क्लिक गर्नुहोस्, र तपाईंले उपकरणहरूको सूची देख्नुहुनेछ:

    ![उपकरणहरू](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. उपकरणलाई चलाउन प्रम्प्टमा इनपुट दिनुहोस्। उदाहरणका लागि, यदि तपाईंले अर्डरको जानकारी प्राप्त गर्ने उपकरण चयन गर्नुभएको छ भने, तपाईं एजेन्टलाई अर्डरको बारेमा सोध्न सक्नुहुन्छ। यहाँ एउटा उदाहरण प्रम्प्ट छ:

    ```text
    get information from order 2
    ```

    तपाईंलाई उपकरण चलाउन अगाडि बढ्न सोध्ने उपकरण आइकन देखाइनेछ। उपकरण चलाउन जारी राख्नुहोस्, तपाईंले यस प्रकारको आउटपुट देख्नुहुनेछ:

    ![प्रम्प्टको नतिजा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **तपाईंले माथि देख्नुभएको कुरा तपाईंले सेटअप गर्नुभएको उपकरणहरूमा निर्भर गर्दछ, तर विचार यो हो कि तपाईंले माथिको जस्तै पाठ्य प्रतिक्रिया प्राप्त गर्नुहुन्छ।**

## सन्दर्भहरू

यहाँ थप जान्न सक्नुहुन्छ:

- [Azure API Management र MCP को ट्युटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमूना: Azure API Management प्रयोग गरेर सुरक्षित रिमोट MCP सर्भरहरू (प्रायोगिक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लाइन्ट प्रमाणिकरण प्रयोगशाला](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management एक्सटेन्सन प्रयोग गरेर VS Code मा API आयात र व्यवस्थापन गर्नुहोस्](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center मा रिमोट MCP सर्भरहरू दर्ता र पत्ता लगाउनुहोस्](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management सँग धेरै AI क्षमताहरू देखाउने उत्कृष्ट रिपोजिटरी
- [AI Gateway कार्यशालाहरू](https://azure-samples.github.io/AI-Gateway/) Azure Portal प्रयोग गरेर कार्यशालाहरू समावेश गर्दछ, जुन AI क्षमताहरू मूल्याङ्कन गर्न सुरु गर्नको लागि उत्कृष्ट तरिका हो।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
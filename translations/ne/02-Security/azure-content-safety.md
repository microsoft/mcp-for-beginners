# Azure Content Safety सँग उन्नत MCP सुरक्षा

Azure Content Safety ले तपाईंको MCP कार्यान्वयनहरूको सुरक्षा बढाउनका लागि धेरै शक्तिशाली उपकरणहरू प्रदान गर्दछ:

## Prompt Shields

Microsoft को AI Prompt Shields ले सिधा र अप्रत्यक्ष prompt injection आक्रमणहरूबाट बलियो सुरक्षा प्रदान गर्दछ:

1. **उन्नत पहिचान**: सामग्रीमा लुकेको दुष्ट निर्देशनहरू पत्ता लगाउन मेशिन लर्निङ प्रयोग गर्छ।
2. **स्पटलाइटिङ**: इनपुट टेक्स्टलाई यस्तो तरिकाले रूपान्तरण गर्छ जसले AI प्रणालीहरूलाई वैध निर्देशन र बाह्य इनपुट बीच फरक गर्न मद्दत गर्छ।
3. **डेलिमिटर र डाटामार्किङ**: विश्वासयोग्य र अविश्वसनीय डाटाबीचको सीमा चिन्हित गर्छ।
4. **Content Safety एकीकरण**: Azure AI Content Safety सँग मिलेर जेलब्रेक प्रयास र हानिकारक सामग्री पत्ता लगाउँछ।
5. **लगातार अपडेटहरू**: Microsoft ले नयाँ खतरा विरुद्ध सुरक्षा प्रणालीहरू नियमित रूपमा अपडेट गर्छ।

## MCP सँग Azure Content Safety कार्यान्वयन

यस विधिले बहु-स्तरीय सुरक्षा प्रदान गर्दछ:
- प्रक्रिया अघि इनपुट स्क्यान गर्ने
- परिणाम फर्काउनु अघि मान्यकरण गर्ने
- परिचित हानिकारक ढाँचाहरूका लागि ब्लकलिस्ट प्रयोग गर्ने
- Azure का निरन्तर अपडेट हुने Content Safety मोडेलहरू उपयोग गर्ने

## Azure Content Safety स्रोतहरू

तपाईंको MCP सर्भरहरूसँग Azure Content Safety कार्यान्वयन गर्ने बारे थप जान्न यी आधिकारिक स्रोतहरू हेर्नुहोस्:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety को आधिकारिक दस्तावेज।
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - prompt injection आक्रमण रोक्ने तरिका सिक्नुहोस्।
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety कार्यान्वयनका लागि विस्तृत API सन्दर्भ।
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# प्रयोग गरी छिटो कार्यान्वयन मार्गदर्शन।
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - विभिन्न प्रोग्रामिङ भाषाहरूका लागि क्लाइन्ट लाइब्रेरीहरू।
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - जेलब्रेक प्रयास पत्ता लगाउने र रोक्ने विशेष निर्देशन।
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - प्रभावकारी रूपमा Content Safety कार्यान्वयनका लागि उत्तम अभ्यासहरू।

थप विस्तृत कार्यान्वयनका लागि, हाम्रो [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) हेर्नुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
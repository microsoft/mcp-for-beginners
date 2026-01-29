# Azure Content Safety के साथ उन्नत MCP सुरक्षा

Azure Content Safety कई शक्तिशाली उपकरण प्रदान करता है जो आपके MCP कार्यान्वयन की सुरक्षा को बढ़ा सकते हैं:

## Prompt Shields

Microsoft के AI Prompt Shields सीधे और अप्रत्यक्ष दोनों प्रकार के प्रॉम्प्ट इंजेक्शन हमलों के खिलाफ मजबूत सुरक्षा प्रदान करते हैं:

1. **उन्नत पहचान**: मशीन लर्निंग का उपयोग करके सामग्री में छिपे दुर्भावनापूर्ण निर्देशों की पहचान करता है।
2. **स्पॉटलाइटिंग**: इनपुट टेक्स्ट को इस तरह परिवर्तित करता है कि AI सिस्टम वैध निर्देशों और बाहरी इनपुट के बीच अंतर कर सके।
3. **डेलिमिटर्स और डाटामार्किंग**: विश्वसनीय और अविश्वसनीय डेटा के बीच सीमाएं चिह्नित करता है।
4. **Content Safety एकीकरण**: Azure AI Content Safety के साथ मिलकर जेलब्रेक प्रयासों और हानिकारक सामग्री का पता लगाता है।
5. **निरंतर अपडेट्स**: Microsoft नियमित रूप से उभरते खतरों के खिलाफ सुरक्षा तंत्रों को अपडेट करता रहता है।

## MCP के साथ Azure Content Safety को लागू करना

यह तरीका बहु-स्तरीय सुरक्षा प्रदान करता है:
- प्रोसेसिंग से पहले इनपुट की स्कैनिंग
- आउटपुट लौटाने से पहले मान्यता
- ज्ञात हानिकारक पैटर्न के लिए ब्लॉकलिस्ट का उपयोग
- Azure के निरंतर अपडेट होने वाले कंटेंट सेफ्टी मॉडल का लाभ उठाना

## Azure Content Safety संसाधन

अपने MCP सर्वरों के साथ Azure Content Safety को लागू करने के बारे में अधिक जानने के लिए, इन आधिकारिक संसाधनों को देखें:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety के लिए आधिकारिक दस्तावेज़।
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - प्रॉम्प्ट इंजेक्शन हमलों को रोकने के तरीके सीखें।
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety को लागू करने के लिए विस्तृत API संदर्भ।
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# का उपयोग करके त्वरित कार्यान्वयन गाइड।
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - विभिन्न प्रोग्रामिंग भाषाओं के लिए क्लाइंट लाइब्रेरी।
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - जेलब्रेक प्रयासों का पता लगाने और रोकने के लिए विशेष मार्गदर्शन।
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - कंटेंट सेफ्टी को प्रभावी ढंग से लागू करने के लिए सर्वोत्तम प्रथाएं।

अधिक गहन कार्यान्वयन के लिए, हमारा [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) देखें।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
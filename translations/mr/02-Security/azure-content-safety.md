# Azure Content Safety सह प्रगत MCP सुरक्षा

Azure Content Safety तुमच्या MCP अंमलबजावणीत सुरक्षा वाढवण्यासाठी अनेक सामर्थ्यशाली साधने प्रदान करते:

## Prompt Shields

Microsoft चे AI Prompt Shields थेट आणि अप्रत्यक्ष prompt injection हल्ल्यांपासून मजबूत संरक्षण देतात:

1. **प्रगत शोध**: सामग्रीमध्ये दडलेले हानिकारक निर्देश ओळखण्यासाठी मशीन लर्निंग वापरते.
2. **स्पॉटलाइटिंग**: इनपुट मजकूर रूपांतरित करून AI प्रणालींना वैध निर्देश आणि बाह्य इनपुट यामध्ये फरक ओळखण्यास मदत करते.
3. **डेलिमीटर्स आणि डेटामार्किंग**: विश्वासार्ह आणि अविश्वसनीय डेटामधील सीमा चिन्हांकित करते.
4. **Content Safety एकत्रीकरण**: Azure AI Content Safety सोबत काम करून jailbreak प्रयत्न आणि हानिकारक सामग्री शोधते.
5. **सतत अद्यतने**: Microsoft नियमितपणे उदयोन्मुख धोक्यांविरुद्ध संरक्षण यंत्रणा अद्ययावत करते.

## MCP सह Azure Content Safety ची अंमलबजावणी

हा दृष्टिकोन बहुस्तरीय संरक्षण प्रदान करतो:
- प्रक्रिया करण्यापूर्वी इनपुट स्कॅन करणे
- परत देण्यापूर्वी आउटपुटची पडताळणी करणे
- ज्ञात हानिकारक नमुन्यांसाठी ब्लॉकलिस्ट वापरणे
- Azure च्या सतत अद्ययावत होणाऱ्या content safety मॉडेल्सचा लाभ घेणे

## Azure Content Safety संसाधने

तुमच्या MCP सर्व्हरसोबत Azure Content Safety कशी अंमलात आणायची हे जाणून घेण्यासाठी, या अधिकृत संसाधनांचा सल्ला घ्या:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety साठी अधिकृत दस्तऐवज.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - prompt injection हल्ले कसे टाळायचे ते शिका.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety अंमलबजावणीसाठी सविस्तर API संदर्भ.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# वापरून जलद अंमलबजावणी मार्गदर्शक.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - विविध प्रोग्रामिंग भाषांसाठी क्लायंट लायब्ररी.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - jailbreak प्रयत्न ओळखण्याबाबत विशिष्ट मार्गदर्शन.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - content safety प्रभावीपणे अंमलात आणण्यासाठी सर्वोत्तम पद्धती.

अधिक सखोल अंमलबजावणीसाठी, आमचा [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) पहा.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
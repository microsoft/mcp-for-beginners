<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d3415b9d2bf58bc69be07f945a69e07",
  "translation_date": "2025-07-14T05:57:14+00:00",
  "source_file": "09-CaseStudy/travelagentsample.md",
  "language_code": "hi"
}
-->
# केस स्टडी: Azure AI ट्रैवल एजेंट्स – संदर्भ कार्यान्वयन

## अवलोकन

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) माइक्रोसॉफ्ट द्वारा विकसित एक व्यापक संदर्भ समाधान है जो दिखाता है कि Model Context Protocol (MCP), Azure OpenAI, और Azure AI Search का उपयोग करके एक मल्टी-एजेंट, AI-संचालित ट्रैवल प्लानिंग एप्लिकेशन कैसे बनाया जा सकता है। यह प्रोजेक्ट कई AI एजेंट्स के समन्वय, एंटरप्राइज डेटा के एकीकरण, और वास्तविक दुनिया के परिदृश्यों के लिए एक सुरक्षित, विस्तार योग्य प्लेटफ़ॉर्म प्रदान करने के सर्वोत्तम तरीकों को प्रदर्शित करता है।

## मुख्य विशेषताएं
- **मल्टी-एजेंट समन्वय:** MCP का उपयोग करके विशेषज्ञ एजेंट्स (जैसे फ्लाइट, होटल, और यात्रा कार्यक्रम एजेंट्स) का समन्वय करता है जो जटिल यात्रा योजना कार्यों को पूरा करने के लिए मिलकर काम करते हैं।
- **एंटरप्राइज डेटा एकीकरण:** Azure AI Search और अन्य एंटरप्राइज डेटा स्रोतों से जुड़कर यात्रा सिफारिशों के लिए नवीनतम, प्रासंगिक जानकारी प्रदान करता है।
- **सुरक्षित, स्केलेबल आर्किटेक्चर:** प्रमाणीकरण, प्राधिकरण, और स्केलेबल तैनाती के लिए Azure सेवाओं का उपयोग करता है, एंटरप्राइज सुरक्षा सर्वोत्तम प्रथाओं का पालन करता है।
- **विस्तार योग्य टूलिंग:** पुन: उपयोग योग्य MCP टूल्स और प्रॉम्प्ट टेम्प्लेट्स को लागू करता है, जिससे नए डोमेन या व्यावसायिक आवश्यकताओं के लिए तेजी से अनुकूलन संभव होता है।
- **उपयोगकर्ता अनुभव:** उपयोगकर्ताओं को यात्रा एजेंट्स के साथ बातचीत करने के लिए एक संवादात्मक इंटरफ़ेस प्रदान करता है, जो Azure OpenAI और MCP द्वारा संचालित है।

## आर्किटेक्चर
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### आर्किटेक्चर डायग्राम विवरण

Azure AI Travel Agents समाधान को मॉड्यूलरिटी, स्केलेबिलिटी, और कई AI एजेंट्स तथा एंटरप्राइज डेटा स्रोतों के सुरक्षित एकीकरण के लिए डिज़ाइन किया गया है। मुख्य घटक और डेटा प्रवाह इस प्रकार हैं:

- **यूजर इंटरफ़ेस:** उपयोगकर्ता एक संवादात्मक UI (जैसे वेब चैट या Teams बॉट) के माध्यम से सिस्टम के साथ बातचीत करते हैं, जो उपयोगकर्ता प्रश्न भेजता है और यात्रा सिफारिशें प्राप्त करता है।
- **MCP सर्वर:** केंद्रीय समन्वयक के रूप में कार्य करता है, उपयोगकर्ता इनपुट प्राप्त करता है, संदर्भ प्रबंधित करता है, और Model Context Protocol के माध्यम से विशेषज्ञ एजेंट्स (जैसे FlightAgent, HotelAgent, ItineraryAgent) के कार्यों का समन्वय करता है।
- **AI एजेंट्स:** प्रत्येक एजेंट एक विशिष्ट डोमेन (फ्लाइट्स, होटल, यात्रा कार्यक्रम) के लिए जिम्मेदार होता है और MCP टूल के रूप में कार्यान्वित होता है। एजेंट प्रॉम्प्ट टेम्प्लेट्स और लॉजिक का उपयोग करके अनुरोधों को संसाधित करते हैं और प्रतिक्रियाएं उत्पन्न करते हैं।
- **Azure OpenAI सेवा:** उन्नत प्राकृतिक भाषा समझ और उत्पादन प्रदान करती है, जिससे एजेंट उपयोगकर्ता की मंशा को समझते हैं और संवादात्मक प्रतिक्रियाएं उत्पन्न करते हैं।
- **Azure AI Search और एंटरप्राइज डेटा:** एजेंट Azure AI Search और अन्य एंटरप्राइज डेटा स्रोतों से नवीनतम जानकारी प्राप्त करने के लिए क्वेरी करते हैं, जैसे फ्लाइट्स, होटल्स, और यात्रा विकल्प।
- **प्रमाणीकरण और सुरक्षा:** Microsoft Entra ID के साथ एकीकृत होता है ताकि सुरक्षित प्रमाणीकरण सुनिश्चित किया जा सके और सभी संसाधनों पर न्यूनतम-प्रिविलेज एक्सेस नियंत्रण लागू किया जा सके।
- **तैनाती:** Azure Container Apps पर तैनाती के लिए डिज़ाइन किया गया है, जो स्केलेबिलिटी, निगरानी, और परिचालन दक्षता सुनिश्चित करता है।

यह आर्किटेक्चर कई AI एजेंट्स के सहज समन्वय, एंटरप्राइज डेटा के सुरक्षित एकीकरण, और डोमेन-विशिष्ट AI समाधान बनाने के लिए एक मजबूत, विस्तार योग्य प्लेटफ़ॉर्म सक्षम बनाता है।

## आर्किटेक्चर डायग्राम का चरण-दर-चरण विवरण
कल्पना करें कि आप एक बड़ी यात्रा की योजना बना रहे हैं और आपके पास हर विवरण में मदद करने के लिए विशेषज्ञ सहायकों की एक टीम है। Azure AI Travel Agents सिस्टम इसी तरह काम करता है, जिसमें विभिन्न भाग (जैसे टीम के सदस्य) होते हैं जिनका अपना विशेष कार्य होता है। यह सब कैसे जुड़ता है, यहाँ बताया गया है:

### यूजर इंटरफ़ेस (UI):
इसे अपने ट्रैवल एजेंट के फ्रंट डेस्क के रूप में सोचें। यह वह जगह है जहाँ आप (उपयोगकर्ता) प्रश्न पूछते हैं या अनुरोध करते हैं, जैसे "पेरिस के लिए फ्लाइट ढूंढो।" यह वेबसाइट पर एक चैट विंडो या मैसेजिंग ऐप हो सकता है।

### MCP सर्वर (समन्वयक):
MCP सर्वर उस मैनेजर की तरह है जो फ्रंट डेस्क पर आपकी रिक्वेस्ट सुनता है और तय करता है कि कौन सा विशेषज्ञ किस हिस्से को संभालेगा। यह आपकी बातचीत का ट्रैक रखता है और सुनिश्चित करता है कि सब कुछ सुचारू रूप से चले।

### AI एजेंट्स (विशेषज्ञ सहायक):
प्रत्येक एजेंट एक विशिष्ट क्षेत्र में विशेषज्ञ होता है—एक फ्लाइट्स के बारे में जानता है, दूसरा होटलों के बारे में, और तीसरा आपकी यात्रा कार्यक्रम की योजना बनाता है। जब आप यात्रा के लिए पूछते हैं, तो MCP सर्वर आपकी रिक्वेस्ट सही एजेंट(स) को भेजता है। ये एजेंट अपनी जानकारी और टूल्स का उपयोग करके आपके लिए सर्वोत्तम विकल्प खोजते हैं।

### Azure OpenAI सेवा (भाषा विशेषज्ञ):
यह ऐसा है जैसे आपके पास एक भाषा विशेषज्ञ हो जो समझता है कि आप क्या पूछ रहे हैं, चाहे आप इसे किसी भी तरह से कहें। यह एजेंट्स को आपकी रिक्वेस्ट समझने और प्राकृतिक, संवादात्मक भाषा में जवाब देने में मदद करता है।

### Azure AI Search और एंटरप्राइज डेटा (सूचना पुस्तकालय):
कल्पना करें कि आपके पास एक विशाल, अद्यतन पुस्तकालय है जिसमें सभी नवीनतम यात्रा जानकारी है—फ्लाइट शेड्यूल, होटल उपलब्धता, और बहुत कुछ। एजेंट इस पुस्तकालय में खोज करते हैं ताकि आपके लिए सबसे सटीक उत्तर मिल सके।

### प्रमाणीकरण और सुरक्षा (सुरक्षा गार्ड):
जैसे एक सुरक्षा गार्ड यह जांचता है कि कौन किन क्षेत्रों में प्रवेश कर सकता है, यह हिस्सा सुनिश्चित करता है कि केवल अधिकृत लोग और एजेंट संवेदनशील जानकारी तक पहुंच सकें। यह आपके डेटा को सुरक्षित और निजी रखता है।

### Azure Container Apps पर तैनाती (भवन):
ये सभी सहायक और टूल एक सुरक्षित, स्केलेबल भवन (क्लाउड) के अंदर मिलकर काम करते हैं। इसका मतलब है कि सिस्टम एक साथ कई उपयोगकर्ताओं को संभाल सकता है और जब भी आपको जरूरत हो, हमेशा उपलब्ध रहता है।

## यह सब कैसे साथ काम करता है:

आप फ्रंट डेस्क (UI) पर एक प्रश्न पूछते हैं।  
मैनेजर (MCP सर्वर) तय करता है कि कौन सा विशेषज्ञ (एजेंट) आपकी मदद करेगा।  
विशेषज्ञ भाषा विशेषज्ञ (OpenAI) का उपयोग करके आपकी रिक्वेस्ट समझता है और पुस्तकालय (AI Search) से सबसे अच्छा जवाब खोजता है।  
सुरक्षा गार्ड (प्रमाणीकरण) सुनिश्चित करता है कि सब कुछ सुरक्षित है।  
यह सब एक भरोसेमंद, स्केलेबल भवन (Azure Container Apps) के अंदर होता है, जिससे आपका अनुभव सहज और सुरक्षित रहता है।  
यह टीमवर्क सिस्टम को तेजी से और सुरक्षित रूप से आपकी यात्रा योजना बनाने में मदद करता है, जैसे एक आधुनिक ऑफिस में विशेषज्ञ ट्रैवल एजेंट्स की टीम मिलकर काम कर रही हो!

## तकनीकी कार्यान्वयन
- **MCP सर्वर:** कोर समन्वय लॉजिक होस्ट करता है, एजेंट टूल्स को एक्सपोज़ करता है, और मल्टी-स्टेप ट्रैवल प्लानिंग वर्कफ़्लोज़ के लिए संदर्भ प्रबंधित करता है।
- **एजेंट्स:** प्रत्येक एजेंट (जैसे FlightAgent, HotelAgent) MCP टूल के रूप में कार्यान्वित होता है जिसमें अपने प्रॉम्प्ट टेम्प्लेट्स और लॉजिक होते हैं।
- **Azure एकीकरण:** प्राकृतिक भाषा समझ के लिए Azure OpenAI और डेटा पुनः प्राप्ति के लिए Azure AI Search का उपयोग करता है।
- **सुरक्षा:** Microsoft Entra ID के साथ एकीकृत होता है और सभी संसाधनों पर न्यूनतम-प्रिविलेज एक्सेस नियंत्रण लागू करता है।
- **तैनाती:** स्केलेबिलिटी और परिचालन दक्षता के लिए Azure Container Apps पर तैनाती का समर्थन करता है।

## परिणाम और प्रभाव
- दिखाता है कि MCP का उपयोग करके वास्तविक दुनिया के उत्पादन-ग्रेड परिदृश्य में कई AI एजेंट्स का समन्वय कैसे किया जा सकता है।
- एजेंट समन्वय, डेटा एकीकरण, और सुरक्षित तैनाती के लिए पुन: उपयोग योग्य पैटर्न प्रदान करके समाधान विकास को तेज करता है।
- MCP और Azure सेवाओं का उपयोग करके डोमेन-विशिष्ट, AI-संचालित एप्लिकेशन बनाने के लिए एक ब्लूप्रिंट के रूप में कार्य करता है।

## संदर्भ
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
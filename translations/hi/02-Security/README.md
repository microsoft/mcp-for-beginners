<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f00aedb7b1d11b7eaacb0618d8791c65",
  "translation_date": "2025-05-29T23:08:43+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "hi"
}
-->
# Security Best Practices

Model Context Protocol (MCP) को अपनाने से AI-चालित एप्लिकेशन में नई शक्तिशाली क्षमताएं आती हैं, लेकिन यह पारंपरिक सॉफ़्टवेयर जोखिमों से परे अनोखी सुरक्षा चुनौतियां भी लाता है। सुरक्षित कोडिंग, न्यूनतम विशेषाधिकार, और सप्लाई चेन सुरक्षा जैसे स्थापित मुद्दों के अलावा, MCP और AI वर्कलोड्स को नई धमकियों का सामना करना पड़ता है जैसे कि prompt injection, tool poisoning, और डायनामिक टूल मॉडिफिकेशन। यदि इन्हें सही तरीके से प्रबंधित नहीं किया गया, तो ये खतरे डेटा चोरी, गोपनीयता उल्लंघन, और अनचाहे सिस्टम व्यवहार का कारण बन सकते हैं।

यह पाठ MCP से जुड़े सबसे महत्वपूर्ण सुरक्षा जोखिमों—जैसे प्रमाणीकरण, प्राधिकरण, अत्यधिक अनुमतियाँ, अप्रत्यक्ष prompt injection, और सप्लाई चेन कमजोरियां—की जांच करता है और इन्हें कम करने के लिए व्यावहारिक नियंत्रण और सर्वोत्तम प्रथाएं प्रदान करता है। आप Microsoft के Prompt Shields, Azure Content Safety, और GitHub Advanced Security जैसे समाधानों का उपयोग करके अपने MCP कार्यान्वयन को मजबूत करना भी सीखेंगे। इन नियंत्रणों को समझकर और लागू करके, आप सुरक्षा उल्लंघनों की संभावना को काफी हद तक कम कर सकते हैं और सुनिश्चित कर सकते हैं कि आपके AI सिस्टम मजबूत और विश्वसनीय बने रहें।

# Learning Objectives

इस पाठ के अंत तक, आप सक्षम होंगे:

- Model Context Protocol (MCP) द्वारा प्रस्तुत अनोखे सुरक्षा जोखिमों की पहचान और व्याख्या करना, जिनमें prompt injection, tool poisoning, अत्यधिक अनुमतियाँ, और सप्लाई चेन कमजोरियां शामिल हैं।
- MCP सुरक्षा जोखिमों के लिए प्रभावी निवारक नियंत्रणों का वर्णन और उपयोग करना, जैसे मजबूत प्रमाणीकरण, न्यूनतम विशेषाधिकार, सुरक्षित टोकन प्रबंधन, और सप्लाई चेन सत्यापन।
- Microsoft के Prompt Shields, Azure Content Safety, और GitHub Advanced Security जैसे समाधानों को समझना और MCP तथा AI वर्कलोड्स की सुरक्षा के लिए उनका लाभ उठाना।
- टूल मेटाडेटा को सत्यापित करने, डायनामिक बदलावों की निगरानी करने, और अप्रत्यक्ष prompt injection हमलों से बचाव के महत्व को पहचानना।
- स्थापित सुरक्षा सर्वोत्तम प्रथाओं—जैसे सुरक्षित कोडिंग, सर्वर हार्डनिंग, और ज़ीरो ट्रस्ट आर्किटेक्चर—को MCP कार्यान्वयन में शामिल करके सुरक्षा उल्लंघनों की संभावना और प्रभाव को कम करना।

# MCP security controls

कोई भी सिस्टम जिसके पास महत्वपूर्ण संसाधनों तक पहुंच होती है, उसे सुरक्षा चुनौतियों का सामना करना पड़ता है। सुरक्षा चुनौतियों को आमतौर पर मौलिक सुरक्षा नियंत्रणों और अवधारणाओं के सही अनुप्रयोग से हल किया जा सकता है। चूंकि MCP अभी नया परिभाषित हुआ है, इसकी विशिष्टता तेजी से बदल रही है और प्रोटोकॉल के विकसित होने के साथ सुरक्षा नियंत्रण भी परिपक्व होंगे, जिससे इसे एंटरप्राइज और स्थापित सुरक्षा आर्किटेक्चर तथा सर्वोत्तम प्रथाओं के साथ बेहतर एकीकरण मिलेगा।

[Microsoft Digital Defense Report](https://aka.ms/mddr) में प्रकाशित शोध के अनुसार, रिपोर्ट किए गए 98% उल्लंघनों को मजबूत सुरक्षा स्वच्छता द्वारा रोका जा सकता है और किसी भी प्रकार के उल्लंघन से बचाव का सबसे अच्छा तरीका है आपकी बुनियादी सुरक्षा स्वच्छता, सुरक्षित कोडिंग सर्वोत्तम प्रथाएं, और सप्लाई चेन सुरक्षा को सही रखना — ये जानी-पहचानी और परीक्षण की गई प्रथाएं सुरक्षा जोखिम को कम करने में सबसे प्रभावी हैं।

आइए देखें कि MCP को अपनाते समय आप सुरक्षा जोखिमों को कैसे संबोधित कर सकते हैं।

> **Note:** निम्नलिखित जानकारी **29 मई 2025** तक सही है। MCP प्रोटोकॉल लगातार विकसित हो रहा है, और भविष्य के कार्यान्वयन नए प्रमाणीकरण पैटर्न और नियंत्रण पेश कर सकते हैं। नवीनतम अपडेट और मार्गदर्शन के लिए हमेशा [MCP Specification](https://spec.modelcontextprotocol.io/) और आधिकारिक [MCP GitHub repository](https://github.com/modelcontextprotocol) तथा [security best practice page](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) देखें।

### Problem statement  
मूल MCP स्पेसिफिकेशन ने यह माना था कि डेवलपर्स अपना खुद का प्रमाणीकरण सर्वर बनाएंगे। इसके लिए OAuth और संबंधित सुरक्षा प्रतिबंधों का ज्ञान आवश्यक था। MCP सर्वर OAuth 2.0 Authorization Servers के रूप में कार्य करते थे, जो सीधे उपयोगकर्ता प्रमाणीकरण प्रबंधित करते थे बजाय इसके कि इसे Microsoft Entra ID जैसे बाहरी सेवा को सौंपा जाए। **26 अप्रैल 2025** से MCP स्पेसिफिकेशन के एक अपडेट ने MCP सर्वरों को उपयोगकर्ता प्रमाणीकरण बाहरी सेवा को सौंपने की अनुमति दी है।

### Risks
- MCP सर्वर में गलत कॉन्फ़िगर किया गया प्राधिकरण लॉजिक संवेदनशील डेटा के खुलासे और गलत तरीके से लागू किए गए एक्सेस कंट्रोल का कारण बन सकता है।
- स्थानीय MCP सर्वर पर OAuth टोकन चोरी। यदि टोकन चोरी हो जाता है, तो इसका उपयोग MCP सर्वर की नकल करने और उस सेवा से संसाधनों और डेटा तक पहुंचने के लिए किया जा सकता है जिसके लिए OAuth टोकन जारी किया गया है।

#### Token Passthrough
Token passthrough प्राधिकरण स्पेसिफिकेशन में स्पष्ट रूप से निषिद्ध है क्योंकि यह कई सुरक्षा जोखिम पैदा करता है, जिनमें शामिल हैं:

#### Security Control Circumvention
MCP सर्वर या डाउनस्ट्रीम APIs महत्वपूर्ण सुरक्षा नियंत्रण लागू कर सकते हैं जैसे कि रेट लिमिटिंग, अनुरोध सत्यापन, या ट्रैफिक मॉनिटरिंग, जो टोकन ऑडियंस या अन्य क्रेडेंशियल प्रतिबंधों पर निर्भर करते हैं। यदि क्लाइंट सीधे डाउनस्ट्रीम APIs के साथ टोकन प्राप्त कर उपयोग कर सकते हैं बिना MCP सर्वर द्वारा सही तरीके से टोकन की वैधता जांचे, तो वे इन नियंत्रणों को बायपास कर देते हैं।

#### Accountability and Audit Trail Issues
जब क्लाइंट अपस्ट्रीम-इशू किए गए एक्सेस टोकन के साथ कॉल करते हैं, जो MCP सर्वर के लिए अस्पष्ट हो सकता है, तो MCP सर्वर MCP क्लाइंट्स की पहचान या भेद नहीं कर पाएगा।  
डाउनस्ट्रीम रिसोर्स सर्वर के लॉग ऐसे अनुरोध दिखा सकते हैं जो किसी अन्य स्रोत या पहचान से आ रहे हों, बजाय उस MCP सर्वर के जो वास्तव में टोकन अग्रेषित कर रहा है।  
ये दोनों पहलू घटना जांच, नियंत्रण और ऑडिटिंग को कठिन बना देते हैं।  
यदि MCP सर्वर टोकन के दावों (जैसे भूमिकाएं, विशेषाधिकार, या ऑडियंस) या अन्य मेटाडेटा को जांचे बिना टोकन पास करता है, तो एक दुर्भावनापूर्ण व्यक्ति जो चोरी किए गए टोकन के कब्जे में है, सर्वर का उपयोग डेटा चोरी के लिए प्रॉक्सी के रूप में कर सकता है।

#### Trust Boundary Issues
डाउनस्ट्रीम रिसोर्स सर्वर विशिष्ट संस्थाओं को भरोसा देता है। यह भरोसा उत्पत्ति या क्लाइंट व्यवहार पैटर्न के बारे में मान्यताएं शामिल कर सकता है। इस ट्रस्ट सीमा को तोड़ना अप्रत्याशित समस्याओं को जन्म दे सकता है।  
यदि टोकन कई सेवाओं द्वारा उचित सत्यापन के बिना स्वीकार किया जाता है, तो एक सेवा के समझौता होने पर हमलावर उस टोकन का उपयोग अन्य जुड़े हुए सेवाओं तक पहुंचने के लिए कर सकता है।

#### Future Compatibility Risk
यदि आज MCP सर्वर "शुद्ध प्रॉक्सी" के रूप में शुरू होता है, तो भविष्य में इसे सुरक्षा नियंत्रण जोड़ने की आवश्यकता हो सकती है। उचित टोकन ऑडियंस पृथक्करण के साथ शुरू करना सुरक्षा मॉडल को विकसित करना आसान बनाता है।

### Mitigating controls

**MCP सर्वर को ऐसे किसी भी टोकन को स्वीकार नहीं करना चाहिए जो स्पष्ट रूप से MCP सर्वर के लिए जारी नहीं किए गए हों।**

- **प्राधिकरण लॉजिक की समीक्षा और सख्ती:** अपने MCP सर्वर के प्राधिकरण कार्यान्वयन का सावधानीपूर्वक ऑडिट करें ताकि केवल इच्छित उपयोगकर्ता और क्लाइंट ही संवेदनशील संसाधनों तक पहुंच सकें। व्यावहारिक मार्गदर्शन के लिए देखें [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) और [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/)।
- **सुरक्षित टोकन प्रथाओं को लागू करें:** टोकन के दुरुपयोग और टोकन पुन: उपयोग या चोरी के जोखिम को कम करने के लिए [Microsoft के टोकन सत्यापन और जीवनकाल के सर्वोत्तम प्रथाओं](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) का पालन करें।
- **टोकन भंडारण की सुरक्षा करें:** टोकन को हमेशा सुरक्षित रूप से स्टोर करें और उन्हें स्थिर और ट्रांजिट दोनों में एन्क्रिप्ट करें। कार्यान्वयन सुझावों के लिए देखें [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)।

# Excessive permissions for MCP servers

### Problem statement  
MCP सर्वरों को उस सेवा/संसाधन के लिए अत्यधिक अनुमतियाँ दी गई हो सकती हैं, जिसे वे एक्सेस कर रहे हैं। उदाहरण के लिए, एक AI बिक्री एप्लिकेशन का हिस्सा MCP सर्वर जिसे एंटरप्राइज डेटा स्टोर से कनेक्ट किया गया है, उसे केवल बिक्री डेटा तक पहुंच होनी चाहिए न कि स्टोर की सभी फाइलों तक। न्यूनतम विशेषाधिकार के सिद्धांत (जो सबसे पुरानी सुरक्षा सिद्धांतों में से एक है) के अनुसार, किसी भी संसाधन को केवल आवश्यक कार्यों को निष्पादित करने के लिए आवश्यक अनुमतियाँ ही मिलनी चाहिए। AI इस संदर्भ में चुनौतीपूर्ण है क्योंकि इसे लचीला बनाने के लिए आवश्यक सटीक अनुमतियों को परिभाषित करना मुश्किल हो सकता है।

### Risks  
- अत्यधिक अनुमतियाँ देने से MCP सर्वर को ऐसे डेटा तक पहुंच या संशोधन करने की अनुमति मिल सकती है जिसे एक्सेस करने का उसका इरादा नहीं था। यदि डेटा व्यक्तिगत पहचान योग्य जानकारी (PII) है, तो यह गोपनीयता का मुद्दा भी हो सकता है।

### Mitigating controls  
- **न्यूनतम विशेषाधिकार सिद्धांत लागू करें:** MCP सर्वर को केवल आवश्यक कार्यों के लिए न्यूनतम अनुमतियाँ दें। नियमित रूप से इन अनुमतियों की समीक्षा और अद्यतन करें ताकि वे आवश्यकता से अधिक न हों। विस्तृत मार्गदर्शन के लिए देखें [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)।
- **Role-Based Access Control (RBAC) का उपयोग करें:** MCP सर्वर को ऐसे भूमिकाएँ सौंपें जो विशिष्ट संसाधनों और क्रियाओं तक सख्ती से सीमित हों, व्यापक या अनावश्यक अनुमतियों से बचें।
- **अनुमतियों की निगरानी और ऑडिट करें:** अनुमति उपयोग की लगातार निगरानी करें और एक्सेस लॉग्स का ऑडिट करें ताकि अत्यधिक या अप्रयुक्त विशेषाधिकारों का शीघ्र पता लगाया जा सके और सुधार किया जा सके।

# Indirect prompt injection attacks

### Problem statement

दुर्भावनापूर्ण या समझौता किए गए MCP सर्वर महत्वपूर्ण जोखिम पैदा कर सकते हैं, जैसे ग्राहक डेटा का खुलासा या अनचाहे क्रियाओं को सक्षम करना। ये खतरे AI और MCP आधारित वर्कलोड्स में विशेष रूप से प्रासंगिक हैं, जहां:

- **Prompt Injection Attacks**: हमलावर prompts या बाहरी सामग्री में दुर्भावनापूर्ण निर्देश छुपाते हैं, जिससे AI सिस्टम अनचाहे कार्य करता है या संवेदनशील डेटा लीक होता है। अधिक जानें: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- **Tool Poisoning**: हमलावर टूल मेटाडेटा (जैसे विवरण या पैरामीटर) को प्रभावित करते हैं ताकि AI के व्यवहार को नियंत्रित किया जा सके, संभवतः सुरक्षा नियंत्रणों को बायपास किया जा सके या डेटा चोरी हो सके। विवरण: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- **Cross-Domain Prompt Injection**: दुर्भावनापूर्ण निर्देश दस्तावेज़ों, वेब पेजों, या ईमेल में छुपाए जाते हैं, जिन्हें AI संसाधित करता है, जिससे डेटा लीक या हेरफेर हो सकता है।
- **Dynamic Tool Modification (Rug Pulls)**: उपयोगकर्ता की मंजूरी के बाद टूल परिभाषाएं बदली जा सकती हैं, जिससे नए दुर्भावनापूर्ण व्यवहार बिना उपयोगकर्ता की जानकारी के आ सकते हैं।

ये कमजोरियां MCP सर्वर और टूल्स को आपके पर्यावरण में एकीकृत करते समय मजबूत सत्यापन, निगरानी, और सुरक्षा नियंत्रण की आवश्यकता को दर्शाती हैं। अधिक जानकारी के लिए ऊपर दिए गए लिंक देखें।

![prompt-injection-lg-2048x1034](../../../translated_images/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.hi.png)

**Indirect Prompt Injection** (जिसे cross-domain prompt injection या XPIA भी कहा जाता है) जनरेटिव AI सिस्टम्स में एक गंभीर कमजोरी है, जिनमें Model Context Protocol (MCP) का उपयोग होता है। इस हमले में, दुर्भावनापूर्ण निर्देश बाहरी सामग्री जैसे दस्तावेज़, वेब पेज, या ईमेल में छुपाए जाते हैं। जब AI सिस्टम इस सामग्री को संसाधित करता है, तो यह छुपाए गए निर्देशों को वैध उपयोगकर्ता कमांड के रूप में समझ सकता है, जिसके परिणामस्वरूप डेटा लीक, हानिकारक सामग्री निर्माण, या उपयोगकर्ता इंटरैक्शन में हेरफेर हो सकता है। विस्तृत व्याख्या और वास्तविक उदाहरणों के लिए देखें [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)।

इस हमले का एक विशेष रूप है **Tool Poisoning**। इसमें हमलावर MCP टूल्स के मेटाडेटा (जैसे टूल विवरण या पैरामीटर) में दुर्भावनापूर्ण निर्देश डालते हैं। चूंकि बड़े भाषा मॉडल (LLMs) इस मेटाडेटा पर निर्भर करते हैं यह तय करने के लिए कि कौन से टूल कॉल करने हैं, इसलिए समझौता किए गए विवरण मॉडल को अनधिकृत टूल कॉल करने या सुरक्षा नियंत्रणों को बायपास करने के लिए प्रेरित कर सकते हैं। ये हेरफेर अक्सर अंतिम उपयोगकर्ताओं के लिए अदृश्य होते हैं, लेकिन AI सिस्टम द्वारा समझे और क्रियान्वित किए जाते हैं। यह जोखिम विशेष रूप से होस्टेड MCP सर्वर वातावरण में बढ़ जाता है, जहां उपयोगकर्ता की मंजूरी के बाद टूल परिभाषाएं अपडेट की जा सकती हैं—जिसे कभी-कभी "[rug pull](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)" कहा जाता है। ऐसे मामलों में, एक टूल जो पहले सुरक्षित था, बाद में दुर्भावनापूर्ण कार्य करने के लिए संशोधित किया जा सकता है, जैसे डेटा चोरी या सिस्टम व्यवहार में बदलाव, बिना उपयोगकर्ता की जानकारी के। इस हमले के बारे में अधिक जानकारी के लिए देखें [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)।

![tool-injection-lg-2048x1239 (1)](../../../translated_images/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.hi.png)

## Risks  
अनचाहे AI क्रियाएं विभिन्न सुरक्षा जोखिम पेश करती हैं, जिनमें डेटा चोरी और गोपनीयता उल्लंघन शामिल हैं।

### Mitigating controls  
### अप्रत्यक्ष Prompt Injection हमलों से बचाव के लिए Prompt Shields का उपयोग
-----------------------------------------------------------------------------

**AI Prompt Shields** Microsoft द्वारा विकसित एक समाधान है जो सीधे और अप्रत्यक्ष दोनों प्रकार के prompt injection हमलों से रक्षा करता है। यह निम्न तरीकों से मदद करता है:

1.  **डिटेक्शन और फ़िल्टरिंग:** Prompt Shields उन्नत मशीन लर्निंग एल्गोरिदम और प्राकृतिक भाषा प्रसंस्करण का उपयोग करके दस्तावेज़ों, वेब पेजों, या ईमेल जैसी बाहरी सामग्री में छुपे दुर्भावनापूर्ण निर्देशों का पता लगाते और उन्हें फ़िल्टर करते हैं।
    
2.  **Spotlighting:** यह तकनीक AI सिस्टम को वैध सिस्टम निर्देशों और संभावित अविश्वसनीय बाहरी इनपुट के बीच अंतर करने में मदद करती है। इनपुट टेक्स्ट को इस तरह परिवर्तित करके जो मॉडल के लिए अधिक प्रासंगिक हो, Spotlighting सुनिश्चित करता है कि AI दुर्भावनापूर्ण निर्देशों को बेहतर तरीके से पहचान सके और अनदेखा कर सके।
    
3.  **Delimiters और Datamarking:** सिस्टम संदेश में delimiters शामिल करना इनपुट टेक्स्ट के स्थान को स्पष्ट रूप से रेखांकित करता है, जिससे AI सिस्टम उपयोगकर्ता इनपुट को संभावित हानिकारक बाहरी सामग्री से अलग पहचान सके। Datamarking इस अवधारणा को आगे बढ़ाता है और विशेष मार्करों का उपयोग करके विश्वसनीय और अविश्वसनीय डेटा की सीमाओं को हाइलाइट करता है।
    
4.  **लगातार निगरानी और अपडेट्स:** Microsoft लगातार Prompt Shields की निगरानी और अपडेट करता है ताकि नए और विकसित हो रहे खतरों का सामना किया जा सके। यह सक्रिय दृष्टिकोण सुनिश्चित करता है कि सुरक्षा नवीनतम हमले तकनीकों के खिलाफ प्रभावी बनी रहे।
    
5. **Azure Content Safety के साथ एकीकरण:** Prompt Shields व्यापक Azure AI Content Safety सूट का हिस्सा हैं, जो AI एप्लिकेशन में jailbreak प्रयासों, हानिकारक सामग्री, और अन्य सुरक्षा जोखिमों का पता लगाने के लिए अतिरिक्त उपकरण प्रदान करता है।

आप AI prompt shields के बारे में अधिक पढ़ सकते हैं [Prompt Shields documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) में।

![prompt-shield-lg-2048x1328](../../../translated_images/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.hi.png)

### Supply chain security

AI युग में सप्लाई चेन सुरक्षा मूलभूत बनी हुई है, लेकिन आपकी सप्ल
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure DevOps](https://azure.microsoft.com/products/devops)
- [Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)
- [Secure Least-Privileged Access (Microsoft)](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Best Practices for Token Validation and Lifetime](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Use Secure Token Storage and Encrypt Tokens (YouTube)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)
- [Azure API Management as Auth Gateway for MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [MCP Security Best Practice](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [Using Microsoft Entra ID to Authenticate with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

### अगला

अगला: [अध्याय 3: शुरूआत](/03-GettingStarted/README.md)

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
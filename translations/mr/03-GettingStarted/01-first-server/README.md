<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bf05718d019040cf0c7d4ccc6d6a1a88",
  "translation_date": "2025-06-13T05:56:33+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "mr"
}
-->
### -2- प्रोजेक्ट तयार करा

आता जेव्हा तुमच्याकडे SDK इन्स्टॉल झाले आहे, तर पुढे प्रोजेक्ट तयार करूया: 

### -3- प्रोजेक्ट फाइल्स तयार करा

### -4- सर्व्हर कोड तयार करा

### -5- टूल आणि रिसोर्स जोडणे

खालील कोड जोडून एक टूल आणि एक रिसोर्स जोडा:

### -6 अंतिम कोड

सर्व्हर सुरू करण्यासाठी आवश्यक शेवटचा कोड जोडूया:

### -7- सर्व्हर चाचणी करा

खालील कमांडने सर्व्हर सुरू करा:

### -8- इन्स्पेक्टर वापरून चालवा

इन्स्पेक्टर हा एक उत्कृष्ट टूल आहे जो तुमचा सर्व्हर सुरू करतो आणि तुम्हाला त्याच्याशी संवाद साधण्याची परवानगी देतो, ज्यामुळे तुम्ही तपासू शकता की तो योग्यरित्या कार्य करत आहे की नाही. चला तो सुरू करूया:

> [!NOTE]
> "command" फील्डमध्ये कमांड थोडी वेगळी दिसू शकते कारण ती तुमच्या विशिष्ट रनटाइमसाठी सर्व्हर चालवण्याची कमांड असते.

तुम्हाला खालील युजर इंटरफेस दिसेल:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.mr.png)

1. Connect बटणावर क्लिक करून सर्व्हरशी कनेक्ट व्हा  
  एकदा तुम्ही सर्व्हरशी कनेक्ट झालात की, तुम्हाला खालील स्क्रीन दिसेल:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.mr.png)

2. "Tools" आणि "listTools" निवडा, तुम्हाला "Add" दिसेल, "Add" निवडा आणि पॅरामीटर व्हॅल्यूज भरा.

  तुम्हाला खालील प्रतिसाद दिसेल, म्हणजे "add" टूलचा निकाल:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.mr.png)

अभिनंदन, तुम्ही तुमचा पहिला सर्व्हर तयार करून चालविला आहे!

### अधिकृत SDKs

MCP विविध भाषांसाठी अधिकृत SDKs पुरवते:  
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft सोबत सहकार्याने देखभाल  
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI सोबत सहकार्याने देखभाल  
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - अधिकृत TypeScript अंमलबजावणी  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - अधिकृत Python अंमलबजावणी  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - अधिकृत Kotlin अंमलबजावणी  
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI सोबत सहकार्याने देखभाल  
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - अधिकृत Rust अंमलबजावणी  

## मुख्य मुद्दे

- MCP विकास वातावरण सेटअप करणे भाषा-विशिष्ट SDKs मुळे सोपे आहे  
- MCP सर्व्हर तयार करताना टूल्स तयार करणे आणि नोंदणी करणे आवश्यक आहे ज्यांचे स्पष्ट स्कीमा असतात  
- चाचणी आणि डिबगिंग विश्वसनीय MCP अंमलबजावणीसाठी अत्यंत महत्त्वाचे आहे  

## नमुने 

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  

## असाइनमेंट

तुमच्या पसंतीच्या टूलसह एक सोपा MCP सर्व्हर तयार करा:  
1. तुमच्या पसंतीच्या भाषेत टूलची अंमलबजावणी करा (.NET, Java, Python, किंवा JavaScript).  
2. इनपुट पॅरामीटर्स आणि परतावा मूल्ये परिभाषित करा.  
3. इन्स्पेक्टर टूल चालवा आणि खात्री करा की सर्व्हर अपेक्षेनुसार कार्य करत आहे.  
4. विविध इनपुटसह अंमलबजावणीची चाचणी करा.  

## सोल्यूशन

[Solution](./solution/README.md)

## अतिरिक्त संसाधने

- [Azure वर Model Context Protocol वापरून एजंट तयार करणे](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)  
- [Azure Container Apps सह Remote MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)  
- [.NET OpenAI MCP एजंट](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)  

## पुढे काय

पुढे: [MCP Clients सह सुरुवात](/03-GettingStarted/02-client/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावणीबद्दल आम्ही जबाबदार नाही.
## चाचणी आणि डीबगिंग

आपला MCP सर्व्हर चाचणीसाठी सुरू करण्यापूर्वी, उपलब्ध साधने आणि डीबगिंगसाठी सर्वोत्तम पद्धती समजून घेणे महत्त्वाचे आहे. प्रभावी चाचणी आपल्या सर्व्हरचा अपेक्षित वर्तन सुनिश्चित करते आणि समस्या लवकर शोधून काढत आणि सोडवण्यात मदत करते. पुढील विभागात आपल्या MCP अंमलबजावणीचे प्रमाणीकरण करण्यासाठी शिफारस केलेले दृष्टिकोन दिले आहेत.

## आढावा

हा धडा योग्य चाचणी दृष्टिकोन कसा निवडायचा आणि सर्वात प्रभावी चाचणी साधन कोणते आहे हे लिहितो.

## शिकण्याचे उद्दिष्ट

या धड्याच्या शेवटी, आपण सक्षम असाल:

- चाचणीसाठी विविध दृष्टिकोनांचे वर्णन करा.
- आपल्या कोडची प्रभावी चाचणी करण्यासाठी वेगवेगळी साधने वापरा.

## MCP सर्व्हर्सची चाचणी

MCP आपले सर्व्हर चाचणीसाठी आणि डीबग करण्यासाठी साधने प्रदान करते:

- **MCP Inspector**: एक कमांड लाइन साधन जे CLI टूल म्हणून आणि व्हिज्युअल टूल म्हणून चालवू शकता.
- **मॅन्युअल चाचणी**: आपण curl सारखे साधन वापरून वेब विनंत्या करू शकता, परंतु कोणतेही HTTP चालवणारे साधन चालेल.
- **युनिट चाचणी**: आपल्या पसंतीच्या चाचणी फ्रेमवर्क वापरून सर्व्हर आणि क्लायंटच्या फिचर्सची चाचणी करणे शक्य आहे.

### MCP Inspector वापरणे

आम्ही या साधनाचा वापर मागील धड्यांत वर्णन केला आहे परंतु यावर थोडक्यात चर्चा करूया. हे Node.js मध्ये तयार केलेले साधन आहे आणि आपण `npx` executable कॉल करून हे वापरू शकता जे साधन स्वतः तात्पुरते डाउनलोड आणि इंस्टॉल करेल आणि नंतर आपली विनंती पूर्ण झाल्यावर ते स्वच्छ करेल.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) आपल्याला मदत करतो:

- **सर्व्हर काबिलियत शोधा**: उपलब्ध संसाधने, साधने आणि प्रॉम्प्ट्स आपोआप शोधणे
- **टूल एक्सिक्युशन तपासा**: विविध पॅरामीटर्स वापरून वेळोवेळी प्रतिसाद पाहणे
- **सर्व्हर मेटाडेटा पहा**: सर्व्हर माहिती, स्कीमा आणि कॉन्फिगरेशन तपासणे

साधन चालवण्याचे एक सामान्य उदाहरण असे दिसते:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

वरील कमांड MCP आणि त्याचा व्हिज्युअल इंटरफेस सुरू करतो आणि आपल्या ब्राउझरमध्ये स्थानिक वेब इंटरफेस उघडतो. आपण एक डॅशबोर्ड पाहू शकता ज्यात आपल्या नोंदणीकृत MCP सर्व्हर्स, त्यांची उपलब्ध साधने, संसाधने आणि प्रॉम्प्ट्स दिसतात. इंटरफेस आपल्याला संवादात्मक पद्धतीने टूल एक्सिक्युशनची चाचणी करण्यास, सर्व्हर मेटाडेटा तपासण्यास आणि रिअल-टाइम प्रतिसाद पाहण्यास अनुमती देतो, ज्यामुळे आपल्या MCP सर्व्हर अंमलबजावणीचे प्रमाणीकरण आणि डीबगिंग सोपे होते.

हे कसे दिसू शकते: ![Inspector](../../../../translated_images/mr/connect.141db0b2bd05f096.webp)

आपण हे साधन CLI मोडमध्ये देखील चालवू शकता ज्यासाठी `--cli` अॅट्रीब्युट जोडा. येथे टूल सर्व्हरवरील सर्व साधने सूचीबद्ध करणाऱ्या "CLI" मोडमध्ये साधन चालवण्याचे उदाहरण आहे:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### मॅन्युअल चाचणी

सर्व्हर काबिलियत तपासण्यासाठी Inspector टूल चालवण्यापासून वेगळा पर्याय म्हणजे HTTP वापरून काही क्लायंट चालवणे, उदाहरणार्थ curl.

curl वापरून आपण MCP सर्व्हर्स थेट HTTP विनंत्यांद्वारे चाचणी करू शकता:

```bash
# उदाहरण: सर्व्हर मेटाडेटा चाचणी
curl http://localhost:3000/v1/metadata

# उदाहरण: एक साधन कार्यान्वित करा
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

वरील curl वापरून दिसत आहे की, आपण POST विनंती वापरून टूलचे नाव आणि त्याचे पॅरामीटर्स असलेला पेलोड वापरून टूल कॉल करता. आपल्यासाठी ज्याप्रमाणे योग्य वाटेल तो दृष्टिकोन वापरा. CLI साधने सामान्यतः वापरण्यास जलद असतात आणि स्क्रिप्ट लिहिण्यास अनुकूल असतात, जे CI/CD वातावरणात उपयुक्त ठरते.

### युनिट चाचणी

आपल्या साधने व संसाधनांसाठी युनिट चाचणी तयार करा जेणेकरून ती अपेक्षित प्रमाणे कार्य करतील. खाली काही उदाहरण चाचणी कोड आहे.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# संपूर्ण मॉड्यूल async चाचण्यांसाठी चिन्हांकित करा
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # काही चाचणी साधने तयार करा
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # कर्सर पॅरामीटरशिवाय चाचणी (वगळलेले)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # कर्सर=None सह चाचणी
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # कर्सर स्ट्रिंग म्हणून चाचणी
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # रिकाम्या स्ट्रिंग कर्सर सह चाचणी
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

वरील कोड पुढील गोष्टी करतो:

- pytest फ्रेमवर्कचा उपयोग करतो जो आपल्याला फंक्शन्स म्हणून चाचण्या तयार करण्याची आणि assert स्टेटमेंट्स वापरण्याची परवानगी देतो.
- दोन वेगवेगळ्या साधनांसह MCP सर्व्हर तयार करतो.
- काही अटी पूर्ण झाल्या आहेत का ते तपासण्यासाठी `assert` स्टेटमेंट वापरतो.

पूर्ण फाइल येथे पहा: [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

वरील फाइलच्या आधारावर, आपण स्वतःचा सर्व्हर चाचणी करू शकता आणि तपासू शकता की काबिलियत योग्य प्रकारे तयार झाली आहे की नाही.

सर्व प्रमुख SDKs मध्ये असेच चाचणी विभाग असतात जेणेकरून आपण आपल्या निवडलेल्या रनटाइमनुसार समायोजन करू शकता.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## अतिरिक्त संसाधने

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## पुढे काय

- पुढे: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेमधील त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. गंभीर माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थसंग्रहासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
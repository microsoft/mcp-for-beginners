## चाचणी आणि डिबगिंग

आपला MCP सर्व्हर चाचणी करायच्या आधी, उपलब्ध साधने आणि डिबगिंगसाठी सर्वोत्तम पद्धती समजून घेणे महत्त्वाचे आहे. प्रभावी चाचणी सुनिश्चित करते की आपला सर्व्हर अपेक्षित वर्तन करतो आणि समस्या त्वरेने ओळखून सोडवायला मदत करते. पुढील विभागात MCP अंमलबजावणी मान्य करण्यासाठी शिफारस केलेल्या दृष्टिकोनांचा उल्लेख केला आहे.

## आढावा

हा धडा योग्य चाचणी दृष्टिकोन कसा निवडायचा आणि सर्वात प्रभावी चाचणी साधन कोणते आहे हे कव्हर करतो.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, आपण सक्षम असाल:

- चाचणीसाठी विविध दृष्टिकोनांचे वर्णन करणे.
- आपला कोड प्रभावीपणे चाचणी करण्यासाठी वेगवेगळ्या साधनांचा वापर करणे.

## MCP सर्व्हर्सची चाचणी करणे

MCP आपल्याला आपले सर्व्हर चाचणी आणि डिबग करण्यासाठी साधने पुरवते:

- **MCP Inspector**: एक कमांड लाइन साधन जे CLI साधन आणि व्हिज्युअल साधन म्हणून चालविले जाऊ शकते.
- **मॅन्युअल चाचणी**: आपण curl सारखे साधन वापरून वेब विनंत्या चालवू शकता, पण HTTP चालविण्यायोग्य कोणतेही साधन चालेल.
- **युनिट चाचणी**: आपल्या पसंतीच्या चाचणी फ्रेमवर्कचा वापर करून दोन्ही सर्व्हर आणि क्लायंटच्या फिचर्सची चाचणी करणे शक्य आहे.

### MCP Inspector चा वापर

आपण या साधनाचा उपयोग मागील धड्यांमध्ये वर्णन केला आहे, पण उच्च पातळीवर याबद्दल थोडक्यात बोलूया. हे Node.js मध्ये तयार केलेले एक साधन आहे आणि आपण ते `npx` कार्यान्वयक कॉल करून वापरू शकता, जे साधन स्वतः थोडक्याच काळासाठी डाउनलोड आणि इंस्टॉल करते आणि आपली विनंती पूर्ण झाल्यावर स्वतःला स्वच्छ करते.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) आपल्याला मदत करतो:

- **सर्व्हर क्षमतांची शोध घेणे**: उपलब्ध संसाधने, साधने आणि प्रॉम्प्ट स्वयंचलितपणे शोधा
- **साधन कार्यान्वयन चाचणी**: विविध पॅरामीटर्स वापरून पाहा आणि रिअल-टाइम प्रतिसाद पहा
- **सर्व्हर मेटाडेटा पहा**: सर्व्हर माहिती, स्कीमां आणि संरचना तपासा

साधनाचा एक सामान्य वापर खालीलप्रमाणे दिसतो:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

वरील आज्ञा एक MCP सुरु करते आणि त्याचा व्हिज्युअल इंटरफेस उघडते, आपल्या ब्राउझरमध्ये एक स्थानिक वेब इंटरफेस लाँच करते. आपण आपल्या नोंदणीकृत MCP सर्व्हर्स, उपलब्ध साधने, संसाधने आणि प्रॉम्प्ट्स दाखवणारा डॅशबोर्ड पाहू शकता. हा इंटरफेस आपल्याला इंटरऐक्टिव्हली साधन कार्यान्वयन चाचणी करण्यास, सर्व्हर मेटाडेटा तपासण्यास आणि रिअल-टाइम प्रतिसाद पाहण्यास परवानगी देतो, ज्यामुळे आपली MCP सर्व्हर अंमलबजावणी वैध ठरणे आणि डिबग करणे सोपे होते.

हे कसे दिसू शकते येथे पाहा: ![Inspector](../../../../translated_images/mr/connect.141db0b2bd05f096.webp)

आपण हे साधन CLI मोडमध्ये देखील चालवू शकता ज्यासाठी आपण `--cli` गुणधर्म जोडू शकता. येथे सर्व्हरवरील सर्व साधने यादीबद्ध करणाऱ्या "CLI" मोडमध्ये साधन चालवण्याचे उदाहरण आहे:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### मॅन्युअल चाचणी

सर्व्हर क्षमतांची चाचणी करण्यासाठी inspector साधन चालविण्याच्या व्यतिरिक्त, आणखी एक समान दृष्टिकोन म्हणजे HTTP वापरण्यास सक्षम क्लायंट, जसे की curl, चालविणे.

curl वापरून, आपण MCP सर्व्हर्स थेट HTTP विनंत्यांद्वारे चाचणी करू शकता:

```bash
# उदाहरण: चाचणी सर्व्हर मेटाडेटा
curl http://localhost:3000/v1/metadata

# उदाहरण: साधन कार्यान्वित करा
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

वर दिलेल्या curl च्या वापरातून आपण पाहू शकता की आपण एक POST विनंती वापरून साधन चालविता, ज्यात साधनाचे नाव आणि त्याचे पॅरामीटर्स दिलेले असतात. आपल्याला योग्य वाटणारी पद्धत वापरा. CLI साधने सामान्यतः वापरण्यास जलद असतात आणि त्यांना स्क्रिप्टमध्ये वापरले जाऊ शकते, जे CI/CD वातावरणात उपयुक्त ठरू शकते.

### युनिट चाचणी

आपल्या साधने आणि संसाधनांसाठी युनिट चाचण्या तयार करा जेणेकरून ते अपेक्षेनुसार काम करतात याची खात्री करता येईल. येथे यामधील काही उदाहरण चाचणी कोड आहे.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# असिंक चाचण्यांसाठी संपूर्ण मॉड्यूल चिन्हांकित करा
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

        # कर्सर=None सह चाचणी करा
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # कर्सर स्ट्रिंग म्हणून आहे अशी चाचणी करा
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # रिक्त स्ट्रिंग कर्सर सह चाचणी करा
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

वरील कोड खालीलप्रमाणे कार्य करतो:

- pytest फ्रेमवर्कचा वापर करतो जो आपल्याला फंक्शन्स म्हणून चाचण्या तयार करण्याची आणि assert स्टेटमेंट्स वापरण्याची परवानगी देतो.
- दोन वेगवेगळ्या साधनांसह एक MCP सर्व्हर तयार करतो.
- काही विशिष्ट स्थिती पूर्ण झाल्या आहेत की नाही हे तपासण्यासाठी `assert` स्टेटमेंट वापरतो.

पूर्ण फाइल येथे पहा: [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

वरील फाइलच्या आधारे, आपण आपला स्वतःचा सर्व्हर चाचणी करू शकता जेणेकरून क्षमतांची निर्मिती योग्यरित्या होत आहे याची खात्री होईल.

सर्व प्रमुख SDK मध्ये तत्सम चाचणी विभाग आहेत जेणेकरून आपण आपल्या निवडलेल्या रनटाइमनुसार समायोजित करू शकता.

## उदाहरणं 

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
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा गैरसमज होऊ शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेतहाच अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवाद करण्याचा सल्ला दिला जातो. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
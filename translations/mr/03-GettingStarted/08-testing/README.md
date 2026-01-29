## Testing and Debugging

आपला MCP सर्व्हर टेस्ट करण्यापूर्वी, उपलब्ध साधने आणि डिबगिंगसाठी सर्वोत्तम पद्धती समजून घेणे महत्त्वाचे आहे. प्रभावी टेस्टिंगमुळे आपला सर्व्हर अपेक्षेनुसार कार्य करतो याची खात्री होते आणि समस्या लवकर ओळखून सोडवता येतात. पुढील विभागात आपली MCP अंमलबजावणी तपासण्यासाठी शिफारस केलेल्या पद्धतींचा आढावा दिला आहे.

## Overview

हा धडा योग्य टेस्टिंग पद्धत कशी निवडायची आणि सर्वात प्रभावी टेस्टिंग साधन कोणते आहे हे समजावून सांगतो.

## Learning Objectives

या धड्याच्या शेवटी, आपण हे करू शकाल:

- टेस्टिंगसाठी विविध पद्धतींचे वर्णन करणे.
- आपला कोड प्रभावीपणे टेस्ट करण्यासाठी वेगवेगळ्या साधनांचा वापर करणे.

## Testing MCP Servers

MCP आपल्याला सर्व्हर टेस्ट आणि डिबग करण्यासाठी खालील साधने पुरवते:

- **MCP Inspector**: एक कमांड लाइन टूल जे CLI आणि व्हिज्युअल दोन्ही प्रकारे चालवता येते.
- **Manual testing**: curl सारखे टूल वापरून वेब विनंत्या चालवू शकता, पण HTTP चालवू शकणं कोणत्याही टूलने चालेल.
- **Unit testing**: आपल्याला आवडणाऱ्या टेस्टिंग फ्रेमवर्कचा वापर करून सर्व्हर आणि क्लायंटच्या फिचर्सची चाचणी करता येते.

### Using MCP Inspector

या टूलचा वापर आपण मागील धड्यांमध्ये पाहिला आहे, पण थोडक्यात याबद्दल बोलूया. हे Node.js मध्ये तयार केलेले टूल आहे आणि आपण `npx` कमांड वापरून ते चालवू शकता, जे टूल तात्पुरते डाउनलोड आणि इन्स्टॉल करेल आणि आपली विनंती पूर्ण झाल्यावर स्वतःला साफ करेल.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) आपल्याला मदत करतो:

- **सर्व्हर क्षमता शोधा**: उपलब्ध संसाधने, साधने आणि प्रॉम्प्ट्स आपोआप शोधा
- **टूल कार्यक्षमता तपासा**: वेगवेगळे पॅरामीटर्स वापरून रिअल-टाइम प्रतिसाद पहा
- **सर्व्हर मेटाडेटा पहा**: सर्व्हरची माहिती, स्कीमा आणि कॉन्फिगरेशन तपासा

टूल चालवण्याचा एक सामान्य प्रकार असा दिसतो:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

वरील कमांड MCP आणि त्याचा व्हिज्युअल इंटरफेस सुरू करते आणि आपल्या ब्राउझरमध्ये स्थानिक वेब इंटरफेस उघडते. येथे आपल्याला नोंदणीकृत MCP सर्व्हर्स, त्यांची उपलब्ध साधने, संसाधने आणि प्रॉम्प्ट्स दिसतील. हा इंटरफेस आपल्याला टूल कार्यक्षमता इंटरॅक्टिव्हली तपासण्याची, सर्व्हर मेटाडेटा पाहण्याची आणि रिअल-टाइम प्रतिसाद पाहण्याची सुविधा देतो, ज्यामुळे आपली MCP अंमलबजावणी तपासणे आणि डिबग करणे सोपे होते.

हे कसे दिसू शकते ते येथे आहे: ![Inspector](../../../../translated_images/mr/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

आपण हे टूल CLI मोडमध्ये देखील चालवू शकता, ज्यासाठी `--cli` अ‍ॅट्रिब्यूट जोडावे लागतो. खाली CLI मोडमध्ये टूल चालवण्याचा एक उदाहरण आहे, जे सर्व्हरवरील सर्व टूल्सची यादी दाखवते:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Manual Testing

सर्व्हर क्षमता तपासण्यासाठी inspector टूल चालवण्याशिवाय, HTTP वापरू शकणारा क्लायंट वापरण्याचा आणखी एक पर्याय आहे, जसे की curl.

curl वापरून आपण MCP सर्व्हर्स थेट HTTP विनंत्यांद्वारे टेस्ट करू शकता:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

वरील curl वापरातून दिसतं की, आपण POST विनंती वापरून टूल चालवता, ज्यामध्ये टूलचे नाव आणि त्याचे पॅरामीटर्स असलेला पेलोड असतो. आपल्याला ज्या पद्धतीने सोयीस्कर वाटेल ती वापरा. CLI टूल्स सामान्यतः जलद असतात आणि स्क्रिप्टिंगसाठी उपयुक्त असतात, जे CI/CD वातावरणात फायदेशीर ठरू शकते.

### Unit Testing

आपल्या टूल्स आणि संसाधनांसाठी युनिट टेस्ट तयार करा जेणेकरून ते अपेक्षेनुसार कार्य करतात याची खात्री करता येईल. खाली काही उदाहरणात्मक टेस्टिंग कोड दिला आहे.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

वरील कोड खालीलप्रमाणे कार्य करतो:

- pytest फ्रेमवर्कचा वापर करतो, ज्यामुळे आपण फंक्शन्स म्हणून टेस्ट तयार करू शकता आणि assert स्टेटमेंट वापरू शकता.
- दोन वेगवेगळ्या टूल्ससह MCP सर्व्हर तयार करतो.
- `assert` स्टेटमेंट वापरून काही अटी पूर्ण झाल्या आहेत का ते तपासतो.

[पूर्ण फाइल येथे पहा](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

वरील फाइलच्या आधारे, आपण आपला स्वतःचा सर्व्हर टेस्ट करू शकता आणि त्याच्या क्षमतांची योग्य निर्मिती झाली आहे का ते पाहू शकता.

सर्व प्रमुख SDKs मध्ये अशाच टेस्टिंग विभाग असतात, त्यामुळे आपण आपल्या निवडलेल्या रनटाइमनुसार ते समायोजित करू शकता.

## Samples 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Additional Resources

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## What's Next

- पुढे: [Deployment](../09-deployment/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
## परीक्षण और डिबगिंग

अपने MCP सर्वर का परीक्षण शुरू करने से पहले, उपलब्ध टूल्स और डिबगिंग के सर्वोत्तम तरीकों को समझना महत्वपूर्ण है। प्रभावी परीक्षण यह सुनिश्चित करता है कि आपका सर्वर अपेक्षित व्यवहार करता है और आपको जल्दी से समस्याओं की पहचान और समाधान करने में मदद करता है। निम्नलिखित अनुभाग में आपके MCP कार्यान्वयन को मान्य करने के लिए अनुशंसित दृष्टिकोण बताए गए हैं।

## अवलोकन

यह पाठ सही परीक्षण दृष्टिकोण चुनने और सबसे प्रभावी परीक्षण टूल के बारे में बताता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- परीक्षण के विभिन्न दृष्टिकोणों का वर्णन करने के लिए।
- अपने कोड का प्रभावी परीक्षण करने के लिए विभिन्न टूल्स का उपयोग करने के लिए।

## MCP सर्वरों का परीक्षण

MCP आपके सर्वरों का परीक्षण और डिबगिंग करने में मदद करने के लिए टूल्स प्रदान करता है:

- **MCP Inspector**: एक कमांड लाइन टूल जो CLI टूल और विज़ुअल टूल दोनों के रूप में चलाया जा सकता है।
- **मैनुअल परीक्षण**: आप curl जैसे टूल का उपयोग वेब अनुरोध चलाने के लिए कर सकते हैं, लेकिन कोई भी टूल जो HTTP चला सकता है, काम करेगा।
- **यूनिट परीक्षण**: आप अपने पसंदीदा परीक्षण फ्रेमवर्क का उपयोग करके सर्वर और क्लाइंट दोनों की विशेषताओं का परीक्षण कर सकते हैं।

### MCP Inspector का उपयोग

हमने इस टूल के उपयोग को पिछले पाठों में बताया है, लेकिन आइए इसे उच्च स्तर पर थोड़ा समझते हैं। यह Node.js में बनाया गया एक टूल है और आप इसे `npx` executable को कॉल करके उपयोग कर सकते हैं, जो टूल को अस्थायी रूप से डाउनलोड और इंस्टॉल करेगा और आपके अनुरोध के पूरा होने के बाद खुद को साफ़ कर देगा।

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) आपकी मदद करता है:

- **सर्वर क्षमताओं की खोज**: उपलब्ध संसाधनों, टूल्स, और प्रॉम्प्ट्स का स्वचालित पता लगाना
- **टूल निष्पादन का परीक्षण**: विभिन्न पैरामीटर आजमाएं और रियल-टाइम में प्रतिक्रियाएं देखें
- **सर्वर मेटाडेटा देखें**: सर्वर जानकारी, स्कीमाओं, और कॉन्फ़िगरेशन की जांच करें

टूल का एक सामान्य उपयोग इस प्रकार दिखता है:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

उपरोक्त कमांड एक MCP और इसका विज़ुअल इंटरफ़ेस शुरू करता है और आपके ब्राउज़र में एक स्थानीय वेब इंटरफ़ेस लॉन्च करता है। आप एक डैशबोर्ड देख सकते हैं जिसमें आपके पंजीकृत MCP सर्वर, उनके उपलब्ध टूल्स, संसाधन, और प्रॉम्प्ट्स दिखाए जाते हैं। यह इंटरफ़ेस आपको इंटरैक्टिव रूप से टूल निष्पादन का परीक्षण करने, सर्वर मेटाडेटा का निरीक्षण करने, और रियल-टाइम प्रतिक्रियाएं देखने की अनुमति देता है, जिससे आपके MCP सर्वर कार्यान्वयन को मान्य और डिबग करना आसान हो जाता है।

यह कुछ इस तरह दिख सकता है: ![Inspector](../../../../translated_images/hi/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

आप इस टूल को CLI मोड में भी चला सकते हैं, जिसमें आप `--cli` एट्रिब्यूट जोड़ते हैं। यहाँ "CLI" मोड में टूल चलाने का एक उदाहरण है जो सर्वर पर सभी टूल्स की सूची दिखाता है:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### मैनुअल परीक्षण

सर्वर क्षमताओं का परीक्षण करने के लिए इंस्पेक्टर टूल चलाने के अलावा, एक समान तरीका HTTP का उपयोग करने में सक्षम क्लाइंट चलाना है, जैसे कि curl।

curl के साथ, आप MCP सर्वरों का सीधे HTTP अनुरोधों के माध्यम से परीक्षण कर सकते हैं:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

जैसा कि आप ऊपर curl के उपयोग से देख सकते हैं, आप टूल के नाम और उसके पैरामीटर वाले पेलोड का उपयोग करके POST अनुरोध के माध्यम से टूल को कॉल करते हैं। वह तरीका चुनें जो आपके लिए सबसे उपयुक्त हो। CLI टूल आमतौर पर तेज़ होते हैं और इन्हें स्क्रिप्ट किया जा सकता है, जो CI/CD वातावरण में उपयोगी हो सकता है।

### यूनिट परीक्षण

अपने टूल्स और संसाधनों के लिए यूनिट टेस्ट बनाएं ताकि यह सुनिश्चित किया जा सके कि वे अपेक्षित रूप से काम कर रहे हैं। यहाँ कुछ उदाहरण परीक्षण कोड है।

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

उपरोक्त कोड निम्नलिखित करता है:

- pytest फ्रेमवर्क का उपयोग करता है जो आपको फ़ंक्शन के रूप में परीक्षण बनाने और assert स्टेटमेंट्स का उपयोग करने देता है।
- दो अलग-अलग टूल्स के साथ एक MCP सर्वर बनाता है।
- `assert` स्टेटमेंट का उपयोग करके यह जांचता है कि कुछ शर्तें पूरी हो रही हैं।

[यहाँ पूरा फ़ाइल देखें](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

उपरोक्त फ़ाइल के आधार पर, आप अपने सर्वर का परीक्षण कर सकते हैं ताकि यह सुनिश्चित किया जा सके कि क्षमताएं सही ढंग से बनाई गई हैं।

सभी प्रमुख SDK में इसी तरह के परीक्षण अनुभाग होते हैं, इसलिए आप अपने चुने हुए रनटाइम के अनुसार समायोजित कर सकते हैं।

## नमूने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## अतिरिक्त संसाधन

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## आगे क्या है

- अगला: [Deployment](../09-deployment/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
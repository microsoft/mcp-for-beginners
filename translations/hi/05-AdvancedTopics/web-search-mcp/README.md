# पाठ: वेब सर्च MCP सर्वर बनाना

यह अध्याय दिखाता है कि कैसे एक वास्तविक दुनिया का AI एजेंट बनाया जाए जो बाहरी APIs के साथ इंटीग्रेट हो, विभिन्न प्रकार के डेटा को संभाले, त्रुटियों का प्रबंधन करे, और कई टूल्स का समन्वय करे—वह भी प्रोडक्शन-तैयार फॉर्मेट में। आप देखेंगे:

- **प्रमाणीकरण की आवश्यकता वाले बाहरी APIs के साथ इंटीग्रेशन**
- **कई endpoints से विविध डेटा प्रकारों को संभालना**
- **मजबूत त्रुटि प्रबंधन और लॉगिंग रणनीतियाँ**
- **एक ही सर्वर में मल्टी-टूल समन्वय**

अंत तक, आपके पास उन पैटर्न्स और सर्वोत्तम प्रथाओं का व्यावहारिक अनुभव होगा जो उन्नत AI और LLM-संचालित एप्लिकेशन के लिए आवश्यक हैं।

## परिचय

इस पाठ में, आप सीखेंगे कि कैसे एक उन्नत MCP सर्वर और क्लाइंट बनाया जाए जो SerpAPI का उपयोग करके LLM क्षमताओं को रियल-टाइम वेब डेटा के साथ बढ़ाता है। यह एक महत्वपूर्ण कौशल है जो डायनामिक AI एजेंट विकसित करने के लिए आवश्यक है जो वेब से नवीनतम जानकारी प्राप्त कर सके।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- बाहरी APIs (जैसे SerpAPI) को सुरक्षित रूप से MCP सर्वर में इंटीग्रेट करना
- वेब, समाचार, उत्पाद खोज, और Q&A के लिए कई टूल्स लागू करना
- LLM के उपयोग के लिए संरचित डेटा को पार्स और फॉर्मेट करना
- त्रुटियों को संभालना और API रेट लिमिट्स का प्रभावी प्रबंधन करना
- स्वचालित और इंटरैक्टिव दोनों प्रकार के MCP क्लाइंट बनाना और परीक्षण करना

## वेब सर्च MCP सर्वर

यह अनुभाग वेब सर्च MCP सर्वर की आर्किटेक्चर और विशेषताओं का परिचय देता है। आप देखेंगे कि कैसे FastMCP और SerpAPI को मिलाकर LLM क्षमताओं को रियल-टाइम वेब डेटा के साथ बढ़ाया जाता है।

### अवलोकन

इस इम्प्लीमेंटेशन में चार टूल्स हैं जो MCP की क्षमता को दिखाते हैं कि वह विविध, बाहरी API-चालित कार्यों को सुरक्षित और कुशलतापूर्वक संभाल सकता है:

- **general_search**: व्यापक वेब परिणामों के लिए
- **news_search**: हाल की खबरों के लिए
- **product_search**: ई-कॉमर्स डेटा के लिए
- **qna**: प्रश्न-उत्तर स्निपेट्स के लिए

### विशेषताएँ
- **कोड उदाहरण**: Python के लिए भाषा-विशिष्ट कोड ब्लॉक्स शामिल हैं (और आसानी से अन्य भाषाओं में बढ़ाए जा सकते हैं) स्पष्टता के लिए कोड पिवट्स का उपयोग करते हुए

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

क्लाइंट चलाने से पहले, यह समझना उपयोगी है कि सर्वर क्या करता है। [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) फाइल MCP सर्वर को इम्प्लीमेंट करती है, जो वेब, समाचार, उत्पाद खोज, और Q&A के लिए टूल्स प्रदान करती है SerpAPI के साथ इंटीग्रेशन के माध्यम से। यह आने वाले अनुरोधों को संभालता है, API कॉल्स का प्रबंधन करता है, प्रतिक्रियाओं को पार्स करता है, और क्लाइंट को संरचित परिणाम लौटाता है।

आप पूरी इम्प्लीमेंटेशन [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) में देख सकते हैं।

यहाँ एक संक्षिप्त उदाहरण है कि सर्वर कैसे एक टूल को परिभाषित और रजिस्टर करता है:

### Python सर्वर

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **बाहरी API इंटीग्रेशन**: API कुंजियों और बाहरी अनुरोधों को सुरक्षित रूप से संभालने का प्रदर्शन
- **संरचित डेटा पार्सिंग**: API प्रतिक्रियाओं को LLM-अनुकूल प्रारूपों में बदलने का तरीका दिखाता है
- **त्रुटि प्रबंधन**: उपयुक्त लॉगिंग के साथ मजबूत त्रुटि प्रबंधन
- **इंटरैक्टिव क्लाइंट**: स्वचालित परीक्षणों और इंटरैक्टिव मोड दोनों को शामिल करता है
- **संदर्भ प्रबंधन**: अनुरोधों के लॉगिंग और ट्रैकिंग के लिए MCP Context का उपयोग करता है

## पूर्वापेक्षाएँ

शुरू करने से पहले, सुनिश्चित करें कि आपका वातावरण सही ढंग से सेटअप है। यह सुनिश्चित करेगा कि सभी निर्भरताएँ इंस्टॉल हों और आपके API कुंजी सही तरीके से कॉन्फ़िगर हों ताकि विकास और परीक्षण सहज हो।

- Python 3.8 या उससे ऊपर
- SerpAPI API Key (साइन अप करें [SerpAPI](https://serpapi.com/) पर - फ्री टियर उपलब्ध)

## स्थापना

शुरू करने के लिए, अपने वातावरण को सेटअप करने के लिए निम्न चरणों का पालन करें:

1. uv (सिफारिश की गई) या pip का उपयोग करके निर्भरताएँ इंस्टॉल करें:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. प्रोजेक्ट रूट में `.env` फाइल बनाएं और उसमें अपनी SerpAPI कुंजी डालें:

```
SERPAPI_KEY=your_serpapi_key_here
```

## उपयोग

वेब सर्च MCP सर्वर मुख्य घटक है जो SerpAPI के साथ इंटीग्रेट होकर वेब, समाचार, उत्पाद खोज, और Q&A के लिए टूल्स प्रदान करता है। यह आने वाले अनुरोधों को संभालता है, API कॉल्स का प्रबंधन करता है, प्रतिक्रियाओं को पार्स करता है, और क्लाइंट को संरचित परिणाम लौटाता है।

आप पूरी इम्प्लीमेंटेशन [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) में देख सकते हैं।

### सर्वर चलाना

MCP सर्वर शुरू करने के लिए, निम्न कमांड का उपयोग करें:

```bash
python server.py
```

सर्वर stdio-आधारित MCP सर्वर के रूप में चलेगा जिसे क्लाइंट सीधे कनेक्ट कर सकता है।

### क्लाइंट मोड्स

क्लाइंट (`client.py`) MCP सर्वर के साथ इंटरैक्ट करने के लिए दो मोड्स सपोर्ट करता है:

- **सामान्य मोड**: स्वचालित परीक्षण चलाता है जो सभी टूल्स का उपयोग करता है और उनकी प्रतिक्रियाओं को सत्यापित करता है। यह जल्दी से जांचने के लिए उपयोगी है कि सर्वर और टूल्स अपेक्षित रूप से काम कर रहे हैं।
- **इंटरैक्टिव मोड**: एक मेनू-आधारित इंटरफ़ेस शुरू करता है जहाँ आप मैन्युअली टूल्स चुन सकते हैं, कस्टम क्वेरी दर्ज कर सकते हैं, और परिणाम वास्तविक समय में देख सकते हैं। यह सर्वर की क्षमताओं का पता लगाने और विभिन्न इनपुट के साथ प्रयोग करने के लिए आदर्श है।

आप पूरी इम्प्लीमेंटेशन [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) में देख सकते हैं।

### क्लाइंट चलाना

स्वचालित परीक्षण चलाने के लिए (यह स्वचालित रूप से सर्वर भी शुरू करेगा):

```bash
python client.py
```

या इंटरैक्टिव मोड में चलाने के लिए:

```bash
python client.py --interactive
```

### विभिन्न तरीकों से परीक्षण

आपकी आवश्यकताओं और वर्कफ़्लो के अनुसार, सर्वर द्वारा प्रदान किए गए टूल्स के साथ परीक्षण और इंटरैक्ट करने के कई तरीके हैं।

#### MCP Python SDK के साथ कस्टम टेस्ट स्क्रिप्ट लिखना
आप MCP Python SDK का उपयोग करके अपनी खुद की टेस्ट स्क्रिप्ट भी बना सकते हैं:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

इस संदर्भ में, "टेस्ट स्क्रिप्ट" का मतलब है एक कस्टम Python प्रोग्राम जो आप MCP सर्वर के क्लाइंट के रूप में लिखते हैं। यह औपचारिक यूनिट टेस्ट नहीं है, बल्कि यह स्क्रिप्ट आपको प्रोग्रामेटिक रूप से सर्वर से कनेक्ट करने, उसके किसी भी टूल को अपनी पसंद के पैरामीटर के साथ कॉल करने, और परिणामों का निरीक्षण करने देती है। यह तरीका उपयोगी है:

- टूल कॉल्स का प्रोटोटाइप और प्रयोग करने के लिए
- यह जांचने के लिए कि सर्वर विभिन्न इनपुट्स पर कैसे प्रतिक्रिया देता है
- टूल्स के बार-बार उपयोग को स्वचालित करने के लिए
- MCP सर्वर के ऊपर अपने वर्कफ़्लोज़ या इंटीग्रेशन बनाने के लिए

आप टेस्ट स्क्रिप्ट्स का उपयोग नए क्वेरीज़ जल्दी से आज़माने, टूल व्यवहार को डिबग करने, या अधिक उन्नत ऑटोमेशन के लिए शुरुआती बिंदु के रूप में कर सकते हैं। नीचे MCP Python SDK का उपयोग करके ऐसी स्क्रिप्ट बनाने का उदाहरण दिया गया है:

## टूल विवरण

आप सर्वर द्वारा प्रदान किए गए निम्न टूल्स का उपयोग विभिन्न प्रकार की खोजों और क्वेरीज़ के लिए कर सकते हैं। प्रत्येक टूल के पैरामीटर और उदाहरण उपयोग नीचे दिया गया है।

यह अनुभाग उपलब्ध प्रत्येक टूल और उनके पैरामीटर के बारे में विवरण प्रदान करता है।

### general_search

सामान्य वेब खोज करता है और फॉर्मेटेड परिणाम लौटाता है।

**इस टूल को कैसे कॉल करें:**

आप MCP Python SDK का उपयोग करके अपनी स्क्रिप्ट से `general_search` कॉल कर सकते हैं, या इंटरैक्टिवली Inspector या इंटरैक्टिव क्लाइंट मोड का उपयोग कर सकते हैं। यहाँ SDK का उपयोग करते हुए कोड उदाहरण है:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

वैकल्पिक रूप से, इंटरैक्टिव मोड में मेनू से `general_search` चुनें और जब पूछा जाए तो अपनी क्वेरी दर्ज करें।

**पैरामीटर:**
- `query` (string): खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

किसी क्वेरी से संबंधित हाल की समाचार लेख खोजता है।

**इस टूल को कैसे कॉल करें:**

आप MCP Python SDK का उपयोग करके अपनी स्क्रिप्ट से `news_search` कॉल कर सकते हैं, या इंटरैक्टिवली Inspector या इंटरैक्टिव क्लाइंट मोड का उपयोग कर सकते हैं। यहाँ SDK का उपयोग करते हुए कोड उदाहरण है:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

वैकल्पिक रूप से, इंटरैक्टिव मोड में मेनू से `news_search` चुनें और जब पूछा जाए तो अपनी क्वेरी दर्ज करें।

**पैरामीटर:**
- `query` (string): खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

किसी क्वेरी से मेल खाने वाले उत्पाद खोजता है।

**इस टूल को कैसे कॉल करें:**

आप MCP Python SDK का उपयोग करके अपनी स्क्रिप्ट से `product_search` कॉल कर सकते हैं, या इंटरैक्टिवली Inspector या इंटरैक्टिव क्लाइंट मोड का उपयोग कर सकते हैं। यहाँ SDK का उपयोग करते हुए कोड उदाहरण है:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

वैकल्पिक रूप से, इंटरैक्टिव मोड में मेनू से `product_search` चुनें और जब पूछा जाए तो अपनी क्वेरी दर्ज करें।

**पैरामीटर:**
- `query` (string): उत्पाद खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

खोज इंजनों से सीधे प्रश्नों के उत्तर प्राप्त करता है।

**इस टूल को कैसे कॉल करें:**

आप MCP Python SDK का उपयोग करके अपनी स्क्रिप्ट से `qna` कॉल कर सकते हैं, या इंटरैक्टिवली Inspector या इंटरैक्टिव क्लाइंट मोड का उपयोग कर सकते हैं। यहाँ SDK का उपयोग करते हुए कोड उदाहरण है:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

वैकल्पिक रूप से, इंटरैक्टिव मोड में मेनू से `qna` चुनें और जब पूछा जाए तो अपना प्रश्न दर्ज करें।

**पैरामीटर:**
- `question` (string): उत्तर खोजने के लिए प्रश्न

**उदाहरण अनुरोध:**

```json
{
  "question": "what is artificial intelligence"
}
```

## कोड विवरण

यह अनुभाग सर्वर और क्लाइंट इम्प्लीमेंटेशन के लिए कोड स्निपेट्स और संदर्भ प्रदान करता है।

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

पूरी इम्प्लीमेंटेशन के लिए [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) और [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) देखें।

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## इस पाठ में उन्नत अवधारणाएँ

बिल्डिंग शुरू करने से पहले, यहाँ कुछ महत्वपूर्ण उन्नत अवधारणाएँ हैं जो इस अध्याय में बार-बार आएंगी। इन्हें समझना आपको बेहतर तरीके से साथ चलने में मदद करेगा, भले ही आप इनके लिए नए हों:

- **मल्टी-टूल समन्वय**: इसका मतलब है कि एक ही MCP सर्वर में कई अलग-अलग टूल्स (जैसे वेब सर्च, समाचार सर्च, उत्पाद सर्च, और Q&A) चलाना। यह आपके सर्वर को विभिन्न कार्यों को संभालने की अनुमति देता है, न कि केवल एक को।
- **API रेट लिमिट हैंडलिंग**: कई बाहरी APIs (जैसे SerpAPI) सीमित करते हैं कि आप एक निश्चित समय में कितने अनुरोध कर सकते हैं। अच्छा कोड इन सीमाओं की जांच करता है और उन्हें सही ढंग से संभालता है, ताकि आपकी ऐप टूटे नहीं अगर आप सीमा पार कर जाएं।
- **संरचित डेटा पार्सिंग**: API प्रतिक्रियाएँ अक्सर जटिल और नेस्टेड होती हैं। यह अवधारणा उन प्रतिक्रियाओं को साफ़, उपयोग में आसान प्रारूपों में बदलने के बारे में है जो LLMs या अन्य प्रोग्रामों के लिए अनुकूल हों।
- **त्रुटि पुनर्प्राप्ति**: कभी-कभी चीजें गलत हो जाती हैं—शायद नेटवर्क फेल हो, या API वह न लौटाए जिसकी आप उम्मीद कर रहे थे। त्रुटि पुनर्प्राप्ति का मतलब है कि आपका कोड इन समस्याओं को संभाल सकता है और उपयोगी प्रतिक्रिया दे सकता है, बजाय क्रैश होने के।
- **पैरामीटर सत्यापन**: यह सुनिश्चित करने के बारे में है कि आपके टूल्स को दिए गए सभी इनपुट सही और सुरक्षित हैं। इसमें डिफ़ॉल्ट मान सेट करना और प्रकारों की जांच करना शामिल है, जो बग्स और भ्रम को रोकने में मदद करता है।

यह अनुभाग आपको वेब सर्च MCP सर्वर के साथ काम करते समय आम समस्याओं का निदान और समाधान करने में मदद करेगा। यदि आप त्रुटियों या अप्रत्याशित व्यवहार का सामना करते हैं, तो यह ट्रबलशूटिंग अनुभाग सबसे सामान्य समस्याओं के समाधान प्रदान करता है। आगे सहायता मांगने से पहले इन सुझावों की समीक्षा करें—अक्सर ये समस्याओं को जल्दी हल कर देते हैं।

## समस्या निवारण

वेब सर्च MCP सर्वर के साथ काम करते समय, कभी-कभी आपको समस्याओं का सामना करना पड़ सकता है—यह बाहरी APIs और नए टूल्स के साथ विकास करते समय सामान्य है। यह अनुभाग सबसे सामान्य समस्याओं के व्यावहारिक समाधान प्रदान करता है, ताकि आप जल्दी से फिर से काम पर लौट सकें। यदि आपको कोई त्रुटि मिलती है, तो यहाँ से शुरू करें: नीचे दिए गए सुझाव उन समस्याओं को संबोधित करते हैं जिनका अधिकांश उपयोगकर्ता सामना करते हैं और अक्सर आपकी समस्या बिना अतिरिक्त मदद के हल कर सकते हैं।

### सामान्य समस्याएँ

नीचे कुछ सबसे आम समस्याएँ दी गई हैं जिनका उपयोगकर्ता सामना करते हैं, साथ ही स्पष्ट व्याख्याएँ और उन्हें हल करने के चरण:

1. **.env फाइल में SERPAPI_KEY गायब है**
   - यदि आपको त्रुटि `SERPAPI_KEY environment variable not found` दिखती है, तो इसका मतलब है कि आपका एप्लिकेशन SerpAPI तक पहुँचने के लिए आवश्यक API कुंजी नहीं ढूंढ पा रहा है। इसे ठीक करने के लिए, अपने प्रोजेक्ट रूट में `.env` नामक फाइल बनाएं (यदि पहले से नहीं है) और उसमें एक लाइन जोड़ें जैसे `SERPAPI_KEY=your_serpapi_key_here`। सुनिश्चित करें कि `your_serpapi_key_here` को अपनी वास्तविक SerpAPI वेबसाइट से मिली कुंजी से बदलें।

2. **मॉड्यूल न मिलने की त्रुटियाँ**
   - `ModuleNotFoundError: No module named 'httpx'` जैसी त्रुटियाँ इंगित करती हैं कि आवश्यक Python पैकेज गायब है। यह आमतौर पर तब होता है जब आपने सभी निर्भरताएँ इंस्टॉल नहीं की हैं। इसे ठीक करने के लिए, टर्मिनल में `pip install -r requirements.txt` चलाएं ताकि आपकी परियोजना को आवश्यक सभी पैकेज मिल जाएं।

3. **कनेक्शन समस्याएँ**
   - यदि आपको `Error during client execution` जैसी त्रुटि मिलती है, तो इसका मतलब अक्सर होता है कि क्लाइंट सर्वर से कनेक्ट नहीं कर पा रहा है, या सर्वर अपेक्षित रूप से नहीं चल रहा है। सुनिश्चित करें कि क्लाइंट और सर्वर दोनों संगत संस्करण हैं, और `server.py` सही डायरेक्टरी में मौजूद है और चल रहा है। सर्वर और क्लाइंट दोनों को पुनः शुरू करना भी मदद कर सकता है।

4. **SerpAPI त्रुटियाँ**
   - `Search API returned error status: 401` देखने का मतलब है कि आपकी SerpAPI कुंजी गायब, गलत, या समाप्त हो चुकी है। अपने SerpAPI डैशबोर्ड पर जाएं, अपनी कुंजी सत्यापित करें, और यदि आवश्यक हो तो अपनी `.env` फाइल अपडेट करें। यदि आपकी कुंजी सही है लेकिन फिर भी यह त्रुटि आ रही है, तो जांचें कि आपका फ्री टियर कोटा समाप्त तो नहीं हो गया।

### डिबग मोड

डिफ़ॉल्ट रूप से, ऐप केवल महत्वपूर्ण जानकारी लॉग करता है। यदि आप यह देखना चाहते हैं कि क्या हो रहा है (जैसे जटिल समस्याओं का निदान करने के लिए), तो आप DEBUG मोड सक्षम कर सकते हैं। यह आपको ऐप के प्रत्येक चरण के बारे में बहुत अधिक जानकारी दिखाएगा।

**उदाहरण: सामान्य आउटपुट**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**उदाहरण: DEBUG आउटपुट**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

ध्यान दें कि DEBUG मोड HTTP अनुरोधों, प्रतिक्रियाओं, और अन्य आंतरिक विवरणों के अतिरिक्त लाइनों को शामिल करता है। यह
DEBUG मोड सक्षम करने के लिए, अपने `client.py` या `server.py` की शुरुआत में लॉगिंग स्तर को DEBUG पर सेट करें:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## आगे क्या है

- [5.10 रियल टाइम स्ट्रीमिंग](../mcp-realtimestreaming/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
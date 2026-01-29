# धडा: वेब सर्च MCP सर्व्हर तयार करणे

हा अध्याय तुम्हाला दाखवतो की कसे एक वास्तविक जगातील AI एजंट तयार करायचा जो बाह्य API शी एकत्रित होतो, विविध प्रकारच्या डेटाचा हाताळणी करतो, त्रुटी व्यवस्थापित करतो आणि अनेक साधने एकत्र चालवतो—तेही उत्पादनासाठी तयार स्वरूपात. तुम्हाला दिसेल:

- **प्रमाणीकरण आवश्यक असलेल्या बाह्य API शी एकत्रीकरण**
- **विविध प्रकारच्या डेटाचा अनेक स्रोतांकडून हाताळणी**
- **मजबूत त्रुटी हाताळणी आणि लॉगिंग धोरणे**
- **एकाच सर्व्हरमध्ये बहु-साधन समन्वय**

शेवटी, तुम्हाला प्रगत AI आणि LLM-आधारित अनुप्रयोगांसाठी आवश्यक असलेल्या पॅटर्न्स आणि सर्वोत्तम पद्धतींचा व्यावहारिक अनुभव मिळेल.

## परिचय

या धड्यात, तुम्ही शिकाल की कसे एक प्रगत MCP सर्व्हर आणि क्लायंट तयार करायचा जो SerpAPI वापरून LLM क्षमतांना रिअल-टाइम वेब डेटाने वाढवतो. ही एक महत्त्वाची कौशल्ये आहे जी गतिशील AI एजंट विकसित करण्यासाठी आवश्यक आहे जे वेबवरून अद्ययावत माहिती मिळवू शकतात.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- बाह्य API (जसे की SerpAPI) सुरक्षितपणे MCP सर्व्हरमध्ये एकत्रित करणे
- वेब, बातम्या, उत्पादन शोध आणि प्रश्नोत्तरे यासाठी अनेक साधने अंमलात आणणे
- LLM साठी संरचित डेटा पार्स आणि स्वरूपित करणे
- त्रुटी हाताळणी करणे आणि API दर मर्यादा प्रभावीपणे व्यवस्थापित करणे
- स्वयंचलित आणि संवादात्मक दोन्ही प्रकारचे MCP क्लायंट तयार करणे आणि चाचणी करणे

## वेब सर्च MCP सर्व्हर

हा विभाग वेब सर्च MCP सर्व्हरची आर्किटेक्चर आणि वैशिष्ट्ये सादर करतो. तुम्हाला दिसेल की FastMCP आणि SerpAPI कसे एकत्र वापरले जातात जेणेकरून LLM क्षमतांना रिअल-टाइम वेब डेटाने वाढवता येईल.

### आढावा

या अंमलबजावणीत चार साधने आहेत जी MCP ची क्षमता दर्शवतात की ती विविध, बाह्य API-आधारित कामे सुरक्षित आणि कार्यक्षमपणे कशी हाताळते:

- **general_search**: व्यापक वेब निकालांसाठी
- **news_search**: अलीकडील बातम्यांसाठी
- **product_search**: ई-कॉमर्स डेटासाठी
- **qna**: प्रश्नोत्तरे मिळवण्यासाठी

### वैशिष्ट्ये
- **कोड उदाहरणे**: Python साठी भाषा-विशिष्ट कोड ब्लॉक्स (आणि इतर भाषांसाठी सहज विस्तारयोग्य) स्पष्टतेसाठी कोड पिव्हट्ससह

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

क्लायंट चालवण्यापूर्वी, सर्व्हर काय करतो हे समजून घेणे उपयुक्त आहे. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) फाईल MCP सर्व्हरची अंमलबजावणी करते, जी वेब, बातम्या, उत्पादन शोध आणि प्रश्नोत्तरे यासाठी साधने SerpAPI शी एकत्र करून उपलब्ध करून देते. हे येणाऱ्या विनंत्या हाताळते, API कॉल्स व्यवस्थापित करते, प्रतिसाद पार्स करते आणि क्लायंटला संरचित निकाल परत करते.

तुम्ही [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) मधील पूर्ण अंमलबजावणी पाहू शकता.

खाली एक संक्षिप्त उदाहरण आहे की सर्व्हर कसा साधन परिभाषित आणि नोंदणी करतो:

### Python सर्व्हर

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

- **बाह्य API एकत्रीकरण**: API की आणि बाह्य विनंत्यांचे सुरक्षित हाताळणी दाखवते
- **संरचित डेटा पार्सिंग**: API प्रतिसाद LLM-योग्य स्वरूपात कसे रूपांतरित करायचे हे दाखवते
- **त्रुटी हाताळणी**: योग्य लॉगिंगसह मजबूत त्रुटी हाताळणी
- **संवादात्मक क्लायंट**: स्वयंचलित चाचण्या आणि संवादात्मक मोड दोन्हीचा समावेश
- **संदर्भ व्यवस्थापन**: विनंत्यांचे लॉगिंग आणि ट्रॅकिंगसाठी MCP Context वापर

## पूर्वअट

सुरू करण्यापूर्वी, तुमचे वातावरण योग्यरित्या सेटअप केले आहे याची खात्री करा. यामुळे सर्व अवलंबित्वे स्थापित होतील आणि तुमच्या API की योग्यरित्या कॉन्फिगर होतील जेणेकरून विकास आणि चाचणी सुरळीत होईल.

- Python 3.8 किंवा त्याहून वर
- SerpAPI API की (नोंदणी करा [SerpAPI](https://serpapi.com/) येथे - मोफत टियर उपलब्ध)

## स्थापना

सुरू करण्यासाठी, तुमचे वातावरण सेटअप करण्यासाठी खालील पायऱ्या फॉलो करा:

1. अवलंबित्वे uv (शिफारस केलेले) किंवा pip वापरून इंस्टॉल करा:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. प्रोजेक्ट रूटमध्ये `.env` फाईल तयार करा आणि त्यात तुमची SerpAPI की जोडा:

```
SERPAPI_KEY=your_serpapi_key_here
```

## वापर

वेब सर्च MCP सर्व्हर हा मुख्य घटक आहे जो वेब, बातम्या, उत्पादन शोध आणि प्रश्नोत्तरे यासाठी साधने SerpAPI शी एकत्र करून उपलब्ध करून देतो. तो येणाऱ्या विनंत्या हाताळतो, API कॉल्स व्यवस्थापित करतो, प्रतिसाद पार्स करतो आणि क्लायंटला संरचित निकाल परत करतो.

तुम्ही [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) मधील पूर्ण अंमलबजावणी पाहू शकता.

### सर्व्हर चालवणे

MCP सर्व्हर सुरू करण्यासाठी खालील कमांड वापरा:

```bash
python server.py
```

सर्व्हर stdio-आधारित MCP सर्व्हर म्हणून चालेल ज्याला क्लायंट थेट कनेक्ट होऊ शकतो.

### क्लायंट मोड्स

क्लायंट (`client.py`) MCP सर्व्हरशी संवाद साधण्यासाठी दोन मोड्सला समर्थन देतो:

- **सामान्य मोड**: सर्व साधने वापरून स्वयंचलित चाचण्या चालवतो आणि त्यांचे प्रतिसाद तपासतो. हे लवकर तपासणीसाठी उपयुक्त आहे की सर्व्हर आणि साधने अपेक्षेप्रमाणे काम करत आहेत की नाही.
- **संवादात्मक मोड**: मेनू-आधारित इंटरफेस सुरू करतो जिथे तुम्ही हाताने साधने निवडू शकता, कस्टम क्वेरी टाकू शकता आणि निकाल रिअल-टाइममध्ये पाहू शकता. हे सर्व्हरच्या क्षमतांचा शोध घेण्यासाठी आणि वेगवेगळ्या इनपुटसह प्रयोग करण्यासाठी उत्तम आहे.

तुम्ही [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) मधील पूर्ण अंमलबजावणी पाहू शकता.

### क्लायंट चालवणे

स्वयंचलित चाचण्या चालवण्यासाठी (हे आपोआप सर्व्हर सुरू करेल):

```bash
python client.py
```

किंवा संवादात्मक मोडमध्ये चालवा:

```bash
python client.py --interactive
```

### वेगवेगळ्या पद्धतींनी चाचणी करणे

तुमच्या गरजा आणि कार्यप्रवाहानुसार, सर्व्हरने दिलेली साधने तपासण्यासाठी आणि त्यांच्याशी संवाद साधण्यासाठी अनेक मार्ग आहेत.

#### MCP Python SDK वापरून कस्टम चाचणी स्क्रिप्ट लिहिणे
तुम्ही MCP Python SDK वापरून स्वतःच्या चाचणी स्क्रिप्ट्स देखील तयार करू शकता:

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

या संदर्भात, "चाचणी स्क्रिप्ट" म्हणजे तुम्ही लिहिलेला एक कस्टम Python प्रोग्राम जो MCP सर्व्हरसाठी क्लायंट म्हणून काम करतो. हा औपचारिक युनिट टेस्ट नसून, हा स्क्रिप्ट तुम्हाला प्रोग्रामॅटिकली सर्व्हरशी कनेक्ट होण्याची, त्याच्या कोणत्याही साधनांना तुमच्या निवडलेल्या पॅरामीटर्ससह कॉल करण्याची आणि निकाल तपासण्याची परवानगी देतो. हा दृष्टिकोन उपयुक्त आहे:

- साधन कॉल्सचे प्रोटोटायपिंग आणि प्रयोग करण्यासाठी
- सर्व्हर वेगवेगळ्या इनपुटवर कसा प्रतिसाद देतो हे पडताळण्यासाठी
- पुनरावृत्ती होणाऱ्या साधन कॉल्सचे स्वयंचलन करण्यासाठी
- MCP सर्व्हरवर तुमचे स्वतःचे कार्यप्रवाह किंवा एकत्रीकरण तयार करण्यासाठी

तुम्ही चाचणी स्क्रिप्ट्स वापरून नवीन क्वेरीज पटकन तपासू शकता, साधनांच्या वर्तनात बग शोधू शकता किंवा प्रगत स्वयंचलनासाठी सुरुवात करू शकता. खाली MCP Python SDK वापरून अशा स्क्रिप्ट तयार करण्याचे उदाहरण दिले आहे:

## साधनांचे वर्णन

तुम्ही खालील साधने वापरून वेगवेगळ्या प्रकारच्या शोध आणि क्वेरी करू शकता. प्रत्येक साधन खाली त्याचे पॅरामीटर्स आणि उदाहरण वापरासह वर्णन केले आहे.

हा विभाग प्रत्येक उपलब्ध साधन आणि त्यांचे पॅरामीटर्स याबाबत तपशीलवार माहिती देतो.

### general_search

सामान्य वेब शोध करतो आणि स्वरूपित निकाल परत करतो.

**हे साधन कसे कॉल करावे:**

तुम्ही `general_search` तुमच्या स्वतःच्या स्क्रिप्टमधून MCP Python SDK वापरून कॉल करू शकता, किंवा Inspector किंवा संवादात्मक क्लायंट मोड वापरून संवादात्मकपणे कॉल करू शकता. SDK वापरून कोड उदाहरण खाली दिले आहे:

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

पर्यायीपणे, संवादात्मक मोडमध्ये मेनूमधून `general_search` निवडा आणि विचारले गेलेले क्वेरी टाका.

**पॅरामीटर्स:**
- `query` (string): शोध क्वेरी

**उदाहरण विनंती:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

क्वेरीशी संबंधित अलीकडील बातम्या शोधतो.

**हे साधन कसे कॉल करावे:**

तुम्ही `news_search` तुमच्या स्वतःच्या स्क्रिप्टमधून MCP Python SDK वापरून कॉल करू शकता, किंवा Inspector किंवा संवादात्मक क्लायंट मोड वापरून संवादात्मकपणे कॉल करू शकता. SDK वापरून कोड उदाहरण खाली दिले आहे:

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

पर्यायीपणे, संवादात्मक मोडमध्ये मेनूमधून `news_search` निवडा आणि विचारले गेलेले क्वेरी टाका.

**पॅरामीटर्स:**
- `query` (string): शोध क्वेरी

**उदाहरण विनंती:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

क्वेरीशी जुळणारी उत्पादने शोधतो.

**हे साधन कसे कॉल करावे:**

तुम्ही `product_search` तुमच्या स्वतःच्या स्क्रिप्टमधून MCP Python SDK वापरून कॉल करू शकता, किंवा Inspector किंवा संवादात्मक क्लायंट मोड वापरून संवादात्मकपणे कॉल करू शकता. SDK वापरून कोड उदाहरण खाली दिले आहे:

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

पर्यायीपणे, संवादात्मक मोडमध्ये मेनूमधून `product_search` निवडा आणि विचारले गेलेले क्वेरी टाका.

**पॅरामीटर्स:**
- `query` (string): उत्पादन शोध क्वेरी

**उदाहरण विनंती:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

शोध इंजिनमधून प्रश्नांची थेट उत्तरे मिळवतो.

**हे साधन कसे कॉल करावे:**

तुम्ही `qna` तुमच्या स्वतःच्या स्क्रिप्टमधून MCP Python SDK वापरून कॉल करू शकता, किंवा Inspector किंवा संवादात्मक क्लायंट मोड वापरून संवादात्मकपणे कॉल करू शकता. SDK वापरून कोड उदाहरण खाली दिले आहे:

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

पर्यायीपणे, संवादात्मक मोडमध्ये मेनूमधून `qna` निवडा आणि विचारले गेलेले प्रश्न टाका.

**पॅरामीटर्स:**
- `question` (string): उत्तर शोधायचा प्रश्न

**उदाहरण विनंती:**

```json
{
  "question": "what is artificial intelligence"
}
```

## कोड तपशील

हा विभाग सर्व्हर आणि क्लायंट अंमलबजावणीसाठी कोड स्निपेट्स आणि संदर्भ पुरवतो.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

पूर्ण अंमलबजावणीसाठी [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) आणि [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) पहा.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## या धड्यातील प्रगत संकल्पना

तुम्ही तयार करायला सुरुवात करण्यापूर्वी, या अध्यायात वारंवार येणाऱ्या काही महत्त्वाच्या प्रगत संकल्पना येथे आहेत. त्यांना समजून घेणे तुम्हाला सोपं जाईल, अगदी तुम्ही नवशिक्या असलात तरी:

- **बहु-साधन समन्वय**: याचा अर्थ एकाच MCP सर्व्हरमध्ये वेगवेगळ्या साधनांना (जसे वेब सर्च, बातम्या सर्च, उत्पादन सर्च, आणि प्रश्नोत्तरे) चालवणे. यामुळे तुमचा सर्व्हर विविध कामे हाताळू शकतो, फक्त एकच नाही.
- **API दर मर्यादा हाताळणी**: अनेक बाह्य API (जसे SerpAPI) ठराविक वेळेत किती विनंत्या करता येतील यावर मर्यादा घालतात. चांगला कोड या मर्यादांची तपासणी करतो आणि त्यांना योग्यरित्या हाताळतो, जेणेकरून तुमचा अॅप मर्यादा ओलांडल्यावरही क्रॅश होणार नाही.
- **संरचित डेटा पार्सिंग**: API प्रतिसाद अनेकदा गुंतागुंतीचे आणि नेस्टेड असतात. ही संकल्पना म्हणजे त्या प्रतिसादांना स्वच्छ, वापरण्यास सोप्या स्वरूपात रूपांतरित करणे जे LLM किंवा इतर प्रोग्रामसाठी अनुकूल असते.
- **त्रुटी पुनर्प्राप्ती**: कधी कधी काहीतरी चुकते—कदाचित नेटवर्क फेल होते, किंवा API अपेक्षित प्रतिसाद देत नाही. त्रुटी पुनर्प्राप्ती म्हणजे तुमचा कोड अशा समस्या हाताळू शकतो आणि उपयुक्त अभिप्राय देतो, क्रॅश न होता.
- **पॅरामीटर वैधता तपासणी**: याचा अर्थ तुमच्या साधनांमध्ये दिलेले सर्व इनपुट योग्य आणि सुरक्षित आहेत का हे तपासणे. यात डीफॉल्ट मूल्ये सेट करणे आणि प्रकार योग्य आहेत याची खात्री करणे यांचा समावेश होतो, ज्यामुळे बग्स आणि गोंधळ टाळता येतो.

हा विभाग तुम्हाला वेब सर्च MCP सर्व्हरशी काम करताना येणाऱ्या सामान्य समस्या ओळखण्यात आणि सोडवण्यात मदत करेल. जर तुम्हाला त्रुटी किंवा अनपेक्षित वर्तन दिसले तर या समस्या निवारण विभागातील सूचना पहा—हे अनेकदा समस्या पटकन सोडवतात.

## समस्या निवारण

वेब सर्च MCP सर्व्हरशी काम करताना कधी कधी समस्या येऊ शकतात—बाह्य API आणि नवीन साधने वापरताना हे सामान्य आहे. हा विभाग सर्वात सामान्य समस्या आणि त्यांचे व्यावहारिक उपाय देतो, जेणेकरून तुम्ही लवकर मार्गावर येऊ शकता. त्रुटी आल्यास, येथे सुरुवात करा: खालील टिप्स बहुतेक वापरकर्त्यांना येणाऱ्या समस्या सोडवतात आणि अतिरिक्त मदत न घेता तुमची समस्या सुटू शकते.

### सामान्य समस्या

खाली काही सर्वात वारंवार येणाऱ्या समस्या आणि त्यांचे स्पष्ट स्पष्टीकरण व सोडवण्याचे पावले दिली आहेत:

1. **.env फाईलमध्ये SERPAPI_KEY नाही**
   - जर तुम्हाला `SERPAPI_KEY environment variable not found` अशी त्रुटी दिसली, तर याचा अर्थ तुमच्या अॅप्लिकेशनला SerpAPI वापरण्यासाठी आवश्यक API की सापडत नाही. हे दुरुस्त करण्यासाठी, प्रोजेक्ट रूटमध्ये `.env` नावाची फाईल तयार करा (जर आधी नसेल तर) आणि त्यात `SERPAPI_KEY=तुमची_serpapi_key_इथे` अशी ओळ जोडा. `तुमची_serpapi_key_इथे` या जागी तुमची खऱ्या SerpAPI की टाका.

2. **मॉड्यूल सापडले नाही त्रुटी**
   - `ModuleNotFoundError: No module named 'httpx'` सारख्या त्रुटी सूचित करतात की आवश्यक Python पॅकेज इंस्टॉल केलेले नाही. हे सहसा तेव्हा होते जेव्हा तुम्ही सर्व अवलंबित्वे इंस्टॉल केलेली नाहीत. हे दुरुस्त करण्यासाठी, टर्मिनलमध्ये `pip install -r requirements.txt` चालवा जेणेकरून प्रोजेक्टसाठी आवश्यक सर्व पॅकेजेस इंस्टॉल होतील.

3. **कनेक्शन समस्या**
   - `Error during client execution` सारखी त्रुटी येणे म्हणजे क्लायंट सर्व्हरशी कनेक्ट होऊ शकत नाही किंवा सर्व्हर अपेक्षेप्रमाणे चालू नाही. खात्री करा की क्लायंट आणि सर्व्हर दोन्ही सुसंग
DEBUG मोड सक्षम करण्यासाठी, आपल्या `client.py` किंवा `server.py` च्या वरच्या भागात लॉगिंग लेव्हल DEBUG वर सेट करा:

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

## पुढे काय

- [5.10 रिअल टाइम स्ट्रीमिंग](../mcp-realtimestreaming/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
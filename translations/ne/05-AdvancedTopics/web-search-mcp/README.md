# पाठ: वेब सर्च MCP सर्भर बनाउने

यस अध्यायले देखाउँछ कसरी वास्तविक संसारको AI एजेन्ट बनाउने जसले बाह्य API हरूसँग एकीकृत हुन्छ, विभिन्न प्रकारका डाटा ह्यान्डल गर्छ, त्रुटिहरू व्यवस्थापन गर्छ, र धेरै उपकरणहरूलाई समन्वय गर्छ—सबै उत्पादन-तयार ढाँचामा। तपाईंले देख्नुहुनेछ:

- **प्रमाणीकरण आवश्यक पर्ने बाह्य API हरूसँग एकीकरण**
- **धेरै एन्डपोइन्टबाट विभिन्न प्रकारका डाटा ह्यान्डल गर्ने**
- **दृढ त्रुटि व्यवस्थापन र लगिङ रणनीतिहरू**
- **एकै सर्भरमा बहु-उपकरण समन्वय**

अन्त्यमा, तपाईंले उन्नत AI र LLM-शक्तिशाली अनुप्रयोगहरूका लागि आवश्यक ढाँचा र उत्तम अभ्यासहरूमा व्यावहारिक अनुभव पाउनुहुनेछ।

## परिचय

यस पाठमा, तपाईंले सिक्नुहुनेछ कसरी एक उन्नत MCP सर्भर र क्लाइन्ट बनाउने जसले SerpAPI प्रयोग गरी LLM क्षमताहरूलाई वास्तविक-समय वेब डाटासँग विस्तार गर्छ। यो वेबबाट अद्यावधिक जानकारी पहुँच गर्न सक्ने गतिशील AI एजेन्टहरू विकास गर्न महत्वपूर्ण सीप हो।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- बाह्य API हरू (जस्तै SerpAPI) लाई सुरक्षित रूपमा MCP सर्भरमा एकीकृत गर्न
- वेब, समाचार, उत्पादन खोज, र प्रश्नोत्तरका लागि धेरै उपकरणहरू कार्यान्वयन गर्न
- LLM को लागि संरचित डाटा पार्स र फर्म्याट गर्न
- त्रुटिहरू व्यवस्थापन गर्न र API दर सीमाहरू प्रभावकारी रूपमा सम्हाल्न
- स्वचालित र अन्तरक्रियात्मक दुवै MCP क्लाइन्टहरू निर्माण र परीक्षण गर्न

## वेब सर्च MCP सर्भर

यस खण्डले वेब सर्च MCP सर्भरको वास्तुकला र सुविधाहरू परिचय गराउँछ। तपाईंले देख्नुहुनेछ कसरी FastMCP र SerpAPI सँगै प्रयोग गरेर LLM क्षमताहरूलाई वास्तविक-समय वेब डाटासँग विस्तार गरिन्छ।

### अवलोकन

यस कार्यान्वयनमा चार उपकरणहरू छन् जसले MCP को क्षमता देखाउँछन् विभिन्न, बाह्य API-चालित कार्यहरूलाई सुरक्षित र प्रभावकारी रूपमा ह्यान्डल गर्ने:

- **general_search**: व्यापक वेब परिणामहरूको लागि
- **news_search**: हालैका शीर्षकहरूको लागि
- **product_search**: ई-कमर्स डाटाको लागि
- **qna**: प्रश्नोत्तर अंशहरूको लागि

### सुविधाहरू
- **कोड उदाहरणहरू**: Python का लागि भाषा-विशिष्ट कोड ब्लकहरू समावेश छन् (र सजिलै अन्य भाषाहरूमा विस्तार गर्न सकिने) स्पष्टताको लागि कोड पिभटहरू प्रयोग गरेर

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

क्लाइन्ट चलाउनु अघि, सर्भरले के गर्छ बुझ्न उपयोगी हुन्छ। [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) फाइलले MCP सर्भर कार्यान्वयन गर्छ, जसले वेब, समाचार, उत्पादन खोज, र प्रश्नोत्तरका लागि उपकरणहरू प्रदान गर्छ SerpAPI सँग एकीकृत गरेर। यसले आउने अनुरोधहरू ह्यान्डल गर्छ, API कलहरू व्यवस्थापन गर्छ, प्रतिक्रियाहरू पार्स गर्छ, र संरचित परिणामहरू क्लाइन्टलाई फर्काउँछ।

तपाईंले पूर्ण कार्यान्वयन [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) मा समीक्षा गर्न सक्नुहुन्छ।

यहाँ सर्भरले कसरी उपकरण परिभाषित र दर्ता गर्छ भन्ने संक्षिप्त उदाहरण छ:

### Python सर्भर

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

- **बाह्य API एकीकरण**: API कुञ्जीहरू र बाह्य अनुरोधहरूको सुरक्षित ह्यान्डलिङ देखाउँछ
- **संरचित डाटा पार्सिङ**: API प्रतिक्रियाहरूलाई LLM-अनुकूल ढाँचामा रूपान्तरण गर्ने तरिका देखाउँछ
- **त्रुटि व्यवस्थापन**: उपयुक्त लगिङसहित दृढ त्रुटि ह्यान्डलिङ
- **अन्तरक्रियात्मक क्लाइन्ट**: स्वचालित परीक्षण र अन्तरक्रियात्मक मोड दुवै समावेश
- **सन्दर्भ व्यवस्थापन**: अनुरोधहरूको लगिङ र ट्र्याकिङका लागि MCP Context प्रयोग

## पूर्वआवश्यकताहरू

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् तपाईंको वातावरण ठीकसँग सेटअप गरिएको छ। यसले सबै निर्भरताहरू इन्स्टल गरिएको र तपाईंका API कुञ्जीहरू सही रूपमा कन्फिगर गरिएको सुनिश्चित गर्नेछ ताकि विकास र परीक्षण सहज होस्।

- Python 3.8 वा माथि
- SerpAPI API कुञ्जी (साइन अप गर्नुहोस् [SerpAPI](https://serpapi.com/) मा - निःशुल्क स्तर उपलब्ध)

## स्थापना

सुरु गर्न, तपाईंको वातावरण सेटअप गर्न यी चरणहरू पालना गर्नुहोस्:

1. निर्भरताहरू uv (सिफारिस गरिएको) वा pip प्रयोग गरेर इन्स्टल गर्नुहोस्:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. परियोजना रुटमा `.env` फाइल बनाउनुहोस् र आफ्नो SerpAPI कुञ्जी राख्नुहोस्:

```
SERPAPI_KEY=your_serpapi_key_here
```

## प्रयोग

वेब सर्च MCP सर्भर मुख्य कम्पोनेन्ट हो जसले वेब, समाचार, उत्पादन खोज, र प्रश्नोत्तरका लागि उपकरणहरू प्रदान गर्छ SerpAPI सँग एकीकृत गरेर। यसले आउने अनुरोधहरू ह्यान्डल गर्छ, API कलहरू व्यवस्थापन गर्छ, प्रतिक्रियाहरू पार्स गर्छ, र संरचित परिणामहरू क्लाइन्टलाई फर्काउँछ।

तपाईंले पूर्ण कार्यान्वयन [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) मा समीक्षा गर्न सक्नुहुन्छ।

### सर्भर चलाउने

MCP सर्भर सुरु गर्न, तलको आदेश प्रयोग गर्नुहोस्:

```bash
python server.py
```

सर्भर stdio-आधारित MCP सर्भरको रूपमा चल्नेछ जसमा क्लाइन्ट सिधै जडान हुन सक्छ।

### क्लाइन्ट मोडहरू

क्लाइन्ट (`client.py`) ले MCP सर्भरसँग अन्तरक्रिया गर्न दुई मोडहरू समर्थन गर्छ:

- **सामान्य मोड**: सबै उपकरणहरूलाई परीक्षण गर्ने स्वचालित परीक्षणहरू चलाउँछ र तिनीहरूको प्रतिक्रियाहरू जाँच गर्छ। यो छिटो जाँच गर्न उपयोगी हुन्छ कि सर्भर र उपकरणहरू अपेक्षित रूपमा काम गरिरहेका छन् कि छैनन्।
- **अन्तरक्रियात्मक मोड**: मेनु-चालित इन्टरफेस सुरु गर्छ जहाँ तपाईं म्यानुअली उपकरणहरू चयन गरी कल गर्न सक्नुहुन्छ, कस्टम क्वेरीहरू प्रविष्ट गर्न सक्नुहुन्छ, र वास्तविक समयमा परिणामहरू हेर्न सक्नुहुन्छ। यो सर्भरको क्षमताहरू अन्वेषण गर्न र विभिन्न इनपुटहरूसँग प्रयोग गर्न उपयुक्त छ।

तपाईंले पूर्ण कार्यान्वयन [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) मा समीक्षा गर्न सक्नुहुन्छ।

### क्लाइन्ट चलाउने

स्वचालित परीक्षणहरू चलाउन (यसले स्वचालित रूपमा सर्भर पनि सुरु गर्नेछ):

```bash
python client.py
```

वा अन्तरक्रियात्मक मोडमा चलाउन:

```bash
python client.py --interactive
```

### विभिन्न तरिकाले परीक्षण गर्ने

सर्भरले प्रदान गर्ने उपकरणहरूसँग परीक्षण र अन्तरक्रिया गर्ने विभिन्न तरिकाहरू छन्, तपाईंको आवश्यकताअनुसार।

#### MCP Python SDK प्रयोग गरी कस्टम परीक्षण स्क्रिप्ट लेख्ने
तपाईं आफ्नो परीक्षण स्क्रिप्टहरू MCP Python SDK प्रयोग गरेर पनि बनाउन सक्नुहुन्छ:

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

यस सन्दर्भमा, "परीक्षण स्क्रिप्ट" भन्नाले तपाईंले लेखेको कस्टम Python प्रोग्राम हो जुन MCP सर्भरको क्लाइन्टको रूपमा काम गर्छ। यो औपचारिक युनिट टेस्ट होइन, तर यसले तपाईंलाई प्रोग्रामेटिक रूपमा सर्भरसँग जडान हुन, कुनै पनि उपकरणलाई तपाईंले रोजेको प्यारामिटरहरूसँग कल गर्न, र परिणामहरू निरीक्षण गर्न अनुमति दिन्छ। यो तरिका उपयोगी छ:

- उपकरण कलहरूको प्रोटोटाइप र प्रयोग गर्न
- सर्भरले विभिन्न इनपुटहरूमा कसरी प्रतिक्रिया दिन्छ भनी मान्यकरण गर्न
- बारम्बार उपकरण कलहरू स्वचालित गर्न
- MCP सर्भरमा आधारित आफ्नै कार्यप्रवाह वा एकीकरणहरू निर्माण गर्न

तपाईंले नयाँ क्वेरीहरू छिटो प्रयास गर्न, उपकरण व्यवहार डिबग गर्न, वा उन्नत स्वचालनको सुरुवातको रूपमा परीक्षण स्क्रिप्टहरू प्रयोग गर्न सक्नुहुन्छ। तल MCP Python SDK प्रयोग गरी यस्तो स्क्रिप्ट कसरी बनाउने उदाहरण छ:

## उपकरण विवरणहरू

तपाईंले सर्भरले प्रदान गर्ने निम्न उपकरणहरू प्रयोग गरेर विभिन्न प्रकारका खोज र क्वेरीहरू गर्न सक्नुहुन्छ। प्रत्येक उपकरण तल यसको प्यारामिटरहरू र उदाहरण प्रयोगसहित वर्णन गरिएको छ।

यस खण्डले उपलब्ध प्रत्येक उपकरण र तिनका प्यारामिटरहरूको विवरण दिन्छ।

### general_search

सामान्य वेब खोज गर्छ र फर्म्याट गरिएको परिणामहरू फर्काउँछ।

**यस उपकरणलाई कसरी कल गर्ने:**

तपाईं `general_search` लाई आफ्नो स्क्रिप्टबाट MCP Python SDK प्रयोग गरेर कल गर्न सक्नुहुन्छ, वा अन्तरक्रियात्मक रूपमा Inspector वा अन्तरक्रियात्मक क्लाइन्ट मोडबाट। यहाँ SDK प्रयोग गरी कोड उदाहरण छ:

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

अथवा, अन्तरक्रियात्मक मोडमा मेनुबाट `general_search` चयन गरी सोधिएको बेला आफ्नो क्वेरी प्रविष्ट गर्नुहोस्।

**प्यारामिटरहरू:**
- `query` (string): खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

कुनै क्वेरीसँग सम्बन्धित हालैका समाचार लेखहरू खोज्छ।

**यस उपकरणलाई कसरी कल गर्ने:**

तपाईं `news_search` लाई आफ्नो स्क्रिप्टबाट MCP Python SDK प्रयोग गरेर कल गर्न सक्नुहुन्छ, वा अन्तरक्रियात्मक रूपमा Inspector वा अन्तरक्रियात्मक क्लाइन्ट मोडबाट। यहाँ SDK प्रयोग गरी कोड उदाहरण छ:

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

अथवा, अन्तरक्रियात्मक मोडमा मेनुबाट `news_search` चयन गरी सोधिएको बेला आफ्नो क्वेरी प्रविष्ट गर्नुहोस्।

**प्यारामिटरहरू:**
- `query` (string): खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

कुनै क्वेरीसँग मेल खाने उत्पादनहरू खोज्छ।

**यस उपकरणलाई कसरी कल गर्ने:**

तपाईं `product_search` लाई आफ्नो स्क्रिप्टबाट MCP Python SDK प्रयोग गरेर कल गर्न सक्नुहुन्छ, वा अन्तरक्रियात्मक रूपमा Inspector वा अन्तरक्रियात्मक क्लाइन्ट मोडबाट। यहाँ SDK प्रयोग गरी कोड उदाहरण छ:

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

अथवा, अन्तरक्रियात्मक मोडमा मेनुबाट `product_search` चयन गरी सोधिएको बेला आफ्नो क्वेरी प्रविष्ट गर्नुहोस्।

**प्यारामिटरहरू:**
- `query` (string): उत्पादन खोज क्वेरी

**उदाहरण अनुरोध:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

खोज इन्जिनहरूबाट प्रश्नहरूको प्रत्यक्ष उत्तर प्राप्त गर्छ।

**यस उपकरणलाई कसरी कल गर्ने:**

तपाईं `qna` लाई आफ्नो स्क्रिप्टबाट MCP Python SDK प्रयोग गरेर कल गर्न सक्नुहुन्छ, वा अन्तरक्रियात्मक रूपमा Inspector वा अन्तरक्रियात्मक क्लाइन्ट मोडबाट। यहाँ SDK प्रयोग गरी कोड उदाहरण छ:

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

अथवा, अन्तरक्रियात्मक मोडमा मेनुबाट `qna` चयन गरी सोधिएको बेला आफ्नो प्रश्न प्रविष्ट गर्नुहोस्।

**प्यारामिटरहरू:**
- `question` (string): उत्तर खोज्नुपर्ने प्रश्न

**उदाहरण अनुरोध:**

```json
{
  "question": "what is artificial intelligence"
}
```

## कोड विवरणहरू

यस खण्डले सर्भर र क्लाइन्ट कार्यान्वयनका लागि कोड स्निपेटहरू र सन्दर्भहरू प्रदान गर्छ।

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

पूर्ण कार्यान्वयन विवरणका लागि [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) र [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) हेर्नुहोस्।

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## यस पाठका उन्नत अवधारणाहरू

निर्माण सुरु गर्नु अघि, यहाँ केही महत्वपूर्ण उन्नत अवधारणाहरू छन् जुन यस अध्यायभर देखिनेछन्। यी बुझ्नाले तपाईंलाई सजिलैसँग अघि बढ्न मद्दत गर्नेछ, चाहे तपाईं नयाँ हुनुहुन्छ भने पनि:

- **बहु-उपकरण समन्वय**: यसको अर्थ हो एउटै MCP सर्भरमा वेब सर्च, समाचार सर्च, उत्पादन सर्च, र प्रश्नोत्तर जस्ता विभिन्न उपकरणहरू चलाउनु। यसले तपाईंको सर्भरलाई विभिन्न कार्यहरू ह्यान्डल गर्न सक्षम बनाउँछ, केवल एउटा मात्र होइन।
- **API दर सीमा व्यवस्थापन**: धेरै बाह्य API हरू (जस्तै SerpAPI) ले निश्चित समयमा कति अनुरोध गर्न सकिन्छ भनेर सीमा लगाउँछन्। राम्रो कोडले यी सीमाहरू जाँच्छ र तिनीहरूलाई सहज रूपमा व्यवस्थापन गर्छ, ताकि तपाईंको एप्लिकेशन सीमा पुगे पनि क्र्यास नहोस्।
- **संरचित डाटा पार्सिङ**: API प्रतिक्रियाहरू प्रायः जटिल र नेस्टेड हुन्छन्। यो अवधारणा ती प्रतिक्रियाहरूलाई सफा, सजिलै प्रयोग गर्न मिल्ने ढाँचामा रूपान्तरण गर्ने बारे हो जुन LLM वा अन्य प्रोग्रामहरूका लागि अनुकूल हुन्छ।
- **त्रुटि पुनर्प्राप्ति**: कहिलेकाहीं समस्या आउँछ—जस्तै नेटवर्क असफलता वा API ले अपेक्षित प्रतिक्रिया नदिनु। त्रुटि पुनर्प्राप्तिले तपाईंको कोडलाई यी समस्याहरू ह्यान्डल गर्न र उपयोगी प्रतिक्रिया दिन सक्षम बनाउँछ, क्र्यास नगरी।
- **प्यारामिटर मान्यकरण**: यसले तपाईंका उपकरणहरूमा सबै इनपुटहरू सही र सुरक्षित छन् कि छैनन् भनेर जाँच्ने कुरा हो। यसमा पूर्वनिर्धारित मानहरू सेट गर्ने र प्रकारहरू मिलाउने समावेश छ, जसले बग र भ्रमबाट बचाउँछ।

## समस्या समाधान

वेब सर्च MCP सर्भरसँग काम गर्दा कहिलेकाहीं समस्या आउन सक्छ—यो बाह्य API र नयाँ उपकरणहरूसँग विकास गर्दा सामान्य हो। यस खण्डले सबैभन्दा सामान्य समस्याहरूका व्यावहारिक समाधानहरू प्रदान गर्छ, ताकि तपाईं छिटो पुनः ट्रयाकमा आउन सक्नुहोस्। यदि तपाईंले कुनै त्रुटि देख्नुभयो भने, यहाँबाट सुरु गर्नुहोस्: तलका सुझावहरूले प्रायः प्रयोगकर्ताहरूले भोग्ने समस्याहरू समाधान गर्छन् र अतिरिक्त सहयोग बिना नै तपाईंको समस्या समाधान हुन सक्छ।

### सामान्य समस्याहरू

तल केही सबैभन्दा सामान्य समस्याहरू छन् जुन प्रयोगकर्ताहरूले भोग्छन्, स्पष्ट व्याख्या र समाधानका कदमहरूसहित:

1. **.env फाइलमा SERPAPI_KEY हराएको**
   - यदि तपाईंले `SERPAPI_KEY environment variable not found` त्रुटि देख्नुभयो भने, यसको अर्थ तपाईंको एप्लिकेशनले SerpAPI पहुँच गर्न आवश्यक API कुञ्जी फेला पार्न सकेन। यसलाई समाधान गर्न, परियोजना रुटमा `.env` नामक फाइल बनाउनुहोस् (यदि छैन भने) र यसमा `SERPAPI_KEY=your_serpapi_key_here` लेख्नुहोस्। `your_serpapi_key_here` लाई तपाईंको वास्तविक SerpAPI कुञ्जीले प्रतिस्थापन गर्नुहोस्।

2. **मोड्युल फेला नपर्ने त्रुटिहरू**
   - `ModuleNotFoundError: No module named 'httpx'` जस्ता त्रुटिहरूले जनाउँछ कि आवश्यक Python प्याकेजहरू इन्स्टल छैनन्। यो प्रायः तब हुन्छ जब तपाईंले सबै निर्भरताहरू इन्स्टल गर्नुभएको छैन। यसलाई समाधान गर्न, टर्मिनलमा `pip install -r requirements.txt` चलाउनुहोस्।

3. **जडान समस्या**
   - `Error during client execution` जस्तो त्रुटि आएमा यसको अर्थ क्लाइन्ट सर्भरसँग जडान हुन सकिरहेको छैन वा सर्भर अपेक्षित रूपमा चलिरहेको छैन। दुवै क्लाइन्ट र सर्भर उपयुक्त संस्करणका छन् कि छैनन् र `server.py` सही स्थानमा छ र चलिरहेको छ कि छैन भनेर पुनः जाँच गर्नुहोस्। सर्भर र क्लाइन्ट दुवै पुनः सुरु गर्नु पनि मद्दत गर्न सक्छ।

4. **SerpAPI त्रुटिहरू**
   - `Search API returned error status: 401` देखिएमा यसको अर्थ तपाईंको SerpAPI कुञ्जी हराएको, गलत, वा म्याद सकिएको छ। आफ्नो SerpAPI ड्यासबोर्डमा जानुहोस्, कुञ्जी जाँच गर्नुहोस्, र आवश्यक परे `.env` फाइल अपडेट गर्नुहोस्। यदि कुञ्जी सही छ तर त्रुटि जारी छ भने, निःशुल्क स्तरको कोटा सकिएको छ कि छैन जाँच गर्नुहोस्।

### डिबग मोड

पूर्वनिर्धारित रूपमा, एपले केवल महत्वपूर्ण जानकारी लग गर्छ। यदि तपाईंलाई के भइरहेको छ भन्ने विस्तृत विवरण हेर्न मन छ भने (जस्तै जटिल समस्याहरू पत्ता लगाउन), DEBUG मोड सक्षम गर्न सक्नुहुन्छ। यसले एपले हरेक चरणमा के गरिरहेको छ भन्ने धेरै थप विवरण देखाउँछ।

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

ध्यान दिनुहोस् DEBUG मोडले HTTP अनुरोध, प्रतिक्रिया, र अन्य आन्तरिक विवरणहरू थप देखाउँछ। यो समस्या समाधानका लागि धेरै उपयोगी हुन सक्छ।
DEBUG मोड सक्षम गर्न, तपाईंको `client.py` वा `server.py` को शीर्षमा लगिङ स्तरलाई DEBUG मा सेट गर्नुहोस्:

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

## अब के गर्ने 

- [5.10 रियल टाइम स्ट्रिमिङ](../mcp-realtimestreaming/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
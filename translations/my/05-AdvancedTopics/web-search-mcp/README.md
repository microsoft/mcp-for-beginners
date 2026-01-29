# သင်ခန်းစာ - Web Search MCP Server တည်ဆောက်ခြင်း

ဤအခန်းတွင် အပြင် API များနှင့် ပေါင်းစပ်၍ အမျိုးမျိုးသောဒေတာအမျိုးအစားများကို ကိုင်တွယ်နိုင်ပြီး အမှားများကို စနစ်တကျ စီမံခန့်ခွဲနိုင်သည့်၊ မျိုးစုံသောကိရိယာများကို တစ်ပြိုင်နက်တည်း စီမံခန့်ခွဲနိုင်သည့် အလုပ်လုပ်နိုင်သော AI agent တစ်ခုကို တည်ဆောက်ပုံကို ပြသထားသည်။ သင်မြင်ရမည့်အချက်များမှာ -

- **အတည်ပြုချက်လိုအပ်သည့် အပြင် API များနှင့် ပေါင်းစပ်ခြင်း**
- **အမျိုးမျိုးသောဒေတာအမျိုးအစားများကို မျိုးစုံသော endpoint များမှ ကိုင်တွယ်ခြင်း**
- **ခိုင်မာသော အမှားစီမံခန့်ခွဲမှုနှင့် မှတ်တမ်းတင်နည်းများ**
- **တစ်ခုတည်းသော server တွင် မျိုးစုံကိရိယာများ စီမံခန့်ခွဲခြင်း**

အဆုံးသတ်သည့်အချိန်တွင် အဆင့်မြင့် AI နှင့် LLM အခြေပြု application များအတွက် မရှိမဖြစ်လိုအပ်သော ပုံစံများနှင့် အကောင်းဆုံးလေ့လာမှုများကို လက်တွေ့ကျကျ လေ့လာနိုင်ပါလိမ့်မည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် SerpAPI ကို အသုံးပြု၍ အချိန်နှင့်တပြေးညီ ဝက်ဘ်ဒေတာများဖြင့် LLM ၏ စွမ်းဆောင်ရည်များကို တိုးချဲ့ပေးသည့် အဆင့်မြင့် MCP server နှင့် client တည်ဆောက်နည်းကို သင်ယူမည်ဖြစ်သည်။ ၎င်းသည် ဝက်ဘ်မှ နောက်ဆုံးရသတင်းအချက်အလက်များကို ရယူနိုင်သည့် dynamic AI agent များ ဖန်တီးရာတွင် အရေးကြီးသော ကျွမ်းကျင်မှုတစ်ခုဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာအပြီးတွင် သင်သည် -

- SerpAPI ကဲ့သို့သော အပြင် API များကို MCP server တွင် လုံခြုံစွာ ပေါင်းစပ်နိုင်မည်
- ဝက်ဘ်၊ သတင်း၊ ထုတ်ကုန်ရှာဖွေရေးနှင့် Q&A အတွက် မျိုးစုံကိရိယာများကို အကောင်အထည်ဖော်နိုင်မည်
- LLM အသုံးပြုမှုအတွက် ဖွဲ့စည်းထားသော ဒေတာများကို ဖော်ပြနိုင်မည်
- အမှားများကို ကိုင်တွယ်နိုင်ပြီး API rate limit များကို ထိရောက်စွာ စီမံနိုင်မည်
- အလိုအလျောက်နှင့် အပြန်အလှန် MCP client များကို တည်ဆောက်၍ စမ်းသပ်နိုင်မည်

## Web Search MCP Server

ဤအပိုင်းတွင် Web Search MCP Server ၏ ဖွဲ့စည်းပုံနှင့် လုပ်ဆောင်ချက်များကို မိတ်ဆက်ပေးမည်ဖြစ်သည်။ FastMCP နှင့် SerpAPI ကို ပေါင်းစပ်၍ LLM ၏ စွမ်းဆောင်ရည်များကို အချိန်နှင့်တပြေးညီ ဝက်ဘ်ဒေတာဖြင့် တိုးချဲ့ပုံကို ကြည့်ရှုနိုင်မည်ဖြစ်သည်။

### အနှစ်ချုပ်

ဤအကောင်အထည်ဖော်မှုတွင် MCP ၏ လုံခြုံပြီး ထိရောက်စွာ အပြင် API များမှ တာဝန်များကို ကိုင်တွယ်နိုင်မှုကို ပြသသည့် ကိရိယာလေးခု ပါဝင်သည် -

- **general_search**: အထွေထွေ ဝက်ဘ် ရလဒ်များအတွက်
- **news_search**: နောက်ဆုံးရ သတင်းခေါင်းစဉ်များအတွက်
- **product_search**: အီလက်ထရွန်းနစ် ကုန်ပစ္စည်းများအတွက်
- **qna**: မေးခွန်းနှင့် ဖြေဆိုချက်များအတွက်

### လုပ်ဆောင်ချက်များ
- **ကုဒ်နမူနာများ**: Python အတွက် အထူးပြုထားသည့် ကုဒ်ပိုင်းများ ပါဝင်ပြီး အခြားဘာသာစကားများသို့လွယ်ကူစွာ တိုးချဲ့နိုင်သည်။

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

Client ကို run မလုပ်မီ server ၏ လုပ်ဆောင်ချက်ကို နားလည်ထားသင့်သည်။ [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ဖိုင်တွင် MCP server ကို အကောင်အထည်ဖော်ထားပြီး SerpAPI နှင့် ပေါင်းစပ်၍ ဝက်ဘ်၊ သတင်း၊ ထုတ်ကုန်ရှာဖွေရေးနှင့် Q&A ကိရိယာများကို ဖော်ပြထားသည်။ ၎င်းသည် လာရောက်သော တောင်းဆိုမှုများကို ကိုင်တွယ်ပြီး API ခေါ်ဆိုမှုများကို စီမံခန့်ခွဲ၊ တုံ့ပြန်ချက်များကို ဖော်ပြပြီး ဖောက်သည်ထံ သတ်မှတ်ထားသော ဖော်မတ်ဖြင့် ပြန်လည်ပေးပို့သည်။

[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) တွင် အပြည့်အစုံကို ကြည့်ရှုနိုင်ပါသည်။

အောက်တွင် server သည် ကိရိယာတစ်ခုကို မည်သို့ သတ်မှတ်ပြီး မှတ်ပုံတင်ထားသည်ကို နမူနာအနေနှင့် ဖော်ပြထားသည်။

### Python Server

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

- **အပြင် API ပေါင်းစပ်ခြင်း**: API key များနှင့် အပြင် API ခေါ်ဆိုမှုများကို လုံခြုံစွာ ကိုင်တွယ်ပုံ ပြသသည်
- **ဖွဲ့စည်းထားသော ဒေတာ ခွဲခြမ်းစိတ်ဖြာခြင်း**: API တုံ့ပြန်ချက်များကို LLM အတွက် သင့်တော်သော ဖော်မတ်သို့ ပြောင်းလဲပုံ
- **အမှားစီမံခန့်ခွဲမှု**: ခိုင်မာပြီး မှတ်တမ်းတင်မှုအပြည့်အစုံပါရှိသည်
- **အပြန်အလှန် Client**: အလိုအလျောက် စမ်းသပ်မှုများနှင့် လက်တွေ့ စမ်းသပ်နိုင်သည့် မျက်နှာပြင်ပါရှိသည်
- **Context စီမံခန့်ခွဲမှု**: MCP Context ကို အသုံးပြု၍ မှတ်တမ်းတင်ခြင်းနှင့် တောင်းဆိုမှုများကို လိုက်လံစစ်ဆေးခြင်း

## မတိုင်မီ လိုအပ်ချက်များ

စတင်မလုပ်မီ သင့်ပတ်ဝန်းကျင်ကို အောက်ပါအတိုင်း ပြင်ဆင်ထားရန် လိုအပ်သည်။ ၎င်းသည် လိုအပ်သော dependency များအားလုံး ထည့်သွင်းပြီး API key များကို မှန်ကန်စွာ ပြင်ဆင်ထားခြင်းဖြစ်သည်။

- Python 3.8 သို့မဟုတ် အထက်
- SerpAPI API Key (အခမဲ့ အဆင့် ရရှိနိုင်သည့် [SerpAPI](https://serpapi.com/) တွင် စာရင်းသွင်းရန်)

## တပ်ဆင်ခြင်း

စတင်ရန် အောက်ပါအဆင့်များကို လိုက်နာပါ -

1. uv (အကြံပြု) သို့မဟုတ် pip ဖြင့် dependency များ တပ်ဆင်ပါ -

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Project root တွင် `.env` ဖိုင်တစ်ခု ဖန်တီးပြီး သင့် SerpAPI key ကို ထည့်သွင်းပါ -

```
SERPAPI_KEY=your_serpapi_key_here
```

## အသုံးပြုနည်း

Web Search MCP Server သည် SerpAPI နှင့် ပေါင်းစပ်၍ ဝက်ဘ်၊ သတင်း၊ ထုတ်ကုန်ရှာဖွေရေးနှင့် Q&A ကိရိယာများကို ဖော်ပြသည့် အဓိက component ဖြစ်သည်။ ၎င်းသည် လာရောက်သော တောင်းဆိုမှုများကို ကိုင်တွယ်ပြီး API ခေါ်ဆိုမှုများကို စီမံခန့်ခွဲ၊ တုံ့ပြန်ချက်များကို ဖော်ပြပြီး ဖောက်သည်ထံ သတ်မှတ်ထားသော ဖော်မတ်ဖြင့် ပြန်လည်ပေးပို့သည်။

[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) တွင် အပြည့်အစုံကို ကြည့်ရှုနိုင်ပါသည်။

### Server ကို စတင်ခြင်း

MCP server ကို စတင်ရန် အောက်ပါ command ကို အသုံးပြုပါ -

```bash
python server.py
```

Server သည် stdio-based MCP server အဖြစ် run ဖြစ်ပြီး client သည် တိုက်ရိုက် ချိတ်ဆက်နိုင်ပါသည်။

### Client Mode များ

Client (`client.py`) သည် MCP server နှင့် ဆက်သွယ်ရာတွင် mode နှစ်မျိုးကို ထောက်ပံ့သည် -

- **Normal mode**: ကိရိယာအားလုံးကို စမ်းသပ်ပြီး တုံ့ပြန်ချက်များကို စစ်ဆေးသည့် automated test များ run လုပ်သည်။ Server နှင့် ကိရိယာများ အလုပ်လုပ်မှုကို အမြန်စစ်ဆေးရန် အသုံးဝင်သည်။
- **Interactive mode**: မီနူးအခြေပြု မျက်နှာပြင်ဖြင့် လက်ဖြင့် ကိရိယာများကို ရွေးချယ်ခေါ်ဆိုနိုင်ပြီး မိမိစိတ်ကြိုက် မေးခွန်းများ ထည့်သွင်း၍ ရလဒ်များကို အချိန်နှင့်တပြေးညီ ကြည့်ရှုနိုင်သည်။ Server ၏ စွမ်းဆောင်ရည်များကို စမ်းသပ်ရန်နှင့် input များကို စမ်းသပ်ရန် အထူးသင့်တော်သည်။

[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) တွင် အပြည့်အစုံကို ကြည့်ရှုနိုင်ပါသည်။

### Client ကို run လုပ်ခြင်း

Automated test များ run လုပ်ရန် (server ကို အလိုအလျောက် စတင်ပါမည်) -

```bash
python client.py
```

သို့မဟုတ် interactive mode ဖြင့် run လုပ်ရန် -

```bash
python client.py --interactive
```

### ကိရိယာများကို စမ်းသပ်ရန် နည်းလမ်းများ

Server မှ ပေးသော ကိရိယာများကို သင့်လိုအပ်ချက်နှင့် workflow အရ စမ်းသပ်နိုင်သည့် နည်းလမ်းများ ရှိသည်။

#### MCP Python SDK ဖြင့် စိတ်ကြိုက် စမ်းသပ်ရေးသားခြင်း

သင်သည် MCP Python SDK ကို အသုံးပြု၍ ကိုယ်ပိုင် စမ်းသပ် script များရေးသားနိုင်သည် -

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

ဤအခြေအနေတွင် "test script" ဆိုသည်မှာ MCP server အတွက် client အဖြစ် လုပ်ဆောင်ရန် သင်ရေးသားသော Python program တစ်ခုဖြစ်သည်။ ၎င်းသည် တရားဝင် unit test မဟုတ်ပေမယ့် server နှင့် ကိရိယာများကို parameter များဖြင့် ခေါ်ဆို၍ ရလဒ်များကို စစ်ဆေးနိုင်သည်။ ၎င်းနည်းလမ်းသည် -

- ကိရိယာခေါ်ဆိုမှုများကို စမ်းသပ်ရန်နှင့် စမ်းသပ်မှုများပြုလုပ်ရန်
- Server ၏ တုံ့ပြန်မှုကို အမျိုးမျိုးသော input များဖြင့် အတည်ပြုရန်
- ကိရိယာများကို အလိုအလျောက် ခေါ်ဆိုမှုများ ပြုလုပ်ရန်
- MCP server အပေါ် ကိုယ်ပိုင် workflow များ သို့မဟုတ် ပေါင်းစပ်မှုများ တည်ဆောက်ရန်

သင်သည် စမ်းသပ် script များကို အသုံးပြု၍ မေးခွန်းအသစ်များကို အမြန်စမ်းသပ်နိုင်ပြီး ကိရိယာများ၏ အပြုအမူကို ပြန်လည်စစ်ဆေးနိုင်သည်။ အောက်တွင် MCP Python SDK ကို အသုံးပြု၍ စမ်းသပ် script တစ်ခု ဖန်တီးနည်းကို နမူနာပြထားသည်။

## ကိရိယာ ဖော်ပြချက်များ

Server မှ ပေးသော ကိရိယာများကို အသုံးပြု၍ မျိုးစုံသော ရှာဖွေရေးနှင့် မေးခွန်းများကို ဆောင်ရွက်နိုင်သည်။ ကိရိယာတိုင်းကို ၎င်း၏ parameter များနှင့် နမူနာအသုံးပြုမှုအတူ ဖော်ပြထားသည်။

### general_search

အထွေထွေ ဝက်ဘ်ရှာဖွေရေး ပြုလုပ်ပြီး ဖော်မတ်ထားသော ရလဒ်များ ပြန်ပေးသည်။

**ကိရိယာကို မည်သို့ ခေါ်ဆိုမည်နည်း**

MCP Python SDK ကို အသုံးပြု၍ ကိုယ်ပိုင် script မှ `general_search` ကို ခေါ်ဆိုနိုင်ပြီး Inspector သို့မဟုတ် interactive client mode မှလည်း အသုံးပြုနိုင်သည်။ SDK အသုံးပြုနည်း နမူနာ -

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

သို့မဟုတ် interactive mode တွင် မီနူးမှ `general_search` ကို ရွေးချယ်ပြီး မေးခွန်းကို ထည့်သွင်းနိုင်သည်။

**Parameters:**
- `query` (string): ရှာဖွေရေး မေးခွန်း

**နမူနာ တောင်းဆိုမှု**

```json
{
  "query": "latest AI trends"
}
```

### news_search

မေးခွန်းနှင့် သက်ဆိုင်သော နောက်ဆုံးရ သတင်းဆောင်းပါးများကို ရှာဖွေသည်။

**ကိရိယာကို မည်သို့ ခေါ်ဆိုမည်နည်း**

MCP Python SDK ကို အသုံးပြု၍ ကိုယ်ပိုင် script မှ `news_search` ကို ခေါ်ဆိုနိုင်ပြီး Inspector သို့မဟုတ် interactive client mode မှလည်း အသုံးပြုနိုင်သည်။ SDK အသုံးပြုနည်း နမူနာ -

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

သို့မဟုတ် interactive mode တွင် မီနူးမှ `news_search` ကို ရွေးချယ်ပြီး မေးခွန်းကို ထည့်သွင်းနိုင်သည်။

**Parameters:**
- `query` (string): ရှာဖွေရေး မေးခွန်း

**နမူနာ တောင်းဆိုမှု**

```json
{
  "query": "AI policy updates"
}
```

### product_search

မေးခွန်းနှင့် ကိုက်ညီသည့် ထုတ်ကုန်များကို ရှာဖွေသည်။

**ကိရိယာကို မည်သို့ ခေါ်ဆိုမည်နည်း**

MCP Python SDK ကို အသုံးပြု၍ ကိုယ်ပိုင် script မှ `product_search` ကို ခေါ်ဆိုနိုင်ပြီး Inspector သို့မဟုတ် interactive client mode မှလည်း အသုံးပြုနိုင်သည်။ SDK အသုံးပြုနည်း နမူနာ -

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

သို့မဟုတ် interactive mode တွင် မီနူးမှ `product_search` ကို ရွေးချယ်ပြီး မေးခွန်းကို ထည့်သွင်းနိုင်သည်။

**Parameters:**
- `query` (string): ထုတ်ကုန်ရှာဖွေရေး မေးခွန်း

**နမူနာ တောင်းဆိုမှု**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

ရှာဖွေရေးအင်ဂျင်များမှ မေးခွန်းများအတွက် တိုက်ရိုက်ဖြေချက်များ ရယူသည်။

**ကိရိယာကို မည်သို့ ခေါ်ဆိုမည်နည်း**

MCP Python SDK ကို အသုံးပြု၍ ကိုယ်ပိုင် script မှ `qna` ကို ခေါ်ဆိုနိုင်ပြီး Inspector သို့မဟုတ် interactive client mode မှလည်း အသုံးပြုနိုင်သည်။ SDK အသုံးပြုနည်း နမူနာ -

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

သို့မဟုတ် interactive mode တွင် မီနူးမှ `qna` ကို ရွေးချယ်ပြီး မေးခွန်းကို ထည့်သွင်းနိုင်သည်။

**Parameters:**
- `question` (string): ဖြေရှာလိုသော မေးခွန်း

**နမူနာ တောင်းဆိုမှု**

```json
{
  "question": "what is artificial intelligence"
}
```

## ကုဒ်အသေးစိတ်

ဤအပိုင်းတွင် server နှင့် client အကောင်အထည်ဖော်မှုများအတွက် ကုဒ်နမူနာများနှင့် ကိုးကားချက်များ ပါဝင်သည်။

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

အပြည့်အစုံကို [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) နှင့် [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) တွင် ကြည့်ရှုနိုင်ပါသည်။

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## ဤသင်ခန်းစာရှိ အဆင့်မြင့်အယူအဆများ

တည်ဆောက်မှု စတင်မလုပ်မီ ဤအခန်းတွင် ပါဝင်မည့် အရေးကြီးသော အဆင့်မြင့်အယူအဆများကို နားလည်ထားသင့်သည်။ ၎င်းတို့ကို နားလည်ခြင်းဖြင့် သင်သည် လမ်းညွှန်ချက်များကို ပိုမိုလွယ်ကူစွာ လိုက်နာနိုင်မည်ဖြစ်သည်။

- **မျိုးစုံကိရိယာ စီမံခန့်ခွဲမှု
To enable DEBUG mode, set the logging level to DEBUG at the top of your `client.py` or `server.py`:

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

## နောက်တစ်ဆင့်

- [5.10 အချိန်နှင့်တပြေးညီ စတ്രീမင်း](../mcp-realtimestreaming/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် မှားဖတ်ရှုမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
## စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေခြင်း

MCP ဆာဗာကို စမ်းသပ်မတိုင်မှီ၊ ရနိုင်သော ကိရိယာများနှင့် အမှားရှာဖွေရေးအတွက် အကောင်းဆုံးနည်းလမ်းများကို နားလည်ထားခြင်းမှာ အရေးကြီးသည်။ ထိရောက်သော စမ်းသပ်ခြင်းက သင့်ဆာဗာသည် မျှော်မှန်းချက်အတိုင်း လုပ်ဆောင်ကြောင်း စစ်ဆေးပေးပြီး ပြဿနာများကို အမြန်ဆုံး ရှာဖွေဖြေရှင်းနိုင်စေသည်။ အောက်ပါ အပိုင်းတွင် MCP ရေးဆွဲမှုကို တည်မြဲစွာ စစ်ဆေးသုံးသပ်ရန် အကြံပြုနည်းလမ်းများကို ဖော်ပြထားသည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာက မှန်ကန်သော စမ်းသပ်နည်းလမ်းရွေးချယ်ခြင်းနှင့် အထိရောက်ဆုံး စမ်းသပ်ကိရိယာ အသုံးပြုနည်းကို မိတ်ဆက်ပေးပါသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးချိန်တွင် သင်သည်

- စမ်းသပ်မှုအမျိုးမျိုးနည်းလမ်းများကို ဖော်ပြနိုင်မည်။
- ကုဒ်ကို ထိရောက်စွာ စမ်းသပ်ရန် ကိရိယာအမျိုးမျိုးကို အသုံးပြုနိင်မည်။

## MCP ဆာဗာများကို စမ်းသပ်ခြင်း

MCP သည် သင့်ဆာဗာများကို စမ်းသပ်နှင့် အမှားရှာဖွေရေးလုပ်ဆောင်နိုင်ရန် ကိရိယာများကို ပံ့ပိုးပေးသည်။

- **MCP Inspector**: CLI ကိရိယာအဖြစ် နှင့် ရုပ်မြင်ကိရိယာအဖြစ် ပြေးနိုင်သော command line ကိရိယာတစ်ခုဖြစ်သည်။
- **လက်တွေ့ စမ်းသပ်ခြင်း**: curl ကဲ့သို့သော ကိရိယာတစ်ခုကို အသုံးပြုပြီး web request များ ပြေးနိုင်ပါသည်၊ သို့သော် HTTP ပြေးနိုင်သော မည်သည့်ကိရိယာမဆို သုံးနိုင်သည်။
- **ယူနစ် စမ်းသပ်ခြင်း**: သင်၏နှစ်သက်ရာ စမ်းသပ်မှုဖွဲ့စည်းမှုကို အသုံးပြု၍ ဆာဗာနှင့် client ၏ လုပ်ဆောင်ချက်များကို စမ်းသပ်နိုင်သည်။

### MCP Inspector အသုံးပြုခြင်း

ဤကိရိယာအသုံးပြုနည်းကို ယခင်သင်ခန်းစာများတွင် ရှင်းပြခဲ့ပြီးနောက်ကျ သေးငယ်စွာ ပြောကြားလိုပါသည်။ Node.js ဖြင့် တည်ဆောက်ထားသော ကိရိယာဖြစ်ပြီး `npx` executable ကို ခေါ်ယူအသုံးပြုနိုင်သည်။ ၎င်းက ကိရိယာကို ခေတ္တ ဒေါင်းလုပ်လုပ်ပြီး 설치 ပြီးပါက သင့်မေးခွန်းကို ပြေးပြီးနောက် ကိရိယာကို   ကိုယ်တိုင်သန့်စင်ပါသည်။

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) က သင့်အား အောက်ပါအတိုင်း အကူအညီပေးသည်။

- **ဆာဗာအင်္ဂါရပ်များ ရှာဖွေခြင်း**: ရနိုင်သော resource များ၊ ကိရိယာများနှင့် prompt များကို အလိုအလျောက် ဖော်ထုတ်နိုင်သည်။
- **ကိရိယာ ပြေးမှု စမ်းသပ်ခြင်း**: အမျိုးမျိုးသော parameter များကို စမ်းသပ်ပြီး တကယ့်တုံ့ပြန်မှုများကို စမ်းသပ်ကြည့်နိုင်သည်။
- **ဆာဗာ Metadata ကြည့်ရှုခြင်း**: ဆာဗာအချက်အလက်များ၊ schema များနှင့် စီမံခန့်ခွဲမှုများကို စစ်ဆေးနိုင်သည်။

ကိရိယာ တစ်ခုကို စတင်တည်ဆောက်ခြင်းမှာ အောက်ပါအတိုင်း ဖြစ်နိုင်သည်။

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

အထက်ပါ command သည် MCP နှင့် ၎င်း၏ ရုပ်မြင်ကိရိယာကို စတင်ပြီး သင့် browser တွင် ဒေသခံ web interface တစ်ခုကိုဖွင့်သည်။ မြှင့်အင်တာဖေ့စ်တွင် သင့်မှတ်ပုံတင်ထားသော MCP ဆာဗာများ၊ ၎င်း၏ရရှိနိုင်သော ကိရိယာများ၊ resource များနှင့် prompt များကို မြင်နိုင်မည်။ ထို့အပြင် ကိရိယာ၏ ပြေးမှုအား ပုံမှန် interactive ဖြင့် စမ်းသပ်ရန်၊ ဆာဗာ metadata ကို စစ်ဆေးရန်နှင့် တကယ့်တုံ့ပြန်မှုများကိုကြည့်ရှုရန် အဆင်ပြေစေသည်။ ၎င်းသည် MCP server ရေးဆွဲမှုများကို စစ်ဆေးရာတွင် ပိုမိုလွယ်ကူစေသည်။

ဤသည်မှာ ၎င်း၏ ပုံစံတစ်ခု : ![Inspector](../../../../translated_images/my/connect.141db0b2bd05f096.webp)

ဤကိရိယာကို CLI mode ဖြင့်လည်း လည်ပတ်နိုင်ပြီး၊ ထိုအခါ `--cli` attribute ကို ထည့်ရပါမည်။ CLI mode တွင် ကိရိယာအား ပေးပို့ခြင်း ချဉ်းကပ်ချက်အစုံကို ဖော်ပြသည့် ဥပမာမှာ အောက်ပါအတိုင်း ဖြစ်သည်။

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### လက်တွေ့ စမ်းသပ်ခြင်း

ဆာဗာအင်္ဂါရပ်များကို စမ်းသပ်ရန် inspector ကိရိယာပြေးခြင်း အပြင် HTTP အသုံးပြုနိုင်သော client ကို အေကြာင်း curl ကဲ့သို့ လည်ပတ်စေခြင်းနှင့် ဆင့်ကြည့်နည်း တစ်ခုလည်း ရှိသည်။

curl ကို အသုံးပြု၍ MCP ဆာဗာများကို တိုက်ရိုက် HTTP request များမှတစ်ဆင့် စမ်းသပ်နိုင်သည်။

```bash
# ဥပမာ - စမ်းသပ်မှု ဆာဗာ metadata
curl http://localhost:3000/v1/metadata

# ဥပမာ - ကိရိယာတစ်ခုကို လုပ်ဆောင်ပါ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

အထက်ပါ curl အသုံးပြုပုံအတိုင်း သင်သည် ကိရိယာကို ဖိတ်ခေါ်ရန် POST request ကို အသုံးပြုသည်။payload တွင် ကိရိယာနာမည်နှင့် ၎င်း၏ parameter များ ပါဝင်သည်။ သင့်အတွက် အဆင်ပြေသော နည်းလမ်းကို ရွေးချယ်ပါ။ CLI ကိရိယာများသည် ပုံမှန်အားဖြင့် အသုံးပြုရန်ပိုမြန်ဆန်ပြီး စကရစ်ပြုလုပ်ရန် အထောက်အကူဖြစ်သည့်အတွက် CI/CD ပတ်ဝန်းကျင်တွင် များစွာသုံးနိုင်သည်။

### ယူနစ် စမ်းသပ်ခြင်း

သင့် ကိရိယာများနှင့် resource များအတွက် ယူနစ် စမ်းသပ်မှုများ ဖန်တီး၍ လုပ်ဆောင်ချက်များမှန်ကန်ကြောင်း သေချာစေပါ။ အောက်တွင် စမ်းသပ်ရေးကုဒ် ဥပမာတစ်ခု ဖေါ်ပြထားသည်။

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# async အတွက် စမ်းသပ်မှုများအတွက် module အားလုံးကို သတ်မှတ်ပါ
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # စမ်းသပ်မှုကိရိယာ ၂ ခု ဖန်တီးပါ
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # cursor ပါရာမီတာမပါဘဲ စမ်းသပ်ပါ (ဖျောက်ထားသည်)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # cursor=None ဖြင့် စမ်းသပ်ပါ
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # cursor ကို string အနေနှင့် အသုံးပြု၍ စမ်းသပ်ပါ
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # ရှုပ်ရှင်းမှုမရှိသော string cursor ဖြင့် စမ်းသပ်ပါ
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

အထက်ပါကုဒ်သည် အောက်ပါအတိုင်း ပြုလုပ်သည်။

- pytest framework ကိုအသုံးပြု၍ function များအဖြစ် စမ်းသပ်မှုများဖန်တီးရန်နှင့် assert ကြေညာချက်များကို သုံးနိုင်သည်။
- ကိရိယာနှစ်ခုပါသော MCP ဆာဗာ တစ်ခု ဖန်တီးသည်။
- အခြေအနေတချို့ ပြည့်မှီခြင်းကို စစ်ဆေးရန် `assert` ကြေညာချက်ကို သုံးသည်။

[ပြည့်စုံသောဖိုင်ကို ဤနေရာတွင် ကြည့်ရှုနိုင်သည်](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

အထက်ဖော်ပြပါ ဖိုင်အရ သင့်ကိုယ်ပိုင် ဆာဗာကို စမ်းသပ်၍ ၎င်း၏ အင်္ဂါရပ်များ ဦးတည်ချက်အတိုင်း ရှိကြောင်း သေချာစေနိုင်သည်။

အဓိက SDK အားလုံးတွင် ယခုအစိတ်အပိုင်းနှင့် ဆင်တူသော စမ်းသပ်ချက်များ ပါရှိသဖြင့် သင့်ရွေးချယ်သော runtime အတွက် ကိုက်ညီအောင် ပြင်ဆင်နိုင်သည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## အပိုဆောင်း အရင်းအမြစ်များ

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## နောက်ဆုံးတွင်

- နောက်တစ်ခု: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဂရုစိုက်ချက်**  
ဤစာတမ်းသည် AI ဘာသာပြန် ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြုပြီး ဘာသာပြန်ထားခြင်းဖြစ်ပါသည်။ ကျွန်ုပ်တို့သည် မှန်ကန်မှုအတွက် ကြိုးစားကာ မည်သည့်အချိန်တွင်မဆို အလိုအလြော မှားယွင်းမှုများ ဖြစ်ပေါ်နိုင်ကြောင်း သတိပြုရန်အရေးကြီးသည်။ မူရင်းစာတမ်းကို မိသားစကားဖြင့် ရှိသည့် ပြည်နယ် အရင်းအမြစ် အဖြစ် ယုံကြည်သင့်ပါသည်။ အရေးပါတဲ့ သတင်းအချက်အလက်များအတွက် မိမိလူငယ်ဘာသာပြန်ပညာရှင်မှ လုပ်ဆောင်သင့်သည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုမှ ဖြစ်ပေါ်နိုင်သော မတိကျမှုများ သို့မဟုတ် အနားမလည်မှုများအတွက် ကျွန်ုပ်တို့ မကျေအားဖြင့် တာဝန်မပါဝင်ပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
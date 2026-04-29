## စမ်းသပ်ခြင်း နှင့် အမှားရှင်းခြင်း

MCP ဆာဗာကို စမ်းသပ်ရန် မစတင်မီမှာ အသုံးပြုနိုင်သော ကိရိယာများနှင့် အမှားရှင်းရန် များအတွက် ကောင်းမွန်သည့် လေ့လာမှုများကို နားလည်ထားရန် အရေးကြီးသည်။ ထိရောက်စွာ စမ်းသပ်ခြင်းသည် သင့်ဆာဗာသည် မျှော်မှန်းထားသည့်အတိုင်း အလုပ်လုပ်နေသည်ကို သေချာစေရန်နှင့် ပြဿနာများကို အမြန်ဆုံး တွေ့ရှိ၍ ဖြေရှင်းရန် ကူညီပေးပါသည်။ အောက်ပါ အပိုင်းတွင် သင့် MCP အကောင်အထည်ဖော်မှုကို အတည်ပြုရန် အကြံပြုထားသော နည်းလမ်းများကို ဖော်ပြထားပါသည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာသည် သင်ကြားရန် သင်တန်းနှင့် ထိရောက်သော စမ်းသပ်ကိရိယာ ရွေးချယ်နည်းကို ဖော်ပြပါသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာ၏ အဆုံးတွင် သင်မှာ အောက်ပါအချက်များပြုလုပ်နိုင်ပါမည်-

- စမ်းသပ်မှုအတွက် အမျိုးမျိုးသောနည်းလမ်းများကို ဖော်ပြနိုင်မည်။
- သင့်ကုဒ်ကို ထိရောက်စွာ စမ်းသပ်ရန် ကိရိယာအမျိုးအစားများကို အသုံးပြုနိုင်မည်။

## MCP ဆာဗာများကို စမ်းသပ်ခြင်း

MCP သည် သင့်ဆာဗာများကို စမ်းသပ်ပြီး အမှားရှင်းရာတွင် ကူညီပေးသော ကိရိယာများကို မိတ်ဆက်ပေးပါသည်-

- **MCP Inspector**: CLI ကိရိယာအဖြစ်ဖြစ်စေ၊ ကြည့်ရှုခွင့်ရှိသောကိရိယာအဖြစ်ဖြစ်စေ အသုံးပြုနိုင်သော command line tool။
- **လက်ဖြင့် စမ်းသပ်ခြင်း**: curl ကဲ့သို့သော ကိရိယာအသုံးပြု၍ web request များ ပြုလုပ်နိုင်သော်လည်း HTTP ကို အသုံးပြုနိုင်သည့် ကိရိယာ များဖြင့်လည်း ပြုလုပ်နိုင်သည်။
- **ယူနစ် စမ်းသပ်ခြင်း**: သင့်အကြိုက် testing framework ကို အသုံးပြု၍ ဆာဗာနှင့် client နှစ်ခုစလုံးရှိ function များကို စမ်းသပ်နိုင်သည်။

### MCP Inspector ကို အသုံးပြုခြင်း

ဤကိရိယာအသုံးပြုမှုကို ယခင်သင်ခန်းစာများတွင် ဖော်ပြခဲ့သော်လည်း ပြည်တွင်းအဆင့်တွင် နည်းနည်း ပြောကြားပါမည်။ ၎င်းသည် Node.js ဖြင့် တည်ဆောက်ထားပြီး npx executable ကို ခေါ်သုံး၍ အသုံးပြုနိုင်သည်။ ၎င်းသည် tool ကို ယာယီ ဒေါင်းလုဒ်လုပ်၍ install ပြုလုပ်ပြီး သင့်ရဲ့ request ကို ပြီးဆုံးသွားလျှင် မူလအတိုင်း သန့်ရှင်းပေးပါသည်။

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) သည် သင့်အား-

- **ဆာဗာ တာဝန်များ ရှာဖွေခြင်း**: အသုံးပြုနိုင်သော resource များ၊ ကိရိယာများနှင့် prompt များကို အလိုအလျောက် ရှာဖွေပြသသည်။
- **ကိရိယာ အကောင်အထည်ဖော်ခြင်း စမ်းသပ်မှု**: parameter များ အမျိုးမျိုးကို စမ်းသပ်ပြီး တုံ့ပြန်ချက်ကို အချိန်နှင့်တပြေးညီ ကြည့်ရှုနိုင်သည်။
- **ဆာဗာ metadata ကြည့်ရှုခြင်း**: ဆာဗာ သတ်မှတ်ချက်များ၊ လုပ်ဆောင်ချက် schemas နှင့် အပြင်အဆင်များ စစ်ဆေးကြည့်ရှုနိုင်သည်။

ဥပမာအနေဖြင့် tool ကို လည်ပတ်မှု တစ်ခုဟူ၍-

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

အထက်ပါ command သည် MCP နှင့် ၎င်း၏ visual interface ကို စတင်၍ သင့် browser တွင် ဒေသီးအခြေခံ web interface ကို ဖွင့်လှစ်ပါသည်။ သင့်ဆာဗာများ၊ ရရှိနိုင်သည့် ကိရိယာများ၊ resource များနှင့် prompt များကို ပြသသည့် dashboard ကို တွေ့ရှိနိုင်သည်။ interface သည် tool များကို အချိန်နှင့်တပြေးညီ စမ်းသပ်ခြင်း၊ ဆာဗာ metadata ကို စိစစ်ခြင်း နှင့် တုံ့ပြန်ချက်များကို ကြည့်ရှုနိုင်ခြင်းတို့အတွက် အသုံးပြုနိုင်သည်။ ၎င်းသည် MCP ဆာဗာ အကောင်အထည်ဖေါ်မှုများအား အတည်ပြုရောင်း ကြည့်ရှုရာတွင် ဂရုစိုက်ဖို့ လွယ်ကူစေပါသည်။

ဤကဲ့သို့ပုံသဏ္ဍာန်ရှိနိုင်ပါသည်- ![Inspector](../../../../translated_images/my/connect.141db0b2bd05f096.webp)

CLI mode ဖြင့်လည်း ၎င်းကိရိယာကို အသုံးပြုနိုင်ပြီး ဤအခန်းကဏ္ဍတွင် `--cli` attribute ကို ထည့်သွင်းရမည်။ ကျွန်ုပ်တို့ရဲ့ မ်ား CLI mode ဖြင့် အသုံးပြုပုံ ဥပမာမှာ ဆာဗာပေါ်ရှိ ကိရိယာအားလုံးကို စာရင်းပြပါသည်-

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### လက်ဖြင့် စမ်းသပ်ခြင်း

Inspector tool ကို အသုံးပြု၍ ဆာဗာ တာဝန်ယူနိုင်မှုများကို စမ်းသပ်ခြင်းမှတဆင့် အသုံးပြုခြင်းမှတပြင် HTTP ကို အသုံးပြုနိုင်သည့် client တစ်ခုကို အသုံးပြုခြင်းလည်း ဆင်တူနည်းလမ်းတစ်ရပ်ဖြစ်သည်။ ဥပမာ curl ကဲ့သို့ရှိသည်။

curl ဖြင့် MCP ဆာဗာများကို တိုက်ရိုက် HTTP request များ အသုံးပြုပြီး စမ်းသပ်နိုင်ပါသည်-

```bash
# ဥပမာ။ စမ်းသပ်မှု ဆာဗာ မဲတာဒေတာ
curl http://localhost:3000/v1/metadata

# ဥပမာ။ ကိရိယာ တစ်ခုကို အကောင်အထည် ဖော်ပါ
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

curl သုံးသည့် အထက်ပါ နမူနာမှ ကြည့်လျှင်၊ POST request ကို အသုံးပြုပြီး ကိရိယာနာမည်နှင့် ၎င်း၏ parameter များပါရှိသော payload ဖြင့် ကိရိယာအား ခေါ်ဆိုသည်။ သင့်အတွက် သင့်တော်သော နည်းလမ်းကို အသုံးပြုပါ။ CLI ကိရိယာများသည် အခြေခံအားဖြင့် အသုံးပြုရ လျင်မြန်ပြီး script ဖြင့် ရေးသားနိုင်သောကြောင့် CI/CD ပတ်ဝန်းကျင်တွင် အသုံးဝင်သည်။

### ယူနစ် စမ်းသပ်ခြင်း

Tools နှင့် resource များအတွက် ယူနစ် စမ်းသပ်မှုများ ဖန်တီးကာ သင့်ဆာဗာသည် မျှော်မှန်းသောအတိုင်း လုပ်ဆောင်နေကြောင်း သေချာစေရန် ပြုလုပ်ပါ။ ဤနေရာတွင် စမ်းသပ်မှု ကုဒ် တစ်စောင်ကို ပါ၊

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# asynchronous စမ်းသပ်ရန်အတွက် မော်ဂျူးလ်တစ်ခုလုံးကို မှတ်သားပါ
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # စမ်းသပ်မှုကိရိယာနှစ်ခုဖန်တီးပါ
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # cursor ပရမီတာမပါဝင်ဘဲ စမ်းသပ်ပါ (ရုပ်သိမ်းထားသည်)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # cursor=None ဝင်ရောက်မှုဖြင့် စမ်းသပ်ပါ
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # string အဖြစ် cursor ဖြင့် စမ်းသပ်ပါ
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # ရှင်းလင်းသည့် string cursor ဖြင့် စမ်းသပ်ပါ
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

အထက်ပါကုဒ်သည် အောက်ပါအတိုင်း လုပ်ဆောင်ပါသည်-

- pytest framework ကို အသုံးပြု၍ function အဖြစ် စမ်းသပ်မှုများ ဖန်တီးနိုင်ပြီး assert ကြေညာချက်များကို အသုံးပြုသည်။
- ကိရိယာနှစ်ခုပါ ၀င်သော MCP ဆာဗာကို ဖန်တီးသည်။
- အချို့သော အခြေအနေများ ပြည့်မှီကြောင်း စစ်ဆေးရန် `assert` ကြေညာချက်ကို အသုံးပြုသည်။

[ပါဝင်သော ဖိုင် အပြည့်အစုံကို ဒီနေရာတွင် ကြည့်ရှုပါ](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

အထက်ဖော်ပြထားသည့် ဖိုင်ကို အခြေခံ၍ သင့်ကိုယ်ပိုင် ဆာဗာကို စမ်းသပ်၍ တာဝန်ယူမှုများကို သေချာ ထားရှိနိုင်ပါသည်။

အဓိက SDK အားလုံးတွင် တူညီသည့် စမ်းသပ်မှု အပိုင်းများ ရှိသောကြောင့် သင့်ရွေးချယ်ထားသော runtime ကို ချိန်ညှိနိုင်ပါသည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## အပေါက်အတွင်း ဆက်စပ် ရင်းမြစ်များ

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## နောက်တစ်ခု

- နောက်တစ်ခု: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**တားမြစ်ချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားခြင်းဖြစ်သည်။ တိကျမှုအတွက် ကြိုးပမ်းနေသော်လည်း စက်ရုပ်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ခြင်းကို ကျေးဇူးပြု၍ အသိပေးအပ်ပါသည်။ မူရင်းစာတမ်းကို ရိုးရာဘာသာစကားဖြင့်သာ အတည်ပြုရမည့် စာရင်းတစ်ရပ်အဖြစ် သတ်မှတ်ရမည် ဖြစ်သည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန် ဝန်ဆောင်မှု ရယူရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ उत्पন্নနိုင်သော မတိကျမှုများ သို့မဟုတ် မှားယွင်းချက်များအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
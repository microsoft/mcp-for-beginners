# ကိစ္စလေ့လာမှု: API Management တွင် REST API ကို MCP ဆာဗာအဖြစ် ထုတ်ဖော်ပြသခြင်း

Azure API Management သည် သင့် API အဆုံးအချက်များ၏ အပေါ်တွင် Gateway ပေးသော ဝန်ဆောင်မှုတစ်ခု ဖြစ်သည်။ ၎င်း၏ လုပ်ဆောင်ပုံမှာ Azure API Management သည် သင့် APIs များ အရှေ့တွင် proxy အဖြစ် လုပ်ဆောင်ပြီး ဝင်ရောက်လာသော တောင်းဆိုမှုများကို ဘာလုပ်ရမည်ကို သတ်မှတ်နိုင်သည်။

၎င်းကို အသုံးပြုခြင်းဖြင့် လုပ်ဆောင်ချက်များစွာကို ထည့်သွင်းပေးနိုင်ပါသည်။

- **လုံခြုံရေး**၊ API keys, JWT မှစ၍ managed identity အထိ အားလုံးကို အသုံးပြုနိုင်ပါသည်။
- **အမြန်နှုန်းကန့်သတ်ခြင်း**၊ တစ်ချိန်ကြာမြင့်ချိန်တစ်ခုအတွင်း ဘယ်လောက်ခေါ်ဆိုမှုများဖြတ်သွားမလဲကို သတ်မှတ်ပေးနိုင်သော အလွန်ကောင်းတဲ့ လုပ်ဆောင်ချက်တစ်ခု ဖြစ်သည်။ ၎င်းက သုံးစွဲသူအားလုံးအတွက် အတွေ့အကြုံ အဆင်ပြေ စေရန်နှင့် သင့်ဝန်ဆောင်မှုသည် တောင်းဆိုမှုများများစွာကြောင့် ဖိအားများတတ်ရန်ကာကွယ်ပေးသည်။
- **မိုက်မားခြင်းနှင့် တွင်ဉ်းခွဲခွားခြင်း**။ ခေါ်ဆိုမှုများကို ချိန်ညှိရန် endpoint များ ပေါင်းစည်းဖွဲ့စည်းနိုင်ပြီး "load balance" ကိုဘယ်လိုလုပ်မလဲလည်း သတ်မှတ်နိုင်သည်။
- **AI လုပ်ဆောင်ချက်များ (semantic caching, token limit, token monitoring)** စသည်တို့ပါဝင်ပြီး တုံ့ပြန်မှုမြန်ဆန်စေရန်နှင့် token အသုံးစရိတ်ကို ထိန်းချုပ်ရန် အကောင်းဆုံးသော လုပ်ဆောင်ချက်များ ဖြစ်သည်။ [အသေးစိတ်ဒီမှာဖတ်ပါ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)။

## ဘာကြောင့် MCP + Azure API Management ဖြစ်သနည်း?

Model Context Protocol သည် agentic AI အပလီကေးရှင်းများနှင့် ကိရိယာနှင့် ဒေတာများကို တစ်မျိုးတည်းနည်းဖြင့် ထုတ်ဖော်ပြသပုံ အဖြစ် အရှိန်မြင့်လာနေသည်။ Azure API Management သည် API များကို "စီမံရန်" လိုအပ်သည့်အခါ သဘာဝ ကြားဖြတ်နေနေရာဖြစ်သည်။ MCP ဆာဗာများသည် တောင်းဆိုမှုများကို ကိရိယာများသို့ ဖြေရှင်းရန် အခြား API များနှင့် ပေါင်းစည်းတတ်သည်။ အထို့ကြောင့် Azure API Management နှင့် MCP ပေါင်းစည်းခြင်းမှာ အလွန်ထူးချွန်ပါတယ်။

## အကျဉ်းချုပ်

ယခု အသုံးပြုမှုအတွက် ကျွန်ုပ်တို့သည် API အဆုံးအချက်များကို MCP ဆာဗာအဖြစ် ထုတ်ဖော်ပြသပုံကို သင်ကြားမှာဖြစ်သည်။ ထို့ကြောင့် agentic အက်ပ်တစ်ခု၏ အစိတ်အပိုင်းအဖြစ် အလွယ်တကူ ထည့်သွင်းနိုင်ပြီး Azure API Management ၏ လုပ်ဆောင်ချက်များကိုလည်း အသုံးချနိုင်မည်ဖြစ်သည်။

## အဓိက လုပ်ဆောင်ချက်များ

- သင်ထုတ်ဖော်ချင်သည့် endpoint များကို ရွေးချယ်နိုင်သည်။
- သင့် API ၏ policy အပိုင်းတွင် သတ်မှတ်ထားသည့် သတ်မှတ်ချက်ပေါ်မူတည်၍ အပိုဆောင်း လုပ်ဆောင်ချက်များ ရရှိနိုင်သည်။ ဤနေရာတွင် rate limiting ကို ထည့်သွင်းနည်းပြပါမည်။

## ကြိုတင်လုပ်ဆောင်ချက်: API တစ်ခုကို ထည့်သွင်းခြင်း

သင်မှာ Azure API Management အတွင်း API ရှိပြီးသားဖြစ်ပါက နှစ်သက်ရာ အဆင့်ကိုကျော်လွှားနိုင်သည်။ မဟုတ်ပါက ဒီလင့်ခ်ကို ကြည့်ပါ၊ [Azure API Management သို့ API ထည့်သွင်းခြင်း](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)။

## API ကို MCP ဆာဗာအဖြစ် ထုတ်ဖော်ပြသခြင်း

API အဆုံးအချက်များကို ထုတ်ဖော်ပြသရန် အဆင့်များကို လိုက်နာကြရအောင်။

1. Azure Portal သို့ သွားပြီး ဒီလင့်ခ် <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> ကိုအသုံးပြုပါ။
သင့် API Management အခြေခံရုံးသို့ သွားပါ။

1. ဘယ်ဘက် menu တွင် APIs > MCP Servers > + Create new MCP Server ကို ရွေးပါ။

1. API မှ MCP ဆာဗာအဖြစ် ထုတ်ဖော်ချင်သည့် REST API ကို ရွေးပါ။

1. ကိရိယာများအဖြစ် ထုတ်ဖော်မည့် API Operation တစ်ခု သို့မဟုတ် အများစုကို ရွေးချယ်ပါ။ ဇယားအားလုံးကို သို့မဟုတ် သတ်မှတ်ထားသော အပိုင်းများသာ ရွေးချယ်နိုင်သည်။

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** ကို ရွေးချယ်ပါ။

1. **APIs** နှင့် **MCP Servers** menu ကို ပြန်သွားပြီး အောက်ပါအတိုင်း ထိတွေ့နိုင်ပါမည်။

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP ဆာဗာကို ဖန်တီးပြီး API operation များကို ကိရိယာများအဖြစ် ထုတ်ဖော်ပြသထားပါသည်။ MCP ဆာဗာသည် MCP Servers အပိုင်းတွင် ပြထားသည်။ URL ကော်လံတွင် စမ်းသပ်ချက်အတွက် သို့မဟုတ် client အက်ပ်လီကေးရှင်းအတွင်း ဖုန်းခေါ်နိုင်သည့် MCP ဆာဗာ၏ endpoint ကို ပြသသည်။

## ရွေးချယ်လို့ရမှု: policy များကို ပြင်ဆင်ခြင်း

Azure API Management တွင် policy ဆိုသည်မှာ သင့် endpoints များအတွက် အမျိုးမျိုးသော စည်းကမ်းချက်များကို သတ်မှတ်နိုင်သည့် အခြေခံအယူအဆတစ်ခု ဖြစ်သည်၊ ဥပမာအနေဖြင့် rate limiting သို့ semantic caching ကို အလွယ်တကူ ထည့်သွင်းနိုင်သည်။ ၎င်း policy များသည် XML ဖြင့် ရေးသားပါသည်။

MCP ဆာဗာ၏ rate limiting ကို ပြုလုပ်ရန် policy များ မည်သို့ သတ်မှတ်ရမည်ကို ပြပါမည်။

1. Portal တွင် APIs အောက်ရှိ **MCP Servers** ကို ရွေးချယ်ပါ။

1. ဖန်တီးထားသော MCP ဆာဗာကို ရွေးပါ။

1. ဘယ်ဘက် menu တွင် MCP အောက်ရှိ **Policies** ကို ရွေးပါ။

1. Policy editor တွင် MCP ဆာဗာကိရိယာများ အတွက် သတ်မှတ်လိုသည့် policy များကို ထည့်သွင်း သို့မဟုတ် ပြင်ဆင်ပါ။ policy များသည် XML နမူနာအတိုင်း သတ်မှတ်ထားသည်။ ဥပမာအနေဖြင့် MCP ဆာဗာကိရိယာများသို့ ခေါ်ဆိုမှုများကို ကန့်သတ်မည့် policy ရေးသားနိုင်သည် (ဒီနမူနာတွင် client IP လိပ်စာတစ်ခုခြား ၃၀ စက္ကန့်အတွင်း ၅ ခေါ်ဆိုမှု ချုပ်ဆိုထားသည်)။ ဒီဟာသည် rate limiting ဖြစ်စေမယ့် XML ဖြစ်သည်။

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    policy editor ၏ ပုံရိပ်ဖြစ်သည်။

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## စမ်းသပ်ကြည့်မယ်

ကျွန်ုပ်တို့၏ MCP ဆာဗာအလုပ်လုပ်မှုကို သေချာစေရန်။

> [!NOTE]
> Azure API Management သည် လက်ရှိတွင် ဒီဆာဗာကို Streamable
> HTTP `/mcp` endpoint မှတဆင့် ထုတ်ဖော်ပြသသည်။ စာရင်းရှစ် SSE နှင့် HTTP+SSE `/sse` သယ်ယူပို့ဆောင်မှုဟာ နောက်ပြန်လိုက်(client legacy) များအတွက်သာ အသုံးပြုသင့်သည်။
> 

ဤကိစ္စအတွက် Visual Studio Code နှင့် GitHub Copilot ၏ Agent mode ကို အသုံးပြုမည်။ MCP ဆာဗာကို *mcp.json* ထဲ ထည့်သွင်းမည်ဖြစ်ပြီး Visual Studio Code သည် agentic စွမ်းရည်ပါရှိသည့် client အဖြစ် အလုပ်လုပ်မည် ဖြစ်သည်။ အသုံးပြုသူများသည် prompt ရိုက်ထည့်ကာ ဆာဗာနှင့် ဆက်သွယ်နိုင်မည်ဖြစ်သည်။

Visual Studio Code တွင် MCP ဆာဗာကို ထည့်သွင်းခြင်းအား မြင်ကြရအောင်။

1. Command Palette မှ MCP: **Add Server command** ကို အသုံးပြုပါ။

1. ဖော်ပြပါအတိုင်း ဆာဗာအမျိုးအစားကို ရွေးချယ်ပါ : **HTTP (HTTP သို့မဟုတ် Server Sent Events)** ။ 

1. API Management တွင် MCP ဆာဗာအတွက် ပြသထားသော Streamable HTTP URL ကို ထည့်ပါ။
    ဥပမာ:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`။

1. သင်ရွေးချယ်လိုသည့် ဆာဗာ ID ကို ရိုက်ထည့်ပါ။ ဒီတန်ဖိုးသည် အရေးကြီးမဟုတ်ပေမယ့် ဆာဗာကို မှတ်မိရန် အထောက်အကူ ဖြစ်မည်။

1. configuration ကို သင့် workspace settings သို့မဟုတ် user settings မှာ သိမ်းဆည်းရန် ရွေးချယ်ပါ။

  - **Workspace settings** - ဆာဗာ configuration ကို ချိတ်ဆက်ထားသည့် workspace အတွင်း .vscode/mcp.json ဖိုင်တစ်ခုသို့သာ သိမ်းဆည်းမည်။

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - ဆာဗာ configuration ကို သင့် global *settings.json* ဖိုင်ထဲထည့်ပြီး workspace အားလုံးတွင် အသုံးပြုနိုင်သည်။ ဖော်ပြထားသည့် ပုံစံမှာ အောက်ပါအတိုင်း ဖြစ်သည်။

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management အတွက် မှန်ကန်စွာ အတည်ပြုရန် header တစ်ခုဖြည့်သွင်းရမည်။ header အမည်မှာ **Ocp-Apim-Subscription-Key* ဖြစ်သည်။

    - settings ထဲသို့ ထည့်သွင်းနည်:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)၊ ၎င်းသည် prompt တစ်ခု ပြသပြီး API key တန်ဖိုးကို မေးမြန်းမည်ဖြစ်ပြီး သင့် Azure API Management အတွက် Azure Portal တွင် ရနိုင်သည်။

   - ထို့အစား *mcp.json* ထဲသို့ ထည့်ရန်၊ အောက်ပါအတိုင်း ထည့်နိုင်သည်။

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Agent mode ကို အသုံးပြုခြင်း

ယခု settings သို့မဟုတ် *.vscode/mcp.json* ထဲ စီစဉ်ပြီးဖြစ်သည်။ စမ်းသပ်ကြည့်ပါ။

အောက်ပါအတိုင်း ကိရိယာများ icon တစ်ခု ရှိမည်၊ ဆာဗာမှ ထုတ်ဖော်ထားသည့် ကိရိယာများ ပါရှိသည်။

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ကိရိယာများ icon ကို နှိပ်ပြီး အောက်ပါအတိုင်း ကိရိယာများစာရင်းကို တွေ့မြင်နိုင်သည်။

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ကိရိယာကို ခေါ်ယူရန် စကားပြောမှာထဲတွင် prompt ကို ထည့်သွင်းပါ။ ဥပမာအနေဖြင့် အော်ဒါအကြောင်း မေးခွန်းတစ်ခု မေးနိုင်သည်။ စကားမေးခွန်း နမူနာ အောက်ပါအတိုင်း ဖြစ်သည်။

    ```text
    get information from order 2
    ```

    ယခု သင့်အား ကိရိယာ icon တစ်ခု ပြသပြီး ကိရိယာကို ဆက်လက်ခေါ်ယူရန် တောင်းဆိုပါမည်။ ဆက်လက်သည့်အခါ ရလဒ်အောက်ပါအတိုင်း ဖြစ်စေပါမည်။

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **အထက်တွင် မြင်သောအရာသည် သင့်အား တပ်ဆင်ထားသော ကိရိယာပေါ်မူတည်သည်၊ သို့သော် အဓိကမှာ အထက်ပါအတိုင်း စာဖတ်ဖြေကြားချက် တစ်ခုပေးသည်ဟု မြင်ရမည် ဖြစ်သည်။**


## ကိုးကားချက်များ

နောက်ထပ်သင်ယူနိုင်သော နည်းလမ်းများသည် အောက်ပါအတိုင်း ဖြစ်သည်။

- [Azure API Management နှင့် MCP အကြောင်း သင်ခန်းစာ](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python နမူနာ: Azure API Management ဖြင့် လုံခြုံပြီး ရွှေ့ပြောင်း MCP ဆာဗာများ (လေ့လာရေး)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client အတည်ပြုခြင်းလိုက်](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management extension ကို VS Code တွင် အသုံးပြု၍ API များကို ထည့်သွင်းစီမံခြင်း](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center တွင် ရွှေ့ပြောင်း MCP ဆာဗာများကို မှတ်ပုံတင်ရှာဖွေရန်](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management အား အသုံးပြု၍ AI စွမ်းဆောင်ရည်များ များစွာ ပြသထားသည့် repository အကောင်းတစ်ခု
- [AI Gateway သင်တန်းများ](https://azure-samples.github.io/AI-Gateway/) Azure Portal အသုံးပြု၍ စတင်လေ့လာရန် အကောင်းဆုံးနည်းလမ်းများပါဝင်သည်။

## အနာဂတ်အခြေအနေ

- ပြန်သွားရန်: [Case Studies Overview](./README.md)
- နောက်ဆက်တွဲ: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
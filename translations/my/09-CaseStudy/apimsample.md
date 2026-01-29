# ကိစ္စလေ့လာမှု - API Management တွင် REST API ကို MCP Server အဖြစ် ဖော်ထုတ်ခြင်း

Azure API Management သည် သင့် API Endpoints အပေါ်တွင် Gateway တစ်ခုကို ပေးသော ဝန်ဆောင်မှုဖြစ်သည်။ ၎င်း၏ လုပ်ဆောင်ပုံမှာ Azure API Management သည် သင့် API များ၏ ရှေ့တွင် proxy အဖြစ် လုပ်ဆောင်ပြီး ဝင်ရောက်လာသော တောင်းဆိုမှုများကို ဘာလုပ်မည်ကို ဆုံးဖြတ်နိုင်သည်။

၎င်းကို အသုံးပြုခြင်းဖြင့် အောက်ပါ အကျိုးကျေးဇူးများစွာ ရရှိနိုင်သည်-

- **လုံခြုံရေး** - API keys, JWT မှ Managed Identity အထိ အားလုံးကို အသုံးပြုနိုင်သည်။
- **Rate Limiting** - တစ်ခုချိန်ကာလအတွင်း ဘယ်လောက်အရေအတွက် တောင်းဆိုမှုများကို ခွင့်ပြုမည်ကို ဆုံးဖြတ်နိုင်သည်။ ၎င်းသည် အသုံးပြုသူများအားလုံးအတွက် အတွေ့အကြုံကောင်းများ ရရှိစေပြီး သင့်ဝန်ဆောင်မှုကို တောင်းဆိုမှုများကြောင့် များလွန်းခြင်းမှ ကာကွယ်ပေးသည်။
- **အတိုင်းအတာချိန်ညှိခြင်းနှင့် Load Balancing** - Load ကို ချိန်ညှိရန် Endpoint အရေအတွက်များကို သတ်မှတ်နိုင်ပြီး "load balance" လုပ်ပုံကိုလည်း ဆုံးဖြတ်နိုင်သည်။
- **AI Features** - Semantic caching, token limit နှင့် token monitoring စသည်တို့က Responsive ဖြစ်စေပြီး သင့် token အသုံးပြုမှုကို ထိန်းချုပ်နိုင်စေသည်။ [ပိုမိုသိရှိရန်](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)။

## MCP + Azure API Management ကို ဘာကြောင့် အသုံးပြုသင့်သလဲ?

Model Context Protocol သည် Agentic AI Apps များအတွက် standard အဖြစ် မြန်ဆန်စွာ ဖြစ်လာနေပြီး Tools နှင့် Data များကို တစ်စည်းတစ်လုံးအဖြစ် ဖော်ထုတ်ရန် အသုံးပြုသည်။ Azure API Management သည် API များကို "manage" လုပ်ရန် လိုအပ်သောအခါ သဘာဝကျသော ရွေးချယ်မှုဖြစ်သည်။ MCP Servers များသည် Tools တစ်ခုကို ဖြေရှင်းရန် အခြား API များနှင့် အတူတကွ ပေါင်းစည်းလေ့ရှိသည်။ ထို့ကြောင့် Azure API Management နှင့် MCP ကို ပေါင်းစည်းခြင်းသည် အကျိုးရှိစေသည်။

## အကျဉ်းချုပ်

ဤအသုံးပြုမှုအတွက် API Endpoints များကို MCP Server အဖြစ် ဖော်ထုတ်ပုံကို လေ့လာမည်။ ၎င်းအားဖြင့် Endpoints များကို Agentic App တစ်ခု၏ အစိတ်အပိုင်းအဖြစ် လွယ်ကူစွာ ဖော်ထုတ်နိုင်ပြီး Azure API Management မှ အကျိုးကျေးဇူးများကိုလည်း ရယူနိုင်သည်။

## အဓိက အင်္ဂါရပ်များ

- Tools အဖြစ် ဖော်ထုတ်လိုသော Endpoint Methods များကို ရွေးချယ်နိုင်သည်။
- သင်ရရှိမည့် အပိုအင်္ဂါရပ်များသည် သင့် API အတွက် Policy Section တွင် သတ်မှတ်ထားသော configuration အပေါ် မူတည်သည်။ ဤနေရာတွင် Rate Limiting ကို ထည့်သွင်းပုံကို ပြသမည်။

## Pre-step: API တစ်ခုကို Import လုပ်ခြင်း

Azure API Management တွင် API တစ်ခုရှိပြီးသားဖြစ်ပါက ဤအဆင့်ကို ကျော်သွားနိုင်သည်။ မရှိသေးပါက [Azure API Management တွင် API တစ်ခုကို Import လုပ်ခြင်း](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api) ကို ကြည့်ပါ။

## API ကို MCP Server အဖြစ် ဖော်ထုတ်ခြင်း

API Endpoints များကို ဖော်ထုတ်ရန် အောက်ပါအဆင့်များကို လိုက်နာပါ-

1. Azure Portal သို့ သွားပြီး <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> သို့ ဝင်ပါ။ သင့် API Management instance သို့ သွားပါ။

1. ဘယ်ဘက် menu တွင် APIs > MCP Servers > + Create new MCP Server ကို ရွေးပါ။

1. API တွင် MCP Server အဖြစ် ဖော်ထုတ်လိုသော REST API ကို ရွေးပါ။

1. Tools အဖြစ် ဖော်ထုတ်လိုသော API Operations တစ်ခု သို့မဟုတ် အများအပြားကို ရွေးပါ။ အားလုံးကို ရွေးနိုင်သလို သီးခြား operation များကိုသာ ရွေးနိုင်သည်။

    ![ဖော်ထုတ်လိုသော methods ရွေးချယ်ခြင်း](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** ကို ရွေးပါ။

1. Menu option **APIs** နှင့် **MCP Servers** သို့ သွားပါ။ အောက်ပါအတိုင်း မြင်ရမည်-

    ![Main pane တွင် MCP Server ကို ကြည့်ရန်](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP Server ကို ဖန်တီးပြီး API Operations များကို Tools အဖြစ် ဖော်ထုတ်ထားသည်။ MCP Servers pane တွင် MCP Server ကို တွေ့ရမည်။ URL column တွင် MCP Server ကို စမ်းသပ်ရန် သို့မဟုတ် Client Application တွင် အသုံးပြုရန် Endpoint ကို ပြထားသည်။

## Optional: Policies ကို Configure လုပ်ခြင်း

Azure API Management တွင် Policies ဆိုသော အဓိကအကြောင်းအရာရှိပြီး Endpoint များအတွက် Rate Limiting သို့မဟုတ် Semantic Caching စသည်တို့ကို သတ်မှတ်နိုင်သည်။ Policies များကို XML ဖြင့် ရေးသားသည်။

MCP Server အတွက် Rate Limiting ကို သတ်မှတ်ပုံ-

1. Portal တွင် APIs အောက်ရှိ **MCP Servers** ကို ရွေးပါ။

1. ဖန်တီးထားသော MCP Server ကို ရွေးပါ။

1. ဘယ်ဘက် menu တွင် MCP အောက်ရှိ **Policies** ကို ရွေးပါ။

1. Policy editor တွင် MCP Server ရဲ့ Tools များအတွက် အသုံးပြုလိုသော Policies များကို ထည့်သွင်း သို့မဟုတ် ပြင်ဆင်ပါ။ Policies များကို XML format ဖြင့် သတ်မှတ်သည်။ ဥပမာအားဖြင့် MCP Server ရဲ့ Tools များကို Client IP Address တစ်ခုလျှင် 30 စက္ကန့်အတွင်း 5 calls အထိသာ ခွင့်ပြုမည့် Policy ကို ထည့်သွင်းနိုင်သည်။

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Policy editor ရဲ့ ပုံရိပ်-

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## စမ်းသပ်ခြင်း

MCP Server သည် ရည်ရွယ်ထားသည့်အတိုင်း လုပ်ဆောင်နေသည်ကို စစ်ဆေးပါ။

ဤအတွက် Visual Studio Code နှင့် GitHub Copilot ၏ Agent mode ကို အသုံးပြုမည်။ MCP Server ကို *mcp.json* ဖိုင်တွင် ထည့်သွင်းမည်။ ၎င်းအားဖြင့် Visual Studio Code သည် Agentic capabilities ရှိသော Client အဖြစ် လုပ်ဆောင်ပြီး End Users များသည် Prompt ရိုက်ထည့်ကာ Server နှင့် အပြန်အလှန် ဆက်သွယ်နိုင်မည်။

Visual Studio Code တွင် MCP Server ကို ထည့်သွင်းပုံ-

1. Command Palette မှ MCP: **Add Server command** ကို အသုံးပြုပါ။

1. Server type ကို ရွေးပါ: **HTTP (HTTP or Server Sent Events)**.

1. API Management တွင် MCP Server ရဲ့ URL ကို ထည့်သွင်းပါ။ ဥပမာ- **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint အတွက်) သို့မဟုတ် **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint အတွက်)၊ transport အတွက် `/sse` သို့မဟုတ် `/mcp` ကွာခြားမှုကို သတိပြုပါ။

1. Server ID ကို သင်ရွေးချယ်ပါ။ ၎င်းသည် အရေးကြီးသောတန်ဖိုးမဟုတ်သော်လည်း Server instance ကို မှတ်မိရန် အထောက်အကူပြုမည်။

1. Configuration ကို workspace settings သို့မဟုတ် user settings တွင် သိမ်းဆည်းမည်ကို ရွေးပါ။

  - **Workspace settings** - Server configuration ကို .vscode/mcp.json ဖိုင်တွင် သိမ်းဆည်းပြီး လက်ရှိ workspace တွင်သာ ရရှိနိုင်သည်။

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Streaming HTTP ကို transport အဖြစ် ရွေးပါက အနည်းငယ် ကွာခြားမည်-

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Server configuration ကို Global *settings.json* ဖိုင်တွင် ထည့်သွင်းပြီး အားလုံး workspace များတွင် ရရှိနိုင်သည်။ Configuration သည် အောက်ပါအတိုင်း ဖြစ်မည်-

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management သို့ authenticate လုပ်ရန် header တစ်ခုကို ထည့်သွင်းရန် လိုအပ်သည်။ ၎င်းသည် **Ocp-Apim-Subscription-Key** header ကို အသုံးပြုသည်။

    - Settings တွင် ထည့်သွင်းပုံ-

    ![Authentication အတွက် header ထည့်သွင်းခြင်း](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)၊ API key value ကို Azure Portal တွင် သင့် Azure API Management instance အတွက် ရှာနိုင်သည်။

   - *mcp.json* တွင် ထည့်သွင်းရန်-

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

Settings သို့မဟုတ် *.vscode/mcp.json* တွင် အားလုံးကို စနစ်တကျ ပြင်ဆင်ပြီးပါပြီ။ စမ်းသပ်ကြည့်ပါ။

Tools icon တစ်ခုကို အောက်ပါအတိုင်း မြင်ရမည်၊ exposed tools များကို Server မှာ ပြထားသည်-

![Server မှ Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools icon ကို နှိပ်ပြီး Tools များ၏ စာရင်းကို အောက်ပါအတိုင်း မြင်ရမည်-

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Chat တွင် Prompt တစ်ခုကို ရိုက်ထည့်ကာ Tool ကို invoke လုပ်ပါ။ ဥပမာအားဖြင့် Order အကြောင်းကို သိရန် Tool တစ်ခုကို ရွေးထားပါက Agent ကို Order အကြောင်း မေးနိုင်သည်။ Prompt ဥပမာ-

    ```text
    get information from order 2
    ```

    Tools icon တစ်ခုကို ပြသပြီး Tool ကို run လုပ်ရန် ခွင့်ပြုမည်။ Tool ကို run လုပ်ရန် ရွေးပါ၊ အောက်ပါအတိုင်း output ကို မြင်ရမည်-

    ![Prompt မှ ရလဒ်](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **အထက်တွင် မြင်ရသည်မှာ သင် setup လုပ်ထားသော Tools များပေါ်မူတည်ပြီး Textual response အဖြစ် ရရှိမည်**


## References

ပိုမိုသိရှိရန်-

- [Azure API Management နှင့် MCP အတွက် Tutorial](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Azure API Management ကို အသုံးပြု၍ Remote MCP Servers ကို လုံခြုံစွာ အသုံးပြုခြင်း (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management extension ကို Visual Studio Code တွင် အသုံးပြု၍ API များကို Import နှင့် Manage လုပ်ခြင်း](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center တွင် Remote MCP Servers ကို Register နှင့် Discover လုပ်ခြင်း](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management နှင့် AI capabilities များကို ပြသသော Repo
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Azure Portal ကို အသုံးပြု၍ AI capabilities များကို စမ်းသပ်ရန် Workshop များ ပါဝင်သည်

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ အတည်ပြုထားသော ဘာသာပြန်ဆိုမှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ဆိုမှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
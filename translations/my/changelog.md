# ပြောင်းလဲမှုမှတ်တမ်း: MCP များအတွက် စတုတ္ထသင်တန်းအစီအစဉ်

ဤစာရွက်သည် Model Context Protocol (MCP) များအတွက် စတုတ္ထသင်တန်းအစီအစဉ်တွင် ပြုလုပ်ထားသော အရေးကြီးပြောင်းလဲမှုများအားလုံးကို မှတ်တမ်းတင်ရန် ဖြစ်သည်။ ပြောင်းလဲမှုများကို အချိန်မှန် တင်ပြီးနောက်မှ ပဉ္စမ အကြောင်းအရာဖြစ်ပါသည် (နောက်ဆုံးပြောင်းလဲမှုများ ပထမဆုံး).

## ၂၀၂၆ ခုနှစ် ဇူလိုင်လ ၂၉ ရက်

### မော်ဒယ် ၀၈ အသစ်အကြောင်း: ယုံကြည်စိတ်ချရသော Sidecars နှင့် လုံခြုံသော ပြန်လည်ကြိုးစားမှုများ

MCP ကိရိယာများအတွက် မင်းစိမ်း ရောင်းချသူ မဟုတ်သော အသင်းသားသင်ခန်းစာ အသစ် တစ်ခု ထည့်သွင်းခဲ့ပြီး
အဆုံးသတ် `2026-07-28` ဖော်ပြချက်နှင့် ကိုက်ညီအောင် လုပ်ဆောင်ခဲ့သည်။

- **အသစ်**: [ယုံကြည်စိတ်ချ ရွက်စာအုပ် သင်ခန်းစာ][reliability-sidecar]
  သည် ကူညီပေးမှု လက်မှတ်တောင်းဆိုမှုတစ်ခု၊ Mermaid diagram နှစ်ခုနှင့် ပြန်လည်ကြိုးစားမှု ဆုံးဖြတ်မှု
  စီးပြားလမ်းကြောင်း အသုံးပြုပြီး တည်ငြိမ်စွာ လည်ပတ်ခြင်း အချက်အလက်၊ atomic duplicate admission,
  ပြန်လည်ညှိနှိုင်းခြင်း၊ သက်သေခံချက်များနှင့် Tasks extension အတိုင်းအတာကို ရှင်းပြသည်။
- **အသစ်**: စံနှုန်းစာကြည့်တိုက် Python နှင့် SQLite အမှားဖန်တီးခြင်း လေ့ကျင့်ခန်းတစ်ခု
  သည် လုပ်ဆောင်မှုနှင့် လက်မှတ်စတိုးဆိုင်များကို သီးခြားအသုံးပြုကာ ရုပ်ပုံဆုံးရှုံးမှု ပြန်လည်တုံ့ပြန်မှုကို ပြသသည်။
  ခြားနားစွာ စမ်းသပ်မှုခြောက်ခုမှာ ရိုးရှင်း duplication၊ ကာကွယ်မှု ပြန်လည်စမတ်ခြင်း၊ payload conflicts,
  cached result များ၊ active claim များနှင့် တပြိုင်နက် duplicate admission ကို ဖုံးကွယ်သည်။
- **အပ်ဒိတ်လုပ်ခဲ့သည်**: Module 08 သည် အခုသင်ခန်းစာကို ချိတ်ဆက်ပေးပြီး
  နောက်ဆုံး `2026-07-28` stateless request မော်ဒယ်ကို ဖော်ပြကာ
  OpenTelemetry မြင်သာရေး မြောက်အမှတ်မဖြစ်သော MCP မှတ်တမ်းတင်ခြင်း features နှင့် ကွဲပြားမှုရှိသည်၊
  ၎င်း၏ မျိုးစိတ်ပြန်ကြိုးစားမှု နမူနာကို သတ်မှတ်ထားသည်။
- **ရွေးချယ်စရာ**: သင်ခန်းစာသည် ၎င်း၏ ပို့ဆောင်နိုင်သော အဓိကအကြောင်းအရာများကို
  တစ်ခုတည်းသော အကြောင်းအရာအသုံးပြု မှုးတိုက် အသင်းလိုက်ဖတ်ချက်များနှင့် ဆက်စပ်ပေးသည်
  သို့မဟုတ် ဝန်ဆောင်မှု host ဖြစ်ခြင်း သို့မဟုတ် ကွန်ယက်ခေါ်ဆိုမှုကို လေ့ကျင့်မှုအပိုင်းတစ်ခုအနေဖြင့် မပါ၀င်ပါ။










- **အပ်ဒိတ်** forward-looking ကြေငြာချက်များ ပါဝင်ပြီး သင်ခန်းစာ အသစ်နှင့် ချိတ်ဆက်ထားသည်:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protocol ဗားရှင်းမှတ်ချက်, Sampling/Roots/Logging/Tasks အပိုင်းများနှင့် "What’s next"
  - [02-Security/README.md](./02-Security/README.md): အတည်ပြုခွင့်ပြုမှု တင်းကျပ်မှု
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): stateless မောင်းနှင်မှု
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling ဖျက်ပစ်မှု
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging ဖျက်ပစ်မှုနှင့် Tasks extension
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): stateless/session routing
  - [README.md](./README.md): ဖော်ပြချက်အပိုင်းတွင် "ရှေ့ဆက်မျှော်လင့်ချက်" မှတ်ချက်နှင့် curriculum မော်ဒယ်ဇယားတွင် `1.1` အသစ်ထည့်သည်
  - [study_guide.md](./study_guide.md): Core Concepts အကျဉ်းချုပ်အောက် forward-looking မှတ်ချက်နှင့် ရက်စွဲထည့်သွင်းချက်
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): stateless request မော်ဒယ်မတိုင်ခင် mcp-session-id လမ်းကြောင်း
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Root Contexts/Sampling ဖျက်ပစ်မှုနှင့် Tasks extension
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): အတည်ပြုခွင့်တင်းထန်မှု






- [MCP in Copilot app](./12-tooling/01-copilot-app/README.md)






core sample များက သွားလာလိုအပ်သလောက် တည်ဆောက်၍ အလုပ်ဖြစ်နေကြောင်း အတည်ပြုခဲ့သည်။

#### ဖော်ပြချက် ဗားရှင်း မှန်ကန်မှုများ (2025-06-18 / 2025-03-26 → 2025-11-25)

အင်္ဂလိပ်စာတွင် မကြာသေးမီစံနှုန်း မပြောင်းလဲမှုပြဿနာကို ပြန်လည်ညှိပြီး `modelcontextprotocol.io` မှ Canonical link များကို ပြောင်းလိုက်သည်။
- **05-AdvancedTopics/mcp-security/README.md**: "လက်ရှိစံနှုန်း" banner၊ မိတ်ဆက်စာ၊ အဓိက လုံခြုံရေးနည်းလမ်းအသုံးပြုမှု ခေါင်းစဉ်၊ မဟာဗျူဟာ လိုအပ်ချက် ခေါင်းစဉ်၊ Microsoft Entra ID အပိုင်း၊ ရင်းမြစ်များနှင့် အရင်းအမြစ် ချိတ်ဆက်ချက်များနှင့် လုံခြုံရေး သတိပေးချက် (၈ ဖော်ပြချက်) ၂၀၂၅-၁၁-၂၅ သို့ ပြောင်းလဲခဲ့သည်
- **05-AdvancedTopics/mcp-transport/README.md**: အပိုဆောင်း ရင်းမြစ် ဖော်ပြချက် link နှင့် "လက်ရှိစံနှုန်း" banner ကို ၂၀၂၅-၁၁-၂၅ သို့ ပြောင်းလဲခဲ့သည်
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: ရှေးစွာ ထည့်သွင်းထားသော ၂၀၂၅-၀၃-၂၆ သုံးလမ်းလုံခြုံရေးနှင့် ယုံကြည်မှု link ကို လက်ရှိ ၂၀၂၅-၁၁-၂၅ သုံရုံရွေးချယ်မှု စံနှုန်းစာမျက်နှာ နှင့် ပြောင်းလဲခဲ့သည်
- **03-GettingStarted/14-sampling/README.md**: တရားဝင် Sampling စာတမ်း link ကို ၂၀၂၅-၁၁-၂၅ သို့ ပြောင်းပြီး ဖြစ်သည်

- **03-GettingStarted/05-stdio-server/README.md**: လက်ရှိ MCP သတ်မှတ်ချက် ရွေ့လျားခြင်းနှင့် Additional Resources သတ်မှတ်ချက် လင့်ခ်ကို 2025-11-25 အထိ အသစ်ပြုလုပ်ခဲ့သည် (သမိုင်းဆောင်း SSE ရပ်ဆိုင်း ချန်ထားမှုမှတ်ချက်များကို တိကျမှုရှိစေရန် မဖြတ်တောက်ထား)

#### လက်ရှိ SDK များနှင့် နမူနာ စစ်ဆေးခြင်း

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` က `@modelcontextprotocol/sdk@1.29.0` ကို ဖြေရှင်းခဲ့သည်; `tsc --noEmit` က စာရေးအမွားမရှိဘဲ ဖြတ်သန်းသွားသည် — ရှိပြီးသား `McpServer`/`StdioServerTransport` API များတည်ရှိနေဆဲ။
- **Python (03-GettingStarted/01-first-server/solution/python)**: ဘေးကင်း `.venv` တွင် `mcp[cli]` (1.27.2) ဖြင့် စစ်ဆေးခဲ့သည်; `py_compile` ဖြတ်သန်းကောင်းပြီး `FastMCP.list_tools()` က `add` နှင့် `subtract` ကိရိယာများကို မှန်ကန်စွာ ပြန်အမ်းပေးခဲ့သည်။
- နမူနာ `@modelcontextprotocol/sdk` ဗားရှင်းအဖြစ် (`>=1.26.0` / `^1.26.0` / `^1.27.0`) တို့သည် လက်ရှိ `1.29.0` နှင့် ပျက်စီးမှုမရှိဘဲ ဖြေရှင်းနိုင်ကြောင်း အတည်ပြုခဲ့သည်။

#### သက်ဆိုင်ရာ မေးလ်များ ပြန်လည်ညှိနှိုင်းခြင်း (ဗားရှင်း ကွာခြားမှု ပြုပြင်ခြင်း)

စီမံခန့်ခွဲမှုပုံစံနှင့် ကိုက်ညီမှုရှိစေရန် နမူနာအားလုံး အဟောင်းသော SDK အချက်များကို လက်ရှိ MCP ထုတ်ပြန်မှုနှင့် ကိုက်ညီအောင် ပြုပြင်ခဲ့သည်။
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` ကို `^1.8.0` မှ `>=1.26.0` သို့ မြှင့်ပြီး `"updated for MCP 2025-06-18"` မှ `"aligned with MCP Specification 2025-11-25"` ဟု ပက်ကေ့ဂျ် ဖေါ်ပြချက်ကို ပြောင်းသွားသည်။
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** နှင့် **lab4/code/github_mcp_server/pyproject.toml**: `mcp==1.23.0` ကို `mcp>=1.26.0` သို့ မြှင့်ပြီး `uv.lock` ဖိုင်နှစ်ဖိုင်ကို `uv lock` ဖြင့် ထပ်မံဖန်တီးခဲ့သည်။ ထို lock ဖိုင်များသည် လက်ရှိ `mcp 1.27.2` ကို ဖြေရှင်းပေးပြီး manifests များနှင့် ကိုက်ညီနေပြီ။

#### သင်ရိုးညွှန်းချက် စစ်ဆေးခြင်း — နောက်ဆုံးအကြောင်းအရာအတွက် Features တာဝန်ခံမှု

သင်ရိုးညွှန်းချက်တွင် MCP 2025-11-25 တွင် အသစ်စွာတိုးချဲ့ ထည့်သွင်းထားသည့် အခြေခံအရာများအားလုံးပါဝင်ကြောင်း သေချာစစ်ဆေးပြီး အကြောင်းအရာ လိုအပ်ချက် မရှိတော့ပါ။
- **Sampling**: သင်ခန်းစာ 03-GettingStarted/14-sampling နှင် 05-AdvancedTopics/mcp-sampling တွင် ဖော်ပြထားသည်။
- **Elicitation (URL မုဒ်အပါအဝင်)**: 01-CoreConcepts နှင့် 05-AdvancedTopics/mcp-protocol-features တွင် မှတ်တမ်းတင်ထားသည်။
- **Roots**: 00-Introduction, 01-CoreConcepts, နှင့် 05-AdvancedTopics/mcp-root-contexts တွင် မှတ်တမ်းတင်ထားသော။
- **Tasks (စမ်းသပ်မှု၊ ရေရှည်လုပ်ငန်းစဉ်များ)**: 01-CoreConcepts နှင့် 05-AdvancedTopics/mcp-protocol-features တွင် မှတ်တမ်းတင်ထားသော။
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): 01-CoreConcepts နှင့် 05-AdvancedTopics/mcp-protocol-features တွင် မှတ်တမ်းတင်ထားသော။

### လုံခြုံရေး တိုးတက်မှုနှင့် မူဝါဒ ချို့ယွင်းချက်များ ပြုပြင်ခြင်း

မူဝါဒ manifest တစ်ခုချင်းစီနှင့် နမူနာ ကိုဒ်များအားလုံးကို လုံခြုံရေးအပြည့်အဝ စစ်ဆေးပြီး npm အကြံပြုချက်များနှင့် ကိုဒ်အဆင့်ရှာဖွေမှု တစ်ခုကို ပြီးစီးအောင် ပြုပြင်လိုက်သည်။ ပြုပြင်ပြီးနောက် `npm audit` က စစ်ဆေးရာ ဒိုင်ရက်တောရီတိုင်း၌ **သိသိသာသာ ချို့ယွင်းချက် မရှိကြောင်း** ပြသည်။

#### npm မူဝါဒ ချို့ယွင်းချက်များ (ပြန်လည်ဖြေရှင်းထားခြင်း)

စုစုပေါင်း 15 ခုသော `package-lock.json` ဖိုင်များအားလုံးကို စစ်ဆေးခဲ့သည်။ ချို့ယွင်းချက်များမှာ MCP Inspector developer tool, OpenAI client နှင့် MCP SDK မှတဆင့် တင်သွင်းထားသော အခြားမူဝါဒများက အဓိက ဖြစ်ခဲ့ပြီးသည်။ မလုပ်ခွင့်ပေးသည့် နမူနာ များနှင့် မပျက်စီးအောင် ဖြေရှင်းထားပါသည်။
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** နှင့် **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`) ဗားရှင်းကို မြှင့်တင်ခဲ့၍ bundled မှာရှိသော `ajv`, `brace-expansion`, `diff`, `path-to-regexp` နှင့် `ws` အကြံပြုချက်များကို ဖယ်ရှားနိုင်ခဲ့သည်။ npm `overrides` တွင် patched `shell-quote@1.8.4` ကို တွဲဖက်ထည့်သွင်းထား၍ `concurrently` မှ ဆက်ခံထားသော အရေးကြီး အကြံပြုချက်ကို ဖြေရှင်းခဲ့သည်။ lockfiles နှစ်ခုကို ထပ်မံဖန်တီးခဲ့ပြီး (ယခု 0 ချို့ယွင်းချက်ရှိ)
- **03-GettingStarted/samples/typescript**: `npm audit fix` က တင်သွင်းထားသော `qs` (moderate) ကို patched ဗားရှင်းသို့ မြှင့်တင်ခဲ့သည်။
- **03-GettingStarted/samples/javascript**: `npm audit fix` က တင်သွင်းထားသော `hono` (moderate) ကို patched ဗားရှင်းသို့ မြှင့်တင်ခဲ့သည်။
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` က တင်သွင်းထားသော `form-data` (high) ကို patched ဗားရှင်းသို့ မြှင့်တင်ခဲ့သည်။
- **03-GettingStarted/11-simple-auth/solution/typescript**: ချို့တဲ့ထားသော `package-lock.json` ဖိုင်ကို ဖန်တီးခဲ့ပြီး project ကို ထပ်မံပြန်လုပ်ဆောင်နိုင်ရန်နှင့် စစ်ဆေးနိုင်ရန် ပြုလုပ်ထားသည် (ချို့ယွင်းချက် 0)

#### ကိုဒ်အဆင့် လုံခြုံရေး ပြင်ဆင်မှု (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` ကိရိယာထဲမှ `shell=True` ကို ဖယ်ရှားလိုက်ပါသည်။ ယခင်က `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` သည် folder လမ်းကြောင်းအတွင်းရှိ shell metacharacters များကို `cmd.exe` မှ interpret ပြုခြင်းဖြင့် command-injection ရလာစေသည်။ ယခုတွင် `Code.exe` ကို တိုက်ရိုက် folder လမ်းကြောင်းနဲ့ဖြင့် စတင်ပေးပြီး shell မပါဝင်သောနည်းဖြင့် လုပ်ဆောင်ပြီး လုံခြုံမှုရှိသော နည်းလမ်းဖြစ်သည်။

#### Python မူဝါဒ စစ်ဆေးမှု

- `pip-audit` ဖြင့် Python requirements အားလုံးကို စစ်ဆေးခဲ့ပါသည်။ `05-AdvancedTopics` နှင့် `03-GettingStarted/samples/python` မှာ **မသိရှိရသေးသော ချို့ယွင်းချက် မရှိပါ** (၎င်းတို့၏ `mcp` / `httpx` / `pydantic` / `python-dotenv` မူဝါဒများသည် လက်ရှိ patched ဗားရှင်းများနှင့် ကိုက်ညီသည်)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` က transitive မူဝါဒ **`werkzeug` 3.1.1** ကို သုံးခု `safe_join` Windows device-name DoS advisory များဖြင့် အမှတ်အသားပြုပြီးဖြစ်သည် – `CVE-2025-66221`, `CVE-2026-21860`, နှင့် `CVE-2026-27199` (အားလုံးကို 3.1.6 မှာပြင်ဆင်ပြီး)။ ရရှိထားသည့် security pin `werkzeug>=3.1.6` ကို ထည့်သွင်းပြီး patched ထုတ်ပြန်မှုကို ဖြေရှင်းစေခဲ့ပါသည်။ ၎င်းကို `chainlit` / `mcp` / `semantic-kernel` stack နဲ့ သေချာစွာ စစ်ဆေးပြီး ဖြေရှင်းနိုင်စေခဲ့သည်။

### ထုတ်ကုန်အမည် ပြင်ဆင် ပြောင်းလဲမှု

သင်ရိုးညွှန်းအကြောင်းအရာအားလုံးကို Microsoft ၏ ထုတ်ကုန် အမှတ်တံဆိပ် ပြောင်းလဲမှုအရ ပြင်ဆင်ပြီး အသစ်ပြုလုပ်ခဲ့သည်။


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord စိန်ဖွင့်လင့်ခ်ကို အသစ်ပြင်ဆင်ခဲ့သည်

- **AGENTS.md**: Discord ဆာဗာကိုရည်ညွှန်းချက်အသစ်ဖြင့် update လုပ်ပြီး
- **README.md**: နည်းပညာအချက်အလက် ecosystem ကို update လုပ်ပြီး
- **study_guide.md**: ကိစ္စလေ့လာမှုရည်ညွှန်းချက်အသစ်များဖြင့် update လုပ်ပြီး
- **05-AdvancedTopics/README.md**: Module 5.13 ခေါင်းစဉ်နှင့် ဖော်ပြချက်အသစ်များဖြင့် update လုပ်ပြီး
- **05-AdvancedTopics/mcp-integration/README.md**: အပိုင်းခေါင်းစဉ်နှင့်ဖော်ပြချက်များကို update လုပ်ပြီး
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: မော်ဂျူးနံပါတ်နှင့် အကြောင်းအရာအားလုံးကို ပြန်လည်ပြင်ဆင်ပြီး
- **05-AdvancedTopics/mcp-security-entra/README.md**: ကြားဆက်ရည်ညွှန်းထားသော လင့်ခ်ကို update လုပ်ပြီး
- **07-LessonsfromEarlyAdoption/README.md**: ကိစ္စလေ့လာမှု ဥပမာများကို update လုပ်ပြီး
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: အတွဲ ၉ ခေါင်းစဉ်၊ ဂုဏ်သတ္တိများနှင့် တတ်နိုင်မှုပြဇာတ်များကို update လုပ်ပြီး
- **08-BestPractices/README.md**: Discord community လင့်ခ်ကို update လုပ်ပြီး
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discord ချန်နယ်အတည်ပြုချက်ကို update လုပ်ပြီး
- **09-CaseStudy/docs-mcp/solution/python/README.md**: မော်ဒယ် တပ်ဆင်မှုအညွှန်းကို update လုပ်ပြီး
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI ဝန်ဆောင်မှုစာရင်းကို update လုပ်ပြီး
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: အရင်းအမြစ်များကို update လုပ်ပြီး

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: ပင်မ သင်ရိုးညွှန်းချက်များကို update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: မော်ဂျူးခေါင်းစဉ်၊ အနှစ်ချုပ်နှင့် မော်ဂျူးအပိုင်းခေါင်းစဉ်အားလုံး update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: ခေါင်းစဉ်၊ သင်ယူရမည့်ရည်ရွယ်ချက်များ၊ စတင်သတ်မှတ်ချက်နှင့် အရင်းအမြစ်များ update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: ခေါင်းစဉ်၊ သင်ယူရမည့်ရည်ရွယ်ချက်များ၊ MCP ဟုတ်များစာရင်းနှင့် ကြားဆက်ပေးချက်များ update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: ခေါင်းစဉ်၊ ဂုဏ်ဆောင်များ၊ ဖြစ်စေမှုရှေ့စွာလိုအပ်ချက်များနှင့် အရင်းအမြစ်များ update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Agent Builder ရည်ညွှန်းချက်များနှင့် တုံ့ပြန်ချက်လင့်ခ်ကို update လုပ်ပြီး
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: 必要条件များနှင့် extension ရည်ညွှန်းချက်များကို update လုပ်ပြီး

---

## 2026 ခုနှစ်၊ ဧပြီလ 11 ရက်

### သင်ခန်းစာအသစ်၊ စာတမ်းပြင်ဆင်မှုများ၊ အခြေခံပစ္စည်းများကို update လုပ်ခြင်း

#### သင့်သို့ မိတ်ဆက်ထားသည့် သင်ခန်းစာခေါင်းစဉ်အသစ်များ

**Module 05 - အဆင့်မြင့်အကြောင်းအရာများ**
- **Lesson 5.17: MCP နှင့် Adversarial Multi-Agent Reasoning** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): multi-agent စနစ်များအတွက် adversarial debate ပုံစံအပြည့်အစုံလမ်းညွှန်
  - Mermaid ပုံစံ ဖေါ်ပြချက်: ၂ ဂျင်နီယပ်များ → ပြန်ခွဲဝေချင် MCP ဆာဗာ → ဆွေးနွေးချက်စာတမ်း → တရားသူကြီး → ဆုံးဖြတ်ချက်
  - Python နှင့် TypeScript ဖြင့် ထုတ်လုပ်ထားသော 공유 MCP tool ဆာဗာ (`web_search` + `run_python`)
  - ဆန့်ကျင်ဘက်စနစ် prompt များ (FOR / AGAINST / တရားသူကြီး) နှင့် ထုတ်လုပ်မှု အသုံးပြုမှုလိုအပ်ချက်များပါရှိခြင်း
  - Python, TypeScript, C# ဖြင့် ဆွေးနွေးချက် စီမံခန့်ခွဲသူ (debate orchestrator) အား စိမ်ရှုတ်မှုများနှင့် တုံ့ပြန်ချက်ကြောင်း ချိတ်ဆက်နေခြင်း
  - MCP `ClientSession` ကို orchestrator အတွက် အမှန် tool ခေါ်ဆိုမှုများအတွက် wiring ပြုလုပ်ခြင်း
  - အသုံးပြုမှု ဇယား (hallucination ရှာဖွေခြင်း, အန္တရာယ်ပုံစံမြှောက်ခြင်း, API ဒီဇိုင်းစစ်ဆေးခြင်း, အချက်အလက်အတည်ပြုခြင်း, နည်းပညာ ရွေးချယ်ခြင်း)
  - လုံခြုံမှုအတွက် စဉ်းစားချက်များ: sandboxed အမိန့်သွင်းမှု, tool ခေါ်စစ်တမ်း, အမြန်နှုန်းကန့်သတ်ခြင်း, စစ်ဆေးမှတ်တမ်းပြုခြင်း
  - ကုဒ်စစ်ဆေးခြင်း, အင်ဂျင်နီယာဆုံးဖြတ်ချက်များ, ပါဝင်စီမံခန့်ခွဲမှု တို့ပါဝင်သည့် လက်တွေ့လေ့ကျင့်ခန်းသုံးခုပါဝင်သော ပြုလုပ်မှု

#### စာတမ်းပြင်ဆင်မှုများ

**Module 03 - စတင်အသုံးပြုခြင်း**
- **05-stdio-server/README.md**: ပြင်ဆင်ထားသော TypeScript stdio server နမူနာ - သယ်ယူပို့ဆောင်မှု object instantiation (`new StdioServerTransport()`) နှင့် `server.connect(transport)` ခေါ်ဆိုမှု မပါသေးသောအပ်ဒိတ်ပြုလုပ်ပြီး၊ Python နှင့် .NET ဥပမာများနှင့် သေချာထိရောက်မှု ဘိုက်တောင်းပါကောင်း
- **14-sampling/README.md**: လုံးမတည့်သော စာလုံးမှားပြင်သည် - `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### သင်ရိုးညွှန်းချက်များ ပြင်ဆင်ခြင်း

**Main README.md**
- သင်ခန်းစာ 5.17 (MCP နှင့် Adversarial Multi-Agent Reasoning) ကိုသင်ရိုးဇယားတွင်ထည့်သွင်း၍ အသစ်သင်ခန်းစာကိုတိုက်ရိုက် လင့်ခ်ပေးသည်

**05-AdvancedTopics/README.md**
- သင်ခန်းစာ 5.17 ကို သင်ခန်းစာဇယားတွင် ထည့်သွင်းသည်

**study_guide.md**
- Advanced Topics ၏ စိတ်ကူးဇယားနှင့် စာတမ်းအကျဉ်းတွင် Adversarial Multi-Agent Reasoning ခေါင်းစဉ် ထည့်သွင်း ပြင်ဆင်သည်

#### ကုဒ်နှင့် လုံခြုံရေး ပြင်ဆင်မှုများ

**Module 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **လုံခြုံရေးပြုပြင်ချက် — command injection**: TypeScript `run_python` tool တွင် `execSync` shell interpolation ကို `execFile` + `promisify` ဖြင့် အစားထိုးပြီး command injection ရာဇဝတ်မှု ကန့်သတ် (LLM ထိန်းချုပ်ထားသောကုဒ်ကို shell ပါမပါဘဲ literal argv element အနေနှင့် ပို့ဆောင်သည်)
- **MCP tool loop wiring**: Python debate orchestrator ကို `AsyncAnthropic` client (block ဖြစ်သော sync `Anthropic` အစား) သုံး၍ အသစ်ပြင်ဆင်၊ agent တစ်ယောက်ချင်း turn တစ်ခုစီအတွက် သက်ရှိ `ClientSession` ပေးပို့၊ turn နဲ့တိုက်ရိုက် `session.list_tools()` ဖြင့် tool ကုဒ်စစ်ဆေးပြီး `session.call_tool()` ဖြင့် loop ထဲတွင် `tool_use` block များဖြန့်တက်၊ နောက်ဆုံး model ဖြစ်စာတမ်းထွက်လာသည်။

#### အခြေခံပစ္စည်းများ Update

- `hono` ကို 4.12.12 မှာ ပြောင်းလဲ (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows များတွင်)
- TypeScript packages တွင် `@hono/node-server` ကို 1.19.11 မှ 1.19.13 သို့တိုးမြှင့်
- Python packages (10-StreamliningAIWorkflows lab 3 နှင့် 4 တွင်) တွင် `cryptography` ကို 46.0.5 မှ 46.0.7 သို့တိုးမြှင့်
- 10-StreamliningAIWorkflows inspector တွင် `lodash` ကို 4.17.23 မှ 4.18.1 သို့ တိုးမြှင့်

#### ဘာသာပြန်

- နောက်ဆုံး source ပြောင်းလဲမှုများနှင့် 48+ ဘာသာစကားများအတွက် ဘာသာပြန်ချက်များ ကိုက်ညီရေးဆွဲပြီး (i18n update)

---

## 2026 ခုနှစ် ဖေဖော်ဝါရီလ 5 ရက်

### စုစုပေါင်း Repository အသက်သာဆုံးစနစ်နှင့် ကြားဆက် တိုးတက်မှုများ

#### သင်ရိုးညွှန်းချက် အသစ်ထည့်သွင်းခြင်း

**Module 03 - စတင်အသုံးပြုခြင်း**
- **12-mcp-hosts/README.md**: MCP ဟုတ်များ စတင်တပ်ဆင်နည်း အသေးစိတ်လမ်းညွှန်ချက် အသစ်
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf တပ်ဆင်ရေး ဥပမာများ
  - အဓိက MCP ဟုတ်များအတွက် JSON configuration စံနမူနာများ
  - သယ်ယူပို့ဆောင်မှု အမျိုးအစားများ နှိုင်းယှဉ်ဇယား (stdio, SSE/HTTP, WebSocket)
  - မကြာခဏ ဖြစ်ပေါ်သော ဆက်သွယ်မှု ပြဿနာများ ကို ဖြေရှင်းနည်းလမ်းများ
  - ဟုတ်များ တပ်ဆင်ရာတွင် လုံခြုံရေး လမ်းညွှန်ချက်များ

- **13-mcp-inspector/README.md**: MCP Inspector အတွက် debugging လမ်းညွှန်ချက် အသစ်
  - 설치နည်းများ (npx, npm global, Source မှ)
  - stdio နဲ့ HTTP/SSE တို့အပေါ် ဆာဗာချိတ်ဆက်နည်း
  - စမ်းသပ်မှု tools, resources, prompts workflow များ
  - MCP Inspector နှင့် VS Code ပေါင်းစည်းမှု
  - ရိုးရာ debugging နည်းလမ်းများနှင့် ဖြေရှင်းချက်များ

**Module 04 - လက်တွေ့အသုံးပြုခြင်း**
- **pagination/README.md**: pagination အသစ် တည်ဆောက်နည်း
  - Python, TypeScript, Java တွင် cursor-based pagination ပုံစံများ
  - Client က ဘက် pagination ကို အုပ်ချုပ်နည်း
  - Cursor ဒီဇိုင်း များ (opaque နှင့် structured)
  - ထိရောက်မှု မြှင့်တင်အကြံပြုချက်များ

**Module 05 - အဆင့်မြင့်အကြောင်းအရာများ**
- **mcp-protocol-features/README.md**: protocol features အသစ် စုံလင်စွာ ရှင်းပြချက်
  - လုပ်ငန်းတိုးတက်မှု သတင်းပေးချက်များ အကောင်အထည်ဖော်ခြင်း
  - အမိန့် ပယ်ဖျက်ခြင်းစနစ်များ
  - URI ပုံစံ resource templates များ
  - ဆာဗာ အသက်သက်တမ်း စီမံခန့်ခွဲမှု
  - မှတ်တမ်းတင်မှု အဆင့် ထိန်းချုပ်မှု
  - JSON-RPC ကုဒ်များနှင့် အမှားဖြေရှင်းခြင်း ပုံစံများ

#### ကြားဆက် ပြင်ဆင်မှုများ (24+ ဖိုင်များ update လုပ်ပြီး)

**ပင်မ Module README များ**
 ယခု သင်ခန်းစာအရင်တစ်ခုနှင့် နောက် Module နှစ်ခုစလုံးသို့ လင့်ခ်ပေးပြီး

**02-Security Sub-files**
- လုံခြုံရေး ဆောင်းပါး ၅ ခုအားလုံးတွင် "What’s Next" navigation ထည့်သွင်းပြီး

**09-CaseStudy ဖိုင်များ**
- ဉပမာဖိုင်များအားလုံးတွင် အဆက်မပြတ် navigation ပုံစံ ပေးသွင်းပြီး

**10-StreamliningAI Labs**
Module 10 အနှစ်ချုပ်နှင့် Module 11 တွင် What’s Next အပိုင်း ထည့်သွင်းပြီး

#### ကုဒ်နှင့် အကြောင်းအရာ ပြင်ဆင်မှုများ

**SDK နှင့် အခြေခံပစ္စည်းများ Update**
empty openai ဗားရှင်းကို `^4.95.0` မှန်ကန်အောင်ပြင်ဆင်ပြီး
SDK ကို `^1.8.0` မှ `>=1.26.0` သို့ update လုပ်ပြီး
mcp ဗားရှင်း pin များကို `>=1.26.0` သို့ update ပြုလုပ်ထားသည်

**ကုဒ် ပြင်ဆင်မှုများ**
မမှန်ကန်သော model `gpt-4o-mini` ကို `gpt-4.1-mini` ဖြင့်ပြင်ဆင်ထားသည်

**အကြောင်းအရာ ပြင်ဆင်မှုများ**
link ပြတ်နေသော `READMEmd` ကို `README.md` ဖြင့်ပြင်၊ သင်ရိုး ခေါင်းစဉ် `Module 1-3` ကို `Module 0-3` ဖြင့်ပြင်၊ အမည်တွက်ချက်မှု sensitive path များအတွက် ပြင်ဆင်မှုများ
ကွဲပြားမှုပြဿနာပါတဲ့ Case Study 5 အကြောင်းအရာ မူရင်းအားဖယ်ရှားပြီး

**အသစ် စတင်သူများအတွက် လမ်းညွှန်မှု အရာများ တိုးတက်အောင် ပြုလုပ်ခြင်း**
စတင်သူများအတွက် မိတ်ဆက်ချက်, သင်ယူရမည့်ရည်ရွယ်ချက်များနှင့် လိုအပ်ချက်များကို ထည့်သွင်းထားသည်

#### သင်ရိုးညွှန်းချက် ပြင်ဆင်မှုများ

**Main README.md**
- သင်ရိုးဇယားတွင် 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) အသစ် ထည့်သွင်းပြီး

**Module README များ**
သင်ခန်းစာ 12 နှင့် 13 ကို သင်ခန်းစာစာရင်းတွင် ထည့်သွင်းပြီး
စိတ်ကြိုက်လမ်းညွှန်များ အနေနဲ့ pagination အပိုင်း ထည့်သွင်းပြီး
သင်ခန်းစာ 5.15 (Custom Transport) နှင့် 5.16 (Protocol Features) ထည့်သွင်းထားသည်

**study_guide.md**
- MCP Hosts Setup, MCP Inspector, Pagination Strategies, Protocol Features Deep Dive အပါအဝင် အသစ်သော ခေါင်းစဉ်များအား စိတ်ကူးဇယားတွင် ထည့်သွင်းထားသည်

## 2026 ခုနှစ်၊ ဇန်နဝါရီလ 28 ရက်

### MCP Specification 2025-11-25 ကိုလိုက်နာမှု ပြန်သုံးသပ်ခြင်း

#### အဓိက အသိပညာ မြှင့်တင်ခြင်း (01-CoreConcepts/)
- **Client Primitive အသစ် - Roots**: Servers များအား ဖိုင်စနစ်နယ်နိမိတ်များနှင့် လက်လွှတ်ခွင့်များကို နားလည်နိုင်စေသော Roots client primitive အတွက် စာတမ်းအပြည့်အစုံ ထည့်သွင်းခဲ့သည်
- **Tool Annotations**: ကောင်းမွန်သော tool အလုပ်လုပ်မှု ဆုံးဖြတ်ချက်များအတွက် tool behavioral annotations (`readOnlyHint`, `destructiveHint`) စာတမ်း ထည့်သွင်းပြီး
- **Sampling တွင် Tool ခေါ်ဆိုမှု**: Sampling တောင်းဆိုမှုများ မှာ model ပြန်ခေါ်ထုတ်မှုအတွက် `tools` နှင့် `toolChoice` ပါရာမီတာများ ထည့်သွင်းပြီး အသစ်ပြင်ဆင်ထားသည်
- **URL Mode Elicitation**: ဆာဗာမှ ပြင်ပ ဝဘ် လှုပ်ရှားမှုများ အတွက် URL-based elicitation စာတမ်းများ ထည့်သွင်းထားသည်
- **Tasks (စမ်းသပ်ရေး)**: ခိုင်မာသော လုပ်ဆောင်မှု ထုပ်ယူမှုနှင့် deferred result retrieval အတွက် experimental Tasks feature စာတမ်းအသစ် ထည့်သွင်းထားသည်
- **Icons ဖော်ပြချက်**: tools, resources, resource templates, နှင့် prompts များတွင် အပို metadata အဖြစ် icons ပေးနိုင်ကြောင်းဖြစ်သော အချက်များ ထည့်သွင်းသည်

#### စာတမ်း ပြင်ဆင်မှုများ
- **README.md**: MCP Specification 2025-11-25 ဗားရှင်း အညွှန်းစာနှင့် ရက်စွဲခံ versioning 설명 ထည့်သွင်းထားသည်
- **study_guide.md**: Core Concepts အပိုင်းတွင် Tasks နှင့် Tool Annotations ထည့်သွင်းပြီး စာတမ်း အချိန်လက္ခဏာ ပြင်ဆင်ထားသည်

#### Specification ကိုလိုက်နာမှု အတည်ပြုခြင်း
- **Protocol ဗားရှင်း**: MCP Specification 2025-11-25 နောက်ဆုံး ဗားရှင်းကို အကုန်လုံး စစ်ဆေးပြီး အသုံးပြုမှုကို အတည်ပြုထားသည်
- **Architecture ကိုက်ညီမှု**: နှစ်အတန်း Architecture (Data Layer + Transport Layer) စာတမ်းတိကျမှုကို အတည်ပြုထားသည်
- **Primitives စာတမ်းများ**: server primitives (Resources, Prompts, Tools) နှင့် client primitives (Sampling, Elicitation, Logging, Roots) စာတမ်းများ အတည်ပြုပြီး
- **Transport စနစ်များ**: STDIO နှင့် Streamable HTTP transport စာတမ်းတိကျမှုကို အတည်ပြုထားသည်
- **လုံခြုံရေး လမ်းညွှန်ချက်များ**: MCP လုံခြုံရေး အကောင်းဆုံး လမ်းညွှန်ချက်များနှင့် ကိုက်ညီမှု အတည်ပြုသည်

#### MCP 2025-11-25 အရေးပါသော လက္ခဏာများ စာတမ်းအသစ်များ
- **OpenID Connect ရှာဖွေရေး**: OIDC ဖြင့် Auth ဆာဗာ ရှာဖွေခြင်းလုပ်ငန်းစဉ်
- **OAuth Client ID Metadata စာတမ်းများ**: client မှတ်ပုံတင်စနစ်အကြံပြုချက်
- **JSON Schema 2020-12**: MCP schema အဓိက ရိုးရာစကားသို့ပြောင်းလဲရေး
- **SDK Tiering System**: SDK ဖျော်ဖြေမှုနှင့် သမားတန်းမှုပိုင်းမူဝါဒ
- **အစိုးရ ထိန်းချုပ်မှု ဖွဲ့စည်းမှု**: MCP အုပ်ချုပ်သူအဖွဲ့များနှင့် အကျိုးစီးပွားအဖွဲ့များ ဖော်ပြချက်

### လုံခြုံရေး စာတမ်း အကြီးစား Update (02-Security/)

#### MCP Security Summit Workshop (Sherpa) ပေါင်းခြင်း
- **အသစ် တည်ဆောက်ထားသော လက်တွေ့သင်ကြားမှု သင့်အားဖြည့်ပစ္စည်း**: [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) နှင့် များစွာသော လုံခြုံရေး စာတမ်းများ ပေါင်းစည်းမှု
- **တောင်ကြီးခရီးလမ်းညွှန်စုစည်းမှု**: Base Camp မှ Summit ထိ အဆင့်ဆင့် ခရီးစဉ် ဖော်ပြချက်
- **OWASP ကိုက်ညီမှု**: လုံခြုံရေး လမ်းညွှန်ချက်များအားလုံးကို OWASP MCP Azure Security Guide ရှုပ်ထွေးမှု အတိုင်းအတာနှင့် ချိန်ညှိပြီး

#### OWASP MCP Top 10 ပေါင်းခြင်း
- **အပိုင်းအသစ်**: OWASP MCP Top 10 လုံခြုံရေး အန္တရာယ်ဇယားနှင့် Azure ကာကွယ်မှုများ အဓိက လုံခြုံရေး README မှာ ထည့်သွင်းထားသည်
- **အန္တရာယ် အခြေပြု စာတမ်းများ**: mcp-security-controls-2025.md တွင် OWASP MCP အန္တရာယ်များအတွက် မြေပုံများ ထည့်သွင်းထားပြီး (MCP01-MCP08)
- **ကိုးကားဖော်ပြချက် Architecture**: OWASP MCP Azure Security Guide ရဲ့ reference architecture နှင့် လက်တွေ့အခြေအနေ ပုံစံများနှင့် ချိတ်ဆက်ထားသည်

#### security ဖိုင်များ ပြင်ဆင်ခြင်း
- **README.md**: Sherpa Workshop အကြောင်းအရာ, ခရီးလမ်းညွှန်ဇယား, OWASP MCP Top 10 အန္တရာယ် အကျဉ်းသုံးသပ်ချက်နှင့် လက်တွေ့သင်တန်း အပိုင်းများ ထည့်သွင်းထားသည်
- **mcp-security-controls-2025.md**: ဖော်ပြချက်ခေါင်းစဉ်ကို 2026 ခုနှစ် ဖေဖော်ဝါရီအထိ ပြောင်းပြီး OWASP အန္တရာယ် ကိုးကားချက်များ ထည့်သွင်းထားသည် (MCP01-MCP08), ဗားရှင်း မတူညီမှု ပြင်ဆင်
- **mcp-security-best-practices-2025.md**: Sherpa နှင့် OWASP ရင်းမြစ်စာရင်း ထည့်သွင်းပြီး အချိန်အမှတ်တမ်း ပြင်ဆင်
- **mcp-best-practices.md**: လက်တွေ့သင်တန်း အပိုင်း Sherpa နှင့် OWASP လင့်ခ်များထည့်သွင်းထားသည်
- **azure-content-safety-implementation.md**: OWASP MCP06 ကိုးကားချက်၊ Sherpa Camp 3 ကိုက်ညီမှု ၊ အပိုရင်းမြစ်များ ထည့်သွင်းထားသည်

#### အရင်းအမြစ် Link အသစ်များ ထည့်သွင်းထား
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Individual OWASP MCP risk pages (MCP01-MCP10)

### Curriculum-Wide MCP Specification 2025-11-25 Alignment

#### Module 03 - Getting Started
- **SDK Documentation**: Added Go SDK to official SDK list; updated all SDK references to align with MCP Specification 2025-11-25
- **Transport Clarification**: Updated STDIO and HTTP Streaming transport descriptions with explicit spec references

#### Module 04 - Practical Implementation
- **SDK Updates**: Added Go SDK; updated SDK list with specification version reference
- **Authorization Spec**: Updated MCP Authorization specification link to current 2025-11-25 version

#### Module 05 - Advanced Topics
- **New Features**: Added note about new MCP Specification 2025-11-25 features (Tasks, Tool Annotations, URL Mode Elicitation, Roots)
- **Security Resources**: Added OWASP MCP Top 10 and Sherpa workshop links to additional references

#### Module 06 - Community Contributions
- **SDK List**: Added Swift and Rust SDKs; updated specification link to 2025-11-25
- **Spec Reference**: Updated MCP Specification link to direct specification URL

#### Module 07 - Lessons from Early Adoption
- **Resource Updates**: Added MCP Specification 2025-11-25 link and OWASP MCP Top 10 to additional resources

#### Module 08 - Best Practices
- **Spec Version**: Updated MCP Specification reference to 2025-11-25
- **Security Resources**: Added OWASP MCP Top 10 and Sherpa workshop to additional references

#### Module 10 - Streamlining AI Workflows
- **Badge Update**: Changed MCP version badge from SDK version (1.9.3) to specification version (2025-11-25)
- **Resource Links**: Updated MCP Specification link; added OWASP MCP Top 10

#### Module 11 - MCP Server Hands-On Labs
- **Spec Reference**: Updated MCP Specification link to 2025-11-25 version
- **Security Resources**: Added OWASP MCP Top 10 to official resources

## December 18, 2025

### Security Documentation Update - MCP Specification 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specification Version Update
- **Protocol Version Update**: Updated to reference latest MCP Specification 2025-11-25 (released November 25, 2025)
  - Updated all specification version references from 2025-06-18 to 2025-11-25
  - Updated document date references from August 18, 2025 to December 18, 2025
  - Verified all specification URLs point to current documentation
- **Content Validation**: Comprehensive validation of security best practices against latest standards
  - **Microsoft Security Solutions**: Verified current terminology and links for Prompt Shields (previously "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID, and Azure Key Vault
  - **OAuth 2.1 Security**: Confirmed alignment with latest OAuth security best practices
  - **OWASP Standards**: Validated OWASP Top 10 for LLMs references remain current
  - **Azure Services**: Verified all Microsoft Azure documentation links and best practices
- **Standards Alignment**: All referenced security standards confirmed current
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure security and compliance frameworks
- **Implementation Resources**: Validated all implementation guide links and resources
  - Azure API Management authentication patterns
  - Microsoft Entra ID integration guides
  - Azure Key Vault secrets management
  - DevSecOps pipelines and monitoring solutions

### Documentation Quality Assurance
- **Specification Compliance**: Ensured all mandatory MCP security requirements (MUST/MUST NOT) align with latest specification
- **Resource Currency**: Verified all external links to Microsoft documentation, security standards, and implementation guides
- **Best Practices Coverage**: Confirmed comprehensive coverage of authentication, authorization, AI-specific threats, supply chain security, and enterprise patterns

## October 6, 2025

### Getting Started Section Expansion – Advanced Server Usage & Simple Authentication

#### Advanced Server Usage (03-GettingStarted/10-advanced)
- **New Chapter Added**: Introduced a comprehensive guide to advanced MCP server usage, covering both regular and low-level server architectures.
  - **Regular vs. Low-Level Server**: Detailed comparison and code examples in Python and TypeScript for both approaches.
  - **Handler-Based Design**: Explanation of handler-based tool/resource/prompt management for scalable, flexible server implementations.
  - **Practical Patterns**: Real-world scenarios where low-level server patterns are beneficial for advanced features and architecture.

#### Simple Authentication (03-GettingStarted/11-simple-auth)
- **New Chapter Added**: Step-by-step guide to implementing simple authentication in MCP servers.
  - **Auth Concepts**: Clear explanation of authentication vs. authorization, and credential handling.
  - **Basic Auth Implementation**: Middleware-based authentication patterns in Python (Starlette) and TypeScript (Express), with code samples.
  - **Progression to Advanced Security**: Guidance on starting with simple auth and advancing to OAuth 2.1 and RBAC, with references to advanced security modules.

These additions provide practical, hands-on guidance for building more robust, secure, and flexible MCP server implementations, bridging foundational concepts with advanced production patterns.

## September 29, 2025

### MCP Server Database Integration Labs - Comprehensive Hands-On Learning Path

#### 11-MCPServerHandsOnLabs - New Complete Database Integration Curriculum
- **Complete 13-Lab Learning Path**: Added comprehensive hands-on curriculum for building production-ready MCP servers with PostgreSQL database integration
  - **Real-World Implementation**: Zava Retail analytics use case demonstrating enterprise-grade patterns
  - **Structured Learning Progression**:
    - **Labs 00-03: Foundations** - Introduction, Core Architecture, Security & Multi-Tenancy, Environment Setup
    - **Labs 04-06: Building the MCP Server** - Database Design & Schema, MCP Server Implementation, Tool Development  
    - **Labs 07-09: Advanced Features** - Semantic Search Integration, Testing & Debugging, VS Code Integration
    - **Labs 10-12: Production & Best Practices** - Deployment Strategies, Monitoring & Observability, Best Practices & Optimization
  - **Enterprise Technologies**: FastMCP framework, PostgreSQL with pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Advanced Features**: Row Level Security (RLS), semantic search, multi-tenant data access, vector embeddings, real-time monitoring

#### Terminology Standardization - Module to Lab Conversion
- **Comprehensive Documentation Update**: Systematically updated all README files in 11-MCPServerHandsOnLabs to use "Lab" terminology instead of "Module"
  - **Section Headers**: Updated "What This Module Covers" to "What This Lab Covers" across all 13 labs
  - **Content Description**: Changed "This module provides..." to "This lab provides..." throughout documentation
  - **Learning Objectives**: Updated "By the end of this module..." to "By the end of this lab..." 
  - **Navigation Links**: Converted all "Module XX:" references to "Lab XX:" in cross-references and navigation
  - **Completion Tracking**: Updated "After completing this module..." to "After completing this lab..."
  - **Preserved Technical References**: Maintained Python module references in configuration files (e.g., `"module": "mcp_server.main"`)

#### Study Guide Enhancement (study_guide.md)
- **Visual Curriculum Map**: Added new "11. Database Integration Labs" section with comprehensive lab structure visualization
- **Repository Structure**: Updated from ten to eleven main sections with detailed 11-MCPServerHandsOnLabs description
- **Learning Path Guidance**: Enhanced navigation instructions to cover sections 00-11
- **Technology Coverage**: Added FastMCP, PostgreSQL, Azure services integration details
- **Learning Outcomes**: Emphasized production-ready server development, database integration patterns, and enterprise security

#### Main README Structure Enhancement
- **Lab-Based Terminology**: Updated main README.md in 11-MCPServerHandsOnLabs to consistently use "Lab" structure
- **Learning Path Organization**: Clear progression from foundational concepts through advanced implementation to production deployment
- **Real-World Focus**: Emphasis on practical, hands-on learning with enterprise-grade patterns and technologies

### Documentation Quality & Consistency Improvements
- **Hands-On Learning Emphasis**: Reinforced practical, lab-based approach throughout documentation
- **Enterprise Patterns Focus**: Highlighted production-ready implementations and enterprise security considerations
- **Technology Integration**: Comprehensive coverage of modern Azure services and AI integration patterns
- **Learning Progression**: Clear, structured path from basic concepts to production deployment

## September 26, 2025

### Case Studies Enhancement - GitHub MCP Registry Integration

#### Case Studies (09-CaseStudy/) - Ecosystem Development Focus
- **README.md**: Major expansion with comprehensive GitHub MCP Registry case study
  - **GitHub MCP Registry Case Study**: New comprehensive case study examining GitHub's MCP Registry launch in September 2025
    - **Problem Analysis**: Detailed examination of fragmented MCP server discovery and deployment challenges
    - **Solution Architecture**: GitHub's centralized registry approach with one-click VS Code installation
    - **Business Impact**: Measurable improvements in developer onboarding and productivity
    - **Strategic Value**: Focus on modular agent deployment and cross-tool interoperability
    - **Ecosystem Development**: Positioning as foundational platform for agentic integration
  - **Enhanced Case Study Structure**: Updated all seven case studies with consistent formatting and comprehensive descriptions
    - Azure AI Travel Agents: Multi-agent orchestration emphasis
    - Azure DevOps Integration: Workflow automation focus
    - Real-Time Documentation Retrieval: Python console client implementation
    - Interactive Study Plan Generator: Chainlit conversational web app
    - In-Editor Documentation: VS Code and GitHub Copilot integration
    - Azure API Management: Enterprise API integration patterns
    - GitHub MCP Registry: Ecosystem development and community platform
  - **Comprehensive Conclusion**: Rewritten conclusion section highlighting seven case studies spanning multiple MCP implementation dimensions
    - Enterprise Integration, Multi-Agent Orchestration, Developer Productivity
    - Ecosystem Development, Educational Applications categorization
    - Enhanced insights into architectural patterns, implementation strategies, and best practices
    - Emphasis on MCP as mature, production-ready protocol

#### Study Guide Updates (study_guide.md)
- **Visual Curriculum Map**: Updated mindmap to include GitHub MCP Registry in Case Studies section
- **Case Studies Description**: Enhanced from generic descriptions to detailed breakdown of seven comprehensive case studies
- **Repository Structure**: Updated section 10 to reflect comprehensive case study coverage with specific implementation details
- **Changelog Integration**: Added September 26, 2025 entry documenting GitHub MCP Registry addition and case study enhancements
- **Date Updates**: Updated footer timestamp to reflect latest revision (September 26, 2025)

### Documentation Quality Improvements
- **Consistency Enhancement**: Standardized case study formatting and structure across all seven examples
- **Comprehensive Coverage**: Case studies now span enterprise, developer productivity, and ecosystem development scenarios
- **Strategic Positioning**: Enhanced focus on MCP as foundational platform for agentic system deployment
- **Resource Integration**: Updated additional resources to include GitHub MCP Registry link

## September 15, 2025

### Advanced Topics Expansion - Custom Transports & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - New Advanced Implementation Guide
- **README.md**: Complete implementation guide for custom MCP transport mechanisms
  - **Azure Event Grid Transport**: Comprehensive serverless event-driven transport implementation
    - C#, TypeScript, and Python examples with Azure Functions integration
    - Event-driven architecture patterns for scalable MCP solutions
    - Webhook receivers and push-based message handling
  - **Azure Event Hubs Transport**: High-throughput streaming transport implementation
    - Real-time streaming capabilities for low-latency scenarios
    - Partitioning strategies and checkpoint management
    - Message batching and performance optimization
  - **Enterprise Integration Patterns**: Production-ready architectural examples
    - Distributed MCP processing across multiple Azure Functions
    - Hybrid transport architectures combining multiple transport types
    - Message durability, reliability, and error handling strategies
  - **Security & Monitoring**: Azure Key Vault integration and observability patterns
    - Managed identity authentication and least privilege access
    - Application Insights telemetry and performance monitoring
    - Circuit breakers and fault tolerance patterns
  - **Testing Frameworks**: Comprehensive testing strategies for custom transports
    - Unit testing with test doubles and mocking frameworks
    - Integration testing with Azure Test Containers
    - Performance and load testing considerations

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Emerging AI Discipline
- **README.md**: Comprehensive exploration of context engineering as an emerging field
  - **Core Principles**: Complete context sharing, action decision awareness, and context window management

  - **MCP ပရိုတိုကောကျမ်းညွန်ချက်ဖြင့် ကိုက်ညီမှု**: MCP ဒီဇိုင်းက နောက်ခံအင်ဂျင်နီယာ ခက်ခဲမှုတွေကို ဘယ်လိုဖြေပေးတာလဲ
    - နောက်ခံပြတင်းပေါက် ကန့်သတ်မှုများနှင့် တဖြည်းဖြည်း ဒါဏ်ငွေစနစ်များ
    - သက်ဆိုင်မှု သတ်မှတ်ခြင်းနှင့် ဒိုင်နမစ် နောက်ခံ ရယူမှု
    - မူလတန်းစုံဖန်တီးမှု နောက်ခံ ကိုင်တွယ်မှုနှင့် လုံခြုံရေး စဉ်းစားချက်များ
  - **ဆောင်ရွက်ချက်နည်းလမ်းများ**: တစ်သုံးတန်း vs. မျိုးစုံ-အေးဂျင့် စက်မှုဖွဲ့စည်းမှု
    - နောက်ခံချိတ်၊ ရွေးချယ်မှုနည်းလမ်းများ
    - တဖြည်းဖြည်း နောက်ခံ တင်ပို့ခြင်းနှင့် စုပ်ယူမှုနည်းလမ်းများ
    - အဆင့်လိုက်နောက်ခံ နည်းလမ်းများနှင့် ရယူမှုတိုးတက်မှု
  - **တိုင်းတာမှု ဖွဲ့စည်းမှု**: နောက်ခံ ထိရောက်မှု လေ့လာသုံးသပ်ရန် ပေါ်ပေါက်လာသော စာရင်းများ
    - ထည့်သွင်းမှု ထိရောက်မှု၊ စွမ်းဆောင်ရည်၊ အရည်အသွေးနှင့် အသုံးပြုသူ အတွေ့အကြုံ စဉ်းစားချက်များ
    - နောက်ခံ ထိရောက်မှု မြှင့်တင်ရေး ဥပမာစမ်းသပ်ခြင်းနည်းလမ်းများ
    - မအောင်မြင်မှု သောသည့်အချက်များကို စိစစ်၍ တိုးတက်အောင်လုပ်နည်းများ

#### သင်တန်းသင်ကြားမှု လမ်းညွှန် ပြင်ဆင်မှုများ (README.md)
- **တိုးတက်ပြောင်းလဲသော မော်ဒျူး ဖွဲ့စည်းမှု**: သင်တန်းဇယားသစ်တွင် လက်ရှိ မြင့်မားတိုးတက်သော ခေါင်းစဉ်အသစ်များ ထည့်သွင်းထားသည်
  - Context Engineering (5.14) နှင့် Custom Transport (5.15) မှတ်သားချက်သစ်များ ထည့်သွင်းပြီး
  - မော်ဒျူးအားလုံးတွင် အတူတူ ဖော်မက်နှင့် လမ်းညွှန် လင့်များကို ထိန်းသိမ်းထားသည်
  - လက်ရှိ အကြောင်းအရာအတိုင်းအတာများကို ဖော်ပြရန် ဖော်ပြချက်များ ပြောင်းလဲပြင်ဆင်ထားသည်

### ဖိုင်အတိုင်းအတာ တိုးတက်မှုများ
- **အမည်ပြုပြင်ခြင်း စံသတ်မှတ်ချက်**: "mcp transport" ကို "mcp-transport" ဟု အခြားမြင့်မားသော ခေါင်းစဉ်ဖိုလ်ဒါများနှင့် သင်္ကေတတူရန် ပြောင်းလဲထားသည်
- **အကြောင်းအရာ စုပေါင်းဆိုင်ရာ**: 05-AdvancedTopics ဖိုလ်ဒါများအားလုံးမှာ mcp-[topic] ဟူသော အမည်ပုံစံ တူညီစွာလိုက်နာထားသည်

### စာရွက်စာတမ်း အရည်အသွေး မြှင့်တင်ခြင်း
- **MCP သတ်မှတ်ချက် နှင့် ကိုက်ညီမှု**: အားလုံးသော အသစ်များသည် MCP Specification 2025-06-18 စံသတ်မှတ်ချက်နှင့် ကိုက်ညီသည်
- **ဘာသာစကားအမျိုးမျိုး နမူနာများ**: C#, TypeScript, Python အတွက် ကျယ်ပြန့်သော ကိုဒ် နမူနာများ
- **စက်မှုဖော်ရွေမှု အာရုံစိုက်မှု**: သွားရာမြေများအတွက် ပုံသေသည့် နမူနာများနှင့် Azure cloud ပေါင်းစပ်မှု
- **မြင်ကွင်း အောက်မေ့စာတမ်း**: ဖွဲ့စည်းတည်ဆောက်မှုနှင့် လည်ပတ်မှု ဓာတ်ပုံများ အတွက် Mermaid ပေးပို့မှု

## 2025 ခုနှစ် ဇြန်လ 18 ရက်

### စာရွက်စာတမ်း အပြည့်အစုံ မူလတန်း ပြုပြင်ခြင်း - MCP 2025-06-18 စံမူများ

#### MCP လုံခြုံရေး မှန်ကန်သော လုပ်ဆောင်ချက်များ (02-Security/) - ပူးပေါင်းပြုပြင်ခြင်း ပြီးစီး
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP Specification 2025-06-18 နှင့် ကိုက်ညီစွာ ပြန်ရေးသားပြီး
  - **လိုအပ်ချက် မလွဲမရှောင်ချက်များ**: တရားဝင်သတ်မှတ်ချက်များမှ ပြတ်သားသော MUST/MUST NOT လိုအပ်ချက်များ ထည့်သွင်းထားသည်
  - **12 အဓိက လုံခြုံရေး လုပ်ထုံးလုပ်နည်းများ**: 15-items စာရင်းမှ လုံခြုံရေးနယ်ပယ်များသို့ ပြန်လည် စီမံ
    - Token လုံခြုံရေး နှင့် အသိမှတ်ပြုမှု (external identity provider ပေါင်းစပ်မှုပါတော့)
    - ဒေသဆိုင်ရာ စီမံခန့်ခွဲမှု နှင့် သယ်ယူပို့ဆောင်မှု လုံခြုံရေး (cryptographic လိုအပ်ချက်များပါတော့)
    - AI သာလျှင်အတွက် အန္တရာယ်ကာကွယ်မှု Microsoft Prompt Shields ပေါင်းစပ်မှု
    - လက်လှမ်းမီမှု ထိန်းချုပ်မှု နှင့် ခွင့်ပြုချက်များ (principle of least privilege အခြေခံ)
    - အကြောင်းအရာ လုံခြုံမှုနှင့် စောင့်ကြည့်မှု (Azure Content Safety ပေါင်းစပ်မှု)
    - Supply Chain လုံခြုံမှု (တပ်ဆင်မှု လုံခြုံမှု စစ်ဆေးမှု)
    - OAuth လုံခြုံရေး နှင့် Confused Deputy ကာကွယ်မှု (PKCE အကောင်အထည်ဖော်ခြင်း)
    - ဖြစ်ရပ်ကြုံ ရှုပ်ထွေးမှု နှင့် ပြန်လည်ရယူနိုင်မှု (အလိုအလျောက် ထိခိုက်မှု ဖော်ထုတ်မှု)
    - အညီအစဉ်နှင့် အုပ်ချုပ်မှု (စည်းကမ်းမှန် အညီစနစ်ထိန်းသိမ်းခြင်း)
    - မြင့်မားသော လုံခြုံရေး ထိန်းချုပ်မှု (zero trust architecture)
    - Microsoft လုံခြုံရေး စနစ် အလိုက်စပ်ခြင်း (တိုးတက်ပြည့်စုံသော ဖြေရှင်းချက်များ)
    - လုံခြုံရေး ဆက်လက် တိုးတက်ကာ ကျင့်သုံးမှုများ (မဲပေးနေ့စနစ်များ)
  - **Microsoft လုံခြုံရေး ဖြေရှင်းချက်များ**: Prompt Shields, Azure Content Safety, Entra ID, GitHub Advanced Security ပေါင်းစပ်မှုကို ပိုမိုကွဲပြားသိရှိမှုပေးခြင်း
  - **ဆောင်ရွက်ချက် အရင်းအမြစ်များ**: တရားဝင် MCP စာရွက်စာတမ်းများ၊ Microsoft လုံခြုံရေး ဖြေရှင်းချက်များ၊ လုံခြုံရေး စံချိန်များ၊ ဆောင်ရွက်မှုလမ်းညွှန်များ အလိုက် ဂဏန်းခွဲ ဖော်ပြချက်များ

#### မြင့်မားသော လုံခြုံရေး ထိန်းချုပ်မှုများ (02-Security/) - စက်မှုဖော်ရွေမှုဆိုင်ရာ ဆောင်ရွက်မှု
- **MCP-SECURITY-CONTROLS-2025.md**: စက်မှုဖော်ရွေမှု အဆင့် မြင့်လုံခြုံရေး ဖွဲ့စည်းမှု အထူးပြုပြင်ခြင်း
  - **လုံခြုံရေး နယ်ပယ် ၉ ခု ကိုလည်းကောင်းဆုံးဖတ်ရှုခြင်း**: အခြေခံ ထိန်းချုပ်မှုများမှ စက်မှုဖော်ရွေမှု ဖွဲ့စည်းမှုသို့ ကျယ်ပြန့်စွာ တိုးချဲ့ခြင်း
    - မြင့်မားသော အသိမှတ်ပြုမှု နှင့် ခွင့်ပြုမှု Microsoft Entra ID ပေါင်းစပ်မှုပါဝင်သည်
    - Token လုံခြုံရေးနှင့် Anti-Passthrough ထိန်းချုပ်မှုများ စပ်ဆိုင်ထိန်းသိမ်းမှုများပါရှိသည်
    - သဘောဝင်ခြင်း လုံခြုံရေး ထိန်းချုပ်မှုများ (hijacking ကာကွယ်မှု)
    - AI သာလျှင် လုံခြုံရေး ထိန်းချုပ်မှုများ (prompt injection နှင့် tool poisoning ကာကွယ်မှု)
    - Confused Deputy တိုက်ခိုက်မှု ကာကွယ်မှု OAuth proxy လုံခြုံရေးနှင့် ဆက်စပ် ထိန်းသိမ်းမှု
    - Tool ထိန်းချုပ်မှု လုံခြုံရေး (sandboxing နှင့် သီးခြားခြင်း)
    - Supply Chain လုံခြုံရေး ထိန်းချုပ်မှုများ (နေ့စဉ်တိုးတက်ဆဲ စစ်ဆေးမှု)
    - စောင့်ကြည့်ခြင်းနှင့် ရှာဖွေဖော်ထုတ်မှု (SIEM ပေါင်းစပ်မှု)
    - ဖြစ်ရပ် ကြုံ ရှုပ်ထွေးမှုနှင့် ပြန်လည်ရယူနိုင်မှု (အလိုအလျောက် စနစ်များ)
  - **ဆောင်ရွက်မှု ဥပမာများ**: YAML configuration block များနှင့် ကုဒ် နမူနာအသေးစိတ် ထည့်သွင်း
  - **Microsoft ဖြေရှင်းချက် ပေါင်းစပ်မှု**: Azure လုံခြုံရေးဝန်ဆောင်မှုများ, GitHub Advanced Security, စက်မှုဖော်ရွေမှု အမှတ်တံဆိပ်များပြည့်စုံအောင်

#### မြင့်မားသော ခေါင်းစဉ် လုံခြုံရေး (05-AdvancedTopics/mcp-security/) - ကုန်ထုတ်စက်မှုဆိုင်ရာ ဆောင်ရွက်မှု ပြီးစီး
- **README.md**: စက်မှုဖော်ရွေမှု လုံခြုံရေးဆိုင်ရာ ပြန်ရေးသားခြင်း ပြီးစီး
  - **လက်ရှိ သတ်မှတ်ချက် နှင့် ကိုက်ညီမှု**: MCP Specification 2025-06-18 နှင့် လိုအပ်သော လုံခြုံရေး စည်းမျဉ်းများပါဝင်သည်
  - **တိုးတက်သော အသိမှတ်ပြုမှု**: Microsoft Entra ID ပေါင်းစပ်ခြင်း၊ .NET နှင့် Java Spring Security များသော နမူနာများ ပါရှိသည်
  - **AI လုံခြုံရေး ပေါင်းစပ်မှု**: Microsoft Prompt Shields နှင့် Azure Content Safety နမူနာ Python အသေးစိတ်ဖြင့် ပါရှိသည်
  - **မြင့်မားသော အန္တရာယ် ကာကွယ်ခြင်း**: များစွာသော ဆောင်ရွက်မှုနမူနာများ
    - Confused Deputy တိုက်ခိုက်မှု ကာကွယ်ခြင်း (PKCE နှင့် အသုံးပြုသူ သဘောတူညီမှု စစ်ဆေးမှု)
    - Token Passthrough ကာကွယ်မှု (audience ဝေဖန်မှုနှင့် လုံခြုံသော token စီမံခန့်ခွဲမှု)
    - Session Hijacking ကာကွယ်မှု (cryptographic binding နှင့် အသုံးပြုသူ အပြုအမူ သုံးသပ်မှု)
  - **စက်မှုဖော်ရွေမှု လုံခြုံရေး ပေါင်းစပ်မှု**: Azure Application Insights စောင့်ကြည့်မှု၊ အန္တရာယ် ရှာဖွေမှု လမ်းကြောင်းများနှင့် supply chain လုံခြုံမှု
  - **ဆောင်ရွက်မှု စစ်ဆေးမှုစာရင်း**: မြင်သာသော လိုအပ်မှုနှင့် အကြံပြုချက် လုံခြုံရေး ထိန်းချုပ်မှုများ Microsoft လုံခြုံရေး စနစ် အကျိုးကျေးဇူးများ ပါရှိသည်

### စာရွက်စာတမ်း အရည်အသွေး & စံသတ်မှတ်ချက် အညီအတွက်
- **သတ်မှတ်ချက် ရည်ညွှန်းချက်များ**: MCP Specification 2025-06-18 ကိုင်းပေါ် သက်ဆိုင်သော ရည်ညွှန်းချက်အားလုံး ပြင်ဆင်ထားသည်
- **Microsoft လုံခြုံရေး စနစ်**: လုံခြုံရေး စာရွက်စာတမ်းအားလုံးတွင် ပိုမိုကွဲပြားသိရှိမှုရန် အသင်းအဖွဲ့ပေါင်းစပ်နည်းလမ်း
- **လက်တွေ့ ဆောင်ရွက်မှု**: .NET, Java နှင့် Python တွင် စက်မှုအဆင့် အထူးနမူနာများ ထည့်သွင်းထားသည်
- **အရင်းအမြစ် စုပေါင်းမှု**: တရားဝင်စာရွက်စာတမ်းများ၊ လုံခြုံရေး စံချိန်များနှင့် ဆောင်ရွက်မှု လမ်းညွှန်များ အလိုက် ကဏ္ဍခွဲ ပြုလုပ်ထားသည်
- **မြင်သာသော အမှတ်အသားများ**: လိုအပ်ချက် ပျော်မှုနှင့် အကြံပြုချက် ပြုလုပ်ချက်များကို ဖော်ပြထားသည်


#### အဓိက အကြောင်းအရာများ (01-CoreConcepts/) - ပြီးပြည့်စုံသော ပြုပြင်မွမ်းမံခြင်း
- **ပရိုတိုကော ဗားရှင်း ပြင်ဆင်ခြင်း**: MCP Specification 2025-06-18 ကို ရည်ညွှန်း၍ ရက်စွဲအရ ဗားရှင်းပုံစံ (YYYY-MM-DD format) ဖြင့် ပြင်ဆင်ထားသည်
- **ဖွဲ့စည်းပုံ ဖွံ့ဖြိုးတိုးတက်မှု**: Hosts, Clients, Servers များ၏ ဖော်ပြချက်များကို လက်ရှိ MCP ဖွဲ့စည်းမှု နမူနာများကို သက်ဆိုင်စွာ တိုးတက်ပြင်ဆင်ထားသည်
  - Hosts ကို AI လျှောက်လွှာများ အနေဖြင့် MCP client connection များစုပေါင်း စီမံအုပ်ချုပ်သူအဖြစ် ပြသထားသည်
  - Clients ကို တစ်ယောက်ချင်း server ဆက်သွယ်မှုများ ထိန်းသိမ်းသူအဖြစ် ဖော်ပြထားသည်
  - Servers ကို ဒေသတွင်း / နယ်ပယ်ပြင် ဝန်ဆောင်မှုပုံစံများ အနေနှင့် ပြင်ဆင်တိုးတက်ထားသည်
- **ပေါ်လွင်ဆန်းသစ်မှု ပြုပြင်ခြင်း**: server နှင့် client primitive များအား လုံးဝပြင်ဆင်ခြင်း
  - Server Primitives: Resources (ဒေတာရင်းမြစ်များ), Prompts (သင်္ချာပုံစံများ), Tools (အကောင်အထည်ဖော်နိုင်သော ဖန့်ဝေမှုများ) အသေးစိတ် ရှင်းလင်းချက်နှင့် ဥပမာများပြုလုပ်ထားသည်
  - Client Primitives: Sampling (LLM အပြီးစီးမှုများ), Elicitation (အသုံးပြုသူ ထည့်သွင်းမှု), Logging (debugging/monitoring)
  - လက်ရှိအသုံးပြုနေသော မေးလေ့လာမှု (`*/list`), ရယူခြင်း (`*/get`), နှင့် လုပ်ဆောင်မှု (`*/call`) နည်းလမ်းပုံစံများဖြင့် ပြင်ဆင်ထားသည်
- **ပရိုတိုကော ဖွဲ့စည်းပုံ**: အဆင့် နှစ်ခုပါဝင်သော ဖွဲ့စည်းပုံ မော်ဒယ်ကို မိတ်ဆက်
  - ဒေတာ အဆင့်: JSON-RPC 2.0 အခြေခံပြီး ဘဝကြာမြင့်မှု စီမံခန့်ခွဲမှုနှင့် primitive များပါဝင်သည်
  - သယ်ယူပို့ဆောင်မှု အဆင့်: STDIO (ဒေသတွင်း) နှင့် Streamable HTTP သည် SSE (ဝေးကွာရာ) သယ်ယူပို့ဆောင်မှု နည်းလမ်းများ
- **လုံခြုံရေး ဖွဲ့စည်းမှု**: အသုံးပြုသူ သဘောတူညီမှု ပြတ်သားမှု, ဒေတာ ကိုယ်ရေးကာကွယ်မှု, Tool လုပ်ဆောင်မှု လုံခြုံမှု, နှင့် သယ်ယူပို့ဆောင်မှု အဆင့် လုံခြုံမှု အကြောင်းအရာအပြည့်အစုံပါရှိသည်
- **ဆက်သွယ်မှု ပုံစံများ**: ပရိုတိုကော မက်ဆေ့ချ်များအား စတင်ခြင်း, ရှာဖွေခြင်း, လုပ်ဆောင်ခြင်း, အသိပေးခြင်း လည်ပတ်မှုစနစ်များ ပြသထားသည်
- **ကုဒ် နမူနာများ**: MCP SDK လက်ရှိ မော်ဒယ်များကို အထောက်အထားပြု၍ မျိုးစုံ-ဘာသာစကား (.NET, Java, Python, JavaScript) နမူနာများ ပြန်လည် အသစ်ပြုလုပ်ထားသည်

#### လုံခြုံရေး (02-Security/) - လုံခြုံရေး အသစ်စွဲ ပြုပြင်မှု လုံးဝ ပြီးစီး
- **စံပြုချက်များ အညီမီ လိုက်နာမှု**: MCP Specification 2025-06-18 လုံခြုံရေး လိုအပ်ချက်များ နှစ်ခြင်းမပြတ် ကိုက်ညီစွာ လိုက်နာထားသည်
- **အသိမှတ်ပြုမှု တိုးတက်လာမှု**: အထူး OAuth server များမှ ပြင်ပ အသိမှတ်ပြုသူ Delegate များ (Microsoft Entra ID) သို့ ပြောင်းလဲမှု စာရွက်စာတမ်း
- **AI အန္တရာယ် သုံးသပ်ချက်**: လက်ရှိ AI တိုက်ခိုက်မှု များကို ပိုမိုအပြည့်အစုံ ထည့်သွင်းခြင်း
  - အသေးစိတ် prompt injection စမ်းသပ်မှု အသုံးဥပမာများနှင့်
  - Tool poisoning နည်းလမ်းများ၊ "rug pull" တိုက်ခိုက်မှု ပုံစံ
  - နောက်ခံ ပြတင်းပေါက် ပိုးထိုးမှုနှင့် အသုံးပြုသူ မျဉ်းဖြတ်မှု လှည့်ခင်းများ
- **Microsoft AI လုံခြုံရေး ဖြေရှင်းချက်များ**: Microsoft လုံခြုံရေး စနစ် အကျယ်ပြန့် ဖော်ပြချက်များ
  - AI Prompt Shields နှင့် နည်းလမ်းတိုးတက်မှုများ (ရှာဖွေမှု၊ အာရုံစိုက်မှု၊ ခွဲခြားရေးနည်းများ)
  - Azure Content Safety ထည့်သွင်းမှု ပုံစံများ
  - GitHub Advanced Security ကျယ်ပြန့်သော supply chain ကာကွယ်မှု
- **အဆင့်မြင့် အန္တရာယ် ကာကွယ်မှု**: အသေးစိတ် ပြင်ဆင်ထားသော လုံခြုံရေး ထိန်းချုပ်မှု
  - Session hijacking MCP အထူး အကြောင်းအရာများနှင့် cryptographic session ID လိုအပ်ချက်များ
  - Confused Deputy ပြဿနာများ MCP proxy ပတ်ဝန်းကျင်တွင် တရားဝင် သဘောတူညီချက်လိုအပ်မှုများနှင့်
  - Token passthrough အရေးကြီးသော စစ်ဆေးမှု ထိန်းချုပ်မှုများ
- **Supply Chain လုံခြုံရေး**: AI supply chain အပေါ် ကာကွယ်မှုများ လုံခြုံစိတ်ချရသော foundation models, embeddings ဝန်ဆောင်မှုများ, context ပံ့ပိုးသူများ နှင့် တတိယပါတီ API များ အပါအဝင် ကျယ်ပြန့်စွာ ဖုံးလွှမ်းထားသည်
- **Foundation လုံခြုံရေး**: စက်မှုဖော်ရွေမှု လုံခြုံရေး ပုံစံများ၊ zero trust architecture နှင့် Microsoft လုံခြုံရေး စနစ် ပေါင်းစပ်မှု တိုးတက်ရန်
- **အရင်းအမြစ် စုပေါင်းမှု**: အမျိုးအစား(တရားဝင် စာရွက်အဖွဲ့, စံချိန်, သုတေသန, Microsoft ဖြေရှင်းချက်များ, ဆောင်ရွက်မှုလမ်းညွှန်များ) အလိုက် သုံးသပ် စီစဉ်မှု

### စာရွက်စာတမ်း အရည်အသွေး တိုးတက်မှုများ
- **ဖွဲ့စည်းတည်ဆောက်မှု ပြင်ဆင်ခြင်း**: အသေးစိတ်၊ လုပ်ဆောင်နိုင်သော သင်ယူရည်မှန်းချက်များ တိုးတက်အောင် ပြုလုပ်ထားသည်
- **ဆက်သွယ်ရပ်ဆိုင် ချိတ်ဆက်မှုများ**: လုံခြုံရေးနှင့် အဓိကနယ်ပယ် ခေါင်းစဉ်များအကြား လင့်များ ထည့်သွင်းထားသည်
- **လက်ရှိ အချက်အလက်များ**: ရက်စွဲနှင့် သတ်မှတ်ချက်လင့်များအားလုံး လက်ရှိ စံနှုန်းအတိုင်း ပြင်ဆင်ထားသည်
- **ဆောင်ရွက်မှု လမ်းညွှန်ချက်များ**: နှစ်ခုလုံးအပိုင်းတွင် အတိုင်းအတာအသေးစိတ် ဖြည့်စွက်ထားသည်

## 2025 ခုနှစ် ဇူလိုင်လ 16 ရက်

### README နဲ့ လမ်းညွှန်မှု တိုးတက်မှုများ
- README.md မှာ သင်တန်း လမ်းညွှန်မူပုံကို လုံးဝ ပြန်လည်ဒီဇိုင်းရေးဆွဲထားသည်
- `<details>` tag များကို ဇယားအခြေခံ ပုံစံဖြင့် ပိုလွယ်ကူစွာသုံးရလွယ်ခြင်းအတွက် အစားထိုးထားသည်
- "alternative_layouts" ဖိုလ်ဒါအသစ်ထဲတွင် အခြားပုံစံများ ဖန်တီးထားသည်
- ကတ်ပေါ်၊ tab-style နှင့် accordion-style လမ်းညွှန်နမူနာများ ထည့်သွင်းထားသည်
- repository ဖွဲ့စည်းမှုအပိုင်းကို လက်ရှိဖိုင်အားလုံးနှင့် မဟာပေါင်းပေါက်ထားသည်
- "ဒီ သင်တန်းကို ဘယ်လိုသုံးရမလဲ" အပိုင်းကို ရှင်းလင်း သွားအောင် ထည့်သွင်းတိုးတက်အောင် ပြုလုပ်ထားသည်
- MCP သတ်မှတ်ချက် လင့်တွေကို မှန်ကန်သည့် URL များသို့ ပြောင်းလဲထားသည်
- သင်တန်းဖွဲ့စည်းမှုတွင် Context Engineering အပိုင်း (5.14) ထည့်သွင်းထားသည်

### သင်ယူ ညွှန်ပြချက်များ ပြင်ဆင်မှုများ
- repository ဖွဲ့စည်းမှု နောက်ဆုံး သဘောတူညီချက်နှင့် လုံးဝ ပြန်လည် ပြင်ဆင်ထားသည်
- MCP Clients နှင့် Tools များ၊ နှင့် လူကြိုက်များသော MCP Servers နေရာအသစ် များကို ထည့်သွင်းထားသည်
- Visual Curriculum Map ကို အမှန်တကယ် ခေါင်းစဉ်အားလုံး ထိရောက်စွာ ပြသနိုင်ရန် ပြင်ဆင်ထားသည်
- အထူးပြု ခေါင်းစဉ်များအကြောင်း ဖော်ပြချက်များ ပိုမိုအသေးစိတ် ရှင်းလင်းထားသည်
- Case Studies အပိုင်းကို အမှန်တကယ် နမူနာများ ပြောင်းလဲ ပြင်ဆင်ထားသည်
- ဤကြားပေးစာရင်း လုံးဝ ထည့်သွင်းထားသည်

### လူထု မိတ်ဖက်မှုများ (06-CommunityContributions/)
- ပုံဖန်တီးရေး MCP server များအကြောင်း အသေးစိတ် ထည့်သွင်းထားသည်
- VSCode တွင် Claude အသုံးပြုပုံအတွက် ကဏ္ဍကြီး ထည့်သွင်းထားသည်
- Cline terminal client စတင်ခြင်းနှင့် အသုံးပြုခြင်း ညွှန်ပြချက် ထည့်သွင်းထားသည်
- MCP client အပိုင်းကို လူကြိုက်များသော client ရွေးချယ်စရာများအားလုံး ထည့်သွင်းထားသည်
- အကူအညီ အထောက်အကူပြု ကုဒ် ဥပမာများ ပိုမို မှန်ကန်ခြင်းဖြင့် တိုးမြှင့်ထားသည်

### အထူး ခေါင်းစဉ်များ (05-AdvancedTopics/)
- အထူးပြု ခေါင်းစဉ် ဖိုလ်ဒါအားလုံးကို အတူတူသည့် နာမည်ပုံစံဖြင့် စုပေါင်းထားသည်
- နောက်ခံ အင်ဂျင်နီယာပညာ မူကြမ်းများနှင့် နမူနာများ ထည့်သွင်းထားသည်
- Foundry အေးဂျင့် ပေါင်းစပ်မှု စာရွက်စာတမ်း ထည့်သွင်းထားသည်
- Entra ID လုံခြုံရေး ပေါင်းစပ်မှု စာရွက်စာတမ်း ဖြည့်စွက်တိုးတက်ထားသည်

## 2025 ခုနှစ် ဇွန်လ 11 ရက်

### စတင်ဖန်တီးမှု
- MCP for Beginners သင်တန်း၏ ပထမဦးဆုံး ဗားရှင်း မိတ်ဆက်မှု
- အဓိက ပိုင်း ၁၀ ခု၏ မူလ ဖွဲ့စည်းမှု ဖန်တီးထားသည်
- လမ်းညွှန်ရန် Visual Curriculum Map ကို ဆောင်ရွက်ထားသည်
- ဘာသာစကား မျိုးစုံဖြင့် နမူနာပရောဂျက် များ ထည့်သွင်းထားသည်

### စတင်သူများအတွက် (03-GettingStarted/)
- ပထမဆုံး server ဆောင်ရွက်မှု ဥပမာများ ဖန်တီးထားသည်
- client ဖွံ့ဖြိုးမှု လမ်းညွှန်ချက်များ ထည့်သွင်းထားသည်
- LLM client ပေါင်းစပ်ခြင်း နည်းလမ်းများ ပါရှိသည်
- VS Code ပေါင်းစပ်မှု စာရွက်စာတမ်း ထဲ ထည့်သွင်းထားသည်
- Server-Sent Events (SSE) server ဥပမာများကို လုပ်ဆောင်ထားသည်

### အဓိကအကြောင်းအရာများ (01-CoreConcepts/)
- client-server ဖွဲ့စည်းမှု အကြောင်း သန့်ရှင်းစွာ ရှင်းပြထားသည်
- အဓိက ပရိုတိုကော အစိတ်အပိုင်းများကို စာရွက်စာတမ်း ဖန်တီးထားသည်
- MCP တွင် သတင်းပို့နည်း ပုံစံများကို စာရွက်စာတမ်းပြုလုပ်သည်

## 2025 ခုနှစ် မေ 23 ရက်

### repository ဖွဲ့စည်းမှု
- မူလ folder ဖွဲ့စည်းမှုနှင့် repository ကို စတင်ခဲ့သည်
- အဓိက section အတွက် README file များ ဖန်တီးထားသည်
- ဘာသာပြန်ခြင်း အခြေခံစွမ်းရည်ဆောက်လုပ်မှု ပြုလုပ်ထားသည်
- ပုံများ နှင့် ဇယားဖိုင်များ ထည့်သွင်းခဲ့သည်

### စာရွက်စာတမ်း
- မူလ README.md ကို သင်တန်း အနှစ်ချုပ် အဖြစ် ဖန်တီးထားသည်
- CODE_OF_CONDUCT.md နှင့် SECURITY.md ထည့်သွင်းထားသည်
- SUPPORT.md ကို အကူအညီ လမ်းညွှန်ချက်အဖြစ် ထည့်သွင်းခဲ့သည်
- စမ်းသပ်မှု လေ့လာမှု ညွှန်ကြားမှု မူလ ဖွဲ့စည်းမှုကို ပြုလုပ်ထားသည်

## 2025 ခုနှစ် ဧပြီလ 15 ရက်

### အစီအစဉ်ဆွဲခြင်းနှင့် ဖွဲ့စည်းမှု
- MCP for Beginners သင်တန်း အစီအစဉ် အခြေခံ ဆွဲဆောင်မှု
- သင်ယူ ရည်ရွယ်ချက်များ၊ ရည်မှန်းသော ဖောက်သည် အုပ်စုကို သတ်မှတ်ထားသည်
- သင်တန်းကို ၁၀ ပိုင်း ဖွဲ့စည်းမှု အတိုင်း သတ်မှတ်ထားသည်
- ဥပမာများနှင့် ကိစ္စလေ့လာမှုများ အတွက် သဘောတူဖြစ်စေသော ဖွဲ့စည်းမှု ဖန်တီးထားသည်
- အဓိက အကြောင်းအရာများအတွက် မူလ prototype ဥပမာများ ဖန်တီးထားသည်

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
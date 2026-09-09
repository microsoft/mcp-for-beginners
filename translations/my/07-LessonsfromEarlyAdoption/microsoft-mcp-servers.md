# 🚀 10 Microsoft MCP ဆာဗာများ သည် Developer ထုတ်လုပ်နိုင်မှုပြောင်းလဲနေခြင်း

## 🎯 ဤလမ်းညွှန်စာအုပ်တွင် သင်ရရှိမည့်အရာများ

ဤလက်တွေ့လမ်းညွှန်သည် AI အစွမ်းထက်ပို့အကူများနှင့် ဖန်တီးသူများအလုပ်လုပ်ပုံကို တက်ကြွစွာ ပြောင်းလဲနေသော Microsoft MCP ဆာဗာသုံးဆယ်ကို ပြသထားသည်။ MCP ဆာဗာများသည် *လုပ်နိုင်စွမ်း* များကို ရှင်းပြခြင်းမဟုတ်ပဲ Microsoft နှင့် ထိုနယ်ပယ်အထက်ရှိ နေ့စဉ်ဖန်တီးမှုလုပ်ငန်းစဉ်များတွင် သက်ရောက်မှုရှိနေသော ဆာဗာများကို ပြသပါမည်။

ဤလမ်းညွှန်၌ ပါဝင်သော ဆာဗာများအား လက်တွေ့အသုံးပြုမှုနှင့် ဖန်တီးသူတုံ့ပြန်ချက်ပေါ်မှ ချထားထားသည်။ ကုဒ်ရေးသမားအနေဖြင့် MC P သို့ အသစ်စက်စက်ရောက်ရှိသူ သို့မဟုတ် ရှိပြီးသား စနစ်ကို တိုးချဲ့လိုသူ မည်သို့ ထိုဆာဗာများကို မည်သို့ အသုံးပြုရမည် နှင့် အရေးကြီးသောအချက်များကို ရှာဖွေတွေ့ရှိမည်ဖြစ်သည်။ Microsoft ပတ်ဝန်းကျင်ထဲ၌ ရရှိနိုင်သည့် အကျိုးသက်ရောက်မှုအများဆုံး နှင့် အကျိုးရှိဆုံးကိရိယာများစွာကို ကိုယ်ပိုင်လုပ်ငန်းများတွင် အသုံးချနိုင်မည်ဖြစ်သည်။

> **💡 လျင်မြန်စတင်ရန် အကြံပြုချက်**
> 
> MCP အသစ်လား? စိတ်ပူစေစေမရှိပါ! ဤလမ်းညွှန်သည် စတင်လေ့လာသူများအတွက် ရည်ရွယ်ထားသည်။ ပုဒ်မများကို နားလည်ရန် ရင်းမြစ်အနေဖြင့် [MCP နိဒါန်း](../00-Introduction/README.md) နှင့် [အဓိကအယူအဆများ](../01-CoreConcepts/README.md) ကို ချက်ချင်း ပြန်ကြည့်နိုင်ပါသည်။

## အနှစ်ချုပ်

ဇယားကျကျ ဖော်ပြချက်များဖြင့် Microsoft MCP ဆာဗာ ၁၀ ခုကို လေ့လာနိုင်မည့် လမ်းညွှန်ဖြစ်ပြီး၊ ဖန်တီးသူများသည် AI အကူအညီနဲ့ ပြင်ပကိရိယာများအတူ ထိတွေ့ဆက်ဆံပုံကို အကြီးအကျယ် ပြောင်းလဲနေကြောင်း ပြသသည်။ Azure အရင်းအမြစ်စီမံခန့်ခွဲမှုပြုခြင်းမှ စာရွက်စာတမ်းသွင်းစနစ်ထိ ထိုဆာဗာများသည် Model Context Protocol ၏ ကျဉ်းမြောင်းပြီး ထိရောက်သော ဖန်တီးမှုလုပ်ငန်းစဉ်များဖန်တီးရာတွင် စွမ်းအားပြသသည်။

## သင်ယူရန် ရည်ရွယ်ချက်များ

ဤလမ်းညွှန်အဆုံးတွင် သင်သည်
- MCP ဆာဗာများသည် ဖန်တီးသူထုတ်လုပ်မှု တိုးမြှင့်ပုံကို နားလည်မည်
- Microsoft ၏ အကျိုးသက်ရောက်မှုအမြင့်ဆုံး MCP ဆာဗာအသုံးပြုမှုများကို လေ့လာမည်
- ဆာဗာတစ်ခုချင်းစီ၏ လက်တွေ့သုံးအသုံးပြုမှုများကို ရှာဖွေမည်
- VS Code နှင့် Visual Studio တွင် ထိုဆာဗာများကို တပ်ဆင်ပြီး စီမံသတ်မှတ်နည်းကို သေချာ သိရှိမည်
- MCP ပတ်ဝန်းကျင်ကျယ်ပြန့်မှုနှင့် အနာဂတ်လမ်းကြောင်းများကို စူးစမ်းလေ့လာမည်

## 🔧 MCP ဆာဗာများနားလည်မှု: စတင်လေ့လာသူအတွက် လမ်းညွှန်

### MCP ဆာဗာဆိုတာဘာလဲ?

Model Context Protocol (MCP) အတွက် စတင်လေ့လာသူအနေဖြင့် "MCP ဆာဗာဆိုတာ တကယ်ဘာလဲ၊ ဘာကြောင့်စိတ်ဝင်စားရမလဲ?" ဟု စဉ်းစားဖို့ ဖြစ်နိုင်ပါသည်။ ရိုးရှင်းသော ဥပမာတစ်ခုနဲ့ စတင်ကြရအောင်။

MCP ဆာဗာများကို သင်၏ AI ကုဒ်ရေးသားသူအကူအညီ (GitHub Copilot အပိုင်းတစ်ခုကဲ့သို့) များအတွက် တိကျပညာရှင်ကူညီသူများအဖြစ် တွေးကြည့်ပါ။ သင့်ဖုန်းအပေါ်တွင် လုပ်ဆောင်ချက်နှင့် သက်ဆိုင်သည့် app များကို အသုံးပြုသလို — အပြောင်းအလဲ တစ်ခုအတွက် ကာလပျက်မှုမရှိပဲ ဖန်တီးမှုအကူအညီများကို ပေးသည်။

### MCP ဆာဗာသည် ဘာပြဿနာဖြေရှင်းသနည်း

MCP ဆာဗာမတိုင်မီ၊ သင်အကယ်၍
- Azure အသုံးပြုမှုများကို စစ်ဆေးရန်
- GitHub ကိစ္စတစ်ခု ဖန်တီးရန်
- ဒေတာဘေ့စ်ကို စုံစမ်းမေးမြန်းရန်
- စာရွက်စာတမ်းများကို ရှာဖွေရန်

သင်သည် ကုဒ်ရေးခြင်းရပ်ပြီး browser ဖွင့်ကာ သင်သွားရမည့်ဝဘ်ဆိုဒ်သို့ သွားရောက်၍ ဤလုပ်ငန်းများကို လက်ဖြင့်ဆောင်ရွက်ရမည်ဖြစ်ပြီး၊ ၎င်းကြောင့် အတွေးလမ်းကြောင်းကျော်လွန်မှု ဖြစ်ပေါ်ကာ ထုတ်လုပ်မှုလျော့နည်းသွားသည်။

### MCP ဆာဗာများသည် သင့်ဖန်တီးမှု အတွေ့အကြုံကို မည်သို့ပြောင်းလဲသနည်း

MCP ဆာဗာများကြောင့် သင်၏ ဖန်တီးရေး ပတ်ဝန်းကျင် (VS Code, Visual Studio စသည်) မှသာ ထားရှိပြီး AI ကူညီရေးသားသူထံတွင် လုပ်ငန်းအားထားအသုံးပြုနိုင်သည်။ ဥပမာအားဖြင့် -

**ရိုးရှင်းသည့် စဉ်ဆက်အစား:**
1. ကုဒ်ရေးခြင်း ရပ်တန့်ခြင်း
2. Browser ဖွင့်ခြင်း
3. Azure portal သို့ သွားရောက်ခြင်း
4. storage account အသေးစိတ် ကြည့်ရှုခြင်း
5. VS Code သို့ ပြန်လည်ဝင်ရောက်ခြင်း
6. ကုဒ်ရေးခြင်း များဆက်လုပ်ခြင်း

**ယခု သင်လုပ်ဆောင်နိုင်သည့် အခြေအနေ:**
1. AI ကိုမေးပါ - "ကျွန်တော့်ရဲ့ Azure storage accounts နေရာအခြေအနေက ဘယ်လိုနဲ့?"
2. ရရှိသောအချက်အလက်ဖြင့် ကုဒ်ရေးခြင်း ဆက်လုပ်ခြင်း

### စတင်လေ့လာသူများအတွက် အဓိက အကျိုးကျေးဇူးများ

#### 1. 🔄 **သင့်လုပ်ဆောင်မှုအခြေအနေတွင် ဆက်လက်တည်ရှိနိုင်မှု**
- အပ်လုပ်ချက်များပြားမှုများ မဖြစ်ပေါ်စေရန်
- သင်ရေးသားနေသော ကုဒ်အပေါ် ဦးတည်မှု ထိန်းသိမ်းထားနိုင်ခြင်း
- ကိရိယာများစွာ စီမံခန့်ခွဲမှု စိတ်ပိုင်းအလွန်ခံနည်း လျော့ချပွားခြင်း

#### 2. 🤖 **ရှုပ်ထွေးသောကမ်းမောင်းလမ်းညွှန်များအစား သဘာဝဘာသာစကားကို အသုံးပြုနိုင်ခြင်း**
- SQL syntax မမှတ်မိဘဲ လိုအပ်သောဒေတာကို ဖြေပေးရန်
- Azure CLI command မမှတ်မိဘဲ လုပ်ဆောင်လိုသောအရာကို ရှင်းပြရန်
- သင်အာရုံစူးစိုက်ရမည့် မဟာဗျူဟာကို AI မှ ကောင်းစွာ ကူညီပေးမည်

#### 3. 🔗 **ကိရိယာအမျိုးမျိုးကို ဆက်သွယ်ပေးနိုင်ခြင်း**
- ဝန်ဆောင်မှုများ ပေါင်းစပ်မှုဖြင့် လုပ်ငန်းစဉ်များ တည်ဆောက်နိုင်ခြင်း
- ဥပမာ - "နောက်ဆုံး GitHub များကို ရယူပြီး Azure DevOps အလုပ်項များ ဖန်တီးခြင်း"
- စာကြောင်းရှည်နက်သော script မရေးဘဲ automation တည်ဆောက်ခြင်း

#### 4. 🌐 **တိုးပြန့်နေသော ပတ်ဝန်းကျင် ထိတွေ့နိုင်ခြင်း**
- Microsoft, GitHub, ပြိုင်ဘက် အဖွဲ့အစည်းများ ဖန်တီးသော ဆာဗာများမှ အကျိုးခံစားခြင်း
- ကွဲပြားသောပံ့ပိုးသူများ၏ ကိရိယာများကို အခက်အခဲမရှိပဲ ပေါင်းစပ်အသုံးပြုနိုင်ခြင်း
- ကွဲပြားသော AI အကူအညီပေးသူများအကြား အသုံးပြုနိုင်သော စံသတ်မှတ်ထားသော ပတ်ဝန်းကျင်တစ်ခုတွင် ပါဝင်ခြင်း

#### 5. 🛠️ **လက်တွေ့ လုပ်ဆောင်ခြင်းမှ သင်ယူနိုင်ခြင်း**
- မူလဆာဗာများနှင့် စတင်လေ့လာမှု
- သင့်အဆင်အဆာပြေလျှင် ကိုယ်ပိုင် ဆာဗာများ တည်ဆောက်နိုင်ခြင်း
- ရရှိနိုင်သော SDK များ နှင့် စာရွက်စာတမ်းများဖြင့် သင်ကြားခြင်း

### စတင်လေ့လာသူများအတွက် လက်တွေ့နမူနာ

သင်သည် ဝက်ဘ်ဖွံ့ဖြိုးရေးအတွက် စတင် လုပ်ကိုင်နေသူအဖြစ်၊ ပထမ ဖြစ်စဉ်ကို စတင်လုပ်ဆောင်နေတယ်ဆိုပါစို့။ MCP ဆာဗာများသည် ဘယ်လိုကူညီနိုင်သလဲ:

**ရိုးရာနည်းလမ်း:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP ဆာဗာများဖြင့်:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### စီးပွားရေးလုပ်ငန်းစံချိန်အားသာချက်

MCP သည် စက်မှုလုပ်ငန်းကျယ်ပြန့်မှု စံချိန်ဖြစ်လာပြီး,
- **တည်ငြိမ်မှု**: ကိရိယာနှင့် ကုမ္ပဏီအမျိုးမျိုးတွင် သက်ဆိုင်မှုတူညီမှု
- **အပြန်အလှန် လုပ်ကိုင်နိုင်မှု**: ကုမ္ပဏီကတစ်ဆင့် ဆာဗာများ လျှပ်တမလှိုင်လုပ်ဆောင်နိုင်ခြင်း
- **အနာဂတ် အတွက် ကြိုတင်ပြင်ဆင်မှု**: ကျွမ်းကျင်မှုနှင့် စနစ်များ AI အကူအညီပေးသူ များကြား အပြန်အလှန် ချဲ့ထွင်နိုင်ခြင်း
- **အသိုင်းအဝိုင်း**: အကြီးစား သိမ်းဆည်းမှု နှင့် ထောက်ပံ့မှု ပတ်ဝန်းကျင်

### စတင်ရန်: သင်၏ သိမှတ်ရမည့် အချက်များ

ဤလမ်းညွှန်တွင် Developer များ အဆင့်အားလုံးအတွက် အထူးအသုံးဝင်သည့် Microsoft MCP ဆာဗာ ၁၀ ခုကို လေ့လာမည်။ ဆာဗာတစ်ခုစီသည်
- ရိုးရှင်းသော ဖန်တီးမှု စိန်ခေါ်မှုများ ဖြေရှင်းရန်
- ထပ်တလဲလဲ လုပ်ဆောင်ရသော အမိန့်များ လျှော့ချပေးရန်
- ကုဒ်အရည်အသွေး တိုးတက်စေရန်
- သင်ယူမှု အခွင့်အလမ်းများ တိုးမြှင့်ရန်

> **💡 သင်ယူမှု အကြံပြုချက်**
> 
> MCP အသစ်ဆုံးသည်ဆိုပါက၊ ကျွန်ုပ်တို့၏ [MCP နိဒါန်း](../00-Introduction/README.md) နှင့် [အဓိကအယူအဆများ](../01-CoreConcepts/README.md) မော်ဂျူးများနှင့် အဆင့်လိုက်စတင်လေ့လာပြီး ထိုနောက် Microsoft ဆာဗာများနှင့် ပတ်သက်သော စက်ရုပ်သန့်စင် သင်ပုဒ်များကို ပြန်လည်ကြည့်ပါ။
>
> MCP ၏ အရေးပါမှုကို နားလည်ရန် Maria Naggaga ဆိုသူ၏စာတမ်း [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps) ကို မှတ်သားဖတ်ရှုပါ။

## VS Code နှင့် Visual Studio တွင် MCP စတင်အသုံးပြုခြင်း 🚀

Visual Studio Code သို့မဟုတ် Visual Studio 2022 နှင့် GitHub Copilot အသုံးပြုပါက MCP ဆာဗာများ တပ်ဆင်ခြင်း သည် ရိုးရှင်းပါသည်။

### VS Code တပ်ဆင်ခြင်း

VS Code အတွက် အခြေခံလုပ်ငန်းစဉ်မှာ ယင်းဖြစ်ပါသည်-

1. **Agent mode ကို ဖွင့်ရန်**: VS Code တွင် Copilot Chat ပြသသည့် ပြတင်းပေါက်၌ Agent mode သို့ ပြောင်းရွှေ့ပါ
2. **MCP ဆာဗာများ ကိုပုံသဏ္ဍာန်ချခြင်း**: VS Code settings.json ဖိုင်တွင် ဆာဗာ ဖွဲ့စည်းမှုများ ထည့်သွင်းပါ
3. **ဆာဗာများ စတင်ရန်**: သင်အသုံးချလိုသော ဆာဗာတိုင်းအတွက် "Start" ခလုတ်ကို နှိပ်ပါ
4. **ကိရိယာများ ရွေးချယ်ခြင်း**: လက်ရှိအစည်းအဝေးအတွက် အသုံးပြုမည့် MCP ဆာဗာများကို ရွေးချယ်ပါ

အသေးစိတ် တပ်ဆင်နည်းများအတွက် [VS Code MCP စာရင်း](https://code.visualstudio.com/docs/copilot/copilot-mcp)ကို ကြည့်ပါ။

> **💡 ခေတ်ကျဆာဗာ မန်နေဂျာ အကြံပြုချက်**
> 
> VS Code Extensions မြင်သာရာတွင် [တပ်ဆင်ပြီး MCP ဆာဗာများကို စီမံခန့်ခွဲရန် UI အသစ်](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode) ပါရှိသည်။ စတင်ခြင်း၊ ရပ်တန့်ခြင်းနှင့် စီမံခန့်ခွဲမှုကို ရိုးရှင်းသည့် မျက်နှာပြင်မှ ပြုလုပ်နိုင်ပါသည်။ လက်တွေ့အသုံးပြု၍ ကြည့်ပါ။

### Visual Studio 2022 တပ်ဆင်ခြင်း

Visual Studio 2022 (ဗားရှင်း ၁၇.၁၄ သို့မဟုတ် ပြီးပြည့်စုံသော ဗားရှင်း) အတွက်-

1. **Agent mode ဖွင့်ခြင်း**: GitHub Copilot Chat မှာ "Ask" dropdown ကို နှိပ်ပြီး "Agent" ကို ရွေးပါ
2. **ဖွဲ့စည်းမှု ဖိုင် ဖန်တီးခြင်း**: သင့် solution directory အတွင်း `.mcp.json` ဖိုင်အား ဖန်တီးပါ (အကြံပြုရာနေရာ: `<SOLUTIONDIR>\.mcp.json`)
3. **ဆာဗာများ ဖွဲ့စည်းခြင်း**: တူညီသော MCP ပုံစံဖြင့် ဆာဗာ ဖွဲ့စည်းမှု ထည့်သွင်းပါ
4. **ကိရိယာ ခွင့်ပြုချက်**: သင်သုံးလိုသော ကိရိယာများအတွက် တောင်းဆိုသော ခွင့်ပြုချက်များကို အတည်ပြုပါ။

Visual Studio စနစ်တပ်ဆင်နည်းအပြည့်အစုံအတွက် [Visual Studio MCP စာစောင်](https://learn.microsoft.com/visualstudio/ide/mcp-servers) ကို ကြည့်ရှုပါ။

MCP ဆာဗာတစ်ခုချင်းစီသည် connection string, authentication စသည့် အချက်အလက်လိုအပ်ချက်များ ရှိသော်လည်း၊ သင့် IDE နှစ်ခုစလုံးတွင် setup ပုံစံသည် တူညီသည်။

## Microsoft MCP ဆာဗာများဆီမှ သင်ခန်းစာများ 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**ဘာလုပ်နိုင်သနည်း**: Microsoft Learn Docs MCP Server သည် cloud ပေါ်တွင် တည်ရှိသည့် ဝန်ဆောင်မှုတစ်ခုဖြစ်ပြီး AI အကူအညီများကို အချိန်နှင့်တပြေးညီ Microsoft ၏ အတည်ပြုစာရွက်စာတမ်းများ သို့ Entry ခွင့် ရရှိစေသည်။ `https://learn.microsoft.com/api/mcp` ထံ ဆက်သွယ်ကာ Microsoft Learn, Azure စာရွက်စာတမ်းများ၊ Microsoft 365 စာရွက်စာတမ်းများနှင့် အခြား တရားဝင် Microsoft ကရင်းမြစ်များဆီ Semantic search လုပ်ပေးသည်။

**ဘာကြောင့်အသုံးဝင်သနည်း**: "Documentation ထဲတင်ပြင်ပဲ"ဟု ယူဆနိုင်သော်လည်း Microsoft နည်းပညာအသုံးပြုသူတိုင်းအတွက် အရေးပါတဲ့ ဝန်ဆောင်မှုတစ်ခုဖြစ်သည်။ .NET developer များနေရာ AI ကုဒ်ရေးသူများအပေါ် အကြီးမားဆုံး အဝါရောင်အရှုံးကွက်မှာ နောက်ဆုံးထွက် .NET နှင့် C# များ ပေါ်လစီ များ မသိကြပါ။ Microsoft Learn Docs MCP Server သည် အချိန်နှင့်တပြေးညီ သတ်မှတ်ထားသည့် API၊ စာရွက်စာတမ်းများနှင့် နည်းလမ်းများကို အသုံးပြုသူ AI ကူညီရေးသားသူများ အတွက် မဖြစ်မနေ ရှိရန် ဦးတည်ချက်အရ အသုံးပြုနိုင်စေနိုင်သည်။ Azure SDK အသစ်များ, C# 13 ၏ အသစ်နှင့် Aspire pattern များကို သုံးစွဲရာတွင် စနစ်တက်ရှိ နှင့် ကျစ်လစ်သည့်ကုဒ်ကို စွမ်းဆောင်နိုင်ရန် ကူညီသည်။

**လက်တွေ့အသုံးပြုမှု**: "Microsoft Learn Documentation အရ Azure container app ဖန်တီးရန် az cli command များက ဘာတွေလဲ?" သို့မဟုတ် "Entity Framework ကို ASP.NET Core နှင့် dependency injection ဖြင့် သတ်မှတ်ရန် မည်သို့လုပ်မလဲ?" သို့မဟုတ် "ကုဒ်ကို Microsoft Learn Documentation မှ စွမ်းဆောင်ရည် အကြံပြုချက်များနှင့်ကိုက်ညီမှုရှိမရှိသုံးသပ်ပါ" လိုမျိုး မေးမြန်းနိုင်သည်။ ဆာဗာမှာ Microsoft Learn, Azure docs နှင့် Microsoft 365 documentation ကို semantic search ဖြင့် အကြောင်းအရာကို အသုံးပြုပြီး အကောင်းဆုံး ဆောင်းပါးခေါင်းစဉ်များနှင့် URL များဖြင့် အကြောင်းအရာအမြောက်အများ ပြန်လည်ပေးသည်။

**နမူနာအထူး**: ဆာဗာတွင် `microsoft_docs_search` ကိရိယာကို ဆက်သွယ်ထားပြီး Microsoft ၏ တရားဝင် နိုင်ငံတကာနည်းပညာ စာရွက်စာတမ်းများမှ semantic search လုပ်နိုင်သည်။ သို့တပ်ဆင်ပြီးနောက် "ASP.NET Core တွင် JWT authentication မည်သို့ အကောင်အထည်ဖော်မလဲ?" ဟူသောမေးခွန်းများ ဆွေးနွေးနိုင်ပြီး အသေးစိတ်နည်းနာများနှင့် အတည်ပြု လင့်ခ်များ ပြန်လည်ရရှိနိုင်သည်။ စုံစမ်းချက်အရည်အသွေးသည် လွန်ခဲ့သော context ကို နားလည်မှုကြောင့် အထူးပါးစပ်သည် - Azure context တွင် "containers" မေးလျှင် Azure Container Instances စာရွက်စာတမ်းရောက်ရှိမည်၊ .NET context တွင်ဆို C# collection သတင်းအချက်အလက်များ လက်ခံရရှိမည်။

ဤကိရိယာသည် လျင်မြန် ပြောင်းလဲမှုများရှိ သို့မဟုတ် မကြာသေးမီက update လုပ်ထားသော library များနှင့် အသုံးထားမှုများအတွက် အထူးထောက်ပံ့မှု ပေးသည်။ ဥပမာ အနေနဲ့ Aspire နှင့် Microsoft.Extensions.AI ၏ နောက်ဆုံးထွက် features များကို မြန်မြန်လေ့လာလိုက်ပြီး Microsoft Learn Docs MCP server ပါ ဝင်ထားသောကြောင့် API documentation များအပြင် လမ်းညွှန်ချက်များကိုလည်း ရရှိနိုင်ခဲ့သည်။

> **💡 အသုံးပြုသူအတွက် အကြံပြုချက်**
> 
> MCP ကိရိယာများအသုံးပြုရေး အတွက် စီမံကိန်းလမ်းညွှန်များ ထည့်သည့်အားပေးမှုလိုအပ်သည်။ "သင်တွင် `microsoft.docs.mcp` ၏ access ရှိသည် - Microsoft နည်းပညာများအကြောင်း မေးခွန်းများတွင် C#, Azure, ASP.NET Core, Entity Framework စသည့် နယ်ပယ်များအတွက် Microsoft ၏ နောက်ဆုံးအတည်ပြုစာရွက်စာတမ်းများကို ရှာဖွေရာတွင် ဤကိရိယာကို အသုံးပြုပါ" ဟု စနစ် prompt များ သို့မဟုတ် [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) တို့ ထည့်သွင်းရန် စဉ်းစားပါ။
>
> ဤအသုံးပြုနည်းအတွက် ကောင်းမွန်သော နမူနာတစ်ခုမှာ Awesome GitHub Copilot repository မှ [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) ဖြစ်သည်။ ဤမုဒ်သည် Microsoft Learn Docs MCP server ကို အသုံးပြုပြီး C# ကုဒ်များကို သန့်ရှင်းပြီး လက်ရှိ နည်းလမ်းများဖြင့် အဆင့်မြှင့်ပေးရန် အထူးပြုထားသည်။
### 2. ☁️ Azure MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**ဘာလုပ်ပါသလဲ**: Azure MCP Server သည် Azure ၀န်ဆောင်မှုများကို အထူးပြုထားသော ၁၅ ကျော်သော ကွန်နက်တာများ စုံလင်စွာ ပါဝင်သည့် ကွန်ပလက်စ် စနစ်တစ်ခုဖြစ်ပြီး သင်၏ AI အလုပ်စဉ်တွင် Azure စနစ်လုံးကို ဖမ်းဆီးသွားသည်။ ယခုကွန်ပြုတာ တစ်ခုတည်း မဟုတ်ပဲ စွမ်းအားပြည့်ဝသော အစုလိုက် အပြုံလိုက်ဖြစ်ကာ လုပ်ငန်းသုံးအရင်းအမြစ်စီမံခန့်ခွဲမှု၊ ဒေတာဘေ့( PostgreSQL, SQL Server ), Azure Monitor log ဝိတ်ချခြင်းနှင့် KQL, Cosmos DB ပေါင်းစည်းခြင်း အပါအဝင် အခြားစွမ်းဆောင်ရည်များကို ပါဝင်သည်။

**ဘာကြောင့်အသုံးဝင်သလဲ**: Azure resource များကိုသာ မစီမံနိုင်ပေမယ့် Azure SDK များနှင့် အလုပ်လုပ်ရာတွင် ကုဒ်အရည်အသွေးကို ထူးခြားစွာတိုးတက်စေသည်။ Azure MCP ကို Agent အတိုင်းအသုံးပြုသောအခါ သင် ကျူးလွန်လိုက်သည့် ကုဒ်ကိုသာ မရေးသွားပေမယ့် လက်ရှိ အတည်ပြုမှု ပုံစံများ၊ အမှား စီမံခန့်ခွဲမှု အကောင်းဆုံး နည်းလမ်းများနှင့် နောက်ဆုံးထွက် SDK ဖိုင်ချ်များနှင့် ကိုက်ညီသည့် ကုဒ်ကို ရေးသားပေးသွားသည်။ မူလကအလုပ်လုပ်နိုင်တဲ့ မွမ်းမံမှုမပါတဲ့ ကုဒ် မဟုတ်ဘဲ Azure ၏ ဖော်ပြုမှုများနှင့် ကိုက်ညီသည့် ကုဒ်ပုံစံတွေနဲ့ ထုတ်လုပ်မှုအတွက် သင့်တော်သော ကုဒ်ကို ရရှိမှာ ဖြစ်သည်။

**အဓိက မော်ဂျူးများမှာ**:
- **🗄️ ဒေတာဘေ့ချ် ကွန်နက်တာများ**: Azure Database for PostgreSQL နှင့် SQL Server သို့ တိုက်ရိုက် သဘာဝဘာသာစကားဖြင့် လွယ်ကူသလို ဝင်ရောက် အသုံးပြုခြင်း
- **📊 Azure Monitor**: KQL ဖြင့် အခြေခံထားသော log ခွဲခြမ်းစိတ်ဖြာမှုနှင့် လည်ပတ်မှု အချက်အလက်များ
- **🌐 အရင်းအမြစ် စီမံခန့်ခွဲမှု**: Azure ရင်းမြစ်များ အပြည့်အစုံ စီမံခန့်ခွဲခြင်း
- **🔐 အတည်ပြုမှု**: DefaultAzureCredential နှင့် စီမံခန့်ခွဲထားသော အထောက်အထား ပုံစံများ
- **📦 သိမ်းဆည်းမှု ၀န်ဆောင်မှုများ**: Blob Storage, Queue Storage, နှင့် Table Storage လုပ်ငန်းစဉ်များ
- **🚀 ကွန်တိန်နာ ၀န်ဆောင်မှုများ**: Azure Container Apps, Container Instances, နှင့် AKS စီမံခန့်ခွဲမှု
- **နှင့် အခြားအထူးပြု ကွန်နက်တာများ အများကြီး**

**အမှန်တကယ်အသုံးပြုခြင်း**: "ကျွန်ုပ်၏ Azure storage အကောင့်များကို စာရင်းပြပါ", "ပြီးခဲ့သော နာရီတွင် ဖြစ်သော အမှားများအတွက် Log Analytics workspace ကို မေးမြန်းပါ", သို့မဟုတ် "Node.js နဲ့ လိုအပ်သော အတည်ပြုမှုနဲ့ Azure application တစ်ခု ဆောက်ရန် ကူညီပါ"

**ပြပွဲ အပြည့်အစုံ**: Azure MCP ကို GitHub Copilot for Azure extension နှင့် VS Code တွင် ပေါင်းစပ်အသုံးပြုရင်း စွမ်းဆောင်ရည်ကို ပြသသည့် ပြပွဲတစ်ခု ဖြစ်သည်။ နှစ်ခုလုံး ထည့်သွင်းပြီး အောက်ပါအတိုင်း  မေးမြန်းပါက-

> "DefaultAzureCredential အတည်ပြုမှုကို အသုံးပြုကာ Azure Blob Storage ထဲသို့ ဖိုင်တင်မည့် Python script တစ်ခု ဖန်တီးပါ။ script သည် 'mycompanystorage' ဟူသော Azure storage account နှင့် ချိတ်ဆက်ပြီး 'documents' ဟူသော container တွင် တင်ရန် ဖြစ်သည်၊ လက်ရှိ အချိန်စံပြချက်ဖြင့် စမ်းသပ်ဖိုင် သိမ်းဆည်းပြီး အမှားများကို စနစ်တကျ ကိုင်တွယ်ကာ အသိပေးစာလုံးများ ထုတ်ပြရမည်၊ Azure ၏ အကောင်းဆုံး authentication နဲ့ အမှားစစ်ဆေးမှု လမ်းညွန်ချက်များနှင့် ကိုက်ညီရန် ဖြစ်ပြီး DefaultAzureCredential အတည်ပြုခြင်း နည်းလမ်းများကို မှတ်ချက်များဖြင့် ရှင်းပြရန်နှင့် ကောင်းမွန်စွာ ဖန်တီးထားသော function များနဲ့ စာတမ်းအပြည့်အစုံ ပါဝင်ရမည်။"

Azure MCP Server သည် အပြည့်အစုံ ဖြစ်အောင် ထုတ်လုပ်နိုင်သော Python script ကို ဖန်တီးပေးပါမည်-
- နောက်ဆုံးထွက် Azure Blob Storage SDK ကို သင့်တော်သော async ပုံစံများဖြင့် အသုံးပြုသည်
- DefaultAzureCredential အတည်ပြုမှုကို အပြည့်အဝ ဖြတ်သန်းမှု ဖော်ပြချက်နှင့် လက်တွေ့အသုံးချမှုဖြင့် ဖော်ပြသည်
- သက်ဆိုင်ရာ Azure exception အမျိုးအစားများနှင့် အမှား စနစ်တကျ ကိုင်တွယ်မှုပါရှိသည်
- Azure SDK ၏ resource management နှင့် ချိတ်ဆက်မှု စနစ်များအတွက် အကောင်းဆုံး လမ်းညွန်ချက်စနစ်ကို လိုက်နာသည်
- အသေးစိတ် မှတ်တမ်းတင်ခြင်းနှင့် အသိပေး စာလုံးများကို ဖန်တီးပေးသည်
- function များ၊ စာတမ်းကောင်းကောင်းနှင့် type hints ပါရှိသော ကောင်းမွန်စွာ ဖွဲ့စည်းထားသော script ဖြစ်သည်

Azure MCP မပါဘဲ သာမာန် blob storage ကုဒ် ကို ရနိုင်သော်လည်း ယခုကိစ္စမကျေရွကား Azure ၏ အတည်ပြု စနစ်အသစ်များ၊ အမှား သီးသန့် ဖြစ်ရပ်ဒီဇိုင်းများကို မလိုက်နာသေးနိုင်ပေ။ Azure MCP နှင့်အတူ ကုဒ်သည် လက်ရှိ authentication နည်းလမ်းများနှင့် လိုက်ကပ်ပြီး Microsoft ၏ ထုတ်လုပ်မှုအတွက် အကောင်းဆုံး လမ်းညွှန်ချက်များကို လိုက်နာ သဘောထားရှိသည်။

**ဖော်ပြချက်နမူနာ**: az နဲ့ azd CLI ကွန်မန်းများကို မေ့ပြီးသားဖြစ်ရတဲ့ ကိစ္စသည် ကျွန်ုပ်အတွက် အခက်အခဲဖြစ်သည်။ ပထမဦးစွာ နည်းလမ်းကို ရှာဖွေ၊ ဒုတိယမှာ လှမ်းပြီးအသုံးပြုရသည်။ သူတော်တော် portal ထဲ ထည့်သွင်းပြီး ခလုတ်ခလုတ်နှိပ်တတ်သည်။ မေ့နေကြောင်း အသိပေးချင်ခြင်းမရှိလို့ပါ။ လိုချင်တာကို ဖော်ပြနိုင်ခြင်းက စိတ်အတက်ကြွစရာ၊ IDE မှ မထွက်မနေ လုပ်နိုင်တာက ပိုကောင်းတယ်။

စတင်အသုံးပြုရန် [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) တွင် သုံးစွဲမှု ဩဇာများ စာရင်းကောင်းတစ်ခုရှိသည်။ အပြည့်အစုံတက်သင်ချက်များနှင့် ကြီးမားသော အဆင့်မြှင့်တင်ရေး နည်းလမ်းများအတွက် [အတည်အသွင်း Azure MCP သဘောတူစာတမ်း](https://learn.microsoft.com/azure/developer/azure-mcp-server/) ကို ကြည့်ပါ။

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**ဘာလုပ်ပါသလဲ**: GitHub MCP Server သည် GitHub ၏ စနစ်လုံးနှင့် ဆက်သွယ်မှု ပြဿနာမရှိစေသော စနစ်ဖြစ်ပြီး hosted remote access နှင့် ဒေါကာ (Docker) ပေါ်တွင် ဒေသတွင်းဖော်ပြမှု နှစ်မျိုးလုံး ရရှိနိုင်သည်။ ၎င်းသည် သာမာန် repository လုပ်ငန်းများသာမက GitHub Actions စီမံခန့်ခွဲမှု၊ pull request workflow များ၊ issue tracking, လုံခြုံရေး စစ်ဆေးမှု၊ အသိပေးချက်များနှင့် ကွမ်းခြံ့ရှိသော automation စွမ်းရည်များ ပါဝင်သည်။

**ဘာကြောင့်အသုံးဝင်သလဲ**: GitHub ကို ပလက်ဖောင်းအပြည့်အစုံ ဖြင့် သင်၏ ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်ထဲသို့ မျှဝေရန် ပြောင်းလဲပေးသည်။ VS Code နှင့် GitHub.com တို့ကို အမြဲပြောင်းလဲဖို့ ကြိုးစားခြင်းမလိုဘဲ သဘာဝဘာသာစကား ကွန်မန်းများ အားဖြင့် စီမံခန့်ခွဲမှုပိုင်း၊ ကုဒ်စစ်ဆေးခြင်း နှင့် CI/CD စောင့်ကြည့်မှုအားလုံးကို တစ်နေရာတည်းက စီမံနိုင်သည်။

> **ℹ️ မှတ်ချက်: Agent မျိုးစုံ အကြောင်း**
> 
> GitHub MCP Server ကို GitHub ၏ Coding Agent (အမှတ်တံဆိပ်များအတွက် ကိုယ်စားလှယ် AI agent) နှင့် မရောမလှပ်ဖြစ်စေရပါနှင့်။ GitHub MCP Server သည် VS Code ၏ Agent mode တွင် GitHub API ဆွဲဆောင်မှု ပေးပြီး GitHub Coding Agent သည် GitHub issues အတွက် pull request များဖန်တီးသည်။

**အဓိက စွမ်းဆောင်ရည်များ**:
- **⚙️ GitHub Actions**: CI/CD pipeline စီမံခန့်ခွဲမှု အပြည့်အစုံ၊ workflow စောင့်ကြည့်ခြင်းနှင့် artifact ကိုင်တွယ်မှု
- **🔀 Pull Requests**: PR များ ဖန်တီး၊ စစ်ဆေး၊ ပေါင်းစည်းခြင်းနှင့် အခြေအနေ စနစ်တကျ စောင့်ကြည့်မှု
- **🐛 Issues**: အပြည့်အစုံ issue lifecycle စီမံခန့်ခွဲမှု၊ မှတ်ချက်ရေးခြင်း၊ အမှတ်အသားပေးခြင်းနှင့် မိတ်ဆက်ခြင်း
- **🔒 လုံခြုံရေး**: ကုဒ် စစ်ဆေးမှု အသိပေးများ၊ လျှို့ဝှက်ချက် ရှာဖွေခြင်းနှင့် Dependabot ပေါင်းစည်းမှု
- **🔔 အသိပေးချက်များ**: ကြိုးစားမှု၊ အသိပေးချက် စီမံခန့်ခွဲမှုနှင့် repository စာရင်း စနစ်ထိန်းချုပ်မှု
- **📁 Repository စီမံခန့်ခွဲမှု**: ဖိုင် လုပ်ဆောင်ချက်များ၊ ပေါင့်ချ်စီမံမှုနှင့် repository အုပ်ချုပ်မှု
- **👥 ပူးပေါင်းဆောင်ရွက်မှု**: အသုံးပြုသူ နှင့် အဖွဲ့အစည်း ရှာဖွေခြင်း၊ အဖွဲ့ စီမံမှုနှင့် လက်ရောက်ခွင့် ထိန်းချုပ်မှု

**အမှန်တကယ် အသုံးဝင်မှု**: "ကျွန်ုပ် feature branch မှ pull request တစ်ခု ဖန်တီးပါ", "ဒီတစ်ပါတ် အကျဉ်းချုပ် မအောင်မြင်သော CI runs များ ပြပါ", "ကျွန်ုပ်၏ repositories များအတွက် အသိပေး လုံခြုံရေး alerts များ စာရင်းပြပါ" သို့မဟုတ် "ကျွန်ုပ်လိုက်နာထားသော issue များအားလုံးကို စာရင်းပြပါ"

**ပြပွဲ အပြည့်အစုံ**: GitHub MCP Server ၏ စွမ်းအား ပြသသည့် workflow အောက်ပါအတိုင်း ဖြစ်သည်-

> "Sprint review အတွက်ပြင်ဆင်နေပါတယ်။ ဒီတစ်ပါတ် ဖန်တီးထားတဲ့ pull requests များအားလုံး ပြပါ၊ CI/CD pipelines ရဲ့ အခြေအနေကို စစ်ဆေးပါ၊ လုံခြုံရေး အသိပေးချက်များ စုစည်းပြီး ပြင်ဆင်ရန် အချက်အလက် တင်ပြပါ၊ 'feature' အမှတ်တံဆိပ်ခံထားသော merged PR များအပေါ် အခြေခံ၍ release notes အကြမ်းဖျဉ်း ရေးဆွဲခြင်း မူကြမ်းကို ကူညီပေးပါ။"

GitHub MCP Server သည်-
- မကြာသေးမီ pull requests များကို အသေးစိတ်အခြေအနေ နဲ့ မေးမြန်းသည်
- workflow runs များ စစ်ဆေးပြီး မအောင်မြင်မှု သို့မဟုတ် လုပ်ဆောင်မှုပိုးချိုးမှုများ ထင်ဟပ်မှု ပေးသည်
- လုံခြုံရေး စစ်ဆေးမှု ရလဒ်များ ကို စုစည်းပြီး အရေးကြီး အသိပေးချက်များ အဓိကထား နိုင်ငံတော်
- merged PR များမှ အချက်အလက်များ ဆွဲထုတ်ကာ release notes အပြည့်အစုံ ကြေညာတင်ပြသည်
- sprint အစီအစဉ်နှင့် ထုတ်လုပ်မှု ပြင်ဆင်မှုအတွက် လုပ်ဆောင်ရမည့် နောက်တန်းဆင့်များ ပေးသည်

**ဖော်ပြချက်နမူနာ**: ကုဒ် စစ်ဆေးမှု ရှုပ်ထွေးမှုများ အတွက် အသုံးပြုရတာ ကြိုက်တယ်။ VS Code, GitHub အသိပေးချက်၊ pull request စာမျက်နှာများ ကြားမှာ ပြောင်းလဲခြင်း မလိုဘဲ "ကျွန်ုပ် ကြည့်ရှုရန် PR များကို ပြပါ" ဟုပြောပြီး "PR #123 တွင် အမှားကိုင်တွယ်မှု ပုံစံအတွက် မှတ်ချက် ထည့်လိုသည်" လို့ ပြောနိုင်သည်။ server သည် GitHub API ခေါ်ယူမှုများ ကိုင်တွယ်ပြီး ဆွေးနွေးမှု context ကို ထိန်းထားကာ တကယ်ကို အကျိုးရှိသော ပြန်လည်သုံးသပ်မှု မှတ်ချက်များရေးရန် ကူညီသည်။

**အတည်ပြုမှု ရွေးချယ်စရာများ**: server သည် VS Code ထဲတွင် နူးညံ့စွာ လုပ်ဆောင်နိုင်သည့် OAuth နှင့် Personal Access Tokens နှစ်မျိုးလုံး ကို ထောက်ပံ့ပြီး သင်လိုအပ်သည့် GitHub အလုပ်အဖွဲ့များသာဖွင့်နိုင်သည်။ remote hosted service အနေနှင့် လုပ်နိုင်သလို ဒေါကာမှ ဒေသတွင်းနည်းဖြင့်လည်း တပ်ဆင်နိုင်၍ ပြည့်စုံထိန်းချုပ်မှု ရရှိသည်။

> **💡 ကျွမ်းကျင်သူ အကြံပေးချက်**
> 
> MCP server ဆက်တင်များတွင် `--toolsets` ပါရာမီတာကို စိတ်ကြိုက် ချိန်ညှိကာ လိုအပ်သော toolsets များကိုသာ ဖွင့်ပါက context အရွယ်အစား လျော့နည်းပြီး AI tool ရွေးချယ်မှု တိုးတက်စေသည်။ ဥပမာ core development workflow အတွက် `"--toolsets", "repos,issues,pull_requests,actions"` ကို ထည့်သုံးပါ၊ GitHub စောင့်ကြည့်မှု ဆိုင်ရာ အတွက် `"--toolsets", "notifications, security"` ကို သုံးပါ။
### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**ဘာလုပ်ပါသလဲ**: Azure DevOps ၀န်ဆောင်မှုများနှင့် ချိတ်ဆက်ကာ အပြည့်အစုံစီမံခန့်ခွဲမှု၊ အလုပ်ပစ္စည်း နှင့် build pipeline စီမံမှု၊ repository လုပ်ငန်းများ ကူညီပေးသည်။

**ဘာကြောင့်အသုံးဝင်သလဲ**: Azure DevOps ကို အဓိက DevOps ပလက်ဖောင်းအဖြစ် အသုံးပြုနေသော အဖွဲ့များအတွက် MCP server သည် လုံးဝပြောင်းလဲမှုဖြစ်ပေါ်စေသည်။ ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်နှင့် Azure DevOps ဝဘ်အင်တာဖေ့စ် တို့ကြား ဒေသအတွင်းဖြတ်ဆိုင်းစွာပြောင်းဖို့ မလိုတော့ပဲ အလုပ်ပစ္စည်းများ စီမံရန်၊ build အခြေအနေ စစ်ဆေးရန်၊ repository မေးမြန်းရာတွင် AI အကူအညီဖြင့် တိုက်ရိုက် ဆောင်ရွက်နိုင်ပေသည်။

**အမှန်တကယ် အသုံးဝင်မှု**: "WebApp project အတွက် လက်ရှိ sprint ထဲတွင် အသက်ဝင်နေသော အလုပ်ပစ္စည်းများအားလုံး ပြပါ", "အသစ်တွေ့ရှိထားသော login ပြဿနာအတွက် bug report တစ်ခု ဖန်တီးပါ", သို့မဟုတ် "Build pipeline အခြေအနေ စစ်ဆေးပြီး မအောင်မြင်မှုများ ပြပါ"

**ဖော်ပြချက်နမူနာ**: ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်မှ ထွက်ခြင်းမရှိပဲ "WebApp project ၏ လက်ရှိ sprint ထဲတွင် အသက်ဝင်နေသော အလုပ်ပစ္စည်းများကို ပြပါ" သို့မဟုတ် "အသစ် တွေ့ရှိထားသော login ပြဿနာ အတွက် bug report ဖန်တီးပါ" စသည်ဖြင့် အခြေအနေ စစ်ဆေးနိုင်သည်။

### 5. 📝 MarkItDown MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**ဘာလုပ်တယ်ဆိုတာ**: MarkItDown သည် စာရွက်စာတမ်း အမျိုးမျိုးကို LLM သုံးစွဲခြင်းနှင့် စာသားစစ်တမ်းလုပ်ငန်းစဉ်များအတွက် စီစစ်ထားသော အမြင့်မားဆုံး Markdown အဖြစ် ပြောင်းလဲပေးသော စာရွက်စာတမ်း ပြောင်းလဲရေး ဆာဗာ တစ်ခုဖြစ်သည်။

**အကျိုးရှိတာဘာလဲ**: ခေတ်မီ စာရွက်စာတမ်းလုပ်ငန်းစဉ်များအတွက် မရှိမျှမဖြစ်! MarkItDown သည် ခေါင်းစဉ်များ၊ စာရင်းများ၊ ဇယားများနှင့် လင့်များကဲ့သို့သော အရေးကြီးသော စာရွက်စာတမ်းဖွဲ့စည်းမှုကို ထိန်းသိမ်းကာ အမျိုးမျိုးသော ဖိုင်ဖော်မတ်များကို စိတ်ဝင်စားဖွယ် ကောင်းစွာ ကိုင်တွယ်ပေးနိုင်သည်။ စာသားထုတ်ယူပစ္စည်းများနှင့် မတူဘဲ AI ကို အသုံးပြုခြင်းနှင့် လူသားများ ဖတ်ရှုမှုအတွက် အဓိပ္ပာယ်နှင့် ပုံစံများကို သိမ်းဆည်းထားပေးသည်။

**ထောက်ခံထားသော ဖိုင်ဖော်မတ်များ**:
- **ရုံးရေးစာရွက်စာတမ်းများ**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **မီဒီယာဖိုင်များ**: ဓာတ်ပုံများ (EXIF မက်တာဒေတာနှင့် OCR ပါရှိသည်), အသံဖိုင်များ (EXIF မက်တာဒေတာနှင့် အသံဖော်ပြချက်)
- **ဝက်ဘ်အကြောင်းအရာ**: HTML, RSS feeds, YouTube URL များ, Wikipedia စာမျက်နှာများ
- **ဒေတာဖော်မတ်များ**: CSV, JSON, XML, ZIP ဖိုင်များ (အတွင်းပါအကြောင်းအရာများကို ထပ်မံ စစ်ဆေးတင်ပြသည်)
- **ထုတ်ဝေဖော်မတ်များ**: EPub, Jupyter notebooks (.ipynb)
- **အီးမေးလ်**: Outlook မက်ဆေ့ခ််များ (.msg)
- **တိုးတက်ဆန်းသစ်မှုများ**: မြှင့်တင်ထားသော PDF ကိစ္စများအတွက် Azure Document Intelligence ပေါင်းစပ်မှု

**တိုးတက်စွမ်းရည်များ**: MarkItDown သည် OpenAI client ဖြင့် ပံ့ပိုးထားပါက LLM ရေးဖြင့် ဓာတ်ပုံ ဖော်ပြချက်များ၊ Azure Document Intelligence ဖြင့် မြှင့်တင်ရမည့် PDF ကိစ္စများ၊ အသံပြောင်းလဲခြင်းနှင့် ဖိုင်ဖော်မတ်အသစ်များထည့်သွင်းနိုင်ရန် ပလပ်ဂ်အင် စနစ် ဖြင့် ထောက်ခံထားသည်။

**အမှန်တကယ် အသုံးပြုမှု**: "ဒီ PowerPoint တင်ဆက်မှုကို ကျွန်ုပ်တို့ စာရွက်စာတမ်းဆိုက်အတွက် Markdown အဖြစ် ပြောင်းလိုသည်", "ဒီ PDF မှ ခေါင်းစဉ်ဖွဲ့စည်းတည်ဆောက်မှုမှန်ကန်စွာဖြင့် စာသားထုတ်ယူလိုသည်", သို့မဟုတ် "ဒီ Excel စာရွက်ဇယားကို ဖတ်ရှုနိုင်သော ဇယားဖော်မတ်အဖြစ် ပြောင်းလိုသည်"

**ဥပမာထူးချွန်ချက်**: [MarkItDown စာတမ်းများ](https://github.com/microsoft/markitdown#why-markdown) မှ ရွေးချယ်ခဲ့သည်။

> Markdown သည် အရေးအသားအနည်းဆုံး စနစ်တကျ markup ဒေတာများဖြင့် အလွန်နီးစပ်သော စာသားဖြစ်ပြီး ထင်ရှားသော စာရွက်စာတမ်းဖွဲ့စည်းမှုကို အထောက်အပံ့ပေးနိုင်သည်။ OpenAI ၏ GPT-4o ကဲ့သို့သော လူကြီးမင်းများ စိတ်ကြိုက် LLM များအနေဖြင့် သဘာဝအတိုင်း Markdown ကို "ပြောဆို" ၍ မေးခွန်းမေးလျှင် Markdown ကို မပေးပို့မီ တစ်ချက်နေရာတွင် ထည့်သွင်းကာ ဖြေကြားကြသည်။ ၎င်းက Markdown နှင့် ပတ်သက်၍ စတင်လေ့လာကြောင်း၊ ချိုပ်ပစ်ချက်များသည် အလွန်တိတ်တဆိတ်ကျပြီး သိပ္ပံ ဆိုင်ရာ ကျွမ်းကျင်မှုရှိကြောင်း ဖော်ပြသည်။

MarkItDown သည် စာရွက်စာတမ်းဖွဲ့စည်းမှုကို ထိန်းသိမ်းရာတွင် အလွန်ကောင်းမွန်သည်။ ဥပမာ PowerPoint တင်ဆက်မှု ဖိုင်ကို ပြောင်းသည့်အခါ Slide များအတွက် သင့်တော်သော ခေါင်းစဉ်များကို ထိန်းသိမ်းပြီး ဇယားများကို Markdown ဇယားအဖြစ် ထုတ်ယူသည်။ ဓာတ်ပုံများအတွက် alt စာသားထည့်သွင်းပြီး စကားပြောမှတ်စုများကိုပါ ကောင်းစွာ ပြန်လည် ထုတ်ယူပေးသည်။ ဇယားများကို ဖတ်ရှုရလွယ်ကူသော ဒေတာဇယားအဖြစ် ပြောင်းလဲကာ နောက်ဆုံးတွင် ထွက်ရှိလာသော Markdown သည် မူလ တင်ဆက်မှု ပြင်ပုံစံဖြစ်ပြီး AI စနစ်များသို့ဖြည့်သွင်းရန် သင်တန်းမှ စာတမ်းရေးရန်အတွက် ကိုက်ညီပါသည်။
### ၆။ 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**ဘာလုပ်တယ်ဆိုတာ**: SQL Server ဒေတာဘေ့စ်များ (on-premises, Azure SQL သို့မဟုတ် Fabric) တွင် စကားပြောဖြင့် ရယူနိုင်ခြင်းပေးသည်။

**အကျိုးရှိတာဘာလဲ**: PostgreSQL ဆာဗာနှင့်တူသော Microsoft SQL ပတ်ဝန်းကျင်အတွက်ဖြစ်သည်။ အသုံးပြုရလွယ်ကူတဲ့ ချိတ်ဆက် String တစ်ခုဖြင့် ချိတ်ဆက်ကာ သဘာဝဘာသာစကားဖြင့် မေးမြန်းနိုင်ပါသည် – နောက်ထပ် ကလစ်ပြောင်း ရှင်းလင်းခြင်း မလိုတော့ပါ!

**အမှန်တကယ် အသုံးပြုမှု**: "နောက်ဆုံး ၃၀ ရက်အတွင်း ဘယ်အော်ဒါတွေ မပြည့်စုံသေးမှတ်ထားသလဲ"ကို သင့်တော်သော SQL စုံစမ်းမေးခွန်းသို့ ပြောင်းလဲကာ ဖော်ပြချက် စနစ်တကျ ပြန်ပေးသည်။

**ဥပမာထူးချွန်ချက်**: အချက်အလက်ချိတ်ဆက်မှုကို တပ်ဆင်ပြီးဖို့နောက်ပိုင်းမှာ၊ ဒေတာနှင့် တိုက်ရိုက် စကားပြောမေးမြန်းနိုင်ပါသည်။ ဘလော့ခ်စတိုင် မှာလဲ "သင့်ချိတ်ဆက်ထားတဲ့ ဒေတာဘေ့စ်ဘာတွေလဲ?" ဆိုတဲ့ မေးခွန်းတစ်ခုနဲ့ ကိုယ်တိုင် MCP စာ‌ရင်းက သူ့က တင်ပြချက်အမျိုးမျိုးကို ရေးသားနိုင်သော ကိရိယာအသုံးပြုပြီး သင့် SQL Server ထဲချိတ်ဆက်ပြီး လက်ရှိ ချိတ်ဆက်ထားတဲ့ ဒေတာဘေ့စ်အချက်အလက်များ ပြန်ကြားပေးသည် – SQL စာကြောင်းတစ်ကြောင်းမှ မရေးဘဲနဲ့။ MCP ဆာဗာသည် schema စီမံခန့်ခွဲမှုမှ ဒေတာပြင်ဆင်မှုအထိ database လုပ်ငန်းစဉ်များအားလုံးကို သဘာဝဘာသာစကား ဖော်ပြချက်များဖြင့် ထောက်ပံ့သည်။ VS Code နဲ့ Claude Desktop နှင့် ပတ်သက်သော အပြည့်အစုံ အတည်ပြုလုပ်ခြင်းနည်းလမ်းများအတွက် [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/) ကို ကြည့်ပါ။


### ၇။ 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**ဘာလုပ်တယ်ဆိုတာ**: AI ကိုယ်စားလှယ်များအား စစ်ဆေးခြင်းနှင့် အော်တိုမေးရှင်းအတွက် ဝက်ဘ်စာမျက်နှာနှင့် ဆက်သည့်အခွင့်အရေး ပေးသည်။

> **ℹ️ GitHub Copilot ကို ခွင့်ပြုခြင်းဖြင့်**
> 
> Playwright MCP Server သည် GitHub Copilot ၏ Coding Agent ကို စွမ်းဆောင်နိုင်စွမ်း ပေးကာ ဝဘ်ဘရောက်ဇာ ခရီးသွားနိုင်စွမ်း ထည့်သွင်းပေးသည်! [ဒီအင်္ဂါရပ်အကြောင်း သိုလှောင်ရန်](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/)။

**အကျိုးရှိတာဘာလဲ**: သဘာဝဘာသာစကား ဖော်ပြချက်များဖြင့် အော်တိုမေးရှင်း စမ်းသပ်ခြင်းအတွက် အကောင်းဆုံးဖြစ်သည်။ AI သည် ဝဘ်ဆိုက်များကို သွားရောက်လေ့လာနိုင်ပြီး ဖောင်များ ဖြည့်စွက်ခြင်းနှင့် ဖွဲ့စည်းတန်းစီ ဖတ်ရှုနိုင်သော ဒေတာရယူမှုများ ခွင့်ပြုသည် – ဤသည်မှာ အလွန်တန်ခိုးကြီးသော အရာဖြစ်သည်။

**အမှန်တကယ် အသုံးပြုမှု**: "Login လုပ်ရုံ လမ်းကြောင်းကို စမ်းသပ်ပြီး Dashboard မှန်ကန်စွာ စတင်တင်ပြသည်ကို အတည်ပြုပါ" သို့မဟုတ် "ကုန်ပစ္စည်းများရှာဖွေပြီး ရလဒ်စာမျက်နှာကို မှန်ကန်မှုစစ်ဆေးသော စမ်းသပ်မှု ဖန်တီးပါ" – အပလီကေးရှင်း ရင်းမြစ်ကုဒ် မလိုအပ်ပဲ

**ဥပမာထူးချွန်ချက်**: ကျွန်ုပ်၏ အဖော် Debbie O'Brien သည် Playwright MCP Server ဖြင့် မကြာသေးခင်က ထူးချွန်သော လုပ်ဆောင်မှုများ ပြုလုပ်နေပါသည်! ဥပမာအားဖြင့် သူမသည် အလွယ်တကူ Playwright စမ်းသပ်မှုများကို အပလီကေးရှင်း ရင်းမြစ်ကုဒ်မရှိဘဲ ဖန်တီးနိုင်ကြောင်း ပြသခဲ့သည်။ သူမ၏အခြေအနေတွင် Copilot ကို စကားပြော ဖြင့် ဇာတ်လမ်းရှာဖွေရေး app အတွက် စမ်းသပ်မှု တစ်ခု ဖန်တီးရန် တောင်းဆိုခဲ့သည် – ဆိုက်ကို သွားရောက်၊ "Garfield" ဖြင့် ရှာဖွေရန်၊ ရလဒ်များတွင် ဇာတ်လမ်း မြင်ကွင်း ပေါ်လာသည်ဟု အတည်ပြုခြင်း။ MCP သည် browser session တစ်ခု ဖွင့်ပေးကာ DOM snapshots ဖြင့် စာမျက်နှာ ဖွဲ့စည်းမှုကို လေ့လာကာ သင့်တော်သော selector များ ရှာဖွေပြီး TypeScript စမ်းသပ်မှု လုံးဝအလုပ်လုပ်သည့် ကုဒ်ကို ပထမဆောင်ရွက်ချက်တွင် ဖြတ်ပြီး ဆောင်ရွက်နိုင်ခဲ့သည်။

ပိုပြီးစွမ်းရည်များသောအချက်မှာ သဘာဝဘာသာစကားညွှန်ကြားချက်များနှင့် လုပ်ဆောင်မှု စမ်းသပ် ကုဒ်များအကြား ချိတ်ဆက်မှု ဖြစ်သည်။ စာရေးသူအလေ့အကျင့်အရ စမ်းသပ်မှုကို ကိုယ်တိုင် ရေးသားရခြင်း သို့မဟုတ် ကိုးဒ်မူလ အချက်အလက်ရရှိခြင်း ဖြစ်ပါသဖြင့် ခွင့်ပြုထားသည်။ ဒါပေမဲ့ Playwright MCP ဖြင့် အပြင်ဆိုက်များ၊ client အပလီကေးရှင်းများ သို့မဟုတ် ကိုးဒ်မရှိသော အနေအထားများတွင် စမ်းသပ်မှုများ ပြုလုပ်နိုင်သည်။


### ၈။ 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**ဘာလုပ်တယ်ဆိုတာ**: Microsoft Dev Box ပတ်ဝန်းကျင်များကို သဘာဝဘာသာစကားဖြင့် စီမံခန့်ခွဲပေးသည်။

**အကျိုးရှိတာဘာလဲ**: ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင် စီမံခြင်းကို အလွန်လွယ်ကူစေသည်! သတ်မှတ်ထားသော command များကို မှတ်မထားဘဲ ဖန်တီး၊ ဖွဲ့စည်း၊ စီမံနိုင်သည်။

**အမှန်တကယ် အသုံးပြုမှု**: "အသစ်တဖန် Dev Box တစ်ခု ဖန်တီးပြီး နောက်ဆုံး .NET SDK ပါထည့်သွင်း၍ ကျွန်ုပ်တို့ ပရောဂျက်အတွက် ပြင်ဆင်ပါ", "ကျွန်ုပ်၏ development ပတ်ဝန်းကျင်အားလုံး၏ အခြေနေကို စစ်ဆေးပါ", သို့မဟုတ် "ကျွန်ုပ်တို့ အသင်း၏ တင်ဆက်ပွဲများအတွက် စံနမူနာ demo ပတ်ဝန်းကျင်တစ်ခု ဖန်တီးပါ"

**ဥပမာထူးချွန်ချက်**: ကျွန်ုပ် Dev Box ကို ကိုယ်ပိုင် ဖွံ့ဖြိုးရေးအတွက် အလွန်နှစ်သက်သည်။ James Montemagno က Dev Box သည် အဆိုပါ conference နဲ့ ကွန်ဖရင့် / ဟိုတယ် / လေယာဉ် wifi အနေအထား အားမနည်းပဲ super-fast Ethernet ချိတ်ဆက်မှုရှိကြောင်း ပြောတဲ့အခါ ကျွန်ုပ်၏ အတွေးတောက်ပခဲ့သည်။ အမှန်အားဖြင့်နောက်ဆုံး ကွန်ဖရင့် demo လေ့ကျင့်ချက်များကို လုပ်ရာတွင် ကျွန်ုပ်၏ laptop ကို ကျွန်ုပ်၏ ဖုန်း hotspot နှင့် ချိတ်ဆက်ထားပြီး Bruges မှ Antwerp သို့ ဘတ်စ်ကားစီးစဉ်တွင် လေ့ကျင့်ခဲ့သည်! ပစ္စည္းနောက်တစ်ခုမှာ အသင်းက လူအများ ပတ်ဝန်းကျင်များစီမံခန့်ခွဲမှုနဲ့ စံနမူနာ demo ပတ်ဝန်းကျင်များ အကြောင်းကို ကိုက်ညီစွာ ရှာဖွေနေခြင်း ဖြစ်သည်။ ယခုလည်း ဖောက်သည်များနှင့် လုပ်ဖော်ကူညီသူများထံမှ အဓိက အသုံးပြုမှုတစ်ခုမှာ Dev Box ကို စိတ်ကြိုက်ဖွဲ့စည်းထားသော ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်များအဖြစ် သုံးခြင်းဖြစ်သည်။ နှစ်ခုစလုံးမှာ MCP သုံးပြီး Dev Box များကို သဘာဝဘာသာစကားဖြင့် အပြန်အလှန် ဆက်သွယ်ကာ စီမံခန့်ခွဲနိုင်သည်။ ၎င်းသည် ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင် ထဲမှာပဲ ကျန်နေရစေပါသည်။

### ၉။ 🤖 Microsoft Foundry MCP Server


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**ဘာလုပ်တယ်ဆိုတာ**: Microsoft Foundry MCP Server သည် Azure ၏ AI ecosystem နှင့် ပူးပေါင်းဆောင်ရွက်ပြီး မော်ဒယ် စာရင်းများ၊ ပြန်လည် တင်သွင်းမှု စီမံခန့်ခွဲမှု၊ Azure AI Search ဖြင့် သတင်းအချက်အလက် စုစည်းခြင်း၊ နှင့် သုံးသပ်ခြင်းကိရိယာများကဲ့သို့ အပြည့်အစုံ ဝင်ရောက်နိုင်မှုများကို တီထွင်တင်ဆက်သူများအား ပံ့ပိုးပေးသည်။ ဤ စမ်းသပ်ဆော့ဝဲ ဆာဗာသည် AI ဖွံ့ဖြိုးတိုးတက်မှုနှင့် Azure ၏ အင်အားမြင့် AI အခြေခံအဆောက်အဦတစ်ခုအကြား အကွာအလွာကို ဖြတ်သန်းပေးကာ AI အပလီကေးရှင်းများကို ပိုမိုပေါ့ပါးစွာ ဆောက်လုပ်၊ တင်သွင်းနှင့် သုံးသပ်နိုင်ရန် အကူအညီပြုသည်။

**ဘာအတွက်အသုံးဝင်သလဲ**: ဤ စာဗာသည် Azure AI ဝန်ဆောင်မှုများနှင့် ဆက်သွယ်ရာတွင် စီးပွားရေးအဆင့် AI လုပ်ဆောင်ချက်များကို တိုက်ရိုက် ဖွံ့ဖြိုးမှု လုပ်ငန်းစဉ်သို့ယူသွားစေပြီး သင်၏ လူပြောစာကွင်းများဖြင့် မော်ဒယ်ရှာဖွေခြင်း၊ ဝန်ဆောင်မှုများ တင်သွင်းခြင်း၊ သိပ္ပံနည်းကျ အချက်အလက်များ စီမံခန့်ခွဲခြင်းနှင့် AI ဆောင်ရွက်မှုများကို သုံးသပ်ခြင်းများ ပြုလုပ်နိုင်သည်။ RAG (Retrieval-Augmented Generation) အပလီကေးရှင်းများ ဖန်တီးနေသူများ၊ မော်ဒယ်များစွာ တင်သွင်းနေသူများ သို့မဟုတ် AI သုံးသပ်မှု ပိုင်းဆိုင်ရာ လုပ်ငန်းစဉ်များ ပြုလုပ်နေသူများအတွက် အထူးပြောစရာ အင်အားသာချက်များ ရှိသည်။

**အဓိက တီထွင်သူ စွမ်းဆောင်ရည်များ**:
- **🔍 မော်ဒယ်ရှာဖွေရေး & တင်သွင်းခြင်း**: Microsoft Foundry ၏ မော်ဒယ်စာရင်းကို ရှာဖွေ၊ မော်ဒယ်အသေးစိတ်အချက်အလက်များနှင့် ကုဒ်နမူနာများရယူပြီး မော်ဒယ်များကို Azure AI ဝန်ဆောင်မှုများသို့ တင်သွင်းနိုင်ပါသည်
- **📚 သိပ္ပံနည်းကျ စီမံခန့်ခွဲမှု**: Azure AI Search အညွှန်းများ ဖန်တီး၊ စီမံခန့်ခွဲခြင်း၊ စာရွက်စာတမ်းများ ထည့်သွင်းခြင်း၊ အညွှန်းဆိုက်များ ထည့်သွင်းဆက်တင်ခြင်းနှင့် တိကျစွာ အဆင့်မြှင့်ထားသည့် RAG စနစ်များ ဖွဲ့စည်းခြင်း
- **⚡ AI အေးဂျင့် ပေါင်းစည်းမှု**: Azure AI အေးဂျင့်များနှင့် ချိတ်ဆက်ခြင်း၊ ရှိပြီးသားအေးဂျင့်များကိုမေးမြန်းခြင်းနှင့် ထုတ်လုပ်မှု အခြေအနေများတွင် အေးဂျင့်စွမ်းဆောင်ရည် သုံးသပ်ခြင်း
- **📊 သုံးသပ်မှု မြှင့်တင်ရာအခြေခံအဆောက်အအုံ**: စာသားနှင့် အေးဂျင့် သုံးသပ်မှုများ ပြီးပြည့်စုံစွာ ဆောင်ရွက်ခြင်း၊ markdown အစီရင်ခံစာများ ပြုလုပ်ခြင်းနှင့် AI အပလီကေးရှင်းများအတွက် အရည်အသွေးအာမခံမှု ထည့်သွင်းခြင်း
- **🚀 စမ်းသပ် ဆောက်လုပ်ရေးကိရိယာများ**: GitHub အခြေပြု စမ်းသပ်မှုဆိုင်ရာ တပ်ဆင်နည်းများ ရယူခြင်းနှင့် Microsoft Foundry Labs တွင် သုတေသန မော်ဒယ်များ အသုံးပြုခြင်း

**လက်တွေ့ တီထွင်သူ အသုံးပြုမှု**: "ကျွန်ုပ်၏ အပလီကေးရှင်းအတွက် Phi-4 မော်ဒယ်ကို Azure AI ဝန်ဆောင်မှုများသို့ တင်သွင်းပါ", "ကျွန်ုပ်၏ စာရွက်စာတမ်း RAG စနစ်အတွက် သစ်တောရှာဖွေမှု အညွှန်းအသစ် တစ်ခု ဖန်တီးပါ", "ကျွန်ုပ်၏ အေးဂျင့်တုံ့ပြန်မှုများကို အရည်အသွေးညီမျှမှုသတ်မှတ်ချက်များအပေါ်မှာ သုံးသပ်ပါ", သို့မဟုတ် "ကျွန်ုပ်၏ ပြန်လည်စစ်ဆေးမှု လုပ်ငန်းများအတွက် အကောင်းဆုံး မှုန့်ပညာမော်ဒယ်ကို ရှာပါ"

**လုံးလုံးကိုယ်ကို စမ်းသပ်ရန် အခြေနေ**: အောက်ပါ AI ဖွံ့ဖြိုးတိုးတက်မှု လုပ်ငန်းစဉ် အသွားအလာရှိသည်။

> "ကျွန်ုပ်သည် ဖောက်သည်ပံ့ပိုးမှု အေးဂျင့်တစ်ယောက်ကို တည်ဆောက်နေပါသည်။ မော်ဒယ်စာရင်းမှ ကောင်းမွန်သော မှုန့်ပညာမော်ဒယ်ကို ရှာဖွေရန် ကူညီပါ၊ Azure AI ဝန်ဆောင်မှုများသို့ တင်သွင်းပါ၊ ကျွန်ုပ်တို့၏ စာရွက်စာတမ်းများမှ သိပ္ပံနည်းကျ အချက်အလက် အခြေခံတည်ဆောက်ပါ၊ တုံ့ပြန်မှု အရည်အသွေး စစ်ဆေးရေး အခြေခံအဆောက်အအုံတည်ဆောက်ပါ၊ ထို့နောက် GitHub token ဖြင့် ပေါင်းစည်းမှု စမ်းသပ်မှု စတင်ရန် ကူညီပါ။"

Microsoft Foundry MCP Server သည်:
- သင့်လိုအပ်ချက်အပေါ် အခြေခံပြီး အကောင်းဆုံး မှုန့်ပညာမော်ဒယ်များ အကြံပြုရန် မော်ဒယ်စာရင်းကို မေးမြန်းသည်
- မိမိနှစ်သက်သော Azure ဒေသအတွက် တင်သွင်းမှု ညွှန်ကြားချက်များနှင့် အဆင့်သတ်မှတ်ချက် ပြသသည်
- သင်၏ စာရွက်စာတမ်းအတွက် သင့်လျော်သော စီမံကိန်းစနစ်ဖြင့် Azure AI Search အညွှန်းများ ဖွဲ့စည်းပေးသည်
- အရည်အသွေးညီမျှမှုနှင့် လုံခြုံမှု စစ်ဆေးမှုများ ပါဝင်သည့် သုံးသပ်မှု လမ်းကြောင်းများ ပြုလုပ်ပေးသည်
- GitHub အတည်ပြုချက်နှင့်အတူ စမ်းသပ်မှုအတွက် ချက်ချင်းအသုံးပြုနိုင်သော စမ်းသပ်ကုဒ်များ ဖန်တီးပေးသည်
- သင်၏နည်းပညာ stack အတွက် သီးသန့် တပ်ဆင်မှုလမ်းညွှန်များ ဖြန့်ဝေသည်

**အထင်ကရ ဥပမာ**: တီထွင်သူအနေနဲ့ မတူညီသည့် LLM မော်ဒယ်များကို ကိုင်တွယ်အသုံးပြုရာတွင် ခက်ခဲခဲ့ရသည်။ နိုင်ငံအနည်းငယ်ကို သိပေမယ့် ပိုမိုထိရောက်သော အရာများကို လက်လွတ်နေသလို ခံစားနေရသည်။ token များနှင့် quota များ စီမံခန့်ခွဲရခက်ခဲပြီး မိမိ၏ စီးပွားရေးအသုံးစရိတ် မမှန်ကန်အောင် မော်ဒယ်ရွေးချယ်မှုရှိနေသည်ကို စိုးရိမ်နေခဲ့သည်။ James Montemagno မှ ရရှိခဲ့သည့် MCP Server အကြောင်းကို လက်တွေ့ကြည့်ရှုရာတွင် မော်ဒယ်ရှာဖွေရေး လုပ်ဆောင်ချက်သည် ကြိုဆိုလိုက်သူများအတွင်း အထူးပါးပါး မော်ဒယ်များထက် ပိုမိုအထူးပြုလုပ်ထားသော မော်ဒယ်များကို ရှာဖွေလိုသူများအတွက် အထူးစိတ်ဝင်စားစရာရှိသည်။ သုံးသပ်မှု မြှင့်တင်ရာ အဆောက်အအုံသည် ကျွန်ုပ်ထင်သလောက် ကောင်းမွန်မှုတိုးတက်မှု ရရှိနေကြောင်း အတည်ပြုနိုင်ရန် ကူညီပေးသည်။

> **ℹ️ စမ်းသပ်မှု အခြေအနေ**
> 
> ဤ MCP server သည် စမ်းသပ်မှုအဆင့်တွင်ရှိပြီး တိုးတက်တည်ဆောက်နေဆဲဖြစ်သည်။ လုပ်ဆောင်ချက်များနှင့် API များဟာ ပြောင်းလဲနိုင်သည်။ Azure AI ၏ လုပ်ဆောင်ချက်များကို စမ်းသပ်ရန်နှင့် ပရိုတိုတိုက်များ တည်ဆောက်ရန် အကောင်းဆုံးဖြစ်သည်၊ ထုတ်လုပ်မှုအသုံးပြုမှုအတွက် တည်ငြိမ်မှု လိုအပ်ချက်များကို အတည်ပြုပါ။
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**ဘာလုပ်တယ်ဆိုတာ**: Microsoft 365 နှင့် Microsoft 365 Copilot နှင့် ပေါင်းစည်းသည့် AI အေးဂျင့်များနှင့် အပလီကေးရှင်းများ တည်ဆောက်ရန် လိုအပ်သော ကိရိယာများကို ဖွံ့ဖြိုးသူများအား ပံ့ပိုးပေးသည်။ ဤတွင် စီမံကိန်း ဖောက်သည်စစ်ဆေးခြင်း၊ ကုဒ်နမူနာ ရယူခြင်းနှင့် ပြဿနာရှာဖွေရေးကူညီမှုတို့ ပါဝင်သည်။

**ဘာအတွက်အသုံးဝင်သလဲ**: Microsoft 365 နှင့် Copilot အတွက် ဆောက်လုပ်ရာတွင် ရှုပ်ထွေးသော manifest schema များနှင့် သီးခြား ဖွံ့ဖြိုးတိုးတက်ရေး နည်းပညာပုံစံများ ပါဝင်သည်။ ဤ MCP server သည် သင်၏ ကုဒ်ရေးသားမှု ပတ်ဝန်းကျင်တွင် တိုက်ရိုက် အရေးကြီးသော ဖွံ့ဖြိုးရေး အရင်းအမြစ်များကို ထောက်ပံ့ပေးကာ schema များအား စစ်ဆေးခြင်း၊ နမူနာကုဒ် ရှာဖွေရေးနှင့် ပုံမှန်ပြဿနာများကူညီ ဖြေရှင်းရေး စသည့် ကိရိယာများကို အကူအညီပေးသည်။

**လက်တွေ့ အသုံးပြုမှု**: "ကျွန်ုပ်၏ ကြေညာချက် manifest ကို စစ်ဆေးပြီး schema အမှားများကို ပြင်ဆင်ပါ", "Microsoft Graph API plugin တည်ဆောက်ရန် နမူနာကုဒ် ပြပါ", "ကျွန်ုပ်၏ Teams app အထောက်အထား မအောင်မြင်မှု ပြဿနာကို ကူညီရှာဖွေပါ"

**အထင်ကရ ဥပမာ**: Build အခမ်းအနားတွင် M365 Agents အကြောင်း John Miller နှင့် စကားပြောပြီးနောက် သူက ဤ MCP ကို အကြံပြုခဲ့သည်။ M365 Agents အသစ်များအတွက် ဤ MCP သည် နမူနာများ၊ နမူနာကုဒ်များနဲ့ စတင်ရန် scaffolding ရှိသောကြောင့် စာတမ်းများတွင် မလျော်မယွင်း ရှိနေစရာမလိုဘဲ အသုံးပြုနိုင်သည်။ schema စစ်ဆေးမှု လုပ်ဆောင်ချက်များသည် manifest ဖွဲ့စည်းမှုပြဿနာများ ကိုရှောင်ရှားနိုင်စေရန် အထူးအသုံးဝင်လိမ့်မည်။

> **💡 အကြံပြုချက်**
> 
> Microsoft Learn Docs MCP Server နှင့်တွဲဖက်အသုံးပြုပါက M365 ဖွံ့ဖြိုးတိုးတက်မှုအတွက် နက်ရှိုင်းပြီး စုံလင်သော ထောက်ပံ့မှုရရှိမည်။ တစ်ခုကို တရားဝင်စာတမ်း အဖြစ် အသုံးပြု၊ စုစုပေါင်းတစ်ခုမှာ ကျက်သရေလုပ်ဆောင်မှု ကိရိယာများနှင့် ပြဿနာဖြေရှင်းကူညီမှုတို့ ဖြစ်သည်။


## အခြားချက် များ? 🔮

## 📋 နိဂုံးချုပ်

Model Context Protocol (MCP) သည် တီထွင်သူများနှင့် AI အကူအညီရနှင့် ပြင်ပကိရိယာများကို မည်သို့ ဆက်သွယ် အသုံးပြုသည်ကို ပြောင်းလဲနေသည်။ ဤ 10 ခု Microsoft MCP server များသည် AI ပေါင်းစည်းမှုကို စံကြည့်ထားသော အင်အားများအဖြစ် ပြသကာ တီထွင်သူများကို သက်ဆိုင်ရာ အပြင်ဘက် စွမ်းရည်များကို သိပ်သိပ်စွာ အသုံးပြုနိုင်စေသည့် စခန်းတစ်ခု ဖြစ်စေသည်။

Azure ecosystem ပေါ်လစီအပြည့်အ ၀ ဝင်ရောက်ဆောင်ရွက်မှုမှ စ ကလောက် ဂျ်တွေကို ထိန်းချုပ်သည့် Playwright နှင့် စာရွက် စီမံခန့်ခွဲရေးအတွက် MarkItDown ကိရိယာများထိမှတ်ထားသည်။ ဤ server များသည် MCP ၏ စံနမူနာ protocol ဖြင့် အလုပ်လုပ်ကာ စည်းစိမ်ပြီး ဆက်စပ်မှုရှိတဲ့ ဖွံ့ဖြိုးတိုးတက်မှု အတွေ့အကြုံ တစ်ခု ဖန်တီးပေးသည်။

MCP ecosystem များ များစွာ တိုးတက်လာသလို မိမိအသင်းအစည်းနှင့် ပူးပေါင်းဆောင်ရွက်ခြင်း၊ ဆာဗာအသစ်များစူးစမ်းခြင်းနှင့် ကိုယ်ပိုင် ဖြေရှင်းနည်းများ တည်ဆောက်ခြင်းသည် ဖွံ့ဖြိုးတိုးတက်မှု ထိရောက်မှုကို မြှင့်တင်ရန် အဓိကဖြစ်လာမည်။ MCP ၏ ဖွင့်လင်းစံနှုန်း ဖြစ်သောကြောင့် vendor မတူသော ကိရိယာများကို တွဲဖက်အသုံးပြု၍ သင့်လိုအပ်ချက်အတွက် အကောင်းဆုံး workflow တစ်ခု ဖန်တီးနိုင်သည်။

## 🔗 အပိုထောက်ပံ့ အရင်းအမြစ်များ

- [တရားဝင် Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP အသင်းနှင့် စာတမ်းများ](https://modelcontextprotocol.io/introduction)
- [VS Code MCP စာတမ်းများ](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP စာတမ်းများ](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP စာတမ်းများ](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP ပြဇာတ်များ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot ပြင်ဆင်မှုများ](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days ကြိုတင်ကြည့်ရှုနိုင်မှု၊ 29th/30th July](https://aka.ms/mcpdevdays)

## 🎯 လေ့ကျင့်ခန်းများ

1. **တပ်ဆင်ပြီး ဖန်တီးထားမှု စမ်းသပ်ခြင်း**: သင့် VS Code ပတ်ဝန်းကျင်တွင် MCP server များထဲမှ တစ်ခုကို တပ်ဆင်ပြီး အခြေခံ လုပ်ဆောင်ချက်များ စမ်းသပ်ပါ။
2. **လုပ်ငန်းစဉ် ပေါင်းစည်းမှု**: MCP server သုံးခု အနည်းဆုံး တစ်စုအဖြစ် ပေါင်းစည်းထားသော ဖွံ့ဖြိုးရေး လုပ်ငန်းစဉ် ပုံစံတစ်ခု ဒီဇိုင်းဆွဲပါ။
3. **စိတ်ကြိုက် Server အတွက် စီမံကိန်း**: သင်၏ နေ့စဉ် ဖွံ့ဖြိုးတိုးတက်မှု လုပ်ငန်းစဉ်တွင် စိတ်ကြိုက် MCP server တစ်ခုမှ ကူညီပေးနိုင်မည့် တာဝန်များ ရှာဖွေပြီး မူလတည်ဆောက်ချက် တစ်ခု ဖန်တီးပါ။
4. **ဆောင်ရွက်မှု စစ်တမ်း**: ပုံမှန်ဖွံ့ဖြိုးမှု အသုံးပြုမှုများတွင် MCP server များအသုံးပြုခြင်းနှင့် ရိုးရိုးနည်းလမ်းများ အသုံးပြုခြင်းတို့၏ ထိရောက်မှုကို နှိုင်းယှဉ်ပါ။
5. **လုံခြုံရေး သုံးသပ်ချက်**: သင့်ဖွံ့ဖြိုးမှု ပတ်ဝန်းကျင်တွင် MCP server များအသုံးပြုရာတွင် လုံခြုံရေးဆိုင်ရာ အကျိုးသက်ရောက်မှုများကို သုံးသပ်ပြီး အကောင်းဆုံး နည်းလမ်းများကို အကြံပြုပါ။


Next:[Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
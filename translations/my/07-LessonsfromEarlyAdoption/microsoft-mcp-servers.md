# 🚀 Developer Productivity ကို ပြောင်းလဲနေတဲ့ Microsoft MCP Servers ၁၀ ခု

## 🎯 ဒီလမ်းညွှန်မှာ သင်ယူမယ့်အကြောင်း

ဒီလက်တွေ့လမ်းညွှန်မှာ Microsoft MCP servers ၁၀ ခုကို ပြသထားပြီး AI အကူအညီပေးသူတွေနဲ့ developer တွေ ဘယ်လိုအလုပ်လုပ်ကြောင်း ပြောင်းလဲနေကြတာကို ဖော်ပြထားပါတယ်။ MCP servers တွေ ဘာလုပ်နိုင်တယ်ဆိုတာသာ မပြောပဲ Microsoft နဲ့ အခြားနေရာတွေမှာ နေ့စဉ်ဖွံ့ဖြိုးတိုးတက်မှုလုပ်ငန်းစဉ်တွေမှာ တကယ်အသုံးဝင်နေတဲ့ servers တွေကို ပြသမှာဖြစ်ပါတယ်။

ဒီလမ်းညွှန်ထဲရှိ server တစ်ခုချင်းစီကို အမှန်တကယ်အသုံးပြုမှုနဲ့ developer တွေရဲ့ တုံ့ပြန်ချက်အပေါ် အခြေခံပြီး ရွေးချယ်ထားပါတယ်။ server တစ်ခုချင်းစီ ဘာလုပ်တယ်၊ ဘာကြောင့် အရေးကြီးတယ်၊ ကိုယ့်ပရောဂျက်တွေမှာ ဘယ်လိုအကျိုးရှိမလဲဆိုတာတွေကို ရှာဖွေတွေ့ရှိနိုင်မှာပါ။ MCP အသစ်ဖြစ်သူဖြစ်စေ၊ ရှိပြီးသား setup ကို တိုးချဲ့ချင်သူဖြစ်စေ ဒီ servers တွေက Microsoft ecosystem ထဲမှာ အကျိုးရှိဆုံး၊ လက်တွေ့အသုံးဝင်ဆုံးကိရိယာတွေဖြစ်ပါတယ်။

> **💡 အမြန်စတင်ရန် အကြံပြုချက်**  
> MCP အသစ်လား? စိတ်မပူပါနဲ့! ဒီလမ်းညွှန်ကို စတင်လေ့လာသူတွေအတွက် ရေးသားထားတာပါ။ အကြောင်းအရာတွေကို တစ်ဆင့်ချင်းရှင်းပြပေးမှာဖြစ်ပြီး [Introduction to MCP](../00-Introduction/README.md) နဲ့ [Core Concepts](../01-CoreConcepts/README.md) မော်ဂျူးတွေကို ပြန်လည်ကြည့်ရှုနိုင်ပါတယ်။

## အနှစ်ချုပ်

ဒီလမ်းညွှန်မှာ Microsoft MCP servers ၁၀ ခုကို လေ့လာပြီး AI အကူအညီပေးသူတွေနဲ့ developer တွေ ဘယ်လို ပိုမိုထိရောက်စွာ ဆက်သွယ်နိုင်ကြောင်း၊ Azure resource များစီမံခန့်ခွဲခြင်းမှ စာရွက်စာတမ်းများကို ပြုလုပ်ခြင်းအထိ MCP ရဲ့ အင်အားကို ဖော်ပြထားပါတယ်။

## သင်ယူရမယ့် ရည်မှန်းချက်များ

ဒီလမ်းညွှန်အဆုံးသတ်တဲ့အချိန်မှာ သင်မှာရှိမယ့် အတတ်ပညာတွေကတော့ -  
- MCP servers တွေက developer productivity ကို ဘယ်လိုမြှင့်တင်ပေးသလဲနားလည်ခြင်း  
- Microsoft ရဲ့ အကျိုးသက်ရောက်မှုအမြင့်ဆုံး MCP server များကို သိရှိခြင်း  
- server တစ်ခုချင်းစီအတွက် လက်တွေ့အသုံးပြုမှုများ ရှာဖွေခြင်း  
- VS Code နဲ့ Visual Studio မှာ ဒီ servers တွေကို ဘယ်လိုတပ်ဆင်ပြင်ဆင်ရမလဲ သိရှိခြင်း  
- MCP ecosystem အကြီးအကျယ်နဲ့ အနာဂတ်လမ်းကြောင်းများကို ရှာဖွေခြင်း

## 🔧 MCP Servers ကို နားလည်ခြင်း - စတင်လေ့လာသူများအတွက်

### MCP Servers ဆိုတာဘာလဲ?

Model Context Protocol (MCP) အသစ်စတင်လေ့လာသူတစ်ယောက်အနေနဲ့ "MCP server ဆိုတာဘာလဲ၊ ဘာကြောင့် ဂရုစိုက်ရမလဲ?" ဆိုတဲ့ မေးခွန်းရှိနိုင်ပါတယ်။ ရိုးရှင်းတဲ့ နမူနာတစ်ခုနဲ့ စတင်ကြည့်ရအောင်။

MCP servers တွေကို သင့် AI coding အကူအညီပေးသူ (GitHub Copilot ကဲ့သို့) ကို အပြင်က ကိရိယာနဲ့ ဝန်ဆောင်မှုတွေကို ချိတ်ဆက်ပေးတဲ့ အကူအညီပေးသူတွေလို ထင်မြင်နိုင်ပါတယ်။ မိမိဖုန်းမှာ မိုးလေဝသကြည့်ဖို့၊ လမ်းညွှန်ဖို့၊ ဘဏ်လုပ်ငန်းလုပ်ဖို့ အမျိုးမျိုးသော app တွေသုံးသလို MCP servers တွေက AI အကူအညီပေးသူကို အမျိုးမျိုးသော ဖွံ့ဖြိုးရေးကိရိယာနဲ့ ဝန်ဆောင်မှုတွေနဲ့ ဆက်သွယ်နိုင်စေပါတယ်။

### MCP Servers ဖြေရှင်းပေးတဲ့ ပြဿနာ

MCP servers မရှိခင်မှာ -  
- Azure resource များစစ်ဆေးချင်ရင်  
- GitHub issue တစ်ခုဖန်တီးချင်ရင်  
- ဒေတာဘေ့စ်ကို မေးမြန်းချင်ရင်  
- စာရွက်စာတမ်းတွေရှာဖွေချင်ရင်  

ကိုယ့်ရဲ့ coding လုပ်ငန်းစဉ်ကို ရပ်နားပြီး browser ဖွင့်၊ သင့်လိုအပ်တဲ့ website ကို သွားရောက်ပြီး လက်ဖြင့်လုပ်ဆောင်ရတာ ဖြစ်ခဲ့ပါတယ်။ ဒီလို context ပြောင်းလဲမှုတွေက သင့်အလုပ်စီးဆင်းမှုကို ချိုးဖောက်ပြီး ထိရောက်မှုနည်းစေပါတယ်။

### MCP Servers တွေက Developer အတွေ့အကြုံကို ဘယ်လိုပြောင်းလဲသလဲ

MCP servers တွေနဲ့ သင့်ရဲ့ ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် (VS Code, Visual Studio စသဖြင့်) ထဲမှာပဲ နေပြီး AI အကူအညီပေးသူကို အလုပ်တွေကို တာဝန်ပေးနိုင်ပါတယ်။ ဥပမာ -  

**ယခင် workflow အစား**  
1. Coding ရပ်တန့်  
2. Browser ဖွင့်  
3. Azure portal သို့ သွားရောက်  
4. Storage account အသေးစိတ်ကြည့်ရှု  
5. VS Code သို့ ပြန်သွား  
6. Coding ဆက်လုပ်  

**ယခုလုပ်နိုင်တာ**  
1. AI ကို မေးပါ - "ကျွန်တော့် Azure storage accounts အခြေအနေ ဘယ်လိုရှိလဲ?"  
2. ရရှိတဲ့ အချက်အလက်နဲ့ coding ဆက်လုပ်  

### စတင်လေ့လာသူတွေအတွက် အဓိက အကျိုးကျေးဇူးများ

#### 1. 🔄 **Flow State ထဲမှာ ဆက်လက်နေထိုင်နိုင်ခြင်း**  
- အမျိုးမျိုးသော app တွေကြား ပြောင်းရွှေ့ရခြင်း မရှိတော့ပါ  
- ရေးသားနေတဲ့ code ပေါ်မှာ အာရုံစိုက်နိုင်ပါသည်  
- ကိရိယာများစွာကို စီမံခန့်ခွဲရတဲ့ စိတ်ဖိစီးမှု လျော့နည်းစေသည်  

#### 2. 🤖 **ရှုပ်ထွေးတဲ့ command မလိုဘဲ သဘာဝဘာသာစကား အသုံးပြုနိုင်ခြင်း**  
- SQL syntax မှတ်မိဖို့ မလိုဘဲ လိုအပ်တဲ့ data ကို ဖော်ပြနိုင်သည်  
- Azure CLI command မမှတ်မိဘဲ လုပ်ဆောင်ချင်တာကို ရှင်းပြနိုင်သည်  
- AI ကို နည်းပညာပိုင်းကို စီမံခန့်ခွဲစေပြီး သင်က logic ပေါ်မှာ အာရုံစိုက်နိုင်သည်  

#### 3. 🔗 **ကိရိယာများစွာကို ချိတ်ဆက်နိုင်ခြင်း**  
- ဝန်ဆောင်မှုအမျိုးမျိုးကို ပေါင်းစပ်ပြီး အင်အားကြီးတဲ့ workflow များ ဖန်တီးနိုင်သည်  
- ဥပမာ - "နောက်ဆုံး GitHub issues တွေကို ရယူပြီး Azure DevOps work items တွေ ဖန်တီးပါ"  
- ရေးသားရခက်တဲ့ script မလိုဘဲ automation တည်ဆောက်နိုင်သည်  

#### 4. 🌐 **တိုးတက်လာနေတဲ့ Ecosystem ကို ဝင်ရောက်အသုံးပြုနိုင်ခြင်း**  
- Microsoft, GitHub နဲ့ အခြားကုမ္ပဏီတွေ ဖန်တီးထားတဲ့ servers တွေကို အသုံးပြုနိုင်သည်  
- ကုန်ပစ္စည်းပေးသူအမျိုးမျိုးရဲ့ ကိရိယာတွေကို ပေါင်းစပ်အသုံးပြုနိုင်သည်  
- AI အကူအညီပေးသူအမျိုးမျိုးမှာ အလုပ်လုပ်နိုင်တဲ့ စံချိန်စံညွှန်း ecosystem တစ်ခုကို ဝင်ရောက်ပါဝင်နိုင်သည်  

#### 5. 🛠️ **လက်တွေ့လုပ်ရင်း သင်ယူနိုင်ခြင်း**  
- ကြိုတင်တပ်ဆင်ထားတဲ့ servers တွေနဲ့ စတင်လေ့လာနိုင်သည်  
- နောက်ပိုင်းမှာ ကိုယ်ပိုင် servers တွေ ဖန်တီးတိုးချဲ့နိုင်သည်  
- ရရှိနိုင်တဲ့ SDKs နဲ့ စာတမ်းများကို လမ်းညွှန်အဖြစ် အသုံးပြုနိုင်သည်  

### စတင်လေ့လာသူများအတွက် လက်တွေ့နမူနာ

သင် web development အသစ်ဖြစ်ပြီး ပထမဆုံး project ကို လုပ်ဆောင်နေတယ်ဆိုပါစို့။ MCP servers တွေက ဘယ်လိုကူညီနိုင်မလဲ -

**ယခင်နည်းလမ်း**  
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP servers နဲ့**  
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### စီးပွားရေးအဆင့် စံချိန်စံညွှန်း

MCP က စက်မှုလုပ်ငန်းအဆင့် စံချိန်စံညွှန်းတစ်ခုဖြစ်လာနေပြီး -  
- **တူညီမှု**: ကိရိယာနဲ့ ကုမ္ပဏီအမျိုးမျိုးမှာ တူညီတဲ့ အတွေ့အကြုံ  
- **အပြန်အလှန်ဆက်သွယ်နိုင်မှု**: ကုန်ပစ္စည်းပေးသူအမျိုးမျိုးရဲ့ servers တွေ ပေါင်းစပ်အသုံးပြုနိုင်ခြင်း  
- **အနာဂတ်အတွက် ပြင်ဆင်မှု**: အတတ်ပညာနဲ့ setup တွေကို AI အကူအညီပေးသူအမျိုးမျိုးကြား လွယ်ကူစွာ လွှဲပြောင်းနိုင်ခြင်း  
- **အသိုင်းအဝိုင်း**: အသိပညာနဲ့ အရင်းအမြစ်များ မျှဝေတဲ့ ecosystem ကြီးတစ်ခု

### စတင်ရန် - သင်ယူမယ့်အကြောင်းအရာများ

ဒီလမ်းညွှန်မှာ developer အဆင့်အားလုံးအတွက် အသုံးဝင်တဲ့ Microsoft MCP servers ၁၀ ခုကို လေ့လာမှာဖြစ်ပြီး၊ server တစ်ခုချင်းစီက -  
- ဖွံ့ဖြိုးရေးအခက်အခဲများကို ဖြေရှင်းပေး  
- ထပ်ခါထပ်ခါလုပ်ရတဲ့ အလုပ်များ လျော့နည်းစေ  
- code အရည်အသွေး မြှင့်တင်  
- သင်ယူမှု အခွင့်အလမ်းများ တိုးတက်စေ

> **💡 သင်ယူမှု အကြံပြုချက်**  
> MCP အသစ်လျှင် [Introduction to MCP](../00-Introduction/README.md) နဲ့ [Core Concepts](../01-CoreConcepts/README.md) မော်ဂျူးတွေကို အရင်ဆုံး လေ့လာပါ။ ပြီးရင် ဒီနေရာကို ပြန်လာပြီး Microsoft ကိရိယာတွေဖြင့် အကြောင်းအရာတွေကို လက်တွေ့ကြည့်ရှုနိုင်ပါသည်။  
> MCP အရေးပါမှုအကြောင်း ပိုမိုသိရှိချင်ရင် Maria Naggaga ရဲ့ [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps) ကို ဖတ်ရှုနိုင်ပါတယ်။

## VS Code နဲ့ Visual Studio မှာ MCP စတင်အသုံးပြုခြင်း 🚀

Visual Studio Code သို့မဟုတ် Visual Studio 2022 ကို GitHub Copilot နဲ့ အသုံးပြုနေပါက MCP servers တွေကို တပ်ဆင်ရတာ လွယ်ကူပါတယ်။

### VS Code Setup

VS Code အတွက် အခြေခံလုပ်ငန်းစဉ်ကတော့ -

1. **Agent Mode ကို ဖွင့်ပါ** - VS Code မှာ Copilot Chat ပြတင်းပေါ်မှာ Agent mode သို့ ပြောင်းပါ  
2. **MCP Servers ကို ပြင်ဆင်ပါ** - VS Code settings.json ဖိုင်ထဲမှာ server configuration များ ထည့်ပါ  
3. **Servers များ စတင်ပါ** - အသုံးပြုလိုတဲ့ server တစ်ခုချင်းစီအတွက် "Start" ခလုတ်ကို နှိပ်ပါ  
4. **ကိရိယာများ ရွေးချယ်ပါ** - လက်ရှိ session အတွက် အသုံးပြုမယ့် MCP servers များကို ရွေးချယ်ပါ  

အသေးစိတ် setup လမ်းညွှန်များအတွက် [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp) ကို ကြည့်ရှုပါ။

> **💡 Pro Tip: MCP Servers ကို ပရော်ဖက်ရှင်နယ်လို စီမံခန့်ခွဲပါ!**  
> VS Code Extensions view မှာ MCP Servers များကို စတင်၊ ရပ်၊ စီမံခန့်ခွဲနိုင်တဲ့ အသစ် UI တစ်ခု ပါဝင်လာပြီဖြစ်ပါတယ်။ လွယ်ကူရှင်းလင်းတဲ့ အင်တာဖေ့စ်နဲ့ စမ်းသပ်ကြည့်ပါ။

### Visual Studio 2022 Setup

Visual Studio 2022 (version 17.14 နှင့်အထက်) အတွက် -

1. **Agent Mode ကို ဖွင့်ပါ** - GitHub Copilot Chat ပြတင်းပေါ်မှာ "Ask" dropdown မှာ "Agent" ကို ရွေးချယ်ပါ  
2. **Configuration ဖိုင် ဖန်တီးပါ** - solution directory ထဲမှာ `.mcp.json` ဖိုင် ဖန်တီးပါ (အကြံပြုထားတဲ့နေရာ - `<SOLUTIONDIR>\.mcp.json`)  
3. **Servers များ ပြင်ဆင်ပါ** - MCP standard format နဲ့ server configuration များ ထည့်ပါ  
4. **ကိရိယာ အတည်ပြုခြင်း** - အသုံးပြုမယ့် ကိရိယာများအတွက် scope permission များကို အတည်ပြုပါ  

Visual Studio setup အတွက် အသေးစိတ်လမ်းညွှန်များကို [Visual Studio MCP documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers) မှာ ကြည့်ရှုနိုင်ပါတယ်။

MCP server တစ်ခုချင်းစီမှာ connection string, authentication စသည့် configuration လိုအပ်ချက်များရှိသော်လည်း IDE နှစ်ခုလုံးမှာ setup ပုံစံတူညီပါတယ်။

## Microsoft MCP Servers မှ သင်ယူရသော သင်ခန်းစာများ 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![VS Code မှာ တပ်ဆင်ရန်](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![VS Code Insiders မှာ တပ်ဆင်ရန်](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**ဘာလုပ်တယ်**: Microsoft Learn Docs MCP Server က cloud မှာ host လုပ်ထားတဲ့ ဝန်ဆောင်မှုတစ်ခုဖြစ်ပြီး AI အကူအညီပေးသူတွေကို Model Context Protocol မှတဆင့် Microsoft ရဲ့ တရားဝင်စာရွက်စာတမ်းများကို real-time ဖြင့် ရယူနိုင်စေပါတယ်။ `https://learn.microsoft.com/api/mcp` နဲ့ ချိတ်ဆက်ပြီး Microsoft Learn, Azure documentation, Microsoft 365 documentation နဲ့ အခြား Microsoft တရားဝင်အရင်းအမြစ်များကို semantic search ဖြင့် ရှာဖွေနိုင်ပါတယ်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: "စာရွက်စာတမ်းပဲ" လို့ ထင်ရနိုင်ပေမယ့် ဒီ server က Microsoft နည်းပညာတွေကို အသုံးပြုတဲ့ developer တစ်ယောက်ချင်းစီအတွက် အရေးကြီးပါတယ်။ .NET developer တွေက AI coding assistant တွေဟာ နောက်ဆုံးထွက် .NET နဲ့ C# version များကို မသိကြောင်း အကြံပြုချက်
> **💡 အကြံပြုချက်**
> 
> ကိရိယာများနှင့်သက်ဆိုင်သော မော်ဒယ်များမှာ MCP ကိရိယာများကို အသုံးပြုရန် အားပေးမှုလိုအပ်ပါသည်။ စနစ်အမိန့် သို့မဟုတ် [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) ကဲ့သို့သော အကြောင်းအရာတစ်ခု ထည့်သွင်းစဉ်းစားပါ။ ဥပမာ - "သင်တွင် `microsoft.docs.mcp` ကို အသုံးပြုခွင့်ရှိသည် – C#, Azure, ASP.NET Core, သို့မဟုတ် Entity Framework ကဲ့သို့သော Microsoft နည်းပညာများနှင့် ပတ်သက်သော မေးခွန်းများကို ကိုင်တွယ်ရာတွင် Microsoft ၏ နောက်ဆုံးထွက် တရားဝင်စာရွက်စာတမ်းများကို ရှာဖွေရန် ဒီကိရိယာကို အသုံးပြုပါ။"
>
> ဒီနည်းလမ်းကို လက်တွေ့အသုံးပြုထားသည့် ဥပမာကောင်းတစ်ခုအနေဖြင့် Awesome GitHub Copilot repository မှ [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) ကို ကြည့်ရှုနိုင်ပါသည်။ ဤ mode သည် Microsoft Learn Docs MCP server ကို အသုံးပြုကာ နောက်ဆုံးပေါ် ပုံစံများနှင့် အကောင်းဆုံး လေ့လာမှုများကို အသုံးပြု၍ C# ကုဒ်များကို သန့်ရှင်းပြီး ခေတ်မီအောင် ပြုပြင်ပေးသည်။
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**ဘာလုပ်ပေးသလဲ**: Azure MCP Server သည် Azure ၀န်ဆောင်မှုများကို အထူးပြုထားသော ၁၅ ကျော်သော ဆာဗာများစုစည်းမှုတစ်ခုဖြစ်ပြီး၊ Azure ပတ်ဝန်းကျင်တစ်ခုလုံးကို သင့် AI အလုပ်စဉ်ထဲသို့ ပေါင်းစည်းပေးသည်။ ဒါဟာ တစ်ခုတည်းသော ဆာဗာမဟုတ်ဘဲ၊ resource management, database connectivity (PostgreSQL, SQL Server), Azure Monitor log analysis with KQL, Cosmos DB integration စသည့် အင်အားကြီးသော ကွန်ရက်များစုစည်းမှုတစ်ခုဖြစ်သည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: Azure resource များကို စီမံခန့်ခွဲခြင်းအပြင်၊ Azure SDK များနှင့်အတူ အလုပ်လုပ်ရာတွင် ကုဒ်အရည်အသွေးကို အလွန်တိုးတက်စေသည်။ Agent mode ဖြင့် Azure MCP ကို အသုံးပြုသောအခါ၊ သင့်ကို ကုဒ်ရေးရာတွင် ကူညီပေးခြင်းသာမက၊ လက်ရှိ authentication ပုံစံများ၊ error handling အကောင်းဆုံးနည်းလမ်းများနှင့် နောက်ဆုံး SDK အင်္ဂါရပ်များကို အသုံးပြုသည့် *ပိုမိုကောင်းမွန်သော* Azure ကုဒ်များရေးသားနိုင်စေသည်။ အလုပ်လုပ်နိုင်မယ့် generic ကုဒ်တစ်ခုရရှိခြင်းမဟုတ်ဘဲ၊ Azure ၏ ထုတ်လုပ်မှုအတွက် အကြံပြုထားသော ပုံစံများကို လိုက်နာသည့် ကုဒ်ကို ရရှိမည်ဖြစ်သည်။

**အဓိက module များ**:
- **🗄️ Database Connectors**: Azure Database for PostgreSQL နှင့် SQL Server ကို သဘာဝဘာသာစကားဖြင့် တိုက်ရိုက် ဝင်ရောက်အသုံးပြုနိုင်ခြင်း
- **📊 Azure Monitor**: KQL ဖြင့် log စစ်တမ်းနှင့် လုပ်ငန်းဆောင်တာ အမြင်များ
- **🌐 Resource Management**: Azure resource lifecycle အပြည့်အစုံ စီမံခန့်ခွဲမှု
- **🔐 Authentication**: DefaultAzureCredential နှင့် managed identity ပုံစံများ
- **📦 Storage Services**: Blob Storage, Queue Storage, နှင့် Table Storage လုပ်ဆောင်ချက်များ
- **🚀 Container Services**: Azure Container Apps, Container Instances, နှင့် AKS စီမံခန့်ခွဲမှု
- **နှင့် အခြား အထူးပြု connector များစွာ**

**လက်တွေ့အသုံးပြုမှု**: "ကျွန်ုပ်၏ Azure storage account များကို စာရင်းပြပါ", "နောက်ဆုံးတစ်နာရီအတွင်း Log Analytics workspace မှ အမှားများကို စုံစမ်းပါ", သို့မဟုတ် "Node.js ဖြင့် မှန်ကန်သော authentication ဖြင့် Azure application တည်ဆောက်ရန် ကူညီပါ"

**ပြည့်စုံသော demonstration**: Azure MCP နှင့် GitHub Copilot for Azure extension ကို VS Code တွင် ပေါင်းစပ်အသုံးပြုသော အပြည့်အစုံ လမ်းညွှန်ချက်ဖြစ်သည်။ နှစ်ခုလုံးကို ထည့်သွင်းပြီး အောက်ပါအတိုင်း မေးမြန်းပါက -

> "DefaultAzureCredential authentication ကို အသုံးပြု၍ Azure Blob Storage သို့ ဖိုင်တင်သွင်းမည့် Python script တစ်ခု ဖန်တီးပါ။ script သည် 'mycompanystorage' ဟု အမည်ပေးထားသော Azure storage account နှင့် ချိတ်ဆက်ပြီး 'documents' ဟု အမည်ပေးထားသော container သို့ ဖိုင်တင်သွင်းရမည်၊ လက်ရှိ အချိန်မှတ်တမ်းပါသော စမ်းသပ်ဖိုင်တစ်ခု ဖန်တီးပြီး တင်သွင်းရမည်၊ အမှားများကို သေချာစွာ ကိုင်တွယ်ပြီး အသိပေး output များ ထုတ်ပေးရမည်၊ authentication နှင့် error handling အတွက် Azure ၏ အကောင်းဆုံးနည်းလမ်းများကို လိုက်နာရမည်၊ DefaultAzureCredential authentication ၏ လုပ်ဆောင်ပုံကို ရှင်းပြသည့် မှတ်ချက်များ ပါဝင်ရမည်၊ function များနှင့် စာတမ်းရေးသားမှုများဖြင့် script ကို ကောင်းမွန်စွာ ဖွဲ့စည်းထားရမည်။"

Azure MCP Server သည် အောက်ပါအတိုင်း ပြည့်စုံပြီး ထုတ်လုပ်မှုအဆင်သင့် Python script တစ်ခု ဖန်တီးပေးမည် -
- နောက်ဆုံး Azure Blob Storage SDK ကို async ပုံစံမှန်ကန်စွာ အသုံးပြုခြင်း
- DefaultAzureCredential ကို fallback chain အပြည့်အစုံရှင်းပြချက်နှင့် အကောင်အထည်ဖော်ခြင်း
- Azure အထူး error များကို သေချာ ကိုင်တွယ်သည့် error handling
- Azure SDK ၏ resource management နှင့် connection handling အကောင်းဆုံးနည်းလမ်းများ လိုက်နာခြင်း
- အသေးစိတ် logging နှင့် အသိပေး console output များ
- function များ၊ စာတမ်းရေးသားမှုများနှင့် type hints ပါဝင်သည့် ကောင်းမွန်စွာ ဖွဲ့စည်းထားသော script

Azure MCP မပါဘဲ ရရှိနိုင်မယ့် generic blob storage ကုဒ်သည် လက်ရှိ Azure ပုံစံများကို မလိုက်နာနိုင်သော်လည်း၊ Azure MCP ဖြင့် ရရှိမယ့် ကုဒ်သည် နောက်ဆုံး authentication နည်းလမ်းများကို အသုံးပြုကာ Azure အထူး error များကို ကိုင်တွယ်နိုင်ပြီး Microsoft ၏ ထုတ်လုပ်မှုအတွက် အကြံပြုထားသော နည်းလမ်းများကို လိုက်နာသည်မှာ ထူးခြားစရာဖြစ်သည်။

**နမူနာအထူးပြုချက်**: `az` နှင့် `azd` CLI command များကို မှတ်မိရန် အခက်အခဲရှိခဲ့သည်။ syntax ကို ရှာဖွေပြီး command ကို ပြေးဆွဲရခြင်းဟာ အဆင့်နှစ်ဆင့်ဖြစ်သည်။ CLI syntax မမှတ်မိတာကို ဝန်ခံချင်မိလို့ portal ထဲ ဝင်ပြီး click လုပ်တာ ပိုလွယ်ကူတယ်။ မိမိလိုချင်တာကို သဘာဝဘာသာစကားဖြင့် ဖော်ပြနိုင်တာက အံ့သြစရာကောင်းပြီး IDE ထဲကနေ မထွက်ဘဲ လုပ်နိုင်တာက ပိုကောင်းတယ်။

စတင်အသုံးပြုရန် [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) တွင် အသုံးအဆောင်များ စာရင်းကောင်းတစ်ခု ရှိသည်။ ပြည့်စုံသော setup လမ်းညွှန်များနှင့် advanced configuration ရွေးချယ်စရာများအတွက် [အတည်ပြု Azure MCP စာတမ်းများ](https://learn.microsoft.com/azure/developer/azure-mcp-server/) ကို ကြည့်ရှုနိုင်သည်။

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**ဘာလုပ်ပေးသလဲ**: GitHub MCP Server သည် GitHub ၏ ecosystem အားလုံးနှင့် ချိတ်ဆက်ပေးပြီး hosted remote access နှင့် local Docker deployment ရွေးချယ်စရာများကို ပံ့ပိုးပေးသည်။ ဒါဟာ repository operation များသာမက GitHub Actions စီမံခန့်ခွဲမှု၊ pull request workflow များ၊ issue tracking, security scanning, notifications နှင့် advanced automation စွမ်းဆောင်ရည်များပါဝင်သော ကိရိယာစုစည်းမှုတစ်ခုဖြစ်သည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: GitHub MCP Server သည် GitHub platform အပြည့်အစုံကို သင့်ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်ထဲသို့ တိုက်ရိုက် ယူဆောင်လာပေးခြင်းဖြင့် GitHub နှင့် VS Code အကြား အမြဲပြောင်းလဲရခြင်းကို လျော့နည်းစေသည်။ project management, code review, CI/CD စောင့်ကြည့်မှုများကို သဘာဝဘာသာစကား command များဖြင့် တစ်နေရာတည်းက စီမံနိုင်သည်။

> **ℹ️ Note: Agent မျိုးစုံအကြောင်း**
> 
> GitHub MCP Server ကို GitHub ၏ Coding Agent (issue များကို automated coding အတွက် သတ်မှတ်နိုင်သော AI agent) နှင့် မရောမလွဲစေပါနှင့်။ GitHub MCP Server သည် VS Code ၏ Agent mode တွင် GitHub API integration ပေးပြီး၊ Coding Agent သည် GitHub issue များသို့ သတ်မှတ်ပြီး pull request ဖန်တီးပေးသော feature တစ်ခုဖြစ်သည်။

**အဓိက စွမ်းဆောင်ရည်များ**:
- **⚙️ GitHub Actions**: CI/CD pipeline စီမံခန့်ခွဲမှု၊ workflow စောင့်ကြည့်မှုနှင့် artifact ကိုင်တွယ်မှု
- **🔀 Pull Requests**: PR ဖန်တီးခြင်း၊ ပြန်လည်သုံးသပ်ခြင်း၊ ပေါင်းစည်းခြင်းနှင့် status tracking အပြည့်အစုံ
- **🐛 Issues**: issue lifecycle စီမံခန့်ခွဲမှု၊ မှတ်ချက်ရေးခြင်း၊ label ပေးခြင်းနှင့် သတ်မှတ်ခြင်း
- **🔒 Security**: code scanning alerts, secret detection နှင့် Dependabot ပေါင်းစည်းမှု
- **🔔 Notifications**: notification စီမံခန့်ခွဲမှုနှင့် repository subscription ထိန်းချုပ်မှု
- **📁 Repository Management**: ဖိုင်လုပ်ဆောင်ချက်များ၊ branch စီမံခန့်ခွဲမှုနှင့် repository စီမံခန့်ခွဲမှု
- **👥 Collaboration**: user နှင့် organization ရှာဖွေမှု၊ team စီမံခန့်ခွဲမှုနှင့် access control

**လက်တွေ့အသုံးပြုမှု**: "ကျွန်ုပ် feature branch မှ pull request တစ်ခု ဖန်တီးပါ", "ဒီအပတ်အတွင်း မအောင်မြင်ခဲ့သော CI run များကို ပြပါ", "ကျွန်ုပ်၏ repository များအတွက် ဖွင့်ထားသော security alerts များကို စာရင်းပြပါ", သို့မဟုတ် "ကျွန်ုပ်အား သတ်မှတ်ထားသော organization များအတွင်းရှိ issue များအားလုံးကို ရှာပါ"

**ပြည့်စုံသော demonstration**: GitHub MCP Server ၏ စွမ်းဆောင်ရည်များကို ပြသသည့် workflow အားဖြင့် -

> "ကျွန်ုပ်တို့၏ sprint review အတွက် ပြင်ဆင်ရန် လိုအပ်သည်။ ဒီအပတ်အတွင်း ကျွန်ုပ်ဖန်တီးထားသော pull request များအားလုံးကို ပြပါ၊ CI/CD pipeline များ၏ status ကို စစ်ဆေးပါ၊ လိုအပ်သော security alerts များ၏ အကျဉ်းချုပ်ကို ဖန်တီးပါ၊ 'feature' label ပါသော merged PR များအပေါ် အခြေခံ၍ release notes များ ရေးဆွဲရန် ကူညီပါ။"

GitHub MCP Server သည် -
- မကြာသေးမီက ဖန်တီးထားသော pull request များကို အသေးစိတ် status အချက်အလက်များနှင့် စုံစမ်းမေးမြန်းပေးမည်
- workflow run များကို စစ်ဆေးပြီး မအောင်မြင်မှုများ သို့မဟုတ် performance ပြဿနာများကို ဖော်ပြပေးမည်
- security scanning ရလဒ်များကို စုစည်းပြီး အရေးကြီးသော alerts များကို ဦးစားပေးပေးမည်
- merged PR များမှ အချက်အလက်များကို ထုတ်ယူ၍ ပြည့်စုံသော release notes များ ဖန်တီးပေးမည်
- sprint စီမံခန့်ခွဲမှုနှင့် release ပြင်ဆင်မှုအတွက် လုပ်ဆောင်ရန် အဆင့်များကို ပံ့ပိုးပေးမည်

**နမူနာအထူးပြုချက်**: code review workflow များအတွက် အသုံးပြုရတာကို ကြိုက်တယ်။ VS Code, GitHub notification များနှင့် pull request စာမျက်နှာများအကြား ပြောင်းလဲရခြင်းမရှိဘဲ "ကျွန်ုပ်အား review အတွက် စောင့်ဆိုင်းနေသော PR များကို ပြပါ" ဟု ပြောပြီး "PR #123 တွင် authentication method ၏ error handling အကြောင်း မှတ်ချက်ထည့်ပါ" ဟု ပြောနိုင်သည်။ server သည် GitHub API ခေါ်ဆိုမှုများကို ကိုင်တွယ်ပြီး ဆွေးနွေးမှု context ကို ထိန်းသိမ်းကာ ပိုမိုတိုးတက်သော review မှတ်ချက်များရေးသားရာတွင် ကူညီပေးသည်။

**Authentication ရွေးချယ်စရာများ**: server သည် OAuth (VS Code တွင် အဆင်ပြေစွာ) နှင့် Personal Access Tokens နှစ်မျိုးလုံးကို ပံ့ပိုးပြီး သင့်လိုအပ်ချက်အရ GitHub လုပ်ဆောင်ချက်များသာ ဖွင့်နိုင်သည်။ remote hosted service အဖြစ် သို့မဟုတ် local Docker ဖြင့် လုံးဝထိန်းချုပ်မှုရှိစွာ အသုံးပြုနိုင်သည်။

> **💡 Pro Tip**
> 
> MCP server settings တွင် `--toolsets` parameter ကို သင့်လိုအပ်သည့် toolset များသာ ဖွင့်ရန် သတ်မှတ်ခြင်းဖြင့် context အရွယ်အစား လျော့နည်းစေပြီး AI tool ရွေးချယ်မှုကို တိုးတက်စေပါ။ ဥပမာ core development workflow များအတွက် `"--toolsets", "repos,issues,pull_requests,actions"` ကို MCP configuration args တွင် ထည့်သွင်းပါ၊ သို့မဟုတ် GitHub monitoring အတွက်သာလိုလျှင် `"--toolsets", "notifications, security"` ကို အသုံးပြုနိုင်သည်။

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**ဘာလုပ်ပေးသလဲ**: MarkItDown သည် အမျိုးမျိုးသောဖိုင်ဖော်မတ်များကို အရည်အသွေးမြင့် Markdown အဖြစ် ပြောင်းလဲပေးနိုင်သော စာရွက်စာတမ်းပြောင်းလဲခြင်းဆာဗာတစ်ခုဖြစ်ပြီး၊ LLM အသုံးပြုမှုနှင့် စာသားခွဲခြမ်းစိတ်ဖြာမှုလုပ်ငန်းစဉ်များအတွက် အထူးသင့်လျော်စွာ တိုးတက်စွာ ပြင်ဆင်ထားသည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: ခေတ်မီစာရွက်စာတမ်းလုပ်ငန်းစဉ်များအတွက် မရှိမဖြစ်လိုအပ်သည်! MarkItDown သည် အမျိုးမျိုးသောဖိုင်ဖော်မတ်များကို ထိန်းသိမ်းကာ စာရွက်စာတမ်း၏ အရေးကြီးသော ဖွဲ့စည်းမှုများဖြစ်သည့် ခေါင်းစဉ်များ၊ စာရင်းများ၊ ဇယားများနှင့် လင့်ခ်များကို ထိန်းသိမ်းပေးနိုင်သည်။ ရိုးရိုးစာသားထုတ်ယူခြင်းကိရိယာများနှင့် မတူဘဲ AI အလုပ်လုပ်မှုနှင့် လူသားဖတ်ရှုနိုင်မှုအတွက် အဓိပ္ပါယ်နှင့် ဖော်မတ်ကို ထိန်းသိမ်းပေးရန် အာရုံစိုက်ထားသည်။

**ထောက်ခံထားသောဖိုင်ဖော်မတ်များ**:
- **ရုံးစာရွက်စာတမ်းများ**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **မီဒီယာဖိုင်များ**: ပုံများ (EXIF မီတာဒေတာနှင့် OCR ပါဝင်သည်), အသံဖိုင်များ (EXIF မီတာဒေတာနှင့် စကားပြောစာတမ်း)
- **ဝက်ဘ်အကြောင်းအရာများ**: HTML, RSS feeds, YouTube URL များ, Wikipedia စာမျက်နှာများ
- **ဒေတာဖော်မတ်များ**: CSV, JSON, XML, ZIP ဖိုင်များ (အတွင်းပါဝင်သောအရာများကို ထပ်မံစစ်ဆေးသည်)
- **စာပေဖော်မတ်များ**: EPub, Jupyter notebooks (.ipynb)
- **အီးမေးလ်**: Outlook မက်ဆေ့ခ်ျများ (.msg)
- **တိုးတက်သော**: Azure Document Intelligence ပေါင်းစပ်မှုဖြင့် PDF ကို ပိုမိုကောင်းမွန်စွာ ဆက်လက်လုပ်ဆောင်နိုင်သည်

**တိုးတက်သောစွမ်းရည်များ**: MarkItDown သည် OpenAI client ဖြင့် ပံ့ပိုးထားပါက LLM အခြေပြု ပုံဖော်ပြချက်များ၊ Azure Document Intelligence ဖြင့် PDF ကို ပိုမိုကောင်းမွန်စွာ ဆက်လက်လုပ်ဆောင်ခြင်း၊ အသံစာတမ်းရေးခြင်းနှင့် ဖိုင်ဖော်မတ်အသစ်များထည့်သွင်းနိုင်သော ပလပ်ဂင်စနစ်များကို ထောက်ပံ့ပေးသည်။

**လက်တွေ့အသုံးပြုမှု**: "ဒီ PowerPoint ကို Markdown အဖြစ် ပြောင်းလဲပြီး ကျွန်ုပ်တို့၏ စာရွက်စာတမ်းဆိုဒ်အတွက် အသုံးပြုပါ", "ဒီ PDF မှ စာသားကို ခေါင်းစဉ်ဖွဲ့စည်းမှုမှန်ကန်စွာ ထုတ်ယူပါ", "ဒီ Excel စာရွက်ကို ဖတ်ရှုနိုင်သော ဇယားအဖြစ် ပြောင်းလဲပါ"

**ထူးခြားသော ဥပမာ**: [MarkItDown စာတမ်းများ](https://github.com/microsoft/markitdown#why-markdown) မှ ကိုးကားပါက -


> Markdown သည် ရိုးရှင်းသော စာသားနှင့် အလွန်နီးစပ်ပြီး များစွာသော မာကပ်အမှတ်အသား သို့မဟုတ် ဖော်မတ်မရှိပေမယ့် အရေးကြီးသော စာရွက်စာတမ်းဖွဲ့စည်းမှုကို ဖော်ပြနိုင်သည်။ OpenAI ၏ GPT-4o ကဲ့သို့သော လူကြိုက်များသော LLM များသည် သဘာဝအားဖြင့် Markdown ကို "ပြောဆို" နိုင်ပြီး မေးခွန်းမမေးခင်မှတစ်ဆင့် Markdown ကို တုံ့ပြန်ချက်များတွင် ထည့်သွင်းအသုံးပြုကြသည်။ ၎င်းသည် Markdown ဖော်မတ်ထားသော စာသားများစွာဖြင့် လေ့ကျင့်ထားကြောင်း ပြသသည်။ ထို့အပြင် Markdown စံနှုန်းများသည် token အသုံးပြုမှုအတွက်လည်း ထိရောက်မှုရှိသည်။

MarkItDown သည် စာရွက်စာတမ်းဖွဲ့စည်းမှုကို ထိန်းသိမ်းရာတွင် အလွန်ကောင်းမွန်ပြီး AI လုပ်ငန်းစဉ်များအတွက် အရေးကြီးသည်။ ဥပမာ PowerPoint ကို ပြောင်းလဲရာတွင် slide အစီအစဉ်ကို ခေါင်းစဉ်မှန်ကန်စွာ ထိန်းသိမ်းပေးပြီး ဇယားများကို Markdown ဇယားအဖြစ် ထုတ်ယူပေးသည်၊ ပုံများအတွက် alt စာသားထည့်သွင်းပေးပြီး မိန့်ခွန်းမှတ်စုများကိုပါ လုပ်ဆောင်ပေးသည်။ ဇယားများကို ဖတ်ရှုနိုင်သော ဒေတာဇယားများအဖြစ် ပြောင်းလဲပေးပြီး ရလာသော Markdown သည် မူလတင်ဆက်မှု၏ အတွဲအဖွဲ့ကို ထိန်းသိမ်းထားသည်။ ၎င်းသည် တင်ဆက်မှုအကြောင်းအရာကို AI စနစ်များသို့ ထည့်သွင်းရန် သို့မဟုတ် ရှိပြီးသား slide များမှ စာရွက်စာတမ်းဖန်တီးရာတွင် အထူးသင့်တော်သည်။

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**ဘာလုပ်ပေးသလဲ**: SQL Server ဒေတာဘေ့စ်များ (on-premises, Azure SQL, သို့မဟုတ် Fabric) ကို စကားပြောဖြင့် ဝင်ရောက်အသုံးပြုခွင့် ပေးသည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: PostgreSQL server နှင့် ဆင်တူသော်လည်း Microsoft SQL ပတ်ဝန်းကျင်အတွက် ဖြစ်သည်။ ရိုးရှင်းသော connection string ဖြင့် ချိတ်ဆက်ပြီး သဘာဝဘာသာစကားဖြင့် မေးမြန်းနိုင်သည် – context ပြောင်းရန် မလိုတော့ပါ!

**လက်တွေ့အသုံးပြုမှု**: "နောက်ဆုံး ၃၀ ရက်အတွင်း မဖြည့်ဆည်းရသေးသော အော်ဒါများအားလုံးကို ရှာပါ" ဆိုသော မေးခွန်းကို သင့်တော်သော SQL မေးခွန်းများသို့ ပြောင်းလဲပြီး ဖော်မတ်ထားသော ရလဒ်များ ပြန်ပေးသည်။

**ထူးခြားသော ဥပမာ**: ဒေတာဘေ့စ် ချိတ်ဆက်မှုကို တပ်ဆင်ပြီးနောက်၊ သင့်ဒေတာနှင့် ချက်ချင်း စကားပြောဆက်သွယ်နိုင်သည်။ ဘလော့ဂ်စာတမ်းတွင် "သင့်ချိတ်ဆက်ထားသော ဒေတာဘေ့စ်က ဘယ်ဟာလဲ?" ဆိုသော ရိုးရှင်းသောမေးခွန်းဖြင့် ပြသထားသည်။ MCP server သည် သင့် SQL Server instance နှင့် ချိတ်ဆက်ပြီး လက်ရှိ ဒေတာဘေ့စ် ချိတ်ဆက်မှုအကြောင်းအရာများကို ပြန်လည်ပေးပို့သည် – SQL စာကြောင်းတစ်ကြောင်းမှ မရေးဘဲ။ ဆာဗာသည် schema စီမံခန့်ခွဲမှုမှ ဒေတာပြုပြင်ထိန်းသိမ်းမှုအထိ သဘာဝဘာသာစကားဖြင့် လုပ်ဆောင်နိုင်သည်။ VS Code နှင့် Claude Desktop ဖြင့် ပြည့်စုံသော တပ်ဆင်ခြင်းနှင့် ဖော်ပြချက်များအတွက် [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/) ကို ကြည့်ပါ။

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**ဘာလုပ်ပေးသလဲ**: AI ကို ဝက်ဘ်စာမျက်နှာများနှင့် အပြန်အလှန် ဆက်သွယ်၍ စမ်းသပ်ခြင်းနှင့် အလိုအလျောက်လုပ်ဆောင်မှုများ ပြုလုပ်နိုင်စေသည်။

> **ℹ️ GitHub Copilot ကို အားဖြည့်ပေးခြင်း**
> 
> Playwright MCP Server သည် GitHub Copilot ၏ Coding Agent ကို ဝက်ဘ်ဘရောက်ဇာ စွမ်းဆောင်ရည်ဖြင့် အားဖြည့်ပေးသည်! [ဒီအင်္ဂါရပ်အကြောင်း ပိုမိုသိရှိရန်](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/) ကို ကြည့်ပါ။

**ဘာကြောင့် အသုံးဝင်သလဲ**: သဘာဝဘာသာစကား ဖော်ပြချက်များဖြင့် အလိုအလျောက် စမ်းသပ်မှုများအတွက် အကောင်းဆုံးဖြစ်သည်။ AI သည် ဝက်ဘ်ဆိုက်များကို လမ်းညွှန်နိုင်ပြီး ဖောင်များ ဖြည့်စွက်နိုင်ပြီး ဖော်ပြချက်များအတိုင်း ဒေတာများ ထုတ်ယူနိုင်သည် – ၎င်းသည် အလွန်အစွမ်းထက်သော နည်းပညာဖြစ်သည်!

**လက်တွေ့အသုံးပြုမှု**: "လော့ဂ်အင် လုပ်ငန်းစဉ်ကို စမ်းသပ်ပြီး ဒက်ရှ်ဘုတ်မှန်ကန်စွာ ဖွင့်လှစ်နေကြောင်း အတည်ပြုပါ" သို့မဟုတ် "ကုန်ပစ္စည်းများ ရှာဖွေပြီး ရလဒ်စာမျက်နှာကို စစ်ဆေးသည့် စမ်းသပ်မှုတစ်ခု ဖန်တီးပါ" – အက်ပလီကေးရှင်း၏ မူရင်းကုဒ် မလိုအပ်ဘဲ

**ထူးခြားသော ဥပမာ**: ကျွန်ုပ်၏ အဖွဲ့သား Debbie O'Brien သည် Playwright MCP Server ဖြင့် အံ့သြဖွယ် ကောင်းမွန်သော အလုပ်များ ပြုလုပ်နေသည်။ ဥပမာအားဖြင့် သူမသည် အက်ပလီကေးရှင်း၏ မူရင်းကုဒ် မရှိဘဲ ပြည့်စုံသော Playwright စမ်းသပ်မှုများ ဖန်တီးနိုင်ကြောင်း ပြသခဲ့သည်။ သူမ၏ အခြေအနေတွင် Copilot ကို "Garfield" ဟု ရုပ်ရှင်ရှာဖွေရန်၊ ရလဒ်စာမျက်နှာတွင် ရုပ်ရှင်ပါရှိကြောင်း အတည်ပြုရန် စမ်းသပ်မှုတစ်ခု ဖန်တီးရန် တောင်းဆိုခဲ့သည်။ MCP သည် ဘရောက်ဇာ စက်တင်တစ်ခု ဖွင့်ပြီး စာမျက်နှာဖွဲ့စည်းမှုကို DOM snapshot များဖြင့် စူးစမ်းကာ မှန်ကန်သော selector များ ရှာဖွေပြီး ပထမဆုံး စမ်းသပ်မှုတွင် ဖြတ်သန်းနိုင်သော TypeScript စမ်းသပ်မှုကို ဖန်တီးပေးခဲ့သည်။

ဤနည်းလမ်းသည် သဘာဝဘာသာစကားညွှန်ကြားချက်များနှင့် အကောင်အထည်ဖော်နိုင်သော စမ်းသပ်ကုဒ်များအကြား အတားအဆီးကို ဖြတ်ကျော်ပေးသည်။ ရိုးရာနည်းလမ်းများတွင် စမ်းသပ်မှုကို လက်ဖြင့်ရေးသားရခြင်း သို့မဟုတ် ကုဒ်အခြေခံကို ဝင်ရောက်ကြည့်ရှုရခြင်း လိုအပ်သည်။ သို့သော် Playwright MCP ဖြင့် သင်သည် ပြင်ပဆိုက်များ၊ client အက်ပလီကေးရှင်းများ သို့မဟုတ် ကုဒ်ဝင်ရောက်ကြည့်ရှုခွင့်မရှိသော black-box စမ်းသပ်မှုများကို စမ်းသပ်နိုင်သည်။

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**ဘာလုပ်ပေးသလဲ**: Azure AI Foundry MCP Server သည် Azure ၏ AI ပတ်ဝန်းကျင်ကို အပြည့်အစုံ အသုံးပြုနိုင်စေပြီး၊ မော်ဒယ်စာရင်းများ၊ တပ်ဆင်မှုစီမံခန့်ခွဲမှု၊ Azure AI Search ဖြင့် အသိပညာညွှန်ကြားမှု၊ နှင့် အကဲဖြတ်ကိရိယာများကို ဖော်ပြပေးသည်။ ဒီစမ်းသပ်ဆာဗာက AI ဖွံ့ဖြိုးတိုးတက်မှုနဲ့ Azure ၏ အင်အားကြီး AI အခြေခံအဆောက်အအုံကြား ချိတ်ဆက်ပေးကာ AI အပလီကေးရှင်းများကို တည်ဆောက်၊ တပ်ဆင်၊ နှင့် အကဲဖြတ်ရန် ပိုမိုလွယ်ကူစေသည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: ဒီဆာဗာက Azure AI ဝန်ဆောင်မှုများကို သင့်ဖွံ့ဖြိုးရေး လုပ်ငန်းစဉ်ထဲသို့ တိုက်ရိုက် ပေးဆောင်ခြင်းဖြင့် စီးပွားရေးအဆင့် AI စွမ်းဆောင်ရည်များကို ပြောင်းလဲပေးသည်။ Azure ပေါ်တယ်၊ စာတမ်းများ၊ နှင့် IDE အကြား ပြောင်းလဲသွားလာရန် မလိုတော့ပဲ မော်ဒယ်တွေ ရှာဖွေ၊ ဝန်ဆောင်မှုတွေ တပ်ဆင်၊ အသိပညာအခြေခံများ စီမံခန့်ခွဲ၊ နှင့် AI စွမ်းဆောင်ရည်ကို သဘာဝဘာသာစကား အမိန့်များဖြင့် အကဲဖြတ်နိုင်သည်။ RAG (Retrieval-Augmented Generation) အပလီကေးရှင်းများ တည်ဆောက်သူများ၊ မော်ဒယ်များစွာ တပ်ဆင်သူများ၊ သို့မဟုတ် AI အကဲဖြတ်မှု လမ်းကြောင်းများ တည်ဆောက်သူများအတွက် အထူးအသုံးဝင်သည်။

**အဓိက ဖွံ့ဖြိုးရေးသူ စွမ်းရည်များ**:
- **🔍 မော်ဒယ် ရှာဖွေခြင်းနှင့် တပ်ဆင်ခြင်း**: Azure AI Foundry ၏ မော်ဒယ်စာရင်းကို စူးစမ်း၊ မော်ဒယ်အသေးစိတ်အချက်အလက်များနှင့် ကုဒ်နမူနာများ ရယူ၊ မော်ဒယ်များကို Azure AI Services သို့ တပ်ဆင်နိုင်သည်
- **📚 အသိပညာ စီမံခန့်ခွဲမှု**: Azure AI Search အညွှန်းများ ဖန်တီး၊ စီမံခန့်ခွဲ၊ စာရွက်စာတမ်းများ ထည့်သွင်း၊ အညွှန်းတင်စက်များ ပြင်ဆင်၊ နှင့် ချဲ့ထွင် RAG စနစ်များ တည်ဆောက်နိုင်သည်
- **⚡ AI အေးဂျင့် ပေါင်းစည်းမှု**: Azure AI Agents နှင့် ချိတ်ဆက်၊ ရှိပြီးသား အေးဂျင့်များကို မေးမြန်း၊ ထုတ်လုပ်မှုအခြေအနေများတွင် အေးဂျင့် စွမ်းဆောင်ရည်ကို အကဲဖြတ်နိုင်သည်
- **📊 အကဲဖြတ်မှု ဖွဲ့စည်းမှု**: စာသားနှင့် အေးဂျင့် အကဲဖြတ်မှုများ ပြုလုပ်၊ markdown အစီရင်ခံစာများ ထုတ်ပေး၊ AI အပလီကေးရှင်းများအတွက် အရည်အသွေး အာမခံမှု တည်ဆောက်နိုင်သည်
- **🚀 စမ်းသပ်မှု ကိရိယာများ**: GitHub အခြေပြု စမ်းသပ်မှုများအတွက် တပ်ဆင်မှု လမ်းညွှန်ချက်များ ရယူ၊ Azure AI Foundry Labs မှ နောက်ဆုံးပေါ် သုတေသန မော်ဒယ်များကို ဝင်ရောက် အသုံးပြုနိုင်သည်

**လက်တွေ့ ဖွံ့ဖြိုးရေးသူ အသုံးပြုမှု**: "ကျွန်ုပ်၏ အပလီကေးရှင်းအတွက် Phi-4 မော်ဒယ်ကို Azure AI Services သို့ တပ်ဆင်ပါ", "ကျွန်ုပ်၏ စာရွက်စာတမ်း RAG စနစ်အတွက် အသစ်သော ရှာဖွေ အညွှန်းတစ်ခု ဖန်တီးပါ", "ကျွန်ုပ်၏ အေးဂျင့် တုံ့ပြန်မှုများကို အရည်အသွေး စံချိန်များနှင့် နှိုင်းယှဉ် အကဲဖြတ်ပါ", သို့မဟုတ် "ကျွန်ုပ်၏ ရှုပ်ထွေးသော ခွဲခြမ်းစိတ်ဖြာမှု လုပ်ငန်းများအတွက် အကောင်းဆုံး အကြံပြုမော်ဒယ်ကို ရှာပါ"

**ပြည့်စုံသော စမ်းသပ်မှု အခြေအနေ**: အောက်ပါ AI ဖွံ့ဖြိုးရေး လုပ်ငန်းစဉ် အလွန်အစွမ်းထက်သည်။

> "ကျွန်ုပ်သည် ဖောက်သည်ပံ့ပိုးမှု အေးဂျင့်တစ်ယောက် တည်ဆောက်နေပါသည်။ စာရင်းမှ ကောင်းမွန်သော အကြံပြုမော်ဒယ်တစ်ခု ရှာဖွေ၊ Azure AI Services သို့ တပ်ဆင်၊ ကျွန်ုပ်တို့၏ စာရွက်စာတမ်းမှ အသိပညာအခြေခံ တည်ဆောက်၊ တုံ့ပြန်မှု အရည်အသွေး စမ်းသပ်ရန် အကဲဖြတ်မှု ဖွဲ့စည်းမှု တည်ဆောက်၊ ထို့နောက် GitHub token ဖြင့် စမ်းသပ်မှုအတွက် ပေါင်းစည်းမှု စမ်းသပ်မှုကို ကူညီပါ။"

Azure AI Foundry MCP Server သည်:
- သင့်လိုအပ်ချက်အရ အကောင်းဆုံး အကြံပြုမော်ဒယ်များကို မော်ဒယ်စာရင်းမှ မေးမြန်းပေးမည်
- သင့်နှစ်သက်ရာ Azure ဒေသအတွက် တပ်ဆင်မှု အမိန့်များနှင့် အရေအတွက် အချက်အလက်များ ပေးမည်
- သင့်စာရွက်စာတမ်းအတွက် သင့်တော်သော စာရင်း schema ဖြင့် Azure AI Search အညွှန်းများ တည်ဆောက်ပေးမည်
- အရည်အသွေး စံချိန်များနှင့် လုံခြုံရေး စစ်ဆေးမှုများပါဝင်သော အကဲဖြတ်မှု လမ်းကြောင်းများ ပြင်ဆင်ပေးမည်
- GitHub အတည်ပြုချက်ဖြင့် စမ်းသပ်မှုအတွက် စမ်းသပ်ကုဒ်များ ထုတ်ပေးမည်
- သင့်နည်းပညာ stack အတွက် သင့်တော်သော တပ်ဆင်မှု လမ်းညွှန်ချက်များ ပေးမည်

**ထူးခြားသော ဥပမာ**: ဖွံ့ဖြိုးရေးသူတစ်ယောက်အနေနဲ့ မတူညီတဲ့ LLM မော်ဒယ်တွေကို လိုက်လံကြည့်ရှုရတာ ခက်ခဲခဲ့ပါတယ်။ အဓိက မော်ဒယ်အချို့ကိုသာ သိပြီး၊ ထူးခြားတဲ့ ထုတ်လုပ်မှုနှင့် ထိရောက်မှု တိုးတက်မှုတွေကို လက်လွတ်နေသလို ခံစားရပါတယ်။ Token နဲ့ quota တွေကို စီမံခန့်ခွဲရတာ စိတ်ဖိစီးမှုရှိပြီး ခက်ခဲပါတယ် – မည်သည့် မော်ဒယ်ကို မည်သည့် လုပ်ငန်းအတွက် ရွေးချယ်ရမည်ကို မသေချာဘူး၊ ဘတ်ဂျက်ကို မထိရောက်စွာ အသုံးပြုနေမလား မသိပါဘူး။ ဒီ MCP Server ကို James Montemagno က MCP Server အကြံပြုချက်များ ရှာဖွေစဉ်က ကြားခဲ့ပြီး အသုံးပြုဖို့ စိတ်လှုပ်ရှားနေပါတယ်! မော်ဒယ် ရှာဖွေရေး စွမ်းရည်တွေက ကျွန်ုပ်လို မော်ဒယ်များကို ပိုမိုရှာဖွေလိုသူများအတွက် အထူးထူးခြားပါတယ်။ အကဲဖြတ်မှု ဖွဲ့စည်းမှုကလည်း အမှန်တကယ် ပိုမိုကောင်းမွန်တဲ့ ရလဒ်ရရှိနေကြောင်း အတည်ပြုရာမှာ ကူညီပေးမယ်လို့ မျှော်လင့်ပါတယ်၊ အသစ်တစ်ခု စမ်းသပ်တာ မဟုတ်ပါဘူး။

> **ℹ️ Experimental Status**
> 
> ဒီ MCP server က စမ်းသပ်ဆာဗာဖြစ်ပြီး တိုးတက်မှုအဆင့်တွင် ရှိသည်။ လုပ်ဆောင်ချက်များနှင့် API များ ပြောင်းလဲနိုင်သည်။ Azure AI စွမ်းဆောင်ရည်များကို စမ်းသပ်ရန်နှင့် စမ်းသပ်မှုများ တည်ဆောက်ရန် အထူးသင့်တော်သော်လည်း ထုတ်လုပ်မှုအတွက် တည်ငြိမ်မှုလိုအပ်ချက်များကို စစ်ဆေးရန် လိုအပ်သည်။
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**ဘာလုပ်ပေးသလဲ**: Microsoft 365 နှင့် Microsoft 365 Copilot နှင့် ပေါင်းစည်းထားသော AI အေးဂျင့်များနှင့် အပလီကေးရှင်းများ တည်ဆောက်ရာတွင် လိုအပ်သော ကိရိယာများ၊ schema အတည်ပြုခြင်း၊ နမူနာကုဒ် ရယူခြင်း၊ နှင့် ပြဿနာဖြေရှင်းမှု ကူညီမှုများ ပေးသည်။

**ဘာကြောင့် အသုံးဝင်သလဲ**: Microsoft 365 နှင့် Copilot အတွက် တည်ဆောက်ရာတွင် ရှုပ်ထွေးသော manifest schema များနှင့် အထူးဖွံ့ဖြိုးရေး ပုံစံများ ပါဝင်သည်။ ဒီ MCP server က သင့်ကုဒ်ရေးရာ ပတ်ဝန်းကျင်ထဲသို့ တိုက်ရိုက် ဖွံ့ဖြိုးရေး အရင်းအမြစ်များကို ယူဆောင်ပေးကာ schema များ အတည်ပြု၊ နမူနာကုဒ် ရှာဖွေ၊ နှင့် ပုံမှန် ပြဿနာများကို စာတမ်းများကို မကြာခဏ ရှာဖွေရန် မလိုဘဲ ဖြေရှင်းနိုင်စေသည်။

**လက်တွေ့ အသုံးပြုမှု**: "ကျွန်ုပ်၏ declarative agent manifest ကို အတည်ပြု၍ schema အမှားများကို ပြင်ဆင်ပါ", "Microsoft Graph API plugin တည်ဆောက်ရန် နမူနာကုဒ် ပြပါ", သို့မဟုတ် "ကျွန်ုပ်၏ Teams app အတည်ပြုမှု ပြဿနာများကို ကူညီ ဖြေရှင်းပါ"

**ထူးခြားသော ဥပမာ**: Build တွင် M365 Agents အကြောင်း John Miller နှင့် စကားပြောပြီးနောက် သူ့ကို ဆက်သွယ်ခဲ့ပြီး ဒီ MCP ကို အကြံပြုခဲ့သည်။ M365 Agents အသစ်စတင်သူများအတွက် စာတမ်းများ များစွာ မဖတ်ရပဲ စတင်နိုင်ရန် template များ၊ နမူနာကုဒ်များ၊ နှင့် scaffolding များ ပေးသောကြောင့် အထူးကောင်းမွန်သည်။ schema အတည်ပြုမှု လုပ်ဆောင်ချက်များက manifest ဖွဲ့စည်းမှု အမှားများကို ရှောင်ရှားနိုင်ပြီး နာရီများကြာ debugging လုပ်ရခြင်းကို လျော့နည်းစေမည်ဟု တွေးထားသည်။

> **💡 Pro Tip**
> 
> ဒီဆာဗာကို Microsoft Learn Docs MCP Server နှင့် တွဲဖက် အသုံးပြုပါက M365 ဖွံ့ဖြိုးရေးအတွက် ပြည့်စုံသော ကူညီမှု ရရှိမည် – တစ်ခုက တရားဝင် စာတမ်းများ ပေးပြီး၊ ဒုတိယက လက်တွေ့ ဖွံ့ဖြိုးရေး ကိရိယာများနှင့် ပြဿနာဖြေရှင်းမှု ကူညီမှု ပေးသည်။

## နောက်တစ်ဆင့်ဘာလဲ? 🔮

## 📋 နိဂုံးချုပ်

Model Context Protocol (MCP) သည် ဖွံ့ဖြိုးရေးသူများအား AI အကူအညီပေးသူများနှင့် ပြင်ပကိရိယာများနှင့် ပေါင်းစည်းဆက်သွယ်ရာတွင် ပြောင်းလဲမှုကြီး ဖြစ်စေသည်။ ဒီ Microsoft MCP ဆာဗာ ၁၀ ခုက စံချိန်တကျ AI ပေါင်းစည်းမှု၏ အင်အားကို ပြသကာ ဖွံ့ဖြိုးရေးသူများကို အဆင်ပြေစွာ လုပ်ငန်းစဉ်များ ဆက်လက်လုပ်ဆောင်နိုင်စေသည်။

Azure ၏ အပြည့်အစုံ ပတ်ဝန်းကျင် ပေါင်းစည်းမှုမှ စ၍ Playwright ကဲ့သို့ ဘရောက်ဇာ အလိုအလျောက်လုပ်ဆောင်မှုနှင့် MarkItDown ကဲ့သို့ စာရွက်စာတမ်း ပြုလုပ်မှု ကိရိယာများအထိ၊ ဒီဆာဗာများက MCP ဖြင့် ထုတ်လုပ်မှု ထိရောက်မှုကို တိုးတက်စေသည်။ စံချိန်တကျ protocol က ဒီကိရိယာများကို အဆက်မပြတ် ပေါင်းစည်းနိုင်စေကာ တစ်ခုတည်းသော ဖွံ့ဖြိုးရေး အတွေ့အကြုံကို ဖန်တီးပေးသည်။

MCP ပတ်ဝန်းကျင် ဆက်လက်တိုးတက်လာသည့်အခါ၊ အသိုင်းအဝိုင်းနှင့် ဆက်သွယ်၊ ဆာဗာအသစ်များကို စူးစမ်း၊ နှင့် ကိုယ်ပိုင် ဖြေရှင်းချက်များ တည်ဆောက်ခြင်းက သင့်ဖွံ့ဖြိုးရေး ထိရ

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
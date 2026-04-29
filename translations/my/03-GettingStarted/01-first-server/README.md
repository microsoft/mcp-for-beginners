# MCP နှင့် အစပြုခြင်း

Model Context Protocol (MCP) နှင့် ပထမဆုံးခြေလှမ်းများသို့ ကြိုဆိုပါသည်။ သင်သည် MCP အသစ်ဖြစ်သည်ဟု သို့မဟုတ် MCP ကို နက်နဲစွာ နားလည်မှု တိုးချဲ့လိုသူဖြစ်ပါက ယခုအညွှန်းသည် စတင်တပ်ဆင်ခြင်းနှင့် ဖွံ့ဖြိုးရေးလုပ်ငန်းစဉ် အရေးပါသောဆင်ခြင်းကို လေ့လာရန် လမ်းညွှန်ပေးမည်ဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် အက်ပ်များကို ချိတ်ဆက်ပေးနိုင်စေရန် ဘယ်လိုပွင့်လင်းစေရန်နှင့် MCP ဖြင့် ထောက်ပံ့ထားသော ဖြေရှင်းနည်းများကို ဖန်တီး၍ စမ်းသပ်ရန် သင့် ပတ်ဝန်းကျင်ကို ဘယ်လိုအမြန် ပြင်ဆင်ရမည်ကို သင်တွေ့မြင်မည်ဖြစ်သည်။

> TLDR; သင်သည် AI အက်ပ်များ တည်ဆောက်ပါက၊ သင်သည် LLM (စာကြီးမော်ဒယ်) ကို ပိုမိုအသိပညာရှိစေရန် ကိရိယာများနှင့် အခြားအရင်းအမြစ်များကို ထည့်သွင်းနိုင်သည်။ သို့သော် အကယ်၍ သင့်ကိရိယာများနှင့် အရင်းအမြစ်များကို ဆာဗာပေါ်တွင် ထားရှိပါက အက်ပ်နှင့် ဆာဗာရဲ့ စွမ်းဆောင်ရည်များကို LLM ပါသည့် သို့မဟုတ် မပါသည့် client မည်သည့်သူမဆို အသုံးပြုနိုင်ပါသည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာသည် MCP ပတ်ဝန်းကျင်များကို တပ်ဆင်ခြင်းနှင့် ပထမ MCP အက်ပ်များ ဖန်တီးခြင်းအပေါ် တတ်ကျွမ်းတဲ့ လမ်းညွှန်ချက်များ ပေးသည်။ လိုအပ်သော ကိရိယာများနှင့် ပုံစံများကို တပ်ဆင်ခြင်း၊ အခြေခံ MCP ဆာဗာများ ဖန်တီးခြင်း၊ ဟော့စ် အက်ပ်များ ဖန်တီးခြင်းနှင့် သင်၏ဆောင်ရွက်ချက်များကို စမ်းသပ်နိုင်ခြင်းကဲ့သို့ များကို သင်လေ့လာနိုင်မည်ဖြစ်သည်။

Model Context Protocol (MCP) သည် အက်ပ်များ LLM များသို့ စံမီနည်းလမ်းဖြင့် နောက်ခံ အချက်အလက်ပေးပို့မှု ပံ့ပိုးပေးသည့် ဖွင့်လှစ်ထားသော နည်းမူဖြစ်သည်။ MCP ကို AI အက်ပ်များအတွက် USB-C ဆိပ်ကမ်းတစ်ခုအဖြစ် သုံးနိုင်သည် - AI မော်ဒယ်များကို အချက်အလက်ရင်းမြစ်များနှင့် ကိရိယာမျိုးစုံနှင့် ချိတ်ဆက်ရာတွင် စံသတ်မှတ်နည်းလမ်းဖြစ်သည်။

## သင်ယူရမည့် အလားအလာများ

ဤသင်ခန်းစာအဆုံး၌ သင်သည်:

- C#, Java, Python, TypeScript နှင့် Rust များအတွက် MCP ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်များ တပ်ဆင်နည်း
- ပုံမှန် အသုံးပြုနိုင်သော function (အရင်းအမြစ်များ၊ prompt များနှင့် ကိရိယာများပါ၀င်သော) MCP ဆာဗာများ ဖန်တီး၍ ပြန်လည်အသုံးပြုခြင်း
- MCP ဆာဗာများနှင့် ချိတ်ဆက်သည့် ဟော့စ် အက်ပ်များ တည်ဆောက်ခြင်း
- MCP ဆောင်ရွက်ချက်များကို စမ်းသပ်ခြင်းနှင့် မှားယွင်းချက်ရှာဖွေပြင်ဆင်ခြင်း

## သင့် MCP ပတ်ဝန်းကျင်ကို တပ်ဆင်ခြင်း

MCP နဲ့ အလုပ်လုပ်ဖို့ စတင်ရန်မတိုင်ခင် သင့် ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်ကို ပြင်ဆင်ထားရမည်နှင့် အခြေခံအလုပ်လုပ်ဆောင်ပုံကို နားလည်ရမည်ဖြစ်သည်။ ဤအပိုင်းမှာ MCP ဖြင့် စတင်လုပ်ဆောင်ရန် လိုအပ်သော အဆင့်များကို လမ်းညွှန်ပေးမည်ဖြစ်သည်။

### လိုအပ်ချက်များ

MCP ဖွံ့ဖြိုးမှုကို စတင်ရန် မတက်ရောက်မီ သင်တွင်ရှိပြီးဖြစ်ရမည့်အရာများမှာ -

- **ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်**: သင့်ရွေးချယ်ထားသည့် ဘာသာစကား (C#, Java, Python, TypeScript, သို့မဟုတ် Rust)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm သို့မဟုတ် ခေတ်မီကုဒ် အပြင်အဆင်တစ်ခု
- **ပက်ကေ့ချ် မန်နေဂျာများ**: NuGet, Maven/Gradle, pip, npm/yarn, သို့မဟုတ် Cargo
- **API Key များ**: သင့်ဟော့စ် အက်ပ်များတွင် အသုံးပြုမည့် AI ဝန်ဆောင်မှုများအတွက်

## အခြေခံ MCP ဆာဗာ ဖွဲ့စည်းပုံ

MCP ဆာဗာသည် အများအားဖြင့် ပါဝင်သော အချက်အလက်များမှာ -

- **ဆာဗာ ပြင်ဆင်မှု**: ဆိပ်ကမ်း, အတည်ပြုချက် နှင့် အခြား ဆက်တင်များ
- **အရင်းအမြစ်များ**: LLM များအတွက် ရရှိနိုင်သော ဒေတာနှင့် နောက်ခံ
- **ကိရိယာများ**: မော်ဒယ်များ အသုံးပြုနိုင်သော လုပ်ဆောင်ချက်များ
- **prompt များ**: စာသား ထုတ်လုပ်ခြင်း သို့မဟုတ် ဖွဲ့စည်းခြင်း အပိုင်း များအတွက် စံနမူနာများ

TypeScript တွင် ပုံပြင် ရိုးရှင်းမှုအတိုင်း -

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP စာကြည့်တိုက်တစ်ခုဖန်တီးပါ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ဖြည့်စွက်ကိရိယာတစ်ခုထည့်ပါ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// သွေးလွတ်တွေ့ကြုံမှုအရင်းအမြစ်တစ်ခုထည့်ပါ
server.resource(
  "file",
  // 'list' parameter သည် အရင်းအမြစ်သည် ရနိုင်သောဖိုင်များကို မည်သို့ရိုက်ချက်ပြုလုပ်သည်ကို ထိန်းချုပ်သည်။ ၎င်းကို undefined သို့ထားသည်မှာ ဤအရင်းအမြစ်အတွက် ရိုက်ချက်ပြုလုပ်ခြင်းကို ပိတ်ဆို့သည်။
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ဖိုင်အတွင်းပါတ်များကို ဖတ်ရှုသောဖိုင်အရင်းအမြစ်တစ်ခုထည့်ပါ
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

server.prompt(
  "review-code",
  { code: z.string() },
  ({ code }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Please review this code:\n\n${code}`
      }
    }]
  })
);

// stdin မှ စာတိုက်ရယူခြင်းနှင့် stdout သို့ စာတိုက်ပို့ခြင်း ပြုလုပ်မှုကို စတင်ပါ
const transport = new StdioServerTransport();
await server.connect(transport);
```

ကုဒ်တွင်-

- MCP TypeScript SDK မှ လိုအပ်သော class များကို import ပြုလုပ်သည်။
- MCP ဆာဗာ instance အသစ်တစ်ခု ဖန်တီးထားပြီး စီမံခန့်ခွဲသည်။
- handler function ပါသော  `calculator` ဆိုသော custom tool တစ်ခု ပေါင်းထည့်သည်။
- MCP တောင်းဆိုမှုများ ခံယူရန် ဆာဗာကို စတင်ချထားသည်။

## စမ်းသပ်ခြင်းနှင့် မှားယွင်းချက်ရှာဖွေခြင်း

MCP ဆာဗာကို စတင် စမ်းသပ်မတိုင်မီ၊ ရရှိနိုင်သော ကိရိယာများနှင့် မှားယွင်းချက်ရှာဖွေရာတွင် အကောင်းဆုံးလမ်းညွှန်ချက်များကို နားလည်ထားသင့်သည်။ ထိရောက်သော စမ်းသပ်ခြင်းသည် ဆာဗာသည် မျှော်မှန်းထားသလို လုပ်ဆောင်သည်ဟု သေချာစေရန်နှင့် ပြသနာများကို လျင်မြန်စွာ ရှာဖွေနိုင်ခြင်းကိုကူညီပေးသည်။ နောက်ပိုင်းတွင် MCP အကောင်အထည်ဖော်ခြင်းကို စစ်ဆေးရန် သတ်မှတ်ထားသော နည်းလမ်းများကို ဖေါ်ပြထားသည်။

MCP သည် သင့်ဆာဗာများကို စမ်းသပ်ဖို့နှင့် မှားယွင်းချက်ရှာဖွေဖို့ ကူညီပေးမယ့် ကိရိယာများကို ပေးသည် -

- **Inspector tool**၊ ဤကိရိယာသည် သင့်ဆာဗာနှင့် ချိတ်ဆက်၍ ကိရိယာများ၊ prompt များနှင့် အရင်းအမြစ်များ စမ်းသပ်နိုင်သော graphical interface อะသည်။
- **curl**, သင့်ဆာဗာနှင့် HTTP command များ ဖန်တီး၍ run လုပ်နိုင်သည့် command line tool တစ်ခုဖြစ်သည်။

### MCP Inspector အသုံးပြုခြင်း

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) သည် မျက်မြင်စမ်းသပ်တဲ့ ကိရိယာတစ်ခုဖြစ်ပြီး သင့်အား -

1. **ဆာဗာ စွမ်းရည်များ ရှာဖွေခြင်း**: ရရှိနိုင်သော အရင်းအမြစ်များ၊ ကိရိယာများနှင့် prompt များကို အလိုအလျောက် ရှာဖွေပါ
2. **ကိရိယာ လုပ်ဆောင်ချက် စမ်းသပ်ခြင်း**: အမျိုးမျိုးသော ပါရာမီတာများကို ထည့်သွင်းပြီး တုံ့ပြန်ချက်များကို real-time ကြည့်ရှုပါ
3. **ဆာဗာ Metadata ကြည့်ရှုခြင်း**: ဆာဗာကိုယ်ရေးကိုယ်တာ၊ schema များနှင့် configuration များ စစ်ဆေးနိုင်သည်

```bash
# ဥပမာ TypeScript, MCP Inspector ကို 설치하고 실행하기 위한 방법
npx @modelcontextprotocol/inspector node build/index.js
```

အထက်ပါ command များကို ပြေးဆွဲလျှင် MCP Inspector သည် သင့် browser တွင် local web interface တစ်ခုကို ဖွင့်လှစ်လိုက်မည်။ စာရင်းပြဘုတ်တွင် သင့်မှတ်ပုံတင်ထားသော MCP ဆာဗာများ၊ မရရှိနိုင်သော ကိရိယာများ၊ အရင်းအမြစ်များနှင့် prompt များ ပြသလိမ့်မည်။ interface က ကိရိယာ လုပ်ဆောင်ချက်များ စမ်းသပ်ရန်၊ ဆာဗာ metadata ကို စစ်ဆေးရန်နှင့် real-time တုံ့ပြန်ချက်များကို ကြည့်ရှုရန် အဆင်ပြေစေသော ပတ်ဝန်းကျင်ဖြစ်ပြီး MCP ဆာဗာ ဖွဲ့စည်းမှုများကို မှန်ကန်စွာ စစ်ဆေးပြင်ဆင်နိုင်စေသည်။

ဤသည်မှာ မြင်ကွင်းပုံတစ်ခုဖြစ်သည် -

![MCP Inspector server connection](../../../../translated_images/my/connected.73d1e042c24075d3.webp)

## အဖြစ်များ တွေ့ရသော စုစုပေါင်း ပြဿနာများနှင့် ဖြေရှင်းနည်းများ

| ပြဿနာ | ကြိုးစားဖြေရှင်းနိုင်သော နည်းလမ်း |
|-------|-------------------|
| ချိတ်ဆက်မှု ငြင်းလိုက်ခြင်း | ဆာဗာလုပ်နေစဥ်ဖြစ်ပြီး ဆိပ်ကမ်းမှန်ကြောင်းစစ်ဆေးပါ |
| ကိရိယာလုပ်ဆောင်မှု အမှား | ပါရာမီတာ စစ်ဆေးမှုနှင့် အမှားကိုင်တွယ်မှု ပြန်လည်သုံးသပ်ပါ |
| အတည်ပြုမှု မအောင်မြင်ခြင်း | API key များနှင့် ခွင့်ပြုချက်များကို စစ်ဆေးပါ |
| Schema စစ်ဆေးမှု အမှား | ပါရာမီတာများသည် သတ်မှတ်ထားသော schema နှင့် ကိုက်ညီမှသာရှိရမည် |
| ဆာဗာ မစတင်နိုင်ခြင်း | ဆိပ်ကမ်း အငြင်းပွားမှုများ သို့မဟုတ် သက်ဆိုင်ရာ လိုအပ်ချက်များ ပျောက်ကွယ်မှုရှိမရှိ စစ်ဆေးပါ |
| CORS အမှားများ | cross-origin တောင်းဆိုမှုများအတွက် CORS header များကို သင့်တော်စွာ ပြင်ဆင်ပါ |
| အတည်ပြုမှု ပတ်သက်ရာ ပြဿနာများ | token အတည်ပြုပြဿနာများနှင့် ခွင့်ပြုချက်များကို စစ်ဆေးပါ |

## ဒေသခံ ဖွံ့ဖြိုးရေး

ဒေသခံ ဖွံ့ဖြိုးရေးနှင့် စမ်းသပ်ရန်အတွက် MCP ဆာဗာများကို သင်၏စက်ပေါ်တွင် တိုက်ရိုက် run နိုင်သည် -

1. **ဆာဗာ လုပ်ငန်းစဉ် စတင်ပါ**: သင့် MCP ဆာဗာ အက်ပ်ကို run လုပ်ပါ
2. **ကွန်ရက် ပြင်ဆင်မှု**: ဆာဗာ၏ ရည်ရွယ်ထားသော ဆိပ်ကမ်းတွင် ဝင်ရောက်နိုင်ရေး စစ်ဆေးပါ
3. **client များ ချိတ်ဆက်ပါ**: `http://localhost:3000` ကဲ့သို့ ဒေသခံ URL များ အသုံးပြုပါ

```bash
# ဥပမာ: TypeScript MCP ဆာဗာကို ဒေသခံ에서 chạyခြင်း
npm run start
# ဆာဗာ http://localhost:3000 တွင် chạyနေသည်
```

## ပထမ MCP ဆာဗာ ဖန်တီးခြင်း

သင်ပြီးခဲ့သော [Core concepts](../../01-CoreConcepts/README.md) သင်ခန်းစာကို ပြီးမြောက်ပြီးဖြစ်ပါသည်။ အခု သင်၏ အသိပညာကို လက်တွေ့ အသုံးချမည့် အချိန်ပါ။

### ဆာဗာမှာ ဘာတွေ ပါနိုင်သလဲ

ကုဒ်ရေးမထွက်မီ ဆာဗာရဲ့ အလုပ်များကို သတိရကြရအောင် -

MCP ဆာဗာသည် -

- ဒေသခံ ဖိုင်နှင့် ဒေတာဘေ့စ်များ အသုံးချနိုင်သည်
- ဝေးလံ API များနှင့် ချိတ်ဆက်နိုင်သည်
- တွက်ချက်မှုများ လုပ်ဆောင်နိုင်သည်
- အခြားကိရိယာများနှင့် ဝန်ဆောင်မှုများ ပေါင်းစည်းနိုင်သည်
- အသုံးပြုသူအပြန်အလှန် ဆက်ဆံမှုအတွက် UI ပံ့ပိုးပေးနိုင်သည်

အံ့သြစရာကောင်းပါတယ်၊ ယခု အလုပ်ဘာတွေ လုပ်နိုင်တယ်ဆိုတာ သိသွားပြီ၊ လက်စတင် ပြုလုပ်ကြမယ်။

## လေ့ကျင့်ခန်း: ဆာဗာ ဖန်တီးခြင်း

ဆာဗာ ဖန်တီးရန် လိုအပ်သည့် အဆင့်များမှာ -

- MCP SDK ကို 설치 ပြုလုပ်ပါ။
- project တစ်ခု ဖန်တီးပြီး project ဖွဲ့စည်းမှုကို သတ်မှတ်ပါ။
- ဆာဗာ ကုဒ် ရေးပါ။
- ဆာဗာကို စမ်းသပ်ပါ။

### -1- Project ဖန်တီးခြင်း

#### TypeScript

```sh
# ပရောဂျက် ဖိုလ်ဒါ ဖန်တီးပြီး npm ပရောဂျက်ကို စတင်တည်ထောင်ပါ
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# ပရောဂျက် ဖိုင်တွဲ ဖန်တီးပါ
mkdir calculator-server
cd calculator-server
# Visual Studio Code မှာ ဖိုင်တွဲကို ဖွင့်ပါ - အခြား IDE အသုံးပြုနေပါက ကျော်သွားနိုင်ပါသည်
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java အတွက် Spring Boot project တစ်ခု ဖန်တီးပါ -

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

Zip ဖိုင်ကို ဖြုတ်ပါ -

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# စမ်းသပ်မှုမသုံးသော အပိုင်းကို လိုအပ်သလို ဖယ်ရှားနိုင်သည်
rm -rf src/test/java
```

*pom.xml* ဖိုင်တွင် အောက်ပါ စီမံခန့်ခွဲမှု ပြည့်စုံကို ထည့်ပါ -

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- လိုအပ်သော Dependencies ထည့်ရန်

Project ဖန်တီးပြီးနောက် Dependencies များ ထည့်ပါ -

#### TypeScript

```sh
# မတင်ထားသေးလျှင် TypeScript ကို ကမ္ဘောလုံးအရ 설치လုပ်ပါ
npm install typescript -g

# MCP SDK နှင့် Zod ကို schema အတည်ပြုမှုအတွက် 설치လုပ်ပါ
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# တႆးပြဲတစ္ခုဖန္တီးၿပီး အခ်က္အလက္မ်ားကိုထည့္သြင္းပါ
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- Project ဖိုင်များ ဖန်တီးခြင်း

#### TypeScript

*package.json* ဖိုင်ကို ဖွင့်၍ ဆာဗာကို ပြုလုပ်နှင့် ပြေးရအောင် အောက်ပါအတိုင်း ဖြည့်ပါ -

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

*tsconfig.json* ဖိုင်ကို ဖန်တီးပါ -

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

ကုတ်ကို သိမ်းဆည်းရန် ဖိုလ်ဒါတစ်ခု ဖန်တီးပါ -

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* ဖိုင် ဖန်တီးပါ -

```sh
touch server.py
```

#### .NET

လိုအပ်သော NuGet package များ 설치 ပြုလုပ်ပါ -

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot project များတွင် ဒီတည်းဆို project ဖွဲ့စည်းပုံကို အလိုအလျောက် ဖန်တီးမည်ဖြစ်သည်။

#### Rust

Rust တွင် `cargo init` အတည်ပြုပြီးနောက် *src/main.rs* ဖိုင်ကို ဖန်တီးပြီးဖြစ်သည်။ ဖိုင်ကို ဖွင့်၍ အဆိုပါ မူလကုဒ်ကို ဖျက်ပစ်ပါ။

### -4- ဆာဗာ ကုဒ် ရေးသားခြင်း

#### TypeScript

*index.ts* ဖိုင်ကို ဖန်တီးပြီး အောက်ပါ ကုဒ်များ ထည့်ပါ -

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// MCP ဆာဗာတစ်ခု ဖန်တီးပါ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ယခု သင့်ဆာဗာရှိပါသော်လည်း အများကြီးမလုပ်ဆိုတော့ ပြန်လည်ပြင်ဆင်ကြရအောင်။

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP ဆာဗာတစ်ခု ဖန်တီးပါ။
mcp = FastMCP("Demo")
```

#### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

// add features
```

#### Java

Java အတွက် ဆာဗာ အဓိက အစိတ်အပိုင်းများကို ဖန်တီးပါ။ ပထမဦးဆုံး main application class ကို ပြင်ဆင်ပါ -

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

calculator service ကို ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**ထုတ်လုပ်ငန်းအဆင့် အဆင့်မြင့် ဝန်ဆောင်မှုများအတွက် စိတ်ကြိုက် ပါဝင်ပစ္စည်းများ:**

startup configuration ဖိုင် ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

health controller ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

exception handler ဖန်တီးပါ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // နောက်ယူသူများ
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

custom banner ဖန်တီးပါ *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

*src/main.rs* ဖိုင်၏ အထက်တွင် အောက်ပါကုဒ်များ ထည့်ပါ။ MCP ဆာဗာအတွက် လိုအပ်သော 라이브러리များနှင့် module များကို import ပြုလုပ်သည်။

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

calculator ဆာဗာသည် နံပါတ်နှစ်ခုကို ပေါင်းခြင်း လုပ်ဆောင်နိုင်သော ရိုးရှင်းသော ဆာဗာတစ်ခု ဖြစ်မည်။ calculator request ကို ကိုယ်စားပြု struct တစ်ခု ဖန်တီးပါ။

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

calculator ဆာဗာ ကိုယ်စားပြု struct တစ်ခု ဖန်တီးပါ။ ဤ struct မှာ ကိရိယာ router ကို ထားရှိပြီး ကိရိယာများ မှတ်ပုံတင်ရန် အသုံးပြုသည်။

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ယခု `Calculator` struct ကို အသစ်ဖန်တီးပြီး ဆာဗာ handler ကို အကောင်အထည်ဖော်ရန် ဆောင်ရွက်ပါ။

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

နောက်ဆုံးသတ်မှတ်ချက်အနေဖြင့် ဆာဗာကို စတင်ရန် main function ကို အကောင်အထည်ဖော်ပါ။ ဤ function သည် `Calculator` struct instance တစ်ခုဖန်တီးပြီး standard input/output မှတစ်ဆင့် ဆာဗာကြေးညှိဖြည့်မည်ဖြစ်သည်။

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

ဆာဗာသည် မိမိကိုယ်ပိုင် အခြေခံသတင်းအချက်အလက်များ ပံ့ပိုးဖြန့်ဝေထုတ်လွှင့်နိုင် ပြီဖြစ်သည်။ နောက်တစ်ဆင့်မှာ ပေါင်းလဒ်ခြင်း လုပ်ဆောင်သော tool တစ်ခု ထည့်သွင်းမည်ဖြစ်သည်။

### -5- ကိရိယာ နှင့် အရင်းအမြစ် ထည့်သွင်းခြင်း

အောက်ပါကုဒ်များ ထည့်သွင်း၍ ကိရိယာနှင့် အရင်းအမြစ် များ ထည့်ပါ -

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);
```

သင်၏ ကိရိယာသည် `a` နှင့် `b` ပါရာမီတာများကို လက်ခံပြီး ဖြေဆိုချက်ကို အောက်ပါပုံစံအတိုင်း ထုတ်ပေးသည် -

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

သင်၏ အရင်းအမြစ် ("greeting") သည် `name` ပါရာမီတာ တစ်ခုကို လက်ခံပြီး ကိရိယာနှင့် ဆင်တူသော ဖြေဆိုချက်ကို ထုတ်ပေးသည် -

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ပေါင်းခြင်းကိရိယာတစ်ခု ထည့်ပါ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ဇိမ်ခံသော မင်္ဂလာဆောင်မှု အရင်းအမြစ် တစ်ခု ထည့်ပါ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

အထက်ဖော်ပြပါ ကုဒ်တွင် -

- `add` ဆိုသော ကိရိယာကို ဖြေရှင်းချက်များ `a` နှင့် `b` (လုံးပေါင်း) သတ်မှတ်ထားသည်။
- `greeting` ဆိုသော အရင်းအမြစ်ကို `name` ပါရာမီတာအား ဖြင့် ဖန်တီးထားသည်။

#### .NET

Program.cs ဖိုင်တွင် အောက်ပါကို ထည့်ပါ -

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ကိရိယာအပိုင်းများကို ယခင် အဆင့်တွင် ပြီးခဲဖြစ်ပါသည်။

#### Rust

`impl Calculator` block အတွင်း သစ်သော ကိရိယာ သွင်းထည့်ပါ -

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- နောက်ဆုံးကုဒ်

ဆာဗာ စတင်ရန် လိုအပ်သည်များကို ပြည့်စုံစွာ ထည့်သွင်းပါ -

#### TypeScript

```typescript
// stdin တွင် မက်ဆေ့ခ််များလက်ခံခြင်းနှင့် stdout မှ မက်ဆေ့ချ်များပို့ခြင်း စတင်မည်။
const transport = new StdioServerTransport();
await server.connect(transport);
```

ပြီးပြည့်စုံသော ကုဒ် -

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP ဆာဗာတစ်ခုဖန်တီးပါ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ပေါင်းထည့်ရန်ကိရိယာတစ်ခုထည့်ပါ
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ဇာတ်ကောင်မြောက်သောကြိုဆိုမှုအရင်းအမြစ်တစ်ခုထည့်ပါ
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// stdin တွင်မက်ဆေ့ချ်များလက်ခံခြင်းနှင့် stdout တွင်မက်ဆေ့ချ်များပို့ခြင်းစတင်ပါ
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP ဆာဗာတစ်ခု ဖန်တီးပါ
mcp = FastMCP("Demo")


# ပေါင်းခြင်းကိရိယာတစ်ခု ထည့်ပါ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# လှုပ်ရှားနိုင်သော သတင်းစကားအစွမ်းသတ္တိ resource ထည့်ပါ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# အဓိက အကောင်အထည်ဖော်အပိုင်း - ဆာဗာကို မြှင့်တင်ရန် အဓိက လိုအပ်သည်
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs ဖိုင်ကို အောက်ပါအတိုင်း ဖန်တီးပါ -

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

အပြည့်အစုံ main application class အဖြစ် ပါဝင်သည် -

```java
// McpServerApplication.java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

#### Rust

Rust ဆာဗာ အပြီးသတ် ကုဒ်မှာ အောက်ပါလို ဖြစ်သည် -

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- ဆာဗာ စမ်းသပ်ခြင်း

အောက်ပါ command များ ဖြင့် ဆာဗာ စတင်ပါ -

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector ကို အသုံးပြုရန် `mcp dev server.py` ကို အသုံးပြုပါ။ ၎င်းသည် Inspector ကို အလိုအလျောက် စတင်ဖြင့် လိုအပ်သော proxy session token ကို ပံ့ပိုးပေးသည်။ `mcp run server.py` အသုံးပြုပါက မန်နျွက်စတင်ရန်နှင့် ချိတ်ဆက်မှု ညှိရန် လိုအပ်သည့် အလှည့်အပြောင်းများကို ကိုယ်တိုင် စီမံရမည်ဖြစ်သည်။

#### .NET

Project directory ထဲတွင် ရှိမှု သေချာပါစေ -

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

ဖော်ပြပါ command များ ဖြင့် code formatting ပြုလုပ်ပြီး ဆာဗာကို လည်ပတ်ပါ -

```sh
cargo fmt
cargo run
```

### -8- Inspector ဖြင့် run ချခြင်း

Inspector သည် သင့်ဆာဗာကို စတင်ပေးပြီး ၎င်းနှင့် စကားစမြည်ရန် နှင့် စမ်းသပ်ရန် ခွင့်ပြုသော ကောင်းမွန်သော ကိရိယာဖြစ်သည်။ စတင်ကြရအောင် -

> [!NOTE]
> "command" field အတွင်းမှာ သတ်မှတ်ထားသည့် runtime အတွက် အဆင်ပြေနေအသဖြင့် မတူညီမှု ရှိနိုင်သည်။

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

သို့မဟုတ် *package.json* တွင် `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ထည့်ပြီး `npm run inspector` ကို run လုပ်ပါ။

#### Python

Python သည် Node.js tool များဖြစ်သည့် inspector ကို wrap လုပ်ထားသည်။ အောက်ပါပုံစံဖြင့် ဖုန်းခေါ်နိုင်ပါသည် -

```sh
mcp dev server.py
```

သို့သော် ကိရိယာတွင်ရရှိနိုင်သည့် method များအားလုံး မလက်ခံသေးပါ၊ ထို့ကြောင့် Node.js tool ကို တိုက်ရိုက် အသုံးပြုရန် အကြံပြုသည် -

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

script များ run အတွက် commands နှင့် arguments များကို ပြင်ဆင်နိုင်သော tool သို့ IDE အသုံးပြုပါက ...
`Command` ကွက်တွင် `python` ကို သတ်မှတ်ပါ၊ `Arguments` အနေနှင့် `server.py` ကို သတ်မှတ်ပေးပါ။ ဒါက စာမျက်နှာကို မှန်ကန်စွာ အလုပ်လုပ်စေပါလိမ့်မယ်။

#### .NET

သင့် project directory ထဲမှာ ရှိနေသည်ကို သေချာစေပါ။

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

သင့် calculator server က အလုပ်လုပ်နေကြောင်း သေချာစေပါ။
ထို့နောက် inspector ကို chạy လိုက်ပါ။

```cmd
npx @modelcontextprotocol/inspector
```

inspector web interface တွင် -

1. "SSE" ကို သယ်ယူ ပို့ဆောင်မှုအမျိုးအစားအဖြစ် ရွေးပါ။
2. URL ကို `http://localhost:8080/sse` အဖြစ် သတ်မှတ်ပါ။
3. "Connect" ကို နှိပ်ပါ။

![Connect](../../../../translated_images/my/tool.163d33e3ee307e20.webp)

**သင်ဟာ server နဲ့ ချိတ်ဆက်သွားပြီ ဖြစ်ပါတယ်။**
**Java server စမ်းသပ်မှု အပိုင်း ပြီးမြောက်သွားပြီ ဖြစ်ပါတယ်။**

နောက်ထပ် အပိုင်းကတော့ server နဲ့ ဆက်သွယ်မှုပါ။

သင်မှာ အောက်ပါ user interface ကို တွေ့ရမယ်။

![Connect](../../../../translated_images/my/connect.141db0b2bd05f096.webp)

1. Connect ခလုတ်ကို အသုံးပြု၍ server နှင့် ချိတ်ဆက်ပါ။
  ချိတ်ဆက်ပြီးနောက် အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်-

  ![Connected](../../../../translated_images/my/connected.73d1e042c24075d3.webp)

1. "Tools" နှင့် "listTools" ကို ရွေးချယ်ပါ၊ "Add" ပြသလာပါမယ်၊ "Add" ကို နှိပ်ပြီး parameter တန်ဖိုးများ ဖြည့်ပါ။

  အောက်ပါ တုံ့ပြန်ချက်ကို ကြည့်ရမှာဖြစ်ပြီး၊ "add" tool မှရလာတဲ့ အဖြေတစ်ခု ဖြစ်ပါသည်။

  ![Result of running add](../../../../translated_images/my/ran-tool.a5a6ee878c1369ec.webp)

ဆုတောင်းပါတယ်၊ သင်ဟာ သင့် ပထမဆုံး server ကို တည်ဆောက်ပြီး အလုပ်လုပ်နိုင်ခဲ့ပါပြီ။

#### Rust

Rust server ကို MCP Inspector CLI ဖြင့် run မည်ဆိုပါက အောက်ပါ command ကို အသုံးပြုနိုင်ပါသည်-

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### အတည်တကျ SDK များ

MCP သည် ဘာသာစကားပိုင်းဆိုင်ရာ SDK များကို တရားဝင်ပံ့ပိုးပေးသည်-

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - တရားဝင် TypeScript အကောင်အထည်ဖော်ချက်
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - တရားဝင် Python အကောင်အထည်ဖော်ချက်
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - တရားဝင် Kotlin အကောင်အထည်ဖော်ချက်
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - တရားဝင် Rust အကောင်အထည်ဖော်ချက်

## အဓိကယူဆချက်များ

- MCP ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်တည်ဆောက်ခြင်းသည် ဘာသာစကားအလိုက် SDK များဖြင့် ရိုးရာအတိုင်း ရိုးရှင်းသည်။
- MCP server များ တည်ဆောက်ခြင်းသည် ရိုးရှင်းသေချာသော schemas ဖြင့် tools များဖန်တီး၊ မှတ်ပုံတင်ခြင်း ဖြစ်သည်။
- စစ်တမ်းယူခြင်းနှင့် debugging များသည် MCP အကောင်အထည်ဖော်မှုများမှာ ယုံကြည်စိတ်ချရစေရန် အရေးကြီးသည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## တာဝန်အပ်

သင်နှစ်သက်ရာ tool ဖြင့် ရိုးရှင်းသော MCP server တည်ဆောက်ပါ-

1. သင်နှစ်သက်သော ဘာသာစကား (.NET, Java, Python, TypeScript, Rust) ဖြင့် tool ကို အကောင်အထည်ဖော်ပါ။
2. input parameters နှင့် return values ကို သတ်မှတ်ပါ။
3. server အလုပ်လုပ်မှုအတည်ပြုရန် inspector tool ကို run ပြီး စစ်ဆေးပါ။
4. ကွဲပြားသော inputs များဖြင့် အကောင်အထည်ဖော်မှုကို စမ်းသပ်ပါ။

## ဖြေရှင်းချက်

[Solution](./solution/README.md)

## အပိုဆောင်း ရင်းမြစ်များ

- [Azure တွင် Model Context Protocol အသုံးပြု၍ Agents ဆောက်ခြင်း](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps တွင် Remote MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## နောက်တစ်ဆင့်

နောက်တစ်ဆင့်- [MCP Clients ဖြင့် စတင်အသုံးပြုခြင်း](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဆက်သွယ်ချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန်တပ်ဆင်မှု ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့မှာ မှန်ကန်မှုအတွက် ကြိုးပမ်းသည်မူဖြစ်သော်လည်း အလိုအလျောက် ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းစာတမ်းသည် ၎င်း၏ သဘာဝဘာသာစကားဖြင့် တရားဝင်အကြောင်းအရာအနေဖြင့် ထည့်သွင်းစဉ်းစားရပါမည်။ အရေးကြီးသော အချက်အလက်များအတွက် အသက်မွေးဝမ်းကြောင်း လူကြီးမင်းအပြည့်အစုံဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော မည်သည့်နားမလည်မှုများ သို့မဟုတ် မှားယွင်းစဉ်းစားမှုများအတွက် ကျွန်တော်တို့ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
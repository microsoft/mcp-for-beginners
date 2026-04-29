# MCP തുടക്കം കുറിക്കുക

Model Context Protocol (MCP) ഇല്‍ നിങ്ങളുടെ ആദ്യ പടികൾക്ക് സ്വാഗതം! നിങ്ങൾ MCP новичков അല്ലെങ്കിൽ നിങ്ങളുടെ മനസിലാക്കലിനെ കൂടുതലാക്കാൻ നോക്കുന്നു എങ്കിൽ, ഈ ഗൈഡ് പരിപൂര്‍ണമായ സജ്ജീകരണവും വികസന പ്രക്രിയയും വഴി നിങ്ങളെ നയിക്കും. MCP എങ്ങനെ എഐ മോഡലുകളുടെയും ആപ്ലിക്കേഷനുകളുടെയും ഇടയിൽ സാര്വത്രികമായ സംയോജനത്തിനും സഹായിക്കുന്നു എന്ന് കണ്ടെത്തുകയും MCP-പോവർ ചെയ്ത പരിഹാരങ്ങൾ നിർമ്മിക്കുന്നതിനും പരിശോധിക്കുന്നതിനും നിങ്ങളുടെ പരിസരത്തെ എളുപ്പത്തിൽ സജ്ജമാക്കണമെന്ന് പഠിക്കുകയും ചെയ്യും.

> TLDR; നിങ്ങൾ എഐ ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുന്നുവെങ്കിൽ, നിങ്ങളുടെ LLM (വലുത് ഭാഷ മോഡൽ) കൂടുതൽ അറിവുള്ളതാക്കുവാൻ ടൂളുകളും മറ്റ് വിഭവങ്ങളും ചേർക്കാൻ കഴിയും എന്നാണ് നിങ്ങൾ അറിയുന്നത്. എങ്കിലും ആ ടൂളുകളും വിഭവങ്ങളും ഒരു സർവറിൽ സ്ഥാപിച്ചാൽ, ആപ്പും സർവർ ശേഷികളും ഒരു LLM ഉള്ളതുമായ അല്ലാത്ത കസ്റ്റമറുടെയും ഉപയോഗിക്കാം.

## പരിചയം

ഈ പാഠം MCP പരിസരങ്ങൾ സജ്ജമാക്കുകയും നിങ്ങളുടെ ആദ്യ MCP ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കുകയും ചെയ്യുന്നതിൽ പ്രായോഗിക മാർഗ്ഗനിർദ്ദേശങ്ങൾ നൽകുന്നു. ആവശ്യമായ ടൂളുകളും ഫ്രെയിമ്വർക്കുകളും സജ്ജീകരിക്കുന്നത്, അടിസ്ഥാന MCP സർവറുകൾ പണിയുന്നത്, ഹോസ്റ്റ് ആപ്ലിക്കേഷനുകൾ സൃഷ്‌ടിക്കുന്നത്, നിങ്ങളുടെ നടപ്പാക്കലുകൾ പരിശോധിക്കുന്നതും അറിയാം.

Model Context Protocol (MCP) ആപ്ലിക്കേഷനുകൾ LLMകൾക്ക് ബന്ധപ്പിടിക്കുന്ന സന്ദർഭം നൽകുന്ന രീതിയാണ് ഏകരാഷ്ട്രികമാക്കുന്നത്. MCP-നെ USB-C പോർട്ടിന്റെ പകരക്കാരൻ എന്നു കരുതുക - ഇത് എഐ മോഡലുകളെ വിവിധ ഡാറ്റ സ്രോതസുകളുമായും ഉപകരണങ്ങളുമായും ബന്ധിപ്പിക്കാൻ ഒരു ഏകീകൃത മാർഗ്ഗം നൽകുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം കഴിഞ്ഞാൽ, നിങ്ങൾക്ക് കഴിയുക:

- C#, Java, Python, TypeScript, Rust എന്നിവയിൽ MCP-യുടെ വികസന പരിസരങ്ങൾ സജ്ജമാക്കാൻ
- കസ്റ്റം സവിശേഷതകളുമായി അടിസ്ഥാന MCP സർവർ നിർമ്മിക്കുകയും വിന്യാസവും ചെയ്യുകയും ചെയ്യാൻ (വളവുകളും, പ്രോംപ്റ്റുകളും, ടൂളുകളും)
- MCP സർവറുകളുമായി ബന്ധപ്പെടുന്ന ഹോസ്റ്റ് ആപ്ലിക്കേഷനുകൾ സൃഷ്‌ടിക്കാൻ
- MCP നടപ്പാക്കലുകൾ പരിശേധിക്കുകയും ഡീബഗ് ചെയ്യുകയും ചെയ്യാൻ

## നിങ്ങളുടെ MCP പരിസരം സജ്ജമാക്കൽ

MCP-വുമായ് ജോലി തുടങ്ങുന്നതിനു മുമ്പ്, നിങ്ങളുടെ വികസന പരിസരം തയ്യാറാക്കുകയും അടിസ്ഥാന പ്രവൃത്തി പ്രവാഹം മനസിലാക്കുകയും ചെയ്യുക അത്യാവശ്യം ആണ്. ഒരു മാർഗ്ഗനിർദ്ദേശം തയ്യാറാക്കിയിട്ടുണ്ട് MCP-യോടെയുള്ള സുഖകരമായ തുടക്കത്തിനായി.

### മുൻരാജം

MCP വികസനം തുടങ്ങുന്നതിനു മുൻപ്, ഉറപ്പ് വരുത്തുക നിങ്ങൾക്കുണ്ട്:

- **വികസന പരിസരം**: നിങ്ങൾ തെരഞ്ഞെടുക്കുന്ന ഭാഷയ്ക്കായി (C#, Java, Python, TypeScript, Rust)
- **IDE/എഡിറ്റർ**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, അല്ലെങ്കിൽ എല്ലാ ആധുനിക കോഡ് എഡിറ്ററുകളും
- **പാക്കേജ് മാനേജറുകൾ**: NuGet, Maven/Gradle, pip, npm/yarn, അല്ലെങ്കിൽ Cargo
- **API കീകൾ**: ഹോസ്റ്റ് ആപ്ലിക്കേഷനുകളിൽ ഉപയോഗിക്കുന്ന ഏത് എഐ സേവനങ്ങൾക്കായുള്ളവ

## അടിസ്ഥാന MCP സർവർ ഘടന

ഒരു MCP സർവർ സാധാരണയായി ഉൾകൊള്ളുന്നു:

- **സർവർ കോൺഫിഗറേഷൻ**: പോർട്ട് സജ്ജീകരണം, ഓഥന്റിക്കേഷൻ, മറ്റ് ക്രമീകരണങ്ങൾ
- **വളവുകൾ**: LLM-കൾക്ക് ലഭ്യമാകുന്ന ഡാറ്റയും സന്ദർഭവുമുള്ളതു
- **ടൂളുകൾ**: മോഡലുകൾ ആഹ്വാനം ചെയ്യുന്നതിന് ഫങ്ഷണലിറ്റി
- **പ്രോംപ്റ്റുകൾ**: വാചകങ്ങൾ ജനറേറ്റ് ചെയ്യുന്നതിനോ ഘടിപ്പിക്കുന്നതിനോ ടെംപ്ലേറ്റുകൾ

TypeScript-ൽ ലളിതീകരിച്ച ഒരു ഉദാഹരണം:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ഒരു MCP സർവർ സൃഷ്ടിക്കുക
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ഒരു കൂട്ടിച്ചേർക്കൽ ടൂൾ ചേർക്കുക
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ഒരു ഡൈനാമിക് ഗ്രീറ്റിംഗ് സ്രോതസ് ചേർക്കുക
server.resource(
  "file",
  // 'list' പാരാമീറ്റർ സ്രോതസ്സ് ലഭ്യമായ ഫയലുകൾ എങ്ങനെ ലിസ്റ്റ് ചെയ്യുമെന്ന് നിയന്ത്രിക്കുന്നു. അത് undefined ആയി സജ്ജമാക്കി ഈ സ്രോതസ്സിനുള്ള ലിസ്റ്റിംഗ് പ്രവർത്തനം നിശ്ചലമാക്കുന്നു.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ഫയൽ ഉള്ളടക്കം വായിക്കുന്ന ഫയൽ സ്രോതസ് ചേർക്കുക
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

// stdin-യിൽ സന്ദേശങ്ങൾ സ്വീകരിക്കുന്നത് ആരംഭിച്ച് stdout-ൽ സന്ദേശങ്ങൾ അയക്കുക
const transport = new StdioServerTransport();
await server.connect(transport);
```

മുമ്പത്തെ കോഡിൽ നാം:

- MCP TypeScript SDK-യിൽ നിന്നുള്ള ആവശ്യമായ ക്ലാസ്സുകൾ ഇറക്കുമതി ചെയ്തു.
- പുതിയ MCP സർവർ ഇൻസ്റ്റൻസിന്റെ സൃഷ്‌ടിയും ക്രമീകരണവും നടത്തി.
- ഒരു കസ്റ്റം ടൂൾ (`calculator`) ഹാൻഡ്‌ലർ ഫങ്ഷൻ സഹിതം രജിസ്റ്റർ ചെയ്തു.
- MCP അഭ്യർത്ഥനകൾ കേൾക്കാൻ സർവർ ആരംഭിച്ചു.

## പരിശോധനയും ഡീബഗിംഗും

നിങ്ങളുടെ MCP സർവർ പരിശോധന ആരംഭിക്കുന്നതിന് മുമ്പ്, ലഭ്യമായ ടൂളുകളും ഡീബഗിംഗിനുള്ള മികച്ച പ്രവർത്തനരീതികളും മനസിലാക്കുകയാണ് പ്രധാനമാണ്. ഫലപ്രദമായ പരിശോധന നിങ്ങളുടെ സർവർ പ്രതീക്ഷിച്ചതുപോലെ പ്രവർത്തിക്കുന്നതായി ഉറപ്പാക്കുകയും പ്രശ്നങ്ങൾ വേഗത്തിൽ കണ്ടെത്തുകയും പരിഹരിക്കുകയും ചെയ്യാൻ സഹായിക്കുകയും ചെയ്യും. താഴെ ഉള്ള വിഭാഗം നിങ്ങളുടെ MCP നടപ്പാക്കൽ പരിശോധിക്കുന്നതിനുള്ള ശുപാർശ ചെയ്യുന്ന സമീപനങ്ങൾ വിവരിക്കുന്നു.

MCP നിങ്ങളുടെ സർവറുകൾ പരീക്ഷിക്കാൻ സഹായിക്കുന്ന ടൂളുകൾ നൽകുന്നു:

- **Inspector ടൂൾ**: ഗ്രാഫിക്കൽ ഇന്റർഫേസ്, ഇത് സർവറുമായി ബന്ധപ്പെടാനും നിങ്ങളുടെ ടൂളുകൾ, പ്രോംപ്റ്റുകൾ, വിഭവങ്ങൾ (Resources) പരീക്ഷിക്കാനും സഹായിക്കുന്നു.
- **curl**: curl പോലുള്ള കമാൻഡ് ലൈനും മറ്റ് HTTP കമാൻഡുകൾ സൃഷ്‌ടിക്കാനും ഓപ്പറേറ്റ് ചെയ്യാനുമുള്ള ക്ലയന്റുകളും സർവറുമായി ബന്ധപ്പെടാൻ കഴിയും.

### MCP ഇൻസ്‌പെക്ടർ ഉപയോഗിച്ച്

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ഒരു ദൃശ്യപരമായ പരിശോധനാ ടൂൾ ആണ്, ഇത് നിങ്ങളെ സഹായിക്കുന്നു:

1. **സർവർ ശേഷികൾ കണ്ടെത്തുക**: ലഭ്യമായ വിഭവങ്ങൾ, ടൂളുകൾ, പ്രോംപ്റ്റുകൾ സ്വയം കണ്ടെത്തുക
2. **ടൂൾ പ്രവൃത്തി പരിശോധന**: വ്യത്യസ്ത പാരാമീറ്ററുകൾ പരീക്ഷിച്ച് കാര്യക്ഷമ പ്രതികരണങ്ങൾリアൽ-ടൈം കാണുക
3. **സർവർ മെറ്റാഡാറ്റ കാണുക**: സർവർ വിവരങ്ങൾ, സ്കീമകൾ, ക്രമീകരണങ്ങൾ പരിശോധിക്കുക

```bash
# ഉദാഹരണമായി TypeScript, MCP ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യാനും പ്രവർത്തിപ്പിക്കാനും
npx @modelcontextprotocol/inspector node build/index.js
```

മുകളിൽ നൽകിയ കമാൻഡുകൾ പ്രവർത്തിപ്പിക്കുന്നത് കൊണ്ട് MCP ഇൻസ്‌പെക്ടർ ബ്രൗസറിൽ ഒരു റവൻ വെബ് ഇന്റർഫേസ് ആരംഭിക്കും. രജിസ്റ്റർ ചെയ്ത MCP സർവറുകൾ, അവയുടെ ലഭ്യമായ ടൂളുകൾ, വിഭവങ്ങൾ, പ്രോംപ്റ്റുകൾ ഡാഷ്‌ബോർഡിൽ കാണാമാകും. വിശകലനപരവും സംവേദനപരവുമായ ടൂൾ പ്രവർത്തന പരിശോധന, സർവർ മെറ്റാഡാറ്റ ഇൻസ്പെക്ഷൻ,リアൽ-ടൈം പ്രതികരണങ്ങൾ കാണുന്നതായി ആശ്രയിച്ച് MCP സർവർ നടപ്പാക്കലുകൾ പരിശോധനയ്ക്കും ഡീബഗിംഗിനും ഇത് സഹായകരമായി പ്രവർത്തിക്കും.

ഇത് എങ്ങനെ കാണാമെന്നു സംക്ഷിപ്തം:

![MCP Inspector server connection](../../../../translated_images/ml/connected.73d1e042c24075d3.webp)

## സാധാരണ സെറ്റ് അപ് പ്രശ്നങ്ങളും പരിഹാരങ്ങളും

| പ്രശ്നം | സാദ്ധ്യമായ പരിഹാരം |
|-------|-------------------|
| ബന്ധം നിഷേധിച്ചു | സർവർ പ്രവർത്തിക്കുന്നുണ്ടോ, പോർട്ട് ശരിയാണോ പരിശോധിക്കുക |
| ടൂൾ പ്രവർത്തന പിശകുകൾ | പാരാമീറ്റർ സാധുതയും പിശക് കൈകാര്യം ചെയ്യലും പരിശോധിക്കുക |
| ഓഥന്റിക്കേഷൻ പരാജയം | API കീകളും അനുമതികളും പരിശോധിക്കുക |
| സ്കീമ വാലിഡേഷൻ പിശകുകൾ | നിർവചിച്ച സ്കീമയുമായി പാരാമീറ്ററുകൾ ഒത്തുചേരുന്നതാണോ എന്ന് ഉറപ്പാക്കുക |
| സർവർ ആരംഭിക്കുന്നില്ല | പോർട്ട് സംഘർഷങ്ങൾ, അനിവാര്യ ആശ്രിതത്വങ്ങൾ പരിശോധിക്കുക |
| CORS പിശകുകൾ | ക്രോസ്-ഓറിജിൻ അഭ്യർത്ഥനകൾക്കായി ശരിയായ CORS ഹെട്ടറുകൾ ക്രമീകരിക്കുക |
| ഓതന്റിക്കേഷൻ പ്രശ്നങ്ങൾ | ടോക്കൺ സാധുതയും അനുമതികളും പരിശോധിക്കുക |

## പ്രാദേശിക വികസനം

പ്രാദേശിക വികസനത്തിനും പരിശോധനയ്ക്കും, നിങ്ങൾക്ക് MCP സർവറുകൾ നേരിട്ട് നിങ്ങളുടെ കമ്പ്യൂട്ടറിൽ പ്രവർത്തിപ്പിക്കാം:

1. **സർവർ പ്രോസസ് ആരംഭിക്കുക**: നിങ്ങളുടെ MCP സർവർ ആപ്ലിക്കേഷൻ ഓടിക്കുക
2. **നെറ്റ്‌വർക്ക് ക്രമീകരിക്കൽ**: സർവർ പ്രതീക്ഷിക്കുന്ന പോർട്ടിൽ പ്രവേശനയോഗ്യമാണെന്ന് ഉറപ്പാക്കുക
3. **ക്ലയന്റുകളെ ബന്ധിപ്പിക്കുക**: `http://localhost:3000` പോലുള്ള പ്രാദേശിക കണക്ഷൻ URLs ഉപയോഗിക്കുക

```bash
# ഉദാഹരണം: ടൈപ്പ്‌സ്ക്രിപ്റ്റ് MCP സർവർ ലൊക്കലായി ഓടിക്കുന്നു
npm run start
# സർവർ http://localhost:3000-ൽ ഓടുന്നു
```

## നിങ്ങളുടെ ആദ്യ MCP സർവർ നിർമ്മിക്കുക

നാം മുമ്പത്തെ പാഠത്തിൽ [Core concepts](../../01-CoreConcepts/README.md) പരിചയപ്പെട്ടു, ഇനി ആ അറിവ് പ്രായോഗികമാക്കാനുള്ള സമയം.

### ഒരു സർവർ എന്തൊക്കെ ചെയ്യാൻ കഴിയും

കോഡ് എഴുതുമ്പോൾ, ഒരു സർവർ എന്തൊക്കെ സാധിക്കും എന്നു ഓർക്കാം:

ഒരു MCP സർവർ ഉദാഹരണമായി ചെയ്‌യാം:

- പ്രാദേശിക ഫയലുകളും ഡാറ്റാബേസുകളും ആക്സസ് ചെയ്യുക
- ദൂരസ്ഥ API കളുമായി ബന്ധപ്പെടുക
- കണക്കുകൂട്ടലുകൾ നടപ്പാക്കുക
- മറ്റ് ടൂളുകളും സേവനങ്ങളും സംയോജിപ്പിക്കുക
- ഇടപെടലിന് ഒരു ഉപയോക്തൃ ഇന്റർഫേസ് നൽകുക

ശരി, ഇനി ഇത് മനസ്സിലായപ്പോൾ, കോഡിംഗ് ആരംഭിക്കാം.

## അഭ്യാസം: സർവർ നിർമ്മിക്കൽ

സർവർ സൃഷ്‌ടിക്കാൻ താഴെ പറയുന്ന പടികൾ പിന്തുടരുക:

- MCP SDK ഇൻസ്റ്റാൾ ചെയ്യുക
- ഒരു പ്രോജക്ട് സൃഷ്‌ടിച്ച് പ്രോജക്ട് ഘടന സജ്ജമാക്കുക
- സർവർ കോഡ് എഴുതുക
- സർവർ പരീക്ഷിക്കുക

### -1- പ്രോജക്ട് സൃഷ്‌ടിക്കുക

#### TypeScript

```sh
# പ്രോജക്ട് ഡയറക്ടറി സൃഷ്ടിച്ച് npm പ്രോജക്ട് ആരംഭിക്കുക
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# പ്രോജക്ട് ഡയറക്ടറി സൃഷ്ടിക്കുക
mkdir calculator-server
cd calculator-server
# ഫോൾഡർ വിസ്വൽ സ്റ്റുഡിയോ കോഡിൽ തുറക്കുക - നിങ്ങള് വേറെ ഐഇഡി ഉപയോഗിക്കുന്ന വേഷം ഇത് തള്ളുക
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java ന്, Spring Boot പ്രോജექტ് സൃഷ്‌ടിക്കുക:

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

Zip ഫയൽ വിരലൊഴിക്കുക:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# തിരഞ്ഞെടുപ്പായി ഉപയോഗിക്കാത്ത ടെസ്റ്റ് നീക്കം ചെയ്യുക
rm -rf src/test/java
```

*pom.xml* ഫയലിൽ താഴെ കൊടുത്ത പൂർണ്ണ കോൺഫിഗറേഷൻ ചേർക്കുക:

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

### -2- ആശ്രിതത്വങ്ങൾ ചേർക്കുക

പ്രോജക്ട് സൃഷ്‌ടിച്ച ശേഷം ആശ്രിതത്വങ്ങൾ ചേർക്കാം:

#### TypeScript

```sh
# ഇതിനകം ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ലെങ്കിൽ, TypeScript ഗ്ലോബലായി ഇൻസ്റ്റാൾ ചെയ്യുക
npm install typescript -g

# MCP SDK ഉം സ്‌കീമ പരിശോധനക്കു വേണ്ടി Zod ഉം ഇൻസ്റ്റാൾ ചെയ്യുക
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ഒരു വെർച്വൽ എൻവയറൺമെന്റ് സൃഷ്‌ടിക്കുകയും ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുകയും ചെയ്യുക
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

### -3- പ്രോജക്ട് ഫയലുകൾ സൃഷ്‌ടിക്കുക

#### TypeScript

*package.json* ഫയൽ തുറന്നിട്ട് താഴെ പറയുന്ന ഉള്ളടക്കം ഉപയോഗിച്ച് മാറ്റുക, സർവർ ബന്ധിപ്പിക്കും പ്രവർത്തിക്കും എന്ന് ഉറപ്പാക്കാൻ:

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

*tsconfig.json* എന്നൊരു ഫയൽ സൃഷ്‌ടിച്ച് താഴെ പറയുന്ന ഉള്ളടക്കം ചേർക്കുക:

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

സുരക്ഷിതമായ സ്രോതകോഡിനായി ഒരു ഡയറക്ടറി സൃഷ്‌ടിക്കുക:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* എന്നൊരു ഫയൽ സൃഷ്‌ടിക്കുക

```sh
touch server.py
```

#### .NET

ആവശ്യമായ NuGet പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot പ്രോജക്ടുകൾക്ക് പ്രോജക്ട് ഘടന സ്വയമെത്തുന്നു.

#### Rust

Rust-നു വേണ്ടി, `cargo init` റൺ ചെയ്താൽ പ്രാഥമികമായ *src/main.rs* ഫയൽ സൃഷ്‌ടിക്കും. അതിൽ പഴയ കോഡ് നീക്കം ചെയ്ത് തുറക്കുക.

### -4- സർവർ കോഡ് സൃഷ്‌ടിക്കുക

#### TypeScript

*index.ts* ഫയൽ സൃഷ്‌ടിച്ച് താഴെ കൊടുത്ത കോഡ് ചേർക്കുക:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ഒരു MCP സെർവർ സൃഷ്ടിക്കൂ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ഇപ്പോൾ നിങ്ങൾക്കൊരു സർവർ ഉണ്ട്, പക്ഷെ അത് അധികം ചെയ്യുന്നതില്ല, പരിഹരിക്കാം.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ഒരു MCP സെർവർ സൃഷ്ടിക്കുക
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

Java-ക്ക് കോർ സർവർ ഘടകങ്ങൾ സൃഷ്‌ടിക്കുക. ആദ്യം പ്രധാന એપ്ലിക്കേഷൻ ക്ലാസ്സ് മാറ്റുക:

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

ക്യാൽക്കുലേറ്റർ സേവനം സൃഷ്‌ടിക്കുക *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ഉത്പാദനത്തിനായി തയ്യാറായുള്ള സേവനത്തിനുള്ള ഓപ്ഷണൽ ഘടകങ്ങൾ:**

സ്റ്റാർട്ടപ്പ് കോൺഫിഗറേഷൻ സൃഷ്‌ടിക്കുക *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

ഹെൽത്ത് കൺട്രോളർ സൃഷ്‌ടിക്കുക *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ശ്യോർപ്പണക്കൾ കൈകാര്യം ചെയ്യുന്ന ഹാൻഡ്ലർ സൃഷ്‌ടിക്കുക *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // ഗെറ്ററുകൾ
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

ഒരുപ്രകാരം കസ്റ്റം ബാനർ സൃഷ്‌ടിക്കുക *src/main/resources/banner.txt*:

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

*src/main.rs* ഫയലിന്റെ മുകളിൽ താഴെ കൊടുത്ത കോഡ് ചേർക്കുക. ഇത് MCP സർവറിന് ആവശ്യമായ ലൈബ്രറികളും മോഡ്യൂളുകളും ഇറക്കുമതി ചെയ്യുന്നു.

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

ക്യാൽക്കുലേറ്റർ സർവർ രണ്ട് സംഖ്യകൾ കൂട്ടിച്ചേർക്കുന്ന ലളിതമായതാണ്. ക്യാല്കുലേറ്റർ അഭ്യർത്ഥനക്കാരനെ പ്രതിനിധീകരിക്കുന്ന struct സൃഷ്‌ടിക്കുക.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

അടുത്തത്, ടൂൾ റൂട്ടർ അടങ്ങിയ ഒരു struct സൃഷ്‌ടിച്ച് ക്യാല്കുലേറ്റർ സർവർ പ്രതിനിധീകരിക്കുക.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ഇപ്പൊൾ, പുതിയ ഒരു ഇൻസ്റ്റൻസ് സൃഷ്‌ടിച്ച് സെർവർ വിവരങ്ങൾ നൽകാനുള്ള ഹാൻഡ്ലർ ഉൾപ്പെടെ `Calculator` struct നടപ്പാക്കാം.

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

അവസാനമായി, സെർവർ ആരംഭിക്കുന്ന പ്രധാന ഫംഗ്ഷൻ നടപ്പാക്കേണ്ടതാണ്. ഇത് `Calculator` struct ഇന്റെ ഇൻസ്റ്റൻസ് സൃഷ്‌ടിച്ച് സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്/ഔട്ട്പുട്ട് വഴി സർവർ സേവനം നടത്തും.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

സർവർ ഇപ്പോൾ സ്വന്തം.metadata് അടിസ്ഥാന വിവരങ്ങൾ നൽകുന്നതിനായി സജ്ജമാക്കി. ഇനി ജോസൂ സ്വാഗതം ഒന്നിച്ചു ചേർക്കാം.

### -5- ഒരു ടൂൾയും ഒരു വിഭവവും ചേർക്കൽ

താഴെ കൊടുത്ത കോഡ് ചേർത്ത് ടൂൾയും വിഭവവും ചേർക്കുക:

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

നിങ്ങളുടെ ടൂൾ `a` , `b` പാരാമീറ്ററുകൾ സ്വീകരിച്ച് ഇത്തരത്തിൽ പ്രതികരണം സൃഷ്‌ടിക്കുന്നു:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

നിങ്ങളുടെ വിഭവം "greeting" എന്ന സ്ട്രിംഗ് വഴിയാണ് ആക്സസ് ചെയ്യപ്പെടുന്നത്, `name` പാരാമീറ്റർ സ്വീകരിച്ച് ടൂളിനെപ്പോലെ സമാനമായ പ്രതികരണം സൃഷ്‌ടിക്കുന്നു:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ഒരു එකතු ചെയ്യുന്ന ടൂൾ ചേർക്കുക
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ഒരു ഡൈനാമിക് സ്വാഗതം സ്രോതസ് ചേർക്കുക
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

മുൻപത്തെ കോഡിൽ നമ്മൾ:

- `add` എന്ന ടൂൾ നിർവചിച്ചു, രണ്ട് പാരാമീറ്ററുകൾ `a`, `b` സ്വീകരിക്കുന്നു, ഇരണ്ടും ഇൻറേജറുകൾ.
- `greeting` എന്ന ഒരു വിഭവം സൃഷ്‌ടിച്ചു, `name` പാരാമീറ്റർ സ്വീകരിക്കുന്നതാണ്.

#### .NET

Program.cs ഫയലിൽ ഇത് ചേർക്കുക:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ടൂളുകൾ മുമ്പത്തെ ഘട്ടത്തിൽ തന്നെ സൃഷ്‌ടിച്ചിരുന്നു.

#### Rust

`impl Calculator` ബ്ലോക്കിൽ ഒരു പുതിയ ടൂൾ ചേർക്കുക:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- അന്തിമ കോഡ്

സർവർ ആരംഭിക്കാൻ വേണ്ട അവസാന കോഡ് ചേർക്കാം:

#### TypeScript

```typescript
// stdin-ൽ സന്ദേശങ്ങൾ സ്വീകരിക്കാൻ തുടങ്ങുക һәм stdout-ൽ സന്ദേശങ്ങൾ അയയ്‌ക്കുക
const transport = new StdioServerTransport();
await server.connect(transport);
```

കൊണ്ട് പൂർണ്ണ കോഡ് ഇതാണ്:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ഒരു MCP സേർവർ സൃഷ്ടിക്കുക
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ഒരു കൂട്ടൽ ഉപകരണം ചേർക്കുക
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ഒരു സജീവ സ്വാഗത വിഭവം ചേർക്കുക
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

// stdin-ൽ സന്ദേശങ്ങൾ സ്വീകരിക്കാൻ ആരംഭിക്കുക, stdout-ൽ സന്ദേശങ്ങൾ അയയ്ക്കുക
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ഒരു MCP സർവർ സൃഷ്ടിക്കുക
mcp = FastMCP("Demo")


# ഒരു കൂട്ടു പരിശോധനാ ഉപകരണം ചേർക്കുക
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ഒരു സജീവ അഭിവാദന സ്രോതസ്സ് ചേർക്കുക
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# പ്രധാന പ്രവർത്തന ബ്ലോക്ക് - ഈ സർവർ പ്രവർത്തിപ്പിക്കാൻ ആവശ്യമാണ്
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs ഫയലിൽ താഴെ കാണുന്ന ഉള്ളടക്കം ഉണ്ടാകണം:

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

നിങ്ങളുടെ പ്രധാന അപ്ലിക്കേഷൻ ക്ലാസ്സ് ഈപോലെ കാണണം:

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

Rust സർവറിന്റെ അവസാന കോഡ് ഇതുപോലെ കാണണം:

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

### -7- സർവർ പരീക്ഷിക്കുക

താഴെ കൊടുത്ത കമാൻഡ് ഉപയോഗിച്ച് സർവർ ആരംഭിക്കുക:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP ഇന്‍സ്‌പെക്ടർ ഉപയോഗിക്കാൻ, `mcp dev server.py` ഉപയോഗിക്കുക, ഇത് സ്വയം ഇൻസ്‌പെക്ടർ ആരംഭിക്കുകയും ആവശ്യമുള്ള പ്രോക്സി സെഷൻ ടോക്കൺ നൽകുകയും ചെയ്യും. `mcp run server.py` ഉപയോഗിക്കുന്ന പക്ഷം, നിങ്ങൾ സ്വയം ഇൻസ്‌പെക്ടർ ആരംഭിച്ച് കണക്ഷൻ ക്രമീകരിക്കേണ്ടതുണ്ട്.

#### .NET

പ്രോജക്ട് ഡയറക്ടറിയിൽ ഉണ്ടെന്ന് ഉറപ്പാക്കുക:

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

ഫോർമാറ്റ് ചെയ്ത് സർവർ ഓടിക്കാൻ താഴെ കൊടുത്ത കമാൻഡുകൾ റൺ ചെയ്യുക:

```sh
cargo fmt
cargo run
```

### -8- ഇൻസ്‌പെക്ടർ ഉപയോഗിച്ച് ഓടിക്കുക

ഇൻസ്‌പെക്ടർ ഒരു മികച്ച ഉപകരണം ആണ്, ഇത് നിങ്ങൾക്ക് സർവർ തുടങ്ങാനും, അതുമായി ഇടപഴകാനും സാദ്ധ്യമാക്കുന്നു, അതു ശരിയായി പ്രവർത്തിക്കുന്നുണ്ടോയെന്ന് പരീക്ഷിക്കാൻ.

> [!NOTE]
> "command" ഫീൽഡിൽ ഉള്ളത് വ്യത്യസ്തമായി കാണാമെന്നു ശ്രദ്ധിക്കുക, കാരണം ഇത് നിങ്ങളുടെ-runtime-ൻറെ ഡിഫാൾട്ട് സർവർ ഓടിക്കുന്ന കമാൻഡ് ആണ്.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

അല്ലെങ്കിൽ ഇത് *package.json* പ്രസ്താവനയിലേക്ക് ചേർക്കാം: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` പിന്നീട് `npm run inspector` പ്രവർത്തിപ്പിക്കുക.

#### Python

Python ഒരു Node.js ടൂൾ ആയ ഇന്‍സ്‌പെക്ടറിൻറെ അതിരുമുകളായ ഒരു റാപ്പർ ആണ്. ഈ ഉപകരണം ഇങ്ങനെ വിളിക്കാം:

```sh
mcp dev server.py
```

എങ്കിലും, ഈ ടൂൾ ലഭ്യമായ എല്ലാ മെത്തഡുകളും നടപ്പിലാക്കിയിരിക്കുന്നത് അല്ല, അതിനാൽ Node.js ടൂൾ നേരിട്ട് ഇങ്ങനെയാണ് ഓടിക്കാൻ ശുപാർശ ചെയ്യുന്നു:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

നിങ്ങൾ കമാൻഡുകളും_ARGUMENTS_കളും സജ്ജമാക്കാവുന്ന ടൂൾ അല്ലെങ്കിൽ IDE ഉപയോഗിക്കുന്നുറച്ച്,
നിശ്ചയിക്കുക `Command` ഫീല्डില്‍ `python` സെറ്റ് ചെയ്തിരിക്കുമെന്ന്, അതുപോലെ `Arguments` ൽ `server.py` ഉം. ഇതുവഴി സ്‌ക്രിപ്റ്റ് ശരിയായി പ്രവർത്തിക്കും.

#### .NET

നിങ്ങളുടെ പ്രോജക്ട് ഡയറക്ടറിയിലാണെന്ന് ഉറപ്പാക്കുക:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### ജാവ

നിങ്ങളുടെ കാൽക്കുലേറ്റർ സർവർ പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക
ഇൻസ്പെക്ടർ പ്രവർത്തിപ്പിക്കുക:

```cmd
npx @modelcontextprotocol/inspector
```

ഇൻസ്പെക്ടർ വെബ് ഇന്റർഫേസ്:

1. ട്രാൻസ്പോർട്ട് തരം ആയി "SSE" തെരഞ്ഞടുക്കുക
2. URL ഈ വിധത്തിൽ സജ്ജമാക്കുക: `http://localhost:8080/sse`
3. "Connect" ക്ലിക് ചെയ്യുക

![Connect](../../../../translated_images/ml/tool.163d33e3ee307e20.webp)

**ഇപ്പോൾ നിങ്ങൾ സർവറുമായി ബന്ധിപ്പിച്ചിരിക്കുന്നു**
**ജാവ സർവർ ടെസ്റ്റിംഗ് വിഭാഗം ഇപ്പോൾ പൂര്‍ത്തിയായി**

അടുത്ത വകുപ്പ് സർവറുമായി ഇടപഴകൽ കുറിച്ചുള്ളതാണ്.

നിങ്ങൾ താഴെ കാണുന്ന ഉപയോക്തൃ ഇന്റർഫേസ് കാണും:

![Connect](../../../../translated_images/ml/connect.141db0b2bd05f096.webp)

1. "Connect" ബട്ടൺ സെലക്ട് ചെയ്ത് സർവറുമായി ബന്ധിപ്പിക്കുക
  ബന്ധിപ്പിച്ചതിന് ശേഷം, താഴെ കാണുന്നവ കാണാം:

  ![Connected](../../../../translated_images/ml/connected.73d1e042c24075d3.webp)

1. "Tools" -> "listTools" സെലക്ട് ചെയ്യുക, "Add" കാണണം, "Add" തിരഞ്ഞെടുക്കുകയും പാരാമീറ്റർ മൂല്യങ്ങൾ പൂരിപ്പിക്കയും ചെയ്യുക.

  താഴെ കാണുന്ന പ്രതികരണം ലഭിക്കും, അതായത് "add" ടൂളിൽ നിന്നുള്ള ഫലം:

  ![Result of running add](../../../../translated_images/ml/ran-tool.a5a6ee878c1369ec.webp)

അഭിനന്ദനങ്ങൾ, നിങ്ങൾ ആദ്യ MCP സർവർ സൃഷ്ടിച്ച് പ്രവർത്തിപ്പിക്കാൻ കഴിഞ്ഞു!

#### റസ്റ്റ്

MCP ഇൻസ്പെക്ടർ CLI ഉപയോഗിച്ച് റസ്റ്റ് സർവർ പ്രവർത്തിപ്പിക്കാൻ താഴെക്കാർദ്ദ വെളിപ്പെടുത്താം:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### ഔദ്യോഗിക SDKകൾ

MCP വിവിധ ഭാഷകൾക്കായി ഔദ്യോഗിക SDKകൾ നൽകുന്നു:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft എന്നിവരുമായി സംയുക്തമായ് പരിപാലനം നടത്തുന്നു
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI സംയുക്തമായി പരിപാലിക്കുന്നു
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - ഔദ്യോഗിക TypeScript നടപ്പ്
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - ഔദ്യോഗിക Python നടപ്പ്
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - ഔദ്യോഗിക Kotlin നടപ്പ്
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI സംയുക്തമായ് പരിപാലിക്കുന്നു
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - ഔദ്യോഗിക Rust നടപ്പ്

## പ്രധാന ക്ലൂകൾ

- MCP ഡെവലപ്‌മെന്റ് പരിസ്ഥിതി സജ്ജീകരിക്കൽ ഭാഷാനുസൃത SDKകളോടൊപ്പം ലളിതമാണ്
- MCP സർവർ നിർമ്മാണം തന്നെ സയിയുടെ ടൂളുകളും വ്യക്തമായ schemaകൾ ഓരോരുത്തരും സൃഷ്ടിക്കുകയും രജിസ്റ്റർ ചെയ്യുകയും ചെയ്യുന്നു
- ടെസ്റ്റിംഗ്, ഡീബഗ്ഗിംഗ് MCP യാഥാർത്ഥ്യത്തിനായി അത്യാവശ്യമാണ്

## സാംപിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## അവലംബം

നിങ്ങളുടെ ഇഷ്ടത്തിലുള്ള ഒരു ടൂൾ ഉപയോഗിച്ച് ലളിതമായ MCP സർവർ സൃഷ്ടിക്കുക:

1. നിങ്ങളുടെ ഇഷ്ടമുള്ള ഭാഷയിൽ ടൂൾ നടപ്പിലാക്കി (.NET, ജാവ, പൈതൺ, ടൈപ്പ്സ്ക്രിപ്റ്റ്, അല്ലെങ്കിൽ റസ്റ്റ്).
2. ഇൻപുട് പാരാമീറ്ററുകളും റിട്ടേൺ മൂല്യങ്ങളും നിർവചിക്കുക.
3. ഇൻസ്പെക്ടർ ടൂൾ ഉപയോഗിച്ച് സെർവർ ശരിയായി പ്രവർത്തിക്കുന്നുവെന്ന് ഉറപ്പ് വരുത്തുക.
4. വിവിധ ഇൻപുട്ടുകളോടെ നടപ്പിൽ പരീക്ഷിക്കുക.

## പരിഹാരം

[Solution](./solution/README.md)

## അധിക സ്രോതസ്സുകൾ

- [Azure-ൽ Model Context Protocol ഉപയോഗിച്ച് ബിൽഡ് ഏജന്റുകൾ](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps තුളെൻറെ MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ഏജന്റ്](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## അടുത്തത്

അടുത്തത്: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ഡിസ്ക്ലെയ്മർ**:  
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി പരിശ്രമിച്ചുവെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ തോന്നൽ കുറവുകൾ ഉണ്ടാകാമെന്ന് ദയവായി മനസിലാക്കുക. അതിന്റെ മാതൃഭാഷയിലെ പ്രാഥമിക ഡോക്യുമെന്റ് അതിന്റെ പ്രാമാണിക സ്രോതസ്സായി കണക്കാക്കപ്പെടണം. നിർണ്ണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിൽ നിന്നുള്ള ഏതൊരു തെറ്റായ ബോധവും അല്ലെങ്കിൽ വ്യാഖ്യാനവും സംബന്ധിച്ച് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP ਨਾਲ ਸ਼ੁਰੂਆਤ

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਨਾਲ ਤੁਹਾਡੇ ਪਹਿਲੇ ਕਦਮਾਂ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ! ਚਾਹੇ ਤੁਸੀਂ MCP ਵਿੱਚ ਨਵੇਂ ਹੋ ਜਾਂ ਆਪਣੀ ਸਮਝ ਨੂੰ ਗਹਿਰਾ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਇਹ ਮਾਰਗਦਰਸ਼ਕ ਤੁਹਾਨੂੰ ਜਰੂਰੀ ਸੈਟਅਪ ਅਤੇ ਵਿਕਾਸ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਰਾਹ ਦਿੱਸੇਗਾ। ਤੁਹਾਨੂੰ ਪਤਾ ਲੱਗੇਗਾ ਕਿ MCP ਕਿਵੇਂ AI ਮਾਡਲਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿਚਕਾਰ ਸਹਜ ਇੰਟੀਗਰੇਸ਼ਨ ਨੂੰ ਸਮਰਥਿਤ ਕਰਦਾ ਹੈ, ਅਤੇ ਤੁਸੀਂ ਜਲਦੀ ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਤਿਆਰ ਕਰਨਾ ਸਿੱਖੋਗੇ ਤਾਂ ਕਿ MCP-ਸਮਰਥਿਤ ਹੱਲ ਬਣਾਉਣ ਅਤੇ ਪਰੀਖਣ ਕਰ ਸਕੋ।

> ਸੰਖੇਪ; ਜੇ ਤੁਸੀਂ AI ਐਪ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ LLM (ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ) ਵਿੱਚ ਟੂਲ ਅਤੇ ਹੋਰ ਸਰੋਤ ਜੋੜ ਸਕਦੇ ਹੋ, ਤਾਂ ਜੋ LLM ਹੋਰ ਗਿਆਨਵਾਨ ਬਣ ਜਾਵੇ। ਪਰ ਜੇ ਤੁਸੀਂ ਉਹ ਸਾਰੇ ਟੂਲ ਅਤੇ ਸਰੋਤ ਸਰਵਰ ਤੇ ਰੱਖੋ, ਤਾਂ ਐਪ ਅਤੇ ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਕਿਸੇ ਵੀ ਕਲਾਇੰਟ ਦੁਆਰਾ ਬਿਨਾਂ/ਲੜਾਈ ਦੇ ਵਰਤੀ ਜਾ ਸਕਦੀਆਂ ਹਨ। 

## ਸਾਰਾਂਸ਼

ਇਹ ਪਾਠ MCP ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ ਅਤੇ ਤੁਹਾਡੇ ਪਹਿਲੇ MCP ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਣਾਉਣ ਲਈ ਵਿਹੰਗਮ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਜਰੂਰੀ ਉਪਕਰਨ ਅਤੇ ਫਰੇਮਵਰਕ ਸੈਟਅਪ ਕਿਵੇਂ ਕਰਨੇ ਹਨ, ਆਧਾਰਭੂਤ MCP ਸਰਵਰ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ, ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣੇ ਹਨ ਅਤੇ ਆਪਣੀ ਕਿਰਿਆਵਲੀ ਦੀ ਜਾਂਚ ਕਿਵੇਂ ਕਰਨ ਦੀ ਹੈ।

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੱਕ ਖੁੱਲ੍ਹਾ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਇਸ ਗੱਲ ਦੀ ਮਿਆਰੀਕਰਨ ਕਰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ LLM ਨੂੰ ਸੰਦਰਭ ਕਿਵੇਂ ਦਿੰਦੇ ਹਨ। MCP ਨੂੰ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ USB-C ਪੋਰਟ ਵਾਂਗ ਸੋਚੋ - ਇਹ ਵੱਖ-ਵੱਖ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ AI ਮਾਡਲਾਂ ਨੂੰ ਜੁੜਨ ਦਾ ਇੱਕ ਮਿਆਰੀਕ੍ਰਿਤ ਤਰੀਕਾ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦਾ ਹੈ।

## ਸਿਖਲਾਈ ਦੇ ਲਕੜੇ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ਸਮਰਥ ਹੋਵੋਗੇ:

- C#, Java, Python, TypeScript, ਅਤੇ Rust ਵਿੱਚ MCP ਲਈ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈਟਅپ ਕਰਨਾ
- ਕਸਟਮ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ (ਸਰੋਤ, ਪ੍ਰੰਪਟ, ਅਤੇ ਟੂਲ) ਨਾਲ ਆਧਾਰਭੂਤ MCP ਸਰਵਰ ਬਣਾਉਣਾ ਅਤੇ ਤੈਨਾਤ ਕਰਨਾ
- MCP ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਨ ਵਾਲੀਆਂ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣਾ
- MCP ਅਮਲਦਾਰੀ ਦੀ ਜਾਂਚ ਅਤੇ ਡੀਬੱਗਿੰਗ ਕਰਨਾ

## ਆਪਣਾ MCP ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨਾ

MCP ਨਾਲ ਕੰਮ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਆਪਣਾ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰਨਾ ਅਤੇ ਬੁਨਿਆਦੀ ਕਾਰਜ ਪ੍ਰਵਾਹ ਨੂੰ ਸਮਝਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਇਹ ਭਾਗ ਤੁਹਾਨੂੰ ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ ਕਦਮਾਂ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ ਤਾਂ ਜੋ MCP ਨਾਲ ਤੁਹਾਡੀ ਸ਼ੁਰੂਆਤ ਸਰਲ ਹੋਵੇ।

### ਲੋੜੀਂਦੇ ਚੀਜ਼ਾਂ

MCP ਵਿਕਾਸ ਵਿਚ ਡੁਬਕੀ ਲਗਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਯਕੀਨੀ ਬਣਾਓ ਕਿ:

- **ਵਿਕਾਸ ਵਾਤਾਵਰਣ**: ਆਪਣੇ ਚੁਣੇ ਭਾਸ਼ਾ (C#, Java, Python, TypeScript, ਜਾਂ Rust) ਲਈ
- **IDE/ਸੰਪਾਦਕ**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, ਜਾਂ ਕੋਈ ਆਧੁਨਿਕ ਕੋਡ ਐਡੀਟਰ
- **ਪੈਕੇਜ ਮੈਨੇਜਰ**: NuGet, Maven/Gradle, pip, npm/yarn, ਜਾਂ Cargo
- **API ਕੁੰਜੀਆਂ**: ਜਿਹੜੀਆਂ ਕਿਸੇ ਵੀ AI ਸੇਵਾਵਾਂ ਲਈ ਤੁਹਾਡੇ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਵਰਤੀ ਜਾਣਗੀਆਂ

## ਆਧਾਰਭੂਤ MCP ਸਰਵਰ ਦੀ ਸੰਰਚਨਾ

ਇੱਕ MCP ਸਰਵਰ ਆਮ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ:

- **ਸਰਵਰ ਸੰਰਚਨਾ**: ਪੋਰਟ, ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਹੋਰ ਸੈਟਿੰਗਾਂ ਦਾ ਸੈਟਅਪ
- **ਸਰੋਤ**: LLM ਨੂੰ ਉਪਲੱਬਧ ਡਾਟਾ ਅਤੇ ਸੰਦਰਭ
- **ਟੂਲ**: ਫੰਕਸ਼ਨਲਿਟੀ ਜੋ ਮਾਡਲ ਆਹਵਾਨ ਕਰ ਸਕਦੇ ਹਨ
- **ਪ੍ਰੰਪਟ**: ਟੈਕਸਟ ਬਣਾਉਣ ਜਾਂ ਬਣਤਰ ਦੇੇਣ ਲਈ ਟੈਮਪਲੇਟ

ਇੱਥੇ TypeScript ਵਿੱਚ ਇੱਕ ਸਧਾਰਿਤ ਉਦਾਹਰਣ ਹੈ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ਇੱਕ ਜੋੜਣ ਵਾਲਾ ਸੰਦ ਸ਼ਾਮਲ ਕਰੋ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਵਾਗਤ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ
server.resource(
  "file",
  // 'list' ਪੈਰਾਮੀਟਰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ ਕਿ ਸਰੋਤ ਕਿਵੇਂ ਉਪਲਬਧ ਫਾਇਲਾਂ ਦੀ ਸੂਚੀ ਦਿੰਦਾ ਹੈ। ਇਸ ਨੂੰ undefined ਤੇ ਸੈੱਟ ਕਰਨ ਨਾਲ ਇਸ ਸਰੋਤ ਲਈ ਸੂਚੀਬੱਧਤਾ ਅਯੋਗ ਹੋ ਜਾਂਦੀ ਹੈ।
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ਇੱਕ ਫਾਇਲ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਫਾਇਲ ਦੀ ਸਮੱਗਰੀ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ
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

// stdin 'ਤੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਅਤੇ stdout 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਣਾ ਸ਼ੁਰੂ ਕਰੋ
const transport = new StdioServerTransport();
await server.connect(transport);
```


ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP TypeScript SDK ਤੋਂ ਜਰੂਰੀ ਕਲਾਸਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕੀਤਾ।
- ਨਵਾਂ MCP ਸਰਵਰ ਉਦਾਹਰਣ ਬਣਾਇਆ ਅਤੇ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਇੱਕ ਕਸਟਮ ਟੂਲ (`calculator`) ਰਜਿਸਟਰ ਕੀਤਾ ਇੱਕ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਨਾਲ।
- ਆਉਣ ਵਾਲੀਆਂ MCP ਬੇਨਤੀਆਂ ਨੂੰ ਸੁਣਨ ਲਈ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕੀਤਾ।

## ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ

ਆਪਣਾ MCP ਸਰਵਰ ਟੈਸਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਉਪਲੱਬਧ ਟੂਲਾਂ ਅਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਸਰਬੋਤਮ ਅਭਿਆਸ ਨੂੰ ਸਮਝਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਤੁਹਾਡੇ ਸਰਵਰ ਦੇ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਚਲਣ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਜਲਦੀ ਪਹਿਚਾਣਨ ਅਤੇ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਭਾਗ ਤੁਹਾਡੇ MCP ਅਮਲਦਾਰੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਸਿਫ਼ਾਰਸ਼ੀਡ ਤਰੀਕੇ ਵੱਖ-ਵੱਖ ਕਰਦਾ ਹੈ।

MCP ਤੁਹਾਡੇ ਸਰਵਰਾਂ ਨੂੰ ਟੈਸਟ ਅਤੇ ਡੀਬੱਗ ਕਰਨ ਲਈ ਟੂਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

- **ਇੰਸਪੈਕਟਰ ਟੂਲ**, ਇਹ ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਤੁਹਾਡੇ ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਅਤੇ ਆਪਣੇ ਟੂਲ, ਪ੍ਰੰਪਟ ਅਤੇ ਸਰੋਤਾਂ ਦੀ ਜਾਂਚ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- **curl**, ਤੁਸੀਂ curl ਵਰਗੇ ਕਮਾਂਡ ਲਾਈਨ ਟੂਲ ਜਾਂ ਹੋਰ ਕਲਾਇੰਟਾਂ ਨੂੰ ਵਰਤ ਕੇ ਆਪਣੇ ਸਰਵਰ ਨਾਲ ਜੁੜ ਸਕਦੇ ਹੋ ਜੋ HTTP ਕਮਾਂਡਾਂ ਬਣਾਉਂਦੇ ਅਤੇ ਚਲਾਉਂਦੇ ਹਨ।

### MCP ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ

[MCP ਇੰਸਪੈਕਟਰ](https://github.com/modelcontextprotocol/inspector) ਇੱਕ ਵਿਜ਼ुअਲ ਟੈਸਟਿੰਗ ਟੂਲ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ:

1. **ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਖੋਜ ਕਰੋ**: ਉਪਲਬਧ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰੰਪਟ ਦੀ ਆਪਣੇ ਆਪ ਪਹਿਚਾਣ ਕਰੋ
2. **ਟੂਲ ਕੰਮਕਾਜ ਨੂੰ ਟੈਸਟ ਕਰੋ**: ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰ ਅਜ਼ਮਾਓ ਅਤੇ ਪ੍ਰਤੀਕ੍ਰਿਆ ਤਤਕਾਲ ਵੇਖੋ
3. **ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਵੇਖੋ**: ਸਰਵਰ ਦੀ ਜਾਣਕਾਰੀ, ਸਕੀਮਾ ਅਤੇ ਸੰਰਚਨਾ ਦੀ ਜਾਂਚ ਕਰੋ

```bash
# ex TypeScript, MCP ਇੰਸਪੈਕਟਰ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨਾ ਅਤੇ ਚਲਾਉਣਾ
npx @modelcontextprotocol/inspector node build/index.js
```


ਉਪਰ ਦਿੱਤੇ ਹੋਏ ਕਮਾਂਡ ਚਲਾਉਣ ‘ਤੇ, MCP ਇੰਸਪੈਕਟਰ ਤੁਹਾਡੇ ਬਰਾਊਜ਼ਰ ਵਿੱਚ ਇੱਕ ਸਥਾਨਕ ਵੈੱਬ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹੇਗਾ। ਤੁਸੀਂ ਆਪਣੇ ਰਜਿਸਟਰਡ MCP ਸਰਵਰਾਂ, ਉਨ੍ਹਾਂ ਦੇ ਉਪਲਭਦ ਟੂਲਾਂ, ਸਰੋਤਾਂ ਅਤੇ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਡੈਸ਼ਬੋਰਡ ਵਿੱਚ ਵੇਖ ਸਕਦੇ ਹੋ। ਇਹ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਟੂਲ ਐਕਜ਼ੀਕਿਊਸ਼ਨ ਦੀ ਤਬਾਦਲਾ ਤੱਤਕਾਲ ਟੈਸਟ ਕਰਨ, ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਦੀ ਜਾਂਚ ਕਰਨ ਅਤੇ ਜਿੰਦਾ ਪ੍ਰਤੀਕ੍ਰਿਆ ਵੇਖਣ ਲਈ ਇੰਟਰੈਕਟਿਵ ਤੌਰ ‘ਤੇ ਆਗਿਆ ਦਿੰਦੀ ਹੈ, ਜੋ ਕਿ MCP ਸਰਵਰ ਅਮਲਦਾਰੀ ਦੀ ਪੁਸ਼ਟੀ ਅਤੇ ਡੀਬੱਗਿੰਗ ਨੂੰ ਸੌਖਾ ਬਣਾਉਂਦੀ ਹੈ।

ਇਸ ਦੀ ਇੱਕ ਸਕ੍ਰੀਨਸ਼ాట్ ਇੱਥੇ ਹੈ:

![MCP Inspector server connection](../../../../translated_images/pa/connected.73d1e042c24075d3.webp)

## ਆਮ ਸੈਟਅਪ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

| ਸਮੱਸਿਆ | ਸੰਭਾਵਿਤ ਹੱਲ |
|-------|-------------------|
| ਕੰਨੈਕਸ਼ਨ ਨੂੰ ਇਨਕਾਰ | ਜਾਂਚੋ ਕਿ ਸਰਵਰ ਚਲ ਰਹਾ ਹੈ ਅਤੇ ਪੋਰਟ ਸਹੀ ਹੈ |
| ਟੂਲ ਕੰਮਕਾਜ ਵਿੱਚ ਗਲਤੀਆਂ | ਪੈਰਾਮੀਟਰ ਦੀ ਜਾਂਚ ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ ਦੀ ਸਮੀਖਿਆ ਕਰੋ |
| ਪ੍ਰਮਾਣਿਕਤਾ ਫੇਲ | API ਕੁੰਜੀਆਂ ਅਤੇ ਅਧਿਕਾਰਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ |
| ਸਕੀਮਾ ਵੈਧਤਾ ਗਲਤੀਆਂ | ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਪੈਰਾਮੀਟਰ ਪਰਿਭਾਸ਼ਿਤ ਸਕੀਮਾ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ |
| ਸਰਵਰ ਸ਼ੁਰੂ ਨਹੀਂ ਹੋ ਰਿਹਾ | ਪੋਰਟ ਟਕਰਾਅ ਜਾਂ ਗੁੰਮDependencies ਦੀ ਜਾਂਚ ਕਰੋ |
| CORS ਗਲਤੀਆਂ | ਪਰਵਾਨਗੀ ਪਾਓ ਸਹੀ CORS ਹੇਡਰਾਂ ਲਈ ਕ੍ਰਾਸ-ਓਰੀਜਨ ਬੇਨਤੀਆਂ ਲਈ |
| ਪ੍ਰਮਾਣਿਕਤਾ ਸਮੱਸਿਆਵਾਂ | ਟੋਕਨ ਦੀ ਮਿਆਦ ਅਤੇ ਅਧਿਕਾਰਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ |

## ਸਥਾਨਕ ਵਿਕਾਸ

ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ, ਤੁਸੀਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਆਪਣੇ ਮਸ਼ੀਨ ‘ਤੇ ਸਿੱਧਾ ਚਲਾ ਸਕਦੇ ਹੋ:

1. **ਸਰਵਰ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰੋ**: ਆਪਣੀ MCP ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ
2. **ਨੈੱਟਵਰਕਿੰਗ ਸੈਟਅਪ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਉਮੀਦ ਕੀਤੇ ਪੋਰਟ ‘ਤੇ ਪਹੁੰਚਯੋਗ ਹੈ
3. **ਕਲਾਇੰਟ ਜੁੜੋ**: ਸਥਾਨਕ ਕਨੈਕਸ਼ਨ URLs ਵਰਗੇ `http://localhost:3000` ਵਰਤੋ

```bash
# ਉਦਾਹਰਨ: ਟਾਈਪਸਕ੍ਰਿਪਟ MCP ਸਰਵਰ ਸਕੇਲਕੀ ਤੌਰ ਤੇ ਚਲਾ ਰਹਿਆ ਹੈ
npm run start
# ਸਰਵਰ http://localhost:3000 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੈ
```

## ਆਪਣਾ ਪਹਿਲਾ MCP ਸਰਵਰ ਬਣਾ ਰਹੇ ਹਾਂ

ਅਸੀਂ ਪਹਿਲਾਂ ਦਿੱਤੇ ਹੌਰ ਪਾਠ [ਮੂਲ ਸੰਕਲਪ](../../01-CoreConcepts/README.md) ਨੂੰ ਕਵਰ ਕਰ ਚੁੱਕੇ ਹਾਂ, ਹੁਣ ਸਮਾਂ ਹੈ ਉਹ ਗਿਆਨ ਕਮਾਉਣ ਦਾ।

### ਸਰਵਰ ਕੀ ਕਰ ਸਕਦਾ ਹੈ

ਕੋਡ ਲਿਖਣ ਤੋਂ ਪਹਿਲਾਂ, ਆਓ ਆਪਣਾ ਯਾਦ ਕਰਾਈਏ ਕਿ ਸਰਵਰ ਕੀ ਕਰ ਸਕਦਾ ਹੈ:

ਇੱਕ MCP ਸਰਵਰ ਉਦਾਹਰਣ ਲਈ ਕਰ ਸਕਦਾ ਹੈ:

- ਸਥਾਨਕ ਫਾਇਲਾਂ ਅਤੇ ਡੈਟਾਬੇਸਾਂ ਤੱਕ ਪਹੁੰਚ
- ਦੂਰੇ API ਨਾਲ ਜੁੜਨ
- ਗਣਨਾਵਾਂ ਕਰਨਾ
- ਹੋਰ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਨਾਲ ਇੱਕਠੇ ਹੋਣਾ
- ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਨਾ

ਚੰਗਾ, ਹੁਣ ਕਿ ਅਸੀਂ ਜਾਣਦੇ ਹਾਂ ਕਿ ਅਸੀਂ ਕੀ ਕਰ ਸਕਦੇ ਹਾਂ, ਆਓ ਕੋਡਿੰਗ ਸ਼ੁਰੂ ਕਰੀਏ।

## ਅਭਿਆਸ: ਸਰਵਰ ਬਣਾਉਣਾ

ਸਰਵਰ ਬਣਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਇਹ ਕਦਮ ਫੋਲੋ ਕਰਨੇ ਪੈਨਗੇ:

- MCP SDK ਇੰਸਟਾਲ ਕਰੋ।
- ਇੱਕ ਪ੍ਰਾਜੈਕਟ ਬਣਾ ਕੇ ਪ੍ਰਾਜੈਕਟ ਸੰਰਚਨਾ ਸੈਟਅਪ ਕਰੋ।
- ਸਰਵਰ ਕੋਡ ਲਿਖੋ।
- ਸਰਵਰ ਦੀ ਟੈਸਟਿੰਗ ਕਰੋ।

### -1- ਪ੍ਰਾਜੈਕਟ ਬਣਾਉਣਾ

#### TypeScript

```sh
# ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ ਅਤੇ npm ਪ੍ਰੋਜੈਕਟ ਸ਼ੁਰੂ ਕਰੋ
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# ਪ੍ਰੋਜੈਕਟ ਡਿਰੈਕਟਰੀ ਬਣਾਓ
mkdir calculator-server
cd calculator-server
# ਫੋਲਡਰ ਨੂੰ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ ਵਿੱਚ ਖੋਲ੍ਹੋ - ਜੇ ਤੁਸੀਂ ਕੋਈ ਹੋਰ IDE ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ ਇਸਨੂੰ ਛੱਡੋ
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

ਜਾਵਾ ਲਈ, ਇੱਕ Spring Boot ਪ੍ਰਾਜੈਕਟ ਬਣਾਓ:

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

ਜਿਪ ਫਾਇਲ ਖੋਲ੍ਹੋ:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ਵਿਕਲਪਿਕ ਅਣਵਰਤੇ ਟੈਸਟ ਨੂੰ ਹਟਾਓ
rm -rf src/test/java
```

ਆਪਣੇ *pom.xml* ਫਾਇਲ ਵਿੱਚ ਪੂਰੀ ਸੰਰਚਨਾ ਸ਼ਾਮਲ ਕਰੋ:

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

### -2- Dependencies ਸ਼ਾਮਲ ਕਰੋ

ਹੁਣ ਜਦੋਂ ਕਿ ਤੁਹਾਡਾ ਪ੍ਰਾਜੈਕਟ ਬਣ ਚੁੱਕਾ ਹੈ, ਆਓ dependencies ਅੱਗੇ ਸ਼ਾਮਲ ਕਰੀਏ:

#### TypeScript

```sh
# ਜੇ ਪਹਿਲਾਂ ਹੀ ਇੰਸਟਾਲ ਨਾ ਕੀਤਾ ਹੋਵੇ, ਤਾਂ ਟਾਈਪਸਕ੍ਰਿਪਟ ਨੂੰ ਗਲੋਬਲੀ ਇੰਸਟਾਲ ਕਰੋ
npm install typescript -g

# ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ MCP SDK ਅਤੇ Zod ਇੰਸਟਾਲ ਕਰੋ
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ
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

### -3- ਪ੍ਰਾਜੈਕਟ ਫਾਇਲਾਂ ਬਣਾਓ

#### TypeScript

*package.json* ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਵਿਚਾਰਵੇਲਾ ਸਮੱਗਰੀ ਹਟਾ ਕੇ ਹੇਠਾਂ ਦਿੱਤੀ ਸਮੱਗਰੀ ਨਾਲ ਬਦਲੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਸਰਵਰ ਨੂੰ ਬਣਾ ਸਕੋ ਅਤੇ ਚਲਾ ਸਕੋ:

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

*tsconfig.json* ਬਣਾਓ ਇਹਤੀ ਸਮੱਗਰੀ ਨਾਲ:

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

ਆਪਣੇ ਕੋਡ ਲਈ ਇੱਕ ਡਾਇਰੇਕਟਰੀ ਬਣਾਓ:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* ਫਾਇਲ ਬਣਾਓ

```sh
touch server.py
```

#### .NET

ਲੋੜੀਂਦੇ NuGet ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot ਪ੍ਰਾਜੈਕਟ ਲਈ ਪ੍ਰਾਜੈਕਟ ਦੀ ਸਟ੍ਰਕਚਰ ਆਟੋਮੈਟਿਕ ਬਣਾਈ ਜਾਂਦੀ ਹੈ।

#### Rust

Rust ਲਈ, ਜਦੋਂ ਤੁਸੀਂ `cargo init` ਚਲਾਉਂਦੇ ਹੋ ਤਾਂ ਆਟੋਮੈਟਿਕ *src/main.rs* ਫਾਇਲ ਬਣਦੀ ਹੈ। ਇਸ ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਮੂਲ ਕੋਡ ਹਟਾ ਦਿਓ।

### -4- ਸਰਵਰ ਕੋਡ ਬਣਾਓ

#### TypeScript

*index.ts* ਫਾਇਲ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਸਰਵਰ ਹੈ, ਪਰ ਇਹ ਕਮ ਨਹੀਂ ਕਰਦਾ, ਆਓ ਇਸ ਨੂੰ ਠੀਕ ਕਰੀਏ।

#### Python

```python
# ਸਰਵਰ.py
from mcp.server.fastmcp import FastMCP

# ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
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

ਜਾਵਾ ਲਈ, ਕੋਰ ਸਰਵਰ ਉਪਕਰਣ ਬਣਾਓ। ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਮੁੱਖ ਐਪਲੀਕੇਸ਼ਨ ਕਲਾਸ ਸੋਧੋ:

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

ਕੈਲਕੁਲੇਟਰ ਸੇਵਾ ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ਪੈਦਾ-ਵਾਲੀ ਸੇਵਾ ਲਈ ਵਿਕਲਪਿਕ ਆਪਣੇ ਹਿੱਸੇ:**

ਸਟਾਰਟਅਪ ਸੰਰਚਨਾ ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

ਹੈਲਥ ਕੰਟਰੋਲਰ ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ਗਲੋਬਲ Exception Handler ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // ਗੇਟਰਜ਼
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

ਕਸਟਮ ਬੈਨਰ ਬਣਾਓ *src/main/resources/banner.txt*:

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

*src/main.rs* ਫਾਇਲ ਦੇ ਸਿਖਰ ਲਿਖੋ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋ MCP ਸਰਵਰ ਲਈ ਲੋੜੀਂਦੇ ਟਿੱਬਾ ਅਤੇ ਮੋਡੀਊਲਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

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

ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਇੱਕ ਸਧਾਰਨ ਸਰਵਰ ਹੋਵੇਗਾ ਜੋ ਦੋ ਨੰਬਰਾਂ ਨੂੰ ਜੋੜ ਸਕਦਾ ਹੈ। ਆਓ ਇੱਕ struct ਬਣਾਈਏ ਜੋ ਕੈਲਕੁਲੇਟਰ ਬੇਨਤੀ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

ਅਗਲਾ, ਇੱਕ struct ਬਣਾਓ ਜੋ ਕੈਲਕੁਲੇਟਰ ਸਰਵਰ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਇਹ struct ਟੂਲ ਰਾਊਟਰ ਨੂੰ ਰੱਖੇਗਾ, ਜੋ ਟੂਲਾਂ ਨੂੰ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ।

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ਹੁਣ, ਅਸੀਂ `Calculator` struct ਨੂੰ ਲਾਗੂ ਕਰਾਂਗੇ ਤਾਂ ਜੋ ਸਰਵਰ ਦੀ ਨਵੀਂ ਉਦਾਹਰਣ ਬਣਾਈ ਜਾ ਸਕੇ ਅਤੇ ਸਰਵਰ ਹੈਂਡਲਰ ਲਾਗੂ ਕਰ ਸਕੀਏ ਜੋ ਸਰਵਰ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ।

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

ਆਖ਼ਿਰਕਾਰ, ਅਸੀਂ main ਫੰਕਸ਼ਨ ਲਾਗੂ ਕਰੀਏਗਾ ਜੋ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰੇਗਾ। ਇਹ ਫੰਕਸ਼ਨ `Calculator` struct ਦੀ ਇੱਕ ਉਦਾਹਰਣ ਬਣਾਏਗਾ ਅਤੇ ਇਸ ਨੂੰ ਸਧਾਰਣ ਇਨਪੁੱਟ/ਆਉਟਪੁੱਟ 'ਤੇ ਸਰਵ ਕਰੇਗਾ।

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

ਸਰਵਰ ਹੁਣ ਆਪਣੇ ਆਪ ਬਾਰੇ ਮੁੱਢਲੀ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ। ਅਗਲਾ, ਅਸੀਂ ਇੱਕ ਟੂਲ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜਿਸ ਨਾਲ ਜੋੜ ਕਰਨਾ ਸੰਭਵ ਹੋਵੇ।

### -5- ਇੱਕ ਟੂਲ ਅਤੇ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰਨਾ

ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜ ਕੇ ਇੱਕ ਟੂਲ ਅਤੇ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ:

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

ਤੁਹਾਡਾ ਟੂਲ ਪੈਰਾਮੀਟਰ `a` ਅਤੇ `b` ਲੈਂਦਾ ਹੈ ਅਤੇ ਇੱਕ ਫੰਕਸ਼ਨ ਚਲਾਉਂਦਾ ਹੈ ਜੋ ਜਵਾਬ ਦੇ ਤੌਰ ਤੇ ਇਸ ਫਾਰਮ ਦਾ ਨਤੀਜਾ ਪੈਦਾ ਕਰਦਾ ਹੈ:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

ਤੁਹਾਡਾ ਸਰੋਤ ਇੱਕ ਸਟਰਿੰਗ "greeting" ਰਾਹੀਂ ਪਹੁੰਚਯੋਗ ਹੈ ਅਤੇ ਇੱਕ ਪੈਰਾਮੀਟਰ `name` ਲੈਂਦਾ ਹੈ ਅਤੇ ਟੂਲ ਵਾਂਗ ਹੀ ਇੱਕ ਜਵਾਬ ਪੈਦਾ ਕਰਦਾ ਹੈ:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ਇੱਕ ਜੋੜਣ ਵਾਲਾ ਸੰਦ ਜੋੜੋ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਤਿਕਾਰ ਸਰੋਤ ਜੋੜੋ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਟੂਲ `add` ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜੋ ਪੈਰਾਮੀਟਰ `a` ਅਤੇ `b`, ਦੋਹਾਂ ਇੰਟੀਜਰ, ਲੈਂਦਾ ਹੈ।
- ਇੱਕ ਸਰੋਤ `greeting` ਬਣਾਇਆ ਜੋ ਪੈਰਾਮੀਟਰ `name` ਲੈਂਦਾ ਹੈ।

#### .NET

ਇਹ ਆਪਣੀ Program.cs ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ਟੂਲ ਪਹਿਲਾਂ ਹੀ ਪਿਛਲੇ ਕਦਮ ਵਿੱਚ ਬਣਾਏ ਜਾ ਚੁੱਕੇ ਹਨ।

#### Rust

`impl Calculator` ਬਲਾਕ ਦੇ ਅੰਦਰ ਇੱਕ ਨਵਾਂ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- ਆਖ਼ਰੀ ਕੋਡ

ਆਓ ਆਖ਼ਰੀ ਕੋਡ ਜੋੜੀਏ ਤਾਂ ਜੋ ਸਰਵਰ ਸ਼ੁਰੂ ਹੋ ਸਕੇ:

#### TypeScript

```typescript
// stdin 'ਤੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰਦਾ ਅਤੇ stdout 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਦਾ ਹੈ
const transport = new StdioServerTransport();
await server.connect(transport);
```

ਪੂਰਾ ਕੋਡ ਇਹ ਹੈ:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ਇੱਕ ਜੋੜਨ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਵਾਗਤ ਸਾਧਨ ਸ਼ਾਮਲ ਕਰੋ
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

// stdin 'ਤੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ stdout 'ਤੇ ਸੁਨੇਹੇ ਭੇਜੋ
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
mcp = FastMCP("Demo")


# ਇੱਕ ਜੋੜਨ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਲਾਮੀ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# ਮੁੱਖ ਕਰਨ ਵਾਲਾ ਬਲਾਕ - ਸਰਵਰ ਚਲਾਉਣ ਲਈ ਇਹ ਲਾਜ਼ਮੀ ਹੈ
if __name__ == "__main__":
    mcp.run()
```

#### .NET

ਇੱਕ Program.cs ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਸਮੱਗਰੀ ਹੋਵੇ:

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

ਤੁਹਾਡੀ ਮੁੱਖ ਐਪਲੀਕੇਸ਼ਨ ਕਲਾਸ ਇੱਥੇ ਦਿੱਤੀ ਤਰ੍ਹਾਂ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:

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

Rust ਸਰਵਰ ਲਈ ਆਖ਼ਰੀ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:

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

### -7- ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ

ਸਰਵਰ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP ਇੰਸਪੈਕਟਰ ਵਰਤਣ ਲਈ, `mcp dev server.py` ਵਰਤੋਂ, ਜੋ ਆਪਣੇ ਆਪ ਇੰਸਪੈਕਟਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ ਅਤੇ ਲੋੜੀਂਦੀ ਪ੍ਰਾਕਸੀ ਸੈਸ਼ਨ ਟੋਕਨ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਜੇ `mcp run server.py` ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਹੱਥੋਂ ਇੰਸਪੈਕਟਰ ਸ਼ੁਰੂ ਕਰਨਾ ਪਵੇਗਾ ਅਤੇ ਜੁੜਾਈ ਸੈਟਅਪ ਕਰਨੀ ਪਵੇਗੀ।

#### .NET

ਆਪਣੇ ਪ੍ਰਾਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹੋਣਾ ਯਕੀਨੀ ਬਣਾਓ:

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

ਸਰਵਰ ਨੂੰ ਫਾਰਮੈਟ ਕਰਨ ਅਤੇ ਚਲਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾਓ:

```sh
cargo fmt
cargo run
```

### -8- ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ ਨਾਲ ਚਲਾਓ

ਇੰਸਪੈਕਟਰ ਇੱਕ ਵਧੀਆ ਟੂਲ ਹੈ ਜੋ ਤੁਹਾਡੇ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਤੁਸੀਂ ਇਸ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਕੇ ਇਸ ਦੀ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਸਭ ਕੁਝ ਠੀਕ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ। ਆਓ ਇਸਨੂੰ ਸ਼ੁਰੂ ਕਰੀਏ:

> [!NOTE]
> “ਕਮਾਂਡ” ਖੇਤਰ ਵਿੱਚ ਕੁਝ ਵੱਖਰਾ ਦਿੱਸ ਸਕਦਾ ਹੈ ਕਿਉਂਕਿ ਇਸ ਵਿੱਚ ਤੁਹਾਡੇ ਖਾਸ ਰਨਟਾਈਮ ਨਾਲ ਸਰਵਰ ਚਲਾਉਣ ਲਈ ਕਮਾਂਡ ਹੁੰਦੀ ਹੈ।

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

ਜਾਂ ਇਸਨੂੰ ਆਪਣੇ *package.json* ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ ਇਨ੍ਹਾਂ ਤਰੀਕਿਆਂ ਨਾਲ: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ਅਤੇ ਫਿਰ `npm run inspector` ਚਲਾਓ।

#### Python

Python ਇੱਕ Node.js ਟੂਲ, inspector, ਨੂੰ ਰੈਪ ਕਰਦਾ ਹੈ। ਇਸ ਟੂਲ ਨੂੰ ਫ਼ਰਮਾ ਇਸ ਤਰ੍ਹਾਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ:

```sh
mcp dev server.py
```

ਪਰ ਇਹ ਸਾਰੇ ਉਪਲਬਧ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਹਵਾਲਾ ਨਹੀਂ ਦਿੰਦਾ, ਇਸ ਲਈ ਤੁਸੀਂ Node.js ਟੂਲ ਨੂੰ ਸਿੱਧਾ ਵਰਤਣ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

ਜੇਕਰ ਤੁਸੀਂ ਕਿਸੇ ਐਸੇ ਟੂਲ ਜਾਂ IDE ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹੋ ਜੋ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਲਈ ਕਮਾਂਡ ਅਤੇ ਆਰਗਮੈਂਟ ਸੰਰਚਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, 
make sure to set `python` in the `Command` field and `server.py` as `Arguments`. This ensures the script runs correctly.

#### .NET

Make sure you're in your project directory:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

Ensure you calculator server is running
The run the inspector:

```cmd
npx @modelcontextprotocol/inspector
```

In the inspector web interface:

1. Select "SSE" as the transport type
2. Set the URL to: `http://localhost:8080/sse`
3. Click "Connect"

![Connect](../../../../translated_images/pa/tool.163d33e3ee307e20.webp)

**ਤੁਸੀਂ ਹੁਣ ਸਰਵਰ ਨਾਲ ਜੁੜ ਚੁੱਕੇ ਹੋ**
**ਜਾਵਾ ਸਰਵਰ ਟੈਸਟਿੰਗ ਸੈਕਸ਼ਨ ਹੁਣ ਮੁਕੰਮਲ ਹੋ ਚੁੱਕਾ ਹੈ**

ਅਗਲਾ ਸੈਕਸ਼ਨ ਸਰਵਰ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਬਾਰੇ ਹੈ।

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ ਦਿਖਾਈ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ:

![Connect](../../../../translated_images/pa/connect.141db0b2bd05f096.webp)

1. Connect to the server by selecting the Connect button
  Once you connect to the server, you should now see the following:

  ![Connected](../../../../translated_images/pa/connected.73d1e042c24075d3.webp)

1. Select "Tools" and "listTools", you should see "Add" show up, select "Add" and fill in the parameter values.

  You should see the following response, i.e a result from "add" tool:

  ![Result of running add](../../../../translated_images/pa/ran-tool.a5a6ee878c1369ec.webp)

ਵਧਾਈਆਂ, ਤੁਸੀਂ ਆਪਣਾ ਪਹਿਲਾ ਸਰਵਰ ਬਣਾਉਣਾ ਅਤੇ ਚਲਾਉਣਾ ਸਫਲਤਾਪੂਰਵਕ ਕਰ ਲਿਆ ਹੈ!

#### Rust

To run the Rust server with the MCP Inspector CLI, use the following command:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### Official SDKs

MCP provides official SDKs for multiple languages:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Maintained in collaboration with Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Maintained in collaboration with Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - The official TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - The official Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - The official Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Maintained in collaboration with Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - The official Rust implementation

## Key Takeaways

- Setting up an MCP development environment is straightforward with language-specific SDKs
- Building MCP servers involves creating and registering tools with clear schemas
- Testing and debugging are essential for reliable MCP implementations

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Assignment

Create a simple MCP server with a tool of your choice:

1. Implement the tool in your preferred language (.NET, Java, Python, TypeScript, or Rust).
2. Define input parameters and return values.
3. Run the inspector tool to ensure the server works as intended.
4. Test the implementation with various inputs.

## Solution

[Solution](./solution/README.md)

## Additional Resources

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## What's next

Next: [Getting Started with MCP Clients](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਇਨਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਅਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
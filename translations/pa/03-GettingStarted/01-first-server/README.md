<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T06:02:53+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "pa"
}
-->
# MCP ਨਾਲ ਸ਼ੁਰੂਆਤ

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਨਾਲ ਤੁਹਾਡੇ ਪਹਿਲੇ ਕਦਮਾਂ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ! ਚਾਹੇ ਤੁਸੀਂ MCP ਵਿੱਚ ਨਵੇਂ ਹੋ ਜਾਂ ਆਪਣੀ ਸਮਝ ਨੂੰ ਗਹਿਰਾ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ ਜਰੂਰੀ ਸੈਟਅਪ ਅਤੇ ਵਿਕਾਸ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਲੈ ਕੇ ਚਲੇਗੀ। ਤੁਸੀਂ ਜਾਣੋਗੇ ਕਿ MCP ਕਿਵੇਂ AI ਮਾਡਲਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਬਿਨਾਂ ਰੁਕਾਵਟ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ, ਅਤੇ ਕਿਵੇਂ ਤੇਜ਼ੀ ਨਾਲ ਆਪਣਾ ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰਕੇ MCP-ਚਲਿਤ ਹੱਲਾਂ ਨੂੰ ਬਣਾਉਣ ਅਤੇ ਟੈਸਟ ਕਰਨ ਲਈ ਤਿਆਰ ਕਰਨਾ ਹੈ।

> TLDR; ਜੇ ਤੁਸੀਂ AI ਐਪ ਬਣਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਜਾਣਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ LLM (ਵੱਡਾ ਭਾਸ਼ਾ ਮਾਡਲ) ਵਿੱਚ ਟੂਲ ਅਤੇ ਹੋਰ ਸਰੋਤ ਜੋੜ ਸਕਦੇ ਹੋ, ਤਾਂ ਜੋ LLM ਹੋਰ ਗਿਆਨਵਾਨ ਬਣ ਜਾਵੇ। ਪਰ ਜੇ ਤੁਸੀਂ ਉਹ ਟੂਲ ਅਤੇ ਸਰੋਤ ਸਰਵਰ 'ਤੇ ਰੱਖਦੇ ਹੋ, ਤਾਂ ਐਪ ਅਤੇ ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਕਿਸੇ ਵੀ ਕਲਾਇੰਟ ਦੁਆਰਾ LLM ਹੋਵੇ ਜਾਂ ਨਾ ਹੋਵੇ ਵਰਤੀ ਜਾ ਸਕਦੀਆਂ ਹਨ।

## ਝਲਕ

ਇਹ ਪਾਠ MCP ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ ਅਤੇ ਆਪਣੇ ਪਹਿਲੇ MCP ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਣਾਉਣ ਬਾਰੇ ਪ੍ਰਯੋਗਿਕ ਮਾਰਗਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਜਰੂਰੀ ਟੂਲ ਅਤੇ ਫਰੇਮਵਰਕ ਕਿਵੇਂ ਸੈਟਅਪ ਕਰਨੇ ਹਨ, ਬੁਨਿਆਦੀ MCP ਸਰਵਰ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ, ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਕਿਵੇਂ ਬਣਾਉਣੀਆਂ ਹਨ, ਅਤੇ ਆਪਣੀਆਂ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਦੀ ਜਾਂਚ ਕਿਵੇਂ ਕਰਨੀ ਹੈ।

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੱਕ ਖੁੱਲ੍ਹਾ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਇਹ ਮਿਆਰੀਕ੍ਰਿਤ ਕਰਦਾ ਹੈ ਕਿ ਐਪਲੀਕੇਸ਼ਨ LLMs ਨੂੰ ਕਾਂਟੈਕਸਟ ਕਿਵੇਂ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। MCP ਨੂੰ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ USB-C ਪੋਰਟ ਵਾਂਗ ਸੋਚੋ - ਇਹ AI ਮਾਡਲਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਡਾਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਜੁੜਨ ਦਾ ਇੱਕ ਮਿਆਰੀਕ੍ਰਿਤ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- C#, ਜਾਵਾ, ਪਾਇਥਨ, ਟਾਈਪਸਕ੍ਰਿਪਟ, ਅਤੇ ਰਸਟ ਵਿੱਚ MCP ਲਈ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ
- ਕਸਟਮ ਫੀਚਰਾਂ (ਸਰੋਤ, ਪ੍ਰਾਂਪਟ, ਅਤੇ ਟੂਲ) ਨਾਲ ਬੁਨਿਆਦੀ MCP ਸਰਵਰ ਬਣਾਉਣ ਅਤੇ ਤੈਨਾਤ ਕਰਨ
- MCP ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਨ ਵਾਲੀਆਂ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ
- MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਦੀ ਜਾਂਚ ਅਤੇ ਡੀਬੱਗਿੰਗ ਕਰਨ

## ਆਪਣਾ MCP ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨਾ

MCP ਨਾਲ ਕੰਮ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਆਪਣਾ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰਨਾ ਅਤੇ ਬੁਨਿਆਦੀ ਵਰਕਫਲੋ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ। ਇਹ ਭਾਗ ਤੁਹਾਨੂੰ ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ ਕਦਮਾਂ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ ਤਾਂ ਜੋ MCP ਨਾਲ ਸੁਚੱਜਾ ਸ਼ੁਰੂਆਤ ਹੋ ਸਕੇ।

### ਲੋੜੀਂਦੇ ਚੀਜ਼ਾਂ

MCP ਵਿਕਾਸ ਵਿੱਚ ਡੁੱਬਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੈ:

- **ਵਿਕਾਸ ਵਾਤਾਵਰਣ**: ਆਪਣੀ ਚੁਣੀ ਹੋਈ ਭਾਸ਼ਾ ਲਈ (C#, ਜਾਵਾ, ਪਾਇਥਨ, ਟਾਈਪਸਕ੍ਰਿਪਟ, ਜਾਂ ਰਸਟ)
- **IDE/ਸੰਪਾਦਕ**: ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ, ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ, ਇੰਟੈਲੀਜੇ, ਇਕਲਿਪਸ, ਪਾਈਚਾਰਮ, ਜਾਂ ਕੋਈ ਵੀ ਆਧੁਨਿਕ ਕੋਡ ਸੰਪਾਦਕ
- **ਪੈਕੇਜ ਮੈਨੇਜਰ**: NuGet, Maven/Gradle, pip, npm/yarn, ਜਾਂ Cargo
- **API ਕੁੰਜੀਆਂ**: ਕਿਸੇ ਵੀ AI ਸੇਵਾਵਾਂ ਲਈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ

## ਬੁਨਿਆਦੀ MCP ਸਰਵਰ ਸੰਰਚਨਾ

ਇੱਕ MCP ਸਰਵਰ ਆਮ ਤੌਰ 'ਤੇ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ:

- **ਸਰਵਰ ਸੰਰਚਨਾ**: ਪੋਰਟ, ਪ੍ਰਮਾਣਿਕਤਾ, ਅਤੇ ਹੋਰ ਸੈਟਿੰਗਜ਼ ਸੈਟਅਪ ਕਰਨਾ
- **ਸਰੋਤ**: LLMs ਲਈ ਉਪਲਬਧ ਡਾਟਾ ਅਤੇ ਸੰਦਰਭ
- **ਟੂਲ**: ਉਹ ਫੰਕਸ਼ਨਲਿਟੀ ਜੋ ਮਾਡਲ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ
- **ਪ੍ਰਾਂਪਟ**: ਟੈਕਸਟ ਬਣਾਉਣ ਜਾਂ ਸੰਰਚਿਤ ਕਰਨ ਲਈ ਟੈਮਪਲੇਟ

ਇੱਥੇ ਟਾਈਪਸਕ੍ਰਿਪਟ ਵਿੱਚ ਇੱਕ ਸਧਾਰਣ ਉਦਾਹਰਨ ਹੈ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ਇੱਕ ਜੋੜਣ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਵਾਗਤ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ
server.resource(
  "file",
  // 'list' ਪੈਰਾਮੀਟਰ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਸਰੋਤ ਉਪਲਬਧ ਫਾਈਲਾਂ ਨੂੰ ਕਿਵੇਂ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ। ਇਸਨੂੰ undefined ਤੇ ਸੈੱਟ ਕਰਨ ਨਾਲ ਇਸ ਸਰੋਤ ਲਈ ਸੂਚੀਬੱਧ ਕਰਨਾ ਅਯੋਗ ਹੋ ਜਾਂਦਾ ਹੈ।
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ਇੱਕ ਫਾਈਲ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਫਾਈਲ ਸਮੱਗਰੀ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ
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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਟਾਈਪਸਕ੍ਰਿਪਟ SDK ਤੋਂ ਜਰੂਰੀ ਕਲਾਸਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕੀਤਾ।
- ਇੱਕ ਨਵਾਂ MCP ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਇਆ ਅਤੇ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਇੱਕ ਕਸਟਮ ਟੂਲ (`calculator`) ਨੂੰ ਹੈਂਡਲਰ ਫੰਕਸ਼ਨ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ।
- ਆਉਣ ਵਾਲੀਆਂ MCP ਬੇਨਤੀਆਂ ਲਈ ਸਰਵਰ ਨੂੰ ਸੁਣਨ ਲਈ ਸ਼ੁਰੂ ਕੀਤਾ।

## ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ

ਆਪਣਾ MCP ਸਰਵਰ ਟੈਸਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਉਪਲਬਧ ਟੂਲਾਂ ਅਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਅਭਿਆਸਾਂ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ। ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਟੈਸਟਿੰਗ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਤੁਹਾਡਾ ਸਰਵਰ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਤੁਹਾਨੂੰ ਜਲਦੀ ਸਮੱਸਿਆਵਾਂ ਦੀ ਪਹਿਚਾਣ ਅਤੇ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਭਾਗ ਤੁਹਾਡੇ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕੇ ਦਰਸਾਉਂਦਾ ਹੈ।

MCP ਤੁਹਾਡੇ ਸਰਵਰਾਂ ਦੀ ਜਾਂਚ ਅਤੇ ਡੀਬੱਗਿੰਗ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ ਟੂਲ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

- **ਇੰਸਪੈਕਟਰ ਟੂਲ**, ਇਹ ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਆਪਣੇ ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਅਤੇ ਆਪਣੇ ਟੂਲ, ਪ੍ਰਾਂਪਟ ਅਤੇ ਸਰੋਤਾਂ ਦੀ ਜਾਂਚ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- **curl**, ਤੁਸੀਂ curl ਜਾਂ ਹੋਰ ਕਮਾਂਡ ਲਾਈਨ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵੀ ਆਪਣੇ ਸਰਵਰ ਨਾਲ ਜੁੜ ਸਕਦੇ ਹੋ ਜੋ HTTP ਕਮਾਂਡ ਬਣਾਉਂਦੇ ਅਤੇ ਚਲਾਉਂਦੇ ਹਨ।

### MCP ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ

[MCP ਇੰਸਪੈਕਟਰ](https://github.com/modelcontextprotocol/inspector) ਇੱਕ ਵਿਜ਼ੂਅਲ ਟੈਸਟਿੰਗ ਟੂਲ ਹੈ ਜੋ ਤੁਹਾਡੀ ਮਦਦ ਕਰਦਾ ਹੈ:

1. **ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਖੋਜ**: ਉਪਲਬਧ ਸਰੋਤ, ਟੂਲ, ਅਤੇ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਪਤਾ ਲਗਾਓ
2. **ਟੂਲ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਦੀ ਜਾਂਚ**: ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਅਤੇ ਤੁਰੰਤ ਜਵਾਬ ਵੇਖੋ
3. **ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਵੇਖੋ**: ਸਰਵਰ ਜਾਣਕਾਰੀ, ਸਕੀਮਾਂ, ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ

```bash
# ਉਦਾਹਰਨ ਲਈ TypeScript, MCP ਇੰਸਪੈਕਟਰ ਨੂੰ ਇੰਸਟਾਲ ਅਤੇ ਚਲਾਉਣਾ
npx @modelcontextprotocol/inspector node build/index.js
```

ਜਦੋਂ ਤੁਸੀਂ ਉਪਰੋਕਤ ਕਮਾਂਡ ਚਲਾਉਂਦੇ ਹੋ, MCP ਇੰਸਪੈਕਟਰ ਤੁਹਾਡੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਇੱਕ ਸਥਾਨਕ ਵੈੱਬ ਇੰਟਰਫੇਸ ਸ਼ੁਰੂ ਕਰੇਗਾ। ਤੁਸੀਂ ਆਪਣੇ ਰਜਿਸਟਰਡ MCP ਸਰਵਰਾਂ, ਉਨ੍ਹਾਂ ਦੇ ਉਪਲਬਧ ਟੂਲਾਂ, ਸਰੋਤਾਂ ਅਤੇ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਡੈਸ਼ਬੋਰਡ ਦੇਖ ਸਕਦੇ ਹੋ। ਇਹ ਇੰਟਰਫੇਸ ਤੁਹਾਨੂੰ ਟੂਲ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਦੀ ਇੰਟਰਐਕਟਿਵ ਜਾਂਚ ਕਰਨ, ਸਰਵਰ ਮੈਟਾਡੇਟਾ ਦੀ ਜਾਂਚ ਕਰਨ ਅਤੇ ਤੁਰੰਤ ਜਵਾਬ ਵੇਖਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਹਾਡੇ MCP ਸਰਵਰ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਦੀ ਪੁਸ਼ਟੀ ਅਤੇ ਡੀਬੱਗਿੰਗ ਆਸਾਨ ਹੋ ਜਾਂਦੀ ਹੈ।

ਇੱਥੇ ਇਸਦਾ ਇੱਕ ਸਕ੍ਰੀਨਸ਼ਾਟ ਹੈ:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.pa.png)

## ਆਮ ਸੈਟਅਪ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

| ਸਮੱਸਿਆ | ਸੰਭਾਵਿਤ ਹੱਲ |
|-------|-------------------|
| ਕਨੈਕਸ਼ਨ ਰੱਦ ਕੀਤਾ ਗਿਆ | ਜਾਂਚੋ ਕਿ ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ ਅਤੇ ਪੋਰਟ ਸਹੀ ਹੈ |
| ਟੂਲ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਵਿੱਚ ਗਲਤੀਆਂ | ਪੈਰਾਮੀਟਰ ਵੈਰੀਫਿਕੇਸ਼ਨ ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ ਦੀ ਸਮੀਖਿਆ ਕਰੋ |
| ਪ੍ਰਮਾਣਿਕਤਾ ਅਸਫਲ | API ਕੁੰਜੀਆਂ ਅਤੇ ਅਧਿਕਾਰਾਂ ਦੀ ਜਾਂਚ ਕਰੋ |
| ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਗਲਤੀਆਂ | ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਪੈਰਾਮੀਟਰ ਪਰਿਭਾਸ਼ਿਤ ਸਕੀਮਾ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ |
| ਸਰਵਰ ਸ਼ੁਰੂ ਨਹੀਂ ਹੋ ਰਿਹਾ | ਪੋਰਟ ਟਕਰਾਅ ਜਾਂ ਗੁੰਮ ਹੋਈਆਂ ਨਿਰਭਰਤਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ |
| CORS ਗਲਤੀਆਂ | ਕ੍ਰਾਸ-ਓਰੀਜਿਨ ਬੇਨਤੀਆਂ ਲਈ ਠੀਕ CORS ਹੈਡਰ ਸੰਰਚਿਤ ਕਰੋ |
| ਪ੍ਰਮਾਣਿਕਤਾ ਸਮੱਸਿਆਵਾਂ | ਟੋਕਨ ਦੀ ਵੈਧਤਾ ਅਤੇ ਅਧਿਕਾਰਾਂ ਦੀ ਜਾਂਚ ਕਰੋ |

## ਸਥਾਨਕ ਵਿਕਾਸ

ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ, ਤੁਸੀਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਸਿੱਧਾ ਆਪਣੇ ਮਸ਼ੀਨ 'ਤੇ ਚਲਾ ਸਕਦੇ ਹੋ:

1. **ਸਰਵਰ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰੋ**: ਆਪਣੀ MCP ਸਰਵਰ ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ
2. **ਨੈੱਟਵਰਕਿੰਗ ਸੰਰਚਿਤ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ ਉਮੀਦ ਕੀਤੇ ਪੋਰਟ 'ਤੇ ਪਹੁੰਚਯੋਗ ਹੈ
3. **ਕਲਾਇੰਟਾਂ ਨੂੰ ਜੁੜੋ**: ਸਥਾਨਕ ਕਨੈਕਸ਼ਨ URL ਵਰਗੇ `http://localhost:3000` ਦੀ ਵਰਤੋਂ ਕਰੋ

```bash
# ਉਦਾਹਰਨ: ਟਾਈਪਸਕ੍ਰਿਪਟ MCP ਸਰਵਰ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚਲਾਉਣਾ
npm run start
# ਸਰਵਰ http://localhost:3000 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੈ
```

## ਆਪਣਾ ਪਹਿਲਾ MCP ਸਰਵਰ ਬਣਾਉਣਾ

ਅਸੀਂ ਪਹਿਲਾਂ ਦੇ ਪਾਠ ਵਿੱਚ [ਮੁੱਖ ਧਾਰਣਾਵਾਂ](/01-CoreConcepts/README.md) ਨੂੰ ਕਵਰ ਕੀਤਾ ਹੈ, ਹੁਣ ਸਮਾਂ ਹੈ ਕਿ ਉਸ ਗਿਆਨ ਨੂੰ ਅਮਲ ਵਿੱਚ ਲਿਆਈਏ।

### ਇੱਕ ਸਰਵਰ ਕੀ ਕਰ ਸਕਦਾ ਹੈ

ਕੋਡ ਲਿਖਣਾ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਆਓ ਯਾਦ ਕਰੀਏ ਕਿ ਇੱਕ ਸਰਵਰ ਕੀ ਕਰ ਸਕਦਾ ਹੈ:

ਇੱਕ MCP ਸਰਵਰ ਉਦਾਹਰਨ ਵਜੋਂ:

- ਸਥਾਨਕ ਫਾਈਲਾਂ ਅਤੇ ਡੇਟਾਬੇਸਾਂ ਤੱਕ ਪਹੁੰਚ ਕਰ ਸਕਦਾ ਹੈ
- ਦੂਰੇ API ਨਾਲ ਜੁੜ ਸਕਦਾ ਹੈ
- ਗਣਨਾਵਾਂ ਕਰ ਸਕਦਾ ਹੈ
- ਹੋਰ ਟੂਲਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰ ਸਕਦਾ ਹੈ
- ਇੰਟਰਐਕਸ਼ਨ ਲਈ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹੈ

ਵਧੀਆ, ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਜਾਣਦੇ ਹਾਂ ਕਿ ਇਹ ਕੀ ਕਰ ਸਕਦਾ ਹੈ, ਆਓ ਕੋਡਿੰਗ ਸ਼ੁਰੂ ਕਰੀਏ।

## ਅਭਿਆਸ: ਇੱਕ ਸਰਵਰ ਬਣਾਉਣਾ

ਸਰਵਰ ਬਣਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਇਹ ਕਦਮ ਫਾਲੋ ਕਰਨੇ ਪੈਣਗੇ:

- MCP SDK ਇੰਸਟਾਲ ਕਰੋ।
- ਇੱਕ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ ਅਤੇ ਪ੍ਰੋਜੈਕਟ ਸੰਰਚਨਾ ਸੈਟਅਪ ਕਰੋ।
- ਸਰਵਰ ਕੋਡ ਲਿਖੋ।
- ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ।

### -1- ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```sh
# ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ ਅਤੇ npm ਪ੍ਰੋਜੈਕਟ ਸ਼ੁਰੂ ਕਰੋ
mkdir calculator-server
cd calculator-server
npm init -y
```

#### ਪਾਇਥਨ

```sh
# ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ
mkdir calculator-server
cd calculator-server
# ਫੋਲਡਰ ਨੂੰ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ ਵਿੱਚ ਖੋਲ੍ਹੋ - ਜੇ ਤੁਸੀਂ ਕੋਈ ਹੋਰ IDE ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ ਇਸਨੂੰ ਛੱਡ ਦਿਓ
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### ਜਾਵਾ

ਜਾਵਾ ਲਈ, ਇੱਕ ਸਪ੍ਰਿੰਗ ਬੂਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ:

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

ਜ਼ਿਪ ਫਾਈਲ ਨੂੰ ਅਨਜ਼ਿਪ ਕਰੋ:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ਵਿਕਲਪਿਕ ਤੌਰ 'ਤੇ ਅਣਵਰਤੇ ਟੈਸਟ ਨੂੰ ਹਟਾਓ
rm -rf src/test/java
```

ਆਪਣੇ *pom.xml* ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਪੂਰੀ ਸੰਰਚਨਾ ਸ਼ਾਮਲ ਕਰੋ:

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

#### ਰਸਟ

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- ਨਿਰਭਰਤਾਵਾਂ ਸ਼ਾਮਲ ਕਰੋ

ਹੁਣ ਜਦੋਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਬਣ ਗਿਆ ਹੈ, ਆਓ ਨਿਰਭਰਤਾਵਾਂ ਸ਼ਾਮਲ ਕਰੀਏ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```sh
# ਜੇ ਪਹਿਲਾਂ ਹੀ ਇੰਸਟਾਲ ਨਾ ਹੋਵੇ, ਤਾਂ ਟਾਈਪਸਕ੍ਰਿਪਟ ਨੂੰ ਗਲੋਬਲੀ ਇੰਸਟਾਲ ਕਰੋ
npm install typescript -g

# ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ MCP SDK ਅਤੇ Zod ਇੰਸਟਾਲ ਕਰੋ
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### ਪਾਇਥਨ

```sh
# ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਨਿਰਭਰਤਾਵਾਂ ਇੰਸਟਾਲ ਕਰੋ
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### ਜਾਵਾ

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### ਰਸਟ

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- ਪ੍ਰੋਜੈਕਟ ਫਾਈਲਾਂ ਬਣਾਓ

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

*package.json* ਫਾਈਲ ਖੋਲ੍ਹੋ ਅਤੇ ਸਰਵਰ ਨੂੰ ਬਣਾਉਣ ਅਤੇ ਚਲਾਉਣ ਯੋਗ ਬਣਾਉਣ ਲਈ ਸਮੱਗਰੀ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਨਾਲ ਬਦਲੋ:

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

*tsconfig.json* ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਸਮੱਗਰੀ ਹੋਵੇ:

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

ਆਪਣੇ ਸਰੋਤ ਕੋਡ ਲਈ ਇੱਕ ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ:

```sh
mkdir src
touch src/index.ts
```

#### ਪਾਇਥਨ

*server.py* ਫਾਈਲ ਬਣਾਓ

```sh
touch server.py
```

#### .NET

ਲੋੜੀਂਦੇ NuGet ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### ਜਾਵਾ

ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ ਪ੍ਰੋਜੈਕਟਾਂ ਲਈ, ਪ੍ਰੋਜੈਕਟ ਸੰਰਚਨਾ ਆਪਣੇ ਆਪ ਬਣ ਜਾਂਦੀ ਹੈ।

#### ਰਸਟ

ਰਸਟ ਲਈ, ਜਦੋਂ ਤੁਸੀਂ `cargo init` ਚਲਾਉਂਦੇ ਹੋ ਤਾਂ *src/main.rs* ਫਾਈਲ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਬਣ ਜਾਂਦੀ ਹੈ। ਫਾਈਲ ਖੋਲ੍ਹੋ ਅਤੇ ਡਿਫਾਲਟ ਕੋਡ ਹਟਾ ਦਿਓ।

### -4- ਸਰਵਰ ਕੋਡ ਬਣਾਓ

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

*index.ts* ਫਾਈਲ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਸਰਵਰ ਹੈ, ਪਰ ਇਹ ਜ਼ਿਆਦਾ ਕੁਝ ਨਹੀਂ ਕਰਦਾ, ਆਓ ਇਸਨੂੰ ਠੀਕ ਕਰੀਏ।

#### ਪਾਇਥਨ

```python
# server.py
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

#### ਜਾਵਾ

ਜਾਵਾ ਲਈ, ਮੁੱਖ ਸਰਵਰ ਕੰਪੋਨੈਂਟ ਬਣਾਓ। ਪਹਿਲਾਂ, ਮੁੱਖ ਐਪਲੀਕੇਸ਼ਨ ਕਲਾਸ ਨੂੰ ਸੋਧੋ:

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

ਕੈਲਕੂਲੇਟਰ ਸੇਵਾ ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ਉਤਪਾਦਨ-ਤਿਆਰ ਸੇਵਾ ਲਈ ਵਿਕਲਪਿਕ ਕੰਪੋਨੈਂਟ:**

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

ਇਕਸੈਪਸ਼ਨ ਹੈਂਡਲਰ ਬਣਾਓ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // ਗੈਟਰਸ
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

#### ਰਸਟ

*src/main.rs* ਫਾਈਲ ਦੇ ਸਿਰਲੇਖ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ। ਇਹ ਤੁਹਾਡੇ MCP ਸਰਵਰ ਲਈ ਜਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਅਤੇ ਮੋਡੀਊਲਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦਾ ਹੈ।

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

ਕੈਲਕੂਲੇਟਰ ਸਰਵਰ ਇੱਕ ਸਧਾਰਣ ਸਰਵਰ ਹੋਵੇਗਾ ਜੋ ਦੋ ਨ
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

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.pa.png)

**You're now connected to the server**
**The Java server testing section is completed now**

The next section it's about interacting with the server.

You should see the following user interface:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.pa.png)

1. Connect to the server by selecting the Connect button
  Once you connect to the server, you should now see the following:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.pa.png)

1. Select "Tools" and "listTools", you should see "Add" show up, select "Add" and fill in the parameter values.

  You should see the following response, i.e a result from "add" tool:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.pa.png)

Congrats, you've managed to create and run your first server!

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
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
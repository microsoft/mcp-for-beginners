## Getting Started  

[![Build Your First MCP Server](../../../translated_images/pa/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(ਇਸ ਪਾਠ ਦੇ ਵੀਡੀਓ ਨੂੰ ਵੇਖਣ ਲਈ ਉੱਪਰ ਦੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

ਇਹ ਭਾਗ ਕਈ ਪਾਠਾਂ 'ਤੇ مشتمل ਹੈ:

- **1 ਤੁਹਾਡਾ ਪਹਿਲਾ ਸਰਵਰ**, ਇਸ ਪਹਿਲੇ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਕਿਵੇਂ ਆਪਣਾ ਪਹਿਲਾ ਸਰਵਰ ਬਣਾਇਆ ਜਾਵੇ ਅਤੇ ਇਸਨੂੰ ਇੰਸਪੈਕਟਰ ਟੂਲ ਨਾਲ ਜਾਂਚਿਆ ਜਾਵੇ, ਜੋ ਸਰਵਰ ਦੀ ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ ਦਾ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਤਰੀਕਾ ਹੈ, [ਪਾਠ ਵੱਲ](01-first-server/README.md)

- **2 ਕਲਾਇੰਟ**, ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਕਿਵੇਂ ਇੱਕ ਕਲਾਇੰਟ ਲਿਖਿਆ ਜਾਵੇ ਜੋ ਤੁਹਾਡੇ ਸਰਵਰ ਨਾਲ ਜੁੜ ਸਕੇ, [ਪਾਠ ਵੱਲ](02-client/README.md)

- **3 LLM ਨਾਲ ਕਲਾਇੰਟ**, ਇੱਕ ਹੋਰ ਵਧੀਆ ਤਰੀਕਾ ਹੈ ਕਿ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਜੋੜ ਕੇ ਤੁਸੀਂ ਆਪਣੇ ਸਰਵਰ ਨਾਲ "ਬਾਤ ਕੀਤੀ" ਜਾ ਸਕਦੀ ਹੈ ਕਿ ਕੀ ਕਰਨਾ ਹੈ, [ਪਾਠ ਵੱਲ](03-llm-client/README.md)

- **4 Visual Studio Code ਵਿੱਚ GitHub Copilot ਏਜੰਟ ਮੋਡ ਨਾਲ ਸਰਵਰ ਦੀ ਵਰਤੋਂ**। ਇੱਥੇ ਅਸੀਂ Visual Studio Code ਵਿੱਚੋਂ ਆਪਣਾ MCP ਸਰਵਰ ਚਲਾਉਣ ਬਾਰੇ ਵੇਖ ਰਹੇ ਹਾਂ, [ਪਾਠ ਵੱਲ](04-vscode/README.md)

- **5 stdio ਟ੍ਰਾਂਸਪੋਰਟ ਸਰਵਰ** stdio ਟ੍ਰਾਂਸਪੋਰਟ ਸਥਾਨਕ MCP ਸਰਵਰ-ਤੋਂ-ਕਲਾਇੰਟ ਸੰਚਾਰ ਲਈ ਸਿਫਾਰਸ਼ੀ ਮਿਯਾਰ ਹੈ, ਜੋ ਸੁਰੱਖਿਅਤ subprocess-ਆਧਾਰਿਤ ਸੰਚਾਰ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਇਂਬਿਲਟ ਪ੍ਰੋਸੈਸ ਆਇਸੋਲੇਸ਼ਨ ਨਾਲ ਕਈ [ਪਾਠ ਵੱਲ](05-stdio-server/README.md)

- **6 MCP ਨਾਲ HTTP ਸਟ੍ਰੀਮਿੰਗ (Streamable HTTP)**। ਆਧੁਨਿਕ HTTP ਸਟ੍ਰੀਮਿੰਗ ਟ੍ਰਾਂਸਪੋਰਟ ਬਾਰੇ ਜਾਣੋ (ਜੋ ਦੂਰੇ MCP ਸਰਵਰਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਹੈ, ਮਾਡਲ ਕੰਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ 2025-11-25 [MCP Specification](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http) ਦੇ ਅਨੁਸਾਰ), ਪ੍ਰਗਤਿ ਸੂਚਨਾਵਾਂ ਅਤੇ ਕਿਵੇਂ Streamable HTTP ਦੀ ਵਰਤੋਂ ਨਾਲ ਸਕੇਲਬਲ, ਰੀਅਲ-ਟਾਈਮ MCP ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਬਣਾਏ ਜਾਣ, [ਪਾਠ ਵੱਲ](06-http-streaming/README.md)

- **7 VSCode ਲਈ AI ਟੂਲਕਿਟ ਦੀ ਵਰਤੋਂ** MCP ਕਲਾਇੰਟ ਅਤੇ ਸਰਵਰਾਂ ਦੀ ਖਪਤ ਅਤੇ ਟੈਸਟ ਕਰਨ ਲਈ [ਪਾਠ ਵੱਲ](07-aitk/README.md)

- **8 Testing**। ਇੱਥੇ ਅਸੀਂ ਖਾਸ ਕਰਕੇ ਵੇਖਾਂਗੇ ਕਿ ਕਿਸ ਤਰੀਕੇ ਨਾਲ ਆਪਣਾ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਨਾਲ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹਾਂ, [ਪਾਠ ਵੱਲ](08-testing/README.md)

- **9 Deployment**। ਇਹ ਅਧਿਆਇ MCP ਹੱਲਾਂ ਦੇ ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਨਾਲ ਡਿਪਲੌਇ ਕਰਨ ਬਾਰੇ ਹੈ, [ਪਾਠ ਵੱਲ](09-deployment/README.md)

- **10 Advanced server usage**। ਇਹ ਅਧਿਆਇ ਉੱਚ-ਸਤਹ ਦਾ ਸਰਵਰ ਉਪਯੋਗ ਕਵਰ ਕਰਦਾ ਹੈ, [ਪਾਠ ਵੱਲ](./10-advanced/README.md)

- **11 Auth**। ਇਹ ਅਧਿਆਇ ਸਧਾਰਣ ਪ੍ਰਮਾਣਿਕਤਾ ਸ਼ਾਮਲ ਕਰਨ ਬਾਰੇ ਹੈ, ਬੇਸਿਕ ਆਥ ਤੋ JWT ਅਤੇ RBAC ਦੀ ਵਰਤੋਂ ਤੱਕ। ਤੁਹਾਨੂੰ ਇੱਥੇ ਸ਼ੁਰੂ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਫਿਰ ਅਧਿਆਇ 5 ਵਿੱਚ ਆਧੁਨਿਕ ਵਿਸ਼ੇਖ ਬਾਰੇ ਵੇਖਣ ਅਤੇ ਅਧਿਆਇ 2 ਵਿੱਚ ਸਿਫਾਰਸ਼ਾਂ ਅਨੁਸਾਰ ਵਾਧੂ ਸੁਰੱਖਿਆ ਕਦਮ ਲੈਣੇ, [ਪਾਠ ਵੱਲ](./11-simple-auth/README.md)

- **12 MCP Hosts**। ਪ੍ਰਸਿੱਧ MCP ਹੋਸਟ ਕਲਾਇੰਟਾਂ ਦਾ ਸੰਰਚਨਾ ਅਤੇ ਵਰਤੋਂ ਜਿਵੇਂ Claude Desktop, Cursor, Cline, ਅਤੇ Windsurf। ਟ੍ਰਾਂਸਪੋਰਟ ਕਿਸਮਾਂ ਅਤੇ ਸਮੱਸਿਆ ਹੱਲ ਬਾਰੇ ਜਾਣੋ, [ਪਾਠ ਵੱਲ](./12-mcp-hosts/README.md)

- **13 MCP Inspector**। MCP ਇੰਸਪੈਕਟਰ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ MCP ਸਰਵਰਾਂ ਦਾ ਅੰਤਰੇਕਟਿਵ ਡੀਬੱਗ ਅਤੇ ਟੈਸਟ ਕਰੋ। ਟੂਲਾਂ, ਸਰੋਤਾਂ ਅਤੇ ਪ੍ਰੋਟੋਕੋਲ ਸੁਨੇਹਿਆਂ ਦੀ ਜाँच ਸਿੱਖੋ, [ਪਾਠ ਵੱਲ](./13-mcp-inspector/README.md)

- **14 Sampling**। MCP ਸਰਵਰ ਬਣਾਓ ਜੋ MCP ਕਲਾਇੰਟਾਂ ਨਾਲ LLM ਸੰਬੰਧਿਤ ਕਾਰਜਾਂ 'ਤੇ ਸਹਿਯੋਗ ਕਰਦੇ ਹਨ। [ਪਾਠ ਵੱਲ](./14-sampling/README.md)

- **15 MCP Apps**। MCP ਸਰਵਰ ਬਣਾਓ ਜੋ UI ਹਦਾਇਤਾਂ ਨਾਲ ਵੀ ਜਵਾਬ ਦੇਂਦੇ ਹਨ, [ਪਾਠ ਵੱਲ](./15-mcp-apps/README.md)

ਮਾਡਲ ਕੰਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੱਕ ਖੁੱਲਾ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ LLM ਲਈ ਸੰਦਰਭ ਪ੍ਰਦਾਨ ਕਰਨ ਦਾ ਮਿਆਰ ਬਣਾਉਂਦਾ ਹੈ। MCP ਨੂੰ ਇੱਕ USB-C ਪੋਰਟ ਵਾਂਗ ਸੋਚੋ ਜੋ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਡੇਟਾ ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਨਾਲ ਜੁੜਨ ਦਾ ਮਿਆਰੀ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਮੁੱਖ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- C#, Java, Python, TypeScript, ਅਤੇ JavaScript ਵਿੱਚ MCP ਲਈ ਵਿਕਾਸ ਦਾ ਵਾਤਾਵਰਨ ਸੈਟਅਪ ਕਰਨਾ
- ਕਸਟਮ ਫੀਚਰ (ਸਰੋਤ, ਪ੍ਰਾਂਪਟ, ਅਤੇ ਟੂਲ) ਨਾਲ ਬੁਨਿਆਦੀ MCP ਸਰਵਰ ਬਣਾਉਣਾ ਅਤੇ ਡਿਪਲੌਇ ਕਰਨਾ
- MCP ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਨ ਵਾਲੀਆਂ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਸਿਰਜਣਾ ਕਰਨਾ
- MCP ਇੰਪਲੀਮੇੰਟੇਸ਼ਨਾਂ ਦੀ ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ ਕਰਨਾ
- ਆਮ ਸੈਟਅਪ ਚੁਣੌਤੀਆਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਹੱਲਾਂ ਨੂੰ ਸਮਝਣਾ
- ਆਪਣੇ MCP ਇੰਪਲੀਮੇੰਟੇਸ਼ਨਾਂ ਨੂੰ ਪ੍ਰਸਿੱਧ LLM ਸੇਵਾਵਾਂ ਨਾਲ ਜੁੜਨ ਲਈ

## ਆਪਣੇ MCP ਵਾਤਾਵਰਨ ਦੀ ਸੈਟਅਪਿੰਗ

MCP ਨਾਲ ਕੰਮ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਆਪਣਾ ਵਿਕਾਸ ਵਾਤਾਵਰਨ ਤਿਆਰ ਕਰਨਾ ਅਤੇ ਬੁਨਿਆਦੀ ਵਰਕਫਲੋ ਨੂੰ ਸਮਝਣਾ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਇਹ ਭਾਗ ਤੁਹਾਨੂੰ ਸ਼ੁਰੂਆਤੀ ਸੈਟਅਪ ਕਦਮਾਂ ਦੇ ਰਾਹ ਦਰਸਾਏਗਾ ਤਾਂ ਜੋ MCP ਨਾਲ ਸੁਚਾਰੂ ਸ਼ੁਰੂਆਤ ਹੋ ਸਕੇ।

### ਲੋੜੀਂਦੇ ਗੁਣ

MCP ਵਿਕਾਸ ਵਿੱਚ ਡੁਬਕੇ ਲਗਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹਨਾਂ ਚੀਜ਼ਾਂ ਦੀ ਯਕੀਨਦਾਰੀ ਕਰੋ:

- **ਵਿਕਾਸ ਵਾਤਾਵਰਨ**: ਤੁਹਾਡੇ ਚੁਣੇ ਭਾਸ਼ਾ (C#, Java, Python, TypeScript, ਜਾਂ JavaScript) ਲਈ
- **IDE/ਸੰਪਾਦਕ**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, ਜਾਂ ਕੋਈ ਵੀ ਆਧੁਨਿਕ ਕੋਡ ਸੰਪਾਦਕ
- **ਪੈਕੇਜ ਮੈਨੇਜਰ**: NuGet, Maven/Gradle, pip, ਜਾਂ npm/yarn
- **API ਕੁੰਜੀਆਂ**: ਕਿਸੇ ਵੀ AI ਸੇਵਾਵਾਂ ਲਈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ


### ਅਧਿਕਾਰਤ SDKs

ਅਗਲੇ ਅਧਿਆਇਆਂ ਵਿੱਚ ਤੁਸੀਂ Python, TypeScript, Java ਅਤੇ .NET ਦੀ ਵਰਤੋਂ ਨਾਲ ਬਣੀਆਂ ਹੱਲਾਂ ਵੇਖੋਗੇ। ਇੱਥੇ ਸਾਰੇ ਅਧਿਕਾਰਤ ਸਹਾਇਤਾਕਾਰ SDKs ਦਿੱਤੇ ਗਏ ਹਨ।

MCP ਵੱਖ-ਵੱਖ ਭਾਸ਼ਾਵਾਂ ਲਈ ਅਧਿਕਾਰਤ SDKs ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ (ਜੋ [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) ਦੇ ਅਨੁਕੂਲ ਹਨ):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - ਮਾਈਕ੍ਰੋਸਾਫ਼ਟ ਨਾਲ ਸਹਿਯੋਗ ਵਿੱਚ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ਨਾਲ ਸਹਿਯੋਗ ਵਿੱਚ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - ਅਧਿਕਾਰਤ TypeScript ਟੂਲ
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - ਅਧਿਕਾਰਤ Python ਟੂਲ (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - ਅਧਿਕਾਰਤ Kotlin ਟੂਲ
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI ਨਾਲ ਸਹਿਯੋਗ ਵਿੱਚ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - ਅਧਿਕਾਰਤ Rust ਟੂਲ
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - ਅਧਿਕਾਰਤ Go ਟੂਲ

## ਪ੍ਰਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀ ਗੱਲਾਂ

- MCP ਵਿਕਾਸ ਵਾਤਾਵਰਨ ਸੈਟਅਪ ਕਰਨਾ ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ SDKs ਨਾਲ ਸੁਗਮ ਹੈ
- MCP ਸਰਵਰ ਬਣਾਉਣ ਵਿੱਚ ਟੂਲਾਂ ਨੂੰ ਸਪਸ਼ਟ schema ਨਾਲ ਬਣਾਉਣਾ ਅਤੇ ਰਜਿਸਟਰ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ
- MCP ਕਲਾਇੰਟ ਸਰਵਰਾਂ ਅਤੇ ਮਾਡਲਾਂ ਨਾਲ ਜੁੜ ਕੇ ਵਧੀਆ ਸਮਰੱਥਾ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ
- ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ MCP ਇੰਪਲੀਮੇੰਟੇਸ਼ਨ ਲਈ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹਨ
- ਡਿਪਲੌਇਮੈਂਟ ਦੇ ਵਿਕਲਪ ਸਥਾਨਕ ਵਿਕਾਸ ਤੋਂ ਲੈ ਕੇ ਕਲਾਉਡ ਅਧਾਰਿਤ ਹੱਲਾਂ ਤੱਕ ਹਨ

## ਅਭਿਆਸ

ਸਾਡੇ ਕੋਲ ਕੁਝ ਨਮੂਨੇ ਹਨ ਜੋ ਇਸ ਭਾਗ ਦੇ ਸਾਰੇ ਅਧਿਆਇਆਂ ਵਿੱਚ ਦਿੱਤੇ ਅਭਿਆਸਾਂ ਨੂੰ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ। ਹਰ ਅਧਿਆਇ ਵਿੱਚ ਵੀ ਆਪਣੀ ਅਲੱਗ ਅਭਿਆਸਾਂ ਅਤੇ ਕਰਤੱਬ ਹਨ

- [Java ਕੈਲਕੂਲੇਟਰ](./samples/java/calculator/README.md)
- [.Net ਕੈਲਕੂਲੇਟਰ](../../../03-GettingStarted/samples/csharp)
- [JavaScript ਕੈਲਕੂਲੇਟਰ](./samples/javascript/README.md)
- [TypeScript ਕੈਲਕੂਲੇਟਰ](./samples/typescript/README.md)
- [Python ਕੈਲਕੂਲੇਟਰ](../../../03-GettingStarted/samples/python)

## ਵਾਧੂ ਸਰੋਤ

- [Azure ਉੱਤੇ ਮਾਡਲ ਕੰਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਏਜੰਟ ਬਣਾਓ](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps ਨਾਲ ਰਿਮੋਟ MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ਏਜੰਟ](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## ਅੱਗੇ ਕੀ ਹੈ

ਪਹਿਲੇ ਪਾਠ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ: [ਆਪਣਾ ਪਹਿਲਾ MCP ਸਰਵਰ ਬਣਾਉਣਾ](01-first-server/README.md)

ਇਸ ਮੋਡੀਊਲ ਨੂੰ ਪੂਰਾ ਕਰ ਲੈਣ ਤੋਂ ਬਾਅਦ, ਜਾਰੀ ਰੱਖੋ: [ਮੋਡੀਊਲ 4: ਪ੍ਰਯੋਗਿਕ ਲਾਗੂ ਕਰਨ](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਸੂਚਿਤ ਰਹੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਤਰਟੀਆਂ ਜਾਂ ਗਲਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕ੍ਰਿਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਪੈਦਾਹ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ्रामਕ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
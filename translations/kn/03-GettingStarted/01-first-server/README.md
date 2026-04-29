# MCP ಜೊತೆ ಆರಂಭಿಸುವುದು

ನಿಮ್ಮ ಮೊದಲ ಹೆಜ್ಜೆಗಳಿಗೆ ಸ್ವಾಗತ, ಮಾದರಿ ಕಾಂಟೆಕ್ಸ್ಟ್ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಜೊತೆಗೆ! ನೀವು MCP ಗಾಗಿ ಹೊಸದಾಗಿದ್ದೀರಾ ಅಥವಾ ನಿಮ್ಮ ತಿಳಿವಳಿಕೆಯನ್ನು ಗಾಢಗೊಳಿಸಲು ಬಯಸುತ್ತಿದ್ದೀರಾ, ಈ ಮಾರ್ಗದರ್ಶಿ ಮುಖ್ಯ ಪರಿಸರ ಮತ್ತು ಅಭಿವೃದ್ಧಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ನಿಮಗೆ ತಿಳಿಸುತ್ತದೆ. MCP ಹೇಗೆ AI ಮಾದರಿಗಳು ಮತ್ತು ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ನಡುವೆ ಸುಗಮ ಸಂಯೋಜನೆಯನ್ನು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ ಎಂದು ನೀವು ಕಂಡುಕೊಳ್ಳುತ್ತೀರಿ ಮತ್ತು ನಿಮ್ಮ ಪರಿಸರವನ್ನು ವೇಗವಾಗಿ ಸಿದ್ಧಪಡಿಸುವ ಮೂಲಕ MCP-ಚಾಲಿತ ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸುವ ಮತ್ತು ಪರೀಕ್ಷಿಸುವ ವಿಧಾನವನ್ನು ತಿಳಿದುಕೊಳ್ಳುತ್ತೀರಿ.

> TLDR; ನೀವು AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವಾಗ, LLM (ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿ) ಗೆ ಸಾಧನಗಳು ಮತ್ತು ಇತರ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸೇರಿಸಬಹುದು, ಇದರಿಂದ LLM ಹೆಚ್ಚು ಜ್ಞಾನ ಹೊಂದಿರುತ್ತದೆ. ಆದಾಗ್ಯೂ ನೀವು ಆ ಸಾಧನಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸರ್ವರ್ ಮೇಲೆ ಇಡಿದರೆ, ಆ ಅಪ್ಲಿಕೇಶನ್ ಮತ್ತು ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಯಾವುದೇ ಕ್ಲೈಂಟ್ LLM ಇದ್ದು ಇಲ್ಲದೆ ಬಳಸಬಹುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠವು MCP ಪರಿಸರಗಳನ್ನು ಸಿದ್ಧಪಡಿಸುವ ಮತ್ತು ನಿಮ್ಮ ಮೊದಲ MCP ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಪ್ರಾಯೋಗಿಕ ಮಾರ್ಗದರ್ಶನವನ್ನು ನೀಡುತ್ತದೆ. ನೀವು ಅವಶ್ಯಕ ಸಾಧನಗಳು ಮತ್ತು ಫ್ರೆ임್‌ವರ್ಕ್‌ಗಳನ್ನು ಹೊಂದಿಸುವುದು, ಮೂಲ MCP ಸರ್ವರ್‍‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು, ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು ಮತ್ತು ನಿಮ್ಮ ಜಾರಿಗೊಳಿಸಿದ ಯೋಜನೆಗಳ ಪರೀಕ್ಷೆ ಹೇಗೆ ಮಾಡಬೇಕೆಂದು ತಿಳಿದುಕೊಳ್ಳುತ್ತಾರೆ.

ಮಾದರಿ ಕಾಂಟೆಕ್ಸ್ಟ್ ಪ್ರೋಟೋಕಾಲ್ (MCP) ಒಂದು ಓಪನ್ ಪ್ರೋಟೋಕಾಲ್ ಆಗಿದ್ದು, ಅಪ್ಲಿಕೇಶನ್‌ಗಳು LLMs ಗೆ ಕಾಂಟೆಕ್ಸ್ಟ್ ನೀಡುವ ವಿಧಾನವನ್ನು ಮಾನ್ಯಗೊಳಿಸುತ್ತದೆ. MCP ಅನ್ನು AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ USB-C పోರ್ಟಿನಂತೆ ಭಾವಿಸಬಹುದು - ಇದು AI ಮಾದರಿಗಳನ್ನು ವಿಭಿನ್ನ ಡೇಟಾ ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳಿಗೆ ಸಂಯೋಜಿಸುವ ಮಾನ್ಯಗೊಳಿತ ವಿಧಿಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

## ಕಲಿಕೆ ಗುರಿಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ ನೀವು ಮಾಡಬಹುದು:

- C#, ಜಾವಾ, ಪೈಥಾನ್, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್, ಮತ್ತು ರಸ್ಟ್‌ಗಳಲ್ಲಿ MCP ಅಭಿವೃದ್ಧಿ ಪರಿಸರಗಳನ್ನು ಸಿದ್ಧಪಡಿಸುವುದು
- ಕಸ್ಟಮ್ ವೈಶಿಷ್ಟ್ಯಗಳು (ಸಂಪನ್ಮೂಲಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಾಧನಗಳು) ಜೊತೆಗೆ ಮೂಲ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ ನಿಯೋಜಿಸುವುದು
- MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಸಂಪರ್ಕಿಸುವ ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ರಚಿಸುವುದು
- MCP ಜಾರಿಗೊಳಾವಣೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ ದೋಷ ನಿರ್ಧಾರ ಮಾಡುವುದು

## ನಿಮ್ಮ MCP ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸುವುದು

MCP ಕಾರ್ಯಗತಗೊಳಿಸುವ ಮುನ್ನ, ನಿಮ್ಮ ಅಭಿವೃದ್ಧಿ ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸುವುದು ಮತ್ತು ಮೂಲ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮುಖ್ಯ. ಈ ವಿಭಾಗವು ನಿಮ್ಮ MCP ಕಾರ್ಯಾರಂಭಕ್ಕಾಗಿ ಪ್ರಾಥಮಿಕ ಸಿದ್ಧತೆ ಹಂತಗಳನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

MCP ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ ನಿಂತುಕೊಳ್ಳುವ ಮೊದಲು, ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ ನಿಮಗೆ:

- **ಅಭಿವೃದ್ಧಿ ಪರಿಸರ**: ನಿಮ್ಮ ಆಯ್ದ ಭಾಷೆಗೆ (C#, ಜಾವಾ, ಪೈಥಾನ್, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್, ಅಥವಾ ರಸ್ಟ್)
- **IDE/ಸಂಪಾದಕ**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, ಅಥವಾ ಯಾವುದೇ ಆಧುನಿಕ ಕೋಡ್ ಸಂಪಾದಕ
- **ಪ್ಯಾಕೇಜ್ ಮ್ಯಾನೇಜರ್‌ಗಳು**: NuGet, Maven/Gradle, pip, npm/yarn, ಅಥವಾ Cargo
- **API ಕೀಲಿಗಳು**: ನೀವು ನಿಮ್ಮ ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಬಳಸಲು ಯೋಜಿಸಿರುವ ಯಾವುದೇ AI ಸೇವೆಗಳಿಗಾಗಿ

## ಮೂಲ MCP ಸರ್ವರ್ ಸಂರಚನೆ

ಒಂದು MCP ಸರ್ವರ್ ಸಾಮಾನ್ಯವಾಗಿ ಒಳಗೊಂಡಿರುತ್ತದೆ:

- **ಸರ್ವರ್ ಸಂರಚನೆ**: ಪೋರ್ಟ್, ಪ್ರಾಮಾಣೀಕರಣ ಮತ್ತು ಇತರೆ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಸಂರಚಿಸುವುದು
- **ಸಂಪನ್ಮೂಲಗಳು**: LLMಗಳಿಗೆ ಲಭ್ಯವಾಗುವ ಡೇಟಾ ಮತ್ತು ಕಾಂಟೆಕ್ಸ್ಟ್
- **ಸಾಧನಗಳು**: ಮಾದರಿಗಳು ಕರೆಮಾಡಬಹುದಾದ ಕಾರ್ಯಕ್ಷಮತೆ
- **ಪ್ರಾಂಪ್ಟ್‌ಗಳು**: ಪಠ್ಯವನ್ನು ನಿರ್ಮಿಸಲು ಅಥವಾ ವಿನ್ಯಾಸಗೊಳಿಸಲು ಟೆಂಪ್ಲೇಟುಗಳು

ಇದೀಗ ಒಂದು ತಗ್ಗುಮಟ್ಟದ ಉದಾಹರಣೆ ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್‌ನಲ್ಲಿ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP ಸರ್ವರ್ ರಚಿಸಿ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ಒಂದು ಸೇರ್ಪಡೆ ಸಾಧನವನ್ನು ಸೇರಿಸಿ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ಒಂದು ಡೈನಾಮಿಕ್ ಆತಿಥ್ಯ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
server.resource(
  "file",
  // 'list' ಪರಿಮಿತಿ ಸಂಪನ್ಮೂಲವು ಲಭ್ಯವಿರುವ ಫೈಲ್ಗಳನ್ನು ಹೇಗೆ ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ ಎಂದು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಇದನ್ನು ಅನಿರ್ದಿಷ್ಟಗೊಳಿಸಿದರೆ ಈ ಸಂಪನ್ಮೂಲಕ್ಕಾಗಿ ಪಟ್ಟಿ ಮಾಡುವಿಕೆ ನಿಷ್ಕ್ರಿಯವಾಗುತ್ತದೆ.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// ಫೈಲ್ ಒಳಗೊಂಡಿಕೆಗಳನ್ನು ಓದುವ ಫೈಲ್ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

// stdin ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸುವುದು ಮತ್ತು stdout ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಿ
const transport = new StdioServerTransport();
await server.connect(transport);
```

ಮಿತಕೊಂಡಿದ ಕೋಡಿನಲ್ಲಿ ನಾವೇನು ಮಾಡಿದ್ದೇವೆ ಎಂದರೆ:

- MCP ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ SDK ಯಿಂದ ಅಗತ್ಯವಿರುವ ತರಗತಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಲಾಗಿದೆ.
- ಹೊಸ MCP ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ಸೃಷ್ಟಿಸಿ ಸಂರಚಿಸಲಾಗಿದೆ.
- ಕಸ್ಟಮ್ ಸಾಧನ (`calculator`) ಅನ್ನು ಹ್ಯಾಂಡ್ಲರ್ ಕಾರ್ಯಚಟುವಟಿಕೆಯೊಂದಿಗೆ ನೋಂದಣಿ ಮಾಡಲಾಗಿದೆ.
- MCP ವಿನಂತಿಗಳನ್ನು ಸ್ವೀಕರಿಸಲು ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಲಾಗಿದೆ.

## ಪರೀಕ್ಷೆ ಮತ್ತು ದೋಷ ಶೋಧನೆ

ನೀವು ನಿಮ್ಮ MCP ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಲು ಆರಂಭಿಸುವ ಮುನ್ನ, ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನೂ ಮತ್ತು ದೋಷ ಶೋಧನೆಯ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳನ್ನೂ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮುಖ್ಯ. ಪರಿಣಾಮಕಾರಿಯುತ ಪರೀಕ್ಷೆ ನಿಮ್ಮ ಸರ್ವರ್ ನಿರೀಕ್ಷೆಯಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು ಖಚಿತಪಡಿಸುತ್ತದೆ ಮತ್ತು ಸಮಸ್ಯೆಗಳಿಗೂ ತಲುಪುವುದಕ್ಕೂ ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಕೆಳಗಿನ ವಿಭಾಗವು ನಿಮ್ಮ MCP ಜಾರಿಗೊಳಣೆ ಮಾನ್ಯಗೊಳಿಸಲು ಶಿಫಾರಸು ಮಾಡಿದ ರೀತಿಗಳನ್ನು ವಿವರಿಸುತ್ತದೆ.

MCP ನಿಮ್ಮ ಸರ್ವರ್ಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಮತ್ತು ದೋಷ ಶೋಧಿಸಲು ಸಲಹೆಗಳನ್ನೂ ನೀಡುತ್ತದೆ:

- **ವೀಕ್ಷಕ ಸಾಧನ**, ಈ ದೃಶ್ಯಮಯ ಇಂಟರ್ಫೇಸ್ ನಿಮ್ಮ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಮಾಡಿ ನಿಮ್ಮ ಸಾಧನಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.
- **curl**, ನೀವು ನಿಮ್ಮ ಸರ್ವರ್‌ಗೆ ಕಮಾಂಡ್ ಲೈನ್ ಸಾಧನವಾದ curl ಅಥವಾ HTTP ಕಮಾಂಡ್ ರಚಿಸಿ ಚಲಾಯಿಸುವ ಇತರ ಕ್ಲೈಂಟ್‌ಗಳ ಮೂಲಕ ಸಂಪರ್ಕಿಸಬಹುದು.

### MCP ವೀಕ್ಷಕ ಉಪಯೋಗಿಸುವುದು

[MCP ವೀಕ್ಷಕ](https://github.com/modelcontextprotocol/inspector) ಒಂದು ದೃಶ್ಯ ಪರೀಕ್ಷಾ ಸಾಧನವಾಗಿದ್ದು, ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ:

1. **ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು**: ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳು, ಸಾಧನಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪತ್ತೆ ಮಾಡುತ್ತದೆ
2. **ಸಾಧನ ಕಾರ್ಯಾಚರಣೆ ಪರೀಕ್ಷೆ**: ವಿಭಿನ್ನ ಪರಾಮಿತಿ ಪರೀಕ್ಷಿಸಿ ನಿರ್ಜೀವಾಗ್ರಹವನ್ನು ನೇರ ಸಮಯದಲ್ಲಿ ನೋಡಬಹುದು
3. **ಸರ್ವರ್ ಮೆಟಾ ಡೇಟಾ ವೀಕ್ಷಣೆ**: ಸರ್ವರ್ ಮಾಹಿತಿ, ಸ್ಕೀಮಾ ಮತ್ತು ಸಂರಚನೆಗಳನ್ನು ಪರಿಗಣಿಸಿ

```bash
# ಉದಾಹರಣೆ TypeScript, MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ ಅನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡುವುದು ಮತ್ತು ನಡೆಸುವುದು
npx @modelcontextprotocol/inspector node build/index.js
```

ನೀವು ಮೇಲಿನ ಕಮಾಂಡ್‌ಗಳು ಚಲಿಸುವಾಗ, MCP ವೀಕ್ಷಕ ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸ್ಥಳೀಯ ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ. ನೀವು ನೋಂದಣಿ ಮಾಡಿರುವ MCP ಸರ್ವರ್‌ಗಳು, ಲಭ್ಯವಿರುವ ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ ಅನ್ನು ಕಾಣಬಹುದು. ಈ ಇಂಟರ್ಫೇಸ್ ಸಾಧನ ಕಾರ್ಯಾಚರಣೆ ನೋಡಿ, ಸರ್ವರ್ ಮೆಟಾ ಡೇಟಾವು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನೇರ ಸಮಯದ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ವೀಕ್ಷಿಸುವ ಮೂಲಕ ಇಂಟರೆಕ್ಟಿವಾಗಿ ಪರೀಕ್ಷೆ ಮಾಡಲು ಅನುಕೂಲ ಮಾಡಿಕೊಡುತ್ತದೆ, ಇದರಿಂದ ನಿಮ್ಮ MCP ಸರ್ವರ್ ಜಾರಿಗೊಳಣೆಗಳನ್ನು ಸರಳವಾಗಿ ಮಾನ್ಯಗೊಳಿಸಿ ದೋಷ ಮುಕ್ತಗೊಳಿಸಲು ಸಹಾಯವಾಗುತ್ತದೆ.

ಇದೀಗ ಒಂದು ಸ್ಕ್ರೀನ್‌ಶಾಟ್ ಇಲ್ಲಿದೆ:

![MCP Inspector server connection](../../../../translated_images/kn/connected.73d1e042c24075d3.webp)

## ಸಾಮಾನ್ಯ ಸೆಟಪ್ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳು

| ಸಮಸ್ಯೆ | ಸಾಧ್ಯವಿರುವ ಪರಿಹಾರ |
|-------|-------------------|
| ಸಂಪರ್ಕ ನಿರಾಕರಿಸಲಾಗಿದೆ | ಸರ್ವರ್ ರನ್ ಆಗುತ್ತಿದೆಯೇ ಎಂದು ಮತ್ತು ಪೋರ್ಟ್ ಸರಿಯೇ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಿ |
| ಸಾಧನ ಕಾರ್ಯಾಚರಣೆ ದೋಷಗಳು | ಪರಾಮಿತಿ ಮಾನ್ಯತೆ ಮತ್ತು ದೋಷ ನಿರ್ವಹಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ |
| ಪ್ರಾಮಾಣೀಕರಣ ವಿಫಲ | API ಕೀಲಿಗಳು ಮತ್ತು ಅನುಮತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ |
| ಸ್ಕೀಮಾ ಮಾನ್ಯತೆ ದೋಷಗಳು | ಪರಾಮಿತಿ ಸುಪತ್ರಿತ ಸ್ಕೀಮಾ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿ |
| ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗುತ್ತಿಲ್ಲ | ಪೋರ್ಟ್ ಸಂಧಾನ ಸಮಸ್ಯೆಗಳು ಅಥವಾ ಅಭಿವೃದ್ದಿ ಅವಲಂಬನೆಗಳು ಇರುವುದಿಲ್ಲವೇ ಎಂದು ಪರಿಶೀಲಿಸಿ |
| CORS ದೋಷಗಳು | ಕ್ರಾಸ್-ಒರಿಜಿನ್ ವಿನಂತಿಗಳಿಗೆ ಸರಿಯಾದ CORS ಹೆಡರ್‌ಗಳನ್ನು ಸಂರಚಿಸಿ |
| ಪ್ರಾಮಾಣೀಕರಣ ಸಮಸ್ಯೆಗಳು | ಟೋಕನ್ ಮಾನ್ಯತೆ ಮತ್ತು ಅನುಮತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ |

## ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿ

ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಪರೀಕ್ಷೆಗಾಗಿ ನೀವು ನಿಮ್ಮ ಯಂತ್ರದಲ್ಲಿ ನೇರವಾಗಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಬಹುದು:

1. **ಸರ್ವರ್ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ**: ನಿಮ್ಮ MCP ಸರ್ವರ್ ಅಪ್ಲಿಕೇಶನ್ ಚಾಲನೆ ಮಾಡಿ
2. **ನೆಟ್‌ವರ್ಕಿಂಗ್ ಸಂರಚನೆ**: ನಿರೀಕ್ಷಿತ ಪೋರ್ಟ್‌ನಲ್ಲಿ ಸರ್ವರ್ ಪ್ರವೇಶಾರ್ಹತೆ ಖಚಿತಪಡಿಸಿ
3. **ಕ್ಲೈಂಟ್ ಸಂಪರ್ಕಿಸಿ**: `http://localhost:3000` వంటి ಸ್ಥಳೀಯ ಸಂಪರ್ಕ URLಗಳನ್ನು ಉಪಯೋಗಿಸಿ

```bash
# ಉದಾಹರಣೆ: TypeScript MCP ಸರ್ವರ್ ಅನ್ನು ಪ್ರാദೇಶಿಕವಾಗಿ ಚಾಲನೆ ಮಾಡುವುದು
npm run start
# ಸರ್ವರ್ http://localhost:3000 ನಲ್ಲಿ ಚಾಲನೆಯಲ್ಲಿ ಇದೆ
```

## ನಿಮ್ಮ ಮೊದಲ MCP ಸರ್ವರ್ ನಿರ್ಮಾಣ

ನಾವು ಹಿಂದೆ [ಮೂಲ ಕಲ್ಪನೆಗಳು](../../01-CoreConcepts/README.md) ನೋಡಿದ್ದೇವೆ, ಈಗ ಆ ಜ್ಞಾನವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುವ ಸಮಯ.

### ಸರ್ವರ್ ಏನು ಮಾಡಬಹುದು

ಕೋಡ್ ಬರೆತಿಡುವ ಮುನ್ನ, ಸರ್ವರ್ ಏನು ಮಾಡುವುದೆಂದು ನೆನಪಿಸಿಕೊಂಡಿಕೊಳ್ಳೋಣ:

MCP ಸರ್ವರ್ ಉದಾಹರಣೆಗೆ:

- ಸ್ಥಳೀಯ ಫೈಲ್‌ಗಳು ಮತ್ತು ದತ್ತಾಂಶದತ್ತ ಸೇರ್ಪಡೆ
- ದೂರಸ್ಥ API ಗಳಿಗೆ ಸಂಪರ್ಕ
- ಗಣನೆ ಮಾಡುವುದು
- ಇತರ ಸಾಧನಗಳು ಮತ್ತು ಸೇವೆಗಳೊಂದಿಗೆ ಸಂಯೋಜನೆ
- ಪರಸ್ಪರ ಸಂವಹನಕ್ಕೆ ಬಳಕೆದಾರ ಇಂಟರ್ಫೇಸ್ ಒದಗಿಸುವುದು

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಸಾವಯವವಾಗಿ ಏನು ಮಾಡಬಹುದೆಂದು ಗೊತ್ತಾಗಿದೆ, ಕೋಡಿಂಗ್ ಆರಂಭಿಸೋಣ.

## ಅಭ್ಯಾಸ: ಸರ್ವರ್ ರಚನೆ

ಸರ್ವರ್ ನಿರ್ಮಿಸಲು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

- MCP SDK ಅನ್ನು ಸ್ಥಾಪಿಸಿ.
- ಪ್ರಾಜೆಕ್ಟ್ ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆಯನ್ನು ಸಿದ್ಧಪಡಿಸಿ.
- ಸರ್ವರ್ ಕೋಡ್ ಬರೆಯಿರಿ.
- ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ.

### -1- ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ

#### TypeScript

```sh
# ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿ ರಚಿಸಿ ಮತ್ತು npm ಪ್ರಾಜೆಕ್ಟ್ ಪ್ರಾರಂಭಿಸಿ
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿ ರಚಿಸಿ
mkdir calculator-server
cd calculator-server
# Visual Studio Code ನಲ್ಲಿ ಫೋಲ್ಡರ್ ಓಪನ್ ಮಾಡಿ - ನೀವು ಬೇರೆ IDE ಬಳಸುತ್ತಿದ್ದರೆ ಇದನ್ನು ಬಿಟ್ಟುಬಿಡಿ
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

ಜಾವಾ ಗಾಗಿ, ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ:

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

Zip ಫೈಲ್ ಅನ್ನು ಅಳಿಸಿ:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# ಐಚ್ಛಿಕವಾಗಿ ಬಳಸದ ಪರೀಕ್ಷೆಯನ್ನು ತೆಗೆದುಹಾಕಿ
rm -rf src/test/java
```

ನಿಮ್ಮ *pom.xml* ಫೈಲ್‌ಗೆ ಕೆಳಗಿನ ಪೂರ್ಣ ಸಂರಚನೆಯನ್ನು ಸೇರಿಸಿ:

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

### -2- ಅವಲಂಬನೆ ಸೇರಿಸುವುದು

ಈಗ ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಸೃಷ್ಟಿಯಾಗಿದೆ, ಈಗ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸೋಣ:

#### TypeScript

```sh
# ಇನ್ಸ್ಟಾಲ್ ಆಗದಿದ್ದರೆ, TypeScript ಅನ್ನು ಜಾಗತಿಕವಾಗಿ ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ
npm install typescript -g

# MCP SDK ಮತ್ತು ಸ್ಕೀಮಾ ವಾಲಿಡೇಶನ್‌ಗೆ Zod ಅನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ವರ್ಚುವಲ್ ಎನ್‌ವೈರನ್ಮೆಂಟ್ ರಚಿಸಿ ಮತ್ತು ಅವಲಂಬನಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ
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

### -3- ಪ್ರಾಜೆಕ್ಟ್ ಫೈಲ್‌ಗಳು ರಚಿಸುವುದು

#### TypeScript

*package.json* ಫೈಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಕೆಳಗಿನ ವಿಷಯದಿಂದ ಬದಲಿಸಿ, ಸರ್ವರ್ ನಿರ್ಮಿಸಿ ಚಾಲನೆ ಮಾಡಲು ಅನುಕೂಲವಾಗುವಂತೆ:

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

*tsconfig.json* ರಚಿಸಿ, ಈ ವಿಷಯ ನೀಡಿ:

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

ನಿಮ್ಮ ಮೂಲ ಕೋಡ್‍ಗಾಗಿ ಡೈರೆಕ್ಟರಿಯನ್ನು ರಚಿಸಿ:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* ಫೈಲ್ ರಚಿಸಿ

```sh
touch server.py
```

#### .NET

ಅಗತ್ಯ NuGet ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

ಜಾವಾ ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿರುತ್ತದೆ.

#### Rust

`cargo init` ಚಲಿಸುವಾಗ *src/main.rs* ಫೈಲ್ ಸ್ವಯಂ ರಚನೆ ಆಗುತ್ತದೆ. ಫೈಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಡೀಫಾಲ್ಟ್ ಕೋಡ್ ಅಳಿಸಿ.

### -4- ಸರ್ವರ್ ಕೋಡ್ ಬರೆಯುವುದು

#### TypeScript

*index.ts* ಫೈಲ್ ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ಒಂದು MCP ಸರ್ವರ್ ಅನ್ನು ರಚಿಸಿ
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

ಇದೀಗ ನೀವು ಒಂದು ಸರ್ವರ್ ಹೊಂದಿದ್ದೀರಿ, ಆದರೆ ಅದು ಹೆಚ್ಚಾಗಿ ಯಾವುದೂ ಮಾಡೋದಿಲ್ಲ, ಅದನ್ನು ಸರಿಪಡಿಸೋಣ.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ಒಂದು MCP ಸರ್ವರ್ ರಚಿಸಿ
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

ಜಾವಾ ಗಾಗಿ, ಮೂಲ ಸರ್ವರ್ ಘಟಕಗಳನ್ನು ರಚಿಸಿ. ಮೊದಲು, ಮುಖ್ಯ ಅಪ್ಲಿಕೇಶನ್ ಕ್ಲಾಸ್ ಪರಿವರ್ತಿಸಿ:

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

ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸೇವೆ ರಚಿಸಿ *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

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

**ಉತ್ಪಾದನಾ-ತಯಾರ ಸೇವೆಗೆ ಐಚ್ಛಿಕ ಘಟകಗಳು:**

ಪ್ರಾರಂಭ ಸಂರಚನೆ ರಚಿಸಿ *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

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

ಅರೋಗ್ಯ ನಿಯಂತ್ರಣಕೂಟ ರಚಿಸಿ *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

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

ವ್ಯತ್ಯಯ ಹ್ಯಾಂಡ್ಲರ್ ರಚಿಸಿ *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

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

        // ಪಡೆಯುವವರು
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

ಕಸ್ಟಮ್ ಬ್ಯಾನರ್ ರಚಿಸಿ *src/main/resources/banner.txt*:

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

*src/main.rs* ಫೈಲ್ ಮೇಲ್ಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ. ಇದು MCP ಸರ್ವರ್‌ಗಾಗಿ ಅಗತ್ಯ ಗ್ರಂಥಾಲಯಗಳು ಮತ್ತು ಮೋಡ್ಯೂಲ್‌ಗಳನ್ನು ಆಮದು ಮಾಡುತ್ತದೆ.

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

ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಒಂದು ಸರಳ ಮಾದರಿ ಆಗಿದ್ದು, ಎರಡು ಸಂಖ್ಯೆಗಳ ಮೊತ್ತವನ್ನು ಸೇರಿಸಬಹುದು. ಕ್ಯಾಲ್ಕುಲೇಟರ್ ವಿನಂತಿಯನ್ನು ಪ್ರತಿನಿಧಿಸುವ struct ಅನ್ನು ರಚಿಸೋಣ.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

ಮುಂದಿನದಾಗಿ, ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಅನ್ನು ಪ್ರತಿನಿಧಿಸುವ struct ರಚಿಸೋಣ. ಈ struct ಸಾಧನ ರೌಟರ್ ಅನ್ನು ಹೊಂದುತ್ತದೆ, ಇದು ಸಾಧನಗಳನ್ನು ನೋಂದಣಿ ಮಾಡಲು ಬಳಸಲಾಗುತ್ತದೆ.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

ಈಗ, `Calculator` struct ಅನ್ನು ಜಾರಿಗೊಳಿಸಿ, ಸರ್ವರ್ ಹೊಸ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ ಮತ್ತು ಸರ್ವರ್ ಮಾಹಿತಿ ಒದಗಿಸಲು ಸರ್ವರ್ ಹ್ಯಾಂಡ್ಲರ್ ಅನ್ನು ಜಾರಿಗೊಳಿಸಿ.

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

ಕೊನೆಗೆ, ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸುವ ಮುಖ್ಯ ಕಾರ್ಯವನ್ನು ಜಾರಿಗೊಳಿಸ ಬೇಕಾಗುತ್ತದೆ. ಈ ಕಾರ್ಯ `Calculator` struct ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ, ಅದು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್‌ಪುಟ್/ ಔಟ್‌ಪುಟ್ ಮೂಲಕ ಸೇವೆ ನೀಡುತ್ತದೆ.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

ಈಗ ಸರ್ವರ್ ತನ್ನ ಬಗ್ಗೆ ಮೂಲ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸಲು ಸಿದ್ಧವಾಗಿದೆ. ಮುಂದಿಗೆ, ಸೇರ್ಪಡೆಗಾಗಿ ಸಾಧನ ಸೇರಿಸಲಾಗುವುದು.

### -5- ಸಾಧನ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಸೇರಿಸುವಿಕೆ

ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ ಸಾಧನ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಸೇರಿಸಿ:

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

ನಿಮ್ಮ ಸಾಧನವು `a` ಮತ್ತು `b` ಎಂಬ ಪರಾಮಿತಿಗಳನ್ನು ತೆಗೆದು, ಕೆಳಗಿನ ರೂಪದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

ನಿಮ್ಮ ಸಂಪನ್ಮೂಲ "greeting" என்ற ಸ್ಟ್ರಿಂಗ್ ಮೂಲಕ ಪ್ರವೇಶಿಸಲಾಗುತ್ತದೆ ಮತ್ತು `name` ಎಂಬ ಪರಾಮಿತಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಸಾಧನದ ಪ್ರಯೋಗ್ಯವಂತ ಸಮಾನ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೀಡುತ್ತದೆ:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ಹೆಚ್ಚುವರಿ ಸಾಧನವನ್ನು ಸೇರಿಸಿ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ಚುರುಕಾದ ನಮಸ್ಕಾರ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

ಮಿತಕೊಂಡಿದ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- `add` ಎಂಬ ಸಾಧನವನ್ನು ನಿರೂಪಿಸಿದ್ದೇವೆ, ಇದು `a` ಮತ್ತು `b` ಎರಡೂ ಪೂರ್ಣಾಂಕಗಳನ್ನು ಪರಾಮಿತಿಗಳಾಗಿ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.
- `greeting` ಎನ್ನುವ ಸಂಪನ್ಮೂಲವನ್ನು ರಚಿಸಿದೆವು, ಇದು `name` ಪರಾಮಿತಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.

#### .NET

ಇದನ್ನು ನಿಮ್ಮ Program.cs ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

ಸಾಧನಗಳು ಹಿಂದಿನ ಹಂತದಲ್ಲಿ ಈಗಾಗಲೇ ರಚಿಸಲಾಗಿದೆ.

#### Rust

`impl Calculator` ಬ್ಲಾಕ್ ಒಳಗೆ ಹೊಸ ಸಾಧನವನ್ನು ಸೇರಿಸಿ:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- ಅಂತಿಮ ಕೋಡ್

ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಲು ಬೇಕಾದ ಕೊನೆಯ ಕೋಡ್ ಸೇರಿಸೋಣ:

#### TypeScript

```typescript
// stdin ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸುವುದನ್ನು ಮತ್ತು stdout ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಿ
const transport = new StdioServerTransport();
await server.connect(transport);
```

ಪೂರ್ಣ ಕೋಡ್ ಇಲ್ಲಿದೆ:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP ಸರ್ವರ್ ಅನ್ನು ರಚಿಸು
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ಒಂದು ಸೇರ್ಪಡೆ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ಒಂದು ಗತಿ ಶೀಲವಾದ ವಂದನಾ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

// stdin ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸಲು ಮತ್ತು stdout ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸಲು ಪ್ರಾರಂಭಿಸು
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ಒಂದು MCP ಸರ್ವರ್ ರಚಿಸು
mcp = FastMCP("Demo")


# ಒಂದು ಸೇರಿಸುವ ಉಪಕರಣ ಸೇರಿಸಿ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ಡೈನಾಮಿಕ್ ಎಳೆದೋಪನಾಸಿಕೆ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# ಮುಖ್ಯ ನಿರ್ವಹಣಾ ಬ್ಲಾಕ್ - ಸರ್ವರ್ ನಿರ್ವಹಿಸಲು ಇದನ್ನು ಅಗತ್ಯವಿದೆ
if __name__ == "__main__":
    mcp.run()
```

#### .NET

Program.cs ಫೈಲ್ ಈ ಕೆಳಗಿನ ವಿಷಯದೊಂದಿಗೆ ರಚಿಸಿ:

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

ನಿಮ್ಮ ಸಂಪೂರ್ಣ ಮುಖ್ಯ ಅಪ್ಲಿಕೇಶನ್ ಕ್ಲಾಸ್ ಹೀಗೆ ಕಾಣಬೇಕು:

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

ರಸ್ಟ್ ಸರ್ವರ್ ಅಂತಿಮ ಕೋಡ್ ಹೀಗೆ ಕಾಣಬೇಕು:

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

### -7- ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

ಪರೀಕ್ಷಿಸಲು ಸರ್ವರ್ ನಡೆಯುತ್ತಲೆ:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP ವೀಕ್ಷಕ ಬಳಸಲು, `mcp dev server.py` ಬಳಸಿರಿ, ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವೀಕ್ಷಕ ಪ್ರಾರಂಭಿಸಿತು ಮತ್ತು ಅಗತ್ಯ ಪ್ರಾಕ್ಸಿ ಸೆಷನ್ ಟೋಕನ್ ಒದಗಿಸುತ್ತದೆ. `mcp run server.py` ಬಳಸಿದರೆ, ನೀವು ಕೈಯಲ್ಲಿ ವೀಕ್ಷಕ ಸಕ್ರಿಯಗೊಳಿಸಿ ಸಂಪರ್ಕವನ್ನು ಸಂರಚಿಸಬೇಕಾಗುತ್ತದೆ.

#### .NET

ನೀವು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇರಬೇಕು:

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

ಸರ್ವರ್ ಚಲಾಯಿಸಲು ಕೆಳಗಿನ കമಾಂಡ್‌ಗಳು ನಡಿಸಿ:

```sh
cargo fmt
cargo run
```

### -8- ವೀಕ್ಷಕ ಬಳಸಿ ಚಲಿಸುವಿಕೆ

ವೀಕ್ಷಕ ಒಂದು ಅದ್ಭುತ ಸಾಧನವಾಗಿದೆ, ಅದು ನಿಮ್ಮ ಸರ್ವರ್ ಚಾಲನೆ ಮಾಡಿ, ಅದನ್ನು ಪರೀಕ್ಷಿಸಲು ನಿಮ್ಮೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ. ಅದನ್ನು ಪ್ರಾರಂಭಿಸೋಣ:

> [!NOTE]
> ನಿಮ್ಮ ಸ್ವಂತ ಪ್ರಾರಂಭRuntime ಕ್ಕೆ ಇದ್ದ ಭಾಗದಲ್ಲಿ "command" ಕ್ಷೇತ್ರದಲ್ಲಿ ಬದಲಾವಣೆ ಕಾಣಬಹುದು.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

ಅಥವಾ ನಿಮ್ಮ *package.json* ಗೆ ಇಂಥದಾಗಿ `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` ಸೇರಿಸಿ ನಂತರ `npm run inspector` ಚಲಾಯಿಸಿ

#### Python

Python Node.js ಸಾಧನವಾದ inspector ಅನ್ನು ಒರಟುಗೊಳಿಸುತ್ತದೆ. ಈ ಸಾಧನವನ್ನು ಹೀಗೆ ಕರೆಮಾಡಬಹುದು:

```sh
mcp dev server.py
```

ಆದರೆ, ಇದು ಸಾಧನದಲ್ಲಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ವಿಧಾನಗಳನ್ನು ಜಾರಿಗೊಳಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ನೇರವಾಗಿ Node.js ಸಾಧನವನ್ನು ಹೀಗೇ ಚಾಲನೆ ಮಾಡಬೇಕೆಂದು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ:

```sh
npx @modelcontextprotocol/inspector mcp run server.py
```

ನೀವು ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಲಿಸುವಾಗ ಆಜ್ಞೆಗಳು ಮತ್ತು ಪರಿಚಯಾರ್ಹ ಸ್ಥಾನಗಳನ್ನು ಹೊಂದಿಸಲು ಸಾಧ್ಯವಾಗುವ ಯಾವುದೇ ಸಾಧನ ಅಥವಾ IDE ಅನ್ನು ಬಳಸುತ್ತಿದ್ದರೆ,
`Command` ಕ್ಷೇತ್ರದಲ್ಲಿ `python` ಅನ್ನು ಹಾಗೂ `Arguments` ನಲ್ಲಿ `server.py` ಅನ್ನು ನಿಶ್ಚಿತರಾಗಿ ಸೆಟ್ ಮಾಡಿಕೊಳ್ಳಿ. ಇದರಿಂದ ಸ್ಕ್ರಿಪ್ಟ್ ಸರಿಯಾಗಿ ಓಡುತ್ತದೆ.

#### .NET

ನೀವು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇದ್ದೀರಿ ಎನ್ನುವುದನ್ನು ದೃಢಪಡಿಸಿ:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### ಜಾವಾ

ನಿಮ್ಮ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಸರ್ವರ್ ಚಾಲನೆಯಲ್ಲಿದ್ದಲ್ಲಿ ನಿಶ್ಚಯಿಸಿಕೊಳ್ಳಿ  
ಇನ್ಸ್ ಸ್ಫೆಕ್ಟರ್ ಅನ್ನು ಓಡಿಸಿ:

```cmd
npx @modelcontextprotocol/inspector
```

ಇನ್ಸ್ ಸ್ಫೆಕ್ಟರ್ ವೆಬ್ ಇಂಟರ್‌ಫೇಸ್ನಲ್ಲಿ:

1. "SSE" ಅನ್ನು ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್ ಪ್ರಕಾರವಾಗಿ ಆಯ್ಕೆಮಾಡಿ  
2. URL ಅನ್ನು ಸರಿಯಾಗಿ ಇಡಿ: `http://localhost:8080/sse`  
3. "Connect" ಕ್ಲಿಕ್ ಮಾಡಿ

![Connect](../../../../translated_images/kn/tool.163d33e3ee307e20.webp)

**ನೀವು ಈಗ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಗೊಂಡಿದ್ದೀರಿ**  
**ಜಾವಾ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸುವ ವಿಭಾಗ ಈಗ ಮುಗಿದಿದೆ**

ಮುಂದಿನ ಅಂಶವು ಸರ್ವರ್‌ನೊಂದಿಗೆ ಸಂವಹನದ ಬಗ್ಗೆ ಇದೆ.

ನೀವು ಕೆಳಗಿನ ಬಳಕೆದಾರ ಇಂಟರ್‌ಫೇಸ್ನನ್ನೇ ನೋಡಬಹುದು:

![Connect](../../../../translated_images/kn/connect.141db0b2bd05f096.webp)

1. ಸಂಪರ್ಕ ಬಟನ್ ಆಯ್ಕೆಮಾಡಿ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದಿ  
  ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಿದ ಮೇಲೆ, ನೀವು ಕೆಳಗಿನಂತಿರುವುದನ್ನು ನೋಡಬಹುದಾಗಿದೆ:

  ![Connected](../../../../translated_images/kn/connected.73d1e042c24075d3.webp)

1. "Tools" ಮತ್ತು "listTools" ಆಯ್ಕೆಮಾಡಿ, "Add" ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತದೆ, "Add" ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು ಪ್ಯಾರಾಮೀಟರ್ ಮೌಲ್ಯಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ.

  ನೀವು ಕೆಳಗಿನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಬಹುದು, ಅಂದರೆ "add" ಉಪಕರಣದಿಂದ ಫಲಿತಾಂಶ:

  ![Result of running add](../../../../translated_images/kn/ran-tool.a5a6ee878c1369ec.webp)

ಶಭಾಶಃ, ನಿಮ್ಮ ಮೊದಲ ಸರ್ವರ್ ಸೃಷ್ಟಿಸಿ ಓಡಿಸಲು ನೀವು ಯಶಸ್ವಿಯಾದಿರಿ!

#### ರಸ್ಟ್

MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ CLI ಮೂಲಕ ರಸ್ಟ್ ಸರ್ವರ್ ಅನ್ನು ಓಡಿಸಲು, ಕೆಳಗಿನ ಕಮಾಂಡ್ ಬಳಸಿರಿ:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### ಅಧಿಕೃತ SDKಗಳು

MCP ಬೃಹತ್ ಭಾಷೆಗಳಿಗಾಗಿ ಅಧಿಕೃತ SDKಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - ಮೈಕ್ರೋಸಾಫ್ಟ್ ಜೊತೆಗೆ ಸಂಯುಕ್ತ ನಿರ್ವಹಣೆ
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ಜೊತೆ ಸಂಯುಕ್ತ ನಿರ್ವಹಣೆ
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - ಅಧಿಕೃತ TypeScript ಅನುಷ್ಠಾನ  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - ಅಧಿಕೃತ Python ಅನುಷ್ಠಾನ  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - ಅಧಿಕೃತ Kotlin ಅನುಷ್ಠಾನ  
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI ಜೊತೆ ಸಂಯುಕ್ತ ನಿರ್ವಹಣೆ  
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - ಅಧಿಕೃತ Rust ಅನುಷ್ಠಾನ  

## ಮುಖ್ಯ ಅಂಶಗಳು

- MCP ಅಭಿವೃದ್ಧಿ ವಾತಾವರಣವನ್ನು ಭಾಷಾ-ನಿರ್ದಿಷ್ಟ SDKಗಳ ಮೂಲಕ ಸುಲಭವಾಗಿ ಸಿದ್ಧಪಡಿಸಬಹುದು  
- MCP ಸರ್ವರ್‌ಗಳ ನಿರ್ಮಾಣ ಸಮಗ್ರ ಯೋಜನೆಗಳಿವೆ, ಸ್ಪಷ್ಟ ಸ್ಕೀಮಾಗಳೊಂದಿಗೆ ಉಪಕರಣಗಳನ್ನು ರಚಿಸಿ ಮತ್ತು ನೋಂದಾಯಿಸಿ  
- ಪರೀಕ್ಷೆ ಮತ್ತು ದೋಷ ಸಂಶೋಧನೆ ವಿಶ್ವಾಸಾರ್ಹ MCP ಅನುಷ್ಠಾನಗಳಿಗೆ ಅಗತ್ಯ  

## ಮಾದರಿಗಳು

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## ಕಾರ್ಯನಿರ್ವಹಣೆ

ನಿಮ್ಮ ಆಯ್ಕೆಯ ಒಂದು ಉಪಕರಣದೊಂದಿಗೆ ಸರಳ MCP ಸರ್ವರ್ ರಚಿಸಿ:

1. ನಿಮ್ಮ ಆರಿಸಿದ ಭಾಷೆಯಲ್ಲಿ ಉಪಕರಣವನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ (.NET, ಜಾವಾ, ಪython, ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್, ಅಥವಾ ರಸ್ಟ್).  
2. ಇನ್‌ಪುಟ್ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಮತ್ತು ರಿಟರ್ನ್ ಮೌಲ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ.  
3. ಸರ್ವರ್ ಸರಿಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆಯಾ ಎಂದು ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಉಪಕರಣವನ್ನು ಓಡಿಸಿ ಪರಿಶೀಲಿಸಿ.  
4. ವಿವಿಧ ಇನ್‌ಪುಟ್‌ಗಳೊಂದಿಗೆ ಅನುಷ್ಠಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ.  

## ಪರಿಹಾರ

[Solution](./solution/README.md)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [Azure ನಲ್ಲಿ Model Context Protocol ಬಳಸಿ ಏಜೆಂಟ್ಸ್ ನಿರ್ಮಾಣ](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)  
- [Azure ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳೊಂದಿಗೆ ದೂರಸ್ಥ MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)  
- [.NET OpenAI MCP ಏಜೆಂಟ್](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)  

## ಮುಂದುವರೆಯುವುದು ಏನು

ಮುಂದೆ: [MCP ಕ್ಲೈಂಟ್‌ಗಳೊಂದಿಗೆ ಪ್ರಾರಂಭ](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅವಿಧೇಯತಾ ಪ್ರಕಟಣೆ**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುವುದಾದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲದಲ್ಲಿನ ನೈಜ ಭಾಷೆಯ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸಿದ ಪರಿಣಾಮ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಗಳು ಅಥವಾ ದುರಾವಣೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
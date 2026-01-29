# Sample

Dis na JavaScript sample for MCP Server

Na so di calculator part of am be:

```javascript
// Define calculator tools for each operation
server.tool(
  "add",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.tool(
  "subtract",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a - b) }]
  })
);

server.tool(
  "multiply",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a * b) }]
  })
);

server.tool(
  "divide",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => {
    if (b === 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot divide by zero" }],
        isError: true
      };
    }
    return {
      content: [{ type: "text", text: String(a / b) }]
    };
  }
);
```

## Install

Run dis command:

```bash
npm install
```

## Run

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
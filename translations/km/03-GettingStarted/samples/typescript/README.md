# Sample

នេះគឺជាគំរូ Typescript សម្រាប់ម៉ាស៊ីនមេ MCP

នេះគឺជាផ្នែកគណនាគារ:

```typescript
// កំណត់ឧបករណ៍គណនាសម្រាប់ប្រតិបត្តិការផ្សេងៗនីមួយៗ
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

រត់ពាក្យបញ្ជាដូចខាងក្រោម៖

```bash
npm install
```

## Run

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំសំរាប់ភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវបាន។ ឯកសារដើមក្នុងភាសាដែលមានរបស់ខ្លួនគួរត្រូវបានពិចារណាថាជាដើមប្រភពដែលមានអំណាចសម្រាប់ព័ត៌មាន។ សម្រាប់ព័ត៌មានសំខាន់ណាស់ សូមណែនាំអោយប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ អ្នកគ្រាន់តែទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
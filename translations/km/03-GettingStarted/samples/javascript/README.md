# គំរូ

នេះគឺជាគំរូ JavaScript សម្រាប់ម៉ាស៊ីនបម្រើ MCP

នេះជាផ្នែកគណនាដែលមានរាងដូចជា៖

```javascript
// កំណត់ឧបករណ៍គណនាសម្រាប់ប្រតិបត្តិការនីមួយៗ
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

## ដំឡើង

បញ្ចូលពាក្យបញ្ជាខាងក្រោម៖

```bash
npm install
```

## រត់

```bash
npm start
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានពិចារណาว่า​ជា​មជ្ឈឹមតំណាងផ្លូវការនៃព័ត៌មាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្ដល់អាទិភាពដល់ការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# ការប្រតិបត្តិរបស់គំរូនេះ

## -1- ដំឡើងការគាំទ្រ

```bash
dotnet restore
```

## -2- រត់គំរូនេះ

```bash
dotnet run
```

## -3- សាកល្បងគំរូនេះ

ចាប់ផ្តើមបញ្ចូល terminal ដាច់ពីគ្នាមួយមុនពេលអ្នករត់ខាងក្រោម (ប្រាកដថា server ยังคงដំណើរការ)។

ពេលដែល server កំពុងដំណើរការនៅក្នុង terminal មួយ បើក terminal មួយផ្សេងទៀត ហើយរត់ពាក្យបញ្ជាខាងក្រោម៖

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

នេះគួរតែចាប់ផ្តើម web server មានផ្ទៃមុខវិជ្ជាជីវៈដែលអនុញ្ញាតឱ្យអ្នកសាកល្បងគំរូនេះ។

> ចូរត្រួតពិនិត្យថា **Streamable HTTP** ត្រូវបានជ្រើសទ្រង់ទ្រាយដឹកជញ្ជូន ហើយ URL គឺ `http://localhost:3001/mcp`។

បន្ទាប់ពី server បានភ្ជាប់៖ 

- សូមសាកល្បងបង្ហាញបញ្ជីឧបករណ៍ ហើយរត់ `add` ជាមួយអាគុយម៉ង់ 2 និង 4 អ្នកគួរតែឃើញ 6 ជាលទ្ធផល។
- ទៅកាន់ resources និង resource template ហើយហៅ "greeting" ផ្ទុកឈ្មោះមួយ ហើយអ្នកគួរតែឃើញការស្វាគមន៍ជាមួយឈ្មោះដែលអ្នកផ្តល់។

### ការសាកល្បងទ្រង់ទ្រាយ CLI

អ្នកអាចចាប់ផ្តើមវាត្រង់ក្នុងរបាំង CLI ដោយរត់ពាក្យបញ្ជា​ខាងក្រោម៖

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

នេះនឹងបង្ហាញបញ្ជីឧបករណ៍ទាំងអស់ដែលមាននៅលើ server។ អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

ដើម្បីអនុវត្តឧបករណ៍ ម្សៅ៖

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> ជាមុនសិន ប្រតិបត្តិការបន្ទាន់ក្នុងរបាំង CLI ឆ្លាតវៃជាងប្រតិបត្តិការនៅកម្មវិធីរុករក។
> អានបន្ថែមអំពី inspector [នៅទីនេះ](https://github.com/modelcontextprotocol/inspector)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការដោះស្រាយ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំបង្ហាញភាពច្បាស់លាស់ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅភាសាដើមគួរត្រូវបានពិចារណាជាដើមហើយសម្រាប់ប្រភពដែលមានអាទិភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមបានប្រើការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកបម្រែបកប្រែខុសៗណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
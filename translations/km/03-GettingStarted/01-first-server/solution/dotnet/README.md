# ការរត់ឧទាហរណ៍នេះ

## -1- ដំឡើងផ្នែកគ្រប់គ្រាន់

```bash
dotnet restore
```

## -3- រត់ឧទាហរណ៍


```bash
dotnet run
```

## -4- សាកល្បងឧទាហរណ៍

ក្រោមពេលម៉ាស៊ីនបម្រើកំពុងរត់នៅក្នុងតេរ៉មីណលមួយ បើកតេរ៉មីណលមួយទៀតហើយរត់ពាក្យបញ្ជាដូចខាងក្រោម៖

```bash
npx @modelcontextprotocol/inspector dotnet run
```

នេះគួរតែនាំឲ្យម៉ាស៊ីនបម្រើវែបមានផ្ទាំងរូបភាពដែលអាចអនុញ្ញាតឲ្យអ្នកសាកល្បងឧទាហរណ៍។

ពេលម៉ាស៊ីនបម្រើភ្ជាប់រួច៖ 

- ព្យាយាមបង្ហាញបញ្ជីឧបករណ៍ ហើយរត់ `add` ជាមួយនឹងអាគុយម៉ង់ 2 និង 4 អ្នកគួរតែឃើញលទ្ធផល 6។
- ទៅកាន់ធនធាន និងគំរូធនធាន ហើយហៅ "greeting" វាយឈ្មោះមួយ ហើយអ្នកគួរតែឃើញសារ​ស្វាគមន៍ជាមួយឈ្មោះដែលអ្នកបានផ្តល់។

### សាកល្បងក្នុងរបៀប CLI

អ្នកអាចចាប់ផ្តើមវាប្រកបដោយរបៀប CLI ដោយរត់ពាក្យបញ្ជាដូចខាងក្រោម៖

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

នេះនឹងបញ្ជីឧបករណ៍ទាំងអស់ដែលមាននៅលើម៉ាស៊ីនបម្រើ។ អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

ដើម្បីហៅឧបករណ៍ មួយវាយៈ

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> វាគឺជា​រឿង​ដ៏លឿន​ជាង​ក្នុង​ការ​រត់កម្មវិធី inspector ក្នុង​របៀប CLI ជាង​ក្នុងកម្មវិធីរុក្ខជាតិ។
> អាន​បន្ថែម​អំពី inspector [នៅទីនេះ](https://github.com/modelcontextprotocol/inspector)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការផ្តល់ការជ្រួលច្របល់**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើ សេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំនឹងរក្សាការត្រឹមត្រូវក៏ដោយ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវនៅក្នុងខ្លឹមសារ។ ឯកសារដើមនៅក្នុងភាសាមួយគួរត្រូវបានគេចាត់ទុកជាដើមទាំងស្រុង។ សម្រាប់ព័ត៌មានសំខាន់ មន្រ្តីបកប្រែដែលជាជំនាញបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសក្នុងការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
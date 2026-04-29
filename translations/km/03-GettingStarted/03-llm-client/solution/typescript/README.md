# ការរត់គំរូនេះ

គំរូនេះពាក់ព័ន្ធនឹងការមាន LLM នៅលើមុខងារគ_Client។ LLM ត្រូវការឲ្យអ្នករត់ថា៉ក្នុង Codespaces ឬអ្នកត្រូវរៀបចំតួអក្សរកំណត់ការចូលទៅផ្ទាល់ខ្លួននៅក្នុង GitHub ដើម្បីធ្វើការ។

## -1- តំរូវការជំនួយ

```bash
npm install
```

## -3- រត់ម៉ាស៊ីនបម្រើ


```bash
npm run build
```

## -4- រត់ម៉ាស៊ីនអតិថិជន

```sh
npm run client
```

អ្នកគួរតែនៅឃើញលទ្ធផលដូចជា:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភាសា គួរត្រូវបានគេរាប់បញ្ចាក់ថាជាប្រភពដែលមានសិទ្ធិគ្រប់គ្រង។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ អ្នកនិយាយមនុស្សដែលមានជំនាញបកប្រែវិជ្ជាជីវៈត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំឬការបកប្រែខុសប្រភេទណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
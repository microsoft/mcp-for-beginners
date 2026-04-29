# គំរូ៖ ម៉ាស៊ីនបម្រើមូលដ្ឋាន

ការអនុវត្តជាឧទាហរណ៍បង្ហាញពីវិធីសាស្រ្តសាងសង់កម្មវិធីម៉ាស៊ីនបម្រើ MCP ដែលភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP ហើយបង្ហាញ UI ឧបករណ៍នៅក្នុងសេនដ្បុកសុវត្ថិភាព។

ម៉ាស៊ីនបម្រើមូលដ្ឋាននេះក៏អាចប្រើសម្រាប់សាកល្បងកម្មវិធី MCP នៅពេលអភិវឌ្ឍន៍ក្នុងជម្រើសក្នុងស្រុកផងដែរ។

## ឯកសារសំខាន់ៗ

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - ម៉ាស៊ីនបម្រើ UI React ជាមួយការជ្រើសរើសឧបករណ៍, ការបញ្ចូលប៉ារ៉ាម៉ែត្រ និងការគ្រប់គ្រង iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - iframe ខាងក្រៅ សំរាប់ជា proxy ជាមួយការត្រួតពិនិត្យសុវត្ថិភាព និងការផ្ញើសារមុខក្រោយពីរទិស
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - រចនាសម្ព័ន្ធស្នូល: ការភ្ជាប់ម៉ាស៊ីនបម្រើ, ការហៅឧបករណ៍ និងការតំឡើង AppBridge

## ចាប់ផ្តើម

```bash
npm install
npm run start
# បើក http://localhost:8080
```

តាមលំនាំដើម កម្មវិធីម៉ាស៊ីនបម្រើនឹងព្យាយាមភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP នៅ `http://localhost:3001/mcp`។ អ្នកអាចកំណត់ពិធានការនេះដោយកំណត់អថេរបរិបទ `SERVERS` ជាមួយអារេ JSON របស់ URL ម៉ាស៊ីនបម្រើ៖

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## ស្ថាបត្យកម្ម

គំរូនេះប្រើលំនាំឈេីនពីរជាន់ iframe សម្រាប់ការខ្ទង់ UI សុវត្ថិភាព៖

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**ហេតុអ្វីបានជាចង់ប្រើ iframe ពីរសន្លឹក?**

- iframe ខាងក្រៅដំណើរការនៅលើឫសដើមដែលផ្សេង (ព្រឹតិ្តលេខ 8081) បង្អោយមិនអាចចូលប្រើម៉ាស៊ីនបម្រើផ្ទាល់បាន
- iframe ខាងក្នុងទទួលលេខ HTML តាមរយៈ `srcdoc` និងត្រូវបានកំណត់ដោយលក្ខណៈ sandbox
- សារបញ្ចោញតាមរយៈ iframe ខាងក្រៅ ដែលធ្វើការត្រួតពិនិត្យ និងផ្ញើតបសារប្រាក់ពីរទិស

ស្ថាបត្យកម្មនេះធានាថា ទោះបីជា কোដ UI ឧបករណ៍មានគំនិតអាក្រក់ ក៏មិនអាចចូលប្រើ DOM កម្មវិធីម៉ាស៊ីនបម្រើ, នំបុ័ន្ទ(cookie), ឬcontext JavaScript បានឡើយ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ចំពោះយើងខ្ញុំ ការខិតខំសម្រាប់ភាពត្រឹមត្រូវ គឺមានស្រាប់ តែសូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមដែលមានជាភាសាដើមគួរត្រូវបានទទួលស្គាល់ថាជាឯកសារដើមដែលមានសមត្ថកិច្ច។ សម្រាប់ព័ត៌មានសំខាន់ៗ មតិយោបល់ពីអ្នកបកប្រែជាមនុស្សជំនាញត្រូវបានណែនាំ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រង់ខុសពីការប្រើប្រាស់ការបកប្រែនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
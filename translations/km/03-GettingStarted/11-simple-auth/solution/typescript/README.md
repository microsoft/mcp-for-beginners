# រត់គំរូ

## ដំឡើងការពឹងផ្អែក

```sh
npm install
```

## សង់

```sh
npm run build
```

## បង្កើតសញ្ញាសម្គាល់

```sh
npm run generate
```

នេះបង្កើតសញ្ញាសម្គាល់ក្នុងឯកសារ *.env*។ អតិថិជននឹងអានពីឯកសារនេះ។

## រត់កូដ

ចាប់ផ្តើមម៉ាស៊ីនបម្រើជាមួយ:

```sh
npm start
```

រត់អតិថិជន ក្នុងផ្ទាំងប្លុចផ្សេងទៀតជាមួយ:

```sh
npm run client
```

នៅផ្ទាំងប្លុចម៉ាស៊ីនបម្រើ អ្នកគួរតែឃើញលទ្ធផលស្រដៀងនឹង៖

```text
User exists
User has required scopes
Middleware executed
```

ហើយក្នុងផ្ទាំងប្លុចអតិថិជន អ្នកគួរតែឃើញលទ្ធផលស្រដៀងនឹង៖

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### ការផ្លាស់ប្តូរព័ត៌មាន

ត្រូវប្រាកដថាយើងយល់ដឹងពីវិសាលភាព។ សូមស្វែងរកឯកសារ *server.ts* និងកូដនេះ៖

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

នេះនិយាយថាសញ្ញាសម្គាល់ដែលបានផ្ញើត្រូវតែមាន "User.Read"។ យើងបម្លែងវាចូលជា "User.Write"។ ឥឡូវនេះចាប់ផ្តើម `npm run build` ហើយចាប់ផ្តើមឡើងវិញម៉ាស៊ីនបម្រើ `npm start`។ អ្នកគួរតែឃើញការផ្ទៀងផ្ទាត់ auth មិនជោគជ័យទេ ព្រោះយើងគ្មានវិសាលភាពនេះ (យើងមាន User.Read និង Admin.Write)៖

អតិថិជនឥឡូវនេះនិយាយថា

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ហើយអ្នកអាចមើលឃើញនៅផ្ទាំងប្លុចម៉ាស៊ីនបម្រើថាវាបាននិយាយថា៖

```text
User exists
```

ហើយវាមិនដំណើរការលើសចំណុចនេះទេ។

ឬបន្ថែមវិសាលភាពនេះ "User.Write" ហើយរត់ `npm run generate` ហើយរត់អតិថិជនម្តងទៀត ឬប្ដូរកូដម៉ាស៊ីនបម្រើវិញ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំថែរក្សាការប្រែសម្រួលឲ្យត្រឹមត្រូវ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការខ្វះត្រឹមត្រូវខ្លះ។ ឯកសារដើមនៅភាសាដើម គួរត្រូវបានគិតជា​ប្រភពត្រឹមត្រូវបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញផ្នែកមនុស្សគឺជាជម្រើសដ៏ល្អបំផុត។ យើងមិនមានភារកិច្ចទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
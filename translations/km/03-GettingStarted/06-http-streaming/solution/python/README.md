# ការរត់គំរូនេះ

នេះជាវិធីរត់ម៉ាស៊ីនបម្រើ និងម៉ាស៊ីនអតិថិជន HTTP streaming ចាស់ៗ ផងដែរ MCP streaming server និង client ដោយប្រើ Python។

### រូបរាងទូទៅ

- អ្នកនឹងតំឡើងម៉ាស៊ីនបម្រើ MCP ដែលបញ្ចេញការជូនដំណឹងជាការរីកវឌ្ឍទៅម៉ាស៊ីនអតិថិជននៅពេលវាបណ្តោះអាសន្ននូវធាតុ។
- ម៉ាស៊ីនអតិថិជននឹងបង្ហាញការជូនដំណឹងគ្រប់យ៉ាងក្នុងពេលពិត។
- មេរៀននេះគ្របដណ្តប់លើការតំឡើងមុន អនុវត្ត ការរត់ និងដោះស្រាយបញ្ហា។

### លក្ខខណ្ឌមុន

- Python 3.9 ឬថ្មីជាងនេះ
- បណ្ណាល័យ Python `mcp` (តំឡើងដោយ `pip install mcp`)

### ការតំឡើង និង ការតម្លើង

1. ចម្លងគម្រោងឬទាញយកឯកសារជាដុំ។

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **បង្កើត និង បើកបរិស្ថានវើឆួល (virtual environment) (ផ្តល់អនុសាសន៍):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **តំឡើងផ្នែកអាស្រ័យពាក់ព័ន្ធដែលបានតម្រូវ:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ឯកសារ

- **ម៉ាស៊ីនបម្រើ:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **ម៉ាស៊ីនអតិថិជន:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### ការរត់ម៉ាស៊ីនបម្រើ HTTP Streaming ចាស់ៗ

1. ធ្វើដំណើរក្នុងថតដំណោះស្រាយ:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. ចាប់ផ្តើមម៉ាស៊ីនបម្រើ HTTP streaming ចាស់ៗ:

   ```pwsh
   python server.py
   ```

3. ម៉ាស៊ីនបម្រើនឹងចាប់ផ្តើម និងបង្ហាញ៖

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ការរត់ម៉ាស៊ីនអតិថិជន HTTP Streaming ចាស់ៗ

1. បើកterminal ថ្មីមួយ (បើកបរិស្ថានវើឆួល និងថតដើមដដែល):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. អ្នកគួរត្រូវបានឃើញសារ ដែលបញ្ជូនចេញរៀងរាល់ពេល:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### ការរត់ម៉ាស៊ីនបម្រើ MCP Streaming

1. ធ្វើដំណើរក្នុងថតដំណោះស្រាយ:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. ចាប់ផ្តើមម៉ាស៊ីនបម្រើ MCP ជាមួយការផ្ទុកបញ្ជូន streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. ម៉ាស៊ីនបម្រើនឹងចាប់ផ្តើម និងបង្ហាញ:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### ការរត់ម៉ាស៊ីនអតិថិជន MCP Streaming

1. បើក terminal ថ្មី (បើកបរិស្ថានវើឆួល និងថតដើមដដែល):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. អ្នកគួរត្រូវបានឃើញការជូនដំណឹងនៅពេលពិតបន្ទាន់ ពេលម៉ាស៊ីនបម្រើកំពុងដំណើរការ​ធាតុ​ទាំងអស់:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### ជំហានអនុវត្តសំខាន់ៗ

1. **បង្កើតម៉ាស៊ីនបម្រើ MCP ដោយប្រើ FastMCP។**
2. **កំណត់ឧបករណ៍ដើម្បីដំណើរការបញ្ជី និងផ្ញើការជូនដំណឹងដោយប្រើ `ctx.info()` ឬ `ctx.log()`។**
3. **រត់ម៉ាស៊ីនបម្រើជាមួយ `transport="streamable-http"`។**
4. **អនុវត្តម៉ាស៊ីនអតិថិជនដោយមានអ្នកដំណោះស្រាយសារដើម្បីបង្ហាញការជូនដំណឹងពេលវាមកដល់។**

### ការដើរតួរលើកូដ
- ម៉ាស៊ីនបម្រើប្រើមុខងារ async និង context MCP ដើម្បីផ្ញើការអាប់ដេតអំពីការរីកចម្រើន។
- ម៉ាស៊ីនអតិថិជនអនុវត្តអ្នកដំណោះស្រាយសារដោយ async ដើម្បីបោះពុម្ពការជូនដំណឹង និងលទ្ធផលចុងក្រោយ។

### កំប្លែង និង ដោះស្រាយបញ្ហា

- ប្រើ `async/await` សម្រាប់ប្រតិបត្តិការដែលមិនអស់ការឆ្លងកាត់។
- តែងតែដោះស្រាយករណីកំហុសទាំងម៉ាស៊ីនបម្រើ និងម៉ាស៊ីនអតិថិជនសម្រាប់ភាពរឹងមាំ។
- ពិសោធន៍ជាមួយម៉ាស៊ីនអតិថិជនច្រើនដើម្បីមើលការអាប់ដេតពេលពិត។
- ប្រសិនបើប្រឈមមុខកំហុស សូមពិនិត្យកំណែ Python និងប្រាកដថាផ្នែកអាស្រ័យពាក់ព័ន្ធបានតំឡើងរួច។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបញ្ជាក់** ៖  
ឯកសារនេះត្រូវបានបញ្ចូលបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខិតខំប្រឹងប្រែងឱ្យបានភាពត្រឹមត្រូវ ក៏សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាជាតិនៃវាគួរត្រូវបានយកជាគម្រោងផ្លូវការពិតប្រាកដ។ សម្រាប់ព័ត៌មានដ៏សំខាន់ ការបកប្រែដោយមនុស្សជំនាញសមរម្យណែនាំបានល្អបំផុត។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ខុស ឬការបកស្រាយមិនត្រឹមត្រូវណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
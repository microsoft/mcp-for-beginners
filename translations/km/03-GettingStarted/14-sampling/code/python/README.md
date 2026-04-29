# ប្រតិបត្តិការសំណុំឧទាហរណ៍

## បង្កើតបរិបទពិភព مجازي

```sh
python -m venv venv
source ./venv/bin/activate
```

## តំឡើងការពឹងផ្អែក

```sh
pip install "mcp[cli]"
```

## ប្រតិបត្តិម៉ាស៊ីន​បម្រើ

```sh
uvicorn server:app --port 8000
```

## សាកល្បងម៉ាស៊ីន​បម្រើ​ជាមួយ GitHub Copilot និង VS Code

បន្ថែមចំណុចចូលទៅក្នុង mcp.json ដូច្នេះ៖

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

ប្រាកដថា​អ្នក​ចុច "start" លើម៉ាស៊ីន​បម្រើ។

នៅក្នុង GitHub Copilot ដាក់ស្នើនូវសំណើដូចខាងក្រោម៖

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

លើកដំបូង អ្នក​នឹងត្រូវបានស្នើឲ្យយល់ព្រមនឹងសកម្មភាព Sampling រួចបន្ទាប់មកអ្នកនឹងត្រូវបានស្នើឲ្យយល់ព្រមឲ្យឧបករណ៍រត់ "create_blog"។ អ្នកគួរតែឃើញការឆ្លើយតបដូចជា៖

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំធ្វើឲ្យបានត្រឹមត្រូវ សូមព្យាយាមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬការមិនពិតប្រាកដ។ ឯកសារដើមក្នុងភាសាព្យាង្គរបស់វាគួរត្រូវបានគេយកជាមូលដ្ឋានដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឲ្យអ្នកប្រើប្រាស់ការបកប្រែដោយអ្នកមានជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
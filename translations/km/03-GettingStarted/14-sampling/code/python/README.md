# រត់គំរូ

> [!WARNING]
> គំរូនេះប្រើ Sampling ដែលបានឃាត់ចោល និង endpoint HTTP+SSE បែបទំនើប។ វាត្រូវបាន
> រក្សាទុកសម្រាប់ការចក្ខុមែន MCP `2025-11-25` ។ ការអនុវត្តថ្មីគួរត្រូវហៅ
> អ្នកផ្គត់ផ្គង់ LLM ផ្ទាល់ និងប្រើ Streamable HTTP សម្រាប់ចរាចរណ៍ MCP ឆ្ងាយ។

## បង្កើតបរិយាកាសវែរជារឹម

```sh
python -m venv venv
source ./venv/bin/activate
```

## តំឡើងកម្រិតការពាក់ព័ន្ធ

```sh
pip install "mcp[cli]"
```

## រត់ម៉ាស៊ីនបម្រើ

```sh
uvicorn server:app --port 8000
```

## សាកល្បងម៉ាស៊ីនបម្រើជាមួយ GitHub Copilot និង VS Code

បន្ថែមវា​ចូល​ទៅ mcp.json ដូច្នេះៈ

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

ត្រូវប្រាកដថាអ្នកចុច "start" នៅលើម៉ាស៊ីនបម្រើ។

នៅក្នុង GitHub Copilot បិទសារដូចខាងក្រោម៖

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

ពេលដំបូងអ្នកនឹងត្រូវបានសួរថាតើទទួលសកម្មភាព Sampling ឬអត់ បន្ទាប់មកអ្នកនឹងត្រូវបានសួរឲ្យទទួលឧបករណ៍ដើម្បីរត់ "create_blog"។ អ្នកគួរតែឃើញចម្លើយដូចខាងក្រោមៈ

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
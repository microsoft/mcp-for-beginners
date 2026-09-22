# ការបញ្ជូលឧទាហរណ៍នេះ

អ្នកត្រូវបានផ្តល់អនុសាសន៍ឲ្យដំឡើង `uv` ប៉ុន្តែមិនចាំបាច់ទេ សូមមើល [សេចក្តីណែនាំ](https://docs.astral.sh/uv/#highlights)

## -0- បង្កើតបរិយាកាសវើឌ្វូល

```bash
python -m venv venv
```

## -1- បើកបរិយាកាសវើឌ្វូល

```bash
venv\Scripts\activate
```

## -2- ដំឡើងការពឹងផ្អែក

```bash
pip install "mcp[cli]"
```

## -3- ប្រតិបត្តិឧទាហរណ៍

```bash
python client.py
```

អ្នកគួរតែឃើញការបញ្ចូលដែលស្រដៀងនឹង៖

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
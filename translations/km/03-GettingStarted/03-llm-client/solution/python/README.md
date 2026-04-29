# រត់ឧទាហរណ៍នេះ

អ្នកត្រូវបានណែនាំឱ្យដំឡើង `uv` ប៉ុន្តែវាមិនបាច់ទេ មើល [បទបញ្ជា](https://docs.astral.sh/uv/#highlights)

## -0- បង្កើតបរិវេណមួយ

```bash
python -m venv venv
```

## -1- បើកបរិវេណ

```bash
venv\Scrips\activate
```

## -2- ដំឡើងការពឹងផ្អែក

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- រត់ឧទាហរណ៍


```bash
python client.py
```

អ្នកគួរតែឃើញលទ្ធផលឆ្លើយតបដូចជា៖

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវខ្លះៗ។ ឯកសារដើមក្នុងភាសាមាតុភូមិគួរត្រូវបានគិតថាជាមូលដ្ឋានអំពើផ្លូវការជាក់លាក់។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សអ្នកជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
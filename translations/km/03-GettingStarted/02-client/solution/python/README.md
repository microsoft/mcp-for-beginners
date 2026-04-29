# កំពុងដំណើរការឧទាហរណ៍នេះ

អ្នកត្រូវបានផ្តល់អនុសាសន៍ឱ្យដំឡើង `uv` ប៉ុន្តែមិនបាច់ ទស្សនា [សេចក្តីណែនាំ](https://docs.astral.sh/uv/#highlights)

## -0- បង្កើតបរិស្ថានវីរុចវៈ

```bash
python -m venv venv
```

## -1- បើកបរិស្ថានវីរុចវៈ

```bash
venv\Scrips\activate
```

## -2- ដំឡើងការពឹងផ្អែក

```bash
pip install "mcp[cli]"
```

## -3- បើករត់ឧទាហរណ៍


```bash
python client.py
```

អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានប្រែសម្រួលដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំប្រឹងប្រែងដល់ភាពត្រឹមត្រូវ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងខ្លះទំនងជាកាន់នូវកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមដែលមានភាសាម្ដងគួរត្រូវបានពិចារណាជាអ្នកដទៃដ៏មានសិទ្ធិលើតម្លៃសម្រួល។ ចំពោះព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការវិភាគខុសប្រហាក់ប្រហែលណាមួយដែលកើតមានពីការប្រើប្រាស់ប្រែសម្រួលនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
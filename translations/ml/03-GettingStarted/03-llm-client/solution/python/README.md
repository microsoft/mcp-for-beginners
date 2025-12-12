<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "24531f2b6b0f7fa3839accf4dc10088a",
  "translation_date": "2025-12-11T12:56:36+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/python/README.md",
  "language_code": "ml"
}
-->
# ഈ സാമ്പിൾ പ്രവർത്തിപ്പിക്കൽ

നിങ്ങൾക്ക് `uv` ഇൻസ്റ്റാൾ ചെയ്യാൻ ശുപാർശ ചെയ്യുന്നു, പക്ഷേ അത് നിർബന്ധമല്ല, [നിർദ്ദേശങ്ങൾ](https://docs.astral.sh/uv/#highlights) കാണുക

## -0- ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക

```bash
python -m venv venv
```

## -1- വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കുക

```bash
venv\Scrips\activate
```

## -2- ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക


```bash
python client.py
```

നിങ്ങൾക്ക് താഴെപോലുള്ള ഔട്ട്പുട്ട് കാണാം:

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
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
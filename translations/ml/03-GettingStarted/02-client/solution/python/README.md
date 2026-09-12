# ഈ സാമ്പിൾ പ്രവർത്തിപ്പിക്കൽ

നിങ്ങളോട് `uv` ഇൻസ്റ്റാൾ ചെയ്യാൻ ശുപാർശ ചെയ്യുന്നു, പക്ഷേ അതുണ്ടാകേണ്ടതില്ല, [നിർദ്ദേശങ്ങൾ](https://docs.astral.sh/uv/#highlights) കാണുക

## -0- ഒരു വെർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക

```bash
python -m venv venv
```

## -1- വെർച്വൽ എൻവയോൺമെന്റ് പ്രവർത്തിപ്പിക്കുക

```bash
venv\Scripts\activate
```

## -2- ആവശ്യമായ പാക്കേജുകൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install "mcp[cli]"
```

## -3- സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക

```bash
python client.py
```

നിങ്ങൾക്ക് താഴെപ്പറയുന്ന രീതിയിലുള്ള ഔട്ട്പുട്ട് കാണാമാകുന്നു:

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
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
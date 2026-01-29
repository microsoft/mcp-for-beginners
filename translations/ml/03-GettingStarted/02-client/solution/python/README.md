# ഈ സാമ്പിൾ പ്രവർത്തിപ്പിക്കൽ

നിങ്ങൾക്ക് `uv` ഇൻസ്റ്റാൾ ചെയ്യാൻ ശുപാർശ ചെയ്യപ്പെടുന്നു, പക്ഷേ അത് നിർബന്ധമല്ല, [നിർദ്ദേശങ്ങൾ](https://docs.astral.sh/uv/#highlights) കാണുക

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
```

## -3- സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക


```bash
python client.py
```

നിങ്ങൾക്ക് താഴെപോലൊരു ഔട്ട്പുട്ട് കാണാം:

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
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# हा नमुना चालवणे

तुम्हाला `uv` इन्स्टॉल करण्याची शिफारस केली जाते, पण ते आवश्यक नाही, पाहा [सूचना](https://docs.astral.sh/uv/#highlights)

## -0- एक वर्चुअल एन्व्हायर्नमेंट तयार करा

```bash
python -m venv venv
```

## -1- वर्चुअल एन्व्हायर्नमेंट सक्रिय करा

```bash
venv\Scrips\activate
```

## -2- अवलंबित्वे इन्स्टॉल करा

```bash
pip install "mcp[cli]"
```

## -3- नमुना चालवा

```bash
python client.py
```

तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

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

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
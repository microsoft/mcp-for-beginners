# हा नमुना चालवित आहे

`uv` इंस्टॉल करण्याची शिफारस केली जाते पण ते आवश्यक नाही, पहा [सूचना](https://docs.astral.sh/uv/#highlights)

## -0- एक आभासी वातावरण तयार करा

```bash
python -m venv venv
```

## -1- आभासी वातावरण सक्रिय करा

```bash
venv\Scripts\activate
```

## -2- अवलंबित्वे इंस्टॉल करा

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
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
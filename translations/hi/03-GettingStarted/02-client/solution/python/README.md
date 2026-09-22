# इस उदाहरण को चलाना

आपको `uv` स्थापित करने की सलाह दी जाती है लेकिन यह अनिवार्य नहीं है, देखें [निर्देश](https://docs.astral.sh/uv/#highlights)

## -0- एक वर्चुअल वातावरण बनाएं

```bash
python -m venv venv
```

## -1- वर्चुअल वातावरण सक्रिय करें

```bash
venv\Scripts\activate
```

## -2- निर्भरताएँ स्थापित करें

```bash
pip install "mcp[cli]"
```

## -3- उदाहरण चलाएं

```bash
python client.py
```

आपको इस प्रकार का आउटपुट दिखाई देना चाहिए:

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
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
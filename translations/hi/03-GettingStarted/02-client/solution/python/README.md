# इस सैंपल को चलाना

आपको `uv` इंस्टॉल करने की सलाह दी जाती है लेकिन यह जरूरी नहीं है, देखें [instructions](https://docs.astral.sh/uv/#highlights)

## -0- एक वर्चुअल एनवायरनमेंट बनाएं

```bash
python -m venv venv
```

## -1- वर्चुअल एनवायरनमेंट को सक्रिय करें

```bash
venv\Scrips\activate
```

## -2- निर्भरताएँ इंस्टॉल करें

```bash
pip install "mcp[cli]"
```

## -3- सैंपल चलाएं

```bash
python client.py
```

आपको इस तरह का आउटपुट दिखना चाहिए:

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
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
# नमूना चलाएं

## वर्चुअल वातावरण सेट करें

```sh
python -m venv venv
source ./venv/bin/activate
```

## निर्भरताएँ स्थापित करें

```sh
pip install "mcp[cli]"
```

## कोड चलाएं

```sh
python client.py
```

आपको यह टेक्स्ट दिखाई देना चाहिए:

```text
Available tools: ['add']
Result of add tool: meta=None content=[TextContent(type='text', text='8.0', annotations=None, meta=None)] structuredContent=None isError=False
```

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
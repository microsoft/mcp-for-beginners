# इस सैंपल को चलाना

इस सैंपल में क्लाइंट पर एक LLM शामिल है। LLM को काम करने के लिए आपको इसे Codespaces में चलाना होगा या GitHub में एक पर्सनल एक्सेस टोकन सेटअप करना होगा।

## -1- डिपेंडेंसीज़ इंस्टॉल करें

```bash
npm install
```

## -3- सर्वर चलाएं

```bash
npm run build
```

## -4- क्लाइंट चलाएं

```sh
npm run client
```

आपको इस तरह का परिणाम दिखना चाहिए:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
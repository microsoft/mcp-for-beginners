# इस सैंपल को चलाना

यहां बताया गया है कि क्लासिक HTTP स्ट्रीमिंग सर्वर और क्लाइंट, साथ ही MCP स्ट्रीमिंग सर्वर और क्लाइंट को Python का उपयोग करके कैसे चलाना है।

### अवलोकन

- आप एक MCP सर्वर सेटअप करेंगे जो आइटम्स को प्रोसेस करते समय प्रोग्रेस नोटिफिकेशन क्लाइंट को स्ट्रीम करेगा।
- क्लाइंट प्रत्येक नोटिफिकेशन को रीयल-टाइम में प्रदर्शित करेगा।
- यह गाइड प्रीरेक्विज़िट्स, सेटअप, रनिंग और ट्रबलशूटिंग को कवर करता है।

### आवश्यकताएँ

- Python 3.9 या नया संस्करण
- `mcp` Python पैकेज (इंस्टॉल करें `pip install mcp` के साथ)

### इंस्टॉलेशन और सेटअप

1. रिपॉजिटरी को क्लोन करें या सॉल्यूशन फाइल्स डाउनलोड करें।

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **एक वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें (सिफारिश की जाती है):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **आवश्यक डिपेंडेंसीज़ इंस्टॉल करें:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### फाइलें

- **सर्वर:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **क्लाइंट:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### क्लासिक HTTP स्ट्रीमिंग सर्वर चलाना

1. सॉल्यूशन डायरेक्टरी पर जाएं:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. क्लासिक HTTP स्ट्रीमिंग सर्वर शुरू करें:

   ```pwsh
   python server.py
   ```

3. सर्वर शुरू होगा और यह प्रदर्शित करेगा:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### क्लासिक HTTP स्ट्रीमिंग क्लाइंट चलाना

1. एक नया टर्मिनल खोलें (उसी वर्चुअल एनवायरनमेंट और डायरेक्टरी को सक्रिय करें):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. आपको क्रमिक रूप से स्ट्रीम किए गए संदेश दिखाई देंगे:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP स्ट्रीमिंग सर्वर चलाना

1. सॉल्यूशन डायरेक्टरी पर जाएं:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP सर्वर को स्ट्रीमेबल-HTTP ट्रांसपोर्ट के साथ शुरू करें:
   ```pwsh
   python server.py mcp
   ```
3. सर्वर शुरू होगा और यह प्रदर्शित करेगा:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP स्ट्रीमिंग क्लाइंट चलाना

1. एक नया टर्मिनल खोलें (उसी वर्चुअल एनवायरनमेंट और डायरेक्टरी को सक्रिय करें):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. जैसे ही सर्वर प्रत्येक आइटम को प्रोसेस करेगा, आपको रीयल-टाइम में नोटिफिकेशन दिखाई देंगे:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### मुख्य कार्यान्वयन चरण

1. **FastMCP का उपयोग करके MCP सर्वर बनाएं।**
2. **एक टूल परिभाषित करें जो एक सूची को प्रोसेस करता है और `ctx.info()` या `ctx.log()` का उपयोग करके नोटिफिकेशन भेजता है।**
3. **सर्वर को `transport="streamable-http"` के साथ चलाएं।**
4. **एक क्लाइंट को लागू करें जिसमें एक मैसेज हैंडलर हो जो नोटिफिकेशन को उनके आने पर प्रदर्शित करे।**

### कोड वॉकथ्रू

- सर्वर प्रोग्रेस अपडेट भेजने के लिए async फंक्शन्स और MCP कॉन्टेक्स्ट का उपयोग करता है।
- क्लाइंट नोटिफिकेशन और अंतिम परिणाम को प्रिंट करने के लिए एक async मैसेज हैंडलर को लागू करता है।

### टिप्स और ट्रबलशूटिंग

- नॉन-ब्लॉकिंग ऑपरेशन्स के लिए `async/await` का उपयोग करें।
- सर्वर और क्लाइंट दोनों में एक्सेप्शन्स को संभालें ताकि सिस्टम मजबूत बना रहे।
- रीयल-टाइम अपडेट देखने के लिए कई क्लाइंट्स के साथ टेस्ट करें।
- यदि आपको त्रुटियां मिलती हैं, तो अपने Python संस्करण की जांच करें और सुनिश्चित करें कि सभी डिपेंडेंसीज़ इंस्टॉल हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में लिखा गया मूल दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
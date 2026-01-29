# यो नमूना चलाउनुहोस्

क्लासिक HTTP स्ट्रिमिङ सर्भर र क्लाइन्ट, साथै MCP स्ट्रिमिङ सर्भर र क्लाइन्ट Python प्रयोग गरेर कसरी चलाउने भन्ने यहाँ विवरण छ।

### अवलोकन

- तपाईंले एउटा MCP सर्भर सेटअप गर्नुहुनेछ जसले वस्तुहरू प्रक्रिया गर्दा क्लाइन्टलाई प्रगति सूचनाहरू स्ट्रिम गर्दछ।
- क्लाइन्टले प्रत्येक सूचनालाई वास्तविक समयमा प्रदर्शन गर्नेछ।
- यो गाइडले पूर्वापेक्षा, सेटअप, चलाउने प्रक्रिया, र समस्या समाधान समेट्छ।

### पूर्वापेक्षा

- Python 3.9 वा नयाँ संस्करण
- `mcp` Python प्याकेज (`pip install mcp` प्रयोग गरेर स्थापना गर्नुहोस्)

### स्थापना र सेटअप

1. रिपोजिटरी क्लोन गर्नुहोस् वा समाधान फाइलहरू डाउनलोड गर्नुहोस्।

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **भर्चुअल वातावरण सिर्जना र सक्रिय गर्नुहोस् (सिफारिस गरिन्छ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **आवश्यक निर्भरता स्थापना गर्नुहोस्:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### फाइलहरू

- **सर्भर:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **क्लाइन्ट:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### क्लासिक HTTP स्ट्रिमिङ सर्भर चलाउने

1. समाधान डाइरेक्टरीमा जानुहोस्:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. क्लासिक HTTP स्ट्रिमिङ सर्भर सुरु गर्नुहोस्:

   ```pwsh
   python server.py
   ```

3. सर्भर सुरु हुनेछ र निम्न देखाउनेछ:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### क्लासिक HTTP स्ट्रिमिङ क्लाइन्ट चलाउने

1. नयाँ टर्मिनल खोल्नुहोस् (उही भर्चुअल वातावरण र डाइरेक्टरी सक्रिय गर्नुहोस्):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. तपाईंले क्रमिक रूपमा स्ट्रिम गरिएको सन्देशहरू देख्नुहुनेछ:

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

### MCP स्ट्रिमिङ सर्भर चलाउने

1. समाधान डाइरेक्टरीमा जानुहोस्:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP सर्भर `streamable-http` ट्रान्सपोर्टको साथ सुरु गर्नुहोस्:
   ```pwsh
   python server.py mcp
   ```
3. सर्भर सुरु हुनेछ र निम्न देखाउनेछ:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP स्ट्रिमिङ क्लाइन्ट चलाउने

1. नयाँ टर्मिनल खोल्नुहोस् (उही भर्चुअल वातावरण र डाइरेक्टरी सक्रिय गर्नुहोस्):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. तपाईंले सर्भरले प्रत्येक वस्तु प्रक्रिया गर्दा वास्तविक समयमा सूचनाहरू देख्नुहुनेछ:
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

### मुख्य कार्यान्वयन चरणहरू

1. **FastMCP प्रयोग गरेर MCP सर्भर सिर्जना गर्नुहोस्।**
2. **सूची प्रक्रिया गर्ने र `ctx.info()` वा `ctx.log()` प्रयोग गरेर सूचनाहरू पठाउने उपकरण परिभाषित गर्नुहोस्।**
3. **`transport="streamable-http"` प्रयोग गरेर सर्भर चलाउनुहोस्।**
4. **सूचनाहरू प्राप्त हुनेबित्तिकै प्रदर्शन गर्न सन्देश ह्यान्डलरको साथ क्लाइन्ट कार्यान्वयन गर्नुहोस्।**

### कोड वाकथ्रु
- सर्भरले असिंक्रोनस कार्यहरू र MCP सन्दर्भ प्रयोग गरेर प्रगति अपडेटहरू पठाउँछ।
- क्लाइन्टले सूचनाहरू प्रिन्ट गर्न र अन्तिम परिणाम प्रदर्शन गर्न असिंक्रोनस सन्देश ह्यान्डलर कार्यान्वयन गर्दछ।

### सुझावहरू र समस्या समाधान

- गैर-अवरोधक अपरेशनहरूको लागि `async/await` प्रयोग गर्नुहोस्।
- सर्भर र क्लाइन्ट दुवैमा अपवादहरू ह्यान्डल गर्नुहोस् ताकि प्रणाली मजबुत होस्।
- वास्तविक समय अपडेटहरू अवलोकन गर्न धेरै क्लाइन्टहरूसँग परीक्षण गर्नुहोस्।
- यदि त्रुटिहरू आउँछन् भने, आफ्नो Python संस्करण जाँच गर्नुहोस् र सबै निर्भरता स्थापना भएको सुनिश्चित गर्नुहोस्।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
# हे नमुना चालवणे

क्लासिक HTTP स्ट्रीमिंग सर्व्हर आणि क्लायंट तसेच MCP स्ट्रीमिंग सर्व्हर आणि क्लायंट Python वापरून कसे चालवायचे ते येथे दिले आहे.

### आढावा

- तुम्ही MCP सर्व्हर सेट अप कराल जो आयटम्स प्रक्रिया करत असताना क्लायंटला प्रगती सूचना स्ट्रीम करतो.
- क्लायंट प्रत्येक सूचना रिअल टाइममध्ये दाखवेल.
- या मार्गदर्शकात पूर्वतयारी, सेटअप, चालवणे आणि समस्या सोडवणे याचा समावेश आहे.

### पूर्वतयारी

- Python 3.9 किंवा त्याहून नवीन आवृत्ती
- `mcp` Python पॅकेज (इंस्टॉल करण्यासाठी `pip install mcp` वापरा)

### इंस्टॉलेशन आणि सेटअप

1. रेपॉझिटरी क्लोन करा किंवा सोल्यूशन फाइल्स डाउनलोड करा.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **व्हर्च्युअल एन्व्हायर्नमेंट तयार करा आणि सक्रिय करा (शिफारस केलेले):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **आवश्यक डिपेंडन्सी इंस्टॉल करा:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### फाइल्स

- **सर्व्हर:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **क्लायंट:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### क्लासिक HTTP स्ट्रीमिंग सर्व्हर चालवणे

1. सोल्यूशन डिरेक्टरीमध्ये जा:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. क्लासिक HTTP स्ट्रीमिंग सर्व्हर सुरू करा:

   ```pwsh
   python server.py
   ```

3. सर्व्हर सुरू होईल आणि खालीलप्रमाणे दिसेल:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### क्लासिक HTTP स्ट्रीमिंग क्लायंट चालवणे

1. नवीन टर्मिनल उघडा (समान व्हर्च्युअल एन्व्हायर्नमेंट आणि डिरेक्टरी सक्रिय करा):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. तुम्हाला स्ट्रीम केलेले संदेश क्रमाने प्रिंट होताना दिसतील:

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

### MCP स्ट्रीमिंग सर्व्हर चालवणे

1. सोल्यूशन डिरेक्टरीमध्ये जा:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP सर्व्हर `streamable-http` ट्रान्सपोर्टसह सुरू करा:
   ```pwsh
   python server.py mcp
   ```
3. सर्व्हर सुरू होईल आणि खालीलप्रमाणे दिसेल:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP स्ट्रीमिंग क्लायंट चालवणे

1. नवीन टर्मिनल उघडा (समान व्हर्च्युअल एन्व्हायर्नमेंट आणि डिरेक्टरी सक्रिय करा):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. तुम्हाला सर्व्हर प्रत्येक आयटम प्रक्रिया करत असताना सूचना रिअल टाइममध्ये प्रिंट होताना दिसतील:
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

### मुख्य अंमलबजावणी चरण

1. **FastMCP वापरून MCP सर्व्हर तयार करा.**
2. **सूचना पाठवण्यासाठी `ctx.info()` किंवा `ctx.log()` वापरून यादी प्रक्रिया करणारे टूल परिभाषित करा.**
3. **`transport="streamable-http"` वापरून सर्व्हर चालवा.**
4. **सूचना येताच दाखवण्यासाठी संदेश हँडलरसह क्लायंट अंमलात आणा.**

### कोड वॉकथ्रू

- सर्व्हर प्रगती अपडेट पाठवण्यासाठी async फंक्शन्स आणि MCP संदर्भ वापरतो.
- क्लायंट सूचना प्रिंट करण्यासाठी आणि अंतिम निकालासाठी async संदेश हँडलर अंमलात आणतो.

### टिप्स आणि समस्या सोडवणे

- नॉन-ब्लॉकिंग ऑपरेशन्ससाठी `async/await` वापरा.
- सर्व्हर आणि क्लायंटमध्ये अपवाद हाताळा जेणेकरून ते मजबूत राहतील.
- अनेक क्लायंटसह चाचणी करा आणि रिअल टाइम अपडेट्स पाहा.
- जर तुम्हाला त्रुटी आढळल्या तर तुमची Python आवृत्ती तपासा आणि सर्व डिपेंडन्सी इंस्टॉल झाल्या आहेत याची खात्री करा.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
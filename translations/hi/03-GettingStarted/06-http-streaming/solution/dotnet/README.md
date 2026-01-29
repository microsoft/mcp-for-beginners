# इस सैंपल को चलाना

## -1- डिपेंडेंसीज़ इंस्टॉल करें

```bash
dotnet restore
```

## -2- सैंपल चलाएं

```bash
dotnet run
```

## -3- सैंपल का परीक्षण करें

नीचे दिए गए कमांड को चलाने से पहले एक अलग टर्मिनल शुरू करें (सुनिश्चित करें कि सर्वर अभी भी चल रहा है)।

सर्वर को एक टर्मिनल में चलाते हुए, दूसरा टर्मिनल खोलें और निम्नलिखित कमांड चलाएं:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

यह एक वेब सर्वर शुरू करेगा जिसमें एक विज़ुअल इंटरफ़ेस होगा जो आपको सैंपल का परीक्षण करने की अनुमति देगा।

> सुनिश्चित करें कि **Streamable HTTP** को ट्रांसपोर्ट प्रकार के रूप में चुना गया है, और URL `http://localhost:3001/mcp` है।

एक बार सर्वर कनेक्ट हो जाए:

- टूल्स की सूची बनाने की कोशिश करें और `add` चलाएं, जिसमें आर्ग्स 2 और 4 हों, आपको परिणाम में 6 दिखना चाहिए।
- रिसोर्सेज और रिसोर्स टेम्पलेट पर जाएं और "greeting" कॉल करें, एक नाम टाइप करें और आपको उस नाम के साथ एक ग्रीटिंग दिखनी चाहिए जो आपने प्रदान किया है।

### CLI मोड में परीक्षण करना

आप इसे सीधे CLI मोड में निम्नलिखित कमांड चलाकर लॉन्च कर सकते हैं:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

यह सर्वर में उपलब्ध सभी टूल्स की सूची दिखाएगा। आपको निम्नलिखित आउटपुट दिखना चाहिए:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

किसी टूल को चलाने के लिए टाइप करें:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

आपको निम्नलिखित आउटपुट दिखना चाहिए:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> ब्राउज़र की तुलना में CLI मोड में इंस्पेक्टर चलाना आमतौर पर बहुत तेज़ होता है।
> इंस्पेक्टर के बारे में अधिक पढ़ें [यहां](https://github.com/modelcontextprotocol/inspector)।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
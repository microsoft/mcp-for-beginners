# नमूना चलाएँ

> [!WARNING]
> यह नमूना पुरानी Sampling और एक पुरानी HTTP+SSE endpoint का उपयोग करता है। इसे MCP `2025-11-25` संगतता के लिए रखा गया है। नई कार्यान्वयन सीधे LLM प्रदाता को कॉल करनी चाहिए और दूरस्थ MCP ट्रैफिक के लिए Streamable HTTP का उपयोग करना चाहिए।
> 
> 

## वर्चुअल वातावरण बनाएं

```sh
python -m venv venv
source ./venv/bin/activate
```

## निर्भरता स्थापित करें

```sh
pip install "mcp[cli]"
```

## सर्वर चलाएँ

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot और VS Code के साथ सर्वर का परीक्षण करें

mcp.json में इस प्रकार प्रविष्टि जोड़ें:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

सुनिश्चित करें कि आप सर्वर पर "start" पर क्लिक करें।

GitHub Copilot में निम्न प्रॉम्प्ट पेस्ट करें:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

पहली बार आपसे Sampling क्रिया स्वीकार करने के लिए पूछा जाएगा, फिर आपसे "create_blog" चलाने के लिए टूल स्वीकार करने को कहा जाएगा। आपको समान प्रतिक्रिया दिखनी चाहिए:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
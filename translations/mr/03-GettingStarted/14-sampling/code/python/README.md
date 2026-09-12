# नमुना चालवा

> [!WARNING]
> हा नमुना जुना Sampling आणि एक पारंपारिक HTTP+SSE एन्डपॉइंट वापरतो. हा
> MCP `2025-11-25` सुसंगततेसाठी राखून ठेवला आहे. नवीन अंमलबजावणीने थेट
> LLM प्रदात्याला कॉल करणे आणि रिमोट MCP ट्रॅफिकसाठी Streamable HTTP वापरणे आवश्यक आहे.

## आभासी वातावरण तयार करा

```sh
python -m venv venv
source ./venv/bin/activate
```

## अवलंबित्वे इंस्टॉल करा

```sh
pip install "mcp[cli]"
```

## सर्व्हर चालू करा

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot आणि VS Code सह सर्व्हर तपासा

mcp.json मध्ये खालील नोंद करा:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

हे निश्चित करा की तुम्ही सर्व्हरवर "start" बटणावर क्लिक केले आहे.

GitHub Copilot मध्ये पुढील प्रॉम्प्ट पेस्ट करा:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

प्रथमच तुम्हाला Sampling क्रिया स्वीकारायची आहे का ते विचारले जाईल, त्यानंतर "create_blog" चालवण्यासाठी साधन स्वीकारायचे का ते विचारले जाईल. तुम्हाला खालील प्रमाणे प्रतिसाद दिसेल:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
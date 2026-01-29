# हे नमुना चालवणे

## -1- आवश्यक गोष्टी स्थापित करा

```bash
dotnet restore
```

## -2- नमुना चालवा

```bash
dotnet run
```

## -3- नमुना तपासा

खालील चालवण्यापूर्वी स्वतंत्र टर्मिनल सुरू करा (सुनिश्चित करा की सर्व्हर चालू आहे).

सर्व्हर एका टर्मिनलमध्ये चालू असताना, दुसरे टर्मिनल उघडा आणि खालील कमांड चालवा:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

यामुळे एक वेब सर्व्हर सुरू होईल ज्यामध्ये नमुना तपासण्यासाठी व्हिज्युअल इंटरफेस उपलब्ध असेल.

> **Streamable HTTP** हा ट्रान्सपोर्ट प्रकार निवडल्याची खात्री करा, आणि URL `http://localhost:3001/mcp` आहे.

सर्व्हर कनेक्ट झाल्यावर:

- टूल्सची यादी करण्याचा प्रयत्न करा आणि `add` चालवा, args 2 आणि 4 सह, तुम्हाला निकालात 6 दिसेल.
- रिसोर्सेस आणि रिसोर्स टेम्पलेटला जा आणि "greeting" कॉल करा, नाव टाइप करा आणि तुम्ही दिलेल्या नावासह अभिवादन दिसेल.

### CLI मोडमध्ये तपासणी

CLI मोडमध्ये थेट सुरू करण्यासाठी खालील कमांड चालवा:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

यामुळे सर्व्हरमध्ये उपलब्ध असलेल्या सर्व टूल्सची यादी होईल. तुम्हाला खालील आउटपुट दिसेल:

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

टूल चालवण्यासाठी टाइप करा:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

तुम्हाला खालील आउटपुट दिसेल:

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
> CLI मोडमध्ये निरीक्षक चालवणे ब्राउझरपेक्षा सहसा खूप जलद असते.
> निरीक्षकाबद्दल अधिक वाचा [इथे](https://github.com/modelcontextprotocol/inspector).

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
# उदाहरण: मूलभूत होस्ट

एक संदर्भ अंमलबजावणी ज्यात दाखवले आहे की कसे एक MCP होस्ट अनुप्रयोग तयार करायचा जो MCP सर्व्हरशी जोडतो आणि सुरक्षित सॅंडबॉक्समध्ये टूल UI रेंडर करतो.

हा मूलभूत होस्ट स्थानिक विकासादरम्यान MCP अ‍ॅप्सची चाचणी करण्यासाठी देखील वापरला जाऊ शकतो.

## मुख्य फाईल्स

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - टूल निवड, पॅरामीटर इनपुट, आणि ifram व्यवस्थापनासह React UI होस्ट
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - सुरक्षा पडताळणी आणि द्विदिश संदेश प्रेषणासह बाह्य iframe प्रॉक्सी
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - मुख्य लॉजिक: सर्व्हर कनेक्शन, टूल कॉलिंग, आणि AppBridge सेटअप

## सुरूवात कशी करावी

```bash
npm install
npm run start
# उघडा http://localhost:8080
```

डीफॉल्टनुसार, होस्ट अनुप्रयोग `http://localhost:3001/mcp` या ठिकाणी MCP सर्व्हरशी कनेक्ट करण्याचा प्रयत्न करेल. तुम्ही `SERVERS` पर्यावरण चल सेट करून सर्व्हर URLs च्या JSON अर्रेने हा व्यवहार कॉन्फिगर करू शकता:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## आर्किटेक्चर

हे उदाहरण सुरक्षित UI पृथकीकरणासाठी डबल-iframe सॅंडबॉक्स पॅटर्न वापरते:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**का दोन iframes?**

- बाह्य iframe वेगळ्या ओरिजिनवर (पोर्ट 8081) चालतो जेणेकरून होस्टमध्ये थेट प्रवेश होऊ नये
- अंतर्गत iframe `srcdoc` द्वारे HTML प्राप्त करतो आणि सॅंडबॉक्स अॅट्रीब्यूट्सने मर्यादित आहे
- संदेश बाह्य iframe मधून प्रवाहित होतात ज्यात त्यांची पडताळणी केली जाते आणि द्विदिश रीतीने प्रेषित केली जातात

हे आर्किटेक्चर सुनिश्चित करते की जर टूल UI कोड हानिकारक असला तरीही, तो होस्ट अनुप्रयोगाच्या DOM, कुकीज किंवा JavaScript संदर्भात प्रवेश करू शकत नाही.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवेद्वारे [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आपण अचूकतेसाठी प्रयत्न करत असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जाणे आवश्यक आहे. महत्त्वाच्या माहितीच्या बाबतीत, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
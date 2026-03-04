# उदाहरण: बुनियादी होस्ट

एक संदर्भ कार्यान्वयन जो दिखाता है कि MCP सर्वर से कनेक्ट होने और सुरक्षित सैंडबॉक्स में टूल UI रेंडर करने वाला MCP होस्ट एप्लिकेशन कैसे बनाया जाए।

यह बुनियादी होस्ट स्थानीय विकास के दौरान MCP एप्लिकेशन का परीक्षण करने के लिए भी उपयोग किया जा सकता है।

## प्रमुख फाइलें

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - टूल चयन, पैरामीटर इनपुट, और iframe प्रबंधन के साथ React UI होस्ट
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - सुरक्षा सत्यापन और द्विदिश संदेश रिले के साथ बाहरी iframe प्रॉक्सी
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - मुख्य लॉजिक: सर्वर कनेक्शन, टूल कॉलिंग, और AppBridge सेटअप

## शुरुआत कैसे करें

```bash
npm install
npm run start
# खोलें http://localhost:8080
```

डिफ़ॉल्ट रूप में, होस्ट एप्लिकेशन `http://localhost:3001/mcp` पर MCP सर्वर से कनेक्ट करने का प्रयास करेगा। आप इस व्यवहार को `SERVERS` पर्यावरण चर को सर्वर URL की JSON सरणी सेट करके कॉन्फ़िगर कर सकते हैं:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## वास्तुकला

यह उदाहरण सुरक्षित UI पृथक्करण के लिए डबल-iframe सैंडबॉक्स पैटर्न का उपयोग करता है:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**दो iframes क्यों?**

- बाहरी iframe अलग मूल (पोर्ट 8081) पर चलता है जो होस्ट तक सीधे पहुंच को रोकता है
- भीतरी iframe `srcdoc` के माध्यम से HTML प्राप्त करता है और सैंडबॉक्स गुणों द्वारा प्रतिबंधित होता है
- संदेश बाहरी iframe के माध्यम से प्रवाहित होते हैं जो उन्हें सत्यापित और द्विदिश रूप से रिले करता है

यह वास्तुकला सुनिश्चित करती है कि भले ही टूल UI कोड दुर्भावनापूर्ण हो, यह होस्ट एप्लिकेशन के DOM, कुकीज़, या जावास्क्रिप्ट संदर्भ तक पहुँच नहीं सकता।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियां या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
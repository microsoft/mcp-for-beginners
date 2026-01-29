# नमूना चलाएं

## डिपेंडेंसी इंस्टॉल करें

```sh
npm install
```

## बिल्ड करें

```sh
npm run build
```

## टोकन जनरेट करें

```sh
npm run generate
```

यह एक टोकन को *.env* फाइल में बनाता है। क्लाइंट इस फाइल से पढ़ेगा।

## कोड चलाएं

सर्वर शुरू करें:

```sh
npm start
```

क्लाइंट को एक अलग टर्मिनल में चलाएं:

```sh
npm run client
```

सर्वर के टर्मिनल में आपको कुछ ऐसा आउटपुट दिखना चाहिए:

```text
User exists
User has required scopes
Middleware executed
```

और क्लाइंट टर्मिनल में आपको कुछ ऐसा आउटपुट दिखना चाहिए:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### चीजें बदलना

आइए सुनिश्चित करें कि हम स्कोप को समझते हैं। *server.ts* फाइल को ढूंढें और यह कोड देखें:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

यह कहता है कि पास किया गया टोकन "User.Read" होना चाहिए। इसे "User.Write" में बदलें। अब `npm run build` चलाएं और सर्वर को फिर से शुरू करें `npm start`। अब आपको ऑथ फेल होते हुए दिखना चाहिए क्योंकि हमारे पास यह स्कोप नहीं है (हमारे पास User.Read और Admin.Write है):

अब क्लाइंट कहता है

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

और आप सर्वर टर्मिनल में देख सकते हैं कि यह कहता है:

```text
User exists
```

और यह इस बिंदु से आगे नहीं बढ़ता।

या तो इस स्कोप "User.Write" को जोड़ें और `npm run generate` चलाएं और क्लाइंट को फिर से चलाएं, या सर्वर कोड को वापस बदल दें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
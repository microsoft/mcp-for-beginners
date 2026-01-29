# नमुना चालवा

## आवश्यक गोष्टी स्थापित करा

```sh
npm install
```

## तयार करा

```sh
npm run build
```

## टोकन्स तयार करा

```sh
npm run generate
```

यामुळे *.env* फाइलमध्ये एक टोकन तयार होते. क्लायंट या फाइलमधून वाचेल.

## कोड चालवा

सर्व्हर सुरू करण्यासाठी:

```sh
npm start
```

क्लायंट चालवा, वेगळ्या टर्मिनलमध्ये:

```sh
npm run client
```

सर्व्हरच्या टर्मिनलमध्ये तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

```text
User exists
User has required scopes
Middleware executed
```

आणि क्लायंटच्या टर्मिनलमध्ये तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### बदल करणे

चला, आपण स्कोप्स समजून घेऊया. *server.ts* फाइल शोधा आणि हा कोड पहा:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

याचा अर्थ दिलेले टोकन "User.Read" असणे आवश्यक आहे, चला ते "User.Write" मध्ये बदलूया. आता `npm run build` चालवा आणि सर्व्हर पुन्हा सुरू करा `npm start`. आता तुम्हाला ऑथ फेल झाल्याचे दिसेल कारण आमच्याकडे हा स्कोप नाही (आमच्याकडे User.Read आणि Admin.Write आहे):

क्लायंट आता असे म्हणतो

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

आणि तुम्ही सर्व्हरच्या टर्मिनलमध्ये पाहू शकता की ते असे म्हणते:

```text
User exists
```

आणि ते यापुढे जात नाही.

तर, "User.Write" स्कोप जोडा आणि `npm run generate` चालवा आणि क्लायंट पुन्हा चालवा किंवा सर्व्हर कोड परत बदला.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.
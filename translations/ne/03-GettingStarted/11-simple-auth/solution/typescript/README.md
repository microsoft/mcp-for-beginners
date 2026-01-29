# नमूना चलाउनुहोस्

## निर्भरता स्थापना गर्नुहोस्

```sh
npm install
```

## निर्माण गर्नुहोस्

```sh
npm run build
```

## टोकनहरू उत्पन्न गर्नुहोस्

```sh
npm run generate
```

यसले *.env* फाइलमा टोकन सिर्जना गर्दछ। क्लाइन्टले यो फाइलबाट पढ्नेछ।

## कोड चलाउनुहोस्

सर्भर सुरु गर्न:

```sh
npm start
```

क्लाइन्ट चलाउनुहोस्, अर्को टर्मिनलमा:

```sh
npm run client
```

सर्भरको टर्मिनलमा, तपाईंले निम्न जस्तै आउटपुट देख्नुहुनेछ:

```text
User exists
User has required scopes
Middleware executed
```

र क्लाइन्ट टर्मिनलबाट, तपाईंले निम्न जस्तै आउटपुट देख्नुहुनेछ:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### परिवर्तनहरू गर्नुहोस्

आउनुहोस्, हामी स्कोपहरू बुझौं। *server.ts* फाइल खोज्नुहोस् र यो कोड हेर्नुहोस्:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

यसले भन्छ कि पास गरिएको टोकनमा "User.Read" हुनुपर्छ, आउनुहोस् यसलाई "User.Write" मा परिवर्तन गरौं। अब `npm run build` चलाउनुहोस् र सर्भरलाई पुनः सुरु गर्नुहोस् `npm start`। अब तपाईंले देख्नुहुनेछ कि प्रमाणीकरण असफल भयो किनकि हामीसँग यो स्कोप छैन (हामीसँग User.Read र Admin.Write छ):

क्लाइन्टले अब भन्छ

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

र तपाईं सर्भर टर्मिनलमा देख्न सक्नुहुन्छ कि यसले भन्छ:

```text
User exists
```

र यो यस बिन्दु भन्दा अगाडि जान सक्दैन।

या त यो स्कोप "User.Write" थप्नुहोस् र `npm run generate` चलाउनुहोस् र क्लाइन्टलाई पुनः चलाउनुहोस् अथवा सर्भर कोडलाई फिर्ता परिवर्तन गर्नुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।
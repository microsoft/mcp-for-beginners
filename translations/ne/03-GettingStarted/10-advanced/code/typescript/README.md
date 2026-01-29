# नमूना चलाउनुहोस्

## आवश्यकताहरू स्थापना गर्नुहोस्

```sh
npm install
```

## निर्माण गर्नुहोस्

```sh
npm run build
```

## चलाउनुहोस्

```sh
npm start
```

तपाईंले यो पाठ देख्नु पर्नेछ:

```text
Registering tools...
Starting server...
```

धेरै राम्रो, यसको मतलब यो सही रूपमा सुरु भएको छ।

## सर्भर परीक्षण गर्नुहोस्

निम्न आदेशको साथ क्षमताहरू परीक्षण गर्नुहोस्:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

यसले निरीक्षक उपकरणको वेब इन्टरफेस सुरु गर्नेछ।

### CLI मोडमा परीक्षण गर्नुहोस्

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

तपाईंले निम्न आउटपुट देख्नु पर्नेछ:

```json
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    },
    {
      "name": "subtract",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    }
  ]
}
```

एउटा उपकरण चलाउनुहोस्:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

तपाईंले निम्न जस्तै प्रतिक्रिया देख्नु पर्नेछ:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" जस्तो अस्तित्वमा नभएको उपकरण परीक्षण गर्न प्रयास गर्नुहोस् यो आदेशको साथ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

अब तपाईंले यो सन्देश देख्नु पर्नेछ जसले तपाईंको मान्यकरण काम गरिरहेको देखाउँछ:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

त्यसैगरी, स्किमाले अस्वीकार गर्नुपर्ने `c` नामक प्यारामिटर पठाउने प्रयास गर्नुहोस् यसरी:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

अब तपाईंले "अवैध तर्कहरू" त्रुटि देख्नु पर्नेछ:

```text
{
  "content": [],
  "error": {
    "code": "invalid_arguments",
    "message": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
  }
}
```

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
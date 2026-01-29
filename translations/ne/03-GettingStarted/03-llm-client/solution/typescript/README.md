# यो नमुना चलाउँदै

यो नमुनामा क्लाइन्टमा LLM राखिएको छ। LLM ले तपाईंलाई यो Codespaces मा चलाउन वा GitHub मा व्यक्तिगत पहुँच टोकन सेटअप गर्न आवश्यक पर्छ।

## -1- निर्भरता स्थापना गर्नुहोस्

```bash
npm install
```

## -3- सर्भर चलाउनुहोस्

```bash
npm run build
```

## -4- क्लाइन्ट चलाउनुहोस्

```sh
npm run client
```

तपाईंले यसै जस्तो परिणाम देख्नु पर्नेछ:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
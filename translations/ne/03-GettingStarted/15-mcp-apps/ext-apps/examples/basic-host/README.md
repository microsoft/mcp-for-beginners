# उदाहरण: आधारभूत होस्ट

एक सन्दर्भ कार्यान्वयन जसले कसरी MCP होस्ट अनुप्रयोग निर्माण गर्ने देखाउँछ जुन MCP सर्भरहरूमा जडान हुन्छ र सुरक्षित स्यान्डबक्समा उपकरण UI हरू प्रस्तुत गर्दछ।

यो आधारभूत होस्ट स्थानीय विकासको क्रममा MCP अनुप्रयोगहरू परीक्षण गर्न पनि प्रयोग गर्न सकिन्छ।

## प्रमुख फाइलहरू

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - टूल छनौट, प्यारामिटर इनपुट, र iframe व्यवस्थापन सहित React UI होस्ट
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - सुरक्षा प्रमाणीकरण र द्विपक्षीय सन्देश प्रेषण सहित बाहिरी iframe प्रोक्सी
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - मुख्य तर्क: सर्भर जडान, उपकरण कल गर्ने, र AppBridge सेटअप

## सुरु गर्ने तरिका

```bash
npm install
npm run start
# http://localhost:8080 खोल्नुहोस्
```

पूर्वनिर्धारित रूपमा, होस्ट अनुप्रयोगले `http://localhost:3001/mcp` मा रहेको MCP सर्भरसँग जडान हुने प्रयास गर्नेछ। तपाईंले `SERVERS` वातावरण चरलाई सर्भर URL हरूको JSON सूचीले सेट गरेर यो व्यवहार कन्फिगर गर्न सक्नुहुन्छ:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## वास्तुकला

यो उदाहरणले सुरक्षित UI पृथकीकरणका लागि डबल-iframe स्यान्डबक्स प्याटर्न प्रयोग गर्दछ:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**किन दुई iframes?**

- बाहिरी iframe फरक मूल (पोर्ट 8081) मा चल्छ जसले होस्टमा प्रत्यक्ष पहुँचलाई रोक्दछ
- भित्री iframe `srcdoc` मार्फत HTML प्राप्त गर्दछ र स्यान्डबक्स विशेषताहरूले प्रतिबन्धित हुन्छ
- सन्देशहरू बाहिरी iframe बाट बहन्छन् जसले तिनीहरूलाई प्रमाणीकरण र द्विपक्षीय रूपमा प्रेषण गर्दछ

यो वास्तुकलाले सुनिश्चित गर्दछ कि यदि उपकरण UI कोड दुष्ट भए पनि, यो होस्ट अनुप्रयोगको DOM, कुकीहरू, वा JavaScript सन्दर्भमा पहुँच गर्न सक्दैन।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो कागजात AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौँ, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलतियाँ हुनसक्छन्। मूल कागजात यसको मूल भाषामा नै आधिकारिक स्रोत मान्नु पर्ने हुन्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानवीय अनुवादलाई सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलत बुझाई वा व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
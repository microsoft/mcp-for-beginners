# नमूना चलाउनुहोस्

> [!WARNING]
> यो नमूनाले अक्तुअल स्याम्पलिङ र लेगेसी HTTP+SSE अन्त बिन्दु प्रयोग गर्दछ। यो
> MCP `2025-11-25` अनुकूलताको लागि राखिएको हो। नयाँ कार्यान्वयनहरूले LLM प्रदायकलाई सिधै कल गर्नुपर्छ र
> रिमोट MCP ट्राफिकको लागि स्ट्रीमबल HTTP प्रयोग गर्नुपर्छ।

## भर्चुअल वातावरण बनाउनुस्

```sh
python -m venv venv
source ./venv/bin/activate
```

## निर्भरताहरू स्थापना गर्नुस्

```sh
pip install "mcp[cli]"
```

## सर्भर चलाउनुस्

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot र VS Code सँग सर्भरको परीक्षण गर्नुस्

mcp.json मा निम्न प्रकारको प्रविष्टि थप्नुस्:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

सर्भरमा "start" क्लिक गर्न निश्चित हुनुस्।

GitHub Copilot मा निम्न प्रॉम्प्ट टाँस्नुस्:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

पहिलो पटक तपाईंसँग Sampling कार्य स्वीकार गर्ने अनुमति मागिनेछ, त्यसपछि "create_blog" चलाउन उपकरणलाई स्वीकार्न अनुरोध गरिनेछ। तपाईंले निम्न झैँ प्रतिक्रिया देख्नुहुनेछ:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# MCP stdio Server - Python समाधान

> **⚠️ महत्त्वपूर्ण**: यो समाधानलाई **stdio transport** प्रयोग गर्न अद्यावधिक गरिएको छ, जसलाई MCP Specification 2025-06-18 द्वारा सिफारिस गरिएको छ। पुरानो SSE transport अब प्रयोगमा छैन।

## अवलोकन

यो Python समाधानले हालको stdio transport प्रयोग गरेर MCP server कसरी निर्माण गर्ने भनेर देखाउँछ। stdio transport सरल, सुरक्षित, र पुरानो SSE विधिभन्दा राम्रो प्रदर्शन प्रदान गर्दछ।

## आवश्यकताहरू

- Python 3.8 वा पछिल्लो संस्करण
- `uv` package management को लागि स्थापना गर्न सिफारिस गरिन्छ, [निर्देशनहरू](https://docs.astral.sh/uv/#highlights) हेर्नुहोस्।

## सेटअप निर्देशहरू

### चरण १: भर्चुअल वातावरण सिर्जना गर्नुहोस्

```bash
python -m venv venv
```

### चरण २: भर्चुअल वातावरण सक्रिय गर्नुहोस्

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### चरण ३: आवश्यकताहरू स्थापना गर्नुहोस्

```bash
pip install mcp
```

## Server चलाउने

stdio server पुरानो SSE server भन्दा फरक तरिकाले चल्छ। वेब server सुरु गर्ने सट्टा, यो stdin/stdout मार्फत सञ्चार गर्दछ:

```bash
python server.py
```

**महत्त्वपूर्ण**: Server रोकिएको जस्तो देखिन्छ - यो सामान्य हो! यो stdin बाट JSON-RPC सन्देशहरूको प्रतीक्षा गरिरहेको छ।

## Server परीक्षण गर्ने

### विधि १: MCP Inspector प्रयोग गरेर (सिफारिस गरिएको)

```bash
npx @modelcontextprotocol/inspector python server.py
```

यसले निम्न कार्य गर्दछ:
1. तपाईंको server लाई subprocess को रूपमा सुरु गर्दछ
2. परीक्षणको लागि वेब इन्टरफेस खोल्छ
3. सबै server उपकरणहरू अन्तरक्रियात्मक रूपमा परीक्षण गर्न अनुमति दिन्छ

### विधि २: प्रत्यक्ष JSON-RPC परीक्षण

तपाईं JSON-RPC सन्देशहरू प्रत्यक्ष रूपमा पठाएर पनि परीक्षण गर्न सक्नुहुन्छ:

1. Server सुरु गर्नुहोस्: `python server.py`
2. JSON-RPC सन्देश पठाउनुहोस् (उदाहरण):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server उपलब्ध उपकरणहरूको प्रतिक्रिया दिनेछ

### उपलब्ध उपकरणहरू

Server ले निम्न उपकरणहरू प्रदान गर्दछ:

- **add(a, b)**: दुई संख्याहरूलाई जोड्नुहोस्
- **multiply(a, b)**: दुई संख्याहरूलाई गुणन गर्नुहोस्  
- **get_greeting(name)**: व्यक्तिगत अभिवादन सिर्जना गर्नुहोस्
- **get_server_info()**: Server को जानकारी प्राप्त गर्नुहोस्

### Claude Desktop सँग परीक्षण गर्ने

यो server Claude Desktop सँग प्रयोग गर्न, तपाईंको `claude_desktop_config.json` मा यो कन्फिगरेसन थप्नुहोस्:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## SSE बाट मुख्य भिन्नताहरू

**stdio transport (हालको):**
- ✅ सरल सेटअप - वेब server आवश्यक छैन
- ✅ राम्रो सुरक्षा - HTTP endpoints आवश्यक छैन
- ✅ Subprocess-आधारित सञ्चार
- ✅ stdin/stdout मार्फत JSON-RPC
- ✅ राम्रो प्रदर्शन

**SSE transport (प्रयोगमा छैन):**
- ❌ HTTP server सेटअप आवश्यक थियो
- ❌ वेब framework (Starlette/FastAPI) आवश्यक थियो
- ❌ Routing र session management जटिल थियो
- ❌ अतिरिक्त सुरक्षा विचारहरू आवश्यक थियो
- ❌ अब MCP 2025-06-18 मा प्रयोगमा छैन

## Debugging सुझावहरू

- Logging को लागि `stderr` प्रयोग गर्नुहोस् (कहिल्यै `stdout` प्रयोग नगर्नुहोस्)
- दृश्यात्मक debugging को लागि Inspector प्रयोग गर्नुहोस्
- सुनिश्चित गर्नुहोस् कि सबै JSON सन्देशहरू newline-delimited छन्
- Server त्रुटि बिना सुरु भएको छ कि जाँच गर्नुहोस्

यो समाधान हालको MCP specification अनुसरण गर्दछ र stdio transport कार्यान्वयनको लागि उत्कृष्ट अभ्यासहरू प्रदर्शन गर्दछ।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
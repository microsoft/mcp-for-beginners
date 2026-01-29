# MCP stdio सर्वर - .NET समाधान

> **⚠️ महत्वपूर्ण**: इस समाधान को **stdio transport** का उपयोग करने के लिए अपडेट किया गया है, जैसा कि MCP Specification 2025-06-18 में अनुशंसित किया गया है। मूल SSE transport को अब बंद कर दिया गया है।

## अवलोकन

यह .NET समाधान दिखाता है कि वर्तमान stdio transport का उपयोग करके MCP सर्वर कैसे बनाया जाए। stdio transport सरल, अधिक सुरक्षित और पुराने SSE दृष्टिकोण की तुलना में बेहतर प्रदर्शन प्रदान करता है।

## आवश्यकताएँ

- .NET 9.0 SDK या बाद का संस्करण
- .NET dependency injection की बुनियादी समझ

## सेटअप निर्देश

### चरण 1: डिपेंडेंसीज़ को पुनर्स्थापित करें

```bash
dotnet restore
```

### चरण 2: प्रोजेक्ट को बिल्ड करें

```bash
dotnet build
```

## सर्वर चलाना

stdio सर्वर पुराने HTTP-आधारित सर्वर से अलग तरीके से चलता है। वेब सर्वर शुरू करने के बजाय, यह stdin/stdout के माध्यम से संचार करता है:

```bash
dotnet run
```

**महत्वपूर्ण**: सर्वर रुका हुआ प्रतीत होगा - यह सामान्य है! यह stdin से JSON-RPC संदेशों की प्रतीक्षा कर रहा है।

## सर्वर का परीक्षण करना

### विधि 1: MCP Inspector का उपयोग करना (अनुशंसित)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

यह करेगा:
1. आपके सर्वर को एक subprocess के रूप में लॉन्च करेगा
2. परीक्षण के लिए एक वेब इंटरफ़ेस खोलेगा
3. आपको सभी सर्वर टूल्स को इंटरैक्टिव तरीके से परीक्षण करने की अनुमति देगा

### विधि 2: सीधे कमांड लाइन परीक्षण

आप Inspector को सीधे लॉन्च करके भी परीक्षण कर सकते हैं:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### उपलब्ध टूल्स

सर्वर निम्नलिखित टूल्स प्रदान करता है:

- **AddNumbers(a, b)**: दो संख्याओं को जोड़ें
- **MultiplyNumbers(a, b)**: दो संख्याओं को गुणा करें  
- **GetGreeting(name)**: एक व्यक्तिगत अभिवादन उत्पन्न करें
- **GetServerInfo()**: सर्वर की जानकारी प्राप्त करें

### Claude Desktop के साथ परीक्षण करना

इस सर्वर को Claude Desktop के साथ उपयोग करने के लिए, अपने `claude_desktop_config.json` में यह कॉन्फ़िगरेशन जोड़ें:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## प्रोजेक्ट संरचना

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE से stdio के प्रमुख अंतर

**stdio transport (वर्तमान):**
- ✅ सरल सेटअप - वेब सर्वर की आवश्यकता नहीं
- ✅ बेहतर सुरक्षा - कोई HTTP endpoints नहीं
- ✅ `Host.CreateApplicationBuilder()` का उपयोग करता है `WebApplication.CreateBuilder()` के बजाय
- ✅ `WithStdioTransport()` का उपयोग करता है `WithHttpTransport()` के बजाय
- ✅ कंसोल एप्लिकेशन वेब एप्लिकेशन के बजाय
- ✅ बेहतर प्रदर्शन

**HTTP/SSE transport (बंद):**
- ❌ ASP.NET Core वेब सर्वर की आवश्यकता थी
- ❌ `app.MapMcp()` रूटिंग सेटअप की आवश्यकता थी
- ❌ अधिक जटिल कॉन्फ़िगरेशन और डिपेंडेंसीज़
- ❌ अतिरिक्त सुरक्षा विचार
- ❌ अब MCP 2025-06-18 में बंद कर दिया गया है

## विकास सुविधाएँ

- **Dependency Injection**: सेवाओं और लॉगिंग के लिए पूर्ण DI समर्थन
- **Structured Logging**: `ILogger<T>` का उपयोग करके stderr पर उचित लॉगिंग
- **Tool Attributes**: `[McpServerTool]` attributes का उपयोग करके साफ टूल परिभाषा
- **Async Support**: सभी टूल्स async ऑपरेशन्स का समर्थन करते हैं
- **Error Handling**: ग्रेसफुल एरर हैंडलिंग और लॉगिंग

## विकास सुझाव

- लॉगिंग के लिए `ILogger` का उपयोग करें (stdout पर सीधे कभी न लिखें)
- परीक्षण से पहले `dotnet build` के साथ बिल्ड करें
- विज़ुअल डिबगिंग के लिए Inspector के साथ परीक्षण करें
- सभी लॉगिंग स्वचालित रूप से stderr पर जाती है
- सर्वर ग्रेसफुल शटडाउन सिग्नल्स को संभालता है

यह समाधान वर्तमान MCP स्पेसिफिकेशन का पालन करता है और .NET का उपयोग करके stdio transport के कार्यान्वयन के लिए सर्वोत्तम प्रथाओं को प्रदर्शित करता है।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
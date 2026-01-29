# ਮਾਡਲ ਸੰਦਰਭ ਪ੍ਰੋਟੋਕੋਲ ਵਿੱਚ ਸੈਂਪਲਿੰਗ

ਸੈਂਪਲਿੰਗ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ MCP ਫੀਚਰ ਹੈ ਜੋ ਸਰਵਰਾਂ ਨੂੰ ਕਲਾਇੰਟ ਰਾਹੀਂ LLM ਪੂਰਨਤਾਵਾਂ ਦੀ ਬੇਨਤੀ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਸੁਖਦਾਇਕ ਏਜੰਟਿਕ ਵਿਹਾਰ ਸੰਭਵ ਹੁੰਦੇ ਹਨ ਅਤੇ ਸੁਰੱਖਿਆ ਅਤੇ ਗੋਪਨੀਯਤਾ ਬਰਕਰਾਰ ਰਹਿੰਦੀ ਹੈ। ਸਹੀ ਸੈਂਪਲਿੰਗ ਸੰਰਚਨਾ ਜਵਾਬ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਬਹੁਤ ਸੁਧਾਰ ਕਰ ਸਕਦੀ ਹੈ। MCP ਇੱਕ ਮਿਆਰੀ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿਸ ਨਾਲ ਮਾਡਲ ਖਾਸ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਲ ਟੈਕਸਟ ਬਣਾਉਂਦੇ ਹਨ ਜੋ ਬੇਤਰਤੀਬੀ, ਰਚਨਾਤਮਕਤਾ ਅਤੇ ਸੰਗਤਤਾ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ MCP ਬੇਨਤੀਆਂ ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਕਿਵੇਂ ਸੰਰਚਿਤ ਕਰਨਾ ਹੈ ਅਤੇ ਸੈਂਪਲਿੰਗ ਦੇ ਅਧਾਰਭੂਤ ਪ੍ਰੋਟੋਕੋਲ ਮਕੈਨਿਕਸ ਨੂੰ ਸਮਝਾਂਗੇ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- MCP ਵਿੱਚ ਉਪਲਬਧ ਮੁੱਖ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸਮਝਣਾ।
- ਵੱਖ-ਵੱਖ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸੰਰਚਿਤ ਕਰਨਾ।
- ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਨਤੀਜੇ ਲਈ ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ ਲਾਗੂ ਕਰਨਾ।
- ਸੰਦਰਭ ਅਤੇ ਉਪਭੋਗਤਾ ਪਸੰਦਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਢਾਲਣਾ।
- ਵੱਖ-ਵੱਖ ਸਥਿਤੀਆਂ ਵਿੱਚ ਮਾਡਲ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਸੁਧਾਰਨ ਲਈ ਸੈਂਪਲਿੰਗ ਰਣਨੀਤੀਆਂ ਲਾਗੂ ਕਰਨਾ।
- MCP ਦੇ ਕਲਾਇੰਟ-ਸਰਵਰ ਪ੍ਰਵਾਹ ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ, ਇਹ ਸਮਝਣਾ।

## MCP ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ

MCP ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਪ੍ਰਕਿਰਿਆ ਇਹਨਾਂ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੀ ਹੈ:

1. ਸਰਵਰ ਕਲਾਇੰਟ ਨੂੰ `sampling/createMessage` ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ
2. ਕਲਾਇੰਟ ਬੇਨਤੀ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਸੋਧ ਸਕਦਾ ਹੈ
3. ਕਲਾਇੰਟ LLM ਤੋਂ ਸੈਂਪਲ ਕਰਦਾ ਹੈ
4. ਕਲਾਇੰਟ ਪੂਰਨਤਾ ਦੀ ਸਮੀਖਿਆ ਕਰਦਾ ਹੈ
5. ਕਲਾਇੰਟ ਨਤੀਜਾ ਸਰਵਰ ਨੂੰ ਵਾਪਸ ਭੇਜਦਾ ਹੈ

ਇਹ ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ ਡਿਜ਼ਾਈਨ ਯੂਜ਼ਰਾਂ ਨੂੰ ਇਹ ਨਿਯੰਤਰਣ ਦੇਂਦਾ ਹੈ ਕਿ LLM ਕੀ ਵੇਖਦਾ ਹੈ ਅਤੇ ਕੀ ਬਣਾਉਂਦਾ ਹੈ।

## ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਦਾ ਜਾਇਜ਼ਾ

MCP ਹੇਠ ਲਿਖੇ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਕਲਾਇੰਟ ਬੇਨਤੀਆਂ ਵਿੱਚ ਸੰਰਚਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

| ਪੈਰਾਮੀਟਰ | ਵਰਣਨ | ਆਮ ਸੀਮਾ |
|-----------|-------------|---------------|
| `temperature` | ਟੋਕਨ ਚੋਣ ਵਿੱਚ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ | 0.0 - 1.0 |
| `maxTokens` | ਬਣਾਏ ਜਾਣ ਵਾਲੇ ਟੋਕਨਾਂ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਗਿਣਤੀ | ਪੂਰਨ ਅੰਕ |
| `stopSequences` | ਖਾਸ ਕ੍ਰਮ ਜੋ ਮਿਲਣ 'ਤੇ ਬਣਾਉਣਾ ਰੋਕਦੇ ਹਨ | ਸਤਰਾਂ ਦੀ ਸੂਚੀ |
| `metadata` | ਵਾਧੂ ਪ੍ਰਦਾਤਾ-ਵਿਸ਼ੇਸ਼ ਪੈਰਾਮੀਟਰ | JSON ਵਸਤੂ |

ਕਈ LLM ਪ੍ਰਦਾਤਾ `metadata` ਖੇਤਰ ਰਾਹੀਂ ਵਾਧੂ ਪੈਰਾਮੀਟਰਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਨ, ਜਿਵੇਂ:

| ਆਮ ਵਾਧੂ ਪੈਰਾਮੀਟਰ | ਵਰਣਨ | ਆਮ ਸੀਮਾ |
|-----------|-------------|---------------|
| `top_p` | ਨਿਊਕਲੀਅਸ ਸੈਂਪਲਿੰਗ - ਟੋਕਨਾਂ ਨੂੰ ਉੱਚ ਕੁੱਲ ਸੰਭਾਵਨਾ ਤੱਕ ਸੀਮਿਤ ਕਰਦਾ ਹੈ | 0.0 - 1.0 |
| `top_k` | ਟੋਕਨ ਚੋਣ ਨੂੰ ਸਿਖਰ K ਵਿਕਲਪਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਦਾ ਹੈ | 1 - 100 |
| `presence_penalty` | ਟੈਕਸਟ ਵਿੱਚ ਪਹਿਲਾਂ ਮੌਜੂਦ ਟੋਕਨਾਂ 'ਤੇ ਦੰਡ ਲਗਾਉਂਦਾ ਹੈ | -2.0 - 2.0 |
| `frequency_penalty` | ਟੈਕਸਟ ਵਿੱਚ ਟੋਕਨਾਂ ਦੀ ਆਵ੍ਰਿਤੀ 'ਤੇ ਦੰਡ ਲਗਾਉਂਦਾ ਹੈ | -2.0 - 2.0 |
| `seed` | ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਨਤੀਜੇ ਲਈ ਖਾਸ ਬੇਤਰਤੀਬੀ ਬੀਜ | ਪੂਰਨ ਅੰਕ |

## ਉਦਾਹਰਨ ਬੇਨਤੀ ਫਾਰਮੈਟ

ਇੱਥੇ MCP ਵਿੱਚ ਕਲਾਇੰਟ ਤੋਂ ਸੈਂਪਲਿੰਗ ਦੀ ਬੇਨਤੀ ਦਾ ਉਦਾਹਰਨ ਹੈ:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## ਜਵਾਬ ਫਾਰਮੈਟ

ਕਲਾਇੰਟ ਇੱਕ ਪੂਰਨਤਾ ਨਤੀਜਾ ਵਾਪਸ ਕਰਦਾ ਹੈ:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ ਨਿਯੰਤਰਣ

MCP ਸੈਂਪਲਿੰਗ ਮਨੁੱਖੀ ਨਿਗਰਾਨੀ ਦੇ ਨਾਲ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ:

- **ਪ੍ਰਾਂਪਟਾਂ ਲਈ**:
  - ਕਲਾਇੰਟਾਂ ਨੂੰ ਯੂਜ਼ਰਾਂ ਨੂੰ ਪ੍ਰਸਤਾਵਿਤ ਪ੍ਰਾਂਪਟ ਦਿਖਾਉਣਾ ਚਾਹੀਦਾ ਹੈ
  - ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਸੋਧਣ ਜਾਂ ਰੱਦ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ
  - ਸਿਸਟਮ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਛਾਣਬੀਨ ਜਾਂ ਸੋਧਿਆ ਜਾ ਸਕਦਾ ਹੈ
  - ਸੰਦਰਭ ਸ਼ਾਮਿਲ ਕਰਨ ਦਾ ਨਿਯੰਤਰਣ ਕਲਾਇੰਟ ਕੋਲ ਹੁੰਦਾ ਹੈ

- **ਪੂਰਨਤਾਵਾਂ ਲਈ**:
  - ਕਲਾਇੰਟਾਂ ਨੂੰ ਯੂਜ਼ਰਾਂ ਨੂੰ ਪੂਰਨਤਾ ਦਿਖਾਉਣੀ ਚਾਹੀਦੀ ਹੈ
  - ਯੂਜ਼ਰ ਪੂਰਨਤਾਵਾਂ ਨੂੰ ਸੋਧਣ ਜਾਂ ਰੱਦ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ
  - ਕਲਾਇੰਟ ਪੂਰਨਤਾਵਾਂ ਨੂੰ ਛਾਣਬੀਨ ਜਾਂ ਸੋਧ ਸਕਦੇ ਹਨ
  - ਯੂਜ਼ਰ ਨਿਯੰਤਰਿਤ ਕਰਦੇ ਹਨ ਕਿ ਕਿਹੜਾ ਮਾਡਲ ਵਰਤਿਆ ਜਾਵੇ

ਇਹ ਸਿਧਾਂਤ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਆਓ ਵੇਖੀਏ ਕਿ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਕਿਵੇਂ ਲਾਗੂ ਕਰਨੀ ਹੈ, ਖਾਸ ਕਰਕੇ ਉਹ ਪੈਰਾਮੀਟਰ ਜੋ ਆਮ ਤੌਰ 'ਤੇ LLM ਪ੍ਰਦਾਤਾ ਵੱਲੋਂ ਸਮਰਥਿਤ ਹਨ।

## ਸੁਰੱਖਿਆ ਸੰਬੰਧੀ ਵਿਚਾਰ

MCP ਵਿੱਚ ਸੈਂਪਲਿੰਗ ਲਾਗੂ ਕਰਦੇ ਸਮੇਂ, ਇਹ ਸੁਰੱਖਿਆ ਦੀਆਂ ਵਧੀਆ ਪ੍ਰਥਾਵਾਂ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ:

- **ਸਭ ਮੈਸੇਜ ਸਮੱਗਰੀ ਦੀ ਜਾਂਚ ਕਰੋ** ਪਹਿਲਾਂ ਕਿ ਇਹ ਕਲਾਇੰਟ ਨੂੰ ਭੇਜੀ ਜਾਵੇ
- **ਪ੍ਰਾਂਪਟਾਂ ਅਤੇ ਪੂਰਨਤਾਵਾਂ ਤੋਂ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਨੂੰ ਸਾਫ਼ ਕਰੋ**
- **ਦੁਰਵਰਤੋਂ ਨੂੰ ਰੋਕਣ ਲਈ ਰੇਟ ਸੀਮਾਵਾਂ ਲਾਗੂ ਕਰੋ**
- **ਅਸਧਾਰਣ ਪੈਟਰਨਾਂ ਲਈ ਸੈਂਪਲਿੰਗ ਦੀ ਵਰਤੋਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ**
- **ਸੁਰੱਖਿਅਤ ਪ੍ਰੋਟੋਕੋਲਾਂ ਰਾਹੀਂ ਡਾਟਾ ਨੂੰ ਇਨਕ੍ਰਿਪਟ ਕਰੋ**
- **ਉਪਭੋਗਤਾ ਡਾਟਾ ਦੀ ਗੋਪਨੀਯਤਾ ਨੂੰ ਸੰਬੰਧਿਤ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਸੰਭਾਲੋ**
- **ਅਨੁਕੂਲਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਲਈ ਸੈਂਪਲਿੰਗ ਬੇਨਤੀਆਂ ਦਾ ਆਡਿਟ ਕਰੋ**
- **ਲਾਗਤ ਦੇ ਖ਼ਰਚੇ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ ਉਚਿਤ ਸੀਮਾਵਾਂ ਰੱਖੋ**
- **ਸੈਂਪਲਿੰਗ ਬੇਨਤੀਆਂ ਲਈ ਸਮਾਂ ਸੀਮਾਵਾਂ ਲਾਗੂ ਕਰੋ**
- **ਮਾਡਲ ਦੀਆਂ ਗਲਤੀਆਂ ਨੂੰ ਸੁਚੱਜੇ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲੋ**

ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੇ ਵਿਹਾਰ ਨੂੰ ਬਰੀਕੀ ਨਾਲ ਢਾਲਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ ਤਾਂ ਜੋ ਨਿਰਧਾਰਿਤ ਅਤੇ ਰਚਨਾਤਮਕ ਨਤੀਜਿਆਂ ਵਿੱਚ ਸੰਤੁਲਨ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ।

ਆਓ ਵੇਖੀਏ ਕਿ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਇਹਨਾਂ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਕਿਵੇਂ ਸੰਰਚਿਤ ਕਰਨਾ ਹੈ।

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਖਾਸ ਸਰਵਰ URL ਨਾਲ MCP ਕਲਾਇੰਟ ਬਣਾਇਆ।
- `temperature`, `top_p`, ਅਤੇ `top_k` ਵਰਗੇ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਬੇਨਤੀ ਸੰਰਚਿਤ ਕੀਤੀ।
- ਬੇਨਤੀ ਭੇਜੀ ਅਤੇ ਬਣਾਇਆ ਗਿਆ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕੀਤਾ।
- ਵਰਤਿਆ:
    - `allowedTools` ਇਹ ਦਰਸਾਉਣ ਲਈ ਕਿ ਮਾਡਲ ਬਣਾਉਣ ਦੌਰਾਨ ਕਿਹੜੇ ਟੂਲ ਵਰਤ ਸਕਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ `ideaGenerator` ਅਤੇ `marketAnalyzer` ਟੂਲਾਂ ਨੂੰ ਰਚਨਾਤਮਕ ਐਪ ਆਈਡੀਆ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਲਈ ਆਗਿਆ ਦਿੱਤੀ।
    - `frequencyPenalty` ਅਤੇ `presencePenalty` ਦੁਹਰਾਵਟ ਅਤੇ ਵਿਭਿੰਨਤਾ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ।
    - `temperature` ਆਉਟਪੁੱਟ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ, ਜਿੱਥੇ ਵੱਧ ਮੁੱਲ ਜ਼ਿਆਦਾ ਰਚਨਾਤਮਕ ਜਵਾਬ ਲੈ ਕੇ ਆਉਂਦੇ ਹਨ।
    - `top_p` ਟੋਕਨਾਂ ਦੀ ਚੋਣ ਨੂੰ ਉੱਚ ਕੁੱਲ ਸੰਭਾਵਨਾ ਵਾਲੇ ਟੋਕਨਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਬਣਾਏ ਗਏ ਟੈਕਸਟ ਦੀ ਗੁਣਵੱਤਾ ਵਧਦੀ ਹੈ।
    - `top_k` ਮਾਡਲ ਨੂੰ ਸਭ ਤੋਂ ਸੰਭਾਵਿਤ K ਟੋਕਨਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਦਾ ਹੈ, ਜੋ ਹੋਰ ਸੰਗਤ ਜਵਾਬ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।
    - `frequencyPenalty` ਅਤੇ `presencePenalty` ਦੁਹਰਾਵਟ ਘਟਾਉਣ ਅਤੇ ਬਣਾਏ ਗਏ ਟੈਕਸਟ ਵਿੱਚ ਵਿਭਿੰਨਤਾ ਵਧਾਉਣ ਲਈ।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਰਵਰ URL ਅਤੇ API ਕੁੰਜੀ ਨਾਲ MCP ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕੀਤਾ।
- ਦੋ ਸੈੱਟ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸੰਰਚਿਤ ਕੀਤਾ: ਇੱਕ ਰਚਨਾਤਮਕ ਕੰਮਾਂ ਲਈ ਅਤੇ ਦੂਜਾ ਤੱਥ-ਆਧਾਰਿਤ ਕੰਮਾਂ ਲਈ।
- ਇਹ ਬੇਨਤੀਆਂ ਭੇਜੀਆਂ, ਮਾਡਲ ਨੂੰ ਹਰ ਕੰਮ ਲਈ ਖਾਸ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੱਤੀ।
- ਬਣਾਏ ਗਏ ਜਵਾਬ ਪ੍ਰਿੰਟ ਕੀਤੇ ਤਾਂ ਜੋ ਵੱਖ-ਵੱਖ ਸੈਂਪਲਿੰਗ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਪ੍ਰਭਾਵ ਦਿਖਾਏ ਜਾ ਸਕਣ।
- ਵਰਤਿਆ `allowedTools` ਇਹ ਦਰਸਾਉਣ ਲਈ ਕਿ ਮਾਡਲ ਬਣਾਉਣ ਦੌਰਾਨ ਕਿਹੜੇ ਟੂਲ ਵਰਤ ਸਕਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਰਚਨਾਤਮਕ ਕੰਮਾਂ ਲਈ `ideaGenerator` ਅਤੇ `environmentalImpactTool` ਅਤੇ ਤੱਥ-ਆਧਾਰਿਤ ਕੰਮਾਂ ਲਈ `factChecker` ਅਤੇ `dataAnalysisTool` ਦੀ ਆਗਿਆ ਦਿੱਤੀ।
- ਵਰਤਿਆ `temperature` ਆਉਟਪੁੱਟ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ, ਜਿੱਥੇ ਵੱਧ ਮੁੱਲ ਜ਼ਿਆਦਾ ਰਚਨਾਤਮਕ ਜਵਾਬ ਲੈ ਕੇ ਆਉਂਦੇ ਹਨ।
- ਵਰਤਿਆ `top_p` ਟੋਕਨਾਂ ਦੀ ਚੋਣ ਨੂੰ ਉੱਚ ਕੁੱਲ ਸੰਭਾਵਨਾ ਵਾਲੇ ਟੋਕਨਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਨ ਲਈ, ਜਿਸ ਨਾਲ ਬਣਾਏ ਗਏ ਟੈਕਸਟ ਦੀ ਗੁਣਵੱਤਾ ਵਧਦੀ ਹੈ।
- ਵਰਤਿਆ `frequencyPenalty` ਅਤੇ `presencePenalty` ਦੁਹਰਾਵਟ ਘਟਾਉਣ ਅਤੇ ਆਉਟਪੁੱਟ ਵਿੱਚ ਵਿਭਿੰਨਤਾ ਵਧਾਉਣ ਲਈ।
- ਵਰਤਿਆ `top_k` ਮਾਡਲ ਨੂੰ ਸਭ ਤੋਂ ਸੰਭਾਵਿਤ K ਟੋਕਨਾਂ ਤੱਕ ਸੀਮਿਤ ਕਰਨ ਲਈ, ਜੋ ਹੋਰ ਸੰਗਤ ਜਵਾਬ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

---

## ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ

ਜਿਨ੍ਹਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਲਗਾਤਾਰ ਨਤੀਜੇ ਚਾਹੀਦੇ ਹਨ, ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਵਾਲੇ ਨਤੀਜੇ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕਰਦੀ ਹੈ ਕਿ ਇੱਕ ਨਿਰਧਾਰਿਤ ਬੇਤਰਤੀਬੀ ਬੀਜ ਵਰਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ temperature ਨੂੰ ਜ਼ੀਰੋ ਤੇ ਸੈੱਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

ਆਓ ਹੇਠਾਂ ਦਿੱਤੇ ਉਦਾਹਰਨ ਨੂੰ ਵੇਖੀਏ ਜੋ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਨਿਰਧਾਰਿਤ ਸਰਵਰ URL ਨਾਲ MCP ਕਲਾਇੰਟ ਬਣਾਇਆ।
- ਦੋ ਬੇਨਤੀਆਂ ਨੂੰ ਇੱਕੋ ਜਿਹਾ ਪ੍ਰਾਂਪਟ, ਨਿਰਧਾਰਿਤ ਬੀਜ ਅਤੇ ਜ਼ੀਰੋ temperature ਨਾਲ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਦੋਹਾਂ ਬੇਨਤੀਆਂ ਭੇਜੀਆਂ ਅਤੇ ਬਣਾਇਆ ਗਿਆ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕੀਤਾ।
- ਦਰਸਾਇਆ ਕਿ ਜਵਾਬ ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ ਸੰਰਚਨਾ (ਇੱਕੋ ਬੀਜ ਅਤੇ temperature) ਕਾਰਨ ਇੱਕੋ ਜਿਹੇ ਹਨ।
- `setSeed` ਵਰਤ ਕੇ ਨਿਰਧਾਰਿਤ ਬੇਤਰਤੀਬੀ ਬੀਜ ਦਿੱਤਾ, ਜਿਸ ਨਾਲ ਮਾਡਲ ਹਰ ਵਾਰੀ ਇੱਕੋ ਆਉਟਪੁੱਟ ਬਣਾਉਂਦਾ ਹੈ।
- `temperature` ਨੂੰ ਜ਼ੀਰੋ ਤੇ ਸੈੱਟ ਕੀਤਾ ਤਾਂ ਜੋ ਵੱਧ ਤੋਂ ਵੱਧ ਨਿਰਧਾਰਿਤਤਾ ਯਕੀਨੀ ਬਣਾਈ ਜਾ ਸਕੇ, ਜਿਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਮਾਡਲ ਹਮੇਸ਼ਾ ਸਭ ਤੋਂ ਸੰਭਾਵਿਤ ਅਗਲਾ ਟੋਕਨ ਚੁਣੇਗਾ।

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਸਰਵਰ URL ਨਾਲ MCP ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕੀਤਾ।
- ਦੋ ਬੇਨਤੀਆਂ ਨੂੰ ਇੱਕੋ ਜਿਹਾ ਪ੍ਰਾਂਪਟ, ਨਿਰਧਾਰਿਤ ਬੀਜ ਅਤੇ ਜ਼ੀਰੋ temperature ਨਾਲ ਸੰਰਚਿਤ ਕੀਤਾ।
- ਦੋਹਾਂ ਬੇਨਤੀਆਂ ਭੇਜੀਆਂ ਅਤੇ ਬਣਾਇਆ ਗਿਆ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕੀਤਾ।
- ਦਰਸਾਇਆ ਕਿ ਜਵਾਬ ਨਿਰਧਾਰਿਤ ਸੈਂਪਲਿੰਗ ਸੰਰਚਨਾ (ਇੱਕੋ ਬੀਜ ਅਤੇ temperature) ਕਾਰਨ ਇੱਕੋ ਜਿਹੇ ਹਨ।
- `seed` ਵਰਤ ਕੇ ਨਿਰਧਾਰਿਤ ਬੇਤਰਤੀਬੀ ਬੀਜ ਦਿੱਤਾ, ਜਿਸ ਨਾਲ ਮਾਡਲ ਹਰ ਵਾਰੀ ਇੱਕੋ ਆਉਟਪੁੱਟ ਬਣਾਉਂਦਾ ਹੈ।
- `temperature` ਨੂੰ ਜ਼ੀਰੋ ਤੇ ਸੈੱਟ ਕੀਤਾ ਤਾਂ ਜੋ ਵੱਧ ਤੋਂ ਵੱਧ ਨਿਰਧਾਰਿਤਤਾ ਯਕੀਨੀ ਬਣਾਈ ਜਾ ਸਕੇ।
- ਤੀਜੀ ਬੇਨਤੀ ਲਈ ਵੱਖਰਾ ਬੀਜ ਵਰਤਿਆ ਤਾਂ ਜੋ ਦਿਖਾਇਆ ਜਾ ਸਕੇ ਕਿ ਬੀਜ ਬਦਲਣ ਨਾਲ ਨਤੀਜੇ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ, ਭਾਵੇਂ ਪ੍ਰਾਂਪਟ ਅਤੇ temperature ਇੱਕੋ ਹੀ ਹੋਣ।

---

## ਗਤੀਸ਼ੀਲ ਸੈਂਪਲਿੰਗ ਸੰਰਚਨਾ

ਸਮਝਦਾਰ ਸੈਂਪਲਿੰਗ ਹਰ ਬੇਨਤੀ ਦੇ ਸੰਦਰਭ ਅਤੇ ਲੋੜਾਂ ਦੇ ਅਨੁਸਾਰ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਢਾਲਦਾ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ temperature, top_p ਅਤੇ ਦੰਡਾਂ ਨੂੰ ਕੰਮ ਦੇ ਕਿਸਮ, ਉਪਭੋਗਤਾ ਪਸੰਦਾਂ ਜਾਂ ਇਤਿਹਾਸਕ ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਅਧਾਰ 'ਤੇ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਬਦਲਣਾ।

ਆਓ ਵੇਖੀਏ ਕਿ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਗਤੀਸ਼ੀਲ ਸੈਂਪਲਿੰਗ ਕਿਵੇਂ ਲਾਗੂ ਕਰਨੀ ਹੈ।

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `DynamicSamplingService` ਕਲਾਸ ਬਣਾਈ ਜੋ ਅਨੁਕ

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
# Azure Content Safety ਨਾਲ ਉੱਚ ਪੱਧਰੀ MCP ਸੁਰੱਖਿਆ

Azure Content Safety ਕਈ ਤਾਕਤਵਰ ਸੰਦ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਤੁਹਾਡੇ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਦੀ ਸੁਰੱਖਿਆ ਨੂੰ ਬਹਿਤਰੀਨ ਬਣਾ ਸਕਦੇ ਹਨ:

## Prompt Shields

Microsoft ਦੇ AI Prompt Shields ਸਿੱਧੇ ਅਤੇ ਅਪਰੋਕਸ਼ prompt injection ਹਮਲਿਆਂ ਤੋਂ ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਦਿੰਦੇ ਹਨ:

1. **ਉੱਚ ਪੱਧਰੀ ਪਛਾਣ**: ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਮੱਗਰੀ ਵਿੱਚ ਛੁਪੇ ਖ਼ਤਰਨਾਕ ਹੁਕਮਾਂ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ।
2. **Spotlighting**: ਇਨਪੁੱਟ ਟੈਕਸਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਬਦਲਦਾ ਹੈ ਕਿ AI ਸਿਸਟਮ ਸਹੀ ਹੁਕਮਾਂ ਅਤੇ ਬਾਹਰੀ ਇਨਪੁੱਟ ਵਿੱਚ ਫਰਕ ਕਰ ਸਕਣ।
3. **Delimiters ਅਤੇ Datamarking**: ਭਰੋਸੇਯੋਗ ਅਤੇ ਅਭਰੋਸੇਯੋਗ ਡੇਟਾ ਦੇ ਵਿਚਕਾਰ ਹੱਦਾਂ ਨਿਸ਼ਾਨਦਾਰ ਕਰਦਾ ਹੈ।
4. **Content Safety ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: Azure AI Content Safety ਨਾਲ ਮਿਲ ਕੇ jailbreak ਕੋਸ਼ਿਸ਼ਾਂ ਅਤੇ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ।
5. **ਲਗਾਤਾਰ ਅੱਪਡੇਟਸ**: Microsoft ਨਵੇਂ ਖ਼ਤਰਨਾਂ ਦੇ ਖਿਲਾਫ ਸੁਰੱਖਿਆ ਤਕਨੀਕਾਂ ਨੂੰ ਨਿਯਮਤ ਤੌਰ 'ਤੇ ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ।

## MCP ਨਾਲ Azure Content Safety ਦੀ ਲਾਗੂਆਈ

ਇਹ ਤਰੀਕਾ ਕਈ ਪਰਤਾਂ ਵਾਲੀ ਸੁਰੱਖਿਆ ਦਿੰਦਾ ਹੈ:
- ਪ੍ਰੋਸੈਸਿੰਗ ਤੋਂ ਪਹਿਲਾਂ ਇਨਪੁੱਟ ਦੀ ਸਕੈਨਿੰਗ
- ਵਾਪਸੀ ਤੋਂ ਪਹਿਲਾਂ ਆਉਟਪੁੱਟ ਦੀ ਜਾਂਚ
- ਜਾਣੇ-ਪਹਚਾਣੇ ਨੁਕਸਾਨਦਾਇਕ ਪੈਟਰਨ ਲਈ ਬਲੌਕਲਿਸਟ ਦੀ ਵਰਤੋਂ
- Azure ਦੇ ਲਗਾਤਾਰ ਅੱਪਡੇਟ ਹੋ ਰਹੇ content safety ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

## Azure Content Safety ਸਰੋਤ

ਆਪਣੇ MCP ਸਰਵਰਾਂ ਨਾਲ Azure Content Safety ਲਾਗੂ ਕਰਨ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, ਇਹ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਵੇਖੋ:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety ਲਈ ਅਧਿਕਾਰਿਕ ਦਸਤਾਵੇਜ਼।
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - prompt injection ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਬਾਰੇ ਜਾਣੋ।
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety ਲਾਗੂ ਕਰਨ ਲਈ ਵਿਸਥਾਰਿਤ API ਸੰਦਰਭ।
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ਦੀ ਵਰਤੋਂ ਨਾਲ ਤੇਜ਼ ਲਾਗੂਆਈ ਗਾਈਡ।
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਲਈ ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀਜ਼।
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - jailbreak ਕੋਸ਼ਿਸ਼ਾਂ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਥਾਮ ਲਈ ਵਿਸ਼ੇਸ਼ ਮਦਦ।
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਨੂੰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣਾਉਣ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਤਰੀਕੇ।

ਹੋਰ ਵਿਸਥਾਰ ਨਾਲ ਲਾਗੂਆਈ ਲਈ, ਸਾਡਾ [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) ਵੇਖੋ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
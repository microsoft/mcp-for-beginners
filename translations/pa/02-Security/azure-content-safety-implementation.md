# MCP ਨਾਲ Azure Content Safety ਦੀ ਲਾਗੂਆਈ

MCP ਦੀ ਸੁਰੱਖਿਆ ਨੂੰ prompt injection, tool poisoning ਅਤੇ ਹੋਰ AI-ਵਿਸ਼ੇਸ਼ ਖਤਰਨਾਕੀਆਂ ਤੋਂ ਮਜ਼ਬੂਤ ਬਣਾਉਣ ਲਈ, Azure Content Safety ਨੂੰ ਸ਼ਾਮਲ ਕਰਨਾ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹੈ।

## MCP ਸਰਵਰ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

ਆਪਣੇ MCP ਸਰਵਰ ਨਾਲ Azure Content Safety ਨੂੰ ਜੋੜਨ ਲਈ, content safety filter ਨੂੰ middleware ਵਜੋਂ ਆਪਣੇ request processing pipeline ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ:

1. ਸਰਵਰ ਸ਼ੁਰੂ ਹੋਣ ਸਮੇਂ filter ਨੂੰ initialize ਕਰੋ  
2. ਸਾਰੇ ਆਉਣ ਵਾਲੇ tool requests ਨੂੰ ਪ੍ਰੋਸੈਸਿੰਗ ਤੋਂ ਪਹਿਲਾਂ validate ਕਰੋ  
3. ਸਾਰੇ ਜਾ ਰਹੇ responses ਨੂੰ clients ਨੂੰ ਵਾਪਸ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਚੈੱਕ ਕਰੋ  
4. ਸੁਰੱਖਿਆ ਉਲੰਘਣਾਂ ਦੀ ਲਾਗਿੰਗ ਅਤੇ ਅਲਰਟਿੰਗ ਕਰੋ  
5. content safety checks ਫੇਲ ਹੋਣ 'ਤੇ ਢੰਗ ਨਾਲ error handling ਲਾਗੂ ਕਰੋ  

ਇਹ ਮਜ਼ਬੂਤ ਸੁਰੱਖਿਆ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:  
- Prompt injection ਹਮਲਿਆਂ ਤੋਂ  
- Tool poisoning ਕੋਸ਼ਿਸ਼ਾਂ ਤੋਂ  
- ਮਾਲਿਸ਼ੀਅਸ ਇਨਪੁੱਟਾਂ ਰਾਹੀਂ ਡਾਟਾ ਚੋਰੀ ਤੋਂ  
- ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਤੋਂ  

## Azure Content Safety ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ ਵਧੀਆ ਅਭਿਆਸ

1. **Custom Blocklists**: MCP injection ਪੈਟਰਨਾਂ ਲਈ ਖਾਸ custom blocklists ਬਣਾਓ  
2. **Severity Tuning**: ਆਪਣੇ ਖਾਸ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਖਤਰੇ ਦੀ ਸਹਿਣਸ਼ੀਲਤਾ ਦੇ ਅਧਾਰ 'ਤੇ severity thresholds ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ  
3. **Comprehensive Coverage**: ਸਾਰੇ ਇਨਪੁੱਟ ਅਤੇ ਆਉਟਪੁੱਟ 'ਤੇ content safety checks ਲਗਾਓ  
4. **Performance Optimization**: ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ content safety checks ਲਈ caching ਲਾਗੂ ਕਰਨ ਬਾਰੇ ਸੋਚੋ  
5. **Fallback Mechanisms**: ਜਦੋਂ content safety ਸੇਵਾਵਾਂ ਉਪਲਬਧ ਨਾ ਹੋਣ, ਤਾਂ ਸਪਸ਼ਟ fallback ਵਿਹਾਰ ਨਿਰਧਾਰਤ ਕਰੋ  
6. **User Feedback**: ਜਦੋਂ ਸਮੱਗਰੀ ਸੁਰੱਖਿਆ ਕਾਰਨਾਂ ਕਰਕੇ ਰੋਕੀ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਸਪਸ਼ਟ ਫੀਡਬੈਕ ਦਿਓ  
7. **Continuous Improvement**: ਨਵੇਂ ਖਤਰਿਆਂ ਦੇ ਅਧਾਰ 'ਤੇ blocklists ਅਤੇ ਪੈਟਰਨਾਂ ਨੂੰ ਨਿਯਮਤ ਅਪਡੇਟ ਕਰੋ

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
# ਕੈਲਕुलेਟਰ LLM ਕਲਾਇੰਟ

> [!NOTE]
> ਇਹ ਹੱਲ ਕੋਰਸ ਦੇ ਲੈਗੇਸੀ HTTP+SSE ਕੈਲਕुलेਟਰ ਸੇਵਾ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ
> MCP `2025-11-25` SDK API ਨੂੰ ਟਾਰਗਟ ਕਰਦਾ ਹੈ। ਇਹ `2026-07-28` ਸਟ੍ਰੀਮੇਬਲ HTTP
> ਉਦਾਹਰਨ ਨਹੀਂ ਹੈ।

ਇੱਕ ਜਾਵਾ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ LangChain4j ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP (ਮਾਡਲ ਕਾਨਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ) ਕੈਲਕुलेਟਰ ਸੇਵਾ ਨਾਲ MiniMax OpenAI-ਸਹਿਯੋਗੀ API ਰਾਹੀਂ ਜੁੜਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਲੋੜੀਂਦੇ ਸ਼ਰਤਾਂ

- ਜਾਵਾ 21 ਜਾਂ ਉੱਪਰ
- Maven 3.6+ (ਜਾਂ ਸ਼ਾਮਲ Maven ਵੇਪਰ ਦੀ ਵਰਤੋਂ ਕਰੋ)
- ਇੱਕ MiniMax API ਕੁੰਜੀ
- ਇੱਕ MCP ਕੈਲਕुलेਟਰ ਸੇਵਾ ਜੋ `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਹੀ ਹੋਵੇ

## API ਕੁੰਜੀ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਇਹ ਐਪਲੀਕੇਸ਼ਨ MiniMax OpenAI-ਸਹਿਯੋਗੀ API ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। ਆਪਣੀ ਕੁੰਜੀ ਅਤੇ ਏਂਡਪਾਇੰਟ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਅਨੁਸਰਣ ਕਰੋ:

### 1. ਇੱਕ ਏਂਡਪਾਇੰਟ ਚੁਣੋ
1. ਗਲੋਬਲ ਏਂਡਪਾਇੰਟ ਲਈ `https://api.minimax.io/v1` ਦੀ ਵਰਤੋਂ ਕਰੋ
2. ਚੀਨ ਏਂਡਪਾਇੰਟ ਲਈ `https://api.minimaxi.com/v1` ਦੀ ਵਰਤੋਂ ਕਰੋ

### 2. API ਕੁੰਜੀ ਬਣਾਓ
1. ਆਪਣੇ MiniMax ਖਾਤੇ ਵਿੱਚੋਂ ਇੱਕ MiniMax API ਕੁੰਜੀ ਬਣਾਓ
2. ਕੁੰਜੀ ਨੂੰ ਸੁਰੱਖਿਅਤ ਥਾਂ ਤੇ ਰੱਖੋ

### 3. ਵਾਤਾਵਰਣ ਬਦਲਚਲ ਸੈੱਟ ਕਰੋ

#### Windows (ਕਮਾਂਡ ਪ੍ਰੰਪਟ) 'ਤੇ:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (ਪਾਵਰਸ਼ੇਲ) 'ਤੇ:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux 'ਤੇ:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## ਸੈਟਅੱਪ ਅਤੇ ਇੰਸਟਾਲੇਸ਼ਨ

1. **ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਕਲੋਨ ਕਰੋ ਜਾਂ ਉਸ ਤੱਕ ਜਾਓ**

2. **ਡਿਪੇਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ**:
   ```cmd
   mvnw clean install
   ```
   ਜਾਂ ਜੇ ਤੁਹਾਡੇ ਕੋਲ Maven ਗਲੋਬਲੀ ਇੰਸਟਾਲ ਹੈ:
   ```cmd
   mvn clean install
   ```

3. **ਵਾਤਾਵਰਣ ਬਦਲਚਲ ਸੈੱਟ ਕਰੋ** ("API ਕੁੰਜੀ ਪ੍ਰਾਪਤ ਕਰਨਾ" ਸੈਕਸ਼ਨ ਦੇਖੋ)

4. **MCP ਕੈਲਕुलेਟਰ ਸੇਵਾ ਸਟਾਰਟ ਕਰੋ**:
   ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਅਧਿਆਇ 1 ਦੀ MCP ਕੈਲਕुलेਟਰ ਸੇਵਾ `http://localhost:8080/sse` 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ। ਇਹ ਕਲਾਇੰਟ ਸਟਾਰਟ ਕਰਨ ਤੱਕ ਚੱਲ ਰਹੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

## ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣਾ

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਐਪਲੀਕੇਸ਼ਨ ਕੀ ਕਰਦੀ ਹੈ

ਐਪਲੀਕੇਸ਼ਨ ਕੈਲਕुलेਟਰ ਸੇਵਾ ਨਾਲ ਤਿੰਨ ਮੁੱਖ ਬਾਤਚੀਤ ਦਿਖਾਉਂਦੀ ਹੈ:

1. **ਜੋੜ**: 24.5 ਅਤੇ 17.3 ਦਾ ਜੋੜ ਗਣਨਾ ਕਰਦਾ ਹੈ
2. **ਵਰਗਮੂਲ**: 144 ਦਾ ਵਰਗਮੂਲ ਗਣਨਾ ਕਰਦਾ ਹੈ
3. **ਮਦਦ**: ਉਪਲਬਧ ਕੈਲਕुलेਟਰ ਫੰਕਸ਼ਨਾਂ ਦਿਖਾਉਂਦਾ ਹੈ

## ਉਮੀਦਵਾਰ ਨਤੀਜਾ

ਜਦੋਂ ਸਫਲਤਾਪੂਰਵਕ ਚੱਲਦਾ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ ਇਲ੍ਹਾਂ ਨਤੀਜੇ ਵੇਖਣ ਨੂੰ ਮਿੰਨ ਦੇਣੇ ਚਾਹੀਦੇ ਹਨ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ਸਮੱਸਿਆ ਸੁਰਾਹਣਾ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **"OPENAI_API_KEY ਵਾਤਾਵਰਣ ਬਦਲਚਲ ਸੈੱਟ ਨਹੀਂ ਹੈ"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ `OPENAI_API_KEY` ਵਾਤਾਵਰਣ ਬਦਲਚਲ ਸੈੱਟ ਕੀਤਾ ਹੈ
   - ਬਦਲ ਜਾਣ ਤੋਂ ਬਾਅਦ ਆਪਣੇ ਟਰਮੀਨਲ/ਕਮਾਂਡ ਪ੍ਰੰਪਟ ਨੂੰ ਫਿਰ ਤੋਂ ਸਟਾਰਟ ਕਰੋ

2. **"localhost:8080 ਨਾਲ ਕਨੈਕਸ਼ਨ ਨਾਕਾਮ"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ MCP ਕੈਲਕुलेਟਰ ਸੇਵਾ ਪੋਰਟ 8080 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ
   - ਦੇਖੋ ਕਿ ਕੋਈ ਹੋਰ ਸੇਵਾ ਪੋਰਟ 8080 ਦੀ ਵਰਤੋਂ ਨਾ ਕਰ ਰਹੀ ਹੋਵੇ

3. **"ਪਹਿਚਾਣ ਪਰਖ ਅਸਫਲ"**
   - ਚੈੱਕ ਕਰੋ ਕਿ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਮਾਨਯ ਹੈ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ `OPENAI_BASE_URL` ਉਸ ਏਂਡਪਾਇੰਟ ਨਾਲ ਮੇਲ ਰੱਖਦਾ ਹੈ ਜੋ ਤੁਸੀਂ ਵਰਤਣੀ ਸੀ

4. **Maven ਬਿਲਡ ਦੀਆਂ ਗਲਤੀਆਂ**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਜਾਵਾ 21 ਜਾਂ ਉੱਪਰ ਵਰਤ ਰਹੇ ਹੋ: `java -version`
   - ਬਿਲਡ ਸਾਫ਼ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ: `mvnw clean`

### ਡੀਬੱਗਿੰਗ

ਡੀਬੱਗ ਲੌਗਿੰਗ ਚਾਲੂ ਕਰਨ ਲਈ, ਚਲਾਉਂਦੇ ਸਮੇਂ ਹੇਠਾਂ ਦਿੱਤਾ JVM ਆਰਗੁਮੈਂਟ ਸ਼ਾਮਲ ਕਰੋ:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਸੰਰਚਨਾ

ਐਪਲੀਕੇਸ਼ਨ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਸੰਰਚਿਤ ਹੈ:
- ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ MiniMax-M3 ਦੀ ਵਰਤੋਂ; `MINIMAX_MODEL_ID` ਸੈੱਟ ਕਰਕੇ `MiniMax-M3` ਜਾਂ `MiniMax-M2.7` ਚੁਣੋ
- ਜਦੋਂ `OPENAI_BASE_URL` ਸੈੱਟ ਹੋ ਤਾਂ ਉਸ ਨਾਲ ਜੁੜੋ; ਨਹੀਂ ਤਾਂ ਜਦੋਂ `MINIMAX_REGION=cn_zh` ਹੋ ਤਾਂ `https://api.minimaxi.com/v1` ਵਰਤੋਂ, ਨਹੀਂ ਤਾਂ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ `https://api.minimax.io/v1`
- MCP ਸੇਵਾ `http://localhost:8080/sse` 'ਤੇ ਜੁੜੋ
- ਅਰਜ਼ੀਆਂ ਲਈ 60 ਸਕਿੰਟ ਦਾ ਟਾਈਮਆਊਟ ਵਰਤੋਂ

## ਡਿਪੇਂਡੈਂਸੀਜ਼

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਵਰਤੀ ਗਈ ਮੁੱਖ ਡਿਪੇਂਡੈਂਸੀਜ਼:
- **LangChain4j**: AI ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ ਟੂਲ ਪ੍ਰਬੰਧਨ ਲਈ
- **LangChain4j MCP**: ਮਾਡਲ ਕਾਨਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ ਸਹਿਯੋਗ ਲਈ
- **LangChain4j OpenAI ਅਧਿਕਾਰਿਤ**: MiniMax OpenAI-ਸਹਿਯੋਗੀ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ
- **Spring Boot**: ਐਪਲੀਕੇਸ਼ਨ ਫ੍ਰੇਮਵਰਕ ਅਤੇ ਡਿਪੇਂਡੈਂਸੀ ਇੰਜੈਕਸ਼ਨ ਲਈ

## ਲਾਈਸੈਂਸ

ਇਹ ਪ੍ਰੋਜੈਕਟ Apache ਲਾਈਸੈਂਸ 2.0 ਦੇ ਤਹਿਤ ਲਾਈਸੈਂਸ ਕੀਤਾ ਗਿਆ ਹੈ - ਵੇਰਵੇ ਲਈ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ਫਾਈਲ ਵੇਖੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# ਕੈਲਕੁਲੇਟਰ LLM ਕਲਾਇੰਟ

ਇੱਕ ਜਾਵਾ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ LangChain4j ਦਾ ਉਪਯੋਗ ਕਰਕੇ MCP (ਮਾਡਲ ਕੌਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ) ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ ਨਾਲ MiniMax OpenAI-ਅਨੁਕੂਲ API ਰਾਹੀਂ ਜੁੜਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਜ਼ਰੂਰੀਆਂ

- ਜਾਵਾ 21 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ
- Maven 3.6+ (ਜਾਂ ਸ਼ਾਮਲ Maven ਵ੍ਰੈਪਰ ਦੀ ਵਰਤੋਂ ਕਰੋ)
- ਇੱਕ MiniMax API ਕੀ
- `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਹੀ MCP ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ

## API ਕੀ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਇਹ ਐਪਲੀਕੇਸ਼ਨ MiniMax OpenAI-ਅਨੁਕੂਲ API ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। ਆਪਣੀ ਕੀ ਅਤੇ ਇੰਡੀਪੌਇੰਟ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਇਹਨਾਂ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

### 1. ਇੱਕ ਇੰਡੀਪੌਇੰਟ ਚੁਣੋ
1. ਗਲੋਬਲ ਇੰਡੀਪੌਇੰਟ ਲਈ `https://api.minimax.io/v1` ਦੀ ਵਰਤੋਂ ਕਰੋ
2. ਚੀਨ ਇੰਡੀਪੌਇੰਟ ਲਈ `https://api.minimaxi.com/v1` ਦੀ ਵਰਤੋਂ ਕਰੋ

### 2. ਇੱਕ API ਕੀ ਬਣਾਓ
1. ਆਪਣੇ MiniMax ਖਾਤੇ ਤੋਂ MiniMax API ਕੀ ਬਣਾਓ
2. ਕੁਝ ਸੁਰੱਖਿਅਤ ਸਥਾਨ 'ਤੇ ਕੀ ਸੰਭਾਲ ਕੇ ਰੱਖੋ

### 3. ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ

#### ਵਿੰਡੋਜ਼ (ਕਮਾਂਡ ਪ੍ਰਾਂਪਟ) 'ਤੇ:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### ਵਿੰਡੋਜ਼ (ਪਾਵਰਸ਼ੈੱਲ) 'ਤੇ:
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

## ਸੈਟਅਪ ਅਤੇ ਇੰਸਟਾਲੇਸ਼ਨ

1. **ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ ਜਾਂ ਜਾਣੂ ਹੋਵੋ**

2. **ਨਾੂਲਤਜ਼ਮ ਇੰਸਟਾਲ ਕਰੋ**:
   ```cmd
   mvnw clean install
   ```
   ਜਾਂ ਜੇ ਤੁਹਾਡੇ ਕੋਲ Maven ਵਿਸ਼ਵ-ਸਤਰ 'ਤੇ ਇੰਸਟਾਲ ਹੈ ਤਾਂ:
   ```cmd
   mvn clean install
   ```

3. **ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ** (ਉਪਰ "API ਕੀ ਪ੍ਰਾਪਤ ਕਰਨਾ" ਸੈਕਸ਼ਨ ਵੇਖੋ)

4. **MCP ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ ਸਟਾਰਟ ਕਰੋ**:
   ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਅੰਸ਼ 1 ਦੀ MCP ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ `http://localhost:8080/sse` 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ। ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਚੱਲਦੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

## ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣਾ

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਐਪਲੀਕੇਸ਼ਨ ਕੀ ਕਰਦਾ ਹੈ

ਐਪਲੀਕੇਸ਼ਨ ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ ਨਾਲ ਤਿੰਨ ਮੁੱਖ ਇੰਟਰਐਕਸ਼ਨਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ:

1. **ਜੋੜ**: 24.5 ਅਤੇ 17.3 ਦਾ ਜੋੜ ਗਣਨਾ ਕਰਦਾ ਹੈ
2. **ਵਰਗਮੂਲ**: 144 ਦਾ ਵਰਗਮੂਲ ਗਣਨਾ ਕਰਦਾ ਹੈ
3. **ਮਦਦ**: ਉਪਲਬਧ ਕੈਲਕੁਲੇਟਰ ਫੰਕਸ਼ਨਾਂ ਦਿਖਾਉਂਦਾ ਹੈ

## ਉਮੀਦ ਕੀਤੀ ਨਤੀਜਾ

ਜਦੋਂ ਸੁਚੱਜੇ ਤੌਰ 'ਤੇ ਚੱਲਦਾ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ ਲਗਭਗ ਇੰਝ ਨਤੀਜਾ ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ਸਮੱਸਿਆ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **"OPENAI_API_KEY ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਸੈੱਟ ਨਹੀਂ ਹੈ"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ `OPENAI_API_KEY` ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕੀਤਾ ਹੈ
   - ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਆਪਣਾ ਟਰਮੀਨਲ/ਕਮਾਂਡ ਪ੍ਰਾਂਪਟ ਰੀਸਟਾਰਟ ਕਰੋ

2. **"localhost:8080 ਨਾਲ ਕਨੈਕਸ਼ਨ ਇਨਕਾਰ ਕਰ ਦਿੱਤਾ"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ MCP ਕੈਲਕੁਲੇਟਰ ਸਰਵਿਸ ਪੋਰਟ 8080 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ
   - ਜਾਂਚੋ ਕਿ ਕੋਈ ਹੋਰ ਸਰਵਿਸ ਪੋਰਟ 8080 ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰ ਰਹੀ

3. **"ਪਛਾਣ ਸਫਲ ਨਹੀਂ ਹੋਈ"**
   - ਆਪਣੇ API ਕੀ ਦੀ ਸਹੀਤਾ ਜਾਂਚੋ
   - ਇਹ ਵੇਖੋ ਕਿ `OPENAI_BASE_URL` ਉਸ ਇੰਡੀਪੌਇੰਟ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ

4. **Maven ਬਿਲਡ ਸਮੱਸਿਆਵਾਂ**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਜਾਵਾ 21 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਵਰਤ ਰਹੇ ਹੋ: `java -version`
   - ਬਿਲਡ ਸਾਫ਼ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ: `mvnw clean`

### ਡિਬੱਗਿੰਗ

ਡિਬੱਗ ਲਾਗਿੰਗ ਚਾਲੂ ਕਰਨ ਲਈ, ਚਲਾਉਂਦੇ ਸਮੇਂ ਹੇਠਾਂ ਦਿੱਤਾ JVM_ARGUMENT ਸ਼ਾਮਲ ਕਰੋ:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਸੰਰਚਨਾ

ਐਪਲੀਕੇਸ਼ਨ ਤਰਤੀਬਬੱਧ ਹੈ:
- ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ MiniMax-M3 ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ; `MINIMAX_MODEL_ID` ਸੈੱਟ ਕਰਕੇ ਜਾਂ ਤਾਂ `MiniMax-M3` ਜਾਂ `MiniMax-M2.7` ਚੁਣਿਆ ਜਾ ਸਕਦਾ ਹੈ
- ਜਦੋਂ `OPENAI_BASE_URL` ਸੈੱਟ ਹੁੰਦਾ ਹੈ ਤਾਂ ਇਸ ਨਾਲ ਜੁੜਦਾ ਹੈ; ਨਹੀਂ ਤਾਂ ਜੇ `MINIMAX_REGION=cn_zh` ਹੈ ਤਾਂ `https://api.minimaxi.com/v1` ਜਾਂ ਡਿਫਾਲਟ ਵਜੋਂ `https://api.minimax.io/v1` ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ
- MCP ਸਰਵਿਸ ਨਾਲ `http://localhost:8080/sse` 'ਤੇ ਜੁੜਦਾ ਹੈ
- ਬੇਨਤੀਆਂ ਲਈ 60 ਸਕਿੰਟ ਦਾ ਟਾਈਮਆਉਟ ਵਰਤਦਾ ਹੈ

## ਨਿਰਭਰਤਾਵਾਂ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਮੂਲ ਨਿਰਭਰਤਾਵਾਂ:
- **LangChain4j**: AI ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ ਟੂਲ ਪ੍ਰਬੰਧਨ ਲਈ
- **LangChain4j MCP**: ਮਾਡਲ ਕੌਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ ਸਮਰਥਨ ਲਈ
- **LangChain4j OpenAI ਅਧਿਕਾਰਿਕ**: MiniMax OpenAI-ਅਨੁਕੂਲ API ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਲਈ
- **Spring Boot**: ਐਪਲੀਕੇਸ਼ਨ ਫ੍ਰੇਮਵਰਕ ਅਤੇ ਨਿਰਭਰਤਾ ਇੰਜੈਕਸ਼ਨ ਲਈ

## ਲਾਇਸੈਂਸ

ਇਹ ਪ੍ਰੋਜੈਕਟ Apache ਲਾਇਸੈਂਸ 2.0 ਤਹਿਤ ਲਾਇਸੈਂਸਸ਼ੁਦਾ ਹੈ - ਵੇਰਵੇ ਲਈ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ਫਾਇਲ ਦੇਖੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
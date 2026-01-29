# Calculator LLM Client

ਇੱਕ ਜਾਵਾ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕਿਵੇਂ LangChain4j ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP (Model Context Protocol) ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ ਨਾਲ GitHub Models ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਨਾਲ ਕਨੈਕਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਲੋੜੀਂਦੇ ਚੀਜ਼ਾਂ

- ਜਾਵਾ 21 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਵਰਜਨ
- Maven 3.6+ (ਜਾਂ ਸ਼ਾਮਲ Maven wrapper ਦੀ ਵਰਤੋਂ ਕਰੋ)
- GitHub Models ਤੱਕ ਪਹੁੰਚ ਵਾਲਾ GitHub ਖਾਤਾ
- `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਹੀ MCP ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ

## GitHub ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਇਹ ਐਪਲੀਕੇਸ਼ਨ GitHub Models ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜਿਸ ਲਈ GitHub ਨਿੱਜੀ ਪਹੁੰਚ ਟੋਕਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਆਪਣਾ ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

### 1. GitHub Models ਤੱਕ ਪਹੁੰਚ ਕਰੋ
1. [GitHub Models](https://github.com/marketplace/models) 'ਤੇ ਜਾਓ
2. ਆਪਣੇ GitHub ਖਾਤੇ ਨਾਲ ਸਾਈਨ ਇਨ ਕਰੋ
3. ਜੇ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ ਤਾਂ GitHub Models ਲਈ ਪਹੁੰਚ ਦੀ ਬੇਨਤੀ ਕਰੋ

### 2. ਨਿੱਜੀ ਪਹੁੰਚ ਟੋਕਨ ਬਣਾਓ
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) 'ਤੇ ਜਾਓ
2. "Generate new token" → "Generate new token (classic)" 'ਤੇ ਕਲਿੱਕ ਕਰੋ
3. ਆਪਣੇ ਟੋਕਨ ਨੂੰ ਕੋਈ ਵਿਆਖਿਆਤਮਕ ਨਾਮ ਦਿਓ (ਜਿਵੇਂ "MCP Calculator Client")
4. ਜਰੂਰਤ ਮੁਤਾਬਕ ਮਿਆਦ ਸੈੱਟ ਕਰੋ
5. ਹੇਠਾਂ ਦਿੱਤੇ ਸਕੋਪ ਚੁਣੋ:
   - `repo` (ਜੇ ਪ੍ਰਾਈਵੇਟ ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਤੱਕ ਪਹੁੰਚ ਚਾਹੀਦੀ ਹੈ)
   - `user:email`
6. "Generate token" 'ਤੇ ਕਲਿੱਕ ਕਰੋ
7. **ਮਹੱਤਵਪੂਰਨ**: ਟੋਕਨ ਨੂੰ ਤੁਰੰਤ ਕਾਪੀ ਕਰੋ - ਇਸਨੂੰ ਦੁਬਾਰਾ ਨਹੀਂ ਦੇਖਿਆ ਜਾ ਸਕਦਾ!

### 3. ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ

#### Windows (Command Prompt) 'ਤੇ:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) 'ਤੇ:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux 'ਤੇ:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## ਸੈਟਅਪ ਅਤੇ ਇੰਸਟਾਲੇਸ਼ਨ

1. **ਪ੍ਰੋਜੈਕਟ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ ਜਾਂ ਉਸ ਵਿੱਚ ਜਾਓ**

2. **ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ**:
   ```cmd
   mvnw clean install
   ```
   ਜਾਂ ਜੇ ਤੁਹਾਡੇ ਕੋਲ Maven ਗਲੋਬਲੀ ਇੰਸਟਾਲ ਹੈ:
   ```cmd
   mvn clean install
   ```

3. **ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰੋ** (ਉਪਰ "Getting the GitHub Token" ਸੈਕਸ਼ਨ ਵੇਖੋ)

4. **MCP ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ ਸ਼ੁਰੂ ਕਰੋ**:
   ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਚੈਪਟਰ 1 ਦੀ MCP ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ `http://localhost:8080/sse` 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ। ਇਹ ਕਲਾਇੰਟ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਚੱਲ ਰਹੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

## ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣਾ

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਐਪਲੀਕੇਸ਼ਨ ਕੀ ਕਰਦਾ ਹੈ

ਐਪਲੀਕੇਸ਼ਨ ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ ਨਾਲ ਤਿੰਨ ਮੁੱਖ ਇੰਟਰੈਕਸ਼ਨਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ:

1. **ਜੋੜ**: 24.5 ਅਤੇ 17.3 ਦਾ ਜੋੜ ਕੈਲਕੂਲੇਟ ਕਰਦਾ ਹੈ
2. **ਵਰਗਮੂਲ**: 144 ਦਾ ਵਰਗਮੂਲ ਕੈਲਕੂਲੇਟ ਕਰਦਾ ਹੈ
3. **ਮਦਦ**: ਉਪਲਬਧ ਕੈਲਕੂਲੇਟਰ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਦਿਖਾਉਂਦਾ ਹੈ

## ਉਮੀਦ ਕੀਤੀ ਨਤੀਜਾ

ਸਫਲਤਾਪੂਰਵਕ ਚਲਾਉਣ 'ਤੇ, ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

1. **"GITHUB_TOKEN environment variable not set"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ `GITHUB_TOKEN` ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕੀਤਾ ਹੈ
   - ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਟਰਮੀਨਲ/ਕਮਾਂਡ ਪ੍ਰਾਂਪਟ ਨੂੰ ਰੀਸਟਾਰਟ ਕਰੋ

2. **"Connection refused to localhost:8080"**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ MCP ਕੈਲਕੂਲੇਟਰ ਸਰਵਿਸ ਪੋਰਟ 8080 'ਤੇ ਚੱਲ ਰਹੀ ਹੈ
   - ਦੇਖੋ ਕਿ ਕੋਈ ਹੋਰ ਸਰਵਿਸ ਪੋਰਟ 8080 ਦੀ ਵਰਤੋਂ ਤਾਂ ਨਹੀਂ ਕਰ ਰਹੀ

3. **"Authentication failed"**
   - ਆਪਣੇ GitHub ਟੋਕਨ ਦੀ ਵੈਧਤਾ ਅਤੇ ਸਹੀ ਅਧਿਕਾਰਾਂ ਦੀ ਜਾਂਚ ਕਰੋ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ GitHub Models ਤੱਕ ਪਹੁੰਚ ਹੈ

4. **Maven ਬਿਲਡ ਗਲਤੀਆਂ**
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਜਾਵਾ 21 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਵਰਜਨ ਵਰਤ ਰਹੇ ਹੋ: `java -version`
   - ਬਿਲਡ ਸਾਫ਼ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ: `mvnw clean`

### ਡੀਬੱਗਿੰਗ

ਡੀਬੱਗ ਲੌਗਿੰਗ ਚਾਲੂ ਕਰਨ ਲਈ, ਚਲਾਉਂਦੇ ਸਮੇਂ ਹੇਠਾਂ ਦਿੱਤਾ JVM ਆਰਗੁਮੈਂਟ ਸ਼ਾਮਲ ਕਰੋ:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ਸੰਰਚਨਾ

ਐਪਲੀਕੇਸ਼ਨ ਇਸ ਤਰ੍ਹਾਂ ਸੰਰਚਿਤ ਹੈ:
- GitHub Models ਨੂੰ `gpt-4.1-nano` ਮਾਡਲ ਨਾਲ ਵਰਤਣਾ
- MCP ਸਰਵਿਸ ਨਾਲ `http://localhost:8080/sse` 'ਤੇ ਕਨੈਕਟ ਕਰਨਾ
- ਬੇਨਤੀ ਲਈ 60 ਸਕਿੰਟ ਦਾ ਟਾਈਮਆਉਟ ਸੈੱਟ ਕਰਨਾ
- ਡੀਬੱਗਿੰਗ ਲਈ ਬੇਨਤੀ/ਜਵਾਬ ਲੌਗਿੰਗ ਚਾਲੂ ਕਰਨਾ

## ਡਿਪੈਂਡੈਂਸੀਜ਼

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਵਰਤੇ ਗਏ ਮੁੱਖ ਡਿਪੈਂਡੈਂਸੀਜ਼:
- **LangChain4j**: AI ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ ਟੂਲ ਮੈਨੇਜਮੈਂਟ ਲਈ
- **LangChain4j MCP**: Model Context Protocol ਸਹਾਇਤਾ ਲਈ
- **LangChain4j GitHub Models**: GitHub Models ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ
- **Spring Boot**: ਐਪਲੀਕੇਸ਼ਨ ਫਰੇਮਵਰਕ ਅਤੇ ਡਿਪੈਂਡੈਂਸੀ ਇੰਜੈਕਸ਼ਨ ਲਈ

## ਲਾਇਸੈਂਸ

ਇਹ ਪ੍ਰੋਜੈਕਟ Apache License 2.0 ਅਧੀਨ ਲਾਇਸੈਂਸ ਕੀਤਾ ਗਿਆ ਹੈ - ਵਿਸਥਾਰ ਲਈ [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) ਫਾਈਲ ਵੇਖੋ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
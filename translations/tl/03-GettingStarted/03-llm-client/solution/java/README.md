# Calculator LLM Client

Isang Java application na nagpapakita kung paano gamitin ang LangChain4j upang kumonekta sa isang MCP (Model Context Protocol) na serbisyo ng calculator sa pamamagitan ng MiniMax OpenAI-compatible API.

## Mga Kinakailangan

- Java 21 o mas mataas pa
- Maven 3.6+ (o gamitin ang kasama na Maven wrapper)
- Isang MiniMax API key
- Isang MCP calculator service na tumatakbo sa `http://localhost:8080`

## Pagkuha ng API Key

Ginagamit ng application na ito ang MiniMax OpenAI-compatible API. Sundin ang mga hakbang na ito upang makuha ang iyong key at endpoint:

### 1. Pumili ng endpoint
1. Gamitin ang `https://api.minimax.io/v1` para sa global endpoint
2. Gamitin ang `https://api.minimaxi.com/v1` para sa China endpoint

### 2. Gumawa ng API key
1. Gumawa ng MiniMax API key mula sa iyong MiniMax account
2. Itago ang key sa isang ligtas na lugar

### 3. Itakda ang Mga Environment Variables

#### Sa Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Sa Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Sa macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Pagsasaayos at Pag-install

1. **I-clone o pumunta sa direktoryo ng proyekto**

2. **I-install ang mga dependencies**:
   ```cmd
   mvnw clean install
   ```
   O kung naka-install ang Maven globally:
   ```cmd
   mvn clean install
   ```

3. **I-set up ang mga environment variables** (tingnan ang seksyong "Pagkuha ng API Key" sa itaas)

4. **Simulan ang MCP Calculator Service**:
   Siguraduhing tumatakbo ang MCP calculator service mula sa kabanata 1 sa `http://localhost:8080/sse`. Dapat ito ay tumatakbo bago mo simulan ang client.

## Paano Patakbuhin ang Application

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ano ang Ginagawa ng Application

Ipinapakita ng application ang tatlong pangunahing interaksyon sa calculator service:

1. **Addition**: Kinakalkula ang kabuuan ng 24.5 at 17.3
2. **Square Root**: Kinakalkula ang square root ng 144
3. **Help**: Ipinapakita ang mga magagamit na function ng calculator

## Inaasahang Output

Kapag matagumpay ang pagtakbo, makikita mo ang output na katulad ng:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Pag-troubleshoot

### Karaniwang Suliranin

1. **"OPENAI_API_KEY environment variable is not set"**
   - Siguraduhing naitakda mo ang `OPENAI_API_KEY` environment variable
   - I-restart ang terminal/command prompt matapos itakda ang variable

2. **"Connection refused to localhost:8080"**
   - Tiyakin na tumatakbo ang MCP calculator service sa port 8080
   - Suriin kung may ibang serbisyo na gumagamit ng port 8080

3. **"Authentication failed"**
   - I-verify kung valid ang iyong API key
   - Suriin na ang `OPENAI_BASE_URL` ay tumutugma sa endpoint na iyong nilayon gamitin

4. **Mga error sa Maven build**
   - Tiyakin na gumagamit ka ng Java 21 o mas mataas: `java -version`
   - Subukang linisin ang build: `mvnw clean`

### Pag-debug

Upang paganahin ang debug logging, idagdag ang sumusunod na JVM argument kapag nagpapagana:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasyon

Ang application ay naka-configure upang:
- Gumamit ng MiniMax-M3 bilang default; itakda ang `MINIMAX_MODEL_ID` upang piliin ang `MiniMax-M3` o `MiniMax-M2.7`
- Kumonekta sa `OPENAI_BASE_URL` kapag ito ay nakaset; kung hindi ay gamitin ang `https://api.minimaxi.com/v1` kapag `MINIMAX_REGION=cn_zh`, o `https://api.minimax.io/v1` bilang default
- Kumonekta sa MCP service sa `http://localhost:8080/sse`
- Gumamit ng 60-segundong timeout para sa mga request

## Mga Dependencies

Mga pangunahing dependencies na ginagamit sa proyektong ito:
- **LangChain4j**: Para sa AI integration at pamamahala ng tools
- **LangChain4j MCP**: Para sa suporta ng Model Context Protocol
- **LangChain4j OpenAI official**: Para sa integrasyon ng MiniMax OpenAI-compatible API
- **Spring Boot**: Para sa application framework at dependency injection

## Lisensya

Ang proyektong ito ay inililisensyahan sa ilalim ng Apache License 2.0 - tingnan ang [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) na file para sa mga detalye.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
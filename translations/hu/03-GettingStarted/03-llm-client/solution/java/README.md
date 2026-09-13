# Számológép LLM kliens

> [!NOTE]
> Ez a megoldás csatlakozik a tanfolyam régi HTTP+SSE számológép szolgáltatásához, és
> az MCP `2025-11-25` SDK API-kat célozza meg. Ez nem egy `2026-07-28` Streamable HTTP
> példa.

Egy Java alkalmazás, amely bemutatja, hogyan lehet a LangChain4j-t használni az MCP (Model Context Protocol) számológép szolgáltatáshoz való kapcsolódáshoz a MiniMax OpenAI-kompatibilis API-n keresztül.

## Előfeltételek

- Java 21 vagy újabb
- Maven 3.6+ (vagy használja a mellékelt Maven wrappert)
- Egy MiniMax API-kulcs
- Egy MCP számológép szolgáltatás fut a `http://localhost:8080` címen

## API-kulcs beszerzése

Ez az alkalmazás a MiniMax OpenAI-kompatibilis API-t használja. Kövesse az alábbi lépéseket a kulcs és az végpont megszerzéséhez:

### 1. Válasszon végpontot
1. Használja a `https://api.minimax.io/v1` című globális végpontot
2. Használja a `https://api.minimaxi.com/v1` című kínai végpontot

### 2. Hozzon létre API kulcsot
1. Hozzon létre MiniMax API kulcsot MiniMax fiókjából
2. Tartsa biztonságos helyen a kulcsot

### 3. Állítsa be a környezeti változókat

#### Windows rendszeren (Parancssor):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows rendszeren (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux rendszeren:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Beállítás és telepítés

1. **Klónozza vagy navigáljon a projekt könyvtárába**

2. **Telepítse a függőségeket**:
   ```cmd
   mvnw clean install
   ```
   Vagy ha globálisan telepítve van a Maven:
   ```cmd
   mvn clean install
   ```

3. **Állítsa be a környezeti változókat** (lásd a fenti "API-kulcs beszerzése" részt)

4. **Indítsa el az MCP számológép szolgáltatást**:
   Győződjön meg, hogy az 1. fejezet MCP számológép szolgáltatása fut a `http://localhost:8080/sse` címen. Ennek futnia kell, mielőtt elindítja a klienst.

## Az alkalmazás futtatása

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mit csinál az alkalmazás

Az alkalmazás három fő interakciót demonstrál a számológép szolgáltatással:

1. **Összeadás**: Kiszámolja 24.5 és 17.3 összegét
2. **Négyzetgyök**: Kiszámolja 144 négyzetgyökét
3. **Segítség**: Megjeleníti a rendelkezésre álló számológép funkciókat

## Várható kimenet

Ha sikeresen fut, hasonló kimenetet kell látnia:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Hibaelhárítás

### Gyakori problémák

1. **„OPENAI_API_KEY környezeti változó nincs beállítva”**
   - Győződjön meg róla, hogy beállította az `OPENAI_API_KEY` környezeti változót
   - Indítsa újra a terminált/parancssort a változó beállítása után

2. **„Kapcsolat megtagadva localhost:8080 címen”**
   - Ellenőrizze, hogy az MCP számológép szolgáltatás fut-e a 8080-as porton
   - Ellenőrizze, hogy nem használja-e valamelyik szolgáltatás a 8080-as portot

3. **„Hitelesítés sikertelen”**
   - Ellenőrizze, hogy az API kulcsa érvényes-e
   - Győződjön meg róla, hogy az `OPENAI_BASE_URL` megfelel annak a végpontnak, amit használni szeretett volna

4. **Maven build hibák**
   - Győződjön meg róla, hogy Java 21 vagy újabb verziót használ: `java -version`
   - Próbálja meg kitisztítani a buildet: `mvnw clean`

### Hibakeresés

A hibakeresési naplózás engedélyezéséhez adja hozzá a következő JVM argumentumot a futtatáskor:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguráció

Az alkalmazás az alábbiak szerint van konfigurálva:
- Alapértelmezésként a MiniMax-M3 modellt használja; állítsa be a `MINIMAX_MODEL_ID` változót, hogy kiválassza a `MiniMax-M3` vagy `MiniMax-M2.7` modellt
- Ha be van állítva, csatlakozik az `OPENAI_BASE_URL`-hoz; különben a `MINIMAX_REGION=cn_zh` esetén a `https://api.minimaxi.com/v1`, egyébként a `https://api.minimax.io/v1` végpontot használja alapértelmezettként
- Csatlakozik az MCP szolgáltatáshoz a `http://localhost:8080/sse` címen
- Kérésenként 60 másodperces időkorlátot használ

## Függőségek

A projekt kulcsfontosságú függőségei:
- **LangChain4j**: AI integrációhoz és eszközkezeléshez
- **LangChain4j MCP**: Model Context Protocol támogatáshoz
- **LangChain4j OpenAI hivatalos**: MiniMax OpenAI-kompatibilis API integrációhoz
- **Spring Boot**: Alkalmazáskerethez és függőség-injektáláshoz

## Licenc

Ez a projekt az Apache License 2.0 licenc alatt áll - részletekért lásd a [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) fájlt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
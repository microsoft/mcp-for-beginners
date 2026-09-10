# Számológép LLM kliens

Egy Java alkalmazás, amely bemutatja, hogyan használható a LangChain4j egy MCP (Model Context Protocol) számológép szolgáltatáshoz való csatlakozáshoz a MiniMax OpenAI-kompatibilis API-n keresztül.

## Előfeltételek

- Java 21 vagy újabb
- Maven 3.6+ (vagy használd a mellékelt Maven wrappert)
- Egy MiniMax API kulcs
- Egy MCP számológép szolgáltatás, amely a `http://localhost:8080` címen fut

## Az API kulcs beszerzése

Ez az alkalmazás a MiniMax OpenAI-kompatibilis API-t használja. A kulcs és az végpont megszerzéséhez kövesd az alábbi lépéseket:

### 1. Válassz egy végpontot
1. A globális végponthoz használd a `https://api.minimax.io/v1` címet
2. A kínai végponthoz használd a `https://api.minimaxi.com/v1` címet

### 2. Készíts API kulcsot
1. Hozz létre egy MiniMax API kulcsot a MiniMax fiókodból
2. Tartsd biztonságos helyen a kulcsot

### 3. Állítsd be a környezeti változókat

#### Windows rendszerben (Parancssor):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows rendszerben (PowerShell):
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

## Telepítés és beállítás

1. **Klónozd vagy navigálj a projekt könyvtárába**

2. **Telepítsd a függőségeket**:
   ```cmd
   mvnw clean install
   ```
   Vagy ha globálisan telepítve van a Maven:
   ```cmd
   mvn clean install
   ```

3. **Állítsd be a környezeti változókat** (lásd a "Az API kulcs beszerzése" részt fent)

4. **Indítsd el az MCP számológép szolgáltatást**:
   Győződj meg róla, hogy az 1. fejezet MCP számológép szolgáltatása fut a `http://localhost:8080/sse` címen. Ennek futnia kell, mielőtt elindítod a klienst.

## Az alkalmazás futtatása

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mit csinál az alkalmazás

Az alkalmazás három fő interakciót mutat be a számológép szolgáltatással:

1. **Összeadás**: Kiszámolja 24.5 és 17.3 összegét
2. **Négyzetgyök**: Kiszámolja 144 négyzetgyökét
3. **Súgó**: Megjeleníti a rendelkezésre álló számológép funkciókat

## Várt kimenet

Sikeres futtatás esetén hasonló kimenetet kell látnod:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Hibakeresés

### Gyakori problémák

1. **"OPENAI_API_KEY környezeti változó nincs beállítva"**
   - Győződj meg róla, hogy beállítottad az `OPENAI_API_KEY` környezeti változót
   - Indítsd újra a terminált/parancssort a változó beállítása után

2. **"Kapcsolódás megtagadva localhost:8080"**
   - Ellenőrizd, hogy az MCP számológép szolgáltatás fut-e a 8080-as porton
   - Nézd meg, hogy nem foglalja-e el más szolgáltatás a 8080-as portot

3. **"Hitelesítés sikertelen"**
   - Ellenőrizd, hogy az API kulcsod érvényes
   - Győződj meg róla, hogy az `OPENAI_BASE_URL` megfelel a szándékolt végpontnak

4. **Maven build hibák**
   - Ellenőrizd, hogy Java 21 vagy újabbat használsz: `java -version`
   - Próbáld meg tisztítani a buildet: `mvnw clean`

### Hibakeresés

A hibakereső naplózás engedélyezéséhez add hozzá az alábbi JVM argumentumot a futtatáskor:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguráció

Az alkalmazás a következőképp van konfigurálva:
- Alapértelmezés szerint a MiniMax-M3 modellt használja; a `MINIMAX_MODEL_ID` beállításával választható a `MiniMax-M3` vagy a `MiniMax-M2.7`
- Csatlakozik az `OPENAI_BASE_URL`-hez ha be van állítva; egyébként a `https://api.minimaxi.com/v1`-et használja, ha `MINIMAX_REGION=cn_zh`, vagy alapértelmezésben a `https://api.minimax.io/v1` végpontot
- Csatlakozik az MCP szolgáltatáshoz a `http://localhost:8080/sse` címen
- 60 másodperces időkorlátot használ a kérésekhez

## Függőségek

A projektben használt kulcsfüggőségek:
- **LangChain4j**: AI integráció és eszközkezelés
- **LangChain4j MCP**: Model Context Protocol támogatás
- **LangChain4j OpenAI hivatalos**: MiniMax OpenAI-kompatibilis API integráció
- **Spring Boot**: Alkalmazáskeret és függőség-injektálás

## Licenc

Ez a projekt az Apache License 2.0 alatt van licencelve - további részletekért lásd a [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) fájlt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
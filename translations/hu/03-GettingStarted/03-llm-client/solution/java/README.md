# Számológép LLM kliens

Egy Java alkalmazás, amely bemutatja, hogyan lehet a LangChain4j használatával MCP (Model Context Protocol) számológép szolgáltatáshoz csatlakozni a MiniMax OpenAI-kompatibilis API-n keresztül.

## Előfeltételek

- Java 21 vagy újabb
- Maven 3.6+ (vagy használd a mellékelt Maven wrapper-t)
- Egy MiniMax API kulcs
- Egy MCP számológép szolgáltatás futtatása `http://localhost:8080` címen

## Az API kulcs beszerzése

Ez az alkalmazás a MiniMax OpenAI-kompatibilis API-t használja. Kövesd az alábbi lépéseket az API kulcsod és a végpont beszerzéséhez:

### 1. Válassz egy végpontot
1. Használd a `https://api.minimax.io/v1` globális végponthoz
2. Használd a `https://api.minimaxi.com/v1` Kínai végponthoz

### 2. API kulcs létrehozása
1. Hozz létre egy MiniMax API kulcsot a MiniMax fiókodból
2. Tárold el biztonságos helyen a kulcsot

### 3. Állítsd be a környezeti változókat

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

1. **Klónozd vagy lépj be a projekt könyvtárba**

2. **Telepítsd a függőségeket**:
   ```cmd
   mvnw clean install
   ```
   Vagy ha globálisan telepítve van a Maven:
   ```cmd
   mvn clean install
   ```

3. **Állítsd be a környezeti változókat** (lásd a fenti "Az API kulcs beszerzése" részt)

4. **Indítsd el az MCP Számológép Szolgáltatást**:
   Győződj meg róla, hogy az 1. fejezetbeli MCP számológép szolgáltatás fut `http://localhost:8080/sse` címen. Ennek futnia kell, mielőtt elindítanád a klienst.

## Az alkalmazás futtatása

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mit csinál az alkalmazás

Az alkalmazás három fő interakciót mutat be a számológép szolgáltatással:

1. **Összeadás**: Kiszámolja 24,5 és 17,3 összegét
2. **Négyzetgyök**: Kiszámolja 144 négyzetgyökét
3. **Súgó**: Megjeleníti a rendelkezésre álló számológép funkciókat

## Várt kimenet

Sikeres futtatás esetén hasonló kimenetet kell látnod:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Hibaelhárítás

### Gyakori problémák

1. **"OPENAI_API_KEY környezeti változó nincs beállítva"**
   - Győződj meg róla, hogy beállítottad az `OPENAI_API_KEY` környezeti változót
   - Indítsd újra a terminált/parancssort a változó beállítása után

2. **"Csatlakozás megtagadva a localhost:8080-hoz"**
   - Ellenőrizd, hogy az MCP számológép szolgáltatás fut-e a 8080-as porton
   - Nézd meg, hogy nincs-e más szolgáltatás, ami használja a 8080-as portot

3. **"Hitelesítés sikertelen"**
   - Ellenőrizd, hogy az API kulcs érvényes-e
   - Győződj meg róla, hogy az `OPENAI_BASE_URL` megfelel annak a végpontnak, amit használni akartál

4. **Maven build hibák**
   - Ellenőrizd, hogy Java 21 vagy újabb van használatban: `java -version`
   - Próbáld meg kitisztítani a buildet: `mvnw clean`

### Hibakeresés

A hibakereső naplózás engedélyezéséhez add hozzá a következő JVM argumentumot a futtatáskor:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguráció

Az alkalmazás a következőképpen van konfigurálva:
- Alapértelmezettként MiniMax-M3 modellt használ, vagy MiniMax-M2.7-et, ha a `MINIMAX_MODEL_ID` be van állítva
- Csatlakozik az `OPENAI_BASE_URL`-hez, ha az be van állítva; különben használja a `https://api.minimaxi.com/v1` címet, ha a `MINIMAX_REGION=cn_zh`, vagy egyébként a `https://api.minimax.io/v1` címet
- Csatlakozik az MCP szolgáltatáshoz a `http://localhost:8080/sse` címen
- 60 másodperces időkorlátot használ a kérésekhez

## Függőségek

A projektben használt kulcsfontosságú függőségek:
- **LangChain4j**: AI integrációhoz és eszközkezeléshez
- **LangChain4j MCP**: Model Context Protocol támogatásához
- **LangChain4j OpenAI hivatalos**: MiniMax OpenAI-kompatibilis API integrációhoz
- **Spring Boot**: Alkalmazás keretrendszerhez és függőség injektáláshoz

## Licenc

Ez a projekt az Apache License 2.0 alatt van licencelve - részletekért lásd a [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) fájlt.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
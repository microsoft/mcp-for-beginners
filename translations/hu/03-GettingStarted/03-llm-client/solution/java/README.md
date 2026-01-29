# Calculator LLM Client

Egy Java alkalmazás, amely bemutatja, hogyan használható a LangChain4j az MCP (Model Context Protocol) kalkulátor szolgáltatáshoz való kapcsolódáshoz GitHub Models integrációval.

## Előfeltételek

- Java 21 vagy újabb
- Maven 3.6+ (vagy használd a mellékelt Maven wrappert)
- GitHub fiók, amely hozzáfér a GitHub Models-hez
- Egy MCP kalkulátor szolgáltatás fut a `http://localhost:8080` címen

## A GitHub Token beszerzése

Ez az alkalmazás GitHub Models-t használ, amihez szükség van egy GitHub személyes hozzáférési tokenre. Kövesd az alábbi lépéseket a token megszerzéséhez:

### 1. Lépj be a GitHub Models-be
1. Nyisd meg a [GitHub Models](https://github.com/marketplace/models) oldalt
2. Jelentkezz be a GitHub fiókoddal
3. Kérj hozzáférést a GitHub Models-hez, ha még nem tetted meg

### 2. Hozz létre egy személyes hozzáférési tokent
1. Menj a [GitHub Beállítások → Fejlesztői beállítások → Személyes hozzáférési tokenek → Tokenek (klasszikus)](https://github.com/settings/tokens) oldalra
2. Kattints a "Generate new token" → "Generate new token (classic)" gombra
3. Adj a tokennek egy beszédes nevet (pl. "MCP Calculator Client")
4. Állítsd be a lejárati időt igény szerint
5. Válaszd ki a következő jogosultságokat:
   - `repo` (ha privát repókhoz is hozzáférsz)
   - `user:email`
6. Kattints a "Generate token" gombra
7. **Fontos**: Másold ki a tokent azonnal – később már nem fogod látni!

### 3. Állítsd be a környezeti változót

#### Windows (Parancssor):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Beállítás és telepítés

1. **Klónozd vagy lépj be a projekt könyvtárába**

2. **Telepítsd a függőségeket**:
   ```cmd
   mvnw clean install
   ```
   Vagy ha globálisan telepítve van a Maven:
   ```cmd
   mvn clean install
   ```

3. **Állítsd be a környezeti változót** (lásd a "A GitHub Token beszerzése" részt fent)

4. **Indítsd el az MCP Calculator szolgáltatást**:
   Győződj meg róla, hogy az 1. fejezetben bemutatott MCP kalkulátor szolgáltatás fut a `http://localhost:8080/sse` címen. Ennek el kell indulnia, mielőtt elindítod a klienst.

## Az alkalmazás futtatása

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mit csinál az alkalmazás

Az alkalmazás három fő interakciót mutat be a kalkulátor szolgáltatással:

1. **Összeadás**: Kiszámolja 24.5 és 17.3 összegét
2. **Négyzetgyök**: Kiszámolja 144 négyzetgyökét
3. **Segítség**: Megjeleníti a rendelkezésre álló kalkulátor funkciókat

## Várt kimenet

Sikeres futtatás esetén hasonló kimenetet kell látnod:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Hibakeresés

### Gyakori problémák

1. **"GITHUB_TOKEN környezeti változó nincs beállítva"**
   - Ellenőrizd, hogy beállítottad-e a `GITHUB_TOKEN` környezeti változót
   - Indítsd újra a terminált/parancssort a változó beállítása után

2. **"Connection refused to localhost:8080"**
   - Győződj meg róla, hogy az MCP kalkulátor szolgáltatás fut a 8080-as porton
   - Ellenőrizd, hogy nem foglalja-e más szolgáltatás a 8080-as portot

3. **"Authentication failed"**
   - Ellenőrizd, hogy a GitHub token érvényes és megfelelő jogosultságokkal rendelkezik
   - Győződj meg róla, hogy hozzáférsz a GitHub Models-hez

4. **Maven build hibák**
   - Ellenőrizd, hogy Java 21 vagy újabb verziót használsz: `java -version`
   - Próbáld meg tisztítani a buildet: `mvnw clean`

### Hibakeresés

A debug naplózás engedélyezéséhez add hozzá a következő JVM argumentumot a futtatáskor:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguráció

Az alkalmazás a következő beállításokkal működik:
- GitHub Models használata a `gpt-4.1-nano` modellel
- Kapcsolódás az MCP szolgáltatáshoz a `http://localhost:8080/sse` címen
- 60 másodperces timeout a kérésekhez
- Kérés/válasz naplózás engedélyezve a hibakereséshez

## Függőségek

A projekt főbb függőségei:
- **LangChain4j**: AI integrációhoz és eszközkezeléshez
- **LangChain4j MCP**: Model Context Protocol támogatáshoz
- **LangChain4j GitHub Models**: GitHub Models integrációhoz
- **Spring Boot**: Alkalmazás keretrendszerhez és függőség injektáláshoz

## Licenc

Ez a projekt az Apache License 2.0 alatt áll - részletekért lásd a [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) fájlt.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
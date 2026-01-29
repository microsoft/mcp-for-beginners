# Calculator HTTP Streaming Demo

Ez a projekt a HTTP streaminget mutatja be Server-Sent Events (SSE) használatával Spring Boot WebFlux keretrendszerrel. Két alkalmazásból áll:

- **Calculator Server**: Egy reaktív webszolgáltatás, amely számításokat végez és SSE segítségével továbbítja az eredményeket
- **Calculator Client**: Egy kliens alkalmazás, amely fogyasztja a streaming végpontot

## Előfeltételek

- Java 17 vagy újabb
- Maven 3.6 vagy újabb

## Projekt felépítése

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Hogyan működik

1. A **Calculator Server** egy `/calculate` végpontot biztosít, amely:
   - Elfogadja a lekérdezési paramétereket: `a` (szám), `b` (szám), `op` (művelet)
   - Támogatott műveletek: `add`, `sub`, `mul`, `div`
   - Server-Sent Events formájában küldi a számítás előrehaladását és az eredményt

2. A **Calculator Client** kapcsolódik a szerverhez és:
   - Lekér egy számítást: `7 * 5`
   - Fogyasztja a streaming választ
   - Kiírja az eseményeket a konzolra

## Az alkalmazások futtatása

### 1. lehetőség: Maven használata (ajánlott)

#### 1. Indítsd el a Calculator Server-t

Nyiss egy terminált és lépj be a szerver könyvtárába:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

A szerver elindul a `http://localhost:8080` címen

Ilyen kimenetet kell látnod:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Futtasd a Calculator Client-et

Nyiss egy **új terminált** és lépj be a kliens könyvtárába:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

A kliens kapcsolódik a szerverhez, elvégzi a számítást, és megjeleníti a streaming eredményeket.

### 2. lehetőség: Java közvetlen használata

#### 1. Fordítsd és futtasd a szervert:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Fordítsd és futtasd a klienst:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## A szerver kézi tesztelése

A szervert böngészőből vagy curl segítségével is tesztelheted:

### Böngésző használata:
Látogass el ide: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl használata:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Várt kimenet

A kliens futtatásakor hasonló streaming kimenetet kell látnod:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Támogatott műveletek

- `add` - Összeadás (a + b)
- `sub` - Kivonás (a - b)
- `mul` - Szorzás (a * b)
- `div` - Osztás (a / b, NaN-t ad vissza, ha b = 0)

## API referencia

### GET /calculate

**Paraméterek:**
- `a` (kötelező): Első szám (double)
- `b` (kötelező): Második szám (double)
- `op` (kötelező): Művelet (`add`, `sub`, `mul`, `div`)

**Válasz:**
- Content-Type: `text/event-stream`
- Server-Sent Events formájában küldi a számítás előrehaladását és az eredményt

**Példa kérés:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Példa válasz:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Hibakeresés

### Gyakori problémák

1. **A 8080-as port már foglalt**
   - Állítsd le azokat az alkalmazásokat, amelyek használják a 8080-as portot
   - Vagy módosítsd a szerver portját a `calculator-server/src/main/resources/application.yml` fájlban

2. **Kapcsolat elutasítva**
   - Győződj meg róla, hogy a szerver fut, mielőtt elindítod a klienst
   - Ellenőrizd, hogy a szerver sikeresen elindult a 8080-as porton

3. **Paraméternév problémák**
   - A projekt tartalmazza a Maven fordító konfigurációját a `-parameters` kapcsolóval
   - Ha paraméter kötési problémákba ütközöl, győződj meg róla, hogy a projekt ezzel a beállítással lett fordítva

### Az alkalmazások leállítása

- Nyomd meg a `Ctrl+C` billentyűkombinációt abban a terminálban, ahol az alkalmazás fut
- Vagy használd a `mvn spring-boot:stop` parancsot, ha háttérben futtatod

## Technológiai stack

- **Spring Boot 3.3.1** - Alkalmazás keretrendszer
- **Spring WebFlux** - Reaktív web keretrendszer
- **Project Reactor** - Reaktív stream könyvtár
- **Netty** - Nem blokkoló I/O szerver
- **Maven** - Build eszköz
- **Java 17+** - Programozási nyelv

## Következő lépések

Próbáld meg módosítani a kódot, hogy:
- Több matematikai műveletet adj hozzá
- Hibakezelést valósíts meg érvénytelen műveletek esetén
- Kérés/válasz naplózást adj hozzá
- Hitelesítést valósíts meg
- Egységteszteket írj

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
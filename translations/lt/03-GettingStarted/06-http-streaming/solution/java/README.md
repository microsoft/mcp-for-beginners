# Skaičiuotuvo HTTP srautinio perdavimo demonstracija

Šis projektas demonstruoja HTTP srautinį perdavimą naudojant Server-Sent Events (SSE) su Spring Boot WebFlux. Jį sudaro dvi programos:

- **Skaičiuotuvo serveris**: Reaktyvi žiniatinklio paslauga, atliekanti skaičiavimus ir perduodanti rezultatus per SSE
- **Skaičiuotuvo klientas**: Kliento programa, kuri naudoja srautinį galinį tašką

## Reikalavimai

- Java 17 ar naujesnė
- Maven 3.6 ar naujesnė

## Projekto struktūra

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

## Kaip tai veikia

1. **Skaičiuotuvo serveris** pateikia `/calculate` galinį tašką, kuris:
   - Priima užklausos parametrus: `a` (skaičius), `b` (skaičius), `op` (operacija)
   - Palaikomos operacijos: `add`, `sub`, `mul`, `div`
   - Grąžina Server-Sent Events su skaičiavimo eiga ir rezultatu

2. **Skaičiuotuvo klientas** prisijungia prie serverio ir:
   - Atlieka užklausą skaičiavimui `7 * 5`
   - Naudoja srautinį atsakymą
   - Spausdina kiekvieną įvykį į konsolę

## Programų paleidimas

### 1 variantas: Naudojant Maven (rekomenduojama)

#### 1. Paleiskite Skaičiuotuvo serverį

Atidarykite terminalą ir eikite į serverio katalogą:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Serveris bus paleistas adresu `http://localhost:8080`

Turėtumėte matyti tokį išvestį:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Paleiskite Skaičiuotuvo klientą

Atidarykite **naują terminalą** ir eikite į kliento katalogą:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klientas prisijungs prie serverio, atliks skaičiavimą ir parodys srautinius rezultatus.

### 2 variantas: Naudojant Java tiesiogiai

#### 1. Kompiliuokite ir paleiskite serverį:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompiliuokite ir paleiskite klientą:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Serverio testavimas rankiniu būdu

Taip pat galite išbandyti serverį naudodami žiniatinklio naršyklę arba curl:

### Naudojant žiniatinklio naršyklę:
Aplankykite: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Naudojant curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Tikėtina išvestis

Paleidus klientą, turėtumėte matyti srautinę išvestį, panašią į:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Palaikomos operacijos

- `add` - Sudėtis (a + b)
- `sub` - Atimtis (a - b)
- `mul` - Daugyba (a * b)
- `div` - Dalyba (a / b, grąžina NaN, jei b = 0)

## API nuoroda

### GET /calculate

**Parametrai:**
- `a` (privalomas): Pirmas skaičius (double)
- `b` (privalomas): Antras skaičius (double)
- `op` (privalomas): Operacija (`add`, `sub`, `mul`, `div`)

**Atsakymas:**
- Turinys-Tipas: `text/event-stream`
- Grąžina Server-Sent Events su skaičiavimo eiga ir rezultatu

**Pavyzdinė užklausa:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Pavyzdinis atsakymas:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Trikčių šalinimas

### Dažnos problemos

1. **Portas 8080 jau naudojamas**
   - Sustabdykite kitas programas, naudojančias portą 8080
   - Arba pakeiskite serverio portą faile `calculator-server/src/main/resources/application.yml`

2. **Ryšys atmestas**
   - Įsitikinkite, kad serveris veikia prieš paleisdami klientą
   - Patikrinkite, ar serveris sėkmingai paleistas porte 8080

3. **Problemos su parametrų pavadinimais**
   - Šis projektas naudoja Maven kompiliatoriaus konfigūraciją su `-parameters` vėliava
   - Jei susiduriate su parametrų susiejimo problemomis, įsitikinkite, kad projektas sukompiliuotas su šia konfigūracija

### Programų sustabdymas

- Paspauskite `Ctrl+C` terminale, kuriame veikia programa
- Arba naudokite `mvn spring-boot:stop`, jei programa veikia fone

## Technologijų rinkinys

- **Spring Boot 3.3.1** - Programų kūrimo karkasas
- **Spring WebFlux** - Reaktyvus žiniatinklio karkasas
- **Project Reactor** - Reaktyvių srautų biblioteka
- **Netty** - Ne-blokuojantis I/O serveris
- **Maven** - Kūrimo įrankis
- **Java 17+** - Programavimo kalba

## Kiti žingsniai

Pabandykite pakeisti kodą, kad:
- Pridėtumėte daugiau matematinių operacijų
- Įtrauktumėte klaidų tvarkymą neteisingoms operacijoms
- Pridėtumėte užklausų/atsakymų žurnalavimą
- Įgyvendintumėte autentifikaciją
- Pridėtumėte vienetinius testus

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama kreiptis į profesionalius vertėjus. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.
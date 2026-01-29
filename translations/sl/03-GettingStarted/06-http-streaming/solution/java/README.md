# Calculator HTTP Streaming Demo

Ta projekt prikazuje HTTP pretakanje z uporabo Server-Sent Events (SSE) s Spring Boot WebFlux. Sestavljen je iz dveh aplikacij:

- **Calculator Server**: reaktivna spletna storitev, ki izvaja izračune in pretaka rezultate z uporabo SSE
- **Calculator Client**: odjemalska aplikacija, ki uporablja pretakanje iz strežniškega konca

## Predpogoji

- Java 17 ali novejša
- Maven 3.6 ali novejši

## Struktura projekta

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

## Kako deluje

1. **Calculator Server** ponuja `/calculate` endpoint, ki:
   - Sprejema parametre poizvedbe: `a` (število), `b` (število), `op` (operacija)
   - Podprte operacije: `add`, `sub`, `mul`, `div`
   - Vrača Server-Sent Events s potekom izračuna in rezultatom

2. **Calculator Client** se poveže na strežnik in:
   - Pošlje zahtevo za izračun `7 * 5`
   - Porabi pretakajoči odgovor
   - Vsak dogodek izpiše na konzolo

## Zagon aplikacij

### Možnost 1: Uporaba Mavena (priporočeno)

#### 1. Zaženi Calculator Server

Odpri terminal in pojdi v imenik strežnika:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Strežnik se bo zagnal na `http://localhost:8080`

Videti bi moral izpis, kot je:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Zaženi Calculator Client

Odpri **nov terminal** in pojdi v imenik odjemalca:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Odjemalec se bo povezal na strežnik, izvedel izračun in prikazal rezultate pretakanja.

### Možnost 2: Neposreden zagon z Javo

#### 1. Prevedi in zaženi strežnik:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Prevedi in zaženi odjemalca:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ročno testiranje strežnika

Strežnik lahko preizkusiš tudi z brskalnikom ali curl:

### Z brskalnikom:
Obišči: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Z curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Pričakovani izpis

Ob zagonu odjemalca bi moral videti pretakajoči izpis, podoben temu:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Podprte operacije

- `add` - seštevanje (a + b)
- `sub` - odštevanje (a - b)
- `mul` - množenje (a * b)
- `div` - deljenje (a / b, vrne NaN, če je b = 0)

## API Referenca

### GET /calculate

**Parametri:**
- `a` (obvezen): prvo število (double)
- `b` (obvezen): drugo število (double)
- `op` (obvezen): operacija (`add`, `sub`, `mul`, `div`)

**Odgovor:**
- Content-Type: `text/event-stream`
- Vrača Server-Sent Events s potekom izračuna in rezultatom

**Primer zahteve:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Primer odgovora:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Reševanje težav

### Pogoste težave

1. **Vrata 8080 so že zasedena**
   - Ustavi druge aplikacije, ki uporabljajo vrata 8080
   - Ali spremeni vrata strežnika v `calculator-server/src/main/resources/application.yml`

2. **Povezava zavrnjena**
   - Prepričaj se, da je strežnik zagnan pred zagonom odjemalca
   - Preveri, da se je strežnik uspešno zagnal na vratih 8080

3. **Težave z imeni parametrov**
   - Projekt vključuje Maven konfiguracijo prevajalnika z zastavico `-parameters`
   - Če naletiš na težave z vezavo parametrov, poskrbi, da je projekt zgrajen s to konfiguracijo

### Ustavitev aplikacij

- Pritisni `Ctrl+C` v terminalu, kjer teče vsaka aplikacija
- Ali uporabi `mvn spring-boot:stop`, če teče kot ozadinski proces

## Tehnološki sklad

- **Spring Boot 3.3.1** - aplikacijski okvir
- **Spring WebFlux** - reaktivni spletni okvir
- **Project Reactor** - knjižnica za reaktivne tokove
- **Netty** - strežnik z neblokirnim I/O
- **Maven** - orodje za gradnjo
- **Java 17+** - programski jezik

## Naslednji koraki

Poskusi spremeniti kodo, da:
- Dodaš več matematičnih operacij
- Vključiš obravnavo napak za neveljavne operacije
- Dodaš beleženje zahtev in odgovorov
- Izvedeš avtentikacijo
- Dodaš enotne teste

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
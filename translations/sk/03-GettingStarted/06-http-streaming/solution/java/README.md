# Calculator HTTP Streaming Demo

Tento projekt demonštruje HTTP streaming pomocou Server-Sent Events (SSE) so Spring Boot WebFlux. Skladá sa z dvoch aplikácií:

- **Calculator Server**: reaktívna webová služba, ktorá vykonáva výpočty a streamuje výsledky pomocou SSE
- **Calculator Client**: klientská aplikácia, ktorá spotrebúva streamingový endpoint

## Požiadavky

- Java 17 alebo novšia
- Maven 3.6 alebo novší

## Štruktúra projektu

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

## Ako to funguje

1. **Calculator Server** sprístupňuje endpoint `/calculate`, ktorý:
   - prijíma query parametre: `a` (číslo), `b` (číslo), `op` (operácia)
   - podporované operácie: `add`, `sub`, `mul`, `div`
   - vracia Server-Sent Events s priebehom výpočtu a výsledkom

2. **Calculator Client** sa pripojí k serveru a:
   - pošle požiadavku na výpočet `7 * 5`
   - spracováva streamingovú odpoveď
   - vypisuje každú udalosť do konzoly

## Spustenie aplikácií

### Možnosť 1: Použitie Maven (odporúčané)

#### 1. Spustenie Calculator Servera

Otvorte terminál a prejdite do adresára servera:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server sa spustí na `http://localhost:8080`

Mali by ste vidieť výstup podobný tomuto:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Spustenie Calculator Clienta

Otvorte **nový terminál** a prejdite do adresára klienta:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klient sa pripojí k serveru, vykoná výpočet a zobrazí streamingové výsledky.

### Možnosť 2: Priame spustenie cez Java

#### 1. Kompilácia a spustenie servera:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompilácia a spustenie klienta:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Manuálne testovanie servera

Server môžete otestovať aj pomocou webového prehliadača alebo curl:

### Použitie webového prehliadača:
Navštívte: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Použitie curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Očakávaný výstup

Pri spustení klienta by ste mali vidieť streamingový výstup podobný tomuto:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Podporované operácie

- `add` - sčítanie (a + b)
- `sub` - odčítanie (a - b)
- `mul` - násobenie (a * b)
- `div` - delenie (a / b, vráti NaN, ak b = 0)

## API Referencia

### GET /calculate

**Parametre:**
- `a` (povinné): prvé číslo (double)
- `b` (povinné): druhé číslo (double)
- `op` (povinné): operácia (`add`, `sub`, `mul`, `div`)

**Odpoveď:**
- Content-Type: `text/event-stream`
- Vracia Server-Sent Events s priebehom výpočtu a výsledkom

**Príklad požiadavky:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Príklad odpovede:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Riešenie problémov

### Bežné problémy

1. **Port 8080 už je obsadený**
   - Zastavte iné aplikácie používajúce port 8080
   - Alebo zmeňte port servera v `calculator-server/src/main/resources/application.yml`

2. **Pripojenie odmietnuté**
   - Uistite sa, že server beží pred spustením klienta
   - Skontrolujte, či sa server úspešne spustil na porte 8080

3. **Problémy s názvami parametrov**
   - Projekt obsahuje Maven konfiguráciu kompilátora s príznakom `-parameters`
   - Ak máte problémy s viazaním parametrov, uistite sa, že projekt je zostavený s touto konfiguráciou

### Zastavenie aplikácií

- Stlačte `Ctrl+C` v termináli, kde aplikácia beží
- Alebo použite `mvn spring-boot:stop`, ak beží na pozadí

## Technologický stack

- **Spring Boot 3.3.1** - aplikačný framework
- **Spring WebFlux** - reaktívny webový framework
- **Project Reactor** - knižnica pre reaktívne streamy
- **Netty** - server s neblokujúcim I/O
- **Maven** - nástroj na buildovanie
- **Java 17+** - programovací jazyk

## Ďalšie kroky

Skúste upraviť kód tak, aby:
- Pridal viac matematických operácií
- Zahrnul spracovanie chýb pre neplatné operácie
- Pridal logovanie požiadaviek/odpovedí
- Implementoval autentifikáciu
- Pridal jednotkové testy

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
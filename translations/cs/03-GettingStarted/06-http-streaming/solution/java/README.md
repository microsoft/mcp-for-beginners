# Calculator HTTP Streaming Demo

Tento projekt demonstruje HTTP streamování pomocí Server-Sent Events (SSE) se Spring Boot WebFlux. Skládá se ze dvou aplikací:

- **Calculator Server**: reaktivní webová služba, která provádí výpočty a streamuje výsledky pomocí SSE
- **Calculator Client**: klientská aplikace, která spotřebovává streamovaný endpoint

## Požadavky

- Java 17 nebo novější
- Maven 3.6 nebo novější

## Struktura projektu

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

## Jak to funguje

1. **Calculator Server** zpřístupňuje endpoint `/calculate`, který:
   - přijímá query parametry: `a` (číslo), `b` (číslo), `op` (operace)
   - podporované operace: `add`, `sub`, `mul`, `div`
   - vrací Server-Sent Events s průběhem výpočtu a výsledkem

2. **Calculator Client** se připojí k serveru a:
   - odešle požadavek na výpočet `7 * 5`
   - spotřebovává streamovanou odpověď
   - vypisuje každou událost do konzole

## Spuštění aplikací

### Možnost 1: Použití Maven (doporučeno)

#### 1. Spuštění Calculator Serveru

Otevřete terminál a přejděte do adresáře serveru:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server poběží na `http://localhost:8080`

Měli byste vidět výstup podobný tomuto:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Spuštění Calculator Clienta

Otevřete **nový terminál** a přejděte do adresáře klienta:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klient se připojí k serveru, provede výpočet a zobrazí streamované výsledky.

### Možnost 2: Přímé spuštění pomocí Java

#### 1. Kompilace a spuštění serveru:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompilace a spuštění klienta:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Manuální testování serveru

Server můžete také otestovat pomocí webového prohlížeče nebo curl:

### Pomocí webového prohlížeče:
Navštivte: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Pomocí curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Očekávaný výstup

Při spuštění klienta byste měli vidět streamovaný výstup podobný tomuto:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Podporované operace

- `add` - sčítání (a + b)
- `sub` - odčítání (a - b)
- `mul` - násobení (a * b)
- `div` - dělení (a / b, vrací NaN pokud b = 0)

## API Reference

### GET /calculate

**Parametry:**
- `a` (povinné): první číslo (double)
- `b` (povinné): druhé číslo (double)
- `op` (povinné): operace (`add`, `sub`, `mul`, `div`)

**Odpověď:**
- Content-Type: `text/event-stream`
- Vrací Server-Sent Events s průběhem výpočtu a výsledkem

**Příklad požadavku:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Příklad odpovědi:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Řešení problémů

### Běžné problémy

1. **Port 8080 je již obsazen**
   - Zastavte jiné aplikace používající port 8080
   - Nebo změňte port serveru v `calculator-server/src/main/resources/application.yml`

2. **Připojení odmítnuto**
   - Ujistěte se, že server běží před spuštěním klienta
   - Zkontrolujte, že server úspěšně startoval na portu 8080

3. **Problémy s názvy parametrů**
   - Projekt obsahuje Maven konfiguraci kompilátoru s příznakem `-parameters`
   - Pokud narazíte na problémy s vázáním parametrů, ujistěte se, že je projekt sestaven s touto konfigurací

### Zastavení aplikací

- Stiskněte `Ctrl+C` v terminálu, kde aplikace běží
- Nebo použijte `mvn spring-boot:stop`, pokud běží na pozadí

## Použité technologie

- **Spring Boot 3.3.1** - aplikační framework
- **Spring WebFlux** - reaktivní webový framework
- **Project Reactor** - knihovna pro reaktivní streamy
- **Netty** - server s neblokujícím I/O
- **Maven** - nástroj pro sestavení
- **Java 17+** - programovací jazyk

## Další kroky

Zkuste upravit kód tak, aby:
- Přidal další matematické operace
- Zahrnul ošetření chyb pro neplatné operace
- Přidal logování požadavků a odpovědí
- Implementoval autentizaci
- Přidal jednotkové testy

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
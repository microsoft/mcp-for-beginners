# Kalkulaatori HTTP voogedastuse demo

See projekt demonstreerib HTTP voogedastust, kasutades Server-Sent Events (SSE) koos Spring Boot WebFluxiga. Projekt koosneb kahest rakendusest:

- **Kalkulaatori server**: Reaktiivne veebiteenus, mis teostab arvutusi ja edastab tulemusi SSE abil
- **Kalkulaatori klient**: Kliendirakendus, mis tarbib voogedastuse lõpp-punkti

## Eeltingimused

- Java 17 või uuem
- Maven 3.6 või uuem

## Projekti struktuur

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

## Kuidas see töötab

1. **Kalkulaatori server** pakub `/calculate` lõpp-punkti, mis:
   - Võtab vastu päringu parameetrid: `a` (arv), `b` (arv), `op` (tehe)
   - Toetatud tehed: `add`, `sub`, `mul`, `div`
   - Tagastab Server-Sent Events voogedastuse arvutuse edenemise ja tulemusega

2. **Kalkulaatori klient** ühendub serveriga ja:
   - Teeb päringu, et arvutada `7 * 5`
   - Tarbib voogedastuse vastust
   - Kuvab iga sündmuse konsoolil

## Rakenduste käivitamine

### Variant 1: Maveni kasutamine (soovitatav)

#### 1. Käivita kalkulaatori server

Ava terminal ja liigu serveri kausta:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server käivitub aadressil `http://localhost:8080`

Peaksid nägema väljundit, mis näeb välja umbes selline:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Käivita kalkulaatori klient

Ava **uus terminal** ja liigu kliendi kausta:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klient ühendub serveriga, teostab arvutuse ja kuvab voogedastuse tulemused.

### Variant 2: Java otse kasutamine

#### 1. Kompileeri ja käivita server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Kompileeri ja käivita klient:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Serveri käsitsi testimine

Serverit saab testida ka veebibrauseri või curl-i abil:

### Veebibrauseri kasutamine:
Külasta: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Curl-i kasutamine:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Oodatav väljund

Kui klienti käivitatakse, peaksid nägema voogedastuse väljundit, mis näeb välja umbes selline:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Toetatud tehed

- `add` - Liitmine (a + b)
- `sub` - Lahutamine (a - b)
- `mul` - Korrutamine (a * b)
- `div` - Jagamine (a / b, tagastab NaN, kui b = 0)

## API viide

### GET /calculate

**Parameetrid:**
- `a` (kohustuslik): Esimene arv (double)
- `b` (kohustuslik): Teine arv (double)
- `op` (kohustuslik): Tehe (`add`, `sub`, `mul`, `div`)

**Vastus:**
- Content-Type: `text/event-stream`
- Tagastab Server-Sent Events voogedastuse arvutuse edenemise ja tulemusega

**Näide päringust:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Näide vastusest:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Tõrkeotsing

### Levinumad probleemid

1. **Port 8080 on juba kasutusel**
   - Peata kõik teised rakendused, mis kasutavad porti 8080
   - Või muuda serveri porti failis `calculator-server/src/main/resources/application.yml`

2. **Ühendus keelatud**
   - Veendu, et server töötab enne kliendi käivitamist
   - Kontrolli, kas server käivitati edukalt pordil 8080

3. **Parameetrite nimede probleemid**
   - See projekt sisaldab Maven kompilaatori konfiguratsiooni `-parameters` lipuga
   - Kui esineb parameetrite sidumise probleeme, veendu, et projekt on selle konfiguratsiooniga ehitatud

### Rakenduste peatamine

- Vajuta `Ctrl+C` terminalis, kus iga rakendus töötab
- Või kasuta `mvn spring-boot:stop`, kui rakendus töötab taustal

## Tehnoloogiline virn

- **Spring Boot 3.3.1** - Rakenduste raamistik
- **Spring WebFlux** - Reaktiivne veebiraamistik
- **Project Reactor** - Reaktiivvoogude teek
- **Netty** - Mitteblokeeriv I/O server
- **Maven** - Ehitustööriist
- **Java 17+** - Programmeerimiskeel

## Järgmised sammud

Proovi koodi muuta, et:
- Lisada rohkem matemaatilisi tehteid
- Lisada veakäsitlus vigaste tehete jaoks
- Lisada päringu/vastuse logimine
- Rakendada autentimine
- Lisada üksustestid

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
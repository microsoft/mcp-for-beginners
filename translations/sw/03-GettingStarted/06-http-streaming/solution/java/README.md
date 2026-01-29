# Calculator HTTP Streaming Demo

Mradi huu unaonyesha utiririshaji wa HTTP kwa kutumia Server-Sent Events (SSE) kwa Spring Boot WebFlux. Unajumuisha programu mbili:

- **Calculator Server**: Huduma ya wavuti inayoreact na kufanya mahesabu na kupeleka matokeo kwa kutumia SSE  
- **Calculator Client**: Programu ya mteja inayotumia kiungo cha utiririshaji

## Mahitaji

- Java 17 au zaidi  
- Maven 3.6 au zaidi

## Muundo wa Mradi

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

## Jinsi Inavyofanya Kazi

1. **Calculator Server** hutoa kiungo `/calculate` ambacho:  
   - Kinakubali vigezo vya query: `a` (nambari), `b` (nambari), `op` (operesheni)  
   - Operesheni zinazotegemewa: `add`, `sub`, `mul`, `div`  
   - Hurejesha Server-Sent Events zenye maendeleo ya mahesabu na matokeo  

2. **Calculator Client** inaunganishwa na server na:  
   - Inatuma ombi la kuhesabu `7 * 5`  
   - Inatumia majibu ya utiririshaji  
   - Inachapisha kila tukio kwenye console  

## Kuendesha Programu

### Chaguo 1: Kutumia Maven (Inapendekezwa)

#### 1. Anzisha Calculator Server

Fungua terminal na uelekeze kwenye saraka ya server:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Server itaanza kwenye `http://localhost:8080`

Utapata matokeo kama haya:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Endesha Calculator Client

Fungua **terminal mpya** na uelekeze kwenye saraka ya client:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Client itaunganishwa na server, itafanya mahesabu, na kuonyesha matokeo ya utiririshaji.

### Chaguo 2: Kutumia Java moja kwa moja

#### 1. Tengeneza na endesha server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Tengeneza na endesha client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Kupima Server Kwa Mikono

Unaweza pia kupima server kwa kutumia kivinjari cha wavuti au curl:

### Kutumia kivinjari cha wavuti:  
Tembelea: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Kutumia curl:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Matokeo Yanayotarajiwa

Unapokimbia client, unapaswa kuona matokeo ya utiririshaji kama ifuatavyo:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operesheni Zinazotegemewa

- `add` - Jumla (a + b)  
- `sub` - Toa (a - b)  
- `mul` - Zidisha (a * b)  
- `div` - Gawanya (a / b, hurejesha NaN ikiwa b = 0)  

## Marejeleo ya API

### GET /calculate

**Vigezo:**  
- `a` (inahitajika): Nambari ya kwanza (double)  
- `b` (inahitajika): Nambari ya pili (double)  
- `op` (inahitajika): Operesheni (`add`, `sub`, `mul`, `div`)  

**Jibu:**  
- Content-Type: `text/event-stream`  
- Hurejesha Server-Sent Events zenye maendeleo ya mahesabu na matokeo  

**Mfano wa Ombi:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Mfano wa Jibu:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Utatuzi wa Matatizo

### Masuala ya Kawaida

1. **Bandari 8080 tayari inatumika**  
   - Zima programu nyingine yoyote inayotumia bandari 8080  
   - Au badilisha bandari ya server katika `calculator-server/src/main/resources/application.yml`  

2. **Muunganisho umekataliwa**  
   - Hakikisha server inaendesha kabla ya kuanzisha client  
   - Angalia server ilianza kwa mafanikio kwenye bandari 8080  

3. **Matatizo ya majina ya vigezo**  
   - Mradi huu unajumuisha usanidi wa Maven compiler na bendera `-parameters`  
   - Ikiwa unakutana na matatizo ya kufunga vigezo, hakikisha mradi umejengwa kwa usanidi huu  

### Kusimamisha Programu

- Bonyeza `Ctrl+C` kwenye terminal ambapo kila programu inaendesha  
- Au tumia `mvn spring-boot:stop` ikiwa inaendesha kama mchakato wa nyuma  

## Teknolojia Zinazotumika

- **Spring Boot 3.3.1** - Mfumo wa programu  
- **Spring WebFlux** - Mfumo wa wavuti unaoreact  
- **Project Reactor** - Maktaba ya mitiririko ya reactive  
- **Netty** - Server isiyozuia I/O  
- **Maven** - Zana ya kujenga programu  
- **Java 17+** - Lugha ya programu  

## Hatua Zifuatazo

Jaribu kubadilisha msimbo ili:  
- Ongeza operesheni zaidi za kihisabati  
- Jumuisha usimamizi wa makosa kwa operesheni zisizo halali  
- Ongeza ufuatiliaji wa maombi/jawabu  
- Tekeleza uthibitishaji  
- Ongeza vipimo vya unit

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
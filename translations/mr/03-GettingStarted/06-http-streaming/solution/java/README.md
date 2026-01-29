# Calculator HTTP Streaming Demo

हा प्रकल्प Spring Boot WebFlux वापरून Server-Sent Events (SSE) द्वारे HTTP स्ट्रीमिंग कसे करायचे हे दाखवतो. यात दोन अ‍ॅप्लिकेशन्स आहेत:

- **Calculator Server**: एक reactive वेब सेवा जी गणिते करते आणि SSE वापरून परिणाम स्ट्रीम करते
- **Calculator Client**: एक क्लायंट अ‍ॅप्लिकेशन जे स्ट्रीमिंग एंडपॉइंट वापरते

## Prerequisites

- Java 17 किंवा त्याहून अधिक
- Maven 3.6 किंवा त्याहून अधिक

## Project Structure

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

## How It Works

1. **Calculator Server** `/calculate` एंडपॉइंट प्रदान करतो जो:
   - क्वेरी पॅरामीटर्स स्वीकारतो: `a` (संख्या), `b` (संख्या), `op` (ऑपरेशन)
   - समर्थित ऑपरेशन्स: `add`, `sub`, `mul`, `div`
   - गणनेची प्रगती आणि निकाल Server-Sent Events स्वरूपात परत करतो

2. **Calculator Client** सर्व्हरशी कनेक्ट होतो आणि:
   - `7 * 5` ची गणना करण्यासाठी विनंती करतो
   - स्ट्रीमिंग प्रतिसाद वापरतो
   - प्रत्येक इव्हेंट कन्सोलवर प्रिंट करतो

## Running the Applications

### Option 1: Maven वापरून (शिफारस केलेले)

#### 1. Calculator Server सुरू करा

टर्मिनल उघडा आणि सर्व्हर डिरेक्टरीमध्ये जा:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

सर्व्हर `http://localhost:8080` वर सुरू होईल

तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client चालवा

नवीन टर्मिनल उघडा आणि क्लायंट डिरेक्टरीमध्ये जा:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

क्लायंट सर्व्हरशी कनेक्ट होईल, गणना करेल आणि स्ट्रीमिंग निकाल दाखवेल.

### Option 2: Java थेट वापरून

#### 1. सर्व्हर कंपाईल आणि चालवा:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. क्लायंट कंपाईल आणि चालवा:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testing the Server Manually

तुम्ही वेब ब्राउझर किंवा curl वापरूनही सर्व्हर तपासू शकता:

### वेब ब्राउझर वापरून:
पत्ता भेट द्या: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl वापरून:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Expected Output

क्लायंट चालवताना तुम्हाला खालीलप्रमाणे स्ट्रीमिंग आउटपुट दिसेल:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Supported Operations

- `add` - बेरीज (a + b)
- `sub` - वजाबाकी (a - b)
- `mul` - गुणाकार (a * b)
- `div` - भागाकार (a / b, जर b = 0 असेल तर NaN परत करते)

## API Reference

### GET /calculate

**Parameters:**
- `a` (आवश्यक): पहिली संख्या (double)
- `b` (आवश्यक): दुसरी संख्या (double)
- `op` (आवश्यक): ऑपरेशन (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- गणनेची प्रगती आणि निकाल Server-Sent Events स्वरूपात परत करते

**Example Request:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Example Response:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Troubleshooting

### Common Issues

1. **पोर्ट 8080 आधीच वापरात आहे**
   - पोर्ट 8080 वापरणारे इतर अ‍ॅप्लिकेशन्स थांबवा
   - किंवा `calculator-server/src/main/resources/application.yml` मध्ये सर्व्हर पोर्ट बदला

2. **कनेक्शन नाकारले गेले**
   - क्लायंट सुरू करण्यापूर्वी सर्व्हर चालू आहे याची खात्री करा
   - सर्व्हर पोर्ट 8080 वर यशस्वीपणे सुरू झाला आहे का ते तपासा

3. **पॅरामीटर नावांच्या समस्या**
   - या प्रकल्पात Maven compiler configuration मध्ये `-parameters` फ्लॅग आहे
   - जर पॅरामीटर बाइंडिंगमध्ये अडचण आली तर प्रकल्प या कॉन्फिगरेशनसह तयार करा

### अ‍ॅप्लिकेशन्स थांबविणे

- प्रत्येक अ‍ॅप्लिकेशन चालू असलेल्या टर्मिनलमध्ये `Ctrl+C` दाबा
- किंवा बॅकग्राउंड प्रोसेस म्हणून चालवताना `mvn spring-boot:stop` वापरा

## Technology Stack

- **Spring Boot 3.3.1** - अ‍ॅप्लिकेशन फ्रेमवर्क
- **Spring WebFlux** - Reactive वेब फ्रेमवर्क
- **Project Reactor** - Reactive streams लायब्ररी
- **Netty** - Non-blocking I/O सर्व्हर
- **Maven** - बिल्ड टूल
- **Java 17+** - प्रोग्रामिंग भाषा

## Next Steps

कोडमध्ये खालील बदल करून पहा:
- अधिक गणिती ऑपरेशन्स जोडा
- अवैध ऑपरेशन्ससाठी त्रुटी हाताळणी समाविष्ट करा
- विनंती/प्रतिसाद लॉगिंग जोडा
- प्रमाणीकरण अंमलात आणा
- युनिट टेस्ट्स जोडा

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
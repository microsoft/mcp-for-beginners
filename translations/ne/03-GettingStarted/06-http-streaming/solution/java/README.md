# Calculator HTTP Streaming Demo

यो प्रोजेक्टले Spring Boot WebFlux सँग Server-Sent Events (SSE) प्रयोग गरी HTTP स्ट्रिमिङ कसरी गर्ने देखाउँछ। यसमा दुईवटा एप्लिकेसनहरू छन्:

- **Calculator Server**: एक प्रतिक्रियाशील वेब सेवा जसले गणना गर्छ र SSE मार्फत परिणाम स्ट्रिम गर्छ
- **Calculator Client**: स्ट्रिमिङ अन्तबिन्दु प्रयोग गर्ने क्लाइन्ट एप्लिकेसन

## आवश्यकताहरू

- Java 17 वा माथि
- Maven 3.6 वा माथि

## प्रोजेक्ट संरचना

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

## यो कसरी काम गर्छ

1. **Calculator Server** ले `/calculate` अन्तबिन्दु प्रदान गर्छ जुन:
   - क्वेरी प्यारामिटरहरू स्वीकार्छ: `a` (संख्या), `b` (संख्या), `op` (अपरेशन)
   - समर्थित अपरेसनहरू: `add`, `sub`, `mul`, `div`
   - गणनाको प्रगति र परिणाम सहित Server-Sent Events फर्काउँछ

2. **Calculator Client** सर्भरसँग जडान हुन्छ र:
   - `7 * 5` गणना गर्न अनुरोध गर्छ
   - स्ट्रिमिङ प्रतिक्रिया उपभोग गर्छ
   - प्रत्येक इभेन्ट कन्सोलमा प्रिन्ट गर्छ

## एप्लिकेसनहरू चलाउने तरिका

### विकल्प १: Maven प्रयोग गरेर (सिफारिस गरिएको)

#### १. Calculator Server सुरु गर्नुहोस्

टर्मिनल खोल्नुहोस् र सर्भर डाइरेक्टरीमा जानुहोस्:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

सर्भर `http://localhost:8080` मा सुरु हुनेछ

तपाईंले यस्तो आउटपुट देख्नुहुनेछ:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### २. Calculator Client चलाउनुहोस्

**नयाँ टर्मिनल** खोल्नुहोस् र क्लाइन्ट डाइरेक्टरीमा जानुहोस्:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

क्लाइन्ट सर्भरसँग जडान हुनेछ, गणना गर्नेछ, र स्ट्रिमिङ परिणाम देखाउनेछ।

### विकल्प २: Java सिधै प्रयोग गरेर

#### १. सर्भर कम्पाइल र चलाउनुहोस्:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### २. क्लाइन्ट कम्पाइल र चलाउनुहोस्:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## सर्भर म्यानुअली परीक्षण गर्ने

तपाईं वेब ब्राउजर वा curl प्रयोग गरेर पनि सर्भर परीक्षण गर्न सक्नुहुन्छ:

### वेब ब्राउजर प्रयोग गरेर:
भिजिट गर्नुहोस्: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl प्रयोग गरेर:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## अपेक्षित आउटपुट

क्लाइन्ट चलाउँदा तपाईंले यस्तो स्ट्रिमिङ आउटपुट देख्नुहुनेछ:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## समर्थित अपरेसनहरू

- `add` - जोड (a + b)
- `sub` - घटाउ (a - b)
- `mul` - गुणा (a * b)
- `div` - भाग (a / b, यदि b = 0 भने NaN फर्काउँछ)

## API सन्दर्भ

### GET /calculate

**प्यारामिटरहरू:**
- `a` (आवश्यक): पहिलो संख्या (double)
- `b` (आवश्यक): दोस्रो संख्या (double)
- `op` (आवश्यक): अपरेशन (`add`, `sub`, `mul`, `div`)

**प्रतिक्रिया:**
- Content-Type: `text/event-stream`
- गणनाको प्रगति र परिणाम सहित Server-Sent Events फर्काउँछ

**उदाहरण अनुरोध:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**उदाहरण प्रतिक्रिया:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## समस्या समाधान

### सामान्य समस्या

1. **पोर्ट 8080 पहिले नै प्रयोगमा छ**
   - पोर्ट 8080 प्रयोग गरिरहेका अन्य एप्लिकेसनहरू बन्द गर्नुहोस्
   - वा `calculator-server/src/main/resources/application.yml` मा सर्भर पोर्ट परिवर्तन गर्नुहोस्

2. **जडान अस्वीकृत**
   - क्लाइन्ट सुरु गर्नु अघि सर्भर चलिरहेको छ भनी सुनिश्चित गर्नुहोस्
   - सर्भर पोर्ट 8080 मा सफलतापूर्वक सुरु भएको छ कि छैन जाँच गर्नुहोस्

3. **प्यारामिटर नाम सम्बन्धी समस्या**
   - यो प्रोजेक्टमा Maven कम्पाइलर कन्फिगरेसन `-parameters` फ्ल्यागसहित छ
   - यदि प्यारामिटर बाइन्डिङमा समस्या आयो भने, प्रोजेक्ट यस कन्फिगरेसनसहित बनाइएको छ कि छैन जाँच गर्नुहोस्

### एप्लिकेसनहरू रोक्ने तरिका

- प्रत्येक एप्लिकेसन चलिरहेको टर्मिनलमा `Ctrl+C` थिच्नुहोस्
- वा ब्याकग्राउन्डमा चलिरहेको भए `mvn spring-boot:stop` प्रयोग गर्नुहोस्

## प्रविधि स्ट्याक

- **Spring Boot 3.3.1** - एप्लिकेसन फ्रेमवर्क
- **Spring WebFlux** - प्रतिक्रियाशील वेब फ्रेमवर्क
- **Project Reactor** - प्रतिक्रियाशील स्ट्रिम लाइब्रेरी
- **Netty** - नन-ब्लकिङ I/O सर्भर
- **Maven** - बिल्ड उपकरण
- **Java 17+** - प्रोग्रामिङ भाषा

## अर्को कदमहरू

कोडमा परिवर्तन गरेर प्रयास गर्नुहोस्:
- थप गणितीय अपरेसनहरू थप्नुहोस्
- अमान्य अपरेसनका लागि त्रुटि ह्यान्डलिङ समावेश गर्नुहोस्
- अनुरोध/प्रतिक्रिया लगिङ थप्नुहोस्
- प्रमाणीकरण कार्यान्वयन गर्नुहोस्
- युनिट टेस्टहरू थप्नुहोस्

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
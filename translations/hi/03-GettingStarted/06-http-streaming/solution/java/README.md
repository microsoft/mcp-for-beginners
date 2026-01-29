# Calculator HTTP Streaming Demo

यह प्रोजेक्ट Server-Sent Events (SSE) का उपयोग करके HTTP स्ट्रीमिंग को Spring Boot WebFlux के साथ प्रदर्शित करता है। इसमें दो एप्लिकेशन शामिल हैं:

- **Calculator Server**: एक रिएक्टिव वेब सेवा जो कैलकुलेशन करती है और SSE के माध्यम से परिणाम स्ट्रीम करती है
- **Calculator Client**: एक क्लाइंट एप्लिकेशन जो स्ट्रीमिंग एंडपॉइंट का उपयोग करता है

## Prerequisites

- Java 17 या उससे ऊपर
- Maven 3.6 या उससे ऊपर

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

## यह कैसे काम करता है

1. **Calculator Server** एक `/calculate` एंडपॉइंट प्रदान करता है जो:
   - क्वेरी पैरामीटर स्वीकार करता है: `a` (संख्या), `b` (संख्या), `op` (ऑपरेशन)
   - समर्थित ऑपरेशन: `add`, `sub`, `mul`, `div`
   - कैलकुलेशन प्रगति और परिणाम के साथ Server-Sent Events लौटाता है

2. **Calculator Client** सर्वर से कनेक्ट होता है और:
   - `7 * 5` कैलकुलेशन के लिए अनुरोध करता है
   - स्ट्रीमिंग प्रतिक्रिया को उपयोग करता है
   - प्रत्येक इवेंट को कंसोल पर प्रिंट करता है

## एप्लिकेशन चलाना

### विकल्प 1: Maven का उपयोग करना (सिफारिश की गई)

#### 1. Calculator Server शुरू करें

टर्मिनल खोलें और सर्वर डायरेक्टरी में जाएं:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

सर्वर `http://localhost:8080` पर शुरू होगा

आपको इस तरह का आउटपुट दिखेगा:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client चलाएं

एक **नया टर्मिनल** खोलें और क्लाइंट डायरेक्टरी में जाएं:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

क्लाइंट सर्वर से कनेक्ट होगा, कैलकुलेशन करेगा, और स्ट्रीमिंग परिणाम दिखाएगा।

### विकल्प 2: सीधे Java का उपयोग करना

#### 1. सर्वर को कंपाइल और चलाएं:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. क्लाइंट को कंपाइल और चलाएं:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## सर्वर को मैन्युअली टेस्ट करना

आप वेब ब्राउज़र या curl का उपयोग करके भी सर्वर का परीक्षण कर सकते हैं:

### वेब ब्राउज़र का उपयोग करते हुए:
यहाँ जाएं: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl का उपयोग करते हुए:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## अपेक्षित आउटपुट

जब क्लाइंट चलाएं, तो आपको इस तरह का स्ट्रीमिंग आउटपुट दिखेगा:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## समर्थित ऑपरेशन

- `add` - जोड़ (a + b)
- `sub` - घटाव (a - b)
- `mul` - गुणा (a * b)
- `div` - भाग (a / b, यदि b = 0 तो NaN लौटाता है)

## API संदर्भ

### GET /calculate

**पैरामीटर:**
- `a` (आवश्यक): पहला नंबर (double)
- `b` (आवश्यक): दूसरा नंबर (double)
- `op` (आवश्यक): ऑपरेशन (`add`, `sub`, `mul`, `div`)

**प्रतिक्रिया:**
- Content-Type: `text/event-stream`
- कैलकुलेशन प्रगति और परिणाम के साथ Server-Sent Events लौटाता है

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

## समस्या निवारण

### सामान्य समस्याएं

1. **पोर्ट 8080 पहले से उपयोग में है**
   - पोर्ट 8080 का उपयोग कर रहे अन्य एप्लिकेशन बंद करें
   - या `calculator-server/src/main/resources/application.yml` में सर्वर पोर्ट बदलें

2. **कनेक्शन अस्वीकृत**
   - क्लाइंट शुरू करने से पहले सुनिश्चित करें कि सर्वर चल रहा है
   - जांचें कि सर्वर सफलतापूर्वक पोर्ट 8080 पर शुरू हुआ है

3. **पैरामीटर नाम की समस्याएं**
   - इस प्रोजेक्ट में Maven कंपाइलर कॉन्फ़िगरेशन `-parameters` फ्लैग के साथ शामिल है
   - यदि पैरामीटर बाइंडिंग में समस्या हो, तो सुनिश्चित करें कि प्रोजेक्ट इस कॉन्फ़िगरेशन के साथ बनाया गया है

### एप्लिकेशन बंद करना

- उस टर्मिनल में `Ctrl+C` दबाएं जहाँ एप्लिकेशन चल रहा हो
- या यदि बैकग्राउंड प्रक्रिया के रूप में चल रहा हो तो `mvn spring-boot:stop` का उपयोग करें

## तकनीकी स्टैक

- **Spring Boot 3.3.1** - एप्लिकेशन फ्रेमवर्क
- **Spring WebFlux** - रिएक्टिव वेब फ्रेमवर्क
- **Project Reactor** - रिएक्टिव स्ट्रीम लाइब्रेरी
- **Netty** - नॉन-ब्लॉकिंग I/O सर्वर
- **Maven** - बिल्ड टूल
- **Java 17+** - प्रोग्रामिंग भाषा

## अगले कदम

कोड में बदलाव करके प्रयास करें:
- और अधिक गणितीय ऑपरेशन जोड़ें
- अमान्य ऑपरेशनों के लिए त्रुटि हैंडलिंग शामिल करें
- अनुरोध/प्रतिक्रिया लॉगिंग जोड़ें
- प्रमाणीकरण लागू करें
- यूनिट टेस्ट जोड़ें

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
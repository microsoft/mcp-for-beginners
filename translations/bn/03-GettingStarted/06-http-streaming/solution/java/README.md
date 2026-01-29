# Calculator HTTP Streaming Demo

এই প্রকল্পটি Server-Sent Events (SSE) ব্যবহার করে HTTP স্ট্রিমিং প্রদর্শন করে Spring Boot WebFlux এর মাধ্যমে। এটি দুটি অ্যাপ্লিকেশন নিয়ে গঠিত:

- **Calculator Server**: একটি রিয়েক্টিভ ওয়েব সার্ভিস যা গণনা করে এবং SSE ব্যবহার করে ফলাফল স্ট্রিম করে
- **Calculator Client**: একটি ক্লায়েন্ট অ্যাপ্লিকেশন যা স্ট্রিমিং এন্ডপয়েন্ট ব্যবহার করে

## Prerequisites

- Java 17 বা তার উপরে
- Maven 3.6 বা তার উপরে

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

1. **Calculator Server** একটি `/calculate` এন্ডপয়েন্ট প্রদান করে যা:
   - কোয়েরি প্যারামিটার গ্রহণ করে: `a` (সংখ্যা), `b` (সংখ্যা), `op` (অপারেশন)
   - সমর্থিত অপারেশন: `add`, `sub`, `mul`, `div`
   - Server-Sent Events হিসেবে গণনার অগ্রগতি এবং ফলাফল রিটার্ন করে

2. **Calculator Client** সার্ভারের সাথে সংযোগ করে এবং:
   - `7 * 5` গণনার জন্য রিকোয়েস্ট পাঠায়
   - স্ট্রিমিং রেসপন্স গ্রহণ করে
   - প্রতিটি ইভেন্ট কনসোলে প্রিন্ট করে

## Running the Applications

### Option 1: Using Maven (Recommended)

#### 1. Start the Calculator Server

একটি টার্মিনাল খুলুন এবং সার্ভার ডিরেক্টরিতে যান:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

সার্ভার শুরু হবে `http://localhost:8080` এ

আপনি এরকম আউটপুট দেখতে পাবেন:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Run the Calculator Client

একটি **নতুন টার্মিনাল** খুলুন এবং ক্লায়েন্ট ডিরেক্টরিতে যান:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

ক্লায়েন্ট সার্ভারের সাথে সংযোগ করবে, গণনা সম্পন্ন করবে এবং স্ট্রিমিং ফলাফল দেখাবে।

### Option 2: Using Java directly

#### 1. সার্ভার কম্পাইল এবং রান করুন:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. ক্লায়েন্ট কম্পাইল এবং রান করুন:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testing the Server Manually

আপনি ব্রাউজার বা curl ব্যবহার করেও সার্ভার পরীক্ষা করতে পারেন:

### Using a web browser:
ভিজিট করুন: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Using curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Expected Output

ক্লায়েন্ট চালানোর সময়, আপনি স্ট্রিমিং আউটপুট দেখতে পাবেন যা এরকম হবে:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Supported Operations

- `add` - যোগ (a + b)
- `sub` - বিয়োগ (a - b)
- `mul` - গুণ (a * b)
- `div` - ভাগ (a / b, b = 0 হলে NaN রিটার্ন করে)

## API Reference

### GET /calculate

**Parameters:**
- `a` (প্রয়োজনীয়): প্রথম সংখ্যা (double)
- `b` (প্রয়োজনীয়): দ্বিতীয় সংখ্যা (double)
- `op` (প্রয়োজনীয়): অপারেশন (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- Server-Sent Events হিসেবে গণনার অগ্রগতি এবং ফলাফল রিটার্ন করে

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

1. **Port 8080 ইতিমধ্যেই ব্যবহৃত হচ্ছে**
   - পোর্ট 8080 ব্যবহার করছে এমন অন্য অ্যাপ্লিকেশন বন্ধ করুন
   - অথবা `calculator-server/src/main/resources/application.yml` এ সার্ভার পোর্ট পরিবর্তন করুন

2. **Connection refused**
   - ক্লায়েন্ট চালানোর আগে সার্ভার চালু আছে কিনা নিশ্চিত করুন
   - সার্ভার সফলভাবে পোর্ট 8080 এ শুরু হয়েছে কিনা চেক করুন

3. **Parameter name issues**
   - এই প্রকল্পে Maven কম্পাইলার কনফিগারেশনে `-parameters` ফ্ল্যাগ ব্যবহার করা হয়েছে
   - যদি প্যারামিটার বাইনডিং সমস্যা হয়, নিশ্চিত করুন প্রকল্পটি এই কনফিগারেশন দিয়ে বিল্ড করা হয়েছে

### Stopping the Applications

- প্রতিটি অ্যাপ্লিকেশন চালু থাকা টার্মিনালে `Ctrl+C` চাপুন
- অথবা ব্যাকগ্রাউন্ড প্রসেস হিসেবে চালালে `mvn spring-boot:stop` ব্যবহার করুন

## Technology Stack

- **Spring Boot 3.3.1** - অ্যাপ্লিকেশন ফ্রেমওয়ার্ক
- **Spring WebFlux** - রিয়েক্টিভ ওয়েব ফ্রেমওয়ার্ক
- **Project Reactor** - রিয়েক্টিভ স্ট্রিম লাইব্রেরি
- **Netty** - নন-ব্লকিং I/O সার্ভার
- **Maven** - বিল্ড টুল
- **Java 17+** - প্রোগ্রামিং ভাষা

## Next Steps

কোড পরিবর্তন করে চেষ্টা করুন:
- আরও গাণিতিক অপারেশন যোগ করা
- অবৈধ অপারেশনের জন্য এরর হ্যান্ডলিং অন্তর্ভুক্ত করা
- রিকোয়েস্ট/রেসপন্স লগিং যোগ করা
- অথেনটিকেশন ইমপ্লিমেন্ট করা
- ইউনিট টেস্ট যোগ করা

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
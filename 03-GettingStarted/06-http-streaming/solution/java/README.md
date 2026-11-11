# Calculator HTTP Streaming Demo

This project demonstrates HTTP streaming using Server-Sent Events (SSE) with Spring Boot WebFlux. It consists of two applications:

- **Calculator Server**: A reactive web service that performs calculations and streams results using SSE
- **Calculator Client**: A client application that consumes the streaming endpoint

## Prerequisites

- Java 21 or higher
- Maven 3.6.3 or higher, installed and on your `PATH` (this sample has no Maven wrapper), for example `brew install maven` on macOS

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

1. The **Calculator Server** exposes a `/calculate` endpoint that:
   - Accepts query parameters: `a` (number), `b` (number), `op` (operation)
   - Supported operations: `add`, `sub`, `mul`, `div`
   - Returns Server-Sent Events with calculation progress and result

2. The **Calculator Client** connects to the server and:
   - Makes a request to calculate `7 * 5`
   - Consumes the streaming response
   - Prints each event to the console

## Running the Applications

### Option 1: Using Maven (Recommended)

#### 1. Start the Calculator Server

Open a terminal and navigate to the server directory:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

The server will start on `http://localhost:8080`

You should see output like:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Run the Calculator Client

Open a **new terminal** and navigate to the client directory:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

The client will connect to the server, perform the calculation, and display the streaming results.

### Option 2: Using Java directly

#### 1. Compile and run the server:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compile and run the client:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testing the Server Manually

You can also test the server using a web browser or curl:

### Using a web browser:
Visit: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Using curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Expected Output

When running the client, it prints the data of each event as it arrives, after the Spring Boot startup log:

```text
Calculating: 7.0 mul 5.0
35.0
```

On macOS you may also see an `ERROR` log line saying that Netty cannot load `MacOSDnsServerAddressStreamProvider`; it falls back to the default DNS resolver and the client still works.

The raw stream, as returned by the `curl` command above, looks like this:

```text
event:info
data:Calculating: 10.0 add 5.0

event:result
data:15.0
```

## Supported Operations

- `add` - Addition (a + b)
- `sub` - Subtraction (a - b)
- `mul` - Multiplication (a * b)
- `div` - Division (a / b, returns NaN if b = 0)

## API Reference

### GET /calculate

**Parameters:**
- `a` (required): First number (double)
- `b` (required): Second number (double)
- `op` (required): Operation (`add`, `sub`, `mul`, `div`)

**Response:**
- Content-Type: `text/event-stream`
- Returns Server-Sent Events with calculation progress and result

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

1. **Port 8080 already in use**
   - Stop any other applications using port 8080
   - Or change the server port in `calculator-server/src/main/resources/application.yml`

2. **Connection refused**
   - Make sure the server is running before starting the client
   - Check that the server started successfully on port 8080

3. **Parameter name issues**
   - This project includes Maven compiler configuration with `-parameters` flag
   - If you encounter parameter binding issues, ensure the project is built with this configuration

### Stopping the Applications

- Press `Ctrl+C` in the terminal where each application is running
- Or use `mvn spring-boot:stop` if running as a background process

## Technology Stack

- **Spring Boot 4.1.2** - Application framework
- **Spring WebFlux** - Reactive web framework
- **Project Reactor** - Reactive streams library
- **Netty** - Non-blocking I/O server
- **Maven** - Build tool
- **Java 21+** - Programming language

## Next Steps

Try modifying the code to:
- Add more mathematical operations
- Include error handling for invalid operations
- Add request/response logging
- Implement authentication
- Add unit tests

# Calculator HTTP Streaming Demo

Ten projekt demonstruje strumieniowanie HTTP za pomocą Server-Sent Events (SSE) w Spring Boot WebFlux. Składa się z dwóch aplikacji:

- **Calculator Server**: reaktywna usługa webowa wykonująca obliczenia i przesyłająca wyniki za pomocą SSE
- **Calculator Client**: aplikacja kliencka konsumująca endpoint strumieniowy

## Wymagania wstępne

- Java 17 lub nowsza
- Maven 3.6 lub nowszy

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

## Jak to działa

1. **Calculator Server** udostępnia endpoint `/calculate`, który:
   - Przyjmuje parametry zapytania: `a` (liczba), `b` (liczba), `op` (operacja)
   - Obsługiwane operacje: `add`, `sub`, `mul`, `div`
   - Zwraca Server-Sent Events z postępem obliczeń i wynikiem

2. **Calculator Client** łączy się z serwerem i:
   - Wysyła zapytanie o obliczenie `7 * 5`
   - Odbiera odpowiedź strumieniową
   - Wyświetla każde zdarzenie w konsoli

## Uruchamianie aplikacji

### Opcja 1: Użycie Mavena (zalecane)

#### 1. Uruchom Calculator Server

Otwórz terminal i przejdź do katalogu serwera:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Serwer uruchomi się pod adresem `http://localhost:8080`

Powinieneś zobaczyć wyjście podobne do:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Uruchom Calculator Client

Otwórz **nowy terminal** i przejdź do katalogu klienta:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Klient połączy się z serwerem, wykona obliczenie i wyświetli wyniki strumieniowe.

### Opcja 2: Uruchomienie bezpośrednio z Javy

#### 1. Skompiluj i uruchom serwer:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Skompiluj i uruchom klienta:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Ręczne testowanie serwera

Możesz także przetestować serwer za pomocą przeglądarki lub curl:

### Za pomocą przeglądarki:
Odwiedź: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Za pomocą curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Oczekiwany wynik

Podczas uruchamiania klienta powinieneś zobaczyć strumieniowe wyjście podobne do:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Obsługiwane operacje

- `add` - dodawanie (a + b)
- `sub` - odejmowanie (a - b)
- `mul` - mnożenie (a * b)
- `div` - dzielenie (a / b, zwraca NaN jeśli b = 0)

## Dokumentacja API

### GET /calculate

**Parametry:**
- `a` (wymagany): pierwsza liczba (double)
- `b` (wymagany): druga liczba (double)
- `op` (wymagany): operacja (`add`, `sub`, `mul`, `div`)

**Odpowiedź:**
- Content-Type: `text/event-stream`
- Zwraca Server-Sent Events z postępem obliczeń i wynikiem

**Przykładowe zapytanie:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Przykładowa odpowiedź:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Rozwiązywanie problemów

### Najczęstsze problemy

1. **Port 8080 jest już zajęty**
   - Zatrzymaj inne aplikacje korzystające z portu 8080
   - Lub zmień port serwera w `calculator-server/src/main/resources/application.yml`

2. **Połączenie odrzucone**
   - Upewnij się, że serwer jest uruchomiony przed startem klienta
   - Sprawdź, czy serwer poprawnie wystartował na porcie 8080

3. **Problemy z nazwami parametrów**
   - Projekt zawiera konfigurację kompilatora Maven z flagą `-parameters`
   - Jeśli masz problemy z wiązaniem parametrów, upewnij się, że projekt jest zbudowany z tą konfiguracją

### Zatrzymywanie aplikacji

- Naciśnij `Ctrl+C` w terminalu, w którym działa aplikacja
- Lub użyj `mvn spring-boot:stop`, jeśli aplikacja działa w tle

## Stos technologiczny

- **Spring Boot 3.3.1** - framework aplikacji
- **Spring WebFlux** - reaktywny framework webowy
- **Project Reactor** - biblioteka strumieni reaktywnych
- **Netty** - serwer I/O nieblokujący
- **Maven** - narzędzie do budowania
- **Java 17+** - język programowania

## Kolejne kroki

Spróbuj zmodyfikować kod, aby:
- Dodać więcej operacji matematycznych
- Uwzględnić obsługę błędów dla nieprawidłowych operacji
- Dodać logowanie zapytań i odpowiedzi
- Wdrożyć uwierzytelnianie
- Dodać testy jednostkowe

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
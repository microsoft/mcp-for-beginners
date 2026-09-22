# Demo MCP OAuth2

> [!WARNING]
> To jest lokalny przykład edukacyjny, a nie produkcyjna usługa autoryzacji.  
> Używa klienta w pamięci i generuje nowy klucz podpisujący podczas startu. Nigdy  
> nie wdrażaj go z współdzielonym, domyślnym lub wersjonowanym w repozytorium kluczem klienta.

## Wprowadzenie

OAuth2 to standardowy w branży protokół autoryzacji, umożliwiający bezpieczny dostęp do zasobów bez udostępniania poświadczeń. W implementacjach MCP (Model Context Protocol) OAuth2 zapewnia solidny sposób uwierzytelniania i autoryzacji klientów (takich jak agenci AI) do dostępu do serwerów MCP i ich narzędzi.

Ta lekcja demonstruje jak wdrożyć uwierzytelnianie OAuth2 dla serwerów MCP z użyciem Spring Boot, co jest powszechnym wzorcem w wdrożeniach korporacyjnych i produkcyjnych.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:
- Zrozumieć, jak OAuth2 integrować z serwerami MCP
- Wdrożyć serwer autoryzacji Spring do wystawiania tokenów
- Chronić punkty końcowe MCP za pomocą uwierzytelniania opartego na JWT
- Skonfigurować przepływ klienta w oparciu o dane uwierzytelniające do komunikacji maszynowej

## Wymagania wstępne

- Podstawowa znajomość Javy i Spring Boot
- Znajomość pojęć MCP z wcześniejszych modułów
- Zainstalowany Maven lub Gradle

---

## Omówienie projektu

Ten projekt to **minimalna aplikacja Spring Boot**, która działa zarówno jako:

* **serwer autoryzacji Spring** (wystawiający tokeny dostępu JWT via `client_credentials`), oraz  
* **serwer zasobów** (chroniący własny punkt końcowy `/hello`).

To odzwierciedla konfigurację pokazaną w [wpisie na blogu Spring (2 kwietnia 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Szybki start (lokalnie)

```bash
# Użyj unikalnej lokalnej wartości i trzymaj ją poza historią powłoki, jeśli to możliwe.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# uzyskaj token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# wywołaj chroniony punkt końcowy
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testowanie konfiguracji OAuth2

Możesz przetestować konfigurację zabezpieczeń OAuth2 wykonując następujące kroki:

### 1. Sprawdź, czy serwer działa i jest zabezpieczony

```bash
# To powinno zwrócić 401 Unauthorized, potwierdzając, że bezpieczeństwo OAuth2 jest aktywne
curl -v http://localhost:8081/
```

### 2. Uzyskaj token dostępu używając danych uwierzytelniających klienta

```bash
# Pobierz i wyodrębnij pełną odpowiedź tokena
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Lub wyodrębnij tylko token (wymaga jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

W PowerShell ustaw lokalny sekret przed uruchomieniem Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Uzyskaj dostęp do chronionego punktu końcowego z użyciem tokenu

```bash
# Używanie zapisanego tokena
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Lub bezpośrednio z wartością tokena
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Pomyślna odpowiedź z "Hello from MCP OAuth2 Demo!" potwierdza, że konfiguracja OAuth2 działa poprawnie.

---

## Budowanie kontenera

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Bezpieczeństwo produkcyjne

Dla wdrożenia produkcyjnego użyj dedykowanego dostawcy tożsamości zamiast
tego wbudowanego demo serwera autoryzacji. Przechowuj dane uwierzytelniające w zarządzanym
sklepie sekretów, rotuj je, stosuj trwałe klucze podpisujące, ogranicz zakresy oraz
ustaw wyraźnego wystawcę (issuer). Nigdy nie umieszczaj sekretu klienta w kodzie źródłowym,
obrazach kontenerów, manifestach wdrożeniowych ani w outputach poleceń.

Dla Azure Container Apps przechowuj wartość jako sekret Container Apps zabezpieczony przez
Key Vault, a następnie udostępniaj tylko referencję sekretu przez zmienną środowiskową
`OAUTH_CLIENT_SECRET`.

---

## Wdróż do **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Adres FQDN punktu wejścia staje się twoim **issuer** (`https://<fqdn>`).  
Azure automatycznie dostarcza zaufany certyfikat TLS dla `*.azurecontainerapps.io`.

---

## Podłącz do **Azure API Management**

Dodaj tę politykę przychodzącą do swojego API:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM pobierze JWKS i zweryfikuje każde żądanie.

---

## Co dalej

- [5.4 Konteksty root](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
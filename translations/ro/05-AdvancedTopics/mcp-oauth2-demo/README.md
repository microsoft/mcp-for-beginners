# Demo MCP OAuth2

> [!WARNING]
> Acesta este un exemplu local de învățare, nu un serviciu de autorizare pentru producție. El
> folosește un client în memorie și generează o nouă cheie de semnare la pornire. Nu
> îl distribuiți niciodată cu un secret de client partajat, implicit sau controlat prin sursă.

## Introducere

OAuth2 este protocolul standard din industrie pentru autorizare, permițând acces securizat la resurse fără a partaja acreditările. În implementările MCP (Model Context Protocol), OAuth2 oferă o modalitate robustă de a autentifica și autoriza clienții (cum ar fi agenții AI) să acceseze serverele MCP și uneltele lor.

Această lecție demonstrează cum să implementați autentificarea OAuth2 pentru serverele MCP folosind Spring Boot, un model comun pentru implementări enterprise și de producție.

## Obiective de învățare

La finalul acestei lecții, vei:
- Înțelege cum se integrează OAuth2 cu serverele MCP
- Implementa un Server de Autorizare Spring pentru emiterea token-urilor
- Proteja endpoint-urile MCP prin autentificare bazată pe JWT
- Configura flow-ul client credentials pentru comunicare între mașini

## Cerințe preliminare

- Înțelegere de bază a Java și Spring Boot
- Familiaritate cu conceptele MCP din modulele anterioare
- Maven sau Gradle instalat

---

## Prezentarea proiectului

Acest proiect este o **aplicație minimală Spring Boot** care acționează ca:

* un **Spring Authorization Server** (emitând token-uri de acces JWT prin flow-ul `client_credentials`), și  
* un **Resource Server** (protejând propriul endpoint `/hello`).

Reflectă configurația prezentată în [postarea de blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Pornire rapidă (local)

```bash
# Folosiți o valoare locală unică și păstrați-o în afara istoricului shell-ului unde este posibil.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obțineți un token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# apelați punctul final protejat
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testarea Configurației OAuth2

Poți testa configurația de securitate OAuth2 urmând pașii de mai jos:

### 1. Verifică dacă serverul rulează și este securizat

```bash
# Aceasta ar trebui să returneze 401 Neautorizat, confirmând că securitatea OAuth2 este activă
curl -v http://localhost:8081/
```

### 2. Obține un token de acces folosind client credentials

```bash
# Obțineți și extrageți răspunsul complet al tokenului
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Sau pentru a extrage doar tokenul (necesită jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Pe PowerShell, setează secretul local înainte de a rula Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Accesează endpoint-ul protejat folosind token-ul

```bash
# Folosind tokenul salvat
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Sau direct cu valoarea tokenului
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Un răspuns de succes cu „Hello from MCP OAuth2 Demo!” confirmă că configurația OAuth2 funcționează corect.

---

## Construirea containerului

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Securitate pentru producție

Pentru un mediu de producție, folosește un furnizor de identitate dedicat în locul
acestui server de autorizare demo în proces. Stochează acreditările într-un depozit
securizat gestionat, rotește-le, folosește chei persistente pentru semnare, restricționează domeniile de acces,
și setează un emițător explicit. Nu introduce niciodată un secret de client în codul sursă,
imaginile containerelor, manifestele de implementare sau output-ul comenzilor.

Pentru Azure Container Apps, stochează valoarea ca un secret în Container Apps susținut de
Key Vault unde este posibil, apoi expune doar o referință de secret prin
variabila de mediu `OAUTH_CLIENT_SECRET`.

---

## Implementare în **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Numele complet calitativ FQDN de acces devine **emițătorul** tău (`https://<fqdn>`).  
Azure furnizează automat un certificat TLS de încredere pentru `*.azurecontainerapps.io`.

---

## Integrare în **Azure API Management**

Adaugă această politică de intrare în API-ul tău:

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

APIM va prelua JWKS și va valida fiecare cerere.

---

## Ce urmează

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
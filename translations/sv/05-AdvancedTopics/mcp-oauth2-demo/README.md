# MCP OAuth2 Demo

> [!WARNING]
> Detta är ett lokalt inlärningsexempel, inte en produktionsauktoriseringstjänst. Den
> använder en klient i minnet och genererar en ny signeringsnyckel vid start. Använd aldrig
> den med en delad, standard eller versionshanterad klienthemlighet.

## Introduktion

OAuth2 är industristandardprotokollet för auktorisering, som möjliggör säker åtkomst till resurser utan att dela inloggningsuppgifter. I MCP (Model Context Protocol) implementationer erbjuder OAuth2 ett robust sätt att autentisera och auktorisera klienter (som AI-agenter) att få åtkomst till MCP-servrar och deras verktyg.

Denna lektion visar hur man implementerar OAuth2-autentisering för MCP-servrar med Spring Boot, ett vanligt mönster för företags- och produktionsdistributioner.

## Mål för lärandet

I slutet av denna lektion kommer du att:
- Förstå hur OAuth2 integreras med MCP-servrar
- Implementera en Spring Authorization Server för tokenutfärdande
- Skydda MCP-endpoints med JWT-baserad autentisering
- Konfigurera klientuppgiftsflöde för maskin-till-maskin-kommunikation

## Förkunskaper

- Grundläggande kunskap om Java och Spring Boot
- Bekantskap med MCP-koncept från tidigare moduler
- Maven eller Gradle installerade

---

## Projektöversikt

Detta projekt är en **minimal Spring Boot-applikation** som fungerar både som:

* en **Spring Authorization Server** (utfärdar JWT-access tokens via `client_credentials`-flödet), samt  
* en **Resource Server** (skyddar sin egen `/hello`-endpoint).

Den speglar inställningen som visas i [Spring-blogginlägget (2 apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Kom igång snabbt (lokalt)

```bash
# Använd ett unikt lokalt värde och håll det utanför shellhistoriken när det är möjligt.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# hämta en token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# anropa den skyddade slutpunkten
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testa OAuth2-konfigurationen

Du kan testa OAuth2-säkerhetskonfigurationen med följande steg:

### 1. Verifiera att servern körs och är säkrad

```bash
# Detta bör returnera 401 Unauthorized, vilket bekräftar att OAuth2-säkerhet är aktiv
curl -v http://localhost:8081/
```

### 2. Skaffa en access-token med klientuppgifter

```bash
# Hämta och extrahera hela token-svaret
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Eller för att extrahera bara token (kräver jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

I PowerShell, ställ in den lokala hemligheten innan du kör Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Använd token för att komma åt den skyddade endpointen

```bash
# Använder den sparade token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Eller direkt med tokenvärdet
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Ett lyckat svar med "Hello from MCP OAuth2 Demo!" bekräftar att OAuth2-konfigurationen fungerar korrekt.

---

## Containerbuild

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Produktionssäkerhet

För en produktionsdistribution, använd en dedikerad identitetsleverantör istället för
denna demoauktoriseringsserver i processen. Spara uppgifter i en hanterad
hemlighetshanterare, rotera dem, använd persistenta signeringsnycklar, begränsa scopes, och
ange en uttrycklig issuer. Placera aldrig en klienthemlighet i källkod, container-
bilder, deployment-mallar eller kommandoutdata.

För Azure Container Apps, spara värdet som en Container Apps-hemlighet backad av
Key Vault där det är möjligt, och exponera sedan endast en hemlighetsreferens via
`OAUTH_CLIENT_SECRET` miljövariabeln.

---

## Distribuera till **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN blir din **issuer** (`https://<fqdn>`).  
Azure tillhandahåller automatiskt ett betrott TLS-certifikat för `*.azurecontainerapps.io`.

---

## Koppla till **Azure API Management**

Lägg till denna inbound-policy till din API:

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

APIM hämtar JWKS och validerar varje begäran.

---

## Vad blir nästa steg

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
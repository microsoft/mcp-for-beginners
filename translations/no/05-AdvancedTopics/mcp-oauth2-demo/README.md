# MCP OAuth2 Demo

> [!WARNING]
> Dette er et lokalt læringseksempel, ikke en produksjonsautorisasjonstjeneste. Den
> bruker en klient i minnet og genererer en ny signeringsnøkkel ved oppstart. Aldri
> distribuer det med en delt, standard eller kildekontrollert klienthemmelighet.

## Introduksjon

OAuth2 er industristandardprotokollen for autorisasjon, som muliggjør sikker tilgang til ressurser uten å dele legitimasjon. I MCP (Model Context Protocol)-implementeringer gir OAuth2 en robust måte å autentisere og autorisere klienter (som AI-agenter) til å få tilgang til MCP-servere og deres verktøy.

Denne leksjonen viser hvordan man implementerer OAuth2-autentisering for MCP-servere ved bruk av Spring Boot, et vanlig mønster for bedrifts- og produksjonsdistribusjoner.

## Læringsmål

Innen slutten av denne leksjonen vil du:
- Forstå hvordan OAuth2 integreres med MCP-servere
- Implementere en Spring Authorization Server for utstedelse av token
- Beskytte MCP-endepunkter med JWT-basert autentisering
- Konfigurere klientlegitimasjonsflyt for maskin-til-maskin-kommunikasjon

## Forutsetninger

- Grunnleggende forståelse av Java og Spring Boot
- Kjennskap til MCP-konsepter fra tidligere moduler
- Maven eller Gradle installert

---

## Prosjektoversikt

Dette prosjektet er en **minimal Spring Boot-applikasjon** som fungerer som både:

* en **Spring Authorization Server** (utsteder JWT-tilgangstoken via `client_credentials`-flyten), og  
* en **Resource Server** (beskytter sitt eget `/hello` endepunkt).

Den speiler oppsettet vist i [Spring blogginnlegget (2. apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Rask start (lokalt)

```bash
# Bruk en unik lokal verdi og hold den ute av shell-historikken der det er mulig.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# skaffe en token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# kall det beskyttede endepunktet
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testing av OAuth2-konfigurasjonen

Du kan teste OAuth2 sikkerhetskonfigurasjonen med følgende trinn:

### 1. Bekreft at serveren kjører og er sikret

```bash
# Dette skal returnere 401 Unauthorized, som bekrefter at OAuth2-sikkerhet er aktiv
curl -v http://localhost:8081/
```

### 2. Skaff et tilgangstoken ved å bruke klientlegitimasjon

```bash
# Hent og hent ut hele tokenresponsen
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Eller for å hente ut bare tokenet (krever jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

På PowerShell, sett den lokale hemmeligheten før du kjører Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Få tilgang til det beskyttede endepunktet ved bruk av tokenet

```bash
# Bruke den lagrede tokenen
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Eller direkte med tokenverdien
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Et vellykket svar med "Hello from MCP OAuth2 Demo!" bekrefter at OAuth2-konfigurasjonen fungerer korrekt.

---

## Containerbygging

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Produksjonssikkerhet

For en produksjonsdistribusjon, bruk en dedikert identitetsleverandør i stedet for
denne in-prosess demo autorisasjonsserveren. Lagre legitimasjon i en administrert
hemmelig butikk, roter dem, bruk persistente signeringsnøkler, begrens scopes, og
sett en eksplisitt utsteder. Ikke plasser noensinne en klienthemmelighet i kildekode, container
bilder, distribusjonsmanifest eller kommandoutgang.

For Azure Container Apps, lagre verdien som en Container Apps-hemmelighet støttet av
Key Vault der det er mulig, og eksponer deretter bare en hemmelighetsreferanse gjennom
`OAUTH_CLIENT_SECRET` miljøvariabel.

---

## Distribuer til **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Inngangsadressen FQDN blir din **utsteder** (`https://<fqdn>`).  
Azure leverer et betrodd TLS-sertifikat automatisk for `*.azurecontainerapps.io`.

---

## Koble til **Azure API Management**

Legg til denne innkommende policyen til din API:

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

APIM vil hente JWKS og validere hver forespørsel.

---

## Hva er det neste

- [5.4 Rotkontekster](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
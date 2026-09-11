# MCP OAuth2 Demo

> [!WARNING]
> Dette er et lokalt læringseksempel, ikke en produktionsautorisationstjeneste. Det
> bruger en in-memory klient og genererer en ny signeringsnøgle ved opstart. Aldrig
> deploy med en delt, standard eller kildekontroleret klienthemmelighed.

## Introduktion

OAuth2 er industristandarden for autorisation, som muliggør sikker adgang til ressourcer uden at dele legitimationsoplysninger. I MCP (Model Context Protocol) implementeringer giver OAuth2 en robust måde at autentificere og autorisere klienter (som AI-agenter) til at få adgang til MCP-servere og deres værktøjer.

Denne lektion demonstrerer, hvordan man implementerer OAuth2-autentifikation for MCP-servere med Spring Boot, et almindeligt mønster for virksomhed og produktion.

## Læringsmål

Ved slutningen af denne lektion vil du:
- Forstå hvordan OAuth2 integreres med MCP-servere
- Implementere en Spring Authorization Server til udstedelse af tokens
- Beskytte MCP-endpoints med JWT-baseret autentifikation
- Konfigurere client credentials flow til maskin-til-maskine kommunikation

## Forudsætninger

- Grundlæggende kendskab til Java og Spring Boot
- Fortrolighed med MCP-konceptet fra tidligere moduler
- Maven eller Gradle installeret

---

## Projektoversigt

Dette projekt er en **minimal Spring Boot applikation** der fungerer som både:

* en **Spring Authorization Server** (udsteder JWT adgangstokens via `client_credentials` flow), og  
* en **Resource Server** (beskytter sin egen `/hello` endpoint).

Det spejler opsætningen vist i [Spring blogindlægget (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Hurtigstart (lokalt)

```bash
# Brug en unik lokal værdi og hold den ude af shell-historikken, hvor det er muligt.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# hent en token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# kald den beskyttede slutpunkt
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Test af OAuth2 konfigurationen

Du kan teste OAuth2 sikkerhedskonfigurationen med følgende trin:

### 1. Bekræft at serveren kører og er sikret

```bash
# Dette burde returnere 401 Unauthorized, hvilket bekræfter at OAuth2-sikkerhed er aktiv
curl -v http://localhost:8081/
```

### 2. Få et adgangstoken ved brug af client credentials

```bash
# Hent og udtræk det fulde token-svar
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Eller for kun at udtrække tokenet (kræver jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

På PowerShell, sæt den lokale hemmelighed før du kører Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Få adgang til det beskyttede endpoint med tokenet

```bash
# Brug af den gemte token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Eller direkte med token værdien
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Et succesfuldt svar med "Hello from MCP OAuth2 Demo!" bekræfter at OAuth2 konfigurationen fungerer korrekt.

---

## Container build

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Produktionssikkerhed

Til produktionsudrulning, brug en dedikeret identitetsudbyder i stedet for
denne in-process demo autorisationsserver. Gem legitimationsoplysninger i en administreret
hemmelighedslager, roter dem, brug persistente signeringsnøgler, begræns scopes, og
sæt en eksplicit issuer. Placer aldrig en klienthemmelighed i kildekode, container
billeder, udrulningsmanifest eller kommandoudgang.

For Azure Container Apps, gem værdien som en Container Apps hemmelighed støttet af
Key Vault hvor muligt, og eksponer kun en hemmelighedsreference via
`OAUTH_CLIENT_SECRET` miljøvariablen.

---

## Deploy til **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN bliver din **issuer** (`https://<fqdn>`).  
Azure leverer et betroet TLS certifikat automatisk for `*.azurecontainerapps.io`.

---

## Kobl til **Azure API Management**

Tilføj denne inbound policy til din API:

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

APIM vil hente JWKS og validere hver forespørgsel.

---

## Hvad er det næste

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
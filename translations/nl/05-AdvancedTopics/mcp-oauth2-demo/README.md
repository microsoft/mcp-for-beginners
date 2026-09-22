# MCP OAuth2 Demo

> [!WARNING]
> Dit is een lokaal leersample, geen productierechtenservice. Het
> gebruikt een in-memory client en genereert een nieuwe ondertekeningssleutel bij opstarten. Plaats het nooit
> in productie met een gedeeld, standaard of brongecontroleerd clientgeheim.

## Introductie

OAuth2 is het industriestandaardprotocol voor autorisatie, waarmee beveiligde toegang tot bronnen mogelijk wordt zonder het delen van inloggegevens. In MCP (Model Context Protocol) implementaties biedt OAuth2 een robuuste manier om clients (zoals AI-agenten) te authenticeren en autoriseren voor toegang tot MCP-servers en hun tools.

Deze les toont hoe je OAuth2-authenticatie implementeert voor MCP-servers met Spring Boot, een veelgebruikt patroon voor enterprise- en productiedeplyments.

## Leerdoelen

Aan het einde van deze les zal je:
- Begrijpen hoe OAuth2 integreert met MCP-servers
- Een Spring Authorization Server implementeren voor tokenuitgifte
- MCP-eindpunten beveiligen met JWT-gebaseerde authenticatie
- Client credentials flow configureren voor machine-naar-machine communicatie

## Vereisten

- Basiskennis van Java en Spring Boot
- Bekendheid met MCP-concepten uit eerdere modules
- Maven of Gradle geïnstalleerd

---

## Projectoverzicht

Dit project is een **minimale Spring Boot applicatie** die zowel optreedt als:

* een **Spring Authorization Server** (uitgifte van JWT-access tokens via de `client_credentials` flow), en  
* een **Resource Server** (bescherming van zijn eigen `/hello` eindpunt).

Het weerspiegelt de opzet getoond in de [Spring blogpost (2 apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Snelle start (lokaal)

```bash
# Gebruik een unieke lokale waarde en houd deze zoveel mogelijk uit de shellgeschiedenis.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# verkrijg een token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# roep het beveiligde eindpunt aan
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testen van de OAuth2-configuratie

Je kan de OAuth2-beveiligingsconfiguratie testen met de volgende stappen:

### 1. Controleer of de server draait en beveiligd is

```bash
# Dit zou 401 Niet Geautoriseerd moeten retourneren, wat bevestigt dat OAuth2-beveiliging actief is
curl -v http://localhost:8081/
```

### 2. Verkrijg een toegangstoken met clientcredentials

```bash
# Haal de volledige tokenrespons op en extraheer deze
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Of om alleen het token te extraheren (vereist jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Zet in PowerShell het lokale geheim voordat je Maven uitvoert:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Toegang tot het beveiligde eindpunt met het token

```bash
# Gebruikmakend van het opgeslagen token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Of direct met de tokenwaarde
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Een succesvolle reactie met "Hello from MCP OAuth2 Demo!" bevestigt dat de OAuth2-configuratie correct werkt.

---

## Containerbuild

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Productiebeveiliging

Voor een productie-implementatie, gebruik een toegewijde identity provider in plaats van
deze in-process demo-autorisatieserver. Bewaar credentials in een beheerde
geheime opslagplaats, roteer ze, gebruik persistente ondertekeningssleutels, beperk scopes, en
stel een expliciete issuer in. Plaats nooit een clientgeheim in broncode, container
images, deployment-manifesten of command output.

Voor Azure Container Apps, sla de waarde op als een Container Apps secret ondersteund door
Key Vault waar mogelijk, en geef vervolgens alleen een geheimreferentie bloot via de
`OAUTH_CLIENT_SECRET` omgeving variabele.

---

## Deployen naar **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Het ingress FQDN wordt je **issuer** (`https://<fqdn>`).  
Azure verzorgt automatisch een vertrouwd TLS-certificaat voor `*.azurecontainerapps.io`.

---

## Koppeling met **Azure API Management**

Voeg deze inbound policy toe aan je API:

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

APIM haalt de JWKS op en valideert elke aanvraag.

---

## Wat volgt

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
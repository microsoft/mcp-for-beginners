# MCP OAuth2 Demonstracija

> [!WARNING]
> Tai yra vietinis mokymosi pavyzdys, o ne gamybinė autorizavimo paslauga. Jis
> naudoja atmintyje saugomą klientą ir generuoja naują pasirašymo raktą paleidimo metu. Niekada
> neįdiekite jo su bendrinu, numatytuoju ar šaltinio valdomu kliento slaptu kodu.

## Įvadas

OAuth2 yra pramonės standartas autoritacijos protokolas, leidžiantis saugiai pasiekti išteklius nesidalinant prisijungimo duomenimis. MCP (Model Context Protocol) įgyvendinimuose OAuth2 suteikia patikimą būdą autentifikuoti ir autorizuoti klientus (pvz., AI agentus) pasiekti MCP serverius ir jų priemones.

Ši pamoka demonstruoja, kaip įgyvendinti OAuth2 autentifikaciją MCP serveriams naudojant Spring Boot, kas yra įprasta praktika verslo ir gamybos aplinkose.

## Mokymosi tikslai

Pamokos pabaigoje jūs:
- Suprasite, kaip OAuth2 integruojasi su MCP serveriais
- Įgyvendinsite Spring autorizacijos serverį žetonų išdavimui
- Apsaugosite MCP galinius taškus naudojant JWT pagrindu veikiančią autentifikaciją
- Konfigūruosite kliento kredencialų srautą mašinų tarpusavio komunikacijai

## Priešprielaidos

- Pagrindinės Java ir Spring Boot žinios
- Susipažinimas su MCP koncepcijomis iš ankstesnių modulių
- Įdiegtas Maven arba Gradle

---

## Projekto apžvalga

Šis projektas yra **minimalus Spring Boot programa**, kuri veikia kaip abu:

* **Spring autorizacijos serveris** (išduodantis JWT prieigos žetonus per `client_credentials` srautą), ir  
* **Ištekliaus serveris** (apsaugantis savo `/hello` galinį tašką).

Jis atspindi konfigūraciją, parodytą [Spring tinklaraščio įraše (2025-04-02)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Greitas paleidimas (vietinis)

```bash
# Naudokite unikalią vietinę reikšmę ir, jei įmanoma, nelaikykite jos shell istorijoje.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# gauti žetoną
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# kvieskite apsaugotą galinį tašką
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2 konfigūracijos testavimas

Galite patikrinti OAuth2 saugos konfigūraciją atlikdami šiuos veiksmus:

### 1. Patvirtinkite, kad serveris veikia ir yra apsaugotas

```bash
# Tai turėtų grąžinti 401 Unauthorized, patvirtinant, kad OAuth2 saugumas yra aktyvus
curl -v http://localhost:8081/
```

### 2. Gaukite prieigos žetoną naudodami kliento kredencialus

```bash
# Gauti ir išskleisti pilną žetonų atsakymą
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Arba išskleisti tik žetoną (reikalauja jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

PowerShell lange nustatykite vietinį slaptą kodą prieš paleisdami Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Naudokite žetoną prieigos prie apsaugoto galinio taško gavimui

```bash
# Naudojant išsaugotą žetoną
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Arba tiesiogiai su žetono verte
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Sėkmingas atsakymas su "Hello from MCP OAuth2 Demo!" patvirtina, kad OAuth2 konfigūracija veikia teisingai.

---

## Konteinerio kūrimas

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Gamybos saugumas

Gamybos diegimui naudokite specialų tapatybės tiekėją, o ne
šį vykdomą autorizavimo serverį demonstracijai. Saugojimo duomenis laikykite valdomame
slaptame sandėlyje, rotuokite juos, naudokite nuolatinį pasirašymo raktą, ribokite prieigos lygius ir
nustatykite aiškų leidėją. Niekada nepridėkite kliento slapto kodo į šaltinio kodą, konteinerių
atvaizdus, diegimo manifestus ar komandų išvestį.

Azure Container Apps atveju, slaptą reikšmę laikykite Container Apps slaptajame saugykloje, paremtoje
Key Vault, jei įmanoma, ir tada atskleiskite tik slaptos nuorodos per
`OAUTH_CLIENT_SECRET` aplinkos kintamąjį.

---

## Diegimas į **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Įeinantis FQDN tampa jūsų **leidėju** (`https://<fqdn>`).  
Azure automatiškai suteikia pasitikėjimo vertą TLS sertifikatą `*.azurecontainerapps.io`.

---

## Integracija su **Azure API Management**

Pridėkite šią įeinančią politiką prie savo API:

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

APIM parsisiųs JWKS ir patikrins kiekvieną užklausą.

---

## Kas toliau

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
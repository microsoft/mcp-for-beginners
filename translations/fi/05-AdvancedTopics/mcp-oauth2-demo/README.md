# MCP OAuth2 Demo

> [!WARNING]
> Tämä on paikallinen oppimismalli, ei tuotantoon tarkoitettu valtuutuspalvelu. Se
> käyttää muistissa olevaa asiakasta ja luo uuden allekirjoitusavaimen käynnistyksen yhteydessä. Älä koskaan
> ota käyttöön jaetun, oletus- tai lähdekoodinhallinnassa olevan asiakassalaisuuden kanssa.

## Johdanto

OAuth2 on teollisuuden standardiprotokolla valtuutukselle, joka mahdollistaa turvallisen pääsyn resursseihin ilman tunnistetietojen jakamista. MCP:n (Model Context Protocol) toteutuksissa OAuth2 tarjoaa vankan tavan todentaa ja valtuuttaa asiakkaita (kuten tekoälyagentteja) pääsemään MCP-palvelimille ja niiden työkaluihin.

Tämä oppitunti näyttää, kuinka toteuttaa OAuth2-todennus MCP-palvelimille käyttäen Spring Bootia, joka on yleinen malli yritys- ja tuotantoympäristössä.

## Oppimistavoitteet

Oppitunnin lopussa osaat:
- Ymmärtää, miten OAuth2 integroidaan MCP-palvelimiin
- Toteuttaa Spring Authorization Server tokenien myöntämiseksi
- Suojata MCP-päätepisteet JWT-pohjaisella todennuksella
- Konfiguroida client credentials -virta koneiden väliseen kommunikointiin

## Esivaatimukset

- Perustiedot Javasta ja Spring Bootista
- Tutustuminen MCP-konsepteihin aiemmista moduuleista
- Maven tai Gradle asennettuna

---

## Projektin yleiskuvaus

Tämä projekti on **minimaalinen Spring Boot -sovellus**, joka toimii sekä:

* a **Spring Authorization Server** (myöntäen JWT-pääsytunnuksia `client_credentials`-virran kautta), ja  
* a **Resurssipalvelin** (suojaamalla oman `/hello` päätepisteensä).

Se peilaa asetusta, joka on esitetty [Springin blogikirjoituksessa (2. huhtikuuta 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Nopeaan alkuun (paikallinen)

```bash
# Use a unique local value and keep it out of shell history where possible.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obtain a token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2-konfiguraation testaaminen

Voit testata OAuth2-turvakonfiguraatiota seuraavin ohjein:

### 1. Varmista, että palvelin on käynnissä ja suojattu

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hanki pääsytunnus käyttämällä asiakastunnistetta

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

PowerShellissä aseta paikallinen salaisuus ennen Mavenin suorittamista:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Käytä suojattua päätettä tunnuksella

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Onnistunut vastaus "Hello from MCP OAuth2 Demo!" vahvistaa, että OAuth2-konfiguraatio toimii oikein.

---

## Kontin rakennus

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Tuotannon turvallisuus

Tuotantokäyttöön käytä omistettua identiteetin tarjoajaa tämän prosessin sisäisen demoauktorisointipalvelimen sijaan. Tallenna tunnistetiedot hallittuun salaisuuskauppaan, kierrätä niitä, käytä pysyviä allekirjoitusavaimia, rajoita skooppeja ja määritä selkeä julkaisija. Älä koskaan laita asiakas salaista lähdekoodiin, kontin kuviin, käyttöönoton manifestiin tai komentotulosteisiin.





Azure Container Appseille tallenna arvo Container Apps -salaisuutena, jota tuetaan
Käytä mahdollisuuksien mukaan Key Vaultia, ja paljasta sitten vain salaisuuden viite
`OAUTH_CLIENT_SECRET`-ympäristömuuttujan kautta.

---

## Ota käyttöön **Azure Container Apps** -palveluun

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingressin FQDN:stä tulee sinun **julkaisijasi** (`https://<fqdn>`).  
Azure tarjoaa automaattisesti luotetun TLS-varmenteen `*.azurecontainerapps.io`:lle.

---

## Kytke **Azure API Managementiin**

Lisää tämä sisääntuleva sääntö API:hesi:

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

APIM hakee JWKS:n ja validoi jokaisen pyynnön.

---

## Mitä seuraavaksi

- [5.4 Juurikontekstit](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
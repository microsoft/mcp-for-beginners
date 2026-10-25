# MCP OAuth2 demonstratsioon

> [!WARNING]
> See on kohalik õppe näidis, mitte tootmiskeskkonna autoriseerimisteenus. See
> kasutab mälupõhist klienti ja genereerib käivitamisel uue allkirjastamisvõtme. Ärge kunagi
> juurutage seda jagatud, vaikimisi või versioonikontrollitud kliendisaladusega.

## Sissejuhatus

OAuth2 on tööstusharu standardne autoriseerimisprotokoll, mis võimaldab turvalist juurdepääsu ressurssidele ilma mandaate jagamata. MCP (Model Context Protocol) rakendustes pakub OAuth2 usaldusväärset viisi klientide (näiteks AI-agentide) autentimiseks ja autoriseerimiseks, et nad saaksid juurde pääseda MCP serveritele ja nende tööriistadele.

See õppetund demonstreerib, kuidas rakendada OAuth2 autentimist MCP serveritele, kasutades Spring Booti — tavalist mustrit ettevõtte- ja tootmiskasutuseks.

## Õpieesmärgid

Selle õppetunni lõpuks:
- Mõista, kuidas OAuth2 integreerub MCP serveritega
- Rakendada Spring Authorization Serverit tokenite väljastamiseks
- Kaitsta MCP lõpp-punkte JWT-põhise autentimisega
- Konfigureerida client credentials voog masinadevaheliseks suhtluseks

## Eeltingimused

- Põhilised teadmised Javast ja Spring Bootist
- Tuttavus MCP kontseptsioonidega varasematest moodulitest
- Maven või Gradle installitud

---

## Projekti ülevaade

See projekt on **minimaalne Spring Booti rakendus**, mis toimib mõlema rollis:

* a **Spring Authorization Server** (väljastades JWT-juurdepääsutokenid `client_credentials` voo kaudu), ja  
* a **Resource Server** (kaitstes oma `/hello` lõpp-punkti).

See peegeldab seadistust, nagu on näidatud [Springi blogipostituses (2. aprill 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Kiire alustamine (kohalik)

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

## OAuth2 konfiguratsiooni testimine

OAuth2 turvakonfiguratsiooni saate testida järgmiste sammude abil:

### 1. Kontrollige, et server töötab ja on kaitstud

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hankige juurdepääsutoken, kasutades client credentials'i

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

PowerShellis määrake kohalik salajane väärtus enne Maveni käivitamist:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Pääsege kaitstud lõpp-punktile tokeni abil

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Edukas vastus tekstiga "Tere MCP OAuth2 demonstratsioonilt!" kinnitab, et OAuth2 konfiguratsioon töötab õigesti.

---

## Konteineri ehitamine

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Tootmisalane turvalisus

Tootmisseadistuse jaoks kasutage pühendatud identiteedipakkujat, mitte
seda protsessis töötavat demo-autoriseerimisteenust. Salvestage mandaadid hallatud
saladustehoidlas, vahetage neid perioodiliselt, kasutage püsiva allkirjastamise võtmeid, piiritlege ulatusi ja
määrake selge väljastaja. Ärge kunagi paigutage kliendisaladust lähtekoodi, konteiner
piltidesse, juurutamise manifestidesse ega käsurea väljundisse.

Azure Container Apps'i puhul salvestage väärtus Container Apps salajana, mida toetab
Key Vaulti tugiteenus, kus võimalik, ja seejärel avaldage ainult salajase viite kaudu
`OAUTH_CLIENT_SECRET` keskkonnamuutuja.

---

## Juuruta **Azure Container Apps**-i

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingressi FQDNist saab teie **väljastaja** (`https://<fqdn>`).  
Azure pakub `*.azurecontainerapps.io` jaoks automaatselt usaldusväärset TLS-sertifikaati.

---

## Ühenda **Azure API Management**-iga

Lisage see sissetulev poliitika oma API-le:

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

APIM hangib JWKS-i ja valideerib iga päringu.

---

## Mis järgmiseks

- [5.4 Juurekontekstid](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
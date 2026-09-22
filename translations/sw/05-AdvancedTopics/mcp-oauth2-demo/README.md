# MCP OAuth2 Demo

> [!WARNING]
> Huu ni mfano wa kujifunza wa ndani, si huduma ya idhini kwa uzalishaji. Inatumia
> mteja wa kumbukumbu ya ndani na huunda ufunguo mpya wa kusaini wakati wa kuanza. Kamwe
> usiitumie pamoja na siri ya mteja iliyoshirikiwa, ya chaguo-msingi, au inayodhibitiwa na chanzo.

## Utangulizi

OAuth2 ni itifaki ya kiwango cha tasnia kwa idhini, ikiruhusu ufikiaji salama wa rasilimali bila kushiriki vyeti. Katika utekelezaji wa MCP (Model Context Protocol), OAuth2 hutoa njia thabiti za kuthibitisha na kutoa idhini kwa wateja (kama wakala wa AI) kufikia seva za MCP na zana zao.

Somo hili linaonyesha jinsi ya kutekeleza uthibitishaji wa OAuth2 kwa seva za MCP kwa kutumia Spring Boot, mfano wa kawaida kwa uenezi wa biashara na uzalishaji.

## Malengo ya Kujifunza

Mwisho wa somo hili, utakuwa umeweza:
- Kuelewa jinsi OAuth2 inavyounganishwa na seva za MCP
- Kutekeleza Spring Authorization Server kwa kutoa tokeni
- Kulinda vituo vya MCP kwa uthibitishaji unaotegemea JWT
- Kusanidi mtiririko wa vyeti vya mteja kwa mawasiliano ya mashine-kwa-mashine

## Masharti ya Awali

- Uelewa wa msingi wa Java na Spring Boot
- Uzoefu na dhana za MCP kutoka moduli za awali
- Maven au Gradle ilisakinishwa

---

## Muhtasari wa Mradi

Mradi huu ni **programu ya chini kabisa ya Spring Boot** inayofanya kazi kama:

* **Spring Authorization Server** (kutolewa tokeni za ufikiaji za JWT kupitia mtiririko wa `client_credentials`), na  
* **Resource Server** (kulinda kituo chake cha `/hello`).

Inafanana na usanidi ulioonyeshwa kwenye [chapisho la blogu la Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Anza Haraka (ndani)

```bash
# Tumia thamani ya kipekee ya ndani na uiweke nje ya historia ya shell inapowezekana.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# pata tokeni
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# piga simu kwa sehemu iliyo salama
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Kupima Usanidi wa OAuth2

Unaweza kupima usanidi wa usalama wa OAuth2 kwa hatua zifuatazo:

### 1. Hakiki seva inakimbia na kupewa usalama

```bash
# Hii inapaswa kurudisha 401 Unauthorized, ikithibitisha usalama wa OAuth2 uko hai
curl -v http://localhost:8081/
```

### 2. Pata tokeni ya ufikiaji kwa kutumia vyeti vya mteja

```bash
# Pata na uchambue majibu kamili ya tokeni
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Au kuchambua tokeni pekee (inahitaji jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Katika PowerShell, weka siri ya eneo kabla ya kuendesha Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Fikia kituo kililolindwa kwa kutumia tokeni

```bash
# Kutumia tokeni iliyohifadhiwa
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Au moja kwa moja kwa thamani ya tokeni
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Jibu lenye mafanikio na "Hello from MCP OAuth2 Demo!" linathibitisha kuwa usanidi wa OAuth2 unafanya kazi ipasavyo.

---

## Ujenzi wa Kontena

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Usalama wa Uzalishaji

Kwa uenezi wa uzalishaji, tumia mtoa huduma wa utambulisho maalum badala ya
seva ya idhini ya majaribio ndani ya mchakato huu. Hifadhi vyeti kwenye
duka la siri lililodhibitiwa, zigeuze mara kwa mara, tumia funguo za kusaini zinazodumu, zizuie upeo wa ruhusa, na
weka mtumiaji (issuer) waziwazi. Kamwe usiweka siri ya mteja kwenye msimbo wa chanzo, picha za kontena,
maelezo ya usambazaji, au matokeo ya amri.

Kwa Azure Container Apps, hifadhi thamani kama siri ya Container Apps inayoungwa mkono na
Key Vault pale inapowezekana, kisha tolea marejeleo ya siri kupitia
 `OAUTH_CLIENT_SECRET` kama tofauti ya mazingira.

---

## Sambaza kwenye **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Anuani kamili ya kulaingilia (FQDN) hutokea kuwa **mtumiaji** (`https://<fqdn>`).  
Azure hutoa cheti cha TLS kinachoaminika kiotomatiki kwa `*.azurecontainerapps.io`.

---

## Unganisha na **Azure API Management**

Ongeza sera hii ya kuingiza kwenye API yako:

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

APIM itachukua JWKS na kuthibitisha kila ombi.

---

## Nini Kifuatayo

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
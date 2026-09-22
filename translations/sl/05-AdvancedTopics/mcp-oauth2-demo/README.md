# MCP OAuth2 Demo

> [!WARNING]
> To je lokalni učni primer, ne proizvodna avtorizacijska storitev. Uporablja
> klienta v pomnilniku in ob zagonu generira nov ključ za podpisovanje. Nikoli
> ga ne nameščajte z deljenim, privzetim ali v izvorni kodi nadzorovanim skrivnim ključem klienta.

## Uvod

OAuth2 je industrijski standardni protokol za avtorizacijo, ki omogoča varen dostop do virov brez deljenja pristopnih podatkov. V implementacijah MCP (Model Context Protocol) OAuth2 zagotavlja zanesljiv način za preverjanje pristnosti in avtorizacijo klientov (kot so AI agenti) za dostop do MCP strežnikov in njihovih orodij.

Ta lekcija prikazuje, kako implementirati OAuth2 preverjanje pristnosti za MCP strežnike z uporabo Spring Boot, pogostega vzorca za poslovne in produkcijske namestitve.

## Cilji učenja

Do konca te lekcije boste:
- Razumeli, kako se OAuth2 integrira z MCP strežniki
- Implementirali Spring Authorization Server za izdajo žetonov
- Zaščitili MCP končne točke z avtentikacijo na osnovi JWT
- Konfigurirali tok poverilnic klienta za komunikacijo stroj-stroj

## Predpogoji

- Osnovno razumevanje Jave in Spring Boot
- Poznavanje pojmov MCP iz prejšnjih modulov
- Nameščen Maven ali Gradle

---

## Pregled projekta

Ta projekt je **minimalna aplikacija Spring Boot**, ki deluje kot:

* **Spring Authorization Server** (izdaja JWT dostopne žetone preko `client_credentials` toka), in  
* **Resource Server** (zaščiti svojo `/hello` končno točko).

Zrcali nastavitev prikazano v [Spring blog zapisu (2. aprila 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Hiter začetek (lokalno)

```bash
# Uporabite edinstveno lokalno vrednost in jo po možnosti ne shranjujte v zgodovino ukazne vrstice.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# pridobite žeton
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# pokličite zaščiteno točko konca
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testiranje OAuth2 konfiguracije

OAuth2 varnostno konfiguracijo lahko testirate z naslednjimi koraki:

### 1. Preverite, da strežnik teče in je zaščiten

```bash
# To bi moralo vrniti 401 Nepooblaščeno, kar potrjuje, da je OAuth2 varnost aktivna
curl -v http://localhost:8081/
```

### 2. Pridobite dostopni žeton z uporabo poverilnic klienta

```bash
# Pridobi in izvleči celoten odgovor tokena
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Ali da izvlečeš samo token (zahteva jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

V PowerShellu nastavite lokalno skrivnost preden zaženete Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Dostopajte do zaščitene končne točke z žetonom

```bash
# Uporaba shranjenega žetona
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ali neposredno z vrednostjo žetona
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uspešen odgovor z "Hello from MCP OAuth2 Demo!" potrjuje pravilno delovanje OAuth2 konfiguracije.

---

## Zgradite kontejner

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Proizvodna varnost

Za proizvodno nameščanje uporabite namenski ponudnik identitete namesto
tega demo avtorizacijskega strežnika v procesu. Shranjujte poverilnice v upravljanem
shrambnem mestu skrivnosti, jih rotirajte, uporabljajte vztrajne ključe za podpisovanje, omejite obsege in
določite eksplicitnega izdajatelja. Nikoli ne vključite skrivnosti klienta v izvorno kodo, slike kontejnerjev,
namestitvene manifeste ali izhode ukazov.

Za Azure Container Apps, shranite vrednost kot skrivnost Container Apps, podprto z
Key Vaultom, kjer je mogoče, nato pa izpostavite samo referenco na skrivnost preko
okoljske spremenljivke `OAUTH_CLIENT_SECRET`.

---

## Namestite v **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Vhodni FQDN postane vaš **izdajatelj** (`https://<fqdn>`).  
Azure samodejno zagotavlja zanesljiv TLS certifikat za `*.azurecontainerapps.io`.

---

## Povežite v **Azure API Management**

Dodajte to vhodno politiko za vaš API:

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

APIM bo pridobil JWKS in validiral vsak zahtevek.

---

## Kaj sledi

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
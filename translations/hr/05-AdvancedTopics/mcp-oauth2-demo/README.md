# MCP OAuth2 Demo

> [!WARNING]
> Ovo je lokalni uzorak za učenje, a ne servis za autorizaciju u produkciji. On
> koristi klijenta u memoriji i generira novi ključ za potpisivanje pri pokretanju. Nikada
> nemojte ovaj servis postaviti sa zajedničkim, zadanim ili u kontroliranoj verziji klijentskim tajnim podacima.

## Uvod

OAuth2 je industrijski standardni protokol za autorizaciju, omogućujući siguran pristup resursima bez dijeljenja vjerodajnica. U implementacijama MCP (Model Context Protocol), OAuth2 pruža robustan način autentikacije i autorizacije klijenata (kao što su AI agenti) za pristup MCP serverima i njihovim alatima.

Ova lekcija pokazuje kako implementirati OAuth2 autentikaciju za MCP servere koristeći Spring Boot, što je uobičajeni obrazac za poduzeća i produkcijske implementacije.

## Ciljevi učenja

Do kraja ove lekcije ćete:
- Razumjeti kako se OAuth2 integrira s MCP serverima
- Implementirati Spring Authorization Server za izdavanje tokena
- Zaštititi MCP krajnje točke s autentikacijom na bazi JWT-a
- Konfigurirati tok klijentskih vjerodajnica za komunikaciju stroj-stroju

## Preduvjeti

- Osnovno razumijevanje Jave i Spring Boota
- Poznavanje MCP koncepata iz ranijih modula
- Instaliran Maven ili Gradle

---

## Pregled projekta

Ovaj projekt je **minimalna Spring Boot aplikacija** koja funkcionira kao:

* **Spring Authorization Server** (izdaje JWT pristupne tokene preko `client_credentials` toka), i  
* **Resource Server** (zaštitio vlastitu `/hello` krajnju točku).

Oponaša postavke prikazane u [Spring blog postu (2. travnja 2025.)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Brzi početak (lokalno)

```bash
# Koristite jedinstvenu lokalnu vrijednost i držite je izvan povijesti ljuske kad god je to moguće.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# pribavite token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# pozovite zaštićenu krajnju točku
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testiranje OAuth2 konfiguracije

Možete testirati OAuth2 sigurnosnu konfiguraciju sljedećim koracima:

### 1. Provjerite da li je server pokrenut i zaštićen

```bash
# Ovo bi trebalo vratiti 401 Neovlašteno, potvrđujući da je OAuth2 sigurnost aktivna
curl -v http://localhost:8081/
```

### 2. Nabavite pristupni token koristeći klijentske vjerodajnice

```bash
# Dohvati i izdvoji puni odgovor tokena
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Ili izdvoji samo token (zahtijeva jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Na PowerShellu, postavite lokalni tajni podatak prije pokretanja Mavena:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Pristupite zaštićenoj krajnjoj točki koristeći token

```bash
# Koristeći spremljeni token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ili izravno s vrijednošću tokena
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uspješan odgovor s "Hello from MCP OAuth2 Demo!" potvrđuje da OAuth2 konfiguracija radi ispravno.

---

## Izgradnja kontejnera

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Sigurnost u produkciji

Za produkcijsko postavljanje, koristite posvećenog pružatelja identiteta umjesto
ovog demo servera za autorizaciju u procesu. Pohranite vjerodajnice u upravljani
skladište tajni, rotirajte ih, koristite trajne ključeve za potpisivanje, ograničite opsege, i
postavite eksplicitan issuer. Nikada ne stavljajte klijentski tajni podatak u izvorni kod, slike kontejnera,
postavne manifeste ili izlaze naredbi.

Za Azure Container Apps, pohranite vrijednost kao tajnu Container Apps koja je podržana
Key Vaultom gdje je moguće, i zatim izložite samo referencu na tajnu preko
`OAUTH_CLIENT_SECRET` varijable okruženja.

---

## Postavljanje na **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN postaje vaš **issuer** (`https://<fqdn>`).  
Azure automatski pruža pouzdani TLS certifikat za `*.azurecontainerapps.io`.

---

## Povezivanje u **Azure API Management**

Dodajte ovu ulaznu politiku u vaš API:

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

APIM će dohvatiti JWKS i validirati svaki zahtjev.

---

## Što je sljedeće

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
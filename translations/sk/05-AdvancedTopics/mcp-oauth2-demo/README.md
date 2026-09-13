# MCP OAuth2 Demo

> [!WARNING]
> Toto je lokálny vzor na učenie, nie produkčná autorizačná služba. Používa
> klienta v pamäti a pri štarte generuje nový podpisovací kľúč. Nikdy ho
> neumiestňujte do produkcie so zdieľaným, predvoleným alebo v zdrojovom kóde kontrolovaným tajomstvom klienta.

## Úvod

OAuth2 je štandardný protokol v priemysle pre autorizáciu, ktorý umožňuje bezpečný prístup k zdrojom bez zdieľania prihlasovacích údajov. V implementáciách MCP (Model Context Protocol) poskytuje OAuth2 robustný spôsob autentifikácie a autorizácie klientov (napríklad AI agentov) na prístup k MCP serverom a ich nástrojom.

Táto lekcia ukazuje, ako implementovať OAuth2 autentifikáciu pre MCP servery pomocou Spring Boot, bežného vzoru pre podnikové a produkčné nasadenia.

## Ciele učenia

Po absolvovaní tejto lekcie budete:
- Rozumieť, ako OAuth2 integruje MCP servery
- Implementovať Spring Authorization Server na vydávanie tokenov
- Chrániť MCP koncové body autentifikáciou založenou na JWT
- Konfigurovať priebeh poverení klienta pre komunikáciu medzi strojmi

## Predpoklady

- Základné znalosti Javy a Spring Boot
- Oboznámenie sa s konceptmi MCP z predošlých modulov
- Nainštalovaný Maven alebo Gradle

---

## Prehľad projektu

Tento projekt je **minimálna aplikácia Spring Boot**, ktorá slúži ako:

* **Spring Authorization Server** (vydáva JWT prístupové tokeny cez priebeh `client_credentials`), a  
* **Resource Server** (chráni vlastný koncový bod `/hello`).

Zrkadlí nastavenie zobrazené v [Spring blogovom príspevku (2. apríl 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Rýchly štart (lokálne)

```bash
# Použite jedinečnú lokálnu hodnotu a ak je to možné, vyhnite sa jej ukladaniu do histórie shellu.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# získajte token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# zavolajte chránený endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testovanie konfigurácie OAuth2

Konfiguráciu zabezpečenia OAuth2 môžete otestovať podľa týchto krokov:

### 1. Overte, že server beží a je zabezpečený

```bash
# Toto by malo vrátiť 401 Unauthorized, čím sa potvrdí, že je aktívna bezpečnosť OAuth2
curl -v http://localhost:8081/
```

### 2. Získajte prístupový token použitím poverení klienta

```bash
# Získať a extrahovať plnú odpoveď tokenu
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Alebo extrahovať iba token (vyžaduje jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

V PowerShell nastavte lokálne tajomstvo pred spustením Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Pristúpte ku chránenému koncovému bodu pomocou tokenu

```bash
# Použitie uloženého tokenu
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Alebo priamo s hodnotou tokenu
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Úspešná odpoveď s "Hello from MCP OAuth2 Demo!" potvrdzuje správne fungovanie konfigurácie OAuth2.

---

## Vytvorenie kontajnera

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Produkčné zabezpečenie

Pre produkčné nasadenie použite vyhradeného poskytovateľa identity namiesto
tohto demo autorizačného servera v rámci procesu. Uchovávajte poverenia v spravovanom
úložisku tajomstiev, rotujte ich, používajte perzistentné podpisovacie kľúče, obmedzujte rozsahy a
nastavte explicitného vydavateľa. Nikdy neumiestňujte klientské tajomstvo do zdrojového kódu, kontajnerových
obrazov, nasadzovacích manifestov alebo výstupu príkazového riadku.

Pre Azure Container Apps uložte hodnotu ako tajomstvo Container Apps podporované
službou Key Vault, kde je to možné, a potom vystavte iba referenciu na tajomstvo cez
environmentálnu premennú `OAUTH_CLIENT_SECRET`.

---

## Nasadenie do **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN sa stane vaším **vydavateľom** (`https://<fqdn>`).  
Azure automaticky poskytuje dôveryhodný TLS certifikát pre `*.azurecontainerapps.io`.

---

## Prepojenie s **Azure API Management**

Pridajte túto vstupnú politiku do vášho API:

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

APIM automaticky získa JWKS a validuje každý požiadavok.

---

## Čo ďalej

- [5.4 Koreňové kontexty](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
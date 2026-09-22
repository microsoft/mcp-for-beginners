# MCP OAuth2 Demo

> [!WARNING]
> Toto je lokální ukázka pro výuku, nikoli produkční autorizační služba. Používá
> klienta v paměti a při spuštění generuje nový podepisovací klíč. Nikdy ji
> nenasazujte s sdíleným, výchozím nebo ve zdrojovém kódu řízeným klientským sekretem.

## Úvod

OAuth2 je průmyslový standardní protokol pro autorizaci, který umožňuje bezpečný přístup k prostředkům bez sdílení přihlašovacích údajů. V implementacích MCP (Model Context Protocol) poskytuje OAuth2 robustní způsob autentizace a autorizace klientů (např. AI agentů) pro přístup k MCP serverům a jejich nástrojům.

Tento návod ukazuje, jak implementovat OAuth2 autentizaci pro MCP servery pomocí Spring Boot, běžného vzoru pro podniková a produkční nasazení.

## Výukové cíle

Na konci této lekce budete umět:
- Pochopit, jak se OAuth2 integruje s MCP servery
- Implementovat Spring Authorization Server pro vydávání tokenů
- Chránit MCP koncové body autentizací založenou na JWT
- Nakonfigurovat client credentials flow pro komunikaci stroj-stroji

## Předpoklady

- Základní znalost Javy a Spring Boot
- Seznámení s pojmy MCP z předchozích modulů
- Nainstalovaný Maven nebo Gradle

---

## Přehled projektu

Tento projekt je **minimální Spring Boot aplikace**, která funguje jako:

* **Spring Authorization Server** (vydává JWT přístupové tokeny přes `client_credentials` flow), a  
* **Resource Server** (chrání svůj vlastní `/hello` endpoint).

Odpovídá nastavení zobrazenému v [Spring blogovém příspěvku (2. dubna 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Rychlý start (lokálně)

```bash
# Použijte jedinečnou lokální hodnotu a pokud možno ji udržujte mimo historii shellu.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# získejte token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# zavolejte chráněný koncový bod
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testování konfigurace OAuth2

Konfiguraci zabezpečení OAuth2 můžete otestovat následujícími kroky:

### 1. Ověřte, že server běží a je zabezpečený

```bash
# Toto by mělo vrátit 401 Unauthorized, což potvrzuje, že zabezpečení OAuth2 je aktivní
curl -v http://localhost:8081/
```

### 2. Získejte přístupový token pomocí client credentials

```bash
# Získat a extrahovat kompletní odpověď tokenu
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Nebo extrahovat pouze token (vyžaduje jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Na PowerShellu nastavte lokální tajemství před spuštěním Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Přistupte k chráněnému endpointu pomocí tokenu

```bash
# Použití uloženého tokenu
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Nebo přímo s hodnotou tokenu
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Úspěšná odpověď s textem "Hello from MCP OAuth2 Demo!" potvrzuje správnou funkci konfigurace OAuth2.

---

## Sestavení kontejneru

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Produkční zabezpečení

Pro produkční nasazení použijte dedikovaného poskytovatele identity namísto
tohoto demo autorizačního serveru v procesu. Ukládejte přihlašovací údaje do
spravovaného úložiště tajemství, pravidelně je obměňujte, používejte
trvalé podepisovací klíče, omezujte autorizační rozsahy a zadávejte explicitního vydavatele. Nikdy
nezapisujte klientský sekret do zdrojového kódu, kontejnerových obrazů,


Pro Azure Container Apps ukládejte hodnotu jako tajemství Container Apps podporované
Key Vault, pokud je to možné, a pak zveřejněte pouze odkaz na tajemství pomocí






```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN se stane vaším **vydavatelem** (`https://<fqdn>`).  








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






- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
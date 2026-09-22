# MCP OAuth2 Demo

> [!WARNING]
> Ito ay isang lokal na sample para sa pag-aaral, hindi isang production na serbisyo ng awtorisasyon. Ginagamit nito ang isang in-memory na kliyente at bumubuo ng bagong signing key sa pagsisimula. Huwag
> itong i-deploy gamit ang isang ibinahagi, default, o source-controlled na client secret.


## Panimula

Ang OAuth2 ay ang industry-standard na protocol para sa awtorisasyon, na nagbibigay-daan sa ligtas na pag-access sa mga resources nang hindi ibinabahagi ang mga kredensyal. Sa mga implementasyon ng MCP (Model Context Protocol), ang OAuth2 ay nagbibigay ng matibay na paraan upang i-authenticate at i-authorize ang mga kliyente (tulad ng mga AI agent) na ma-access ang mga MCP server at ang kanilang mga tools.

Ipinapakita ng leksyon na ito kung paano ipatupad ang OAuth2 authentication para sa mga MCP server gamit ang Spring Boot, isang karaniwang pattern para sa enterprise at production na deploy.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng leksyon na ito, iyong:
- Maiintindihan kung paano nagsasama ang OAuth2 sa MCP servers
- Makakapagpatupad ng Spring Authorization Server para sa pagpapalabas ng token
- Mapoprotektahan ang MCP endpoints gamit ang JWT-based authentication
- Makakakonpigura ng client credentials flow para sa machine-to-machine na komunikasyon

## Mga Kinakailangan

- Basic na pag-unawa sa Java at Spring Boot
- Pamilyar sa mga konsepto ng MCP mula sa mga naunang module
- Nakainstall ang Maven o Gradle

---

## Pangkalahatang-ideya ng Proyekto

Ang proyektong ito ay isang **minimal Spring Boot application** na nagsisilbi bilang parehong:

* isang **Spring Authorization Server** (naglalabas ng JWT access tokens gamit ang `client_credentials` flow), at  
* isang **Resource Server** (pinoprotektahan ang sarili nitong `/hello` endpoint).

Ginagaya nito ang setup na ipinakita sa [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mabilis na pagsisimula (lokal)

```bash
# Gumamit ng natatanging lokal na halaga at panatilihing hindi naka-save sa kasaysayan ng shell kung maaari.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# kumuha ng token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# tawagan ang protektadong endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Pagsusuri ng OAuth2 Configuration

Maaari mong subukan ang OAuth2 security configuration gamit ang mga sumusunod na hakbang:

### 1. Suriin kung tumatakbo at naka-secure ang server

```bash
# Dapat itong magbalik ng 401 Unauthorized, na nagpapatunay na aktibo ang seguridad ng OAuth2
curl -v http://localhost:8081/
```

### 2. Kumuha ng access token gamit ang client credentials

```bash
# Kunin at kunin ang buong tugon ng token
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# O upang kunin lamang ang token (kailangan ng jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Sa PowerShell, itakda ang lokal na secret bago patakbuhin ang Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. I-access ang protektadong endpoint gamit ang token

```bash
# Ginagamit ang na-save na token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# O direkta gamit ang halaga ng token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Ang matagumpay na tugon na may "Hello from MCP OAuth2 Demo!" ay nagpapatunay na tama ang pagkaka-configure ng OAuth2.

---

## Pagbuo ng container

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Seguridad sa Produksyon

Para sa production deployment, gumamit ng dedikadong identity provider sa halip na
itong in-process demo authorization server. Itago ang mga kredensyal sa isang managed
secret store, i-rotate ang mga ito, gumamit ng persistent signing keys, limitahan ang mga scope, at
magtakda ng isang tiyak na issuer. Huwag kailanman ilagay ang client secret sa source code, container
images, deployment manifests, o output ng command.

Para sa Azure Container Apps, itago ang halaga bilang isang Container Apps secret na suportado ng
Key Vault kung maaari, pagkatapos ay ilantad lamang ang isang secret reference sa pamamagitan ng
`OAUTH_CLIENT_SECRET` environment variable.

---

## I-deploy sa **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ang ingress FQDN ang magiging iyong **issuer** (`https://<fqdn>`).  
Ang Azure ay awtomatikong nagbibigay ng isang pinagkakatiwalaang TLS certificate para sa `*.azurecontainerapps.io`.

---

## I-wire sa **Azure API Management**

Idagdag ang inbound policy na ito sa iyong API:

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

Kukunin ng APIM ang JWKS at susuriin ang bawat kahilingan.

---

## Ano ang susunod

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
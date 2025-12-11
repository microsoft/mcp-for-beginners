<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0a7083e660ca0d85fd6a947514c61993",
  "translation_date": "2025-12-11T16:16:22+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/README.md",
  "language_code": "ml"
}
-->
# MCP OAuth2 ഡെമോ

ഈ പ്രോജക്ട് ഒരു **മിനിമൽ സ്പ്രിംഗ് ബൂട്ട് അപ്ലിക്കേഷൻ** ആണ്, ഇത് രണ്ട് കാര്യങ്ങൾ ചെയ്യുന്നു:

* ഒരു **സ്പ്രിംഗ് ഓതറൈസേഷൻ സർവർ** ( `client_credentials` ഫ്ലോ വഴി JWT ആക്സസ് ടോക്കണുകൾ നൽകുന്നു), കൂടാതെ  
* ഒരു **റിസോഴ്‌സ് സർവർ** (തന്റെ സ്വന്തം `/hello` എൻഡ്‌പോയിന്റ് സംരക്ഷിക്കുന്നു).

ഇത് [സ്പ്രിംഗ് ബ്ലോഗ് പോസ്റ്റ് (2 ഏപ്രിൽ 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) ൽ കാണിച്ച സജ്ജീകരണത്തെ അനുകരിക്കുന്നു.

---

## ക്വിക്ക് സ്റ്റാർട്ട് (ലോകൽ)

```bash
# നിർമ്മിച്ച് പ്രവർത്തിപ്പിക്കുക
./mvnw spring-boot:run

# ഒരു ടോക്കൺ നേടുക
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# സംരക്ഷിത എൻഡ്‌പോയിന്റ് വിളിക്കുക
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2 കോൺഫിഗറേഷൻ ടെസ്റ്റിംഗ്

നിങ്ങൾക്ക് താഴെ പറയുന്ന ഘട്ടങ്ങൾ ഉപയോഗിച്ച് OAuth2 സുരക്ഷാ കോൺഫിഗറേഷൻ ടെസ്റ്റ് ചെയ്യാം:

### 1. സർവർ പ്രവർത്തിക്കുന്നതും സുരക്ഷിതമാണെന്നും സ്ഥിരീകരിക്കുക

```bash
# ഇത് 401 അനധികൃതം തിരികെ നൽകണം, OAuth2 സുരക്ഷ സജീവമാണെന്ന് സ്ഥിരീകരിക്കുന്നു
curl -v http://localhost:8081/
```

### 2. ക്ലയന്റ് ക്രെഡൻഷ്യലുകൾ ഉപയോഗിച്ച് ആക്സസ് ടോക്കൺ നേടുക

```bash
# പൂർണ്ണ ടോക്കൺ പ്രതികരണം നേടുകയും പിഴുതെടുക്കുകയും ചെയ്യുക
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# അല്ലെങ്കിൽ ടോക്കൺ മാത്രം പിഴുതെടുക്കാൻ (jq ആവശ്യമാണ്)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

കുറിപ്പ്: ബേസിക് ഓതന്റിക്കേഷൻ ഹെഡർ (`bWNwLWNsaWVudDpzZWNyZXQ=`) `mcp-client:secret` എന്നതിന്റെ Base64 എൻകോഡിങ്ങാണ്.

### 3. ടോക്കൺ ഉപയോഗിച്ച് സംരക്ഷിത എൻഡ്‌പോയിന്റ് ആക്സസ് ചെയ്യുക

```bash
# സേവ് ചെയ്ത ടോക്കൺ ഉപയോഗിക്കുന്നു
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# അല്ലെങ്കിൽ ടോക്കൺ മൂല്യത്തോടെ നേരിട്ട്
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" എന്ന വിജയകരമായ പ്രതികരണം OAuth2 കോൺഫിഗറേഷൻ ശരിയായി പ്രവർത്തിക്കുന്നതായി സ്ഥിരീകരിക്കുന്നു.

---

## കണ്ടെയ്‌നർ ബിൽഡ്

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** ലേക്ക് ഡിപ്ലോയ് ചെയ്യുക

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ഇൻഗ്രസ് FQDN നിങ്ങളുടെ **ഇഷ്യൂവർ** (`https://<fqdn>`) ആകുന്നു.  
`*.azurecontainerapps.io` ന് Azure സ്വയം വിശ്വസനീയമായ TLS സർട്ടിഫിക്കറ്റ് നൽകുന്നു.

---

## **Azure API Management** ൽ വയർ ചെയ്യുക

നിങ്ങളുടെ API-യിൽ ഈ ഇൻബൗണ്ട് പോളിസി ചേർക്കുക:

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

APIM JWKS ഫെച്ച് ചെയ്ത് ഓരോ അഭ്യർത്ഥനയും സാധുത പരിശോധിക്കും.

---

## അടുത്തത് എന്താണ്

- [5.4 റൂട്ട് കോൺടെക്സ്റ്റുകൾ](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
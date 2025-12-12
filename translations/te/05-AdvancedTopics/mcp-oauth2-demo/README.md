<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0a7083e660ca0d85fd6a947514c61993",
  "translation_date": "2025-12-11T16:15:38+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/README.md",
  "language_code": "te"
}
-->
# MCP OAuth2 డెమో

ఈ ప్రాజెక్ట్ ఒక **సూక్ష్మ స్ప్రింగ్ బూట్ అప్లికేషన్** గా పనిచేస్తుంది, ఇది రెండు విధాలుగా ఉంటుంది:

* ఒక **స్ప్రింగ్ ఆథరైజేషన్ సర్వర్** ( `client_credentials` ఫ్లో ద్వారా JWT యాక్సెస్ టోకెన్లను జారీ చేస్తుంది), మరియు  
* ఒక **రిసోర్స్ సర్వర్** (తన స్వంత `/hello` ఎండ్‌పాయింట్‌ను రక్షిస్తుంది).

ఇది [స్ప్రింగ్ బ్లాగ్ పోస్ట్ (2 ఏప్రిల్ 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) లో చూపించిన సెటప్‌ను ప్రతిబింబిస్తుంది.

---

## త్వరిత ప్రారంభం (లోకల్)

```bash
# నిర్మించండి & నడపండి
./mvnw spring-boot:run

# టోకెన్ పొందండి
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# రక్షిత ఎండ్‌పాయింట్‌ను కాల్ చేయండి
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2 కాన్ఫిగరేషన్‌ను పరీక్షించడం

క్రింది దశలతో మీరు OAuth2 సెక్యూరిటీ కాన్ఫిగరేషన్‌ను పరీక్షించవచ్చు:

### 1. సర్వర్ నడుస్తున్నదని మరియు సురక్షితమై ఉందని నిర్ధారించుకోండి

```bash
# ఇది 401 Unauthorized ను తిరిగి ఇవ్వాలి, OAuth2 భద్రత సక్రియంగా ఉందని నిర్ధారిస్తుంది
curl -v http://localhost:8081/
```

### 2. క్లయింట్ క్రెడెన్షియల్స్ ఉపయోగించి యాక్సెస్ టోకెన్ పొందండి

```bash
# పూర్తి టోకెన్ ప్రతిస్పందనను పొందండి మరియు తీసుకోండి
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# లేదా కేవలం టోకెన్‌ను తీసుకోవడానికి (jq అవసరం)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

గమనిక: బేసిక్ ఆథెంటికేషన్ హెడ్డర్ (`bWNwLWNsaWVudDpzZWNyZXQ=`) అనేది `mcp-client:secret` యొక్క Base64 ఎన్‌కోడింగ్.

### 3. టోకెన్ ఉపయోగించి రక్షిత ఎండ్‌పాయింట్‌ను యాక్సెస్ చేయండి

```bash
# సేవ్ చేసిన టోకెన్ ఉపయోగించడం
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# లేదా టోకెన్ విలువతో నేరుగా
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" అనే విజయవంతమైన స్పందన OAuth2 కాన్ఫిగరేషన్ సరిగ్గా పనిచేస్తున్నదని నిర్ధారిస్తుంది.

---

## కంటైనర్ బిల్డ్

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** కు డిప్లాయ్ చేయండి

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ఇన్‌గ్రెస్ FQDN మీ **ఇష్యూ** అవుతుంది (`https://<fqdn>`).  
Azure `*.azurecontainerapps.io` కోసం ఆటోమేటిక్‌గా ట్రస్టెడ్ TLS సర్టిఫికేట్ అందిస్తుంది.

---

## **Azure API Management** లో వైర్ చేయండి

మీ APIకి ఈ ఇన్‌బౌండ్ పాలసీని జోడించండి:

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

APIM JWKSని తీసుకుని ప్రతి అభ్యర్థనను ధృవీకరిస్తుంది.

---

## తదుపరి ఏమిటి

- [5.4 రూట్ కాంటెక్స్ట్‌లు](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
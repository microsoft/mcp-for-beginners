# MCP OAuth2 ដេមូ

## ការណែនាំ

OAuth2 គឺជាកម្មវិធីផ្លូវការ​កម្រិតឧស្សាហកម្មសម្រាប់ការអនុញ្ញាត ដែលអនុញ្ញាតឲ្យចូលដំណើរការដោយសុវត្ថិភាពទៅធនធានដោយមិនចែករំលែកគណនីសម្ងាត់។ ក្នុងការអនុវត្ត MCP (Model Context Protocol) OAuth2 នឹងផ្តល់នូវវិធីសាស្រ្តរឹងមាំសម្រាប់ធ្វើអត្តសញ្ញាណ និងអនុញ្ញាតឲ្យអតិថិជនៗ (ដូចជាតំណាង AI) ចូលប្រើម៉ាស៊ីនមេ MCP និងឧបករណ៍របស់ខ្លួន។

មេរៀននេះបង្ហាញពីរបៀបអនុវត្តAuthentication OAuth2 សម្រាប់ម៉ាស៊ីនមេ MCP ដោយប្រើ Spring Boot ដែលជាគំរូទូទៅសម្រាប់ការដាក់បញ្ចូលក្នុងសហគ្រាស និងផលិតកម្ម។

## គោលបំណងការសិក្សា

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖  
- យល់ពីរបៀបដែល OAuth2 បន្សំពាក់ជាមួយម៉ាស៊ីនមេ MCP  
- អនុវត្តSpring Authorization Server សម្រាប់ចេញផ្ដល់សញ្ញាអត្តសញ្ញាណ  
- ពារបញ្ចប់ MCP ជាមួយAuthentication ដោយផ្អែកលើ JWT  
- កំណត់រចនាសម្ព័ន្ធ client credentials flow សម្រាប់ទំនាក់ទំនងម៉ាស៊ីនទៅម៉ាស៊ីន

## គ្រោងចាំបាច់

- ការយល់ដឹងមូលដ្ឋាននៃ Java និង Spring Boot  
- ស្គាល់គំនិត MCP ពីមូឌុលមុនៗ  
- មានការតំឡើង Maven ឬ Gradle

---

## ជម្រេីសគម្រោង

គម្រោងនេះគឺជា **កម្មវិធី Spring Boot តូចបំផុត**ដែលដំណើរការជាទាំង៖  

* **Spring Authorization Server** (ចេញផ្ដល់ access tokens JWT តាម client_credentials flow), និង  
* **Resource Server** (ការពារបញ្ចប់ `/hello` របស់ខ្លួន)។

វាស្រដៀងនឹងការកំណត់ដែលបង្ហាញក្នុង [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2)។

---

## ចាប់ផ្ដើមបានរហ័ស (ក្នុងកន្លែង)

```bash
# សង់ និងរត់
./mvnw spring-boot:run

# ទទួលបានតូកែន
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# ហៅច្រកចូលបានការពារ
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## ការតេស្តការកំណត់ OAuth2

អ្នកអាចតេស្តការកំណត់សុវត្ថិភាព OAuth2 ជាមួយជំហានដូចតទៅ៖

### ១. ពិនិត្យមើលមើលម៉ាស៊ីនមេកំពុងដំណើរការនិងមានសុវត្ថិភាព

```bash
# នេះគួរតែត្រឡប់មក 401 Unauthorized ដែលបញ្ជាក់ថាសុវត្ថិភាព OAuth2 កំពុងដំណើរការ។
curl -v http://localhost:8081/
```

### ២. ទទួលសញ្ញាអោយចូល (access token) ដោយប្រើ client credentials

```bash
# ទទួលនិងដកយកចេញចម្លើយទូទាំងសញ្ញាតំណាង
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# ឬដកយកគ្រាន់តែសញ្ញាតំណាងប៉ុណ្ណោះ (តម្រូវឱ្យមាន jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

គំនិតៈ ក្បាលAuthentication Basic (`bWNwLWNsaWVudDpzZWNyZXQ=`) គឺជាការអ៊ិនកូដ Base64 នៃ `mcp-client:secret`។

### ៣. ចូលដំណើរការបញ្ចប់ដែលបានការពារ ដោយប្រើសញ្ញា

```bash
# ការប្រើប្រាស់សញ្ញាស្លាកដែលបានរក្សាទុក
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# ឬផ្ទាល់ជាមួយតម្លៃសញ្ញាស្លាក
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

ចម្លើយជោគជ័យជាមួយ "Hello from MCP OAuth2 Demo!" បញ្ជាក់ថាការកំណត់ OAuth2 ធ្វើការបានត្រឹមត្រូវ។

---

## ការបង្កើតកុងតឺន័រ

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## ដាក់បញ្ចូលទៅ **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ឈ្មោះ FQDN ចូល (ingress) ក្លាយជាអ្នកផ្ដល់សញ្ញា (issuer) របស់អ្នក (`https://<fqdn>`)។  
Azure ផ្ដល់វិញ្ញាបនបត្រ TLS ដែលមានទំនុកចិត្តដោយស្វ័យប្រវត្តសម្រាប់ `*.azurecontainerapps.io`។

---

## តភ្ជាប់ទៅ **Azure API Management**

បន្ថែមគោលការណ៍ inbound នេះទៅ API របស់អ្នក៖

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

APIM នឹងយក JWKS ហើយផ្ទៀងផ្ទាត់គ្រប់សំណើ។

---

## តើក្រោមនេះជាអ្វី

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយល់ឱ្យបានថាការបកប្រែដោយម៉ាស៊ីនអាចមានកំហុស ឬមិនត្រឹមត្រូវបាន។ ឯកសារដើមដែលមានជាភាសមូលដ្ឋានគួរត្រូវបានគិតថាជាដែនកំណត់ដើម។ សម្រាប់ព័ត៌មានសំខាន់ៗ គេណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីព។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបញ្ចេញមតិបញ្ចេញលទ្ធផលខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
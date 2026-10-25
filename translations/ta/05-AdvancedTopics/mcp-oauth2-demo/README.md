# MCP OAuth2 டெமோ

> [!WARNING]
> இது உள்ளூரான கற்றல் உதாரணம், உற்பத்தி அங்கீகார சேவையானது அல்ல. இது
> நினைவகத்தில் உள்ளது என்பது ஒரு கிளையண்டைப் பயன்படுத்துகிறது மற்றும் துவக்கத்தில் புதிய கையொப்பச் சாவியை உருவாக்குகிறது. ஒருபோதும்
> இதனை பகிரப்பட்ட, இயல்புநிலை அல்லது மூலகட்டுப்படுத்தப்பட்ட கிளையண்ட் ரகசியத்துடன் பயன்படுத்த வேண்டாம்.

## அறிமுகம்

OAuth2 என்பது vjerpஅங்கீகாரம் க்கான தொழிற்துறை தரமான நெறிமுறை, அங்கீகாரச் சான்றுகளைப் பகிராமல் வளங்களுக்கான பாதுகாப்பான அணுகலை வழங்குகிறது. MCP (மாதிரி சூழல் நெறிமுறை) செயல்பாடுகளில், OAuth2 MCP சேவையகங்கள் மற்றும் அவற்றின் கருவிகளுக்கு அணுகு உள்வாழ்க்கைகளை ஆட்சி செய்ய AI முகவரிகள் போன்ற வாடிக்கையாளர்களை உறுதிப்படுத்தவும் அங்கீகரிக்கவும் வலுவான வழியை வழங்குகிறது.

இந்த பாடத்தில் MCP சேவையகங்களுக்கு OAuth2 அங்கீகாரத்தை வினியோகிப்பது எப்படி என்று Spring Boot பயன்படுத்தி நிறுவுவது ஒரு பொதுவான நடைமுறையாகும் என்பதை காண்பிக்கிறது, இது நிறுவன மற்றும் உற்பத்தி பிசுதாக்கல்களுக்கு பயன்படுத்தப்படுகிறது.

## கற்றல் நோக்குகள்

இந்த பாடத்தின் இறுதிக்குப் பிறகு, நீங்கள்:
- OAuth2 MCP சேவையகங்களுடன் எப்படி இணைபட்டுள்ளது என்பதை புரிந்து கொள்வீர்கள்
- குறிச்சொல் வழங்குவதற்கு Spring அங்கீகார சேவையகத்தை செயல்படுத்துவீர்கள்
- JWT அடிப்படையிலான அங்கீகாரத்துடன் MCP முடிச்சுகளை பாதுகாக்கவீர்கள்
- இயந்திரத்திலிருந்து இயந்திரம் தொடர்புக்கு கிளையண்ட் அங்கீகார இலைகளின் ஓட்டத்தை அமைப்பீர்கள்

## முன்னோட்டத் தேவைகள்

- ஜாவா மற்றும் ஸ்பிரிங்க் பூட் அடிப்படைக் கோட்பாடுகள்
- முற்பகுதி கணக்கீடு மூலம் MCP கருத்துக்களின் பனம்
- மேவன் அல்லது கிரேடில் நிறுவியிருக்க வேண்டும்

---

## திட்டம் கண்ணோட்டம்

இந்த திட்டம் ஒரு **குறைந்தபட்ச Spring Boot பயன்பாடு** ஆகும், இரண்டும் செயல்படுகிறது:

* ஒரு **Spring அங்கீகாரம் சேவையகம்** (JWT அணுகல் டோக்கன்களை `client_credentials` ஓட்டத்தில் வழங்குகிறது), மற்றும்  
* ஒரு **வள சேவையகம்** (தன் சொந்த `/hello` இடைமுகத்தை பாதுகாக்கிறது).

இது [Spring வலைப்பதிவு பதிவில் (2 ஏப் 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) காட்டப்பட்ட அமைப்பை பிரதிபலிக்கிறது.

---

## விரைவான தொடக்கம் (உள்ளூர்)

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

## OAuth2 கட்டமைப்பை சோதனை செய்தல்

கீழ்காணும் படிகளை பின்பற்றி OAuth2 பாதுகாப்பு கட்டமைப்பை சோதிக்கலாம்:

### 1. சேவையகம் இயக்கத்தில் உள்ளது மற்றும் பாதுகாக்கப்பட்டது என்பதை உறுதிப்படுத்துக

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. கிளையன்ட் சான்றுகளைக் கொண்டு அணுகல் டோக்கனைப் பெறுக

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

PowerShell இல், Maven ஓடுவதற்கு முன் உள்ளூர் ரகசியத்தை அமைக்கவும்:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. டோக்கனைக் கொண்டு பாதுகாக்கப்பட்ட இடைமுகத்துக்கு அணுகவும்

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" என்ற வெற்றிகரமான பதில் OAuth2 கட்டமைப்பு சரியாக இயங்குகின்றது என்பதை உறுதிப்படுத்துகிறது.

---

## கன்டெய்னர் கட்டமைப்பு

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## உற்பத்தி பாதுகாப்பு

உற்பத்தி பயன்பாட்டிற்காக, இந்த செயல்முறை டெமோ அங்கீகாரம் சேவையகத்தைவிட
தனித்த அடையாள வழங்குநரை பயன்படுத்தவும். சான்றுகளை
ரகசிய கண்காணிப்பு, அவற்றை மறு சுழற்சி செய்யவும், நிலையான கையெழுத்து விசைகள் பயன்படுத்தவும், வரம்புகளை கட்டுப்படுத்தவும்,
தெளிவான வெளியீட்டாளரை அமைக்கவும். எப்போதும் ஒரு கிளையன்ட் ரகசியத்தை மூலக் குறியீடு, கன்டெய்னர்
படங்கள், சமர்ப்பிப்பு காட்சி விவரங்கள் அல்லது கட்டளை வெளிப்பாடுகளில் இட வேண்டாம்.

ஆழூர் கன்டெய்னர் செயலிகளுக்கு, மதிப்பை இடைக்கால சேமிப்பகமாக
Key Vault ஆதரவுடன் கன்டெய்னர் செயலிகள் ரகசியமாக சேமிக்கவும், பின்னர் ரகசிய குறிப்பு மட்டும்
`OAUTH_CLIENT_SECRET` சுற்றுச் சூழல் மாறிலி மூலம் வெளிப்படுத்தவும்.

---

## **Azure Container Apps**-க்கு வருகின்றிடவும்

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

வளைய FQDN உங்கள் **வெளியீட்டாளராக** (`https://<fqdn>`) மாறும்.  
Azure க்கு `*.azurecontainerapps.io` க்கான நம்பிக்கையுடனான TLS சான்று தானாக வழங்கப்படுகிறது.

---

## **Azure API Management**-உடன் இணைக்கவும்

உங்கள் API-க்கு இந்த உள்ளே வருகின்ற கொள்கையை சேர்க்கவும்:

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

APIM JWKS ஐ பெற்று ஒவ்வொரு கோரிக்கையையும் சரிபார்க்கும்.

---

## அடுத்து என்ன

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Calculator LLM Client

GitHub Models இணைப்புடன் MCP (Model Context Protocol) கணிகையாளர் சேவையை இணைக்க LangChain4j பயன்படுத்துவதற்கான ஒரு ஜாவா பயன்பாடு.

## முன் தேவைகள்

- Java 21 அல்லது அதற்கு மேல்
- Maven 3.6+ (அல்லது சேர்க்கப்பட்ட Maven wrapper ஐ பயன்படுத்தவும்)
- GitHub Models க்கு அணுகலுடன் GitHub கணக்கு
- `http://localhost:8080` இல் இயங்கும் MCP கணிகையாளர் சேவை

## GitHub Token ஐ பெறுதல்

இந்த பயன்பாடு GitHub Models ஐ பயன்படுத்துகிறது, இது GitHub தனிப்பட்ட அணுகல் டோக்கனை தேவைப்படுகிறது. உங்கள் டோக்கனை பெற இந்த படிகளை பின்பற்றவும்:

### 1. GitHub Models ஐ அணுகுதல்
1. [GitHub Models](https://github.com/marketplace/models) க்கு செல்லவும்
2. உங்கள் GitHub கணக்குடன் உள்நுழையவும்
3. GitHub Models க்கு அணுகலை கோரவும், நீங்கள் இதுவரை கோரவில்லை என்றால்

### 2. தனிப்பட்ட அணுகல் டோக்கனை உருவாக்குதல்
1. [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens) க்கு செல்லவும்
2. "Generate new token" → "Generate new token (classic)" ஐ கிளிக் செய்யவும்
3. உங்கள் டோக்கனுக்கு விளக்கமான பெயரை கொடுக்கவும் (எ.கா., "MCP Calculator Client")
4. தேவையானபடி காலாவதியை அமைக்கவும்
5. பின்வரும் scopes ஐ தேர்ந்தெடுக்கவும்:
   - `repo` (தனிப்பட்ட repository களை அணுகும் போது)
   - `user:email`
6. "Generate token" ஐ கிளிக் செய்யவும்
7. **முக்கியம்**: டோக்கனை உடனடியாக நகலெடுக்கவும் - அதை மீண்டும் பார்க்க முடியாது!

### 3. சூழல் மாறியை அமைத்தல்

#### Windows (Command Prompt) இல்:
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell) இல்:
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux இல்:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## அமைப்பு மற்றும் நிறுவல்

1. **Project directory ஐ clone செய்யவும் அல்லது அதில் செல்லவும்**

2. **Dependencies ஐ நிறுவவும்**:
   ```cmd
   mvnw clean install
   ```
   அல்லது நீங்கள் Maven ஐ உலகளவில் நிறுவியிருந்தால்:
   ```cmd
   mvn clean install
   ```

3. **சூழல் மாறியை அமைக்கவும்** ("GitHub Token ஐ பெறுதல்" பிரிவை பார்க்கவும்)

4. **MCP கணிகையாளர் சேவையை தொடங்கவும்**:
   Chapter 1 இன் MCP கணிகையாளர் சேவை `http://localhost:8080/sse` இல் இயங்க வேண்டும். Client ஐ தொடங்குவதற்கு முன் இது இயங்க வேண்டும்.

## பயன்பாட்டை இயக்குதல்

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## பயன்பாடு என்ன செய்கிறது

இந்த பயன்பாடு கணிகையாளர் சேவையுடன் மூன்று முக்கிய தொடர்புகளை விளக்குகிறது:

1. **Addition**: 24.5 மற்றும் 17.3 இன் கூட்டுத்தொகையை கணக்கிடுகிறது
2. **Square Root**: 144 இன் வேர்க்கொறியை கணக்கிடுகிறது
3. **Help**: கிடைக்கக்கூடிய கணிகையாளர் செயல்பாடுகளை காட்டுகிறது

## எதிர்பார்க்கப்படும் வெளியீடு

வெற்றிகரமாக இயக்கும்போது, நீங்கள் பின்வருமாறு வெளியீட்டை காணலாம்:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## சிக்கல்களை தீர்க்குதல்

### பொதுவான பிரச்சினைகள்

1. **"GITHUB_TOKEN சூழல் மாறி அமைக்கப்படவில்லை"**
   - `GITHUB_TOKEN` சூழல் மாறியை அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்
   - மாறியை அமைத்த பிறகு உங்கள் terminal/command prompt ஐ மீண்டும் தொடங்கவும்

2. **"localhost:8080 க்கு இணைப்பு மறுக்கப்பட்டது"**
   - MCP கணிகையாளர் சேவை 8080 port இல் இயங்குகிறது என்பதை உறுதிப்படுத்தவும்
   - மற்றொரு சேவை 8080 port ஐ பயன்படுத்துகிறதா என்பதை சரிபார்க்கவும்

3. **"Authentication failed"**
   - உங்கள் GitHub டோக்கன் செல்லுபடியாகும் மற்றும் சரியான அனுமதிகள் உள்ளதா என்பதை சரிபார்க்கவும்
   - GitHub Models க்கு நீங்கள் அணுகலுடையவரா என்பதை சரிபார்க்கவும்

4. **Maven build errors**
   - நீங்கள் Java 21 அல்லது அதற்கு மேல் பயன்படுத்துகிறீர்கள் என்பதை உறுதிப்படுத்தவும்: `java -version`
   - Build ஐ சுத்தம் செய்ய முயற்சிக்கவும்: `mvnw clean`

### Debugging

Debug logging ஐ இயக்க, இயக்கும்போது பின்வரும் JVM argument ஐ சேர்க்கவும்:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## கட்டமைப்பு

இந்த பயன்பாடு பின்வருமாறு கட்டமைக்கப்பட்டுள்ளது:
- `gpt-4.1-nano` மாடலுடன் GitHub Models ஐ பயன்படுத்த
- MCP சேவையை `http://localhost:8080/sse` இல் இணைக்க
- கோரிக்கைகளுக்கு 60-வினாடி timeout ஐ பயன்படுத்த
- Debugging க்கு கோரிக்கை/பதில் பதிவு செய்ய

## Dependencies

இந்த திட்டத்தில் பயன்படுத்தப்படும் முக்கிய dependencies:
- **LangChain4j**: AI இணைப்பு மற்றும் கருவி மேலாண்மைக்கு
- **LangChain4j MCP**: Model Context Protocol ஆதரவுக்கு
- **LangChain4j GitHub Models**: GitHub Models இணைப்புக்கு
- **Spring Boot**: பயன்பாட்டு framework மற்றும் dependency injection க்கு

## License

இந்த திட்டம் Apache License 2.0 இன் கீழ் உரிமம் பெற்றது - விவரங்களுக்கு [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) கோப்பை பார்க்கவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
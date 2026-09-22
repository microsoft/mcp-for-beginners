# Pagrindinė skaičiuoklės MCP paslauga

> [!NOTE]
> Šis pavyzdys naudoja paveldėtą HTTP+SSE transportą ir skirtas SDK, suderinamam
> su MCP `2025-11-25`. Nauji nuotoliniai serveriai turėtų naudoti `2026-07-28` Streamable
> HTTP palaikymą.

Ši paslauga teikia pagrindines skaičiuoklės operacijas per Model Context Protocol (MCP) naudojant Spring Boot su WebFlux transportu. Ji sukurta kaip paprastas pavyzdys pradedantiesiems, mokantis apie MCP įgyvendinimus.

Daugiau informacijos žr. [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) dokumentacijoje.

## Apžvalga

Paslauga demonstruoja:
- SSE (Server-Sent Events) palaikymą
- Automatinį įrankių registravimą naudojant Spring AI `@Tool` anotaciją
- Pagrindines skaičiuoklės funkcijas:
  - Sudėjimą, atimimą, daugybą, dalybą
  - Kėlimo laipsniu ir kvadratinę šaknį
  - Modulį (likutį) ir absoliučią vertę
  - Pagalbos funkciją operacijų aprašymams

## Funkcijos

Ši skaičiuoklės paslauga siūlo šias galimybes:

1. **Pagrindinės aritmetinės operacijos**:
   - Dviejų skaičių sudėjimas
   - Vieno skaičiaus atimimas iš kito
   - Dviejų skaičių daugyba
   - Vieno skaičiaus dalijimas iš kito (su nulio patikra)

2. **Išplėstinės operacijos**:
   - Kėlimas laipsniu (bazės kėlimas į eksponentą)
   - Kvadratinės šaknies skaičiavimas (su neigiamo skaičiaus patikra)
   - Modulio (likutis) skaičiavimas
   - Absoliučios vertės skaičiavimas

3. **Pagalbos sistema**:
   - Įmontuota pagalbos funkcija, paaiškinanti visas turimas operacijas

## Paslaugos naudojimas

Paslauga per MCP protokolą teikia šiuos API taškus:

- `add(a, b)`: Sudėti du skaičius
- `subtract(a, b)`: Atimti antrą skaičių iš pirmo
- `multiply(a, b)`: Padauginti du skaičius
- `divide(a, b)`: Pirmą skaičių padalyti iš antro (su nulio patikra)
- `power(base, exponent)`: Apskaičiuoti skaičiaus laipsnį
- `squareRoot(number)`: Apskaičiuoti kvadratinę šaknį (su neigiamo patikra)
- `modulus(a, b)`: Apskaičiuoti dalybos likutį
- `absolute(number)`: Apskaičiuoti absoliučią vertę
- `help()`: Gauti informaciją apie turimas operacijas

## Testavimo klientas

Paprastas testavimo klientas yra įtrauktas į paketą `com.microsoft.mcp.sample.client`. Klasė `SampleCalculatorClient` demonstruoja turimas skaičiuoklės paslaugos operacijas.

## Naudojimasis LangChain4j klientu

Projekte yra LangChain4j pavyzdinis klientas `com.microsoft.mcp.sample.client.LangChain4jClient`, kuris demonstruoja, kaip integruoti skaičiuoklės paslaugą su LangChain4j ir GitHub modeliais:

### Prieš sąlygos

1. **GitHub žetono nustatymas**:
   
   Norėdami naudoti GitHub AI modelius (pvz., phi-4), jums reikia GitHub asmeninio prieigos žetono:

   a. Eikite į savo GitHub paskyros nustatymus: https://github.com/settings/tokens
   
   b. Spauskite "Generate new token" → "Generate new token (classic)"
   
   c. Suteikite žetonui aprašomą pavadinimą
   
   d. Pasirinkite šias apimtis:
      - `repo` (Pilnas privatų saugyklų valdymas)
      - `read:org` (Skaityti organizacijos ir komandos narių informaciją, skaityti organizacijos projektus)
      - `gist` (Kurti gist'us)
      - `user:email` (Prieiga prie vartotojo el. pašto adresų (tik skaitymui))
   
   e. Spauskite "Generate token" ir nukopijuokite naują žetoną
   
   f. Nustatykite jį kaip aplinkos kintamąjį:
      
      Windows sistemoje:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      macOS/Linux sistemose:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Norint nuolatinio nustatymo, pridėkite jį prie aplinkos kintamųjų per sistemos nustatymus

2. Pridėkite LangChain4j GitHub priklausomybę į savo projektą (jau įtraukta į pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Įsitikinkite, kad skaičiuoklės serveris veikia `localhost:8080`

### LangChain4j kliento paleidimas

Šis pavyzdys demonstruoja:
- Jungimąsi prie skaičiuoklės MCP serverio per SSE transportą
- LangChain4j naudojimą kuriant pokalbių robotą, kuris naudoja skaičiuoklės operacijas
- Integraciją su GitHub AI modeliais (dabar naudojamas phi-4 modelis)

Klientas siunčia šiuos pavyzdinius užklausimus, kad parodytų funkcionalumą:
1. Dviejų skaičių sumos skaičiavimas
2. Kvadratinės šaknies radimas
3. Pagalbos informacijos gavimas apie turimas skaičiuoklės operacijas

Paleiskite pavyzdį ir patikrinkite konsolės išvestį, kad pamatytumėte, kaip AI modelis naudoja skaičiuoklės įrankius atsakymams į užklausas.

### GitHub modelio konfigūracija

LangChain4j klientas yra sukonfigūruotas naudoti GitHub phi-4 modelį su šiais nustatymais:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Norėdami naudoti kitus GitHub modelius, tiesiog pakeiskite `modelName` parametrą į kitą palaikomą modelį (pvz., "claude-3-haiku-20240307", "llama-3-70b-8192" ir pan.).

## Priklausomybės

Projektui reikalingos šios pagrindinės priklausomybės:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Projekto statymas

Statykite projektą naudodami Maven:
```bash
./mvnw clean install -DskipTests
```

## Serverio paleidimas

### Naudojant Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Naudojantis MCP Inspector

MCP Inspector yra naudingas įrankis sąveikai su MCP paslaugomis. Norėdami jį naudoti su šia skaičiuoklės paslauga:

1. **Įdiekite ir paleiskite MCP Inspector** naujame terminalo lange:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Prisijunkite prie žiniatinklio sąsajos** spustelėdami programos parodytą URL (dažniausiai http://localhost:6274)

3. **Sukonfigūruokite ryšį**:
   - Nustatykite transporto tipą "SSE"
   - Nustatykite savo veikiančio serverio SSE URL: `http://localhost:8080/sse`
   - Spauskite "Connect"

4. **Naudokite įrankius**:
   - Spustelėkite "List Tools", kad pamatytumėte turimas skaičiuoklės operacijas
   - Pasirinkite įrankį ir spustelėkite "Run Tool", kad vykdytumėte operaciją

![MCP Inspector ekrano nuotrauka](../../../../../../translated_images/lt/tool.c75a0b2380efcf1a.webp)

### Naudojimasis Docker

Projekte yra Dockerfile konteinerinei diegčiai:

1. **Sukurkite Docker atvaizdą**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Paleiskite Docker konteinerį**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Tai padarys:
- Sukurs daugiasluoksnį Docker atvaizdą su Maven 3.9.9 ir Eclipse Temurin 24 JDK
- Sukurs optimizuotą konteinerio atvaizdą
- Atvers paslaugą per 8080 prievadą
- Paleis MCP skaičiuoklės paslaugą konteineryje

Kai konteineris veiks, pasiekti paslaugą bus galima adresu `http://localhost:8080`.

## Gedimų šalinimas

### Dažnos problemos su GitHub žetonu

1. **Žetono leidimų problemos**: Jei gaunate 403 Forbidden klaidą, patikrinkite, ar jūsų žetonas turi reikiamus leidimus pagal sąlygas.

2. **Žetonas nerastas**: Jei gaunate „No API key found“ klaidą, įsitikinkite, kad GITHUB_TOKEN aplinkos kintamasis yra tinkamai nustatytas.

3. **Ribojimų dažnis**: GitHub API turi užklausų ribas. Jei susiduriate su ribojimo klaida (statuso kodas 429), palaukite kelias minutes ir bandykite dar kartą.

4. **Žetono galiojimo pabaiga**: GitHub žetonai gali baigtis galiojimu. Jei po kurio laiko gaunate autentifikavimo klaidas, sugeneruokite naują žetoną ir atnaujinkite aplinkos kintamąjį.

Jei reikalinga tolesnė pagalba, žr. [LangChain4j dokumentaciją](https://github.com/langchain4j/langchain4j) arba [GitHub API dokumentaciją](https://docs.github.com/en/rest).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
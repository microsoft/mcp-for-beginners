# Pagrindinė Skaičiuotuvo MCP Paslauga

Ši paslauga teikia pagrindines skaičiuotuvo operacijas per Model Context Protocol (MCP), naudojant Spring Boot su WebFlux transportu. Ji sukurta kaip paprastas pavyzdys pradedantiesiems, norintiems susipažinti su MCP įgyvendinimu.

Daugiau informacijos rasite [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) dokumentacijoje.

## Apžvalga

Paslauga demonstruoja:
- SSE (Server-Sent Events) palaikymą
- Automatinį įrankių registravimą naudojant Spring AI `@Tool` anotaciją
- Pagrindines skaičiuotuvo funkcijas:
  - Sudėtis, atimtis, daugyba, dalyba
  - Laipsnio ir kvadratinės šaknies skaičiavimas
  - Modulis (liekana) ir absoliuti reikšmė
  - Pagalbos funkcija operacijų aprašymams

## Funkcijos

Ši skaičiuotuvo paslauga siūlo šias galimybes:

1. **Pagrindinės aritmetinės operacijos**:
   - Dviejų skaičių sudėtis
   - Vieno skaičiaus atimtis iš kito
   - Dviejų skaičių daugyba
   - Vieno skaičiaus dalyba iš kito (su nulio dalybos patikra)

2. **Pažangios operacijos**:
   - Laipsnio skaičiavimas (bazės pakėlimas laipsniu)
   - Kvadratinės šaknies skaičiavimas (su neigiamų skaičių patikra)
   - Modulio (liekamosios dalies) skaičiavimas
   - Absoliučios reikšmės skaičiavimas

3. **Pagalbos sistema**:
   - Integruota pagalbos funkcija, paaiškinanti visas galimas operacijas

## Paslaugos naudojimas

Paslauga teikia šiuos API galinius taškus per MCP protokolą:

- `add(a, b)`: Sudeda du skaičius
- `subtract(a, b)`: Atima antrą skaičių iš pirmo
- `multiply(a, b)`: Padaugina du skaičius
- `divide(a, b)`: Padalina pirmą skaičių iš antro (su nulio patikra)
- `power(base, exponent)`: Apskaičiuoja skaičiaus laipsnį
- `squareRoot(number)`: Apskaičiuoja kvadratinę šaknį (su neigiamų skaičių patikra)
- `modulus(a, b)`: Apskaičiuoja liekaną dalijant
- `absolute(number)`: Apskaičiuoja absoliučią reikšmę
- `help()`: Pateikia informaciją apie galimas operacijas

## Testavimo klientas

Paprastas testavimo klientas yra įtrauktas į `com.microsoft.mcp.sample.client` paketą. `SampleCalculatorClient` klasė demonstruoja galimas skaičiuotuvo paslaugos operacijas.

## LangChain4j Kliento Naudojimas

Projekte yra LangChain4j pavyzdinis klientas `com.microsoft.mcp.sample.client.LangChain4jClient`, kuris demonstruoja, kaip integruoti skaičiuotuvo paslaugą su LangChain4j ir GitHub modeliais:

### Reikalavimai

1. **GitHub Token Nustatymas**:
   
   Norint naudoti GitHub AI modelius (pvz., phi-4), reikia GitHub asmeninio prieigos rakto:

   a. Eikite į savo GitHub paskyros nustatymus: https://github.com/settings/tokens
   
   b. Spustelėkite "Generate new token" → "Generate new token (classic)"
   
   c. Suteikite savo raktui aprašomąjį pavadinimą
   
   d. Pasirinkite šiuos leidimus:
      - `repo` (Visiška kontrolė privačiuose repozitorijose)
      - `read:org` (Organizacijos ir komandos narystės skaitymas, projektų skaitymas)
      - `gist` (Gistų kūrimas)
      - `user:email` (Prieiga prie vartotojo el. pašto adresų (tik skaitymas))
   
   e. Spustelėkite "Generate token" ir nukopijuokite savo naują raktą
   
   f. Nustatykite jį kaip aplinkos kintamąjį:
      
      Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Norėdami nustatyti nuolat, pridėkite jį prie savo sistemos aplinkos kintamųjų nustatymų

2. Pridėkite LangChain4j GitHub priklausomybę prie savo projekto (jau įtraukta į pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Įsitikinkite, kad skaičiuotuvo serveris veikia `localhost:8080`

### LangChain4j Kliento Paleidimas

Šis pavyzdys demonstruoja:
- Prisijungimą prie skaičiuotuvo MCP serverio per SSE transportą
- LangChain4j naudojimą kuriant pokalbių robotą, kuris naudoja skaičiuotuvo operacijas
- Integraciją su GitHub AI modeliais (šiuo metu naudojamas phi-4 modelis)

Klientas siunčia šiuos pavyzdinius užklausimus, kad parodytų funkcionalumą:
1. Dviejų skaičių sumos skaičiavimas
2. Skaičiaus kvadratinės šaknies radimas
3. Pagalbos informacijos apie galimas skaičiuotuvo operacijas gavimas

Paleiskite pavyzdį ir patikrinkite konsolės išvestį, kad pamatytumėte, kaip AI modelis naudoja skaičiuotuvo įrankius atsakymams pateikti.

### GitHub Modelio Konfigūracija

LangChain4j klientas sukonfigūruotas naudoti GitHub phi-4 modelį su šiais nustatymais:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Norėdami naudoti kitus GitHub modelius, tiesiog pakeiskite `modelName` parametrą į kitą palaikomą modelį (pvz., "claude-3-haiku-20240307", "llama-3-70b-8192" ir kt.).

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

## Projekto Kūrimas

Sukurkite projektą naudodami Maven:
```bash
./mvnw clean install -DskipTests
```

## Serverio Paleidimas

### Naudojant Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Naudojant MCP Inspector

MCP Inspector yra naudingas įrankis sąveikai su MCP paslaugomis. Norėdami jį naudoti su šia skaičiuotuvo paslauga:

1. **Įdiekite ir paleiskite MCP Inspector** naujame terminalo lange:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pasiekite internetinę sąsają** spustelėdami programos rodomą URL (dažniausiai http://localhost:6274)

3. **Sukonfigūruokite ryšį**:
   - Nustatykite transporto tipą į "SSE"
   - Nustatykite URL į savo veikiančio serverio SSE galinį tašką: `http://localhost:8080/sse`
   - Spustelėkite "Connect"

4. **Naudokite įrankius**:
   - Spustelėkite "List Tools", kad pamatytumėte galimas skaičiuotuvo operacijas
   - Pasirinkite įrankį ir spustelėkite "Run Tool", kad vykdytumėte operaciją

![MCP Inspector Ekrano Nuotrauka](../../../../../../translated_images/lt/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### Naudojant Docker

Projektas apima Dockerfile konteinerizuotam diegimui:

1. **Sukurkite Docker atvaizdą**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Paleiskite Docker konteinerį**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Tai:
- Sukurs kelių etapų Docker atvaizdą su Maven 3.9.9 ir Eclipse Temurin 24 JDK
- Sukurs optimizuotą konteinerio atvaizdą
- Atvers paslaugą 8080 prievade
- Paleis MCP skaičiuotuvo paslaugą konteineryje

Kai konteineris veiks, paslaugą galėsite pasiekti adresu `http://localhost:8080`.

## Trikčių Šalinimas

### Dažnos Problemos su GitHub Raktu

1. **Raktų Leidimų Problemos**: Jei gaunate 403 Forbidden klaidą, patikrinkite, ar jūsų raktas turi tinkamus leidimus, kaip nurodyta reikalavimuose.

2. **Raktas Nerastas**: Jei gaunate "No API key found" klaidą, įsitikinkite, kad GITHUB_TOKEN aplinkos kintamasis tinkamai nustatytas.

3. **Kvietimų Limitas**: GitHub API turi kvietimų limitus. Jei susiduriate su limito klaida (statuso kodas 429), palaukite kelias minutes prieš bandydami dar kartą.

4. **Rakto Galiojimo Pabaiga**: GitHub raktai gali baigti galioti. Jei po kurio laiko gaunate autentifikavimo klaidas, sugeneruokite naują raktą ir atnaujinkite savo aplinkos kintamąjį.

Jei reikia papildomos pagalbos, peržiūrėkite [LangChain4j dokumentaciją](https://github.com/langchain4j/langchain4j) arba [GitHub API dokumentaciją](https://docs.github.com/en/rest).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.
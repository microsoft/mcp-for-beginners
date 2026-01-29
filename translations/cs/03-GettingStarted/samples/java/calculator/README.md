# Základní kalkulační MCP služba

Tato služba poskytuje základní kalkulační operace prostřednictvím Model Context Protocol (MCP) pomocí Spring Boot s WebFlux transportem. Je navržena jako jednoduchý příklad pro začátečníky, kteří se učí o implementacích MCP.

Pro více informací si přečtěte referenční dokumentaci [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).

## Přehled

Služba ukazuje:
- Podporu SSE (Server-Sent Events)
- Automatickou registraci nástrojů pomocí anotace `@Tool` ze Spring AI
- Základní kalkulační funkce:
  - Sčítání, odčítání, násobení, dělení
  - Výpočet mocniny a druhé odmocniny
  - Modulo (zbytek po dělení) a absolutní hodnota
  - Nápověda k popisu operací

## Funkce

Tato kalkulační služba nabízí následující možnosti:

1. **Základní aritmetické operace**:
   - Sčítání dvou čísel
   - Odčítání jednoho čísla od druhého
   - Násobení dvou čísel
   - Dělení jednoho čísla druhým (s kontrolou dělení nulou)

2. **Pokročilé operace**:
   - Výpočet mocniny (základ na exponent)
   - Výpočet druhé odmocniny (s kontrolou záporného čísla)
   - Výpočet zbytku po dělení (modulo)
   - Výpočet absolutní hodnoty

3. **Nápovědní systém**:
   - Vestavěná funkce nápovědy vysvětlující všechny dostupné operace

## Použití služby

Služba zpřístupňuje následující API endpointy přes MCP protokol:

- `add(a, b)`: Sečte dvě čísla
- `subtract(a, b)`: Odečte druhé číslo od prvního
- `multiply(a, b)`: Vynásobí dvě čísla
- `divide(a, b)`: Vydělí první číslo druhým (s kontrolou dělení nulou)
- `power(base, exponent)`: Vypočítá mocninu čísla
- `squareRoot(number)`: Vypočítá druhou odmocninu (s kontrolou záporného čísla)
- `modulus(a, b)`: Vypočítá zbytek po dělení
- `absolute(number)`: Vypočítá absolutní hodnotu
- `help()`: Získá informace o dostupných operacích

## Testovací klient

Jednoduchý testovací klient je součástí balíčku `com.microsoft.mcp.sample.client`. Třída `SampleCalculatorClient` demonstruje dostupné operace kalkulační služby.

## Použití LangChain4j klienta

Projekt obsahuje příklad klienta LangChain4j v `com.microsoft.mcp.sample.client.LangChain4jClient`, který ukazuje, jak integrovat kalkulační službu s LangChain4j a GitHub modely:

### Požadavky

1. **Nastavení GitHub tokenu**:
   
   Pro použití AI modelů GitHubu (např. phi-4) potřebujete osobní přístupový token GitHub:

   a. Přejděte do nastavení svého GitHub účtu: https://github.com/settings/tokens
   
   b. Klikněte na "Generate new token" → "Generate new token (classic)"
   
   c. Pojmenujte token popisným názvem
   
   d. Vyberte následující oprávnění:
      - `repo` (plná kontrola nad soukromými repozitáři)
      - `read:org` (čtení členství v organizacích a týmech, čtení projektů organizace)
      - `gist` (vytváření gistů)
      - `user:email` (přístup k e-mailovým adresám uživatele (pouze pro čtení))
   
   e. Klikněte na "Generate token" a zkopírujte nový token
   
   f. Nastavte ho jako proměnnou prostředí:
      
      Na Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      Na macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Pro trvalé nastavení přidejte token do systémových proměnných prostředí

2. Přidejte závislost LangChain4j GitHub do svého projektu (již zahrnuto v pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Ujistěte se, že kalkulační server běží na `localhost:8080`

### Spuštění LangChain4j klienta

Tento příklad ukazuje:
- Připojení ke kalkulačnímu MCP serveru přes SSE transport
- Použití LangChain4j k vytvoření chatbota využívajícího kalkulační operace
- Integraci s GitHub AI modely (nyní používá model phi-4)

Klient odesílá následující ukázkové dotazy pro demonstraci funkcí:
1. Výpočet součtu dvou čísel
2. Výpočet druhé odmocniny čísla
3. Získání nápovědy o dostupných kalkulačních operacích

Spusťte příklad a sledujte výstup v konzoli, abyste viděli, jak AI model využívá kalkulační nástroje k odpovědím.

### Konfigurace GitHub modelu

LangChain4j klient je nastaven pro použití GitHub modelu phi-4 s následujícími parametry:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Pro použití jiných GitHub modelů stačí změnit parametr `modelName` na jiný podporovaný model (např. "claude-3-haiku-20240307", "llama-3-70b-8192" atd.).

## Závislosti

Projekt vyžaduje následující klíčové závislosti:

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

## Sestavení projektu

Projekt sestavíte pomocí Maven:
```bash
./mvnw clean install -DskipTests
```

## Spuštění serveru

### Použití Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Použití MCP Inspectoru

MCP Inspector je užitečný nástroj pro práci s MCP službami. Pro použití s touto kalkulační službou:

1. **Nainstalujte a spusťte MCP Inspector** v novém terminálovém okně:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Přistupte k webovému rozhraní** kliknutím na URL zobrazenou aplikací (obvykle http://localhost:6274)

3. **Nastavte připojení**:
   - Zvolte typ transportu "SSE"
   - Nastavte URL na SSE endpoint běžícího serveru: `http://localhost:8080/sse`
   - Klikněte na "Connect"

4. **Používejte nástroje**:
   - Klikněte na "List Tools" pro zobrazení dostupných kalkulačních operací
   - Vyberte nástroj a klikněte na "Run Tool" pro spuštění operace

![MCP Inspector Screenshot](../../../../../../translated_images/cs/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### Použití Dockeru

Projekt obsahuje Dockerfile pro nasazení v kontejneru:

1. **Sestavte Docker image**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Spusťte Docker kontejner**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Tímto se:
- Sestaví multi-stage Docker image s Mavenem 3.9.9 a Eclipse Temurin 24 JDK
- Vytvoří optimalizovaný kontejnerový image
- Otevře port 8080 pro službu
- Spustí MCP kalkulační službu uvnitř kontejneru

Službu pak můžete používat na `http://localhost:8080`, jakmile kontejner poběží.

## Řešení problémů

### Běžné problémy s GitHub tokenem

1. **Problémy s oprávněními tokenu**: Pokud dostanete chybu 403 Forbidden, zkontrolujte, zda má token správná oprávnění podle požadavků výše.

2. **Token nenalezen**: Pokud se zobrazí chyba "No API key found", ujistěte se, že proměnná prostředí GITHUB_TOKEN je správně nastavena.

3. **Omezení počtu požadavků**: GitHub API má limity na počet požadavků. Pokud narazíte na chybu limitu (kód 429), počkejte několik minut a zkuste to znovu.

4. **Vypršení platnosti tokenu**: GitHub tokeny mohou vypršet. Pokud po čase dostáváte chyby autentizace, vygenerujte nový token a aktualizujte proměnnou prostředí.

Pokud potřebujete další pomoc, podívejte se do [dokumentace LangChain4j](https://github.com/langchain4j/langchain4j) nebo [dokumentace GitHub API](https://docs.github.com/en/rest).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
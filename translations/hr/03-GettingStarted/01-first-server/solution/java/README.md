# Osnovna MCP usluga kalkulatora

> [!NOTE]
> Ovo Java rješenje koristi naslijeđeni HTTP+SSE transport i cilja SDK
> kompatibilan s MCP `2025-11-25`. Zadržano je za podudaranje s kodom tečaja;
> novi udaljeni poslužitelji trebali bi koristiti `2026-07-28` Streamable HTTP podršku.

Ova usluga pruža osnovne operacije kalkulatora putem Model Context Protocol (MCP) koristeći Spring Boot s WebFlux transportom. Osmišljena je kao jednostavan primjer za početnike koji uče o MCP implementacijama.

Za više informacija, pogledajte [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) referentnu dokumentaciju.


## Korištenje usluge

Usluga izlaže sljedeće API krajnje točke putem MCP protokola:

- `add(a, b)`: Zbrojiti dva broja
- `subtract(a, b)`: Oduzeti drugi broj od prvog
- `multiply(a, b)`: Pomnožiti dva broja
- `divide(a, b)`: Podijeliti prvi broj s drugim (s provjerom na nulu)
- `power(base, exponent)`: Izračunati potenciju broja
- `squareRoot(number)`: Izračunati kvadratni korijen (s provjerom na negativan broj)
- `modulus(a, b)`: Izračunati ostatak dijeljenja
- `absolute(number)`: Izračunati apsolutnu vrijednost

## Ovisnosti

Projekt zahtijeva sljedeće ključne ovisnosti:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Izrada projekta

Izradite projekt pomoću Mavena:
```bash
./mvnw clean install -DskipTests
```

## Pokretanje poslužitelja

### Korištenje Jave

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Korištenje MCP Inspektora

MCP Inspektor je koristan alat za interakciju s MCP uslugama. Za korištenje s ovom uslugom kalkulatora:

1. **Instalirajte i pokrenite MCP Inspektor** u novom terminal prozoru:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pristupite web korisničkom sučelju** klikom na URL koji aplikacija prikazuje (obično http://localhost:6274)

3. **Konfigurirajte vezu**:
   - Postavite tip transporta na "SSE"
   - Postavite URL na vaš aktivni SSE endpoint poslužitelja: `http://localhost:8080/sse`
   - Kliknite "Connect"

4. **Koristite alate**:
   - Kliknite "List Tools" za pregled dostupnih operacija kalkulatora
   - Odaberite alat i kliknite "Run Tool" za izvršenje operacije

![MCP Inspector Screenshot](../../../../../../translated_images/hr/tool.40e180a7b0d0fe20.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
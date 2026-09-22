# Basis Calculator MCP Service

> [!NOTE]
> Deze Java-oplossing gebruikt het legacy HTTP+SSE transport en is gericht op een SDK
> compatibel met MCP `2025-11-25`. Het wordt behouden voor overeenkomende cursuscode;
> nieuwe externe servers moeten `2026-07-28` Streamable HTTP-ondersteuning gebruiken.

Deze service biedt basis rekenmachineoperaties via het Model Context Protocol (MCP) met Spring Boot en WebFlux transport. Het is ontworpen als een eenvoudig voorbeeld voor beginners die MCP-implementaties leren.

Voor meer informatie, zie de [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) referentiedocumentatie.


## Gebruik van de Service

De service exposeert de volgende API-eindpunten via het MCP-protocol:

- `add(a, b)`: Tel twee getallen bij elkaar op
- `subtract(a, b)`: Trek het tweede getal af van het eerste
- `multiply(a, b)`: Vermenigvuldig twee getallen
- `divide(a, b)`: Deel het eerste getal door het tweede (met nultoets)
- `power(base, exponent)`: Bereken de macht van een getal
- `squareRoot(number)`: Bereken de wortel (met controle op negatieve getallen)
- `modulus(a, b)`: Bereken de rest bij deling
- `absolute(number)`: Bereken de absolute waarde

## Afhankelijkheden

Het project vereist de volgende belangrijkste afhankelijkheden:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Project Bouwen

Bouw het project met Maven:
```bash
./mvnw clean install -DskipTests
```

## Server Starten

### Met Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Met MCP Inspector

De MCP Inspector is een handig gereedschap voor interactie met MCP services. Om het te gebruiken met deze calculator service:

1. **Installeer en start MCP Inspector** in een nieuw terminalvenster:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Open de webinterface** door te klikken op de URL die de app toont (meestal http://localhost:6274)

3. **Configureer de verbinding**:
   - Stel het transporttype in op "SSE"
   - Stel de URL in naar het SSE-eindpunt van je draaiende server: `http://localhost:8080/sse`
   - Klik op "Connect"

4. **Gebruik de tools**:
   - Klik op "List Tools" om beschikbare rekenmachineoperaties te bekijken
   - Selecteer een tool en klik op "Run Tool" om een operatie uit te voeren

![MCP Inspector Screenshot](../../../../../../translated_images/nl/tool.40e180a7b0d0fe20.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
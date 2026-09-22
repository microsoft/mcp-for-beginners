# Serviciul de Calculator de Bază MCP

> [!NOTE]
> Această soluție Java utilizează transportul HTTP+SSE moștenit și țintește un SDK
> compatibil cu MCP `2025-11-25`. Este păstrată pentru a se potrivi cu codul cursului;
> noile servere la distanță ar trebui să folosească suportul HTTP Streamable `2026-07-28`.

Acest serviciu oferă operații de calculator de bază prin Model Context Protocol (MCP) folosind Spring Boot cu transport WebFlux. Este conceput ca un exemplu simplu pentru începătorii care învață despre implementările MCP.

Pentru mai multe informații, consultați documentația de referință [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).


## Utilizarea Serviciului

Serviciul expune următoarele endpoint-uri API prin protocolul MCP:

- `add(a, b)`: Adună două numere
- `subtract(a, b)`: Scade al doilea număr din primul
- `multiply(a, b)`: Înmulțește două numere
- `divide(a, b)`: Împarte primul număr la al doilea (cu verificare pentru zero)
- `power(base, exponent)`: Calculează puterea unui număr
- `squareRoot(number)`: Calculează rădăcina pătrată (cu verificare pentru număr negativ)
- `modulus(a, b)`: Calculează restul împărțirii
- `absolute(number)`: Calculează valoarea absolută

## Dependențe

Proiectul necesită următoarele dependențe majore:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Construirea Proiectului

Construiește proiectul utilizând Maven:
```bash
./mvnw clean install -DskipTests
```

## Rularea Serverului

### Utilizând Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Utilizând MCP Inspector

MCP Inspector este un instrument util pentru interacțiunea cu serviciile MCP. Pentru a-l folosi cu acest serviciu de calculator:

1. **Instalează și rulează MCP Inspector** într-o fereastră terminal nouă:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Accesează interfața web** făcând clic pe URL-ul afișat de aplicație (de obicei http://localhost:6274)

3. **Configurează conexiunea**:
   - Setează tipul de transport la "SSE"
   - Setează URL-ul către endpoint-ul SSE al serverului tău în funcțiune: `http://localhost:8080/sse`
   - Click pe "Connect"

4. **Folosește uneltele**:
   - Click pe "List Tools" pentru a vedea operațiile de calculator disponibile
   - Selectează o unealtă și click pe "Run Tool" pentru a executa o operație

![MCP Inspector Screenshot](../../../../../../translated_images/ro/tool.40e180a7b0d0fe20.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
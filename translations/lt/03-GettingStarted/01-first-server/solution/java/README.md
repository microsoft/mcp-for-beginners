# Pagrindinė skaičiuoklės MCP paslauga

Ši paslauga teikia pagrindines skaičiuoklės operacijas per Model Context Protocol (MCP), naudojant Spring Boot su WebFlux transportu. Ji sukurta kaip paprastas pavyzdys pradedantiesiems, norintiems išmokti apie MCP įgyvendinimus.

Daugiau informacijos rasite [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) dokumentacijoje.

## Paslaugos naudojimas

Paslauga per MCP protokolą pateikia šiuos API galinius taškus:

- `add(a, b)`: Sudeda du skaičius
- `subtract(a, b)`: Atima antrą skaičių iš pirmojo
- `multiply(a, b)`: Padaugina du skaičius
- `divide(a, b)`: Padalija pirmą skaičių iš antrojo (su nulio patikra)
- `power(base, exponent)`: Apskaičiuoja skaičiaus laipsnį
- `squareRoot(number)`: Apskaičiuoja kvadratinę šaknį (su neigiamo skaičiaus patikra)
- `modulus(a, b)`: Apskaičiuoja likutį dalijant
- `absolute(number)`: Apskaičiuoja absoliučią vertę

## Priklausomybės

Projektui reikalingos šios pagrindinės priklausomybės:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Projekto kūrimas

Sukurkite projektą naudodami Maven:
```bash
./mvnw clean install -DskipTests
```

## Serverio paleidimas

### Naudojant Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Naudojant MCP Inspector

MCP Inspector yra naudingas įrankis, skirtas sąveikai su MCP paslaugomis. Norėdami jį naudoti su šia skaičiuoklės paslauga:

1. **Įdiekite ir paleiskite MCP Inspector** naujame terminalo lange:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pasiekite internetinę sąsają**, paspausdami programos rodomą URL (dažniausiai http://localhost:6274)

3. **Konfigūruokite ryšį**:
   - Nustatykite transporto tipą kaip "SSE"
   - Nurodykite savo veikiančio serverio SSE galinio taško URL: `http://localhost:8080/sse`
   - Paspauskite "Connect"

4. **Naudokitės įrankiais**:
   - Paspauskite "List Tools", kad pamatytumėte galimas skaičiuoklės operacijas
   - Pasirinkite įrankį ir paspauskite "Run Tool", kad įvykdytumėte operaciją

![MCP Inspector ekrano nuotrauka](../../../../../../translated_images/lt/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.
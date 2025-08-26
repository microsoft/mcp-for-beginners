<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed9cab32cc67c12d8969b407aa47100a",
  "translation_date": "2025-08-26T16:45:54+00:00",
  "source_file": "03-GettingStarted/01-first-server/solution/java/README.md",
  "language_code": "lt"
}
-->
# Pagrindinė skaičiuoklės MCP paslauga

Ši paslauga teikia pagrindines skaičiuoklės operacijas per Model Context Protocol (MCP), naudojant Spring Boot su WebFlux transportu. Ji sukurta kaip paprastas pavyzdys pradedantiesiems, norintiems išmokti apie MCP įgyvendinimus.

Daugiau informacijos rasite [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) dokumentacijoje.

## Paslaugos naudojimas

Paslauga per MCP protokolą pateikia šiuos API galinius taškus:

- `add(a, b)`: Sudėti du skaičius
- `subtract(a, b)`: Atimti antrą skaičių iš pirmo
- `multiply(a, b)`: Padauginti du skaičius
- `divide(a, b)`: Padalyti pirmą skaičių iš antro (su nulio patikra)
- `power(base, exponent)`: Apskaičiuoti skaičiaus laipsnį
- `squareRoot(number)`: Apskaičiuoti kvadratinę šaknį (su neigiamo skaičiaus patikra)
- `modulus(a, b)`: Apskaičiuoti likutį dalijant
- `absolute(number)`: Apskaičiuoti absoliučią vertę

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

2. **Pasiekite internetinę sąsają** spustelėdami programos rodomą URL (dažniausiai http://localhost:6274)

3. **Konfigūruokite ryšį**:
   - Nustatykite transporto tipą kaip "SSE"
   - Nurodykite URL į jūsų veikiančio serverio SSE galinį tašką: `http://localhost:8080/sse`
   - Spustelėkite "Connect"

4. **Naudokitės įrankiais**:
   - Spustelėkite "List Tools", kad pamatytumėte galimas skaičiuoklės operacijas
   - Pasirinkite įrankį ir spustelėkite "Run Tool", kad įvykdytumėte operaciją

![MCP Inspector ekrano nuotrauka](../../../../../../translated_images/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.lt.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
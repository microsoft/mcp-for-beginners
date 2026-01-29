# Mifano Kamili za Wateja wa MCP

Hili jalada lina mifano kamili na inayofanya kazi ya wateja wa MCP katika lugha mbalimbali za programu. Kila mteja anaonyesha utendaji wote ulioelezwa katika mafunzo ya README.md kuu.

## Wateja Waliopo

### 1. Mteja wa Java (`client_example_java.java`)

- **Usafirishaji**: SSE (Matukio Yanayotumwa na Seva) kupitia HTTP
- **Seva Lengwa**: `http://localhost:8080`
- **Vipengele**:
  - Kuanzisha muunganisho na ping
  - Orodha ya zana
  - Operesheni za kikokotoo (kujumlisha, kutoa, kuzidisha, kugawa, msaada)
  - Kushughulikia makosa na uchimbaji wa matokeo

**Kukimbia:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Mteja wa C# (`client_example_csharp.cs`)

- **Usafirishaji**: Stdio (Ingizo/Toleo la Kawaida)
- **Seva Lengwa**: Seva ya MCP ya .NET ya ndani kupitia dotnet run
- **Vipengele**:
  - Kuanza seva kiotomatiki kupitia usafirishaji wa stdio
  - Orodha ya zana na rasilimali
  - Operesheni za kikokotoo
  - Kuchambua matokeo ya JSON
  - Kushughulikia makosa kwa kina

**Kukimbia:**

```bash
dotnet run
```

### 3. Mteja wa TypeScript (`client_example_typescript.ts`)

- **Usafirishaji**: Stdio (Ingizo/Toleo la Kawaida)
- **Seva Lengwa**: Seva ya MCP ya Node.js ya ndani
- **Vipengele**:
  - Msaada kamili wa itifaki ya MCP
  - Operesheni za zana, rasilimali, na maelekezo
  - Operesheni za kikokotoo
  - Kusoma rasilimali na kutekeleza maelekezo
  - Kushughulikia makosa kwa nguvu

**Kukimbia:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Mteja wa Python (`client_example_python.py`)

- **Usafirishaji**: Stdio (Ingizo/Toleo la Kawaida)  
- **Seva Lengwa**: Seva ya MCP ya Python ya ndani
- **Vipengele**:
  - Muundo wa async/await kwa operesheni
  - Kugundua zana na rasilimali
  - Kupima operesheni za kikokotoo
  - Kusoma maudhui ya rasilimali
  - Mpangilio wa msingi wa darasa

**Kukimbia:**

```bash
python client_example_python.py
```

## Vipengele vya Kawaida Kati ya Wateja Wote

Kila utekelezaji wa mteja unaonyesha:

1. **Usimamizi wa Muunganisho**
   - Kuanzisha muunganisho na seva ya MCP
   - Kushughulikia makosa ya muunganisho
   - Usimamizi sahihi wa rasilimali na kusafisha

2. **Ugunduzi wa Seva**
   - Kuorodhesha zana zinazopatikana
   - Kuorodhesha rasilimali zinazopatikana (ikiwa zinasaidiwa)
   - Kuorodhesha maelekezo yanayopatikana (ikiwa yanasaidiwa)

3. **Utekelezaji wa Zana**
   - Operesheni za msingi za kikokotoo (kujumlisha, kutoa, kuzidisha, kugawa)
   - Amri ya msaada kwa taarifa za seva
   - Uwasilishaji sahihi wa hoja na kushughulikia matokeo

4. **Kushughulikia Makosa**
   - Makosa ya muunganisho
   - Makosa ya utekelezaji wa zana
   - Kushindwa kwa neema na maoni kwa mtumiaji

5. **Usindikaji wa Matokeo**
   - Kuchimba maudhui ya maandishi kutoka kwa majibu
   - Kuweka muundo wa matokeo kwa usomaji rahisi
   - Kushughulikia miundo tofauti ya majibu

## Mahitaji

Kabla ya kukimbia wateja hawa, hakikisha una:

1. **Seva ya MCP inayolingana inayoendesha** (kutoka `../01-first-server/`)
2. **Vitegemezi vinavyohitajika vimesakinishwa** kwa lugha uliyochagua
3. **Muunganisho sahihi wa mtandao** (kwa usafirishaji unaotegemea HTTP)

## Tofauti Muhimu Kati ya Utekelezaji

| Lugha       | Usafirishaji | Kuanza Seva   | Muundo wa Async | Maktaba Muhimu       |
|-------------|-------------|---------------|-----------------|---------------------|
| Java        | SSE/HTTP    | Nje           | Synkroni        | WebFlux, MCP SDK    |
| C#          | Stdio       | Kiotomatiki   | Async/Await     | .NET MCP SDK        |
| TypeScript  | Stdio       | Kiotomatiki   | Async/Await     | Node MCP SDK        |
| Python      | Stdio       | Kiotomatiki   | AsyncIO         | Python MCP SDK      |
| Rust        | Stdio       | Kiotomatiki   | Async/Await     | Rust MCP SDK, Tokio |

## Hatua Zifuatazo

Baada ya kuchunguza mifano hii ya wateja:

1. **Badilisha wateja** ili kuongeza vipengele au operesheni mpya
2. **Unda seva yako mwenyewe** na uijaribu na wateja hawa
3. **Jaribu usafirishaji tofauti** (SSE dhidi ya Stdio)
4. **Jenga programu ngumu zaidi** inayojumuisha utendaji wa MCP

## Kutatua Tatizo

### Masuala ya Kawaida

1. **Muunganisho umekataliwa**: Hakikisha seva ya MCP inaendesha kwenye bandari/njia inayotarajiwa
2. **Moduli haikupatikana**: Sakinisha MCP SDK inayohitajika kwa lugha yako
3. **Ruhusa imekataliwa**: Angalia ruhusa za faili kwa usafirishaji wa stdio
4. **Zana haikupatikana**: Thibitisha seva inatekeleza zana zinazotarajiwa

### Vidokezo vya Urekebishaji

1. **Washa ufuatiliaji wa kina** katika MCP SDK yako
2. **Angalia kumbukumbu za seva** kwa ujumbe wa makosa
3. **Thibitisha majina ya zana na saini** yanalingana kati ya mteja na seva
4. **Jaribu na MCP Inspector** kwanza ili kuthibitisha utendaji wa seva

## Nyaraka Zinazohusiana

- [Mafunzo Makuu ya Mteja](./README.md)
- [Mifano ya Seva ya MCP](../../../../03-GettingStarted/01-first-server)
- [MCP na Muunganisho wa LLM](../../../../03-GettingStarted/03-llm-client)
- [Nyaraka Rasmi za MCP](https://modelcontextprotocol.io/)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
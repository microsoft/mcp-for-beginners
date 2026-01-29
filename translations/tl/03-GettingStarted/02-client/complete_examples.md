# Kumpletong Halimbawa ng MCP Client

Ang direktoryong ito ay naglalaman ng mga kumpleto at gumaganang halimbawa ng MCP clients sa iba't ibang programming languages. Ang bawat client ay nagpapakita ng buong functionality na inilarawan sa pangunahing tutorial na README.md.

## Mga Available na Client

### 1. Java Client (`client_example_java.java`)

- **Transportasyon**: SSE (Server-Sent Events) gamit ang HTTP
- **Target na Server**: `http://localhost:8080`
- **Mga Tampok**:
  - Pagbuo ng koneksyon at ping
  - Paglista ng mga tool
  - Mga operasyon sa calculator (add, subtract, multiply, divide, help)
  - Paghawak ng error at pagkuha ng resulta

**Paano patakbuhin:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# Client (`client_example_csharp.cs`)

- **Transportasyon**: Stdio (Standard Input/Output)
- **Target na Server**: Lokal na .NET MCP server gamit ang dotnet run
- **Mga Tampok**:
  - Awtomatikong pagsisimula ng server gamit ang stdio transport
  - Paglista ng mga tool at resource
  - Mga operasyon sa calculator
  - JSON result parsing
  - Komprehensibong paghawak ng error

**Paano patakbuhin:**

```bash
dotnet run
```

### 3. TypeScript Client (`client_example_typescript.ts`)

- **Transportasyon**: Stdio (Standard Input/Output)
- **Target na Server**: Lokal na Node.js MCP server
- **Mga Tampok**:
  - Buong suporta sa MCP protocol
  - Mga operasyon sa tool, resource, at prompt
  - Mga operasyon sa calculator
  - Pagbasa ng resource at pagpapatupad ng prompt
  - Matibay na paghawak ng error

**Paano patakbuhin:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python Client (`client_example_python.py`)

- **Transportasyon**: Stdio (Standard Input/Output)  
- **Target na Server**: Lokal na Python MCP server
- **Mga Tampok**:
  - Async/await na pattern para sa mga operasyon
  - Pagdiskubre ng mga tool at resource
  - Pagsubok sa mga operasyon ng calculator
  - Pagbasa ng nilalaman ng resource
  - Organisasyon gamit ang klase

**Paano patakbuhin:**

```bash
python client_example_python.py
```

## Karaniwang Tampok sa Lahat ng Client

Ang bawat implementasyon ng client ay nagpapakita ng:

1. **Pamamahala ng Koneksyon**
   - Pagbuo ng koneksyon sa MCP server
   - Paghawak ng mga error sa koneksyon
   - Wastong paglilinis at pamamahala ng resource

2. **Pagdiskubre ng Server**
   - Paglista ng mga available na tool
   - Paglista ng mga available na resource (kung sinusuportahan)
   - Paglista ng mga available na prompt (kung sinusuportahan)

3. **Pagpapatupad ng Tool**
   - Mga pangunahing operasyon sa calculator (add, subtract, multiply, divide)
   - Help command para sa impormasyon ng server
   - Wastong pagpasa ng argumento at paghawak ng resulta

4. **Paghawak ng Error**
   - Mga error sa koneksyon
   - Mga error sa pagpapatupad ng tool
   - Maayos na paghawak ng pagkabigo at pagbibigay ng feedback sa user

5. **Pagproseso ng Resulta**
   - Pagkuha ng text content mula sa mga tugon
   - Pag-format ng output para sa mas madaling basahin
   - Paghawak ng iba't ibang format ng tugon

## Mga Kinakailangan

Bago patakbuhin ang mga client na ito, tiyakin na mayroon ka ng:

1. **Tumatakbong MCP server** (mula sa `../01-first-server/`)
2. **Mga kinakailangang dependency na naka-install** para sa napiling wika
3. **Wastong koneksyon sa network** (para sa mga transportasyon na nakabatay sa HTTP)

## Pangunahing Pagkakaiba sa Bawat Implementasyon

| Wika       | Transportasyon | Pagsisimula ng Server | Async Model | Pangunahing Libraries       |
|------------|----------------|-----------------------|-------------|-----------------------------|
| Java       | SSE/HTTP       | External              | Sync        | WebFlux, MCP SDK            |
| C#         | Stdio          | Awtomatiko            | Async/Await | .NET MCP SDK                |
| TypeScript | Stdio          | Awtomatiko            | Async/Await | Node MCP SDK                |
| Python     | Stdio          | Awtomatiko            | AsyncIO     | Python MCP SDK              |
| Rust       | Stdio          | Awtomatiko            | Async/Await | Rust MCP SDK, Tokio         |

## Mga Susunod na Hakbang

Pagkatapos tuklasin ang mga halimbawa ng client na ito:

1. **I-modify ang mga client** upang magdagdag ng mga bagong tampok o operasyon
2. **Gumawa ng sarili mong server** at subukan ito gamit ang mga client na ito
3. **Mag-eksperimento sa iba't ibang transportasyon** (SSE vs. Stdio)
4. **Bumuo ng mas kumplikadong aplikasyon** na may integrasyon ng MCP functionality

## Pag-aayos ng Problema

### Karaniwang Isyu

1. **Connection refused**: Siguraduhing tumatakbo ang MCP server sa inaasahang port/path
2. **Module not found**: I-install ang kinakailangang MCP SDK para sa iyong wika
3. **Permission denied**: Suriin ang mga pahintulot ng file para sa stdio transport
4. **Tool not found**: Tiyaking ang server ay may implementasyon ng inaasahang mga tool

### Mga Tip sa Pag-debug

1. **I-enable ang verbose logging** sa iyong MCP SDK
2. **Suriin ang mga log ng server** para sa mga mensahe ng error
3. **Siguraduhin ang mga pangalan at lagda ng tool** ay tumutugma sa pagitan ng client at server
4. **Subukan gamit ang MCP Inspector** upang i-validate ang functionality ng server

## Kaugnay na Dokumentasyon

- [Pangunahing Tutorial ng Client](./README.md)
- [Mga Halimbawa ng MCP Server](../../../../03-GettingStarted/01-first-server)
- [MCP na may LLM Integration](../../../../03-GettingStarted/03-llm-client)
- [Opisyal na Dokumentasyon ng MCP](https://modelcontextprotocol.io/)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
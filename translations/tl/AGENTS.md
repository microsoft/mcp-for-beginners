# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang **MCP for Beginners** ay isang open-source na kurikulum para sa pag-aaral ng Model Context Protocol (MCP) - isang standardized na framework para sa interaksyon sa pagitan ng mga AI model at client applications. Ang repository na ito ay nagbibigay ng komprehensibong materyales sa pag-aaral na may mga praktikal na halimbawa ng code sa iba't ibang programming languages.

### Pangunahing Teknolohiya

- **Programming Languages**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL na may pgvector extension
- **Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build Tools**: npm, Maven, pip, Cargo
- **Dokumentasyon**: Markdown na may automated multi-language translation (48+ na wika)

### Arkitektura

- **11 Core Modules (00-11)**: Sunod-sunod na landas sa pag-aaral mula sa mga pangunahing kaalaman hanggang sa advanced na mga paksa
- **Hands-on Labs**: Mga praktikal na ehersisyo na may kumpletong solusyon ng code sa iba't ibang wika
- **Sample Projects**: Gumaganang MCP server at client implementations
- **Translation System**: Automated GitHub Actions workflow para sa suporta sa multi-language
- **Image Assets**: Sentralisadong direktoryo ng mga imahe na may mga bersyong isinalin

## Mga Utos sa Setup

Ang repository na ito ay nakatuon sa dokumentasyon. Karamihan sa setup ay nagaganap sa loob ng mga indibidwal na sample projects at labs.

### Setup ng Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Paggamit ng Sample Projects

Ang mga sample projects ay matatagpuan sa:
- `03-GettingStarted/samples/` - Mga halimbawa na partikular sa wika
- `03-GettingStarted/01-first-server/solution/` - Mga unang server implementations
- `03-GettingStarted/02-client/solution/` - Mga client implementations
- `11-MCPServerHandsOnLabs/` - Komprehensibong database integration labs

Ang bawat sample project ay may sariling setup instructions:

#### TypeScript/JavaScript Projects
```bash
cd <project-directory>
npm install
npm start
```

#### Python Projects
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java Projects
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Workflow ng Pag-develop

### Estruktura ng Dokumentasyon

- **Modules 00-11**: Pangunahing nilalaman ng kurikulum sa sunod-sunod na pagkakasunod
- **translations/**: Mga bersyon na partikular sa wika (auto-generated, huwag direktang i-edit)
- **translated_images/**: Mga lokal na bersyon ng imahe (auto-generated)
- **images/**: Mga source na imahe at diagram

### Paggawa ng Mga Pagbabago sa Dokumentasyon

1. I-edit lamang ang mga English markdown files sa root module directories (00-11)
2. I-update ang mga imahe sa direktoryo ng `images/` kung kinakailangan
3. Ang co-op-translator GitHub Action ay awtomatikong magbuo ng mga pagsasalin
4. Ang mga pagsasalin ay muling binubuo kapag may push sa main branch

### Paggamit ng Mga Pagsasalin

- **Automated Translation**: Ang GitHub Actions workflow ang humahawak sa lahat ng pagsasalin
- **Huwag** manu-manong i-edit ang mga file sa direktoryo ng `translations/`
- Ang metadata ng pagsasalin ay naka-embed sa bawat isinaling file
- Mga suportadong wika: 48+ na wika kabilang ang Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, at marami pang iba

## Mga Tagubilin sa Pagsubok

### Pag-validate ng Dokumentasyon

Dahil ang repository na ito ay pangunahing nakatuon sa dokumentasyon, ang pagsubok ay nakatuon sa:

1. **Pag-validate ng Link**: Siguraduhing gumagana ang lahat ng internal links
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Pag-validate ng Code Sample**: Subukan kung ang mga halimbawa ng code ay nagko-compile/tumatakbo
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown Linting**: Suriin ang pagkakapare-pareho ng formatting
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Pagsubok ng Sample Project

Ang bawat sample na partikular sa wika ay may sariling paraan ng pagsubok:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Mga Alituntunin sa Estilo ng Code

### Estilo ng Dokumentasyon

- Gumamit ng malinaw, madaling maunawaan na wika para sa mga baguhan
- Isama ang mga halimbawa ng code sa iba't ibang wika kung naaangkop
- Sundin ang pinakamahusay na kasanayan sa markdown:
  - Gumamit ng ATX-style headers (`#` syntax)
  - Gumamit ng fenced code blocks na may language identifiers
  - Isama ang deskriptibong alt text para sa mga imahe
  - Panatilihin ang makatwirang haba ng linya (walang mahigpit na limitasyon, ngunit maging praktikal)

### Estilo ng Halimbawa ng Code

#### TypeScript/JavaScript
- Gumamit ng ES modules (`import`/`export`)
- Sundin ang TypeScript strict mode conventions
- Isama ang type annotations
- Targetin ang ES2022

#### Python
- Sundin ang PEP 8 style guidelines
- Gumamit ng type hints kung naaangkop
- Isama ang docstrings para sa mga function at klase
- Gumamit ng modernong Python features (3.8+)

#### Java
- Sundin ang Spring Boot conventions
- Gumamit ng Java 21 features
- Sundin ang standard Maven project structure
- Isama ang Javadoc comments

### Organisasyon ng File

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build at Deployment

### Deployment ng Dokumentasyon

Ang repository ay gumagamit ng GitHub Pages o katulad para sa hosting ng dokumentasyon (kung naaangkop). Ang mga pagbabago sa main branch ay nagti-trigger ng:

1. Translation workflow (`.github/workflows/co-op-translator.yml`)
2. Awtomatikong pagsasalin ng lahat ng English markdown files
3. Lokal na bersyon ng mga imahe kung kinakailangan

### Walang Kinakailangang Build Process

Ang repository na ito ay pangunahing naglalaman ng markdown documentation. Walang kinakailangang compilation o build step para sa pangunahing nilalaman ng kurikulum.

### Deployment ng Sample Project

Ang mga indibidwal na sample projects ay maaaring may mga tagubilin sa deployment:
- Tingnan ang `03-GettingStarted/09-deployment/` para sa gabay sa deployment ng MCP server
- Mga halimbawa ng deployment ng Azure Container Apps sa `11-MCPServerHandsOnLabs/`

## Mga Alituntunin sa Pag-aambag

### Proseso ng Pull Request

1. **Fork at Clone**: I-fork ang repository at i-clone ang iyong fork nang lokal
2. **Gumawa ng Branch**: Gumamit ng deskriptibong pangalan ng branch (hal., `fix/typo-module-3`, `add/python-example`)
3. **Gumawa ng Mga Pagbabago**: I-edit lamang ang English markdown files (hindi ang mga pagsasalin)
4. **Subukan Lokal**: Siguraduhing tama ang pag-render ng markdown
5. **I-submit ang PR**: Gumamit ng malinaw na pamagat at deskripsyon ng PR
6. **CLA**: Pirmahan ang Microsoft Contributor License Agreement kapag na-prompt

### Format ng Pamagat ng PR

Gumamit ng malinaw, deskriptibong pamagat:
- `[Module XX] Maikling deskripsyon` para sa mga pagbabago sa module
- `[Samples] Deskripsyon` para sa mga pagbabago sa sample code
- `[Docs] Deskripsyon` para sa pangkalahatang update sa dokumentasyon

### Ano ang Maaaring I-ambag

- Pag-aayos ng bug sa dokumentasyon o mga halimbawa ng code
- Mga bagong halimbawa ng code sa karagdagang wika
- Mga paglilinaw at pagpapabuti sa umiiral na nilalaman
- Mga bagong case studies o praktikal na halimbawa
- Mga ulat ng isyu para sa hindi malinaw o maling nilalaman

### Ano ang HINDI Dapat Gawin

- Huwag direktang i-edit ang mga file sa direktoryo ng `translations/`
- Huwag i-edit ang direktoryo ng `translated_images/`
- Huwag magdagdag ng malalaking binary files nang walang diskusyon
- Huwag baguhin ang mga translation workflow files nang walang koordinasyon

## Karagdagang Tala

### Pagpapanatili ng Repository

- **Changelog**: Ang lahat ng mahahalagang pagbabago ay idodokumento sa `changelog.md`
- **Study Guide**: Gamitin ang `study_guide.md` para sa pangkalahatang-ideya ng navigation ng kurikulum
- **Issue Templates**: Gamitin ang mga template ng isyu ng GitHub para sa bug reports at feature requests
- **Code of Conduct**: Ang lahat ng kontribyutor ay dapat sumunod sa Microsoft Open Source Code of Conduct

### Landas ng Pag-aaral

Sundin ang mga module sa sunod-sunod na pagkakasunod (00-11) para sa pinakamainam na pag-aaral:
1. **00-02**: Mga Pangunahing Kaalaman (Introduksyon, Core Concepts, Security)
2. **03**: Pagsisimula sa hands-on implementation
3. **04-05**: Praktikal na implementasyon at advanced na mga paksa
4. **06-10**: Komunidad, pinakamahusay na kasanayan, at mga aplikasyon sa totoong mundo
5. **11**: Komprehensibong database integration labs (13 sunod-sunod na labs)

### Mga Suporta na Mapagkukunan

- **Dokumentasyon**: https://modelcontextprotocol.io/
- **Specification**: https://spec.modelcontextprotocol.io/
- **Komunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Kaugnay na Kurso**: Tingnan ang README.md para sa iba pang Microsoft learning paths

### Karaniwang Troubleshooting

**Q: Ang PR ko ay nabigo sa translation check**
A: Siguraduhing in-edit mo lamang ang English markdown files sa root module directories, hindi ang mga isinaling bersyon.

**Q: Paano ako magdaragdag ng bagong wika?**
A: Ang suporta sa wika ay pinamamahalaan sa pamamagitan ng co-op-translator workflow. Magbukas ng isyu para talakayin ang pagdaragdag ng bagong wika.

**Q: Hindi gumagana ang mga halimbawa ng code**
A: Siguraduhing sinunod mo ang mga tagubilin sa setup sa README ng partikular na sample. Suriin kung tama ang mga bersyon ng dependencies na naka-install.

**Q: Hindi nagpapakita ang mga imahe**
A: Siguraduhing ang mga path ng imahe ay relative at gumagamit ng forward slashes. Ang mga imahe ay dapat nasa direktoryo ng `images/` o `translated_images/` para sa mga lokal na bersyon.

### Mga Pagsasaalang-alang sa Performance

- Ang translation workflow ay maaaring tumagal ng ilang minuto upang makumpleto
- Ang malalaking imahe ay dapat i-optimize bago i-commit
- Panatilihing nakatuon at makatwirang laki ang mga indibidwal na markdown files
- Gumamit ng relative links para sa mas mahusay na portability

### Pamamahala ng Proyekto

Ang proyektong ito ay sumusunod sa mga kasanayan ng Microsoft open source:
- MIT License para sa code at dokumentasyon
- Microsoft Open Source Code of Conduct
- Kinakailangan ang CLA para sa mga kontribusyon
- Mga isyu sa seguridad: Sundin ang mga alituntunin sa SECURITY.md
- Suporta: Tingnan ang SUPPORT.md para sa mga mapagkukunan ng tulong

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
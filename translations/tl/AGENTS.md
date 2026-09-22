# AGENTS.md

## Pangkalahatang Pagtingin ng Proyekto

**MCP para sa Mga Baguhan** ay isang open-source na pang-edukasyong kurikulum para matutunan ang Model Context Protocol (MCP) - isang pinagsanib na balangkas para sa mga interaksyon sa pagitan ng mga AI model at mga kliyenteng aplikasyon. Ang repository na ito ay nagbibigay ng malawak na materyales sa pag-aaral kasama ang mga halimbawa ng kodigo sa maraming programming languages.

### Mga Pangunahing Teknolohiya

- **Mga Programming Languages**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Mga Framework at SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Mga Database**: PostgreSQL na may pgvector extension
- **Mga Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Mga Build Tools**: npm, Maven, pip, Cargo
- **Dokumentasyon**: Markdown na may awtomatikong pagsasalin sa maraming wika (48+ na mga wika)

### Arkitektura

- **11 Core Modules (00-11)**: Sunod-sunod na landas sa pag-aaral mula sa mga pundamental hanggang sa mga advanced na paksa
- **Hands-on Labs**: Praktikal na mga pagsasanay na may kumpletong solution code sa maraming wika
- **Mga Halimbawang Proyekto**: Gumaganang MCP server at client implementations
- **Sistemang Pagsasalin**: Awtomatikong GitHub Actions workflow para sa suporta sa maraming wika
- **Mga Larawan**: Sentralisadong direktoryo ng mga larawan na may mga salin na bersyon

## Mga Utos para sa Setup

Ito ay isang dokumentasyong nakatuon na repository. Karamihan sa setup ay ginagawa sa mga indibidwal na halimbawang proyekto at mga labs.

### Setup ng Repository

```bash
# Kopyahin ang repositoryo
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Paggawa sa mga Halimbawang Proyekto

Ang mga halimbawang proyekto ay matatagpuan sa:
- `03-GettingStarted/samples/` - Mga halimbawa ayon sa wika
- `03-GettingStarted/01-first-server/solution/` - Mga unang implementasyon ng server
- `03-GettingStarted/02-client/solution/` - Mga implementasyon ng client
- `11-MCPServerHandsOnLabs/` - Komprehensibong pagsasanay sa integrasyon ng database

Bawat halimbawang proyekto ay may sariling mga tagubilin sa setup:

#### Mga Proyekto sa TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Mga Proyekto sa Python
```bash
cd <project-directory>
pip install -r requirements.txt
# o
pip install -e .
python main.py
```

#### Mga Proyekto sa Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Daloy ng Pag-unlad

### Kahandaan sa MCP 7-28

#### Checklist para sa kahandaan ng repo

- [x] **Kalidad para sa mga bagong kontribyutor**: Ang file na ito ay naglalarawan ng layunin ng repositoryo,
  istruktura, mga alituntunin sa kontribusyon, at mga landas para sa halimbawang setup.
- [x] **Mga utos para sa build/test/lint na may eksaktong mga flag**:
  - Lint sa dokumentasyon ng repositoryo:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit ng pattern ng link sa dokumentasyon ng repositoryo:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validation ng sample sa TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validation ng sample sa Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validation ng sample sa Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **Isang realistiko na workflow na maaaring maging MCP tool**:
  `validate_curriculum_change`
- [x] **Malinaw ang mga inputs/outputs** (tingnan ang espesipikasyon sa ibaba).
- [x] **Naitala ang mga permiso at failure modes** (tingnan ang espesipikasyon sa ibaba).
- [x] **Malinaw ang CI testability** (deterministic na mga utos, malinaw na
  exit codes, at machine-readable na mga outputs).

#### Kandidato na workflow para sa MCP tool: `validate_curriculum_change`

##### Layunin

Suriin ang mga pagbabago sa dokumentasyon ng kurikulum at kalagayan ng representative sample code
bago i-merge.

##### Mga Inputs

- `changed_paths: string[]` (kinakailangan) - mga relative na path na binago sa PR.
- `run_docs_lint: boolean` (default `true`)
- `run_links_audit: boolean` (default `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (default lahat ay `false`)

##### Mga Outputs

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Mga Permiso

- Basahin ang mga file sa workspace at isulat lang ang mga tool-generated na artifacts (hal. lint
  reports, test logs); walang pagsusulat sa `translations/` o
  `translated_images/`.
- Patakbuhin ang mga lokal na shell commands.
- Opsiyonal na access sa network para lang sa package restore (`npm ci`,
  `python -m pip install`, `mvn` dependency resolution).
- Walang permiso na mag-push, mag-merge, o mag-modify ng `translations/` o
  `translated_images/`.

##### Mga Failure modes

- `E_NO_INPUT_PATHS`: walang laman ang `changed_paths`.
- `E_INVALID_PATH`: ang input path ay lumalabas sa root ng repository.
- `E_LINT_FAILED`: nag-exit ng non-zero ang markdown lint.
- `E_LINK_AUDIT_FAILED`: nag-exit ng non-zero ang link audit command.
- `E_SAMPLE_TEST_FAILED`: nag-exit ng non-zero ang sample test/build.
- `E_TIMEOUT`: lumampas sa nakatakdang timeout ang utos.

##### Inirekomendang CI contract

Para i-automate ang validation, i-configure ang isang CI job na:

- Magti-trigger sa mga pull request na tumatama sa `*.md`, sample code, o file na ito.
- Patakbuhin ang eksaktong mga utos na nakalista sa itaas.
- I-save bilang artifacts ang mga logs.
- I-fail ang job kapag mayroong non-zero exit code.

#### Kung maghahain ka ng MCP server mula sa repo na ito

- [ ] Basahin ang pangwakas na MCP `2026-07-28` changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Siguraduhing sinusuportahan ng napiling SDK release ang MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] I-alis ang mga assumptions tungkol sa session at handshake; ituring ang bawat request bilang
  self-contained:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Ipadala ang mga header na `Mcp-Method` at `Mcp-Name` para sa raw na HTTP requests:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Suriin ang mga hardcoded na error codes (`missing resource` inilipat mula `-32002` papuntang `-32602`).

- [ ] Ilipat ang deprecated na Roots, Sampling, Logging, at Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Ilipat mula sa experimental na `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Suriin ang awtorisasyon para sa OAuth at OpenID Connect hardening:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Estruktura ng Dokumentasyon

- **Mga Module 00-11**: Pangunahing nilalaman ng kurikulum ayon sa pagkakasunod-sunod
- **translations/**: Mga bersyon sa partikular na wika (auto-generated, huwag direktang baguhin)
- **translated_images/**: Lokal na bersyon ng mga imahe (auto-generated)
- **images/**: Pinagmulan ng mga imahe at diagram

### Paggawa ng Mga Pagbabago sa Dokumentasyon

1. I-edit lamang ang mga English markdown files sa root module directories (00-11)
2. I-update ang mga imahe sa `images/` directory kung kinakailangan
3. Awtomatikong gagawa ng mga pagsasalin ang co-op-translator GitHub Action
4. Muling nililikha ang mga pagsasalin kapag may push sa main branch

### Paggamit sa Mga Pagsasalin

- **Awtomatikong Pagsasalin**: Isang workflow ng GitHub Actions ang humahawak sa lahat ng pagsasalin
- **Huwag mano-manong mag-edit** ng mga file sa `translations/` directory
- Nakapaloob ang metadata ng pagsasalin sa bawat isinaling file
- Suportadong mga wika: 48+ na wika kabilang ang Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, at iba pa

## Mga Tagubilin sa Pagsubok

### Pag-validate ng Dokumentasyon

Dahil ito ay pangunahing isang repositoryong dokumentasyon, ang pagsubok ay nakatuon sa:

1. **Audit ng Pattern ng Link**: Ilahad ang mga Markdown link para suriin

   ```bash
   # Ilista ang mga Markdown na link (pattern audit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Pag-validate ng Code Sample**: Subukang mag-compile/patakbuhin ang mga halimbawa ng code

   ```bash
   # Mag-navigate sa tiyak na sample at patakbuhin ang mga pagsusuri nito
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Suriin ang pagkakapare-pareho ng format

   ```bash
   # Gamitin ang markdownlint kung kinakailangan
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pagsubok sa Sample na Proyekto

Ang bawat halimbawa sa partikular na wika ay may sariling paraan ng pagsusuri:

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

## Mga Patnubay sa Estilo ng Code

### Estilo ng Dokumentasyon

- Gumamit ng malinaw, pangkaraniwang wikang madaling maintindihan
- Isama ang mga halimbawa ng code sa maraming wika kung naaangkop
- Sundan ang mga pinakamahusay na kasanayan sa markdown:
  - Gumamit ng ATX-style headers (`#` syntax)
  - Gumamit ng fenced code blocks na may mga tag ng wika
  - Isama ang deskriptibong alt na teksto para sa mga larawan
  - Panatilihin ang makatwirang haba ng mga linya (walang mahigpit na limitasyon, ngunit maging maingat)

### Estilo ng Sample na Code

#### TypeScript/JavaScript
- Gumamit ng ES modules (`import`/`export`)
- Sundan ang TypeScript strict mode conventions
- Isama ang mga type annotations
- Target ES2022

#### Python
- Sundan ang mga Patnubay sa istilo ng PEP 8
- Gumamit ng mga type hints kung naaangkop
- Isama ang mga docstrings para sa mga function at klase
- Gumamit ng mga modernong tampok ng Python (3.8+)

#### Java
- Sundan ang mga Spring Boot conventions
- Gumamit ng mga tampok ng Java 21
- Sundan ang karaniwang istruktura ng Maven project
- Isama ang mga komento ng Javadoc

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

Ang repositoryo ay gumagamit ng GitHub Pages o katulad para sa pagho-host ng dokumentasyon (kung naaangkop). Ang mga pagbabago sa main branch ay nagpapasimula ng:

1. Workflow ng pagsasalin (`.github/workflows/co-op-translator.yml`)
2. Awtomatikong pagsasalin ng lahat ng English markdown files
3. Lokal na pagsalin ng mga imahe kung kinakailangan

### Walang Kinakailangang Build Process

Ang repositoryong ito ay pangunahing naglalaman ng markdown dokumentasyon. Walang kinakailangang compilation o build step para sa pangunahing kurikulum na nilalaman.

### Deployment ng Sample na Proyekto

Ang bawat indibidwal na sample proyekto ay maaaring may mga tagubilin sa deployment:
- Tingnan ang `03-GettingStarted/09-deployment/` para sa gabay sa MCP server deployment
- Mga halimbawa ng Azure Container Apps deployment sa `11-MCPServerHandsOnLabs/`

## Mga Patnubay sa Pag-ambag

### Proseso ng Pull Request

1. **Fork at Clone**: I-fork ang repositoryo at i-clone ang iyong fork sa lokal
2. **Gumawa ng Branch**: Gumamit ng mga mapanuring pangalan ng branch (hal., `fix/typo-module-3`, `add/python-example`)
3. **Gumawa ng Mga Pagbabago**: I-edit lamang ang mga English markdown files (huwag ang mga pagsasalin)
4. **Subukan Lokal**: Suriin na tama ang pag-render ng markdown
5. **Isumite ang PR**: Gumamit ng malinaw na mga pamagat at paglalarawan ng PR
6. **CLA**: Lagdaan ang Microsoft Contributor License Agreement kapag hiniling

### Format ng Pamagat ng PR

Gumamit ng malinaw at mapanuring mga pamagat:
- `[Module XX] Maikling paglalarawan` para sa mga pagbabago sa module na partikular
- `[Samples] Paglalarawan` para sa mga pagbabago sa sample code
- `[Docs] Paglalarawan` para sa pangkalahatang update sa dokumentasyon

### Ano ang Iaambag

- Mga pag-ayos ng bug sa dokumentasyon o mga halimbawa ng code
- Mga bagong halimbawa ng code sa dagdag na mga wika
- Mga paglilinaw at pagpapabuti sa umiiral na nilalaman
- Mga bagong case studies o praktikal na halimbawa
- Mga ulat ng isyu para sa hindi malinaw o maling nilalaman

### Ano ang Huwag Gawin

- Huwag direktang i-edit ang mga file sa `translations/` directory
- Huwag i-edit ang `translated_images/` directory
- Huwag magdagdag ng malalaking binary files nang walang pag-uusap
- Huwag baguhin ang mga workflow file ng pagsasalin nang walang koordinasyon

## Karagdagang Tala

### Pangangalaga ng Repositoryo

- **Changelog**: Lahat ng mahahalagang pagbabago ay dokumentado sa `changelog.md`
- **Study Guide**: Gamitin ang `study_guide.md` para sa pangkalahatang overview ng pag-navigate sa kurikulum
- **Issue Templates**: Gamitin ang mga template ng isyu ng GitHub para sa ulat ng bug at kahilingan para sa feature
- **Code of Conduct**: Lahat ng contributor ay dapat sumunod sa Microsoft Open Source Code of Conduct

### Learning Path

Sundan ang mga module ayon sa pagkakasunod-sunod (00-11) para sa pinakamainam na pagkatuto:
1. **00-02**: Mga Pangunahing Kaalaman (Introduksyon, Pangunahing Konsepto, Seguridad)
2. **03**: Pagsisimula na may praktikal na implementasyon
3. **04-05**: Praktikal na implementasyon at mga advanced na paksa
4. **06-10**: Komunidad, pinakamahusay na mga praktis, at mga totoong aplikasyon
5. **11**: Komprehensibong mga lab sa pagsasama ng database (13 magkakasunod na lab)

### Mga Suportang Mapagkukunan

- **Dokumentasyon**: https://modelcontextprotocol.io/
- **Spezipikasyon**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Komunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Mga Kaugnay na Kurso**: Tingnan ang README.md para sa iba pang mga landas sa pag-aaral ng Microsoft

### Karaniwang Pag-aayos ng Problema

**Q: Ang aking PR ay bumabagsak sa translation check**
A: Siguraduhing English markdown files lamang sa root module directories ang na-edit, hindi ang mga isinalin na bersyon.

**Q: Paano ako magdadagdag ng bagong wika?**
A: Ang suporta sa wika ay pinamamahalaan sa pamamagitan ng co-op-translator workflow. Magbukas ng isyu upang pag-usapan ang pagdagdag ng mga bagong wika.

**Q: Hindi gumagana ang mga halimbawa ng code**
A: Siguraduhing nasundan mo ang mga tagubilin sa setup sa README ng partikular na sample. Tingnan kung tama ang mga bersyon ng dependencies na naka-install.


**Q: Hindi lumalabas ang mga larawan**

A: Tiyakin na ang mga landas ng larawan ay relative at gumagamit ng forward slashes. Ang mga larawan ay dapat nasa `images/` na direktoryo o `translated_images/` para sa mga lokal na bersyon.

### Mga Pagsasaalang-alang sa Pagganap

- Maaaring tumagal ng ilang minuto ang workflow ng pagsasalin upang makumpleto
- Ang mga malalaking larawan ay dapat ma-optimize bago i-commit
- Panatilihing nakatuon at makatwiran ang laki ng mga indibidwal na markdown file
- Gumamit ng relative links para sa mas mahusay na portability

### Pamamahala ng Proyekto

Sinusunod ng proyektong ito ang mga open source na gawain ng Microsoft:
- MIT License para sa code at dokumentasyon
- Microsoft Open Source Code of Conduct
- Kinakailangang CLA para sa mga kontribusyon
- Mga isyu sa seguridad: Sundin ang mga patnubay ng SECURITY.md
- Suporta: Tingnan ang SUPPORT.md para sa mga mapagkukunan ng tulong

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

**MCP para sa mga Nagsisimula** ay isang open-source na edukasyonal na kurikulum para sa pag-aaral ng Model Context Protocol (MCP) - isang standardized na balangkas para sa mga interaksyon sa pagitan ng mga AI model at mga client application. Ang imbakan na ito ay nagbibigay ng komprehensibong mga materyales sa pag-aaral na may mga praktikal na halimbawa ng kodigo sa iba't ibang mga programming language.

### Mga Pangunahing Teknolohiya

- **Mga Programming Language**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Mga Framework at SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Mga Database**: PostgreSQL na may pgvector extension
- **Mga Cloud Platform**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Mga Build Tool**: npm, Maven, pip, Cargo
- **Dokumentasyon**: Markdown na may awtomatikong multi-language na pagsasalin (48+ na mga wika)

### Arkitektura

- **11 Core Modules (00-11)**: Sunud-sunod na landas ng pag-aaral mula sa mga pangunahing kaalaman hanggang sa mga advanced na paksa
- **Hands-on Labs**: Praktikal na mga pagsasanay na may kumpletong solusyong kodigo sa iba't ibang wika
- **Mga Halimbawang Proyekto**: Gumagawang implementasyon ng MCP server at client
- **Sistema ng Pagsasalin**: Awtomatikong workflow ng GitHub Actions para sa suporta sa maraming wika
- **Mga Larawan**: Sentralisadong direktoryo ng mga imahe na may mga isinalin na bersyon

## Mga Utos sa Setup

Ito ay isang repositoryo na nakatuon sa dokumentasyon. Karamihan sa setup ay nangyayari sa loob ng mga indibidwal na halimbawang proyekto at mga lab.

### Setup ng Repositoryo

```bash
# Kopyahin ang repositoryo
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Pagtatrabaho sa Mga Halimbawang Proyekto

Ang mga halimbawang proyekto ay matatagpuan sa:
- `03-GettingStarted/samples/` - Mga halimbawa ayon sa wika
- `03-GettingStarted/01-first-server/solution/` - Mga unang implementasyon ng server
- `03-GettingStarted/02-client/solution/` - Mga implementasyon ng client
- `11-MCPServerHandsOnLabs/` - Komprehensibong mga lab ng integrasyon sa database

Ang bawat halimbawang proyekto ay may sariling mga tagubilin sa setup:

#### Mga Proyekto ng TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Mga Proyekto ng Python
```bash
cd <project-directory>
pip install -r requirements.txt
# o
pip install -e .
python main.py
```

#### Mga Proyekto ng Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Daloy ng Pag-unlad

### Kahandaan para sa MCP 7-28

#### Checklist para sa kahandaan ng repo

- [x] **Kalakhihan para sa bagong contributor**: Itinatakda ng file na ito ang layunin ng repositoryo,
  istruktura, mga patakaran sa kontribusyon, at mga path sa setup ng sample.
- [x] **Mga utos sa build/test/lint na may eksaktong flag**:
  - Linisin ang dokumentasyon ng repositoryo:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit ng pattern ng mga link sa dokumentasyon ng repositoryo:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Pagbalidate ng sample sa TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Pagbalidate ng sample sa Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Pagbalidate ng sample sa Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Isang makatotohanang daloy ng trabaho na maaaring maging MCP tool**:
  `validate_curriculum_change`
- [x] **Ang mga input/output ay tahasan** (tingnan ang espesipikasyon sa ibaba).
- [x] **Naipabatid ang mga permiso at mga mode ng pagkabigo** (tingnan ang espesipikasyon sa ibaba).
- [x] **Tahasan ang testability sa CI** (mga deterministic na utos, tahasang
  exit code, at mga output na nababasa ng makina).

#### Halimbawang daloy ng MCP tool: `validate_curriculum_change`

##### Layunin

Suriin ang mga pagbabago sa dokumentasyon ng kurikulum at ang kalusugan ng kinatawang sample code bago ang pagsasama.


##### Mga Input

- `changed_paths: string[]` (kailangan) - mga relative na path na binago sa PR.
- `run_docs_lint: boolean` (default `true`)
- `run_links_audit: boolean` (default `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (default lahat `false`)

##### Mga Output

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Mga Pahintulot

- Basahin lamang ang mga file sa workspace at isulat ang mga artifact na ginawa ng tool (hal., lint
  reports, test logs); walang pagsulat sa `translations/` o
  `translated_images/`.
- Patakbuhin ang mga lokal na utos ng shell.
- Opsyonal na access sa network para lamang sa package restore (`npm ci`,
  `python -m pip install`, `mvn` dependency resolution).
- Walang pahintulot na mag-push, mag-merge, o magbago ng `translations/` o
  `translated_images/`.

##### Mga Mode ng Pagkabigo

- `E_NO_INPUT_PATHS`: walang laman ang `changed_paths`.
- `E_INVALID_PATH`: ang input path ay lumalagpas sa ugat ng repositoryo.
- `E_LINT_FAILED`: ang markdown lint ay nag-exit ng di-zero.
- `E_LINK_AUDIT_FAILED`: ang audit ng link ay nag-exit ng di-zero.
- `E_SAMPLE_TEST_FAILED`: ang sample na test/build ay nag-exit ng di-zero.
- `E_TIMEOUT`: ang utos ay lumampas sa itinakdang timeout.

##### Inirekomendang kontrata sa CI

Para sa awtomatikong pag-validate, i-configure ang isang CI na trabaho na:

- Nagsisimula sa mga pull request na tumutukoy sa `*.md`, sample code, o sa file na ito.
- Pinapatakbo ang eksaktong mga utos na nakalista sa itaas.
- Pinananatili ang mga log bilang mga artifact.
- Pinapabagsak ang trabaho kapag may anumang non-zero exit code.

#### Kung magpapadala ka ng MCP server mula sa repositoryong ito

- [ ] Basahin ang draft changelog para sa MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Patakbuhin ang iyong server laban sa mga SDK beta:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Alisin ang mga palagay ng session at handshake; tratuhin ang bawat kahilingan bilang
  self-contained:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Magpadala ng `Mcp-Method` at `Mcp-Name` na mga header para sa raw HTTP requests:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] I-audit ang hardcoded na mga error code (`missing resource` inilipat mula sa `-32002` patungong `-32602`).

- [ ] I-flag at planuhin ang migrasyon para sa mga deprecated na root, sampling, at
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Lumipat mula sa experimental na `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Suriin ang awtorisasyon para sa pagpapatibay ng OAuth at OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Istruktura ng Dokumentasyon

- **Modules 00-11**: Pangunahing nilalaman ng kurikulum sa sunud-sunod na ayos
- **translations/**: Mga bersyon ng wika (auto-generated, huwag direktang i-edit)
- **translated_images/**: Lokalisadong bersyon ng mga imahe (auto-generated)
- **images/**: Mga pinagmulan ng mga imahe at diagram

### Paggawa ng Mga Pagbabago sa Dokumentasyon

1. I-edit lamang ang mga English na markdown file sa root module directories (00-11)
2. I-update ang mga imahe sa direktoryong `images/` kung kinakailangan
3. Ang co-op-translator GitHub Action ay awtomatikong gagawa ng mga pagsasalin
4. Mulit na ginagawa ang mga pagsasalin kapag may push sa main branch

### Paggamit ng Mga Pagsasalin

- **Awtomatikong Pagsasalin**: Ang workflow ng GitHub Actions ang humahawak sa lahat ng pagsasalin
- **Huwag MANUAL na i-edit** ang mga file sa direktoryong `translations/`
- Nakapaloob sa bawat isinalin na file ang metadata ng pagsasalin
- Suportadong mga wika: 48+ na wika kabilang ang Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, at marami pa

## Mga Tagubilin sa Pagsubok

### Pag-validate ng Dokumentasyon

Dahil ito ay pangunahing isang dokumentasyon na repositoryo, nakatuon ang pagsubok sa:

1. **Audit ng Pattern ng Link**: Maglista ng mga Markdown link para sa pagrepaso

   ```bash
   # Ilista ang mga link ng Markdown (audit ng pattern)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Pag-validate ng Halimbawang Code**: Subukang mag-compile/run ng mga halimbawa ng code

   ```bash
   # Mag-navigate sa partikular na sample at patakbuhin ang mga pagsusuri nito
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Suriin ang pagkakapare-pareho ng format

   ```bash
   # Gamitin ang markdownlint kung kinakailangan
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pagsubok sa Halimbawang Proyekto

Kasama sa bawat wika ang sarili nitong paraan ng pagsubok:

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

- Gumamit ng malinaw, madaling maintindihang wika para sa mga baguhan
- Isama ang mga halimbawa ng code sa iba't ibang mga wika kung naaangkop
- Sundin ang mga pinakamahusay na kasanayan sa markdown:
  - Gumamit ng mga ATX-style header (`#` na sintaks)
  - Gumamit ng fenced code blocks na may mga language identifier
  - Isama ang naglalarawang alt text para sa mga imahe
  - Panatilihing makatwiran ang haba ng mga linya (walang mahigpit na limitasyon, ngunit maging makatwiran)

### Estilo ng Halimbawang Code

#### TypeScript/JavaScript
- Gumamit ng ES modules (`import`/`export`)
- Sundin ang mga kumbensyon ng TypeScript strict mode
- Isama ang mga type annotation
- Target ang ES2022

#### Python
- Sundin ang mga patnubay sa estilo ng PEP 8
- Gumamit ng type hints kung naaangkop
- Isama ang mga docstring para sa mga function at klase
- Gumamit ng mga modernong tampok ng Python (3.8+)

#### Java
- Sundin ang mga kumbensyon ng Spring Boot
- Gumamit ng mga tampok ng Java 21
- Sundin ang karaniwang istruktura ng Maven project
- Isama ang mga komentaryo sa Javadoc

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

## Pagbuo at Deployment

### Deployment ng Dokumentasyon

Ang repositoryo ay gumagamit ng GitHub Pages o katulad para sa pagtanggap ng dokumentasyon (kung naaangkop). Ang mga pagbabago sa main branch ay nagpapasimula ng:

1. Workflow ng pagsasalin (`.github/workflows/co-op-translator.yml`)
2. Awtomatikong pagsasalin ng lahat ng English na markdown file
3. Lokalisasyon ng mga imahe kung kinakailangan

### Walang Kailangan na Proseso ng Build

Ang repositoryo na ito ay pangunahing naglalaman ng dokumentasyong markdown. Walang kinakailangang compilation o build step para sa pangunahing nilalaman ng kurikulum.

### Deployment ng Halimbawang Proyekto

Maaaring may mga tagubilin sa deployment ang bawat indibidwal na halimbawang proyekto:
- Tingnan ang `03-GettingStarted/09-deployment/` para sa gabay sa deployment ng MCP server
- Mga halimbawa ng deployment para sa Azure Container Apps sa `11-MCPServerHandsOnLabs/`

## Mga Alituntunin sa Pagsusumite

### Proseso ng Pull Request

1. **Fork at Clone**: I-fork ang repositoryo at i-clone ang iyong fork nang lokal
2. **Gumawa ng Branch**: Gumamit ng mga nakalarawang pangalan ng branch (hal. `fix/typo-module-3`, `add/python-example`)
3. **Gumawa ng Mga Pagbabago**: I-edit lamang ang mga English markdown file (huwag ang mga pagsasalin)
4. **Subukan Nang Lokal**: Siguraduhing maayos ang pag-render ng markdown
5. **Isumite ang PR**: Gumamit ng malinaw na mga pamagat at paglalarawan ng PR
6. **CLA**: Pirmahan ang Microsoft Contributor License Agreement kapag hinihiling

### Format ng PR Title

Gumamit ng malinaw, nakalarawang mga pamagat:
- `[Module XX] Maikling paglalarawan` para sa mga pagbabago sa partikular na module
- `[Samples] Paglalarawan` para sa mga pagbabago sa sample code
- `[Docs] Paglalarawan` para sa pangkalahatang mga update sa dokumentasyon

### Ano ang Maibibigay

- Mga pag-ayos ng bug sa dokumentasyon o mga halimbawang code
- Mga bagong halimbawa ng code sa karagdagang mga wika
- Mga paglilinaw at mga pagpapabuti sa umiiral na nilalaman
- Mga bagong case study o praktikal na halimbawa
- Mga ulat ng isyu para sa mga hindi malinaw o maling nilalaman

### Ano ang HINDI Dapat Gawin

- Huwag direktang i-edit ang mga file sa direktoryong `translations/`
- Huwag i-edit ang direktoryong `translated_images/`
- Huwag magdagdag ng malalaking binary file nang walang talakayan
- Huwag baguhin ang mga workflow file ng pagsasalin nang walang koordinasyon

## Karagdagang Tala

### Pangangalaga sa Repositoryo

- **Changelog**: Dokumentado ang lahat ng mahahalagang pagbabago sa `changelog.md`
- **Study Guide**: Gamitin ang `study_guide.md` para sa overview ng pag-navigate ng kurikulum
- **Issue Templates**: Gamitin ang mga template ng GitHub issue para sa pag-uulat ng bug at feature request
- **Code of Conduct**: Kailangang sundin ng lahat ng contributor ang Microsoft Open Source Code of Conduct

### Landas ng Pagkatuto

Sundan ang mga module nang sunud-sunod (00-11) para sa pinakamainam na pagkatuto:
1. **00-02**: Pangunahing kaalaman (Panimula, Mga Pangunahing Konsepto, Seguridad)
2. **03**: Pagsisimula sa hands-on na implementasyon
3. **04-05**: Praktikal na implementasyon at mga advanced na paksa
4. **06-10**: Komunidad, mga pinakamahusay na kasanayan, at mga aplikasyon sa totoong buhay
5. **11**: Komprehensibong mga laboratoryo sa integrasyon ng database (13 sunod-sunod na laboratorio)

### Mga Suporta at Mapagkukunan

- **Dokumentasyon**: https://modelcontextprotocol.io/
- **Espesipikasyon**: https://spec.modelcontextprotocol.io/
- **Komunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Mga Kaugnay na Kurso**: Tingnan ang README.md para sa iba pang mga landas ng pagkatuto ng Microsoft

### Karaniwang Pagsasaayos ng Problema

**Q: Ang aking PR ay pumapalya sa translation check**
A: Siguraduhing English markdown files lamang ang na-edit mo sa root module directories, hindi ang mga isinalin na bersyon.

**Q: Paano ako magdadagdag ng bagong wika?**
A: Pinamamahalaan ang suporta sa wika sa pamamagitan ng co-op-translator workflow. Magbukas ng isyu para talakayin ang pagdaragdag ng mga bagong wika.

**Q: Hindi gumagana ang mga halimbawang code**

A: Tiyakin na nasunod mo ang mga tagubilin sa setup sa README ng partikular na sample. Suriin na mayroon kang tamang mga bersyon ng mga dependency na naka-install.

**Q: Hindi lumalabas ang mga larawan**
A: Siguraduhin na ang mga landas ng larawan ay relative at gumagamit ng forward slash. Ang mga larawan ay dapat nasa `images/` na direktoryo o `translated_images/` para sa mga lokal na bersyon.

### Mga Pagsasaalang-alang sa Pagganap

- Maaaring tumagal ng ilang minuto ang workflow ng pagsasalin upang matapos
- Dapat i-optimize muna ang malalaking larawan bago mag-commit
- Panatilihing nakatuon at makatwiran ang laki ng mga indibidwal na markdown file
- Gumamit ng mga relative na link para sa mas mahusay na portability

### Pamamahala ng Proyekto

Sinusunod ng proyektong ito ang mga open source na praktis ng Microsoft:
- MIT License para sa code at dokumentasyon
- Microsoft Open Source Code of Conduct
- Kinakailangan ang CLA para sa mga kontribusyon
- Mga isyu sa seguridad: Sundin ang mga patnubay sa SECURITY.md
- Suporta: Tingnan ang SUPPORT.md para sa mga tulong na mapagkukunan

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
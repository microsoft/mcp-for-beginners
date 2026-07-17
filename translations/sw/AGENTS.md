# AGENTS.md

## Muhtasari wa Mradi

**MCP kwa Wananchi** ni mtaala wa elimu wa chanzo huria kwa ajili ya kujifunza Mkataba wa Muktadha wa Mfano (MCP) - mfumo uliosanifiwa wa mwingiliano kati ya mifano ya AI na programu za mteja. Hazina hii hutoa vifaa kamili vya kujifunzia yenye mifano ya vitendo ya msimbo katika lugha nyingi za programu.

### Teknolojia Muhimu

- **Lugha za Programu**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Mifumo na SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Hifadhidata**: PostgreSQL na nyongeza ya pgvector
- **Majukwaa ya Wingu**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Vifaa vya Ujenzi**: npm, Maven, pip, Cargo
- **Nyaraka**: Markdown na tafsiri za lugha nyingi zilizo otomatiki (lugha 48+)

### Mimarisha

- **Moduli 11 Muhimu (00-11)**: Njia ya kujifunza kwa mfuatano kutoka misingi hadi mada za juu
- **Maabara za Vitendo**: Mazoezi ya vitendo yenye msimbo kamili wa suluhisho katika lugha nyingi
- **Miradi ya Kielelezo**: Utekelezaji wa seva na mteja wa MCP unaofanya kazi
- **Mfumo wa Tafsiri**: Kazi za GitHub Actions za kiotomatiki kwa msaada wa lugha nyingi
- **Rasilimali za Picha**: Saraka kuu ya picha zilizo na matoleo ya tafsiri

## Amri za Kuanzisha

Hii ni hazina inayolenga nyaraka. Mipangilio mingi hufanyika ndani ya miradi na maabara za kielelezo binafsi.

### Kuanzisha Hazina

```bash
# Nakili hifadhi
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Kufanya kazi na Miradi ya Kielelezo

Miradi ya kielelezo zipo katika:
- `03-GettingStarted/samples/` - Mifano maalum ya lugha
- `03-GettingStarted/01-first-server/solution/` - Utekelezaji wa seva za kwanza
- `03-GettingStarted/02-client/solution/` - Utekelezaji wa mteja
- `11-MCPServerHandsOnLabs/` - Maabara kamili za uunganishaji wa hifadhidata

Kila mradi wa kielelezo una maelekezo yake ya mipangilio:

#### Miradi ya TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Miradi ya Python
```bash
cd <project-directory>
pip install -r requirements.txt
# au
pip install -e .
python main.py
```

#### Miradi ya Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Mtiririko wa Maendeleo

### Uko tayari wa MCP 7-28

#### Orodha ya ukarabati wa hazina

- [x] **Uwazi wa mchango mpya**: Faili hii inaweka madhumuni ya hazina,
  muundo, kanuni za michango, na njia za mipangilio ya kielelezo.
- [x] **Amri za kujenga/kupima/lint na bendera sahihi**:
  - Lint ya nyaraka za hazina:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Ukaguzi wa muundo wa viungo vya nyaraka za hazina:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Uhakiki wa sampuli ya TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Uhakiki wa sampuli ya Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Uhakiki wa sampuli ya Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **Njia halisi moja ya kazi inayoweza kuwa chombo cha MCP**:
  `validate_curriculum_change`
- [x] **Ingizo/Matokeo ni wazi** (angalau maelezo hapa chini).
- [x] **Ruhusa na hali za kushindwa zimeandikwa** (angalau maelezo hapa chini).
- [x] **Uwezo wa kupimwa CI ni wazi** (amri thabiti, kodi za kutoka zilizo wazi,
  na matokeo yanayoweza kusomwa na mashine).

#### Mfuatano wa chombo cha MCP kinachowezekana: `validate_curriculum_change`

##### Lengo

Thibitisha mabadiliko ya nyaraka za mtaala na afya ya mfano wa kuwakilisha wa nambari kabla ya kuunganisha.


##### Ingizo

- `changed_paths: string[]` (inahitajika) - njia zinazobadilika ndani ya PR.
- `run_docs_lint: boolean` (chaguo-msingi `true`)
- `run_links_audit: boolean` (chaguo-msingi `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (chaguo-msingi zote `false`)

##### Matokeo

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Ruhusa

- Soma faili za mazingira na andika vitu vilivyotengenezwa na chombo (mfano ripoti za lint,
  kumbukumbu za majaribio) tu; usiandike kwenye `translations/` au
  `translated_images/`.
- Endesha amri za shell za hapa nyumbani.
- Ruhusa ya mtandao ni hiari tu kwa ajili ya kurejesha kifurushi (`npm ci`,
  `python -m pip install`, utatuzi wa utegemezi wa `mvn`).
- Hakuna ruhusa ya kushinikiza, kuunganisha, au kubadilisha `translations/` au
  `translated_images/`.

##### Hali za kushindwa

- `E_NO_INPUT_PATHS`: `changed_paths` ni tupu.
- `E_INVALID_PATH`: njia ya ingizo inatoka kaskazini ya mzizi wa hazina.
- `E_LINT_FAILED`: lint ya markdown inatoka na kodi isiyo sifuri.
- `E_LINK_AUDIT_FAILED`: amri ya ukaguzi wa viungo inatoka na kodi isiyo sifuri.
- `E_SAMPLE_TEST_FAILED`: jaribio/ujenzi wa mfano unatoka na kodi isiyo sifuri.
- `E_TIMEOUT`: amri imeshindwa ndani ya muda uliowekwa.

##### Mkataba wa CI uliopendekezwa

Ili kuendesha uthibitisho kiotomati, sanidi kazi ya CI ambayo:

- Huchochewa kwenye ombi za pull zinazoangalia `*.md`, nambari ya mfano, au faili hii.
- Inaendesha amri halisi zilizoorodheshwa hapo juu.
- Huhifadhi kumbukumbu kama vitu.
- Hushindwa kazi ikiwa na kodi ya kutoka isiyo sifuri.

#### Ikiwa unatuma server ya MCP kutoka hazina hii

- [ ] Soma rasimu ya mabadiliko ya MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Endesha server yako dhidi ya betas za SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Ondoa makadirio ya kikao na chakusanye mikono; chukulia kila ombi kama
  la kujitegemea:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Tuma vichwa vya `Mcp-Method` na `Mcp-Name` kwa maombi ya raw HTTP:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Hakiki makodi magumu ya hitilafu (`missing resource` imehamishwa kutoka `-32002` hadi `-32602`).

- [ ] Bendera na panga uhamishaji wa mizizi iliyopitwa na wakati, sampuli, na
  kuandika:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Hamisha mbali na API ya majaribio ya `2025-11-25` ya Kazi:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Kagua idhini kwa ajili ya kuimarisha OAuth na OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Muundo wa Nyaraka

- **Modules 00-11**: Maudhui ya mtaala wa msingi kwa mpangilio mfululizo
- **translations/**: Toleo la lugha maalum (limeundwa kiotomatiki, usihariri moja kwa moja)
- **translated_images/**: Toleo la picha zilizoamilishwa kwa lugha (limeundwa kiotomatiki)
- **images/**: Picha na michoro za asili

### Kufanya Mabadiliko ya Nyaraka

1. Hariri tu faili za markdown za Kiingereza katika saraka kuu za moduli (00-11)
2. Sasisha picha katika saraka `images/` ikiwa inahitajika
3. Kitendo cha GitHub cha co-op-translator kitaunda tafsiri kiotomatiki
4. Tafsiri hutengenezwa upya kila wakati ukurasa mkuu unapobebwa push

### Kufanya Kazi na Tafsiri

- **Tafsiri ya Kiotomatiki**: Mchakato wa GitHub Actions hushughulikia tafsiri zote
- USIhariri faili za `translations/` kwa mkono
- Metadata ya tafsiri imejumuishwa katika kila faili lililotafsiriwa
- Lugha zinazotegemezwa: Lugha 48+ ikiwa ni pamoja na Kiarabu, Kichina, Kifaransa, Kijerumani, Hindi, Kijapani, Kikorea, Kireno, Kirusi, Kihispania, na nyingine nyingi

## Maagizo ya Kupima

### Uthibitishaji wa Nyaraka

Kwa kuwa hii ni hifadhidata ya nyaraka hasa, upimaji unazingatia:

1. **Ukaguzi wa Muundo wa Viungo**: Orodhesha viungo vya Markdown kwa kupitia

   ```bash
   # Orodhesha viungo vya Markdown (ukaguzi wa muundo)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Uthibitishaji wa Sampuli za Msimbo**: Jaribu mifano ya msimbo ikiwa inakusanya/inaendesha

   ```bash
   # Elekeza kwenye sampuli maalum na endesha vipimo vyake
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Ukaguzi wa Markdown**: Angalia muafaka wa muundo

   ```bash
   # Tumia markdownlint ikiwa inahitajika
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Kupima Mradi wa Sampuli

Kila sampuli ya lugha maalum ni pamoja na mbinu yake ya kupima:

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

## Miongozo ya Mtindo wa Msimbo

### Mtindo wa Nyaraka

- Tumia lugha wazi, rafiki kwa wanaoanza
- Jumuisha mifano ya msimbo katika lugha nyingi inapowezekana
- Fuata mbinu bora za markdown:
  - Tumia vichwa vya ATX (`#` syntax)
  - Tumia viboreshaji vya msimbo vyenye vitambulisho vya lugha
  - Jumuisha maandishi wa alt ya kueleza kwa picha
  - Weka urefu wa mistari kuwa wa busara (hakuna kikomo kigumu, lakini kuwa na busara)

### Mtindo wa Mfano wa Msimbo

#### TypeScript/JavaScript
- Tumia moduli za ES (`import`/`export`)
- Fuata kanuni za mode ngumu za TypeScript
- Jumuisha maelezo ya aina
- Lenga ES2022

#### Python
- Fuata miongozo ya mtindo wa PEP 8
- Tumia vihimizo vya aina inapofaa
- Jumuisha docstrings kwa kazi na madarasa
- Tumia sifa za kisasa za Python (3.8+)

#### Java
- Fuata kanuni za Spring Boot
- Tumia vipengele vya Java 21
- Fuata muundo wa mradi wa Maven wa kawaida
- Jumuisha maoni ya Javadoc

### Uandaaji wa Faili

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

## Ujenzi na Utoaji

### Utoaji wa Nyaraka

Hifadhidata hutumia GitHub Pages au sawa kwa kuhudumia nyaraka (ikiwa inahitajika). Mabadiliko kwenye tawi kuu husababisha:

1. Mchakato wa tafsiri (`.github/workflows/co-op-translator.yml`)
2. Tafsiri ya kiotomatiki ya faili zote za markdown za Kiingereza
3. Uamilishaji wa picha inapohitajika

### Hakuna Mchakato wa Ujenzi Unaohitajika

Hifadhidata hii kwa kawaida ina nyaraka za markdown. Hakuna hatua ya kukusanya au kujenga inahitajika kwa maudhui ya mtaala wa msingi.

### Utoaji wa Mradi wa Sampuli

Miradi ya sampuli ya mtu binafsi inaweza kuwa na maelekezo ya utoaji:
- Angalia `03-GettingStarted/09-deployment/` kwa mwongozo wa utoaji wa seva ya MCP
- Mifano ya utoaji wa Azure Container Apps katika `11-MCPServerHandsOnLabs/`

## Miongozo ya Kuchangia

### Mchakato wa Ombi la Viongezeo

1. **Furukisha na Nakili**: Furukisha hifadhidata na nakili furukisho lako kwa eneo lako
2. **Unda Tawi**: Tumia majina ya tawi yanayoelezea (mfano, `fix/typo-module-3`, `add/python-example`)
3. **Fanya Mabadiliko**: Hariri tu faili za markdown za Kiingereza (si tafsiri)
4. **Jaribu Kwenye Eneo**: Hakiki markdown inaonekana vizuri
5. **Tuma PR**: Tumia vichwa vya PR vya wazi na maelezo
6. **CLA**: Saini Makubaliano ya Leseni ya Mchangiaji ya Microsoft unapoombwa

### Muundo wa Kichwa cha PR

Tumia vichwa vya wazi, vya kuelezea:
- `[Module XX] Maelezo mafupi` kwa mabadiliko maalum ya moduli
- `[Samples] Maelezo` kwa mabadiliko ya mifano ya msimbo
- `[Docs] Maelezo` kwa masasisho ya jumla ya nyaraka

### Kile cha Kuchangia

- Marekebisho ya kasoro katika nyaraka au mifano ya msimbo
- Mifano mipya ya msimbo katika lugha zaidi
- Ufafanuzi na maboresho ya maudhui yaliyopo
- Masomo mapya ya kesi au mifano ya vitendo
- Ripoti za masuala kwa maudhui yasiyo wazi au yasiyo sahihi

### Kile KISICHO FANYIKA

- Usihariri moja kwa moja faili katika saraka ya `translations/`
- Usihariri saraka ya `translated_images/`
- Usiongeze faili kubwa za binary bila mazungumzo
- Usibadilishe faili za mchakato wa tafsiri bila uratibu

## Vidokezo Zaidi

### Matunzo ya Hifadhidata

- **Changelog**: Mabadiliko yote muhimu yameandikwa katika `changelog.md`
- **Mwongozo wa Kusoma**: Tumia `study_guide.md` kwa muhtasari wa urambazaji wa mtaala
- **Milandishi ya Masuala**: Tumia milandishi ya masuala ya GitHub kwa ripoti za kasoro na maombi ya vipengele
- **Kanuni za Maadili**: Washiriki wote lazima wafuate Kanuni za Maadili za Chanzo Huria za Microsoft

### Njia ya Kujifunza

Fuata moduli kwa mpangilio mfululizo (00-11) kwa ujifunzaji bora:
1. **00-02**: Misingi (Utangulizi, Dhana za Msingi, Usalama)
2. **03**: Kuanzishwa na utekelezaji wa vitendo
3. **04-05**: Utekelezaji wa vitendo na mada za juu
4. **06-10**: Jumuiya, mbinu bora, na matumizi ya ulimwengu halisi
5. **11**: Mafunzo ya kina ya ujumuishaji wa hifadhidata (mafunzo 13 mfululizo)

### Rasilimali za Msaada

- **Nyaraka**: https://modelcontextprotocol.io/
- **Maelezo Kamili**: https://spec.modelcontextprotocol.io/
- **Jumuiya**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Server ya Microsoft Foundry Discord
- **Kozi Zinazohusiana**: Angalia README.md kwa njia nyingine za kujifunza Microsoft

### Matatizo ya Kawaida

**Q: PR yangu inashindwa ukaguzi wa tafsiri**
J: Hakikisha umehariri tu faili za markdown za Kiingereza katika saraka kuu za moduli, sio matoleo yaliyotafsiriwa.

**Q: Ninawezaje kuongeza lugha mpya?**
J: Msaada wa lugha unasimamiwa kupitia mchakato wa co-op-translator. Fungua shida ili kujadili kuongeza lugha mpya.

**Q: Sampuli za msimbo hazifanyi kazi**

J: Hakikisha umefuata maagizo ya usanidi katika README ya sampuli maalum. Angalia kuwa umeweka matoleo sahihi ya utegemezi.

**S: Picha hazionekani**
J: Hakiki njia za picha kuwa ni za jamaa na tumia mikato mbele. Picha zinapaswa kuwa katika saraka ya `images/` au `translated_images/` kwa matoleo yaliyotafsiriwa.

### Vizingiti vya Utendaji

- Mchakato wa tafsiri unaweza kuchukua dakika kadhaa kukamilika
- Picha kubwa zinapaswa kuboreshwa kabla ya kuziweka
- Hifadhi faili za markdown binafsi ziwe na mkazo na zilele zinazofaa kwa ukubwa
- Tumia viungo vya jamaa kwa unyumbufu bora

### Usimamizi wa Mradi

Mradi huu unafuata mazoea ya chanzo huria ya Microsoft:
- Leseni ya MIT kwa msimbo na nyaraka
- Kanuni za Microsoft za Chanzo Huria
- CLA inahitajika kwa michango
- Masuala ya usalama: Fuata miongozo ya SECURITY.md
- Msaada: Tazama SUPPORT.md kwa rasilimali za msaada

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
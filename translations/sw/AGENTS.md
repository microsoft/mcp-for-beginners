# AGENTS.md

## Muhtasari wa Mradi

**MCP kwa Kompyuta** ni mtaala wa elimu wa chanzo huria kwa ajili ya kujifunza Model Context Protocol (MCP) - mfumo sanifu wa mawasiliano kati ya mifano ya AI na programu za wateja. Hifadhi hii inatoa vifaa vya kujifunza vya kina pamoja na mifano ya msimbo wa vitendo katika lugha mbalimbali za programu.

### Teknolojia Muhimu

- **Lugha za Programu**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Hifadhidata**: PostgreSQL na upanuzi wa pgvector
- **Majukwaa ya Wingu**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Zana za Ujenzi**: npm, Maven, pip, Cargo
- **Nyaraka**: Markdown na tafsiri ya lugha nyingi kiotomatiki (lugha 48+)

### Muundo wa Mfumo

- **Moduli 11 za Msingi (00-11)**: Njia ya kujifunza kwa mpangilio kutoka misingi hadi mada za juu
- **Maabara ya Vitendo**: Mazoezi ya vitendo na msimbo wa suluhisho kamili katika lugha mbalimbali
- **Miradi ya Mfano**: Utekelezaji wa seva ya MCP na wateja
- **Mfumo wa Tafsiri**: Mtiririko wa kazi wa GitHub Actions kwa msaada wa lugha nyingi
- **Picha**: Saraka ya picha iliyojikita na matoleo yaliyotafsiriwa

## Amri za Usanidi

Hii ni hifadhi inayolenga nyaraka. Usanidi mwingi hufanyika ndani ya miradi ya mfano na maabara.

### Usanidi wa Hifadhi

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Kufanya Kazi na Miradi ya Mfano

Miradi ya mfano iko katika:
- `03-GettingStarted/samples/` - Mifano maalum ya lugha
- `03-GettingStarted/01-first-server/solution/` - Utekelezaji wa seva ya kwanza
- `03-GettingStarted/02-client/solution/` - Utekelezaji wa wateja
- `11-MCPServerHandsOnLabs/` - Maabara ya kina ya ujumuishaji wa hifadhidata

Kila mradi wa mfano una maagizo yake ya usanidi:

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
# or
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

### Muundo wa Nyaraka

- **Moduli 00-11**: Maudhui ya mtaala wa msingi kwa mpangilio
- **translations/**: Matoleo maalum ya lugha (yanayotengenezwa kiotomatiki, usihariri moja kwa moja)
- **translated_images/**: Matoleo ya picha yaliyotafsiriwa (yanayotengenezwa kiotomatiki)
- **images/**: Picha za chanzo na michoro

### Kufanya Mabadiliko ya Nyaraka

1. Hariri faili za markdown za Kiingereza pekee katika saraka za moduli za mizizi (00-11)
2. Sasisha picha katika saraka ya `images/` ikiwa inahitajika
3. Mtiririko wa kazi wa GitHub Action wa co-op-translator utazalisha tafsiri kiotomatiki
4. Tafsiri zinazalishwa upya wakati wa kusukuma kwenye tawi kuu

### Kufanya Kazi na Tafsiri

- **Tafsiri ya Kiotomatiki**: Mtiririko wa kazi wa GitHub Actions hushughulikia tafsiri zote
- **USIHARIRI** faili moja kwa moja katika saraka ya `translations/`
- Metadata ya tafsiri imejumuishwa katika kila faili iliyotafsiriwa
- Lugha zinazoungwa mkono: Lugha 48+ ikiwa ni pamoja na Kiarabu, Kichina, Kifaransa, Kijerumani, Kihindi, Kijapani, Kikorea, Kireno, Kirusi, Kihispania, na nyingine nyingi

## Maagizo ya Kupima

### Uthibitishaji wa Nyaraka

Kwa kuwa hii ni hifadhi inayolenga nyaraka, upimaji unalenga:

1. **Uthibitishaji wa Viungo**: Hakikisha viungo vyote vya ndani vinafanya kazi
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Uthibitishaji wa Mifano ya Msimbo**: Jaribu kwamba mifano ya msimbo inakamilika/inakimbia
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting ya Markdown**: Angalia uthabiti wa muundo
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Upimaji wa Miradi ya Mfano

Kila mfano maalum wa lugha unajumuisha mbinu yake ya upimaji:

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

- Tumia lugha wazi, inayofaa kwa kompyuta
- Jumuisha mifano ya msimbo katika lugha mbalimbali inapowezekana
- Fuata mbinu bora za markdown:
  - Tumia vichwa vya ATX (`#` syntax)
  - Tumia vizuizi vya msimbo vilivyo na vitambulisho vya lugha
  - Jumuisha maandishi ya maelezo kwa picha
  - Weka urefu wa mistari kuwa wa busara (hakuna kikomo kigumu, lakini uwe na busara)

### Mtindo wa Mifano ya Msimbo

#### TypeScript/JavaScript
- Tumia moduli za ES (`import`/`export`)
- Fuata kanuni za hali kali za TypeScript
- Jumuisha maelezo ya aina
- Lenga ES2022

#### Python
- Fuata miongozo ya mtindo wa PEP 8
- Tumia vidokezo vya aina inapofaa
- Jumuisha maelezo ya kazi na madarasa
- Tumia vipengele vya kisasa vya Python (3.8+)

#### Java
- Fuata kanuni za Spring Boot
- Tumia vipengele vya Java 21
- Fuata muundo wa mradi wa Maven wa kawaida
- Jumuisha maoni ya Javadoc

### Mpangilio wa Faili

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

## Ujenzi na Utekelezaji

### Utekelezaji wa Nyaraka

Hifadhi hutumia GitHub Pages au sawa kwa ajili ya kuhifadhi nyaraka (ikiwa inafaa). Mabadiliko kwenye tawi kuu husababisha:

1. Mtiririko wa kazi wa tafsiri (`.github/workflows/co-op-translator.yml`)
2. Tafsiri ya kiotomatiki ya faili zote za markdown za Kiingereza
3. Ujanibishaji wa picha inapohitajika

### Hakuna Mchakato wa Ujenzi Unaohitajika

Hifadhi hii ina nyaraka za markdown pekee. Hakuna hatua ya ujenzi au mkusanyiko inayohitajika kwa maudhui ya mtaala wa msingi.

### Utekelezaji wa Miradi ya Mfano

Miradi ya mfano ya mtu binafsi inaweza kuwa na maagizo ya utekelezaji:
- Tazama `03-GettingStarted/09-deployment/` kwa mwongozo wa utekelezaji wa seva ya MCP
- Mifano ya utekelezaji wa Azure Container Apps katika `11-MCPServerHandsOnLabs/`

## Miongozo ya Kuchangia

### Mchakato wa Ombi la Kuvuta

1. **Fork na Clone**: Fork hifadhi na clone fork yako kwa ndani
2. **Unda Tawi**: Tumia majina ya tawi yanayoelezea (mfano, `fix/typo-module-3`, `add/python-example`)
3. **Fanya Mabadiliko**: Hariri faili za markdown za Kiingereza pekee (si tafsiri)
4. **Jaribu kwa Ndani**: Hakikisha markdown inaonyeshwa vizuri
5. **Wasilisha PR**: Tumia vichwa na maelezo wazi vya PR
6. **CLA**: Saini Mkataba wa Leseni ya Mchangiaji wa Microsoft unapoulizwa

### Muundo wa Kichwa cha PR

Tumia vichwa vya wazi, vinavyoelezea:
- `[Module XX] Maelezo mafupi` kwa mabadiliko maalum ya moduli
- `[Samples] Maelezo` kwa mabadiliko ya msimbo wa mfano
- `[Docs] Maelezo` kwa masasisho ya nyaraka za jumla

### Nini cha Kuchangia

- Marekebisho ya hitilafu katika nyaraka au mifano ya msimbo
- Mifano mpya ya msimbo katika lugha za ziada
- Ufafanuzi na maboresho ya maudhui yaliyopo
- Masomo mapya ya kesi au mifano ya vitendo
- Ripoti za masuala kwa maudhui yasiyoeleweka au yasiyo sahihi

### Nini USIFANYE

- Usihariri faili moja kwa moja katika saraka ya `translations/`
- Usihariri saraka ya `translated_images/`
- Usiongeze faili kubwa za binary bila majadiliano
- Usibadilishe faili za mtiririko wa kazi wa tafsiri bila uratibu

## Vidokezo vya Ziada

### Matengenezo ya Hifadhi

- **Changelog**: Mabadiliko yote makubwa yanarekodiwa katika `changelog.md`
- **Mwongozo wa Kujifunza**: Tumia `study_guide.md` kwa muhtasari wa urambazaji wa mtaala
- **Violezo vya Masuala**: Tumia violezo vya masuala vya GitHub kwa ripoti za hitilafu na maombi ya vipengele
- **Kanuni za Maadili**: Wote wanaochangia lazima wafuate Kanuni za Maadili za Microsoft Open Source

### Njia ya Kujifunza

Fuata moduli kwa mpangilio (00-11) kwa kujifunza bora:
1. **00-02**: Misingi (Utangulizi, Dhana za Msingi, Usalama)
2. **03**: Kuanza na utekelezaji wa vitendo
3. **04-05**: Utekelezaji wa vitendo na mada za juu
4. **06-10**: Jamii, mbinu bora, na matumizi halisi
5. **11**: Maabara ya kina ya ujumuishaji wa hifadhidata (maabara 13 kwa mpangilio)

### Rasilimali za Msaada

- **Nyaraka**: https://modelcontextprotocol.io/
- **Vipimo**: https://spec.modelcontextprotocol.io/
- **Jamii**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Kozi Zinazohusiana**: Tazama README.md kwa njia nyingine za kujifunza za Microsoft

### Masuala ya Kawaida ya Utatuzi

**Q: PR yangu inashindwa ukaguzi wa tafsiri**
A: Hakikisha umehariri faili za markdown za Kiingereza pekee katika saraka za moduli za mizizi, si matoleo yaliyotafsiriwa.

**Q: Ninawezaje kuongeza lugha mpya?**
A: Msaada wa lugha unasimamiwa kupitia mtiririko wa kazi wa co-op-translator. Fungua suala kujadili kuongeza lugha mpya.

**Q: Mifano ya msimbo haifanyi kazi**
A: Hakikisha umefuata maagizo ya usanidi katika README ya mfano husika. Angalia kwamba una matoleo sahihi ya utegemezi yaliyosakinishwa.

**Q: Picha haziwezi kuonyeshwa**
A: Thibitisha njia za picha ni za jamaa na tumia mistari ya mbele. Picha zinapaswa kuwa katika saraka ya `images/` au `translated_images/` kwa matoleo yaliyotafsiriwa.

### Mazingatio ya Utendaji

- Mtiririko wa kazi wa tafsiri unaweza kuchukua dakika kadhaa kukamilika
- Picha kubwa zinapaswa kuboreshwa kabla ya kujitolea
- Weka faili za markdown za mtu binafsi zikiwa zinalenga na zenye ukubwa wa busara
- Tumia viungo vya jamaa kwa kubebeka bora

### Usimamizi wa Mradi

Mradi huu unafuata mbinu za chanzo huria za Microsoft:
- Leseni ya MIT kwa msimbo na nyaraka
- Kanuni za Maadili za Microsoft Open Source
- CLA inahitajika kwa michango
- Masuala ya usalama: Fuata miongozo ya SECURITY.md
- Msaada: Tazama SUPPORT.md kwa rasilimali za msaada

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
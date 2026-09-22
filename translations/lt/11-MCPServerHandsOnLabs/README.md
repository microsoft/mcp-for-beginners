# 🚀 MCP serveris su PostgreSQL – Pilnas mokymosi gidas

## 🧠 MCP duomenų bazės integracijos mokymosi kelio apžvalga

Šis išsamus mokymosi gidas moko, kaip sukurti gamybai paruoštus **Model Context Protocol (MCP) serverius**, integruotus su duomenų bazėmis, praktiško mažmeninės prekybos analizės įgyvendinimo pavyzdžiu. Išmoksite įmonių lygio modelių, įskaitant **eilutės lygio saugumą (RLS)**, **semantinę paiešką**, **Azure AI integraciją** ir **daugiaverslį duomenų prieigą**.

Nesvarbu, ar esate backend programuotojas, AI inžinierius, ar duomenų architektas, šis gidas suteikia struktūruotą mokymą su realaus pasaulio pavyzdžiais ir praktiniais užsiėmimais, kurie jus veda per šį MCP serverį https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Oficiali MCP medžiaga

- 📘 [MCP dokumentacija](https://modelcontextprotocol.io/) – Išsamūs vadovai ir naudotojų gairės
- 📜 [MCP specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokolo architektūra ir techninės nuorodos
- 🧑‍💻 [MCP GitHub saugykla](https://github.com/modelcontextprotocol) – Atviro kodo SDK, įrankiai ir kodo pavyzdžiai
- 🌐 [MCP bendruomenė](https://github.com/orgs/modelcontextprotocol/discussions) – Prisijunkite prie diskusijų ir prisidėkite prie bendruomenės
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Saugumo gerosios praktikos ir rizikų mažinimas


## 🧭 MCP duomenų bazės integracijos mokymosi kelias

### 📚 Pilna mokymosi struktūra https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratorija | Tema | Aprašymas | Nuoroda |
|--------|-------|-------------|------|
| **Laboratorijos 1-3: Pagrindai** | | | |
| 00 | [Įvadas į MCP duomenų bazės integraciją](./00-Introduction/README.md) | MCP su duomenų bazės integracija apžvalga ir mažmeninės prekybos analizės atvejis | [Pradėti čia](./00-Introduction/README.md) |
| 01 | [Pagrindinės architektūros sąvokos](./01-Architecture/README.md) | MCP serverio architektūros, duomenų bazių sluoksnių ir saugumo modelių supratimas | [Sužinoti](./01-Architecture/README.md) |
| 02 | [Sauga ir daugiaverslumas](./02-Security/README.md) | Eilutės lygio saugumas, autentifikacija ir daugiaverslė duomenų prieiga | [Sužinoti](./02-Security/README.md) |
| 03 | [Aplinkos paruošimas](./03-Setup/README.md) | Plėtros aplinkos, Docker, Azure resursų nustatymas | [Paruošti](./03-Setup/README.md) |
| **Laboratorijos 4-6: MCP serverio kūrimas** | | | |
| 04 | [Duomenų bazės dizainas ir schema](./04-Database/README.md) | PostgreSQL nustatymas, mažmeninės prekybos schemos kūrimas ir pavyzdiniai duomenys | [Kurti](./04-Database/README.md) |
| 05 | [MCP serverio įgyvendinimas](./05-MCP-Server/README.md) | FastMCP serverio kūrimas su duomenų bazės integracija | [Kurti](./05-MCP-Server/README.md) |
| 06 | [Įrankių kūrimas](./06-Tools/README.md) | Duomenų užklausų įrankių ir schemos introspekcijos kūrimas | [Kurti](./06-Tools/README.md) |
| **Laboratorijos 7-9: Pažangios funkcijos** | | | |
| 07 | [Semantinės paieškos integracija](./07-Semantic-Search/README.md) | Vektoriniai įterpimai su Azure OpenAI ir pgvector įgyvendinimas | [Išvystyti](./07-Semantic-Search/README.md) |
| 08 | [Testavimas ir derinimas](./08-Testing/README.md) | Testavimo strategijos, derinimo įrankiai ir patvirtinimo metodai | [Testuoti](./08-Testing/README.md) |
| 09 | [VS Code integracija](./09-VS-Code/README.md) | VS Code MCP integracijos ir AI pokalbių naudojimas | [Integruoti](./09-VS-Code/README.md) |
| **Laboratorijos 10-12: Gamyba ir gerosios praktikos** | | | |
| 10 | [Diegimo strategijos](./10-Deployment/README.md) | Docker diegimas, Azure Container Apps ir skalavimo sprendimai | [Diegti](./10-Deployment/README.md) |
| 11 | [Stebėsena ir matomumas](./11-Monitoring/README.md) | Application Insights, žurnalo vedimas, našumo stebėjimas | [Stebėti](./11-Monitoring/README.md) |
| 12 | [Gerosios praktikos ir optimizavimas](./12-Best-Practices/README.md) | Našumo optimizavimas, saugumo stiprinimas ir gamybos patarimai | [Optimizuoti](./12-Best-Practices/README.md) |

### 💻 Ką Jūs Sukursite

Baigę šį mokymosi kelią sukursite pilną **Zava mažmeninės prekybos analizės MCP serverį**, kuriame yra:

- **Daugialentelė mažmeninės prekybos duomenų bazė** su klientų užsakymais, produktais ir atsargomis
- **Eilutės lygio saugumas** parduotuvės duomenų izoliacijai
- **Semantinė produktų paieška** naudojant Azure OpenAI įterpimus
- **VS Code AI pokalbių integracija** natūralios kalbos užklausoms
- **Gamybai paruoštas diegimas** su Docker ir Azure
- **Išsami stebėsena** su Application Insights

## 🎯 Mokymosi išankstiniai reikalavimai

Norėdami kuo geriau išnaudoti šį mokymosi kelią, turėtumėte turėti:

- **Programavimo patirtį**: pažinimą su Python (pageidautina) arba panašiomis kalbomis
- **Duomenų bazių žinias**: bazinį SQL ir reliacinių duomenų bazių supratimą
- **API sąvokas**: REST API ir HTTP sąvokų supratimą
- **Programavimo įrankius**: komandinės eilutės, Git ir kodo redaktorių patirtį
- **Debesų pagrindus**: (neprivaloma) bazines Azure ar panašių debesų platformų žinias
- **Docker pažintį**: (neprivaloma) konteinerizacijos sąvokų supratimą

### Būtini įrankiai

- **Docker Desktop** – PostgreSQL ir MCP serverio paleidimui
- **Azure CLI** – debesų resursų diegimui
- **VS Code** – plėtrai ir MCP integracijai
- **Git** – versijų valdymui
- **Python 3.8+** – MCP serverio kūrimui

## 📚 Mokymosi vadovas ir ištekliai

Šis mokymosi kelias apima išsamią medžiagą, kuri padės jums efektyviai naršyti:

### Mokymosi vadovas

Kiekviena laboratorija apima:
- **Aiškūs mokymosi tikslai** – ką pasieksite
- **Žingsnis po žingsnio instrukcijos** – išsamios realizacijos gairės
- **Kodo pavyzdžiai** – veikiantys pavyzdžiai su paaiškinimais
- **Praktiniai užsiėmimai** – galimybės praktiškai išbandyti
- **Trikčių šalinimo gairės** – dažniausios problemos ir sprendimai
- **Papildomi ištekliai** – tolesnis skaitymas ir tyrinėjimas

### Išankstiniai reikalavimai

Prieš pradėdami kiekvieną laboratoriją, rasite:
- **Reikalingas žinias** – ką turite žinoti iš anksto
- **Aplinkos patikrinimą** – kaip patvirtinti aplinkos paruošimą
- **Laiko įverčius** – laukiamas užbaigimo laikas
- **Mokymosi rezultatus** – ką žinosite baigę

### Rekomenduojami mokymosi keliai

Pasirinkite kelią pagal savo patirties lygį:

#### 🟢 **Pradedančiųjų kelias** (Nauji MCP naudotojai)
1. Įsitikinkite, kad iš anksto baigėte 0-10 [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners)
2. Baikite užduotis 00-03, kad sutvirtintumėte pagrindus
3. Sekite laboratorijas 04-06 praktiniam kūrimui
4. Išbandykite laboratorijas 07-09 praktiniam naudojimui

#### 🟡 **Vidutinio lygio kelias** (Šiek tiek MCP patirties)
1. Peržiūrėkite laboratorijas 00-01 dėl duomenų bazės specifikos suvokimo
2. Koncentruokitės į laboratorijas 02-06 realizacijai
3. Gilinkitės į laboratorijas 07-12 dėl pažangių funkcijų

#### 🔴 **Pažengusiųjų kelias** (Patyrę MCP naudotojai)
1. Trumpai peržvelkite laboratorijas 00-03 kontekstui
2. Daug dėmesio skirkite laboratorijoms 04-09 dėl duomenų bazės integracijos
3. Susitelkite į laboratorijas 10-12 gamybiniam diegimui

## 🛠️ Kaip efektyviai naudotis šiuo mokymosi keliu

### Sekantis mokymasis (rekomenduojama)

Dirbkite laboratorijas iš eilės, kad gautumėte išsamų supratimą:

1. **Perskaitykite apžvalgą** – Supraskite, ką išmoksite
2. **Patikrinkite išankstinius reikalavimus** – Užtikrinkite reikalingas žinias
3. **Sekite žingsnis po žingsnio vadovus** – Įgyvendinkite mokydamiesi
4. **Atlikite pratimus** – Stiprinkite žinias
5. **Peržiūrėkite pagrindines išvadas** – Įtvirtinkite mokymosi rezultatus

### Tikslingas mokymasis

Jei reikia specifinių įgūdžių:

- **Duomenų bazės integracija**: koncentruokitės į laboratorijas 04-06
- **Saugumo įgyvendinimas**: skirkite dėmesį laboratorijoms 02, 08, 12
- **AI/Semantinė paieška**: gilinkitės į laboratoriją 07
- **Gamybinis diegimas**: studijuokite laboratorijas 10-12

### Praktiniai užsiėmimai

Kiekviena laboratorija apima:
- **Veikiančius kodo pavyzdžius** – kopijuokite, modifikuokite ir eksperimentuokite
- **Realaus pasaulio scenarijus** – praktinius mažmeninės prekybos analizės atvejus
- **Progresuojančią sudėtingumą** – nuo paprasto iki pažangaus
- **Patvirtinimo žingsnius** – įsitikinkite, kad įgyvendinimas veikia

## 🌟 Bendruomenė ir palaikymas

### Gaukite pagalbą

- **Azure AI Discord**: [Prisijunkite dėl ekspertų pagalbos](https://discord.com/invite/ByRwuEEgH4)
- **GitHub saugykla ir įgyvendinimo pavyzdys**: [Diegimo pavyzdys ir ištekliai](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP bendruomenė**: [Prisijunkite prie platesnių MCP diskusijų](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pasiruošę pradėti?

Pradėkite savo kelionę su **[Laboratorija 00: Įvadas į MCP duomenų bazės integraciją](./00-Introduction/README.md)**

---

*Išmokite kurti gamybai paruoštus MCP serverius su duomenų bazės integracija per šią išsamią praktinę mokymosi patirtį.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
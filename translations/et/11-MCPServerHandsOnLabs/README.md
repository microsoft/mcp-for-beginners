# 🚀 MCP Server PostgreSQL-ga – Täielik Õppejuhend

## 🧠 Ülevaade MCP andmebaasi integreerimise õpiteest

See põhjalik õppejuhend õpetab, kuidas luua tootmisvalmis **Model Context Protocol (MCP) servereid**, mis integreeruvad andmebaasidega praktilise jaemüügi analüütika rakenduse kaudu. Õpid ettevõtte tasemel mustreid, sealhulgas **ridade tasemel turvalisus (RLS)**, **semantiline otsing**, **Azure AI integratsioon** ja **mitme rentniku andmete ligipääs**.

Olenemata sellest, kas oled taustaarendaja, AI insener või andmearhitekt, pakub see juhend struktureeritud õppimist koos päriselu näidete ja praktiliste harjutustega, mis juhatavad sind läbi MCP serveri https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Ametlikud MCP ressursid

- 📘 [MCP dokumentatsioon](https://modelcontextprotocol.io/) – Üksikasjalikud õpetused ja kasutusjuhendid
- 📜 [MCP spetsifikatsioon](https://modelcontextprotocol.io/docs/) – Protokolli arhitektuur ja tehnilised viited
- 🧑‍💻 [MCP GitHubi repositoorium](https://github.com/modelcontextprotocol) – Avatud lähtekoodiga SDK-d, tööriistad ja koodinäited
- 🌐 [MCP kogukond](https://github.com/orgs/modelcontextprotocol/discussions) – Liitu aruteludega ja panusta kogukonda

## 🧭 MCP andmebaasi integreerimise õpitee

### 📚 Täielik õpistruktuur https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail jaoks

| Labor | Teema | Kirjeldus | Link |
|--------|-------|-------------|------|
| **Labor 1-3: Alused** | | | |
| 00 | [Sissejuhatus MCP andmebaasi integreerimisse](./00-Introduction/README.md) | Ülevaade MCP-st koos andmebaasi integreerimise ja jaemüügi analüütika kasutusjuhtumiga | [Alusta siit](./00-Introduction/README.md) |
| 01 | [Põhialused arhitektuurikontseptsioonid](./01-Architecture/README.md) | MCP serveri arhitektuuri, andmebaasikihtide ja turvalisusmustrite mõistmine | [Õpi](./01-Architecture/README.md) |
| 02 | [Turvalisus ja mitme rentniku tugi](./02-Security/README.md) | Ridade tasemel turvalisus, autentimine ja mitme rentniku andmete ligipääs | [Õpi](./02-Security/README.md) |
| 03 | [Keskkonna seadistamine](./03-Setup/README.md) | Arenduskeskkonna, Dockeri ja Azure'i ressursside seadistamine | [Seadista](./03-Setup/README.md) |
| **Labor 4-6: MCP serveri ehitamine** | | | |
| 04 | [Andmebaasi disain ja skeem](./04-Database/README.md) | PostgreSQL seadistamine, jaemüügi skeemi disain ja näidisandmed | [Ehita](./04-Database/README.md) |
| 05 | [MCP serveri rakendamine](./05-MCP-Server/README.md) | FastMCP serveri ehitamine koos andmebaasi integreerimisega | [Ehita](./05-MCP-Server/README.md) |
| 06 | [Tööriistade arendamine](./06-Tools/README.md) | Andmebaasi päringutööriistade ja skeemi introspektsiooni loomine | [Ehita](./06-Tools/README.md) |
| **Labor 7-9: Täiustatud funktsioonid** | | | |
| 07 | [Semantilise otsingu integreerimine](./07-Semantic-Search/README.md) | Vektorite sisestamine Azure OpenAI ja pgvectoriga | [Edenda](./07-Semantic-Search/README.md) |
| 08 | [Testimine ja silumine](./08-Testing/README.md) | Testimisstrateegiad, silumistööriistad ja valideerimismeetodid | [Testi](./08-Testing/README.md) |
| 09 | [VS Code integratsioon](./09-VS-Code/README.md) | VS Code MCP integratsiooni ja AI vestluse kasutamise seadistamine | [Integreeri](./09-VS-Code/README.md) |
| **Labor 10-12: Tootmine ja parimad praktikad** | | | |
| 10 | [Paigaldusstrateegiad](./10-Deployment/README.md) | Dockeri paigaldus, Azure Container Apps ja skaleerimise kaalutlused | [Paigalda](./10-Deployment/README.md) |
| 11 | [Jälgimine ja nähtavus](./11-Monitoring/README.md) | Application Insights, logimine, jõudluse jälgimine | [Jälgi](./11-Monitoring/README.md) |
| 12 | [Parimad praktikad ja optimeerimine](./12-Best-Practices/README.md) | Jõudluse optimeerimine, turvalisuse tugevdamine ja tootmisnõuanded | [Optimeeri](./12-Best-Practices/README.md) |

### 💻 Mida sa ehitad

Õpitee lõpuks oled ehitanud täieliku **Zava jaemüügi analüütika MCP serveri**, mis sisaldab:

- **Mitme tabeliga jaemüügi andmebaas** klientide tellimuste, toodete ja laoseisuga
- **Ridade tasemel turvalisus** poe põhise andmete eraldamiseks
- **Semantiline tooteotsing** Azure OpenAI sisestuste abil
- **VS Code AI vestluse integratsioon** loomuliku keele päringuteks
- **Tootmisvalmis paigaldus** Dockeriga ja Azure'iga
- **Terviklik jälgimine** Application Insightsiga

## 🎯 Õppimise eeldused

Et sellest õpiteest maksimumi võtta, peaksid omama:

- **Programmeerimiskogemus**: Pythoniga (soovitatav) või sarnaste keeltega
- **Andmebaasi teadmised**: SQL-i ja relatsiooniliste andmebaaside põhiteadmised
- **API kontseptsioonid**: REST API-de ja HTTP kontseptsioonide mõistmine
- **Arendustööriistad**: Käsurea, Git-i ja koodiredaktorite kasutamise kogemus
- **Pilve põhitõed**: (Valikuline) Azure'i või sarnaste pilveplatvormide põhiteadmised
- **Dockeri tundmine**: (Valikuline) Konteinerite kontseptsioonide mõistmine

### Vajalikud tööriistad

- **Docker Desktop** – PostgreSQL-i ja MCP serveri käitamiseks
- **Azure CLI** – Pilveressursside paigaldamiseks
- **VS Code** – Arenduseks ja MCP integratsiooniks
- **Git** – Versioonihalduseks
- **Python 3.8+** – MCP serveri arendamiseks

## 📚 Õppejuhend ja ressursid

See õpitee sisaldab põhjalikke ressursse, mis aitavad sul tõhusalt navigeerida:

### Õppejuhend

Iga labor sisaldab:
- **Selged õpieesmärgid** – Mida saavutad
- **Samm-sammult juhised** – Üksikasjalikud rakendusjuhendid
- **Koodinäited** – Töötavad näited koos selgitustega
- **Harjutused** – Praktilised harjutusvõimalused
- **Tõrkeotsingu juhendid** – Levinud probleemid ja lahendused
- **Täiendavad ressursid** – Edasine lugemine ja uurimine

### Eelduste kontroll

Enne iga labori alustamist leiad:
- **Nõutavad teadmised** – Mida peaksid eelnevalt teadma
- **Seadistuse valideerimine** – Kuidas oma keskkonda kontrollida
- **Ajahinnangud** – Eeldatav lõpetamise aeg
- **Õpitulemused** – Mida tead pärast lõpetamist

### Soovitatud õpiteed

Vali oma kogemustasemele vastav tee:

#### 🟢 **Algaja tee** (Uus MCP-s)
1. Veendu, et oled lõpetanud 0-10 [MCP algajatele](https://aka.ms/mcp-for-beginners)
2. Lõpeta laborid 00-03, et tugevdada aluseid
3. Järgi laboreid 04-06 praktiliseks ehitamiseks
4. Proovi laboreid 07-09 praktiliseks kasutamiseks

#### 🟡 **Kesktaseme tee** (Mõningane MCP kogemus)
1. Vaata üle laborid 00-01 andmebaasispetsiifiliste kontseptsioonide jaoks
2. Keskendu laboritele 02-06 rakendamiseks
3. Süvene laboritesse 07-12 täiustatud funktsioonide jaoks

#### 🔴 **Edasijõudnute tee** (Kogenud MCP-ga)
1. Sirvi laborid 00-03 konteksti jaoks
2. Keskendu laboritele 04-09 andmebaasi integreerimiseks
3. Keskendu laboritele 10-12 tootmise paigaldamiseks

## 🛠️ Kuidas seda õpiteed tõhusalt kasutada

### Järjestikune õppimine (soovitatav)

Tööta laborid järjest läbi, et saada terviklik arusaam:

1. **Loe ülevaadet** – Mõista, mida õpid
2. **Kontrolli eeldusi** – Veendu, et sul on vajalikud teadmised
3. **Järgi samm-sammult juhiseid** – Rakenda õppides
4. **Täida harjutused** – Tugevda oma arusaamist
5. **Vaata üle peamised punktid** – Kinnista õpitulemused

### Sihtotstarbeline õppimine

Kui vajad konkreetseid oskusi:

- **Andmebaasi integreerimine**: Keskendu laboritele 04-06
- **Turvalisuse rakendamine**: Keskendu laboritele 02, 08, 12
- **AI/semantiline otsing**: Süvene laborisse 07
- **Tootmise paigaldamine**: Uuri laboreid 10-12

### Praktiline harjutamine

Iga labor sisaldab:
- **Töötavaid koodinäiteid** – Kopeeri, muuda ja katseta
- **Päriselu stsenaariume** – Praktilised jaemüügi analüütika kasutusjuhtumid
- **Progressiivne keerukus** – Liikumine lihtsast keerukani
- **Valideerimissammud** – Kontrolli, et sinu rakendus töötab

## 🌟 Kogukond ja tugi

### Abi saamine

- **Azure AI Discord**: [Liitu ekspertide toetuseks](https://discord.com/invite/ByRwuEEgH4)
- **GitHubi repo ja rakenduse näidis**: [Paigaldusnäidis ja ressursid](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP kogukond**: [Liitu MCP aruteludega](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Valmis alustama?

Alusta oma teekonda **[Labor 00: Sissejuhatus MCP andmebaasi integreerimisse](./00-Introduction/README.md)**

---

*Valda tootmisvalmis MCP serverite ehitamist koos andmebaasi integreerimisega selle põhjaliku ja praktilise õpikogemuse kaudu.*

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
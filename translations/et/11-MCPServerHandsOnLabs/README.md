# 🚀 MCP server koos PostgreSQL-iga – täielik õppejuhend

## 🧠 Ülevaade MCP andmebaasi integreerimise õpitee kohta

See põhjalik õppejuhend õpetab, kuidas ehitada tootmiskõlblikke **Model Context Protocol (MCP) servereid**, mis integreeruvad andmebaasidega läbi praktilise jaemüügi analüüsi rakenduse. Õpid ettevõtte tasemel mustreid, sealhulgas **rida-tasandi turvalisus (RLS)**, **semantiline otsing**, **Azure AI integratsioon** ja **mitme kasutajaga andmete juurdepääs**.

Olgu su roll back-end arendaja, AI insener või andmearhitekt, see juhend pakub struktureeritud õppimist reaalse maailma näidete ja praktiliste harjutustega ning läbib MCP serveri https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Ametlikud MCP ressursid

- 📘 [MCP dokumentatsioon](https://modelcontextprotocol.io/) – Üksikasjalikud juhendid ja kasutajajuhendid
- 📜 [MCP spetsifikatsioon (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokolli arhitektuur ja tehnilised viited
- 🧑‍💻 [MCP GitHub hoidla](https://github.com/modelcontextprotocol) – Avatud lähtekoodiga SDK-d, tööriistad ja koodinäited
- 🌐 [MCP kogukond](https://github.com/orgs/modelcontextprotocol/discussions) – Liitu aruteludega ja panusta kogukonda
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Turvalisuse parimad tavad ja riskide maandamine


## 🧭 MCP andmebaasi integreerimise õpitee

### 📚 Täielik õpperida aadressil https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Labor | Teema | Kirjeldus | Link |
|--------|-------|-------------|------|
| **Labor 1-3: Alused** | | | |
| 00 | [Sissejuhatus MCP andmebaasi integreerimisse](./00-Introduction/README.md) | MCP ülevaade andmebaasi integratsiooni ja jaemüügi analüüsi näitel | [Alusta siin](./00-Introduction/README.md) |
| 01 | [Põhiarhitektuuri mõisted](./01-Architecture/README.md) | MCP serveri arhitektuuri, andmebaasi kihtide ja turvalisuse mustrite mõistmine | [Õpi](./01-Architecture/README.md) |
| 02 | [Turvalisus ja mitme kasutajaga ligipääs](./02-Security/README.md) | Rida tasandi turvalisus, autentimine ja mitme üürnikuga andmete juurdepääs | [Õpi](./02-Security/README.md) |
| 03 | [Keskkonna seadistamine](./03-Setup/README.md) | Arenduskeskkonna seadistamine, Docker, Azure ressursid | [Seadista](./03-Setup/README.md) |
| **Labor 4-6: MCP serveri ehitamine** | | | |
| 04 | [Andmebaaside disain ja skeem](./04-Database/README.md) | PostgreSQL seadistamine, jaemüügi skeemi disain ja näidisandmed | [Ehita](./04-Database/README.md) |
| 05 | [MCP serveri rakendamine](./05-MCP-Server/README.md) | FastMCP serveri ehitamine andmebaasi integratsiooniga | [Ehita](./05-MCP-Server/README.md) |
| 06 | [Tööriistade arendus](./06-Tools/README.md) | Andmebaasi päringu tööriistade ja skeemi introspektsiooni loomine | [Ehita](./06-Tools/README.md) |
| **Labor 7-9: Täiustatud funktsioonid** | | | |
| 07 | [Semantilise otsingu integratsioon](./07-Semantic-Search/README.md) | Vektorpõhiste manuste rakendamine Azure OpenAI ja pgvector abil | [Arenda](./07-Semantic-Search/README.md) |
| 08 | [Testimine ja silumine](./08-Testing/README.md) | Testimisstrateegiad, silumislahendused ja valideerimise meetodid | [Testi](./08-Testing/README.md) |
| 09 | [VS Code integratsioon](./09-VS-Code/README.md) | VS Code MCP integratsiooni ja AI vestluse seadistamine | [Integreeri](./09-VS-Code/README.md) |
| **Labor 10-12: Tootmine ja parimad praktikad** | | | |
| 10 | [Juurutamise strateegiad](./10-Deployment/README.md) | Dockeri juurutamine, Azure konteinerirakendused ja skaleerimine | [Juuruta](./10-Deployment/README.md) |
| 11 | [Jälgimine ja jälgitavus](./11-Monitoring/README.md) | Application Insights, logimine, jõudluse jälgimine | [Jälgi](./11-Monitoring/README.md) |
| 12 | [Parimad praktikad ja optimeerimine](./12-Best-Practices/README.md) | Jõudluse optimeerimine, turvalisuse tugevdamine ja tootmise näpunäited | [Optimeeri](./12-Best-Practices/README.md) |

### 💻 Mida sa ehitad

Selle õpitee lõpuks oled ehitanud täiskomplektse **Zava Retail Analytics MCP serveri**, mis sisaldab:

- **Mitmetabelilist jaemüügi andmebaasi** kliendi tellimuste, toodete ja laoseisuga
- **Rida tasandi turvalisust** poeandmete isolatsiooniks
- **Semantilist tooteteid** Azure OpenAI manustega
- **VS Code AI vestluse integratsiooni** loomulike keelepäringutega
- **Tootmiskõlblikku juurutamist** Dockeriga ja Azures
- **Terviklikku jälgimist** Application Insights abil

## 🎯 Õppimiseks vajalikud eeldused

Selle õpitee edukaks läbimiseks peaks sul olema:

- **Programmeerkogemus**: Tutvumine Pythoni (soovitatav) või teiste sarnaste keelidega
- **Andmebaasi teadmised**: Põhiline arusaam SQL-ist ja relatsioonilistest andmebaasidest
- **API mõisted**: REST API-de ja HTTP põhimõtete mõistmine
- **Arendustööriistad**: Kogemus käsurea, Giti ja koodiredaktoritega
- **Pilvepõhiteadmised**: (valikuline) Põhilised teadmised Azurist või sarnastest pilveteenustest
- **Dockeri tundmine**: (valikuline) Mõistmine konteineriseerimisest

### Vajalikud tööriistad

- **Docker Desktop** – PostgreSQL ja MCP serveri käivitamiseks
- **Azure CLI** – Pilveressursside juurutamiseks
- **VS Code** – Arenduseks ja MCP integratsiooniks
- **Git** – Versioonihalduseks
- **Python 3.8+** – MCP serveri arenduseks

## 📚 Õppejuhend ja ressursid

See õpitee sisaldab põhjalikke ressursse, mis aitavad sul sihtmärgini jõuda:

### Õppejuhend

Igas laboris on:
- **Selged õppimiseesmärgid** – Mida sa saavutad
- **Samm-sammult juhised** – Üksikasjalikud rakendusjuhendid
- **Koodi näited** – Töötavad näited selgitustega
- **Harjutused** – Praktilise osa võimalused
- **Veaotsingu juhendid** – Levinumad probleemid ja lahendused
- **Täiendavad ressursid** – Lisalugemised ja uurimistööd

### Eelduste kontroll

Iga labori alustamisel leiad:
- **Nõutavad teadmised** – Mida peaksid eelnevalt teadma
- **Keskkonna valideerimine** – Kuidas keskkonda kontrollida
- **Ajahinnangud** – Oodatav läbimise aeg
- **Õpitulemused** – Mida tead peale läbimist

### Soovitatud õpiread

Vali oma tee kogemuse järgi:

#### 🟢 **Algajate rada** (Uus MCP-ga)
1. Veendu, et oled lõpetanud esmalt 0-10 [MCP algajatele](https://aka.ms/mcp-for-beginners)
2. Läbige laborid 00-03, et tugevdada aluseid
3. Jälgi laboreid 04-06 praktilise ehitamise jaoks
4. Proovi laboreid 07-09 praktiliseks kasutamiseks

#### 🟡 **Kesktasemel rada** (Mõningane MCP kogemus)
1. Vaata üle laborid 00-01 andmebaasisõbralike mõistete jaoks
2. Keskendu laboreile 02-06 rakendamise jaoks
3. Süvene laboreisse 07-12 täiustatud funktsioonide jaoks

#### 🔴 **Arenenud rada** (Kogenud MCP kasutajad)
1. Läbi laborid 00-03 konteksti saamiseks
2. Keskendu laboreile 04-09 andmebaasi integratsiooniks
3. Pööra tähelepanu laboreile 10-12 tootmise juurutamiseks

## 🛠️ Kuidas seda õpiretke tõhusalt kasutada

### Järjestikune õppimine (Soovitatav)

Läbi kogu laborite järjekorra, et saada põhjalik arusaam:

1. **Loe ülevaadet** – Saan aru, mida õpid
2. **Kontrolli eeldusi** – Veendu oma vajalikes teadmistes
3. **Järgi samm-sammulisi juhiseid** – Rakenda neid õppides
4. **Tee harjutusi** – Tugevda oma arusaama
5. **Korda olulisemaid punkte** – Kinnista õpitulemused

### Sihtotstarbeline õppimine

Kui vajad spetsiifilisi oskusi:

- **Andmebaasi integratsioon**: Keskendu laboreile 04-06
- **Turvalisuse rakendamine**: Keskendu laboreile 02, 08, 12
- **AI/Semantiline otsing**: Süvene laboris 07
- **Tootmise juurutamine**: Õpi laboreid 10-12

### Praktiline harjutamine

Igas laboris on:
- **Töötavad koodi näited** – Kopeeri, muuda ja katseta
- **Reaalse maailma stsenaariumid** – Praktilised jaemüügi analüüsi kasutusjuhud
- **Samm-sammult kasvav keerukus** – Ehita lihtsast keerukamaks
- **Valideerimisetapid** – Kontrolli, et su rakendus töötab

## 🌟 Kogukond ja tugi

### Abi saamine

- **Azure AI Discord**: [Liitu eksperttoe saamiseks](https://discord.com/invite/ByRwuEEgH4)
- **GitHub hoidla ja rakendusnäide**: [Juurutamise näide ja ressursid](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP kogukond**: [Liitu laiemate MCP aruteludega](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Valmis alustama?

Alusta oma teekonda **[Labor 00: Sissejuhatus MCP andmebaasi integreerimisse](./00-Introduction/README.md)**

---

*Omandage tootmiskõlblike MCP serverite ehitamise oskus andmebaasi integreerimise kaudu selle põhjaliku ja praktilise õpikogemuse abil.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
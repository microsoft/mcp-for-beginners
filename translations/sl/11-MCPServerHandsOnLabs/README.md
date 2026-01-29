# 🚀 MCP strežnik s PostgreSQL - Celoten učni vodič

## 🧠 Pregled učne poti za integracijo MCP podatkovne baze

Ta obsežen učni vodič vas nauči, kako zgraditi produkcijsko pripravljene **Model Context Protocol (MCP) strežnike**, ki se povezujejo s podatkovnimi bazami prek praktične implementacije analitike v maloprodaji. Spoznali boste vzorce na ravni podjetja, vključno z **varnostjo na ravni vrstic (RLS)**, **semantičnim iskanjem**, **integracijo Azure AI** in **dostopom do podatkov za več najemnikov**.

Ne glede na to, ali ste razvijalec zaledja, inženir umetne inteligence ali podatkovni arhitekt, ta vodič ponuja strukturirano učenje z resničnimi primeri in praktičnimi vajami, ki vas vodijo skozi naslednji MCP strežnik https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Uradni MCP viri

- 📘 [MCP Dokumentacija](https://modelcontextprotocol.io/) – Podrobni vodiči in uporabniški priročniki
- 📜 [MCP Specifikacija](https://modelcontextprotocol.io/docs/) – Arhitektura protokola in tehnične reference
- 🧑‍💻 [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) – SDK-ji odprte kode, orodja in vzorčne kode
- 🌐 [MCP Skupnost](https://github.com/orgs/modelcontextprotocol/discussions) – Pridružite se razpravam in prispevajte k skupnosti

## 🧭 Učna pot za integracijo MCP podatkovne baze

### 📚 Celotna struktura učenja za https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratorij | Tema | Opis | Povezava |
|-------------|------|------|----------|
| **Lab 1-3: Osnove** | | | |
| 00 | [Uvod v integracijo MCP podatkovne baze](./00-Introduction/README.md) | Pregled MCP z integracijo podatkovne baze in primer uporabe analitike v maloprodaji | [Začni tukaj](./00-Introduction/README.md) |
| 01 | [Osnovni koncepti arhitekture](./01-Architecture/README.md) | Razumevanje arhitekture MCP strežnika, podatkovnih slojev in varnostnih vzorcev | [Nauči se](./01-Architecture/README.md) |
| 02 | [Varnost in večnajemništvo](./02-Security/README.md) | Varnost na ravni vrstic, avtentikacija in dostop do podatkov za več najemnikov | [Nauči se](./02-Security/README.md) |
| 03 | [Nastavitev okolja](./03-Setup/README.md) | Nastavitev razvojnega okolja, Docker, Azure virov | [Nastavi](./03-Setup/README.md) |
| **Lab 4-6: Gradnja MCP strežnika** | | | |
| 04 | [Oblikovanje podatkovne baze in shema](./04-Database/README.md) | Nastavitev PostgreSQL, oblikovanje sheme maloprodaje in vzorčni podatki | [Zgradi](./04-Database/README.md) |
| 05 | [Implementacija MCP strežnika](./05-MCP-Server/README.md) | Gradnja FastMCP strežnika z integracijo podatkovne baze | [Zgradi](./05-MCP-Server/README.md) |
| 06 | [Razvoj orodij](./06-Tools/README.md) | Ustvarjanje orodij za poizvedbe podatkovne baze in introspekcijo sheme | [Zgradi](./06-Tools/README.md) |
| **Lab 7-9: Napredne funkcije** | | | |
| 07 | [Integracija semantičnega iskanja](./07-Semantic-Search/README.md) | Implementacija vektorskih vdelav z Azure OpenAI in pgvector | [Napreduj](./07-Semantic-Search/README.md) |
| 08 | [Testiranje in odpravljanje napak](./08-Testing/README.md) | Strategije testiranja, orodja za odpravljanje napak in pristopi k validaciji | [Testiraj](./08-Testing/README.md) |
| 09 | [Integracija z VS Code](./09-VS-Code/README.md) | Konfiguracija integracije MCP z VS Code in uporaba AI klepeta | [Integriraj](./09-VS-Code/README.md) |
| **Lab 10-12: Produkcija in najboljše prakse** | | | |
| 10 | [Strategije uvajanja](./10-Deployment/README.md) | Uvajanje z Dockerjem, Azure Container Apps in premisleki o skaliranju | [Uvedi](./10-Deployment/README.md) |
| 11 | [Nadzor in opazovanje](./11-Monitoring/README.md) | Application Insights, beleženje, nadzor zmogljivosti | [Nadzoruj](./11-Monitoring/README.md) |
| 12 | [Najboljše prakse in optimizacija](./12-Best-Practices/README.md) | Optimizacija zmogljivosti, utrjevanje varnosti in nasveti za produkcijo | [Optimiziraj](./12-Best-Practices/README.md) |

### 💻 Kaj boste zgradili

Na koncu te učne poti boste zgradili popoln **Zava Retail Analytics MCP strežnik**, ki vključuje:

- **Podatkovno bazo za maloprodajo z več tabelami** s podatki o naročilih strank, izdelkih in zalogi
- **Varnost na ravni vrstic** za izolacijo podatkov po trgovinah
- **Semantično iskanje izdelkov** z uporabo vdelav Azure OpenAI
- **Integracijo AI klepeta v VS Code** za poizvedbe v naravnem jeziku
- **Produkcijsko pripravljeno uvajanje** z Dockerjem in Azure
- **Celovit nadzor** z Application Insights

## 🎯 Predpogoji za učenje

Da bi kar najbolje izkoristili to učno pot, bi morali imeti:

- **Izkušnje s programiranjem**: Poznavanje Pythona (priporočljivo) ali podobnih jezikov
- **Znanje o podatkovnih bazah**: Osnovno razumevanje SQL in relacijskih podatkovnih baz
- **Koncepti API-jev**: Razumevanje REST API-jev in konceptov HTTP
- **Razvojna orodja**: Izkušnje z ukazno vrstico, Gitom in urejevalniki kode
- **Osnove oblaka**: (Neobvezno) Osnovno znanje o Azure ali podobnih oblačnih platformah
- **Poznavanje Dockerja**: (Neobvezno) Razumevanje konceptov kontejnerizacije

### Potrebna orodja

- **Docker Desktop** - Za zagon PostgreSQL in MCP strežnika
- **Azure CLI** - Za uvajanje oblačnih virov
- **VS Code** - Za razvoj in integracijo MCP
- **Git** - Za nadzor različic
- **Python 3.8+** - Za razvoj MCP strežnika

## 📚 Učni vodič in viri

Ta učna pot vključuje obsežne vire, ki vam pomagajo pri učinkovitem navigiranju:

### Učni vodič

Vsak laboratorij vključuje:
- **Jasne učne cilje** - Kaj boste dosegli
- **Navodila po korakih** - Podrobni vodiči za implementacijo
- **Primeri kode** - Delujoči vzorci z razlagami
- **Vaje** - Priložnosti za praktično vadbo
- **Vodiči za odpravljanje težav** - Pogoste težave in rešitve
- **Dodatni viri** - Nadaljnje branje in raziskovanje

### Preverjanje predpogojev

Pred začetkom vsakega laboratorija boste našli:
- **Potrebno znanje** - Kaj bi morali vedeti vnaprej
- **Validacija nastavitev** - Kako preveriti svoje okolje
- **Časovne ocene** - Predviden čas za dokončanje
- **Rezultati učenja** - Kaj boste znali po zaključku

### Priporočene učne poti

Izberite svojo pot glede na raven izkušenj:

#### 🟢 **Pot za začetnike** (Novinci v MCP)
1. Poskrbite, da ste dokončali 0-10 [MCP za začetnike](https://aka.ms/mcp-for-beginners)
2. Dokončajte laboratorije 00-03 za utrditev osnov
3. Sledite laboratorijem 04-06 za praktično gradnjo
4. Preizkusite laboratorije 07-09 za praktično uporabo

#### 🟡 **Pot za srednje izkušene** (Nekaj izkušenj z MCP)
1. Preglejte laboratorije 00-01 za koncept specifičen za podatkovne baze
2. Osredotočite se na laboratorije 02-06 za implementacijo
3. Poglobite se v laboratorije 07-12 za napredne funkcije

#### 🔴 **Pot za napredne** (Izkušeni z MCP)
1. Preletite laboratorije 00-03 za kontekst
2. Osredotočite se na laboratorije 04-09 za integracijo podatkovne baze
3. Osredotočite se na laboratorije 10-12 za uvajanje v produkcijo

## 🛠️ Kako učinkovito uporabljati to učno pot

### Sekvenčno učenje (Priporočeno)

Sledite laboratorijem po vrsti za celovito razumevanje:

1. **Preberite pregled** - Razumite, kaj boste spoznali
2. **Preverite predpogoje** - Poskrbite, da imate potrebno znanje
3. **Sledite navodilom po korakih** - Implementirajte med učenjem
4. **Dokončajte vaje** - Utrdite svoje razumevanje
5. **Preglejte ključne točke** - Utrdite rezultate učenja

### Ciljno učenje

Če potrebujete specifične veščine:

- **Integracija podatkovne baze**: Osredotočite se na laboratorije 04-06
- **Implementacija varnosti**: Osredotočite se na laboratorije 02, 08, 12
- **AI/Semantično iskanje**: Poglobite se v laboratorij 07
- **Uvajanje v produkcijo**: Preučite laboratorije 10-12

### Praktična vadba

Vsak laboratorij vključuje:
- **Delujoče primere kode** - Kopirajte, prilagodite in eksperimentirajte
- **Resnične scenarije** - Praktični primeri uporabe analitike v maloprodaji
- **Postopno kompleksnost** - Gradnja od enostavnega do naprednega
- **Korake validacije** - Preverite, ali vaša implementacija deluje

## 🌟 Skupnost in podpora

### Pridobite pomoč

- **Azure AI Discord**: [Pridružite se za strokovno podporo](https://discord.com/invite/ByRwuEEgH4)
- **GitHub repozitorij in vzorčna implementacija**: [Vzorčno uvajanje in viri](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Skupnost**: [Pridružite se širšim razpravam o MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pripravljeni na začetek?

Začnite svojo pot z **[Lab 00: Uvod v integracijo MCP podatkovne baze](./00-Introduction/README.md)**

---

*Obvladajte gradnjo produkcijsko pripravljenih MCP strežnikov z integracijo podatkovne baze prek te obsežne, praktične učne izkušnje.*

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
# 🚀 MCP strežnik s PostgreSQL - popoln učni vodič

## 🧠 Pregled učne poti integracije MCP z bazo podatkov

Ta celovit učni vodič vas nauči, kako zgraditi produkcijsko pripravljene **strežnike Model Context Protocol (MCP)**, ki se povezujejo z bazami podatkov prek praktične implementacije analitike maloprodaje. Spoznali boste poslovne vzorce, kot so **Row Level Security (RLS)**, **semantično iskanje**, **integracija Azure AI** in **dostop do podatkov z več najemniki**.

Ne glede na to, ali ste razvijalec backend aplikacij, inženir AI ali podatkovni arhitekt, vam ta vodič nudi strukturirano učenje s primeri iz resničnega sveta in praktičnimi vajami, ki vas vodijo skozi https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail MCP strežnik.

## 🔗 Uradni viri MCP

- 📘 [Dokumentacija MCP](https://modelcontextprotocol.io/) – Podrobni vodiči in navodila za uporabnike
- 📜 [Specifikacija MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Arhitektura protokola in tehnične reference
- 🧑‍💻 [MCP GitHub repozitorij](https://github.com/modelcontextprotocol) – Odprtokodni SDK-ji, orodja in vzorci kode
- 🌐 [Skupnost MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Pridružite se razpravam in prispevajte skupnosti
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Najboljše varnostne prakse in zmanjševanje tveganj


## 🧭 Učna pot integracije MCP baze podatkov

### 📚 Celovita učna struktura za https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratorij | Tema | Opis | Povezava |
|--------|-------|-------------|------|
| **Laboratorij 1-3: Osnove** | | | |
| 00 | [Uvod v integracijo MCP z bazo podatkov](./00-Introduction/README.md) | Pregled MCP z integracijo baze podatkov in primer uporabe maloprodajne analitike | [Začni tukaj](./00-Introduction/README.md) |
| 01 | [Osnovni arhitekturni koncepti](./01-Architecture/README.md) | Razumevanje arhitekture MCP strežnika, plasti baze podatkov in varnostnih vzorcev | [Uči se](./01-Architecture/README.md) |
| 02 | [Varnost in večnajemniški dostop](./02-Security/README.md) | Row Level Security, avtentikacija in dostop do podatkov z več najemniki | [Uči se](./02-Security/README.md) |
| 03 | [Nastavitev okolja](./03-Setup/README.md) | Nastavitev razvojnega okolja, Docker, Azure viri | [Nastavi](./03-Setup/README.md) |
| **Laboratorij 4-6: Izgradnja MCP strežnika** | | | |
| 04 | [Oblikovanje baze podatkov in shema](./04-Database/README.md) | Nastavitev PostgreSQL, oblikovanje maloprodajne sheme in vzorčni podatki | [Zgradi](./04-Database/README.md) |
| 05 | [Implementacija MCP strežnika](./05-MCP-Server/README.md) | Izgradnja FastMCP strežnika z integracijo baze podatkov | [Zgradi](./05-MCP-Server/README.md) |
| 06 | [Razvoj orodij](./06-Tools/README.md) | Ustvarjanje orodij za poizvedbe baze podatkov in introspekcija sheme | [Zgradi](./06-Tools/README.md) |
| **Laboratorij 7-9: Napredne funkcije** | | | |
| 07 | [Integracija semantičnega iskanja](./07-Semantic-Search/README.md) | Implementacija vektorskih vdelav z Azure OpenAI in pgvector | [Napreduj](./07-Semantic-Search/README.md) |
| 08 | [Testiranje in odpravljanje napak](./08-Testing/README.md) | Testne strategije, orodja za odpravljanje napak in metode validacije | [Testiraj](./08-Testing/README.md) |
| 09 | [Integracija VS Code](./09-VS-Code/README.md) | Konfiguracija VS Code integracije MCP in uporaba AI klepeta | [Integriraj](./09-VS-Code/README.md) |
| **Laboratorij 10-12: Produkcija in najboljše prakse** | | | |
| 10 | [Strategije uvajanja](./10-Deployment/README.md) | Uvajanje z Dockerjem, Azure Container Apps in razmisleki o skaliranju | [Uvedi](./10-Deployment/README.md) |
| 11 | [Monitoring in opazovanje](./11-Monitoring/README.md) | Application Insights, beleženje, spremljanje zmogljivosti | [Spremljaj](./11-Monitoring/README.md) |
| 12 | [Najboljše prakse in optimizacija](./12-Best-Practices/README.md) | Optimizacija zmogljivosti, utrjevanje varnosti in nasveti za produkcijo | [Optimiziraj](./12-Best-Practices/README.md) |

### 💻 Kaj boste zgradili

Do konca te učne poti boste zgradili popoln **Zava Retail Analytics MCP strežnik** z naslednjimi značilnostmi:

- **Večtabelna maloprodajna baza podatkov** z naročili strank, izdelki in zalogami
- **Row Level Security** za izolacijo podatkov po trgovinah
- **Semantično iskanje izdelkov** z uporabo Azure OpenAI vdelav
- **Integracija VS Code AI Chat** za poizvedbe v naravnem jeziku
- **Produkcijsko uvajanje** z Dockerjem in Azure
- **Celovito spremljanje** z Application Insights

## 🎯 Predpogoj za učenje

Za kar najboljši izkoristek te učne poti bi morali:

- **Izkušnje s programiranjem**: Poznavanje Pythona (zaželeno) ali podobnih jezikov
- **Znanje baz podatkov**: Osnovno razumevanje SQL in relacijskih baz podatkov
- **API koncepti**: Razumevanje REST API-jev in HTTP konceptov
- **Razvojna orodja**: Izkušnje s ukazno vrstico, Gitom in urejevalniki kode
- **Osnove oblaka**: (neobvezno) Osnovno znanje Azure ali podobnih oblačnih platform
- **Poznavanje Dockerja**: (neobvezno) Razumevanje konceptov kontejnerizacije

### Potrebna orodja

- **Docker Desktop** - Za zagon PostgreSQL in MCP strežnika
- **Azure CLI** - Za uvajanje oblačnih virov
- **VS Code** - Za razvoj in integracijo MCP
- **Git** - Za upravljanje različic
- **Python 3.8+** - Za razvoj MCP strežnika

## 📚 Vodič za učenje in viri

Ta učna pot vključuje obsežne vire, ki vam pomagajo učinkovito napredovati:

### Vodič za učenje

Vsak laboratorij vključuje:
- **Jasne učne cilje** - Kaj boste dosegli
- **Navodila korak za korakom** - Podrobni vodiči za izvedbo
- **Primeri kode** - Delujoči vzorci s pojasnili
- **Vaje** - Priložnosti za praktično delo
- **Vodiči za odpravljanje težav** - Pogoste težave in rešitve
- **Dodatni viri** - Nadaljnje branje in raziskovanje

### Pregled predpogojev

Pred vsakim laboratorijem boste našli:
- **Zahtevano znanje** - Kaj morate vedeti vnaprej
- **Preverjanje nastavitve** - Kako preveriti okolje
- **Časovne ocene** - Pričakovan čas zaključka
- **Učni izidi** - Kaj boste znali po končanem laboratoriju

### Priporočene učne poti

Izberite pot glede na svojo raven izkušenj:

#### 🟢 **Začetniška pot** (novi v MCP)
1. Najprej dokončajte 0-10 [MCP za začetnike](https://aka.ms/mcp-for-beginners)
2. Dokončajte laboratorije od 00 do 03, da utrdite osnovno razumevanje
3. Sledite laboratorijem 04-06 za praktično izgradnjo
4. Poskusite laboratorije 07-09 za praktično uporabo

#### 🟡 **Vmesna pot** (nekaj izkušenj z MCP)
1. Preglejte laboratorije 00-01 za baze podatkov specifične koncepte
2. Osredotočite se na laboratorije 02-06 za implementacijo
3. Poglobite se v laboratorije 07-12 za napredne funkcije

#### 🔴 **Napredna pot** (izkušen z MCP)
1. Preglejte laboratorije 00-03 za kontekst
2. Osredotočite se na laboratorije 04-09 za integracijo baze podatkov
3. Osredotočite se na laboratorije 10-12 za produkcijsko uvajanje

## 🛠️ Kako učinkovito uporabljati to učno pot

### Zaporedno učenje (priporočeno)

Delajte laboratorije po vrsti za celovito razumevanje:

1. **Preberite pregled** - Razumete, kaj boste spoznali
2. **Preverite predpogoje** - Prepričajte se o zahtevanem znanju
3. **Sledite navodilom korak za korakom** - Izvedite med učenjem
4. **Dokončajte vaje** - Utrdite svoje razumevanje
5. **Preglejte ključne ugotovitve** - Utrdite učne rezultate

### Ciljno učenje

Če potrebujete specifične veščine:

- **Integracija baze podatkov**: Osredotočite se na laboratorije 04-06
- **Implementacija varnosti**: Osredotočite se na laboratorije 02, 08, 12
- **AI/semantično iskanje**: Poglobite se v laboratorij 07
- **Produkcijsko uvajanje**: Študirajte laboratorije 10-12

### Praktične vaje

Vsak laboratorij vključuje:
- **Delujoče primere kode** - Kopirajte, spreminjajte in eksperimentirajte
- **Primeri iz resničnega sveta** - Praktični primeri maloprodajne analitike
- **Progresivno zahtevnost** - Izgradnja od preprostega do naprednega
- **Preveritvene korake** - Potrdite, da vaša implementacija deluje

## 🌟 Skupnost in podpora

### Poiščite pomoč

- **Azure AI Discord**: [Pridružite se za strokovno podporo](https://discord.com/invite/ByRwuEEgH4)
- **GitHub repozitorij in vzorec implementacije**: [Vzorec uvajanja in viri](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Skupnost MCP**: [Pridružite se širšim razpravam MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Pripravljeni za začetek?

Začnite svojo pot z **[Laboratorij 00: Uvod v integracijo MCP z bazo podatkov](./00-Introduction/README.md)**

---

*Obvladovanje izgradnje produkcijsko pripravljenih MCP strežnikov z integracijo baz podatkov skozi ta celovit, praktičen učni pristop.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
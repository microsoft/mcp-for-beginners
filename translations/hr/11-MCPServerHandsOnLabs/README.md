# 🚀 MCP poslužitelj s PostgreSQL-om - Potpuni vodič za učenje

## 🧠 Pregled putanje učenja integracije MCP baze podataka

Ovaj sveobuhvatni vodič za učenje uči vas kako izgraditi produkcijski spremne **Model Context Protocol (MCP) poslužitelje** koji se integriraju s bazama podataka kroz praktičnu implementaciju maloprodajne analitike. Naučit ćete obrasce industrijske razine uključujući **Row Level Security (RLS)**, **semantičko pretraživanje**, **Azure AI integraciju** i **pristup podacima za više zakupaca**.

Bilo da ste backend razvijač, AI inženjer ili arhitekt podataka, ovaj vodič pruža strukturirano učenje s primjerima iz stvarnog svijeta i praktičnim vježbama koje vas vode kroz sljedeći MCP poslužitelj https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Službeni MCP resursi

- 📘 [MCP Dokumentacija](https://modelcontextprotocol.io/) – Detaljni tutorijali i korisnički vodiči
- 📜 [MCP Specifikacija (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Arhitektura protokola i tehničke reference
- 🧑‍💻 [MCP GitHub Repozitorij](https://github.com/modelcontextprotocol) – Open-source SDK-ovi, alati i uzorci koda
- 🌐 [MCP Zajednica](https://github.com/orgs/modelcontextprotocol/discussions) – Pridružite se raspravama i doprinesite zajednici
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Najbolje sigurnosne prakse i ublažavanje rizika


## 🧭 Putanja učenja integracije MCP baze podataka

### 📚 Potpuna struktura učenja za https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratorij | Tema | Opis | Veza |
|--------|-------|-------------|------|
| **Laboratorij 1-3: Osnove** | | | |
| 00 | [Uvod u integraciju MCP baze podataka](./00-Introduction/README.md) | Pregled MCP-a s integracijom baze podataka i upotrebni slučaj maloprodajne analitike | [Započni ovdje](./00-Introduction/README.md) |
| 01 | [Osnovni koncepti arhitekture](./01-Architecture/README.md) | Razumijevanje arhitekture MCP poslužitelja, slojeva baze podataka i sigurnosnih obrazaca | [Nauči](./01-Architecture/README.md) |
| 02 | [Sigurnost i višezakupnički pristup](./02-Security/README.md) | Row Level Security, autentikacija i višezakupnički pristup podacima | [Nauči](./02-Security/README.md) |
| 03 | [Postavljanje okruženja](./03-Setup/README.md) | Postavljanje razvojnih okruženja, Docker, Azure resursi | [Postavi](./03-Setup/README.md) |
| **Laboratorij 4-6: Izgradnja MCP poslužitelja** | | | |
| 04 | [Dizajn baze podataka i šema](./04-Database/README.md) | Postavljanje PostgreSQL-a, dizajn maloprodajne šeme i uzorci podataka | [Izgradi](./04-Database/README.md) |
| 05 | [Implementacija MCP poslužitelja](./05-MCP-Server/README.md) | Izgradnja FastMCP poslužitelja s integracijom baze podataka | [Izgradi](./05-MCP-Server/README.md) |
| 06 | [Razvoj alata](./06-Tools/README.md) | Izrada alata za upite baze i introspektivno ispitivanje šeme | [Izgradi](./06-Tools/README.md) |
| **Laboratorij 7-9: Napredne značajke** | | | |
| 07 | [Integracija semantičkog pretraživanja](./07-Semantic-Search/README.md) | Implementacija vektorskih ugrađivanja s Azure OpenAI i pgvector | [Napredni](./07-Semantic-Search/README.md) |
| 08 | [Testiranje i ispravljanje pogrešaka](./08-Testing/README.md) | Strategije testiranja, alati za debugiranje i pristupi validaciji | [Testiraj](./08-Testing/README.md) |
| 09 | [Integracija VS Code-a](./09-VS-Code/README.md) | Konfiguracija VS Code MCP integracije i korištenje AI chata | [Integriraj](./09-VS-Code/README.md) |
| **Laboratorij 10-12: Produkcija i najbolje prakse** | | | |
| 10 | [Strategije implementacije](./10-Deployment/README.md) | Docker implementacija, Azure Container Apps i razmatranja skaliranja | [Implementiraj](./10-Deployment/README.md) |
| 11 | [Praćenje i uočljivost](./11-Monitoring/README.md) | Application Insights, zapisivanje, praćenje performansi | [Nadzor](./11-Monitoring/README.md) |
| 12 | [Najbolje prakse i optimizacija](./12-Best-Practices/README.md) | Optimizacija performansi, jačanje sigurnosti i savjeti za produkciju | [Optimiziraj](./12-Best-Practices/README.md) |

### 💻 Što ćete izgraditi

Do kraja ove putanje učenja, izgradit ćete potpuni **Zava Retail Analytics MCP poslužitelj** koji uključuje:

- **Višestolnu maloprodajnu bazu podataka** s narudžbama kupaca, proizvodima i zalihama
- **Row Level Security** za izolaciju podataka po trgovinama
- **Semantičko pretraživanje proizvoda** koristeći Azure OpenAI ugrađivanja
- **VS Code AI Chat integraciju** za upite na prirodnom jeziku
- **Implementaciju spremnu za produkciju** s Dockerom i Azureom
- **Sveobuhvatno praćenje** putem Application Insights

## 🎯 Preduvjeti za učenje

Kako biste maksimalno iskoristili ovu putanju učenja, trebali biste imati:

- **Iskustvo u programiranju**: Poznavanje Pythona (poželjno) ili sličnih jezika
- **Znanje baze podataka**: Osnovno razumijevanje SQL-a i relacijskih baza podataka
- **API koncepti**: Razumijevanje REST API-ja i HTTP koncepata
- **Razvojni alati**: Iskustvo s komandnom linijom, Gitom i uređivačima koda
- **Osnove clouda**: (Neobavezno) Osnovno znanje Azurea ili sličnih cloud platformi
- **Poznavanje Dockera**: (Neobavezno) Razumijevanje kontejnerizacije

### Potrebni alati

- **Docker Desktop** - Za pokretanje PostgreSQL-a i MCP poslužitelja
- **Azure CLI** - Za implementaciju cloud resursa
- **VS Code** - Za razvoj i MCP integraciju
- **Git** - Za kontrolu verzija
- **Python 3.8+** - Za razvoj MCP poslužitelja

## 📚 Vodič za učenje i resursi

Ova putanja učenja uključuje sveobuhvatne resurse kako bi vam pomogla učinkovito napredovati:

### Vodič za učenje

Svaki laboratorij uključuje:
- **Jasne ciljeve učenja** - Što ćete postići
- **Upute korak po korak** - Detaljni vodiči za implementaciju
- **Primjere koda** - Radni uzorci s objašnjenjima
- **Vježbe** - Praktične prilike za vježbanje
- **Vodiče za rješavanje problema** - Uobičajeni problemi i rješenja
- **Dodatne resurse** - Daljnje čitanje i istraživanje

### Provjera preduvjeta

Prije početka svakog laboratorija naći ćete:
- **Potrebno znanje** - Što trebate znati unaprijed
- **Provjeru postavljanja** - Kako potvrditi vaše okruženje
- **Procjene vremena** - Očekivano vrijeme završetka
- **Ishode učenja** - Što ćete znati nakon završetka

### Preporučene putanje učenja

Odaberite svoj put prema razini iskustva:

#### 🟢 **Put početnika** (Novi u MCP-u)
1. Pobrinite se da ste prethodno završili 0-10 iz [MCP za početnike](https://aka.ms/mcp-for-beginners)
2. Završite laboratorije 00-03 za učvršćivanje temelja
3. Slijedite laboratorije 04-06 za praktičnu izgradnju
4. Isprobajte laboratorije 07-09 za praktičnu upotrebu

#### 🟡 **Srednji put** (Nekoliko iskustva s MCP-om)
1. Pregledajte laboratorije 00-01 za specifične koncepte baze podataka
2. Usredotočite se na laboratorije 02-06 za implementaciju
3. Zaronite duboko u laboratorije 07-12 za napredne značajke

#### 🔴 **Napredni put** (Iskusan s MCP-om)
1. Brzo pregledajte laboratorije 00-03 za kontekst
2. Usredotočite se na laboratorije 04-09 za integraciju baze podataka
3. Koncentrirajte se na laboratorije 10-12 za produkcijsku implementaciju

## 🛠️ Kako učinkovito koristiti ovu putanju učenja

### Sekvencijalno učenje (Preporučeno)

Prođite kroz laboratorije redoslijedom za sveobuhvatno razumijevanje:

1. **Pročitajte pregled** - Razumite što ćete naučiti
2. **Provjerite preduvjete** - Osigurajte da imate potrebno znanje
3. **Slijedite vodiče korak po korak** - Implementirajte dok učite
4. **Završite vježbe** - Učvrstite svoje razumijevanje
5. **Pregledajte glavne zaključke** - Utvrdite ishode učenja

### Ciljano učenje

Ako trebate specifične vještine:

- **Integracija baza podataka**: Usredotočite se na laboratorije 04-06
- **Implementacija sigurnosti**: Koncentrirajte se na laboratorije 02, 08, 12
- **AI/Semantičko pretraživanje**: Duboko proučite laboratorij 07
- **Produkcijska implementacija**: Proučite laboratorije 10-12

### Praktična vježba

Svaki laboratorij uključuje:
- **Radne primjere koda** - Kopirajte, modificirajte i eksperimentirajte
- **Scenarije iz stvarnog svijeta** - Praktični slučajevi maloprodajne analitike
- **Postupno složenost** - Izgradnja od jednostavnog do naprednog
- **Korake validacije** - Provjerite radi li vaša implementacija

## 🌟 Zajednica i podrška

### Dobijte pomoć

- **Azure AI Discord**: [Pridružite se za stručnu podršku](https://discord.com/invite/ByRwuEEgH4)
- **GitHub repo i primjer implementacije**: [Primjer implementacije i resursi](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP zajednica**: [Pridružite se širej MCP raspravi](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Spremni za početak?

Započnite svoje putovanje s **[Laboratorij 00: Uvod u integraciju MCP baze podataka](./00-Introduction/README.md)**

---

*Ovladavajte izgradnjom produkcijski spremnih MCP poslužitelja s integracijom baza podataka kroz ovaj sveobuhvatni, praktični program učenja.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
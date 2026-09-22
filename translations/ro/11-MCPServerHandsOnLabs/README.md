# 🚀 Server MCP cu PostgreSQL - Ghid complet de învățare

## 🧠 Prezentare generală a traseului de învățare pentru integrarea bazei de date MCP

Acest ghid complet de învățare te învață cum să construiești servere **Model Context Protocol (MCP)** gata de producție care se integrează cu baze de date printr-o implementare practică de analiză de retail. Vei învăța modele de nivel enterprise inclusiv **Securitate la nivel de rând (Row Level Security - RLS)**, **căutare semantică**, **integrare Azure AI** și **acces multi-chiriaș la date**.

Fie că ești dezvoltator backend, inginer AI sau arhitect de date, acest ghid oferă o învățare structurată cu exemple din viața reală și exerciții practice care te ghidează prin următorul server MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Resurse oficiale MCP

- 📘 [Documentația MCP](https://modelcontextprotocol.io/) – Tutoriale detaliate și ghiduri pentru utilizatori
- 📜 [Specificația MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Arhitectura protocolului și referințe tehnice
- 🧑‍💻 [Repository MCP pe GitHub](https://github.com/modelcontextprotocol) – SDK-uri open-source, unelte și exemple de cod
- 🌐 [Comunitatea MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Alătură-te discuțiilor și contribuie în comunitate
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Cele mai bune practici de securitate și atenuarea riscurilor


## 🧭 Traseul de învățare pentru integrarea bazei de date MCP

### 📚 Structura completă de învățare pentru https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laborator | Subiect | Descriere | Link |
|--------|-------|-------------|------|
| **Laboratoarele 1-3: Fundamente** | | | |
| 00 | [Introducere în integrarea bazei de date MCP](./00-Introduction/README.md) | Prezentare generală MCP cu integrare de baze de date și caz de utilizare pentru analiză de retail | [Începe aici](./00-Introduction/README.md) |
| 01 | [Concepte de arhitectură de bază](./01-Architecture/README.md) | Înțelegerea arhitecturii serverului MCP, straturilor bazei de date și modelelor de securitate | [Învață](./01-Architecture/README.md) |
| 02 | [Securitate și multichiriaș](./02-Security/README.md) | Securitate la nivel de rând, autentificare și acces multi-chiriaș la date | [Învață](./02-Security/README.md) |
| 03 | [Configurarea mediului](./03-Setup/README.md) | Configurarea mediului de dezvoltare, Docker, resurse Azure | [Configurează](./03-Setup/README.md) |
| **Laboratoarele 4-6: Construirea serverului MCP** | | | |
| 04 | [Proiectarea și schema bazei de date](./04-Database/README.md) | Configurare PostgreSQL, proiectarea schemei retail și date exemplu | [Construiește](./04-Database/README.md) |
| 05 | [Implementarea serverului MCP](./05-MCP-Server/README.md) | Construirea serverului FastMCP cu integrare în baza de date | [Construiește](./05-MCP-Server/README.md) |
| 06 | [Dezvoltarea uneltelor](./06-Tools/README.md) | Crearea uneltelor de interogare a bazei de date și introspecția schemei | [Construiește](./06-Tools/README.md) |
| **Laboratoarele 7-9: Funcții avansate** | | | |
| 07 | [Integrarea căutării semantice](./07-Semantic-Search/README.md) | Implementarea vector embeddings cu Azure OpenAI și pgvector | [Avansează](./07-Semantic-Search/README.md) |
| 08 | [Testare și depanare](./08-Testing/README.md) | Strategii de testare, unelte de depanare și metode de validare | [Testează](./08-Testing/README.md) |
| 09 | [Integrarea VS Code](./09-VS-Code/README.md) | Configurarea integrării MCP în VS Code și utilizarea AI Chat | [Integrează](./09-VS-Code/README.md) |
| **Laboratoarele 10-12: Producție și cele mai bune practici** | | | |
| 10 | [Strategii de implementare](./10-Deployment/README.md) | Implementarea cu Docker, Azure Container Apps și considerente pentru scalare | [Deplasează](./10-Deployment/README.md) |
| 11 | [Monitorizare și observabilitate](./11-Monitoring/README.md) | Application Insights, jurnalizare, monitorizarea performanței | [Monitorizează](./11-Monitoring/README.md) |
| 12 | [Cele mai bune practici și optimizare](./12-Best-Practices/README.md) | Optimizarea performanței, consolidarea securității și sfaturi pentru producție | [Optimizează](./12-Best-Practices/README.md) |

### 💻 Ce vei construi

La finalul acestui traseu de învățare, vei fi construit un complet **Server MCP de analiză retail Zava** care include:

- **Bază de date retail multi-tabel** cu comenzi clienți, produse și inventar
- **Securitate la nivel de rând** pentru izolarea datelor pe magazin
- **Căutare semantică a produselor** folosind embeddinguri Azure OpenAI
- **Integrare VS Code AI Chat** pentru interogări în limbaj natural
- **Implementare gata de producție** cu Docker și Azure
- **Monitorizare cuprinzătoare** cu Application Insights

## 🎯 Pregătiri pentru învățare

Pentru a obține maximul de pe acest traseu de învățare, ar trebui să ai:

- **Experiență în programare**: Familiaritate cu Python (preferat) sau limbaje similare
- **Cunoștințe de baze de date**: Înțelegere de bază a SQL și bazelor de date relaționale
- **Concepte API**: Înțelegerea API-urilor REST și a conceptelor HTTP
- **Unelte de dezvoltare**: Experiență cu linia de comandă, Git și editoare de cod
- **Noțiuni de cloud**: (Opțional) Cunoștințe de bază despre Azure sau platforme cloud similare
- **Familiaritate Docker**: (Opțional) Înțelegere a conceptelor de containerizare

### Unelte necesare

- **Docker Desktop** - Pentru rularea PostgreSQL și serverului MCP
- **Azure CLI** - Pentru implementarea resurselor cloud
- **VS Code** - Pentru dezvoltare și integrarea MCP
- **Git** - Pentru controlul versiunilor
- **Python 3.8+** - Pentru dezvoltarea serverului MCP

## 📚 Ghid de studiu și resurse

Acest traseu de învățare include resurse complete pentru a te ajuta să navighezi eficient:

### Ghid de studiu

Fiecare laborator include:
- **Obiective clare de învățare** - Ce vei realiza
- **Instrucțiuni pas cu pas** - Ghiduri detaliate de implementare
- **Exemple de cod** - Exemple funcționale cu explicații
- **Exerciții** - Oportunități de practică hands-on
- **Ghiduri de depanare** - Probleme frecvente și soluții
- **Resurse suplimentare** - Lecturi și explorări adiționale

### Verificarea pregătirii

Înainte de a începe fiecare laborator, vei găsi:
- **Cunoștințe necesare** - Ce ar trebui să știi în prealabil
- **Validarea configurării** - Cum să verifici mediul tău
- **Estimări de timp** - Timpul așteptat pentru finalizare
- **Rezultate de învățare** - Ce vei cunoaște după finalizare

### Trasee recomandate de învățare

Alege traseul în funcție de nivelul tău de experiență:

#### 🟢 **Traseu începător** (Nou în MCP)
1. Asigură-te că ai finalizat mai întâi 0-10 din [MCP pentru începători](https://aka.ms/mcp-for-beginners)
2. Finalizează laboratoarele 00-03 pentru a-ți consolida fundamentele
3. Urmează laboratoarele 04-06 pentru practică
4. Încearcă laboratoarele 07-09 pentru utilizare practică

#### 🟡 **Traseu intermediar** (Experiență MCP moderată)
1. Recapitulează laboratoarele 00-01 pentru concepte specifice bazei de date
2. Concentrează-te pe laboratoarele 02-06 pentru implementare
3. Aprofundează laboratoarele 07-12 pentru funcții avansate

#### 🔴 **Traseu avansat** (Cu experiență MCP)
1. Parcurge rapid laboratoarele 00-03 pentru context
2. Axă pe laboratoarele 04-09 pentru integrare în baza de date
3. Concentrează-te pe laboratoarele 10-12 pentru implementarea în producție

## 🛠️ Cum să folosești acest traseu de învățare eficient

### Învață secvențial (Recomandat)

Parcurge laboratoarele în ordine pentru o înțelegere cuprinzătoare:

1. **Citește prezentarea generală** - Înțelege ce vei învăța
2. **Verifică pregătirile** - Asigură-te că ai cunoștințele necesare
3. **Urmează ghidurile pas cu pas** - Implementează pe măsură ce înveți
4. **Finalizați exercițiile** - Consolidează-ți înțelegerea
5. **Revizuiește punctele cheie** - Consolidarea rezultatelor învățării

### Învățare țintită

Dacă ai nevoie de abilități specifice:

- **Integrarea bazei de date**: Concentrează-te pe laboratoarele 04-06
- **Implementarea securității**: Acordă atenție laboratoarelor 02, 08, 12
- **AI/Căutare semantică**: Aprofundează laboratorul 07
- **Implementare în producție**: Studiază laboratoarele 10-12

### Practică hands-on

Fiecare laborator include:
- **Exemple de cod funcționale** - Copiază, modifică și experimentează
- **Scenarii din lumea reală** - Cazuri practice de analiză retail
- **Complexitate progresivă** - Construiește de la simplu la avansat
- **Pași de validare** - Verifică dacă implementarea ta funcționează

## 🌟 Comunitate și suport

### Obține ajutor

- **Discord Azure AI**: [Alătură-te pentru suport de la experți](https://discord.com/invite/ByRwuEEgH4)
- **Repository GitHub și exemplu de implementare**: [Exemplu de implementare și resurse](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Comunitatea MCP**: [Participă la discuții mai largi MCP](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Ești gata să începi?

Pornește-ți călătoria cu **[Laboratorul 00: Introducere în integrarea bazei de date MCP](./00-Introduction/README.md)**

---

*Dezvoltă servere MCP gata de producție cu integrare în bazele de date prin această experiență cuprinzătoare și practică de învățare.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
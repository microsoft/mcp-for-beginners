# Case Study: Azure AI Travel Agents – Referentna Implementacija

## Pregled

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) je sveobuhvatno referentno rješenje koje je razvio Microsoft, a koje pokazuje kako izgraditi aplikaciju za planiranje putovanja s više agenata pokretanih umjetnom inteligencijom koristeći Model Context Protocol (MCP), Azure OpenAI i Azure AI Search. Ovaj projekt prikazuje najbolje prakse za koordinaciju više AI agenata, integraciju podataka iz poduzeća te pružanje sigurne i proširive platforme za stvarne scenarije.

## Ključne Značajke
- **Orkestracija Više Agenata:** Koristi MCP za koordinaciju specijaliziranih agenata (npr. agenti za letove, hotele i itinerere) koji surađuju kako bi ispunili složene zadatke planiranja putovanja.
- **Integracija Podataka iz Poduzeća:** Povezuje se s Azure AI Search i drugim izvorima podataka poduzeća kako bi pružio ažurirane i relevantne informacije za preporuke putovanja.
- **Sigurna i Skalabilna Arhitektura:** Iskorištava Azure usluge za autentifikaciju, autorizaciju i skalabilno postavljanje, slijedeći najbolje sigurnosne prakse za poduzeća.
- **Proširivi Alati:** Implementira ponovno upotrebljive MCP alate i predloške za promptove, omogućujući brzu prilagodbu novim domenama ili poslovnim zahtjevima.
- **Korisničko Iskustvo:** Pruža konverzacijsko sučelje za interakciju korisnika s agentima za putovanja, pokretano Azure OpenAI i MCP-om.

## Arhitektura
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Opis Dijagrama Arhitekture

Rješenje Azure AI Travel Agents dizajnirano je za modularnost, skalabilnost i sigurnu integraciju više AI agenata i izvora podataka poduzeća. Glavne komponente i tok podataka su sljedeći:

- **Korisničko Sučelje:** Korisnici komuniciraju sa sustavom putem konverzacijskog UI-ja (poput web chata ili Teams bota), koji šalje upite korisnika i prima preporuke za putovanja.
- **MCP Server:** Djeluje kao središnji orkestrator, prima korisničke ulaze, upravlja kontekstom i koordinira rad specijaliziranih agenata (npr. FlightAgent, HotelAgent, ItineraryAgent) putem Model Context Protocol-a.
- **AI Agenti:** Svaki agent je zadužen za određenu domenu (letovi, hoteli, itinereri) i implementiran je kao MCP alat. Agenti koriste predloške promptova i logiku za obradu zahtjeva i generiranje odgovora.
- **Azure OpenAI Service:** Pruža napredno razumijevanje i generiranje prirodnog jezika, omogućujući agentima da interpretiraju korisničke namjere i generiraju konverzacijske odgovore.
- **Azure AI Search & Podaci Poduzeća:** Agenti pretražuju Azure AI Search i druge izvore podataka poduzeća kako bi dohvatili najnovije informacije o letovima, hotelima i opcijama putovanja.
- **Autentifikacija i Sigurnost:** Integrira se s Microsoft Entra ID za sigurnu autentifikaciju i primjenjuje kontrole pristupa s najmanjim privilegijama na sve resurse.
- **Postavljanje:** Dizajnirano za postavljanje na Azure Container Apps, osiguravajući skalabilnost, nadzor i operativnu učinkovitost.

Ova arhitektura omogućuje besprijekornu orkestraciju više AI agenata, sigurnu integraciju s podacima poduzeća i robusnu, proširivu platformu za izgradnju AI rješenja specifičnih za domenu.

## Korak-po-korak Objašnjenje Dijagrama Arhitekture
Zamislite da planirate veliko putovanje i imate tim stručnih pomoćnika koji vam pomažu sa svakim detaljem. Sustav Azure AI Travel Agents radi na sličan način, koristeći različite dijelove (kao članove tima) od kojih svaki ima posebnu ulogu. Evo kako se sve uklapa:

### Korisničko Sučelje (UI):
Zamislite ovo kao recepciju vašeg putničkog agenta. Tu vi (korisnik) postavljate pitanja ili dajete zahtjeve, poput "Pronađi mi let za Pariz." To može biti chat prozor na web stranici ili aplikacija za poruke.

### MCP Server (Koordinator):
MCP Server je poput menadžera koji sluša vaš zahtjev na recepciji i odlučuje koji stručnjak treba obraditi svaki dio. On prati vašu konverzaciju i osigurava da sve teče glatko.

### AI Agenti (Stručni Pomoćnici):
Svaki agent je stručnjak za određeno područje – jedan zna sve o letovima, drugi o hotelima, a treći o planiranju itinerera. Kad zatražite putovanje, MCP Server šalje vaš zahtjev pravom agentu ili agentima. Ti agenti koriste svoje znanje i alate da pronađu najbolje opcije za vas.

### Azure OpenAI Service (Stručnjak za Jezik):
To je kao da imate stručnjaka za jezik koji točno razumije što tražite, bez obzira kako to izrazite. Pomaže agentima da shvate vaše zahtjeve i odgovore prirodnim, konverzacijskim jezikom.

### Azure AI Search & Podaci Poduzeća (Informacijska Knjižnica):
Zamislite ogromnu, ažuriranu knjižnicu sa svim najnovijim informacijama o putovanjima – rasporedima letova, dostupnosti hotela i slično. Agenti pretražuju tu knjižnicu kako bi vam dali najtočnije odgovore.

### Autentifikacija i Sigurnost (Čuvar Sigurnosti):
Baš kao što čuvar sigurnosti provjerava tko može ući u određene prostorije, ovaj dio osigurava da samo ovlaštene osobe i agenti mogu pristupiti osjetljivim informacijama. Čuva vaše podatke sigurnima i privatnima.

### Postavljanje na Azure Container Apps (Zgrada):
Svi ovi pomoćnici i alati rade zajedno unutar sigurne, skalabilne zgrade (oblaka). To znači da sustav može istovremeno podržati mnogo korisnika i uvijek je dostupan kad vam treba.

## Kako sve funkcionira zajedno:

Počinjete tako da postavite pitanje na recepciji (UI).
Menadžer (MCP Server) odlučuje koji stručnjak (agent) će vam pomoći.
Stručnjak koristi jezičnog eksperta (OpenAI) da razumije vaš zahtjev i knjižnicu (AI Search) da pronađe najbolji odgovor.
Čuvar sigurnosti (Autentifikacija) osigurava da je sve sigurno.
Sve se to događa unutar pouzdane, skalabilne zgrade (Azure Container Apps), pa je vaše iskustvo glatko i sigurno.
Ova suradnja omogućuje sustavu da brzo i sigurno pomogne u planiranju vašeg putovanja, baš kao tim stručnih putničkih agenata koji rade zajedno u modernom uredu!

## Tehnička Implementacija
- **MCP Server:** Hostira osnovnu logiku orkestracije, izlaže alate agenata i upravlja kontekstom za višestepene tijekove planiranja putovanja.
- **Agenti:** Svaki agent (npr. FlightAgent, HotelAgent) implementiran je kao MCP alat sa svojim predlošcima promptova i logikom.
- **Azure Integracija:** Koristi Azure OpenAI za razumijevanje prirodnog jezika i Azure AI Search za dohvat podataka.
- **Sigurnost:** Integrira se s Microsoft Entra ID za autentifikaciju i primjenjuje kontrole pristupa s najmanjim privilegijama na sve resurse.
- **Postavljanje:** Podržava postavljanje na Azure Container Apps radi skalabilnosti i operativne učinkovitosti.

## Rezultati i Utjecaj
- Pokazuje kako se MCP može koristiti za orkestraciju više AI agenata u stvarnom, produkcijskom okruženju.
- Ubrzava razvoj rješenja pružajući ponovno upotrebljive obrasce za koordinaciju agenata, integraciju podataka i sigurno postavljanje.
- Služi kao nacrt za izgradnju domena-specifičnih, AI-pokretanih aplikacija koristeći MCP i Azure usluge.

## Reference
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
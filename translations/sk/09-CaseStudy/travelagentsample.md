# Prípadová štúdia: Azure AI Travel Agents – Referenčná implementácia

## Prehľad

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) je komplexné referenčné riešenie vyvinuté spoločnosťou Microsoft, ktoré ukazuje, ako vytvoriť viacagentovú aplikáciu na plánovanie ciest poháňanú umelou inteligenciou pomocou Model Context Protocol (MCP), Azure OpenAI a Azure AI Search. Tento projekt predstavuje osvedčené postupy pre koordináciu viacerých AI agentov, integráciu podnikových dát a poskytovanie bezpečnej, rozšíriteľnej platformy pre reálne scenáre.

## Kľúčové vlastnosti
- **Koordinácia viacerých agentov:** Využíva MCP na koordináciu špecializovaných agentov (napr. agenti pre lety, hotely a itineráre), ktorí spolupracujú na riešení komplexných úloh plánovania ciest.
- **Integrácia podnikových dát:** Pripája sa k Azure AI Search a ďalším podnikových zdrojom dát, aby poskytol aktuálne a relevantné informácie pre odporúčania na cestovanie.
- **Bezpečná a škálovateľná architektúra:** Využíva Azure služby pre autentifikáciu, autorizáciu a škálovateľné nasadenie, pričom dodržiava najlepšie bezpečnostné postupy pre podniky.
- **Rozšíriteľné nástroje:** Implementuje znovupoužiteľné MCP nástroje a šablóny promptov, čo umožňuje rýchlu adaptáciu na nové oblasti alebo obchodné požiadavky.
- **Používateľská skúsenosť:** Poskytuje konverzačné rozhranie, cez ktoré môžu používatelia komunikovať s cestovnými agentmi, poháňané Azure OpenAI a MCP.

## Architektúra
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Popis architektonického diagramu

Riešenie Azure AI Travel Agents je navrhnuté s dôrazom na modularitu, škálovateľnosť a bezpečnú integráciu viacerých AI agentov a podnikových zdrojov dát. Hlavné komponenty a tok dát sú nasledovné:

- **Používateľské rozhranie:** Používatelia komunikujú so systémom cez konverzačné UI (napríklad webový chat alebo Teams bot), ktoré odosiela používateľské otázky a prijíma odporúčania na cestovanie.
- **MCP Server:** Slúži ako centrálny koordinátor, ktorý prijíma vstupy od používateľa, spravuje kontext a koordinuje činnosť špecializovaných agentov (napr. FlightAgent, HotelAgent, ItineraryAgent) cez Model Context Protocol.
- **AI agenti:** Každý agent je zodpovedný za konkrétnu oblasť (lety, hotely, itineráre) a je implementovaný ako MCP nástroj. Agenti používajú šablóny promptov a logiku na spracovanie požiadaviek a generovanie odpovedí.
- **Azure OpenAI Service:** Poskytuje pokročilé porozumenie a generovanie prirodzeného jazyka, čo umožňuje agentom interpretovať úmysly používateľa a vytvárať konverzačné odpovede.
- **Azure AI Search & podnikové dáta:** Agenti vyhľadávajú v Azure AI Search a ďalších podnikových zdrojoch dát, aby získali aktuálne informácie o letoch, hoteloch a možnostiach cestovania.
- **Autentifikácia a bezpečnosť:** Integruje sa s Microsoft Entra ID pre bezpečnú autentifikáciu a uplatňuje princíp najmenších práv na všetky zdroje.
- **Nasadenie:** Navrhnuté pre nasadenie na Azure Container Apps, čo zabezpečuje škálovateľnosť, monitorovanie a efektívnu prevádzku.

Táto architektúra umožňuje plynulú koordináciu viacerých AI agentov, bezpečnú integráciu s podnikových dátami a robustnú, rozšíriteľnú platformu pre tvorbu doménovo špecifických AI riešení.

## Podrobný popis architektonického diagramu krok za krokom
Predstavte si, že plánujete veľkú cestu a máte tím odborných asistentov, ktorí vám pomáhajú s každým detailom. Systém Azure AI Travel Agents funguje podobne, využíva rôzne časti (ako členov tímu), z ktorých každý má svoju špecializovanú úlohu. Takto to všetko spolu funguje:

### Používateľské rozhranie (UI):
Predstavte si to ako recepciu vášho cestovného agenta. Tu vy (používateľ) kladiete otázky alebo zadávate požiadavky, napríklad „Nájdi mi let do Paríža.“ Môže to byť chatové okno na webovej stránke alebo v aplikácii na odosielanie správ.

### MCP Server (Koordinátor):
MCP Server je ako manažér, ktorý počúva vašu požiadavku na recepcii a rozhoduje, ktorý špecialista by mal riešiť jednotlivé časti. Sleduje priebeh konverzácie a zabezpečuje, že všetko prebieha hladko.

### AI agenti (Špecializovaní asistenti):
Každý agent je expert na konkrétnu oblasť – jeden pozná všetko o letoch, iný o hoteloch a ďalší o plánovaní itinerárov. Keď požiadate o cestu, MCP Server odošle vašu požiadavku správnemu agentovi alebo agentom. Tí využívajú svoje znalosti a nástroje na nájdenie najlepších možností pre vás.

### Azure OpenAI Service (Jazykový expert):
Je to ako mať jazykového experta, ktorý presne rozumie, čo žiadate, bez ohľadu na to, ako to formulujete. Pomáha agentom pochopiť vaše požiadavky a odpovedať prirodzeným, konverzačným spôsobom.

### Azure AI Search & podnikové dáta (Informačná knižnica):
Predstavte si obrovskú, aktuálnu knižnicu so všetkými najnovšími informáciami o cestovaní – letové poriadky, dostupnosť hotelov a ďalšie. Agenti túto knižnicu prehľadávajú, aby vám poskytli najpresnejšie odpovede.

### Autentifikácia a bezpečnosť (Strážca bezpečnosti):
Rovnako ako strážca kontroluje, kto môže vstúpiť do určitých priestorov, táto časť zabezpečuje, že len oprávnené osoby a agenti majú prístup k citlivým informáciám. Chráni vaše dáta a súkromie.

### Nasadenie na Azure Container Apps (Budova):
Všetci títo asistenti a nástroje spolupracujú v bezpečnej, škálovateľnej budove (v cloude). To znamená, že systém zvládne veľa používateľov naraz a je vždy dostupný, keď ho potrebujete.

## Ako to všetko spolu funguje:

Začnete tým, že položíte otázku na recepcii (UI).  
Manažér (MCP Server) rozhodne, ktorý špecialista (agent) vám pomôže.  
Špecialista využije jazykového experta (OpenAI), aby pochopil vašu požiadavku, a knižnicu (AI Search), aby našiel najlepšiu odpoveď.  
Strážca bezpečnosti (Autentifikácia) zabezpečí, že je všetko v poriadku.  
To všetko prebieha v spoľahlivej, škálovateľnej budove (Azure Container Apps), takže vaša skúsenosť je plynulá a bezpečná.  
Táto spolupráca umožňuje systému rýchlo a bezpečne pomôcť s plánovaním vašej cesty, presne ako tím odborných cestovných agentov pracujúcich v modernom kancelárskom prostredí!

## Technická implementácia
- **MCP Server:** Hostuje jadrovú logiku koordinácie, sprístupňuje nástroje agentov a spravuje kontext pre viacstupňové pracovné postupy plánovania ciest.
- **Agenti:** Každý agent (napr. FlightAgent, HotelAgent) je implementovaný ako MCP nástroj so svojimi vlastnými šablónami promptov a logikou.
- **Integrácia s Azure:** Využíva Azure OpenAI pre porozumenie prirodzenému jazyku a Azure AI Search pre získavanie dát.
- **Bezpečnosť:** Integruje sa s Microsoft Entra ID pre autentifikáciu a uplatňuje princíp najmenších práv na všetky zdroje.
- **Nasadenie:** Podporuje nasadenie na Azure Container Apps pre škálovateľnosť a efektívnu prevádzku.

## Výsledky a dopad
- Ukazuje, ako možno MCP využiť na koordináciu viacerých AI agentov v reálnom, produkčnom prostredí.
- Urýchľuje vývoj riešení poskytovaním znovupoužiteľných vzorov pre koordináciu agentov, integráciu dát a bezpečné nasadenie.
- Slúži ako vzor pre tvorbu doménovo špecifických aplikácií poháňaných AI pomocou MCP a Azure služieb.

## Referencie
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
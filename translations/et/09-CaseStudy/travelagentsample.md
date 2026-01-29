# Juhtumiuuring: Azure AI reisibürood – viiteimplementatsioon

## Ülevaade

[Azure AI reisibürood](https://github.com/Azure-Samples/azure-ai-travel-agents) on Microsofti poolt välja töötatud terviklik viitelahendus, mis näitab, kuidas luua mitme agendiga, tehisintellektiga juhitud reisiplaneerimise rakendust, kasutades Model Context Protocol (MCP), Azure OpenAI ja Azure AI Search teenuseid. Projekt demonstreerib parimaid praktikaid mitme AI agendi orkestreerimisel, ettevõtte andmete integreerimisel ja turvalise, laiendatava platvormi pakkumisel reaalseks kasutamiseks.

## Põhifunktsioonid
- **Mitme agendi orkestreerimine:** Kasutab MCP-d spetsialiseeritud agentide (nt lennu-, hotelli- ja reisikava agendid) koordineerimiseks, kes teevad koostööd keerukate reisiplaneerimise ülesannete täitmiseks.
- **Ettevõtte andmete integreerimine:** Ühendub Azure AI Search ja teiste ettevõtte andmeallikatega, et pakkuda ajakohast ja asjakohast teavet reisisoovituste jaoks.
- **Turvaline ja skaleeritav arhitektuur:** Kasutab Azure teenuseid autentimiseks, autoriseerimiseks ja skaleeritavaks juurutamiseks, järgides ettevõtte turvalisuse parimaid tavasid.
- **Laiendatav tööriistakomplekt:** Rakendab korduvkasutatavaid MCP tööriistu ja viipemalle, võimaldades kiiret kohandamist uute valdkondade või ärinõuete jaoks.
- **Kasutajakogemus:** Pakub vestlusliidest, mille kaudu kasutajad saavad reisibüroodega suhelda, kasutades Azure OpenAI ja MCP-d.

## Arhitektuur
![Arhitektuur](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Arhitektuuri diagrammi kirjeldus

Azure AI reisibüroode lahendus on loodud modulaarsuse, skaleeritavuse ja turvalise integreerimise jaoks mitme AI agendi ja ettevõtte andmeallikatega. Peamised komponendid ja andmevoog on järgmised:

- **Kasutajaliides:** Kasutajad suhtlevad süsteemiga vestlusliidese kaudu (nt veebivestlus või Teams bot), mis saadab kasutaja päringuid ja saab reisisoovitusi.
- **MCP server:** Toimib keskse orkestreerijana, võtab vastu kasutaja sisendi, haldab konteksti ja koordineerib spetsialiseeritud agentide (nt FlightAgent, HotelAgent, ItineraryAgent) tegevusi Model Context Protocol abil.
- **AI agendid:** Iga agent vastutab konkreetse valdkonna eest (lennud, hotellid, reisikavad) ja on rakendatud MCP tööriistana. Agendid kasutavad viipemalle ja loogikat päringute töötlemiseks ja vastuste genereerimiseks.
- **Azure OpenAI teenus:** Pakub arenenud loomuliku keele mõistmist ja genereerimist, võimaldades agentidel tõlgendada kasutaja kavatsusi ja luua vestluslikke vastuseid.
- **Azure AI Search ja ettevõtte andmed:** Agendid pärivad Azure AI Search ja teistest ettevõtte andmeallikatest, et saada ajakohast teavet lendude, hotellide ja reisivõimaluste kohta.
- **Autentimine ja turvalisus:** Integreerub Microsoft Entra ID-ga turvaliseks autentimiseks ja rakendab kõigile ressurssidele minimaalse juurdepääsu kontrolli.
- **Juurutamine:** Kavandatud juurutamiseks Azure Container Apps-is, tagades skaleeritavuse, jälgimise ja operatiivse tõhususe.

See arhitektuur võimaldab mitme AI agendi sujuvat orkestreerimist, turvalist integreerimist ettevõtte andmetega ja tugeva, laiendatava platvormi loomist valdkonnaspetsiifiliste AI lahenduste jaoks.

## Arhitektuuri diagrammi samm-sammuline selgitus
Kujutage ette, et plaanite suurt reisi ja teil on ekspertide meeskond, kes aitab teid igas detailis. Azure AI reisibüroode süsteem töötab sarnaselt, kasutades erinevaid osi (nagu meeskonnaliikmeid), millest igaühel on eriline ülesanne. Siin on, kuidas kõik kokku sobitub:

### Kasutajaliides (UI):
Mõelge sellele kui reisibüroo vastuvõtulauale. See on koht, kus teie (kasutaja) esitate küsimusi või teete päringuid, näiteks „Leia mulle lend Pariisi.“ See võib olla vestlusaken veebisaidil või sõnumirakenduses.

### MCP server (koordinaator):
MCP server on nagu juht, kes kuulab teie päringut vastuvõtulauas ja otsustab, milline spetsialist peaks iga osa käsitlema. See jälgib teie vestlust ja tagab, et kõik toimib sujuvalt.

### AI agendid (spetsialistid):
Iga agent on ekspert konkreetses valdkonnas – üks teab kõike lendudest, teine hotellidest ja kolmas teie reisikava planeerimisest. Kui te küsite reisi kohta, saadab MCP server teie päringu õigetele agentidele. Need agendid kasutavad oma teadmisi ja tööriistu, et leida teile parimad võimalused.

### Azure OpenAI teenus (keeleekspert):
See on nagu keeleekspert, kes mõistab täpselt, mida te küsite, olenemata sellest, kuidas te seda sõnastate. See aitab agentidel teie päringuid mõista ja vastata loomulikus, vestluslikus keeles.

### Azure AI Search ja ettevõtte andmed (infokogu):
Kujutage ette suurt, ajakohast raamatukogu, kus on kõik uusimad reisiteave – lennugraafikud, hotellide saadavus ja palju muud. Agendid otsivad sellest raamatukogust kõige täpsemaid vastuseid teie jaoks.

### Autentimine ja turvalisus (turvamees):
Nagu turvamees, kes kontrollib, kes pääseb teatud aladele, tagab see osa, et ainult volitatud isikud ja agendid pääsevad tundlikule teabele. See hoiab teie andmed turvalisena ja privaatsena.

### Juurutamine Azure Container Apps-is (hoone):
Kõik need assistendid ja tööriistad töötavad koos turvalises, skaleeritavas hoones (pilves). See tähendab, et süsteem suudab korraga teenindada palju kasutajaid ja on alati saadaval, kui te seda vajate.

## Kuidas kõik koos töötab:

Te alustate küsimuse esitamisega vastuvõtulauas (UI).
Juht (MCP server) otsustab, milline spetsialist (agent) peaks teid aitama.
Spetsialist kasutab keeleeksperti (OpenAI), et teie päringut mõista, ja raamatukogu (AI Search), et leida parim vastus.
Turvamees (autentimine) tagab, et kõik on turvaline.
Kõik see toimub usaldusväärses, skaleeritavas hoones (Azure Container Apps), et teie kogemus oleks sujuv ja turvaline.
See meeskonnatöö võimaldab süsteemil kiiresti ja turvaliselt aidata teil oma reisi planeerida, nagu ekspertide reisibüroode meeskond, kes töötab koos kaasaegses kontoris!

## Tehniline teostus
- **MCP server:** Majutab põhiorkestreerimisloogikat, pakub agentide tööriistu ja haldab konteksti mitmeastmeliste reisiplaneerimise töövoogude jaoks.
- **Agendid:** Iga agent (nt FlightAgent, HotelAgent) on rakendatud MCP tööriistana, millel on oma viipemallid ja loogika.
- **Azure integratsioon:** Kasutab Azure OpenAI-d loomuliku keele mõistmiseks ja Azure AI Search-i andmete pärimiseks.
- **Turvalisus:** Integreerub Microsoft Entra ID-ga autentimiseks ja rakendab kõigile ressurssidele minimaalse juurdepääsu kontrolli.
- **Juurutamine:** Toetab juurutamist Azure Container Apps-is skaleeritavuse ja operatiivse tõhususe tagamiseks.

## Tulemused ja mõju
- Näitab, kuidas MCP-d saab kasutada mitme AI agendi orkestreerimiseks reaalses, tootmiskvaliteediga stsenaariumis.
- Kiirendab lahenduste arendamist, pakkudes korduvkasutatavaid mustreid agentide koordineerimiseks, andmete integreerimiseks ja turvaliseks juurutamiseks.
- Toimib juhendina valdkonnaspetsiifiliste, tehisintellektiga juhitud rakenduste loomiseks MCP ja Azure teenuste abil.

## Viited
- [Azure AI reisibüroode GitHubi hoidla](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI teenus](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
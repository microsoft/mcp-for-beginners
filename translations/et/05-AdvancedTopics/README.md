# Täiustatud teemad MCP-s

[![Täiustatud MCP: Turvalised, skaleeritavad ja multimodaalsed tehisintellekti agendid](../../../translated_images/et/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Klõpsake ülaloleval pildil, et vaadata selle tunni videot)_

Käesolev peatükk käsitleb keerukamaid teemasid Mudeli Konteksti Protokolli (MCP) rakendamises, sealhulgas multimodaalset integreerimist, skaleeritavust, turvalisuse parimaid tavasid ja ettevõtluse integreerimist. Need teemad on olulised vastupidavate ja tootmiskõlblike MCP rakenduste loomiseks, mis suudavad vastata tänapäevaste tehisintellektisüsteemide nõuetele.

## Ülevaade

See tund uurib täiustatud mõisteid Mudeli Konteksti Protokolli rakendamises, keskendudes multimodaalsele integratsioonile, skaleeritavusele, turvalisuse parimatele tavadele ja ettevõtete integreerimisele. Need teemad on hädavajalikud tootmiskõlblike MCP rakenduste loomisel, mis suudavad toime tulla keerukate nõudmistega ettevõttekeskkondades.

> **Praeguse spetsifikatsiooni märkus:** MCP `2026-07-28` aeglustab Roots ja
> proovivõtu primitiive, mida käsitletakse tundides 5.4 ja 5.6. Samuti liigub
> eksperimenteeriv Tasks funktsioon, mis on viidatud Protokolli funktsioonides (5.16), nüüd
> pühendatud Tasks laiendusse. Need õppetunnid on säilitatud pärandi
> `2025-11-25` rakenduste jaoks ja sisaldavad migratsiooni juhiseid. Vaata
> [Mis on MCP-s muutunud: spetsifikatsioon 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md).

## Õpieesmärgid

Selle tunni lõpuks oskate:

- Rakendada multimodaalseid võimalusi MCP raamistikus
- Kujundada skaleeritavaid MCP arhitektuure kõrge nõudlusega olukordadeks
- Rakendada turvalisuse parimaid tavasid, mis on kooskõlas MCP turvaprintsiipidega
- Integreerida MCP ettevõtte AI süsteemidega ja raamistikuga
- Optimeerida jõudlust ja töökindlust tootmiskeskkondades

## Õppetunnid ja näidisprojektid

| Link | Pealkiri | Kirjeldus |
|------|----------|-----------|
| [5.1 Integratsioon Azure'iga](./mcp-integration/README.md) | Integratsioon Azure'iga | Õppige, kuidas integreerida oma MCP server Azure'is |
| [5.2 Multimodaalne näidis](./mcp-multi-modality/README.md) | MCP multimodaalsed näidised  | Näidised heli, pildi ja multimodaalse vastusega |
| [5.3 MCP OAuth2 näidis](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 demo | Minimalistlik Spring Boot rakendus, mis demonstreerib OAuth2 kasutamist MCP-ga nii autoriseerimise kui ka ressursside serverina. Näitab turvalist tokenite väljastamist, kaitstud otspunktide loomist, Azure Container Apps'i deploy’d ja API halduse integratsiooni. |
| [5.4 Juurekontekstid](./mcp-root-contexts/README.md) | Juurekontekstid  | Õppige pärandi `2025-11-25` Roots primitiivi ja praegused migratsioonivõimalused (aeglustatud `2026-07-28`) |
| [5.5 Marsruutimine](./mcp-routing/README.md) | Marsruutimine | Õppige erinevaid marsruutimise tüüpe |
| [5.6 Proovivõtt](./mcp-sampling/README.md) | Proovivõtt | Õppige pärandi `2025-11-25` proovivõtu primitiivi ja praegused migratsioonivõimalused (aeglustatud `2026-07-28`) |
| [5.7 Skaleerimine](./mcp-scaling/README.md) | Skaleerimine  | Õppige skaleerimisest |
| [5.8 Turvalisus](./mcp-security/README.md) | Turvalisus  | Tagage oma MCP serveri turvalisus |
| [5.9 Veebiotsingu näidis](./web-search-mcp/README.md) | Veebiotsing MCP | Python MCP server ja klient integratsiooniga SerpAPI-ga reaalajas veebipõhise, uudiste, toodete otsinguks ja küsimuste-vastuste halduseks. Demonstreerib mitme tööriista orkestreerimist, välist API integratsiooni ja tugevat vigade käsitlemist. |
| [5.10 Reaalaja voogedastus](./mcp-realtimestreaming/README.md) | Voogedastus  | Reaalaja andmevoogude edastamine on tänapäeva andmepõhises maailmas hädavajalik, kuna ettevõtted ja rakendused vajavad teabele kohest juurdepääsu õigeaegsete otsuste tegemiseks.|
| [5.11 Reaalaja veebipõhine otsing](./mcp-realtimesearch/README.md) | Veebiotsing | Reaalaja veebipõhine otsing: kuidas MCP muudab reaalaja veebipõhist otsingut, pakkudes standardiseeritud lähenemist konteksti juhtimisele AI mudelite, otsingumootorite ja rakenduste vahel.| 
| [5.12 Entra ID autentimine Model Context Protocol serveritele](./mcp-security-entra/README.md) | Entra ID autentimine | Microsoft Entra ID pakub tugevat pilvepõhist identiteedi- ja juurdepääsuhalduse lahendust, mis tagab, et ainult volitatud kasutajad ja rakendused saavad suhelda teie MCP serveriga.|
| [5.13 Microsoft Foundry agendi integratsioon](./mcp-foundry-agent-integration/README.md) | Microsoft Foundry integratsioon | Õppige, kuidas integreerida Mudeli Konteksti Protokolli serverid Microsoft Foundry agentidega, võimaldades võimsa tööriistade orkestreerimise ja ettevõtte AI võimekuse standardiseeritud välistest andmeallikatest ühenduste kaudu.|
| [5.14 Konteksti inseneritehnika](./mcp-contextengineering/README.md) | Konteksti inseneritehnika | MCP serverite konteksti inseneritehnika tuleviku võimalused, sh konteksti optimeerimine, dünaamiline konteksti haldus ja tõhusa promptide inseneritöö strateegiad MCP raamistikus.|
| [5.15 MCP kohandatud transpordimehhanism](./mcp-transport/README.md) | Kohandatud transpordimehhanism | Õppige, kuidas rakendada kohandatud transpordimehhanisme spetsiaalseks MCP suhtlusolukordades.|
| [5.16 Protokolli funktsioonide süvitsi uurimine](./mcp-protocol-features/README.md) | Protokolli funktsioonid | Valdage täiustatud protokolli funktsioone, sealhulgas edenemiseteated, päringu tühistamine, ressursitemplid ja vigade käsitlusmustrid.|
| [5.17 Vastuoluline mitmeagendiline mõtlemine](./mcp-adversarial-agents/README.md) | Vastuolulised agendid | Kasutage kahte agenti vastandlike seisukohtadega, jagades ühte MCP tööriistakomplekti, et tabada hallutsinatsioone, tuua välja äärealasid ja toota paremini kalibreeritud tulemusi läbi struktureeritud debati.|

> **Ajalooline `2025-11-25` märkus:** see versioon tutvustas eksperimenteerivaid
> Tasks funktsioone ja laiendas mitmeid protokolli omadusi. Versioonis `2026-07-28` liikus Tasks
> ametlikku laiendusse ja Roots sai aegluseks. Ärge kasutage
> `2025-11-25` funktsioonistaatust praeguste juhistena; vaadake
> [2026-07-28 muudatuste logi](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Täiendavad viited

Kõige ajakohasema teabe saamiseks täiustatud MCP teemadel, vaadake:
- [MCP dokumentatsioon](https://modelcontextprotocol.io/)
- [MCP spetsifikatsioon (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHubi hoidla](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Turvariskid ja leevendused
- [MCP turvalisuse tippkohtumise töötuba (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktiline turvakoolitus

## Põhipunktid

- Mitmemodaalsed MCP rakendused laiendavad tehisintellekti võimalusi tekstipõhisest töötlemisest kaugemale
- Skaleeritavus on ettevõtte kasutusele võtmisel kriitiline ning seda saab lahendada horisontaalse ja vertikaalse skaleerimisega
- Ulatuslikud turvameetmed kaitsevad andmeid ja tagavad nõuetekohase juurdepääsukontrolli
- Ettevõtte integratsioon platvormidega nagu Azure OpenAI ja Microsoft AI Foundry suurendab MCP võimekust
- Täiustatud MCP rakendused saavad kasu optimeeritud arhitektuuridest ja hoolikast ressursside haldamisest

## Harjutus

Kujundage ettevõttele sobiv MCP rakendus konkreetse kasutusjuhtumi jaoks:

1. Määrake oma kasutusjuhtumi multimodaalsed nõuded
2. Kirjeldage turvakontrollid, mis on vajalikud tundlike andmete kaitseks
3. Kujundage skaleeritav arhitektuur, mis suudab toime tulla muutuvate koormustega
4. Planeerige integratsioonipunktid ettevõtte AI süsteemidega
5. Dokumenteerige võimalikud jõudluspiirangud ja leevendusstrateegiad

## Täiendavad ressursid

- [Azure OpenAI dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/ai-services/)

---

## Mis järgmiseks

Uurige selle mooduli õppetunde, alustades: [5.1 MCP integratsioon](./mcp-integration/README.md)

Kui olete selle mooduli lõpetanud, jätkake: [Moodul 6: Kogukonna panused](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
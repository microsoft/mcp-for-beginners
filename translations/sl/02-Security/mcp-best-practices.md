# Najboljše varnostne prakse MCP - Posodobitev september 2026

Ta obsežen vodič predstavlja ključne varnostne najboljše prakse za
implementacijo sistemov Model Context Protocol (MCP) na podlagi
**MCP specifikacije 2026-07-28** in trenutnih industrijskih standardov. Te
prakse naslovijo tako tradicionalne varnostne izzive kot tudi grožnje, specifične za AI,
edinstvene za MCP implementacije.

## Kritične varnostne zahteve

### Obvezni varnostni ukrepi (ZAHTEVE)

1. **Preverjanje žetonov**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso bili izrecno izdani za samega MCP strežnika
2. **Preverjanje pooblastil**: MCP strežniki, ki izvajajo pooblastila, **MORAJO** preveriti VSE vhodne zahteve in **NE SMEJO** uporabljati sej za preverjanje pristnosti  
3. **Privolitev uporabnika**: MCP proxy strežniki, ki uporabljajo statične trojne ID-je odjemalcev, **MORAJO** pridobiti izrecno privolitev za vsakega MCP odjemalca pred posredovanjem toka avtentikacije
4. **Varnost upravljalnika stanja**: MCP strežniki **NE SMEJO** obravnavati posedovanje
	vrednosti stanja aplikacije kot overjanje in **MORAJO** pooblastiti vsak
	zahtevek, ki ga uporablja

## Osnovne varnostne prakse

### 1. Preverjanje in čiščenje vhodov
- **Celovito preverjanje vhodov**: Preverite in očistite vse vhode, da preprečite napade z injekcijo, probleme z zmedeno pooblastitvijo in ranljivosti z injiciranjem pozivov
- **Izvajanje struktur parametrov**: Uvedite strogo preverjanje JSON shem za vse parametre orodij in API vhodov
- **Filtriranje vsebine**: Uporabite Microsoft Prompt Shields in Azure Content Safety za filtriranje zlonamerne vsebine v pozivih in odzivih
- **Čiščenje izhodov**: Preverite in očistite vse izhode modelov pred prikazom uporabnikom ali nadaljnjim sistemom

### 2. Odličnost avtentikacije in pooblastil  
- **Zunanji ponudniki identitete**: Predelegirajte avtentikacijo uveljavljenim ponudnikom identitete (Microsoft Entra ID, ponudniki OAuth 2.1) namesto implementacije lastne avtentikacije
- **Registracija odjemalcev**: Raje uporabljajte dokumente o metapodatkih ID odjemalcev ali predhodno registracijo; zastarelo Dinamično registracijo odjemalcev uporabite samo za združljivost
- **Natančna dovoljenja**: Uvedite granulirana dovoljenja, specifična za orodja, po principu najmanjših pravic
- **Upravljanje življenjskega cikla žetonov**: Uporabljajte kratkožive dostopne žetone s varnim rotiranjem in pravilnim preverjanjem ciljne publike
- **Večfaktorska avtentikacija**: Zahtevajte MFA za vse administratorske dostope in občutljive operacije

### 3. Varnostni komunikacijski protokoli
- **Varnost sloja transporta**: Uporabljajte HTTPS z ustreznim preverjanjem certifikatov
	za oddaljene HTTP MCP komunikacije; uporabite izolacijo procesov in
	okoljske poverilnice za lokalne stdio strežnike
- **Šifriranje od konca do konca**: Uvedite dodatne plasti šifriranja za zelo občutljive podatke v prenosu in na mestu shranjevanja
- **Upravljanje certifikatov**: Vzdržujte pravilen življenjski cikel certifikatov z avtomatiziranimi postopki podaljševanja
- **Izvajanje različice protokola**: Uporabite MCP `2026-07-28`, vključite zahtevane
	metapodatke o verziji pri vsakem zahtevku in zavrnite nepodprte verzije

### 4. Napredno omejevanje hitrosti in zaščita virov
- **Večplastno omejevanje hitrosti**: Implementirajte omejevanje hitrosti po uporabniku, poverilnicah,
  operacijah, orodjih in virih, da preprečite zlorabo
- **Prilagodljivo omejevanje hitrosti**: Uporabite omejevanje hitrosti, temelječe na strojno učenih vzorcih uporabe in indikatorjih groženj
- **Upravljanje kvote virov**: Nastavite ustrezne omejitve za računske vire, porabo pomnilnika in čas izvajanja
- **Zaščita pred DDoS**: Uporabite celovite zaščitne in analitične sisteme za DDoS in promet

### 5. Celovito beleženje in nadzor
- **Strukturirano revizijsko beleženje**: Implementirajte podrobne, iskane dnevnike za vse MCP operacije, izvajanje orodij in varnostne dogodke
- **Varnostni nadzor v realnem času**: Uporabite SIEM sisteme z AI-poganjano zaznavo anomalij za MCP delovne obremenitve
- **Beleženje skladno z zasebnostjo**: Beležite varnostne dogodke ob spoštovanju zahtev in predpisov varstva podatkov
- **Integracija odziva na incidente**: Povežite beleženje z avtomatiziranimi delovnimi tokovi za odziv na incidente

### 6. Izboljšane prakse varnega shranjevanja
- **Strojni varnostni moduli**: Uporabljajte HSM-podprto shranjevanje ključev (Azure Key Vault, AWS CloudHSM) za kritične kriptografske operacije
- **Upravljanje šifrirnih ključev**: Izvajajte ustrezno rotacijo, ločevanje in nadzor dostopa za šifrirne ključe
- **Upravljanje skrivnosti**: Shranjujte vse API ključe, žetone in poverilnice v namenskih sistemih za upravljanje skrivnosti
- **Klasifikacija podatkov**: Razvrščajte podatke glede na nivo občutljivosti in uporabljajte ustrezne zaščitne ukrepe

### 7. Napredno upravljanje žetonov
- **Preprečevanje posredovanja žetonov**: Izrecno prepovedujte vzorce posredovanja žetonov, ki zaobidejo varnostne ukrepe
- **Preverjanje ciljne publike**: Vedno preverite, da trditve o ciljni publiki žetona ustrezajo identiteti namenjenega MCP strežnika
- **Pooblastila na osnovi trditev**: Uvedite natančna pooblastila na podlagi trditev v žetonih in uporabniških atributov
- **Povezovanje žetonov**: Preverite, da žetoni ciljajo na namenjeni MCP vir in
	povežite upravljalnike stanja aplikacije na strani strežnika z overjenim principalom

### 8. Varnost stanja aplikacije

- **Kriptografski upravljalniki stanja**: Generirajte neprosojne, nedeterministične upravljalnike
	za stanje, ki presega posamezne zahteve
- **Povezovanje s posameznim uporabnikom**: Povežite vsak upravljalnik na strani strežnika z overjenim
	principalom; ne zaupajte uporabniškim ID-jem, ki jih posreduje odjemalec
- **Kontrole življenjskega cikla**: Potek in preklic upravljalnikov ter določite postopke,
	kako klicatelji obnovijo zastarelo stanje
- **Pooblastila za vsak zahtevek**: Preverjajte pooblastila vsakič, ko je upravljalnik
	predložen; upravljalnik je ime, ne poverilnica

### 9. AI-specifični varnostni ukrepi
- **Obramba pred injiciranjem pozivov**: Uporabite Microsoft Prompt Shields z označevanjem, ločili in tehnikami označevanja podatkov
- **Preprečevanje zastrupitve orodij**: Preverite metapodatke orodij, nadzirajte dinamične spremembe in preverjajte integriteto orodij
- **Preverjanje izhodov modela**: Preglejte izhode modela zaradi morebitnih uhajanj podatkov, škodljive vsebine ali kršitev varnostnih politik
- **Zaščita okna konteksta**: Uvedite ukrepe za preprečevanje zastrupitve in manipulacijskih napadov na okna konteksta

### 10. Varnost izvajanja orodij
- **Izvajanje v peskovniku**: Zaženite izvajanja orodij v vsebnikih, izoliranih okoljih z omejitvami virov
- **Ločevanje privilegijev**: Izvajajte orodja z minimalnimi potrebnimi privilegiji in ločenimi servisnimi računi
- **Omrežna izolacija**: Uvedite omrežno segmentacijo za okolja izvajanja orodij
- **Nadzor izvajanja**: Spremljajte izvajanje orodij zaradi nenavadnega vedenja, porabe virov in varnostnih kršitev

### 11. Neprekinjeno preverjanje varnosti
- **Avtomatizirano varnostno testiranje**: Integrirajte varnostno testiranje v CI/CD pipeline z orodji, kot je GitHub Advanced Security
- **Upravljanje ranljivosti**: Redno skenirajte vse odvisnosti, vključno z AI modeli in zunanjimi storitvami
- **Testiranje penetracije**: Izvajajte redne varnostne ocene, posebej osredotočene na MCP implementacije
- **Pregledi varnostne kode**: Uvedite obvezne varnostne preglede za vse spremembe kode povezane z MCP

### 12. Varnost dobavne verige za AI
- **Preverjanje komponent**: Preverite izvor, integriteto in varnost vseh AI komponent (modeli, vgradnje, API-ji)
- **Upravljanje odvisnosti**: Vzdržujte ažurne sezname vseh programske opreme in AI odvisnosti z nadzorom ranljivosti
- **Zaupanja vredni repozitoriji**: Uporabljajte preverjene, zaupanja vredne vire za vse AI modele, knjižnice in orodja
- **Nadzor dobavne verige**: Neprekinjeno spremljajte morebitne kompromitacije pri ponudnikih AI storitev in repozitorijih modelov

## Napredni varnostni vzorci

### Arhitektura ničelnega zaupanja za MCP
- **Nikoli ne zaupaj, vedno preverjaj**: Uvedite neprekinjeno preverjanje za vse udeležence MCP
- **Mikro-segmentacija**: Izolirajte MCP komponente z granulirano omrežno in identitetno kontrolo
- **Pogojni dostop**: Uvedite dostopne kontrole, osnovane na tveganju, ki se prilagajajo kontekstu in vedenju
- **Neprekinjena ocena tveganja**: Dinamično ocenjujte varnostno stanje na podlagi trenutnih indikatorjev groženj

### Implementacija AI, ki varuje zasebnost
- **Minimizacija podatkov**: Razkrijte le minimalno potrebno količino podatkov za vsako MCP operacijo
- **Differenčna zasebnost**: Izvajajte tehnike varovanja zasebnosti pri obdelavi občutljivih podatkov
- **Homomorfno šifriranje**: Uporabljajte napredne tehnike šifriranja za varno računanje na šifriranih podatkih
- **Federativno učenje**: Uvedite porazdeljene pristope k učenju, ki varujejo lokalnost podatkov in zasebnost

### Odziv na incidente za AI sisteme
- **Postopki za AI-specifične incidente**: Razvijte postopke odziva na incidente, prilagojene AI in grožnjam specifičnim za MCP
- **Avtomatiziran odziv**: Uvedite avtomatizirano omejitev in sanacijo za pogoste varnostne incidente AI  
- **Forenzične zmogljivosti**: Vzdržujte forenzično pripravljenost za kompromitacije AI sistemov in uhajanja podatkov
- **Postopki okrevanja**: Vzpostavite postopke za okrevanje po zastrupitvi AI modelov, napadih z injiciranjem pozivov in kompromisih storitev

## Viri in standardi za implementacijo

### 🏔️ Praktično varnostno usposabljanje
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Celovita praktična delavnica za varovanje MCP strežnikov v Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Referenčna arhitektura in vodnik za implementacijo OWASP MCP Top 10

### Uradna dokumentacija MCP
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutna specifikacija MCP protokola
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Uradna varnostna priporočila
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Vzorce HTTP avtentikacije
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Zahteve za transport

### Microsoftove varnostne rešitve
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Napredna zaščita pred injiciranjem pozivov
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Celovito filtriranje vsebine AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Upravljanje identitete in dostopa v podjetju
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Varnostno shranjevanje skrivnosti in poverilnic
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Varnostno skeniranje dobavne verige in kode

### Varnostni standardi in okviri
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Trenutna vodila za varnost OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Tveganja spletnih aplikacij
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifična varnostna tveganja
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Celovit okvir za upravljanje tveganj AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemi upravljanja informacijske varnosti

### Vodniki za implementacijo in vadnice
- [Azure API Management kot MCP avtentikacijski prehod](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Vzorce bedrijfske avtentikacije
- [Microsoft Entra ID z MCP strežniki](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracija ponudnika identitete
- [Implementacija varnega shranjevanja žetonov](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najboljše prakse upravljanja žetonov
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Napredni vzorci šifriranja

### Napredni varnostni viri
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Prakse varnega razvoja
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifično varnostno testiranje
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologija modeliranja groženj AI sistemov
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tehnike varovanja zasebnosti AI

### Skladnost in upravljanje
- [GDPR skladnost za AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Skladnost z zasebnostjo v AI sistemih
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odgovorna implementacija AI
- [SOC 2 za AI storitve](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Varnostni ukrepi za ponudnike AI storitev
- [HIPAA skladnost za AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Zahteve skladnosti za zdravstveni AI

### DevSecOps in avtomatizacija
- [DevSecOps pipeline za AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Varnostni razvojni pipeline za AI
- [Avtomatizirano varnostno testiranje](https://learn.microsoft.com/security/engineering/devsecops) - Neprekinjeno preverjanje varnosti
- [Varnost infrastrukture kot kode](https://learn.microsoft.com/security/engineering/infrastructure-security) - Varno uvajanje infrastrukture
- [Varnost kontejnerjev za AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Varnost kontejnerizacije delovne obremenitve AI

### Nadzor in odziv na incidente  
- [Azure Monitor za AI delovne obremenitve](https://learn.microsoft.com/azure/azure-monitor/overview) - Celovite rešitve za nadzor
- [Odziv na varnostne incidente AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifični postopki za incidente
- [SIEM za AI sisteme](https://learn.microsoft.com/azure/sentinel/overview) - Upravljanje varnostnih informacij in dogodkov

- [Obveščanje o grožnjah za AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Viri obveščanja o grožnjah za AI

## 🔄 Nenehno Izboljševanje

### Ostani na tekočem z razvijajočimi se standardi
- **Posodobitve specifikacij MCP**: Spremljajte uradne spremembe specifikacij MCP in varnostna obvestila
- **Obveščanje o grožnjah**: Naročite se na vire varnostnih groženj in baze ranljivosti za AI  
- **Sodelovanje v skupnosti**: Sodelujte v razpravah in delovnih skupinah varnostne skupnosti MCP
- **Redna ocena**: Izvajajte četrtletne ocene varnostnega stanja in posodabljajte prakse

### Prispevanje k varnosti MCP
- **Varnostne raziskave**: Prispevajte k varnostnim raziskavam MCP in programom razkrivanja ranljivosti
- **Deljenje najboljših praks**: Delite varnostne implementacije in pridobljene izkušnje s skupnostjo
- **Razvoj standardov**: Sodelujte pri razvoju specifikacij MCP in ustvarjanju varnostnih standardov
- **Razvoj orodij**: Razvijajte in delite varnostna orodja in knjižnice za ekosistem MCP

---

*Ta dokument odraža najboljše varnostne prakse MCP z dne 9. septembra 2026,
na podlagi specifikacije MCP `2026-07-28`. Varnostne prakse je treba redno
pregledovati, saj se protokol in grožnje spreminjajo.*

## Kaj sledi

- Preberi: [Najboljše varnostne prakse MCP](./mcp-security-best-practices.md)
- Vrni se na: [Pregled varnostnega modula](./README.md)
- Nadaljuj do: [Modul 3: Začetek](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
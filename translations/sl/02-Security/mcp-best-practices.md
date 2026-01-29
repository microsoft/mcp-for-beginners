# Najboljše varnostne prakse MCP 2025

Ta obsežen vodič opisuje bistvene varnostne najboljše prakse za implementacijo sistemov Model Context Protocol (MCP) na podlagi najnovejše **MCP specifikacije 2025-11-25** in trenutnih industrijskih standardov. Te prakse obravnavajo tako tradicionalne varnostne pomisleke kot tudi AI-specifične grožnje, značilne za implementacije MCP.

## Kritične varnostne zahteve

### Obvezni varnostni nadzori (zahteve MUST)

1. **Preverjanje žetonov**: MCP strežniki **NE SMEJO** sprejemati nobenih žetonov, ki niso bili izrecno izdani za samega MCP strežnika  
2. **Preverjanje avtorizacije**: MCP strežniki, ki izvajajo avtorizacijo, **MORAJO** preveriti VSE dohodne zahteve in **NE SMEJO** uporabljati sej za avtentikacijo  
3. **Soglasje uporabnika**: MCP proxy strežniki, ki uporabljajo statične ID-je odjemalcev, **MORAJO** pridobiti izrecno soglasje uporabnika za vsakega dinamično registriranega odjemalca  
4. **Varnostni ID-ji sej**: MCP strežniki **MORAJO** uporabljati kriptografsko varne, nedeterministične ID-je sej, ustvarjene z varnimi generatorji naključnih števil

## Osnovne varnostne prakse

### 1. Preverjanje in čiščenje vhodnih podatkov
- **Celovito preverjanje vhodnih podatkov**: Preverite in očistite vse vhode, da preprečite napade z injekcijo, težave z zmedo pooblaščenca in ranljivosti vbrizgavanja pozivov  
- **Uveljavljanje sheme parametrov**: Uvedite strogo preverjanje JSON sheme za vse parametre orodij in API vhode  
- **Filtriranje vsebine**: Uporabite Microsoft Prompt Shields in Azure Content Safety za filtriranje zlonamerne vsebine v pozivih in odgovorih  
- **Čiščenje izhodov**: Preverite in očistite vse izhode modela pred prikazom uporabnikom ali nadaljnjim sistemom

### 2. Odličnost pri avtentikaciji in avtorizaciji  
- **Zunanji ponudniki identitete**: Avtentikacijo delegirajte uveljavljenim ponudnikom identitete (Microsoft Entra ID, ponudniki OAuth 2.1) namesto lastne implementacije  
- **Natančne pravice**: Uvedite granulirane, orodju specifične pravice po načelu najmanjših privilegijev  
- **Upravljanje življenjskega cikla žetonov**: Uporabljajte kratkotrajne dostopne žetone z varno rotacijo in pravilnim preverjanjem občinstva  
- **Večfaktorska avtentikacija**: Zahtevajte MFA za ves administrativni dostop in občutljive operacije

### 3. Varnostni komunikacijski protokoli
- **Varnost sloja transporta**: Uporabljajte HTTPS/TLS 1.3 za vso MCP komunikacijo s pravilnim preverjanjem certifikatov  
- **Šifriranje od konca do konca**: Uvedite dodatne plasti šifriranja za zelo občutljive podatke med prenosom in v mirovanju  
- **Upravljanje certifikatov**: Vzdržujte pravilno upravljanje življenjskega cikla certifikatov z avtomatiziranimi postopki podaljševanja  
- **Uveljavljanje različice protokola**: Uporabljajte trenutno različico MCP protokola (2025-11-25) s pravilnim dogovarjanjem različic.

### 4. Napredno omejevanje hitrosti in zaščita virov
- **Večplastno omejevanje hitrosti**: Uvedite omejevanje hitrosti na ravni uporabnika, seje, orodja in virov, da preprečite zlorabe  
- **Prilagodljivo omejevanje hitrosti**: Uporabljajte omejevanje hitrosti na osnovi strojnega učenja, ki se prilagaja vzorcem uporabe in indikatorjem groženj  
- **Upravljanje kvot virov**: Nastavite ustrezne omejitve za računske vire, uporabo pomnilnika in čas izvajanja  
- **Zaščita pred DDoS**: Uvedite celovite sisteme za zaščito pred DDoS in analizo prometa

### 5. Celovito beleženje in nadzor
- **Strukturirano revizijsko beleženje**: Uvedite podrobne, iskalne dnevnike za vse MCP operacije, izvajanje orodij in varnostne dogodke  
- **Varnostni nadzor v realnem času**: Uporabite SIEM sisteme z AI-podprtim odkrivanjem anomalij za MCP delovne obremenitve  
- **Beleženje v skladu z zasebnostjo**: Beležite varnostne dogodke ob spoštovanju zahtev in predpisov o zasebnosti podatkov  
- **Integracija odziva na incidente**: Povežite sisteme beleženja z avtomatiziranimi delovnimi tokovi odziva na incidente

### 6. Izboljšane prakse varnega shranjevanja
- **Strojni varnostni moduli**: Uporabljajte shranjevanje ključev, podprto s HSM (Azure Key Vault, AWS CloudHSM) za kritične kriptografske operacije  
- **Upravljanje šifrirnih ključev**: Uvedite pravilno rotacijo ključev, ločevanje in nadzore dostopa za šifrirne ključe  
- **Upravljanje skrivnosti**: Shranjujte vse API ključe, žetone in poverilnice v namenskih sistemih za upravljanje skrivnosti  
- **Klasifikacija podatkov**: Razvrstite podatke glede na stopnjo občutljivosti in uporabite ustrezne zaščitne ukrepe

### 7. Napredno upravljanje žetonov
- **Preprečevanje prehoda žetonov**: Izrecno prepovedujte vzorce prehoda žetonov, ki zaobidejo varnostne kontrole  
- **Preverjanje občinstva**: Vedno preverite, da trditve o občinstvu žetona ustrezajo identiteti MCP strežnika  
- **Avtorizacija na podlagi trditev**: Uvedite granulirano avtorizacijo na podlagi trditev v žetonu in atributov uporabnika  
- **Povezava žetonov**: Povežite žetone s specifičnimi sejami, uporabniki ali napravami, kjer je to primerno

### 8. Varnostno upravljanje sej
- **Kriptografski ID-ji sej**: Ustvarjajte ID-je sej z uporabo kriptografsko varnih generatorjev naključnih števil (nepredvidljive zaporedja)  
- **Povezava z uporabnikom**: Povežite ID-je sej z uporabniško specifičnimi informacijami z uporabo varnih formatov, kot je `<user_id>:<session_id>`  
- **Nadzor življenjskega cikla sej**: Uvedite pravilno potekanje, rotacijo in razveljavitev sej  
- **Varnostni glavi sej**: Uporabljajte ustrezne HTTP varnostne glave za zaščito sej

### 9. AI-specifični varnostni nadzori
- **Obramba pred vbrizgavanjem pozivov**: Uporabite Microsoft Prompt Shields z osvetlitvijo, ločili in tehnikami označevanja podatkov  
- **Preprečevanje zastrupitve orodij**: Preverjajte metapodatke orodij, spremljajte dinamične spremembe in preverjajte integriteto orodij  
- **Preverjanje izhodov modela**: Preglejte izhode modela za morebitno uhajanje podatkov, škodljivo vsebino ali kršitve varnostnih politik  
- **Zaščita kontekstnega okna**: Uvedite nadzore za preprečevanje zastrupitve in manipulacije kontekstnega okna

### 10. Varnost izvajanja orodij
- **Izvajanje v peskovniku**: Zaženite izvajanje orodij v kontejneriziranih, izoliranih okoljih z omejitvami virov  
- **Ločevanje privilegijev**: Izvajajte orodja z minimalnimi potrebnimi privilegiji in ločenimi servisnimi računi  
- **Omrežna izolacija**: Uvedite omrežno segmentacijo za okolja izvajanja orodij  
- **Nadzor izvajanja**: Spremljajte izvajanje orodij zaradi nenavadnega vedenja, uporabe virov in varnostnih kršitev

### 11. Neprestano preverjanje varnosti
- **Avtomatizirano varnostno testiranje**: Integrirajte varnostno testiranje v CI/CD cevovode z orodji, kot je GitHub Advanced Security  
- **Upravljanje ranljivosti**: Redno pregledujte vse odvisnosti, vključno z AI modeli in zunanjimi storitvami  
- **Penetracijsko testiranje**: Redno izvajajte varnostne ocene, posebej usmerjene na implementacije MCP  
- **Pregledi varnostne kode**: Uvedite obvezne varnostne preglede za vse spremembe kode, povezane z MCP

### 12. Varnost dobavne verige za AI
- **Preverjanje komponent**: Preverjajte izvor, integriteto in varnost vseh AI komponent (modeli, vdelave, API-ji)  
- **Upravljanje odvisnosti**: Vzdržujte aktualne sezname vseh programske opreme in AI odvisnosti z evidentiranjem ranljivosti  
- **Zanesljivi repozitoriji**: Uporabljajte preverjene, zaupanja vredne vire za vse AI modele, knjižnice in orodja  
- **Nadzor dobavne verige**: Neprestano spremljajte morebitne kompromitacije pri ponudnikih AI storitev in repozitorijih modelov

## Napredni varnostni vzorci

### Arhitektura ničelnega zaupanja za MCP
- **Nikoli ne zaupaj, vedno preverjaj**: Uvedite neprekinjeno preverjanje za vse udeležence MCP  
- **Mikrosegmentacija**: Izolirajte MCP komponente z granuliranimi omrežnimi in identitetnimi kontrolami  
- **Pogojni dostop**: Uvedite dostopne kontrole, ki temeljijo na tveganju in se prilagajajo kontekstu ter vedenju  
- **Neprestana ocena tveganja**: Dinamično ocenjujte varnostno stanje na podlagi trenutnih indikatorjev groženj

### Implementacija AI, ki varuje zasebnost
- **Minimizacija podatkov**: Razkrijte le najmanj potrebne podatke za vsako MCP operacijo  
- **Diferencialna zasebnost**: Uvedite tehnike varovanja zasebnosti pri obdelavi občutljivih podatkov  
- **Homomorfno šifriranje**: Uporabljajte napredne šifrirne tehnike za varno računanje na šifriranih podatkih  
- **Federativno učenje**: Uvedite distribuirane pristope učenja, ki ohranjajo lokalnost podatkov in zasebnost

### Odziv na incidente za AI sisteme
- **AI-specifični postopki za incidente**: Razvijte postopke odziva na incidente, prilagojene AI in MCP specifičnim grožnjam  
- **Avtomatiziran odziv**: Uvedite avtomatizirano zajezitev in odpravo za pogoste AI varnostne incidente  
- **Forenzične zmogljivosti**: Vzdržujte forenzično pripravljenost za kompromitacije AI sistemov in kršitve podatkov  
- **Postopki okrevanja**: Vzpostavite postopke za okrevanje po zastrupitvi AI modelov, napadih z vbrizgavanjem pozivov in kompromitacijah storitev

## Viri in standardi za implementacijo

### Uradna MCP dokumentacija
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Trenutna specifikacija MCP protokola  
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Uradne varnostne smernice  
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Vzorci avtentikacije in avtorizacije  
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Zahteve za varnost sloja transporta

### Microsoft varnostne rešitve
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Napredna zaščita pred vbrizgavanjem pozivov  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Celovito filtriranje AI vsebin  
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Upravljanje identitete in dostopa za podjetja  
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Varen sistem za upravljanje skrivnosti in poverilnic  
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Pregled varnosti dobavne verige in kode

### Varnostni standardi in okviri
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Trenutne varnostne smernice za OAuth  
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Največja tveganja za spletne aplikacije  
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI-specifična varnostna tveganja  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Celovit okvir za upravljanje tveganj AI  
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Sistemi upravljanja informacijske varnosti

### Vodiči in tutoriali za implementacijo
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Vzorci avtentikacije za podjetja  
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracija ponudnika identitete  
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najboljše prakse upravljanja žetonov  
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Napredni vzorci šifriranja

### Napredni varnostni viri
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Prakse varnega razvoja  
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI-specifično varnostno testiranje  
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologija modeliranja groženj za AI  
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Tehnike varovanja zasebnosti v AI

### Skladnost in upravljanje
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Skladnost z zasebnostjo v AI sistemih  
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odgovorna implementacija AI  
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Varnostni nadzori za ponudnike AI storitev  
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Zahteve za skladnost AI v zdravstvu

### DevSecOps in avtomatizacija
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Varnostni cevovodi za razvoj AI  
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Neprestano preverjanje varnosti  
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Varnost uvajanja infrastrukture  
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Varnost kontejnerizacije AI delovnih obremenitev

### Nadzor in odziv na incidente  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Celovite rešitve za nadzor  
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI-specifični postopki za incidente  
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Upravljanje varnostnih informacij in dogodkov  
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Viri obveščanja o grožnjah za AI

## 🔄 Neprestano izboljševanje

### Bodite na tekočem z razvijajočimi se standardi
- **Posodobitve MCP specifikacije**: Spremljajte uradne spremembe MCP specifikacije in varnostna obvestila  
- **Obveščanje o grožnjah**: Naročite se na vire groženj in baze ranljivosti za AI  
- **Sodelovanje v skupnosti**: Sodelujte v razpravah in delovnih skupinah MCP varnostne skupnosti  
- **Redne ocene**: Izvajajte četrtletne ocene varnostnega stanja in ustrezno posodabljajte prakse

### Prispevanje k varnosti MCP
- **Varnostne raziskave**: Prispevajte k raziskavam varnosti MCP in programom razkritja ranljivosti  
- **Deljenje najboljših praks**: Delite varnostne implementacije in pridobljene izkušnje s skupnostjo
- **Standardni razvoj**: Sodelujte pri razvoju specifikacij MCP in ustvarjanju varnostnih standardov  
- **Razvoj orodij**: Razvijajte in delite varnostna orodja ter knjižnice za ekosistem MCP  

---

*Ta dokument odraža najboljše varnostne prakse MCP z dne 18. decembra 2025, na podlagi specifikacije MCP 2025-11-25. Varnostne prakse je treba redno pregledovati in posodabljati, saj se protokol in grožnje nenehno spreminjajo.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
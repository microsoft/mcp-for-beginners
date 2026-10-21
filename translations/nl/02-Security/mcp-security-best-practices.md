# MCP Beveiligingsrichtlijnen - Update september 2026

> **Belangrijk:** Dit document weerspiegelt
> [MCP Specificatie 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> en de officiële
> [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

## 🏔️ Praktische Beveiligingstraining

Voor praktische implementatie-ervaring raden wij de **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** aan - een uitgebreide begeleide expeditie voor het beveiligen van MCP-servers in Azure. De workshop behandelt alle OWASP MCP Top 10 risico’s via een "kwetsbaar → exploit → oplossen → valideren" methodologie.

Alle praktijken in dit document zijn in overeenstemming met de **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** voor Azure-specifieke implementatie-instructies.

## Essentiële Beveiligingspraktijken voor MCP-Implementaties

Het Model Context Protocol introduceert unieke beveiligingsuitdagingen die verder gaan dan traditionele softwarebeveiliging. Deze praktijken behandelen fundamentele vereisten en MCP-specifieke dreigingen waaronder promptinjectie, toolverontreiniging, state-handle kaping, confused deputy-problemen en token-doorvoer kwetsbaarheden.





### **VERPLICHTE Beveiligingseisen** 

**Kritieke vereisten uit de MCP-specificatie:**

> **MAG NIET**: MCP-servers **MAG NIET** tokens accepteren die niet expliciet zijn uitgegeven voor de MCP-server
> 
> **MOET**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren
>  
> **MAG NIET**: MCP-servers **MAG NIET** sessies gebruiken voor authenticatie
>
> **MOET**: MCP-proxyservers die een statische client-ID van derden gebruiken **MOETEN**
> toestemming verkrijgen voor elke MCP-client voordat autorisatie wordt doorgestuurd

---

## 1. **Tokenbeveiliging & Authenticatie**

**Authenticatie- & Autorisatiecontroles:**
   - **Grondige autorisatiebeoordeling**: Voer uitgebreide audits uit van MCP-server autorisatielogica om ervoor te zorgen dat alleen bedoelde gebruikers en clients toegang hebben tot bronnen
   - **Integratie van externe identiteitproviders**: Gebruik gevestigde identiteitproviders zoals Microsoft Entra ID in plaats van zelf aangepaste authenticatie te implementeren
   - **Token Audience Validatie**: Valideer altijd dat tokens expliciet zijn uitgegeven voor jouw MCP-server - accepteer nooit upstream tokens
   - **Juiste tokenlevenscyclus**: Implementeer veilige tokenrotatie, vervalbeleid en voorkom token replay-aanvallen

**Beschermde tokenopslag:**
   - Gebruik Azure Key Vault of soortgelijke beveiligde credential stores voor alle geheimen
   - Implementeer encryptie voor tokens zowel in rust als in transit
   - Regelmatige rotatie van credentials en monitoring op niet-geautoriseerde toegang

## 2. **State Handle & Transportbeveiliging**

**Veilige applicatietoestandspraktijken:**

- **Ondoorzichtige state handles**: Gebruik veilige, niet-deterministische handles voor
   applicatietoestand die meerdere verzoeken overspant
- **Gebruikersspecifieke binding**: Bind handles aan de serverzijde aan de geauthenticeerde
   principal en wees strikt tegen hergebruik door andere gebruikers
- **Levenscyclusbeheer**: Laat handles verlopen en intrekken om kwetsbaarheidsvensters te beperken
- **Autoriseer per verzoek**: Behandel een state handle nooit als authenticatie;
   autoriseer elk verzoek dat er een presenteert




- Gebruik procesisolatie en omgevingscredentials voor lokale stdio-servers
- Configureer moderne TLS met juiste certificaatrotatie en validatie




   - **Microsoft Prompt Shields**: Zet AI Prompt Shields in voor geavanceerde detectie en filtering van kwaadwillende instructies
   - **Inputsanering**: Valideer en reinig alle invoer om injectie-aanvallen en confused deputy-problemen te voorkomen
   - **Inhoudsgrenzen**: Gebruik delimiter- en datamerking systemen om vertrouwde instructies te onderscheiden van externe inhoud


   - **Validatie van toolmetadata**: Implementeer integriteitscontroles voor tooldefinities en monitor op onverwachte wijzigingen
   - **Dynamische toolmonitoring**: Monitor runtime gedrag en stel waarschuwingen in voor onverwachte uitvoeringspatronen
   - **Goedkeuringsworkflows**: Vereis expliciete gebruikersgoedkeuring voor toolwijzigingen en capaciteitswijzigingen




   - Geef MCP-servers alleen minimale rechten die nodig zijn voor de beoogde functionaliteit
   - Implementeer rolgebaseerde toegangscontrole (RBAC) met fijnmazige permissies
   - Regelmatige herziening van permissies en voortdurende monitoring op privilege-escalatie


   - Pas resourcelimieten toe om uitputtingsaanvallen te voorkomen
   - Gebruik containerisolatie voor tool-uitvoeringsomgevingen  
   - Implementeer just-in-time toegang voor administratieve functies




   - **Integratie met Azure Content Safety**: Gebruik Azure Content Safety om schadelijke inhoud, jailbreakpogingen en beleidsinbreuken te detecteren
   - **Gedragsanalyse**: Implementeer runtime gedragsmonitoring om afwijkingen in MCP-server en tooluitvoering te detecteren
   - **Uitgebreide logging**: Log alle authenticatiepogingen, tool-aanroepen en beveiligingsgebeurtenissen met veilige, onkraakbare opslag


   - Real-time waarschuwingen voor verdachte patronen en niet-geautoriseerde toegangspogingen  
   - Integratie met SIEM-systemen voor gecentraliseerd beheer van beveiligingsgebeurtenissen
   - Regelmatige beveiligingsaudits en penetratietesten van MCP-implementaties




   - **Dependency scanning**: Gebruik geautomatiseerde kwetsbaarheidsscans voor alle softwareafhankelijkheden en AI-componenten
   - **Validatie van herkomst**: Verifieer de oorsprong, licenties en integriteit van modellen, databronnen en externe diensten
   - **Ondertekende pakketten**: Gebruik cryptografisch ondertekende pakketten en verifieer handtekeningen voor uitrol


   - **GitHub Advanced Security**: Implementeer geheimscanner, afhankelijkheidsanalyse en CodeQL statische analyse
   - **CI/CD beveiliging**: Integreer beveiligingsvalidatie in geautomatiseerde deployment pipelines
   - **Integriteit van artefacten**: Implementeer cryptografische verificatie voor uitgerolde artefacten en configuraties




   - **PKCE-implementatie**: Gebruik Proof Key for Code Exchange (PKCE) voor alle autorisatieaanvragen
    - **Clientregistratie**: Geef de voorkeur aan Client ID Metadata-documenten of
       preregistratie; gebruik de verouderde Dynamic Client Registration alleen als
       compatibiliteitsfallback
    - **Expliciete toestemming**: MCP-proxy’s die een statische client-ID van derden gebruiken moeten
       toestemming verkrijgen voor elke MCP-client voordat autorisatie wordt doorgestuurd
   - **Validatie van redirect URI**: Implementeer strikte validatie van redirect-URI’s en clientidentifiers


   - Voorkom autorisatie-omzeiling via exploitatie van statische client-ID
   - Implementeer juiste toestemmingsworkflows voor toegang tot API’s van derden
   - Monitor op diefstal van autorisatiecodes en niet-geautoriseerde toegang tot API’s




   - **Geautomatiseerde reactie**: Implementeer geautomatiseerde systemen voor credentialrotatie en dreigingsbeperking
   - **Rollback-procedures**: Mogelijkheid om snel terug te keren naar bekende goede configuraties en componenten
   - **Forensische mogelijkheden**: Gedetailleerde audit trails en logging voor incidentonderzoek


   - Duidelijke escalatieprocedures voor beveiligingsincidenten
   - Integratie met organisatorische incidentrespons-teams
   - Regelmatige beveiligingsincident-simulaties en tabletop-oefeningen




   - Zorg dat MCP-implementaties voldoen aan branchespecifieke vereisten (GDPR, HIPAA, SOC 2)
   - Implementeer dataclassificatie en privacycontroles voor AI-gegevensverwerking
   - Houd uitgebreide documentatie bij voor compliance-audits


   - Formele beveiligingsbeoordelingsprocessen voor alle MCP-systeemwijzigingen
   - Versiebeheer en goedkeuringsworkflows voor configuratiewijzigingen
   - Regelmatige compliance-evaluaties en gap-analyses




   - **Nooit vertrouwen, altijd verifiëren**: Continue verificatie van gebruikers, apparaten en verbindingen
   - **Microsegmentatie**: Fijne netwerkcontrols die individuele MCP-componenten isoleren
   - **Conditionele toegang**: Risicogebaseerde toegangscontroles die zich aanpassen aan huidige context en gedrag


   - **Runtime Application Self-Protection (RASP)**: Zet RASP-technieken in voor realtime dreigingsdetectie
   - **Toepassingsprestatiemonitoring**: Monitor op prestatie-afwijkingen die kunnen wijzen op aanvallen
   - **Dynamische beveiligingspolicies**: Implementeer beveiligingsbeleid die zich aanpast aan het actuele dreigingslandschap




   - **Microsoft Defender for Cloud**: Cloud security posture management voor MCP workloads
   - **Azure Sentinel**: Cloud-native SIEM- en SOAR-mogelijkheden voor geavanceerde dreigingsdetectie
   - **Microsoft Purview**: Data governance en compliance voor AI-workflows en databronnen


   - **Microsoft Entra ID**: Enterprise identiteitsbeheer met conditionele toegangsbeleidsregels
   - **Privileged Identity Management (PIM)**: Just-in-time toegang en goedkeuringsworkflows voor administratieve functies
   - **Identiteitsbescherming**: Risicogebaseerde conditionele toegang en geautomatiseerde dreigingsrespons




   - **Specificatiemonitoring**: Regelmatige beoordeling van MCP-specificatie-updates en wijzigingen in beveiligingsrichtlijnen
   - **Threat Intelligence**: Integratie van AI-specifieke dreigingsfeeds en indicators of compromise
   - **Deelname aan beveiligingscommunity**: Actieve deelname aan MCP-beveiligingscommunity en programma's voor het melden van kwetsbaarheden


   - **Machine Learning beveiliging**: Gebruik ML-gebaseerde anomaliedetectie voor het identificeren van nieuwe aanvalspatronen
   - **Predictive security analytics**: Implementeer voorspellende modellen voor proactieve dreigingsidentificatie
   - **Beveiligingsautomatisering**: Geautomatiseerde updates van beveiligingsbeleid gebaseerd op threat intelligence en specificatiewijzigingen


---

## **Kritieke Beveiligingsbronnen**

### **Officiële MCP Documentatie**
- [MCP-specificatie (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Beveiligingspraktijken](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP-autorisatiespecificatie](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **OWASP MCP Beveiligingsbronnen**
- [OWASP MCP Azure Beveiligingsgids](https://microsoft.github.io/mcp-azure-security-guide/) - Uitgebreide OWASP MCP Top 10 met Azure-implementatie
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Officiële OWASP MCP beveiligingsrisico's
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktische beveiligingstraining voor MCP op Azure

### **Microsoft Beveiligingsoplossingen**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Beveiliging](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Beveiligingsnormen**
- [OAuth 2.0 Beveiligingspraktijken (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 voor Grote Taalmodellen](https://genai.owasp.org/)
- [NIST AI Risicobeheerframework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementatiehandleidingen**
- [Azure API Management MCP Authenticatie Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID met MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Beveiligingsmelding:** MCP beveiligingspraktijken ontwikkelen zich snel. Verifieer altijd
> aan de hand van de huidige [MCP-specificatie](https://modelcontextprotocol.io/specification/2026-07-28/)
> en [officiële beveiligingsdocumentatie](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> vóór implementatie.

## Wat is de volgende stap

- Lees: [MCP Beveiligingscontroles](./mcp-security-controls.md)
- Ga terug naar: [Overzicht van het beveiligingsmodule](./README.md)
- Ga verder naar: [Module 3: Aan de slag](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
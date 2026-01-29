# MCP Beveiligingsrichtlijnen - Update December 2025

> **Belangrijk**: Dit document weerspiegelt de nieuwste [MCP Specificatie 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) beveiligingseisen en officiële [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Raadpleeg altijd de actuele specificatie voor de meest recente richtlijnen.

## Essentiële Beveiligingspraktijken voor MCP-Implementaties

Het Model Context Protocol introduceert unieke beveiligingsuitdagingen die verder gaan dan traditionele softwarebeveiliging. Deze praktijken behandelen zowel fundamentele beveiligingseisen als MCP-specifieke bedreigingen zoals promptinjectie, toolvergiftiging, sessiekaping, confused deputy-problemen en token passthrough-kwetsbaarheden.

### **VERPLICHTE Beveiligingseisen** 

**Kritieke Eisen uit MCP Specificatie:**

### **VERPLICHTE Beveiligingseisen** 

**Kritieke Eisen uit MCP Specificatie:**

> **MAG NIET**: MCP-servers **MAGEN GEEN** tokens accepteren die niet expliciet voor de MCP-server zijn uitgegeven  
>  
> **MOET**: MCP-servers die autorisatie implementeren **MOETEN** ALLE inkomende verzoeken verifiëren  
>  
> **MAG NIET**: MCP-servers **MAGEN GEEN** sessies gebruiken voor authenticatie  
>  
> **MOET**: MCP-proxyservers die statische client-ID's gebruiken **MOETEN** gebruikersconsent verkrijgen voor elke dynamisch geregistreerde client  

---

## 1. **Tokenbeveiliging & Authenticatie**

**Authenticatie- & Autorisatiecontroles:**
   - **Grondige Autorisatiecontrole**: Voer uitgebreide audits uit van de autorisatielogica van MCP-servers om te waarborgen dat alleen bedoelde gebruikers en clients toegang hebben tot resources  
   - **Integratie met Externe Identiteitsproviders**: Gebruik gevestigde identiteitsproviders zoals Microsoft Entra ID in plaats van eigen authenticatie te implementeren  
   - **Validatie van Token Audience**: Valideer altijd dat tokens expliciet voor jouw MCP-server zijn uitgegeven - accepteer nooit upstream tokens  
   - **Correcte Tokenlevenscyclus**: Implementeer veilige tokenrotatie, vervalbeleid en voorkom token replay-aanvallen  

**Beschermde Tokenopslag:**
   - Gebruik Azure Key Vault of vergelijkbare veilige credentialopslag voor alle geheimen  
   - Implementeer encryptie voor tokens zowel in rust als tijdens transport  
   - Regelmatige credentialrotatie en monitoring op ongeautoriseerde toegang  

## 2. **Sessiebeheer & Transportbeveiliging**

**Veilige Sessies:**
   - **Cryptografisch Veilige Sessie-ID's**: Gebruik veilige, niet-deterministische sessie-ID's gegenereerd met cryptografisch veilige willekeurige generatoren  
   - **Gebruikersspecifieke Binding**: Bind sessie-ID's aan gebruikersidentiteiten met formaten zoals `<user_id>:<session_id>` om misbruik tussen gebruikers te voorkomen  
   - **Beheer van Sessielevenscyclus**: Implementeer correcte verval, rotatie en ongeldigmaking om kwetsbaarheidsvensters te beperken  
   - **HTTPS/TLS Verplichting**: Verplicht HTTPS voor alle communicatie om onderschepping van sessie-ID's te voorkomen  

**Transportlaagbeveiliging:**
   - Configureer TLS 1.3 waar mogelijk met correct certificaatbeheer  
   - Implementeer certificaatpinning voor kritieke verbindingen  
   - Regelmatige certificaatrotatie en geldigheidscontrole  

## 3. **AI-Specifieke Bedreigingsbescherming** 🤖

**Verdediging tegen Promptinjectie:**
   - **Microsoft Prompt Shields**: Zet AI Prompt Shields in voor geavanceerde detectie en filtering van kwaadaardige instructies  
   - **Inputsanering**: Valideer en reinig alle invoer om injectieaanvallen en confused deputy-problemen te voorkomen  
   - **Inhoudsgrenzen**: Gebruik delimiter- en datamarkering systemen om vertrouwde instructies te onderscheiden van externe inhoud  

**Voorkoming van Toolvergiftiging:**
   - **Validatie van Toolmetadata**: Implementeer integriteitscontroles voor tooldefinities en monitor op onverwachte wijzigingen  
   - **Dynamische Toolmonitoring**: Monitor runtime-gedrag en stel waarschuwingen in voor onverwachte uitvoeringspatronen  
   - **Goedkeuringsworkflows**: Vereis expliciete gebruikersgoedkeuring voor toolwijzigingen en capaciteitsaanpassingen  

## 4. **Toegangscontrole & Machtigingen**

**Principe van Minimaal Privilege:**
   - Verleen MCP-servers alleen de minimale machtigingen die nodig zijn voor de beoogde functionaliteit  
   - Implementeer rolgebaseerde toegangscontrole (RBAC) met fijnmazige machtigingen  
   - Regelmatige machtigingsreviews en continue monitoring op privilege-escalatie  

**Runtime Machtigingscontroles:**
   - Pas resourcebeperkingen toe om resource-uitputtingsaanvallen te voorkomen  
   - Gebruik containerisolatie voor tooluitvoeringsomgevingen  
   - Implementeer just-in-time toegang voor administratieve functies  

## 5. **Inhoudsveiligheid & Monitoring**

**Implementatie van Inhoudsveiligheid:**
   - **Integratie met Azure Content Safety**: Gebruik Azure Content Safety om schadelijke inhoud, jailbreakpogingen en beleidschendingen te detecteren  
   - **Gedragsanalyse**: Implementeer runtime gedragsmonitoring om anomalieën in MCP-server en tooluitvoering te detecteren  
   - **Uitgebreide Logging**: Log alle authenticatiepogingen, toolaanroepen en beveiligingsevenementen met veilige, manipulatiebestendige opslag  

**Continue Monitoring:**
   - Real-time waarschuwingen voor verdachte patronen en ongeautoriseerde toegangspogingen  
   - Integratie met SIEM-systemen voor gecentraliseerd beheer van beveiligingsevenementen  
   - Regelmatige beveiligingsaudits en penetratietesten van MCP-implementaties  

## 6. **Beveiliging van de Leveringsketen**

**Componentverificatie:**
   - **Dependency Scanning**: Gebruik geautomatiseerde kwetsbaarheidsscans voor alle softwareafhankelijkheden en AI-componenten  
   - **Validatie van Herkomst**: Verifieer de oorsprong, licenties en integriteit van modellen, databronnen en externe diensten  
   - **Ondertekende Pakketten**: Gebruik cryptografisch ondertekende pakketten en verifieer handtekeningen vóór uitrol  

**Veilige Ontwikkelpijplijn:**
   - **GitHub Advanced Security**: Implementeer geheimscanning, afhankelijkheidsanalyse en CodeQL statische analyse  
   - **CI/CD Beveiliging**: Integreer beveiligingsvalidatie door geautomatiseerde uitrolpijplijnen heen  
   - **Integriteit van Artefacten**: Implementeer cryptografische verificatie voor uitgerolde artefacten en configuraties  

## 7. **OAuth Beveiliging & Voorkoming van Confused Deputy**

**OAuth 2.1 Implementatie:**
   - **PKCE Implementatie**: Gebruik Proof Key for Code Exchange (PKCE) voor alle autorisatieverzoeken  
   - **Expliciete Toestemming**: Verkrijg gebruikersconsent voor elke dynamisch geregistreerde client om confused deputy-aanvallen te voorkomen  
   - **Validatie van Redirect URI's**: Implementeer strikte validatie van redirect URI's en clientidentificaties  

**Proxybeveiliging:**
   - Voorkom autorisatieomzeiling via exploitatie van statische client-ID's  
   - Implementeer correcte toestemmingsworkflows voor toegang tot API's van derden  
   - Monitor op diefstal van autorisatiecodes en ongeautoriseerde API-toegang  

## 8. **Incidentrespons & Herstel**

**Snelle Reactiemogelijkheden:**
   - **Geautomatiseerde Reactie**: Implementeer geautomatiseerde systemen voor credentialrotatie en dreigingsbeperking  
   - **Rollback Procedures**: Mogelijkheid om snel terug te keren naar bekende goede configuraties en componenten  
   - **Forensische Capaciteiten**: Gedetailleerde audittrajecten en logging voor incidentonderzoek  

**Communicatie & Coördinatie:**
   - Duidelijke escalatieprocedures voor beveiligingsincidenten  
   - Integratie met organisatorische incidentrespons-teams  
   - Regelmatige simulaties van beveiligingsincidenten en tafel-oefeningen  

## 9. **Naleving & Governance**

**Regelgevende Naleving:**
   - Zorg dat MCP-implementaties voldoen aan branchespecifieke eisen (GDPR, HIPAA, SOC 2)  
   - Implementeer dataclassificatie en privacycontroles voor AI-gegevensverwerking  
   - Onderhoud uitgebreide documentatie voor compliance-audits  

**Wijzigingsbeheer:**
   - Formele beveiligingsreviewprocessen voor alle MCP-systeemwijzigingen  
   - Versiebeheer en goedkeuringsworkflows voor configuratiewijzigingen  
   - Regelmatige compliancebeoordelingen en gap-analyses  

## 10. **Geavanceerde Beveiligingscontroles**

**Zero Trust Architectuur:**
   - **Nooit Vertrouwen, Altijd Verifiëren**: Continue verificatie van gebruikers, apparaten en verbindingen  
   - **Micro-segmentatie**: Fijne netwerkcontroles die individuele MCP-componenten isoleren  
   - **Conditionele Toegang**: Risicogebaseerde toegangscontroles die zich aanpassen aan de huidige context en gedrag  

**Runtime Applicatiebescherming:**
   - **Runtime Application Self-Protection (RASP)**: Zet RASP-technieken in voor realtime dreigingsdetectie  
   - **Applicatieprestatiemonitoring**: Monitor op prestatie-anomalieën die op aanvallen kunnen wijzen  
   - **Dynamische Beveiligingsbeleid**: Implementeer beveiligingsbeleid die zich aanpast op basis van het actuele dreigingslandschap  

## 11. **Integratie met Microsoft Beveiligingsecosysteem**

**Uitgebreide Microsoft Beveiliging:**
   - **Microsoft Defender for Cloud**: Cloud security posture management voor MCP workloads  
   - **Azure Sentinel**: Cloud-native SIEM en SOAR mogelijkheden voor geavanceerde dreigingsdetectie  
   - **Microsoft Purview**: Data governance en compliance voor AI-workflows en databronnen  

**Identiteits- & Toegangsbeheer:**
   - **Microsoft Entra ID**: Enterprise identiteitsbeheer met conditionele toegangsbeleid  
   - **Privileged Identity Management (PIM)**: Just-in-time toegang en goedkeuringsworkflows voor administratieve functies  
   - **Identity Protection**: Risicogebaseerde conditionele toegang en geautomatiseerde dreigingsrespons  

## 12. **Continue Beveiligingsevolutie**

**Actueel Blijven:**
   - **Specificatiemonitoring**: Regelmatige review van MCP-specificatie-updates en wijzigingen in beveiligingsrichtlijnen  
   - **Threat Intelligence**: Integratie van AI-specifieke dreigingsfeeds en indicators of compromise  
   - **Betrokkenheid bij Beveiligingscommunity**: Actieve deelname aan MCP-beveiligingscommunity en kwetsbaarheidsrapportageprogramma's  

**Adaptieve Beveiliging:**
   - **Machine Learning Beveiliging**: Gebruik ML-gebaseerde anomaliedetectie voor het identificeren van nieuwe aanvalspatronen  
   - **Voorspellende Beveiligingsanalyse**: Implementeer voorspellende modellen voor proactieve dreigingsidentificatie  
   - **Beveiligingsautomatisering**: Geautomatiseerde updates van beveiligingsbeleid op basis van threat intelligence en specificatiewijzigingen  

---

## **Kritieke Beveiligingsbronnen**

### **Officiële MCP Documentatie**
- [MCP Specificatie (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Beveiligingsrichtlijnen](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Autorisatiespecificatie](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Microsoft Beveiligingsoplossingen**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Beveiliging](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Beveiligingsstandaarden**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 voor Large Language Models](https://genai.owasp.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

### **Implementatiehandleidingen**
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID met MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

---

> **Beveiligingsmelding**: MCP-beveiligingspraktijken evolueren snel. Verifieer altijd aan de hand van de actuele [MCP-specificatie](https://spec.modelcontextprotocol.io/) en [officiële beveiligingsdocumentatie](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) vóór implementatie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
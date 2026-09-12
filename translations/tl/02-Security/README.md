# Seguridad ng MCP: Komprehensibong Proteksyon para sa mga Sistemang AI

[![Pinakamahusay na Kasanayan sa Seguridad ng MCP](../../../translated_images/tl/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Ang seguridad ay pundamental sa disenyo ng sistema ng AI, kaya binibigyan namin ito ng prayoridad bilang ikalawang seksyon namin. Ito ay alinsunod sa prinsipyo ng Microsoft na **Secure by Design** mula sa [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Ang Model Context Protocol (MCP) ay nagdadala ng makapangyarihang bagong kakayahan sa mga AI-driven na aplikasyon habang nag-iintroduce ng mga natatanging hamon sa seguridad na lampas sa tradisyonal na panganib ng software. Ang mga sistema ng MCP ay humaharap sa parehong establisadong mga isyu sa seguridad (secure coding, least privilege, seguridad ng supply chain) at mga bagong banta na espesipiko sa AI tulad ng prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough vulnerabilities, at dynamic capability modification.

Pinag-aaralan ng araling ito ang pinakamahalagang panganib sa seguridad sa implementasyon ng MCP—sinasaklaw ang authentication, authorization, sobrang mga pahintulot, indirect prompt injection, seguridad ng session, mga problema ng confused deputy, pamamahala ng token, at mga kahinaan sa supply chain. Matututuhan mo ang mga kontrol at pinakamahusay na kasanayan para mapagaan ang mga panganib na ito habang ginagamit ang mga solusyon ng Microsoft tulad ng Prompt Shields, Azure Content Safety, at GitHub Advanced Security upang patatagin ang iyong deployment ng MCP.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- **Kilalanin ang Mga Espesipikong Banta sa MCP**: Kilalanin ang mga natatanging panganib sa seguridad sa mga sistemang MCP kabilang ang prompt injection, tool poisoning, sobrang pahintulot, session hijacking, mga problema ng confused deputy, token passthrough vulnerabilities, at mga panganib sa supply chain
- **Ipatupad ang Mga Kontrol sa Seguridad**: Magpatupad ng epektibong mga mitigasyon kabilang ang matatag na authentication, least privilege access, secure token management, session security controls, at verification ng supply chain
- **Gamitin ang Mga Solusyon sa Seguridad ng Microsoft**: Unawain at gamitin ang Microsoft Prompt Shields, Azure Content Safety, at GitHub Advanced Security para sa proteksyon ng MCP workload
- **Kumpirmahin ang Seguridad ng Tool**: Kilalanin ang kahalagahan ng pagsusuri sa metadata ng tool, pagmamanman para sa dynamic na pagbabago, at pagtatanggol laban sa indirect prompt injection attacks
- **I-integrate ang Pinakamahusay na Kasanayan**: Pagsamahin ang mga napatunayang pundamental na seguridad (secure coding, server hardening, zero trust) kasama ang mga kontrol na espesipiko sa MCP para sa komprehensibong proteksyon

# Arkitektura at Mga Kontrol sa Seguridad ng MCP

Ang mga modernong implementasyon ng MCP ay nangangailangan ng mga patong-patong na diskarte sa seguridad na tinutugunan ang parehong tradisyonal na seguridad ng software at AI-espesipikong mga banta. Ang mabilis na pag-unlad ng MCP specification ay patuloy na pinapabuti ang mga kontrol nito sa seguridad, na nagpapahintulot sa mas mahusay na integrasyon sa mga arkitektura ng seguridad ng enterprise at mga napatunayang pinakamahusay na kasanayan.

Ipinapakita ng pananaliksik mula sa [Microsoft Digital Defense Report](https://aka.ms/mddr) na **98% ng mga naiulat na paglabag ay maiiwasan sa pamamagitan ng matibay na hygiene sa seguridad**. Ang pinakaepektibong estratehiya sa proteksyon ay pinagsasama ang mga pundamental na kasanayan sa seguridad kasama ang mga kontrol na espesipiko sa MCP—ang mga napatunayang baseline security measures ang pinakamabisang paraan upang mabawasan ang pangkalahatang panganib sa seguridad.

## Kasalukuyang Kalagayan ng Seguridad

> **Tandaan:** Pinagsasama ng kabanatang ito ang mga established na kontrol sa seguridad ng MCP sa
> kasalukuyang **MCP Specification 2026-07-28** na patnubay sa authorization. Palaging sumangguni
> sa kasalukuyang [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub repository](https://github.com/modelcontextprotocol), at
> [dokumentasyon ng pinakamahusay na kasanayan sa seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> kapag nag-iimplementa ng sensitibong code sa seguridad.

> **Pag-update sa Authorization:** Iniaatas ng MCP `2026-07-28` na tiyakin ng mga kliyente ang
> `iss` parameter sa mga tugon sa authorization (RFC 9207) at itali ang mga rehistradong
> kredensyal sa nag-isyu na authorization server. Ang Dynamic Client Registration
> ay hindi na ginagawang suporta; ang mga bagong implementasyon ay dapat gumamit ng Client ID Metadata Documents.
> Tingnan ang [Ano ang Nagbago sa MCP: Ang 2026-07-28 Specification](../01-CoreConcepts/mcp-2026-07-28.md)
> para sa buong listahan ng mga pagbabago sa authorization.

## 🏔️ MCP Security Summit Workshop (Sherpa)

Para sa **praktikal na pagsasanay sa seguridad**, lubos naming inirerekomenda ang **MCP Security Summit Workshop** (Sherpa) - isang komprehensibong guided expedition para sa pag-secure ng mga MCP server sa Microsoft Azure.

### Pangkalahatang Pagsusuri ng Workshop

Ang [MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) ay nagbibigay ng praktikal at maaaksiyong pagsasanay sa seguridad gamit ang napatunayang metodolohiyang "vulnerable → exploit → fix → validate". Gagawin mo:

- **Matuto sa Pamamagitan ng Pagsira**: Maranasan ang mga kahinaan sa pamamagitan ng pagsasamantala sa mga sadyang insecure na server
- **Gamitin ang Azure-Native Security**: Samantalahin ang Azure Entra ID, Key Vault, API Management, at AI Content Safety
- **Sundin ang Defense-in-Depth**: Umabante sa mga kampo na bumubuo ng komprehensibong mga patong ng seguridad
- **Ipatupad ang mga Pamantayan ng OWASP**: Bawat teknik ay tumutugma sa [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Makakuha ng Code para sa Produksyon**: Umalis na may gumagana at nasuring mga implementasyon

### Ruta ng Ekspedisyon

| Kampo | Pokus | Mga Panganib ng OWASP na Tinugunan |
|------|-------|---------------------|
| **Base Camp** | Mga pundamental ng MCP at kahinaan sa authentication | MCP01, MCP07 |
| **Camp 1: Identity** | OAuth 2.1, Azure Managed Identity, Key Vault | MCP01, MCP02, MCP07 |
| **Camp 2: Gateway** | API Management, Private Endpoints, pamamahala | MCP02, MCP06, MCP07, MCP09 |
| **Camp 3: I/O Security** | Prompt injection, proteksyon sa PII, content safety | MCP03, MCP05, MCP06, MCP10 |
| **Camp 4: Monitoring** | Log Analytics, dashboards, pagtuklas ng banta | MCP04, MCP08 |
| **The Summit** | Red Team / Blue Team integration test | Lahat |

**Simulan Dito**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Lalagyan ng Panganib sa Seguridad ng OWASP MCP Top 10

Detalyado sa [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) ang sampung pinaka-kritis na panganib sa seguridad para sa mga implementasyon ng MCP:

| Panganib | Paglalarawan | Mitigasyon sa Azure |
|------|-------------|------------------|
| **MCP01** | Hindi Maayos na Pamamahala ng Token at Paglalantad ng Lihim | Azure Key Vault, Managed Identity |
| **MCP02** | Pag-akyat ng Pribilehiyo sa pamamagitan ng Scope Creep | RBAC, Conditional Access |
| **MCP03** | Tool Poisoning | Pag-validate ng tool, pag-verify ng integridad |
| **MCP04** | Atake sa Software Supply Chain at Dependency Tampering | GitHub Advanced Security, dependency scanning |
| **MCP05** | Command Injection at Execution | Input validation, sandboxing |
| **MCP06** | Panlilinlang sa Intent Flow | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Hindi Sapat na Authentication at Authorization | Azure Entra ID, OAuth 2.1 na may PKCE |
| **MCP08** | Kakulangan sa Audit at Telemetry | Azure Monitor, Application Insights |
| **MCP09** | Shadow MCP Servers | API Center governance, network isolation |
| **MCP10** | Context Injection at Sobrang Pagbabahagi | Data classification, minimal exposure |

### Ebolusyon ng Authentication sa MCP

Malaki ang pag-usbong ng specification ng MCP sa paraan ng authentication at authorization:

- **Orihinal na Paraan**: Kailangan ng mga naunang specification na magpatupad ang mga developer ng custom authentication servers, kung saan ang mga MCP server ay gumaganap bilang OAuth 2.0 Authorization Servers na direktang namamahala sa authentication ng mga user
- **Kasalukuyang Pamantayan (`2026-07-28`)**: Maaari nang idelegate ng MCP servers ang authentication
  sa mga panlabas na identity provider tulad ng Microsoft Entra ID. Dapat ding
  ipatupad ng mga kliyente ang kasalukuyang mga pangangailangan sa issuer-validation at credential-binding.
- **Transport Layer Security**: Pinahusay na suporta para sa secure na mga mekanismo sa transportasyon na may angkop na mga pattern ng authentication para sa lokal (STDIO) at remote (Streamable HTTP) na koneksyon

## Seguridad ng Authentication at Authorization

### Mga Kasalukuyang Hamon sa Seguridad

Ang mga modernong implementasyon ng MCP ay humaharap sa ilang mga hamon sa authentication at authorization:

### Mga Panganib at Vector ng Banta

- **Maling Pagkonpigura ng Authorization Logic**: Ang may depektong pagpapatupad ng authorization sa mga MCP server ay maaaring maglantad ng sensitibong data at mali ang paglalapat ng mga control sa access
- **Komprumiso ng OAuth Token**: Ang pagnakaw ng token mula sa lokal na MCP server ay nagbibigay-daan sa mga uma-atake na magpanggap bilang mga server at ma-access ang downstream na mga serbisyo
- **Mga Kahinaan sa Token Passthrough**: Ang maling pamamahala sa token ay lumilikha ng mga bypass sa mga kontrol sa seguridad at mga puwang sa pananagutan
- **Sobrang mga Pahintulot**: Ang mga MCP server na may sobrang pribilehiyo ay lumalabag sa mga prinsipyo ng least privilege at pinalalawak ang mga attack surface

#### Token Passthrough: Isang Kritikal na Anti-Pattern

**Mahigpit na ipinagbabawal ang token passthrough** sa kasalukuyang MCP authorization specification dahil sa malubhang implikasyon sa seguridad:

##### Pag-iiwas sa Kontrol sa Seguridad
- Ang mga MCP server at downstream APIs ay nagpapatupad ng mahahalagang kontrol sa seguridad (rate limiting, request validation, traffic monitoring) na nakadepende sa tamang pagsusuri ng token
- Direktang paggamit ng token mula sa kliyente papunta sa API ang lumilikha ng paglabas sa mga mahahalagang proteksyon, na pinahihina ang arkitektura ng seguridad

##### Mga Hamon sa Pananagutan at Audit  
- Hindi nagagawang makilala ng mga MCP server ang mga kliyente gamit ang mga token na iniisyu sa itaas ng kanilang antas, kaya't nasisira ang mga audit trail
- Ang mga log ng downstream resource server ay nagpapakita ng maling pinagmulan ng mga kahilingan sa halip na ang mga aktwal na MCP server na nag-intermedyo
- Ang pagsisiyasat ng insidente at auditing para sa pagsunod ay nagiging mas mahirap

##### Mga Panganib ng Panlabas na Pag-agaw ng Data
- Ang hindi napapatunayang mga claim sa token ay nagpapahintulot sa masasamang aktor na may mga nakaw na token na gamitin ang mga MCP server bilang mga proxy para sa pag-agaw ng data
- Nagsisira ng tiwala ang mga paglabag sa trust boundary na nagbibigay-daan sa hindi awtorisadong mga pattern ng pag-access na nilalabag ang pinag-isang mga kontrol sa seguridad

##### Multi-Serbisyo na Mga Vector ng Atake
- Ang mga nakompromisong token na tinatanggap ng maraming serbisyo ay nagbibigay-daan sa lateral na galaw sa magkakaugnay na mga sistema
- Maaaring masira ang mga trust assumption sa pagitan ng mga serbisyo kapag hindi maalaman ang pinagmulan ng token

### Mga Kontrol at Mitigasyon sa Seguridad

**Kritikal na Mga Pangangailangan sa Seguridad:**

> **MANDATORY**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang mga token na hindi tahasang ini-isyu para sa MCP server

#### Mga Kontrol sa Authentication at Authorization

- **Masusing Rebyu sa Authorization**: Magsagawa ng komprehensibong pagsusuri ng authorization logic sa mga MCP server upang matiyak na tanging ang mga inaasahang gumagamit at kliyente lamang ang makakagamit sa sensitibong mga resources
  - **Gabayan sa Pagpapatupad**: [Azure API Management bilang Authentication Gateway para sa mga MCP Server](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasyon sa Identity**: [Paggamit ng Microsoft Entra ID para sa MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Ipatupad ang [pinakamahusay na kasanayan sa pagtitiyak at lifecycle ng token ng Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Suriin na tumutugma ang audience claims ng token sa pagkakakilanlan ng MCP server
  - Magpatupad ng tamang mga patakaran sa pag-ikot at pag-expire ng token
  - Iwasan ang token replay attacks at hindi awtorisadong paggamit

- **Protektadong Storage ng Token**: I-secure ang imbakan ng token gamit ang encryption kapwa sa pahinga at transit
  - **Pinakamahusay na Kasanayan**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Pagpapatupad ng Access Control

- **Prinsipyo ng Pinakamababang Pribilehiyo**: Bigyan lamang ang mga MCP server ng pinakamababang pahintulot na kailangan para sa inaasahang functionality
  - Regular na rebyu at pag-update ng mga pahintulot upang maiwasan ang privilege creep
  - **Dokumentasyon ng Microsoft**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Ipatupad ang detalyadong role assignments
  - Higpitan ang mga role sa tiyak na mga resource at aksyon
  - Iwasan ang malawak o hindi kailangang mga pahintulot na nagpapalawak sa mga attack surface

- **Patuloy na Pagmamanman ng Pahintulot**: Magpatupad ng tuloy-tuloy na pag-audit at pagmamanman sa access
  - Imonitor ang mga pattern ng paggamit ng pahintulot para sa mga anomalya
  - Agarang ayusin ang sobrang at hindi nagamit na mga pribilehiyo

## Mga Espesipikong Banta sa Seguridad ng AI

### Mga Atake sa Prompt Injection at Manipulasyon ng Tool

Ang mga modernong implementasyon ng MCP ay humaharap sa sopistikadong mga vector ng atake na espesipiko sa AI na hindi lubos na natutugunan ng mga tradisyonal na hakbang sa seguridad:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

Ang **Indirect Prompt Injection** ay isa sa mga pinakamahalagang kahinaan sa mga sistemang AI na may MCP. Ang mga uma-atake ay naglalagay ng mapanirang mga utos sa loob ng panlabas na nilalaman—mga dokumento, web pages, emails, o mga pinanggagalingan ng data—na pinoproseso ng mga sistemang AI bilang lehitimong utos.

**Mga Senaryo ng Atake:**
- **Pagsusustansya sa Dokumento**: Mga mapanirang utos na nakatago sa mga dokumentong pinoproseso na nagdudulot ng hindi inaasahang aksyon mula sa AI
- **Eksploytasyon ng Nilalaman sa Web**: Mga napinsalang pahina ng web na naglalaman ng naka-embed na prompts na gumagawa ng manipulasyon sa asal ng AI kapag ini-scrape
- **Atake sa Email**: Mga mapanirang prompt sa mga email na nagpapabunyag sa AI assistant ng impormasyon o nagpapagawa ng hindi awtorisadong aksyon
- **Kontaminasyon ng Pinanggagalingan ng Data**: Mga napinsalang database o API na naghahatid ng polusyon sa nilalaman para sa mga sistemang AI

**Tunay na Epekto**: Ang mga atakeng ito ay maaaring magresulta sa pag-agaw ng data, paglabag sa privacy, paglikha ng mapanganib na nilalaman, at manipulasyon ng mga interaksyon ng user. Para sa detalyadong pagsusuri, tingnan ang [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/tl/prompt-injection.ed9fbfde297ca877.webp)

#### **Tool Poisoning Attacks**

Ang **Tool Poisoning** ay target ang metadata na nagtatakda sa MCP tools, sinasamantala kung paano iniintindihan ng mga LLM ang mga paglalarawan ng tool at mga parametro para gawin ang mga desisyon sa pag-eexecute.

**Mga Mekanismo ng Atake:**
- **Manipulasyon ng Metadata**: Naglalagay ang uma-atake ng mga mapanirang utos sa mga paglalarawan ng tool, depinisyon ng parametro, o mga halimbawa ng paggamit
- **Hindi Nakikitang mga Utos**: Mga nakatagong prompts sa metadata ng tool na pinoproseso ng mga modelo ng AI ngunit hindi nakikita ng mga tao
- **Dynamic Tool Modification ("Rug Pulls")**: Ang mga tool na inaprubahan ng mga user ay kalaunan binabago para gumawa ng masamang aksyon nang hindi alam ng user
- **Parameter Injection**: Mga mapanirang nilalaman na inilalagay sa mga schema ng parametro ng tool na nakakaapekto sa pag-uugali ng modelo


**Mga Panganib sa Hosted Server**: Ang mga remote MCP server ay nagdudulot ng mas mataas na panganib dahil maaaring ma-update ang mga depinisyon ng tool pagkatapos ng inisyal na pag-apruba ng gumagamit, na naglilikha ng mga sitwasyon kung saan ang mga dati nang ligtas na tool ay nagiging malisyoso. Para sa komprehensibong pagsusuri, tingnan ang [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/tl/tool-injection.3b0b4a6b24de6bef.webp)

#### **Karagdagang Mga AI na Vector ng Atake**

- **Cross-Domain Prompt Injection (XPIA)**: Mga sopistikadong atake na gumagamit ng nilalaman mula sa iba't ibang domain upang lampasan ang mga kontrol sa seguridad
- **Dynamic Capability Modification**: Mga real-time na pagbabago sa mga kakayahan ng tool na nakakalusot sa mga unang pagtatasa ng seguridad
- **Context Window Poisoning**: Mga atake na manipulahin ang malalaking context window upang itago ang malisyosong mga utos
- **Model Confusion Attacks**: Pagsasamantala sa mga limitasyon ng modelo upang lumikha ng hindi inaasahan o hindi ligtas na mga pag-uugali


### Epekto ng Panganib sa Seguridad ng AI

**Mataas na Epekto ng Mga Bunga:**
- **Pagkawatak ng Data**: Hindi awtorisadong pag-access at pagnanakaw ng sensitibong data ng enterprise o personal na impormasyon
- **Paglabag sa Privacy**: Pagbunyag ng personal na impormasyong maaaring makilala (PII) at kumpidensyal na data ng negosyo  
- **Pagmanipula ng Sistema**: Hindi inaasahang mga pagbabago sa mga kritikal na sistema at workflows
- **Pagnanakaw ng Kredensyal**: Pagsira sa mga authentication token at service credentials
- **Lateral Movement**: Paggamit ng mga kompromisadong AI system bilang mga puntahan para sa mas malawak na mga pag-atake sa network

### Mga Solusyon sa Seguridad ng Microsoft AI

#### **AI Prompt Shields: Advanced Protection Against Injection Attacks**

Nagbibigay ang Microsoft **AI Prompt Shields** ng komprehensibong depensa laban sa parehong direktang at di-direktang mga injection attack sa pamamagitan ng maraming mga layer ng seguridad:

##### **Pangunahing Mekanismo ng Proteksyon:**

1. **Advanced Detection & Filtering**
   - Mga algorithm ng machine learning at mga teknik sa NLP na nakakakita ng malisyosong mga utos sa panlabas na nilalaman
   - Real-time na pagsusuri ng mga dokumento, web page, email, at mga pinagkukunan ng data para sa mga nakatagong panganib
   - Kontekstwal na pag-unawa sa lehitimo laban sa malisyosong mga pattern ng prompt

2. **Spotlighting Techniques**  
   - Nakikilala ang pagkakaiba ng mga pinagkakatiwalaang sistema ng mga utos at mga posibleng kompromisadong panlabas na input
   - Mga paraan ng pagbabago ng teksto na nagpapahusay sa kaugnayan ng modelo habang iniaalis ang malisyosong nilalaman
   - Tinutulungan ang mga AI system na mapanatili ang tamang hierarchy ng mga utos at i-ignore ang mga injected na command

3. **Delimiter & Datamarking Systems**
   - Maliwanag na pagpapakahulugan ng hangganan sa pagitan ng mga pinagkakatiwalaang mensahe ng sistema at panlabas na input na teksto
   - Mga espesyal na marka na nagha-highlight ng mga hangganan sa pagitan ng pinagkakatiwalaan at hindi pinagkakatiwalaang mga pinagkukunan ng data
   - Malinaw na paghihiwalay na pumipigil sa kalituhan ng utos at sa hindi awtorisadong pagpapatupad ng mga command

4. **Continuous Threat Intelligence**
   - Patuloy na minomonitor ng Microsoft ang mga umuusbong na mga pattern ng atake at ina-update ang mga depensa
   - Proactive na pangingisda ng panganib para sa mga bagong teknik ng injection at mga vector ng atake
   - Regular na pag-update ng security model upang mapanatili ang bisa laban sa mga nagbabagong panganib

5. **Azure Content Safety Integration**
   - Bahagi ng komprehensibong Azure AI Content Safety suite
   - Karagdagang deteksyon para sa mga pagtatangka ng jailbreak, nakasasama o mapanganib na nilalaman, at paglabag sa mga polisiya sa seguridad
   - Pinagsama-samang mga kontrol sa seguridad sa mga bahagi ng AI application

**Mga Mapagkukunan ng Implementasyon**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/tl/prompt-shield.ff5b95be76e9c78c.webp)


## Mga Advanced na Banta sa Seguridad ng MCP

### Mga Kahinaan sa Session Hijacking

Ang **session hijacking** ay kumakatawan sa isang kritikal na vector ng atake sa mga stateful MCP implementation kung saan ang hindi awtorisadong mga partido ay nakakakuha at inaabuso ang lehitimong mga session identifier upang magpanggap bilang mga kliyente at magsagawa ng mga hindi awtorisadong aksyon.

#### **Mga Senaryo ng Atake at Panganib**

- **Session Hijack Prompt Injection**: Ang mga nag-atake na may mga ninakaw na session ID ay nag-iinject ng malisyosong mga kaganapan sa mga server na nagbabahagi ng session state, na posibleng magdulot ng mapanganib na mga aksyon o pag-access sa sensitibong data
- **Direct Impersonation**: Ang mga ninakaw na session ID ay nagpapahintulot ng direktang mga tawag sa MCP server na lumalampas sa authentication, tinatrato ang mga nag-atake bilang mga lehitimong gumagamit
- **Kompromisadong Resumable Streams**: Maaaring tapusin ng mga nag-atake ang mga kahilingan nang maaga, na nagiging sanhi para sa mga lehitimong kliyente na mag-resume gamit ang posibleng malisyosong nilalaman

#### **Mga Kontrol sa Seguridad para sa Pamamahala ng Session**

**Mga Kritikal na Kinakailangan:**
- **Pagpapatunay ng Awtorisasyon**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** mag-verify ng LAHAT ng mga papasok na kahilingan at **HINDI DAPAT** umasa sa mga session para sa authentication
- **Secure Session Generation**: Gumamit ng cryptographically secure, non-deterministic session ID na nilikha gamit ang mga secure random number generator
- **User-Specific Binding**: Itali ang mga session ID sa impormasyong tukoy sa gumagamit gamit ang mga format tulad ng `<user_id>:<session_id>` upang maiwasan ang pag-abuso sa cross-user session
- **Pamamahala ng Lifecycle ng Session**: Ipatupad ang tamang expiration, rotation, at invalidation upang limitahan ang mga bintana ng kahinaan
- **Transport Security**: Kinakailangang HTTPS para sa lahat ng komunikasyon upang maiwasan ang interception ng session ID

### Problema ng Confused Deputy

Nangyayari ang **confused deputy problem** kapag ang mga MCP server ay kumikilos bilang mga authentication proxy sa pagitan ng mga kliyente at mga third-party na serbisyo, na lumilikha ng mga pagkakataon para sa bypass ng authorization sa pamamagitan ng static client ID exploitation.

#### **Mekaniks ng Atake at Panganib**

- **Cookie-based Consent Bypass**: Ang naunang authentication ng gumagamit ay lumilikha ng mga consent cookie na sinasamantala ng mga attacker sa pamamagitan ng malisyosong mga kahilingan ng awtorisasyon na may mga ginawa na redirect URI
- **Pagnanakaw ng Authorization Code**: Maaaring magdulot ang mga umiiral na consent cookie upang laktawan ng mga authorization server ang mga consent screen, na nire-redirect ang mga code sa mga endpoint na kontrolado ng attacker  
- **Hindi Awtorisadong API Access**: Pinapayagan ng mga ninakaw na authorization code ang token exchange at pamamagitang-pagpanggap ng gumagamit na walang malinaw na pag-apruba

#### **Mga Estratehiya sa Pagbawas**

**Mga Kinakailangang Kontrol:**
- **Mga Kinakailangan para sa Explicit Consent**: Ang mga MCP proxy server na gumagamit ng static client IDs **DAPAT** kumuha ng pahintulot ng gumagamit para sa bawat dynamic na rehistradong kliyente
- **Implementasyon ng Seguridad ng OAuth 2.1**: Sundin ang mga kasalukuyang pinakamahusay na kasanayan sa seguridad ng OAuth kabilang ang PKCE (Proof Key for Code Exchange) para sa lahat ng kahilingan ng awtorisasyon
- **Mahigpit na Validasyon ng Kliyente**: Ipatupad ang masusing validasyon ng mga redirect URI at client identifier upang maiwasan ang pagsasamantala

### Mga Kahinaan sa Token Passthrough  

Ang **token passthrough** ay kumakatawan sa isang sadyang anti-pattern kung saan tinatanggap ng mga MCP server ang mga token ng kliyente nang walang tamang validasyon at ipinapasa ang mga ito sa mga downstream na API, na nilalabag ang mga espesipikasyon ng awtorisasyon ng MCP.

#### **Mga Implikasyon sa Seguridad**

- **Circumvention ng Kontrol**: Direktang paggamit ng token mula sa kliyente papuntang API na lumalampas sa mga kritikal na limitasyon sa rate, validasyon, at monitoring na kontrol
- **Pagkasira ng Audit Trail**: Ang mga token na ibinigay sa upstream ay ginagawang imposible ang pagkilala ng kliyente, na sumisira sa kakayahan sa pagsisiyasat ng insidente
- **Data Exfiltration na Nakabase sa Proxy**: Pinapayagan ng mga hindi na-validate na token ang mga malisyosong aktor na gamitin ang mga server bilang proxy para sa hindi awtorisadong pag-access ng data
- **Paglabag sa Trust Boundary**: Maaaring malabag ang mga tiwala ng downstream services kapag hindi ma-verify ang pinagmulan ng token
- **Pagpapalawak ng Atake sa Maramihang Serbisyo**: Pinapayagan ng mga tinanggap na kompromisadong token ang lateral movement sa iba't ibang serbisyo

#### **Mga Kinakailangang Kontrol sa Seguridad**

**Hindi mapag-uusapang Kinakailangan:**
- **Token Validation**: Ang mga MCP server **HINDI DAPAT** tumanggap ng mga token na hindi tahasang inilabas para sa MCP server
- **Audience Verification**: Laging i-validate na tumutugma ang audience claims ng token sa pagkakakilanlan ng MCP server
- **Tamang Lifecycle ng Token**: Ipatupad ang mga maikling-buhay na access token na may secure rotation na mga pamamaraan


## Seguridad sa Supply Chain para sa mga AI System

Ang seguridad sa supply chain ay umunlad lampas sa tradisyunal na mga software dependency upang saklawin ang buong AI ecosystem. Ang mga modernong MCP implementation ay dapat mahigpit na beripikahin at imonitor ang lahat ng mga bahagi na may kaugnayan sa AI, dahil bawat isa ay nagdadala ng posibleng kahinaan na maaaring makompromiso ang integridad ng sistema.

### Pinalawak na mga Komponent ng AI Supply Chain

**Tradisyunal na Mga Software Dependency:**
- Mga open-source na library at framework
- Mga container image at mga base system  
- Mga development tool at build pipeline
- Mga infrastructure component at serbisyo

**Mga Elemento ng Supply Chain na Tiyak sa AI:**
- **Foundation Models**: Mga pre-trained na modelo mula sa iba't ibang tagapagbigay na nangangailangan ng beripikasyon ng pinagmulan
- **Embedding Services**: Mga panlabas na vectorization at semantic search na serbisyo
- **Context Providers**: Mga pinagkukunan ng data, knowledge base, at mga document repository  
- **Third-party APIs**: Mga panlabas na serbisyo ng AI, ML pipeline, at mga endpoint sa pagproseso ng data
- **Model Artifacts**: Mga timbang, konfigurasyon, at mga fine-tuned na variant ng modelo
- **Training Data Sources**: Mga dataset na ginagamit para sa pagsasanay at fine-tuning ng modelo

### Komprehensibong Estratehiya sa Seguridad ng Supply Chain

#### **Pagberipika at Pagtitiwala sa mga Komponent**
- **Pag-validate ng Pinagmulan**: Beripikahin ang pinagmulan, lisensya, at integridad ng lahat ng mga AI component bago ang integrasyon
- **Pagsusuri sa Seguridad**: Magsagawa ng vulnerability scans at security reviews para sa mga modelo, pinagkukunan ng data, at mga AI serbisyo
- **Pagsusuri ng Reputasyon**: Suriin ang track record ng seguridad at mga gawi ng mga tagapagbigay ng AI serbisyo
- **Pagberipika ng Pagsunod sa Regulasyon**: Tiyakin na ang lahat ng bahagi ay tumutugon sa mga pangangailangan ng seguridad ng organisasyon at regulasyon

#### **Secure Deployment Pipelines**  
- **Automated CI/CD Security**: Isama ang security scanning sa kabuuan ng mga automated deployment pipeline
- **Integridad ng Artifact**: Ipatupad ang cryptographic verification para sa lahat ng deployed artifact (code, modelo, configuração)
- **Staged Deployment**: Gumamit ng progressive deployment strategies na may security validation sa bawat yugto
- **Mga Trusted Artifact Repository**: Mag-deploy lamang mula sa mga verified at secure na artifact registries at repositories

#### **Patuloy na Pagmamanman at Pagsagot**
- **Dependency Scanning**: Patuloy na pagmo-monitor ng vulnerability para sa lahat ng software at AI component dependency
- **Pagsubaybay sa Modelo**: Tuloy-tuloy na pagsusuri ng pag-uugali ng modelo, performance drift, at mga anomaliya sa seguridad
- **Pagsubaybay sa Kalusugan ng Serbisyo**: I-monitor ang mga panlabas na AI serbisyo para sa availability, security incidents, at mga pagbabago sa polisiya
- **Integrasyon ng Threat Intelligence**: Isama ang mga threat feed na partikular para sa AI at ML security risks

#### **Kontrol sa Access at Least Privilege**
- **Mga Pahintulot sa Antas ng Komponent**: I-limit ang access sa mga modelo, data, at serbisyo batay sa pangangailangan ng negosyo
- **Pamamahala ng Service Account**: Ipatupad ang dedikadong mga service account na may pinakamababang kailangang pahintulot
- **Segmentasyon ng Network**: I-isolate ang mga AI component at limitahan ang access sa network sa pagitan ng mga serbisyo
- **Kontrol ng API Gateway**: Gumamit ng centralized API gateways upang kontrolin at imonitor ang access sa panlabas na AI serbisyo

#### **Pagsagot sa Insidente at Pag-recover**
- **Mga Mabilis na Proseso ng Pagsagot**: Itinatag na mga proseso para sa pag-patch o pagpapalit ng mga kompromisadong AI component
- **Pag-ikot ng Kredensyal**: Automated na sistema para sa pag-ikot ng mga sikreto, API key, at service credentials
- **Kakayahan sa Rollback**: Kakayahang mabilis na magbalik sa mga dating kilala at ligtas na bersyon ng mga AI component
- **Pag-recover mula sa Supply Chain Breach**: Mga espesipikong proseso para sa pagtugon sa mga kompromisadong upstream AI service

### Mga Tool at Integrasyon sa Seguridad ng Microsoft

Nagbibigay ang **GitHub Advanced Security** ng komprehensibong proteksyon sa supply chain kabilang ang:
- **Secret Scanning**: Automated na pag-detect ng mga kredensyal, API key, at token sa mga repositoryo
- **Dependency Scanning**: Pagsusuri ng vulnerability para sa mga open-source na dependency at library
- **CodeQL Analysis**: Static code analysis para sa mga security vulnerability at isyu sa coding
- **Insights sa Supply Chain**: Visibility sa kalusugan at estado ng seguridad ng mga dependency

**Integrasyon ng Azure DevOps & Azure Repos:**
- Seamless na integrasyon ng security scanning sa mga Microsoft development platform
- Automated na mga security check sa Azure Pipelines para sa mga AI workload
- Enforcement ng polisiya para sa secure na deployment ng mga AI component

**Internal na Gawain ng Microsoft:**
Malawak na ipinatutupad ng Microsoft ang mga kasanayan sa seguridad ng supply chain sa lahat ng produkto. Alamin ang tungkol sa mga napatunayang pamamaraan sa [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Pinakamahuhusay na Kasanayan sa Seguridad ng Patakaran

Pinapamana at pinapalawak ng mga implementasyon ng MCP ang kasalukuyang seguridad na posisyon ng inyong organisasyon. Ang pagpapalakas ng mga pundasyong kasanayan sa seguridad ay makabuluhang nagpapabuti sa kabuuang seguridad ng mga AI system at MCP deployment.

### Pangunahing Mga Prinsipyo ng Seguridad

#### **Mga Praktis sa Secure Development**
- **Pagsunod sa OWASP**: Protektahan laban sa [OWASP Top 10](https://owasp.org/www-project-top-ten/) na mga kahinaan ng web application
- **Mga Proteksyon na Tiyak sa AI**: Ipatupad ang mga kontrol para sa [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Secure Secrets Management**: Gumamit ng dedikadong vault para sa mga token, API key, at sensitibong data ng konfigurasyon
- **End-to-End Encryption**: Ipatupad ang secure na komunikasyon sa lahat ng bahagi ng application at daloy ng data
- **Input Validation**: Masusing pag-validate ng lahat ng input ng user, API parameter, at pinagkukunan ng data

#### **Infrastructure Hardening**
- **Multi-Factor Authentication**: Mandatory MFA para sa lahat ng administratibong account at service account
- **Patch Management**: Automated, napapanahong pag-patch para sa operating system, framework, at dependency  
- **Integrasyon sa Identity Provider**: Sentralisadong pamamahala ng identity gamit ang enterprise identity provider (Microsoft Entra ID, Active Directory)
- **Segmentasyon ng Network**: Lohikal na pag-isolate ng mga MCP component upang limitahan ang potensyal ng lateral movement
- **Prinsipyo ng Least Privilege**: Pinakamababang kinakailangang pahintulot para sa lahat ng bahagi ng sistema at mga account

#### **Security Monitoring at Detection**
- **Komprehensibong Logging**: Detalyadong pag-log ng mga aktibidad ng AI application, kabilang ang pakikipag-ugnayan ng MCP client-server
- **Integrasyon ng SIEM**: Sentralisadong security information at event management para sa pagtuklas ng anomalya
- **Behavioral Analytics**: AI-powered monitoring upang matukoy ang hindi pangkaraniwang pattern sa sistema at pag-uugali ng gumagamit
- **Threat Intelligence**: Integrasyon ng mga panlabas na threat feed at mga indikator ng kompromiso (IOC)
- **Incident Response**: Malinaw na mga proseso para sa pagtuklas ng insidente sa seguridad, pagtugon, at pag-recover

#### **Zero Trust Architecture**
- **Huwag Manalig, Laging Mag-verify**: Patuloy na pagpapatunay sa mga gumagamit, mga device, at koneksyon sa network
- **Micro-Segmentation**: Detalyadong kontrol sa network na naghihiwalay ng bawat workload at serbisyo
- **Identity-Centric Security**: Mga polisiya sa seguridad na nakabase sa beripikadong pagkakakilanlan kaysa sa lokasyon ng network
- **Patuloy na Pagsusuri ng Panganib**: Dinamikong pagtatasa ng security posture batay sa kasalukuyang konteksto at pag-uugali
- **Conditional Access**: Mga kontrol sa access na umaangkop ayon sa mga factor ng panganib, lokasyon, at tiwala sa device

### Mga Pattern ng Integrasyon ng Enterprise

#### **Integrasyon sa Microsoft Security Ecosystem**
- **Microsoft Defender for Cloud**: Komprehensibong pamamahala ng posture sa seguridad ng cloud
- **Azure Sentinel**: Cloud-native SIEM at SOAR na kakayahan para sa proteksyon ng AI workload
- **Microsoft Entra ID**: Enterprise identity at access management na may mga polisiya ng conditional access
- **Azure Key Vault**: Sentralisadong pamamahala ng sikreto na may hardware security module (HSM) backing
- **Microsoft Purview**: Pamamahala ng data at pagsunod sa mga regulasyon para sa mga pinagkukunan ng AI data at workflow

#### **Pagsunod sa Regulasyon at Pamamahala**
- **Pagsunod sa Regulasyon**: Tiyakin na ang mga MCP implementation ay nakakatugon sa mga espesipikong pang-industriyang pangangailangan sa pagsunod (GDPR, HIPAA, SOC 2)

- **Pagsusuri ng Datos**: Tamang pagkategorya at paghawak ng sensitibong datos na pinoproseso ng mga sistemang AI
- **Audit Trails**: Komprehensibong pag-log para sa pagsunod sa regulasyon at pagsisiyasat na forensic
- **Mga Kontrol sa Privacy**: Pagpapatupad ng mga prinsipyo ng privacy-by-design sa arkitektura ng sistema ng AI
- **Pamamahala ng Pagbabago**: Pormal na mga proseso para sa pagsusuri ng seguridad ng mga pagbabago sa sistema ng AI

Ang mga pundasyong praktikang ito ay lumilikha ng matatag na baseline ng seguridad na nagpapahusay sa bisa ng mga kontrol sa seguridad na partikular sa MCP at nagbibigay ng komprehensibong proteksyon para sa mga aplikasyon na pinapatakbo ng AI.

## Mga Pangunahing Paalala sa Seguridad

- **Patong-patong na Lapit sa Seguridad**: Pagsamahin ang mga pundasyong praktika ng seguridad (secure coding, least privilege, supply chain verification, continuous monitoring) kasama ang mga kontrol na partikular sa AI para sa komprehensibong proteksyon

- **Natatanging Tanawin ng Banta sa AI**: Ang mga MCP system ay nahaharap sa mga natatanging panganib kabilang ang prompt injection, tool poisoning, session hijacking, confused deputy problems, token passthrough vulnerabilities, at labis na mga permiso na nangangailangan ng espesyal na mga lunas

- **Kahusayan sa Pagpapatunay at Awtorisasyon**: Magpatupad ng matibay na pagpapatunay gamit ang external identity providers (Microsoft Entra ID), ipatupad ang tamang beripikasyon ng token, at huwag kailanman tanggapin ang mga token na hindi malinaw na inilabas para sa iyong MCP server

- **Pag-iwas sa Atake sa AI**: Gumamit ng Microsoft Prompt Shields at Azure Content Safety para ipagtanggol laban sa mga indirect prompt injection at tool poisoning attack, habang sinusuri ang metadata ng tool at mino-monitor ang mga dynamic changes

- **Seguridad sa Session at Transportasyon**: Gumamit ng cryptographically secure, non-deterministic na session IDs na nakatali sa pagkakakilanlan ng user, ipatupad ang wastong pamamahala sa lifecycle ng session, at huwag kailanman gamitin ang mga session para sa pagpapatunay

- **Pinakamahusay na Praktika sa Seguridad ng OAuth**: Iwasan ang confused deputy attacks sa pamamagitan ng malinaw na pahintulot ng user para sa dynamically registered clients, tamang implementasyon ng OAuth 2.1 na may PKCE, at mahigpit na beripikasyon ng redirect URI  

- **Mga Prinsipyo ng Seguridad sa Token**: Iwasan ang mga anti-pattern ng token passthrough, suriin ang mga claim ng audience ng token, magpatupad ng panandaliang token na may secure na rotation, at panatilihin ang malinaw na hangganan ng pagtitiwala

- **Komprehensibong Seguridad ng Supply Chain**: Tratuhin ang lahat ng bahagi ng AI ecosystem (mga modelo, embeddings, context providers, external APIs) gamit ang parehong siguridad na istrikto gaya ng mga tradisyunal na software dependencies

- **Tuloy-tuloy na Pagbabago**: Manatiling napapanahon sa mabilis na nagbabagong espesipikasyon ng MCP, mag-ambag sa mga pamantayan ng komunidad para sa seguridad, at panatilihin ang adaptive security posture habang umuunlad ang protokol

- **Integrasyon ng Seguridad ng Microsoft**: Gamitin ang komprehensibong ecosystem ng seguridad ng Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para sa pinahusay na proteksyon sa deployment ng MCP

## Komprehensibong Mga Pinagkukunan

### **Opisyal na Dokumentasyon ng Seguridad ng MCP**
- [MCP Specification (Current: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **Mga Pinagkukunan sa Seguridad ng OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Komprehensibong OWASP MCP Top 10 na may patnubay sa implementasyon sa Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Opisyal na mga panganib sa seguridad ng OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on na pagsasanay sa seguridad para sa MCP sa Azure

### **Mga Pamantayan sa Seguridad at Pinakamahusay na Praktika**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Pananaliksik at Pagsusuri sa Seguridad ng AI**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Mga Solusyon sa Seguridad ng Microsoft**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Mga Gabay sa Implementasyon at Tutorial**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps at Seguridad ng Supply Chain**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Karagdagang Dokumentasyon sa Seguridad**

Para sa komprehensibong gabay sa seguridad, sumangguni sa mga espesyalisadong dokumentong ito sa seksyong ito:

- **[CIMD and DCR Authorization Sample](./samples/cimd-dcr-auth/README.md)** - Maaaring patakbuhing TypeScript MCP `2026-07-28` resource server na naghahambing ng preferred Client ID Metadata Documents sa deprecated Dynamic Client Registration fallback
- **[MCP Security Best Practices](./mcp-security-best-practices.md)** - Kumpletong pinakamahusay na praktika sa seguridad para sa mga implementasyon ng MCP
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Praktikal na mga halimbawa ng implementasyon para sa pagsasama ng Azure Content Safety  
- **[MCP Security Controls](./mcp-security-controls.md)** - Pinakabagong mga kontrol at teknika sa seguridad para sa mga deployment ng MCP
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Mabilisang sanggunian para sa mahahalagang praktika sa seguridad ng MCP
- **[BlueHat 2026: Securing the future of AI: Securing MCP with defense in depth patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Mga defense-in-depth pattern mula sa Microsoft Security Response Center (MSRC)

### **Hands-On na Pagsasanay sa Seguridad**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Komprehensibong hands-on na workshop para sa pag-seguro ng mga MCP server sa Azure na may progresibong mga camp mula Base Camp hanggang Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Reference architecture at gabay sa implementasyon para sa lahat ng panganib sa OWASP MCP Top 10

---

## Ano ang Susunod

Susunod: [Chapter 3: Getting Started](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
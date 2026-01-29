# MCP Security: Komprehensibong Proteksyon para sa mga AI System

[![MCP Security Best Practices](../../../translated_images/tl/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Ang seguridad ay pundamental sa disenyo ng AI system, kaya't inuuna namin ito bilang aming pangalawang seksyon. Ito ay naaayon sa prinsipyo ng Microsoft na **Secure by Design** mula sa [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Ang Model Context Protocol (MCP) ay nagdadala ng makapangyarihang bagong kakayahan sa mga AI-driven na aplikasyon habang nagpapakilala ng mga natatanging hamon sa seguridad na lampas sa tradisyunal na panganib sa software. Ang mga MCP system ay humaharap sa parehong mga kilalang isyu sa seguridad (secure coding, least privilege, supply chain security) at mga bagong banta na partikular sa AI kabilang ang prompt injection, tool poisoning, session hijacking, confused deputy attacks, token passthrough vulnerabilities, at dynamic capability modification.

Tinutuklas ng araling ito ang pinakamahalagang panganib sa seguridad sa mga implementasyon ng MCP—sumasaklaw sa authentication, authorization, labis na mga permiso, indirect prompt injection, session security, confused deputy problems, token management, at supply chain vulnerabilities. Matututuhan mo ang mga praktikal na kontrol at pinakamahusay na mga kasanayan upang mabawasan ang mga panganib na ito habang ginagamit ang mga solusyon ng Microsoft tulad ng Prompt Shields, Azure Content Safety, at GitHub Advanced Security upang palakasin ang iyong MCP deployment.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- **Kilalanin ang mga Natatanging Banta sa MCP**: Tukuyin ang mga natatanging panganib sa seguridad sa mga MCP system kabilang ang prompt injection, tool poisoning, labis na mga permiso, session hijacking, confused deputy problems, token passthrough vulnerabilities, at panganib sa supply chain
- **Ipatupad ang mga Kontrol sa Seguridad**: Magpatupad ng epektibong mga mitigasyon kabilang ang matibay na authentication, least privilege access, secure token management, session security controls, at supply chain verification
- **Gamitin ang mga Solusyon sa Seguridad ng Microsoft**: Unawain at i-deploy ang Microsoft Prompt Shields, Azure Content Safety, at GitHub Advanced Security para sa proteksyon ng MCP workload
- **Patunayan ang Seguridad ng Tool**: Kilalanin ang kahalagahan ng tool metadata validation, pagmamanman para sa mga dynamic na pagbabago, at pagtatanggol laban sa indirect prompt injection attacks
- **Isama ang Pinakamahusay na Kasanayan**: Pagsamahin ang mga itinatag na pundasyon ng seguridad (secure coding, server hardening, zero trust) sa mga kontrol na partikular sa MCP para sa komprehensibong proteksyon

# MCP Security Architecture & Controls

Ang mga modernong implementasyon ng MCP ay nangangailangan ng mga layered security approach na tumutugon sa parehong tradisyunal na seguridad ng software at mga banta na partikular sa AI. Ang mabilis na pag-unlad ng MCP specification ay patuloy na pinapahusay ang mga kontrol sa seguridad nito, na nagpapahintulot ng mas mahusay na integrasyon sa mga enterprise security architecture at mga itinatag na pinakamahusay na kasanayan.

Ipinapakita ng pananaliksik mula sa [Microsoft Digital Defense Report](https://aka.ms/mddr) na **98% ng mga naiulat na paglabag ay maiiwasan sa pamamagitan ng matibay na security hygiene**. Ang pinakaepektibong estratehiya sa proteksyon ay pinagsasama ang mga pundamental na kasanayan sa seguridad sa mga kontrol na partikular sa MCP—ang mga napatunayang baseline security measures ay nananatiling pinakaepektibo sa pagbawas ng pangkalahatang panganib sa seguridad.

## Kasalukuyang Kalagayan ng Seguridad

> **Note:** Ang impormasyong ito ay sumasalamin sa mga pamantayan sa seguridad ng MCP hanggang sa **Disyembre 18, 2025**. Ang MCP protocol ay patuloy na mabilis na umuunlad, at ang mga susunod na implementasyon ay maaaring magpakilala ng mga bagong pattern ng authentication at pinahusay na mga kontrol. Palaging sumangguni sa kasalukuyang [MCP Specification](https://spec.modelcontextprotocol.io/), [MCP GitHub repository](https://github.com/modelcontextprotocol), at [security best practices documentation](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) para sa pinakabagong gabay.

### Ebolusyon ng MCP Authentication

Malaki ang naging pagbabago ng MCP specification sa paraan ng authentication at authorization:

- **Orihinal na Paraan**: Ang mga unang specification ay nangangailangan ng mga developer na magpatupad ng custom authentication servers, kung saan ang MCP servers ay kumikilos bilang OAuth 2.0 Authorization Servers na direktang namamahala sa user authentication
- **Kasalukuyang Pamantayan (2025-11-25)**: Ang na-update na specification ay nagpapahintulot sa MCP servers na i-delegate ang authentication sa mga external identity providers (tulad ng Microsoft Entra ID), na nagpapabuti sa security posture at nagpapababa ng komplikasyon sa implementasyon
- **Transport Layer Security**: Pinahusay na suporta para sa secure transport mechanisms na may tamang authentication patterns para sa parehong lokal (STDIO) at remote (Streamable HTTP) na koneksyon

## Seguridad sa Authentication at Authorization

### Mga Hamon sa Seguridad Ngayon

Ang mga modernong implementasyon ng MCP ay humaharap sa ilang mga hamon sa authentication at authorization:

### Mga Panganib at Vector ng Banta

- **Maling Pag-configure ng Authorization Logic**: Ang depektibong implementasyon ng authorization sa MCP servers ay maaaring maglantad ng sensitibong data at maling paglalapat ng access controls
- **Pagkumpromiso ng OAuth Token**: Ang pagnanakaw ng token mula sa lokal na MCP server ay nagpapahintulot sa mga attacker na magpanggap bilang mga server at ma-access ang downstream services
- **Token Passthrough Vulnerabilities**: Ang maling paghawak ng token ay lumilikha ng bypass sa mga security control at mga puwang sa pananagutan
- **Labis na Mga Pahintulot**: Ang MCP servers na may sobra-sobrang pribilehiyo ay lumalabag sa prinsipyo ng least privilege at nagpapalawak ng attack surface

#### Token Passthrough: Isang Kritikal na Anti-Pattern

**Ang token passthrough ay tahasang ipinagbabawal** sa kasalukuyang MCP authorization specification dahil sa malubhang implikasyon sa seguridad:

##### Pag-iwas sa Mga Kontrol sa Seguridad
- Ang MCP servers at downstream APIs ay nagpapatupad ng mahahalagang security controls (rate limiting, request validation, traffic monitoring) na nakasalalay sa tamang token validation
- Ang direktang paggamit ng client-to-API token ay nilalampasan ang mga mahahalagang proteksyong ito, na sumisira sa security architecture

##### Mga Hamon sa Pananagutan at Audit  
- Hindi makikilala ng MCP servers ang mga client na gumagamit ng mga token na ibinigay ng upstream, na nagwawasak sa audit trails
- Ang mga log ng downstream resource server ay nagpapakita ng maling pinagmulan ng mga request sa halip na ang tunay na MCP server na tagapamagitan
- Ang pagsisiyasat ng insidente at compliance auditing ay nagiging mas mahirap

##### Panganib sa Pag-exfiltrate ng Data
- Ang mga hindi na-validate na token claims ay nagpapahintulot sa mga malisyosong aktor na may mga ninakaw na token na gamitin ang MCP servers bilang proxy para sa pag-exfiltrate ng data
- Ang paglabag sa trust boundary ay nagpapahintulot ng hindi awtorisadong mga pattern ng pag-access na nilalampasan ang mga nakatakdang security controls

##### Mga Vector ng Atake sa Maramihang Serbisyo
- Ang mga kompromisadong token na tinatanggap ng maraming serbisyo ay nagpapahintulot ng lateral movement sa mga konektadong sistema
- Ang mga trust assumptions sa pagitan ng mga serbisyo ay maaaring malabag kapag hindi mapatunayan ang pinagmulan ng token

### Mga Kontrol sa Seguridad at Mga Mitigasyon

**Kritikal na Mga Kinakailangan sa Seguridad:**

> **MANDATORY**: Ang mga MCP server **HINDI DAPAT** tumanggap ng anumang token na hindi tahasang inilabas para sa MCP server

#### Mga Kontrol sa Authentication at Authorization

- **Masusing Pagsusuri ng Authorization**: Magsagawa ng komprehensibong audit ng authorization logic ng MCP server upang matiyak na tanging mga inaasahang user at client lamang ang makaka-access sa sensitibong resources
  - **Gabay sa Implementasyon**: [Azure API Management bilang Authentication Gateway para sa MCP Servers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrasyon ng Identity**: [Paggamit ng Microsoft Entra ID para sa MCP Server Authentication](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Secure Token Management**: Ipatupad ang [mga best practice sa token validation at lifecycle ng Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - I-validate na tumutugma ang token audience claims sa pagkakakilanlan ng MCP server
  - Ipatupad ang tamang token rotation at expiration policies
  - Pigilan ang token replay attacks at hindi awtorisadong paggamit

- **Protektadong Imbakan ng Token**: Siguraduhing naka-encrypt ang token storage kapwa sa rest at in transit
  - **Pinakamahusay na Kasanayan**: [Secure Token Storage and Encryption Guidelines](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementasyon ng Access Control

- **Prinsipyo ng Least Privilege**: Bigyan ang MCP servers ng pinakamababang pahintulot na kinakailangan para sa inaasahang functionality
  - Regular na pagsusuri at pag-update ng mga permiso upang maiwasan ang privilege creep
  - **Dokumentasyon ng Microsoft**: [Secure Least-Privileged Access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Role-Based Access Control (RBAC)**: Magpatupad ng masusing role assignments
  - Limitahan ang mga role sa partikular na mga resource at aksyon
  - Iwasan ang malawak o hindi kinakailangang mga permiso na nagpapalawak ng attack surface

- **Patuloy na Pagmamanman ng Permiso**: Magpatupad ng tuloy-tuloy na pag-audit at pagmamanman ng access
  - Subaybayan ang mga pattern ng paggamit ng permiso para sa mga anomalya
  - Agarang ayusin ang labis o hindi nagagamit na mga pribilehiyo

## Mga Banta sa Seguridad na Partikular sa AI

### Prompt Injection at Mga Atake sa Manipulasyon ng Tool

Ang mga modernong implementasyon ng MCP ay humaharap sa mga sopistikadong AI-specific attack vector na hindi ganap na natutugunan ng tradisyunal na mga hakbang sa seguridad:

#### **Indirect Prompt Injection (Cross-Domain Prompt Injection)**

Ang **Indirect Prompt Injection** ay isa sa mga pinaka-kritikal na kahinaan sa mga MCP-enabled AI system. Ang mga attacker ay naglalagay ng malisyosong mga utos sa loob ng panlabas na nilalaman—mga dokumento, web page, email, o mga pinagmumulan ng data—na pagkatapos ay pinoproseso ng AI system bilang mga lehitimong utos.

**Mga Senaryo ng Atake:**
- **Injection sa Dokumento**: Mga malisyosong utos na nakatago sa mga pinoprosesong dokumento na nagdudulot ng hindi inaasahang aksyon ng AI
- **Eksploytasyon ng Web Content**: Mga kompromisadong web page na naglalaman ng mga naka-embed na prompt na nakokontrol ang kilos ng AI kapag na-scrape
- **Atake sa Email**: Mga malisyosong prompt sa mga email na nagdudulot sa AI assistant na mag-leak ng impormasyon o gumawa ng hindi awtorisadong aksyon
- **Kontaminasyon ng Pinagmumulan ng Data**: Mga kompromisadong database o API na naghahatid ng kontaminadong nilalaman sa AI system

**Epekto sa Totoong Mundo**: Ang mga atakeng ito ay maaaring magresulta sa pag-exfiltrate ng data, paglabag sa privacy, paglikha ng mapanganib na nilalaman, at manipulasyon ng interaksyon ng user. Para sa detalyadong pagsusuri, tingnan ang [Prompt Injection sa MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/tl/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Tool Poisoning Attacks**

Ang **Tool Poisoning** ay tumatarget sa metadata na naglalarawan sa mga MCP tool, sinasamantala kung paano ini-interpret ng mga LLM ang mga paglalarawan at parameter ng tool upang gumawa ng mga desisyon sa pagpapatupad.

**Mga Mekanismo ng Atake:**
- **Manipulasyon ng Metadata**: Ang mga attacker ay naglalagay ng malisyosong mga utos sa mga paglalarawan ng tool, mga depinisyon ng parameter, o mga halimbawa ng paggamit
- **Hindi Nakikitang Mga Utos**: Mga nakatagong prompt sa tool metadata na pinoproseso ng mga AI model ngunit hindi nakikita ng mga tao
- **Dynamic Tool Modification ("Rug Pulls")**: Ang mga tool na inaprubahan ng user ay binabago pagkatapos upang gumawa ng malisyosong aksyon nang hindi nalalaman ng user
- **Parameter Injection**: Malisyosong nilalaman na naka-embed sa mga schema ng parameter ng tool na nakakaapekto sa kilos ng modelo

**Panganib sa Hosted Server**: Ang mga remote MCP server ay may mas mataas na panganib dahil maaaring i-update ang mga depinisyon ng tool pagkatapos ng paunang pag-apruba ng user, na lumilikha ng mga senaryo kung saan ang dating ligtas na mga tool ay nagiging malisyoso. Para sa komprehensibong pagsusuri, tingnan ang [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/tl/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Karagdagang AI Attack Vectors**

- **Cross-Domain Prompt Injection (XPIA)**: Mga sopistikadong atake na gumagamit ng nilalaman mula sa maraming domain upang lampasan ang mga security control
- **Dynamic Capability Modification**: Mga real-time na pagbabago sa mga kakayahan ng tool na nakakalusot sa paunang pagsusuri sa seguridad
- **Context Window Poisoning**: Mga atake na nagmamaniobra sa malalaking context window upang itago ang malisyosong mga utos
- **Model Confusion Attacks**: Pagsasamantala sa mga limitasyon ng modelo upang lumikha ng hindi inaasahan o hindi ligtas na mga kilos

### Epekto ng Panganib sa Seguridad ng AI

**Mataas na Epekto ng mga Resulta:**
- **Pag-exfiltrate ng Data**: Hindi awtorisadong pag-access at pagnanakaw ng sensitibong data ng enterprise o personal
- **Paglabag sa Privacy**: Paglantad ng personal na impormasyon (PII) at kumpidensyal na data ng negosyo  
- **Manipulasyon ng Sistema**: Hindi inaasahang pagbabago sa mga kritikal na sistema at workflow
- **Pagnanakaw ng Credential**: Pagkumpromiso ng mga authentication token at service credential
- **Lateral Movement**: Paggamit ng kompromisadong AI system bilang pivot para sa mas malawak na pag-atake sa network

### Mga Solusyon sa Seguridad ng AI ng Microsoft

#### **AI Prompt Shields: Advanced na Proteksyon Laban sa Injection Attacks**

Nagbibigay ang Microsoft **AI Prompt Shields** ng komprehensibong depensa laban sa parehong direktang at indirect prompt injection attacks sa pamamagitan ng maraming layer ng seguridad:

##### **Pangunahing Mekanismo ng Proteksyon:**

1. **Advanced Detection at Filtering**
   - Mga algorithm ng machine learning at NLP techniques na nakakakita ng malisyosong utos sa panlabas na nilalaman
   - Real-time na pagsusuri ng mga dokumento, web page, email, at mga pinagmumulan ng data para sa mga naka-embed na banta
   - Kontekstwal na pag-unawa sa pagitan ng lehitimo at malisyosong mga pattern ng prompt

2. **Spotlighting Techniques**  
   - Nakikilala ang pinagkakatiwalaang mga utos ng sistema mula sa posibleng kompromisadong panlabas na input
   - Mga paraan ng pag-transform ng teksto na nagpapahusay sa kaugnayan ng modelo habang inihihiwalay ang malisyosong nilalaman
   - Tinutulungan ang mga AI system na mapanatili ang tamang hierarchy ng utos at balewalain ang mga iniksiyong command

3. **Delimiter at Datamarking Systems**
   - Malinaw na pagtukoy ng hangganan sa pagitan ng pinagkakatiwalaang mga mensahe ng sistema at panlabas na input na teksto
   - Mga espesyal na marker na nagha-highlight ng mga hangganan sa pagitan ng pinagkakatiwalaan at hindi pinagkakatiwalaang mga pinagmumulan ng data
   - Malinaw na paghihiwalay na pumipigil sa kalituhan ng utos at hindi awtorisadong pagpapatupad ng command

4. **Tuloy-tuloy na Threat Intelligence**
   - Patuloy na pagmamanman ng Microsoft sa mga bagong pattern ng atake at pag-update ng mga depensa
   - Proaktibong paghahanap ng banta para sa mga bagong injection technique at attack vector
   - Regular na pag-update ng security model upang mapanatili ang bisa laban sa mga umuusbong na banta

5. **Integrasyon ng Azure Content Safety**
   - Bahagi ng komprehensibong Azure AI Content Safety suite
   - Karagdagang pagtuklas para sa jailbreak attempts, mapanganib na nilalaman, at paglabag sa security policy
   - Pinag-isang mga kontrol sa seguridad sa buong bahagi ng AI application

**Mga Mapagkukunan sa Implementasyon**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/tl/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Mga Advanced na Banta sa Seguridad ng MCP

### Mga Kahinaan sa Session Hijacking

Ang **session hijacking** ay isang kritikal na vector ng atake sa mga stateful na implementasyon ng MCP kung saan ang mga hindi awtorisadong partido ay nakakakuha at inaabuso ang mga lehitimong session identifier upang magpanggap bilang mga client at magsagawa ng hindi awtorisadong mga aksyon.

#### **Mga Senaryo ng Atake at Panganib**

- **Session Hijack Prompt Injection**: Ang mga attacker na may ninakaw na session ID ay nag-iinject ng malisyosong mga event sa mga server na nagbabahagi ng session state, na posibleng mag-trigger ng mapanganib na aksyon o makakuha ng sensitibong data
- **Direktang Pagpapanggap**: Ang mga ninakaw na session ID ay nagpapahintulot ng direktang pagtawag sa MCP server na nilalampasan ang authentication, na itinuturing ang mga attacker bilang lehitimong user
- **Kompromisadong Resumable Streams**: Maaaring putulin ng mga attacker ang mga request nang maaga, na nagdudulot sa mga lehitimong client na mag-resume gamit ang posibleng malisyosong nilalaman

#### **Mga Kontrol sa Seguridad para sa Pamamahala ng Session**

**Kritikal na Mga Kinakailangan:**
- **Pagpapatunay ng Awtorisasyon**: Ang mga MCP server na nagpapatupad ng awtorisasyon **DAPAT** suriin ang LAHAT ng papasok na kahilingan at **HINDI DAPAT** umasa sa mga session para sa pagpapatunay ng pagkakakilanlan
- **Ligtas na Paggawa ng Session**: Gumamit ng cryptographically secure, non-deterministic na mga session ID na ginawa gamit ang secure random number generators
- **Pagtali sa Partikular na User**: Itali ang mga session ID sa impormasyon ng partikular na user gamit ang mga format tulad ng `<user_id>:<session_id>` upang maiwasan ang pang-aabuso ng session sa pagitan ng mga user
- **Pamamahala ng Lifecycle ng Session**: Magpatupad ng wastong expiration, rotation, at invalidation upang limitahan ang mga bintana ng kahinaan
- **Seguridad sa Transportasyon**: Sapilitang HTTPS para sa lahat ng komunikasyon upang maiwasan ang interception ng session ID

### Problema ng Confused Deputy

Ang **problema ng confused deputy** ay nangyayari kapag ang mga MCP server ay kumikilos bilang mga authentication proxy sa pagitan ng mga kliyente at mga third-party na serbisyo, na lumilikha ng mga pagkakataon para sa pag-bypass ng awtorisasyon sa pamamagitan ng pagsasamantala sa static client ID.

#### **Mekanismo ng Atake at mga Panganib**

- **Bypass ng Consent gamit ang Cookie**: Ang naunang pagpapatunay ng user ay lumilikha ng mga consent cookie na sinasamantala ng mga umaatake sa pamamagitan ng mga malisyosong kahilingan ng awtorisasyon na may crafted redirect URI
- **Pagnanakaw ng Authorization Code**: Ang umiiral na mga consent cookie ay maaaring magdulot sa mga authorization server na laktawan ang mga consent screen, na nagreredirect ng mga code sa mga endpoint na kontrolado ng umaatake  
- **Hindi Awtorisadong Access sa API**: Ang mga nakaw na authorization code ay nagpapahintulot ng token exchange at pagpapanggap ng user nang walang tahasang pahintulot

#### **Mga Estratehiya sa Pag-iwas**

**Mga Sapilitang Kontrol:**
- **Mga Eksplisit na Kinakailangan ng Consent**: Ang mga MCP proxy server na gumagamit ng static client ID **DAPAT** kumuha ng pahintulot ng user para sa bawat dynamically registered client
- **Pagpapatupad ng Seguridad ng OAuth 2.1**: Sundin ang kasalukuyang pinakamahusay na kasanayan sa seguridad ng OAuth kabilang ang PKCE (Proof Key for Code Exchange) para sa lahat ng kahilingan ng awtorisasyon
- **Mahigpit na Pagpapatunay ng Kliyente**: Magpatupad ng mahigpit na pagpapatunay ng redirect URI at mga identifier ng kliyente upang maiwasan ang pagsasamantala

### Mga Kahinaan sa Token Passthrough  

Ang **token passthrough** ay kumakatawan sa isang tahasang anti-pattern kung saan tinatanggap ng mga MCP server ang mga token ng kliyente nang walang wastong pagpapatunay at ipinapasa ang mga ito sa downstream na mga API, na lumalabag sa mga espesipikasyon ng awtorisasyon ng MCP.

#### **Mga Implikasyon sa Seguridad**

- **Pag-iwas sa Kontrol**: Ang direktang paggamit ng token mula kliyente papuntang API ay nilalaktawan ang mahahalagang rate limiting, pagpapatunay, at mga kontrol sa pagmamanman
- **Pagkasira ng Audit Trail**: Ang mga token na inilabas sa upstream ay nagpapahirap sa pagtukoy ng kliyente, na sumisira sa kakayahan sa pagsisiyasat ng insidente
- **Proxy-based na Pag-exfiltrate ng Data**: Ang mga hindi napapatunayang token ay nagpapahintulot sa mga malisyosong aktor na gamitin ang mga server bilang proxy para sa hindi awtorisadong pag-access ng data
- **Paglabag sa Trust Boundary**: Ang mga downstream na serbisyo ay maaaring malabag ang mga palagay sa tiwala kapag hindi mapatunayan ang pinagmulan ng token
- **Paglawak ng Atake sa Maramihang Serbisyo**: Ang mga kompromisadong token na tinatanggap sa maraming serbisyo ay nagpapahintulot ng lateral movement

#### **Kinakailangang Mga Kontrol sa Seguridad**

**Hindi Mapag-uusapang Mga Kinakailangan:**
- **Pagpapatunay ng Token**: Ang mga MCP server **HINDI DAPAT** tumanggap ng mga token na hindi tahasang inilabas para sa MCP server
- **Pagpapatunay ng Audience**: Laging suriin na ang mga audience claim ng token ay tumutugma sa pagkakakilanlan ng MCP server
- **Wastong Lifecycle ng Token**: Magpatupad ng mga panandaliang access token na may ligtas na mga kasanayan sa rotation


## Seguridad ng Supply Chain para sa mga AI System

Ang seguridad ng supply chain ay umunlad lampas sa tradisyunal na mga dependency ng software upang saklawin ang buong AI ecosystem. Ang mga modernong implementasyon ng MCP ay dapat mahigpit na suriin at subaybayan ang lahat ng mga bahagi na may kaugnayan sa AI, dahil bawat isa ay nagdadala ng mga potensyal na kahinaan na maaaring makompromiso ang integridad ng sistema.

### Pinalawak na Mga Bahagi ng AI Supply Chain

**Tradisyunal na Mga Dependency ng Software:**
- Mga open-source na library at framework
- Mga container image at base system  
- Mga tool sa pag-develop at build pipeline
- Mga bahagi ng imprastraktura at serbisyo

**Mga Elemento ng AI-Specific Supply Chain:**
- **Foundation Models**: Mga pre-trained na modelo mula sa iba't ibang provider na nangangailangan ng pagpapatunay ng pinagmulan
- **Embedding Services**: Mga panlabas na serbisyo para sa vectorization at semantic search
- **Context Providers**: Mga pinagkukunan ng data, knowledge base, at mga repositoryo ng dokumento  
- **Third-party APIs**: Mga panlabas na AI service, ML pipeline, at mga endpoint ng pagproseso ng data
- **Model Artifacts**: Mga timbang, configuration, at mga fine-tuned na variant ng modelo
- **Training Data Sources**: Mga dataset na ginamit para sa pagsasanay at fine-tuning ng modelo

### Komprehensibong Estratehiya sa Seguridad ng Supply Chain

#### **Pagpapatunay ng Bahagi at Tiwala**
- **Pagpapatunay ng Pinagmulan**: Suriin ang pinagmulan, lisensya, at integridad ng lahat ng bahagi ng AI bago ang integrasyon
- **Pagsusuri sa Seguridad**: Magsagawa ng vulnerability scan at security review para sa mga modelo, pinagkukunan ng data, at AI service
- **Pagsusuri ng Reputasyon**: Suriin ang track record sa seguridad at mga kasanayan ng mga AI service provider
- **Pagpapatunay ng Pagsunod**: Tiyakin na ang lahat ng bahagi ay sumusunod sa mga pangangailangan sa seguridad at regulasyon ng organisasyon

#### **Ligtas na Deployment Pipelines**  
- **Automated CI/CD Security**: Isama ang security scanning sa buong automated deployment pipeline
- **Integridad ng Artifact**: Magpatupad ng cryptographic verification para sa lahat ng deployed artifact (code, modelo, configuration)
- **Staged Deployment**: Gumamit ng progressive deployment strategies na may security validation sa bawat yugto
- **Trusted Artifact Repositories**: Mag-deploy lamang mula sa mga verified at secure na artifact registry at repository

#### **Patuloy na Pagsubaybay at Pagtugon**
- **Dependency Scanning**: Patuloy na pagmamanman ng mga kahinaan para sa lahat ng software at AI component dependencies
- **Model Monitoring**: Patuloy na pagsusuri ng pag-uugali ng modelo, performance drift, at mga security anomaly
- **Pagsubaybay sa Kalusugan ng Serbisyo**: Subaybayan ang mga panlabas na AI service para sa availability, security incidents, at mga pagbabago sa polisiya
- **Pagsasama ng Threat Intelligence**: Isama ang mga threat feed na partikular sa AI at ML security risks

#### **Kontrol sa Access at Pinakamababang Pribilehiyo**
- **Mga Pahintulot sa Antas ng Bahagi**: Limitahan ang access sa mga modelo, data, at serbisyo batay sa pangangailangan ng negosyo
- **Pamamahala ng Service Account**: Magpatupad ng dedikadong service account na may pinakamababang kinakailangang pahintulot
- **Segmentation ng Network**: Ihiwalay ang mga bahagi ng AI at limitahan ang network access sa pagitan ng mga serbisyo
- **Kontrol sa API Gateway**: Gumamit ng sentralisadong API gateway upang kontrolin at subaybayan ang access sa mga panlabas na AI service

#### **Pagtugon sa Insidente at Pagbawi**
- **Mabilis na Proseso ng Pagtugon**: Itinatag na mga proseso para sa pag-patch o pagpapalit ng mga kompromisadong bahagi ng AI
- **Pag-ikot ng Credential**: Automated na sistema para sa pag-ikot ng mga lihim, API key, at mga kredensyal ng serbisyo
- **Kakayahan sa Rollback**: Kakayahang mabilis na bumalik sa mga naunang kilalang mabuting bersyon ng mga bahagi ng AI
- **Pagbawi mula sa Supply Chain Breach**: Mga partikular na proseso para sa pagtugon sa kompromiso ng upstream AI service

### Mga Microsoft Security Tool at Integrasyon

**GitHub Advanced Security** ay nagbibigay ng komprehensibong proteksyon sa supply chain kabilang ang:
- **Secret Scanning**: Automated na pagtuklas ng mga kredensyal, API key, at token sa mga repositoryo
- **Dependency Scanning**: Pagsusuri ng kahinaan para sa mga open-source dependency at library
- **CodeQL Analysis**: Static code analysis para sa mga security vulnerability at isyu sa coding
- **Supply Chain Insights**: Visibility sa kalusugan at status ng seguridad ng mga dependency

**Integrasyon ng Azure DevOps at Azure Repos:**
- Seamless na integrasyon ng security scanning sa mga Microsoft development platform
- Automated na security check sa Azure Pipelines para sa mga AI workload
- Pagpapatupad ng polisiya para sa ligtas na deployment ng AI component

**Mga Panloob na Kasanayan ng Microsoft:**
Malawak ang implementasyon ng Microsoft ng mga kasanayan sa seguridad ng supply chain sa lahat ng produkto. Alamin ang mga napatunayang pamamaraan sa [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Pinakamahusay na Kasanayan sa Foundation Security

Ang mga implementasyon ng MCP ay namamana at bumubuo sa umiiral na security posture ng iyong organisasyon. Ang pagpapalakas ng mga pundamental na kasanayan sa seguridad ay malaki ang naitutulong sa pangkalahatang seguridad ng mga AI system at MCP deployment.

### Pangunahing Mga Pundasyon ng Seguridad

#### **Ligtas na Mga Kasanayan sa Pag-develop**
- **Pagsunod sa OWASP**: Protektahan laban sa [OWASP Top 10](https://owasp.org/www-project-top-ten/) na mga kahinaan sa web application
- **Proteksyon na AI-Specific**: Magpatupad ng mga kontrol para sa [OWASP Top 10 para sa LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Ligtas na Pamamahala ng Lihim**: Gumamit ng dedikadong vault para sa mga token, API key, at sensitibong configuration data
- **End-to-End Encryption**: Magpatupad ng ligtas na komunikasyon sa lahat ng bahagi ng aplikasyon at daloy ng data
- **Pagpapatunay ng Input**: Mahigpit na pagpapatunay ng lahat ng input ng user, parameter ng API, at pinagkukunan ng data

#### **Pagpapalakas ng Imprastraktura**
- **Multi-Factor Authentication**: Sapilitang MFA para sa lahat ng administrative at service account
- **Pamamahala ng Patch**: Automated at napapanahong pag-patch para sa mga operating system, framework, at dependency  
- **Integrasyon ng Identity Provider**: Sentralisadong pamamahala ng pagkakakilanlan sa pamamagitan ng enterprise identity provider (Microsoft Entra ID, Active Directory)
- **Segmentation ng Network**: Lohikal na paghihiwalay ng mga bahagi ng MCP upang limitahan ang potensyal na lateral movement
- **Prinsipyo ng Pinakamababang Pribilehiyo**: Pinakamababang kinakailangang pahintulot para sa lahat ng bahagi ng sistema at account

#### **Pagsubaybay at Pag-detect ng Seguridad**
- **Komprehensibong Logging**: Detalyadong pag-log ng mga aktibidad ng AI application, kabilang ang mga interaksyon ng MCP client-server
- **Integrasyon ng SIEM**: Sentralisadong security information at event management para sa pagtuklas ng anomaly
- **Behavioral Analytics**: AI-powered na pagmamanman upang matukoy ang mga hindi pangkaraniwang pattern sa sistema at pag-uugali ng user
- **Threat Intelligence**: Pagsasama ng mga panlabas na threat feed at indicator of compromise (IOC)
- **Pagtugon sa Insidente**: Mahusay na tinukoy na mga proseso para sa pagtuklas, pagtugon, at pagbawi sa mga security incident

#### **Zero Trust Architecture**
- **Huwag Magsalig, Laging Patunayan**: Patuloy na pagpapatunay ng mga user, device, at koneksyon sa network
- **Micro-Segmentation**: Granular na kontrol sa network na naghihiwalay ng mga indibidwal na workload at serbisyo
- **Identity-Centric Security**: Mga polisiya sa seguridad na nakabase sa napatunayang pagkakakilanlan sa halip na lokasyon ng network
- **Patuloy na Pagsusuri ng Panganib**: Dinamikong pagsusuri ng security posture batay sa kasalukuyang konteksto at pag-uugali
- **Conditional Access**: Mga kontrol sa access na umaangkop batay sa mga risk factor, lokasyon, at tiwala sa device

### Mga Pattern ng Integrasyon sa Enterprise

#### **Integrasyon ng Microsoft Security Ecosystem**
- **Microsoft Defender for Cloud**: Komprehensibong pamamahala ng security posture sa cloud
- **Azure Sentinel**: Cloud-native SIEM at SOAR na kakayahan para sa proteksyon ng AI workload
- **Microsoft Entra ID**: Enterprise identity at access management na may conditional access policy
- **Azure Key Vault**: Sentralisadong pamamahala ng lihim na may hardware security module (HSM) backing
- **Microsoft Purview**: Pamamahala ng data at pagsunod para sa mga pinagkukunan ng data at workflow ng AI

#### **Pagsunod at Pamamahala**
- **Pagsunod sa Regulasyon**: Tiyakin na ang mga implementasyon ng MCP ay sumusunod sa mga pang-industriyang kinakailangan sa pagsunod (GDPR, HIPAA, SOC 2)
- **Klasipikasyon ng Data**: Wastong pag-uuri at paghawak ng sensitibong data na pinoproseso ng mga AI system
- **Audit Trails**: Komprehensibong pag-log para sa pagsunod sa regulasyon at forensic na pagsisiyasat
- **Kontrol sa Privacy**: Pagpapatupad ng privacy-by-design na mga prinsipyo sa arkitektura ng AI system
- **Pamamahala ng Pagbabago**: Pormal na mga proseso para sa security review ng mga pagbabago sa AI system

Ang mga pundamental na kasanayang ito ay lumilikha ng matibay na baseline ng seguridad na nagpapahusay sa bisa ng mga MCP-specific na kontrol sa seguridad at nagbibigay ng komprehensibong proteksyon para sa mga AI-driven na aplikasyon.

## Mga Pangunahing Punto sa Seguridad

- **Layered Security Approach**: Pagsamahin ang mga pundamental na kasanayan sa seguridad (ligtas na coding, pinakamababang pribilehiyo, pagpapatunay ng supply chain, patuloy na pagmamanman) kasama ang mga AI-specific na kontrol para sa komprehensibong proteksyon

- **AI-Specific Threat Landscape**: Ang mga sistema ng MCP ay humaharap sa mga natatanging panganib kabilang ang prompt injection, tool poisoning, session hijacking, problema ng confused deputy, mga kahinaan sa token passthrough, at labis na pahintulot na nangangailangan ng espesyal na mga mitigasyon

- **Kahusayan sa Authentication at Authorization**: Magpatupad ng matibay na authentication gamit ang mga panlabas na identity provider (Microsoft Entra ID), ipatupad ang wastong pagpapatunay ng token, at huwag kailanman tumanggap ng mga token na hindi tahasang inilabas para sa iyong MCP server

- **Pag-iwas sa AI Attack**: Mag-deploy ng Microsoft Prompt Shields at Azure Content Safety upang ipagtanggol laban sa indirect prompt injection at tool poisoning attacks, habang sinusuri ang tool metadata at minomonitor ang mga dynamic na pagbabago

- **Seguridad ng Session at Transport**: Gumamit ng cryptographically secure, non-deterministic na mga session ID na nakatali sa pagkakakilanlan ng user, magpatupad ng wastong pamamahala ng lifecycle ng session, at huwag kailanman gamitin ang mga session para sa authentication

- **Pinakamahusay na Kasanayan sa OAuth Security**: Pigilan ang mga confused deputy attack sa pamamagitan ng eksplisitong pahintulot ng user para sa dynamically registered clients, wastong pagpapatupad ng OAuth 2.1 gamit ang PKCE, at mahigpit na pagpapatunay ng redirect URI  

- **Mga Prinsipyo sa Seguridad ng Token**: Iwasan ang mga anti-pattern ng token passthrough, patunayan ang mga audience claim ng token, magpatupad ng panandaliang token na may ligtas na rotation, at panatilihin ang malinaw na trust boundary

- **Komprehensibong Seguridad ng Supply Chain**: Tratuhin ang lahat ng bahagi ng AI ecosystem (mga modelo, embedding, context provider, panlabas na API) na may parehong higpit sa seguridad tulad ng tradisyunal na mga dependency ng software

- **Patuloy na Ebolusyon**: Manatiling napapanahon sa mabilis na pag-unlad ng mga espesipikasyon ng MCP, mag-ambag sa mga pamantayan ng security community, at panatilihin ang adaptive na security posture habang umuunlad ang protocol

- **Integrasyon ng Microsoft Security**: Gamitin ang komprehensibong security ecosystem ng Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) para sa pinahusay na proteksyon sa deployment ng MCP

## Komprehensibong Mga Mapagkukunan

### **Opisyal na Dokumentasyon ng Seguridad ng MCP**
- [MCP Specification (Current: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **Mga Pamantayan at Pinakamahusay na Kasanayan sa Seguridad**
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
- [Azure API Management bilang MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication gamit ang MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Seguridad sa DevOps at Supply Chain**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Karagdagang Dokumentasyon sa Seguridad**

Para sa komprehensibong gabay sa seguridad, sumangguni sa mga espesyal na dokumentong ito sa seksyong ito:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Kumpletong mga pinakamahusay na kasanayan sa seguridad para sa mga implementasyon ng MCP
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Mga praktikal na halimbawa ng implementasyon para sa integrasyon ng Azure Content Safety  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Pinakabagong mga kontrol at teknik sa seguridad para sa mga deployment ng MCP
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Mabilisang gabay sa mga mahahalagang kasanayan sa seguridad ng MCP

---

## Ano ang Susunod

Susunod: [Kabanata 3: Pagsisimula](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Mga Advanced na Paksa sa MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/tl/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(I-click ang larawan sa itaas upang panoorin ang video ng leksyong ito)_

Saklaw ng kabanatang ito ang isang serye ng mga advanced na paksa sa implementasyon ng Model Context Protocol (MCP), kabilang ang multi-modal integration, scalability, mga pinakamahusay na kasanayan sa seguridad, at enterprise integration. Mahalaga ang mga paksang ito para sa pagbuo ng matibay at handang gamitin sa produksyon na mga aplikasyon ng MCP na maaaring matugunan ang mga pangangailangan ng modernong mga sistema ng AI.

## Pangkalahatang-ideya

Tinutuklas ng leksyong ito ang mga advanced na konsepto sa implementasyon ng Model Context Protocol, na nakatuon sa multi-modal integration, scalability, mga pinakamahusay na kasanayan sa seguridad, at enterprise integration. Mahalaga ang mga paksang ito para sa pagbuo ng mga aplikasyon ng MCP na pang-produksyon na kayang humarap sa masalimuot na mga pangangailangan sa mga kapaligiran ng enterprise.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng leksyong ito, magagawa mong:

- Mag-implementa ng mga multi-modal na kakayahan sa loob ng mga framework ng MCP
- Magdisenyo ng scalable na mga arkitektura ng MCP para sa mga senaryong may mataas na pangangailangan
- Magpatupad ng mga pinakamahusay na kasanayan sa seguridad na nakaayon sa mga prinsipyo ng seguridad ng MCP
- Isama ang MCP sa mga enterprise AI system at framework
- I-optimize ang pagganap at pagiging maaasahan sa mga kapaligirang pang-produksyon

## Mga Leksiyon at Halimbawang Proyekto

| Link | Pamagat | Paglalarawan |
|------|--------|--------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integrate with Azure | Matutunan kung paano isama ang iyong MCP Server sa Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multi modal samples | Mga halimbawa para sa audio, larawan, at multi modal na tugon |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimal na Spring Boot app na nagpapakita ng OAuth2 gamit ang MCP, bilang Authorization at Resource Server. Ipinapakita ang secure na pag-isyu ng token, mga protektadong endpoints, deployment sa Azure Container Apps, at integrasyon ng API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root contexts | Matutunan pa ang tungkol sa root context at kung paano ito i-implementa |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Matutunan ang iba't ibang uri ng routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Matutunan kung paano magtrabaho gamit ang sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Scaling | Matutunan tungkol sa scaling |
| [5.8 Security](./mcp-security/README.md) | Security | Pangalagaan ang iyong MCP Server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP server at client na isinama sa SerpAPI para sa real-time web, balita, paghahanap ng produkto, at Q&A. Ipinapakita ang multi-tool orchestration, integrasyon ng external API, at masusing paghawak ng error. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Mahalaga na ngayon ang real-time data streaming sa mundo ng datos, kung saan ang mga negosyo at aplikasyon ay nangangailangan ng agarang access sa impormasyon para makagawa ng napapanahong mga desisyon. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Real-time na paghahanap sa web at kung paano binabago ng MCP ang real-time web search sa pamamagitan ng pagbibigay ng standardized na paraan ng pamamahala ng konteksto sa AI models, search engines, at mga aplikasyon. | 
| [5.12 Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authentication | Nagbibigay ang Microsoft Entra ID ng matatag na cloud-based identity at access management solution, na tumutulong tiyakin na tanging awtorisadong mga gumagamit at aplikasyon lamang ang maaaring makipag-ugnayan sa iyong MCP server. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integration | Matutunan kung paano isama ang Model Context Protocol servers sa Azure AI Foundry agents, na nagbibigay-daan sa makapangyarihang tool orchestration at enterprise AI capabilities gamit ang standardized na koneksyon sa mga external data source. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | Ang mga oportunidad sa hinaharap ng mga teknik sa context engineering para sa mga MCP server, kabilang ang context optimization, dynamic context management, at mga estratehiya para sa epektibong prompt engineering sa loob ng mga framework ng MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Custom Transport | Matutunan kung paano mag-implementa ng mga custom transport mechanism para sa mga espesyal na sitwasyon ng komunikasyon sa MCP. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protocol Features | Maging bihasa sa mga advanced na katangian ng protocol kabilang ang mga notification sa progreso, pagkansela ng request, mga template ng resource, at mga pattern ng paghawak ng error. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarial Agents | Gumamit ng dalawang agent na may magkasalungat na posisyon, na nagbabahagi ng isang set ng MCP tool, upang mahuli ang mga hallucination, maiulat ang mga edge case, at makagawa ng mas maayos na output sa pamamagitan ng estrukturadong debate. |

> **Bago sa MCP Specification 2025-11-25**: Kasama na ngayon sa specification ang experimental na suporta para sa **Tasks** (mga operasyon na tumatagal at may pagsubaybay sa progreso), **Tool Annotations** (metadata tungkol sa kilos ng tool para sa kaligtasan), **URL Mode Elicitation** (hilingin ang partikular na nilalaman ng URL mula sa mga kliyente), at pinahusay na **Roots** (para sa pamamahala ng konteksto sa workspace). Tingnan ang [MCP Specification changelog](https://spec.modelcontextprotocol.io/) para sa buong detalye.

## Karagdagang Sanggunian

Para sa pinakabagong impormasyon tungkol sa mga advanced na paksa sa MCP, sumangguni sa:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Mga panganib sa seguridad at mga mitigasyon
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktikal na pagsasanay sa seguridad

## Pangunahing Mga Punto

- Ang mga multi-modal na implementasyon ng MCP ay nagpapalawak ng kakayahan ng AI lampas sa pagproseso ng teksto
- Mahalaga ang scalability para sa mga enterprise deployment at maaaring tugunan sa pamamagitan ng horizontal at vertical scaling
- Pinoprotektahan ng komprehensibong mga hakbang sa seguridad ang datos at sinisiguro ang wastong kontrol sa access
- Pinapahusay ng integrasyon sa enterprise sa mga plataporma tulad ng Azure OpenAI at Microsoft AI Foundry ang mga kakayahan ng MCP
- Nakikinabang ang mga advanced na implementasyon ng MCP mula sa optimized na mga arkitektura at maingat na pamamahala ng mga mapagkukunan

## Ehersisyo

Magdisenyo ng isang enterprise-grade na implementasyon ng MCP para sa isang partikular na kaso ng paggamit:

1. Tukuyin ang mga multi-modal na pangangailangan para sa iyong kaso ng paggamit
2. Ilahad ang mga kontrol sa seguridad na kailangan upang protektahan ang sensitibong datos
3. Disenyuhin ang scalable na arkitektura na kayang humawak ng nagbabagong load
4. Planuhin ang mga integration point sa mga enterprise AI system
5. Idokumento ang mga posibleng bottlenecks sa pagganap at mga estratehiya para sa mitigasyon

## Karagdagang Mga Mapagkukunan

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Ano ang susunod

Suriin ang mga leksyon sa module na ito simula sa: [5.1 MCP Integration](./mcp-integration/README.md)

Kapag natapos mo na ang module na ito, magpatuloy sa: [Module 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga automated na pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
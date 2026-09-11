# Advanced Topics for MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/pcm/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Clik di pikshua wey dey for top to watch dis lesson video)_

Dis chapter dey cover plenty advanced tins for how to take do Model Context Protocol (MCP), like multi-modal join, how e fit take big, security beta beta, and how business fit connect am. Dis tins na important for build strong and ready-to-use MCP waka wey fit run modern AI system dem well well.

## Overview

Dis lesson go talk about advanced mata dem for Model Context Protocol setup, e go focus on multi-modal join, how e fit take handle high demand, security beta beta, and how business fit connect am. Dis tins na important to build MCP wey go fit run for enterprise wahala dem wey get plenty requirement.

> **Current specification note:** MCP `2026-07-28` don stop to use di Roots and
> Sampling basic tins wey lesson 5.4 and 5.6 talk about. E don also move
> experimental Tasks feature wey dey for Protocol Features (5.16) go
> special Tasks extension. Dem still keep dat old tins for legacy
> `2025-11-25` way to use dem and dem put instruction on how to change. See
> [Wetin Don Change for MCP: The 2026-07-28 Specification](../01-CoreConcepts/mcp-2026-07-28.md).

## Wetin You Go Learn

By the end of dis lesson, you go fit:

- Run multi-modal abilities inside MCP framework dem
- Design MCP systems wey fit scale well for when demand high
- Use security beta beta wey follow MCP security style
- Join MCP with business AI systems and different frameworks
- Make sure performance and reliability dey beta for production

## Lessons and sample Projects

| Link | Title | Description |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Join with Azure | Learn how to join your MCP Server for Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multi modal samples  | Samples for audio, image and multi modal response |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Small Spring Boot app wey show OAuth2 with MCP, both as Authorization and Resource Server. E show how secure token dey issued, e protect endpoints, how e fit deploy to Azure Container Apps, plus API Management join. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root contexts  | Learn old `2025-11-25` Roots basic tin plus how to change am (dem dey stop am for `2026-07-28`) |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Learn different types of routing |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Learn old `2025-11-25` Sampling basic tin plus how to change am (dem dey stop am for `2026-07-28`) |
| [5.7 Scaling](./mcp-scaling/README.md) | Scaling  | Learn about scaling |
| [5.8 Security](./mcp-security/README.md) | Security  | Secure your MCP Server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP server and client wey join with SerpAPI for real-time web, news, product search, plus Q&A. E show multi-tool join together, external API join, plus strong error handling. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming  | Real-time data streaming don become important for today data wahala, where business and apps need quick info to take decision sharp sharp.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Real-time web search how MCP take change real-time web search by giving standard way to manage context for AI models, search engines, and apps.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authentication | Microsoft Entra ID na strong cloud-based identity plus access management solution, e dey help make sure say only correct users and apps fit use your MCP server.|
| [5.13 Microsoft Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Microsoft Foundry Integration | Learn how to join Model Context Protocol servers with Microsoft Foundry agents, e go allow strong tool cooperation and business AI powers with standard external data source connections.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | The future chance for context engineering methods for MCP servers, including optimizing context, dynamic context management, and smart prompt engineering for MCP framework dem.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Custom Transport | Learn how to build custom transport waya dem for special MCP communication cases.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protocol Features | Become master for advanced protocol features including progress notifications, how to cancel request, resource templates, and error management style.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarial Agents | Use two agents wey get opposing ideas, dem share one MCP tool set, to catch hallucination, bring wahala case, and produce better output through proper discussion.|

> **Historical `2025-11-25` note:** dis update bring experimental
> Tasks and make beta several protocol features. For `2026-07-28`, Tasks join go
> official extension and Roots stop. No use
> `2025-11-25` feature status as current instruction; check
> [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Extra References

For the latest info on advanced MCP topics, check:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Security risk and how to stop am
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on security training

## Main Takeaways

- Multi-modal MCP implementations dey extend AI power pass just text processing
- Scalability na important for business deployment and fit handle am through horizontal and vertical scaling
- Complete security steps go protect data and make sure say only correct people fit access am
- Business join with platform dem like Azure OpenAI and Microsoft AI Foundry dey improve MCP power
- Advanced MCP setups go beta if dem get optimized designs and good resource control

## Exercise

Design one strong MCP system for one special use case:

1. Identify multi-modal needs for your use case
2. Outline di security controls wey you need to protect sensitive data
3. Design one scalable system wey fit handle different load
4. Plan join points with business AI systems dem
5. Write down where performance fit slow and how to fix am

## More Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Wetin dey next

Explore the lessons for this module beginnin with: [5.1 MCP Integration](./mcp-integration/README.md)

After you don finish dis module, continue go: [Module 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
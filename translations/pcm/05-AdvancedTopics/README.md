# Advanced Topics for MCP

[![Advanced MCP: Secure, Scalable, and Multi-modal AI Agents](../../../translated_images/pcm/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Click di picture wey dey up top to watch video for dis lesson)_

Dis chapter dey cover series of advanced mata for Model Context Protocol (MCP) implementation, including multi-modal integration, scalability, security best practices, and how to join am with enterprise. Dis topics dey important to build strong and production-ready MCP applications wey fit meet wetin modern AI systems need.

## Overview

Dis lesson go show advanced ideas for Model Context Protocol implementation, dem go focus on multi-modal integration, scalability, security best practices, and how to join am with enterprise. Dis topics na key to build production-level MCP applications wey fit handle complex requirements for enterprise enviroment.

## Learning Objectives

By di end of dis lesson, you fit:

- Implement multi-modal capabilities for MCP frameworks
- Design scalable MCP architectures for big workload
- Apply security best practices wey agree with MCP security principles
- Connect MCP wit enterprise AI systems and frameworks
- Make performance and reliability beta for production environments

## Lessons and sample Projects

| Link | Title | Description |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Join wit Azure | Learn how to join your MCP Server ontop Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP Multi modal samples  | Samples for audio, picture and multi modal answer |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demo | Minimal Spring Boot app wey dey show OAuth2 wit MCP, both as Authorization and Resource Server. E dey show how dem dey secure token, protect endpoints, Azure Container Apps deploy, and API Management join. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Root contexts  | Learn more about root context and how to implement dem |
| [5.5 Routing](./mcp-routing/README.md) | Routing | Learn different kain routing wey dey |
| [5.6 Sampling](./mcp-sampling/README.md) | Sampling | Learn how to work wit sampling |
| [5.7 Scaling](./mcp-scaling/README.md) | Scaling  | Learn about how to scale |
| [5.8 Security](./mcp-security/README.md) | Security  | Secure your MCP Server |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web Search MCP | Python MCP server and client wey join wit SerpAPI for real-time web, news, product search, and Q&A. E show multi-tool arrangement, external API join, and strong error handling. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming  | Real-time data streaming don become important for today world wey data dey drive everywhere, where business and applications need quick info to make decision fast.|
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Web Search | Real-time web search, how MCP dey change real-time web search by giving one standard way to manage context for AI models, search engines, and applications.| 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID Authentication | Microsoft Entra ID dey provide strong cloud-based identity and access management, e dey help make sure only authorized users and apps fit interact with your MCP server.|
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integration | Learn how to join Model Context Protocol servers wit Azure AI Foundry agents, make strong tool arrangement and enterprise AI things wey get correct external data source connection.|
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Context Engineering | Future chance for context engineering ways for MCP servers, including how to optimize context, dynamic context management, and better prompt engineering strategies inside MCP frameworks.|
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Custom Transport | Learn how to do custom transport methods for special MCP communication situations.|
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Protocol Features | Master advanced protocol features like progress notifications, request cancellation, resource templates, and error handling patterns.|
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Adversarial Agents | Use two agents wey get opposite positions, sharing one MCP tool set, to catch hallucinations, show edge cases, and make better-calibrated outputs through structured debate.|

> **New for MCP Specification 2025-11-25**: Di specification don add experimental support for **Tasks** (long-running operations with progress tracking), **Tool Annotations** (metadata about how tool dey behave for safety), **URL Mode Elicitation** (to request specific URL content from clients), and better **Roots** (for workspace context management). See di [MCP Specification changelog](https://spec.modelcontextprotocol.io/) for full details.

## Additional References

For di most current information on advanced MCP topics, check:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [GitHub Repository](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - Security risks and how to stop am
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Hands-on security training

## Key Takeaways

- Multi-modal MCP implementations dey extend AI power pass just text processing
- Scalability na key for enterprise deployments and e fit happen through horizontal and vertical scaling
- Strong security measures dey protect data and make sure access correct
- Enterprise integration wit platforms like Azure OpenAI and Microsoft AI Foundry dey improve MCP power
- Advanced MCP dey benefit from beta architectures and careful resource management

## Exercise

Design one enterprise-grade MCP implementation for one specific use:

1. Find di multi-modal requirements wey your use case need
2. Write down the security controls wey you need to protect sensitive data
3. Design one scalable architecture wey fit handle different workloads
4. Plan how to join with enterprise AI systems
5. Write down where performance fit slow and how you go fix am

## Additional Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Documentation](https://learn.microsoft.com/en-us/ai-services/)

---

## Wetin dey next

Explore lessons for dis module starting with: [5.1 MCP Integration](./mcp-integration/README.md)

When you finish this module, continue to: [Module 6: Community Contributions](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we dey try make am correct, abeg sabi say automated translation fit get error or wrong. Di original document for im own language na di correct source. For important mata, better human professional translation dey recommended. We no go responsible for any wahala or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
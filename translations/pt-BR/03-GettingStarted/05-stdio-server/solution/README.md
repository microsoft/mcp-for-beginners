# Soluções de Servidor MCP stdio

> **⚠️ Importante**: Essas soluções foram atualizadas para usar o **transporte stdio**, conforme recomendado pela Especificação MCP 2025-06-18. O transporte original SSE (Server-Sent Events) foi descontinuado.

Aqui estão as soluções completas para construir servidores MCP usando o transporte stdio em cada runtime:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Implementação completa de servidor stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Servidor stdio em Python com asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Servidor stdio em .NET com injeção de dependência

Cada solução demonstra:
- Configuração do transporte stdio
- Definição de ferramentas do servidor
- Manipulação adequada de mensagens JSON-RPC
- Integração com clientes MCP, como o Claude

Todas as soluções seguem a especificação atual do MCP e utilizam o transporte stdio recomendado para desempenho e segurança ideais.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
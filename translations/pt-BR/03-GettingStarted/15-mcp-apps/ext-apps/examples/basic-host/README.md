# Example: Basic Host

Uma implementação de referência mostrando como construir um aplicativo host MCP que se conecta a servidores MCP e renderiza interfaces de ferramentas em uma sandbox segura.

Este host básico também pode ser usado para testar Apps MCP durante o desenvolvimento local.

## Key Files

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host UI React com seleção de ferramenta, entrada de parâmetros e gerenciamento de iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy iframe externo com validação de segurança e retransmissão de mensagens bidirecional
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Lógica principal: conexão com servidor, chamada de ferramenta e configuração do AppBridge

## Getting Started

```bash
npm install
npm run start
# Abra http://localhost:8080
```

Por padrão, o aplicativo host tentará se conectar a um servidor MCP em `http://localhost:3001/mcp`. Você pode configurar esse comportamento definindo a variável de ambiente `SERVERS` com um array JSON de URLs de servidores:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Este exemplo usa um padrão sandbox de duplo iframe para isolamento seguro da interface:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Por que dois iframes?**

- O iframe externo é executado em uma origem separada (porta 8081) evitando acesso direto ao host
- O iframe interno recebe HTML via `srcdoc` e é restringido pelos atributos sandbox
- As mensagens passam pelo iframe externo que as valida e encaminha bidirecionalmente

Esta arquitetura assegura que mesmo que o código da interface da ferramenta seja malicioso, ele não pode acessar o DOM, cookies ou contexto JavaScript do aplicativo host.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomendamos a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
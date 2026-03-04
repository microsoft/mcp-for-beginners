# Exemplo: Host Básico

Uma implementação de referência que mostra como construir uma aplicação host MCP que se liga a servidores MCP e apresenta interfaces de ferramentas num sandbox seguro.

Este host básico pode também ser usado para testar Apps MCP durante o desenvolvimento local.

## Ficheiros Principais

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host de UI React com seleção de ferramenta, introdução de parâmetros, e gestão de iframes
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy do iframe exterior com validação de segurança e retransmissão bidirecional de mensagens
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Lógica principal: ligação ao servidor, chamada de ferramentas, e configuração do AppBridge

## Início Rápido

```bash
npm install
npm run start
# Abrir http://localhost:8080
```

Por predefinição, a aplicação host irá tentar ligar-se a um servidor MCP em `http://localhost:3001/mcp`. Pode configurar este comportamento definindo a variável de ambiente `SERVERS` com um array JSON de URLs de servidores:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arquitetura

Este exemplo utiliza um padrão de sandbox com dois iframes para isolamento seguro da interface:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Porque dois iframes?**

- O iframe exterior corre numa origem separada (porto 8081), impedindo o acesso direto ao host
- O iframe interior recebe HTML via `srcdoc` e está restrito por atributos sandbox
- As mensagens passam pelo iframe exterior, que as valida e retransmite bidirecionalmente

Esta arquitetura assegura que, mesmo que o código da interface da ferramenta seja malicioso, este não pode aceder ao DOM da aplicação host, cookies, ou contexto JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
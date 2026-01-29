# Servidor MCP stdio - Solução em TypeScript

> **⚠️ Importante**: Esta solução foi atualizada para usar o **transporte stdio** conforme recomendado pela Especificação MCP 2025-06-18. O transporte original SSE foi descontinuado.

## Visão Geral

Esta solução em TypeScript demonstra como construir um servidor MCP usando o transporte stdio atual. O transporte stdio é mais simples, mais seguro e oferece melhor desempenho em comparação com a abordagem SSE descontinuada.

## Pré-requisitos

- Node.js 18+ ou mais recente
- Gerenciador de pacotes npm ou yarn

## Instruções de Configuração

### Etapa 1: Instale as dependências

```bash
npm install
```

### Etapa 2: Compile o projeto

```bash
npm run build
```

## Executando o Servidor

O servidor stdio funciona de forma diferente do antigo servidor SSE. Em vez de iniciar um servidor web, ele se comunica por meio de stdin/stdout:

```bash
npm start
```

**Importante**: O servidor parecerá estar travado - isso é normal! Ele está aguardando mensagens JSON-RPC via stdin.

## Testando o Servidor

### Método 1: Usando o MCP Inspector (Recomendado)

```bash
npm run inspector
```

Isso irá:
1. Iniciar seu servidor como um subprocesso
2. Abrir uma interface web para testes
3. Permitir que você teste todas as ferramentas do servidor de forma interativa

### Método 2: Teste direto via linha de comando

Você também pode testar iniciando o Inspector diretamente:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Ferramentas Disponíveis

O servidor fornece as seguintes ferramentas:

- **add(a, b)**: Soma dois números
- **multiply(a, b)**: Multiplica dois números  
- **get_greeting(name)**: Gera uma saudação personalizada
- **get_server_info()**: Obtém informações sobre o servidor

### Testando com Claude Desktop

Para usar este servidor com o Claude Desktop, adicione esta configuração ao seu `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Estrutura do Projeto

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Principais Diferenças em Relação ao SSE

**Transporte stdio (Atual):**
- ✅ Configuração mais simples - sem necessidade de servidor HTTP
- ✅ Maior segurança - sem endpoints HTTP
- ✅ Comunicação baseada em subprocessos
- ✅ JSON-RPC via stdin/stdout
- ✅ Melhor desempenho

**Transporte SSE (Descontinuado):**
- ❌ Requeria configuração de servidor Express
- ❌ Necessitava de roteamento e gerenciamento de sessões complexos
- ❌ Mais dependências (Express, manipulação de HTTP)
- ❌ Considerações adicionais de segurança
- ❌ Agora descontinuado na MCP 2025-06-18

## Dicas de Desenvolvimento

- Use `console.error()` para logs (nunca `console.log()`, pois escreve no stdout)
- Compile com `npm run build` antes de testar
- Teste com o Inspector para depuração visual
- Certifique-se de que todas as mensagens JSON estejam devidamente formatadas
- O servidor lida automaticamente com desligamento gracioso em SIGINT/SIGTERM

Esta solução segue a especificação atual do MCP e demonstra as melhores práticas para implementação de transporte stdio usando TypeScript.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
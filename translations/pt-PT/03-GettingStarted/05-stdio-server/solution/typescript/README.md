# Servidor MCP stdio - Solução em TypeScript

> **⚠️ Importante**: Esta solução foi atualizada para utilizar o **transporte stdio**, conforme recomendado pela Especificação MCP 2025-06-18. O transporte SSE original foi descontinuado.

## Visão Geral

Esta solução em TypeScript demonstra como construir um servidor MCP utilizando o transporte stdio atual. O transporte stdio é mais simples, mais seguro e oferece melhor desempenho em comparação com a abordagem SSE descontinuada.

## Pré-requisitos

- Node.js 18+ ou superior
- Gerenciador de pacotes npm ou yarn

## Instruções de Configuração

### Passo 1: Instalar as dependências

```bash
npm install
```

### Passo 2: Construir o projeto

```bash
npm run build
```

## Executar o Servidor

O servidor stdio funciona de forma diferente do antigo servidor SSE. Em vez de iniciar um servidor web, ele comunica-se através de stdin/stdout:

```bash
npm start
```

**Importante**: O servidor parecerá estar parado - isso é normal! Ele está aguardando mensagens JSON-RPC via stdin.

## Testar o Servidor

### Método 1: Utilizar o MCP Inspector (Recomendado)

```bash
npm run inspector
```

Isso irá:
1. Iniciar o seu servidor como um subprocesso
2. Abrir uma interface web para testes
3. Permitir testar todas as ferramentas do servidor de forma interativa

### Método 2: Testar diretamente via linha de comando

Também é possível testar iniciando o Inspector diretamente:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Ferramentas Disponíveis

O servidor fornece as seguintes ferramentas:

- **add(a, b)**: Soma dois números
- **multiply(a, b)**: Multiplica dois números  
- **get_greeting(name)**: Gera uma saudação personalizada
- **get_server_info()**: Obtém informações sobre o servidor

### Testar com o Claude Desktop

Para utilizar este servidor com o Claude Desktop, adicione esta configuração ao seu `claude_desktop_config.json`:

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
- ✅ Configuração mais simples - não é necessário servidor HTTP
- ✅ Maior segurança - sem endpoints HTTP
- ✅ Comunicação baseada em subprocessos
- ✅ JSON-RPC via stdin/stdout
- ✅ Melhor desempenho

**Transporte SSE (Descontinuado):**
- ❌ Requeria configuração de servidor Express
- ❌ Necessitava de roteamento e gestão de sessões complexos
- ❌ Mais dependências (Express, manipulação de HTTP)
- ❌ Considerações adicionais de segurança
- ❌ Agora descontinuado na MCP 2025-06-18

## Dicas de Desenvolvimento

- Utilize `console.error()` para registos (nunca `console.log()`, pois escreve no stdout)
- Compile com `npm run build` antes de testar
- Teste com o Inspector para depuração visual
- Certifique-se de que todas as mensagens JSON estão devidamente formatadas
- O servidor lida automaticamente com encerramento gracioso em SIGINT/SIGTERM

Esta solução segue a especificação atual do MCP e demonstra as melhores práticas para implementação de transporte stdio utilizando TypeScript.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
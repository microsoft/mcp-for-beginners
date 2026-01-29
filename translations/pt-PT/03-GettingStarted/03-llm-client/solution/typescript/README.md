# Executar este exemplo

Este exemplo envolve ter um LLM no cliente. O LLM necessita que execute isto num Codespaces ou que configure um token de acesso pessoal no GitHub para funcionar.

## -1- Instalar as dependências

```bash
npm install
```

## -3- Executar o servidor

```bash
npm run build
```

## -4- Executar o cliente

```sh
npm run client
```

Deverá ver um resultado semelhante a:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
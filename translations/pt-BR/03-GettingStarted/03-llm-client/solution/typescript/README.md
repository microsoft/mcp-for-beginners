# Executando este exemplo

Este exemplo envolve ter um LLM no cliente. O LLM precisa que você execute isso em um Codespaces ou que configure um token de acesso pessoal no GitHub para funcionar.

## -1- Instale as dependências

```bash
npm install
```

## -3- Execute o servidor

```bash
npm run build
```

## -4- Execute o cliente

```sh
npm run client
```

Você deverá ver um resultado semelhante a:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
# Cliente Calculator LLM

Uma aplicação Java que demonstra como usar LangChain4j para se conectar a um serviço de calculadora MCP (Model Context Protocol) através da API MiniMax compatível com OpenAI.

## Pré-requisitos

- Java 21 ou superior
- Maven 3.6+ (ou use o wrapper Maven incluído)
- Uma chave de API MiniMax
- Um serviço de calculadora MCP rodando em `http://localhost:8080`

## Obtendo a Chave de API

Esta aplicação usa a API MiniMax compatível com OpenAI. Siga estes passos para obter sua chave e endpoint:

### 1. Escolha um endpoint
1. Use `https://api.minimax.io/v1` para o endpoint global
2. Use `https://api.minimaxi.com/v1` para o endpoint da China

### 2. Crie uma chave de API
1. Crie uma chave de API MiniMax a partir da sua conta MiniMax
2. Guarde a chave em um local seguro

### 3. Configure as Variáveis de Ambiente

#### No Windows (Prompt de Comando):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### No Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### No macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Configuração e Instalação

1. **Clone ou navegue até o diretório do projeto**

2. **Instale as dependências**:
   ```cmd
   mvnw clean install
   ```
   Ou se você tiver o Maven instalado globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configure as variáveis de ambiente** (veja a seção "Obtendo a Chave de API" acima)

4. **Inicie o Serviço de Calculadora MCP**:
   Certifique-se de que o serviço de calculadora MCP do capítulo 1 esteja rodando em `http://localhost:8080/sse`. Ele deve estar ativo antes de você iniciar o cliente.

## Executando a Aplicação

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## O Que a Aplicação Faz

A aplicação demonstra três interações principais com o serviço de calculadora:

1. **Adição**: Calcula a soma de 24,5 e 17,3
2. **Raiz Quadrada**: Calcula a raiz quadrada de 144
3. **Ajuda**: Mostra as funções disponíveis da calculadora

## Saída Esperada

Quando executada com sucesso, você deverá ver uma saída similar a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Solução de Problemas

### Problemas Comuns

1. **"Variável de ambiente OPENAI_API_KEY não está configurada"**
   - Certifique-se de que você configurou a variável de ambiente `OPENAI_API_KEY`
   - Reinicie o terminal/prompt de comando após configurar a variável

2. **"Conexão recusada para localhost:8080"**
   - Garanta que o serviço de calculadora MCP esteja rodando na porta 8080
   - Verifique se outro serviço não está usando a porta 8080

3. **"Falha na autenticação"**
   - Verifique se sua chave de API é válida
   - Confira se `OPENAI_BASE_URL` corresponde ao endpoint que você pretende usar

4. **Erros de build do Maven**
   - Confirme que está usando o Java 21 ou superior: `java -version`
   - Tente limpar o build: `mvnw clean`

### Depuração

Para ativar o registro de depuração, adicione o seguinte argumento JVM ao executar:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuração

A aplicação está configurada para:
- Usar MiniMax-M3 por padrão, ou MiniMax-M2.7 quando `MINIMAX_MODEL_ID` estiver definido
- Conectar a `OPENAI_BASE_URL` quando estiver configurado; caso contrário, usar `https://api.minimaxi.com/v1` quando `MINIMAX_REGION=cn_zh`, ou `https://api.minimax.io/v1` por padrão
- Conectar ao serviço MCP em `http://localhost:8080/sse`
- Usar um timeout de 60 segundos para requisições

## Dependências

Dependências principais usadas neste projeto:
- **LangChain4j**: Para integração de IA e gestão de ferramentas
- **LangChain4j MCP**: Para suporte ao Model Context Protocol
- **LangChain4j OpenAI oficial**: Para integração com a API MiniMax compatível com OpenAI
- **Spring Boot**: Para framework de aplicação e injeção de dependências

## Licença

Este projeto está licenciado sob a Licença Apache 2.0 - veja o arquivo [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) para mais detalhes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
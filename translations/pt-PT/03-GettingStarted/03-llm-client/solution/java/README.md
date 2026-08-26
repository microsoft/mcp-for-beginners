# Cliente LLM Calculadora

Uma aplicação Java que demonstra como usar LangChain4j para se conectar a um serviço de calculadora MCP (Model Context Protocol) através da API MiniMax compatível com OpenAI.

## Pré-requisitos

- Java 21 ou superior
- Maven 3.6+ (ou use o Maven wrapper incluído)
- Uma chave de API MiniMax
- Um serviço de calculadora MCP a correr em `http://localhost:8080`

## Obter a Chave de API

Esta aplicação usa a API MiniMax compatível com OpenAI. Siga estes passos para obter a sua chave e endpoint:

### 1. Escolha um endpoint
1. Use `https://api.minimax.io/v1` para o endpoint global
2. Use `https://api.minimaxi.com/v1` para o endpoint da China

### 2. Crie uma chave de API
1. Crie uma chave de API MiniMax na sua conta MiniMax
2. Guarde a chave num local seguro

### 3. Defina as Variáveis de Ambiente

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

1. **Clone ou navegue até ao diretório do projeto**

2. **Instale as dependências**:
   ```cmd
   mvnw clean install
   ```
   Ou se tiver o Maven instalado globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configure as variáveis de ambiente** (veja a seção "Obter a Chave de API" acima)

4. **Inicie o Serviço de Calculadora MCP**:
   Certifique-se que o serviço de calculadora MCP do capítulo 1 está a correr em `http://localhost:8080/sse`. Este deve estar em execução antes de iniciar o cliente.

## Executar a Aplicação

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## O Que a Aplicação Faz

A aplicação demonstra três interações principais com o serviço de calculadora:

1. **Adição**: Calcula a soma de 24.5 e 17.3
2. **Raiz Quadrada**: Calcula a raiz quadrada de 144
3. **Ajuda**: Mostra as funções disponíveis da calculadora

## Saída Esperada

Quando correr com sucesso, deverá ver uma saída semelhante a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Resolução de Problemas

### Problemas Comuns

1. **"A variável de ambiente OPENAI_API_KEY não está definida"**
   - Certifique-se que definiu a variável de ambiente `OPENAI_API_KEY`
   - Reinicie o terminal/prompt de comando após definir a variável

2. **"Conexão recusada para localhost:8080"**
   - Verifique se o serviço de calculadora MCP está a correr na porta 8080
   - Verifique se outro serviço está a usar a porta 8080

3. **"Falha na autenticação"**
   - Verifique se a sua chave de API é válida
   - Confira se `OPENAI_BASE_URL` corresponde ao endpoint que pretende usar

4. **Erros na construção com Maven**
   - Certifique-se que está a usar Java 21 ou superior: `java -version`
   - Tente limpar a construção: `mvnw clean`

### Depuração

Para ativar a escrita de logs de debug, adicione o seguinte argumento JVM ao correr:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuração

A aplicação está configurada para:
- Usar MiniMax-M3 por defeito, ou MiniMax-M2.7 quando `MINIMAX_MODEL_ID` está definido
- Conectar ao `OPENAI_BASE_URL` se estiver definido; caso contrário usar `https://api.minimaxi.com/v1` quando `MINIMAX_REGION=cn_zh`, ou `https://api.minimax.io/v1` por defeito
- Conectar ao serviço MCP em `http://localhost:8080/sse`
- Usar um timeout de 60 segundos para requisições

## Dependências

Dependências principais usadas neste projeto:
- **LangChain4j**: Para integração AI e gestão de ferramentas
- **LangChain4j MCP**: Para suporte ao Model Context Protocol
- **LangChain4j OpenAI oficial**: Para integração com a API MiniMax compatível com OpenAI
- **Spring Boot**: Para framework de aplicação e injeção de dependências

## Licença

Este projeto está licenciado sob a Licença Apache 2.0 - veja o ficheiro [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) para detalhes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Calculator LLM Client

Uma aplicação Java que demonstra como usar o LangChain4j para se conectar a um serviço de calculadora MCP (Model Context Protocol) com integração dos GitHub Models.

## Pré-requisitos

- Java 21 ou superior
- Maven 3.6+ (ou use o Maven wrapper incluído)
- Uma conta GitHub com acesso aos GitHub Models
- Um serviço de calculadora MCP a correr em `http://localhost:8080`

## Obter o Token do GitHub

Esta aplicação usa os GitHub Models, que requerem um token de acesso pessoal do GitHub. Siga estes passos para obter o seu token:

### 1. Aceder aos GitHub Models
1. Vá a [GitHub Models](https://github.com/marketplace/models)
2. Inicie sessão com a sua conta GitHub
3. Solicite acesso aos GitHub Models, caso ainda não o tenha feito

### 2. Criar um Token de Acesso Pessoal
1. Vá a [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome descritivo ao seu token (ex.: "MCP Calculator Client")
4. Defina a expiração conforme necessário
5. Selecione os seguintes scopes:
   - `repo` (se for aceder a repositórios privados)
   - `user:email`
6. Clique em "Generate token"
7. **Importante**: Copie o token imediatamente - não poderá vê-lo novamente!

### 3. Definir a Variável de Ambiente

#### No Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### No Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### No macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Configuração e Instalação

1. **Clone ou navegue até ao diretório do projeto**

2. **Instale as dependências**:
   ```cmd
   mvnw clean install
   ```
   Ou, se tiver o Maven instalado globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configure a variável de ambiente** (veja a secção "Obter o Token do GitHub" acima)

4. **Inicie o Serviço de Calculadora MCP**:
   Certifique-se de que o serviço de calculadora MCP do capítulo 1 está a correr em `http://localhost:8080/sse`. Este deve estar ativo antes de iniciar o cliente.

## Executar a Aplicação

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## O que a Aplicação Faz

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

1. **"GITHUB_TOKEN environment variable not set"**
   - Certifique-se de que definiu a variável de ambiente `GITHUB_TOKEN`
   - Reinicie o terminal/linha de comandos após definir a variável

2. **"Connection refused to localhost:8080"**
   - Verifique se o serviço de calculadora MCP está a correr na porta 8080
   - Confirme se outro serviço não está a usar a porta 8080

3. **"Authentication failed"**
   - Verifique se o seu token GitHub é válido e tem as permissões corretas
   - Confirme se tem acesso aos GitHub Models

4. **Erros na compilação com Maven**
   - Certifique-se de que está a usar Java 21 ou superior: `java -version`
   - Tente limpar a compilação: `mvnw clean`

### Depuração

Para ativar o logging de depuração, adicione o seguinte argumento JVM ao executar:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuração

A aplicação está configurada para:
- Usar os GitHub Models com o modelo `gpt-4.1-nano`
- Conectar ao serviço MCP em `http://localhost:8080/sse`
- Usar um timeout de 60 segundos para pedidos
- Ativar logging de pedidos/respostas para depuração

## Dependências

Principais dependências usadas neste projeto:
- **LangChain4j**: Para integração de IA e gestão de ferramentas
- **LangChain4j MCP**: Para suporte ao Model Context Protocol
- **LangChain4j GitHub Models**: Para integração com GitHub Models
- **Spring Boot**: Para framework da aplicação e injeção de dependências

## Licença

Este projeto está licenciado sob a Apache License 2.0 - consulte o ficheiro [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) para mais detalhes.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
# Calculator LLM Client

Uma aplicação Java que demonstra como usar o LangChain4j para se conectar a um serviço de calculadora MCP (Model Context Protocol) com integração dos GitHub Models.

## Pré-requisitos

- Java 21 ou superior
- Maven 3.6+ (ou use o Maven wrapper incluído)
- Uma conta GitHub com acesso aos GitHub Models
- Um serviço de calculadora MCP rodando em `http://localhost:8080`

## Obtendo o Token do GitHub

Esta aplicação usa os GitHub Models, que requerem um token de acesso pessoal do GitHub. Siga os passos abaixo para obter seu token:

### 1. Acesse os GitHub Models
1. Vá para [GitHub Models](https://github.com/marketplace/models)
2. Faça login com sua conta GitHub
3. Solicite acesso aos GitHub Models, caso ainda não tenha

### 2. Crie um Token de Acesso Pessoal
1. Vá para [Configurações do GitHub → Configurações de desenvolvedor → Tokens de acesso pessoal → Tokens (clássicos)](https://github.com/settings/tokens)
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome descritivo para seu token (ex: "MCP Calculator Client")
4. Defina a expiração conforme necessário
5. Selecione os seguintes escopos:
   - `repo` (se for acessar repositórios privados)
   - `user:email`
6. Clique em "Generate token"
7. **Importante**: Copie o token imediatamente - você não poderá vê-lo novamente!

### 3. Configure a Variável de Ambiente

#### No Windows (Prompt de Comando):
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

1. **Clone ou navegue até o diretório do projeto**

2. **Instale as dependências**:
   ```cmd
   mvnw clean install
   ```
   Ou, se você tiver o Maven instalado globalmente:
   ```cmd
   mvn clean install
   ```

3. **Configure a variável de ambiente** (veja a seção "Obtendo o Token do GitHub" acima)

4. **Inicie o Serviço de Calculadora MCP**:
   Certifique-se de que o serviço de calculadora MCP do capítulo 1 esteja rodando em `http://localhost:8080/sse`. Ele deve estar ativo antes de iniciar o cliente.

## Executando a Aplicação

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## O que a Aplicação Faz

A aplicação demonstra três interações principais com o serviço de calculadora:

1. **Adição**: Calcula a soma de 24.5 e 17.3
2. **Raiz Quadrada**: Calcula a raiz quadrada de 144
3. **Ajuda**: Exibe as funções disponíveis da calculadora

## Saída Esperada

Quando executada com sucesso, você deve ver uma saída semelhante a:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Solução de Problemas

### Problemas Comuns

1. **"Variável de ambiente GITHUB_TOKEN não configurada"**
   - Verifique se você configurou a variável de ambiente `GITHUB_TOKEN`
   - Reinicie seu terminal/prompt de comando após configurar a variável

2. **"Conexão recusada para localhost:8080"**
   - Certifique-se de que o serviço de calculadora MCP está rodando na porta 8080
   - Verifique se outro serviço não está usando a porta 8080

3. **"Falha na autenticação"**
   - Verifique se seu token do GitHub é válido e tem as permissões corretas
   - Confirme se você tem acesso aos GitHub Models

4. **Erros na build do Maven**
   - Confirme que está usando Java 21 ou superior: `java -version`
   - Tente limpar a build: `mvnw clean`

### Depuração

Para ativar o log de depuração, adicione o seguinte argumento JVM ao executar:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configuração

A aplicação está configurada para:
- Usar os GitHub Models com o modelo `gpt-4.1-nano`
- Conectar ao serviço MCP em `http://localhost:8080/sse`
- Usar timeout de 60 segundos para requisições
- Habilitar log de requisição/resposta para depuração

## Dependências

Principais dependências usadas neste projeto:
- **LangChain4j**: Para integração com IA e gerenciamento de ferramentas
- **LangChain4j MCP**: Para suporte ao Model Context Protocol
- **LangChain4j GitHub Models**: Para integração com GitHub Models
- **Spring Boot**: Para framework da aplicação e injeção de dependências

## Licença

Este projeto está licenciado sob a Apache License 2.0 - veja o arquivo [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) para mais detalhes.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
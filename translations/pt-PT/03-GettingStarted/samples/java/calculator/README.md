# Serviço MCP Calculadora Básica

> [!NOTE]
> Este exemplo utiliza o transporte HTTP+SSE legado e destina-se a um SDK compatível
> com MCP `2025-11-25`. Novos servidores remotos devem usar o suporte HTTP
> Streamable `2026-07-28`.

Este serviço fornece operações básicas de calculadora através do Protocolo de Contexto de Modelo (MCP) usando Spring Boot com transporte WebFlux. Está concebido como um exemplo simples para principiantes que aprendem sobre implementações MCP.

Para mais informações, consulte a documentação de referência do [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).

## Visão Geral

O serviço apresenta:
- Suporte para SSE (Server-Sent Events)
- Registo automático de ferramentas usando a anotação `@Tool` do Spring AI
- Funções básicas de calculadora:
  - Adição, subtração, multiplicação, divisão
  - Cálculo de potência e raiz quadrada
  - Módulo (resto) e valor absoluto
  - Função de ajuda para descrições das operações

## Funcionalidades

Este serviço de calculadora oferece as seguintes capacidades:

1. **Operações Aritméticas Básicas**:
   - Adição de dois números
   - Subtração de um número por outro
   - Multiplicação de dois números
   - Divisão de um número por outro (com verificação de divisão por zero)

2. **Operações Avançadas**:
   - Cálculo de potência (elevar uma base a um expoente)
   - Cálculo da raiz quadrada (com verificação de números negativos)
   - Cálculo do módulo (resto da divisão)
   - Cálculo do valor absoluto

3. **Sistema de Ajuda**:
   - Função de ajuda incorporada que explica todas as operações disponíveis

## Utilização do Serviço

O serviço expõe os seguintes endpoints de API através do protocolo MCP:

- `add(a, b)`: Adicionar dois números
- `subtract(a, b)`: Subtrair o segundo número ao primeiro
- `multiply(a, b)`: Multiplicar dois números
- `divide(a, b)`: Dividir o primeiro número pelo segundo (com verificação de zero)
- `power(base, exponent)`: Calcular a potência de um número
- `squareRoot(number)`: Calcular a raiz quadrada (com verificação de número negativo)
- `modulus(a, b)`: Calcular o resto da divisão
- `absolute(number)`: Calcular o valor absoluto
- `help()`: Obter informações sobre as operações disponíveis

## Cliente de Teste

Um cliente de teste simples está incluído no pacote `com.microsoft.mcp.sample.client`. A classe `SampleCalculatorClient` demonstra as operações disponíveis do serviço de calculadora.

## Uso do Cliente LangChain4j

O projeto inclui um cliente de exemplo LangChain4j em `com.microsoft.mcp.sample.client.LangChain4jClient` que demonstra como integrar o serviço de calculadora com LangChain4j e modelos GitHub:

### Pré-requisitos

1. **Configuração do Token do GitHub**:
   
   Para usar os modelos de IA do GitHub (como phi-4), necessita de um token de acesso pessoal do GitHub:

   a. Vá às definições da sua conta GitHub: https://github.com/settings/tokens
   
   b. Clique em "Generate new token" → "Generate new token (classic)"
   
   c. Dê um nome descritivo ao seu token
   
   d. Selecione os seguintes escopos:
      - `repo` (Controlo total de repositórios privados)
      - `read:org` (Leitura de membros da organização e equipas, leitura de projetos da organização)
      - `gist` (Criar gists)
      - `user:email` (Acesso a endereços de email do utilizador (somente leitura))
   
   e. Clique em "Generate token" e copie o seu novo token
   
   f. Defina-o como variável de ambiente:
      
      No Windows:
      ```
      set GITHUB_TOKEN=your-github-token
      ```
      
      No macOS/Linux:
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. Para configuração persistente, adicione-o às variáveis de ambiente através das definições do sistema

2. Adicione a dependência GitHub do LangChain4j ao seu projeto (já incluída no pom.xml):
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. Assegure que o servidor da calculadora está a correr em `localhost:8080`

### Executar o Cliente LangChain4j

Este exemplo demonstra:
- Ligação ao servidor MCP da calculadora via transporte SSE
- Uso do LangChain4j para criar um bot de chat que aproveita as operações da calculadora
- Integração com modelos de IA do GitHub (agora usando o modelo phi-4)

O cliente envia as seguintes consultas de exemplo para demonstrar a funcionalidade:
1. Calcular a soma de dois números
2. Encontrar a raiz quadrada de um número
3. Obter informações de ajuda sobre as operações disponíveis da calculadora

Execute o exemplo e verifique a saída na consola para ver como o modelo de IA utiliza as ferramentas da calculadora para responder às consultas.

### Configuração do Modelo GitHub

O cliente LangChain4j está configurado para usar o modelo phi-4 do GitHub com as seguintes definições:

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

Para usar modelos GitHub diferentes, basta alterar o parâmetro `modelName` para outro modelo suportado (ex.: "claude-3-haiku-20240307", "llama-3-70b-8192", etc.).

## Dependências

O projeto requer as seguintes dependências principais:

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## Construção do Projeto

Construa o projeto usando Maven:
```bash
./mvnw clean install -DskipTests
```

## Execução do Servidor

### Usando Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Usando o MCP Inspector

O MCP Inspector é uma ferramenta útil para interagir com serviços MCP. Para usá-lo com este serviço de calculadora:

1. **Instale e execute o MCP Inspector** numa nova janela de terminal:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Aceda à interface web** clicando na URL mostrada pela aplicação (tipicamente http://localhost:6274)

3. **Configure a ligação**:
   - Defina o tipo de transporte para "SSE"
   - Defina a URL para o endpoint SSE do seu servidor em execução: `http://localhost:8080/sse`
   - Clique em "Connect"

4. **Use as ferramentas**:
   - Clique em "List Tools" para ver as operações disponíveis da calculadora
   - Selecione uma ferramenta e clique em "Run Tool" para executar uma operação

![Captura de ecrã do MCP Inspector](../../../../../../translated_images/pt-PT/tool.c75a0b2380efcf1a.webp)

### Usando Docker

O projeto inclui um Dockerfile para implantação em container:

1. **Construa a imagem Docker**:
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **Execute o contentor Docker**:
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

Isto irá:
- Construir uma imagem Docker multi-stágio com Maven 3.9.9 e Eclipse Temurin 24 JDK
- Criar uma imagem de container otimizada
- Expor o serviço na porta 8080
- Iniciar o serviço MCP de calculadora dentro do container

Pode aceder ao serviço em `http://localhost:8080` assim que o container estiver a correr.

## Resolução de Problemas

### Problemas Comuns com o Token do GitHub


1. **Problemas de Permissão do Token**: Se receber um erro 403 Forbidden, verifique se o seu token tem as permissões corretas conforme descrito nos pré-requisitos.

2. **Token Não Encontrado**: Se receber um erro "No API key found", certifique-se de que a variável de ambiente GITHUB_TOKEN está devidamente configurada.

3. **Limitação de Taxa**: A API do GitHub tem limites de taxa. Se encontrar um erro de limite de taxa (código de estado 429), aguarde alguns minutos antes de tentar novamente.

4. **Expiração do Token**: Os tokens do GitHub podem expirar. Se receber erros de autenticação após algum tempo, gere um novo token e atualize a sua variável de ambiente.

Se precisar de mais ajuda, consulte a [documentação do LangChain4j](https://github.com/langchain4j/langchain4j) ou a [documentação da API do GitHub](https://docs.github.com/en/rest).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
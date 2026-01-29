# Cliente Java MCP - Demonstração da Calculadora

Este projeto demonstra como criar um cliente Java que se conecta e interage com um servidor MCP (Model Context Protocol). Neste exemplo, vamos ligar-nos ao servidor da calculadora do Capítulo 01 e realizar várias operações matemáticas.

## Pré-requisitos

Antes de executar este cliente, precisa de:

1. **Iniciar o Servidor da Calculadora** do Capítulo 01:
   - Navegue até ao diretório do servidor da calculadora: `03-GettingStarted/01-first-server/solution/java/`
   - Construa e execute o servidor da calculadora:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - O servidor deverá estar a correr em `http://localhost:8080`

2. Ter o **Java 21 ou superior** instalado no seu sistema
3. Ter o **Maven** (incluído via Maven Wrapper)

## O que é o SDKClient?

O `SDKClient` é uma aplicação Java que demonstra como:
- Ligar-se a um servidor MCP usando transporte Server-Sent Events (SSE)
- Listar as ferramentas disponíveis no servidor
- Invocar remotamente várias funções da calculadora
- Tratar as respostas e mostrar os resultados

## Como Funciona

O cliente utiliza o framework Spring AI MCP para:

1. **Estabelecer Ligação**: Cria um transporte WebFlux SSE para se ligar ao servidor da calculadora
2. **Inicializar o Cliente**: Configura o cliente MCP e estabelece a ligação
3. **Descobrir Ferramentas**: Lista todas as operações disponíveis da calculadora
4. **Executar Operações**: Invoca várias funções matemáticas com dados de exemplo
5. **Mostrar Resultados**: Exibe os resultados de cada cálculo

## Estrutura do Projeto

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Dependências Principais

O projeto utiliza as seguintes dependências principais:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Esta dependência fornece:
- `McpClient` - A interface principal do cliente
- `WebFluxSseClientTransport` - Transporte SSE para comunicação web
- Esquemas do protocolo MCP e tipos de pedido/resposta

## Construir o Projeto

Construa o projeto usando o Maven wrapper:

```cmd
.\mvnw clean install
```

## Executar o Cliente

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Nota**: Certifique-se de que o servidor da calculadora está a correr em `http://localhost:8080` antes de executar qualquer um destes comandos.

## O que o Cliente Faz

Quando executar o cliente, ele irá:

1. **Ligar-se** ao servidor da calculadora em `http://localhost:8080`
2. **Listar Ferramentas** - Mostra todas as operações disponíveis da calculadora
3. **Realizar Cálculos**:
   - Adição: 5 + 3 = 8
   - Subtração: 10 - 4 = 6
   - Multiplicação: 6 × 7 = 42
   - Divisão: 20 ÷ 4 = 5
   - Potência: 2^8 = 256
   - Raiz Quadrada: √16 = 4
   - Valor Absoluto: |-5.5| = 5.5
   - Ajuda: Mostra as operações disponíveis

## Saída Esperada

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Nota**: Pode ver avisos do Maven sobre threads pendentes no final - isto é normal em aplicações reativas e não indica erro.

## Compreender o Código

### 1. Configuração do Transporte
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Isto cria um transporte SSE (Server-Sent Events) que se liga ao servidor da calculadora.

### 2. Criação do Cliente
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Cria um cliente MCP síncrono e inicializa a ligação.

### 3. Invocação das Ferramentas
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Invoca a ferramenta "add" com os parâmetros a=5.0 e b=3.0.

## Resolução de Problemas

### Servidor Não Está a Correr
Se receber erros de ligação, certifique-se de que o servidor da calculadora do Capítulo 01 está a correr:
```
Error: Connection refused
```
**Solução**: Inicie primeiro o servidor da calculadora.

### Porta Já Está a Ser Usada
Se a porta 8080 estiver ocupada:
```
Error: Address already in use
```
**Solução**: Pare outras aplicações que estejam a usar a porta 8080 ou altere o servidor para usar uma porta diferente.

### Erros na Construção
Se encontrar erros na construção:
```cmd
.\mvnw clean install -DskipTests
```

## Saiba Mais

- [Documentação Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Especificação do Model Context Protocol](https://modelcontextprotocol.io/)
- [Documentação Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
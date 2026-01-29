# Demonstração de Streaming HTTP da Calculadora

Este projeto demonstra streaming HTTP usando Server-Sent Events (SSE) com Spring Boot WebFlux. Consiste em duas aplicações:

- **Calculator Server**: Um serviço web reativo que realiza cálculos e transmite resultados usando SSE
- **Calculator Client**: Uma aplicação cliente que consome o endpoint de streaming

## Pré-requisitos

- Java 17 ou superior
- Maven 3.6 ou superior

## Estrutura do Projeto

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Como Funciona

1. O **Calculator Server** expõe um endpoint `/calculate` que:
   - Aceita parâmetros de query: `a` (número), `b` (número), `op` (operação)
   - Operações suportadas: `add`, `sub`, `mul`, `div`
   - Retorna Server-Sent Events com o progresso do cálculo e o resultado

2. O **Calculator Client** conecta-se ao servidor e:
   - Faz um pedido para calcular `7 * 5`
   - Consome a resposta em streaming
   - Imprime cada evento no console

## Executar as Aplicações

### Opção 1: Usar Maven (Recomendado)

#### 1. Iniciar o Calculator Server

Abra um terminal e navegue até ao diretório do servidor:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

O servidor irá iniciar em `http://localhost:8080`

Deverá ver uma saída semelhante a:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Executar o Calculator Client

Abra um **novo terminal** e navegue até ao diretório do cliente:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

O cliente irá conectar-se ao servidor, realizar o cálculo e mostrar os resultados em streaming.

### Opção 2: Usar Java diretamente

#### 1. Compilar e executar o servidor:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Compilar e executar o cliente:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testar o Servidor Manualmente

Também pode testar o servidor usando um navegador web ou curl:

### Usando um navegador web:
Visite: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Usando curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Saída Esperada

Ao executar o cliente, deverá ver uma saída em streaming semelhante a:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Operações Suportadas

- `add` - Adição (a + b)
- `sub` - Subtração (a - b)
- `mul` - Multiplicação (a * b)
- `div` - Divisão (a / b, retorna NaN se b = 0)

## Referência da API

### GET /calculate

**Parâmetros:**
- `a` (obrigatório): Primeiro número (double)
- `b` (obrigatório): Segundo número (double)
- `op` (obrigatório): Operação (`add`, `sub`, `mul`, `div`)

**Resposta:**
- Content-Type: `text/event-stream`
- Retorna Server-Sent Events com o progresso do cálculo e o resultado

**Exemplo de Pedido:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Exemplo de Resposta:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Resolução de Problemas

### Problemas Comuns

1. **Porta 8080 já em uso**
   - Pare quaisquer outras aplicações que estejam a usar a porta 8080
   - Ou altere a porta do servidor em `calculator-server/src/main/resources/application.yml`

2. **Conexão recusada**
   - Certifique-se de que o servidor está a correr antes de iniciar o cliente
   - Verifique se o servidor iniciou corretamente na porta 8080

3. **Problemas com nomes de parâmetros**
   - Este projeto inclui configuração do compilador Maven com a flag `-parameters`
   - Se encontrar problemas de binding de parâmetros, assegure-se de que o projeto foi construído com esta configuração

### Parar as Aplicações

- Pressione `Ctrl+C` no terminal onde cada aplicação está a correr
- Ou use `mvn spring-boot:stop` se estiver a correr como processo em background

## Stack Tecnológico

- **Spring Boot 3.3.1** - Framework de aplicação
- **Spring WebFlux** - Framework web reativo
- **Project Reactor** - Biblioteca de streams reativos
- **Netty** - Servidor de I/O não bloqueante
- **Maven** - Ferramenta de build
- **Java 17+** - Linguagem de programação

## Próximos Passos

Experimente modificar o código para:
- Adicionar mais operações matemáticas
- Incluir tratamento de erros para operações inválidas
- Adicionar logging de pedidos/respostas
- Implementar autenticação
- Adicionar testes unitários

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
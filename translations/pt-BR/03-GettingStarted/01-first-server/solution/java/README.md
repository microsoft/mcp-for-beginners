# Serviço Básico de Calculadora MCP

Este serviço oferece operações básicas de calculadora através do Model Context Protocol (MCP) usando Spring Boot com transporte WebFlux. Foi criado como um exemplo simples para iniciantes que estão aprendendo sobre implementações MCP.

Para mais informações, consulte a documentação de referência do [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).


## Usando o Serviço

O serviço expõe os seguintes endpoints de API através do protocolo MCP:

- `add(a, b)`: Soma dois números
- `subtract(a, b)`: Subtrai o segundo número do primeiro
- `multiply(a, b)`: Multiplica dois números
- `divide(a, b)`: Divide o primeiro número pelo segundo (com verificação de zero)
- `power(base, exponent)`: Calcula a potência de um número
- `squareRoot(number)`: Calcula a raiz quadrada (com verificação de número negativo)
- `modulus(a, b)`: Calcula o resto da divisão
- `absolute(number)`: Calcula o valor absoluto

## Dependências

O projeto requer as seguintes dependências principais:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Construindo o Projeto

Compile o projeto usando Maven:
```bash
./mvnw clean install -DskipTests
```

## Executando o Servidor

### Usando Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Usando o MCP Inspector

O MCP Inspector é uma ferramenta útil para interagir com serviços MCP. Para usá-lo com este serviço de calculadora:

1. **Instale e execute o MCP Inspector** em uma nova janela do terminal:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Acesse a interface web** clicando na URL exibida pelo app (normalmente http://localhost:6274)

3. **Configure a conexão**:
   - Defina o tipo de transporte como "SSE"
   - Defina a URL para o endpoint SSE do seu servidor em execução: `http://localhost:8080/sse`
   - Clique em "Connect"

4. **Use as ferramentas**:
   - Clique em "List Tools" para ver as operações de calculadora disponíveis
   - Selecione uma ferramenta e clique em "Run Tool" para executar uma operação

![Captura de tela do MCP Inspector](../../../../../../translated_images/pt-BR/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
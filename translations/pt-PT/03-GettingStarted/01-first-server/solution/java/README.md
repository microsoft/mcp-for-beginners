# Serviço MCP Calculadora Básica

> [!NOTE]
> Esta solução Java utiliza o transporte legacy HTTP+SSE e destina-se a um SDK
> compatível com MCP `2025-11-25`. É mantida para corresponder ao código do curso;
> novos servidores remotos devem usar o suporte HTTP Streamable `2026-07-28`.

Este serviço fornece operações básicas de calculadora através do Protocolo de Contexto de Modelo (MCP) usando Spring Boot com transporte WebFlux. Está concebido como um exemplo simples para iniciantes que aprendem sobre implementações MCP.

Para mais informações, consulte a documentação de referência do [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html).


## Usar o Serviço

O serviço expõe os seguintes endpoints API através do protocolo MCP:

- `add(a, b)`: Somar dois números
- `subtract(a, b)`: Subtrair o segundo número do primeiro
- `multiply(a, b)`: Multiplicar dois números
- `divide(a, b)`: Dividir o primeiro número pelo segundo (com verificação de zero)
- `power(base, exponent)`: Calcular a potência de um número
- `squareRoot(number)`: Calcular a raiz quadrada (com verificação de número negativo)
- `modulus(a, b)`: Calcular o resto da divisão
- `absolute(number)`: Calcular o valor absoluto

## Dependências

O projeto requer as seguintes dependências principais:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Construir o Projeto

Construa o projeto usando Maven:
```bash
./mvnw clean install -DskipTests
```

## Executar o Servidor

### Usando Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### Usando MCP Inspector

O MCP Inspector é uma ferramenta útil para interagir com serviços MCP. Para usá-lo com este serviço de calculadora:

1. **Instale e execute o MCP Inspector** numa nova janela de terminal:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Aceda à interface web** clicando no URL apresentado pela app (tipicamente http://localhost:6274)

3. **Configure a ligação**:
   - Defina o tipo de transporte para "SSE"
   - Defina o URL para o endpoint SSE do seu servidor em execução: `http://localhost:8080/sse`
   - Clique em "Connect"

4. **Use as ferramentas**:
   - Clique em "List Tools" para ver as operações da calculadora disponíveis
   - Selecione uma ferramenta e clique em "Run Tool" para executar uma operação

![Captura de ecrã do MCP Inspector](../../../../../../translated_images/pt-PT/tool.40e180a7b0d0fe20.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
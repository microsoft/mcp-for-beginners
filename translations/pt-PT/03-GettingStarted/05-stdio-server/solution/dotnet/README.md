# Servidor MCP stdio - Solução .NET

> **⚠️ Importante**: Esta solução foi atualizada para utilizar o **transporte stdio**, conforme recomendado pela Especificação MCP 2025-06-18. O transporte SSE original foi descontinuado.

## Visão Geral

Esta solução .NET demonstra como construir um servidor MCP utilizando o transporte stdio atual. O transporte stdio é mais simples, mais seguro e oferece melhor desempenho do que a abordagem SSE descontinuada.

## Pré-requisitos

- SDK .NET 9.0 ou superior
- Conhecimento básico sobre injeção de dependências no .NET

## Instruções de Configuração

### Passo 1: Restaurar dependências

```bash
dotnet restore
```

### Passo 2: Construir o projeto

```bash
dotnet build
```

## Executando o Servidor

O servidor stdio funciona de forma diferente do antigo servidor baseado em HTTP. Em vez de iniciar um servidor web, ele se comunica através de stdin/stdout:

```bash
dotnet run
```

**Importante**: O servidor parecerá estar travado - isso é normal! Ele está aguardando mensagens JSON-RPC via stdin.

## Testando o Servidor

### Método 1: Usando o MCP Inspector (Recomendado)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Isso irá:
1. Iniciar o seu servidor como um subprocesso
2. Abrir uma interface web para testes
3. Permitir que você teste todas as ferramentas do servidor de forma interativa

### Método 2: Teste direto via linha de comando

Você também pode testar iniciando o Inspector diretamente:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Ferramentas Disponíveis

O servidor fornece as seguintes ferramentas:

- **AddNumbers(a, b)**: Soma dois números
- **MultiplyNumbers(a, b)**: Multiplica dois números  
- **GetGreeting(name)**: Gera uma saudação personalizada
- **GetServerInfo()**: Obtém informações sobre o servidor

### Testando com o Claude Desktop

Para usar este servidor com o Claude Desktop, adicione esta configuração ao seu `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Estrutura do Projeto

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Principais Diferenças em Relação ao HTTP/SSE

**Transporte stdio (Atual):**
- ✅ Configuração mais simples - não é necessário servidor web
- ✅ Maior segurança - sem endpoints HTTP
- ✅ Utiliza `Host.CreateApplicationBuilder()` em vez de `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` em vez de `WithHttpTransport()`
- ✅ Aplicação de console em vez de aplicação web
- ✅ Melhor desempenho

**Transporte HTTP/SSE (Descontinuado):**
- ❌ Requeria servidor web ASP.NET Core
- ❌ Necessitava de configuração de roteamento com `app.MapMcp()`
- ❌ Configuração e dependências mais complexas
- ❌ Considerações adicionais de segurança
- ❌ Agora descontinuado na MCP 2025-06-18

## Funcionalidades de Desenvolvimento

- **Injeção de Dependências**: Suporte completo a DI para serviços e logging
- **Logging Estruturado**: Logging adequado para stderr utilizando `ILogger<T>`
- **Atributos de Ferramenta**: Definição limpa de ferramentas usando atributos `[McpServerTool]`
- **Suporte a Async**: Todas as ferramentas suportam operações assíncronas
- **Tratamento de Erros**: Tratamento de erros e logging de forma elegante

## Dicas de Desenvolvimento

- Use `ILogger` para logging (nunca escreva diretamente no stdout)
- Construa o projeto com `dotnet build` antes de testar
- Teste com o Inspector para depuração visual
- Todo o logging é direcionado automaticamente para stderr
- O servidor lida com sinais de encerramento de forma graciosa

Esta solução segue a especificação atual do MCP e demonstra as melhores práticas para a implementação do transporte stdio utilizando .NET.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
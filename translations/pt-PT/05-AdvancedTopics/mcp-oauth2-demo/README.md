# Demonstração MCP OAuth2

> [!WARNING]
> Esta é uma amostra local para aprendizagem, não um serviço de autorização para produção. Usa um cliente em memória e gera uma nova chave de assinatura à inicialização. Nunca a
> implemente com um segredo de cliente partilhado, padrão ou controlado por código fonte.


## Introdução

OAuth2 é o protocolo padrão da indústria para autorização, permitindo acesso seguro a recursos sem partilhar credenciais. Em implementações MCP (Model Context Protocol), OAuth2 fornece uma forma robusta de autenticar e autorizar clientes (como agentes de IA) para aceder aos servidores MCP e às suas ferramentas.

Esta lição demonstra como implementar autenticação OAuth2 para servidores MCP usando Spring Boot, um padrão comum para implementações empresariais e de produção.

## Objetivos de Aprendizagem

No final desta lição, irá:
- Compreender como o OAuth2 se integra com servidores MCP
- Implementar um Servidor de Autorização Spring para emissão de tokens
- Proteger endpoints MCP com autenticação baseada em JWT
- Configurar o fluxo de credenciais do cliente para comunicação máquina-a-máquina

## Pré-requisitos

- Conhecimentos básicos de Java e Spring Boot
- Familiaridade com conceitos MCP dos módulos anteriores
- Maven ou Gradle instalados

---

## Visão geral do projeto

Este projeto é uma **aplicação Spring Boot mínima** que atua como:

* um **Servidor de Autorização Spring** (emitindo tokens de acesso JWT via o fluxo `client_credentials`), e  
* um **Servidor de Recursos** (protegendo o seu próprio endpoint `/hello`).

Espelha a configuração mostrada no [post do blog Spring (2 Abr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Início rápido (local)

```bash
# Use um valor local único e mantenha-o fora do histórico do shell sempre que possível.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obter um token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# chamar o endpoint protegido
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testar a configuração OAuth2

Pode testar a configuração de segurança OAuth2 com os seguintes passos:

### 1. Verificar que o servidor está a correr e protegido

```bash
# Isto deve retornar 401 Unauthorized, confirmando que a segurança OAuth2 está ativa
curl -v http://localhost:8081/
```

### 2. Obter um token de acesso usando credenciais do cliente

```bash
# Obter e extrair a resposta completa do token
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Ou para extrair apenas o token (requer jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

No PowerShell, defina o segredo local antes de executar o Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Aceder ao endpoint protegido usando o token

```bash
# A usar o token guardado
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ou diretamente com o valor do token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uma resposta com sucesso "Hello from MCP OAuth2 Demo!" confirma que a configuração OAuth2 está a funcionar corretamente.

---

## Construção do container

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Segurança em produção

Para uma implementação em produção, use um fornecedor de identidade dedicado em vez
deste servidor de autorização de demonstração em processo. Guarde as credenciais num
cofre de segredos gerido, faça a sua rotação, use chaves de assinatura persistentes, restrinja os escopos, e
estabeleça um emissor explícito. Nunca coloque um segredo de cliente no código fonte, imagens de container,
manifestos de implantação ou saída de comandos.

Para Azure Container Apps, armazene o valor como um segredo de Container Apps suportado por
Key Vault quando possível, e exponha apenas uma referência secreta através da
variável de ambiente `OAUTH_CLIENT_SECRET`.

---

## Implantar no **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

O nome completo (FQDN) de entrada torna-se o seu **emissor** (`https://<fqdn>`).  
A Azure fornece automaticamente um certificado TLS confiável para `*.azurecontainerapps.io`.

---

## Ligar ao **Azure API Management**

Adicione esta política de entrada à sua API:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

O APIM irá buscar os JWKS e validar todas as requisições.

---

## Próximos passos

- [5.4 Contextos raiz](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
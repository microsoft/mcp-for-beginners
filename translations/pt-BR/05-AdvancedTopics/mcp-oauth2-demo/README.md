# Demonstração MCP OAuth2

> [!WARNING]
> Este é um exemplo local para aprendizado, não um serviço de autorização para produção. Ele
> usa um cliente em memória e gera uma nova chave de assinatura ao iniciar. Nunca
> o implante com um segredo de cliente compartilhado, padrão ou controlado por código-fonte.

## Introdução

OAuth2 é o protocolo padrão da indústria para autorização, permitindo acesso seguro a recursos sem compartilhar credenciais. Em implementações MCP (Model Context Protocol), OAuth2 oferece uma forma robusta de autenticar e autorizar clientes (como agentes de IA) para acessar servidores MCP e suas ferramentas.

Esta lição demonstra como implementar autenticação OAuth2 para servidores MCP usando Spring Boot, um padrão comum para implantações empresariais e de produção.

## Objetivos de aprendizagem

Ao final desta lição, você irá:
- Entender como OAuth2 se integra com servidores MCP
- Implementar um Servidor de Autorização Spring para emissão de tokens
- Proteger endpoints MCP com autenticação baseada em JWT
- Configurar o fluxo de credenciais de cliente para comunicação máquina-a-máquina

## Pré-requisitos

- Conhecimento básico de Java e Spring Boot
- Familiaridade com conceitos MCP dos módulos anteriores
- Maven ou Gradle instalados

---

## Visão geral do projeto

Este projeto é uma **aplicação mínima Spring Boot** que atua como:

* um **Servidor de Autorização Spring** (emitindo tokens JWT via o fluxo `client_credentials`), e  
* um **Servidor de Recursos** (protegendo seu próprio endpoint `/hello`).

Ele espelha a configuração mostrada no [post do blog Spring (2 de abril de 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

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

## Testando a configuração OAuth2

Você pode testar a configuração de segurança OAuth2 com os seguintes passos:

### 1. Verifique se o servidor está rodando e seguro

```bash
# Isso deve retornar 401 Unauthorized, confirmando que a segurança OAuth2 está ativa
curl -v http://localhost:8081/
```

### 2. Obtenha um token de acesso usando credenciais do cliente

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

No PowerShell, defina o segredo local antes de rodar o Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Acesse o endpoint protegido usando o token

```bash
# Usando o token salvo
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Ou diretamente com o valor do token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uma resposta bem-sucedida com "Hello from MCP OAuth2 Demo!" confirma que a configuração OAuth2 está funcionando corretamente.

---

## Construção do container

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Segurança em produção

Para um ambiente de produção, use um provedor de identidade dedicado em vez
deste servidor de autorização de demonstração em processo. Armazene as credenciais em um
cofre de segredos gerenciado, rotacione-as, use chaves de assinatura persistentes,
restrinja escopos e defina um emissor explícito. Nunca coloque o segredo do cliente no código-fonte, imagens de container, manifests de implantação ou saída de comandos.


Para Azure Container Apps, armazene o valor como um segredo do Container Apps respaldado pelo
Key Vault quando possível, depois exponha apenas uma referência secreta pela variável de ambiente
`OAUTH_CLIENT_SECRET`.

---

## Implantar no **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

O FQDN de entrada torna-se seu **emissor** (`https://<fqdn>`).  
A Azure fornece automaticamente um certificado TLS confiável para `*.azurecontainerapps.io`.

---

## Integrar ao **Azure API Management**

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

O APIM irá buscar o JWKS e validar toda requisição.

---

## Próximos passos

- [5.4 Contextos raiz](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
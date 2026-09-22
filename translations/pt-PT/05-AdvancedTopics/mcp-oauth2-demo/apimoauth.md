# Implantação da aplicação Spring AI MCP para Azure Container Apps

> [!WARNING]
> Este servidor combinado de autorização/recursos destina-se a fins de aprendizagem e
> uso de desenvolvimento/teste. Sistemas de produção devem usar um fornecedor de identidade dedicado,
> chaves de assinatura persistentes e credenciais armazenadas num cofre de segredos gerido.

 ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP protegido com Spring Authorization Server. O servidor emite tokens de acesso para clientes e valida-os nas requisições recebidas (fonte: blog Spring) ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para implantar o servidor Spring MCP, construa-o como um contentor e use Azure Container Apps com entrada externa. Por exemplo, usando a CLI do Azure pode executar:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

Isto cria uma Container App acessível publicamente com HTTPS ativado (Azure emite um certificado TLS gratuito para o domínio padrão `*.azurecontainerapps.io` ([Nomes de domínio personalizados e certificados geridos gratuitos em Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A saída do comando inclui o FQDN da app (ex.: `my-mcp-app.eastus.azurecontainerapps.io`), que passa a ser a base da **URL do emissor**. Assegure que o ingresso HTTP está ativado (como acima) para que o APIM possa aceder à app. Num ambiente de teste/desenvolvimento, use a opção `--ingress external` (ou associe um domínio personalizado com TLS conforme [docs Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nomes de domínio personalizados e certificados geridos gratuitos em Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Armazene quaisquer propriedades sensíveis (como segredos do cliente OAuth) nos segredos da Container Apps ou no Azure Key Vault, e as mapeie para o contentor como variáveis de ambiente. 

## Configurar o Spring Authorization Server

No código da sua aplicação Spring Boot, inclua os starters Spring Authorization Server e Resource Server. Configure um `RegisteredClient` (para a concessão `client_credentials` em dev/teste) e uma fonte de chave JWT. Por exemplo, em `application.properties` poderá definir:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Ative o Authorization Server e o Resource Server definindo uma cadeia de filtros de segurança. Por exemplo:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Ativar os pontos finais do Servidor de Autorização
            .apply(authzServer.and())
            // Ativar o Servidor de Recursos (validar JWT em pedidos recebidos)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Desativar CSRF (o servidor MCP não é baseado em browser)
            .csrf(csrf -> csrf.disable())
            // Permitir CORS para ferramentas de demonstração do cliente
            .cors(withDefaults());
        return http.build();
    }

    // Definir um cliente em memória (RegisteredClient) e uma fonte JWK:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Gerar uma chave RSA (para dev/teste, gerar de novo na inicialização)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Esta configuração expõe os endpoints OAuth2 por defeito: `/oauth2/token` para tokens e `/oauth2/jwks` para o Conjunto de Chaves Web JSON. (Por defeito, as `AuthorizationServerSettings` do Spring mapearão `/oauth2/token` e `/oauth2/jwks` ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) O servidor emitirá tokens de acesso JWT assinados pela chave RSA acima, e publicará a sua chave pública em `https://<sua-app>:/oauth2/jwks`. 

**Ative a descoberta OpenID Connect:** Para permitir que o APIM recupere automaticamente o emissor e JWKS, ative o endpoint de configuração do provedor OIDC adicionando `.oidc(Customizer.withDefaults())` na sua configuração de segurança ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por exemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– permite /.well-known/openid-configuration
```

Isto expõe `/.well-known/openid-configuration`, que o APIM pode usar para metadados. Finalmente, poderá querer personalizar a claim JWT **audience** para que a verificação `<audiences>` do APIM seja aprovada. Por exemplo, adicionando um personalizador de tokens:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Definir um público personalizado (por exemplo, o ID do cliente ou identificador da API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Isto assegura que os tokens contenham `"aud": ["mcp-client"]`, correspondendo ao ID do cliente ou ao escopo esperado pelo APIM. 

## Exposição dos Endpoints de Token e JWKS

Após implantar, a **URL do emissor** da sua app será `https://<app-fqdn>`, p.ex., `https://my-mcp-app.eastus.azurecontainerapps.io`. Os seus endpoints OAuth2 são:

- **Endpoint de Token:** `https://<app-fqdn>/oauth2/token` – os clientes obtêm tokens aqui (fluxo client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – devolve o conjunto JWK (usado pelo APIM para obter as chaves de assinatura).
- **Configuração OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descoberta OIDC (contém `issuer`, `token_endpoint`, `jwks_uri`, etc.).  

O APIM aponta para a **URL de configuração OpenID**, a partir da qual descobre o `jwks_uri`. Por exemplo, se o FQDN da sua Container App for `my-mcp-app.eastus.azurecontainerapps.io`, então o `<openid-config url="...">` do APIM deve usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por defeito, o Spring definirá o `issuer` nesses metadados para a mesma URL base ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurando o Azure API Management (`validate-jwt`)

No Azure APIM, adicione uma política de inbound que use a política `<validate-jwt>` para verificar os JWTs recebidos face ao seu Spring Authorization Server. Para uma configuração simples, pode usar a URL de metadados OpenID Connect. Exemplo de trecho de política:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Esta política instrui o APIM a obter a configuração OpenID do Spring Auth Server, recuperar o seu JWKS, e validar que cada token está assinado por uma chave confiável e tem a audiência correta. (Se omitir `<issuers>`, o APIM usará a claim `issuer` dos metadados automaticamente.) O `<audience>` deve corresponder ao seu ID de cliente ou identificador do recurso API no token (no exemplo acima, definimos como `"mcp-client"`). Isto é consistente com a documentação da Microsoft para uso de `validate-jwt` com `<openid-config>` ([Referência da política Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Após a validação, o APIM encaminhará a requisição (incluindo o cabeçalho `Authorization` original) para o backend. Como a app Spring é também um servidor de recursos, irá revalidar o token, mas o APIM já garantiu a sua validade. (Para desenvolvimento, pode confiar na verificação do APIM e desativar verificações adicionais na app se desejar, mas é mais seguro manter ambas.)

## Configurações de Exemplo

| Configuração       | Valor de Exemplo                                                    | Notas                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Emissor**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL da sua Container App (URI base)        |
| **Endpoint de Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Endpoint de token Spring por defeito ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Endpoint padrão do conjunto JWK ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Configuração OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descoberta OIDC (gerado automaticamente)    |
| **Audiência APIM**  | `mcp-client`                                                         | ID do cliente OAuth ou nome do recurso API       |
| **Política APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa esta URL ([Referência da política Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Armadilhas Comuns

- **HTTPS/TLS:** A gateway APIM exige que o endpoint OpenID/JWKS seja HTTPS com um certificado válido. Por defeito, o Azure Container Apps fornece um certificado TLS confiável para o domínio gerido pela Azure ([Nomes de domínio personalizados e certificados geridos gratuitos em Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se usar um domínio personalizado, assegure-se de associar um certificado (pode usar a funcionalidade de certificado gerido gratuito da Azure) ([Nomes de domínio personalizados e certificados geridos gratuitos em Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se o APIM não puder confiar no certificado do endpoint, o `<validate-jwt>` falhará ao obter os metadados.  

- **Acessibilidade do Endpoint:** Garanta que os endpoints da app Spring estão acessíveis a partir do APIM. Usar `--ingress external` (ou ativar o ingresso no portal) é o mais simples. Se escolheu um ambiente interno ou ligado a vNet, o APIM (por defeito público) poderá não conseguir alcançá-lo, a menos que estejam na mesma VNet. Num ambiente de teste, prefira ingresso público para que o APIM possa chamar as URLs `.well-known` e `/jwks`. 

- **Descoberta OpenID Ativada:** Por defeito, o Spring Authorization Server **não expõe** o `/.well-known/openid-configuration` a menos que o OIDC esteja ativado. Certifique-se de incluir `.oidc(Customizer.withDefaults())` na sua configuração de segurança (ver acima) para que o endpoint de configuração do provedor esteja ativo ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Caso contrário, a chamada `<openid-config>` do APIM retornará 404.

- **Claim Audience:** O comportamento padrão do Spring é definir a claim `aud` para o ID do cliente. Se a verificação `<audience>` do APIM falhar, poderá ser necessário personalizar o token (como mostrado acima) ou ajustar a política do APIM. Assegure que a audiência do seu JWT corresponde ao que configura em `<audience>`. 

- **Análise dos Metadados JSON:** O JSON de configuração OpenID deve ser válido. A configuração padrão do Spring emite um documento de metadados OIDC padrão. Verifique que contém o `issuer` e o `jwks_uri` corretos. Se hospedar o Spring atrás de um proxy ou numa rota baseada em caminho, confira os URLs nesses metadados. O APIM usará esses valores tal como estão. 

- **Ordem das Políticas:** Na política APIM, coloque o `<validate-jwt>` **antes** de qualquer roteamento para o backend. Caso contrário, chamadas podem alcançar a sua app sem um token válido. Também assegure que o `<validate-jwt>` aparece imediatamente dentro de `<inbound>` (não aninhado dentro de outra condição) para que o APIM o aplique corretamente.

Seguindo os passos acima, pode executar o seu servidor Spring AI MCP em Azure Container Apps e ter o Azure API Management a validar JWTs OAuth2 recebidos com uma política mínima. Os pontos chave são: expor os endpoints do Spring Auth publicamente com TLS, ativar a descoberta OIDC, e apontar o `validate-jwt` do APIM para a URL de configuração OpenID (para que possa obter o JWKS automaticamente). Esta configuração é adequada para um ambiente de desenvolvimento/teste; para produção, considere a gestão adequada de segredos, tempos de vida dos tokens, e rotatividade de chaves no JWKS conforme necessário. 


**Referências:** Consulte a documentação do Spring Authorization Server para os endpoints padrão ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e configuração OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulte a documentação Microsoft APIM para exemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e a documentação do Azure Container Apps para implantação e certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Implantação da aplicação Spring AI MCP no Azure Container Apps

 ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP protegido com Spring Authorization Server. O servidor emite tokens de acesso para os clientes e valida-os nas requisições recebidas (fonte: blog Spring) ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para implantar o servidor Spring MCP, construa-o como um container e utilize o Azure Container Apps com ingresso externo. Por exemplo, usando o Azure CLI pode executar:

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

Isto cria uma Container App acessível publicamente com HTTPS ativado (a Azure emite um certificado TLS gratuito para o domínio padrão `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A saída do comando inclui o FQDN da app (ex.: `my-mcp-app.eastus.azurecontainerapps.io`), que se torna a base da **URL do emissor**. Certifique-se de que o ingresso HTTP está ativado (como acima) para que o APIM consiga aceder à app. Num ambiente de teste/desenvolvimento, use a opção `--ingress external` (ou associe um domínio personalizado com TLS conforme [documentação Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Armazene quaisquer propriedades sensíveis (como segredos de clientes OAuth) nos segredos do Container Apps ou no Azure Key Vault, e mapeie-os para o container como variáveis de ambiente.

## Configuração do Spring Authorization Server

No código da sua aplicação Spring Boot, inclua os starters do Spring Authorization Server e Resource Server. Configure um `RegisteredClient` (para o grant `client_credentials` em dev/teste) e uma fonte de chave JWT. Por exemplo, em `application.properties` pode definir:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
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
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Esta configuração expõe os endpoints OAuth2 padrão: `/oauth2/token` para tokens e `/oauth2/jwks` para o JSON Web Key Set. (Por padrão, o `AuthorizationServerSettings` do Spring mapeia `/oauth2/token` e `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) O servidor emitirá tokens de acesso JWT assinados pela chave RSA acima, e publicará a sua chave pública em `https://<your-app>:/oauth2/jwks`.

**Ativar descoberta OpenID Connect:** Para permitir que o APIM recupere automaticamente o emissor e o JWKS, ative o endpoint de configuração do provedor OIDC adicionando `.oidc(Customizer.withDefaults())` na sua configuração de segurança ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por exemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Isto expõe `/.well-known/openid-configuration`, que o APIM pode usar para obter metadados. Por fim, poderá querer personalizar a claim **audience** do JWT para que a verificação `<audiences>` do APIM seja bem-sucedida. Por exemplo, adicione um customizador de token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Isto garante que os tokens contenham `"aud": ["mcp-client"]`, correspondendo ao ID do cliente ou ao scope esperado pelo APIM.

## Exposição dos endpoints Token e JWKS

Após a implantação, a **URL do emissor** da sua app será `https://<app-fqdn>`, por exemplo `https://my-mcp-app.eastus.azurecontainerapps.io`. Os seus endpoints OAuth2 são:

- **Endpoint de token:** `https://<app-fqdn>/oauth2/token` – onde os clientes obtêm tokens (fluxo client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – devolve o conjunto JWK (usado pelo APIM para obter as chaves de assinatura).
- **Configuração OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descoberta OIDC (contém `issuer`, `token_endpoint`, `jwks_uri`, etc.).

O APIM apontará para a **URL de configuração OpenID**, de onde descobre o `jwks_uri`. Por exemplo, se o FQDN da sua Container App for `my-mcp-app.eastus.azurecontainerapps.io`, então o `<openid-config url="...">` do APIM deve usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por padrão, o Spring define o `issuer` nesses metadados para a mesma URL base ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configuração do Azure API Management (`validate-jwt`)

No Azure APIM, adicione uma política inbound que utilize a política `<validate-jwt>` para validar os JWTs recebidos contra o seu Spring Authorization Server. Para uma configuração simples, pode usar a URL de metadados OpenID Connect. Exemplo de trecho de política:

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

Esta política instrui o APIM a buscar a configuração OpenID do Spring Auth Server, obter o seu JWKS e validar que cada token está assinado por uma chave confiável e tem a audiência correta. (Se omitir `<issuers>`, o APIM usará automaticamente a claim `issuer` dos metadados.) O `<audience>` deve corresponder ao ID do cliente ou identificador do recurso API no token (no exemplo acima, definimos como `"mcp-client"`). Isto está em conformidade com a documentação da Microsoft sobre o uso de `validate-jwt` com `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Após a validação, o APIM encaminhará a requisição (incluindo o cabeçalho `Authorization` original) para o backend. Como a app Spring é também um resource server, ela revalidará o token, mas o APIM já garantiu a sua validade. (Para desenvolvimento, pode confiar na validação do APIM e desativar verificações adicionais na app, se desejar, mas é mais seguro manter ambas.)

## Exemplo de configurações

| Configuração       | Valor de Exemplo                                                   | Notas                                      |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL da sua Container App (URI base)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Endpoint padrão de token do Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Endpoint padrão do JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descoberta OIDC (gerado automaticamente)    |
| **APIM audience**  | `mcp-client`                                                      | ID do cliente OAuth ou nome do recurso API |
| **Política APIM**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa esta URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Armadilhas comuns

- **HTTPS/TLS:** O gateway APIM exige que o endpoint OpenID/JWKS seja HTTPS com um certificado válido. Por padrão, o Azure Container Apps fornece um certificado TLS confiável para o domínio gerido pela Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se usar um domínio personalizado, certifique-se de associar um certificado (pode usar o recurso de certificado gerido gratuito da Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se o APIM não confiar no certificado do endpoint, o `<validate-jwt>` falhará ao buscar os metadados.

- **Acessibilidade dos endpoints:** Garanta que os endpoints da app Spring são acessíveis a partir do APIM. Usar `--ingress external` (ou ativar o ingresso no portal) é o mais simples. Se escolheu um ambiente interno ou ligado a vNet, o APIM (por padrão público) pode não conseguir aceder, a menos que esteja na mesma vNet. Num ambiente de teste, prefira ingresso público para que o APIM possa chamar as URLs `.well-known` e `/jwks`.

- **Descoberta OpenID ativada:** Por padrão, o Spring Authorization Server **não expõe** `/.well-known/openid-configuration` a menos que o OIDC esteja ativado. Certifique-se de incluir `.oidc(Customizer.withDefaults())` na sua configuração de segurança (veja acima) para que o endpoint de configuração do provedor esteja ativo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Caso contrário, a chamada `<openid-config>` do APIM retornará 404.

- **Claim Audience:** O comportamento padrão do Spring é definir a claim `aud` para o ID do cliente. Se a verificação `<audience>` do APIM falhar, poderá precisar personalizar o token (como mostrado acima) ou ajustar a política do APIM. Certifique-se de que a audiência no seu JWT corresponde ao que configurou em `<audience>`.

- **Parsing dos metadados JSON:** O JSON da configuração OpenID deve ser válido. A configuração padrão do Spring emitirá um documento padrão de metadados OIDC. Verifique que contém o `issuer` e o `jwks_uri` corretos. Se hospedar o Spring atrás de um proxy ou rota baseada em caminho, verifique cuidadosamente as URLs nestes metadados. O APIM usará estes valores tal como estão.

- **Ordem das políticas:** Na política do APIM, coloque `<validate-jwt>` **antes** de qualquer roteamento para o backend. Caso contrário, as chamadas podem chegar à sua app sem um token válido. Também garanta que `<validate-jwt>` aparece imediatamente dentro de `<inbound>` (não aninhado dentro de outra condição) para que o APIM o aplique.

Seguindo os passos acima, pode executar o seu servidor Spring AI MCP no Azure Container Apps e fazer com que o Azure API Management valide os JWTs OAuth2 recebidos com uma política mínima. Os pontos-chave são: expor os endpoints Spring Auth publicamente com TLS, ativar a descoberta OIDC e apontar o `validate-jwt` do APIM para a URL de configuração OpenID (para que possa buscar o JWKS automaticamente). Esta configuração é adequada para ambientes de desenvolvimento/teste; para produção, considere a gestão adequada de segredos, tempos de vida dos tokens e rotação de chaves no JWKS conforme necessário.
**Referências:** Consulte a documentação do Spring Authorization Server para os endpoints padrão ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e a configuração OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulte a documentação da Microsoft APIM para exemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e a documentação do Azure Container Apps para deployment e certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
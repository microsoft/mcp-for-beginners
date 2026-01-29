# Implantando o aplicativo Spring AI MCP no Azure Container Apps

([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP protegido com Spring Authorization Server. O servidor emite tokens de acesso para os clientes e os valida nas requisições recebidas (fonte: blog Spring) ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para implantar o servidor Spring MCP, construa-o como um container e use o Azure Container Apps com ingresso externo. Por exemplo, usando o Azure CLI, você pode executar:

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

Isso cria um Container App acessível publicamente com HTTPS habilitado (o Azure emite um certificado TLS gratuito para o domínio padrão `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A saída do comando inclui o FQDN do app (ex: `my-mcp-app.eastus.azurecontainerapps.io`), que se torna a base da **URL do emissor**. Certifique-se de que o ingresso HTTP esteja habilitado (como acima) para que o APIM possa acessar o app. Em um ambiente de teste/desenvolvimento, use a opção `--ingress external` (ou vincule um domínio personalizado com TLS conforme [documentação Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Armazene quaisquer propriedades sensíveis (como segredos de cliente OAuth) nos segredos do Container Apps ou no Azure Key Vault, e mapeie-os para o container como variáveis de ambiente.

## Configurando o Spring Authorization Server

No código do seu app Spring Boot, inclua os starters do Spring Authorization Server e Resource Server. Configure um `RegisteredClient` (para o grant `client_credentials` em dev/test) e uma fonte de chave JWT. Por exemplo, em `application.properties` você pode definir:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Habilite o Authorization Server e o Resource Server definindo uma cadeia de filtros de segurança. Por exemplo:

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

Essa configuração expõe os endpoints OAuth2 padrão: `/oauth2/token` para tokens e `/oauth2/jwks` para o JSON Web Key Set. (Por padrão, o `AuthorizationServerSettings` do Spring mapeia `/oauth2/token` e `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) O servidor emitirá tokens JWT assinados pela chave RSA acima e publicará sua chave pública em `https://<seu-app>:/oauth2/jwks`.

**Habilite a descoberta OpenID Connect:** Para que o APIM recupere automaticamente o emissor e o JWKS, habilite o endpoint de configuração do provedor OIDC adicionando `.oidc(Customizer.withDefaults())` na sua configuração de segurança ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por exemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Isso expõe `/.well-known/openid-configuration`, que o APIM pode usar para metadados. Por fim, você pode querer personalizar a claim **audience** do JWT para que a verificação `<audiences>` do APIM seja aprovada. Por exemplo, adicione um customizador de token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Isso garante que os tokens carreguem `"aud": ["mcp-client"]`, correspondendo ao client ID ou escopo esperado pelo APIM.

## Expondo os endpoints de Token e JWKS

Após a implantação, a **URL do emissor** do seu app será `https://<app-fqdn>`, ex: `https://my-mcp-app.eastus.azurecontainerapps.io`. Seus endpoints OAuth2 são:

- **Endpoint de token:** `https://<app-fqdn>/oauth2/token` – onde os clientes obtêm tokens (fluxo client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – retorna o conjunto JWK (usado pelo APIM para obter as chaves de assinatura).
- **Configuração OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descoberta OIDC (contém `issuer`, `token_endpoint`, `jwks_uri`, etc.).

O APIM apontará para a **URL de configuração OpenID**, de onde descobrirá o `jwks_uri`. Por exemplo, se o FQDN do seu Container App for `my-mcp-app.eastus.azurecontainerapps.io`, então o `<openid-config url="...">` do APIM deve usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por padrão, o Spring define o `issuer` nesses metadados para a mesma URL base ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurando o Azure API Management (`validate-jwt`)

No Azure APIM, adicione uma política de entrada que use a política `<validate-jwt>` para validar os JWTs recebidos contra seu Spring Authorization Server. Para uma configuração simples, você pode usar a URL de metadados OpenID Connect. Exemplo de trecho de política:

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

Essa política instrui o APIM a buscar a configuração OpenID do Spring Auth Server, recuperar seu JWKS e validar que cada token foi assinado por uma chave confiável e possui a audiência correta. (Se você omitir `<issuers>`, o APIM usará automaticamente a claim `issuer` dos metadados.) O `<audience>` deve corresponder ao seu client ID ou identificador do recurso API no token (no exemplo acima, definimos como `"mcp-client"`). Isso está alinhado com a documentação da Microsoft sobre o uso de `validate-jwt` com `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Após a validação, o APIM encaminhará a requisição (incluindo o cabeçalho `Authorization` original) para o backend. Como o app Spring também é um resource server, ele revalidará o token, mas o APIM já garantiu sua validade. (Para desenvolvimento, você pode confiar na verificação do APIM e desabilitar verificações adicionais no app, se desejar, mas é mais seguro manter ambos.)

## Configurações de exemplo

| Configuração       | Valor de Exemplo                                                   | Observações                                |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL do seu Container App (URI base)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Endpoint padrão de token do Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Endpoint padrão do JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descoberta OIDC (gerado automaticamente)    |
| **APIM audience**  | `mcp-client`                                                      | Client ID OAuth ou nome do recurso da API  |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa essa URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Armadilhas comuns

- **HTTPS/TLS:** O gateway APIM exige que o endpoint OpenID/JWKS seja HTTPS com certificado válido. Por padrão, o Azure Container Apps fornece um certificado TLS confiável para o domínio gerenciado pelo Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se você usar um domínio personalizado, certifique-se de vincular um certificado (pode usar o recurso de certificado gerenciado gratuito do Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se o APIM não confiar no certificado do endpoint, o `<validate-jwt>` falhará ao buscar os metadados.

- **Acessibilidade do Endpoint:** Garanta que os endpoints do app Spring estejam acessíveis pelo APIM. Usar `--ingress external` (ou habilitar ingresso no portal) é o mais simples. Se você escolheu um ambiente interno ou vinculado a vNet, o APIM (que é público por padrão) pode não conseguir acessá-lo, a menos que esteja na mesma VNet. Em um ambiente de teste, prefira ingresso público para que o APIM possa chamar as URLs `.well-known` e `/jwks`.

- **Descoberta OpenID habilitada:** Por padrão, o Spring Authorization Server **não expõe** `/.well-known/openid-configuration` a menos que o OIDC esteja habilitado. Certifique-se de incluir `.oidc(Customizer.withDefaults())` na sua configuração de segurança (veja acima) para ativar o endpoint de configuração do provedor ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Caso contrário, a chamada `<openid-config>` do APIM retornará 404.

- **Claim Audience:** O comportamento padrão do Spring é definir a claim `aud` como o client ID. Se a verificação `<audience>` do APIM falhar, pode ser necessário personalizar o token (como mostrado acima) ou ajustar a política do APIM. Garanta que a audiência no seu JWT corresponda ao que você configurou em `<audience>`.

- **Parsing dos Metadados JSON:** O JSON de configuração OpenID deve ser válido. A configuração padrão do Spring emitirá um documento padrão de metadados OIDC. Verifique se contém o `issuer` e o `jwks_uri` corretos. Se você hospedar o Spring atrás de um proxy ou rota baseada em caminho, confira os URLs nesses metadados. O APIM usará esses valores como estão.

- **Ordem da Política:** Na política do APIM, coloque `<validate-jwt>` **antes** de qualquer roteamento para o backend. Caso contrário, as chamadas podem chegar ao seu app sem um token válido. Também garanta que `<validate-jwt>` apareça imediatamente dentro de `<inbound>` (não aninhado dentro de outra condição) para que o APIM o aplique.

Seguindo os passos acima, você pode executar seu servidor Spring AI MCP no Azure Container Apps e fazer com que o Azure API Management valide os JWTs OAuth2 recebidos com uma política mínima. Os pontos principais são: expor os endpoints Spring Auth publicamente com TLS, habilitar a descoberta OIDC e apontar o `validate-jwt` do APIM para a URL de configuração OpenID (para que ele possa buscar o JWKS automaticamente). Essa configuração é adequada para ambientes de dev/test; para produção, considere o gerenciamento adequado de segredos, tempo de vida dos tokens e rotação de chaves no JWKS conforme necessário.
**Referências:** Veja a documentação do Spring Authorization Server para os endpoints padrão ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e a configuração OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulte a documentação do Microsoft APIM para exemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e a documentação do Azure Container Apps para implantação e certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
# Implantando o Aplicativo Spring AI MCP no Azure Container Apps

> [!WARNING]
> Este servidor combinado de autorização/recursos é destinado para uso de aprendizado e
> desenvolvimento/teste. Sistemas de produção devem usar um provedor de identidade dedicado,
> chaves de assinatura persistentes e credenciais armazenadas em um cofre de segredos gerenciado.

 ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP protegido com Spring Authorization Server. O servidor emite tokens de acesso para clientes e os valida nas requisições recebidas (fonte: blog Spring) ([Protegendo servidores Spring AI MCP com OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para implantar o servidor Spring MCP, construa-o como um contêiner e use o Azure Container Apps com ingresso externo. Por exemplo, usando o Azure CLI você pode executar:

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

Isso cria um Container App acessível publicamente com HTTPS habilitado (a Azure emite um certificado TLS gratuito para o domínio padrão `*.azurecontainerapps.io` ([Nomes de domínio personalizados e certificados gerenciados gratuitos no Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). A saída do comando inclui o FQDN do app (ex.: `my-mcp-app.eastus.azurecontainerapps.io`), que se torna a base da **URL do emissor**. Certifique-se de que o ingresso HTTP está habilitado (como acima) para que o APIM possa alcançar o app. Em uma configuração de teste/desenvolvimento, use a opção `--ingress external` (ou vincule um domínio personalizado com TLS conforme [docs Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nomes de domínio personalizados e certificados gerenciados gratuitos no Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Armazene quaisquer propriedades sensíveis (como segredos de cliente OAuth) nos segredos do Container Apps ou no Azure Key Vault, e mapeie-os dentro do contêiner como variáveis de ambiente.

## Configurando o Spring Authorization Server

No código do seu aplicativo Spring Boot, inclua os starters Spring Authorization Server e Resource Server. Configure um `RegisteredClient` (para a concessão `client_credentials` em dev/test) e uma fonte de chave JWT. Por exemplo, em `application.properties` você pode definir:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Habilite o Authorization Server e Resource Server definindo uma cadeia de filtro de segurança. Por exemplo:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Habilitar os endpoints do Servidor de Autorização
            .apply(authzServer.and())
            // Habilitar o Servidor de Recursos (validar JWT nas requisições recebidas)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Desabilitar CSRF (servidor MCP não é baseado em navegador)
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
        // Gerar uma chave RSA (para desenvolvimento/teste, gerar novamente na inicialização)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Essa configuração exporá os endpoints OAuth2 padrão: `/oauth2/token` para tokens e `/oauth2/jwks` para o JSON Web Key Set. (Por padrão, o `AuthorizationServerSettings` do Spring mapeia `/oauth2/token` e `/oauth2/jwks` ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) O servidor emitirá tokens de acesso JWT assinados pela chave RSA acima, e publicará sua chave pública em `https://<seu-app>:/oauth2/jwks`.

**Habilite a descoberta OpenID Connect:** Para permitir que o APIM recupere automaticamente o emissor e JWKS, habilite o endpoint de configuração do provedor OIDC adicionando `.oidc(Customizer.withDefaults())` na sua configuração de segurança ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por exemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– habilita /.well-known/openid-configuration
```

Isso expõe `/.well-known/openid-configuration`, que o APIM pode usar para metadados. Por fim, você pode querer personalizar a reivindicação **audience** do JWT para que a verificação `<audiences>` do APIM passe. Por exemplo, adicione um customizador de token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Defina um público personalizado (por exemplo, o ID do cliente ou identificador da API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Isso garante que os tokens carreguem `"aud": ["mcp-client"]`, correspondendo ao ID do cliente ou escopo esperado pelo APIM.

## Expondo Endpoints de Token e JWKS

Após a implantação, a **URL do emissor** do seu app será `https://<app-fqdn>`, por exemplo `https://my-mcp-app.eastus.azurecontainerapps.io`. Seus endpoints OAuth2 são:

- **Endpoint de token:** `https://<app-fqdn>/oauth2/token` – onde os clientes obtêm tokens (fluxo client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – retorna o conjunto JWK (usado pelo APIM para obter as chaves de assinatura).
- **Configuração OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descoberta OIDC (contém `issuer`, `token_endpoint`, `jwks_uri`, etc.).

O APIM usará a **URL da configuração OpenID**, da qual descobrirá o `jwks_uri`. Por exemplo, se o FQDN do seu Container App for `my-mcp-app.eastus.azurecontainerapps.io`, então o `<openid-config url="...">` do APIM deve usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por padrão, o Spring define o `issuer` nessa metadata para o mesmo URL base ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurando o Azure API Management (`validate-jwt`)

No Azure APIM, adicione uma política de entrada que utilize a política `<validate-jwt>` para verificar os JWTs recebidos contra seu Spring Authorization Server. Para uma configuração simples, você pode usar a URL de metadados OpenID Connect. Exemplo de snippet de política:

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

Essa política instrui o APIM a buscar a configuração OpenID do Spring Auth Server, recuperar seu JWKS e validar se cada token está assinado por uma chave confiável e tem a audiência correta. (Se você omitir `<issuers>`, o APIM usará automaticamente a reivindicação `issuer` da metadata.) O `<audience>` deve corresponder ao ID do cliente ou identificador do recurso API no token (no exemplo acima, definimos como `"mcp-client"`). Isso é consistente com a documentação da Microsoft sobre o uso de `validate-jwt` com `<openid-config>` ([Referência de política do Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Após a validação, o APIM encaminhará a requisição (incluindo o cabeçalho original `Authorization`) ao backend. Como o app Spring também é um Resource Server, ele revalidará o token, mas o APIM já garantiu sua validade. (Para desenvolvimento, você pode confiar na verificação do APIM e desabilitar verificações adicionais no app se desejar, mas é mais seguro manter ambas.)

## Configurações de Exemplo

| Configuração       | Valor de Exemplo                                                    | Notas                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Emissor**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | URL do seu Container App (URI base)        |
| **Endpoint de token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | Endpoint de token padrão do Spring ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | Endpoint padrão do conjunto JWK ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Configuração OpenID** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descoberta OIDC (auto-gerado)  |
| **Audiência APIM** | `mcp-client`                                                        | ID do cliente OAuth ou nome do recurso API |
| **Política APIM**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa essa URL ([Referência de política do Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Armadilhas Comuns

- **HTTPS/TLS:** O gateway APIM requer que o endpoint OpenID/JWKS seja HTTPS com certificado válido. Por padrão, o Azure Container Apps fornece um certificado TLS confiável para o domínio gerenciado pela Azure ([Nomes de domínio personalizados e certificados gerenciados gratuitos no Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se você usar um domínio personalizado, certifique-se de vincular um certificado (você pode usar o recurso de certificado gerenciado gratuito da Azure) ([Nomes de domínio personalizados e certificados gerenciados gratuitos no Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Se o APIM não puder confiar no certificado do endpoint, o `<validate-jwt>` falhará ao buscar os metadados.

- **Acessibilidade do Endpoint:** Certifique-se de que os endpoints do app Spring estejam acessíveis pelo APIM. Usar `--ingress external` (ou habilitar ingresso no portal) é o mais simples. Se você escolheu um ambiente interno ou vinculado a vNet, o APIM (por padrão público) pode não alcançá-lo a menos que esteja na mesma VNet. Em um ambiente de teste, prefira ingresso público para que o APIM possa chamar as URLs `.well-known` e `/jwks`.

- **Descoberta OpenID Habilitada:** Por padrão, o Spring Authorization Server **não expõe** `/.well-known/openid-configuration` a menos que o OIDC esteja habilitado. Certifique-se de incluir `.oidc(Customizer.withDefaults())` na sua configuração de segurança (veja acima) para que o endpoint de configuração do provedor esteja ativo ([Modelo de Configuração :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Caso contrário, a chamada `<openid-config>` do APIM retornará 404.

- **Reivindicação Audience:** O comportamento padrão do Spring é definir a reivindicação `aud` para o ID do cliente. Se a verificação `<audience>` do APIM falhar, você pode precisar personalizar o token (como mostrado acima) ou ajustar a política do APIM. Certifique-se de que a audiência no seu JWT corresponda ao que você configurou em `<audience>`.

- **Parseamento de Metadados JSON:** O JSON da configuração OpenID deve ser válido. A configuração padrão do Spring emitirá um documento de metadados OIDC padrão. Verifique se ele contém o `issuer` e `jwks_uri` corretos. Se você hospeda o Spring atrás de um proxy ou rota baseada em caminho, confira os URLs nesses metadados. O APIM usará esses valores como estão.

- **Ordem das Políticas:** Na política do APIM, coloque `<validate-jwt>` **antes** de qualquer roteamento para o backend. Caso contrário, chamadas podem alcançar seu app sem um token válido. Também garanta que `<validate-jwt>` apareça logo sob `<inbound>` (não aninhado dentro de outra condição) para que o APIM o aplique.

Seguindo os passos acima, você pode rodar seu servidor Spring AI MCP no Azure Container Apps e fazer o Azure API Management validar os JWTs OAuth2 recebidos com uma política mínima. Os pontos chave são: expor os endpoints Spring Auth publicamente com TLS, habilitar a descoberta OIDC, e apontar o `validate-jwt` do APIM para a URL da configuração OpenID (para que ele busque o JWKS automaticamente). Esta configuração é adequada para ambiente de dev/test; para produção, considere gerenciamento apropriado de segredos, tempos de vida de tokens e rotação de chaves no JWKS conforme necessário.


**Referências:** Veja a documentação do Spring Authorization Server para endpoints padrão ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) e configuração OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); veja a documentação da Microsoft APIM para exemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); e a documentação do Azure Container Apps para implantação e certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
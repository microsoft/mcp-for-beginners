# Spring AI MCPアプリをAzure Container Appsにデプロイする

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *図：Spring Authorization Serverで保護されたSpring AI MCPサーバー。サーバーはクライアントにアクセストークンを発行し、受信リクエストでそれを検証します（出典：Springブログ）([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCPサーバーをデプロイするには、コンテナとしてビルドし、外部イングレス付きのAzure Container Appsを使用します。例えば、Azure CLIを使って以下のコマンドを実行できます：

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

これにより、HTTPSが有効なパブリックにアクセス可能なContainer Appが作成されます（Azureはデフォルトの`*.azurecontainerapps.io`ドメインに対して無料のTLS証明書を発行します（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)））。コマンドの出力にはアプリのFQDN（例：`my-mcp-app.eastus.azurecontainerapps.io`）が含まれ、これが**issuer URL**のベースとなります。APIMがアプリにアクセスできるようにHTTPイングレスが有効になっていることを確認してください（上記のように）。テストや開発環境では、`--ingress external`オプションを使用するか、[Microsoftのドキュメント](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates)に従ってTLS付きのカスタムドメインをバインドしてください（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。OAuthクライアントシークレットなどの機密情報はContainer AppsのシークレットやAzure Key Vaultに保存し、環境変数としてコンテナにマッピングしてください。

## Spring Authorization Serverの設定

Spring BootアプリのコードにSpring Authorization ServerとResource Serverのスターターを含めます。`RegisteredClient`（開発/テスト環境での`client_credentials`グラント用）とJWTキーソースを設定します。例えば、`application.properties`に以下を設定することがあります：

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

セキュリティフィルタチェーンを定義してAuthorization ServerとResource Serverを有効にします。例：

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

この設定により、デフォルトのOAuth2エンドポイントが公開されます：トークン用の`/oauth2/token`とJSON Web Key Set用の`/oauth2/jwks`です。（デフォルトでSpringの`AuthorizationServerSettings`は`/oauth2/token`と`/oauth2/jwks`をマッピングします（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）。）サーバーは上記のRSAキーで署名されたJWTアクセストークンを発行し、公開鍵を`https://<your-app>:/oauth2/jwks`で公開します。

**OpenID Connectディスカバリーを有効にする：** APIMがissuerとJWKSを自動取得できるように、セキュリティ設定に`.oidc(Customizer.withDefaults())`を追加してOIDCプロバイダー設定エンドポイントを有効にします（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）。例：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

これにより`/.well-known/openid-configuration`が公開され、APIMはこれをメタデータ取得に利用できます。最後に、JWTの**audience**クレームをカスタマイズしてAPIMの`<audiences>`チェックを通過させることも検討してください。例えば、トークンカスタマイザーを追加します：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

これにより、トークンに`"aud": ["mcp-client"]`が含まれ、APIMが期待するクライアントIDやスコープと一致します。

## トークンおよびJWKSエンドポイントの公開

デプロイ後、アプリの**issuer URL**は`https://<app-fqdn>`（例：`https://my-mcp-app.eastus.azurecontainerapps.io`）となります。OAuth2エンドポイントは以下の通りです：

- **トークンエンドポイント:** `https://<app-fqdn>/oauth2/token` – クライアントがトークンを取得する場所（client_credentialsフロー）。
- **JWKSエンドポイント:** `https://<app-fqdn>/oauth2/jwks` – JWKセットを返す（APIMが署名鍵を取得するために使用）。
- **OpenID設定:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDCディスカバリー用JSON（`issuer`、`token_endpoint`、`jwks_uri`などを含む）。

APIMは**OpenID設定URL**を参照し、そこから`jwks_uri`を検出します。例えば、Container AppのFQDNが`my-mcp-app.eastus.azurecontainerapps.io`の場合、APIMの`<openid-config url="...">`は`https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`を使用します。（デフォルトでSpringはメタデータ内の`issuer`を同じベースURLに設定します（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）。）

## Azure API Managementの設定（`validate-jwt`）

Azure APIMで、Spring Authorization ServerのJWTを検証するために`<validate-jwt>`ポリシーを使ったインバウンドポリシーを追加します。シンプルな設定ではOpenID ConnectメタデータURLを利用できます。ポリシー例：

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

このポリシーはAPIMにSpring Auth ServerからOpenID設定を取得させ、JWKSを取得し、各トークンが信頼できる鍵で署名されているか、audienceが正しいかを検証させます。（`<issuers>`を省略すると、APIMはメタデータの`issuer`クレームを自動的に使用します。）`<audience>`はトークン内のクライアントIDやAPIリソース識別子と一致させてください（上記例では`"mcp-client"`に設定）。これはMicrosoftの`validate-jwt`と`<openid-config>`の使用に関するドキュメントと整合しています（[Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)）。

検証後、APIMはリクエスト（元の`Authorization`ヘッダーを含む）をバックエンドに転送します。Springアプリもリソースサーバーなのでトークンを再検証しますが、APIMが既に有効性を保証しています。（開発時はAPIMの検証に依存し、アプリ側の追加検証を無効にすることも可能ですが、両方有効にしておく方が安全です。）

## 設定例

| 設定項目           | 例値                                                                 | 備考                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Container AppのURL（ベースURI）             |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | デフォルトのSpringトークンエンドポイント（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)） |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | デフォルトのJWKセットエンドポイント（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)） |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDCディスカバリードキュメント（自動生成） |
| **APIM audience**  | `mcp-client`                                                         | OAuthクライアントIDまたはAPIリソース名     |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>`で使用するURL（[Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)） |

## よくある落とし穴

- **HTTPS/TLS:** APIMゲートウェイはOpenID/JWKSエンドポイントが有効な証明書付きのHTTPSであることを要求します。デフォルトでAzure Container AppsはAzure管理ドメインに対して信頼されたTLS証明書を提供します（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。カスタムドメインを使う場合は証明書をバインドしてください（Azureの無料管理証明書機能を利用可能）（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。APIMがエンドポイントの証明書を信頼できない場合、`<validate-jwt>`はメタデータの取得に失敗します。

- **エンドポイントのアクセス可能性:** SpringアプリのエンドポイントがAPIMからアクセス可能であることを確認してください。`--ingress external`を使うか、ポータルでイングレスを有効にするのが最も簡単です。内部またはvNetバウンド環境を選択した場合、APIM（デフォルトはパブリック）が同じVNet内にないとアクセスできない可能性があります。テスト環境ではパブリックイングレスを推奨し、APIMが`.well-known`や`/jwks`のURLにアクセスできるようにしてください。

- **OpenIDディスカバリーの有効化:** デフォルトでSpring Authorization ServerはOIDCを有効にしない限り`/.well-known/openid-configuration`を公開しません。セキュリティ設定に`.oidc(Customizer.withDefaults())`を含めてプロバイダー設定エンドポイントを有効にしてください（上記参照）。これをしないとAPIMの`<openid-config>`呼び出しは404になります。

- **Audienceクレーム:** Springのデフォルト動作では`aud`クレームはクライアントIDに設定されます。APIMの`<audience>`チェックが失敗する場合は、トークンカスタマイズ（上記参照）やAPIMポリシーの調整が必要です。JWT内のaudienceが`<audience>`設定と一致していることを確認してください。

- **JSONメタデータの解析:** OpenID設定JSONは有効な形式である必要があります。Springのデフォルト設定は標準的なOIDCメタデータドキュメントを出力します。`issuer`や`jwks_uri`が正しいか確認してください。Springをプロキシやパスベースのルーティングの背後でホストしている場合は、このメタデータ内のURLを再確認してください。APIMはこれらの値をそのまま使用します。

- **ポリシーの順序:** APIMポリシーでは、`<validate-jwt>`をバックエンドへのルーティングより**前**に配置してください。そうしないと有効なトークンなしでアプリにリクエストが届く可能性があります。また、`<validate-jwt>`は`<inbound>`直下に置き、他の条件の内側にネストしないようにしてください。これによりAPIMが確実に適用します。

以上の手順に従うことで、Spring AI MCPサーバーをAzure Container Apps上で稼働させ、Azure API ManagementでOAuth2 JWTの検証を最小限のポリシーで実現できます。ポイントは、Spring AuthエンドポイントをTLS付きで公開し、OIDCディスカバリーを有効にし、APIMの`validate-jwt`をOpenID設定URLに向けてJWKSを自動取得させることです。この構成は開発/テスト環境に適しており、本番環境では適切なシークレット管理、トークンの有効期限、JWKSのキーのローテーションなどを検討してください。
**References:** Spring Authorization Serverのドキュメントでデフォルトのエンドポイントを確認してください（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）およびOIDC設定（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）；Microsoft APIMのドキュメントで`validate-jwt`の例を参照してください（[Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)）；およびAzure Container Appsのドキュメントでデプロイと証明書について確認してください（[Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)）（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
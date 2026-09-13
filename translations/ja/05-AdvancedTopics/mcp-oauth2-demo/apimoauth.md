# Spring AI MCP アプリを Azure Container Apps にデプロイする

> [!WARNING]
> この結合された認可/リソースサーバーは学習および開発/テスト用途を目的としています。 
> 本番システムでは専用のアイデンティティプロバイダー、永続的なサインキー、および管理されたシークレットストアに格納された資格情報を使用してください。




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

これにより、HTTPS が有効なパブリックにアクセス可能なコンテナ アプリが作成されます（Azure はデフォルトの `*.azurecontainerapps.io` ドメインに無料の TLS 証明書を発行します ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). コマンド出力にはアプリのFQDN（例：`my-mcp-app.eastus.azurecontainerapps.io`）が含まれ、これが<strong>issuer URL</strong> のベースになります。APIM からアプリに接続できるように HTTP イングレスが有効であることを確認してください（上記のとおり）。テスト/開発環境では `--ingress external` オプションを使用するか、[Microsoftドキュメント](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates)に従いカスタムドメインを TLS でバインドします（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。OAuth クライアントシークレットなどの機密情報は、Container Apps シークレットまたは Azure Key Vault に保存し、環境変数としてコンテナにマッピングしてください。

## Spring Authorization Server の設定

Spring Boot アプリのコードに Spring Authorization Server と Resource Server のスターターを含めます。`RegisteredClient`（開発/テスト用に `client_credentials` グラント）と JWT キーソースを設定します。たとえば、`application.properties` に次を設定します:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

セキュリティフィルターチェーンを定義して Authorization Server と Resource Server を有効化します。例：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // 認可サーバーのエンドポイントを有効にする
            .apply(authzServer.and())
            // リソースサーバーを有効にする（受信リクエストでJWTを検証）
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRFを無効化する（MCPサーバーはブラウザベースではない）
            .csrf(csrf -> csrf.disable())
            // クライアントデモツールのためにCORSを許可する
            .cors(withDefaults());
        return http.build();
    }

    // インメモリクライアント（RegisteredClient）およびJWKソースを定義する
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
        // RSAキーを生成する（開発／テスト用で、起動時に新規生成）
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

これによりデフォルトの OAuth2 エンドポイント `/oauth2/token`（トークン発行）と `/oauth2/jwks`（JSON Web Key Set）が公開されます。（Spring のデフォルトの `AuthorizationServerSettings` は `/oauth2/token` と `/oauth2/jwks` にマッピングします ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）サーバーは上記のRSAキーで署名されたJWTアクセストークンを発行し、その公開キーを `https://<your-app>:/oauth2/jwks` で公開します。

**OpenID Connect 発見を有効にする:** APIM が発行者と JWKS を自動取得できるよう、セキュリティ設定に `.oidc(Customizer.withDefaults())` を追加して OIDC プロバイダー設定エンドポイントを有効にします ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。例：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration を有効にします
```

これにより `/.well-known/openid-configuration` が公開され、APIM がメタデータに利用できます。最後に、JWT の **audience** クレームをカスタマイズして APIM の `<audiences>` チェックに合格させることもできます。例として、トークンカスタマイザを追加します：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // カスタムオーディエンスを設定します（例：クライアントIDまたはAPI識別子）
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

これによりトークンは `"aud": ["mcp-client"]` を含み、APIM が期待するクライアントIDまたはスコープに合致します。

## トークンおよび JWKS エンドポイントの公開

デプロイ後、アプリの<strong>issuer URL</strong> は `https://<app-fqdn>` となります（例：`https://my-mcp-app.eastus.azurecontainerapps.io`）。OAuth2 エンドポイントは以下です:

- **トークンエンドポイント:** `https://<app-fqdn>/oauth2/token` – クライアントがトークンを取得するための場所（client_credentials フロー）。
- **JWKS エンドポイント:** `https://<app-fqdn>/oauth2/jwks` – JWK セットを返す場所（APIMが署名キー取得に使用）。
- **OpenID 設定:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 発見のJSON（`issuer`、`token_endpoint`、`jwks_uri`などを含む）。

APIM は **OpenID 設定 URL** を使用して `jwks_uri` を検出します。たとえば、コンテナアプリの FQDN が `my-mcp-app.eastus.azurecontainerapps.io` の場合、APIM の `<openid-config url="...">` は `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` を使用してください。（Spring はデフォルトでメタデータ内の `issuer` を同じベースURLに設定します ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）

## Azure API Management (`validate-jwt`) の設定

Azure APIM で、インバウンドポリシーに `<validate-jwt>` を使用して Spring Authorization Server の JWT を検証するポリシーを追加します。簡単な設定では、OpenID Connect メタデータ URL を使用できます。ポリシースニペット例：

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

このポリシーにより、APIM は Spring Auth Server から OpenID 構成を取得し、JWKS を取得して各トークンが信頼できるキーで署名され、正しい audience を持つことを検証します。(`<issuers>` を省略した場合、APIM はメタデータから自動的に `issuer` クレームを使用します)。`<audience>` はトークン内のクライアントIDまたは API リソース識別子に一致させてください（この例では `"mcp-client"` に設定しました）。これは Microsoft の `validate-jwt` と `<openid-config>` の使用に関するドキュメントにも合致します ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))。

検証後、APIM はリクエスト（元の `Authorization` ヘッダーを含む）をバックエンドへ転送します。Spring アプリはリソースサーバーでもあるためトークンを再検証しますが、APIM が既に有効性を保証しています。（開発時は APIM のチェックだけに頼り、アプリのチェックを無効化できますが、両方残すのが安全です。）

## 設定例

| セット項目          | 例の値                                                             | 備考                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | コンテナアプリの URL（ベース URI）          |
| <strong>トークンエンドポイント</strong> | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Spring のデフォルトトークンエンドポイント ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS エンドポイント**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | デフォルト JWK セットエンドポイント ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID 設定**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 発見ドキュメント（自動生成）             |
| **APIM audience**  | `mcp-client`                                                         | OAuth クライアント ID または API リソース名  |
| **APIM ポリシー**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` がこの URL を使用 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## よくある落とし穴

- **HTTPS/TLS:** APIM ゲートウェイは OpenID/JWKS エンドポイントに対し有効な証明書の HTTPS が必要です。Azure Container Apps はデフォルトで Azure 管理ドメインに信頼された TLS 証明書を提供します ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。カスタムドメインを使用する場合は証明書をバインドしてください（Azure の無料管理証明書機能を利用可能） ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。APIM がエンドポイント証明書を信用できなければ `<validate-jwt>` はメタデータの取得に失敗します。

- **エンドポイントのアクセス可能性:** Spring アプリのエンドポイントが APIM から到達可能である必要があります。`--ingress external`（またはポータルでのイングレス有効化）が最も簡単です。内部または vNet バウンド環境を選択した場合、APIM（デフォルトでパブリック）がアプリに到達できない可能性があります（同じ VNet に配置しない限り）。テスト環境では、APIM が `.well-known` と `/jwks` URL にアクセスできるようにパブリックイングレスを推奨します。

- **OpenID Discovery 有効化:** Spring Authorization Server はデフォルトで OIDC が有効化されていない限り、`/.well-known/openid-configuration` を公開しません。上記の `.oidc(Customizer.withDefaults())` をセキュリティ設定に含め、プロバイダー設定エンドポイントを有効にしてください ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。そうでないと APIM の `<openid-config>` 呼び出しは 404 エラーになります。

- **Audience クレーム:** Spring のデフォルトは `aud` クレームにクライアントIDを設定します。APIM の `<audience>` チェックが失敗する場合は、トークンカスタマイズ（前述のとおり）を行うか、APIM ポリシーを調整してください。JWT の audience が `<audience>` 設定と一致していることを確認してください。

- **JSON メタデータ解析:** OpenID 設定の JSON は有効でなければなりません。Spring のデフォルト設定は標準的な OIDC メタデータドキュメントを生成します。正しい `issuer` と `jwks_uri` を含むことを確認してください。Spring をプロキシやパスベースのルートの背後にホストしている場合は、このメタデータ内の URL を再確認してください。APIM はこれらの値をそのまま使用します。

- **ポリシーの順序:** APIM ポリシーでは `<validate-jwt>` をバックエンドへのルーティングの<strong>前</strong>に配置してください。そうしないと、有効なトークンなしで呼び出しがアプリに到達する可能性があります。また、`<validate-jwt>` は `<inbound>` の直下に置き（別の条件の内側にネストしない）、APIM が適用するようにしてください。

上記の手順に従うことで、Azure Container Apps 上で Spring AI MCP サーバーを実行し、Azure API Management で最小限のポリシーで OAuth2 JWT の検証が可能になります。重要なポイントは、Spring 認証エンドポイントを TLS 有効のパブリックアクセスで公開し、OIDC 発見を有効化し、APIM の `validate-jwt` を OpenID 設定 URL に向けて JWKS を自動取得させることです。この構成は開発/テスト環境に適しています。本番環境では適切なシークレット管理、トークン有効期間設定、JWKS キーのローテーションなどを検討してください。


**参考:** デフォルトエンドポイントについては Spring Authorization Server のドキュメントを参照してください（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）および OIDC 設定については（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）; `validate-jwt` の例については Microsoft APIM のドキュメントを参照してください（[Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)）; また、デプロイと証明書に関しては Azure Container Apps のドキュメントを参照してください（[Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)）（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
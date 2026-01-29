# MCP OAuth2 デモ

このプロジェクトは、**最小限の Spring Boot アプリケーション**であり、以下の両方の役割を果たします：

* **Spring Authorization Server**（`client_credentials` フローを使って JWT アクセストークンを発行）  
* **Resource Server**（自身の `/hello` エンドポイントを保護）

これは、[Spring ブログ記事（2025年4月2日）](https://spring.io/blog/2025/04/02/mcp-server-oauth2) に示された設定を再現しています。

---

## クイックスタート（ローカル）

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2 設定のテスト

以下の手順で OAuth2 セキュリティ設定をテストできます：

### 1. サーバーが起動してセキュアになっていることを確認

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. クライアント認証情報を使ってアクセストークンを取得

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

Note: Basic 認証ヘッダー（`bWNwLWNsaWVudDpzZWNyZXQ=`）は `mcp-client:secret` の Base64 エンコードです。

### 3. トークンを使って保護されたエンドポイントにアクセス

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" という成功レスポンスが返れば、OAuth2 設定が正しく動作していることを示します。

---

## コンテナのビルド

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** へのデプロイ

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ingress の FQDN があなたの **issuer** (`https://<fqdn>`) になります。  
Azure は `*.azurecontainerapps.io` 用の信頼された TLS 証明書を自動的に提供します。

---

## **Azure API Management** への連携

API に以下のインバウンドポリシーを追加してください：

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

APIM は JWKS を取得し、すべてのリクエストを検証します。

---

## 次にやること

- [5.4 ルートコンテキスト](../mcp-root-contexts/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
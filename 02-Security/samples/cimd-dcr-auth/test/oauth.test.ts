import assert from "node:assert/strict";
import { createServer } from "node:http";
import { test } from "node:test";

import { OAuthError } from "@modelcontextprotocol/server";
import { exportJWK, generateKeyPair, SignJWT } from "jose";

import { createTokenVerifier } from "../src/oauth.js";

test("verifies signature, issuer, audience, client ID, expiry, and scopes", async (context) => {
  const { publicKey, privateKey } = await generateKeyPair("RS256", { extractable: true });
  const publicJwk = await exportJWK(publicKey);
  publicJwk.kid = "course-test-key";
  publicJwk.alg = "RS256";

  const jwksServer = createServer((_request, response) => {
    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ keys: [publicJwk] }));
  });
  await new Promise<void>((resolve) => jwksServer.listen(0, "127.0.0.1", resolve));
  context.after(() => jwksServer.close());
  const address = jwksServer.address();
  assert(address && typeof address !== "string");

  const issuer = "https://issuer.example.com/";
  const audience = "http://127.0.0.1:3001/mcp";
  const token = await new SignJWT({
    client_id: "https://client.example.com/oauth/metadata.json",
    scope: "tool:greet profile"
  })
    .setProtectedHeader({ alg: "RS256", kid: publicJwk.kid })
    .setIssuer(issuer)
    .setAudience(audience)
    .setSubject("course-user")
    .setIssuedAt()
    .setExpirationTime("5m")
    .sign(privateKey);

  const verifier = createTokenVerifier({
    issuer,
    audience,
    jwksUri: `http://127.0.0.1:${address.port}/jwks`,
    algorithm: "RS256"
  });
  const authInfo = await verifier.verifyAccessToken(token);
  assert.equal(authInfo.clientId, "https://client.example.com/oauth/metadata.json");
  assert.deepEqual(authInfo.scopes, ["tool:greet", "profile"]);

  const wrongAudienceVerifier = createTokenVerifier({
    issuer,
    audience: "https://wrong.example.com/mcp",
    jwksUri: `http://127.0.0.1:${address.port}/jwks`,
    algorithm: "RS256"
  });
  await assert.rejects(() => wrongAudienceVerifier.verifyAccessToken(token), OAuthError);
});
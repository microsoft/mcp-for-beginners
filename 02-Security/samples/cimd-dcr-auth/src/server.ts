import {
  createMcpExpressApp,
  getOAuthProtectedResourceMetadataUrl,
  mcpAuthMetadataRouter,
  requireBearerAuth
} from "@modelcontextprotocol/express";
import { toNodeHandler } from "@modelcontextprotocol/node";
import { createMcpHandler } from "@modelcontextprotocol/server";

import { loadConfig } from "./config.js";
import { buildServer } from "./mcp.js";
import { createTokenVerifier, loadAuthorizationServerMetadata } from "./oauth.js";
import { createClientMetadata } from "./registration.js";

async function main(): Promise<void> {
  const config = loadConfig();
  const oauthMetadata = await loadAuthorizationServerMetadata(
    config.authorizationServerMetadataUrl,
    config.authorizationServerIssuer
  );
  const verifier = createTokenVerifier({
    issuer: config.authorizationServerIssuer,
    audience: config.mcpServerUrl.href,
    jwksUri: oauthMetadata.jwks_uri,
    algorithm: config.jwtAlgorithm
  });

  const handler = createMcpHandler(({ authInfo }) =>
    buildServer(authInfo, config.dcrClientIdPrefix)
  );
  const nodeHandler = toNodeHandler(handler);
  const app = createMcpExpressApp({ host: config.host });

  app.get("/health", (_request, response) => response.json({ status: "ok" }));
  app.get(config.clientMetadataUrl.pathname, (_request, response) =>
    response.json(createClientMetadata(config.clientMetadataUrl, config.redirectUris))
  );
  app.use(
    mcpAuthMetadataRouter({
      oauthMetadata,
      resourceServerUrl: config.mcpServerUrl,
      scopesSupported: ["tool:greet"]
    })
  );

  const auth = requireBearerAuth({
    verifier,
    requiredScopes: [],
    resourceMetadataUrl: getOAuthProtectedResourceMetadataUrl(config.mcpServerUrl)
  });
  app.all("/mcp", auth, (request, response) =>
    void nodeHandler(request, response, request.body)
  );

  const httpServer = app.listen(config.port, config.host, () => {
    console.log(`MCP server: ${config.mcpServerUrl.href}`);
    console.log(`Client metadata: ${config.clientMetadataUrl.href}`);
  });

  process.on("SIGINT", async () => {
    await handler.close();
    httpServer.close(() => process.exit(0));
  });
}

main().catch((error: unknown) => {
  console.error(error);
  process.exitCode = 1;
});
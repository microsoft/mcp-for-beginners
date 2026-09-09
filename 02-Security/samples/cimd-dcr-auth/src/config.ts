export interface SampleConfig {
  host: string;
  port: number;
  mcpServerUrl: URL;
  authorizationServerIssuer: string;
  authorizationServerMetadataUrl: URL;
  jwtAlgorithm: string;
  clientMetadataUrl: URL;
  redirectUris: string[];
  dcrClientIdPrefix?: string;
}

const LOOPBACK_HOSTS = new Set(["127.0.0.1", "localhost", "[::1]"]);
const ALLOWED_JWT_ALGORITHMS = new Set(["RS256", "PS256", "ES256"]);

export function requireSecureUrl(url: URL, name: string): URL {
  if (url.protocol === "https:") {
    return url;
  }
  if (url.protocol === "http:" && LOOPBACK_HOSTS.has(url.hostname)) {
    return url;
  }
  throw new Error(`${name} must use HTTPS except for loopback development`);
}

function required(name: string): string {
  const value = process.env[name]?.trim();
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
}

export function loadConfig(): SampleConfig {
  const port = Number.parseInt(process.env.PORT ?? "3001", 10);
  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error("PORT must be an integer between 1 and 65535");
  }

  const jwtAlgorithm = process.env.JWT_ALGORITHM?.trim() || "RS256";
  if (!ALLOWED_JWT_ALGORITHMS.has(jwtAlgorithm)) {
    throw new Error("JWT_ALGORITHM must be RS256, PS256, or ES256");
  }

  const redirectUris = required("OAUTH_REDIRECT_URIS")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);
  for (const redirectUri of redirectUris) {
    const parsed = requireSecureUrl(new URL(redirectUri), "OAuth redirect URI");
    if (parsed.hash) {
      throw new Error("OAuth redirect URIs must not contain fragments");
    }
  }

  const authorizationServerIssuer = required("AUTHORIZATION_SERVER_ISSUER");
  requireSecureUrl(new URL(authorizationServerIssuer), "AUTHORIZATION_SERVER_ISSUER");

  return {
    host: process.env.HOST?.trim() || "127.0.0.1",
    port,
    mcpServerUrl: requireSecureUrl(
      new URL(process.env.MCP_SERVER_URL ?? `http://127.0.0.1:${port}/mcp`),
      "MCP_SERVER_URL"
    ),
    authorizationServerIssuer,
    authorizationServerMetadataUrl: requireSecureUrl(
      new URL(required("AUTHORIZATION_SERVER_METADATA_URL")),
      "AUTHORIZATION_SERVER_METADATA_URL"
    ),
    jwtAlgorithm,
    clientMetadataUrl: requireSecureUrl(
      new URL(required("CLIENT_METADATA_URL")),
      "CLIENT_METADATA_URL"
    ),
    redirectUris,
    dcrClientIdPrefix: process.env.DCR_CLIENT_ID_PREFIX?.trim() || undefined
  };
}
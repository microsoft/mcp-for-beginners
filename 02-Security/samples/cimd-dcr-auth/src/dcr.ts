import { requireSecureUrl } from "./config.js";

export interface DynamicClientRequest {
  client_name: string;
  application_type: "native";
  grant_types: ["authorization_code", "refresh_token"];
  response_types: ["code"];
  redirect_uris: string[];
  token_endpoint_auth_method: "none";
}

export interface DynamicClientResult {
  client_id: string;
  client_secret?: string;
  [key: string]: unknown;
}

export function createDynamicClientRequest(redirectUris: string[]): DynamicClientRequest {
  if (redirectUris.length === 0) {
    throw new Error("At least one OAuth redirect URI is required");
  }
  return {
    client_name: "MCP DCR compatibility client",
    application_type: "native",
    grant_types: ["authorization_code", "refresh_token"],
    response_types: ["code"],
    redirect_uris: redirectUris,
    token_endpoint_auth_method: "none"
  };
}

export async function registerDynamicClient(
  registrationEndpoint: URL,
  request: DynamicClientRequest
): Promise<DynamicClientResult> {
  const secureEndpoint = requireSecureUrl(registrationEndpoint, "registration_endpoint");
  const response = await fetch(secureEndpoint, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(request)
  });
  if (!response.ok) {
    throw new Error(`Dynamic client registration failed: ${response.status}`);
  }

  const result = (await response.json()) as Record<string, unknown>;
  if (typeof result.client_id !== "string" || result.client_id.length === 0) {
    throw new Error("Dynamic client registration response has no client_id");
  }
  if (result.client_secret !== undefined && typeof result.client_secret !== "string") {
    throw new Error("Dynamic client registration client_secret must be a string");
  }
  return result as DynamicClientResult;
}
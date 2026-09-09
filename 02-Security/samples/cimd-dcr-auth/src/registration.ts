export type RegistrationMechanism = "cimd" | "dcr" | "opaque-client-id";

export interface RegistrationDetails {
  mechanism: RegistrationMechanism;
  clientId: string;
  explanation: string;
}

export function classifyRegistration(
  clientId: string,
  dcrClientIdPrefix?: string
): RegistrationDetails {
  try {
    const url = new URL(clientId);
    if (url.protocol === "https:" && url.pathname !== "/") {
      return {
        mechanism: "cimd",
        clientId,
        explanation: "The client_id is an HTTPS URL with a path, matching the CIMD identifier shape."
      };
    }
  } catch {
    // Opaque client IDs are handled below.
  }

  if (dcrClientIdPrefix && clientId.startsWith(dcrClientIdPrefix)) {
    return {
      mechanism: "dcr",
      clientId,
      explanation: `The opaque client_id matches the configured DCR prefix '${dcrClientIdPrefix}'.`
    };
  }

  return {
    mechanism: "opaque-client-id",
    clientId,
    explanation:
      "The token contains an opaque client_id. Standard token claims alone cannot distinguish DCR from pre-registration."
  };
}

export interface ClientMetadataDocument {
  client_id: string;
  client_name: string;
  client_uri: string;
  application_type: "native";
  grant_types: ["authorization_code", "refresh_token"];
  response_types: ["code"];
  redirect_uris: string[];
  token_endpoint_auth_method: "none";
}

export function createClientMetadata(
  clientMetadataUrl: URL,
  redirectUris: string[]
): ClientMetadataDocument {
  if (clientMetadataUrl.protocol !== "https:" || clientMetadataUrl.pathname === "/") {
    throw new Error("CLIENT_METADATA_URL must be an HTTPS URL with a non-root path");
  }
  if (clientMetadataUrl.search || clientMetadataUrl.hash) {
    throw new Error("CLIENT_METADATA_URL must not contain a query string or fragment");
  }
  if (redirectUris.length === 0) {
    throw new Error("At least one OAuth redirect URI is required");
  }

  return {
    client_id: clientMetadataUrl.href,
    client_name: "MCP CIMD and DCR course sample",
    client_uri: clientMetadataUrl.origin,
    application_type: "native",
    grant_types: ["authorization_code", "refresh_token"],
    response_types: ["code"],
    redirect_uris: redirectUris,
    token_endpoint_auth_method: "none"
  };
}
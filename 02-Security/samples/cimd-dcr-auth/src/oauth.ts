import type { OAuthTokenVerifier } from "@modelcontextprotocol/express";
import {
  OAuthError,
  OAuthErrorCode,
  type AuthInfo,
  type OAuthMetadata
} from "@modelcontextprotocol/server";
import { createRemoteJWKSet, jwtVerify, type JWTPayload } from "jose";

import { requireSecureUrl } from "./config.js";

export type ValidatedOAuthMetadata = OAuthMetadata & {
  issuer: string;
  authorization_endpoint: string;
  token_endpoint: string;
  jwks_uri: string;
  registration_endpoint?: string;
};

function stringClaim(payload: JWTPayload, name: string): string | undefined {
  const value = payload[name];
  return typeof value === "string" ? value : undefined;
}

function scopesFrom(payload: JWTPayload): string[] {
  const scope = payload.scope;
  if (typeof scope === "string") {
    return scope.split(" ").filter(Boolean);
  }
  const permissions = payload.permissions;
  return Array.isArray(permissions)
    ? permissions.filter((value): value is string => typeof value === "string")
    : [];
}

export async function loadAuthorizationServerMetadata(
  metadataUrl: URL,
  expectedIssuer: string
): Promise<ValidatedOAuthMetadata> {
  const response = await fetch(metadataUrl, { redirect: "error" });
  if (!response.ok) {
    throw new Error(`Authorization server metadata request failed: ${response.status}`);
  }

  const metadata = (await response.json()) as Record<string, unknown>;
  if (metadata.issuer !== expectedIssuer) {
    throw new Error("Authorization server metadata issuer does not match AUTHORIZATION_SERVER_ISSUER");
  }
  if (
    typeof metadata.authorization_endpoint !== "string" ||
    typeof metadata.token_endpoint !== "string" ||
    typeof metadata.jwks_uri !== "string"
  ) {
    throw new Error("Authorization server metadata is missing required endpoints");
  }
  requireSecureUrl(new URL(metadata.authorization_endpoint), "authorization_endpoint");
  requireSecureUrl(new URL(metadata.token_endpoint), "token_endpoint");
  requireSecureUrl(new URL(metadata.jwks_uri), "jwks_uri");
  if (
    metadata.registration_endpoint !== undefined &&
    typeof metadata.registration_endpoint !== "string"
  ) {
    throw new Error("Authorization server registration_endpoint must be a string");
  }
  return metadata as ValidatedOAuthMetadata;
}

export function createTokenVerifier(options: {
  issuer: string;
  audience: string;
  jwksUri: string;
  algorithm: string;
}): OAuthTokenVerifier {
  const jwks = createRemoteJWKSet(new URL(options.jwksUri));

  return {
    async verifyAccessToken(token: string): Promise<AuthInfo> {
      try {
        const { payload } = await jwtVerify(token, jwks, {
          issuer: options.issuer,
          audience: options.audience,
          algorithms: [options.algorithm]
        });
        const clientId = stringClaim(payload, "client_id") ?? stringClaim(payload, "azp");
        if (!clientId || !payload.exp) {
          throw new Error("Token must contain client_id (or azp) and exp claims");
        }

        return {
          token,
          clientId,
          scopes: scopesFrom(payload),
          expiresAt: payload.exp
        };
      } catch {
        throw new OAuthError(OAuthErrorCode.InvalidToken, "Access token is invalid or expired");
      }
    }
  };
}
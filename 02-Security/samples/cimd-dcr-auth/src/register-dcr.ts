import { loadConfig } from "./config.js";
import { createDynamicClientRequest, registerDynamicClient } from "./dcr.js";
import { loadAuthorizationServerMetadata } from "./oauth.js";

async function main(): Promise<void> {
  const config = loadConfig();
  const metadata = await loadAuthorizationServerMetadata(
    config.authorizationServerMetadataUrl,
    config.authorizationServerIssuer
  );
  if (!metadata.registration_endpoint) {
    throw new Error("Authorization server does not advertise registration_endpoint");
  }

  const registration = await registerDynamicClient(
    new URL(metadata.registration_endpoint),
    createDynamicClientRequest(config.redirectUris)
  );
  console.log(`Registered legacy DCR client: ${registration.client_id}`);
  if (registration.client_secret) {
    console.log("The authorization server returned a client secret; store it securely.");
  }
}

main().catch((error: unknown) => {
  console.error(error);
  process.exitCode = 1;
});
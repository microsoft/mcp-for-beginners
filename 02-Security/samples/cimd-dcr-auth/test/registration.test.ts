import assert from "node:assert/strict";
import { test } from "node:test";

import { classifyRegistration, createClientMetadata } from "../src/registration.js";

test("classifies an HTTPS URL client_id as CIMD", () => {
  const result = classifyRegistration("https://client.example.com/oauth/metadata.json");
  assert.equal(result.mechanism, "cimd");
});

test("classifies an opaque ID as DCR only with a provider hint", () => {
  const hinted = classifyRegistration("dcr_example", "dcr_");
  const unhinted = classifyRegistration("dcr_example");
  assert.equal(hinted.mechanism, "dcr");
  assert.equal(unhinted.mechanism, "opaque-client-id");
});

test("does not classify prohibited URL shapes as CIMD", () => {
  const invalidClientIds = [
    "https://user@client.example.com/metadata.json",
    "https://client.example.com/metadata.json?version=1",
    "https://client.example.com/metadata.json#current"
  ];
  for (const clientId of invalidClientIds) {
    assert.equal(classifyRegistration(clientId).mechanism, "opaque-client-id");
  }
});

test("creates a valid public native-client metadata document", () => {
  const metadata = createClientMetadata(
    new URL("https://client.example.com/oauth/metadata.json"),
    ["http://127.0.0.1:6274/oauth/callback"]
  );
  assert.equal(metadata.client_id, "https://client.example.com/oauth/metadata.json");
  assert.equal(metadata.token_endpoint_auth_method, "none");
  assert.deepEqual(metadata.response_types, ["code"]);
});

test("rejects a non-HTTPS CIMD URL", () => {
  assert.throws(
    () => createClientMetadata(new URL("http://client.example.com/metadata.json"), ["https://app/callback"]),
    /HTTPS URL/
  );
});

test("rejects a CIMD URL containing a query or fragment", () => {
  assert.throws(
    () =>
      createClientMetadata(
        new URL("https://client.example.com/metadata.json?version=1"),
        ["http://127.0.0.1:6274/oauth/callback"]
      ),
    /query string or fragment/
  );
});
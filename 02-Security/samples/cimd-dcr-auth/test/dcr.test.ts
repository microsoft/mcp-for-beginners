import assert from "node:assert/strict";
import { createServer } from "node:http";
import { test } from "node:test";

import { createDynamicClientRequest, registerDynamicClient } from "../src/dcr.js";

test("registers a public DCR compatibility client", async (context) => {
  const server = createServer((request, response) => {
    assert.equal(request.method, "POST");
    response.writeHead(201, { "content-type": "application/json" });
    response.end(JSON.stringify({ client_id: "dcr_test_client" }));
  });
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  context.after(() => server.close());
  const address = server.address();
  assert(address && typeof address !== "string");

  const result = await registerDynamicClient(
    new URL(`http://127.0.0.1:${address.port}/register`),
    createDynamicClientRequest(["http://127.0.0.1:6274/oauth/callback"])
  );
  assert.equal(result.client_id, "dcr_test_client");
});

test("rejects an insecure remote DCR endpoint", async () => {
  await assert.rejects(
    () =>
      registerDynamicClient(
        new URL("http://authorization.example.com/register"),
        createDynamicClientRequest(["http://127.0.0.1:6274/oauth/callback"])
      ),
    /must use HTTPS/
  );
});
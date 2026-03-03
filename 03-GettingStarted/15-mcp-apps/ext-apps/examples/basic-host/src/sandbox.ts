import type { McpUiSandboxProxyReadyNotification, McpUiSandboxResourceReadyNotification } from "../../../dist/src/types";
import { buildAllowAttribute } from "../../../dist/src/app-bridge";

function isAllowedReferrer(referrer: string): boolean {
  try {
    const url = new URL(referrer);
    const host = url.hostname.toLowerCase();

    // Local development (http or https)
    if (host === "localhost" || host === "127.0.0.1") {
      return true;
    }

    // GitHub Codespaces / forwarded ports
    if (host.endsWith(".github.dev") || host.endsWith(".app.github.dev")) {
      return true;
    }

    return false;
  } catch {
    return false;
  }
}

function isAllowedHost(host: string): boolean {
  const h = host.toLowerCase();
  if (h === "localhost" || h === "127.0.0.1") {
    return true;
  }
  if (h.endsWith(".github.dev") || h.endsWith(".app.github.dev")) {
    return true;
  }
  return false;
}

function getExpectedHostOrigin(): string {
  // Preferred source: browser referrer.
  if (document.referrer && isAllowedReferrer(document.referrer)) {
    return new URL(document.referrer).origin;
  }

  // Fallback: explicit host origin passed by the host via query params.
  const hostOriginParam = new URL(window.location.href).searchParams.get("hostOrigin");
  if (hostOriginParam) {
    try {
      const hostOrigin = new URL(hostOriginParam).origin;
      const host = new URL(hostOrigin).hostname;
      if (isAllowedHost(host)) {
        return hostOrigin;
      }
      throw new Error(`Host origin not allowed: ${hostOrigin}`);
    } catch {
      throw new Error(`Invalid hostOrigin query parameter: ${hostOriginParam}`);
    }
  }

  throw new Error(
    "No trusted embedding origin found. Provide referrer or hostOrigin query param.",
  );
}

if (window.self === window.top) {
  throw new Error("This file is only to be used in an iframe sandbox.");
}

// Compute expected host origin used for postMessage origin validation.
const EXPECTED_HOST_ORIGIN = getExpectedHostOrigin();

const OWN_ORIGIN = new URL(window.location.href).origin;

// Security self-test: verify iframe isolation is working correctly.
// This MUST throw a SecurityError -- if `window.top` is accessible, the sandbox
// configuration is dangerously broken and untrusted content could escape.
try {
  window.top!.alert("If you see this, the sandbox is not setup securely.");
  throw "FAIL";
} catch (e) {
  if (e === "FAIL") {
    throw new Error("The sandbox is not setup securely.");
  }

  // Expected: SecurityError confirms proper sandboxing.
}

// Double-iframe sandbox architecture: THIS file is the outer sandbox proxy
// iframe on a separate origin. It creates an inner iframe for untrusted HTML
// content. Per the specification, the Host and the Sandbox MUST have different
// origins.
const inner = document.createElement("iframe");
inner.style = "width:100%; height:100%; border:none;";
inner.setAttribute("sandbox", "allow-scripts allow-same-origin allow-forms");
// Note: allow attribute is set later when receiving sandbox-resource-ready notification
// based on the permissions requested by the app
document.body.appendChild(inner);

const RESOURCE_READY_NOTIFICATION: McpUiSandboxResourceReadyNotification["method"] =
  "ui/notifications/sandbox-resource-ready";
const PROXY_READY_NOTIFICATION: McpUiSandboxProxyReadyNotification["method"] =
  "ui/notifications/sandbox-proxy-ready";

// Message relay: This Sandbox (outer iframe) acts as a bidirectional bridge,
// forwarding messages between:
//
//   Host (parent window) ↔ Sandbox (outer frame) ↔ View (inner iframe)
//
// Reason: the parent window and inner iframe have different origins and can't
// communicate directly, so the outer iframe forwards messages in both
// directions to connect them.
//
// Special case: The "ui/notifications/sandbox-proxy-ready" message is
// intercepted here (not relayed) because the Sandbox uses it to configure and
// load the inner iframe with the view HTML content.
//
// Security: CSP is enforced via HTTP headers on sandbox.html (set by serve.ts
// based on ?csp= query param). This is tamper-proof unlike meta tags.

window.addEventListener("message", async (event) => {
  if (event.source === window.parent) {
    // Validate that messages from parent come from the expected host origin.
    // This prevents malicious pages from sending messages to this sandbox.
    if (event.origin !== EXPECTED_HOST_ORIGIN) {
      console.error(
        "[Sandbox] Rejecting message from unexpected origin:",
        event.origin,
        "expected:",
        EXPECTED_HOST_ORIGIN
      );
      return;
    }

    if (event.data && event.data.method === RESOURCE_READY_NOTIFICATION) {
      const { html, sandbox, permissions } = event.data.params;
      if (typeof sandbox === "string") {
        inner.setAttribute("sandbox", sandbox);
      }
      // Set Permission Policy allow attribute if permissions are requested
      const allowAttribute = buildAllowAttribute(permissions);
      if (allowAttribute) {
        console.log("[Sandbox] Setting allow attribute:", allowAttribute);
        inner.setAttribute("allow", allowAttribute);
      }
      if (typeof html === "string") {
        // Use document.write instead of srcdoc (which the CesiumJS Map won't work with)
        const doc = inner.contentDocument || inner.contentWindow?.document;
        if (doc) {
          doc.open();
          doc.write(html);
          doc.close();
        } else {
          // Fallback to srcdoc if document is not accessible
          console.warn("[Sandbox] document.write not available, falling back to srcdoc");
          inner.srcdoc = html;
        }
      }
    } else {
      if (inner && inner.contentWindow) {
        inner.contentWindow.postMessage(event.data, "*");
      }
    }
  } else if (event.source === inner.contentWindow) {
    if (event.origin !== OWN_ORIGIN) {
      console.error(
        "[Sandbox] Rejecting message from inner iframe with unexpected origin:",
        event.origin,
        "expected:",
        OWN_ORIGIN
      );
      return;
    }
    // Relay messages from inner frame to parent window.
    // Use specific origin instead of "*" to prevent message interception.
    window.parent.postMessage(event.data, EXPECTED_HOST_ORIGIN);
  }
});

// Notify the Host that the Sandbox is ready to receive view HTML.
// Use specific origin instead of "*" to ensure only the expected host receives this.
window.parent.postMessage({
  jsonrpc: "2.0",
  method: PROXY_READY_NOTIFICATION,
  params: {},
}, EXPECTED_HOST_ORIGIN);

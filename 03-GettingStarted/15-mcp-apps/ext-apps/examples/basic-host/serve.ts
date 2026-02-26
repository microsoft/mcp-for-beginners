#!/usr/bin/env npx tsx
/**
 * HTTP servers for the MCP UI example:
 * - Host server (port 8080): serves host HTML files (React and Vanilla examples)
 * - Sandbox server (port 8081): serves sandbox.html with CSP headers
 *
 * Running on separate ports ensures proper origin isolation for security.
 *
 * Security: CSP is set via HTTP headers based on ?csp= query param.
 * This ensures content cannot tamper with CSP (unlike meta tags).
 */

import express from "express";
import cors from "cors";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import type { McpUiResourceCsp } from "@modelcontextprotocol/ext-apps";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const HOST_PORT = parseInt(process.env.HOST_PORT || "8080", 10);
const SANDBOX_PORT = parseInt(process.env.SANDBOX_PORT || "8081", 10);
const DIRECTORY = join(__dirname, "dist");
const SERVERS: string[] = process.env.SERVERS
  ? JSON.parse(process.env.SERVERS)
  : ["https://psychic-xylophone-657rpjgvxpc5g64-3001.app.github.dev/mcp"]; // https://psychic-xylophone-657rpjgvxpc5g64-3001.app.github.dev/mcp

// ============ Host Server (port 8080) ============
const hostApp = express();
hostApp.use(cors());

// Exclude sandbox.html from host server
hostApp.use((req, res, next) => {
  if (req.path === "/sandbox.html") {
    res.status(404).send("Sandbox is served on a different port");
    return;
  }
  next();
});

hostApp.use(express.static(DIRECTORY));

// API endpoint to get configured server URLs
hostApp.get("/api/servers", (_req, res) => {
  res.json(SERVERS);
});

hostApp.get("/", (_req, res) => {
  res.redirect("/index.html");
});

// ============ Sandbox Server (port 8081) ============
const sandboxApp = express();
sandboxApp.use(cors());

// Validate CSP domain entries to prevent injection attacks.
// Rejects entries containing characters that could:
// - `;` or newlines: break out to new CSP directive
// - quotes: inject CSP keywords like 'unsafe-eval'
// - space: inject multiple sources in one entry
function sanitizeCspDomains(domains?: string[]): string[] {
  if (!domains) return [];
  return domains.filter((d) => typeof d === "string" && !/[;\r\n'" ]/.test(d));
}

function buildCspHeader(csp?: McpUiResourceCsp): string {
  const resourceDomains = sanitizeCspDomains(csp?.resourceDomains).join(" ");
  const connectDomains = sanitizeCspDomains(csp?.connectDomains).join(" ");
  const frameDomains = sanitizeCspDomains(csp?.frameDomains).join(" ") || null;
  const baseUriDomains =
    sanitizeCspDomains(csp?.baseUriDomains).join(" ") || null;

  const directives = [
    // Default: allow same-origin + inline styles/scripts (needed for bundled apps)
    "default-src 'self' 'unsafe-inline'",
    // Scripts: same-origin + inline + eval (some libs need eval) + blob (workers) + specified domains
    `script-src 'self' 'unsafe-inline' 'unsafe-eval' blob: data: ${resourceDomains}`.trim(),
    // Styles: same-origin + inline + specified domains
    `style-src 'self' 'unsafe-inline' blob: data: ${resourceDomains}`.trim(),
    // Images: same-origin + data/blob URIs + specified domains
    `img-src 'self' data: blob: ${resourceDomains}`.trim(),
    // Fonts: same-origin + data/blob URIs + specified domains
    `font-src 'self' data: blob: ${resourceDomains}`.trim(),
    // Media (audio/video): same-origin + data/blob URIs + specified domains
    `media-src 'self' data: blob: ${resourceDomains}`.trim(),
    // Network requests: same-origin + specified API/tile domains
    `connect-src 'self' ${connectDomains}`.trim(),
    // Workers: same-origin + blob (dynamic workers) + specified domains
    // This is critical for WebGL apps (CesiumJS, Three.js) that use workers for:
    // - Tile decoding and terrain processing
    // - Image processing and texture loading
    // - Physics and geometry calculations
    `worker-src 'self' blob: ${resourceDomains}`.trim(),
    // Nested iframes: use frameDomains if provided, otherwise block all
    frameDomains ? `frame-src ${frameDomains}` : "frame-src 'none'",
    // Plugins: always blocked (defense in depth)
    "object-src 'none'",
    // Base URI: use baseUriDomains if provided, otherwise block all
    baseUriDomains ? `base-uri ${baseUriDomains}` : "base-uri 'none'",
  ];

  return directives.join("; ");
}

// Serve sandbox.html with CSP from query params
sandboxApp.get(["/", "/sandbox.html"], (req, res) => {
  // Parse CSP config from query param: ?csp=<url-encoded-json>
  let cspConfig: McpUiResourceCsp | undefined;
  if (typeof req.query.csp === "string") {
    try {
      cspConfig = JSON.parse(req.query.csp);
    } catch (e) {
      console.warn("[Sandbox] Invalid CSP query param:", e);
    }
  }

  // Set CSP via HTTP header - tamper-proof unlike meta tags
  const cspHeader = buildCspHeader(cspConfig);
  res.setHeader("Content-Security-Policy", cspHeader);

  // Prevent caching to ensure fresh CSP on each load
  res.setHeader("Cache-Control", "no-cache, no-store, must-revalidate");
  res.setHeader("Pragma", "no-cache");
  res.setHeader("Expires", "0");

  res.sendFile(join(DIRECTORY, "sandbox.html"));
});

sandboxApp.use((_req, res) => {
  res.status(404).send("Only sandbox.html is served on this port");
});

// ============ Start both servers ============
hostApp.listen(HOST_PORT, (err) => {
  if (err) {
    console.error("Error starting server:", err);
    process.exit(1);
  }
  console.log(`Host server:    http://localhost:${HOST_PORT}`);
});

sandboxApp.listen(SANDBOX_PORT, (err) => {
  if (err) {
    console.error("Error starting server:", err);
    process.exit(1);
  }
  console.log(`Sandbox server: http://localhost:${SANDBOX_PORT}`);
  console.log("\nPress Ctrl+C to stop\n");
});

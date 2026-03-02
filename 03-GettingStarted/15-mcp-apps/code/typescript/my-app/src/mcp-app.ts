import { App } from "@modelcontextprotocol/ext-apps";

// Get element references
const serverTimeEl = document.getElementById("server-time")!;
const getTimeBtn = document.getElementById("get-time-btn")!;
const faqResponseEl = document.getElementById("faq-response")!;
const getFaqBtn = document.getElementById("get-faq-btn")!;
const faqQueryInput = document.getElementById("faq-query") as HTMLInputElement;
const getPingBtn = document.getElementById("ping")!;
const pingResponse = document.getElementById("ping-response")!;

// rps
const getRpsBtn = document.getElementById("rps-button")!;
const rpsResponseEl = document.getElementById("rps-result")!;
const rpsOptions = document.getElementById("rps-options") as HTMLSelectElement;

// Get element references

// Create app instance
const app = new App({ name: "Get Time App", version: "1.0.0" });

// Handle tool results from the server. Set before `app.connect()` to avoid
// missing the initial tool result.
app.ontoolresult = (result) => {
  const time = result.content?.find((c) => c.type === "text")?.text;
  serverTimeEl.textContent = time ?? "[ERROR]";
};

getRpsBtn.addEventListener("click", async () => {
  const userChoice = rpsOptions.value;
  const result = await app.callServerTool({ name: "play-rps", arguments: { choice: userChoice } });
  const rpsResult = result.content?.find((c) => c.type === "text")?.text;
  rpsResponseEl.textContent = rpsResult ?? "[ERROR]";
});

getPingBtn.addEventListener("click", async () => {
  const result = await app.callServerTool({ "name": "ping", arguments: {} });
  const res =  result.content?.find((c) => c.type === "text")?.text;
  pingResponse.textContent = res ?? "[ERROR]";
});

// Wire up button click
getTimeBtn.addEventListener("click", async () => {
  // `app.callServerTool()` lets the UI request fresh data from the server
  const result = await app.callServerTool({ name: "get-time", arguments: {} });
  const time = result.content?.find((c) => c.type === "text")?.text;
  serverTimeEl.textContent = time ?? "[ERROR]";
});

getFaqBtn.addEventListener("click", async () => {
  const query = faqQueryInput.value;
  const result = await app.callServerTool({ name: "get-faq", arguments: { query } });
  const faq = result.content?.find((c) => c.type === "text")?.text;
  faqResponseEl.textContent = faq ?? "[ERROR]";
});

// Connect to host
app.connect();
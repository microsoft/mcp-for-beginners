import { App } from "@modelcontextprotocol/ext-apps";

// Get element references
const serverTimeEl = document.getElementById("server-time")!;

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

// Connect to host
app.connect();
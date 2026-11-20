import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["./build/index.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "review-code",
  arguments: {
    code: "console.log(\"hello\");"
  }
});

console.log("Prompt: ", prompt.messages[0].content);

// List resources
const resources = await client.listResources();
for(let resource in resources.resources) {
  console.log("Resource: ", resource);
}

// List resource templates
const templates = await client.listResourceTemplates();
for(let template of templates.resourceTemplates) {
  console.log("Resource template: ", template.name);
}

// Read a resource
const resource = await client.readResource({
  uri: "greeting://hello"
});
const content = resource.contents[0];
console.log("Resource: ", "text" in content ? content.text : content.blob);

// Call a tool
const result = await client.callTool({
  name: "add",
  arguments: {
    a: 1,
    b: 8
  }
});

console.log("Tool result: ", result);

await client.close();

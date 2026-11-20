import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

/**
 * Complete TypeScript MCP Client Example
 * 
 * This client demonstrates how to:
 * 1. Connect to an MCP server using stdio transport
 * 2. List available tools, resources, and prompts
 * 3. Call calculator tools
 * 4. Read resources and get prompts
 * 5. Handle responses from the server
 */

async function runClient() {
    console.log("🚀 Starting MCP TypeScript Client...");

    try {
        // Start the server from 01-first-server/solution/typescript over stdio.
        // Run this client from that directory (see complete_examples.md).
        const transport = new StdioClientTransport({
            command: "node",
            args: ["build/index.js"]
        });

        // Create client instance
        const client = new Client({
            name: "calculator-client",
            version: "1.0.0"
        });

        console.log("📡 Connecting to MCP server...");

        // Connect to the server
        await client.connect(transport);

        console.log("✅ Connected to MCP server successfully!");

        // List available tools
        console.log("\n📋 Listing available tools:");
        const tools = await client.listTools();
        tools.tools.forEach(tool => {
            console.log(`  - ${tool.name}: ${tool.description ?? "(no description)"}`);
        });

        // Call the add tool
        console.log("\n🧮 Testing Calculator Operations:");
        const addResult = await client.callTool({
            name: "add",
            arguments: {
                a: 5,
                b: 3
            }
        });
        console.log(`Add 5 + 3 = ${extractTextResult(addResult)}`);

        // List resource templates and read a resource from one
        try {
            console.log("\n📄 Listing available resource templates:");
            const templates = await client.listResourceTemplates();
            templates.resourceTemplates.forEach(template => {
                console.log(`  - ${template.name}: ${template.uriTemplate}`);
            });

            // The server exposes greeting://{name}; fill in a name to read it
            console.log("\n📖 Reading resource: greeting://World");
            const resourceContent = await client.readResource({
                uri: "greeting://World"
            });
            const content = resourceContent.contents[0];
            console.log(`Resource content: ${"text" in content ? content.text : content.blob}`);
        } catch (error) {
            console.log("  Error reading resources:", error instanceof Error ? error.message : error);
        }

        // List available prompts and get one
        try {
            console.log("\n💬 Listing available prompts:");
            const prompts = await client.listPrompts();
            prompts.prompts.forEach(prompt => {
                console.log(`  - ${prompt.name}`);
            });

            console.log("\n💬 Getting prompt: review-code");
            const promptResult = await client.getPrompt({
                name: "review-code",
                arguments: {
                    code: "console.log('Hello, MCP!');"
                }
            });
            console.log(`Prompt result: ${JSON.stringify(promptResult.messages[0].content)}`);
        } catch (error) {
            console.log("  Error getting prompts:", error instanceof Error ? error.message : error);
        }

        // Close the connection so the process can exit
        await client.close();

        console.log("\n✨ Client operations completed successfully!");

    } catch (error) {
        console.error("❌ Error running MCP client:", error);
        process.exit(1);
    }
}

/**
 * Extract the text result from a tool call response
 */
function extractTextResult(result: any): string {
    try {
        if (result && result.content && Array.isArray(result.content)) {
            const textContent = result.content.find((c: any) => c.type === "text");
            if (textContent && textContent.text) {
                return textContent.text;
            }
        }
        
        // Fallback: stringify the entire result
        return JSON.stringify(result, null, 2);
    } catch {
        return result?.toString() || "No result";
    }
}

// Error handling wrapper
async function main() {
    try {
        await runClient();
    } catch (error) {
        console.error("Fatal error:", error);
        process.exit(1);
    }
}

// Run the client
main();

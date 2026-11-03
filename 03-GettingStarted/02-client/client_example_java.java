package com.microsoft.mcp.sample.client;

import java.util.Map;
import org.springframework.ai.mcp.client.webflux.transport.WebClientStreamableHttpTransport;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
import io.modelcontextprotocol.spec.McpSchema.TextContent;

/**
 * Complete Java MCP Client Example
 * 
 * This client demonstrates how to:
 * 1. Connect to an MCP server using the Streamable HTTP transport
 * 2. List available tools
 * 3. Call various calculator tools
 * 4. Handle responses from the server
 */
public class SDKClient {
    
    public static void main(String[] args) {
        // Create a Streamable HTTP transport pointing to the MCP server (default endpoint: /mcp)
        var transport = WebClientStreamableHttpTransport.builder(
            WebClient.builder().baseUrl("http://localhost:8080")
        ).build();
        
        // Create and run the client
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        try {
            // Create synchronous MCP client
            var client = McpClient.sync(this.transport).build();
            
            // Initialize the connection
            client.initialize();
            System.out.println("✅ Connected to MCP server successfully!");
            
            // Verify connection with ping
            client.ping();
            System.out.println("✅ Server ping successful!");
            
            // List available tools
            ListToolsResult toolsList = client.listTools();
            System.out.println("\n📋 Available Tools:");
            toolsList.tools().forEach(tool -> {
                System.out.println("  - " + tool.name() + ": " + tool.description());
            });
            
            // Test calculator operations
            System.out.println("\n🧮 Testing Calculator Operations:");
            
            // Addition
            CallToolResult resultAdd = client.callTool(
                CallToolRequest.builder("add").arguments(Map.of("a", 5.0, "b", 3.0)).build()
            );
            System.out.println("Add 5 + 3 = " + extractResult(resultAdd));
            
            // Subtraction
            CallToolResult resultSubtract = client.callTool(
                CallToolRequest.builder("subtract").arguments(Map.of("a", 10.0, "b", 4.0)).build()
            );
            System.out.println("Subtract 10 - 4 = " + extractResult(resultSubtract));
            
            // Multiplication
            CallToolResult resultMultiply = client.callTool(
                CallToolRequest.builder("multiply").arguments(Map.of("a", 6.0, "b", 7.0)).build()
            );
            System.out.println("Multiply 6 × 7 = " + extractResult(resultMultiply));
            
            // Division
            CallToolResult resultDivide = client.callTool(
                CallToolRequest.builder("divide").arguments(Map.of("a", 20.0, "b", 4.0)).build()
            );
            System.out.println("Divide 20 ÷ 4 = " + extractResult(resultDivide));
            
            // Help
            CallToolResult resultHelp = client.callTool(
                CallToolRequest.builder("help").arguments(Map.of()).build()
            );
            System.out.println("\n📖 Help Information:");
            System.out.println(extractResult(resultHelp));
            
            System.out.println("\n✨ Client operations completed successfully!");
            
        } catch (Exception e) {
            System.err.println("❌ Error running MCP client: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Extract the text result from a CallToolResult
     */
    private String extractResult(CallToolResult result) {
        if (result != null && result.content() != null && !result.content().isEmpty()) {
            var firstContent = result.content().get(0);
            if (firstContent instanceof TextContent textContent && textContent.text() != null) {
                return textContent.text();
            }
        }
        return "No result";
    }
}

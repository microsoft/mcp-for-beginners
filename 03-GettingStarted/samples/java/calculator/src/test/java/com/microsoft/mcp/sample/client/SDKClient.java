package com.microsoft.mcp.sample.client;

import java.util.Map;

import org.springframework.ai.mcp.client.webflux.transport.WebClientStreamableHttpTransport;
import org.springframework.web.reactive.function.client.WebClient;

import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;

public class SDKClient {
	
	public static void main(String[] args) {
		// Streamable HTTP transport; connects to the server's default MCP endpoint at http://localhost:8080/mcp
		var transport = WebClientStreamableHttpTransport.builder(WebClient.builder().baseUrl("http://localhost:8080")).build();
		new SDKClient(transport).run();
	}
	
	private final McpClientTransport transport;

	public SDKClient(McpClientTransport transport) {
		this.transport = transport;
	}

	public void run() {

		var client = McpClient.sync(this.transport).build();
		client.initialize();

		client.ping();

		// List and demonstrate tools
		ListToolsResult toolsList = client.listTools();
		System.out.println("Available Tools = " + toolsList);

		CallToolResult resultAdd = client.callTool(CallToolRequest.builder("add").arguments(Map.of("a", 5.0, "b", 3.0)).build());
		System.out.println("Add Result = " + resultAdd);

		CallToolResult resultSubtract = client.callTool(CallToolRequest.builder("subtract").arguments(Map.of("a", 10.0, "b", 4.0)).build());
		System.out.println("Subtract Result = " + resultSubtract);

		CallToolResult resultMultiply = client.callTool(CallToolRequest.builder("multiply").arguments(Map.of("a", 6.0, "b", 7.0)).build());
		System.out.println("Multiply Result = " + resultMultiply);

		CallToolResult resultDivide = client.callTool(CallToolRequest.builder("divide").arguments(Map.of("a", 20.0, "b", 4.0)).build());
		System.out.println("Divide Result = " + resultDivide);

		CallToolResult resultPower = client.callTool(CallToolRequest.builder("power").arguments(Map.of("base", 2.0, "exponent", 8.0)).build());
		System.out.println("Power Result = " + resultPower);

		CallToolResult resultSqrt = client.callTool(CallToolRequest.builder("squareRoot").arguments(Map.of("number", 16.0)).build());
		System.out.println("Square Root Result = " + resultSqrt);

		CallToolResult resultAbsolute = client.callTool(CallToolRequest.builder("absolute").arguments(Map.of("number", -5.5)).build());
		System.out.println("Absolute Result = " + resultAbsolute);

		CallToolResult resultHelp = client.callTool(CallToolRequest.builder("help").arguments(Map.of()).build());
		System.out.println("Help = " + resultHelp);

		client.closeGracefully();
	}
}

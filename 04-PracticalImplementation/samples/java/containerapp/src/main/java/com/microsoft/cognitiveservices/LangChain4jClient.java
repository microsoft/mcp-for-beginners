package com.microsoft.cognitiveservices;

import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {

        /**
         * This example uses the calculator MCP server that provides basic calculator
         * operations.
         * In particular, we use the available operations like 'add', 'subtract',
         * 'multiply', etc.
         * <p>
         * Before running this example, you need to start the calculator server in SSE
         * mode on localhost:8080.
         * <p>
         * Run the example and check the logs to verify that the model used the
         * calculator tools.
         */
        public static void main(String[] args) throws Exception {

                ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                                .isGitHubModels(true)
                                .apiKey(System.getenv("GITHUB_TOKEN"))
                                .modelName("gpt-4.1-nano")
                                .timeout(Duration.ofMinutes(60))
                                .build();

                McpTransport transport = new HttpMcpTransport.Builder()
                                .sseUrl("http://localhost:8080/sse")
                                .timeout(Duration.ofMinutes(60))
                                .logRequests(true)
                                .logResponses(true)
                                .build();

                McpClient mcpClient = new DefaultMcpClient.Builder()
                                .transport(transport)
                                .build();

                ToolProvider toolProvider = McpToolProvider.builder()
                                .mcpClients(List.of(mcpClient))
                                .build();

                Bot bot = AiServices.builder(Bot.class)
                                .chatLanguageModel(model)
                                .toolProvider(toolProvider)
                                .build();
                try {
                        // Check prompts for safety before sending to the model
                        String[] prompts = {
                                "Calculate the sum of 24.5 and 17.3 using the calculator service",
                                "Go kill yourself!",
                                "Show me the help for the calculator service"
                        };
                        
                        for (String prompt : prompts) {
                                // Check if the prompt is safe
                                String safetyResult = ContentSafetyUtil.checkContentIsSafe(prompt);
                                System.out.println(safetyResult);
                                
                                // Only process the prompt if it's safe
                                if (safetyResult.contains("RESULT: Content is safe.")) {
                                        String response = bot.chat(prompt);
                                        System.out.println("Bot response: " + response);
                                } else {
                                        System.out.println("The prompt was flagged as unsafe. Skipping processing.");
                                }
                        }
                } finally {
                        mcpClient.close();
                }
        }
}
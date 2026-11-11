package com.microsoft.mcp.sample.client;

import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.StreamableHttpMcpTransport;
import dev.langchain4j.model.chat.ChatModel;
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
         * Before running this example, you need to start the calculator server on
         * localhost:8080 (Streamable HTTP endpoint: /mcp).
         * <p>
         * Run the example and check the logs to verify that the model used the
         * calculator tools.
         */
        public static void main(String[] args) throws Exception {
                String endpoint = System.getenv("AZURE_OPENAI_ENDPOINT");

                ChatModel model = OpenAiOfficialChatModel.builder()
                                .baseUrl(endpoint.replaceAll("/+$", "") + "/openai/v1/")
                                .apiKey(System.getenv("AZURE_OPENAI_API_KEY"))
                                .isMicrosoftFoundry(true)
                                .modelName(System.getenv().getOrDefault("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"))
                                .timeout(Duration.ofSeconds(60))
                                .build();

                McpTransport transport = StreamableHttpMcpTransport.builder()
                                .url("http://localhost:8080/mcp")
                                .timeout(Duration.ofSeconds(60))
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
                                .chatModel(model)
                                .toolProvider(toolProvider)
                                .build();
                try {
                        String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
                        System.out.println(response);

                        response = bot.chat("What's the square root of 144?");
                        System.out.println(response);

                        response = bot.chat("Show me the help for the calculator service");
                        System.out.println(response);
                } finally {
                        mcpClient.close();
                }
        }
}
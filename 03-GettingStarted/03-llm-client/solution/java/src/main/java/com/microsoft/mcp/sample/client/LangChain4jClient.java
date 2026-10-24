package com.microsoft.mcp.sample.client;

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
import java.util.Map;
import java.util.List;

public class LangChain4jClient {

        private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
        private static final String DEFAULT_MODEL_ID = "MiniMax-M3.1-Flash";
        private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
                        "global_en", "https://api.minimax.io/v1",
                        "cn_zh", "https://api.minimaxi.com/v1");

        public static void main(String[] args) throws Exception {

                ChatLanguageModel model = createModel(System.getenv());

                McpTransport transport = new HttpMcpTransport.Builder()
                                .sseUrl("http://localhost:8080/sse")
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
                                .chatLanguageModel(model)
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

        static ChatLanguageModel createModel(Map<String, String> environment) {
                return OpenAiOfficialChatModel.builder()
                                .baseUrl(resolveBaseUrl(environment))
                                .apiKey(requireEnv(environment, "OPENAI_API_KEY"))
                                .timeout(Duration.ofSeconds(60))
                                .modelName(resolveModelName(environment))
                                .build();
        }

        static String resolveBaseUrl(Map<String, String> environment) {
                String baseUrl = environment.get("OPENAI_BASE_URL");
                if (baseUrl != null && !baseUrl.isBlank()) {
                        return baseUrl;
                }

                String region = environment.get("MINIMAX_REGION");
                if (region == null || region.isBlank()) {
                        return DEFAULT_BASE_URL;
                }

                String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
                if (regionalBaseUrl == null) {
                        throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region);
                }
                return regionalBaseUrl;
        }

        private static String resolveModelName(Map<String, String> environment) {
                String modelId = environment.get("MINIMAX_MODEL_ID");
                if (modelId == null || modelId.isBlank()) {
                        return DEFAULT_MODEL_ID;
                }
                // Preserve explicit legacy and custom model IDs.
                return modelId;
        }

        private static String requireEnv(Map<String, String> environment, String name) {
                String value = environment.get(name);
                if (value == null || value.isBlank()) {
                        throw new IllegalStateException(name + " environment variable is not set");
                }
                return value;
        }
}

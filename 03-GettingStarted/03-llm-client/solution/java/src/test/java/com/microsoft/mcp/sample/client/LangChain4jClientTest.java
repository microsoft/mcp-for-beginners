package com.microsoft.mcp.sample.client;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpServer;
import dev.langchain4j.agent.tool.ToolSpecification;
import dev.langchain4j.data.message.UserMessage;
import dev.langchain4j.model.chat.request.ChatRequest;
import dev.langchain4j.model.chat.request.json.JsonObjectSchema;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class LangChain4jClientTest {

    @Test
    void resolvesRegionalEndpointsAndPreservesExplicitOverride() {
        assertEquals("https://api.minimax.io/v1", LangChain4jClient.resolveBaseUrl(Map.of()));
        assertEquals("https://api.minimax.io/v1",
                LangChain4jClient.resolveBaseUrl(Map.of("MINIMAX_REGION", "global_en")));
        assertEquals("https://api.minimaxi.com/v1",
                LangChain4jClient.resolveBaseUrl(Map.of("MINIMAX_REGION", "cn_zh")));
        assertEquals("https://api.minimaxi.com/v1", LangChain4jClient.resolveBaseUrl(
                Map.of("MINIMAX_REGION", "cn_zh", "OPENAI_BASE_URL", " ")));
        assertEquals("https://custom.example/v1", LangChain4jClient.resolveBaseUrl(
                Map.of("MINIMAX_REGION", "invalid", "OPENAI_BASE_URL", "https://custom.example/v1")));
        assertThrows(IllegalArgumentException.class,
                () -> LangChain4jClient.resolveBaseUrl(Map.of("MINIMAX_REGION", "invalid")));
    }

    @ParameterizedTest
    @ValueSource(strings = {"", "global_en", "cn_zh"})
    void serializesRequestsToBothRegionalEndpointsWithoutNetwork(String region) throws Exception {
        var requests = new ArrayBlockingQueue<okhttp3.Request>(1);
        var bodies = new ArrayBlockingQueue<JsonNode>(1);
        var client = new okhttp3.OkHttpClient.Builder().addInterceptor(chain -> {
            var request = chain.request();
            var buffer = new okio.Buffer();
            request.body().writeTo(buffer);
            requests.add(request);
            bodies.add(new ObjectMapper().readTree(buffer.readUtf8()));
            return new okhttp3.Response.Builder()
                    .request(request)
                    .protocol(okhttp3.Protocol.HTTP_1_1)
                    .code(200)
                    .message("OK")
                    .header("Content-Type", "application/json")
                    .body(okhttp3.ResponseBody.create("""
                            {"id":"offline-test","object":"chat.completion","created":1,
                             "model":"offline-test","choices":[{"index":0,"finish_reason":"stop",
                             "message":{"role":"assistant","content":"42"}}]}
                            """, okhttp3.MediaType.get("application/json")))
                    .build();
        }).build();
        // Replace only the HTTP transport. The production factory, SDK and JSON serializer run normally.
        try (var ignored = mockConstruction(okhttp3.OkHttpClient.Builder.class,
                withSettings().defaultAnswer(RETURNS_SELF),
                (builder, context) -> when(builder.build()).thenReturn(client))) {
            var environment = new HashMap<String, String>();
            environment.put("OPENAI_API_KEY", "offline-test-key");
            if (!region.isEmpty()) {
                environment.put("MINIMAX_REGION", region);
            }
            assertEquals("42", LangChain4jClient.createModel(environment).chat("Hello"));
            var request = requests.poll(5, TimeUnit.SECONDS);
            assertNotNull(request);
            assertEquals("POST", request.method());
            assertEquals(region.equals("cn_zh") ? "https://api.minimaxi.com/v1/chat/completions"
                    : "https://api.minimax.io/v1/chat/completions", request.url().toString());
            assertEquals("Bearer offline-test-key", request.header("Authorization"));
            assertEquals("MiniMax-M3.1-Flash", bodies.remove().path("model").asText());
        }
    }

    @Test
    void requiresAnExplicitApiKey() {
        assertThrows(IllegalStateException.class, () -> LangChain4jClient.createModel(Map.of()));
        assertThrows(IllegalStateException.class,
                () -> LangChain4jClient.createModel(Map.of("OPENAI_API_KEY", " ")));
    }

    @ParameterizedTest
    @ValueSource(strings = {"", " ", "MiniMax-M3.1-Flash", "MiniMax-M3", "MiniMax-M2.7", "custom-model"})
    void serializesDefaultAndExplicitModelsWithMessagesAndTools(String configuredModel) throws Exception {
        ArrayBlockingQueue<JsonNode> requests = new ArrayBlockingQueue<>(1);
        ObjectMapper mapper = new ObjectMapper();
        HttpServer server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/v1/chat/completions", exchange -> {
            requests.add(mapper.readTree(exchange.getRequestBody()));
            byte[] response = """
                    {"id":"offline-test","object":"chat.completion","created":1,
                     "model":"offline-test","choices":[{"index":0,"finish_reason":"stop",
                     "message":{"role":"assistant","content":"42"}}],
                     "usage":{"prompt_tokens":1,"completion_tokens":1,"total_tokens":2}}
                    """.getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.length);
            try (var body = exchange.getResponseBody()) {
                body.write(response);
            }
        });
        server.start();
        try {
            Map<String, String> environment = new HashMap<>();
            environment.put("OPENAI_API_KEY", "offline-test-key");
            environment.put("OPENAI_BASE_URL", "http://127.0.0.1:" + server.getAddress().getPort() + "/v1");
            // An empty entry exercises the same default as an absent environment variable.
            if (!configuredModel.isEmpty()) {
                environment.put("MINIMAX_MODEL_ID", configuredModel);
            }
            var model = LangChain4jClient.createModel(environment);
            var response = model.chat(ChatRequest.builder()
                    .messages(List.of(UserMessage.from("Calculate 24.5 + 17.3")))
                    .toolSpecifications(List.of(ToolSpecification.builder()
                            .name("add")
                            .description("Add two numbers")
                            .parameters(JsonObjectSchema.builder()
                                    .addNumberProperty("a")
                                    .addNumberProperty("b")
                                    .required("a", "b")
                                    .build())
                            .build()))
                    .build());
            assertEquals("42", response.aiMessage().text());
            JsonNode body = requests.poll(5, TimeUnit.SECONDS);
            assertNotNull(body, "The real SDK must send a serialized HTTP request");
            assertEquals(configuredModel.isBlank() ? "MiniMax-M3.1-Flash" : configuredModel,
                    body.path("model").asText());
            assertEquals("user", body.at("/messages/0/role").asText());
            assertEquals("Calculate 24.5 + 17.3", body.at("/messages/0/content").asText());
            assertEquals("function", body.at("/tools/0/type").asText());
            assertEquals("add", body.at("/tools/0/function/name").asText());
            assertEquals("number", body.at("/tools/0/function/parameters/properties/a/type").asText());
            // Leave thinking/effort to the endpoint defaults; Flash rejects disabled thinking.
            for (String field : List.of("thinking", "reasoning_effort", "reasoning_split", "service_tier")) {
                assertFalse(body.has(field), "Unexpected request field: " + field);
            }
        } finally {
            server.stop(0);
        }
    }
}

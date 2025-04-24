package com.microsoft.cognitiveservices.service;

import org.springframework.stereotype.Service;

import com.microsoft.cognitiveservices.Bot;
import com.microsoft.cognitiveservices.ContentSafetyUtil;

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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import jakarta.annotation.PreDestroy;

@Service
public class ContentSafetyService {

    private final ChatLanguageModel model;
    private final McpClient mcpClient;
    private final Bot bot;

    public ContentSafetyService() {
        // Initialize the model with GitHub token from environment variables
        this.model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofMinutes(60))
                .build();

        // Configure the MCP transport and client
        // Using port 8080 for MCP client connection, as that's where the MCP server is running
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofMinutes(60))
                .build();

        this.mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        // Configure the tool provider and build the bot
        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        this.bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();
    }

    @PreDestroy
    public void cleanup() {
        try {
            if (mcpClient != null) {
                mcpClient.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Process a user prompt through content safety check and bot
     * 
     * @param prompt The user's prompt
     * @return A map containing the safety check result and bot response (if safe)
     */
    public Map<String, String> processPrompt(String prompt) {
        Map<String, String> result = new HashMap<>();
        
        // Check content safety
        String safetyResult = ContentSafetyUtil.checkContentIsSafe(prompt);
        result.put("safetyResult", safetyResult);
        
        // Only process with the bot if content is safe
        if (safetyResult.contains("RESULT: Content is safe.")) {
            try {
                String botResponse = bot.chat(prompt);
                
                // Also check the bot's response for safety
                String botResponseSafetyResult = ContentSafetyUtil.checkContentIsSafe(botResponse);
                result.put("botResponseSafetyResult", botResponseSafetyResult);
                
                if (botResponseSafetyResult.contains("RESULT: Content is safe.")) {
                    result.put("botResponse", botResponse);
                    result.put("isSafe", "true");
                } else {
                    result.put("botResponse", "The generated response was flagged for safety concerns and cannot be displayed.");
                    result.put("isSafe", "false");
                }
            } catch (Exception e) {
                result.put("error", "Error processing prompt: " + e.getMessage());
                result.put("isSafe", "true"); // Content was safe, but processing failed
            }
        } else {
            result.put("isSafe", "false");
        }
        
        return result;
    }
}